"""Seth Briars, reference fiche, PART D: base data, Development and performance, Reception
(21 Oct 2026, medium tier).

His live page (characters/seth-briars/) was generated from the v2 entry in scripts/_wave4.py (order 21,
"slug": "seth-briars"; no entry in _enrich.py). publishDate 2026-08-05 kept (git 3066799, drip publish of
seth-briars, 5 Aug 2026). Eyebrow kept as on the live page ("Character &middot; New Austin"); reg_role matches
characters_registry.py ("Grave-robber &middot; RDR1" / "Pilleur de tombes &middot; RDR1").
Corrections to the v2 base:
- v2 "Born: Early 1870s" as a fact: no birth date is given in the game. The GOTY Edition guide, quoted by the Red
  Dead Wiki, puts him in his late thirties; the wiki's "early 1870s" is derived from it. Both attributed.
- v2 "An 1914 newspaper reports that he hauled a sack of real gold and jewels... at last striking the fortune his
  obsession promised": the article ("Treasure Found", Blackwater Ledger & Sentinel No. 213, read on the page image,
  seth/fc/Treasure_Found_1914.txt) says he "walked out of the mountains in Tall Trees and into Blackwater with a
  massive haul of gold and precious stones"; no "sack", no "jewels"; mood clause dropped. It says NOTHING about his
  family: the wiki "Newspapers" page, the FR wiki and Gameranx (2016), which say he returned to his family and opened
  a business in Blackwater, are wrong.
- v2 "Red Dead Redemption (2010) and its 2024 remaster": dropped (the 2023 console and 2024 PC releases are ports).
- v2 "deranged", "unhinged", "unstable", "visibly unwell", "split-personality behaviour... suggest serious mental
  illness": interpretation; replaced by the GOTY guide quote (part B) and by facts.
- v2 "escort a wagon of exhumed corpses to Tumbleweed to find the map's other half": the corpses come from Odd
  Fellow's Rest and are searched on the way; the piece is found during the drive (transcript).
- v2 "In-game newspapers wrongly credit Moses Forth for the grave-robbings": the 1911 article (Blackwater Ledger No. 53,
  "Grave Robber Captured, But Crimes Persist") names only Moses and notes that desecrations continue after his
  arrest; it does not name Seth. Left to parts A/C, not in the base.
- v2 "Rob Wiethoff has named Seth his favourite character": the only source is a Red Dead Wiki footnote to a 2021
  YouTube interview whose content could not be checked; attributed to the wiki (Reception).
- v2 "Games: Red Dead Redemption": Undead Nightmare added, plus the unused Red Dead Online model.

SOURCE REGISTER (read 21 Oct 2026):
- Wikipedia "Red Dead Redemption" (landon/fc/wp_rdr.txt): "grave robber and treasure hunter Seth Briars (Kevin
  Glikmann)". Wikipedia "Red Dead Redemption: Undead Nightmare" (landon/fc/wp_un.txt): "treasure hunter Seth Briars
  (Kevin Glikmann)".
- Red Dead Wiki "Kevin Glikmann" (_m/Kevin_Glikmann.txt): American actor; Changeling, Hot Tamale, Splinter Cell:
  Double Agent (attributed). IMDb returned 403: not used.
- PCGamesN, Iain Harris, "Red Dead Redemption's creepiest NPC has popped up in Red Dead Online's files", 17 Aug 2020
  (WebFetch, seth/fc/web_notes_BD.txt): dataminer VideoTech; model added with the first update in 2018; 41 finished
  lines of dialogue, one referring to a mission. Red Dead Wiki trivia: the model shares a slightly altered face with
  John Marston (attributed).
- Newspaper "Treasure Found" (Blackwater Ledger & Sentinel No. 213, 1914), page image read directly.
- Reception: Gameranx, Dennis Patrick, "Characters We Wouldn't Mind Seeing Again In Red Dead Redemption 2", 4 Nov 2016
  (WebFetch); Sportskeeda, Aniket Mukherjee, "10 best characters in the Red Dead Redemption franchise", page modified
  13 Aug 2023 (landon/fc/sportskeeda_2023-08-13.txt: Seth 8th, Irish 9th, Leigh Johnson 7th); Dan Allen Gaming
  (YouTube), "John Marston Actor Rob Wiethoff on how Red Dead Redemption changed his life!", 27 Mar 2021 (metadata
  only; cited by the Red Dead Wiki).

Excluded: motion capture for Seth (no source names a performer; a search-engine summary claiming Glikmann did it and
"reprised the role in 2025" has no source and was dropped); Glikmann's other credits beyond the Red Dead Wiki list
(IMDb unreadable); the GamePro.de article on Seth's absence from RDR2 (403, not read); The Man from Blackwater (2010
machinima) and the Liars and Cheats multiplayer model, left to part C (Other media); the Gameranx claim that he
reunites his family and opens a business in Blackwater (contradicted by the newspaper).
DUPLICATE ownership: the actor, the Red Dead Online cut model and Wiethoff's reported preference live HERE; part C
(Trivia, Other media) must not repeat them.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Seth Briars appears in Red Dead Redemption and its expansion Undead Nightmare, both released in 2010. Wikipedia credits Kevin Glikmann with the role in both games. According to the Red Dead Wiki, Glikmann is an American actor whose other credits include the film Changeling, the film Hot Tamale and the video game Splinter Cell: Double Agent. No source consulted names a performer for Seth's motion capture.",
              "Seth Briars apparaît dans Red Dead Redemption et dans son extension Undead Nightmare, sortis tous deux en 2010. Wikipédia attribue le rôle à Kevin Glikmann dans les deux jeux. D'après le Red Dead Wiki, Glikmann est un acteur américain dont la filmographie compte aussi les films L'Échange (Changeling) et Hot Tamale, ainsi que le jeu vidéo Splinter Cell: Double Agent. Aucune des sources consultées ne nomme d'interprète pour la capture de mouvement de Seth.")},
    {"h3": two("Unused Red Dead Online model", "Le modèle inutilisé de Red Dead Online")},
    {"p": two("Seth does not appear in Red Dead Redemption 2. On August 17, 2020, PCGamesN (Iain Harris) reported that the dataminer VideoTech had found him in the files of Red Dead Online, where he was added with the game's first update in 2018. According to the report, the character has 41 finished lines of dialogue, one of which refers to a mission, and he was either cut or kept for later use. According to the Red Dead Wiki, the unused model shares a slightly altered version of John Marston's face.",
              "Seth n'apparaît pas dans Red Dead Redemption 2. Le 17 août 2020, PCGamesN (Iain Harris) rapporte que le dataminer VideoTech l'a découvert dans les fichiers de Red Dead Online, où il avait été ajouté avec la première mise à jour du jeu, en 2018. Selon l'article, le personnage dispose de 41 répliques entièrement enregistrées, dont l'une évoque une mission, et il a soit été abandonné, soit mis de côté pour plus tard. D'après le Red Dead Wiki, ce modèle inutilisé reprend, légèrement modifié, le visage de John Marston.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Character lists", "Classements de personnages")},
    {"p": two("On November 4, 2016, Dennis Patrick of Gameranx included Seth among the characters he wanted to see again in Red Dead Redemption 2: \"Everyone remembers Seth Briars, you might not remember the name, but you can't forget the crazy lunatic speaking to the dead and hunting for unimaginable wealth.\" In a list of the ten best characters of the Red Dead Redemption franchise, published by Sportskeeda (page last modified on August 13, 2023), Aniket Mukherjee ranked him eighth, between Irish (ninth) and Leigh Johnson (seventh), citing \"his quirky personality and unwavering determination to discover hidden treasures\".",
              "Le 4 novembre 2016, Dennis Patrick, de Gameranx, cite Seth parmi les personnages qu'il aimerait revoir dans Red Dead Redemption 2 : \"Everyone remembers Seth Briars, you might not remember the name, but you can't forget the crazy lunatic speaking to the dead and hunting for unimaginable wealth.\" (tout le monde se souvient de Seth Briars ; on a peut-être oublié son nom, mais pas ce fou furieux qui parle aux morts et court après des richesses inimaginables). Dans une liste des dix meilleurs personnages de la série Red Dead Redemption publiée par Sportskeeda (page modifiée pour la dernière fois le 13 août 2023), Aniket Mukherjee le classe huitième, entre Irish (neuvième) et Leigh Johnson (septième), en saluant \"his quirky personality and unwavering determination to discover hidden treasures\" (sa personnalité excentrique et sa détermination sans faille à dénicher des trésors).")},
    {"h3": two("Rob Wiethoff", "Rob Wiethoff")},
    {"p": two("According to the Red Dead Wiki, Rob Wiethoff, who plays John Marston, named Seth as his favorite character in Red Dead Redemption. The wiki cites an interview with the YouTube channel Dan Allen Gaming, published on March 27, 2021.",
              "D'après le Red Dead Wiki, Rob Wiethoff, l'interprète de John Marston, a désigné Seth comme son personnage préféré de Red Dead Redemption. Le wiki renvoie à un entretien accordé à la chaîne YouTube Dan Allen Gaming, mis en ligne le 27 mars 2021.")},
]


BASE = {
    "slug": "seth-briars", "name": "Seth Briars",
    "publishDate": "2026-08-05", "updated": "2026-10-21", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Grave-robber &middot; RDR1", "reg_role_fr": "Pilleur de tombes &middot; RDR1",
    "gender": "Male", "birth": None, "death": None, "nationality": "American",
    "portrait_alt": two("Seth Briars in Red Dead Redemption", "Seth Briars dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; New Austin", "Personnage &middot; New Austin"),
    "meta_desc": two("Seth Briars, the grave robber of Red Dead Redemption: the stolen map, Moses Forth, the glass eye of Tumbleweed, Fort Mercer, the 1914 treasure, Kevin Glikmann.",
                     "Seth Briars, le pilleur de tombes de Red Dead Redemption : la carte volée, Moses Forth, l'œil de verre de Tumbleweed, Fort Mercer, le trésor de 1914, Kevin Glikmann."),
    "og_desc": two("The complete reference on Seth Briars: life, missions, quotes, development and reception.",
                   "La référence complète sur Seth Briars : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Grave robber and treasure hunter in New Austin who, in 1911, helps John Marston get inside Fort Mercer once John has helped him search for the missing half of a treasure map, in Red Dead Redemption.",
                       "Pilleur de tombes et chasseur de trésor du New Austin qui, en 1911, aide John Marston à entrer dans Fort Mercer après que John l'a aidé à chercher la moitié manquante d'une carte au trésor, dans Red Dead Redemption."),
    "chips": [two("Grave robber", "Pilleur de tombes"), two("New Austin", "New Austin"),
              two("Alive in <strong>1914</strong>", "Vivant en <strong>1914</strong>"),
              two("Voiced by <strong>Kevin Glikmann</strong>", "Voix : <strong>Kevin Glikmann</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Seth Briars (surname printed only in the 1914 newspaper)", "Seth Briars (nom de famille imprimé seulement dans le journal de 1914)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game; in his late thirties in 1911 according to the Game of the Year Edition guide, quoted by the Red Dead Wiki (early 1870s)", "Non précisée dans le jeu ; la fin de la trentaine en 1911 selon le guide de l'édition Game of the Year, cité par le Red Dead Wiki (début des années 1870)")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1914 (Blackwater Ledger & Sentinel)", "Vivant en 1914 (Blackwater Ledger & Sentinel)")},
        {"label": two("Nationality", "Nationalité"), "value": two("American (Game of the Year Edition guide)", "Américaine (guide de l'édition Game of the Year)")},
        {"label": two("Residence", "Résidence"), "value": two("No fixed home in New Austin in 1911, according to the Red Dead Wiki; The Old Bacchus Place in Undead Nightmare", "Sans domicile fixe au New Austin en 1911, selon le Red Dead Wiki ; The Old Bacchus Place dans Undead Nightmare")},
        {"label": two("Occupation", "Activité"), "value": two("Grave robber and treasure hunter; formerly ran a business, by his own account", "Pilleur de tombes et chasseur de trésor ; à l'en croire, il a eu autrefois une affaire")},
        {"label": two("Family", "Famille"), "value": two("A wife and children he says he has lost; his mother is dead", "Une femme et des enfants qu'il dit avoir perdus ; sa mère est morte")},
        {"label": two("Former partners", "Anciens associés"), "value": two("Moses Forth, Aiden O'Leary", "Moses Forth, Aiden O'Leary")},
        {"label": two("Allies", "Alliés"), "value": two("[[john-marston|John Marston]], [[nigel-west-dickens|Nigel West Dickens]]", "[[john-marston|John Marston]], [[nigel-west-dickens|Nigel West Dickens]]")},
        {"label": two("Weapons", "Armes"), "value": two("Knife; Cattleman Revolver and Repeater Carbine (Red Dead Wiki)", "Couteau ; Cattleman Revolver et Repeater Carbine (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption, Undead Nightmare; unused model in Red Dead Online", "Red Dead Redemption, Undead Nightmare ; modèle inutilisé dans Red Dead Online")},
        {"label": two("Voiced by", "Voix"), "value": two("Kevin Glikmann", "Kevin Glikmann")},
    ],
    "intro": [
        two("Seth Briars is a grave robber and treasure hunter in Red Dead Redemption (2010), set in 1911. [[nigel-west-dickens|Nigel West Dickens]] sends [[john-marston|John Marston]] to him for a way into Fort Mercer, the hideout of [[bill-williamson|Bill Williamson]]'s gang. Seth agrees to help once he has his treasure map. John helps him force his former partner Moses Forth to talk, then drives a wagon of corpses to Tumbleweed while Seth searches them for the missing piece. In the Tumbleweed mansion, the treasure chest holds only a glass eye. Seth keeps his word and is inside Fort Mercer when the assault begins.",
            "Seth Briars est un pilleur de tombes et chasseur de trésor de Red Dead Redemption (2010), dont l'action se déroule en 1911. [[nigel-west-dickens|Nigel West Dickens]] envoie [[john-marston|John Marston]] le trouver pour entrer dans Fort Mercer, repaire de la bande de [[bill-williamson|Bill Williamson]]. Seth accepte d'aider, mais seulement une fois sa carte au trésor complète. John l'aide à faire parler son ancien associé, Moses Forth, puis conduit jusqu'à Tumbleweed un chariot de cadavres que Seth fouille en route pour trouver le morceau manquant. Dans le manoir de Tumbleweed, le coffre ne contient qu'un œil de verre. Seth tient parole : il est dans Fort Mercer quand l'assaut commence."),
        two("In 1914, the last newspaper of the game reports that he walked into Blackwater with a large haul of gold and precious stones found in the mountains of Tall Trees. He is voiced by Kevin Glikmann and also appears in Undead Nightmare.",
            "En 1914, le dernier journal du jeu rapporte qu'il est arrivé à Blackwater avec un énorme butin d'or et de pierres précieuses trouvé dans les montagnes de Tall Trees. Il a la voix de Kevin Glikmann et apparaît aussi dans Undead Nightmare."),
    ],
    "essentials": [
        two("In \"Exhuming and Other Fine Hobbies\", John finds him robbing graves at Coot's Chapel; Seth names his price for helping with Fort Mercer: the missing half of his treasure map.",
            "Dans \"Exhuming and Other Fine Hobbies\", John le trouve en train de piller des tombes à Coot's Chapel ; Seth fixe son prix pour l'aider contre Fort Mercer : la moitié manquante de sa carte au trésor."),
        two("At Benedict Point, he threatens his former partner Moses Forth with a knife until Moses names Odd Fellow's Rest.",
            "À Benedict Point, il menace au couteau son ancien associé, Moses Forth, jusqu'à ce que celui-ci lâche le nom d'Odd Fellow's Rest."),
        two("In \"A Gentle Drive with Friends\", he finds the missing piece on a corpse in the wagon; in \"Let the Dead Bury Their Dead\", the chest it leads to holds a glass eye.",
            "Dans \"A Gentle Drive with Friends\", il trouve le morceau manquant sur un cadavre du chariot ; dans \"Let the Dead Bury Their Dead\", le coffre auquel il mène contient un œil de verre."),
        two("In \"The Assault on Fort Mercer\", he is already inside the fort and lets Dickens's wagon through the gate.",
            "Dans \"The Assault on Fort Mercer\", il est déjà dans le fort et fait entrer le chariot de Dickens."),
        two("In 1914, the Blackwater Ledger & Sentinel reports his return from Tall Trees with gold and precious stones.",
            "En 1914, le Blackwater Ledger & Sentinel annonce son retour de Tall Trees avec de l'or et des pierres précieuses."),
        two("In Undead Nightmare, which is not canon, he sends John to clear three cemeteries and later steals the mask that ended the plague.",
            "Dans Undead Nightmare, qui n'appartient pas au canon, il envoie John nettoyer trois cimetières, puis vole le masque qui avait mis fin à l'épidémie."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["john-marston", "nigel-west-dickens", "irish", "bill-williamson"],
}
