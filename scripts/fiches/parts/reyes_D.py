"""Abraham Reyes, reference fiche, PART D: base data, Development and performance, Reception
(21 Oct 2026, medium tier).

His live page (characters/abraham-reyes/) was generated from the v2 entry in scripts/_wave4.py (order 23,
"slug": "abraham-reyes"; no entry in _enrich.py). publishDate 2026-08-11 kept (git 9de7e30, drip publish of
abraham-reyes, 11 Aug 2026). Eyebrow kept as on the live page ("Character &middot; Nuevo Paraíso"); reg_role matches
characters_registry.py ("Revolutionary &middot; RDR1" / "Révolutionnaire &middot; RDR1").
Corrections to the v2 base:
- v2 "charismatic... Vain and self-serving beneath the speeches, he uses the rebellion to make himself ruler of
  Mexico" and "wins his war, then betrays it and rules as a tyrant": interpretation; replaced by the GOTY guide quote
  (part B) and by what the 1914 article reports (he DENIES being a tyrant after a massacre; the article does not say he
  ordered it).
- v2 "installs himself as President of Mexico in November 1911": the month is a Red Dead Wiki deduction from issue
  numbers, not a dated source. Dropped from the base; the 1911 takeover is told (attributed) in part A.
- v2 "delays elections, and is accused of massacring peaceful protesters": the article says the path to democratic rule
  has been slower than he would have liked, and that troops shot thousands of peaceful protesters "last month"; reworded.
- v2 "Born c. 1881" as a bare fact: attributed (GOTY guide quoted by the Red Dead Wiki: 30 years old; the wiki's
  "circa 1881" is footnoted to that guide).
- v2 "Reyes later returns the favour, sniping the executioner" and "the player chooses which man John kills, and Reyes
  shoots the other": narrative now in part A, worded as HOUSE_FACTS ("shot by John or by Reyes").
- v2 "Reyes speaks admiringly of Dutch": kept as a paraphrase of the transcript (part B), without the wiki's "would have
  liked to meet him" (not in the transcript).
- v2 "modelled largely on the real revolutionary Francisco Madero" and "The march on Escalera mirrors the real 1911
  Battle of Ciudad Juárez": Red Dead Wiki speculation, no Rockstar source. Dropped.
- v2 "His surname... a pointed nod to his ambitions": interpretation; the meaning of the word is in part B (Names).
- v2 "Red Dead Redemption (2010) and its 2024 remaster": dropped (the 2023 and 2024 releases are ports).
- v2 "Games: Red Dead Redemption": Undead Nightmare and the Liars and Cheats multiplayer model added.
- v2 related ccards (Ricketts, John, Dutch, Bill) replaced by the characters he deals with most (Luisa, Allende,
  De Santa, John), all live since October 2026.

SOURCE REGISTER (read 21 Oct 2026):
- Wikipedia "Josh Segarra" (reyes/fc/wp_josh_segarra.txt, raw wikitext): born June 3, 1986 in Longwood, Florida;
  Puerto Rican descent; NYU Tisch School of the Arts; Hector Ruiz in The Electric Company (2009-2011); Adrian Chase in
  Arrow (season 5, 2016-2017); originated Emilio Estefan in On Your Feet! on Broadway (opened November 5, 2015); She-Hulk:
  Attorney at Law (2022); Scream VI (2023); video games: Red Dead Redemption and Undead Nightmare (2010), Abraham Reyes.
  Red Dead Wiki "Josh Segarra" (_m/Josh_Segarra.txt) agrees on the role.
- Wikipedia "Red Dead Redemption" (landon/fc/wp_rdr.txt): "Abraham Reyes (Josh Segarra), the leader of a rebellion
  against Allende's government".
- Red Dead Wiki "Abraham Reyes" (trivia: neater hair and goatee in pre-release screenshots; gallery captions "Pre-release
  screenshot"); "Red Dead Redemption Cut Content" (_m/: unused bounty poster of Reyes with an unused goatee).
- Newspapers (wiki text): "Another Civil War in Mexico?" (Blackwater Ledger No. 56), "President Reyes Denies He is a
  Tyrant, Despite Massacre" (Blackwater Ledger No. 213). Used here for the base only; told in part A.
- Reception (reyes/fc/web_notes_BD.txt): Game Informer, Matt Bertz, review, May 17, 2010 (WebFetch; Reyes not named);
  Sportskeeda, Aniket Mukherjee, "10 best characters in the Red Dead Redemption franchise", August 13, 2023
  (landon/fc/sportskeeda_2023-08-13.txt: Reyes 10th); Javier Aldape (Texas A&M University), "The Mustang Diaries: A Study
  of Mexico in Red Dead Redemption 1", Revista Panamericana de Comunicación, vol. 4, no. 2, published October 21, 2022
  (Redalyc page; SciELO Mexico indexing April 2023, WebFetch).
- Checked, nothing on Reyes: AP profile of Segarra (Alicia Rancilio, March 29, 2023, via Stars and Stripes); Remezcla
  interview with Segarra (no Red Dead mention). No interview in which Segarra speaks of the role was found.

Excluded: motion capture for Reyes (no source names a performer); a different voice for Reyes in the early trailers
(stated in john_E.py, but its source was not found in the cache: John's wiki page has no such line today; left out
here, to be checked); Segarra's Grand Theft Auto V credit ("The Local Population", Wikipedia table) as irrelevant; the
Aldape article's claim that Rockstar hired historians (no source cited by the author); the Madero, Villa, Zapata,
Carranza and Bernardo Reyes models (wiki speculation); the Liars and Cheats model, its release date and the multiplayer
lines (part C, Other media and Quotes).
DUPLICATE ownership: the actor, the pre-release look and the cut bounty poster live HERE; part C (Trivia, Other media)
must not repeat them. The Bertz review is the only place that quotes the "upstart rebel" line.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Abraham Reyes appears in Red Dead Redemption and its expansion Undead Nightmare, both released in 2010. Wikipedia credits Josh Segarra with the role, in its article on the game and in his own article. Segarra is an American actor of Puerto Rican descent, born on June 3, 1986 in Longwood, Florida, and a graduate of New York University's Tisch School of the Arts. At the time of Red Dead Redemption he played Hector Ruiz in the PBS children's series The Electric Company (2009 to 2011). He later created the role of Emilio Estefan in the Broadway musical On Your Feet!, which opened on November 5, 2015, played Adrian Chase in the fifth season of Arrow (2016 to 2017), and appeared in She-Hulk: Attorney at Law (2022) and Scream VI (2023). No interview in which he discusses the role was found, and no source consulted names a performer for Reyes's motion capture.",
              "Abraham Reyes apparaît dans Red Dead Redemption et dans son extension Undead Nightmare, sortis tous deux en 2010. Wikipédia attribue le rôle à Josh Segarra, dans son article sur le jeu comme dans celui consacré à l'acteur. Né le 3 juin 1986 à Longwood, en Floride, Segarra est un acteur américain d'origine portoricaine, diplômé de la Tisch School of the Arts de l'université de New York. À l'époque de Red Dead Redemption, il tient le rôle d'Hector Ruiz dans la série jeunesse The Electric Company, diffusée sur PBS de 2009 à 2011. Il crée ensuite le rôle d'Emilio Estefan dans la comédie musicale On Your Feet!, lancée à Broadway le 5 novembre 2015, incarne Adrian Chase dans la cinquième saison d'Arrow (2016-2017), et joue dans She-Hulk : Avocate (2022) et Scream VI (2023). Aucune interview dans laquelle il évoque ce rôle n'a été trouvée, et aucune des sources consultées ne nomme d'interprète pour la capture de mouvement de Reyes.")},
    {"h3": two("Before release", "Avant la sortie")},
    {"p": two("In the screenshots Rockstar released before launch, his hair and goatee are shorter than in the released game, according to the Red Dead Wiki. The wiki's page on the game's cut content adds that an unused bounty poster of Reyes was left in the game files, with a goatee model that is not used in the final game.",
              "Sur les captures d'écran diffusées par Rockstar avant la sortie, ses cheveux et son bouc sont plus courts que dans le jeu commercialisé, relève le Red Dead Wiki. La page du wiki consacrée au contenu coupé du jeu ajoute qu'un avis de recherche inutilisé à son nom est resté dans les fichiers du jeu, avec un modèle de bouc absent de la version finale.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Reviews", "Critiques")},
    {"p": two("Game Informer's review of Red Dead Redemption, written by Matt Bertz and published on May 17, 2010, gave the game 9.75 out of 10. Bertz does not name Reyes, but describes the Mexican part of the story as John having to \"get cozy with both the corrupt ruler of the border region and the upstart rebel hell-bent on taking power for himself.\" He judged that this \"tangential plot drags on far too long without engaging the task at hand, and the game's momentum suffers for it.\"",
              "La critique de Red Dead Redemption publiée par Game Informer le 17 mai 2010, signée Matt Bertz, attribue au jeu la note de 9,75 sur 10. Sans nommer Reyes, Bertz résume la partie mexicaine de l'histoire : John doit \"get cozy with both the corrupt ruler of the border region and the upstart rebel hell-bent on taking power for himself.\" (se mettre bien à la fois avec le dirigeant corrompu de la région frontalière et avec le rebelle parvenu décidé à prendre le pouvoir pour lui-même). Il juge que cette \"tangential plot drags on far too long without engaging the task at hand, and the game's momentum suffers for it.\" (intrigue secondaire traîne beaucoup trop en longueur sans faire avancer la mission principale, et le rythme du jeu en pâtit).")},
    {"h3": two("Character lists", "Classements de personnages")},
    {"p": two("In a list of the ten best characters of the Red Dead Redemption franchise, published by Sportskeeda and last updated on August 13, 2023, Aniket Mukherjee ranked Reyes tenth, just behind Irish (ninth). He wrote that Reyes \"is ranked 10th because of his significant contribution to the Mexican revolution, which adds depth to the Red Dead Redemption's narrative by introducing political intrigue.\"",
              "Dans une liste des dix meilleurs personnages de la série Red Dead Redemption publiée par Sportskeeda, mise à jour pour la dernière fois le 13 août 2023, Aniket Mukherjee classe Reyes dixième, juste derrière Irish (neuvième). Il explique que Reyes \"is ranked 10th because of his significant contribution to the Mexican revolution, which adds depth to the Red Dead Redemption's narrative by introducing political intrigue.\" (doit sa dixième place à son rôle important dans la révolution mexicaine, qui enrichit le récit de Red Dead Redemption d'une intrigue politique).")},
    {"h3": two("Academic study", "Étude universitaire")},
    {"p": two("In \"The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1\", published in the Revista Panamericana de Comunicación (vol. 4, no. 2, published on October 21, 2022), Javier Aldape, of Texas A&M University, reads Allende and Reyes as the two sides of the caudillo figure. He calls Reyes \"The revolutionary Messiah who will restore peace to Mexico\" and writes: \"He womanizes and makes the same promise to all of them, which he never keeps.\" He also notes that Reyes is \"more concerned about corridos of him than the heroic deeds of the soldaderas\", the women who fought in the revolution.",
              "Dans \"The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1\", article paru dans la Revista Panamericana de Comunicación (vol. 4, n° 2, paru le 21 octobre 2022), Javier Aldape, de l'université Texas A&M, voit en Allende et Reyes les deux faces de la figure du caudillo. Il qualifie Reyes de \"revolutionary Messiah who will restore peace to Mexico\" (messie révolutionnaire qui ramènera la paix au Mexique) et écrit : \"He womanizes and makes the same promise to all of them, which he never keeps.\" (il collectionne les femmes et leur fait à toutes la même promesse, qu'il ne tient jamais). Il relève aussi que Reyes se soucie davantage des corridos à sa gloire que des exploits des soldaderas, les femmes qui ont combattu pendant la révolution.")},
]


BASE = {
    "slug": "abraham-reyes", "name": "Abraham Reyes",
    "publishDate": "2026-08-11", "updated": "2026-10-21", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Revolutionary &middot; RDR1", "reg_role_fr": "Révolutionnaire &middot; RDR1",
    "gender": "Male", "birth": None, "death": None, "nationality": "Mexican",
    "portrait_alt": two("Abraham Reyes in Red Dead Redemption", "Abraham Reyes dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; Nuevo Paraíso", "Personnage &middot; Nuevo Paraíso"),
    "meta_desc": two("Abraham Reyes, rebel leader of Nuevo Paraíso in Red Dead Redemption: El Presidio, Chuparosa, the train robbery, Escalera, President of Mexico in 1914, Josh Segarra.",
                     "Abraham Reyes, chef des rebelles du Nuevo Paraíso dans Red Dead Redemption : El Presidio, Chuparosa, l'attaque du train, Escalera, président du Mexique en 1914, Josh Segarra."),
    "og_desc": two("The complete reference on Abraham Reyes: life, missions, quotes, development and reception.",
                   "La référence complète sur Abraham Reyes : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Leader of the rebels of Nuevo Paraíso, Mexico, who in 1911 allies with John Marston against Colonel Allende in Red Dead Redemption, and is President of Mexico by 1914.",
                       "Chef des rebelles du Nuevo Paraíso, au Mexique, qui s'allie en 1911 à John Marston contre le colonel Allende dans Red Dead Redemption, et qui est président du Mexique en 1914."),
    "chips": [two("Rebel leader", "Chef rebelle"), two("Nuevo Paraíso", "Nuevo Paraíso"),
              two("President of Mexico in <strong>1914</strong>", "Président du Mexique en <strong>1914</strong>"),
              two("Voiced by <strong>Josh Segarra</strong>", "Voix : <strong>Josh Segarra</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Abraham Reyes", "Abraham Reyes")},
        {"label": two("Born", "Naissance"), "value": two("Date not given in the games; the Game of the Year Edition guide, quoted by the Red Dead Wiki, describes him as 30 years old (born around 1881, according to the wiki). Birthplace: a ranch outside the capital (Blackwater Ledger)", "Date non précisée dans les jeux ; le guide de l'édition Game of the Year, cité par le Red Dead Wiki, lui donne 30 ans (né vers 1881, selon le wiki). Lieu : un ranch aux abords de la capitale (Blackwater Ledger)")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1914, President of Mexico (Blackwater Ledger & Sentinel); killed as an undead in Undead Nightmare (non-canon)", "Vivant en 1914, président du Mexique (Blackwater Ledger & Sentinel) ; abattu en mort-vivant dans Undead Nightmare (hors canon)")},
        {"label": two("Nationality", "Nationalité"), "value": two("Mexican", "Mexicaine")},
        {"label": two("Occupation", "Activité"), "value": two("Leader of Reyes' Rebels in Nuevo Paraíso (1911); President of Mexico from 1911 (Blackwater Ledger No. 60), still in office in 1914 (Blackwater Ledger & Sentinel)", "Chef des rebelles de Reyes au Nuevo Paraíso (1911) ; président du Mexique à partir de 1911 (Blackwater Ledger n° 60), toujours en fonctions en 1914 (Blackwater Ledger & Sentinel)")},
        {"label": two("Base", "Base"), "value": two("His ranch at Agave Viejo, Perdido, Nuevo Paraíso", "Son ranch d'Agave Viejo, Perdido, Nuevo Paraíso")},
        {"label": two("Family", "Famille"), "value": two("A nobleman father (Blackwater Ledger); his mother, dead", "Un père aristocrate (Blackwater Ledger) ; sa mère, décédée")},
        {"label": two("Allies", "Alliés"), "value": two("[[john-marston|John Marston]], [[luisa-fortuna|Luisa Fortuna]]", "[[john-marston|John Marston]], [[luisa-fortuna|Luisa Fortuna]]")},
        {"label": two("Enemies", "Ennemis"), "value": two("[[agustin-allende|Agustin Allende]], [[vincente-de-santa|Vincente de Santa]], President Ignacio Sanchez", "[[agustin-allende|Agustin Allende]], [[vincente-de-santa|Vincente de Santa]], le président Ignacio Sanchez")},
        {"label": two("Weapons", "Armes"), "value": two("Winchester Repeater, Schofield Revolver, Rolling Block Rifle, Hunting Knife (Red Dead Wiki)", "Winchester Repeater, Schofield Revolver, Rolling Block Rifle, couteau de chasse (Red Dead Wiki)")},
        {"label": two("Horse", "Cheval"), "value": two("Cleveland Bay (Red Dead Wiki)", "Cleveland Bay (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption, Undead Nightmare; multiplayer model (Liars and Cheats)", "Red Dead Redemption, Undead Nightmare ; modèle multijoueur (Liars and Cheats)")},
        {"label": two("Voiced by", "Voix"), "value": two("Josh Segarra", "Josh Segarra")},
    ],
    "intro": [
        two("Abraham Reyes is the leader of the rebels of Nuevo Paraíso, in Mexico, in Red Dead Redemption (2010), set in 1911. The son of a nobleman, he leads a revolt against the province's governor, Colonel [[agustin-allende|Agustin Allende]], and the government of President Ignacio Sanchez. [[john-marston|John Marston]] frees him from a firing squad at El Presidio after [[luisa-fortuna|Luisa Fortuna]] tells him of his capture, and Reyes's rebels save John from his own execution in Chuparosa. In exchange for John's help, Reyes's spies track down [[javier-escuella|Javier Escuella]], and the rebels take El Presidio, then Escalera; Allende and [[bill-williamson|Bill Williamson]], fleeing by stagecoach, die on the road, shot by John or by Reyes.",
            "Abraham Reyes est le chef des rebelles du Nuevo Paraíso, au Mexique, dans Red Dead Redemption (2010), dont l'action se déroule en 1911. Fils d'aristocrate, il mène la révolte contre le gouverneur de la province, le colonel [[agustin-allende|Agustin Allende]], et contre le gouvernement du président Ignacio Sanchez. [[john-marston|John Marston]] le tire des mains d'un peloton d'exécution à El Presidio après que [[luisa-fortuna|Luisa Fortuna]] lui a appris sa capture, et les rebelles de Reyes sauvent à leur tour John de son exécution à Chuparosa. En échange de l'aide de John, les espions de Reyes retrouvent [[javier-escuella|Javier Escuella]], et les rebelles prennent El Presidio, puis Escalera ; Allende et [[bill-williamson|Bill Williamson]], en fuite dans une diligence, meurent sur la route, abattus par John ou par Reyes."),
        two("In 1914, the last newspaper of the game, the Blackwater Ledger & Sentinel, reports that President Reyes denies being a tyrant after troops shot thousands of peaceful protesters south of Mexico City. He is voiced by Josh Segarra. He also appears in the non-canon expansion Undead Nightmare, as the undead source of the plague, whom John kills in the second-to-last mission.",
            "En 1914, le dernier journal du jeu, le Blackwater Ledger & Sentinel, rapporte que le président Reyes nie être un tyran, après que des soldats ont abattu des milliers de manifestants pacifiques au sud de Mexico. Il a la voix de Josh Segarra. On le retrouve aussi dans Undead Nightmare, une extension hors canon : devenu mort-vivant, il est à l'origine de l'épidémie, et John l'abat dans l'avant-dernière mission."),
    ],
    "essentials": [
        two("In \"Must a Savior Die?\", John shoots his executioner at El Presidio and rides him to Luisa.",
            "Dans \"Must a Savior Die?\", John abat son bourreau à El Presidio et le ramène à cheval auprès de Luisa."),
        two("In \"Cowards Die Many Times\", Reyes and his rebels save John from execution in Chuparosa, where De Santa has betrayed him.",
            "Dans \"Cowards Die Many Times\", Reyes et ses rebelles sauvent John de l'exécution à Chuparosa, où De Santa l'a trahi."),
        two("In \"The Great Mexican Train Robbery\", he and John rob an army supply train in Chuparosa.",
            "Dans \"The Great Mexican Train Robbery\", John et lui attaquent un train de ravitaillement de l'armée à Chuparosa."),
        two("In \"The Gates of El Presidio\", his rebels storm the fort so that John can reach Javier Escuella.",
            "Dans \"The Gates of El Presidio\", ses rebelles prennent le fort d'assaut pour que John puisse atteindre Javier Escuella."),
        two("In \"An Appointed Time\", the rebels take Escalera; Luisa is killed trying to save him, and Allende and Bill die on the road.",
            "Dans \"An Appointed Time\", les rebelles prennent Escalera ; Luisa est tuée en tentant de le sauver, et Allende et Bill meurent sur la route."),
        two("In 1914, the Blackwater Ledger & Sentinel calls him President Reyes.",
            "En 1914, le Blackwater Ledger & Sentinel l'appelle President Reyes."),
        two("In Undead Nightmare, which is not canon, John kills him as an undead in \"A Civilized Man\".",
            "Dans Undead Nightmare, qui n'appartient pas au canon, John l'abat en mort-vivant dans \"A Civilized Man\"."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["luisa-fortuna", "agustin-allende", "vincente-de-santa", "john-marston"],
}
