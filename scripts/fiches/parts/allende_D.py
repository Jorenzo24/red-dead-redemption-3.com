"""Agustin Allende, reference fiche, PART D: base data, Development and performance, Reception
(21 Oct 2026, medium tier).

His live page (characters/agustin-allende/) was generated from the v2 entry in scripts/_wave6.py (order 32,
"slug": "agustin-allende"; no entry in _enrich.py). publishDate 2026-09-15 kept (live byline "Updated September 15,
2026"). Eyebrow kept as on the live page ("Character &middot; Nuevo Paraiso", without the accent in EN); reg_role matches
characters_registry.py ("Provincial governor &middot; RDR1" / "Gouverneur de province &middot; RDR1").
Corrections to the v2 base:
- v2 "Bill Williamson and Javier Escuella... working as hired guns for his regime": no transcript says so. Reyes says they
  paid Allende to hide them ("The Gates of El Presidio"); reworded as protection.
- v2 "Allende neither hands them over nor admits they are there": he tells John in "Mexican Caesar" that the two men ride
  with Reyes, and in "Cowards Die Many Times" that they have been captured in Chuparosa; dropped.
- v2 "His soldiers conscript villagers, seize property", "his authority... effectively absolute", "taxes": not in the
  transcripts in those terms; replaced by what the games show (Tesoro Azul, the women brought to the villa, the prisoners
  sent to their deaths) and by the GOTY guide description (part B).
- v2 "Allende is killed during the collapse... Abraham Reyes takes the province immediately afterwards": now precise and
  worded as HOUSE_FACTS (shot by John or by Reyes on the road out of Escalera, "An Appointed Time").
- v2 "John Marston... works for him under false pretences": John says he works for him to get Bill and Javier; reworded.
- v2 relationship "Vincente de Santa" had slug None: De Santa is now live (linked).
- v2 "Behind the scenes" (one sentence) replaced by Development and performance (actor) and Reception.
- v2 facts grid lacked actor, family, weapons, death place: added. Nationality "Mexican" kept (the games give no other).

SOURCE REGISTER (read 21 Oct 2026; notes in scripts/v3/work/allende/fc/web_notes_BD.txt):
- Wikipedia "Red Dead Redemption" (landon/fc/wp_rdr.txt): "Colonel Agustín Allende (Gary Carlos Cervantes), the state's
  tyrannical governor".
- Red Dead Wiki "Gary Carlos Cervantes" (_m/Gary_Carlos_Cervantes.txt): American actor born January 24, 1953, voice of
  Allende.
- TMDb person page 48136 (WebFetch 21 Oct 2026): "Gary Anthony 'Carlos' Cervantes", born January 24, 1953 in Maywood,
  California; Commando (1985, Diaz), Wild Wild West (1999).
- Wikipedia "Commando (1985 film)" cast: "Carlos Cervantes as Diaz"; Wikipedia "Wild Wild West" cast: "Gary Carlos
  Cervantes as Professor Guillermo Escobar, an MIT scientist kidnapped by Loveless".
- Red Dead Wiki "Agustin Allende" (trivia and Appearance: pre-release artwork fatter, no epaulets, no soul patch;
  gallery caption "Pre-release artwork of Colonel Allende"). "Red Dead Redemption Cut Content" checked: nothing on him.
- Game Informer, Matt Bertz, review of Red Dead Redemption, May 17, 2010 (quoted from reyes/fc/web_notes_BD.txt).
- WhatCulture, Matt Thompson, "Red Dead Redemption: Every Villain Ranked From Worst To Best", February 7, 2022 (curl of
  the 15 pages; Allende = no. 13, page 3).
- Javier Aldape (Texas A&M University), "The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1", Revista
  Panamericana de Comunicación, vol. 4, no. 2, pp. 21-34, 2022 (Redalyc; received 30 Sep 2022, accepted 21 Oct 2022;
  saved as allende/fc/aldape_mustang_diaries_redalyc.html).
- Newspaper for the base: "'Tyrannical' Governor Overthrown. Is Sanchez Next?" (Blackwater Ledger No. 58; text in
  reyes/fc/newspapers_reyes.txt). Told in part A.
- Checked, nothing found: any interview of Cervantes about the role; any motion-capture credit for Allende.

Excluded: the Victoriano Huerta, Salvador Allende, Pinochet, Ricardo Diaz and border-town "models" (wiki speculation;
Aldape's Huerta photo comparison is kept, attributed, in Reception); "his voice actor speaks Spanish in a strong American
accent, even committing several grammatical errors" (wiki opinion, no source); the Japanese voice actress Risa Taneda
(FR wiki, unsourced; Red Dead Redemption had no Japanese dub to our knowledge, not verified either way); Aldape's
"He begins shooting people randomly for simply 'looking at him'" and "his military sword and decorations are now worn and
ripped" (not supported by any transcript; not repeated); Aldape's "RDR1 hired cultural experts and Mexican historians"
(cites no source); Cervantes's full filmography beyond two cast lists verified on Wikipedia; Scarface and 1941 (TMDb
only); the GOTY box art and the Liars and Cheats model (part C, Other media).
DUPLICATE ownership: the actor and the pre-release artwork live HERE; part C (Trivia, Other media) must not repeat them.
The Bertz "corrupt ruler" line is quoted only here in this fiche.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Colonel Allende appears in Red Dead Redemption, released in 2010. Wikipedia's article on the game credits Gary Carlos Cervantes with the role and describes the character as \"the state's tyrannical governor\"; the Red Dead Wiki credits him as the voice of Allende. Cervantes is an American actor born on January 24, 1953, in Maywood, California, according to the TMDb database. Wikipedia's cast lists name him in Commando (1985), as Diaz, and in Wild Wild West (1999), as Professor Guillermo Escobar, a scientist kidnapped by the villain. No interview in which he discusses Red Dead Redemption was found, and no source consulted names a performer for Allende's motion capture.",
              "Le colonel Allende apparaît dans Red Dead Redemption, sorti en 2010. L'article de Wikipédia consacré au jeu attribue le rôle à Gary Carlos Cervantes et présente le personnage comme le gouverneur tyrannique de l'État ; le Red Dead Wiki le crédite comme voix d'Allende. Selon la base de données TMDb, Cervantes est un acteur américain né le 24 janvier 1953 à Maywood, en Californie. Les distributions publiées par Wikipédia le citent dans Commando (1985), dans le rôle de Diaz, et dans Wild Wild West (1999), dans celui du professeur Guillermo Escobar, un scientifique enlevé par le méchant du film. Aucune interview dans laquelle il évoque Red Dead Redemption n'a été trouvée, et aucune des sources consultées ne nomme d'interprète pour la capture de mouvement d'Allende.")},
    {"h3": two("Before release", "Avant la sortie")},
    {"p": two("Rockstar released artwork of the colonel before launch. According to the Red Dead Wiki, he looks heavier in this pre-release artwork than in the game, his uniform has no epaulettes, and he has no tuft of beard under the lip. The wiki's page on the game's cut content lists nothing else about him.",
              "Rockstar a diffusé avant la sortie une illustration du colonel. D'après le Red Dead Wiki, il y paraît plus corpulent que dans le jeu, son uniforme n'a pas d'épaulettes et il ne porte pas de mouche sous la lèvre. La page du wiki consacrée au contenu coupé du jeu ne mentionne rien d'autre à son sujet.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Reviews", "Critiques")},
    {"p": two("Game Informer's review of Red Dead Redemption, written by Matt Bertz and published on May 17, 2010, does not name Allende. It sums up the Mexican part of the story as John having to \"get cozy with both the corrupt ruler of the border region and the upstart rebel hell-bent on taking power for himself.\"",
              "La critique de Red Dead Redemption publiée par Game Informer le 17 mai 2010, signée Matt Bertz, ne nomme pas Allende. Elle résume la partie mexicaine de l'histoire : John doit \"get cozy with both the corrupt ruler of the border region and the upstart rebel hell-bent on taking power for himself.\" (se mettre bien à la fois avec le dirigeant corrompu de la région frontalière et avec le rebelle parvenu décidé à prendre le pouvoir pour lui-même).")},
    {"h3": two("Villain rankings", "Classements de méchants")},
    {"p": two("In \"Red Dead Redemption: Every Villain Ranked From Worst To Best\", published by WhatCulture on February 7, 2022, Matt Thompson ranks Allende 13th of 15 villains from both games. He writes that \"Colonel Allende could have had more depth written into his character\". He adds that the colonel's corruption, taste for murder and sexual assaults show in his words, \"but it's all surface level\", and that the game never explains how he rose to power and came to command such an army.",
              "Dans \"Red Dead Redemption: Every Villain Ranked From Worst To Best\", publié par WhatCulture le 7 février 2022, Matt Thompson classe Allende 13e sur 15 méchants des deux jeux. Il estime que \"Colonel Allende could have had more depth written into his character\" (le colonel Allende aurait mérité davantage de profondeur). Il ajoute que la corruption du colonel, son goût du meurtre et ses agressions sexuelles transparaissent dans ses paroles, \"but it's all surface level\" (mais tout reste en surface), et que le jeu n'explique jamais comment il est arrivé au pouvoir ni comment il commande une telle armée.")},
    {"h3": two("Academic study", "Étude universitaire")},
    {"p": two("In \"The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1\", published in the Revista Panamericana de Comunicación (vol. 4, no. 2, 2022), Javier Aldape, of Texas A&M University, writes that the game \"has two versions of caudillos in the personification of Colonel Agustin Allende on the Federales side and Abraham Reyes, the leader of the Mexican rebeldes.\" He compares the women and alcohol of Allende's house to period photographs of military men such as Victoriano Huerta with a cigar and a glass of cognac. He concludes that \"Allende falls victim to his desire to rule Mexico through betrayals\", in the manner of the caudillos of the time.",
              "Dans \"The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1\", article paru dans la Revista Panamericana de Comunicación (vol. 4, n° 2, 2022), Javier Aldape, de l'université Texas A&M, écrit que le jeu \"has two versions of caudillos in the personification of Colonel Agustin Allende on the Federales side and Abraham Reyes, the leader of the Mexican rebeldes.\" (incarne deux versions du caudillo : le colonel Agustin Allende, côté fédéral, et Abraham Reyes, chef des rebelles mexicains). Il rapproche les femmes et l'alcool de la demeure d'Allende des photographies d'époque de militaires comme Victoriano Huerta, cigare et verre de cognac en main. Il conclut qu'Allende est victime de son désir de gouverner le Mexique par la trahison, à la manière des caudillos de l'époque.")},
]


BASE = {
    "slug": "agustin-allende", "name": "Agustin Allende",
    "publishDate": "2026-09-15", "updated": "2026-10-21", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Provincial governor &middot; RDR1", "reg_role_fr": "Gouverneur de province &middot; RDR1",
    "gender": "Male", "birth": None, "death": "1911", "nationality": "Mexican",
    "portrait_alt": two("Colonel Agustin Allende in uniform at Escalera in Red Dead Redemption",
                        "Le colonel Agustin Allende en uniforme à Escalera dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; Nuevo Paraiso", "Personnage &middot; Nuevo Paraíso"),
    "meta_desc": two("Agustin Allende, colonel and governor of Nuevo Paraíso in Red Dead Redemption: Escalera, Bill Williamson and Javier Escuella, the Chuparosa betrayal, his death in 1911, Gary Carlos Cervantes.",
                     "Agustin Allende, colonel et gouverneur du Nuevo Paraíso dans Red Dead Redemption : Escalera, Bill Williamson et Javier Escuella, le piège de Chuparosa, sa mort en 1911, Gary Carlos Cervantes."),
    "og_desc": two("The complete reference on Agustin Allende: life, missions, quotes, development and reception.",
                   "La référence complète sur Agustin Allende : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Colonel of the Mexican Army and governor of Nuevo Paraíso, who shelters Bill Williamson and Javier Escuella in 1911 and is killed when the rebels take Escalera in Red Dead Redemption.",
                       "Colonel de l'armée mexicaine et gouverneur du Nuevo Paraíso, qui protège Bill Williamson et Javier Escuella en 1911 et meurt quand les rebelles prennent Escalera dans Red Dead Redemption."),
    "chips": [two("Colonel, Mexican Army", "Colonel de l'armée mexicaine"),
              two("Governor of Nuevo Paraíso", "Gouverneur du Nuevo Paraíso"),
              two("Died in <strong>1911</strong>", "Mort en <strong>1911</strong>"),
              two("Voiced by <strong>Gary Carlos Cervantes</strong>", "Voix : <strong>Gary Carlos Cervantes</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Agustin Allende (Agustín on Wikipedia)", "Agustin Allende (Agustín sur Wikipédia)")},
        {"label": two("Born", "Naissance"), "value": two("Date not given in the games; the Game of the Year Edition guide, quoted by the Red Dead Wiki, describes him as 53 years old (born around 1858, according to the wiki)", "Date non précisée dans les jeux ; le guide de l'édition Game of the Year, cité par le Red Dead Wiki, lui donne 53 ans (né vers 1858, selon le wiki)")},
        {"label": two("Died", "Mort"), "value": two("1911, on the road out of Escalera (\"An Appointed Time\"), shot by John Marston or by Abraham Reyes depending on the player", "1911, sur la route à la sortie d'Escalera (\"An Appointed Time\"), abattu par John Marston ou par Abraham Reyes selon le joueur")},
        {"label": two("Nationality", "Nationalité"), "value": two("Mexican", "Mexicaine")},
        {"label": two("Occupation", "Activité"), "value": two("Colonel in the Mexican Army; governor of Nuevo Paraíso under President Ignacio Sanchez", "Colonel de l'armée mexicaine ; gouverneur du Nuevo Paraíso sous la présidence d'Ignacio Sanchez")},
        {"label": two("Residence", "Résidence"), "value": two("His mansion at the top of Escalera, Punta Orgullo", "Sa demeure au sommet d'Escalera, Punta Orgullo")},
        {"label": two("Family", "Famille"), "value": two("An unnamed uncle, on whose land Javier Escuella's father worked (the Red Dead Wiki says he owned farmland in the province)", "Un oncle dont le nom n'est pas donné, sur les terres duquel travaillait le père de Javier Escuella (le Red Dead Wiki en fait un propriétaire terrien de la province)")},
        {"label": two("Officers", "Officiers"), "value": two("Captain [[vincente-de-santa|Vincente de Santa]], Captain Espinoza, Major Raul Zubieta", "Le capitaine [[vincente-de-santa|Vincente de Santa]], le capitaine Espinoza, le major Raul Zubieta")},
        {"label": two("Under his protection", "Sous sa protection"), "value": two("[[bill-williamson|Bill Williamson]], [[javier-escuella|Javier Escuella]]", "[[bill-williamson|Bill Williamson]], [[javier-escuella|Javier Escuella]]")},
        {"label": two("Enemies", "Ennemis"), "value": two("[[abraham-reyes|Abraham Reyes]] and his rebels, [[luisa-fortuna|Luisa Fortuna]], [[john-marston|John Marston]] (after Chuparosa)", "[[abraham-reyes|Abraham Reyes]] et ses rebelles, [[luisa-fortuna|Luisa Fortuna]], [[john-marston|John Marston]] (après Chuparosa)")},
        {"label": two("Weapons", "Armes"), "value": two("Sabre, Cattleman Revolver (Red Dead Wiki); an armored stagecoach with a Gatling gun", "Sabre, Cattleman Revolver (Red Dead Wiki) ; une diligence blindée armée d'une Gatling")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption; multiplayer model (Liars and Cheats)", "Red Dead Redemption ; modèle multijoueur (Liars and Cheats)")},
        {"label": two("Voiced by", "Voix"), "value": two("Gary Carlos Cervantes", "Gary Carlos Cervantes")},
    ],
    "intro": [
        two("Colonel Agustin Allende is the governor of Nuevo Paraíso, a Mexican province, in Red Dead Redemption (2010), set in 1911. He commands the army there in the name of President Ignacio Sanchez from his mansion in Escalera, and fights the rebellion led by [[abraham-reyes|Abraham Reyes]]. [[bill-williamson|Bill Williamson]] and [[javier-escuella|Javier Escuella]] live under his protection. Through his captain, [[vincente-de-santa|Vincente de Santa]], he promises to find them for [[john-marston|John Marston]] in exchange for his help against the rebels, then has John led into a trap in Chuparosa.",
            "Le colonel Agustin Allende est le gouverneur du Nuevo Paraíso, une province mexicaine, dans Red Dead Redemption (2010), dont l'action se déroule en 1911. Depuis sa demeure d'Escalera, il commande l'armée au nom du président Ignacio Sanchez et combat la rébellion menée par [[abraham-reyes|Abraham Reyes]]. [[bill-williamson|Bill Williamson]] et [[javier-escuella|Javier Escuella]] vivent sous sa protection. Par l'intermédiaire de son capitaine, [[vincente-de-santa|Vincente de Santa]], il promet à [[john-marston|John Marston]] de les lui trouver s'il l'aide contre les rebelles, puis le fait attirer dans un piège à Chuparosa."),
        two("John then joins Reyes. When the rebels take Escalera, Allende flees by stagecoach with Bill and offers him to John to save himself; both men die on the road, shot by John or by Reyes. He is voiced by Gary Carlos Cervantes.",
            "John rejoint alors Reyes. Quand les rebelles prennent Escalera, Allende s'enfuit en diligence avec Bill et le livre à John pour sauver sa peau ; les deux hommes meurent sur la route, abattus par John ou par Reyes. Il a la voix de Gary Carlos Cervantes."),
    ],
    "essentials": [
        two("In \"The Demon Drink\", he meets John at his mansion in Escalera and sends him to fight the rebels at Tesoro Azul.",
            "Dans \"The Demon Drink\", il reçoit John dans sa demeure d'Escalera et l'envoie combattre les rebelles à Tesoro Azul."),
        two("In \"Mexican Caesar\", De Santa offers John 20,000 pesos and Javier's whereabouts, on his behalf, to escort a munitions train.",
            "Dans \"Mexican Caesar\", De Santa propose à John, en son nom, 20 000 pesos et la cachette de Javier pour escorter un train de munitions."),
        two("In \"Cowards Die Many Times\", he tells John that Bill and Javier are prisoners in Chuparosa; it is a trap, and Reyes's rebels save John.",
            "Dans \"Cowards Die Many Times\", il annonce à John que Bill et Javier sont prisonniers à Chuparosa ; c'est un piège, et les rebelles de Reyes sauvent John."),
        two("In \"An Appointed Time\", the rebels storm his mansion; he flees by stagecoach with Bill and dies on the road, shot by John or by Reyes.",
            "Dans \"An Appointed Time\", les rebelles prennent sa demeure d'assaut ; il s'enfuit en diligence avec Bill et meurt sur la route, abattu par John ou par Reyes."),
        two("The Blackwater Ledger reports his death under the headline \"'Tyrannical' Governor Overthrown\".",
            "Le Blackwater Ledger annonce sa mort sous le titre \"'Tyrannical' Governor Overthrown\" (un gouverneur \"tyrannique\" renversé)."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["abraham-reyes", "vincente-de-santa", "bill-williamson", "john-marston"],
}
