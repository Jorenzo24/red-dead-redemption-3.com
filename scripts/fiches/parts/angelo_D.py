"""Angelo Bronte, reference fiche, PART D: base data, Development and performance, Reception
(20 Oct 2026, medium tier).

His live page (characters/angelo-bronte/) was generated from the v2 entry in scripts/_wave3.py
("slug": "angelo-bronte"; no entry in _enrich.py). The base below is rebuilt from that entry, with
corrections: the v2 intro called him a gangster "who styles himself a man of honour" and "first a reluctant ally"
(interpretation: the "man of honor" is the mission title, not a line of his), said he "buys" Jack (the game says
the Braithwaite sons handed the boy over to him; Arthur's guess that it was for money is in part A), and the v2
"Death and fate" text called the murder "one of the clearest early signs of Dutch's growing instability"
(analysis, dropped); "Charming, theatrical and cruel" (v2 Personality) is dropped. The "Deceased" chip duplicated
"Died 1899" and is dropped; the facts grid gains Name, Aliases, Born, Residence, Occupation, Affiliations, Weapon and
Played by. Eyebrow (kicker) kept as on the live page ("Character &middot; Saint Denis"); reg_role matches
characters_registry.py ("Crime lord &middot; RDR2"). publishDate 2026-07-09 kept (git: 3f81072, drip publish of
angelo-bronte, 9 Jul 2026; the live byline shows an older generator date).

Sources (internal register, fetched 20 Oct 2026, saved in scratchpad cov/angelo/fc/ and fcb/):
- Wikipedia "Jim Pirri" (fc/wp_pirri.txt): American actor and fight choreographer, born 4 September 1964 in
  Lakewood, Colorado; son of a linguist, grew up in Italy and speaks Italian (citing his agency, SBV Talent); best
  known for Angelo Bronte, Luca Cocchiola (Battlefield 1), Rais (Dying Light), Boozer (Days Gone) and Kraven the
  Hunter (Marvel's Spider-Man 2); David Vega in Victorious. The Red Dead Wiki "Jim Pirri" stub gives 1967 as birth
  year (conflict: no birth year used) and calls him the voice and motion-capture actor of Bronte.
- Wikipedia "List of Red Dead Redemption 2 characters", Bronte section (m/wp_List_of_Red_Dead_Redemption_2_characters.txt):
  credits Pirri; Davis's remarks on the casting (Shacknews) and on Bronte as the man Dutch wanted to be (Fan Expo
  Canada cast panel, Toronto, 24 Aug 2019, YouTube; not watched: given as Wikipedia's summary, attributed); Davis on
  Dutch turning villain when faced with powerful figures such as Catherine Braithwaite and Bronte (Twinfinite, Ed
  McGlone, 19 Feb 2019; page refused, 403: given as Wikipedia's summary, attributed).
- Shacknews, "Exclusive Interview: Campfire chat with the stars of Red Dead Redemption 2", 1 Feb 2019 (archived copy
  of 3 Feb 2019 fetched, fc/shack.txt). Benjamin Byron Davis: "the final scene in the skiff with Bronte, the mob boss
  at Saint Denis, and it took a long time I think to find Jim Pirri, who is the actor who so wonderfully played
  Bronte"; "I had the scene for nearly a year before we finally got to do it"; "about as iconic and thrilling and
  every bit of drama as I got to do".
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (cov/abigail/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt):
  unused outfit with a towel and shaving cream; a partially unused outfit seen only in a photo in the game; the
  unused "bronteasc" model used in place of the referee in an animation of "Bare Knuckle Friendships"; an unused vest
  for Bronte's butler; a cut short cutscene of Arthur and John leaving the cemetery. "Saint Denis Mob" trivia: PC
  files dialogue in which the mansion guards were to flee once the law arrived.
- GamesRadar+, Tom Power, "At the heart of Arthur Morgan's struggle in Red Dead Redemption 2 is a Shakespearean
  tragedy worth reflecting on", 4 Mar 2019 (archived copy fetched, fc/gr.txt): "Bronte's violent death at Dutch's
  hands repulses him even if Arthur fails to admit it".
- WhatCulture, Matt Thompson, "Red Dead Redemption: Every Villain Ranked From Worst To Best", 7 Feb 2022 (all 15 pages
  fetched): Bronte ranked 9th of 15; "one of the most brutal cut scene deaths".
Fix pass (20 Oct 2026): Davis's "I think" kept in the quote; GamesRadar+ structure (five stages of grief,
Bronte under "Clemens Point and Saint Denis (Bargaining)"); WhatCulture neighbors checked on the live pages (8 Javier,
10 Skinner Gang, 11 Bill, 12 Cornwall); born about 1844 = the wiki's deduction from "aged 55", attributed.
Excluded: Pirri's birth year (Wikipedia 1964, Red Dead Wiki 1967: not needed); "motion capture" as a fact (only the
Red Dead Wiki stub says so; Davis's "the final scene in the skiff" is quoted instead); WhatCulture's claim that Jack
was "collateral for their stolen moonshine" (the game does not say so); dcdouglas.com talent page (3 Apr 2025, credit
only, nothing new); the wiki's Angelo Bruno and Charles Matranga comparisons (no source).
DUPLICATE ownership: actor, casting remarks, cut content and reviews live HERE; part C trivia must not repeat them.
Reception must not repeat Development's Davis remarks.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Angelo Bronte appears only in Red Dead Redemption 2 (2018). He is played by Jim Pirri, an American actor and fight choreographer credited in the role by the Red Dead Wiki and by Wikipedia's list of the game's characters. According to Wikipedia, Pirri is the son of a linguist, grew up in Italy and speaks Italian. He has often played Italian characters. His other credits include David Vega in the series Victorious, Rais in Dying Light, Boozer in Days Gone and Kraven the Hunter in Marvel's Spider-Man 2.",
              "Angelo Bronte n'apparaît que dans Red Dead Redemption 2 (2018). Il est interprété par Jim Pirri, acteur et chorégraphe de combats américain, que le Red Dead Wiki et la liste des personnages du jeu sur Wikipédia créditent dans ce rôle. D'après Wikipédia, Pirri est fils de linguiste, a grandi en Italie et parle italien. Il a souvent joué des personnages italiens. On lui doit aussi David Vega dans la série Victorious, Rais dans Dying Light, Boozer dans Days Gone et Kraven le Chasseur dans Marvel's Spider-Man 2.")},
    {"p": two("Benjamin Byron Davis, who plays Dutch, talked about the role in an interview with Shacknews published on 1 February 2019. Asked for his favorite scene, he named \"the final scene in the skiff with Bronte\". He said that \"it took a long time I think to find Jim Pirri, who is the actor who so wonderfully played Bronte\". Davis added that he had the scene for nearly a year before it was shot. He called the result \"about as iconic and thrilling and every bit of drama as I got to do\".",
              "Benjamin Byron Davis, interprète de Dutch, évoque le rôle dans un entretien publié par Shacknews le 1er février 2019. Invité à citer sa scène préférée, il choisit \"the final scene in the skiff with Bronte\" (la dernière scène dans la barque avec Bronte). Selon lui, \"it took a long time I think to find Jim Pirri, who is the actor who so wonderfully played Bronte\" (il a fallu longtemps, je crois, pour trouver Jim Pirri, l'acteur qui a si merveilleusement joué Bronte). Davis précise qu'il a eu cette scène entre les mains près d'un an avant son tournage. Il la décrit comme \"about as iconic and thrilling and every bit of drama as I got to do\" (à peu près ce que j'ai pu jouer de plus emblématique, de plus palpitant et de plus dramatique).")},
    {"p": two("Davis came back to Bronte in other appearances, as summarized by Wikipedia. In an interview with Twinfinite (19 February 2019), he said that Dutch starts turning into a villain when he faces powerful figures such as Catherine Braithwaite and Angelo Bronte. On a cast panel at Fan Expo Canada in Toronto (24 August 2019), he described Bronte as the man Dutch wanted to be, which led to what happens between the two.",
              "Davis est revenu sur Bronte à d'autres occasions, que résume Wikipédia. Dans un entretien avec Twinfinite (19 février 2019), il explique que Dutch commence à basculer du côté des méchants face à des figures puissantes comme Catherine Braithwaite et Angelo Bronte. Lors d'une table ronde des acteurs au Fan Expo Canada de Toronto (24 août 2019), il présente Bronte comme l'homme que Dutch aurait voulu être, ce qui mène à ce qui se passe entre eux.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The Red Dead Wiki's page on cut content lists a few unused files around Bronte. One is an outfit with a towel and shaving cream. Another outfit is partly unused and appears only in a photograph in the game. An unused character model named \"bronteasc\" stands in for the referee in an animation of \"Bare Knuckle Friendships\", which the wiki reads as a planned associate of Bronte. The same page lists an unused vest for Bronte's butler and a short cutscene, removed from the game, in which Arthur and John leave the cemetery. The page on his organization adds that a line in the PC files has the mansion guards fleeing once the law arrives, whereas in the game they help the lawmen.",
              "La page du Red Dead Wiki consacrée au contenu coupé recense quelques fichiers inutilisés autour de Bronte. L'un est une tenue avec serviette et mousse à raser. Une autre tenue n'est utilisée qu'en partie et n'apparaît que sur une photographie dans le jeu. Un modèle de personnage inutilisé, baptisé \"bronteasc\", remplace l'arbitre dans une animation de \"Bare Knuckle Friendships\", ce que le wiki interprète comme un associé de Bronte prévu à l'origine. La même page signale un gilet inutilisé pour le majordome de Bronte et une courte cinématique coupée où Arthur et John quittent le cimetière. La page consacrée à son organisation ajoute qu'une réplique des fichiers PC faisait fuir les gardes de la demeure à l'arrivée de la loi, alors que dans le jeu ils prêtent main-forte aux hommes de loi.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("A turning point for Arthur", "Un tournant pour Arthur")},
    {"p": two("In GamesRadar+ on 4 March 2019, Tom Power read Arthur's story as a Shakespearean tragedy and structured his article on the five stages of grief. He placed the Bronte episode in the part titled \"Clemens Point and Saint Denis (Bargaining)\". He wrote that \"Bronte's violent death at Dutch's hands repulses him even if Arthur fails to admit it\". In his view, it leads Arthur to ask whether a man with such brutal methods is worth following.",
              "Dans GamesRadar+, le 4 mars 2019, Tom Power lit l'histoire d'Arthur comme une tragédie shakespearienne et construit son article sur les cinq étapes du deuil. Il range l'épisode Bronte dans la partie intitulée \"Clemens Point and Saint Denis (Bargaining)\", celle du marchandage. Il écrit que \"Bronte's violent death at Dutch's hands repulses him even if Arthur fails to admit it\" (la mort violente de Bronte de la main de Dutch le révulse, même si Arthur refuse de l'admettre). Selon lui, elle pousse Arthur à se demander s'il vaut la peine de suivre un homme aux méthodes aussi brutales.")},
    {"h3": two("Villain rankings", "Classements des méchants")},
    {"p": two("WhatCulture's Matt Thompson ranked Bronte ninth of the fifteen villains of the series in a list published on 7 February 2022. He comes after Javier Escuella (eighth) and ahead of the Skinner Brothers (tenth), Bill Williamson (11th) and Leviticus Cornwall (12th). He singled out the scene of his death as \"one of the most brutal cut scene deaths\".",
              "Matt Thompson, de WhatCulture, classe Bronte neuvième des quinze méchants de la série dans une liste publiée le 7 février 2022. Il arrive derrière Javier Escuella (huitième) et devant les frères Skinner (dixième), Bill Williamson (onzième) et Leviticus Cornwall (douzième). Il retient la scène de sa mort comme \"one of the most brutal cut scene deaths\" (l'une des morts les plus brutales en cinématique).")},
]


BASE = {
    "slug": "angelo-bronte", "name": "Angelo Bronte",
    "publishDate": "2026-07-09", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Crime lord &middot; RDR2", "reg_role_fr": "Chef de la pègre &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": "Italian",
    "portrait_alt": two("Angelo Bronte in Red Dead Redemption 2", "Angelo Bronte dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Saint Denis", "Personnage &middot; Saint-Denis"),
    "meta_desc": two("Angelo Bronte, the crime lord of Saint Denis in RDR2: Jack Marston held at his mansion, the mayor's party, the trolley station trap, his death at Dutch's hands in 1899, Jim Pirri.",
                     "Angelo Bronte, chef de la pègre de Saint-Denis dans RDR2 : Jack Marston retenu chez lui, la réception du maire, le piège de la station de tramway, sa mort de la main de Dutch en 1899, Jim Pirri."),
    "og_desc": two("The complete reference on Angelo Bronte: life, organization, quotes, development and reception.",
                   "La référence complète sur Angelo Bronte : vie, organisation, citations, conception et accueil."),
    "schema_desc": two("Italian businessman and crime lord of Saint Denis who holds the kidnapped Jack Marston, returns him to the Van der Linde gang, sets the gang up at a trolley station and is drowned by Dutch van der Linde in 1899, in Red Dead Redemption 2.",
                       "Homme d'affaires italien et chef de la pègre de Saint-Denis qui retient Jack Marston après son enlèvement, le rend au gang Van der Linde, lui tend un piège à une station de tramway et que Dutch van der Linde noie en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Crime lord", "Chef de la pègre"),
              two("Saint Denis", "Saint-Denis"),
              two("Played by <strong>Jim Pirri</strong>", "Interprété par <strong>Jim Pirri</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Angelo Bronte", "Angelo Bronte")},
        {"label": two("Aliases", "Surnoms"), "value": two("Signor Bronte; Mister Big and Papa Bronte, according to the Red Dead Wiki", "Signor Bronte ; Mister Big et Papa Bronte, selon le Red Dead Wiki")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game; about 1844 according to the Red Dead Wiki, deduced from his age (55) in a newspaper article of 1899", "Non précisée dans le jeu ; vers 1844 selon le Red Dead Wiki, qui la déduit de son âge (55 ans) dans un article de presse de 1899")},
        {"label": two("Died", "Mort"), "value": two("1899, drowned by [[dutch-van-der-linde|Dutch van der Linde]] in \"Revenge is a Dish Best Eaten\"", "1899, noyé par [[dutch-van-der-linde|Dutch van der Linde]] dans \"Revenge is a Dish Best Eaten\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédé")},
        {"label": two("Nationality", "Nationalité"), "value": two("Italian", "Italienne")},
        {"label": two("Residence", "Résidence"), "value": two("A mansion on Flavian Street, Saint Denis", "Une demeure de Flavian Street, à Saint-Denis")},
        {"label": two("Occupation", "Activité"), "value": two("Businessman and crime lord", "Homme d'affaires et chef de la pègre")},
        {"label": two("Affiliations", "Affiliations"), "value": two("His Saint Denis organization (the Saint Denis Mob, in the Red Dead Wiki), with Guido Martelli as underboss; business ties with the [[catherine-braithwaite|Braithwaite family]]", "Son organisation de Saint-Denis (la Saint Denis Mob, dans le Red Dead Wiki), avec Guido Martelli pour second ; des affaires avec la [[catherine-braithwaite|famille Braithwaite]]")},
        {"label": two("Enemy", "Ennemi"), "value": two("The Van der Linde gang", "Le gang Van der Linde")},
        {"label": two("Weapon", "Arme"), "value": two("Mauser pistol", "Pistolet Mauser")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Jim Pirri", "Jim Pirri")},
    ],
    "intro": [
        two("Angelo Bronte is an Italian businessman and crime lord in Saint Denis in Red Dead Redemption 2 (2018), set in 1899. In chapter 3 the Braithwaite family kidnaps [[jack-marston|Jack Marston]], and Catherine Braithwaite's sons hand the boy over to him. In chapter 4 [[dutch-van-der-linde|Dutch van der Linde]], [[arthur-morgan|Arthur Morgan]] and [[john-marston|John Marston]] get Jack back from his mansion in exchange for a job in the city cemetery. Bronte then invites Dutch to the mayor's party and points him to a trolley station, where the robbery turns into a police trap. The gang raids his mansion and carries him off, and Dutch drowns him and throws his body to an alligator.",
            "Angelo Bronte est un homme d'affaires italien et chef de la pègre de Saint-Denis dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Au chapitre 3, la famille Braithwaite enlève [[jack-marston|Jack Marston]], et les fils de Catherine Braithwaite lui livrent l'enfant. Au chapitre 4, [[dutch-van-der-linde|Dutch van der Linde]], [[arthur-morgan|Arthur Morgan]] et [[john-marston|John Marston]] récupèrent Jack dans sa demeure en échange d'un service rendu au cimetière de la ville. Bronte invite ensuite Dutch à la réception du maire et lui désigne une station de tramway, où le braquage tourne au guet-apens policier. Le gang prend d'assaut sa demeure et l'emmène, puis Dutch le noie et jette son corps à un alligator."),
        two("He is played by Jim Pirri.",
            "Il est interprété par Jim Pirri."),
    ],
    "essentials": [
        two("He runs a criminal organization from his mansion on Flavian Street, in Saint Denis, and is the guest of honor at the mayor's garden party.",
            "Il dirige une organisation criminelle depuis sa demeure de Flavian Street, à Saint-Denis, et il est l'invité d'honneur de la garden-party du maire."),
        two("In \"Angelo Bronte, A Man of Honor\", he gives Jack back to the gang once Arthur and John have cleared grave robbers out of the city cemetery.",
            "Dans \"Angelo Bronte, A Man of Honor\", il rend Jack à la bande une fois qu'Arthur et John ont chassé des pilleurs de tombes du cimetière de la ville."),
        two("In \"Urban Pleasures\", the trolley station he suggested holds only a few dollars, and armed police close in on Dutch, Arthur and Lenny.",
            "Dans \"Urban Pleasures\", la station de tramway qu'il a suggérée ne contient que quelques dollars, et des policiers armés cernent Dutch, Arthur et Lenny."),
        two("In \"Revenge is a Dish Best Eaten\", the gang abducts him from his mansion and Dutch drowns him from a skiff.",
            "Dans \"Revenge is a Dish Best Eaten\", le gang l'enlève dans sa demeure et Dutch le noie depuis une barque."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["dutch-van-der-linde", "jack-marston", "john-marston", "catherine-braithwaite"],
}
