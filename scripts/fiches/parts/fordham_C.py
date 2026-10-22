"""Archer Fordham, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN and FR, fetched Oct 2026; shared cache scripts/v3/work/_m/, extra copies in
scripts/v3/work/fordham/fc/):
- Character page "Archer Fordham" (Mission appearances, Quotes, Trivia, Gallery captions) and FR page (Apparitions,
  Anecdotes), fordham/en.txt and fordham/fr.txt.
- Mission pages (infobox givers and rewards, order numbers, failure conditions, casualties, trivia): "Exodus in
  America" (1st), "The Gates of El Presidio" (40th; giver Abraham Reyes; 300 fame, 350 with the Gold Medal, 125
  honor), "Bear One Another's Burdens" (42nd, first of West Elizabeth; giver Edgar Ross; High Power Pistol, 150 fame,
  200 with the Gold Medal, 25 honor; failure if the car is damaged or Ross, Fordham or Nastas is assaulted, killed or
  left to die; trivia: Galatians 6:2, Fordham starts the car from the driver's seat), "Great Men are Not Always Wise"
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

OWNERSHIP: narrative events live in part A (one line per mission here). Lines left to part B "In his own words" and
therefore NOT quoted here: "Marston, you're a public menace. We should've had you killed.", "It ends when we say it
ends. You're in no position to make demands.", "Like you always say, sir, the higher the stakes, the smarter you have
to play the game.", "See, this is what happens when you fraternize with savages...", "Van der Linde is a psychopath. A
murderer and a rapist.", "I don't understand you people...", "There's always somebody watching, Mr. Marston...", "But
you aren't from anywhere.", "We are neither, Mr. Marston." If part B uses a line quoted below, the fixer removes it
from one place. Ross's "Don't get snarky with me, Fordham." is quoted in edgar_B and only paraphrased in this fiche.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A1 = two("Act I: New Austin", "Acte I : New Austin")
A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")
A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
E2 = two("RDR2, epilogue II", "RDR2, épilogue II")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Fordham appears in six story missions of Red Dead Redemption, numbered 1, 40, 42, 43, 47 and 48 in the story order, and gives none of them. The last four belong to Edgar Ross's strand, which opens the West Elizabeth part of the game and ends with the death of Dutch van der Linde. The English-language Red Dead Wiki also places him in the last story mission, number 57. In Red Dead Redemption 2 he appears only in the end credits that follow \"American Venom\". Several missions fail if the player assaults or kills him.",
              "Fordham apparaît dans six missions principales de Red Dead Redemption, numérotées 1, 40, 42, 43, 47 et 48 dans l'ordre de l'histoire, et n'en confie aucune. Les quatre dernières appartiennent à la série d'Edgar Ross, qui ouvre la partie West Elizabeth du jeu et se clôt sur la mort de Dutch van der Linde. Le Red Dead Wiki anglophone le place aussi dans la dernière mission principale, la 57e. Dans Red Dead Redemption 2, il n'apparaît que dans le générique de fin qui suit \"American Venom\". Plusieurs missions échouent si le joueur l'agresse ou le tue.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Fordham's role", "Rôle de Fordham")], "rows": [
        M("Exodus in America", A1,
          "Escorts John with Ross from the Blackwater ferry to the train for Armadillo (named by the mission page; the transcript speaks of two lawmen). First mission of the game.",
          "Escorte John avec Ross du ferry de Blackwater jusqu'au train pour Armadillo (nommé par la page de la mission ; la transcription parle de deux hommes de loi). Première mission du jeu."),
        M("The Gates of El Presidio", A2,
          "Waits with Ross near the border bridge and takes Javier Escuella, alive or dead depending on the player's choice. Mission giver: Abraham Reyes. Rewards: 300 fame (350 with the Gold Medal) and 125 honor.",
          "Attend avec Ross près du pont de la frontière et récupère Javier Escuella, vivant ou mort selon le choix du joueur. Donneur de mission : Abraham Reyes. Récompenses : 300 points de célébrité (350 avec la médaille d'or) et 125 d'honneur."),
        M("Bear One Another's Burdens", A3,
          "Drives Ross and John to the wreck of the Serendipity, searches it with John, finds Nastas and repairs the car under fire. Mission giver: Edgar Ross. Rewards: High Power Pistol, 150 fame (200 with the Gold Medal) and 25 honor. Fails if the agents' car is damaged, or if Ross, Fordham or Nastas is attacked, killed or left to Dutch's men.",
          "Conduit Ross et John jusqu'à l'épave du Serendipity, la fouille avec John, trouve Nastas et répare la voiture sous les balles. Donneur de mission : Edgar Ross. Récompenses : pistolet High Power, 150 points de célébrité (200 avec la médaille d'or) et 25 d'honneur. Échec si la voiture des agents est endommagée, ou si Ross, Fordham ou Nastas est agressé, tué ou abandonné aux hommes de Dutch."),
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
          "According to the English-language Red Dead Wiki only: among the firing squad at the barn, and a possible casualty of John's last Dead Eye sequence. Last story mission of the game.",
          "Selon le seul Red Dead Wiki anglophone : présent dans le peloton d'exécution devant la grange, et victime possible de la dernière séquence en Dead Eye de John. Dernière mission principale du jeu."),
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
        {"q": two("Van der Linde is the priority. We go in, take him down and get the hell out of here. Quick and clean.", "Van der Linde is the priority. We go in, take him down and get the hell out of here. Quick and clean."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), on the way down to the wreck",
                    "Bear One Another's Burdens (RDR1, acte III), en descendant vers l'épave. Traduction : « Van der Linde est la priorité. On entre, on l'abat et on fiche le camp d'ici. Vite et proprement. »")},
        {"q": two("It doesn't feel right. This place is usually teeming with lowlifes.", "It doesn't feel right. This place is usually teeming with lowlifes."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), on the deserted wreck of the Serendipity",
                    "Bear One Another's Burdens (RDR1, acte III), sur l'épave déserte du Serendipity. Traduction : « Ça ne me dit rien de bon. D'habitude, l'endroit grouille de voyous. »")},
        {"q": two("I was trying to escape an ambush, sir.", "I was trying to escape an ambush, sir."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), when Ross blames the breakdown on his driving",
                    "Bear One Another's Burdens (RDR1, acte III), quand Ross met la panne sur le compte de sa conduite. Traduction : « J'essayais d'échapper à une embuscade, monsieur. »")},
        {"q": two("Our armed forces have no equal. We have made incredible progress the past few years.", "Our armed forces have no equal. We have made incredible progress the past few years."),
         "src": two("And You Will Know The Truth (RDR1, Act III), when John remarks that the machine gun is turning heads",
                    "And You Will Know The Truth (RDR1, acte III), quand John remarque que la mitrailleuse attire les regards. Traduction : « Nos forces armées n'ont pas d'égales. Nous avons fait des progrès incroyables ces dernières années. »")},
        {"q": two("And this isn't much more than a simple prototype. You should see what they're working on in Virginia. Soon there will be no war we can't win.", "And this isn't much more than a simple prototype. You should see what they're working on in Virginia. Soon there will be no war we can't win."),
         "src": two("And You Will Know The Truth (RDR1, Act III), on the way to the army camp",
                    "And You Will Know The Truth (RDR1, acte III), en route vers le camp de l'armée. Traduction : « Et ce n'est guère plus qu'un simple prototype. Vous devriez voir ce qu'ils préparent en Virginie. Bientôt, il n'y aura plus une guerre que nous ne puissions gagner. »")},
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
        {"q": two("Nice of you to help us out. Hell of a plan sendin' in two men to take on an entire gang of outlaws. Especially when one of them's an office clerk or social secretary or some such.", "Nice of you to help us out. Hell of a plan sendin' in two men to take on an entire gang of outlaws. Especially when one of them's an office clerk or social secretary or some such."),
         "src": two("John Marston, Bear One Another's Burdens (RDR1, Act III), to Ross, back in the car",
                    "John Marston, Bear One Another's Burdens (RDR1, acte III), à Ross, de retour dans la voiture. Traduction : « Merci du coup de main. Sacré plan, d'envoyer deux hommes contre toute une bande de hors-la-loi. Surtout quand l'un d'eux est un employé de bureau, un secrétaire mondain ou je ne sais quoi. »")},
        {"q": two("Perhaps if Mr. Fordham maneuvered it with a little more finesse.", "Perhaps if Mr. Fordham maneuvered it with a little more finesse."),
         "src": two("Edgar Ross, Bear One Another's Burdens (RDR1, Act III), when John complains about the automobile",
                    "Edgar Ross, Bear One Another's Burdens (RDR1, acte III), quand John se plaint de l'automobile. Traduction : « Peut-être que si M. Fordham la manœuvrait avec un peu plus de finesse. »")},
        {"q": two("I thought you were talkin' to Fordham.", "I thought you were talkin' to Fordham."),
         "src": two("John Marston, And You Will Know The Truth (RDR1, Act III), when Ross warns him that there must be no mistakes this time",
                    "John Marston, And You Will Know The Truth (RDR1, acte III), quand Ross le prévient qu'il n'y aura pas droit à l'erreur cette fois. Traduction : « Je croyais que vous parliez à Fordham. »")},
        {"q": two("Can't you hold this thing steady, Fordham?", "Can't you hold this thing steady, Fordham?"),
         "src": two("Edgar Ross, And You Will Know The Truth (RDR1, Act III), during the chase off the road",
                    "Edgar Ross, And You Will Know The Truth (RDR1, acte III), pendant la poursuite hors de la route. Traduction : « Vous ne pouvez pas tenir ce machin droit, Fordham ? »")},
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
        two("According to the mission page of \"Bear One Another's Burdens\", Fordham starts the automobile from the driver's seat with the ignition, which the page notes was rare for cars of the time.",
            "D'après la page de la mission \"Bear One Another's Burdens\", Fordham démarre l'automobile depuis le siège du conducteur, avec le contact, ce qui était rare sur les voitures de l'époque, note la page."),
        two("According to the Red Dead Wiki's page on the end credits of Red Dead Redemption 2, Ross and Fordham both wear Pinkerton badges in their 1907 scenes, although a newspaper of the epilogue reports that Ross now heads the Bureau of Investigation.",
            "D'après la page du Red Dead Wiki consacrée au générique de fin de Red Dead Redemption 2, Ross et Fordham portent tous deux un insigne Pinkerton dans leurs scènes de 1907, alors qu'un journal de l'épilogue annonce que Ross dirige désormais le Bureau of Investigation."),
        two("According to the mission page of \"Americans at Rest\" (Red Dead Redemption 2, chapter 2), the woman Ross and Fordham talk to in the Valentine saloon during the credits is one of the two women [[javier-escuella|Javier Escuella]] drinks with in that mission.",
            "D'après la page de la mission \"Americans at Rest\" (Red Dead Redemption 2, chapitre 2), la femme à qui Ross et Fordham parlent dans le saloon de Valentine pendant le générique est l'une des deux femmes avec qui [[javier-escuella|Javier Escuella]] boit dans cette mission."),
        two("A U.S. marshal, Isaac McKinnon, is often taken for Fordham in \"The Last Enemy That Shall Be Destroyed\", according to the English-language Red Dead Wiki: he stands near Ross after John's death, wears a similar dark three-piece suit and bowler hat, and has similar features. The French-language wiki goes further and holds that Fordham is not in the mission at all, and that the man seen beside Ross is McKinnon.",
            "Selon le Red Dead Wiki anglophone, un marshal, Isaac McKinnon, est souvent pris pour Fordham dans \"The Last Enemy That Shall Be Destroyed\" : il se tient près de Ross après la mort de John, porte un costume trois pièces sombre et un chapeau melon semblables, et lui ressemble de visage. Le wiki francophone va plus loin : selon lui, Fordham est absent de la mission, et l'homme vu aux côtés de Ross est McKinnon."),
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
