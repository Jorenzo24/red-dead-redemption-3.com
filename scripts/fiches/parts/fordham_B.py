"""Archer Fordham, part B: Personality (official description, observable traits, In his own words, Names, Appearance),
Weapons and the automobile (the fiche-specific skills section), Relationships (22 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN infobox (gender, location, affiliations, family, occupation, weapons, voice), the GOTY
guide quote box, the Personality and Appearance sections, the trivia items on his weapons and on his presence at
Beecher's Hope; the FR wiki infobox (allié, ennemi, arme, véhicule); the mission pages and transcripts listed in
fordham/missions.txt. Narrative events are told in part A; the entries below point to them.

SOURCE REGISTER (read 22 Oct 2026; wiki cache scripts/v3/work/_m/):
- Official description: the Game of the Year Edition guide, quoted in the Background quote box of the Red Dead Wiki EN
  page ("GOTY guide description."). The guide itself was not read and the sentence was not found elsewhere (web search
  22 Oct 2026): quoted through the wiki, attributed. Rockstar's 6 Sep 2018 descriptions (sources/thr_descriptions.txt)
  cover the RDR2 gang only: none for Fordham.
- Transcripts (every quoted line checked): "The Gates of El Presidio/dialogues" (both branches), "Bear One Another's
  Burdens/dialogues", "Great Men are Not Always Wise/dialogues", "And You Will Know The Truth/dialogues", "And The Truth
  Will Set You Free/dialogues". Fordham has no line in "Exodus in America/dialogues" (the two escorts are unnamed
  "lawmen" there; the mission page names Ross and Fordham) nor in "The Last Enemy That Shall Be Destroyed/dialogues".
  The RDR2 "Ending Credits" page has no transcript.
- Mission pages: failure conditions of "Bear One Another's Burdens" (car, Ross, Fordham, Nastas), "Great Men are Not
  Always Wise" (Ross, Fordham, lawmen; Ross and Fordham use the Winchester Repeater), "And You Will Know The Truth"
  (Ross, Fordham; the Browning gun); the ignition trivia and the engine cranked by Fordham ("Bear One Another's
  Burdens"); "The Last Enemy That Shall Be Destroyed" (casualties: Fordham can be shot in the last Dead Eye sequence
  and disappears afterwards whether shot or not; Ross cannot be killed).
- Red Dead Wiki "Archer Fordham": infobox (Cattleman Revolver, High Power Pistol, Winchester Repeater; mother Maybelle),
  trivia (Cattleman early, High Power Pistol later, as Ross; Maybelle's grave), Appearance section (taller than Ross
  in 1911). FR wiki infobox: Ford Model T as vehicle (not used: model name unsupported by any transcript).
- Consistency: edgar_B (Fordham entry: "trite", "snarky"; "We are neither, Mr. Marston." quoted there), bill_B,
  abigail_B, nastas_B, macdougal_B, dutch_B/dutch_C (Cochinay exchange), HOUSE_FACTS (Beecher's Hope 1911 attributed
  to the wiki; Javier's fate = player's choice).
- Visual check: live portrait.jpeg (1911, interior, with John) and gallery-1.jpeg (1907, outdoors), for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only (part C Quotes must not repeat them): the GOTY guide description (Personality); "I don't understand
  you people. The trappings of progress are here for the taking...", "Our armed forces have no equal...", "There's
  always somebody watching, Mr. Marston..." (In his own words); the forms of address "Mr. Fordham", "Agent Fordham",
  "Archer" and John's "office clerk or social secretary" (Names).
- Paraphrased here, left to part C Quotes: the El Presidio lines (both branches), "Like you always say, sir...",
  "It ends when we say it ends...", "Marston, you're a public menace...", "See, this is what happens when you
  fraternize with savages...", "Van der Linde is a psychopath...", the Fort Mercer reproach, the "send your wife out
  to work" jab, "Thank you, Mr. Marston, for everything...", "Good god, that's our informant", "Make sure you do.".
- Gameplay HERE only: weapons, the automobile (the failure conditions live in the part C Missions table).
- Told once elsewhere, pointer here: every mission event and every exchange of dialogue (A, which paraphrases them all:
  the maxim, "snarky", the engine, the roof, the MacDougal introduction, the Cochinay ride); Maybelle (A Origins and
  the facts grid; no relationship entry); actor and cut content (D, incl. "Bessie" and Rufus).

WIKI-ONLY (kept, attributed): the GOTY guide description; the three weapons and their order of use; his height compared with Ross's; his presence and death option at Beecher's Hope (mission page); the crank and the ignition (mission page).

FIX (22 Oct 2026, fc_report1/2, coverage, FIX_RULES.md): failure conditions moved to the part C table only (pointer
here); Pinkerton badge to part C Trivia only; Beecher's Hope 1911 told with the standard hedge; "Van der Linde is
the priority" paraphrased here (quoted in C).

Excluded: "more hot-headed and impulsive than his cold and calculating mentor", "exceedingly capable", "unwaveringly
supports Ross", "develops a respect of sorts for Marston" (wiki readings; his lines are given instead); the wiki
trivia contrasting Ross and Fordham like Jonah and Eli ("deceitful" vs "honest and blunt": interpretation); the
"immodest, lighter three-piece suit" of 1911 as worded (FIX 22 Oct 2026: gallery-4 shows a brown three-piece suit and
a dark red tie, used in Appearance; gallery-1 shows the 1907 charcoal suit and black tie); "noticeably more positive" if Javier is captured (reading of the two branches, which are
told in A and quoted in C); the FR wiki's cut NPC line about a "Bureau fella" whose mother was shot in a massacre (it
does not name Fordham; the link is the FR wiki's inference); the FR wiki's "Maybelle Foreman" (conflicts with the EN
wiki's "Maybelle Fordham"); the Ford Model T (FR wiki only); Andrew Milton as a relationship (no scene, line or source
links them; v2 entry dropped); Isaac McKinnon (resemblance trivia, part C).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "The Red Dead Wiki quotes the description of Fordham given in the Game of the Year Edition guide of Red Dead Redemption: \"Archer is a young, sturdy, and keen-eyed government agent. He is Ross's right-hand man and he is very ambitious and aggressive.\" In the game, he often calls Ross \"sir\" and agrees with his proposals. He mostly addresses John as Mr. Marston, uses plain Marston in orders and insults, and calls him John only once, at the border bridge in the branch where Javier is captured.",
        "Le Red Dead Wiki cite la description de Fordham donnée par le guide de l'édition Game of the Year de Red Dead Redemption : \"Archer is a young, sturdy, and keen-eyed government agent. He is Ross's right-hand man and he is very ambitious and aggressive.\" (Archer est un agent du gouvernement jeune, solide et à l'œil vif. Bras droit de Ross, il est très ambitieux et agressif). Dans le jeu, il donne souvent du \"sir\" à Ross et approuve ses propositions. Avec John, il s'en tient le plus souvent à monsieur Marston, passe à Marston tout court pour les ordres et les insultes, et ne l'appelle John qu'une fois, au pont de la frontière, quand Javier a été capturé.")},
    {"p": two(
        "He threatens John several times. He defends the Bureau's methods and the progress of the age: motorcars, rail transport of cattle, the army's new weapons. He says Dutch van der Linde is insane, calls him a psychopath, and speaks of \"savages\" when he asks John how he could follow such a man (see Biography).",
        "Il menace John à plusieurs reprises. Il défend les méthodes du Bureau et le progrès de son époque : l'automobile, le bétail qui voyage par le train, les nouvelles armes de l'armée. Il tient Dutch van der Linde pour un fou et un psychopathe, et parle de \"sauvages\" quand il demande à John comment il a pu suivre un tel homme (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "On the drive to the wreck of the Serendipity, in \"Bear One Another's Burdens\": \"I don't understand you people. The trappings of progress are here for the taking and you're too stubborn to take them.\" Leaving Blackwater in the armed vehicle, in \"And You Will Know The Truth\": \"Our armed forces have no equal. We have made incredible progress the past few years.\" Then, about the vehicle: \"And this isn't much more than a simple prototype. You should see what they're working on in Virginia. Soon there will be no war we can't win.\" On the ride to Cochinay, in \"And The Truth Will Set You Free\": \"There's always somebody watching, Mr. Marston. I thought you'd have gleaned that much by now.\"",
        "Sur la route de l'épave du Serendipity, dans \"Bear One Another's Burdens\" : \"I don't understand you people. The trappings of progress are here for the taking and you're too stubborn to take them.\" (je ne vous comprends pas, vous autres. Les bienfaits du progrès sont à portée de main et vous êtes trop têtus pour les saisir). En quittant Blackwater à bord du véhicule armé, dans \"And You Will Know The Truth\" : \"Our armed forces have no equal. We have made incredible progress the past few years.\" (nos forces armées n'ont pas d'égal. Nous avons fait des progrès incroyables ces dernières années). Puis, à propos du véhicule : \"And this isn't much more than a simple prototype. You should see what they're working on in Virginia. Soon there will be no war we can't win.\" (et ce n'est guère plus qu'un simple prototype. Vous devriez voir ce qu'ils préparent en Virginie. Bientôt, il n'y aura plus une guerre que nous ne puissions gagner). En route vers Cochinay, dans \"And The Truth Will Set You Free\" : \"There's always somebody watching, Mr. Marston. I thought you'd have gleaned that much by now.\" (il y a toujours quelqu'un qui observe, monsieur Marston. Je pensais que vous l'aviez compris, depuis le temps).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "The cast list of the Red Dead Redemption manual names him Archer Fordham, and the Red Dead Wiki calls him Agent Archer Fordham. Ross addresses him as \"Mr. Fordham\" or simply Fordham, calls him \"Agent Fordham\" when he tells John to follow him on foot to the wreck, and uses his first name, \"Archer\", twice: when he says that he and Archer are the bad guys, and when he leads him away from the foot of the cliff at Cochinay. Harold MacDougal greets him as \"Mr. Fordham\". In the automobile, John describes one of the two men sent onto the wreck as \"an office clerk or social secretary or some such\".",
        "La liste des interprètes de la notice de Red Dead Redemption le nomme Archer Fordham, et le Red Dead Wiki l'appelle l'agent Archer Fordham. Ross l'appelle \"Mr. Fordham\" ou simplement Fordham, parle de lui comme de l'\"Agent Fordham\" quand il envoie John le suivre à pied jusqu'à l'épave, et emploie deux fois son prénom, \"Archer\" : quand il dit que lui et Archer sont les méchants de l'histoire, et quand il l'emmène loin du pied de la falaise de Cochinay. Harold MacDougal le salue d'un \"Mr. Fordham\". Dans l'automobile, John présente l'un des deux hommes envoyés sur l'épave comme \"an office clerk or social secretary or some such\" (un employé de bureau, un secrétaire mondain ou quelque chose du genre).")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "Fordham is a dark-haired, clean-shaven man. In 1907 he wears a charcoal three-piece suit, a white shirt, a black tie and a bowler hat. In Red Dead Redemption (1911), his three-piece suit is brown and his tie dark red. According to the Red Dead Wiki, he is much taller than Ross in Red Dead Redemption.",
        "Fordham a les cheveux sombres et le visage rasé de près. En 1907, il porte un costume trois pièces anthracite, une chemise blanche, une cravate noire et un chapeau melon. Dans Red Dead Redemption (1911), son costume trois pièces est brun et sa cravate rouge sombre. D'après le Red Dead Wiki, il dépasse Ross d'une bonne tête dans Red Dead Redemption.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Suggested section title for the module: "Weapons and the automobile" / "Armes et automobile".
BLOCKS_SKILLS = [
    {"h4": two("Weapons", "Armes")},
    {"p": two(
        "The Red Dead Wiki lists three weapons for him: a Cattleman Revolver, a High Power Pistol and a Winchester Repeater. According to the same wiki, he carries the Cattleman Revolver in his earlier missions and the High Power Pistol later, like Ross. The page of \"Great Men are Not Always Wise\" notes that Ross and Fordham use the Winchester Repeater, while the sheriffs and marshals of the mission carry the older Repeater Carbine.",
        "Le Red Dead Wiki lui attribue trois armes : un Cattleman Revolver, un High Power Pistol et une Winchester Repeater. Selon le même wiki, il porte le Cattleman Revolver dans ses premières missions, puis le High Power Pistol, comme Ross. La page de \"Great Men are Not Always Wise\" précise que Ross et Fordham se servent de la Winchester Repeater, quand les shérifs et marshals de la mission ont la Repeater Carbine, plus ancienne.")},
    {"h4": two("Behind the wheel", "Au volant")},
    {"p": two(
        "Fordham is the agents' driver: he is at the wheel of the automobile in \"Bear One Another's Burdens\" and of the armed vehicle in \"And You Will Know The Truth\" (see Biography). The page of \"Bear One Another's Burdens\" says he gets the stalled car going again with the crank. The same page notes that he can also start it with the ignition without leaving his seat, a feature few cars of the period had.",
        "Fordham sert de chauffeur aux agents : il tient le volant de l'automobile dans \"Bear One Another's Burdens\" et celui du véhicule armé dans \"And You Will Know The Truth\" (voir la biographie). La page de \"Bear One Another's Burdens\" indique qu'il remet en route à la manivelle la voiture calée. Elle relève aussi qu'il peut la démarrer au contact sans quitter son siège, ce que peu de voitures permettaient à l'époque.")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "Three of his missions fail if John attacks or kills him (conditions in the Missions table). According to the English-language Red Dead Wiki, Fordham is visible among the men facing John through the barn doors at Beecher's Hope in 1911 (he can be shot in the final Dead Eye and may disappear from the cutscene that follows); the French-language wiki says he does not take part in the mission. The page of \"The Last Enemy That Shall Be Destroyed\" adds that Ross cannot be killed there.",
        "Trois de ses missions échouent si John l'agresse ou le tue (conditions détaillées dans le tableau des missions). D'après le Red Dead Wiki anglophone, on aperçoit Fordham parmi les hommes qui font face à John entre les portes de la grange de Beecher's Hope en 1911 (il peut être abattu pendant le Dead Eye final et disparaître de la cinématique qui suit) ; le wiki francophone affirme qu'il ne participe pas à la mission. La page de \"The Last Enemy That Shall Be Destroyed\" précise que Ross, lui, ne peut pas y être tué.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
# Pointers: every event is told in the Biography (part A); verbatim mission lines live in part C Quotes.
RELATIONSHIPS = [
    {"img": "edgar-ross.jpeg", "slug": "edgar-ross", "name": "Edgar Ross", "text": two(
        "Fordham is Ross's subordinate at the Bureau of Investigation, beside him in almost all his scenes, from 1907 to 1911 (see Biography). He drives for him and backs him against John. Ross often belittles him, from the maxim he denies having coined to the blame for the car's breakdown, yet counts him on his own side when he tells John that the two of them are the ones who enforce the rules.",
        "Fordham est le subordonné de Ross au Bureau of Investigation, à ses côtés dans presque toutes ses scènes, de 1907 à 1911 (voir la biographie). Il lui sert de chauffeur et le soutient face à John. Ross le rabaisse souvent, de la maxime qu'il refuse d'avoir inventée à la panne de voiture qu'il lui impute, mais le range dans son camp quand il explique à John que ce sont eux deux qui font respecter les règles.")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "Fordham is one of the two agents who force John to hunt his former gang in 1911, and gives him most of his orders in the field (see Biography). Their exchanges are hostile on both sides until Dutch's death, when Fordham thanks him. He had already watched John at Beecher's Hope with Ross in 1907. According to the English-language Red Dead Wiki, Fordham is visible among the men facing John through the barn doors at Beecher's Hope in 1911 (he can be shot in the final Dead Eye and may disappear from the cutscene that follows); the French-language wiki says he does not take part in the mission.",
        "Fordham est l'un des deux agents qui contraignent John à traquer son ancienne bande en 1911, et c'est lui qui lui donne l'essentiel de ses ordres sur le terrain (voir la biographie). Leurs échanges restent hostiles de part et d'autre jusqu'à la mort de Dutch, où Fordham le remercie. Il l'avait déjà observé à Beecher's Hope avec Ross en 1907. D'après le Red Dead Wiki anglophone, on aperçoit Fordham parmi les hommes qui font face à John entre les portes de la grange de Beecher's Hope en 1911 (il peut être abattu pendant le Dead Eye final et disparaître de la cinématique qui suit) ; le wiki francophone affirme qu'il ne participe pas à la mission.")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "The Bureau holds Abigail while John works for it; Fordham never sees her on screen. He fends off John's questions about her and, on the ride to Cochinay, makes a jibe about sending her out to work (see Biography).",
        "Le Bureau retient Abigail pendant que John travaille pour lui ; Fordham ne la croise jamais à l'écran. Il élude les questions de John à son sujet et, sur la route de Cochinay, lance une pique sur la possibilité de l'envoyer travailler (voir la biographie).")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "In the 1907 end credits, Fordham and Ross watch Jack and his father at Beecher's Hope (see Biography). In 1911 the Bureau holds Jack with his mother until Dutch's death.",
        "Dans le générique de 1907, Fordham et Ross observent Jack et son père à Beecher's Hope (voir la biographie). En 1911, le Bureau retient Jack avec sa mère jusqu'à la mort de Dutch.")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "Fordham never meets him alive: he searches Micah's cabin on Mount Hagen in 1907 while Ross examines the body (see Biography).",
        "Fordham ne le croise jamais vivant : il fouille la cabane de Micah sur le mont Hagen en 1907, pendant que Ross examine le corps (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Fordham takes charge of Javier near the border bridge after El Presidio, alive or dead depending on the player, and greets the two outcomes differently (see Biography).",
        "Fordham prend Javier en charge près du pont de la frontière, après El Presidio, vivant ou mort selon le choix du joueur, et n'accueille pas les deux issues de la même façon (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Fordham never meets Bill, the first target the Bureau gives John; he sends John after him from the border, and on the ride to Cochinay reproaches John for running all over Mexico instead of killing Bill at Fort Mercer (see Biography).",
        "Fordham ne rencontre jamais Bill, la première cible que le Bureau assigne à John ; il lance John à sa poursuite depuis la frontière, puis, sur la route de Cochinay, reproche à John d'avoir couru le Mexique au lieu d'abattre Bill à Fort Mercer (voir la biographie).")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Dutch is the target of Fordham's whole part of the hunt in 1911, from the wreck of the Serendipity to Cochinay, but the two men never come face to face (see Biography). Fordham first mentions him in neutral terms: he tells John at the border that \"Dutch van der Linde is in the area\", calls him the priority on the way down to the wreck and asks John whether Dutch has changed. Later, on the ride to Cochinay, he calls him a psychopath, a murderer and a rapist. John answers that Dutch was a good man once, a far better man than Fordham (see Quotes).",
        "Dutch est la cible de toute la part que prend Fordham à la traque de 1911, de l'épave du Serendipity à Cochinay, mais les deux hommes ne se retrouvent jamais face à face (voir la biographie). Fordham parle d'abord de lui sans animosité : il annonce à John, à la frontière, que \"Dutch van der Linde is in the area\" (Dutch van der Linde est dans la région), en fait la priorité en descendant vers l'épave et demande à John si Dutch a changé. Plus tard, sur la route de Cochinay, il le traite de psychopathe, d'assassin et de violeur. John lui répond que Dutch a été un homme bien, bien meilleur que lui (voir Citations).")},
    {"img": "nastas.jpeg", "slug": "nastas", "name": "Nastas", "text": two(
        "For Fordham, Nastas is the Bureau's informant on Dutch's gang; he recognizes him on the wreck of the Serendipity and vouches for him to Ross (see Biography).",
        "Pour Fordham, Nastas est l'informateur du Bureau sur la bande de Dutch ; il le reconnaît sur l'épave du Serendipity et le présente à Ross (voir la biographie).")},
    {"img": "harold-macdougal.jpeg", "slug": "harold-macdougal", "name": "Harold MacDougal", "text": two(
        "The professor works with the agents on the Native Americans of the region; Fordham introduces him to John and puts the wounded Nastas in his care (see Biography).",
        "Le professeur aide les agents dans leurs rapports avec les Amérindiens de la région ; Fordham le présente à John et lui confie Nastas, blessé (voir la biographie).")},
]
