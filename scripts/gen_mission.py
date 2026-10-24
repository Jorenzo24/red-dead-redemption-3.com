#!/usr/bin/env python3
"""
Mission page generator (data -> EN + FR HTML), sister of gen_fiche.py.

One page per story mission:
  EN  /missions/<slug>/       -> missions/<slug>/index.html
  FR  /fr/missions/<slug>/    -> fr/missions/<slug>/index.html
slug = the EN mission name, slugified (same slug in every language).

Data lives in scripts/missions/<module>.py (one module per mission, a MISSION
dict); scripts/build_missions.py builds them all. The dict shape is documented
in DATA-SCHEMA.md, section "Mission" (future Astro content collection).

Presentation reuses the existing classes only (no CSS of its own): article
column (.article, .article-header, .article-hero), .story-meta chips, fiche fact
grid (.profile__facts), fiche accordions (.accordion, tobacco "read-dark"
blocks), .data-table, .quotes and .story-nav. Header, footer, byline, block
rendering and inline-link tokens come from gen_fiche.

Tokens in any prose string:
  [[<character-slug>|Text]]  -> character fiche, linked only if the fiche is live
  [[m:<mission-slug>|Text]]  -> mission page, linked only if that page exists
"""
import json, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_fiche as gf
from gen_fiche import ROOT, CSS_V, JS_V

SITE = "https://red-dead-redemption-3.com"

# Chapter / act registry: key -> (en guide slug, fr guide slug, EN label, FR label,
# EN short, FR short, game). Keys match CH in _enrich.py.
CHAPTERS = {
    1: ("rdr2-chapter-1-colter", "rdr2-chapitre-1-colter", "Chapter 1: Colter", "Chapitre 1 : Colter", "Chapter 1", "Chapitre 1", "rdr2"),
    2: ("rdr2-chapter-2-horseshoe-overlook", "rdr2-chapitre-2-horseshoe-overlook", "Chapter 2: Horseshoe Overlook", "Chapitre 2 : Horseshoe Overlook", "Chapter 2", "Chapitre 2", "rdr2"),
    3: ("rdr2-chapter-3-clemens-point", "rdr2-chapitre-3-clemens-point", "Chapter 3: Clemens Point", "Chapitre 3 : Clemens Point", "Chapter 3", "Chapitre 3", "rdr2"),
    4: ("rdr2-chapter-4-saint-denis", "rdr2-chapitre-4-saint-denis", "Chapter 4: Saint Denis", "Chapitre 4 : Saint-Denis", "Chapter 4", "Chapitre 4", "rdr2"),
    5: ("rdr2-chapter-5-guarma", "rdr2-chapitre-5-guarma", "Chapter 5: Guarma", "Chapitre 5 : Guarma", "Chapter 5", "Chapitre 5", "rdr2"),
    6: ("rdr2-chapter-6-beaver-hollow", "rdr2-chapitre-6-beaver-hollow", "Chapter 6: Beaver Hollow", "Chapitre 6 : Beaver Hollow", "Chapter 6", "Chapitre 6", "rdr2"),
    "E1": ("rdr2-epilogue-part-1-pronghorn-ranch", "rdr2-epilogue-partie-1-pronghorn-ranch", "Epilogue Part 1: Pronghorn Ranch", "Épilogue, partie 1 : Pronghorn Ranch", "Epilogue Part 1", "Épilogue, partie 1", "rdr2"),
    "E2": ("rdr2-epilogue-part-2-beechers-hope", "rdr2-epilogue-partie-2-beechers-hope", "Epilogue Part 2: Beecher's Hope", "Épilogue, partie 2 : Beecher's Hope", "Epilogue Part 2", "Épilogue, partie 2", "rdr2"),
    "A1": ("rdr1-act-1-new-austin", "rdr1-acte-1-new-austin", "Act I: New Austin", "Acte I : New Austin", "Act I", "Acte I", "rdr1"),
    "A2": ("rdr1-act-2-nuevo-paraiso", "rdr1-acte-2-nuevo-paraiso", "Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso", "Act II", "Acte II", "rdr1"),
    "A3": ("rdr1-act-3-west-elizabeth", "rdr1-acte-3-west-elizabeth", "Act III: West Elizabeth", "Acte III : West Elizabeth", "Act III", "Acte III", "rdr1"),
}
GAMES = {"rdr2": ("Red Dead Redemption 2", "RDR2"), "rdr1": ("Red Dead Redemption", "RDR1")}

SECTION_TITLES = {
    "story":   ("Story", "Déroulé"),
    "choices": ("Choices and variants", "Choix et variantes"),
    "gold":    ("Gold Medal objectives", "Objectifs de la médaille d'or"),
    "quotes":  ("Quotes", "Citations"),
    "trivia":  ("Trivia", "Anecdotes"),
}
SECTION_ORDER = ["story", "choices", "gold", "quotes", "trivia"]


def slugify(name):
    """EN mission name -> URL slug ("Who the Hell is Leviticus Cornwall?" ->
    "who-the-hell-is-leviticus-cornwall"). ASCII only, apostrophes dropped."""
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = s.lower().replace("'", "").replace("’", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def _du(short_fr):
    """'Chapitre 1' -> 'du chapitre 1'; 'Acte I' -> "de l'acte I"; 'Épilogue, partie 1' -> "de l'épilogue, partie 1"."""
    low = short_fr[0].lower() + short_fr[1:]
    return ("de l'" + low) if low[0] in "aeéiouy" else ("du " + low)


def urls(slug):
    return f"/missions/{slug}/", f"/fr/missions/{slug}/"


def _L(d, lang):
    return d[lang] if isinstance(d, dict) else d


# ------------------------------------------------------------------ blocks
def _blocks(blocks, lang, depth, slug):
    """Render accordion body blocks. Everything gen_fiche knows (p, h3, h4, ul,
    quotes, video) is delegated to gen_fiche._accordion; "table" is rendered
    here because mission tables carry a caption (attribution)."""
    out = []
    for b in blocks:
        if "table" in b:
            t = b["table"]
            cell = (lambda x: gf._links(_L(x, lang), lang))
            out.append('                            <div class="table-wrap">')
            out.append('                            <table class="data-table">')
            if t.get("caption"):
                out.append(f'                                <caption>{cell(t["caption"])}</caption>')
            out.append('                                <thead><tr>' + "".join(f'<th scope="col">{cell(h)}</th>' for h in t["head"]) + '</tr></thead>')
            out.append('                                <tbody>')
            for row in t["rows"]:
                out.append('                                    <tr>' + "".join(f'<td>{cell(x)}</td>' for x in row) + '</tr>')
            out.append('                                </tbody>')
            out.append('                            </table>')
            out.append('                            </div>')
        else:
            html = gf._accordion({"summary": {"en": "", "fr": ""}, "blocks": [b]}, lang, depth, slug)
            out += html.split("\n")[3:-2]  # drop the <details>/<summary>/<div> wrapper
    return out


def _section(key, blocks, lang, depth, slug, is_open):
    title = SECTION_TITLES[key][0 if lang == "en" else 1]
    out = [f'                    <details class="accordion"{" open" if is_open else ""}>',
           f'                        <summary>{title}</summary>',
           '                        <div class="accordion__body">']
    out += _blocks(blocks, lang, depth, slug)
    out += ['                        </div>', '                    </details>']
    return "\n".join(out)


def _section_blocks(m, key, lang):
    """Turn the data of one section into blocks; [] = section not rendered."""
    s = m.get("sections", {}).get(key)
    if not s:
        return []
    if key == "gold":
        # {"objectives": [two..], "caption": two, "after": [blocks]}
        objs = s.get("objectives") or []
        if not objs:
            return []
        rows = [[str(i + 1), o] for i, o in enumerate(objs)]
        cap = s.get("caption") or {
            "en": "Gold Medal objectives as listed on the Red Dead Wiki mission page.",
            "fr": "Objectifs de la médaille d'or tels que les liste la page de la mission sur le Red Dead Wiki."}
        return [{"table": {"caption": cap, "head": [{"en": "#", "fr": "#"}, {"en": "Objective", "fr": "Objectif"}],
                           "rows": rows}}] + list(s.get("after", []))
    if key == "quotes":
        # [{"q": "VO line", "src": two, "fr": "French translation"}]
        items = []
        for q in s:
            src_fr = q["src"]["fr"]
            if q.get("fr"):
                src_fr = f'{src_fr}. Traduction : "{q["fr"]}"'
            items.append({"q": {"en": q["q"], "fr": q["q"]}, "src": {"en": q["src"]["en"], "fr": src_fr}})
        return [{"quotes": items}]
    if key == "trivia" and s and "ul" not in s[0] and "p" not in s[0] and "h3" not in s[0]:
        return [{"ul": s}]  # plain list of two() bullets
    return s


# ------------------------------------------------------------------ page
def _page(m, lang):
    depth = 2 if lang == "en" else 3
    up = "../" * depth
    L = (lambda d: _L(d, lang))
    en = lang == "en"
    slug, name = m["slug"], m["name"]
    ch = CHAPTERS[m["chapter"]]
    ch_en, ch_fr, chl_en, chl_fr, chs_en, chs_fr, game = ch
    game_name, game_abbr = GAMES[game]
    ch_href = f"/story/{ch_en}/" if en else f"/fr/histoire/{ch_fr}/"
    ch_label = chl_en if en else chl_fr
    ch_short = chs_en if en else chs_fr
    enpath, frpath = urls(slug)
    enurl, frurl = SITE + enpath, SITE + frpath
    canon = enurl if en else frurl
    htmllang, locale = ("en", "en_US") if en else ("fr", "fr_FR")

    page_title = (f"{name}: {game_abbr} Mission Walkthrough and Story" if en
                  else f"{name} : mission de {game_abbr}, déroulé et histoire")
    eyebrow = f"Mission &middot; {game_name} &middot; {ch_short}"
    hero = m.get("hero")
    img_og = SITE + "/" + (hero["src"] if hero else "assets/logo-red-dead-redemption-3-1.png")

    menu = gf.header_menu(lang, "story", enpath, frpath)
    logo_href, logo_aria, navlabel = (("/", "Red Dead Redemption 3, Home", "Primary") if en
                                      else ("/fr/", "Red Dead Redemption 3, accueil", "Principale"))

    # chips
    n, tot = m["number"], m.get("chapter_total")
    pos = (f"Mission <strong>{n} of {tot}</strong>" if en else f"Mission <strong>{n} sur {tot}</strong>") if tot \
        else (f"Mission <strong>{n}</strong>")
    chips = [game_name, ch_label, pos] + [L(c) for c in m.get("chips", [])]
    chips_html = "\n".join(f'                    <span class="chip">{c}</span>' for c in chips)

    # facts grid
    def mlink(ref):
        if not ref:
            return None
        return gf._links(f'[[m:{ref["slug"]}|{ref["name"]}]]', lang)
    none_prev = ("None (first mission of the game)" if en else "Aucune (première mission du jeu)") \
        if m.get("story_order") == 1 else ("None" if en else "Aucune")
    order_txt = (f"{n} of {tot} in {ch_short}" if en else f"{n} sur {tot} {_du(ch_short)}") if tot else str(n)
    if m.get("story_order"):
        order_txt += (f"; story mission no. {m['story_order']} of the game" if en
                      else f" ; mission principale n° {m['story_order']} du jeu")
    f = m.get("facts", {})
    rows = [
        (("Game", "Jeu"), game_name),
        (("Chapter", "Chapitre"), f'<a href="{ch_href}">{ch_label}</a>'),
        (("Mission", "Mission"), order_txt),
        (("Started by", "Donnée par"), f.get("giver")),
        (("Location", "Lieu"), f.get("location")),
        (("Characters", "Personnages"), f.get("characters")),
        (("Unlocks", "Débloque"), f.get("unlocks")),
        (("Rewards", "Récompenses"), f.get("rewards")),
        (("Previous mission", "Mission précédente"), mlink(m.get("prev")) or none_prev),
        (("Next mission", "Mission suivante"), mlink(m.get("next")) or ("None" if en else "Aucune")),
    ]
    facts_html = "\n".join(
        f'                <div><dt>{lbl[0] if en else lbl[1]}</dt><dd>{gf._links(L(v), lang)}</dd></div>'
        for lbl, v in rows if v)

    intro = "\n".join(f'                <p>{gf._links(L(p), lang)}</p>' for p in m["intro"])

    secs = [(k, _section_blocks(m, k, lang)) for k in SECTION_ORDER]
    secs = [(k, b) for k, b in secs if b]  # never render an empty section
    accordions = "\n".join(_section(k, b, lang, depth, slug, i == 0) for i, (k, b) in enumerate(secs))

    hero_html = ""
    if hero:
        hero_html = (f'            <figure class="article-hero">\n'
                     f'                <img src="{up}{hero["src"]}" alt="{L(hero["alt"])}" fetchpriority="high">\n'
                     f'                <figcaption>{gf._links(L(hero["cap"]), lang)}</figcaption>\n'
                     f'            </figure>\n')

    # bottom nav: previous / all missions of the chapter / next
    def navitem(ref, small, cls):
        c = f' class="{cls}"' if cls else ""
        if gf.mission_live(ref["slug"]):
            href = urls(ref["slug"])[0 if en else 1]
            return f'                <a{c} href="{href}"><small>{small}</small>{ref["name"]}</a>\n'
        return f'                <span{c}><small>{small}</small>{ref["name"]}</span>\n'
    nav = ""
    if m.get("prev"):
        nav += navitem(m["prev"], "Previous mission" if en else "Mission précédente", "")
    all_lbl = (f"All missions of {ch_short}" if en else f"Toutes les missions {_du(ch_short)}")
    nav += f'                <a href="{ch_href}"><small>{ch_label}</small>{all_lbl}</a>\n'
    if m.get("next"):
        nav += navitem(m["next"], "Next mission" if en else "Mission suivante", "story-nav__next")

    bdate = m.get("updated") or m["publishDate"]
    byline = gf.byline_html(lang, bdate)
    footer = gf.footer_html(lang)

    # breadcrumb
    home_lbl, home_href = ("Home", "/") if en else ("Accueil", "/fr/")
    story_lbl, story_href = ("Story", "/story/") if en else ("Histoire", "/fr/histoire/")
    breadcrumb = (
        '        <nav class="breadcrumb" aria-label="Breadcrumb">\n'
        '            <ol>\n'
        f'                <li><a href="{home_href}">{home_lbl}</a></li>\n'
        f'                <li><span class="breadcrumb__sep">&rsaquo;</span><a href="{story_href}">{story_lbl}</a></li>\n'
        f'                <li><span class="breadcrumb__sep">&rsaquo;</span><a href="{ch_href}">{ch_label}</a></li>\n'
        f'                <li><span class="breadcrumb__sep">&rsaquo;</span><span aria-current="page">{name}</span></li>\n'
        '            </ol>\n'
        '        </nav>\n')

    def jsonld(obj):
        j = json.dumps(obj, ensure_ascii=False, indent=4)
        return '    <script type="application/ld+json">\n' + "\n".join("    " + l for l in j.splitlines()) + '\n    </script>\n'
    games_about = [{"@type": "VideoGame", "name": GAMES[g][0],
                    "publisher": {"@type": "Organization", "name": "Rockstar Games"}}
                   for g in ([game] + [x for x in m.get("also_games", []) if x != game])]
    article = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": page_title,
        "description": L(m["meta_desc"]),
        "image": img_og,
        "about": games_about[0] if len(games_about) == 1 else games_about,
        "author": {"@type": "Person", "name": "Joseph Lambert", "url": SITE + "/about/joseph-lambert/"},
        "publisher": {"@type": "Organization", "name": "Red Dead Redemption 3", "url": SITE + "/"},
        "datePublished": m["publishDate"], "dateModified": bdate,
        "mainEntityOfPage": canon, "inLanguage": htmllang,
    }
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": home_lbl, "item": SITE + home_href},
        {"@type": "ListItem", "position": 2, "name": story_lbl, "item": SITE + story_href},
        {"@type": "ListItem", "position": 3, "name": ch_label, "item": SITE + ch_href},
        {"@type": "ListItem", "position": 4, "name": name, "item": canon}]}

    # front-matter (DATA-SCHEMA.md §1): extractible metadata before any tag
    fm = "\n".join([
        "<!--", "---", "type: mission", f"slug: {slug}", f"lang: {htmllang}",
        f"title: {json.dumps(name, ensure_ascii=False)}",
        f"game: {game}", f"chapter: {json.dumps(m['chapter'])}", f"number: {n}",
        f"publishedAt: {m['publishDate']}", f"updatedAt: {bdate}", "author: joseph",
        "hreflang:", f'  - {{ lang: en, href: "{enpath}" }}', f'  - {{ lang: fr, href: "{frpath}" }}',
        f"data: scripts/missions/{m.get('_module', slug.replace('-', '_'))}.py", "---", "-->"])

    og_desc = L(m.get("og_desc") or m["meta_desc"])
    return f"""<!DOCTYPE html>
{fm}
<html lang="{htmllang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <meta name="description" content="{L(m['meta_desc'])}">
    <link rel="canonical" href="{canon}">

    <link rel="alternate" hreflang="en" href="{enurl}">
    <link rel="alternate" hreflang="fr" href="{frurl}">
    <link rel="alternate" hreflang="x-default" href="{enurl}">

    <meta property="og:type" content="article">
    <meta property="og:locale" content="{locale}">
    <meta property="og:url" content="{canon}">
    <meta property="og:site_name" content="Red Dead Redemption 3">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="{og_desc}">
    <meta property="og:image" content="{img_og}">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{page_title}">
    <meta name="twitter:description" content="{og_desc}">
    <meta name="twitter:image" content="{img_og}">

    <link rel="icon" type="image/png" href="{up}assets/favicon-red-dead-redemption-3.png">
    <link rel="preload" href="{up}assets/fonts/chinese-rock.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="{up}css/style.css?v={CSS_V}">

{jsonld(article)}{jsonld(bc)}</head>
<body class="theme-light{' read-dark' if m.get('reading_dark', True) else ''}">
    <header class="site-header">
        <div class="site-header__inner">
            <a href="{logo_href}" class="site-header__logo" aria-label="{logo_aria}">
                <img src="{up}assets/logo-red-dead-redemption-3-1.png" alt="Red Dead Redemption 3">
            </a>
            <nav class="site-header__nav" aria-label="{navlabel}">
{menu}
            </nav>
        </div>
    </header>

    <main>
{breadcrumb}        <article class="article mission">
            <header class="article-header">
                <p class="article-eyebrow">{eyebrow}</p>
                <h1 class="article-title">{name}</h1>
                <div class="story-meta">
{chips_html}
                </div>
                <p class="profile__byline">{byline}</p>
            </header>
{hero_html}
            <div class="profile__intro">
{intro}
            </div>

            <dl class="profile__facts">
{facts_html}
            </dl>

            <div class="accordions">
{accordions}
            </div>

            <nav class="story-nav" aria-label="{'Missions' if en else 'Missions'}">
{nav}            </nav>
        </article>
    </main>

    <footer class="site-footer">
{footer}
    </footer>

    <script src="{up}js/main.js?v={JS_V}"></script>
</body>
</html>
"""


# ------------------------------------------------------------------ sitemaps
def _sitemap_add(path, loc, enurl, frurl, lastmod):
    """Insert (or refresh lastmod of) one <url> entry, idempotent."""
    p = os.path.join(ROOT, path)
    s = open(p, encoding="utf-8").read()
    if f"<loc>{loc}</loc>" in s:
        s2 = re.sub(rf"(<loc>{re.escape(loc)}</loc>\s*<lastmod>)[^<]*(</lastmod>)", rf"\g<1>{lastmod}\g<2>", s)
        if s2 != s:
            open(p, "w", encoding="utf-8").write(s2)
        return False
    entry = (f"    <url>\n"
             f"        <loc>{loc}</loc>\n"
             f"        <lastmod>{lastmod}</lastmod>\n"
             f"        <changefreq>monthly</changefreq>\n"
             f"        <priority>0.6</priority>\n"
             f'        <xhtml:link rel="alternate" hreflang="en" href="{enurl}"/>\n'
             f'        <xhtml:link rel="alternate" hreflang="fr" href="{frurl}"/>\n'
             f'        <xhtml:link rel="alternate" hreflang="x-default" href="{enurl}"/>\n'
             f"    </url>\n")
    s = s.replace("</urlset>", entry + "</urlset>")
    open(p, "w", encoding="utf-8").write(s)
    return True


def build(m):
    """Write missions/<slug>/index.html + fr/missions/<slug>/index.html and add
    both URLs to the per-language sitemaps. Returns the two file paths."""
    if slugify(m["name"]) != m["slug"]:
        raise SystemExit(f"ERROR: slug {m['slug']!r} != slugify(name) {slugify(m['name'])!r}")
    from characters_registry import CHARACTERS as REG
    for s, nm, ren, rfr, _g in REG:
        gf.reg(s, nm, ren, rfr)
    paths = []
    gf.LINK_LIVE_ONLY = True  # character tokens to fiches not live yet -> plain text
    try:
        for lang, rel in (("en", f"missions/{m['slug']}/index.html"),
                          ("fr", f"fr/missions/{m['slug']}/index.html")):
            p = os.path.join(ROOT, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write(gf._annotate_dims(_page(m, lang), m["slug"]))
            paths.append(rel)
    finally:
        gf.LINK_LIVE_ONLY = False
    enpath, frpath = urls(m["slug"])
    lastmod = m.get("updated") or m["publishDate"]
    _sitemap_add("sitemap-en.xml", SITE + enpath, SITE + enpath, SITE + frpath, lastmod)
    _sitemap_add("sitemap-fr.xml", SITE + frpath, SITE + enpath, SITE + frpath, lastmod)
    return paths
