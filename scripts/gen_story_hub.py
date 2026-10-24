#!/usr/bin/env python3
"""
Story hub generator: /story/ (EN) and /fr/histoire/ (FR), from data.

    python3 scripts/gen_story_hub.py

The hub lists every chapter (RDR2) and act (RDR1) in story order. Each block has:
  - a stable anchor id (e.g. "rdr2-chapter-1", "rdr1-act-3"), the same in both
    languages: the chapter guides will later 301 to /story/#<id>, so NEVER change
    an id once published;
  - a short factual summary (SUMMARIES below: where/when, camp, main arc, mission
    count when a source gives it);
  - an accordion (<details>) listing the chapter's mission pages in story order,
    read from scripts/missions/*.py (only missions whose page is live). A chapter
    with no mission page yet gets no accordion;
  - a link to the chapter guide while its page still exists on disk (when the
    guide is removed and redirected, the link disappears on the next run).

Run again after building mission pages (scripts/build_missions.py calls it).
Inline tokens in summaries: [[<character-slug>|Text]] and [[m:<mission-slug>|Text]],
linked only when the target page is live (gen_fiche._links, LINK_LIVE_ONLY).

Summaries sources (Oct 2026): our chapter guides story/*/ and fr/histoire/*/
(Chapter 1 = the v3 guide), the v3 fiches (Cornwall, Arthur, Micah, Hosea, Dutch,
Bronte, Catherine Braithwaite, Fussar), and the Red Dead Wiki page "Missions in
Redemption 2" (scripts/v3/work/_m/Missions_in_Redemption_2.txt) for the mission
counts of Chapters 2 and 4. RDR1 acts: no verified count, none given.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_fiche as gf
from gen_fiche import ROOT, CSS_V, JS_V
from gen_mission import CHAPTERS, urls as mission_urls

SITE = "https://red-dead-redemption-3.com"
UPDATED = "2026-10-24"

# Story order: (game heading, [(year divider, [chapter keys])]). Keys = gen_mission.CHAPTERS.
LAYOUT = [
    ("Red Dead Redemption 2", [("1899", [1, 2, 3, 4, 5, 6]), ("1907", ["E1", "E2"])]),
    ("Red Dead Redemption", [("1911", ["A1", "A2", "A3"])]),
]

# key -> anchor id, frieze label (en, fr), title (en, fr), location thumbnail
BLOCKS = {
    1:    ("rdr2-chapter-1",  ("Chapter 1", "Chapitre 1"),   ("Colter", "Colter"),                         "colter"),
    2:    ("rdr2-chapter-2",  ("Chapter 2", "Chapitre 2"),   ("Horseshoe Overlook", "Horseshoe Overlook"), "horseshoe"),
    3:    ("rdr2-chapter-3",  ("Chapter 3", "Chapitre 3"),   ("Clemens Point", "Clemens Point"),           "clemens"),
    4:    ("rdr2-chapter-4",  ("Chapter 4", "Chapitre 4"),   ("Saint Denis", "Saint-Denis"),               "saint-denis"),
    5:    ("rdr2-chapter-5",  ("Chapter 5", "Chapitre 5"),   ("Guarma", "Guarma"),                         "guarma"),
    6:    ("rdr2-chapter-6",  ("Chapter 6", "Chapitre 6"),   ("Beaver Hollow", "Beaver Hollow"),           "beaver-hollow"),
    "E1": ("rdr2-epilogue-1", ("Epilogue I", "Épilogue I"),  ("Pronghorn Ranch", "Pronghorn Ranch"),       "pronghorn"),
    "E2": ("rdr2-epilogue-2", ("Epilogue II", "Épilogue II"), ("Beecher's Hope", "Beecher's Hope"),        "beechers-hope"),
    "A1": ("rdr1-act-1",      ("Act I", "Acte I"),           ("New Austin", "New Austin"),                 "new-austin"),
    "A2": ("rdr1-act-2",      ("Act II", "Acte II"),         ("Nuevo Paraíso", "Nuevo Paraíso"),           "nuevo-paraiso"),
    "A3": ("rdr1-act-3",      ("Act III", "Acte III"),       ("West Elizabeth", "West Elizabeth"),         "west-elizabeth"),
}

SUMMARIES = {
    1: {
        "en": "May 1899. After the failed Blackwater ferry robbery, the Van der Linde gang shelters in Colter, an abandoned mining town under snow in the Grizzlies West of Ambarino. The gang takes in the widow [[sadie-adler|Sadie Adler]] after a fight with the O'Driscolls, finds [[john-marston|John Marston]] on a mountain ledge, captures [[kieran-duffy|Kieran Duffy]] and robs the train of [[leviticus-cornwall|Leviticus Cornwall]]. The chapter has six story missions and ends with the move to Horseshoe Overlook.",
        "fr": "Mai 1899. Après l'échec du braquage du ferry de Blackwater, le gang Van der Linde se réfugie à Colter, une ville minière abandonnée et enneigée des Grizzlies West, dans l'Ambarino. Le gang recueille la veuve [[sadie-adler|Sadie Adler]] après un affrontement avec les O'Driscoll, retrouve [[john-marston|John Marston]] sur une corniche, capture [[kieran-duffy|Kieran Duffy]] et dévalise le train de [[leviticus-cornwall|Leviticus Cornwall]]. Le chapitre compte six missions principales et s'achève sur le départ pour Horseshoe Overlook.",
    },
    2: {
        "en": "1899. The gang camps at Horseshoe Overlook, above the Dakota River near Valentine, in the Heartlands of New Hanover. Collecting a debt for [[leopold-strauss|Leopold Strauss]], [[arthur-morgan|Arthur Morgan]] is exposed to tuberculosis by the farmer Thomas Downes. [[sean-macguire|Sean MacGuire]] is rescued, Arthur breaks [[micah-bell|Micah Bell]] out of jail in Strawberry, and the Pinkertons make contact in \"[[m:a-fisher-of-men|A Fisher of Men]]\". A shootout with Cornwall's men in Valentine forces the gang to move. The Red Dead Wiki counts 24 missions, optional ones included.",
        "fr": "1899. Le gang campe à Horseshoe Overlook, au-dessus de la Dakota River, près de Valentine, dans les Heartlands de New Hanover. En recouvrant une dette pour [[leopold-strauss|Leopold Strauss]], [[arthur-morgan|Arthur Morgan]] est exposé à la tuberculose par le fermier Thomas Downes. [[sean-macguire|Sean MacGuire]] est délivré, Arthur fait évader [[micah-bell|Micah Bell]] de la prison de Strawberry, et les Pinkerton prennent contact avec le gang dans \"[[m:a-fisher-of-men|A Fisher of Men]]\". Une fusillade avec les hommes de Cornwall à Valentine oblige le gang à partir. Le Red Dead Wiki recense 24 missions, facultatives comprises.",
    },
    3: {
        "en": "1899. The gang moves south to Clemens Point, on Flat Iron Lake near Rhodes, in Lemoyne. Dutch tries to play two feuding families, the Grays and the Braithwaites, against each other. The Grays ambush the gang in Rhodes and [[sean-macguire|Sean MacGuire]] is killed. The Braithwaites kidnap [[jack-marston|Jack Marston]]; after the gang burns their manor, [[catherine-braithwaite|Catherine Braithwaite]] reveals that her sons gave him to [[angelo-bronte|Angelo Bronte]], in Saint Denis.",
        "fr": "1899. Le gang descend vers le sud et s'installe à Clemens Point, au bord du Flat Iron Lake, près de Rhodes, dans le Lemoyne. Dutch tente de monter l'une contre l'autre deux familles rivales, les Gray et les Braithwaite. Les Gray tendent une embuscade au gang dans Rhodes, et [[sean-macguire|Sean MacGuire]] est tué. Les Braithwaite enlèvent [[jack-marston|Jack Marston]] ; une fois leur manoir incendié par le gang, [[catherine-braithwaite|Catherine Braithwaite]] révèle que ses fils l'ont remis à [[angelo-bronte|Angelo Bronte]], à Saint-Denis.",
    },
    4: {
        "en": "1899. The gang camps at Shady Belle, an abandoned plantation house in the Bayou Nwa outside Saint Denis. [[angelo-bronte|Angelo Bronte]] returns Jack to the gang, then Dutch kills him in \"[[m:revenge-is-a-dish-best-eaten|Revenge is a Dish Best Eaten]]\". The O'Driscolls kill [[kieran-duffy|Kieran Duffy]]. The bank robbery in \"[[m:banking-the-old-american-art|Banking, The Old American Art]]\" is a Pinkerton trap: [[lenny-summers|Lenny Summers]] and [[hosea-matthews|Hosea Matthews]] are killed, John is arrested, and Arthur, Dutch, Micah, Bill and Javier flee by ship and are wrecked at sea. The Red Dead Wiki counts 16 missions, four of them optional.",
        "fr": "1899. Le gang s'installe à Shady Belle, une demeure de plantation abandonnée du Bayou Nwa, aux portes de Saint-Denis. [[angelo-bronte|Angelo Bronte]] rend Jack au gang, puis Dutch le tue dans \"[[m:revenge-is-a-dish-best-eaten|Revenge is a Dish Best Eaten]]\". Les O'Driscoll tuent [[kieran-duffy|Kieran Duffy]]. Le braquage de la banque, dans \"[[m:banking-the-old-american-art|Banking, The Old American Art]]\", est un piège des Pinkerton : [[lenny-summers|Lenny Summers]] et [[hosea-matthews|Hosea Matthews]] sont tués, John est arrêté, et Arthur, Dutch, Micah, Bill et Javier s'enfuient par bateau avant de faire naufrage. Le Red Dead Wiki recense 16 missions, dont quatre facultatives.",
    },
    5: {
        "en": "1899. Arthur, Dutch, Micah, Bill and Javier wash up on Guarma, a Caribbean sugar island ruled by Colonel [[alberto-fussar|Alberto Fussar]]. The five men join the rebels of [[hercule-fontaine|Hercule Fontaine]] in exchange for passage home. Arthur kills Fussar during the attack on Aguasdulces, and the group sails back to America. They rejoin the rest of the gang at Lakay, in the bayou, where the Pinkertons attack the camp in \"[[m:fleeting-joy|Fleeting Joy]]\".",
        "fr": "1899. Arthur, Dutch, Micah, Bill et Javier échouent sur Guarma, une île sucrière des Caraïbes dominée par le colonel [[alberto-fussar|Alberto Fussar]]. Les cinq hommes se rangent aux côtés des rebelles d'[[hercule-fontaine|Hercule Fontaine]] en échange d'un passage vers l'Amérique. Arthur tue Fussar lors de l'attaque d'Aguasdulces, et le groupe reprend la mer. Ils retrouvent le reste du gang à Lakay, dans le bayou, où les Pinkerton attaquent le camp dans \"[[m:fleeting-joy|Fleeting Joy]]\".",
    },
    6: {
        "en": "1899. After the Lakay raid, the gang takes the Beaver Hollow caves, in Roanoke Ridge, New Hanover, from the Murfree Brood. Arthur is diagnosed with tuberculosis and, with Sadie, frees John from Sisika Penitentiary. Dutch kills [[leviticus-cornwall|Leviticus Cornwall]] at Annesburg. Agent [[andrew-milton|Andrew Milton]] reveals that Micah has informed for the Pinkertons since they picked him up on the gang's return from Guarma, and the gang breaks apart. The chapter has 14 story missions and four versions of its final scene, in which Arthur dies.",
        "fr": "1899. Après le raid sur Lakay, le gang chasse la Murfree Brood des grottes de Beaver Hollow, à Roanoke Ridge, dans le New Hanover, et s'y installe. Arthur apprend qu'il a la tuberculose et libère John du pénitencier de Sisika avec Sadie. Dutch abat [[leviticus-cornwall|Leviticus Cornwall]] à Annesburg. L'agent [[andrew-milton|Andrew Milton]] révèle que Micah renseigne les Pinkerton depuis qu'ils l'ont arrêté au retour de Guarma, et le gang se disloque. Le chapitre compte 14 missions principales et quatre versions de sa scène finale, où Arthur meurt.",
    },
    "E1": {
        "en": "1907, eight years after Chapter 6. The player now controls [[john-marston|John Marston]], who works at Pronghorn Ranch, in Big Valley, West Elizabeth, under the name Jim Milton, while Abigail and Jack live near Strawberry. [[sadie-adler|Sadie Adler]] returns and brings him into bounty work. John takes a bank loan from Ansel Atherton to buy the Beecher's Hope ranch, and Uncle joins the family. This part has 11 story missions.",
        "fr": "1907, huit ans après le chapitre 6. Le joueur incarne désormais [[john-marston|John Marston]], employé à Pronghorn Ranch, à Big Valley, dans le West Elizabeth, sous le nom de Jim Milton ; Abigail et Jack vivent près de Strawberry. [[sadie-adler|Sadie Adler]] reparaît et l'entraîne dans la chasse aux primes. John obtient un prêt du banquier Ansel Atherton pour acheter le ranch de Beecher's Hope, et Uncle rejoint la famille. Cette partie compte 11 missions principales.",
    },
    "E2": {
        "en": "1907. John builds the Beecher's Hope ranch house with [[charles-smith|Charles Smith]] and [[uncle|Uncle]], pays down his bank debt through bounty work with Sadie, and proposes to Abigail. In \"[[m:american-venom|American Venom]]\", John, Sadie and Charles track [[micah-bell|Micah Bell]] to Mount Hagen; Dutch shoots Micah first and John kills him. Agents [[edgar-ross|Edgar Ross]] and [[archer-fordham|Archer Fordham]] then watch the ranch, which sets up Red Dead Redemption. This part has 12 story missions, followed by the end credits.",
        "fr": "1907. John bâtit la maison de Beecher's Hope avec [[charles-smith|Charles Smith]] et [[uncle|Uncle]], rembourse la banque grâce aux primes chassées avec Sadie et demande Abigail en mariage. Dans \"[[m:american-venom|American Venom]]\", John, Sadie et Charles retrouvent [[micah-bell|Micah Bell]] au mont Hagen ; Dutch tire le premier sur Micah, et John l'achève. Les agents [[edgar-ross|Edgar Ross]] et [[archer-fordham|Archer Fordham]] surveillent ensuite le ranch, ce qui amène l'histoire du premier Red Dead Redemption. Cette partie compte 12 missions principales, suivies du générique de fin.",
    },
    "A1": {
        "en": "1911. Bureau of Investigation agents [[edgar-ross|Edgar Ross]] and [[archer-fordham|Archer Fordham]] hold Abigail and Jack, and send John after Bill Williamson, Javier Escuella and Dutch van der Linde. John is shot at Fort Mercer, in Rio Bravo, and recovers at the ranch of [[bonnie-macfarlane|Bonnie MacFarlane]]. Helped by [[nigel-west-dickens|Nigel West Dickens]], [[seth-briars|Seth Briars]], [[irish|Irish]] and Marshal [[leigh-johnson|Leigh Johnson]], he takes the fort, but [[bill-williamson|Bill]] has already fled to Mexico.",
        "fr": "1911. Les agents du Bureau of Investigation [[edgar-ross|Edgar Ross]] et [[archer-fordham|Archer Fordham]] retiennent Abigail et Jack, et envoient John traquer Bill Williamson, Javier Escuella et Dutch van der Linde. Blessé devant Fort Mercer, dans le Rio Bravo, John se remet au ranch de [[bonnie-macfarlane|Bonnie MacFarlane]]. Avec l'aide de [[nigel-west-dickens|Nigel West Dickens]], [[seth-briars|Seth Briars]], [[irish|Irish]] et du marshal [[leigh-johnson|Leigh Johnson]], il prend le fort, mais [[bill-williamson|Bill]] a déjà fui au Mexique.",
    },
    "A2": {
        "en": "1911. John crosses the San Luis River into Nuevo Paraíso, a Mexican province at war. He works both for the army of Colonel [[agustin-allende|Agustin Allende]] and Captain [[vincente-de-santa|Vincente de Santa]] and for the rebels of [[abraham-reyes|Abraham Reyes]], until De Santa betrays him in Chuparosa. [[landon-ricketts|Landon Ricketts]], a retired gunslinger, trains him. John kills or captures [[javier-escuella|Javier]] at El Presidio; at Escalera, [[luisa-fortuna|Luisa Fortuna]] is killed, then Allende and Bill are shot on the road by John or by Reyes.",
        "fr": "1911. John franchit la San Luis River et entre dans le Nuevo Paraíso, une province mexicaine en guerre. Il travaille à la fois pour l'armée du colonel [[agustin-allende|Agustin Allende]] et du capitaine [[vincente-de-santa|Vincente de Santa]], et pour les rebelles d'[[abraham-reyes|Abraham Reyes]], jusqu'à ce que De Santa le trahisse à Chuparosa. [[landon-ricketts|Landon Ricketts]], un pistolero retiré, l'entraîne. John tue ou capture [[javier-escuella|Javier]] à El Presidio ; à Escalera, [[luisa-fortuna|Luisa Fortuna]] est tuée, puis Allende et Bill sont abattus sur la route par John ou par Reyes.",
    },
    "A3": {
        "en": "1911 and 1914. From Blackwater, with Professor [[harold-macdougal|Harold MacDougal]] and the informant [[nastas|Nastas]], John tracks [[dutch-van-der-linde|Dutch]] to Cochinay, in Tall Trees, where Dutch steps off a cliff. John returns to Beecher's Hope. Soldiers and Bureau agents attack the ranch: [[uncle|Uncle]] is killed and John is shot down outside his barn. In 1914, [[jack-marston|Jack Marston]] kills [[edgar-ross|Edgar Ross]] in a duel.",
        "fr": "1911 et 1914. Depuis Blackwater, avec le professeur [[harold-macdougal|Harold MacDougal]] et l'informateur [[nastas|Nastas]], John remonte la piste de [[dutch-van-der-linde|Dutch]] jusqu'à Cochinay, dans Tall Trees, où Dutch recule dans le vide du haut d'une falaise. John rentre à Beecher's Hope. L'armée et le Bureau attaquent le ranch : [[uncle|Uncle]] est tué et John est abattu devant sa grange. En 1914, [[jack-marston|Jack Marston]] tue [[edgar-ross|Edgar Ross]] en duel.",
    },
}

TXT = {
    "en": {
        "title": "The Red Dead Story, Chapter by Chapter | Red Dead Redemption 3",
        "og_title": "The Red Dead Story, Chapter by Chapter",
        "desc": "The story of Red Dead Redemption 2 and Red Dead Redemption, chapter by chapter: setting, camp and main events of each chapter, with the list of its missions.",
        "og_desc": "The story of Red Dead Redemption 2 and Red Dead Redemption, chapter by chapter, with the missions of each chapter.",
        "eyebrow": "Story guide",
        "h1": "The Red Dead story, chapter by chapter",
        "intro": "This page summarizes the story of Red Dead Redemption 2 (1899 and 1907) and Red Dead Redemption (1911 and 1914) in story order. Each summary gives the setting, the camp and the main events of the chapter. Where mission pages exist, the chapter's missions are listed in order, each with its own page. Each chapter also links to its full guide.",
        "note": "This page contains story spoilers.",
        "missions": lambda short, n: f"The {n} missions of {short}",
        "guide": lambda short: f"Full guide to {short}",
        "home": ("Home", "/"), "story": ("Story", "/story/"),
    },
    "fr": {
        "title": "L'histoire de Red Dead, chapitre par chapitre | Red Dead Redemption 3",
        "og_title": "L'histoire de Red Dead, chapitre par chapitre",
        "desc": "L'histoire de Red Dead Redemption 2 et de Red Dead Redemption, chapitre par chapitre : cadre, camp et principaux événements de chaque chapitre, avec la liste de ses missions.",
        "og_desc": "L'histoire de Red Dead Redemption 2 et de Red Dead Redemption, chapitre par chapitre, avec les missions de chaque chapitre.",
        "eyebrow": "Guide de l'histoire",
        "h1": "L'histoire de Red Dead, chapitre par chapitre",
        "intro": "Cette page résume l'histoire de Red Dead Redemption 2 (1899 et 1907) et de Red Dead Redemption (1911 et 1914), dans l'ordre du récit. Chaque résumé indique le cadre, le camp et les principaux événements du chapitre. Quand les pages de missions existent, les missions du chapitre sont listées dans l'ordre, chacune avec sa propre page. Chaque chapitre renvoie aussi à son guide complet.",
        "note": "Cette page dévoile l'histoire des deux jeux.",
        "missions": lambda short, n: f"Les {n} missions {_du(short)}",
        "guide": lambda short: f"Le guide complet {_du(short)}",
        "home": ("Accueil", "/fr/"), "story": ("Histoire", "/fr/histoire/"),
    },
}


def _du(short_fr):
    """'Chapitre 1' -> 'du chapitre 1'; 'Acte I' -> "de l'acte I"; 'Épilogue, partie 1' -> "de l'épilogue, partie 1"."""
    low = short_fr[0].lower() + short_fr[1:]
    return ("de l'" + low) if low[0] in "aeéiouy" else ("du " + low)


def load_missions():
    """Mission dicts from scripts/missions/*.py whose page is live, grouped by chapter key."""
    import build_missions
    out = {}
    for m in build_missions.load_all().values():
        if gf.mission_live(m["slug"]):
            out.setdefault(m["chapter"], []).append(m)
    for lst in out.values():
        lst.sort(key=lambda m: (m["number"], m["slug"]))
    return out


def guide_href(key, lang):
    en_slug, fr_slug = CHAPTERS[key][0], CHAPTERS[key][1]
    rel = os.path.join("story", en_slug) if lang == "en" else os.path.join("fr", "histoire", fr_slug)
    if not os.path.isfile(os.path.join(ROOT, rel, "index.html")):
        return None
    return "/" + rel.replace(os.sep, "/") + "/"


def _block(key, lang, missions):
    t = TXT[lang]
    i = 0 if lang == "en" else 1
    anchor, labels, titles, thumb = BLOCKS[key]
    short = CHAPTERS[key][4 + i]  # "Chapter 1" / "Chapitre 1"
    g = guide_href(key, lang)
    title = f'<a href="{g}">{titles[i]}</a>' if g else titles[i]
    summary = gf._links(SUMMARIES[key][lang], lang)
    thumb_img = (f'<img src="/assets/story/locations/{thumb}.jpeg" alt="" width="640" height="360" loading="lazy">')
    thumb_html = (f'<a class="storyrow__thumb" href="{g}" tabindex="-1" aria-hidden="true">{thumb_img}</a>' if g
                  else f'<span class="storyrow__thumb" aria-hidden="true">{thumb_img}</span>')
    out = [
        f'                    <li class="timeline__item" id="{anchor}">',
        f'                        <div class="timeline__year">{labels[i]}</div>',
        '                        <div class="timeline__content">',
        '                            <div class="storyrow">',
        '                                <div class="storyrow__text">',
        f'                                    <h3 class="timeline__title">{title}</h3>',
        f'                                    <p>{summary}</p>',
        '                                </div>',
        f'                                {thumb_html}',
        '                            </div>',
    ]
    ms = missions.get(key, [])
    if ms:
        mbase = mission_urls  # (en, fr)
        items = []
        for m in ms:
            href = mbase(m["slug"])[i]
            note = " ".join(c[lang] for c in m.get("chips", []))
            note_html = f'<span class="story-missions__note">{note}</span>' if note else ""
            items.append(
                f'                                        <li><span class="story-missions__num">{m["number"]}</span>'
                f'<span class="story-missions__name"><a href="{href}">{m["name"]}</a>{note_html}</span></li>')
        out += [
            '                            <details class="accordion story-missions">',
            f'                                <summary>{t["missions"](short, len(ms))}</summary>',
            '                                <div class="accordion__body">',
            '                                    <ol class="story-missions__list">',
            *items,
            '                                    </ol>',
            '                                </div>',
            '                            </details>',
        ]
    if g:
        out.append(f'                            <p class="storyrow__guide"><a href="{g}">{t["guide"](short)}</a></p>')
    out += ['                        </div>', '                    </li>']
    return "\n".join(out)


def _page(lang, missions):
    en = lang == "en"
    t = TXT[lang]
    path = "/story/" if en else "/fr/histoire/"
    url = SITE + path
    up = "../" if en else "../../"
    home_lbl, home_href = t["home"]
    story_lbl, _ = t["story"]

    body = []
    for game, groups in LAYOUT:
        body.append(f'                <h2>{game}</h2>')
        body.append('                <ol class="timeline">')
        for year, keys in groups:
            body.append(f'                    <li class="timeline__yeardiv">{year}</li>')
            for k in keys:
                body.append(_block(k, lang, missions))
        body.append('                </ol>')
        body.append('')
    body_html = "\n".join(body).rstrip()

    logo_href, logo_aria, navlabel = (("/", "Red Dead Redemption 3, Home", "Primary") if en
                                      else ("/fr/", "Red Dead Redemption 3, accueil", "Principale"))
    menu = gf.header_menu(lang, "story", "/story/", "/fr/histoire/")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t["title"]}</title>
    <meta name="description" content="{t["desc"]}">
    <link rel="canonical" href="{url}">

    <link rel="alternate" hreflang="en" href="{SITE}/story/">
    <link rel="alternate" hreflang="fr" href="{SITE}/fr/histoire/">
    <link rel="alternate" hreflang="x-default" href="{SITE}/story/">

    <meta property="og:type" content="website">
    <meta property="og:locale" content="{"en_US" if en else "fr_FR"}">
    <meta property="og:url" content="{url}">
    <meta property="og:site_name" content="Red Dead Redemption 3">
    <meta property="og:title" content="{t["og_title"]}">
    <meta property="og:description" content="{t["og_desc"]}">
    <meta property="og:image" content="{SITE}/assets/logo-red-dead-redemption-3-1.png">

    <link rel="icon" type="image/png" href="{up}assets/favicon-red-dead-redemption-3.png">
    <link rel="preload" href="{up}assets/fonts/chinese-rock.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="{up}css/style.css?v={CSS_V}">

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "{t["og_title"]}",
        "description": "{t["og_desc"]}",
        "url": "{url}",
        "inLanguage": "{lang}",
        "dateModified": "{UPDATED}",
        "publisher": {{ "@type": "Organization", "name": "Red Dead Redemption 3", "url": "{SITE}/" }}
    }}
    </script>
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "{home_lbl}", "item": "{SITE}{home_href}" }},
            {{ "@type": "ListItem", "position": 2, "name": "{story_lbl}", "item": "{url}" }}
        ]
    }}
    </script>
</head>
<body class="theme-light read-dark">
    <header class="site-header">
        <div class="site-header__inner">
            <a href="{logo_href}" class="site-header__logo" aria-label="{logo_aria}">
                <img src="{up}assets/logo-red-dead-redemption-3-1.png" alt="Red Dead Redemption 3" width="5794" height="1698">
            </a>
            <nav class="site-header__nav" aria-label="{navlabel}">
{menu}
            </nav>
        </div>
    </header>

    <main>
        <nav class="breadcrumb" aria-label="Breadcrumb">
            <ol>
                <li><a href="{home_href}">{home_lbl}</a></li>
                <li><span class="breadcrumb__sep">&rsaquo;</span><span aria-current="page">{story_lbl}</span></li>
            </ol>
        </nav>
        <article class="article">
            <header class="article-header">
                <p class="article-eyebrow">{t["eyebrow"]}</p>
                <h1 class="article-title">{t["h1"]}</h1>
            </header>
            <div class="article-body">
                <p>{t["intro"]}</p>
                <p class="note"><em>{t["note"]}</em></p>

{body_html}
            </div>
        </article>
    </main>

    <footer class="site-footer">
{gf.footer_html(lang)}
    </footer>

    <script src="{up}js/main.js?v={JS_V}"></script>
</body>
</html>
'''


def main():
    gf.LINK_LIVE_ONLY = True  # never link a fiche that is not live yet
    missions = load_missions()
    for lang, rel in (("en", "story/index.html"), ("fr", "fr/histoire/index.html")):
        p = os.path.join(ROOT, rel)
        with open(p, "w", encoding="utf-8") as f:
            f.write(_page(lang, missions))
        print("wrote", rel)


if __name__ == "__main__":
    main()
