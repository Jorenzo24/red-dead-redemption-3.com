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

Presentation reuses the article column (.article, .article-header,
.article-hero), .story-meta chips, fiche accordions (.accordion, tobacco
"read-dark" blocks), .data-table, .quotes and .story-nav, plus two mission-only
components: the ticket-style mission card (.mcard, replaces the fact grid) and
inline story figures (.mfig). Header, footer, byline, block
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
def _figure(fg, lang, depth):
    """{"src": "assets/.../scene-1.jpeg", "alt": two, "cap": two} -> <figure class="mfig">
    with a WebP <source> (when the .webp twin exists) and the JPEG fallback."""
    up = "../" * depth
    src = fg["src"]
    webp = os.path.splitext(src)[0] + ".webp"
    w, h = _img_size(src)
    out = ['                            <figure class="mfig">',
           '                                <picture>']
    if os.path.isfile(os.path.join(ROOT, webp)):
        out.append(f'                                    <source srcset="{up}{webp}" type="image/webp">')
    out.append(f'                                    <img src="{up}{src}" alt="{_L(fg["alt"], lang)}" width="{w}" height="{h}" loading="lazy" decoding="async">')
    out.append('                                </picture>')
    if fg.get("cap"):
        out.append(f'                                <figcaption>{gf._links(_L(fg["cap"], lang), lang)}</figcaption>')
    out.append('                            </figure>')
    return out


def _img_size(rel):
    from PIL import Image
    p = os.path.join(ROOT, rel)
    if not os.path.isfile(p):
        raise SystemExit(f"ERROR: missing image {rel}")
    with Image.open(p) as im:
        return im.size


def _blocks(blocks, lang, depth, slug):
    """Render accordion body blocks. Everything gen_fiche knows (p, h3, h4, ul,
    quotes, video) is delegated to gen_fiche._accordion; "table" and "figure"
    are rendered here (mission tables carry a caption, figures a <picture>)."""
    out = []
    for b in blocks:
        if "figure" in b:
            out += _figure(b["figure"], lang, depth)
        elif "table" in b:
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



# ------------------------------------------------------------------ mission card
# Monoline 24px icons (stroke = currentColor), drawn for the mission card.
_ICON_PATHS = {
    "game": '<path d="M7 8.5h10a4.5 4.5 0 0 1 4.4 5.4l-.7 3.3a2.4 2.4 0 0 1-4.1 1.2L14.4 16H9.6l-2.2 2.4a2.4 2.4 0 0 1-4.1-1.2l-.7-3.3A4.5 4.5 0 0 1 7 8.5z"/><path d="M7.5 11.2v3.2M5.9 12.8h3.2"/><path d="M15.6 12.2h.01M17.8 14h.01" stroke-width="2.4"/>',
    "chapter": '<path d="M12 6.6C10 5 7.2 4.5 3.5 4.9v13.2c3.7-.4 6.5.1 8.5 1.7 2-1.6 4.8-2.1 8.5-1.7V4.9C16.8 4.5 14 5 12 6.6z"/><path d="M12 6.6v13.2"/>',
    "location": '<path d="M12 21s-6.5-6.1-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 14.9 12 21 12 21z"/><circle cx="12" cy="9.8" r="2.4"/>',
    "rewards": '<path d="M8.5 3h3l1.2 5M15.5 3h-3"/><circle cx="12" cy="14.5" r="5.5"/><path d="M12 11.6l.9 1.9 2 .3-1.5 1.4.4 2-1.8-1-1.8 1 .4-2-1.5-1.4 2-.3z"/>',
    "unlocks": '<circle cx="7.5" cy="15.5" r="3.8"/><path d="M10.2 12.8 20 3M16.3 6.7l2.6 2.6M13.8 9.2l2 2"/>',
    "prev": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    "next": '<path d="M5 12h14M13 6l6 6-6 6"/>',
}


def _icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" '
            f'focusable="false">{_ICON_PATHS[name]}</svg>')


def _plain_len(html):
    return len(re.sub(r"\[\[(?:m:)?[^|\]]+\|([^\]]+)\]\]", r"\1", re.sub(r"<[^>]+>", "", html)))


def _avatar(p, lang, up):
    """One round portrait icon. p = {"slug": str|None, "name": str|two, "short": str|two?}.
    Linked to the fiche (and portrait used) only if the fiche is live; otherwise the
    western placeholder avatar, no link."""
    name = _L(p["name"], lang)
    short = _L(p.get("short"), lang) if p.get("short") else name.split()[0]
    slug = p.get("slug")
    live = bool(slug) and gf.character_live(slug)
    if live:
        base = f"assets/characters/{slug}/portrait"
        src = base + ".jpeg"
        if not os.path.isfile(os.path.join(ROOT, src)):
            raise SystemExit(f"ERROR: no portrait for {slug}")
        webp = f'<source srcset="{up}{base}.webp" type="image/webp">' \
            if os.path.isfile(os.path.join(ROOT, base + ".webp")) else ""
        pic = (f'<picture>{webp}<img src="{up}{src}" alt="{name}" width="64" height="64" '
               f'loading="lazy" decoding="async"></picture>')
        href = ("/characters/" if lang == "en" else "/fr/personnages/") + slug + "/"
        return (f'<li><a class="mav" href="{href}"><span class="mav__img">{pic}</span>'
                f'<span class="mav__name" aria-hidden="true">{short}</span></a></li>')
    pic = (f'<img src="{up}assets/characters/placeholder-avatar.svg" alt="{name}" width="64" height="64" '
           f'loading="lazy" decoding="async">')
    return (f'<li><span class="mav mav--none"><span class="mav__img">{pic}</span>'
            f'<span class="mav__name" aria-hidden="true">{short}</span></span></li>')


def _people(lst, lang, up, ind):
    """List of people -> <ul class="mavs">. A legacy two() string (old data) renders as text."""
    if isinstance(lst, dict):
        return f'{ind}<p class="mcard__text">{gf._links(_L(lst, lang), lang)}</p>'
    items = "\n".join(f"{ind}    {_avatar(p, lang, up)}" for p in lst)
    return f'{ind}<ul class="mavs">\n{items}\n{ind}</ul>'


def _mcard(m, lang, up):
    """Ticket-style mission card: tiles (game, chapter, location, rewards, unlocks),
    a dashed tear line, people (started by, characters, at camp) as round portrait
    icons, then previous / next buttons. Pure HTML + CSS (.mcard ...)."""
    en = lang == "en"
    L = (lambda d: _L(d, lang))
    ch_en, ch_fr, chl_en, chl_fr, chs_en, chs_fr, game = CHAPTERS[m["chapter"]]
    game_name = GAMES[game][0]
    ch_href = f"/story/{ch_en}/" if en else f"/fr/histoire/{ch_fr}/"
    ch_label, ch_short = (chl_en, chs_en) if en else (chl_fr, chs_fr)
    n, tot = m["number"], m.get("chapter_total")
    f = m.get("facts", {})
    I = "            "

    def tile(icon, label, value, sub=None):
        if not value:
            return ""
        wide = " mtile--wide" if _plain_len(value) > 34 else ""
        sub_html = f'<span class="mtile__sub">{sub}</span>' if sub else ""
        return (f'{I}        <div class="mtile{wide}">\n'
                f'{I}            <dt>{_icon(icon)}{label}</dt>\n'
                f'{I}            <dd>{gf._links(value, lang)}{sub_html}</dd>\n'
                f'{I}        </div>\n')

    pos = (f"Mission {n} of {tot}" if en else f"Mission {n} sur {tot}") if tot else f"Mission {n}"
    so = m.get("story_order")
    game_sub = ((f"Story mission no. {so}" if en else f"Mission principale n° {so}") if so else None)
    tiles = (tile("game", "Game" if en else "Jeu", game_name, game_sub)
             + tile("chapter", "Chapter" if en else "Chapitre", f'<a href="{ch_href}">{ch_label}</a>', pos)
             + tile("location", "Location" if en else "Lieu", L(f.get("location")) if f.get("location") else None)
             + tile("rewards", "Rewards" if en else "Récompenses", L(f.get("rewards")) if f.get("rewards") else None)
             + tile("unlocks", "Unlocks" if en else "Débloque", L(f.get("unlocks")) if f.get("unlocks") else None))

    # people
    def note(key):
        v = f.get(key)
        return f'\n{I}        <p class="mcard__note">{gf._links(L(v), lang)}</p>' if v else ""
    blocks = []
    if f.get("giver"):
        blocks.append(f'{I}    <div class="mcard__group mcard__group--giver">\n'
                      f'{I}        <p class="mcard__label">{"Started by" if en else "Donnée par"}</p>\n'
                      f'{_people(f["giver"], lang, up, I + "        ")}{note("giver_note")}\n'
                      f'{I}    </div>')
    chars = f.get("characters")
    if chars:
        if isinstance(chars, dict):  # legacy text
            inner = _people(chars, lang, up, I + "        ")
        else:
            main = [p for p in chars if not p.get("camp")]
            camp = [p for p in chars if p.get("camp")]
            inner = _people(main, lang, up, I + "        ")
            if camp:
                inner += (f'\n{I}        <p class="mcard__label mcard__label--sub">{"At camp" if en else "Au camp"}</p>\n'
                          + _people(camp, lang, up, I + "        "))
        blocks.append(f'{I}    <div class="mcard__group mcard__group--cast">\n'
                      f'{I}        <p class="mcard__label">{"Characters" if en else "Personnages"}</p>\n'
                      f'{inner}{note("characters_note")}\n'
                      f'{I}    </div>')
    people = ""
    if blocks:
        people = (f'{I}    <div class="mcard__cut" aria-hidden="true"></div>\n'
                  f'{I}    <div class="mcard__sec mcard__people">\n' + "\n".join("    " + b.replace("\n", "\n    ") for b in blocks) + f'\n{I}    </div>\n')

    # previous / next buttons
    def btn(ref, kind):
        small = (("Previous mission" if en else "Mission précédente") if kind == "prev"
                 else ("Next mission" if en else "Mission suivante"))
        if ref:
            label = ref["name"]
        elif kind == "prev":
            label = ("None, first mission of the game" if en else "Aucune, première mission du jeu") \
                if so == 1 else ("None" if en else "Aucune")
        else:
            label = "None" if en else "Aucune"
        ico = _icon(kind)
        body = f'<span class="mbtn__txt"><small>{small}</small>{label}</span>'
        inner = (ico + body) if kind == "prev" else (body + ico)
        cls = f"mbtn mbtn--{kind}"
        if ref and gf.mission_live(ref["slug"]):
            return f'{I}        <a class="{cls}" href="{urls(ref["slug"])[0 if en else 1]}">{inner}</a>\n'
        return f'{I}        <span class="{cls} is-off">{inner}</span>\n'
    nav = (f'{I}    <div class="mcard__cut" aria-hidden="true"></div>\n'
           f'{I}    <nav class="mcard__sec mcard__nav" aria-label="{"Previous and next mission" if en else "Mission précédente et suivante"}">\n'
           + btn(m.get("prev"), "prev") + btn(m.get("next"), "next") + f'{I}    </nav>\n')

    aria = "Mission card" if en else "Fiche de la mission"
    return (f'{I}<section class="mcard" aria-label="{aria}">\n'
            f'{I}    <dl class="mcard__sec mcard__tiles">\n{tiles}{I}    </dl>\n'
            + people
            + nav + f'{I}</section>')


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

    # mission card (ticket-style facts box, mission pages only)
    mcard_html = _mcard(m, lang, up)

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

{mcard_html}

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
