#!/usr/bin/env python3
"""
Drip-publisher for red-dead-redemption-3.com.

Picks the next DUE character fiche from _queue/ (publishDate <= today, UTC),
moves it live, regenerates the listing pages + homepage counts + sitemaps with a
fresh lastmod, and removes it from the queue. Designed to be run once a day by
.github/workflows/daily-publish.yml (the workflow commits + deploys the result).

Queue layout (one folder per item). Three kinds, keyed by meta.json "type"
(absent = "character", so older queue entries keep working):

  type "character":
    _queue/NN-<slug>/
        meta.json   -> {"slug","name","role_en","role_fr","publishDate":"YYYY-MM-DD"}
        en.html     -> final EN page (paths already ../../ as if at /characters/<slug>/)
        fr.html     -> final FR page (paths already ../../../ as if at /fr/personnages/<slug>/)
    (character images must already live in assets/characters/<slug>/)

  type "story" (a story-guide chapter):
    _queue/NN-<slug_en>/
        meta.json   -> {"type":"story","slug_en","slug_fr","title_en","title_fr",
                        "timeline_thumb","nav_label_en","nav_label_fr",
                        "prev_en":{"slug","label"}, "prev_fr":{"slug","label"},
                        "publishDate":"YYYY-MM-DD"}
        en.html     -> final EN page (paths already ../../ as if at /story/<slug_en>/)
        fr.html     -> final FR page (paths already ../../../ as if at /fr/histoire/<slug_fr>/)
    Publishing a chapter also flips its "Soon" placeholder in the two story index
    timelines to a live entry, and repoints the previous chapter's "next" nav.
    (chapter images must already live in assets/story/<slug_en>/)

  type "article" (a news article, EN + FR mirror):
    _queue/NN-<slug_en>/
        meta.json     -> {"type":"article","slug_en","slug_fr","asset_dir",
                          "publishDate":"YYYY-MM-DD"}
        en.html       -> final EN page (paths already ../../ as if at /articles/<slug_en>/)
        fr.html       -> final FR page (paths already ../../../ as if at /fr/articles/<slug_fr>/)
        card_en.html  -> the EN <article class="acard"> card, image src ABSOLUTE (/assets/...)
        card_fr.html  -> the FR card, same
    Publishing puts the card first on both article indexes and both homepage
    "Latest news" grids (which keep 3 cards: the oldest one drops off).
    The byline/dates inside the pages must already equal publishDate.
    (article images must already live in assets/articles/<asset_dir>/)

Exit codes: 0 = published one OR nothing due (no error); 1 = a real error.
Prints "PUBLISHED <slug>" on success, "NOTHING_DUE" when idle (the workflow keys
its commit on a real git diff, so an idle run is a harmless no-op).
"""
import json, os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(ROOT, "_queue")
TODAY = datetime.datetime.now(datetime.timezone.utc).date()
LASTMOD = TODAY.isoformat()

def die(msg):
    print("ERROR:", msg, file=sys.stderr)
    sys.exit(1)


def live_path(meta):
    """Where this queue item lands once published (used to skip already-live items)."""
    if meta.get("type") == "story":
        return os.path.join(ROOT, "story", meta["slug_en"], "index.html")
    if meta.get("type") == "article":
        return os.path.join(ROOT, "articles", meta["slug_en"], "index.html")
    return os.path.join(ROOT, "characters", meta["slug"], "index.html")


def pick_due():
    if not os.path.isdir(QUEUE):
        return None
    due = []
    for name in sorted(os.listdir(QUEUE)):
        d = os.path.join(QUEUE, name)
        mp = os.path.join(d, "meta.json")
        if not os.path.isfile(mp):
            continue
        meta = json.load(open(mp, encoding="utf-8"))
        try:
            pd = datetime.date.fromisoformat(meta["publishDate"])
        except Exception:
            die(f"bad publishDate in {mp}")
        if pd <= TODAY and not os.path.exists(live_path(meta)):
            due.append((pd, name, d, meta))
    if not due:
        return None
    due.sort(key=lambda t: (t[0], t[1]))  # earliest date, then folder order
    return due[0]


def add_to_sitemap(relpath, loc, en, fr, priority):
    p = os.path.join(ROOT, relpath)
    s = open(p, encoding="utf-8").read()
    if f"<loc>{loc}</loc>" in s:
        return
    entry = (
        "    <url>\n"
        f"        <loc>{loc}</loc>\n"
        f"        <lastmod>{LASTMOD}</lastmod>\n"
        "        <changefreq>monthly</changefreq>\n"
        f"        <priority>{priority}</priority>\n"
        f'        <xhtml:link rel="alternate" hreflang="en" href="{en}"/>\n'
        f'        <xhtml:link rel="alternate" hreflang="fr" href="{fr}"/>\n'
        f'        <xhtml:link rel="alternate" hreflang="x-default" href="{en}"/>\n'
        "    </url>\n"
    )
    open(p, "w", encoding="utf-8").write(s.replace("</urlset>", entry + "</urlset>"))


def copy_live(src, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    with open(src, encoding="utf-8") as f:
        open(os.path.join(dest_dir, "index.html"), "w", encoding="utf-8").write(f.read())


def timeline_go_live(relpath, thumb, href, title, soon, folder):
    """New content for a story index with this chapter's 'Soon' placeholder made live.

    Returns None if it is already live. Pure: computes, never writes, so that a
    publish can validate every edit before touching the disk.
    """
    p = os.path.join(ROOT, relpath)
    s = open(p, encoding="utf-8").read()
    if f'href="{href}"' in s:
        return None  # already live, idempotent

    # Isolate the <li> block that carries this chapter's thumbnail.
    needle = f"/assets/story/locations/{thumb}.jpeg"
    if needle not in s:
        die(f"timeline thumb {needle} not found in {relpath}")
    li_start = s.rindex('<li class="timeline__item is-upcoming">', 0, s.index(needle))
    li_end = s.index("</li>", li_start) + len("</li>")
    block = s[li_start:li_end]

    new = block.replace('<li class="timeline__item is-upcoming">', '<li class="timeline__item">', 1)
    # title: drop the "Soon" badge, link the chapter
    new, n_title = re.subn(
        r'<h3 class="timeline__title">\s*' + re.escape(title) +
        r'\s*<span class="storyrow__soon">' + re.escape(soon) + r'</span>\s*</h3>',
        f'<h3 class="timeline__title"><a href="{href}">{title}</a></h3>', new, count=1)
    # thumbnail: inert <span> becomes a real link, image markup untouched
    new, n_thumb = re.subn(
        r'<span class="storyrow__thumb">(.*?)</span>',
        f'<a class="storyrow__thumb" href="{href}" tabindex="-1" aria-hidden="true">'
        r'\1</a>', new, count=1, flags=re.S)

    if n_title != 1:
        die(f"'Soon' title for {thumb} not in expected shape in {relpath} (title {title!r}?)")
    if n_thumb != 1:
        die(f"thumb span for {thumb} not in expected shape in {relpath}")
    if "storyrow__soon" in new or "is-upcoming" in new:
        die(f"leftover placeholder markup on the {thumb} entry in {relpath}")
    return s[:li_start] + new + s[li_end:]


def repoint_prev_nav(prev_page, index_href, next_href, small, label, folder):
    """New content for the previous chapter, its 'next' link aimed at this chapter.

    Returns None if already repointed. Pure: computes, never writes.
    """
    p = os.path.join(ROOT, prev_page)
    if not os.path.isfile(p):
        die(f"previous chapter page not found: {prev_page} (from {folder})")
    s = open(p, encoding="utf-8").read()
    if f'class="story-nav__next" href="{next_href}"' in s:
        return None  # already repointed, idempotent
    old = f'<a class="story-nav__next" href="{index_href}">'
    if old not in s:
        die(f"'next' nav not in expected shape in {prev_page}")
    start = s.index(old)
    end = s.index("</a>", start) + len("</a>")
    new = f'<a class="story-nav__next" href="{next_href}"><small>{small}</small>{label}</a>'
    return s[:start] + new + s[end:]


def publish_story(d, meta, folder):
    for key in ("slug_en", "slug_fr", "title_en", "title_fr", "timeline_thumb",
                "nav_label_en", "nav_label_fr", "prev_en", "prev_fr"):
        if not meta.get(key):
            die(f"meta.json missing '{key}' in {folder}")
    slug_en, slug_fr = meta["slug_en"], meta["slug_fr"]

    en_src, fr_src = os.path.join(d, "en.html"), os.path.join(d, "fr.html")
    if not (os.path.isfile(en_src) and os.path.isfile(fr_src)):
        die(f"en.html/fr.html missing in {folder}")
    hero = os.path.join(ROOT, "assets", "story", slug_en, "hero.jpeg")
    if not os.path.isfile(hero):
        die(f"hero.jpeg missing for {slug_en} (assets must be in place)")

    # Compute EVERY edit before writing anything. A chapter that goes live without
    # its timeline entry and nav would be orphaned, and pick_due() would then skip
    # it forever as "already live", so a partial publish must not be possible.
    edits = {}  # relpath -> new content
    for relpath, href, title, soon in (
        ("story/index.html", f"/story/{slug_en}/", meta["title_en"], "Soon"),
        ("fr/histoire/index.html", f"/fr/histoire/{slug_fr}/", meta["title_fr"], "Bientôt"),
    ):
        out = timeline_go_live(relpath, meta["timeline_thumb"], href, title, soon, folder)
        if out is not None:
            edits[relpath] = out

    for prev_page, index_href, next_href, small, label in (
        (f"story/{meta['prev_en']['slug']}/index.html", "/story/",
         f"/story/{slug_en}/", "Next", meta["nav_label_en"]),
        (f"fr/histoire/{meta['prev_fr']['slug']}/index.html", "/fr/histoire/",
         f"/fr/histoire/{slug_fr}/", "Suivant", meta["nav_label_fr"]),
    ):
        out = repoint_prev_nav(prev_page, index_href, next_href, small, label, folder)
        if out is not None:
            edits[prev_page] = out

    # Everything validated: now write.
    copy_live(en_src, os.path.join(ROOT, "story", slug_en))
    copy_live(fr_src, os.path.join(ROOT, "fr", "histoire", slug_fr))
    for relpath, content in edits.items():
        open(os.path.join(ROOT, relpath), "w", encoding="utf-8").write(content)

    D = "https://red-dead-redemption-3.com"
    en_url, fr_url = f"{D}/story/{slug_en}/", f"{D}/fr/histoire/{slug_fr}/"
    add_to_sitemap("sitemap-en.xml", en_url, en_url, fr_url, "0.7")
    add_to_sitemap("sitemap-fr.xml", fr_url, en_url, fr_url, "0.6")
    return slug_en


CARD_OPEN = '<article class="acard">'
HOME_NEWS_MAX = 3


def card_first(relpath, card, href, home=False):
    """New content for a listing with `card` inserted as its first article card.

    On a homepage, only the "Latest news" grid is touched and it is trimmed back
    to HOME_NEWS_MAX cards. Returns None if the card is already there. Pure.
    """
    p = os.path.join(ROOT, relpath)
    s = open(p, encoding="utf-8").read()
    if f'href="{href}"' in s:
        return None  # already listed, idempotent
    start = 0
    if home:
        if 'aria-labelledby="news-title"' not in s:
            die(f"news section not found in {relpath}")
        start = s.index('aria-labelledby="news-title"')
    if CARD_OPEN not in s[start:]:
        die(f"no article card to insert before in {relpath}")
    i = s.index(CARD_OPEN, start)
    s = s[:i] + card.strip() + "\n                    " + s[i:]
    if home:
        g0 = s.rindex('<div class="card-grid">', 0, i)
        g1 = s.index("</section>", g0)
        grid = s[g0:g1]
        cards = list(re.finditer(r'\s*<article class="acard">.*?</article>', grid, re.S))
        if len(cards) < 1 or len(cards) > HOME_NEWS_MAX + 1:
            die(f"unexpected number of news cards ({len(cards)}) in {relpath}")
        for m in reversed(cards[HOME_NEWS_MAX:]):
            grid = grid[:m.start()] + grid[m.end():]
        s = s[:g0] + grid + s[g1:]
    return s


def publish_article(d, meta, folder):
    for key in ("slug_en", "slug_fr", "asset_dir"):
        if not meta.get(key):
            die(f"meta.json missing '{key}' in {folder}")
    slug_en, slug_fr = meta["slug_en"], meta["slug_fr"]
    src = {k: os.path.join(d, k) for k in ("en.html", "fr.html", "card_en.html", "card_fr.html")}
    for k, path in src.items():
        if not os.path.isfile(path):
            die(f"{k} missing in {folder}")
    if not os.path.isfile(os.path.join(ROOT, "assets", "articles", meta["asset_dir"], "hero.jpeg")):
        die(f"hero.jpeg missing in assets/articles/{meta['asset_dir']} (assets must be in place)")
    pd = meta["publishDate"]
    for k in ("en.html", "fr.html"):
        page = open(src[k], encoding="utf-8").read()
        if f'datePublished": "{pd}"' not in page:
            die(f"{k} datePublished does not match publishDate {pd} in {folder}")
    card_en = open(src["card_en.html"], encoding="utf-8").read()
    card_fr = open(src["card_fr.html"], encoding="utf-8").read()
    for name, card in (("card_en.html", card_en), ("card_fr.html", card_fr)):
        if not card.strip().startswith(CARD_OPEN) or 'src="/assets/' not in card:
            die(f"{name} must be one acard with an absolute /assets/ image in {folder}")

    href_en, href_fr = f"/articles/{slug_en}/", f"/fr/articles/{slug_fr}/"
    # Compute every edit before writing anything (same rule as stories).
    edits = {}
    for relpath, card, href, home in (
        ("articles/index.html", card_en, href_en, False),
        ("fr/articles/index.html", card_fr, href_fr, False),
        ("index.html", card_en, href_en, True),
        ("fr/index.html", card_fr, href_fr, True),
    ):
        out = card_first(relpath, card, href, home)
        if out is not None:
            edits[relpath] = out

    copy_live(src["en.html"], os.path.join(ROOT, "articles", slug_en))
    copy_live(src["fr.html"], os.path.join(ROOT, "fr", "articles", slug_fr))
    for relpath, content in edits.items():
        open(os.path.join(ROOT, relpath), "w", encoding="utf-8").write(content)

    D = "https://red-dead-redemption-3.com"
    en_url, fr_url = D + href_en, D + href_fr
    add_to_sitemap("sitemap-en.xml", en_url, en_url, fr_url, "0.7")
    add_to_sitemap("sitemap-fr.xml", fr_url, en_url, fr_url, "0.6")
    return slug_en


def main():
    nxt = pick_due()
    if not nxt:
        print("NOTHING_DUE")
        return
    _, folder, d, meta = nxt

    if meta.get("type") in ("story", "article"):
        publish = publish_story if meta["type"] == "story" else publish_article
        published = publish(d, meta, folder)
        import shutil
        shutil.rmtree(d)
        print(f"PUBLISHED {published}")
        return

    slug = meta["slug"]
    for key in ("slug", "name", "role_en", "role_fr"):
        if not meta.get(key):
            die(f"meta.json missing '{key}' in {folder}")

    en_src, fr_src = os.path.join(d, "en.html"), os.path.join(d, "fr.html")
    if not (os.path.isfile(en_src) and os.path.isfile(fr_src)):
        die(f"en.html/fr.html missing in {folder}")
    if not os.path.isfile(os.path.join(ROOT, "assets", "characters", slug, "portrait.jpeg")):
        die(f"portrait.jpeg missing for {slug} (assets must be in place)")

    # 1. move pages live
    en_dir = os.path.join(ROOT, "characters", slug)
    fr_dir = os.path.join(ROOT, "fr", "personnages", slug)
    os.makedirs(en_dir, exist_ok=True)
    os.makedirs(fr_dir, exist_ok=True)
    with open(en_src, encoding="utf-8") as f:
        open(os.path.join(en_dir, "index.html"), "w", encoding="utf-8").write(f.read())
    with open(fr_src, encoding="utf-8") as f:
        open(os.path.join(fr_dir, "index.html"), "w", encoding="utf-8").write(f.read())

    # 2. regenerate the grouped listing pages + the homepage faction counts
    #    (the homepage cards themselves are hand-picked and never touched here)
    import gen_listing
    gen_listing.regenerate()

    # 3. sitemaps
    D = "https://red-dead-redemption-3.com"
    add_to_sitemap("sitemap-en.xml", f"{D}/characters/{slug}/",
                   f"{D}/characters/{slug}/", f"{D}/fr/personnages/{slug}/", "0.7")
    add_to_sitemap("sitemap-fr.xml", f"{D}/fr/personnages/{slug}/",
                   f"{D}/characters/{slug}/", f"{D}/fr/personnages/{slug}/", "0.6")

    # 4. drop from queue
    import shutil
    shutil.rmtree(d)

    print(f"PUBLISHED {slug}")


if __name__ == "__main__":
    main()
