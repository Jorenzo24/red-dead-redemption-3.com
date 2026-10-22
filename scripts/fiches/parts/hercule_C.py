"""Hercule Fontaine, part C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (fetched Oct 2026; wiki pages cached in scripts/v3/work/_m/, transcript in scripts/v3/work/hercule/fc/):
- Red Dead Wiki EN "Hercule Fontaine" (en.txt): Mission appearances ("Welcome to the New World", "Hell Hath No Fury",
  "Paradise Mercifully Departed"); the page has no Quotes or Trivia section. Red Dead Wiki FR (fr.txt): same three missions.
- Mission pages: "Welcome to the New World" (Mission Failure: assaulting or killing Hercule or Leon; Background Music: the
  score track "Welcome to the New World", Part II), "Hell Hath No Fury" (infobox giver: Hercule; Trivia: the cannon magazine
  that does not empty while Hercule reloads, Hercule running fast back to the roof), "Paradise Mercifully Departed" (giver:
  Bill Williamson; Gold Medal Tips: Hercule shouting at the player to move on). "Welcome to the New World" giver: Dutch.
- TRANSCRIPT: "Red Dead Redemption 2 Full Transcript", Game Scripts Wiki (game-scripts-wiki.blogspot.com), fan transcript
  saved as scripts/v3/work/hercule/fc/gsw.txt (not committed). Every quoted line below is checked word for word against it
  (curly apostrophes and the ellipsis character replaced by straight apostrophes and "..."); the speaker labels are the
  transcript's ("Stranger 2" before Hercule gives his name in "Welcome to the New World"). The lines "In French" are
  given by the transcript in English translation only: not quoted.
- Wiki pages: "Captain C." (Trivia: the captain visible among the men following Hercule in "Welcome to the New World"),
  "Guarma Rebels" (Trivia: random encounter with rebels chased by soldiers), "Guarma" (island not accessible in Red Dead
  Online; Guarma flag as a camp flag, rank 59 of the third Outlaw Pass), "Baptiste".
- Rockstar's character descriptions published by The Hollywood Reporter (Sept. 2018; scripts/v3/sources/thr_descriptions.txt):
  no entry for Hercule (checked by search).

FIXER (22 Oct 2026): the seven lines quoted in part B (In his own words, Relationships) were removed from Quotes and
replaced by B's "left to C" lines plus two Dutch lines (gsw.txt 10666, 10844), all checked verbatim; Trivia no longer
repeats the mission-fail, French-lines and fast-run items (B owns them); the THR sentence lives in B Personality only;
"appears only in Red Dead Redemption 2" lives here, not in D.

OWNERSHIP: one line per mission in the table, narrative in part A. Quotes chosen among mission lines; lines that part B may
quote in "In his own words" must be removed from one of the two places by the fixer (candidates: "It's not my island",
"I am not from here...", "I'll fight Alberto Fussar every day I can"). Part A paraphrases all of them.

EXCLUDED (one line each)
- Hercule's French lines ("Take that, asshole", "Shit", the rebel calling him): the transcript gives them only in translation,
  so no verbatim French is available.
- Captain C. appearing in "Welcome to the New World" being a developer "oversight": interpretation of the wiki; only the
  observation is kept.
- The two songbirds of "Hell Hath No Fury" read as Hosea and Lenny: fan belief (mission trivia), and not about Hercule.
- The Cinco Torres rum brand and the Morro Castle resemblance: about the fort, not about Hercule.
- Any appearance in trailers, artwork or Red Dead Online: none found; nothing invented.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C5 = two("5. Guarma", "5. Guarma")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The Red Dead Wiki lists three missions of Red Dead Redemption 2 for Hercule, all in chapter 5. He is the giver of \"Hell Hath No Fury\"; the other two missions are given by Dutch and by Bill.",
              "Le Red Dead Wiki recense trois missions de Red Dead Redemption 2 pour Hercule, toutes au chapitre 5. C'est lui qui donne \"Hell Hath No Fury\" ; les deux autres sont confiées par Dutch et par Bill.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Hercule's role", "Rôle d'Hercule")], "rows": [
        M("Welcome to the New World", C5,
          "His rebels ambush the soldiers marching the chained castaways; he leads the survivors to his weapons cache, then offers a boat in exchange for their help.",
          "Ses rebelles attaquent les soldats qui escortent les naufragés enchaînés ; il conduit les rescapés à sa cache d'armes, puis leur propose un bateau en échange de leur aide."),
        M("Hell Hath No Fury", C5,
          "Defends Cinco Torres with the gang and reloads the fort's cannon while [[arthur-morgan|Arthur]] sinks the warship sent from Cuba.",
          "Défend Cinco Torres avec la bande et recharge le canon du fort pendant qu'[[arthur-morgan|Arthur]] coule le navire de guerre venu de Cuba."),
        M("Paradise Mercifully Departed", C5,
          "Guides the attack on Fussar's gun positions, spots [[alberto-fussar|Fussar]] in the tower and sees the gang off at the dock.",
          "Guide l'attaque des batteries de Fussar, repère [[alberto-fussar|Fussar]] dans la tour et salue le départ de la bande sur le quai."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Hercule", "Lien avec Hercule")], "rows": [
        M("Savagery Unleashed", C5,
          "Baptiste, who works with him, tells Arthur that Hercule is lining up a boat and to meet him at Cinco Torres.",
          "Baptiste, qui travaille avec lui, apprend à Arthur qu'Hercule prépare un bateau et qu'il faut le rejoindre à Cinco Torres."),
        M("A Kind and Benevolent Despot", C5,
          "[[dutch-van-der-linde|Dutch]] uses the cave Hercule told him about to reach Aguasdulces and free [[javier-escuella|Javier]].",
          "[[dutch-van-der-linde|Dutch]] emprunte la grotte qu'Hercule lui a indiquée pour atteindre Aguasdulces et libérer [[javier-escuella|Javier]]."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English and checked against a full transcript of the game's dialogue. Hercule's French lines are covered under Languages. Lines already quoted in Personality and Relationships are not repeated here.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise et vérifiées sur une transcription complète des dialogues du jeu. Ses quelques mots en français sont traités dans la partie Langues. Les répliques déjà citées dans Personnalité et Relations ne sont pas reprises ici.")},
    {"h4": two("Hercule", "Hercule")},
    {"quotes": [
        {"q": two("Okay. Well, Fussar will be desperate to find you. We must be very careful.",
                  "Okay. Well, Fussar will be desperate to find you. We must be very careful."),
         "src": two("To Dutch, after the introductions, Welcome to the New World (RDR2, chapter 5)",
                    "À Dutch, une fois les présentations faites, Welcome to the New World (RDR2, chapitre 5). Traduction : « Bon. Eh bien, Fussar va tout faire pour vous retrouver. Il faut être très prudents. »")},
        {"q": two("Leon wants the people to stand up to Fussar... but most are too afraid.",
                  "Leon wants the people to stand up to Fussar... but most are too afraid."),
         "src": two("After Leon describes Fussar, Welcome to the New World (RDR2, chapter 5)",
                    "Après le portrait de Fussar dressé par Leon, Welcome to the New World (RDR2, chapitre 5). Traduction : « Leon voudrait que le peuple tienne tête à Fussar... mais la plupart ont trop peur. »")},
        {"q": two("Gentlemen, goodbye.", "Gentlemen, goodbye."),
         "src": two("Leaving the castaways to rest, Welcome to the New World (RDR2, chapter 5)",
                    "En laissant les naufragés se reposer, Welcome to the New World (RDR2, chapitre 5). Traduction : « Messieurs, au revoir. »")},
        {"q": two("But, if we can silence him... then I can help you escape before anyone has time... to get here from America. That way, we all get what we want.",
                  "But, if we can silence him... then I can help you escape before anyone has time... to get here from America. That way, we all get what we want."),
         "src": two("To Dutch, at Cinco Torres, Hell Hath No Fury (RDR2, chapter 5)",
                    "À Dutch, à Cinco Torres, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Mais si on arrive à le faire taire... je pourrai vous aider à partir avant que qui que ce soit ait le temps... de venir d'Amérique. Comme ça, tout le monde y trouve son compte. »")},
        {"q": two("And you will. But you have found yourself in the middle of a war, my friend. Fussar has called in the navy from Cuba. There's no way a boat could leave right now.",
                  "And you will. But you have found yourself in the middle of a war, my friend. Fussar has called in the navy from Cuba. There's no way a boat could leave right now."),
         "src": two("To Dutch, who demands the promised boat, Hell Hath No Fury (RDR2, chapter 5)",
                    "À Dutch, qui réclame le bateau promis, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Et vous l'aurez. Mais vous êtes tombé en pleine guerre, mon ami. Fussar a fait venir la marine de Cuba. Aucun bateau ne peut partir pour le moment. »")},
        {"q": two("So now we have a real problem. This must be the boat he called in from Cuba.",
                  "So now we have a real problem. This must be the boat he called in from Cuba."),
         "src": two("Seeing the warship from the fort, Hell Hath No Fury (RDR2, chapter 5)",
                    "En apercevant le navire de guerre depuis le fort, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Là, on a un vrai problème. Ça doit être le bateau qu'il a fait venir de Cuba. »")},
        {"q": two("We fight or we run.", "We fight or we run."),
         "src": two("When Arthur asks what now, Hell Hath No Fury (RDR2, chapter 5)",
                    "Quand Arthur demande quoi faire, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « On se bat ou on fuit. »")},
        {"q": two("You man the cannon... I'll get you some more shot. Aim at the waterline... we need to put a serious hole in that boat.",
                  "You man the cannon... I'll get you some more shot. Aim at the waterline... we need to put a serious hole in that boat."),
         "src": two("To Arthur, on the roof of Cinco Torres, Hell Hath No Fury (RDR2, chapter 5)",
                    "À Arthur, sur le toit de Cinco Torres, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Tu t'occupes du canon... je te ramène des boulets. Vise la ligne de flottaison... il faut faire un sacré trou dans ce bateau. »")},
        {"q": two("Oh, they'll be back... but, I found a boat for you... and he should be arriving on the dock anytime now.",
                  "Oh, they'll be back... but, I found a boat for you... and he should be arriving on the dock anytime now."),
         "src": two("To Dutch, after the warship sinks, Hell Hath No Fury (RDR2, chapter 5)",
                    "À Dutch, après le naufrage du navire de guerre, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Oh, ils reviendront... mais je vous ai trouvé un bateau... et il devrait arriver au quai d'un moment à l'autre. »")},
        {"q": two("He's shooting, we have to take him down! Arthur, there's another cannon up ahead on our left. Can you get to that?",
                  "He's shooting, we have to take him down! Arthur, there's another cannon up ahead on our left. Can you get to that?"),
         "src": two("Spotting Fussar in the tower, Paradise Mercifully Departed (RDR2, chapter 5)",
                    "En repérant Fussar dans la tour, Paradise Mercifully Departed (RDR2, chapitre 5). Traduction : « Il tire, il faut l'abattre ! Arthur, il y a un autre canon devant nous, sur la gauche. Tu peux l'atteindre ? »")},
    ]},
    {"h4": two("About Hercule", "Au sujet d'Hercule")},
    {"quotes": [
        {"q": two("Hercule is getting a boat lined up... to get you and your men out of here. Just meet him at Cinco Torres.",
                  "Hercule is getting a boat lined up... to get you and your men out of here. Just meet him at Cinco Torres."),
         "src": two("Baptiste to Arthur, Savagery Unleashed (RDR2, chapter 5)",
                    "Baptiste à Arthur, Savagery Unleashed (RDR2, chapitre 5). Traduction : « Hercule est en train de trouver un bateau... pour vous sortir d'ici, toi et tes hommes. Retrouve-le simplement à Cinco Torres. »")},
        {"q": two("Well, I found the cave Hercule spoke of and also a... guide...",
                  "Well, I found the cave Hercule spoke of and also a... guide..."),
         "src": two("Dutch to Arthur, A Kind and Benevolent Despot (RDR2, chapter 5)",
                    "Dutch à Arthur, A Kind and Benevolent Despot (RDR2, chapitre 5). Traduction : « Bon, j'ai trouvé la grotte dont parlait Hercule, et aussi une... guide... »")},
        {"q": two("This will give us a chance to get to Hercule's fort. I'll meet you there, Arthur.",
                  "This will give us a chance to get to Hercule's fort. I'll meet you there, Arthur."),
         "src": two("Dutch, carrying Javier out of Aguasdulces, A Kind and Benevolent Despot (RDR2, chapter 5)",
                    "Dutch, qui emmène Javier hors d'Aguasdulces, A Kind and Benevolent Despot (RDR2, chapitre 5). Traduction : « Ça nous laissera le temps de gagner le fort d'Hercule. On se retrouve là-bas, Arthur. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("According to the Red Dead Wiki, the second part of the score track \"Welcome to the New World\" plays when the castaways break free and fight the soldiers with Hercule's help.",
            "Selon le Red Dead Wiki, la seconde partie du morceau \"Welcome to the New World\", tiré de la musique originale du jeu, accompagne le moment où les naufragés se libèrent et combattent les soldats avec l'aide d'Hercule."),
        two("In \"Hell Hath No Fury\", Hercule reloads the cannon between Arthur's shots, but according to the Red Dead Wiki the shells visible in the magazine never move.",
            "Dans \"Hell Hath No Fury\", Hercule recharge le canon entre les tirs d'Arthur, mais selon le Red Dead Wiki, les obus visibles dans la réserve ne bougent jamais."),
        two("According to the Red Dead Wiki, the ship's captain can already be seen among the men following Hercule after the first fight of \"Welcome to the New World\", before the story introduces him.",
            "Selon le Red Dead Wiki, le capitaine du navire est déjà visible parmi les hommes qui suivent Hercule après le premier combat de \"Welcome to the New World\", avant que l'histoire ne le présente."),
        two("The Red Dead Wiki mentions a random encounter on Guarma in which rebels are chased by Fussar's soldiers.",
            "Le Red Dead Wiki signale une rencontre aléatoire, à Guarma, au cours de laquelle des rebelles sont poursuivis par les soldats de Fussar."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("Hercule appears only in Red Dead Redemption 2. Guarma cannot be visited in Red Dead Online, and Hercule does not appear there. According to the Red Dead Wiki, players of the online mode can set a flag bearing the Guarma coat of arms as their camp flag after reaching rank 59 of the third Outlaw Pass.",
              "Hercule n'apparaît que dans Red Dead Redemption 2. Guarma n'est pas accessible dans Red Dead Online, et Hercule n'y apparaît pas. Selon le Red Dead Wiki, les joueurs du mode en ligne peuvent adopter pour leur camp un drapeau aux armes de Guarma après avoir atteint le rang 59 du troisième Outlaw Pass.")},
]
