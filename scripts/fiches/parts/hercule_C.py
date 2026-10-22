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
    {"p": two("The Red Dead Wiki lists three missions of Red Dead Redemption 2 for Hercule, all in chapter 5. He is the giver of \"Hell Hath No Fury\"; the other two missions are given by Dutch and by Bill. Two more Guarma missions mention him without showing him.",
              "Le Red Dead Wiki recense trois missions de Red Dead Redemption 2 pour Hercule, toutes au chapitre 5. C'est lui qui donne \"Hell Hath No Fury\" ; les deux autres sont confiées par Dutch et par Bill. Deux autres missions de Guarma parlent de lui sans le montrer.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Hercule's role", "Rôle d'Hercule")], "rows": [
        M("Welcome to the New World", C5,
          "His rebels ambush the soldiers marching the chained castaways; he leads the survivors to his weapons cache, then offers a boat in exchange for their help.",
          "Ses rebelles attaquent les soldats qui escortent les naufragés enchaînés ; il conduit les rescapés à sa cache d'armes, puis leur propose un bateau en échange de leur aide."),
        M("Hell Hath No Fury", C5,
          "Defends Cinco Torres with the gang and reloads the fort's cannon while [[arthur-morgan|Arthur]] sinks the Cuban warship.",
          "Défend Cinco Torres avec la bande et recharge le canon du fort pendant qu'[[arthur-morgan|Arthur]] coule le navire de guerre cubain."),
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
    {"p": two("The lines below are given in the original English and checked against a full transcript of the game's dialogue. The game gives Hercule's French lines only in passing; they are not quoted here.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise et vérifiées sur une transcription complète des dialogues du jeu. Les quelques mots qu'Hercule prononce en français ne sont pas repris ici.")},
    {"h4": two("Hercule", "Hercule")},
    {"quotes": [
        {"q": two("It's not my island.", "It's not my island."),
         "src": two("To Arthur, who has just remarked on the island, Welcome to the New World (RDR2, chapter 5)",
                    "À Arthur, qui vient de faire une remarque sur l'île, Welcome to the New World (RDR2, chapitre 5). Traduction : « Ce n'est pas mon île. »")},
        {"q": two("I don't see you have any choice. I am the only one who can arrange a boat for you. But... I need something in return.",
                  "I don't see you have any choice. I am the only one who can arrange a boat for you. But... I need something in return."),
         "src": two("To Dutch, who asks whether they can trust him, Welcome to the New World (RDR2, chapter 5)",
                    "À Dutch, qui demande s'ils peuvent lui faire confiance, Welcome to the New World (RDR2, chapitre 5). Traduction : « Je ne vois pas bien quel choix vous avez. Je suis le seul à pouvoir vous trouver un bateau. Mais... il me faut quelque chose en retour. »")},
        {"q": two("And you will. But you have found yourself in the middle of a war, my friend. Fussar has called in the navy from Cuba. There's no way a boat could leave right now.",
                  "And you will. But you have found yourself in the middle of a war, my friend. Fussar has called in the navy from Cuba. There's no way a boat could leave right now."),
         "src": two("To Dutch, who demands the promised boat, Hell Hath No Fury (RDR2, chapter 5)",
                    "À Dutch, qui réclame le bateau promis, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Et vous l'aurez. Mais vous êtes tombé en pleine guerre, mon ami. Fussar a fait venir la marine de Cuba. Aucun bateau ne peut partir pour le moment. »")},
        {"q": two("We fight or we run.", "We fight or we run."),
         "src": two("Seeing the warship, Hell Hath No Fury (RDR2, chapter 5)",
                    "En voyant le navire de guerre, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « On se bat ou on fuit. »")},
        {"q": two("I am! What do you want me to do? We are trapped up here!", "I am! What do you want me to do? We are trapped up here!"),
         "src": two("To Bill, who shouts that he promised them a boat, Hell Hath No Fury (RDR2, chapter 5)",
                    "À Bill, qui lui crie qu'il leur avait promis un bateau, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Je m'en occupe ! Qu'est-ce que vous voulez que je fasse ? On est coincés ici ! »")},
        {"q": two("You man the cannon... I'll get you some more shot. Aim at the waterline... we need to put a serious hole in that boat.",
                  "You man the cannon... I'll get you some more shot. Aim at the waterline... we need to put a serious hole in that boat."),
         "src": two("To Arthur, on the roof of Cinco Torres, Hell Hath No Fury (RDR2, chapter 5)",
                    "À Arthur, sur le toit de Cinco Torres, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Tu t'occupes du canon... je te ramène des boulets. Vise la ligne de flottaison... il faut faire un sacré trou dans ce bateau. »")},
        {"q": two("He's shooting, we have to take him down! Arthur, there's another cannon up ahead on our left. Can you get to that?",
                  "He's shooting, we have to take him down! Arthur, there's another cannon up ahead on our left. Can you get to that?"),
         "src": two("Spotting Fussar in the tower, Paradise Mercifully Departed (RDR2, chapter 5)",
                    "En repérant Fussar dans la tour, Paradise Mercifully Departed (RDR2, chapitre 5). Traduction : « Il tire, il faut l'abattre ! Arthur, il y a un autre canon devant nous, sur la gauche. Tu peux l'atteindre ? »")},
        {"q": two("We'll be like you. We'll disappear probably... back to Haiti. Believe me, we'll be long gone by morning.",
                  "We'll be like you. We'll disappear probably... back to Haiti. Believe me, we'll be long gone by morning."),
         "src": two("To Dutch, who asks whether he will be all right, Paradise Mercifully Departed (RDR2, chapter 5)",
                    "À Dutch, qui lui demande s'il s'en sortira, Paradise Mercifully Departed (RDR2, chapitre 5). Traduction : « On fera comme vous. On va disparaître, sans doute... retourner en Haïti. Croyez-moi, on sera loin avant le matin. »")},
    ]},
    {"h4": two("About Hercule", "Au sujet d'Hercule")},
    {"quotes": [
        {"q": two("Almost certainly, but he's the best chance we have right now of getting out of this place.",
                  "Almost certainly, but he's the best chance we have right now of getting out of this place."),
         "src": two("Dutch, when Arthur asks whether Hercule is just using them, A Kind and Benevolent Despot (RDR2, chapter 5)",
                    "Dutch, quand Arthur se demande si Hercule ne se sert pas d'eux, A Kind and Benevolent Despot (RDR2, chapitre 5). Traduction : « Presque à coup sûr, mais c'est notre meilleure chance de quitter cet endroit pour l'instant. »")},
        {"q": two("Hercule is getting a boat lined up... to get you and your men out of here. Just meet him at Cinco Torres.",
                  "Hercule is getting a boat lined up... to get you and your men out of here. Just meet him at Cinco Torres."),
         "src": two("Baptiste to Arthur, Savagery Unleashed (RDR2, chapter 5)",
                    "Baptiste à Arthur, Savagery Unleashed (RDR2, chapitre 5). Traduction : « Hercule est en train de trouver un bateau... pour vous sortir d'ici, toi et tes hommes. Retrouve-le simplement à Cinco Torres. »")},
        {"q": two("He's using us!", "He's using us!"),
         "src": two("Micah, during the defense of the fort, Hell Hath No Fury (RDR2, chapter 5)",
                    "Micah, pendant la défense du fort, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Il se sert de nous ! »")},
        {"q": two("Hercule... it was a great pleasure to make your acquaintance.", "Hercule... it was a great pleasure to make your acquaintance."),
         "src": two("Dutch, after the warship sinks, Hell Hath No Fury (RDR2, chapter 5)",
                    "Dutch, après le naufrage du navire de guerre, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Hercule... ce fut un grand plaisir de faire votre connaissance. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("In \"Welcome to the New World\", the mission fails if the player attacks or kills Hercule or Leon Fuentes.",
            "Dans \"Welcome to the New World\", la mission échoue si le joueur agresse ou tue Hercule ou Leon Fuentes."),
        two("He switches to French several times during the fighting: a few exclamations, an order to move on and an insult aimed at the soldiers.",
            "Il passe plusieurs fois au français pendant les combats : quelques exclamations, un ordre de départ et une insulte lancée aux soldats."),
        two("According to the Red Dead Wiki, the second part of the score track \"Welcome to the New World\" plays when the castaways break free and fight the soldiers with Hercule's help.",
            "Selon le Red Dead Wiki, la seconde partie du morceau \"Welcome to the New World\", tiré de la musique originale du jeu, accompagne le moment où les naufragés se libèrent et combattent les soldats avec l'aide d'Hercule."),
        two("In \"Hell Hath No Fury\", Hercule reloads the cannon between Arthur's shots, but according to the Red Dead Wiki the shells visible in the magazine never move.",
            "Dans \"Hell Hath No Fury\", Hercule recharge le canon entre les tirs d'Arthur, mais selon le Red Dead Wiki, les obus visibles dans la réserve ne bougent jamais."),
        two("The Red Dead Wiki notes that Hercule runs very fast on the way back up to the roof of Cinco Torres, along a path with sharp turns and drops, and that the player can easily lose sight of him.",
            "Le Red Dead Wiki remarque qu'Hercule court très vite en remontant vers le toit de Cinco Torres, par un chemin plein de virages serrés et de dénivelés, et que le joueur le perd facilement de vue."),
        two("According to the Red Dead Wiki, the ship's captain can already be seen among the men following Hercule after the first fight of \"Welcome to the New World\", before the story introduces him.",
            "Selon le Red Dead Wiki, le capitaine du navire est déjà visible parmi les hommes qui suivent Hercule après le premier combat de \"Welcome to the New World\", avant que l'histoire ne le présente."),
        two("The Red Dead Wiki mentions a random encounter on Guarma in which rebels are chased by Fussar's soldiers.",
            "Le Red Dead Wiki signale une rencontre aléatoire, à Guarma, au cours de laquelle des rebelles sont poursuivis par les soldats de Fussar."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("Hercule appears only in Red Dead Redemption 2. He was not among the characters described in the details Rockstar gave The Hollywood Reporter in September 2018, which covered members of the Van der Linde gang. Guarma cannot be visited in Red Dead Online, and Hercule does not appear there. According to the Red Dead Wiki, players of the online mode can set a flag bearing the Guarma coat of arms as their camp flag after reaching rank 59 of the third Outlaw Pass.",
              "Hercule n'apparaît que dans Red Dead Redemption 2. Il ne figurait pas parmi les personnages présentés dans les informations que Rockstar a confiées au Hollywood Reporter en septembre 2018, consacrées aux membres de la bande de Van der Linde. Guarma n'est pas accessible dans Red Dead Online, et Hercule n'y apparaît pas. Selon le Red Dead Wiki, les joueurs du mode en ligne peuvent adopter pour leur camp un drapeau aux armes de Guarma après avoir atteint le rang 59 du troisième Outlaw Pass.")},
]
