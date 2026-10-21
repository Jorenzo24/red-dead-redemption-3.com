"""Leigh Johnson, reference fiche, PART D: base data, Development and performance, Reception
(21 Oct 2026, medium tier).

His live page (characters/leigh-johnson/) was generated from the v2 entry in scripts/_wave4.py (order 22,
"slug": "leigh-johnson"; no entry in _enrich.py). publishDate 2026-08-08 kept (git 03ef08f, drip publish of
leigh-johnson, 8 Aug 2026). Eyebrow kept as on the live page ("Character &middot; Armadillo"); reg_role matches
characters_registry.py ("Marshal &middot; RDR1" in both languages).
Corrections to the v2 base:
- v2 "a weary but principled lawman", "decent under the weariness", "two loyal deputies": interpretation; replaced by
  the GOTY guide quote (part B) and by facts.
- v2 "Red Dead Redemption (2010) and its 2024 remaster": dropped (the 2023 console and 2024 PC releases are ports).
- v2 "Games: Red Dead Redemption": Undead Nightmare added ("Dinner for Two"), plus the Liars and Cheats multiplayer model.
- v2 "Born c. 1860" as a bare fact: now sourced (the 1914 Blackwater Ledger & Sentinel gives his age as 54 when he
  retires; the GOTY guide, quoted by the Red Dead Wiki, says 50).
- v2 "Johnson leads the Tumbleweed prisoner exchange... which he correctly reads as a trap": the transcript has him
  doubt that the gang will "play fair"; John, not Johnson, walks Deek in and makes the exchange.
- v2 "Johnson and John part ways": kept; the wiki's "Johnson and Marston thank each other" is not in the transcript
  (Johnson only says "I'm sorry about this, John.").
- v2 "clear the Bollard Twins from Pike's Basin": the transcript has Eli say he thinks the rustlers are the Bollard
  Twins; the 1914 article credits Johnson with taking them down. Kept with that wording.

SOURCE REGISTER (read 21 Oct 2026):
- Wikipedia "Red Dead Redemption" (landon/fc/wp_rdr.txt): "U.S. Marshal Leigh Johnson (Anthony De Longis)".
- Wikipedia "Anthony De Longis" (leigh/fc/wp_anthony_de_longis.txt, raw wikitext): born March 23, 1950 in Glendale,
  California; actor, stuntman and fight choreographer; voice of Marshal Leigh Johnson in Red Dead Redemption and
  Undead Nightmare (2010); Blade in Masters of the Universe (1987); First Maje Jal Culluh in Star Trek: Voyager;
  whip training for Harrison Ford (Indiana Jones and the Kingdom of the Crystal Skull, 2008) and for Michelle Pfeiffer
  (Batman Returns, 1992). Red Dead Wiki "Anthony De Longis" (_m/Anthony_De_Longis.txt) agrees on the role and the date.
- Kotaku, Owen Good, "Losing His Voice In Red Dead Redemption", August 17, 2010 (leigh/fc/kotaku_2010-08-17_nissan.txt):
  Colin Nissan recorded the role at Rockstar's SoHo studio over two hours; the Marshal appeared in a trailer two months
  before release without his voice, and spoke with someone else's voice in the released game. Nissan's own piece,
  "Searching For Me In Red Dead Redemption" (The Paris Review blog, 2010; exact date not verified), returned 403 and has no Wayback
  snapshot: cited only through Kotaku.
- Newspaper "Marshall Johnson of Armadillo Retires" (Blackwater Ledger & Sentinel No. 213, 1914), read on the page
  image (seth/fc/Blackwater_Ledger_Sentinel_No_213.png).
- Reception: Sportskeeda, Aniket Mukherjee, "10 best characters in the Red Dead Redemption franchise", page last
  modified August 13, 2023 (landon/fc/sportskeeda_2023-08-13.txt: Leigh Johnson 7th). Checked and NOT featuring him:
  Gameranx, Dennis Patrick, "Characters We Wouldn't Mind Seeing Again In Red Dead Redemption 2", 4 Nov 2016 (WebFetch).
  No other review or article on the character was found.

Excluded: motion capture for Johnson (no source names a performer); De Longis's other credits beyond those listed
above; whose voice the Marshal had in the pre-release trailer (Kotaku does not say; John's fiche notes that the early
trailers used different voices for several characters, told there); Nissan's line "Be careful with that thing" as a
line of the final game (not in any transcript); The Man from Blackwater (2010 machinima), the Liars and Cheats model,
"L. Johnson's Run" and the Red Dead Online mention, left to part C (Other media); Giant Bomb's "51 years old" (no game
source).
DUPLICATE ownership: the actor, De Longis's career and Colin Nissan's account live HERE; part C (Trivia, Other media)
must not repeat them.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Leigh Johnson appears in Red Dead Redemption and its expansion Undead Nightmare, both released in 2010. Wikipedia credits Anthony De Longis with the role in both games. According to Wikipedia, De Longis is an American actor, stuntman and fight choreographer, born on March 23, 1950 in Glendale, California. His other roles include Blade in the film Masters of the Universe (1987) and the Kazon leader Jal Culluh in Star Trek: Voyager. A weapons master, he taught Michelle Pfeiffer the bullwhip for Batman Returns (1992) and gave Harrison Ford whip training for Indiana Jones and the Kingdom of the Crystal Skull (2008). No source consulted names a performer for Johnson's motion capture.",
              "Leigh Johnson apparaît dans Red Dead Redemption et dans son extension Undead Nightmare, sortis tous deux en 2010. Wikipédia attribue le rôle à Anthony De Longis dans les deux jeux. Selon Wikipédia, De Longis est un acteur, cascadeur et chorégraphe de combat américain, né le 23 mars 1950 à Glendale, en Californie. On lui doit aussi le rôle de Blade dans le film Les Maîtres de l'univers (1987) et celui du chef kazon Jal Culluh dans Star Trek: Voyager. Maître d'armes, il a appris le maniement du fouet à Michelle Pfeiffer pour Batman : Le Défi (1992) et à Harrison Ford pour Indiana Jones et le Royaume du crâne de cristal (2008). Aucune des sources consultées ne nomme d'interprète pour la capture de mouvement de Johnson.")},
    {"h3": two("A first actor replaced", "Un premier interprète remplacé")},
    {"p": two("On August 17, 2010, Kotaku (Owen Good) relayed an account by the actor Colin Nissan, written for the blog of The Paris Review under the title \"Searching For Me In Red Dead Redemption\". Nissan had been cast as the Marshal and recorded his lines over two hours at Rockstar's studio in SoHo. According to the article, the Marshal appeared in a trailer two months before the game's release without Nissan's voice. When the game came out, Nissan found that the character spoke with another actor's voice.",
              "Le 17 août 2010, Kotaku (Owen Good) relaie le récit de l'acteur Colin Nissan, écrit pour le blog de The Paris Review sous le titre \"Searching For Me In Red Dead Redemption\". Nissan avait été choisi pour incarner le marshal et avait enregistré ses répliques en deux heures dans le studio de Rockstar à SoHo. D'après l'article, le marshal apparaît dans une bande-annonce deux mois avant la sortie du jeu, sans la voix de Nissan. À la sortie, Nissan découvre que le personnage parle avec la voix d'un autre acteur.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Character lists", "Classements de personnages")},
    {"p": two("In a list of the ten best characters of the Red Dead Redemption franchise, published by Sportskeeda (page last modified on August 13, 2023), Aniket Mukherjee ranked Marshal Leigh Johnson seventh, between Seth Briars (eighth) and Nigel West Dickens (sixth). The author cited \"his commitment to maintaining law and order in a chaotic frontier\" and wrote that \"His partnership with John Marston adds an interesting dynamic to the story.\" No other review or article dedicated to the character was found.",
              "Dans une liste des dix meilleurs personnages de la série Red Dead Redemption publiée par Sportskeeda (page modifiée pour la dernière fois le 13 août 2023), Aniket Mukherjee classe le marshal Leigh Johnson septième, entre Seth Briars (huitième) et Nigel West Dickens (sixième). L'auteur met en avant \"his commitment to maintaining law and order in a chaotic frontier\" (son engagement à maintenir l'ordre dans une frontière chaotique) et estime que \"His partnership with John Marston adds an interesting dynamic to the story.\" (son association avec John Marston apporte une dynamique intéressante à l'histoire). Aucune autre critique ni aucun autre article consacré au personnage n'a été trouvé.")},
]


BASE = {
    "slug": "leigh-johnson", "name": "Leigh Johnson",
    "publishDate": "2026-08-08", "updated": "2026-10-21", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Marshal &middot; RDR1", "reg_role_fr": "Marshal &middot; RDR1",
    "gender": "Male", "birth": None, "death": None, "nationality": "American",
    "portrait_alt": two("Marshal Leigh Johnson in Red Dead Redemption", "Le marshal Leigh Johnson dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; Armadillo", "Personnage &middot; Armadillo"),
    "meta_desc": two("Marshal Leigh Johnson of Armadillo in Red Dead Redemption: Walton Lowe, Pike's Basin, Ridgewood Farm, Tumbleweed, Fort Mercer, his 1914 retirement, Anthony De Longis.",
                     "Le marshal Leigh Johnson d'Armadillo dans Red Dead Redemption : Walton Lowe, Pike's Basin, Ridgewood Farm, Tumbleweed, Fort Mercer, sa retraite en 1914, Anthony De Longis."),
    "og_desc": two("The complete reference on Leigh Johnson: life, missions, quotes, development and reception.",
                   "La référence complète sur Leigh Johnson : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Marshal of Armadillo, New Austin, who in 1911 has John Marston help him against local gangs in exchange for his help against Bill Williamson, and joins the assault on Fort Mercer, in Red Dead Redemption.",
                       "Marshal d'Armadillo, au New Austin, qui en 1911 obtient l'aide de John Marston contre les bandes de la région en échange de son appui contre Bill Williamson, et prend part à l'assaut de Fort Mercer, dans Red Dead Redemption."),
    "chips": [two("Marshal of Armadillo", "Marshal d'Armadillo"), two("New Austin", "New Austin"),
              two("Retires in <strong>1914</strong>", "Retraité en <strong>1914</strong>"),
              two("Voiced by <strong>Anthony De Longis</strong>", "Voix : <strong>Anthony De Longis</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Leigh Johnson; usually called the Marshal or Marshal Johnson", "Leigh Johnson ; on l'appelle le plus souvent le Marshal ou le marshal Johnson")},
        {"label": two("Born", "Naissance"), "value": two("Around 1860: aged 54 when he retires in 1914, according to the Blackwater Ledger & Sentinel; 50 according to the Game of the Year Edition guide, quoted by the Red Dead Wiki", "Vers 1860 : 54 ans à sa retraite en 1914, selon le Blackwater Ledger & Sentinel ; 50 ans selon le guide de l'édition Game of the Year, cité par le Red Dead Wiki")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1914, retired (Blackwater Ledger & Sentinel)", "Vivant en 1914, à la retraite (Blackwater Ledger & Sentinel)")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Occupation", "Activité"), "value": two("Marshal of Armadillo for 17 years, until 1914", "Marshal d'Armadillo pendant 17 ans, jusqu'en 1914")},
        {"label": two("Base", "Base"), "value": two("Sheriff's office, Armadillo, Cholla Springs, New Austin", "Bureau du shérif d'Armadillo, Cholla Springs, New Austin")},
        {"label": two("Family", "Famille"), "value": two("Priscilla Johnson, his wife (died April 23, 1903, according to her tombstone)", "Priscilla Johnson, sa femme (morte le 23 avril 1903, selon sa pierre tombale)")},
        {"label": two("Deputies", "Adjoints"), "value": two("Jonah, Eli", "Jonah, Eli")},
        {"label": two("Allies", "Alliés"), "value": two("[[john-marston|John Marston]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[nigel-west-dickens|Nigel West Dickens]]", "[[john-marston|John Marston]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[nigel-west-dickens|Nigel West Dickens]]")},
        {"label": two("Weapons", "Armes"), "value": two("Two nickel-plated Cattleman Revolvers; Repeater Carbine, Winchester Repeater and Double-barreled Shotgun (Red Dead Wiki)", "Deux Cattleman Revolvers nickelés ; Repeater Carbine, Winchester Repeater et fusil à double canon (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption, Undead Nightmare; multiplayer model (Liars and Cheats)", "Red Dead Redemption, Undead Nightmare ; modèle multijoueur (Liars and Cheats)")},
        {"label": two("Voiced by", "Voix"), "value": two("Anthony De Longis", "Anthony De Longis")},
    ],
    "intro": [
        two("Leigh Johnson is the marshal of Armadillo, in New Austin, in Red Dead Redemption (2010), set in 1911. When [[john-marston|John Marston]] asks him for help against [[bill-williamson|Bill Williamson]], John first helps him with his own problems. They track the outlaw Walton Lowe, wipe out a band of cattle rustlers at Pike's Basin and capture Norman Deek, Williamson's second-in-command, after a raid on Ridgewood Farm. When Bill's gang kidnaps [[bonnie-macfarlane|Bonnie MacFarlane]] to free Deek, Johnson leads the posse to Tumbleweed. He then joins the assault on Fort Mercer with his deputies Jonah and Eli, but Bill has already left for Mexico.",
            "Leigh Johnson est le marshal d'Armadillo, au New Austin, dans Red Dead Redemption (2010), dont l'action se déroule en 1911. Quand [[john-marston|John Marston]] lui demande de l'aide contre [[bill-williamson|Bill Williamson]], John commence par l'aider à régler ses propres problèmes. Ensemble, ils traquent le hors-la-loi Walton Lowe, éliminent une bande de voleurs de bétail à Pike's Basin et capturent Norman Deek, le bras droit de Williamson, après un raid sur Ridgewood Farm. Quand la bande de Bill enlève [[bonnie-macfarlane|Bonnie MacFarlane]] pour faire libérer Deek, Johnson mène la troupe jusqu'à Tumbleweed. Il prend ensuite part à l'assaut de Fort Mercer avec ses adjoints Jonah et Eli, mais Bill est déjà parti pour le Mexique."),
        two("In 1914, the last newspaper of the game reports that he has retired at 54, after 17 years as marshal. He is voiced by Anthony De Longis and also appears in Undead Nightmare.",
            "En 1914, le dernier journal du jeu annonce qu'il a pris sa retraite à 54 ans, après 17 ans comme marshal. Il a la voix d'Anthony De Longis et apparaît aussi dans Undead Nightmare."),
    ],
    "essentials": [
        two("In \"Political Realities in Armadillo\", John offers to deal with Walton's gang before they discuss Williamson; together they follow Walton Lowe to Pleasance House.",
            "Dans \"Political Realities in Armadillo\", John propose de régler le cas de la bande de Walton avant de parler de Williamson ; ensemble, ils suivent Walton Lowe jusqu'à Pleasance House."),
        two("In \"Justice in Pike's Basin\", he and his deputies wipe out the rustlers holding a rancher's cattle.",
            "Dans \"Justice in Pike's Basin\", ses adjoints et lui éliminent les voleurs qui détiennent le bétail d'un éleveur."),
        two("In \"Spare the Rod, Spoil the Bandit\", his posse finds the massacre at Ridgewood Farm and captures Norman Deek.",
            "Dans \"Spare the Rod, Spoil the Bandit\", sa troupe découvre le massacre de Ridgewood Farm et capture Norman Deek."),
        two("In \"Hanging Bonnie MacFarlane\", the exchange of Deek for Bonnie at Tumbleweed is a trap; John cuts Bonnie down from the gallows.",
            "Dans \"Hanging Bonnie MacFarlane\", l'échange de Deek contre Bonnie à Tumbleweed est un piège ; John décroche Bonnie de la potence."),
        two("In \"The Assault on Fort Mercer\", he and his deputies take the fort with John, Dickens and Seth, but Bill has left for Mexico.",
            "Dans \"The Assault on Fort Mercer\", ses adjoints et lui prennent le fort avec John, Dickens et Seth, mais Bill est parti pour le Mexique."),
        two("In Undead Nightmare, which is not canon, he sends John after his missing deputies in \"Dinner for Two\".",
            "Dans Undead Nightmare, qui n'appartient pas au canon, il envoie John chercher ses adjoints disparus dans \"Dinner for Two\"."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["john-marston", "bonnie-macfarlane", "nigel-west-dickens", "bill-williamson"],
}
