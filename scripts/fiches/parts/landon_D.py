"""Landon Ricketts, reference fiche, PART D: base data, Development and performance, Reception
(20 Oct 2026, medium tier).

His live page (characters/landon-ricketts/) was generated from the v2 entry in scripts/_wave4.py (order 19,
"slug": "landon-ricketts"; no entry in _enrich.py). publishDate 2026-07-30 kept (git c176aae, drip publish of
landon-ricketts, 30 Jul 2026). Eyebrow kept as on the live page ("Character &middot; Nuevo Paraíso"); reg_role matches
characters_registry.py ("Gunslinger &middot; RDR1" / "Pistolero &middot; RDR1").
Corrections to the v2 base:
- v2 "death": "1911" and facts "Died c. 1911 (reported 1914)": WRONG. The article "Landon Ricketts Dead" (Blackwater
  Ledger No. 213, the last issue, 1914) says he died "last week" and had returned to the US "three years ago". Death =
  1914.
- v2 "dies quietly in his sleep of old age": the article says only that he "passed away quietly in his sleep"; no
  cause is given. "Old age" dropped (also in the CLAUDE.md wave 4 note, to fix there).
- v2 "He is the only one of John's Red Dead Redemption allies to die within the story's span": false (Uncle and Luisa,
  among others, die in the story). Dropped.
- v2 "voiced by Ross Hagen, in his final role": no source found (Wikipedia lists Red Dead Redemption and Undead
  Nightmare among his credits, nothing about a last role). Dropped.
- v2 "modelled on figures like Wyatt Earp and Wild Bill Hickok" and the Lee Van Cleef trivia: Red Dead Wiki
  speculation ("appears to be", "resemblance", "possible"), no Rockstar source. Dropped.
- v2 "Past his prime but still the fastest gun around", "the town's unofficial protector", "calm, principled and
  world-weary": interpretation or wiki wording; replaced by what the transcripts and the guide (quoted in part B) say.
- v2 "Colonel Agustín Allende": the live slug and registry spell "Agustin Allende"; aligned.
- v2 "its 2024 remaster": dropped (port dates not needed here).
- Facts grid gains Name, Born (attributed), Residence, Occupation, Family, Weapons, Games (incl. Undead Nightmare and
  RDR2 mentions), Played by. The "Deceased" chip duplicated the status and is dropped.

Sources (internal register, read 20 Oct 2026; saved in scripts/v3/work/_m/ and scripts/v3/work/landon/fc/):
- Wikipedia "Ross Hagen" (fc/wp_ross_hagen.txt): born Leland Lando Lilly, 21 May 1938, Williams, Arizona; died of
  cancer at his home in Brentwood, Los Angeles, on 7 May 2011, aged 72; Daktari (Bart Jason, 1968-1969), The Hellcats
  (1967), The Sidehackers (1969); played Landon Ricketts in Red Dead Redemption and Undead Nightmare; Mount Hagen and
  Hagen Orchards in Red Dead Redemption 2 named in his honor.
- Wikipedia "Red Dead Redemption" (fc/wp_rdr.txt): plot summary credits "Landon Ricketts (Ross Hagen)".
- Red Dead Wiki "Ross Hagen" (_m/Ross_Hagen.txt): prostate cancer (cites Variety, 2011; the Variety page could not be
  read: archive offline); Mount Hagen and Hagen Orchards named after him. "Hagen Orchards" trivia: reference to Hagen.
- Red Dead Wiki "Myths and Mavericks" (_m/Myths_and_Mavericks.txt): Rockstar used lines recorded for the single-player
  game for the multiplayer Ricketts, out of respect for Hagen, rather than hire another actor (wiki trivia, unsourced:
  attributed).
- Newspaper articles (wiki text): "Landon Ricketts Dead" (Blackwater Ledger No. 213), "Landon Ricketts Rumored Alive"
  (Blackwater Ledger No. 55). Narrative use is in part A; used here only for the base dates.
- Red Dead Wiki EN "Landon Ricketts": GOTY guide quote box (born circa 1861, footnoted to the GOTY guidebook).
- Reception: Sportskeeda, Aniket Mukherjee, "10 best characters in the Red Dead Redemption franchise", 13 Aug 2023
  (fc/sportskeeda_2023-08-13.txt, read in full: 4th of 10; 3rd Bonnie MacFarlane, 5th Bill Williamson); WhatCulture,
  Stacey Henley, "Red Dead Redemption 2: 10 Iconic Western Characters You Must Create", 1 Jun 2019 (10th; costume based
  on his cigarette card); EarlyGame (German edition), Alisa Eiber, "Wer wird der Hauptcharakter in Red Dead Redemption 3
  sein?", 9 Dec 2021; Ei Nerd! (Brazil), Vinicius Miranda, "Red Dead Redemption 3 poderia ter outro protagonista; saiba
  quem é", 26 Jul 2026. Notes in fc/web_notes_BD.txt (WebFetch extracts).

Excluded: "final role" (no source); the Earp, Hickok, Michael Landon and Lee Van Cleef models (wiki speculation); the
Variety obituary's details (not read); Rob Wiethoff naming "The Mexican Wagon Train" his favorite mission (mission page
trivia with no source or date: left out; part C may keep it only if a dated source is found); Hagen's other credits
beyond those Wikipedia names; the EarlyGame and Ei Nerd articles presented as anything but speculation (they are
quoted as press articles about fan expectations, with no Rockstar announcement); no cut content found for Ricketts
(Red Dead Redemption Cut Content page, 20 Oct 2026: no mention).
DUPLICATE ownership: actor, the Hagen place names and the Myths and Mavericks voice decision live HERE; part C (Other
media, Trivia) may name the pack and the ability card but must not repeat these points.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Landon Ricketts appears in Red Dead Redemption and its expansion Undead Nightmare, both released in 2010. He is played by Ross Hagen, credited in the role by the Red Dead Wiki and by Wikipedia's article on the game. Hagen, born Leland Lando Lilly on 21 May 1938 in Williams, Arizona, was an American actor, director, screenwriter and producer. According to Wikipedia, his credits include the series Daktari, in which he played the photographer Bart Jason from 1968 to 1969, and the films The Hellcats (1967) and The Sidehackers (1969).",
              "Landon Ricketts apparaît dans Red Dead Redemption et dans son extension Undead Nightmare, sortis tous deux en 2010. Il est interprété par Ross Hagen, que le Red Dead Wiki et l'article de Wikipédia consacré au jeu créditent dans ce rôle. Né Leland Lando Lilly le 21 mai 1938 à Williams, en Arizona, Hagen était acteur, réalisateur, scénariste et producteur américain. D'après Wikipédia, on lui doit notamment le rôle du photographe Bart Jason dans la série Daktari, de 1968 à 1969, ainsi que les films The Hellcats (1967) et The Sidehackers (1969).")},
    {"h3": two("After Ross Hagen's death", "Après la mort de Ross Hagen")},
    {"p": two("Ross Hagen died of cancer at his home in Brentwood, Los Angeles, on 7 May 2011, at the age of 72, according to Wikipedia; the Red Dead Wiki specifies prostate cancer. Ricketts became a playable character model in the multiplayer mode with the Myths and Mavericks pack, released later that year. According to the Red Dead Wiki, Rockstar gave him lines taken from the single-player game, out of respect for Hagen, rather than cast another actor. Wikipedia reports that two places in Red Dead Redemption 2 (2018) were named in his honor: Mount Hagen and Hagen Orchards, a plantation in the Bayou Nwa region of Lemoyne.",
              "Ross Hagen est mort d'un cancer à son domicile de Brentwood, à Los Angeles, le 7 mai 2011, à 72 ans, selon Wikipédia ; le Red Dead Wiki précise un cancer de la prostate. Ricketts devient un modèle de personnage jouable du mode multijoueur avec le pack Myths and Mavericks, publié plus tard la même année. D'après le Red Dead Wiki, Rockstar lui a donné des répliques reprises du mode solo, par respect pour Hagen, plutôt que d'engager un autre acteur. Wikipédia indique que deux lieux de Red Dead Redemption 2 (2018) portent son nom en hommage : Mount Hagen et Hagen Orchards, une plantation de la région de Bayou Nwa, en Lemoyne.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Character rankings", "Classements de personnages")},
    {"p": two("In a list of the ten best characters of the Red Dead Redemption franchise, published by Sportskeeda on 13 August 2023, Aniket Mukherjee ranked Ricketts fourth. He comes after John Marston, Dutch van der Linde and Bonnie MacFarlane, and ahead of Bill Williamson (fifth). The author wrote that he \"earns the fourth place for his pivotal role as a mentor\" to John. On 1 June 2019, Stacey Henley of WhatCulture placed him tenth in a list of Western characters to recreate in Red Dead Redemption 2, noting that the outfit can be based on his cigarette card in that game.",
              "Dans une liste des dix meilleurs personnages de la série Red Dead Redemption publiée par Sportskeeda le 13 août 2023, Aniket Mukherjee classe Ricketts quatrième. Il arrive derrière John Marston, Dutch van der Linde et Bonnie MacFarlane, et devant Bill Williamson (cinquième). L'auteur écrit qu'il \"earns the fourth place for his pivotal role as a mentor\" (doit sa quatrième place à son rôle central de mentor) auprès de John. Le 1er juin 2019, Stacey Henley, de WhatCulture, le place dixième d'une liste de personnages de western à recréer dans Red Dead Redemption 2, en précisant que la tenue peut s'inspirer de sa carte de cigarettes dans ce jeu.")},
    {"h3": two("Talk of a Red Dead Redemption 3", "Les spéculations sur un Red Dead Redemption 3")},
    {"p": two("Rockstar has not announced a Red Dead Redemption 3. Ricketts has been named in press articles about what players expect from one. On 9 December 2021, Alisa Eiber, writing for the German edition of EarlyGame, considered him the most likely protagonist among three candidates, as a famous gunslinger whose story would take the series back to an earlier period of the Old West. On 26 July 2026, the Brazilian site Ei Nerd! (Vinicius Miranda) reported that fans favored him as a protagonist for a game set in his prime, while stressing that there was no official confirmation.",
              "Rockstar n'a annoncé aucun Red Dead Redemption 3. Ricketts est pourtant cité dans des articles de presse consacrés aux attentes des joueurs. Le 9 décembre 2021, Alisa Eiber, pour l'édition allemande d'EarlyGame, le jugeait le protagoniste le plus probable parmi trois candidats : un pistolero célèbre, dont l'histoire ramènerait la série à une période plus ancienne de l'Ouest. Le 26 juillet 2026, le site brésilien Ei Nerd! (Vinicius Miranda) rapportait que les fans le verraient bien en héros d'un jeu situé à l'époque de sa gloire, tout en soulignant l'absence de toute confirmation officielle.")},
]


BASE = {
    "slug": "landon-ricketts", "name": "Landon Ricketts",
    "publishDate": "2026-07-30", "updated": "2026-10-20", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Gunslinger &middot; RDR1", "reg_role_fr": "Pistolero &middot; RDR1",
    "gender": "Male", "birth": None, "death": "1914", "nationality": "American",
    "portrait_alt": two("Landon Ricketts in Red Dead Redemption", "Landon Ricketts dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; Nuevo Paraíso", "Personnage &middot; Nuevo Paraíso"),
    "meta_desc": two("Landon Ricketts, the retired gunslinger of Chuparosa in Red Dead Redemption: John Marston's teacher, Luisa's rescue, the prison convoy, his death in 1914, Ross Hagen.",
                     "Landon Ricketts, le pistolero retiré à Chuparosa dans Red Dead Redemption : le maître de John Marston, l'évasion de Luisa, le convoi de prisonniers, sa mort en 1914, Ross Hagen."),
    "og_desc": two("The complete reference on Landon Ricketts: life, missions, quotes, development and reception.",
                   "La référence complète sur Landon Ricketts : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Retired American gunslinger living in Chuparosa, Mexico, who trains John Marston, helps him free Luisa Fortuna and a convoy of prisoners in 1911, and dies in his sleep in 1914, in Red Dead Redemption.",
                       "Pistolero américain retiré à Chuparosa, au Mexique, qui entraîne John Marston, l'aide à libérer Luisa Fortuna puis un convoi de prisonniers en 1911, et meurt dans son sommeil en 1914, dans Red Dead Redemption."),
    "chips": [two("Died <strong>1914</strong>", "Mort en <strong>1914</strong>"), two("Gunslinger", "Pistolero"),
              two("Chuparosa", "Chuparosa"),
              two("Played by <strong>Ross Hagen</strong>", "Interprété par <strong>Ross Hagen</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Landon Ricketts", "Landon Ricketts")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game; about 1861 according to the Red Dead Wiki, citing the Game of the Year Edition guide (which calls him 50 years old)", "Non précisée dans le jeu ; vers 1861 selon le Red Dead Wiki, qui s'appuie sur le guide de l'édition Game of the Year (qui lui donne 50 ans)")},
        {"label": two("Died", "Mort"), "value": two("1914, in his sleep, three years after returning to the United States (Blackwater Ledger)", "1914, dans son sommeil, trois ans après son retour aux États-Unis (Blackwater Ledger)")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédé")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Residence", "Résidence"), "value": two("Chuparosa, Nuevo Paraíso (1911); the United States from 1911", "Chuparosa, Nuevo Paraíso (1911) ; les États-Unis à partir de 1911")},
        {"label": two("Occupation", "Activité"), "value": two("Retired gunslinger", "Pistolero retiré")},
        {"label": two("Family", "Famille"), "value": two("A wife, unnamed, deceased before 1911", "Une épouse, jamais nommée, morte avant 1911")},
        {"label": two("Allies", "Alliés"), "value": two("[[john-marston|John Marston]], [[luisa-fortuna|Luisa Fortuna]]", "[[john-marston|John Marston]], [[luisa-fortuna|Luisa Fortuna]]")},
        {"label": two("Enemy", "Ennemi"), "value": two("The Mexican Army of [[agustin-allende|Agustin Allende]]", "L'armée mexicaine d'[[agustin-allende|Agustin Allende]]")},
        {"label": two("Weapons", "Armes"), "value": two("Cattleman Revolver, Schofield Revolver", "Cattleman Revolver, Schofield Revolver")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption, Undead Nightmare; mentioned in Red Dead Redemption 2", "Red Dead Redemption, Undead Nightmare ; cité dans Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Ross Hagen", "Ross Hagen")},
    ],
    "intro": [
        two("Landon Ricketts is a retired American gunslinger in Red Dead Redemption (2010), set in 1911. Newspapers in the game tie him to the Blackwater Massacre of 1899 and to the deaths of the Butcher Brothers in 1896. He lives in Chuparosa, in Nuevo Paraíso, when [[john-marston|John Marston]] arrives there. He trains John, helps him free [[luisa-fortuna|Luisa Fortuna]] from an army jail, sits with him at a poker game that ends in two duels, and rides with him to take a convoy of prisoners of [[agustin-allende|Agustin Allende]] across the border. The two part at the border. In 1914 the Blackwater Ledger reports that he has died in his sleep, three years after returning to the United States.",
            "Landon Ricketts est un pistolero américain retiré dans Red Dead Redemption (2010), dont l'action se déroule en 1911. Les journaux du jeu l'associent au massacre de Blackwater de 1899 et à la mort des frères Butcher en 1896. Il vit à Chuparosa, au Nuevo Paraíso, quand [[john-marston|John Marston]] y arrive. Il entraîne John, l'aide à libérer [[luisa-fortuna|Luisa Fortuna]] d'une prison de l'armée, partage avec lui une partie de poker qui se termine en deux duels, et l'accompagne pour faire passer la frontière à un convoi de prisonniers d'[[agustin-allende|Agustin Allende]]. Les deux hommes se séparent à la frontière. En 1914, le Blackwater Ledger annonce sa mort dans son sommeil, trois ans après son retour aux États-Unis."),
        two("He is played by Ross Hagen. He also appears in Undead Nightmare and is mentioned in Red Dead Redemption 2.",
            "Il est interprété par Ross Hagen. Il apparaît aussi dans Undead Nightmare et il est cité dans Red Dead Redemption 2."),
    ],
    "essentials": [
        two("In \"The Gunslinger's Tragedy\", he gives John a Schofield Revolver and teaches him the third level of Dead Eye.",
            "Dans \"The Gunslinger's Tragedy\", il offre à John un Schofield Revolver et lui enseigne le troisième niveau du Dead Eye."),
        two("In \"Landon Ricketts Rides Again\", he and John break Luisa Fortuna out of an army jail in the caves near El Matadero.",
            "Dans \"Landon Ricketts Rides Again\", John et lui font évader Luisa Fortuna d'une prison de l'armée, dans les grottes près d'El Matadero."),
        two("In \"Lucky in Love\", a poker game at the Chuparosa cantina turns into John's duels with Andreas Müller and the Stranger.",
            "Dans \"Lucky in Love\", une partie de poker à la cantina de Chuparosa tourne aux duels de John contre Andreas Müller et l'Étranger."),
        two("In \"The Mexican Wagon Train\", he and John seize Allende's prison wagons and drive them across the border, where they part.",
            "Dans \"The Mexican Wagon Train\", John et lui s'emparent des chariots de prisonniers d'Allende et leur font passer la frontière, où ils se séparent."),
        two("The last Blackwater Ledger of 1914 reports his death in his sleep; the article gives no cause.",
            "Le dernier Blackwater Ledger de 1914 annonce sa mort dans son sommeil ; l'article n'en donne pas la cause."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["john-marston", "luisa-fortuna", "agustin-allende", "abraham-reyes"],
}
