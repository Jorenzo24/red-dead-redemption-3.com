"""Landon Ricketts, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/, copies in
scripts/v3/work/landon/fc/):
- Character page "Landon Ricketts" (Mission appearances, Quotes incl. Multiplayer and Undead Nightmare lists,
  Trivia, Gallery captions) and FR page (Apparitions dans les missions, Anecdotes).
- Mission pages: "The Gunslinger's Tragedy" (30th mission, rewards, unlocks), "Landon Ricketts Rides Again"
  (trivia: train comments, near invincibility, Luisa strand unlocked), "Lucky in Love" (32nd mission, rewards,
  poker and dueling introduced, "Eva in Peril" unlocked), "The Mexican Wagon Train" (33rd mission, hijacking
  introduced, continuity trivia, prisoners' names), "Biographies and Lies" (quote box, Boom Bait reward);
  "We Shall Be Together in Paradise/dialogues" (Irish's "American guy", linked to Ricketts by the wiki);
  "Good, Honest, Snake Oil/dialogues" (RDR2 chapter 2, the Valentine lawman's line); "Further Questions of Female
  Suffrage" (RDR2 chapter 3, trivia line, as in sadie_C).
- Transcripts used word for word for every mission quote: "The Gunslinger's Tragedy/dialogues", "Landon Ricketts
  Rides Again/dialogues", "Lucky in Love/dialogues", "The Mexican Wagon Train/dialogues". Free-roam, multiplayer
  and Undead Nightmare lines come from the wiki's quote list; the "Biographies and Lies" welcome line from the
  mission page's quote box (no transcript exists for that mission).
- Other pages: "Famous Gunslingers Card Set" (card location), "Cigarette Cards Give Fame to Murderers" (RDR2
  newspaper: Blackwater Ledger No. 63, New Hanover Gazette No. 28, Saint Denis Times No. 44), "Wild West Heroes,
  No. 132" (full text of chapter VII, location), "Red Dead Online Ability Cards" (Landon's Patience, rank 18),
  "Myths and Mavericks" (contents, seven taunts, reuse of story lines, gallery captions), "Legends and Killers"
  (released August 10, 2010; contents), "Undead Nightmare" (multiplayer characters, undead lookalike models),
  "Casa Madrugada".
- Real world: Rockstar Newswire post "The Free Red Dead Redemption Myths and Mavericks Bonus Pack DLC Is Coming in
  September" (July 27, 2011; title checked on rockstargames.com, 20 Oct 2026; its naming of Ricketts as a playable
  character is taken from the wiki's citation of it); Myths and Mavericks free release September 13, 2011 (wiki,
  as in uncle_C and javier_C); RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 without multiplayer
  (as in uncle_C).

VERIFIED POINTS: chapter labels from the mission infoboxes ("Good, Honest, Snake Oil" chapter 2, "Further
Questions of Female Suffrage" chapter 3); the Lucky in Love casualty list credits Manolo Santander's death to
"either John Marston or Landon Ricketts"; the Wagon Train page spells the writer "Castilla", the transcript
"Castillo" (transcript followed in part A).

EXCLUDED: the Earp, Hickok, Michael Landon and Lee Van Cleef comparisons (real-world inspiration: part D, and
partly speculative); Rob Wiethoff naming "The Mexican Wagon Train" his favorite mission (real world, unsourced on
the wiki: left to part D if a source is found); weapons used in missions, Schofield preference vs Cattleman use,
Spanish (part B Skills); the "never married" trivia (no such line in the transcript); the "watery eye" reading;
"The Gunslinger's Tragedy" title as a GTA IV reference (the wiki says "could be"); Fermin Ichinaga "rescued twice"
(the wiki sentence is garbled, nothing confirms the first rescue); glitches (double Landon after Missing Persons,
freezing in the cave, Luisa vanishing on PS3, alternative pistols in the dynamite cutscene); the "1/4th chance"
spawn rate of the undead Ricketts (unverifiable figure; the appearance itself is kept, attributed); the FR wiki's
"Pistolet GP" and Ross Hagen's death (parts B and D).

OWNERSHIP: narrative events live in part A (one line per mission here). The Butcher Brothers, Blackwater and
Johnny West newspaper content is told in part A; the RDR2 newspaper about cigarette cards is told here only.
The Chicago biographer and Pittsburgh portrait are told in part A (Undead Nightmare), not repeated in Trivia.
Quotes picked here should not be repeated in part B "In his own words"; if part B uses one, the fixer removes
it from one place.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
A1 = two("Act I: New Austin", "Acte I : New Austin")
A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")
UNM = two("Undead Nightmare", "Undead Nightmare")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Ricketts has a strand of four story missions in the second act of Red Dead Redemption, all starting in Chuparosa. The first becomes available after \"We Shall Be Together in Paradise\", the last mission of the first act. \"The Gunslinger's Tragedy\" gives John the Schofield Revolver and the third level of Dead Eye. \"Landon Ricketts Rides Again\" opens the strand of [[luisa-fortuna|Luisa Fortuna]]. \"Lucky in Love\" introduces poker and duels, and unlocks the stranger mission \"Eva in Peril\". \"The Mexican Wagon Train\", which introduces the hijacking of vehicles, closes the strand and leads to the [[abraham-reyes|Abraham Reyes]] mission \"The Gates of El Presidio\". In Undead Nightmare, he gives one side mission.",
              "Ricketts propose une série de quatre missions principales dans le deuxième acte de Red Dead Redemption, toutes au départ de Chuparosa. La première se débloque après \"We Shall Be Together in Paradise\", dernière mission du premier acte. \"The Gunslinger's Tragedy\" apporte à John le revolver Schofield et le troisième niveau du Dead Eye. \"Landon Ricketts Rides Again\" ouvre la série de [[luisa-fortuna|Luisa Fortuna]]. \"Lucky in Love\" introduit le poker et les duels, et débloque la mission d'inconnu \"Eva in Peril\". \"The Mexican Wagon Train\", qui introduit le détournement de véhicules, clôt la série et mène à la mission d'[[abraham-reyes|Abraham Reyes]] \"The Gates of El Presidio\". Dans Undead Nightmare, il confie une mission secondaire.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Ricketts's role", "Rôle de Ricketts")], "rows": [
        M("The Gunslinger's Tragedy", A2,
          "Mission giver. Watches John kill the bandits of Chuparosa, trains him on bottles and vultures, then rides with him to save the bank's wagon. Rewards: Schofield Revolver, Dead Eye level 3, 100 honor and 75 fame.",
          "Donneur de mission. Voit John abattre les bandits de Chuparosa, l'entraîne sur des bouteilles et des vautours, puis l'accompagne pour sauver le chariot de la banque. Récompenses : revolver Schofield, Dead Eye niveau 3, 100 points d'honneur et 75 de célébrité."),
        M("Landon Ricketts Rides Again", A2,
          "Mission giver. Questions Emilio Fortuna about Escuella, then breaks Luisa out of the caves near El Matadero with John and blows her cell door with dynamite.",
          "Donneur de mission. Interroge Emilio Fortuna au sujet d'Escuella, puis fait évader Luisa des grottes d'El Matadero avec John et fait sauter la porte de sa cellule à la dynamite."),
        M("Lucky in Love", A2,
          "Mission giver. Invites John to his poker table, defuses the standoff with Müller and coaches John before the duel. Rewards: 50 dollars, 125 honor and 100 fame.",
          "Donneur de mission. Invite John à sa table de poker, désamorce l'impasse avec Müller et conseille John avant le duel. Récompenses : 50 dollars, 125 points d'honneur et 100 de célébrité."),
        M("The Mexican Wagon Train", A2,
          "Mission giver. Hears Luisa's plea, ambushes Allende's prison convoy with John and drives a wagon to American soil, where he says goodbye to John. Reward: 150 fame.",
          "Donneur de mission. Entend l'appel de Luisa, attaque avec John le convoi de prisonniers d'Allende et conduit un chariot jusqu'au sol américain, où il fait ses adieux à John. Récompense : 150 points de célébrité."),
        M("Biographies and Lies", UNM,
          "Side mission giver. Asks for Undead Bait and dynamite, makes Boom Bait and gives John two charges.",
          "Donneur de mission secondaire. Réclame des appâts et de la dynamite, fabrique des Boom Baits et en remet deux à John."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter or act", "Chapitre ou acte"), two("Link with Ricketts", "Lien avec Ricketts")], "rows": [
        M("We Shall Be Together in Paradise", A1,
          "[[irish|Irish]] tells John he once drank in Chuparosa with an American he saw shoot a man. The Red Dead Wiki identifies this American as Ricketts; Irish never gives a name.",
          "[[irish|Irish]] raconte à John qu'il a un jour bu à Chuparosa avec un Américain qu'il a vu abattre un homme. Le Red Dead Wiki identifie cet Américain à Ricketts ; Irish ne donne aucun nom."),
        M("Good, Honest, Snake Oil", C2,
          "In Red Dead Redemption 2, a Valentine lawman says the wanted snake-oil seller has killed more people than Landon Ricketts without pulling a trigger.",
          "Dans Red Dead Redemption 2, un homme de loi de Valentine affirme que le vendeur d'élixir recherché a tué plus de monde que Landon Ricketts sans jamais appuyer sur la détente."),
        M("Further Questions of Female Suffrage", C3,
          "In Red Dead Redemption 2, [[arthur-morgan|Arthur]] teases [[sadie-adler|Sadie]] after she starts a gunfight with the Lemoyne Raiders: \"A new pair of pants and you think you're Landon Ricketts\".",
          "Dans Red Dead Redemption 2, [[arthur-morgan|Arthur]] se moque de [[sadie-adler|Sadie]] après qu'elle a déclenché une fusillade contre les Lemoyne Raiders : \"A new pair of pants and you think you're Landon Ricketts\" (un pantalon neuf et tu te prends pour Landon Ricketts)."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the mission transcripts of the Red Dead Wiki. The free-roam, Undead Nightmare and multiplayer lines come from the wiki's quote list, and the welcome line of \"Biographies and Lies\" from its mission page, as no transcript exists for that mission.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Les répliques d'exploration libre, d'Undead Nightmare et du multijoueur proviennent de la liste de citations du wiki, et la phrase d'accueil de \"Biographies and Lies\", de la page de cette mission, faute de transcription.")},
    {"h4": two("Red Dead Redemption, Act II", "Red Dead Redemption, acte II")},
    {"quotes": [
        {"q": two("You kill peasants, you become a peasant.", "You kill peasants, you become a peasant."),
         "src": two("The Gunslinger's Tragedy (RDR1, Act II), to John, who has just killed the bandits of Chuparosa",
                    "The Gunslinger's Tragedy (RDR1, acte II), à John, qui vient d'abattre les bandits de Chuparosa. Traduction : « À tuer des paysans, on devient un paysan. »")},
        {"q": two("Landon Ricketts. Not a name that means much anymore.", "Landon Ricketts. Not a name that means much anymore."),
         "src": two("The Gunslinger's Tragedy (RDR1, Act II), introducing himself to John after the bottle practice",
                    "The Gunslinger's Tragedy (RDR1, acte II), quand il se présente à John après l'exercice des bouteilles. Traduction : « Landon Ricketts. Un nom qui ne veut plus dire grand-chose. »")},
        {"q": two("Yeah, killing men's a strange kind of fame. I was the fastest in my time. I must have been. I'm the only one left.", "Yeah, killing men's a strange kind of fame. I was the fastest in my time. I must have been. I'm the only one left."),
         "src": two("The Gunslinger's Tragedy (RDR1, Act II), to John, who remembers him as famous",
                    "The Gunslinger's Tragedy (RDR1, acte II), à John, qui se souvient de sa célébrité. Traduction : « Oui, tuer des hommes, c'est une drôle de célébrité. J'étais le plus rapide de mon temps. Je devais l'être. Je suis le seul qui reste. »")},
        {"q": two("Only a buzzard feeds on his friends.", "Only a buzzard feeds on his friends."),
         "src": two("The Gunslinger's Tragedy (RDR1, Act II), to John, who says he once rode with the men he hunts",
                    "The Gunslinger's Tragedy (RDR1, acte II), à John, qui dit avoir chevauché avec les hommes qu'il traque. Traduction : « Il n'y a qu'un vautour pour se nourrir de ses amis. »")},
        {"q": two("I didn't say I'd become a coward. I'm not going to stand by and watch good people suffer.", "I didn't say I'd become a coward. I'm not going to stand by and watch good people suffer."),
         "src": two("The Gunslinger's Tragedy (RDR1, Act II), to John, who mocks his quiet life during the wagon fight",
                    "The Gunslinger's Tragedy (RDR1, acte II), à John, qui raille sa vie tranquille pendant le combat autour du chariot. Traduction : « Je n'ai pas dit que j'étais devenu un lâche. Je ne vais pas rester là à regarder souffrir des braves gens. »")},
        {"q": two("Those who sit on the fence make a choice... in their own way. Don't you think, Mr. Marston?", "Those who sit on the fence make a choice... in their own way. Don't you think, Mr. Marston?"),
         "src": two("Landon Ricketts Rides Again (RDR1, Act II), to John, who says Emilio's troubles are not his own",
                    "Landon Ricketts Rides Again (RDR1, acte II), à John, qui dit que les ennuis d'Emilio ne le regardent pas. Traduction : « Ceux qui restent assis sur la barrière font un choix... à leur manière. Vous ne croyez pas, monsieur Marston ? »")},
        {"q": two("I'll tell you what choice I made. I'm a fighter, sir, and I'll fight to the end.", "I'll tell you what choice I made. I'm a fighter, sir, and I'll fight to the end."),
         "src": two("Landon Ricketts Rides Again (RDR1, Act II), to John, who calls him a man living in the past",
                    "Landon Ricketts Rides Again (RDR1, acte II), à John, qui le traite d'homme qui vit dans le passé. Traduction : « Je vais vous dire quel choix j'ai fait. Je suis un combattant, monsieur, et je me battrai jusqu'au bout. »")},
        {"q": two("She's a good woman, a teacher. If they lay a finger on her, I swear I'll feed those bastards their balls.", "She's a good woman, a teacher. If they lay a finger on her, I swear I'll feed those bastards their balls."),
         "src": two("Landon Ricketts Rides Again (RDR1, Act II), about Luisa Fortuna, on the ride to El Matadero",
                    "Landon Ricketts Rides Again (RDR1, acte II), au sujet de Luisa Fortuna, en route vers El Matadero. Traduction : « C'est une femme bien, une institutrice. S'ils osent la toucher, je jure que je ferai bouffer leurs couilles à ces salauds. »")},
        {"q": two("Very well, sir. Thank God my wife died. Unlucky in love, lucky in cards.", "Very well, sir. Thank God my wife died. Unlucky in love, lucky in cards."),
         "src": two("Lucky in Love (RDR1, Act II), to John, while winning at poker",
                    "Lucky in Love (RDR1, acte II), à John, alors qu'il gagne au poker. Traduction : « Très bien, monsieur. Dieu merci, ma femme est morte. Malheureux en amour, heureux au jeu. »")},
        {"q": two("An impasse, sir. An impasse. We could all die, here and now.", "An impasse, sir. An impasse. We could all die, here and now."),
         "src": two("Lucky in Love (RDR1, Act II), to Andreas Müller, as every gun in the cantina is drawn",
                    "Lucky in Love (RDR1, acte II), à Andreas Müller, quand toutes les armes de la cantina sont dégainées. Traduction : « Une impasse, monsieur. Une impasse. Nous pourrions tous mourir, ici et maintenant. »")},
        {"q": two("God, can't a man drink in peace? Come on, smoke these bastards up!", "God, can't a man drink in peace? Come on, smoke these bastards up!"),
         "src": two("Lucky in Love (RDR1, Act II), as the Stranger's accomplices open fire",
                    "Lucky in Love (RDR1, acte II), quand les complices de l'Étranger ouvrent le feu. Traduction : « Bon sang, on ne peut pas boire en paix ? Allez, fumons-moi ces salauds ! »")},
        {"q": two("I spent twenty-five years killing men. Look at me now. Sitting around here like some low rent would-be messiah. We're relics.", "I spent twenty-five years killing men. Look at me now. Sitting around here like some low rent would-be messiah. We're relics."),
         "src": two("The Mexican Wagon Train (RDR1, Act II), to John, who has told him about his mission for the Bureau",
                    "The Mexican Wagon Train (RDR1, acte II), à John, qui vient de lui parler de sa mission pour le Bureau. Traduction : « J'ai passé vingt-cinq ans à tuer des hommes. Regarde-moi maintenant. Assis là comme un messie de pacotille. Nous sommes des reliques. »")},
        {"q": two("Let's hang up our self-pity and go shoot ourselves some bad guys.", "Let's hang up our self-pity and go shoot ourselves some bad guys."),
         "src": two("The Mexican Wagon Train (RDR1, Act II), after Luisa's plea",
                    "The Mexican Wagon Train (RDR1, acte II), après l'appel de Luisa. Traduction : « Rangeons notre apitoiement et allons descendre quelques méchants. »")},
        {"q": two("Just be careful, John. Keep jumping from one side of the fence to the other, you might just get impaled on it.", "Just be careful, John. Keep jumping from one side of the fence to the other, you might just get impaled on it."),
         "src": two("The Mexican Wagon Train (RDR1, Act II), to John, on the ride to Escalera. The same fence line appears in the dime novel Wild West Heroes, No. 132 (see Other media)",
                    "The Mexican Wagon Train (RDR1, acte II), à John, en route vers Escalera. La même phrase sur la barrière figure dans le roman Wild West Heroes, No. 132 (voir Autres médias). Traduction : « Fais attention, John. À sauter sans cesse d'un côté à l'autre de la barrière, tu pourrais bien finir empalé dessus. »")},
        {"q": two("You know, you remind me a lot of myself. How I used to be. Stubborn and angry.", "You know, you remind me a lot of myself. How I used to be. Stubborn and angry."),
         "src": two("The Mexican Wagon Train (RDR1, Act II), to John, after their quarrel on the trail",
                    "The Mexican Wagon Train (RDR1, acte II), à John, après leur dispute en chemin. Traduction : « Tu sais, tu me rappelles beaucoup l'homme que j'étais. Têtu et en colère. »")},
        {"q": two("If you say so, Marston. If you say so.", "If you say so, Marston. If you say so."),
         "src": two("The Mexican Wagon Train (RDR1, Act II), his last words to John, who says he knows what he is looking for",
                    "The Mexican Wagon Train (RDR1, acte II), ses derniers mots à John, qui affirme savoir ce qu'il cherche. Traduction : « Si tu le dis, Marston. Si tu le dis. »")},
    ]},
    {"h4": two("Red Dead Redemption, free roam and combat", "Red Dead Redemption, exploration libre et combat")},
    {"quotes": [
        {"q": two("It's as good a place as any to call home. Warm sun, cheap liquor, and beautiful women.", "It's as good a place as any to call home. Warm sun, cheap liquor, and beautiful women."),
         "src": two("Red Dead Redemption, about Mexico (quote list of the wiki)",
                    "Red Dead Redemption, à propos du Mexique (liste de citations du wiki). Traduction : « C'est un endroit aussi bon qu'un autre pour se sentir chez soi. Du soleil, de l'alcool pas cher et de jolies femmes. »")},
        {"q": two("It's a terrible thing, getting older... Your looks have gone, your back hurts, and your pecker isn't working like it's supposed to.", "It's a terrible thing, getting older... Your looks have gone, your back hurts, and your pecker isn't working like it's supposed to."),
         "src": two("Red Dead Redemption (quote list of the wiki)",
                    "Red Dead Redemption (liste de citations du wiki). Traduction : « C'est terrible de vieillir... Ta beauté s'en va, ton dos te fait mal, et ta queue ne fonctionne plus comme elle devrait. »")},
        {"q": two("Chuparosa is my town!", "Chuparosa is my town!"),
         "src": two("Red Dead Redemption, during a shootout (quote list of the wiki)",
                    "Red Dead Redemption, pendant une fusillade (liste de citations du wiki). Traduction : « Chuparosa, c'est ma ville ! »")},
        {"q": two("It doesn't feel good getting executed, does it?", "It doesn't feel good getting executed, does it?"),
         "src": two("Red Dead Redemption, fighting the Mexican Army (quote list of the wiki)",
                    "Red Dead Redemption, face à l'armée mexicaine (liste de citations du wiki). Traduction : « Ça ne fait pas plaisir de se faire exécuter, hein ? »")},
        {"q": two("Manolo is sure getting lucky in the ass today.", "Manolo is sure getting lucky in the ass today."),
         "src": two("Red Dead Redemption, at the poker table when Manolo Santander wins chips (quote list of the wiki)",
                    "Red Dead Redemption, à la table de poker, quand Manolo Santander gagne des jetons (liste de citations du wiki). Traduction : « Manolo a une sacrée veine aujourd'hui. »")},
        {"q": two("I am not gonna give you a second chance to put that down, partner.", "I am not gonna give you a second chance to put that down, partner."),
         "src": two("Red Dead Redemption, if the player aims a weapon at him (quote list of the wiki)",
                    "Red Dead Redemption, si le joueur le met en joue (liste de citations du wiki). Traduction : « Je ne te laisserai pas une deuxième chance de baisser ça, l'ami. »")},
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"quotes": [
        {"q": two("Well, we got sunshine, sand and a plague that makes people want to eat each other. Come to think of it, it must feel just like America to you.", "Well, we got sunshine, sand and a plague that makes people want to eat each other. Come to think of it, it must feel just like America to you."),
         "src": two("Biographies and Lies (Undead Nightmare), welcoming John to Mexico (quote box of the mission page)",
                    "Biographies and Lies (Undead Nightmare), quand il accueille John au Mexique (citation de la page de la mission). Traduction : « Eh bien, on a du soleil, du sable et une épidémie qui donne envie aux gens de se manger entre eux. À bien y réfléchir, tu dois te sentir comme en Amérique. »")},
        {"q": two("I've killed all that can be killed.", "I've killed all that can be killed."),
         "src": two("Undead Nightmare (quote list of the wiki)",
                    "Undead Nightmare (liste de citations du wiki). Traduction : « J'ai tué tout ce qui pouvait l'être. »")},
        {"q": two("Truth is long dead.", "Truth is long dead."),
         "src": two("Undead Nightmare (quote list of the wiki)",
                    "Undead Nightmare (liste de citations du wiki). Traduction : « La vérité est morte depuis longtemps. »")},
    ]},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"quotes": [
        {"q": two("You have no idea who you're up against, do you?", "You have no idea who you're up against, do you?"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Tu n'as aucune idée de qui tu affrontes, pas vrai ? »")},
        {"q": two("I've been through the mill, but you're somethin' else.", "I've been through the mill, but you're somethin' else."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « J'en ai vu de toutes les couleurs, mais toi, tu es un cas. »")},
        {"q": two("You're as crazy as a sheep herder.", "You're as crazy as a sheep herder."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Tu es aussi fou qu'un berger. »")},
        {"q": two("Do I have to show you where the trigger is?", "Do I have to show you where the trigger is?"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Tu veux que je te montre où est la détente ? »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("According to the Red Dead Wiki, when the camera widens as John sits down at the poker table in \"Lucky in Love\", a few playing cards can be seen on Ricketts's right thigh, under the table.",
            "D'après le Red Dead Wiki, quand le plan s'élargit au moment où John s'assoit à la table de poker de \"Lucky in Love\", on aperçoit quelques cartes à jouer sur la cuisse droite de Ricketts, sous la table."),
        two("In \"Landon Ricketts Rides Again\", if John sets off on horseback and then jumps onto the train on the way, Ricketts comments on it, for example: \"So much for my relaxing train ride. Did you really miss me that much?\"",
            "Dans \"Landon Ricketts Rides Again\", si John part à cheval puis saute dans le train en route, Ricketts le relève, par exemple : \"So much for my relaxing train ride. Did you really miss me that much?\" (adieu mon voyage reposant en train ; je t'ai vraiment manqué à ce point ?)."),
        two("The mission page of \"Landon Ricketts Rides Again\" describes Ricketts as nearly invincible during the mission.",
            "La page de la mission \"Landon Ricketts Rides Again\" décrit Ricketts comme presque invincible pendant la mission."),
        two("In \"The Mexican Wagon Train\", Ricketts reproaches John for working for both sides of the war even if the player has done none of the missions of Vincente de Santa, Luisa Fortuna or Abraham Reyes.",
            "Dans \"The Mexican Wagon Train\", Ricketts reproche à John de travailler pour les deux camps même si le joueur n'a fait aucune mission de Vincente de Santa, de Luisa Fortuna ou d'Abraham Reyes."),
        two("None of the four prisoners named on the mission page of \"The Mexican Wagon Train\" is the writer or the local official Luisa describes at the start of the mission.",
            "Aucun des quatre prisonniers que nomme la page de la mission \"The Mexican Wagon Train\" n'est l'écrivain ou le fonctionnaire local que Luisa évoque au début de la mission."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"ul": [
        two("According to the Red Dead Wiki, if undead get into Casa Madrugada, for example during a Missing Persons mission, they do not attack Ricketts, and he does not treat them as a threat, however close they come.",
            "D'après le Red Dead Wiki, si des morts-vivants pénètrent dans Casa Madrugada, par exemple pendant une mission de personnes disparues, ils n'attaquent pas Ricketts, qui ne les considère pas non plus comme une menace, quelle que soit leur proximité."),
        two("After \"Biographies and Lies\", Ricketts sits on a chair in Casa Madrugada. Shooting a bottle near him, or his hat, makes him attack John. He can then be killed with no effect on the story, and Casa Madrugada stays a safe zone. According to the Red Dead Wiki, like Amos in the main game, he can survive a Cattleman Revolver shot to the face.",
            "Après \"Biographies and Lies\", Ricketts reste assis sur une chaise à Casa Madrugada. Tirer sur une bouteille près de lui, ou sur son chapeau, le pousse à attaquer John. On peut alors le tuer sans conséquence sur l'histoire, et Casa Madrugada reste une zone sûre. D'après le Red Dead Wiki, comme Amos dans le jeu principal, il peut survivre à une balle de Cattleman Revolver en plein visage."),
        two("Some undead in the expansion use a zombified lookalike of Ricketts, without his hat, and can appear among the hordes anywhere in the world, even before he is met alive in \"Biographies and Lies\". According to the Red Dead Wiki, Bolters and Retchers use this model, the Retchers with differences in design.",
            "Certains morts-vivants de l'extension reprennent un modèle zombifié de Ricketts, sans chapeau, et peuvent surgir au sein des hordes n'importe où, avant même que John ne le rencontre vivant dans \"Biographies and Lies\". D'après le Red Dead Wiki, ce modèle est utilisé par des Bolters et des Retchers, ces derniers avec quelques différences."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"p": two("Red Dead Redemption 2 (2018), set in 1899, never shows Ricketts but refers to him several times, besides the two mission lines listed above. A cigarette card of the Famous Gunslingers set shows him as a younger man; it lies on a barrel behind the house facing the undertaker in Armadillo. The newspaper article \"Cigarette Cards Give Fame to Murderers\", printed in the Blackwater Ledger, the New Hanover Gazette and the Saint Denis Times, describes the Falcon Claw tobacco set and says the Butcher Brothers featured in it ran afoul of the legendary gunslinger Landon Ricketts. According to the Red Dead Wiki, John can also mention him during a poker game in camp.",
              "Red Dead Redemption 2 (2018), qui se déroule en 1899, ne montre jamais Ricketts mais le cite à plusieurs reprises, en plus des deux répliques de mission mentionnées plus haut. Une carte de cigarettes de la collection Famous Gunslingers le représente plus jeune ; elle se trouve sur un tonneau derrière la maison qui fait face aux pompes funèbres d'Armadillo. L'article \"Cigarette Cards Give Fame to Murderers\", publié dans le Blackwater Ledger, la New Hanover Gazette et le Saint Denis Times, présente la collection du tabac Falcon Claw et rappelle que les Butcher Brothers qui y figurent ont croisé la route du légendaire pistolero Landon Ricketts. D'après le Red Dead Wiki, John peut aussi l'évoquer lors d'une partie de poker au camp.")},
    {"p": two("Ricketts also appears in the dime novel Wild West Heroes, No. 132, titled \"Mexican Ballad of Blood\", found on a nightstand in the main bedroom of Downes Ranch. In its chapter VII, the gunslinger Jim \"Boy\" Calloway, wearing a deputy's badge, creeps through a Mexican camp to reach a besieged fort. Ricketts shoots the knife out of his hand, knocks him down and holds a Schofield Revolver on him. He tells Calloway that the general he nearly killed hates the outlaw holed up in the fort as much as he does. He also says the line about jumping from one side of the fence to the other that he tells John in \"The Mexican Wagon Train\". According to the Red Dead Wiki, the book is one Arthur can give to [[jack-marston|Jack]].",
              "Ricketts figure aussi dans le roman de gare Wild West Heroes, No. 132, intitulé \"Mexican Ballad of Blood\", posé sur une table de nuit de la chambre principale de Downes Ranch. Dans son chapitre VII, le pistolero Jim \"Boy\" Calloway, une étoile d'adjoint sur la poitrine, se faufile dans un camp mexicain pour rejoindre un fort assiégé. Ricketts fait sauter son couteau d'un coup de feu, le met à terre et le tient en joue avec un revolver Schofield. Il explique à Calloway que le général qu'il a failli tuer hait autant que lui le hors-la-loi retranché dans le fort. Il prononce aussi la phrase sur la barrière qu'on enjambe d'un côté à l'autre, celle-là même qu'il adresse à John dans \"The Mexican Wagon Train\". D'après le Red Dead Wiki, Arthur peut offrir ce livre à [[jack-marston|Jack]].")},
    {"h4": two("Red Dead Online", "Red Dead Online")},
    {"p": two("Ricketts is neither seen nor named in Red Dead Online. One of its passive ability cards, Landon's Patience, unlocked at rank 18, refers to him: waiting up to 15 seconds between shots slightly increases the damage dealt.",
              "Ricketts n'apparaît pas et n'est pas nommé dans Red Dead Online. L'une de ses cartes de capacité passive, Landon's Patience, débloquée au rang 18, lui fait référence : attendre jusqu'à 15 secondes entre deux tirs augmente légèrement les dégâts infligés.")},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"p": two("Two versions of Ricketts are playable in the multiplayer mode of Red Dead Redemption. The Undead Nightmare pack of 2010 added Zombie Ricketts, an undead version of the character, in the Zombies section of the Outfitter. The Myths and Mavericks Bonus Pack then added the living Ricketts in the Revolution section. According to the Red Dead Wiki, a Rockstar Newswire post of July 27, 2011, which set a September release window, already named him as a playable character. The pack was released free on September 13, 2011 on PlayStation 3 and Xbox 360, with eight new character models, among them [[javier-escuella|Javier Escuella]], [[uncle|Uncle]], [[nastas|Nastas]] and [[vincente-de-santa|Vincente de Santa]].",
              "Deux versions de Ricketts sont jouables dans le multijoueur de Red Dead Redemption. Le pack Undead Nightmare, en 2010, ajoute Zombie Ricketts, une version morte-vivante du personnage, dans la section Zombies de l'Outfitter. Le Myths and Mavericks Bonus Pack ajoute ensuite le Ricketts vivant, dans la section Revolution. D'après le Red Dead Wiki, un billet du Rockstar Newswire du 27 juillet 2011, qui annonçait une sortie en septembre, le citait déjà parmi les personnages jouables. Le pack est publié gratuitement le 13 septembre 2011 sur PlayStation 3 et Xbox 360, avec huit nouveaux modèles de personnages, dont [[javier-escuella|Javier Escuella]], [[uncle|Uncle]], [[nastas|Nastas]] et [[vincente-de-santa|Vincente de Santa]].")},
    {"p": two("Like the other characters of the pack, Ricketts has only seven taunts. According to the Red Dead Wiki, Rockstar reused lines from the story mode for him rather than cast another actor, out of respect for his voice actor, who had died. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so neither Ricketts model is available in them.",
              "Comme les autres personnages du pack, Ricketts ne dispose que de sept provocations. D'après le Red Dead Wiki, Rockstar a repris pour lui des répliques du mode histoire plutôt que de faire appel à un autre comédien, par respect pour son interprète, qui venait de mourir. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : aucun des deux modèles de Ricketts n'y est donc disponible.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Ricketts for Red Dead Redemption, and a promotional screenshot showing him with John. For Undead Nightmare, an official artwork shows him as one of the undead. According to the Red Dead Wiki, the expansion's official trailer includes a shortened line from the start of \"Biographies and Lies\": \"I have never seen anything quite like this.\" According to their captions on the wiki, promotional images of Myths and Mavericks show Ricketts in a shootout at Nekoti Rock in which he kills Javier Escuella, in a Gang Shootout at Gaptooth Breach with Uncle and Nastas, and in a Stronghold match at Beecher's Hope with Uncle, Eli and Jonah. According to the Red Dead Wiki, Ricketts was also shown on the Xbox LIVE Marketplace and PlayStation Store to promote the Legends and Killers pack of August 10, 2010, although he is not in it: that pack's eight characters come from Red Dead Revolver.",
              "Rockstar a diffusé une illustration officielle de Ricketts pour Red Dead Redemption, ainsi qu'une capture promotionnelle qui le montre avec John. Pour Undead Nightmare, une illustration officielle le représente en mort-vivant. D'après le Red Dead Wiki, la bande-annonce officielle de l'extension reprend, en version raccourcie, une phrase du début de \"Biographies and Lies\" : \"I have never seen anything quite like this\" (je n'ai jamais rien vu de pareil). D'après leurs légendes sur le wiki, les images promotionnelles de Myths and Mavericks le montrent lors d'une fusillade à Nekoti Rock où il abat Javier Escuella, dans une partie de Gang Shootout à Gaptooth Breach avec Uncle et Nastas, et dans une partie de Stronghold à Beecher's Hope avec Uncle, Eli et Jonah. D'après le Red Dead Wiki, Ricketts a aussi servi à promouvoir sur le Xbox LIVE Marketplace et le PlayStation Store le pack Legends and Killers du 10 août 2010, alors qu'il n'y figure pas : les huit personnages de ce pack viennent de Red Dead Revolver.")},
]
