#!/usr/bin/env python3
"""
Character fiche generator (data -> EN + FR HTML on the stabilised gabarit).

Keeps content (data) separate from presentation, which both removes copy-paste
and matches the Astro-ready goal in CLAUDE.md §4. A driver script defines a list
of character dicts and calls build_to_queue() for each.

Inline links use tokens [[slug|Display text]] inside any prose string; the
generator expands them to the correct per-language URL (/characters/<slug>/ in
EN, /fr/personnages/<slug>/ in FR). Relationship names link the same way and are
styled red via CSS when a slug is given.

See CHAR SCHEMA at the bottom for the expected dict shape.
"""
import json, os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_V = "20260622t"

# Registry used to build "More characters" ccards (role per language).
REGISTRY = {
    "arthur-morgan":       ("Arthur Morgan",       "Van der Linde gang &middot; RDR2",   "Gang Van der Linde &middot; RDR2"),
    "john-marston":        ("John Marston",         "Van der Linde gang &middot; RDR1",   "Gang Van der Linde &middot; RDR1"),
    "dutch-van-der-linde": ("Dutch van der Linde",  "Gang leader &middot; RDR1 &amp; 2",  "Chef de gang &middot; RDR1 &amp; 2"),
    "micah-bell":          ("Micah Bell",           "Main antagonist &middot; RDR2",      "Antagoniste principal &middot; RDR2"),
    "sadie-adler":         ("Sadie Adler",          "Bounty hunter &middot; RDR2",        "Chasseuse de primes &middot; RDR2"),
    "hosea-matthews":      ("Hosea Matthews",       "Gang co-founder &middot; RDR2",      "Cofondateur du gang &middot; RDR2"),
    "bill-williamson":     ("Bill Williamson",      "Outlaw &middot; RDR1 &amp; 2",       "Hors-la-loi &middot; RDR1 &amp; 2"),
    "charles-smith":       ("Charles Smith",        "Tracker &middot; RDR2",              "Pisteur &middot; RDR2"),
}


def reg(slug, name, role_en, role_fr):
    REGISTRY[slug] = (name, role_en, role_fr)


_TOKEN = re.compile(r"\[\[([a-z0-9-]+)\|([^\]]+)\]\]")


def _links(text, lang):
    base = "/characters/" if lang == "en" else "/fr/personnages/"
    return _TOKEN.sub(lambda m: f'<a href="{base}{m.group(1)}/">{m.group(2)}</a>', text)


def _ccard(slug, lang, depth):
    name, role_en, role_fr = REGISTRY[slug]
    role = role_en if lang == "en" else role_fr
    img = ("../" * depth) + f"assets/characters/{slug}/portrait.jpeg"
    base = "/characters/" if lang == "en" else "/fr/personnages/"
    if lang == "en":
        tag, cta, aria = "Character", "View profile &rarr;", f"{name} character profile"
    else:
        tag, cta, aria = "Personnage", "Voir le profil &rarr;", f"Fiche du personnage {name}"
    return (
        f'                        <a class="ccard" href="{base}{slug}/" aria-label="{aria}">\n'
        f'                            <img src="{img}" alt="{name}" loading="lazy">\n'
        f'                            <span class="ccard__overlay">\n'
        f'                                <span class="ccard__tag">{tag}</span>\n'
        f'                                <span class="ccard__name">{name}</span>\n'
        f'                                <span class="ccard__role">{role}</span>\n'
        f'                                <span class="ccard__cta">{cta}</span>\n'
        f'                            </span>\n'
        f'                        </a>\n'
    )


def _accordion(sec, lang, depth, slug):
    L = (lambda d: d[lang])
    open_attr = " open" if sec.get("open") else ""
    out = [f'                    <details class="accordion"{open_attr}>',
           f'                        <summary>{L(sec["summary"])}</summary>',
           '                        <div class="accordion__body">']
    for b in sec["blocks"]:
        if "h3" in b:
            out.append(f'                            <h3>{L(b["h3"])}</h3>')
        elif "p" in b:
            out.append(f'                            <p>{_links(L(b["p"]), lang)}</p>')
        elif "ul" in b:
            out.append('                            <ul>')
            for li in b["ul"]:
                out.append(f'                                <li>{_links(L(li), lang)}</li>')
            out.append('                            </ul>')
        elif "figure" in b:
            fg = b["figure"]
            img = ("../" * depth) + f'assets/characters/{slug}/{fg["img"]}'
            out.append('                            <figure class="media-figure">')
            out.append(f'                                <img src="{img}" alt="{L(fg["alt"])}" loading="lazy">')
            out.append(f'                                <figcaption>{L(fg["cap"])}</figcaption>')
            out.append('                            </figure>')
    out += ['                        </div>', '                    </details>']
    return "\n".join(out)


def _relationships(rels, lang, depth, slug):
    L = (lambda d: d[lang])
    base = "/characters/" if lang == "en" else "/fr/personnages/"
    out = ['                    <details class="accordion">',
           f'                        <summary>{"Relationships" if lang=="en" else "Relations"}</summary>',
           '                        <div class="accordion__body">']
    for r in rels:
        img = ("../" * depth) + f'assets/characters/{slug}/rel/{r["img"]}'
        op = r.get("pos", "center")
        style = f' style="object-position:{op}"' if op else ''
        if r.get("slug"):
            head = f'<h3><a href="{base}{r["slug"]}/">{r["name"]}</a></h3>'
        else:
            head = f'<h3>{r["name"]}</h3>'
        out += ['                            <div class="rel">',
                f'                                <img class="rel__img" src="{img}" alt="{r["name"]}" loading="lazy"{style}>',
                '                                <div class="rel__body">',
                f'                                    {head}',
                f'                                    <p>{_links(L(r["text"]), lang)}</p>',
                '                                </div>',
                '                            </div>']
    out += ['                        </div>', '                    </details>']
    return "\n".join(out)


def _gallery(gal, lang, depth, slug):
    L = (lambda d: d[lang])
    out = ['                    <details class="accordion">',
           f'                        <summary>{"Gallery" if lang=="en" else "Galerie"}</summary>',
           '                        <div class="accordion__body">',
           '                            <div class="accordion__gallery">']
    for g in gal:
        img = ("../" * depth) + f'assets/characters/{slug}/{g["img"]}'
        out += ['                                <figure>',
                f'                                    <img src="{img}" alt="{L(g["alt"])}" loading="lazy">',
                f'                                    <figcaption>{L(g["cap"])}</figcaption>',
                '                                </figure>']
    out += ['                            </div>', '                        </div>', '                    </details>']
    return "\n".join(out)


def _page(c, lang):
    """depth: EN fiche = 2 (../../), FR fiche = 3 (../../../)."""
    depth = 2 if lang == "en" else 3
    up = "../" * depth
    L = (lambda d: d[lang])
    slug = c["slug"]; name = c["name"]
    enurl = f"https://red-dead-redemption-3.com/characters/{slug}/"
    frurl = f"https://red-dead-redemption-3.com/fr/personnages/{slug}/"
    canon = enurl if lang == "en" else frurl
    htmllang = "en" if lang == "en" else "fr"
    locale = "en_US" if lang == "en" else "fr_FR"
    img_og = f"https://red-dead-redemption-3.com/assets/characters/{slug}/portrait.jpeg"

    # header menu (Characters active)
    if lang == "en":
        logo_href, logo_aria, navlabel = "/", "Red Dead Redemption 3, Home", "Primary"
        menu = (f'                <div class="site-header__menu">\n'
                f'                    <a href="/characters/" class="site-header__link is-active" aria-current="page">Characters</a>\n'
                f'                    <a href="/articles/" class="site-header__link">Articles</a>\n'
                f'                    <a href="/timeline/" class="site-header__link">Timeline</a>\n'
                f'                </div>\n'
                f'                <div class="lang-switch"><span class="site-header__lang is-active" aria-current="true">EN</span><a href="{frurl.replace("https://red-dead-redemption-3.com","")}" class="site-header__lang" hreflang="fr" aria-label="Lire en français">FR</a></div>')
    else:
        logo_href, logo_aria, navlabel = "/fr/", "Red Dead Redemption 3, accueil", "Principale"
        menu = (f'                <div class="site-header__menu">\n'
                f'                    <a href="/fr/personnages/" class="site-header__link is-active" aria-current="page">Personnages</a>\n'
                f'                    <a href="/fr/articles/" class="site-header__link">Articles</a>\n'
                f'                    <a href="/fr/chronologie/" class="site-header__link">Chronologie</a>\n'
                f'                </div>\n'
                f'                <div class="lang-switch"><a href="{enurl.replace("https://red-dead-redemption-3.com","")}" class="site-header__lang" hreflang="en" aria-label="Read in English">EN</a><span class="site-header__lang is-active" aria-current="true">FR</span></div>')

    chips = "\n".join(f'                    <span class="chip">{L(ch)}</span>' for ch in c["chips"])
    facts = "\n".join(
        f'                    <div><dt>{L(f["label"])}</dt><dd>{_links(L(f["value"]), lang)}</dd></div>'
        for f in c["facts"])
    intro = "\n".join(f'                    <p>{_links(L(p), lang)}</p>' for p in c["intro"])

    # accordions: bio + extra sections, relationships, gallery (relationships placed
    # at the position requested by data via c["rel_after"], default after section idx 1)
    acc = []
    for i, sec in enumerate(c["sections"]):
        acc.append(_accordion(sec, lang, depth, slug))
        if i == c.get("rel_after", 1):
            acc.append(_relationships(c["relationships"], lang, depth, slug))
    acc.append(_gallery(c["gallery"], lang, depth, slug))
    accordions = "\n".join(acc)

    related = "".join(_ccard(s, lang, depth) for s in c["related"])
    rel_title = "More characters" if lang == "en" else "Plus de personnages"
    rel_all_href = "/characters/" if lang == "en" else "/fr/personnages/"
    rel_all = "All characters &rarr;" if lang == "en" else "Tous les personnages &rarr;"
    rel_label = "More characters" if lang == "en" else "Plus de personnages"

    author_url = "/about/joseph-lambert/" if lang == "en" else "/fr/a-propos/joseph-lambert/"
    byline = (f'By <a href="{author_url}"><span>Joseph Lambert</span></a> &middot; Updated <time datetime="2026-06-23">June 23, 2026</time>'
              if lang == "en" else
              f'Par <a href="{author_url}"><span>Joseph Lambert</span></a> &middot; Mis à jour le <time datetime="2026-06-23">23 juin 2026</time>')
    if lang == "en":
        fnav = ('        <nav class="site-footer__nav" aria-label="Footer">\n'
                '            <a href="/about/">About</a>\n'
                '            <a href="/about/joseph-lambert/">Author</a>\n'
                '            <a href="/characters/">Characters</a>\n'
                '            <a href="/timeline/">Timeline</a>\n'
                '            <a href="/articles/">Articles</a>\n'
                '            <a href="/contact/">Contact</a>\n'
                '        </nav>\n')
        footer = (fnav +
                  '        <p>&copy; <span id="year">2026</span> red-dead-redemption-3.com &middot; All rights reserved.</p>\n'
                  '        <p>This is a fan site. Not affiliated with, endorsed, or sponsored by Rockstar Games or Take-Two Interactive.</p>')
    else:
        fnav = ('        <nav class="site-footer__nav" aria-label="Pied de page">\n'
                '            <a href="/fr/a-propos/">À propos</a>\n'
                '            <a href="/fr/a-propos/joseph-lambert/">Auteur</a>\n'
                '            <a href="/fr/personnages/">Personnages</a>\n'
                '            <a href="/fr/chronologie/">Chronologie</a>\n'
                '            <a href="/fr/articles/">Articles</a>\n'
                '            <a href="/fr/contact/">Contact</a>\n'
                '        </nav>\n')
        footer = (fnav +
                  '        <p>&copy; <span id="year">2026</span> red-dead-redemption-3.com &middot; Tous droits réservés.</p>\n'
                  '        <p>Site de fans. Sans aucune affiliation avec Rockstar Games ou Take-Two Interactive, ni leur approbation.</p>')

    schema = {
        "@context": "https://schema.org", "@type": "Person", "name": name,
        "description": L(c["schema_desc"]),
        "image": img_og, "gender": c.get("gender", "Male"),
        "nationality": c.get("nationality", "American"),
        "subjectOf": {"@type": "VideoGame", "name": c["schema_game"],
                      "publisher": {"@type": "Organization", "name": "Rockstar Games"}},
        "mainEntityOfPage": canon, "inLanguage": htmllang,
    }
    if c.get("birth"): schema["birthDate"] = c["birth"]
    if c.get("death"): schema["deathDate"] = c["death"]
    schema_json = json.dumps(schema, ensure_ascii=False, indent=4)
    schema_json = "\n".join("    " + ln for ln in schema_json.splitlines())

    # breadcrumb (visual + BreadcrumbList JSON-LD)
    home_lbl, home_href = ("Home", "/") if lang == "en" else ("Accueil", "/fr/")
    chars_lbl, chars_href = ("Characters", "/characters/") if lang == "en" else ("Personnages", "/fr/personnages/")
    breadcrumb = (
        '        <nav class="breadcrumb" aria-label="Breadcrumb">\n'
        '            <ol>\n'
        f'                <li><a href="{home_href}">{home_lbl}</a></li>\n'
        f'                <li><span class="breadcrumb__sep">&rsaquo;</span><a href="{chars_href}">{chars_lbl}</a></li>\n'
        f'                <li><span class="breadcrumb__sep">&rsaquo;</span><span aria-current="page">{name}</span></li>\n'
        '            </ol>\n'
        '        </nav>\n')
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": home_lbl, "item": "https://red-dead-redemption-3.com" + home_href},
        {"@type": "ListItem", "position": 2, "name": chars_lbl, "item": "https://red-dead-redemption-3.com" + chars_href},
        {"@type": "ListItem", "position": 3, "name": name, "item": canon}]}
    bcj = json.dumps(bc, ensure_ascii=False, indent=4)
    bc_jsonld = '    <script type="application/ld+json">\n' + "\n".join("    " + l for l in bcj.splitlines()) + '\n    </script>\n'

    return f"""<!DOCTYPE html>
<html lang="{htmllang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | Red Dead Redemption 3</title>
    <meta name="description" content="{L(c['meta_desc'])}">
    <link rel="canonical" href="{canon}">

    <link rel="alternate" hreflang="en" href="{enurl}">
    <link rel="alternate" hreflang="fr" href="{frurl}">
    <link rel="alternate" hreflang="x-default" href="{enurl}">

    <meta property="og:type" content="profile">
    <meta property="og:locale" content="{locale}">
    <meta property="og:url" content="{canon}">
    <meta property="og:site_name" content="Red Dead Redemption 3">
    <meta property="og:title" content="{name}">
    <meta property="og:description" content="{L(c['og_desc'])}">
    <meta property="og:image" content="{img_og}">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{name}">
    <meta name="twitter:description" content="{L(c['og_desc'])}">
    <meta name="twitter:image" content="{img_og}">

    <link rel="icon" type="image/png" href="{up}assets/favicon-red-dead-redemption-3.png">
    <link rel="preload" href="{up}assets/fonts/chinese-rock.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="{up}css/style.css?v={CSS_V}">

    <script type="application/ld+json">
{schema_json}
    </script>
{bc_jsonld}</head>
<body class="theme-light">
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
{breadcrumb}        <article class="profile">
            <div class="profile__cover">
                <img src="{up}assets/characters/{slug}/cover.jpeg" alt="" aria-hidden="true" loading="eager">
            </div>
            <div class="profile__inner">
                <div class="profile__head">
                    <img class="profile__avatar" src="{up}assets/characters/{slug}/portrait.jpeg" alt="{L(c['portrait_alt'])}" fetchpriority="high">
                    <div class="profile__id">
                        <p class="profile__eyebrow">{L(c['eyebrow'])}</p>
                        <h1 class="profile__name">{name}</h1>
                    </div>
                </div>

                <div class="profile__chips">
{chips}
                </div>
                <p class="profile__byline">{byline}</p>

                <div class="profile__intro">
{intro}
                </div>

                <dl class="profile__facts">
{facts}
                </dl>

                <div class="accordions">
{accordions}
                </div>

                <aside class="related" aria-label="{rel_label}">
                    <div class="related__head">
                        <h2 class="related__title">{rel_title}</h2>
                        <a href="{rel_all_href}" class="related__all">{rel_all}</a>
                    </div>
                    <div class="card-grid card-grid--portraits">
{related}                    </div>
                </aside>
            </div>
        </article>
    </main>

    <footer class="site-footer">
{footer}
    </footer>

    <script src="{up}js/main.js?v=20260518a"></script>
</body>
</html>
"""


def _annotate_dims(s, slug):
    """Add width/height (read from the real files) to this slug's <img> tags — anti-CLS."""
    import subprocess
    base = os.path.join(ROOT, "assets", "characters", slug)
    cache = {}
    def dim(fn):
        if fn in cache: return cache[fn]
        try:
            out = subprocess.check_output(["sips", "-g", "pixelWidth", "-g", "pixelHeight",
                                           os.path.join(base, fn)], stderr=subprocess.DEVNULL).decode()
            w = re.search(r"pixelWidth:\s*(\d+)", out); h = re.search(r"pixelHeight:\s*(\d+)", out)
            cache[fn] = (w.group(1), h.group(1)) if (w and h) else None
        except Exception:
            cache[fn] = None
        return cache[fn]
    def repl(m):
        tag = m.group(0)
        if "width=" in tag: return tag
        sm = re.search(r'assets/characters/' + re.escape(slug) + r'/([^"]+)', tag)
        if not sm: return tag
        d = dim(sm.group(1))
        return tag[:-1] + f' width="{d[0]}" height="{d[1]}">' if d else tag
    return re.sub(r'<img\b[^>]*?>', repl, s)


def build_to_queue(c):
    """Write _queue/NN-<slug>/{meta.json,en.html,fr.html}. NN from c['order']."""
    reg(c["slug"], c["name"], c["reg_role_en"], c["reg_role_fr"])
    folder = os.path.join(ROOT, "_queue", f'{c["order"]:02d}-{c["slug"]}')
    os.makedirs(folder, exist_ok=True)
    open(os.path.join(folder, "en.html"), "w", encoding="utf-8").write(_annotate_dims(_page(c, "en"), c["slug"]))
    open(os.path.join(folder, "fr.html"), "w", encoding="utf-8").write(_annotate_dims(_page(c, "fr"), c["slug"]))
    meta = {"slug": c["slug"], "name": c["name"],
            "role_en": c["reg_role_en"], "role_fr": c["reg_role_fr"],
            "publishDate": c["publishDate"]}
    open(os.path.join(folder, "meta.json"), "w", encoding="utf-8").write(
        json.dumps(meta, ensure_ascii=False, indent=2))
    return folder
