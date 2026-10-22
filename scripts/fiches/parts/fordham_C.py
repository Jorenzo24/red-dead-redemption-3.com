"""Archer Fordham, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN and FR, fetched Oct 2026; shared cache scripts/v3/work/_m/, extra copies in
scripts/v3/work/fordham/fc/):
- Character page "Archer Fordham" (Mission appearances, Quotes, Trivia, Gallery captions) and FR page (Apparitions,
  Anecdotes), fordham/en.txt and fordham/fr.txt.
- Mission pages (infobox givers and rewards, order numbers, failure conditions, casualties, trivia): "Exodus in
  America" (1st), "The Gates of El Presidio" (40th; giver Abraham Reyes; 300 fame, 350 with the Gold Medal, 125
  honor), "Bear One Another's Burdens" (42nd, first of West Elizabeth; giver Edgar Ross; High Power Pistol, 150 fame,
  200 with the Gold Medal, 25 honor; failure if the car is damaged or Ross, Fordham or Nastas is assaulted, killed or
  left to die; trivia: Galatians 6:2), "Great Men are Not Always Wise"
  (43rd; giver Ross; 150 fame, 200 with the Gold Medal, up to 225 honor; failure if Ross, Fordham or another lawman is
  assaulted or killed; trivia: Job 32:9), "And You Will Know The Truth" (47th; giver Ross; 50 fame with the Gold Medal;
  failure if Ross or Fordham is assaulted or killed; trivia: John 8:32), "And The Truth Will Set You Free" (48th, last
  of West Elizabeth; giver Ross; 500 fame, 550 with the Gold Medal, 250 honor), "The Last Enemy That Shall Be
  Destroyed" (57th and last story mission; potential casualties; trivia: 1 Corinthians 15:26), "Ending Credits"
  (RDR2; trivia: Pinkerton badges), "Americans at Rest" (RDR2, chapter 2; trivia on the woman of the Valentine
  scene), "Isaac McKinnon" (trivia and gallery caption), "Liars and Cheats" (15 story characters, released September
  21, 2010), "Myths and Mavericks" (eight characters, released September 13, 2011).
- Transcripts used word for word for every quote: "Bear One Another's Burdens/dialogues", "The Gates of El
  Presidio/dialogues", "Great Men are Not Always Wise/dialogues", "And You Will Know The Truth/dialogues", "And The
  Truth Will Set You Free/dialogues".
- Real world: Red Dead Redemption released May 18, 2010 (North America); Red Dead Redemption 2 released October 26,
  2018; RDR1 on PlayStation 4 and Nintendo Switch August 17, 2023, on PC October 29, 2024, without multiplayer (as in
  nastas_C, irish_C).

VERIFIED POINTS: mission numbers and rewards are those of the infoboxes; the giver of "The Last Enemy That Shall Be
Destroyed" in the infobox is Jack Marston (not repeated, irrelevant to Fordham). Every quote below is in the
transcripts; "You've done well..." and "Unfortunately, nothing is cleared..." are capture-branch lines, "He's not
looking very... healthy..." is the kill branch (javier_A). Ross's "Come on, Archer..." line is in the transcript.

EXCLUDED: the weapon change from the Cattleman Revolver to the High Power Pistol and the Winchester Repeater of "Great
Men" (part B, weapons); the "Ross and Fordham contrast" trivia (light/dark clothes, old/young and short/tall are
appearance, part B; "deceitful and sardonic" versus "honest and blunt" is interpretation); the Javier-alive/dead
attitude trivia (told in part A); the 1914 absence and the Ledger No. 213 credit (part A); the unused 1899 Pinkerton
model, the unused fbi03 cutscene ("My Bessie does, sir.") and the cut line of the dog Rufus killed by Fordham (cut
content, part D); Maybelle Fordham's grave (part A Origins); the FR wiki's unused NPC line about the mother (part D)
and its Blackwater massacre reading (speculation); the Ending Credits page's "developer oversight" and the Prodigal
Son page's "it is quite unknown why" the agents are absent (commentary); the Americans at Rest page's "likely asking
her about the whereabouts of Micah Bell's killer" (interpretation: only her presence is kept); the wiki's link of
Fordham's "we have been watching" to the 1907 credits (the wiki's reading).

OWNERSHIP: narrative events live in part A (one line per mission here). Lines quoted in part B ("In his own words":
"I don't understand you people...", "Our armed forces have no equal...", "And this isn't much more than a simple
prototype...", "There's always somebody watching, Mr. Marston..."; Names: "Mr. Fordham", "Agent Fordham", John's
"office clerk or social secretary or some such") are NOT quoted here. Quoted HERE (FIX 22 Oct 2026, coverage items
1-5): "Marston, you're a public menace...", "Like you always say, sir...", "It ends when we say it ends...", "See, this
is what happens when you fraternize with savages...", John's "Dutch was a good man once, a far better man than you."
(transcripts: And You Will Know The Truth l.9, Bear One Another's Burdens l.87 and l.109, And The Truth Will Set You
Free l.61 and l.67). "Van der Linde is the priority..." is quoted here and paraphrased in part B. Failure conditions
live in the Missions table only; the ignition fact lives in part B (Trivia item cut); the full EN-vs-FR wiki dispute
on the last mission is told once, in Trivia; elsewhere the standard hedge of FIX_RULES.md. Ross's "Don't get snarky
with me, Fordham." is quoted in edgar_B and only paraphrased in this fiche.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A1 = two("Act I: New Austin", "Acte I : New Austin")
A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")
A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
E2 = two("RDR2, epilogue II", "RDR2, épilogue II")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Fordham appears in six story missions of Red Dead Redemption, numbered 1, 40, 42, 43, 47 and 48 in the story order, and gives none of them. The last four belong to Edgar Ross's strand, which opens the West Elizabeth part of the game and ends with the death of Dutch van der Linde. The English-language Red Dead Wiki, but not the French-language one, also places him in the last story mission, number 57. In Red Dead Redemption 2 he appears only in the end credits that follow \"American Venom\".",
              "Fordham apparaît dans six missions principales de Red Dead Redemption, numérotées 1, 40, 42, 43, 47 et 48 dans l'ordre de l'histoire, et n'en confie aucune. Les quatre dernières appartiennent à la série d'Edgar Ross, qui ouvre la partie West Elizabeth du jeu et se clôt sur la mort de Dutch van der Linde. Le Red Dead Wiki anglophone, contrairement au wiki francophone, le place aussi dans la dernière mission principale, la 57e. Dans Red Dead Redemption 2, il n'apparaît que dans le générique de fin qui suit \"American Venom\".")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Fordham's role", "Rôle de Fordham")], "rows": [
        M("Exodus in America", A1,
          "Escorts John with Ross from the Blackwater ferry to the train for Armadillo (named by the mission page; the transcript speaks of two lawmen). First mission of the game.",
          "Escorte John avec Ross du ferry de Blackwater jusqu'au train pour Armadillo (nommé par la page de la mission ; la transcription parle de deux hommes de loi). Première mission du jeu."),
        M("The Gates of El Presidio", A2,
          "Waits with Ross near the border bridge and takes Javier Escuella, alive or dead depending on the player's choice. Mission giver: Abraham Reyes. Rewards: 300 fame (350 with the Gold Medal) and 125 honor.",
          "Attend avec Ross près du pont de la frontière et récupère Javier Escuella, vivant ou mort selon le choix du joueur. Donneur de mission : Abraham Reyes. Récompenses : 300 points de célébrité (350 avec la médaille d'or) et 125 d'honneur."),
        M("Bear One Another's Burdens", A3,
          "Drives Ross and John to the wreck of the Serendipity, searches it with John, identifies Nastas once John finds him and repairs the car under fire. Mission giver: Edgar Ross. Rewards: High Power Pistol, 150 fame (200 with the Gold Medal) and 25 honor. Fails if the agents' car is damaged, or if Ross, Fordham or Nastas is attacked, killed or left to Dutch's men.",
          "Conduit Ross et John jusqu'à l'épave du Serendipity, la fouille avec John, identifie Nastas une fois que John l'a trouvé, et répare la voiture sous les balles. Donneur de mission : Edgar Ross. Récompenses : pistolet High Power, 150 points de célébrité (200 avec la médaille d'or) et 25 d'honneur. Échec si la voiture des agents est endommagée, ou si Ross, Fordham ou Nastas est agressé, tué ou abandonné aux hommes de Dutch."),
        M("Great Men are Not Always Wise", A3,
          "Takes position with Ross and John on a roof facing the Blackwater bank, then rides in the pursuit of Dutch. Mission giver: Edgar Ross. Rewards: 150 fame (200 with the Gold Medal) and up to 225 honor. Fails if Ross, Fordham or another lawman is attacked or killed.",
          "Se poste avec Ross et John sur un toit face à la banque de Blackwater, puis participe à la poursuite de Dutch. Donneur de mission : Edgar Ross. Récompenses : 150 points de célébrité (200 avec la médaille d'or) et jusqu'à 225 d'honneur. Échec si Ross, Fordham ou un autre homme de loi est agressé ou tué."),
        M("And You Will Know The Truth", A3,
          "Rides with Ross and John in the machine-gun vehicle to the army camp and through the chase, until it overturns. Mission giver: Edgar Ross. Reward: 50 fame with the Gold Medal. Fails if Ross or Fordham is attacked or killed.",
          "Accompagne Ross et John dans le véhicule à mitrailleuse jusqu'au camp de l'armée, puis pendant la poursuite, jusqu'à ce qu'il se renverse. Donneur de mission : Edgar Ross. Récompense : 50 points de célébrité avec la médaille d'or. Échec si Ross ou Fordham est agressé ou tué."),
        M("And The Truth Will Set You Free", A3,
          "Rides to Cochinay with Ross, John and the army, then thanks John after Dutch's fall. Mission giver: Edgar Ross. Rewards: 500 fame (550 with the Gold Medal) and 250 honor. Last mission of the West Elizabeth part.",
          "Chevauche jusqu'à Cochinay avec Ross, John et l'armée, puis remercie John après la chute de Dutch. Donneur de mission : Edgar Ross. Récompenses : 500 points de célébrité (550 avec la médaille d'or) et 250 d'honneur. Dernière mission de la partie West Elizabeth."),
        M("The Last Enemy That Shall Be Destroyed", A3,
          "According to the English-language Red Dead Wiki, Fordham is visible among the men facing John through the barn doors at Beecher's Hope in 1911 (he can be shot in the final Dead Eye and may disappear from the cutscene that follows); the French-language wiki says he does not take part in the mission. Last story mission of the game.",
          "D'après le Red Dead Wiki anglophone, on aperçoit Fordham parmi les hommes qui font face à John entre les portes de la grange de Beecher's Hope en 1911 (il peut être abattu pendant le Dead Eye final et disparaître de la cinématique qui suit) ; le wiki francophone affirme qu'il ne participe pas à la mission. Dernière mission principale du jeu."),
        M("Ending Credits", E2,
          "Searches Micah Bell's cabin while Ross examines the body, questions witnesses with him in Valentine and near Rhodes, and watches John and Jack at Beecher's Hope.",
          "Fouille la cabane de Micah Bell pendant que Ross examine le corps, interroge avec lui des témoins à Valentine et près de Rhodes, et observe John et Jack à Beecher's Hope."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English and checked against the transcripts of the Red Dead Wiki. The credits of Red Dead Redemption 2 have no transcript, and no line of Fordham from them is quoted.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction, et vérifiées sur les transcriptions du Red Dead Wiki. Le générique de Red Dead Redemption 2 n'a pas de transcription, et aucune réplique de Fordham n'en est tirée.")},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"quotes": [
        {"q": two("You've done well, Mr. Marston. Now, Javier here gets to see how far the hand of justice can reach.", "You've done well, Mr. Marston. Now, Javier here gets to see how far the hand of justice can reach."),
         "src": two("The Gates of El Presidio (RDR1, Act II), if Javier is captured",
                    "The Gates of El Presidio (RDR1, acte II), si Javier est capturé. Traduction : « Beau travail, monsieur Marston. Javier, ici présent, va pouvoir constater jusqu'où s'étend le bras de la justice. »")},
        {"q": two("Unfortunately, nothing is cleared, John, until your obligations are met.", "Unfortunately, nothing is cleared, John, until your obligations are met."),
         "src": two("The Gates of El Presidio (RDR1, Act II), if Javier is captured, when John asks whether one of his commitments is cleared",
                    "The Gates of El Presidio (RDR1, acte II), si Javier est capturé, quand John demande si l'un de ses engagements est rempli. Traduction : « Malheureusement, rien n'est réglé, John, tant que vous n'avez pas honoré vos obligations. »")},
        {"q": two("He's not looking very... healthy. We told you to keep them alive.", "He's not looking very... healthy. We told you to keep them alive."),
         "src": two("The Gates of El Presidio (RDR1, Act II), if Javier is killed",
                    "The Gates of El Presidio (RDR1, acte II), si Javier est tué. Traduction : « Il n'a pas l'air très... en forme. On vous avait dit de les garder en vie. »")},
        {"q": two("Mr. Marston, I ask you to calm down.", "Mr. Marston, I ask you to calm down."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), when John threatens him in the Blackwater office",
                    "Bear One Another's Burdens (RDR1, acte III), quand John le menace dans le bureau de Blackwater. Traduction : « Monsieur Marston, je vous demande de vous calmer. »")},
        {"q": two('Like you always say, sir, the higher the stakes, the smarter you have to play the game.', 'Like you always say, sir, the higher the stakes, the smarter you have to play the game.'),
         "src": two("Bear One Another's Burdens (RDR1, Act III), to Ross, on the drive to the wreck",
                    "Bear One Another's Burdens (RDR1, acte III), à Ross, sur la route de l'épave. Traduction : « Comme vous dites toujours, monsieur : plus les enjeux sont élevés, plus il faut jouer finement. »")},
        {"q": two("It ends when we say it ends. You're in no position to make demands.", "It ends when we say it ends. You're in no position to make demands."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), when John asks where it will all end",
                    "Bear One Another's Burdens (RDR1, acte III), quand John demande où tout cela s'arrêtera. Traduction : « Ça s'arrêtera quand nous le déciderons. Vous n'êtes pas en position d'exiger quoi que ce soit. »")},
        {"q": two("Van der Linde is the priority. We go in, take him down and get the hell out of here. Quick and clean.", "Van der Linde is the priority. We go in, take him down and get the hell out of here. Quick and clean."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), on the way down to the wreck",
                    "Bear One Another's Burdens (RDR1, acte III), en descendant vers l'épave. Traduction : « Van der Linde est la priorité. On entre, on l'abat et on fiche le camp d'ici. Vite et proprement. »")},
        {"q": two("It doesn't feel right. This place is usually teeming with lowlifes.", "It doesn't feel right. This place is usually teeming with lowlifes."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), on the deserted wreck of the Serendipity",
                    "Bear One Another's Burdens (RDR1, acte III), sur l'épave déserte du Serendipity. Traduction : « Ça ne me dit rien de bon. D'habitude, l'endroit grouille de voyous. »")},
        {"q": two("I was trying to escape an ambush, sir.", "I was trying to escape an ambush, sir."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), when Ross blames the breakdown on his driving",
                    "Bear One Another's Burdens (RDR1, acte III), quand Ross met la panne sur le compte de sa conduite. Traduction : « J'essayais d'échapper à une embuscade, monsieur. »")},
        {"q": two("Marston, you're a public menace. We should've had you killed.", "Marston, you're a public menace. We should've had you killed."),
         "src": two('And You Will Know The Truth (RDR1, Act III), in the Blackwater office, after Ross tells John he has failed',
                    'And You Will Know The Truth (RDR1, acte III), dans le bureau de Blackwater, après que Ross a reproché son échec à John. Traduction : « Marston, vous êtes un danger public. On aurait dû vous faire tuer. »')},
        {"q": two('See, this is what happens when you fraternize with savages. How could you ever follow a man like that?', 'See, this is what happens when you fraternize with savages. How could you ever follow a man like that?'),
         "src": two('And The Truth Will Set You Free (RDR1, Act III), on the ride to Cochinay',
                    'And The Truth Will Set You Free (RDR1, acte III), sur la route de Cochinay. Traduction : « Voilà ce qui arrive quand on fraie avec des sauvages. Comment avez-vous pu suivre un homme pareil ? »')},
        {"q": two("It's time to kill these motherless bastards!", "It's time to kill these motherless bastards!"),
         "src": two("And The Truth Will Set You Free (RDR1, Act III), when the gate of Cochinay is blown",
                    "And The Truth Will Set You Free (RDR1, acte III), quand la porte de Cochinay saute. Traduction : « Il est temps de tuer ces fils de rien ! »")},
        {"q": two("Thank you, Mr. Marston, for everything. I know this wasn't easy for you, but I have to say, you've done your country proud.", "Thank you, Mr. Marston, for everything. I know this wasn't easy for you, but I have to say, you've done your country proud."),
         "src": two("And The Truth Will Set You Free (RDR1, Act III), his last words to John, after Dutch's death",
                    "And The Truth Will Set You Free (RDR1, acte III), ses derniers mots à John, après la mort de Dutch. Traduction : « Merci, monsieur Marston, pour tout. Je sais que ça n'a pas été facile pour vous, mais je dois dire que vous avez fait honneur à votre pays. »")},
    ]},
    {"h4": two("What others say to him", "Ce que les autres lui disent")},
    {"quotes": [
        {"q": two("You leave Dutch to me. We don't want you gettin' that suit dirty.", "You leave Dutch to me. We don't want you gettin' that suit dirty."),
         "src": two("John Marston, Bear One Another's Burdens (RDR1, Act III), when Fordham sets out the plan",
                    "John Marston, Bear One Another's Burdens (RDR1, acte III), quand Fordham expose le plan. Traduction : « Laissez-moi Dutch. On ne voudrait pas que vous salissiez ce costume. »")},
        {"q": two("Perhaps if Mr. Fordham maneuvered it with a little more finesse.", "Perhaps if Mr. Fordham maneuvered it with a little more finesse."),
         "src": two("Edgar Ross, Bear One Another's Burdens (RDR1, Act III), when John complains about the automobile",
                    "Edgar Ross, Bear One Another's Burdens (RDR1, acte III), quand John se plaint de l'automobile. Traduction : « Peut-être que si M. Fordham la manœuvrait avec un peu plus de finesse. »")},
        {"q": two("I thought you were talkin' to Fordham.", "I thought you were talkin' to Fordham."),
         "src": two("John Marston, And You Will Know The Truth (RDR1, Act III), when Ross warns him that there must be no mistakes this time",
                    "John Marston, And You Will Know The Truth (RDR1, acte III), quand Ross le prévient qu'il n'y aura pas droit à l'erreur cette fois. Traduction : « Je croyais que vous parliez à Fordham. »")},
        {"q": two("Can't you hold this thing steady, Fordham?", "Can't you hold this thing steady, Fordham?"),
         "src": two("Edgar Ross, And You Will Know The Truth (RDR1, Act III), during the chase off the road",
                    "Edgar Ross, And You Will Know The Truth (RDR1, acte III), pendant la poursuite hors de la route. Traduction : « Vous ne pouvez pas tenir ce machin droit, Fordham ? »")},
        {"q": two("Ross don't seem too different. Dutch was a good man once, a far better man than you.", "Ross don't seem too different. Dutch was a good man once, a far better man than you."),
         "src": two('John Marston, And The Truth Will Set You Free (RDR1, Act III), on the ride to Cochinay, after Fordham calls Dutch a psychopath',
                    "John Marston, And The Truth Will Set You Free (RDR1, acte III), sur la route de Cochinay, quand Fordham traite Dutch de psychopathe. Traduction : « Ross n'a pas l'air bien différent. Dutch a été un homme bien, autrefois, bien meilleur que vous. »")},
        {"q": two("Come on, Archer, let's go find somebody else we can annoy.", "Come on, Archer, let's go find somebody else we can annoy."),
         "src": two("Edgar Ross, And The Truth Will Set You Free (RDR1, Act III), after Dutch's death",
                    "Edgar Ross, And The Truth Will Set You Free (RDR1, acte III), après la mort de Dutch. Traduction : « Venez, Archer, allons trouver quelqu'un d'autre à embêter. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("Five of the missions in which Fordham appears take their titles from the Bible, as their mission pages note: \"Bear One Another's Burdens\" (Galatians 6:2), \"Great Men are Not Always Wise\" (Job 32:9), \"And You Will Know The Truth\" and \"And The Truth Will Set You Free\" (John 8:32) and \"The Last Enemy That Shall Be Destroyed\" (1 Corinthians 15:26).",
            "Cinq des missions où apparaît Fordham tirent leur titre de la Bible, comme le relèvent leurs pages de mission : \"Bear One Another's Burdens\" (Galates 6:2), \"Great Men are Not Always Wise\" (Job 32:9), \"And You Will Know The Truth\" et \"And The Truth Will Set You Free\" (Jean 8:32), et \"The Last Enemy That Shall Be Destroyed\" (1 Corinthiens 15:26)."),
        two("According to the Red Dead Wiki's page on the end credits of Red Dead Redemption 2, Ross and Fordham both wear Pinkerton badges in their 1907 scenes, although a newspaper of the epilogue reports that Ross now heads the Bureau of Investigation.",
            "D'après la page du Red Dead Wiki consacrée au générique de fin de Red Dead Redemption 2, Ross et Fordham portent tous deux un insigne Pinkerton dans leurs scènes de 1907, alors qu'un journal de l'épilogue annonce que Ross dirige désormais le Bureau of Investigation."),
        two("According to the mission page of \"Americans at Rest\" (Red Dead Redemption 2, chapter 2), the woman Ross and Fordham talk to in the Valentine saloon during the credits is one of the two women [[javier-escuella|Javier Escuella]] is talking to at the bar in that mission.",
            "D'après la page de la mission \"Americans at Rest\" (Red Dead Redemption 2, chapitre 2), la femme à qui Ross et Fordham parlent dans le saloon de Valentine pendant le générique est l'une des deux femmes avec qui [[javier-escuella|Javier Escuella]] discute au bar dans cette mission."),
        two("The two Red Dead Wikis disagree about Fordham's presence in \"The Last Enemy That Shall Be Destroyed\". The English-language wiki places him among the men at the barn. It also names a U.S. marshal, Isaac McKinnon, who looks and dresses like Fordham and stands beside Ross in the last cutscene, and notes that the two are often confused. The French-language wiki holds that Fordham is not in the mission at all and that the man beside Ross is McKinnon.",
            "Les deux Red Dead Wiki ne s'accordent pas sur la présence de Fordham dans \"The Last Enemy That Shall Be Destroyed\". Le wiki anglophone le compte parmi les hommes postés devant la grange. Il signale aussi un marshal, Isaac McKinnon, qui a le physique et la tenue de Fordham, et qui se tient aux côtés de Ross dans la dernière cinématique ; on confond souvent les deux hommes, note-t-il. Le wiki francophone soutient que Fordham est absent de la mission et que l'homme aux côtés de Ross est McKinnon."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Fordham is not a playable character in the multiplayer mode of Red Dead Redemption. He is absent from the fifteen story characters added to the Outfitter by the Liars and Cheats Pack, released on September 21, 2010, which includes Edgar Ross, and from the eight added by the free Myths and Mavericks Bonus Pack, released on September 13, 2011. The versions of the game released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, have no multiplayer mode.",
              "Fordham n'est pas un personnage jouable du multijoueur de Red Dead Redemption. Il ne figure ni parmi les quinze personnages de l'histoire ajoutés à l'Outfitter par le Liars and Cheats Pack, sorti le 21 septembre 2010, qui comprend Edgar Ross, ni parmi les huit du Myths and Mavericks Bonus Pack, gratuit, sorti le 13 septembre 2011. Les versions du jeu sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, n'ont pas de mode multijoueur.")},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"p": two("Red Dead Redemption 2, released on October 26, 2018, is a prequel set in 1899 and 1907. Fordham appears only in its end credits, eight years after his first appearance in Red Dead Redemption (May 18, 2010 in North America). The Red Dead Wiki lists no appearance of Fordham in Red Dead Online or in Undead Nightmare.",
              "Red Dead Redemption 2, sorti le 26 octobre 2018, est une préquelle dont l'action se déroule en 1899 et en 1907. Fordham n'apparaît que dans son générique de fin, huit ans après sa première apparition dans Red Dead Redemption (18 mai 2010 en Amérique du Nord). Le Red Dead Wiki ne lui recense aucune apparition dans Red Dead Online ni dans Undead Nightmare.")},
]
