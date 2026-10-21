"""Seth Briars, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/, copies in
scripts/v3/work/seth/fc/):
- Character page "Seth Briars" (Mission appearances, Quotes, Trivia, Gallery captions) and FR page (Apparitions
  dans les missions, Anecdotes).
- Mission pages (infobox rewards, order numbers, prerequisites, unlocks, new game elements, failure conditions,
  trivia): "Exhuming and Other Fine Hobbies" (13th mission), "A Gentle Drive with Friends" (14th), "Let the Dead
  Bury Their Dead" (15th), "The Assault on Fort Mercer" (24th, per nigel_C), "Get Back in That Hole, Partner" and
  "On a Pale Horse" (Undead Nightmare, no transcript on the wiki), "Funny Man" (Part 1 unlocked by Seth's first
  mission).
- Transcripts used word for word for every mission quote: "Exhuming and Other Fine Hobbies/dialogues", "A Gentle
  Drive with Friends/dialogue", "Let the Dead Bury Their Dead/dialogues", "The Assault on Fort Mercer/dialogues",
  "You Shall Not Give False Testimony, Except for Profit/dialogues", "Liars, Cheats and Other Proud
  Americans/dialogues". Undead Nightmare lines come from the character page's quote list and gallery captions, and
  from the quote pages "Lucille Billingsgate" and the mission page's quote box (no transcript exists).
- Other pages: "Treasure" (Rank 4 treasure in the Tumbleweed mansion basement, found with treasure map 3), "Moses
  Forth" (Herbert Forth's tombstone), "Josephine Byrd" (grave opened with a fire bottle), "Mordecai Robbard's niece",
  "Francine", "Liars and Cheats" (released September 21, 2010; Seth in the Redemption list), "Undead Nightmare",
  "Red Dead Redemption: The Man from Blackwater" (aired on Fox on May 29, 2010; 5USA on June 5, 2010; scenes used).
- Real world: Liars and Cheats Pack details published by Rockstar on August 27, 2010 and released September 21,
  2010 (as in nigel_C, bonnie_C, jack_C); The Man from Blackwater, directed by John Hillcoat, aired on Fox on May 29,
  2010 (as in nigel_C, john_E); RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 without multiplayer (as
  in bonnie_C, nigel_C).

VERIFIED POINTS: the treasure Seth walks past is the one that the third treasure map leads to (character page:
"third treasure"; mission page: "Treasure Hunter Rank 4"; the Treasure page reconciles both: map 3 leads to the Rank 4
treasure in the mansion basement); the campfire story exists in two versions on the wiki (family gunned down, per the
character page; family eaten by a ghost, per the mission page): both given, no link to Seth's eye asserted; the
machine gun line in "A Gentle Drive with Friends" plays only if John already has the gun (mission page trivia).

EXCLUDED: "His last name is never mentioned" (character page trivia, contradicted by the 1914 newspaper, which
names him; names belong to part B); the Shaun of the Dead and Gollum comparisons and the Egyptian god Seth (the wiki's
own readings); split personality and the reading of his dislike of women (interpretation); the glass eye as the cause
of the plague or as a shield from the undead (GameStop preview reading and fan theory, both called wrong or
unproven by the wiki itself); the chair glitch at The Old Bacchus Place (glitch); Seth "relaxing" or "taming" the
undead (the wiki's reading); the FR wiki claims (homosexuality, abandonment by his father, family reunion in 1914);
the unused Red Dead Online model (cut content, part D) and Rob Wiethoff naming Seth his favorite character (part D);
"I hate the living" (wiki quote list without source or context, and close to the "I hate people" line kept for part
B); "Fly! Fly!" when riding (horse line, left to part B Skills); the movie line "I'm here to paint my picture" (gallery caption that differs from the quote list's wording).

OWNERSHIP: narrative events live in part A (one line per mission here). Lines likely used in part B "In his own
words" ("I hate people", "I've lost it all", "my mind's going", "I needs the map", "I don't like women") are not
quoted here. The 1911 and 1914 newspapers are told in part A only.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A1 = two("Act I: New Austin", "Acte I : New Austin")
UNM = two("Undead Nightmare", "Undead Nightmare")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Seth has a strand of three story missions in the first act of Red Dead Redemption, all in New Austin, numbered 13 to 15 in the story order. The first, \"Exhuming and Other Fine Hobbies\", becomes available once John has completed Bonnie MacFarlane's \"Wild Horses, Tamed Passions\" and Nigel West Dickens's \"You Shall Not Give False Testimony, Except for Profit\". It introduces wanted levels, bounties and hogtying, and unlocks the stranger mission \"Funny Man\". \"A Gentle Drive with Friends\" introduces fire bottles. \"Let the Dead Bury Their Dead\" is one of the four strands that must be completed before Leigh Johnson's \"The Assault on Fort Mercer\", with those of Johnson, Dickens and Irish. In Undead Nightmare, Seth gives one mission; completing it with Dickens's \"A Cure for Most of What Ails You\" unlocks the achievement \"Judge A Man By The...\".",
              "Seth propose une série de trois missions principales dans le premier acte de Red Dead Redemption, toutes dans le New Austin, numérotées de 13 à 15 dans l'ordre de l'histoire. La première, \"Exhuming and Other Fine Hobbies\", se débloque une fois terminées \"Wild Horses, Tamed Passions\", une mission de Bonnie MacFarlane, et \"You Shall Not Give False Testimony, Except for Profit\", une mission de Nigel West Dickens. Elle introduit les avis de recherche, les primes et le ligotage, et débloque la mission d'inconnu \"Funny Man\". \"A Gentle Drive with Friends\" introduit les cocktails incendiaires. \"Let the Dead Bury Their Dead\" fait partie des quatre séries à terminer avant \"The Assault on Fort Mercer\", la mission de Leigh Johnson, avec celles de Johnson, de Dickens et d'Irish. Dans Undead Nightmare, Seth confie une mission ; la terminer, ainsi que \"A Cure for Most of What Ails You\", de Dickens, débloque le succès \"Judge A Man By The...\".")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Seth's role", "Rôle de Seth")], "rows": [
        M("Exhuming and Other Fine Hobbies", A1,
          "Mission giver. Found robbing a grave at Coot's Chapel; with John's help, forces Moses Forth to give up the location of his half of the map. Rewards: 25 fame (75 with the gold medal) and a pardon letter.",
          "Donneur de mission. Surpris en train de piller une tombe à Coot's Chapel ; avec l'aide de John, force Moses Forth à révéler où se trouve sa moitié de carte. Récompenses : 25 points de célébrité (75 avec la médaille d'or) et une lettre de grâce."),
        M("A Gentle Drive with Friends", A1,
          "Mission giver. Searches corpses in the back of the wagon John drives to Tumbleweed, and finds the map. Rewards: 10 dollars, 2 medicines and 75 fame (125 with the gold medal).",
          "Donneur de mission. Fouille les cadavres à l'arrière du chariot que John conduit jusqu'à Tumbleweed, et trouve la carte. Récompenses : 10 dollars, 2 médicaments et 75 points de célébrité (125 avec la médaille d'or)."),
        M("Let the Dead Bury Their Dead", A1,
          "Mission giver. Leads John to the Tumbleweed mansion, where the chest holds only a glass eye. Rewards: 10 dollars, 150 fame (200 with the gold medal) and 100 honor.",
          "Donneur de mission. Conduit John jusqu'au manoir de Tumbleweed, où le coffre ne contient qu'un œil de verre. Récompenses : 10 dollars, 150 points de célébrité (200 avec la médaille d'or) et 100 points d'honneur."),
        M("The Assault on Fort Mercer", A1,
          "Already inside the fort, distracts the gang and welcomes Dickens's wagon through the gate. His last appearance in the story.",
          "Déjà dans le fort, distrait la bande et fait entrer le chariot de Dickens. Sa dernière apparition dans l'histoire."),
        M("Get Back in That Hole, Partner", UNM,
          "Mission giver. Sends John to cleanse three cemeteries, then points him to Mexico. Reward: The Old Bacchus Place as a safehouse.",
          "Donneur de mission. Envoie John purifier trois cimetières, puis l'oriente vers le Mexique. Récompense : The Old Bacchus Place comme refuge."),
        M("On a Pale Horse", UNM,
          "Seen stealing the mask from the Escalera catacombs, which raises the dead again.",
          "Aperçu en train de voler le masque dans les catacombes d'Escalera, ce qui relève de nouveau les morts."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Link with Seth", "Lien avec Seth")], "rows": [
        M("You Shall Not Give False Testimony, Except for Profit", A1,
          "Dickens sends John to Seth at Coot's Chapel.",
          "Dickens envoie John voir Seth à Coot's Chapel."),
        M("Liars, Cheats and Other Proud Americans", A1,
          "John tells Dickens he has met Seth; the two men discuss him on the road.",
          "John annonce à Dickens qu'il a rencontré Seth ; les deux hommes parlent de lui en chemin."),
        M("The Sport of Kings, and Liars", A1,
          "Dickens says the team will be ready once Seth and Irish have done their part.",
          "Dickens annonce que l'équipe sera prête quand Seth et Irish auront fait leur part."),
        M("Curious Tales from Blackwater", UNM,
          "Survivors name a freak with a glass eye among the possible causes of the plague.",
          "Des survivants citent un détraqué à l'œil de verre parmi les causes possibles de l'épidémie."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the mission transcripts of the Red Dead Wiki. The Undead Nightmare lines come from the wiki's quote list and mission pages, as no transcript exists for the expansion's missions.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Celles d'Undead Nightmare proviennent de la liste de citations et des pages de missions du wiki, faute de transcription pour les missions de l'extension.")},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("I want you to go see my old friend, Seth. He can come across as a little curious, but I'm sure you two will get on. He's most often found at Coot's Chapel. He's very devout.", "I want you to go see my old friend, Seth. He can come across as a little curious, but I'm sure you two will get on. He's most often found at Coot's Chapel. He's very devout."),
         "src": two("Nigel West Dickens, You Shall Not Give False Testimony, Except for Profit (RDR1, Act I)",
                    "Nigel West Dickens, You Shall Not Give False Testimony, Except for Profit (RDR1, acte I). Traduction : « Je veux que tu ailles voir mon vieil ami Seth. Il peut paraître un peu étrange, mais je suis sûr que vous vous entendrez. On le trouve le plus souvent à Coot's Chapel. Il est très pieux. »")},
        {"q": two("Yes, contemporary society is remarkably harsh on professional exhumers, but did you know, in Ancient Egypt, it was an art form more highly valued than literature? I believe Seth comes from that school of thought.", "Yes, contemporary society is remarkably harsh on professional exhumers, but did you know, in Ancient Egypt, it was an art form more highly valued than literature? I believe Seth comes from that school of thought."),
         "src": two("Nigel West Dickens, Liars, Cheats and Other Proud Americans (RDR1, Act I)",
                    "Nigel West Dickens, Liars, Cheats and Other Proud Americans (RDR1, acte I). Traduction : « Oui, la société moderne est remarquablement dure envers les exhumateurs de métier, mais saviez-vous que dans l'Égypte ancienne, c'était un art plus prisé que la littérature ? Je crois que Seth est de cette école. »")},
        {"q": two("A connection with them, more like. You and Seth have a lot in common. You both rob people, for one. Mind you, at least he waits until they're dead.", "A connection with them, more like. You and Seth have a lot in common. You both rob people, for one. Mind you, at least he waits until they're dead."),
         "src": two("John Marston, Liars, Cheats and Other Proud Americans (RDR1, Act I), after Dickens says he has a soft spot for life's flotsam and jetsam",
                    "John Marston, Liars, Cheats and Other Proud Americans (RDR1, acte I), quand Dickens avoue un faible pour les laissés-pour-compte. Traduction : « Des affinités avec eux, plutôt. Toi et Seth, vous avez beaucoup en commun. Vous volez les gens, déjà. Remarque, lui, au moins, il attend qu'ils soient morts. »")},
        {"q": two("You must be stupid, trustin' that crazy bastard. Seth'd sell his own mother. We'll split it between us, just me and you.", "You must be stupid, trustin' that crazy bastard. Seth'd sell his own mother. We'll split it between us, just me and you."),
         "src": two("Moses Forth to John, Exhuming and Other Fine Hobbies (RDR1, Act I), hogtied",
                    "Moses Forth à John, Exhuming and Other Fine Hobbies (RDR1, acte I), ligoté. Traduction : « Faut être idiot pour faire confiance à ce cinglé. Seth vendrait sa propre mère. On partagera entre nous, rien que toi et moi. »")},
        {"q": two("Thanks for all the hard work, Seth! Now kill 'em, boys!", "Thanks for all the hard work, Seth! Now kill 'em, boys!"),
         "src": two("A treasure hunter, Let the Dead Bury Their Dead (RDR1, Act I)",
                    "Un chasseur de trésor, Let the Dead Bury Their Dead (RDR1, acte I). Traduction : « Merci pour tout le boulot, Seth ! Allez, tuez-les, les gars ! »")},
        {"q": two("Seth has managed to get himself inside, but we can't leave it too long, or they will soon realize how very curious he is, and remove him from the premises, or slit his throat and watch him bleed to death, but for a minute, he will delight and amuse them. That's when he'll get us inside.", "Seth has managed to get himself inside, but we can't leave it too long, or they will soon realize how very curious he is, and remove him from the premises, or slit his throat and watch him bleed to death, but for a minute, he will delight and amuse them. That's when he'll get us inside."),
         "src": two("Nigel West Dickens, The Assault on Fort Mercer (RDR1, Act I), as Seth dances on the wall",
                    "Nigel West Dickens, The Assault on Fort Mercer (RDR1, acte I), pendant que Seth danse sur le mur. Traduction : « Seth a réussi à entrer, mais il ne faut pas tarder, sinon ils vont vite comprendre à quel point il est bizarre et le jeter dehors, ou lui trancher la gorge et le regarder se vider de son sang ; mais pendant une minute, il va les ravir et les amuser. C'est là qu'il nous fera entrer. »")},
        {"q": two("It's the glass eye! The freak with the glass eye! He caused this!", "It's the glass eye! The freak with the glass eye! He caused this!"),
         "src": two("Lucille Billingsgate, Undead Nightmare, on the cause of the plague (quoted on her page of the Red Dead Wiki)",
                    "Lucille Billingsgate, Undead Nightmare, sur la cause de l'épidémie (citée sur sa page du Red Dead Wiki). Traduction : « C'est l'œil de verre ! Le détraqué à l'œil de verre ! C'est lui qui a fait ça ! »")},
    ]},
    {"h4": two("Red Dead Redemption, Act I", "Red Dead Redemption, acte I")},
    {"quotes": [
        {"q": two("Marston: How can you sink that low? Diggin' up graves and lootin' from the dead. / Seth: Hypocrites, the whole damn lotta you! Are you sayin' it's better to steal from the livin'? They're corpses. They don't care none.", "Marston: How can you sink that low? Diggin' up graves and lootin' from the dead. / Seth: Hypocrites, the whole damn lotta you! Are you sayin' it's better to steal from the livin'? They're corpses. They don't care none."),
         "src": two("Exhuming and Other Fine Hobbies (RDR1, Act I), on the ride to Benedict Point",
                    "Exhuming and Other Fine Hobbies (RDR1, acte I), en route vers Benedict Point. Traduction : « Marston : Comment peut-on tomber aussi bas ? Déterrer des tombes et dépouiller les morts. / Seth : Tous des hypocrites, autant que vous êtes ! Tu veux dire que c'est mieux de voler les vivants ? Ce sont des cadavres. Ils s'en fichent. »")},
        {"q": two("Seth: Are we really livin' anyway? Do you exist outside my mind? Maybe we're both havin' the same dream and when we wake up we'll die? / Marston: I certainly seem to be in some kind of nightmare.", "Seth: Are we really livin' anyway? Do you exist outside my mind? Maybe we're both havin' the same dream and when we wake up we'll die? / Marston: I certainly seem to be in some kind of nightmare."),
         "src": two("Exhuming and Other Fine Hobbies (RDR1, Act I)",
                    "Exhuming and Other Fine Hobbies (RDR1, acte I). Traduction : « Seth : Est-ce qu'on est vraiment vivants, d'abord ? Est-ce que tu existes en dehors de ma tête ? Peut-être qu'on fait le même rêve et qu'on mourra en se réveillant ? / Marston : En tout cas, j'ai l'impression d'être dans une sorte de cauchemar. »")},
        {"q": two("Seth: Have you looked in the cave, Seth? No, it's very dark. / Marston: What did you say? / Seth: I-I didn't say nothin'.", "Seth: Have you looked in the cave, Seth? No, it's very dark. / Marston: What did you say? / Seth: I-I didn't say nothin'."),
         "src": two("Exhuming and Other Fine Hobbies (RDR1, Act I), Seth answering himself",
                    "Exhuming and Other Fine Hobbies (RDR1, acte I), Seth se répondant à lui-même. Traduction : « Seth : T'as regardé dans la grotte, Seth ? Non, il fait très noir. / Marston : Qu'est-ce que tu as dit ? / Seth : J-j'ai rien dit. »")},
        {"q": two("Marston: Seth, I need someone who can get a wagon inside Fort Mercer. I was told you could help me but I'm not sure you even know what day it is. / Seth: I don't. I can't even tell you what year it is.", "Marston: Seth, I need someone who can get a wagon inside Fort Mercer. I was told you could help me but I'm not sure you even know what day it is. / Seth: I don't. I can't even tell you what year it is."),
         "src": two("Exhuming and Other Fine Hobbies (RDR1, Act I)",
                    "Exhuming and Other Fine Hobbies (RDR1, acte I). Traduction : « Marston : Seth, j'ai besoin de quelqu'un qui puisse faire entrer un chariot dans Fort Mercer. On m'a dit que tu pourrais m'aider, mais je ne suis même pas sûr que tu saches quel jour on est. / Seth : Je ne sais pas. Je ne pourrais même pas te dire en quelle année on est. »")},
        {"q": two("Seth: Then I'm gonna cut you up piece by piece, 'til ya find your tongue. / Marston: Friend, this man's gone crazy in the sun. I suggest you take my advice and start talking. / Seth: Shut up, Marston, I wanna cut into a bonafide man's flesh! Ain't never cut into a live one before.", "Seth: Then I'm gonna cut you up piece by piece, 'til ya find your tongue. / Marston: Friend, this man's gone crazy in the sun. I suggest you take my advice and start talking. / Seth: Shut up, Marston, I wanna cut into a bonafide man's flesh! Ain't never cut into a live one before."),
         "src": two("Exhuming and Other Fine Hobbies (RDR1, Act I), threatening Moses Forth at Benedict Point",
                    "Exhuming and Other Fine Hobbies (RDR1, acte I), en menaçant Moses Forth à Benedict Point. Traduction : « Seth : Alors je vais te découper morceau par morceau, jusqu'à ce que ta langue se délie. / Marston : L'ami, cet homme a pris un coup de soleil sur la tête. Je te conseille de m'écouter et de parler. / Seth : La ferme, Marston, je veux entailler de la vraie chair d'homme ! J'en ai jamais découpé un vivant. »")},
        {"q": two("Marston: You're not even going to wait until they're buried before you... / Seth: Well they don't care, do ya boys? Honest folk, off to a better place.", "Marston: You're not even going to wait until they're buried before you... / Seth: Well they don't care, do ya boys? Honest folk, off to a better place."),
         "src": two("A Gentle Drive with Friends (RDR1, Act I), about the bodies in the wagon",
                    "A Gentle Drive with Friends (RDR1, acte I), à propos des corps dans le chariot. Traduction : « Marston : Tu n'attends même pas qu'ils soient enterrés pour... / Seth : Bah, ça leur est égal, pas vrai, les gars ? D'honnêtes gens, partis pour un monde meilleur. »")},
        {"q": two("Seth: You remind me why I hate people. For a man who kills so much, you sure seem to have a problem with the dead. Life kills everyone in the end. They ain't so different from you and me. / Marston: Aside from them being dead and rotting, I guess they ain't...", "Seth: You remind me why I hate people. For a man who kills so much, you sure seem to have a problem with the dead. Life kills everyone in the end. They ain't so different from you and me. / Marston: Aside from them being dead and rotting, I guess they ain't..."),
         "src": two("A Gentle Drive with Friends (RDR1, Act I), after John calls him a sick man",
                    "A Gentle Drive with Friends (RDR1, acte I), quand John le traite de malade. Traduction : « Seth : Tu me rappelles pourquoi je déteste les gens. Pour un homme qui tue autant, tu as l'air d'avoir un sacré problème avec les morts. La vie finit par tuer tout le monde. Ils ne sont pas si différents de toi et moi. / Marston : À part qu'ils sont morts et qu'ils pourrissent, je suppose que non... »")},
        {"q": two("Christ alive! It's the map! I found the map! Go left up here! Looks like the treasure's in Tumbleweed! That's where I was headed! It's fate!", "Christ alive! It's the map! I found the map! Go left up here! Looks like the treasure's in Tumbleweed! That's where I was headed! It's fate!"),
         "src": two("A Gentle Drive with Friends (RDR1, Act I), searching the bodies during the chase",
                    "A Gentle Drive with Friends (RDR1, acte I), en fouillant les corps pendant la poursuite. Traduction : « Bon sang de bonsoir ! C'est la carte ! J'ai trouvé la carte ! À gauche, là-haut ! On dirait que le trésor est à Tumbleweed ! C'est là que j'allais ! C'est le destin ! »")},
        {"q": two("Yeee Hooo! Finally, I see the light at the end of this very long, long tunnel. Seth's gonna be rich after all these years... It's silk sheets and Parisian whores from now on, mister!", "Yeee Hooo! Finally, I see the light at the end of this very long, long tunnel. Seth's gonna be rich after all these years... It's silk sheets and Parisian whores from now on, mister!"),
         "src": two("Let the Dead Bury Their Dead (RDR1, Act I), on finding the chest",
                    "Let the Dead Bury Their Dead (RDR1, acte I), en découvrant le coffre. Traduction : « Youhou ! Enfin, je vois la lumière au bout de ce très, très long tunnel. Seth va être riche, après toutes ces années... Désormais, ce sera draps de soie et putains parisiennes, mon gars ! »")},
        {"q": two("Seth: What the goddamn hell is this? A glass eye? / Marston: I'm sure whoever that belonged to treasured it very much.", "Seth: What the goddamn hell is this? A glass eye? / Marston: I'm sure whoever that belonged to treasured it very much."),
         "src": two("Let the Dead Bury Their Dead (RDR1, Act I), on opening the chest",
                    "Let the Dead Bury Their Dead (RDR1, acte I), à l'ouverture du coffre. Traduction : « Seth : Qu'est-ce que c'est que ce foutu bordel ? Un œil de verre ? / Marston : Je suis sûr que son propriétaire y tenait comme à un trésor. »")},
        {"q": two("Hunting dead men's treasure ain't done me no favors. Sure. Sure, I'm ready for the living. I'll see you and Mr. West Dickens over at Fort Mercer when you gentlemen is ready.", "Hunting dead men's treasure ain't done me no favors. Sure. Sure, I'm ready for the living. I'll see you and Mr. West Dickens over at Fort Mercer when you gentlemen is ready."),
         "src": two("Let the Dead Bury Their Dead (RDR1, Act I), the last line of his strand",
                    "Let the Dead Bury Their Dead (RDR1, acte I), dernière réplique de sa série. Traduction : « Courir après le trésor des morts ne m'a rien rapporté de bon. D'accord. D'accord, je suis prêt pour les vivants. On se retrouve à Fort Mercer, toi et M. West Dickens, quand vous serez prêts, messieurs. »")},
        {"q": two("Hey, hey there! Come on in, come on in. Welcome to my humble abode! Come on.", "Hey, hey there! Come on in, come on in. Welcome to my humble abode! Come on."),
         "src": two("The Assault on Fort Mercer (RDR1, Act I), opening the gate to Dickens's wagon",
                    "The Assault on Fort Mercer (RDR1, acte I), en ouvrant la porte au chariot de Dickens. Traduction : « Hé, salut ! Entrez, entrez. Bienvenue dans mon humble demeure ! Allez, venez. »")},
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"quotes": [
        {"q": two("It ain't nothin'.", "It ain't nothin'."),
         "src": two("Get Back in That Hole, Partner (Undead Nightmare), when John asks him about the plague (quote box of the mission page)",
                    "Get Back in That Hole, Partner (Undead Nightmare), quand John l'interroge sur l'épidémie (encadré de la page de la mission). Traduction : « C'est rien du tout. »")},
        {"q": two("Folks? Folks! Folks! Damn them folks, John Marston! Damn them! And damn you!", "Folks? Folks! Folks! Damn them folks, John Marston! Damn them! And damn you!"),
         "src": two("Get Back in That Hole, Partner (Undead Nightmare), when John says Blackwater blames the plague on his glass eye (quote list of the wiki)",
                    "Get Back in That Hole, Partner (Undead Nightmare), quand John lui apprend que Blackwater accuse son œil de verre (liste de citations du wiki). Traduction : « Les gens ? Les gens ! Les gens ! Au diable les gens, John Marston ! Au diable ! Et toi avec ! »")},
        {"q": two("Moses wouldn't hurt a fly, would you darling?", "Moses wouldn't hurt a fly, would you darling?"),
         "src": two("Undead Nightmare, to John (quote list of the wiki)",
                    "Undead Nightmare, à John (liste de citations du wiki). Traduction : « Moses ne ferait pas de mal à une mouche, pas vrai, mon chou ? »")},
        {"q": two("Moses is having a tough time right now. Ain't ya, pal?", "Moses is having a tough time right now. Ain't ya, pal?"),
         "src": two("Get Back in That Hole, Partner (Undead Nightmare), at the card table (gallery caption of the wiki)",
                    "Get Back in That Hole, Partner (Undead Nightmare), à la table de jeu (légende d'une image du wiki). Traduction : « Moses traverse une mauvaise passe en ce moment. Pas vrai, mon vieux ? »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("In \"Let the Dead Bury Their Dead\", Seth walks through the basement of the Tumbleweed mansion past a real treasure: the one that the third treasure map of the Treasure Hunter challenge leads to, which gives Rank 4. If the player has already dug it up, there is nothing left there.",
            "Dans \"Let the Dead Bury Their Dead\", Seth traverse la cave du manoir de Tumbleweed en passant à côté d'un vrai trésor : celui que désigne la troisième carte du défi de chasseur de trésor, qui donne le rang 4. Si le joueur l'a déjà déterré, il n'y a plus rien."),
        two("Strangers at campfires sometimes tell a story about a family in Tumbleweed of whom nothing was left but a glass eye. The Red Dead Wiki gives two versions: on the character page, the family is gunned down and its possessions destroyed; on the mission page, it is eaten by a ghost.",
            "Autour des feux de camp, des inconnus racontent parfois l'histoire d'une famille de Tumbleweed dont il ne serait resté qu'un œil de verre. Le Red Dead Wiki en donne deux versions : sur la page du personnage, la famille est abattue et ses biens détruits ; sur celle de la mission, elle est dévorée par un fantôme."),
        two("The title \"Let the Dead Bury Their Dead\" quotes Jesus in Matthew 8:22 and Luke 9:60, answering a disciple who asks to bury his father first.",
            "Le titre \"Let the Dead Bury Their Dead\" reprend une parole de Jésus (Matthieu 8:22 et Luc 9:60), adressée à un disciple qui demande d'abord à enterrer son père."),
        two("At the end of \"Exhuming and Other Fine Hobbies\", the player can pay off the bounty with money instead and keep the pardon letter. According to the mission page, Seth does not die if John shoots him at the start of the mission: he gets up and runs away.",
            "À la fin de \"Exhuming and Other Fine Hobbies\", le joueur peut payer la prime avec son argent et garder la lettre de grâce. D'après la page de la mission, Seth ne meurt pas si John lui tire dessus au début : il se relève et s'enfuit."),
        two("According to the mission page of \"A Gentle Drive with Friends\", the first body in the wagon uses the same model as Sam Odessa, found dead outside Tumbleweed. If the player drives through Armadillo against Seth's advice, extra lines play, and a lawman who sees the wagon stopped for long enough examines it, which fails the mission.",
            "D'après la page de la mission \"A Gentle Drive with Friends\", le premier corps du chariot reprend le modèle de Sam Odessa, retrouvé mort près de Tumbleweed. Si le joueur traverse Armadillo malgré le conseil de Seth, des répliques supplémentaires se déclenchent, et un représentant de la loi qui voit le chariot arrêté trop longtemps vient l'inspecter, ce qui fait échouer la mission."),
        two("According to the Red Dead Wiki, Josephine Byrd, whose grave Seth digs up at Coot's Chapel, died on April 1, 1878. Her grave can be opened with a fire bottle, and her body wears the same trousers as Seth.",
            "D'après le Red Dead Wiki, Josephine Byrd, dont Seth ouvre la tombe à Coot's Chapel, est morte le 1er avril 1878. Sa tombe peut être ouverte avec un cocktail incendiaire, et son corps porte le même pantalon que Seth."),
        two("According to the Red Dead Wiki, Moses Forth's father, Herbert Forth, is buried in the Tumbleweed cemetery, under a tombstone that reads \"This is one grave he cannot rob.\"",
            "D'après le Red Dead Wiki, le père de Moses Forth, Herbert Forth, est enterré au cimetière de Tumbleweed, sous une pierre tombale où l'on lit \"This is one grave he cannot rob.\" (voilà une tombe qu'il ne pourra pas piller)."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"ul": [
        two("According to the Red Dead Wiki, Seth and the niece of Mordecai Robbard are the only characters the undead never attack. The wiki also says that Seth and Nigel West Dickens are the only uninfected major characters of the expansion who never fight the undead.",
            "D'après le Red Dead Wiki, Seth et la nièce de Mordecai Robbard sont les seuls personnages que les morts-vivants n'attaquent jamais. Le wiki ajoute que Seth et Nigel West Dickens sont les seuls personnages majeurs non infectés de l'extension à ne jamais combattre les morts-vivants."),
        two("The undead at Seth's party cannot be shot, but a stick of dynamite or a fire bottle can kill them. According to the mission page, if Seth survives, he draws a revolver, fires at John and tries to flee. John can kill him, but this changes nothing: Seth still steals the mask at the end of the expansion.",
            "Les morts-vivants de la fête de Seth sont insensibles aux balles, mais un bâton de dynamite ou un cocktail incendiaire peut les tuer. D'après la page de la mission, si Seth en réchappe, il sort un revolver, tire sur John et tente de s'enfuir. John peut l'abattre, mais cela ne change rien : Seth vole quand même le masque à la fin de l'extension."),
        two("According to the Red Dead Wiki, when John searches the bodies of the undead, he can say \"Seth, I'm sorry about all the insults\", \"Seth, finally I've joined you\" or \"Seth, how do you enjoy this?\".",
            "D'après le Red Dead Wiki, quand John fouille les corps des morts-vivants, il peut dire \"Seth, I'm sorry about all the insults\" (Seth, désolé pour toutes ces insultes), \"Seth, finally I've joined you\" (Seth, me voilà enfin des tiens) ou \"Seth, how do you enjoy this?\" (Seth, ça te plaît ?)."),
        two("\"Get Back in That Hole, Partner\" is also the title of a track on the Undead Nightmare soundtrack.",
            "\"Get Back in That Hole, Partner\" est aussi le titre d'un morceau de la bande originale d'Undead Nightmare."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("The Man from Blackwater (2010)", "The Man from Blackwater (2010)")},
    {"p": two("Seth appears in Red Dead Redemption: The Man from Blackwater, a short film made with the game's engine, directed by John Hillcoat and broadcast by Fox on May 29, 2010, then by 5USA in the United Kingdom on June 5, 2010. The film follows the first act and reuses his meeting with John and the confrontation with Moses Forth from \"Exhuming and Other Fine Hobbies\". Its final segment changes the order of events: the map leads to Fort Mercer, and Seth finds the glass eye in a room of the fort, a scene taken from the Tumbleweed mansion of \"Let the Dead Bury Their Dead\". According to the Red Dead Wiki's quote list, he says in the film: \"Put me on a cross and paint my picture\" and \"I'm gonna make you a nose check.\"",
              "Seth apparaît dans Red Dead Redemption: The Man from Blackwater, un court métrage réalisé avec le moteur du jeu par John Hillcoat, diffusé par Fox le 29 mai 2010, puis par 5USA au Royaume-Uni le 5 juin 2010. Le film reprend le premier acte, dont sa rencontre avec John et la confrontation avec Moses Forth de \"Exhuming and Other Fine Hobbies\". Son dernier segment bouscule l'ordre des événements : la carte mène à Fort Mercer, et Seth trouve l'œil de verre dans une pièce du fort, une scène tirée du manoir de Tumbleweed de \"Let the Dead Bury Their Dead\". D'après la liste de citations du Red Dead Wiki, il y dit : \"Put me on a cross and paint my picture\" (clouez-moi sur une croix et faites mon portrait) et \"I'm gonna make you a nose check.\"")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Seth became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. Players select him in the Redemption section of the Outfitter, alongside [[john-marston|John]], [[abigail-marston|Abigail]], [[jack-marston|Jack]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[leigh-johnson|Leigh Johnson]], [[luisa-fortuna|Luisa Fortuna]] and [[nigel-west-dickens|Nigel West Dickens]]. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, do not include the multiplayer mode.",
              "Seth devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. On le choisit dans la section Redemption de l'Outfitter, aux côtés de [[john-marston|John]], d'[[abigail-marston|Abigail]], de [[jack-marston|Jack]], de [[bonnie-macfarlane|Bonnie MacFarlane]], de [[leigh-johnson|Leigh Johnson]], de [[luisa-fortuna|Luisa Fortuna]] et de [[nigel-west-dickens|Nigel West Dickens]]. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, ne comprennent pas le multijoueur.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Seth for Red Dead Redemption; according to the Red Dead Wiki, it shows him with longer, thicker hair than in the game. According to the same wiki, the debut trailer of Undead Nightmare opens on Moses Forth digging up a grave at Coot's Chapel before an undead Bruiser charges and devours him, and briefly shows Josephine Byrd's tombstone stained with blood.",
              "Rockstar a diffusé une illustration officielle de Seth pour Red Dead Redemption ; d'après le Red Dead Wiki, il y a les cheveux plus longs et plus épais que dans le jeu. Toujours selon ce wiki, la première bande-annonce d'Undead Nightmare s'ouvre sur Moses Forth en train de déterrer une tombe à Coot's Chapel, avant qu'un Bruiser mort-vivant ne le charge et ne le dévore, et montre brièvement la pierre tombale de Josephine Byrd tachée de sang.")},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"p": two("Seth does not appear in Red Dead Redemption 2, which is set in 1899. The Red Dead Wiki's character page lists only Red Dead Redemption and its Undead Nightmare expansion among his games, and the wiki records no mention of him in the later game.",
              "Seth n'apparaît pas dans Red Dead Redemption 2, qui se déroule en 1899. La page du personnage sur le Red Dead Wiki ne cite que Red Dead Redemption et son extension Undead Nightmare parmi ses jeux, et le wiki ne relève aucune mention de lui dans le second opus.")},
]
