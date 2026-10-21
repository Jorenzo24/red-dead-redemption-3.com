"""Seth Briars, part B: Personality (official description, observable traits, In his own words, Names, Appearance),
Grave robbing, weapons and horse (the fiche-specific skills section), Relationships (21 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN sections Personality and Appearance, the GOTY quote box, the infobox (aka, weapon,
family, affiliations, occupation, location), the trivia items on his dislike of women, the piglet, the talking to
himself, his surname and the undead, plus the pages "Moses Forth", "Aiden O'Leary", "Treasure Hunters",
"Undead Nightmare" and the mission pages listed in seth/missions.txt. Narrative events are told in part A; entries
below point to them.

SOURCE REGISTER (read 21 Oct 2026; wiki cache scripts/v3/work/_m/):
- Official description: Red Dead Redemption: Game of the Year Edition Guide (BradyGames), quoted in the quote box of
  the Red Dead Wiki EN page "Seth Briars" ("Seth is an American male in his late thirties..."). The guide itself was
  not read: quoted through the wiki, attributed. Rockstar's 6 Sep 2018 descriptions (sources/thr_descriptions.txt)
  cover the RDR2 gang only: none for Seth.
- Transcripts (every quoted line checked): "Exhuming and Other Fine Hobbies/dialogues", "A Gentle Drive with
  Friends/dialogue" (singular page title on the wiki, fetched 21 Oct 2026), "Let the Dead Bury Their Dead/dialogues",
  "The Assault on Fort Mercer/dialogues", "Liars, Cheats and Other Proud Americans/dialogues" (Dickens and John on
  Seth).
- Mission pages: "Exhuming and Other Fine Hobbies" (Coot's Chapel, Josephine Byrd's grave, fail conditions incl.
  Seth's horse, pardon letter, wanted levels and hogtying introduced; failed-ride crow/piglet line in Trivia, no
  transcript), "A Gentle Drive with Friends" (Fire Bottles introduced; machine gun line conditional), "Let the Dead
  Bury Their Dead", "The Assault on Fort Mercer" (Seth distracts the gang; last appearance), "Get Back in that Hole,
  Partner" (no transcript; revolver if attacked), "On a Pale Horse".
- Other wiki pages: "Moses Forth", "Aiden O'Leary", "Treasure Hunters" (members resemble Seth; Treasure Hunter
  Outfit), "Undead Nightmare" (the "Freak with a glass eye" lead).
- Newspaper: Blackwater Ledger & Sentinel No. 213 (1914), "Treasure Found", read on the page image
  (seth/fc/Treasure_Found_1914.txt): gives his full name, "Seth Briars" and "Mr. Briars".
- Visual check: the live portrait.jpeg and gallery-1.jpeg for Appearance.

OWNERSHIP NOTES FOR THE LEAD (parts A and C must not repeat these quoted lines; part C Quotes should draw on the
wiki's Quotes list, NONE of whose entries is quoted here):
- Quoted HERE: the GOTY description; "Oh, I've lost it all partner... and I don't care."; "Used to be about the
  money, but now... only it's me."; "No way I can stop now. It's taken me over."; "I talk to 'em... alone.";
  "I feel less alone with them... just like me." (In his own words); "Seth of the dead"; "a twistly little freak";
  "Thanks for all the hard work, Seth!" (Names); "Hunting dead men's treasure ain't done me no favors. Sure. Sure,
  I'm ready for the living." (John entry); "I met some sick bastards in my time, Seth, but you, you're
  special."; "I know, I can smell you from here."; "a sick man" / "You remind me why I hate
  people. For a man who kills so much, you sure seem to have a problem with the dead." (John); "You and Seth have a
  lot in common... at least he waits until they're dead."; "for a minute, he will delight and amuse them. That's when
  he'll get us inside." (Dickens); "My partner. My boy. My man."; "Him, me, we the same. The self same."; "Seth'd sell
  his own mother." (Moses); "Apart from that Aiden O'Leary fella, I never liked him." (Aiden); "Sometimes they call
  me on... most other fellas won't." (Bill); "Sounds like I need to pay Irish another visit." (Irish); "The bastards
  followed me here!" (Treasure Hunters); "I don't like women, partner. I don't. Not since mammy died." (family).
- John's undead-looting lines ("Seth, I'm sorry about all the insults", etc.) live HERE (John entry): C Trivia must drop
  them. The surname appearing only in the 1914 paper lives HERE (Names): C Trivia must not say "his last name is never
  mentioned" (wrong: the paper prints it). The father/piglet story lives HERE (family entry).
- Items Seth finds on the corpses during "A Gentle Drive with Friends" (bullets, a bottle of elixir, the map piece)
  are in Skills; A should tell the drive without listing them.

WIKI-ONLY (kept, attributed): the GOTY guide description; the Cattleman Revolver and Repeater Carbine (infobox); the
balding head under the hat and the rope belt (Appearance section); the crow and piglet story (failed-ride dialogue,
no transcript); the resemblance of the Treasure Hunters to Seth; the "Freak with a glass eye" lead name; John's
undead-looting lines (trivia); Seth's "history of working with Bill" (character page; the transcript supports a
looser link, quoted instead).

Excluded: "certifiably insane" as our own claim (kept only inside the GOTY quote); split-personality disorder,
bipolar disorder, schizophrenia (wiki and Giant Bomb diagnoses, interpretation); "misanthropic", "his morality is all
but lost" (wiki interpretation); "his hatred of women comes from his mother's death and his wife leaving"
(wiki/FR wiki speculation); a sexual relationship with Moses (FR wiki speculation); Gollum resemblance (comparison);
"Seth of the Dead is a reference to Shaun of the Dead" and the Egyptian god Set (wiki "presumably"; Dickens's Egypt
remark is kept as his words only); the glass eye protecting him from the undead (fan theory); the "emaciated horse"
(Giant Bomb, no game source); "Lucille Billingsgate" as the person calling him "Freak with the Glass Eye" (the wiki
infobox marks it "(?)"); the FR wiki "his father abandoned him" (contradicted by the piglet story; no transcript);
the FR wiki "Marshal Leigh Johnson" as an ally and Josephine Byrd as a relationship (no interaction).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the gang of Red Dead Redemption 2 and do not include Seth. The Red Dead Wiki quotes the Game of the Year Edition guide of Red Dead Redemption: \"Seth is an American male in his late thirties. He is certifiably insane. He is not unlike an opium addict, only his addiction is money and he has been utterly consumed by it. His gold prospecting partner died on him, with the map to vast riches, and now he digs up graves in search of treasures.\"",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang de Red Dead Redemption 2 et ne le concernent pas. Le Red Dead Wiki cite le guide de l'édition Game of the Year de Red Dead Redemption : \"Seth is an American male in his late thirties. He is certifiably insane. He is not unlike an opium addict, only his addiction is money and he has been utterly consumed by it. His gold prospecting partner died on him, with the map to vast riches, and now he digs up graves in search of treasures.\" (Seth est un Américain qui approche de la quarantaine. Il est fou à lier. Il rappelle un opiomane, sauf que sa drogue à lui, c'est l'argent, qui l'a entièrement dévoré. Son associé dans la prospection d'or est mort en emportant la carte d'un immense trésor, et depuis, il déterre des tombes en quête de richesses.)")},
    {"p": two(
        "In the game he talks to the corpses he digs up and carries, and answers himself in a second, higher voice. He often speaks of himself in the third person (\"Seth's gonna be rich\"). He calls the men he deals with partner or mister. He tells John that he hates people and that he cannot say what year it is. His moods swing within a single scene, from begging to threats and from euphoria to tears (see Biography). In Undead Nightmare, which is not canon, he keeps the undead as company (see Biography).",
        "Dans le jeu, il parle aux cadavres qu'il déterre et transporte, et se répond à lui-même d'une seconde voix, plus aiguë. Il parle souvent de lui à la troisième personne (\"Seth's gonna be rich\", Seth va être riche). Il appelle ses interlocuteurs partner (l'associé) ou mister. Il confie à John qu'il déteste les gens et qu'il serait incapable de dire en quelle année on est. Son humeur bascule d'un instant à l'autre au cours d'une même scène, de la supplication à la menace, de l'euphorie aux larmes (voir la biographie). Dans Undead Nightmare, qui n'appartient pas au canon, il fait des morts-vivants sa compagnie (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "On the road to Benedict Point, in \"Exhuming and Other Fine Hobbies\", he sums up his situation: \"Oh, I've lost it all partner. My wife, my children, my business. Good riddance to them all. I don't eat, I don't sleep, I don't wash, and I don't care.\" He goes on: \"Used to be about the money, but now... I don't know who I am no more. I see myself but it's like I'm lookin' at somebody else, only it's me.\" When John tells him to move on: \"No way I can stop now. It's taken me over.\"",
        "Sur la route de Benedict Point, dans \"Exhuming and Other Fine Hobbies\", il résume sa situation : \"Oh, I've lost it all partner. My wife, my children, my business. Good riddance to them all. I don't eat, I don't sleep, I don't wash, and I don't care.\" (j'ai tout perdu, l'ami : ma femme, mes enfants, mon affaire. Bon débarras. Je ne mange pas, je ne dors pas, je ne me lave pas, et je m'en fiche). Il poursuit : \"Used to be about the money, but now... I don't know who I am no more. I see myself but it's like I'm lookin' at somebody else, only it's me.\" (au début, c'était pour l'argent, mais maintenant, je ne sais plus qui je suis. Je me vois, mais comme si je regardais un autre, sauf que c'est moi). Quand John lui conseille de passer à autre chose : \"No way I can stop now. It's taken me over.\" (impossible d'arrêter maintenant, ça m'a pris tout entier).")},
    {"p": two(
        "On why he robs graves, in the same ride: \"I talk to 'em, long after they been forgotten by every other fella. I tell 'em it's alright to be scared and alone.\" On the corpses in his wagon, in \"A Gentle Drive with Friends\": \"I feel less alone with them than in a crowd of people. The way I see it, they lost their souls, just like me.\"",
        "Sur ses pillages de tombes, pendant la même chevauchée : \"I talk to 'em, long after they been forgotten by every other fella. I tell 'em it's alright to be scared and alone.\" (je leur parle, bien après que tout le monde les a oubliés ; je leur dis qu'ils ont le droit d'avoir peur et de se sentir seuls). Sur les cadavres de son chariot, dans \"A Gentle Drive with Friends\" : \"I feel less alone with them than in a crowd of people. The way I see it, they lost their souls, just like me.\" (je me sens moins seul avec eux qu'au milieu d'une foule ; à mon avis, ils ont perdu leur âme, tout comme moi).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "In the missions he is only ever called Seth. His surname appears in print in the last newspaper of the game, the Blackwater Ledger & Sentinel of 1914, which names him \"Seth Briars\" and then \"Mr. Briars\". Nigel West Dickens calls him \"Seth of the dead\" when John reports their meeting, in \"Liars, Cheats and Other Proud Americans\". Moses Forth calls him \"a twistly little freak\" (the transcript's spelling). A treasure hunter greets him with \"Thanks for all the hard work, Seth!\" at Tumbleweed. In Undead Nightmare, according to the Red Dead Wiki, the lead that sends John to him is labelled Freak with a glass eye.",
        "Dans les missions, on ne l'appelle jamais autrement que Seth. Son nom de famille n'apparaît qu'imprimé, dans le dernier journal du jeu, le Blackwater Ledger & Sentinel de 1914, qui le nomme \"Seth Briars\" puis \"Mr. Briars\". Nigel West Dickens le surnomme \"Seth of the dead\" (Seth des morts) quand John lui raconte leur rencontre, dans \"Liars, Cheats and Other Proud Americans\". Moses Forth le traite de \"twistly little freak\" (sale petit tordu, selon la graphie de la transcription). À Tumbleweed, un chasseur de trésors l'accueille d'un \"Thanks for all the hard work, Seth!\" (merci pour tout ce travail, Seth !). Dans Undead Nightmare, d'après le Red Dead Wiki, la piste qui mène John jusqu'à lui s'intitule Freak with a glass eye (le monstre à l'œil de verre).")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is a gaunt man with sunken cheeks, visible ribs, sores around the mouth, a thin pale mustache and long, lank hair under a battered, wide-brimmed hat. He wears a torn, dirty shirt open on his chest. According to the Red Dead Wiki, a piece of rope serves as his belt and he is balding under the hat.",
        "C'est un homme décharné, aux joues creuses et aux côtes saillantes, la bouche couverte de plaies, avec une fine moustache pâle et de longs cheveux filasse sous un chapeau à large bord tout cabossé. Il porte une chemise déchirée et crasseuse, ouverte sur la poitrine. Selon le Red Dead Wiki, un bout de corde lui tient lieu de ceinture, et il est presque chauve sous son chapeau.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Suggested section title for the module: "Grave robbing, weapons and horse" / "Pillage de tombes, armes et cheval".
BLOCKS_SKILLS = [
    {"h4": two("Grave robbing", "Le pillage de tombes")},
    {"p": two(
        "John first finds him at work in the cemetery of Coot's Chapel; according to the mission page, the grave he is digging is that of Josephine Byrd. He later works the cemetery of Tumbleweed, and he takes the bodies of flu victims from Odd Fellow's Rest before they are even buried (see Biography). In \"A Gentle Drive with Friends\", he searches the corpses in the back of the wagon while John drives: according to the transcript, he turns up a few bullets and a bottle of elixir before he finds the piece of map. He tells John that Bill Williamson's gang sometimes calls on him for special jobs (see Relationships).",
        "John le trouve pour la première fois à l'ouvrage dans le cimetière de Coot's Chapel ; d'après la page de la mission, la tombe qu'il fouille est celle de Josephine Byrd. Il s'attaque ensuite au cimetière de Tumbleweed et emporte d'Odd Fellow's Rest les corps de victimes de la grippe avant même leur enterrement (voir la biographie). Dans \"A Gentle Drive with Friends\", il fouille les cadavres à l'arrière du chariot pendant que John conduit : selon la transcription, il y trouve quelques balles et un flacon d'élixir avant de mettre la main sur le morceau de carte. Il raconte à John que la bande de Bill Williamson fait parfois appel à lui pour des besognes particulières (voir les relations).")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "Seth gives three missions in Red Dead Redemption and one in Undead Nightmare, listed in the Missions table. His first introduces wanted levels, bounties and hogtying: John must steal a lawman's horse, then catch and hogtie Moses Forth. Seth has no money and pays John with a pardon letter, which clears the bounty; the player can keep the letter and pay the bounty instead. \"A Gentle Drive with Friends\" introduces fire bottles. His missions in Red Dead Redemption fail if he is killed or abandoned.",
        "Seth confie trois missions dans Red Dead Redemption et une dans Undead Nightmare, recensées dans le tableau des missions. La première introduit les niveaux de recherche, les primes et le ligotage : John doit voler le cheval d'un représentant de la loi, puis rattraper et ligoter Moses Forth. Seth n'a pas d'argent et paie John avec une lettre de grâce, qui efface la prime ; le joueur peut aussi garder la lettre et payer la prime. \"A Gentle Drive with Friends\" introduit les bouteilles incendiaires. Ses missions de Red Dead Redemption échouent s'il est tué ou abandonné.")},
    {"h4": two("Weapons and horse", "Armes et cheval")},
    {"p": two(
        "At Benedict Point he draws a knife to threaten Moses Forth (see Biography). The Red Dead Wiki also lists a Cattleman Revolver and a Repeater Carbine. He rides his own horse to Benedict Point, and the mission fails if that horse is killed. In Undead Nightmare, which is not canon, he pulls a revolver and fires at John if John attacks him, according to the mission page of \"Get Back in that Hole, Partner\".",
        "À Benedict Point, il sort un couteau pour menacer Moses Forth (voir la biographie). Le Red Dead Wiki lui attribue en outre un Cattleman Revolver et une Repeater Carbine. Il se rend à Benedict Point sur son propre cheval, et la mission échoue si ce cheval est tué. Dans Undead Nightmare, qui n'appartient pas au canon, il dégaine un revolver et tire sur John si celui-ci l'attaque, selon la page de la mission \"Get Back in that Hole, Partner\".")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [two(
        "John comes to Seth for help getting inside Fort Mercer and agrees to recover his map first (see Biography). John makes no secret of his disgust. On the road to Benedict Point he tells him: \"I met some sick bastards in my time, Seth, but you, you're special.\" When Seth lists what he has given up, John answers: \"I know, I can smell you from here.\" In \"A Gentle Drive with Friends\", John calls him \"a sick man\"; Seth replies: \"You remind me why I hate people. For a man who kills so much, you sure seem to have a problem with the dead.\"",
        "John vient demander à Seth de l'aider à entrer dans Fort Mercer et accepte de retrouver d'abord sa carte (voir la biographie). John ne cache pas son dégoût. Sur la route de Benedict Point, il lui lance : \"I met some sick bastards in my time, Seth, but you, you're special.\" (j'ai croisé des tordus dans ma vie, Seth, mais toi, tu es un cas à part). Quand Seth énumère tout ce qu'il a abandonné, John répond : \"I know, I can smell you from here.\" (je sais, je te sens d'ici). Dans \"A Gentle Drive with Friends\", John le traite de malade ; Seth rétorque : \"You remind me why I hate people. For a man who kills so much, you sure seem to have a problem with the dead.\" (tu me rappelles pourquoi je déteste les gens ; pour un homme qui tue autant, tu as l'air d'avoir un problème avec les morts)."),
        two(
        "After the glass eye, Seth keeps his word: \"Hunting dead men's treasure ain't done me no favors. Sure. Sure, I'm ready for the living.\" In Undead Nightmare, which is not canon, John seeks him out again (see Biography). According to the Red Dead Wiki, John sometimes says \"Seth, I'm sorry about all the insults\", \"Seth, finally I've joined you\" or \"Seth, how do you enjoy this?\" while searching the bodies of the undead.",
        "Après l'œil de verre, Seth tient parole : \"Hunting dead men's treasure ain't done me no favors. Sure. Sure, I'm ready for the living.\" (chasser le trésor des morts ne m'a rien apporté de bon ; d'accord, je suis prêt pour les vivants). Dans Undead Nightmare, qui n'appartient pas au canon, John va de nouveau le trouver (voir la biographie). D'après le Red Dead Wiki, John lâche parfois \"Seth, I'm sorry about all the insults\" (Seth, désolé pour toutes ces insultes), \"Seth, finally I've joined you\" (Seth, me voilà enfin des vôtres) ou \"Seth, how do you enjoy this?\" (Seth, ça te plaît ?) en fouillant les corps des morts-vivants.")]},
    {"img": "nigel-west-dickens.jpeg", "slug": "nigel-west-dickens", "name": "Nigel West Dickens", "text": two(
        "Dickens is the old friend who sends John to Seth (see Biography). When John reports the meeting, in \"Liars, Cheats and Other Proud Americans\", Dickens defends grave robbing, which he says ancient Egypt valued above literature. John answers: \"You and Seth have a lot in common. You both rob people, for one. Mind you, at least he waits until they're dead.\" At Fort Mercer, Dickens explains that Seth will keep the outlaws busy: \"for a minute, he will delight and amuse them. That's when he'll get us inside.\"",
        "Dickens est le vieil ami qui envoie John chez Seth (voir la biographie). Quand John lui raconte leur rencontre, dans \"Liars, Cheats and Other Proud Americans\", Dickens prend la défense du pillage de tombes, plus estimé que la littérature dans l'Égypte ancienne, assure-t-il. John répond : \"You and Seth have a lot in common. You both rob people, for one. Mind you, at least he waits until they're dead.\" (Seth et vous avez beaucoup en commun : vous détroussez les gens, pour commencer. Lui, au moins, attend qu'ils soient morts). À Fort Mercer, Dickens explique que Seth va occuper les hors-la-loi : \"for a minute, he will delight and amuse them. That's when he'll get us inside.\" (pendant une minute, il va les ravir et les amuser ; c'est là qu'il nous fera entrer).")},
    {"img": None, "slug": None, "name": "Moses Forth", "text": [two(
        "His former partner, whom he blames for taking half of the map. Seth describes him to John as \"My partner. My boy. My man.\", and says of the two of them: \"Him, me, we the same. The self same.\" Hogtied at Benedict Point, Moses warns John that \"Seth'd sell his own mother\" (see Biography for the knife and the confession). In \"A Gentle Drive with Friends\", Seth decides that Moses did not lie to him after all and blames Aiden O'Leary. In 1914, Seth tells the Blackwater press that he has no connection with the grave robberies blamed on Moses (see Biography).",
        "Son ancien associé, qu'il accuse d'avoir pris la moitié de la carte. Seth le présente à John comme \"My partner. My boy. My man.\" (mon associé, mon gars, mon homme) et dit d'eux deux : \"Him, me, we the same. The self same.\" (lui, moi, on est pareils, exactement pareils). Ligoté à Benedict Point, Moses prévient John que \"Seth'd sell his own mother\" (Seth vendrait sa propre mère) (voir la biographie pour le couteau et les aveux). Dans \"A Gentle Drive with Friends\", Seth conclut que Moses ne lui a pas menti et s'en prend à Aiden O'Leary. En 1914, Seth assure à la presse de Blackwater n'avoir rien à voir avec les pillages de tombes imputés à Moses (voir la biographie)."),
        two(
        "In Undead Nightmare, which is not canon, Moses is one of the undead and plays cards with Seth at The Old Bacchus Place; by the end of the mission he is dancing at Seth's party with other undead guests, Mary Lou and Francine (see Biography).",
        "Dans Undead Nightmare, qui n'appartient pas au canon, Moses est devenu un mort-vivant et joue aux cartes avec Seth à The Old Bacchus Place ; à la fin de la mission, il danse à la fête de Seth avec d'autres invités morts-vivants, Mary Lou et Francine (voir la biographie).")]},
    {"img": None, "slug": None, "name": "Aiden O'Leary", "text": two(
        "Seth ends up blaming this man, who claimed to have the body, and says he died in the flu epidemic before the dead were even buried (see Biography). Seth adds: \"Apart from that Aiden O'Leary fella, I never liked him.\" He never appears on screen.",
        "Seth finit par accuser cet homme, qui prétendait avoir le corps, et raconte qu'il est mort de la grippe avant même que les victimes ne soient enterrées (voir la biographie). Seth ajoute : \"Apart from that Aiden O'Leary fella, I never liked him.\" (sauf ce type, Aiden O'Leary, je ne l'ai jamais aimé). Il n'apparaît jamais à l'écran.")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Seth knows the gang John is after: \"I met Williamson and Deek and all them boys. Sometimes they call me on when they got some special job needs doin'. I got a reputation as a man who do things most other fellas won't.\" He tells John he can get him into Fort Mercer \"no bother\", once the map is found. On the day of the assault, Seth is already inside and Bill has already left for Mexico (see Biography).",
        "Seth connaît la bande que traque John : \"I met Williamson and Deek and all them boys. Sometimes they call me on when they got some special job needs doin'. I got a reputation as a man who do things most other fellas won't.\" (j'ai rencontré Williamson, Deek et toute leur clique ; il leur arrive de m'appeler quand ils ont une besogne spéciale ; on me sait capable de faire ce que la plupart des gars refusent). Il assure à John qu'il le fera entrer dans Fort Mercer \"no bother\" (sans problème), une fois la carte retrouvée. Le jour de l'assaut, Seth est déjà dans la place et Bill est déjà parti au Mexique (voir la biographie).")},
    {"img": "irish.jpeg", "slug": "irish", "name": "Irish", "text": two(
        "Both are part of the Fort Mercer plan, but they share no scene. On the road to Tumbleweed, Seth passes on a message from Dickens: there is no ammunition in John's machine gun. John answers: \"Sounds like I need to pay Irish another visit.\" According to the mission page, this exchange only plays if John has already collected the gun.",
        "Tous deux font partie du plan contre Fort Mercer, sans partager aucune scène. Sur la route de Tumbleweed, Seth transmet un message de Dickens : la mitrailleuse de John n'a pas de munitions. John répond : \"Sounds like I need to pay Irish another visit.\" (on dirait que je vais devoir rendre une nouvelle visite à Irish). Selon la page de la mission, cet échange n'a lieu que si John a déjà récupéré l'arme.")},
    {"img": None, "slug": None, "name": "The Treasure Hunters", "text": two(
        "An armed gang after the same treasure. They chase the wagon on the road to Tumbleweed, then attack Seth and John in the town (see Biography). Seth: \"The bastards followed me here!\" According to the Red Dead Wiki, their members share Seth's worn clothes and poor hygiene, and John can later wear a Treasure Hunter Outfit to walk into their hideout unharmed.",
        "Une bande armée lancée sur le même trésor. Elle prend le chariot en chasse sur la route de Tumbleweed, puis attaque Seth et John dans la ville (voir la biographie). Seth : \"The bastards followed me here!\" (ces salauds m'ont suivi jusqu'ici !). D'après le Red Dead Wiki, ses membres partagent les vêtements usés et la crasse de Seth, et John peut plus tard revêtir une tenue de chasseur de trésors (Treasure Hunter Outfit) pour entrer sans risque dans leur repaire.")},
    {"img": None, "slug": None, "name": "His family", "text": two(
        "The games show none of his relatives. Seth says he has lost his wife, his children and his business (see In his own words above). Of his mother, he says in \"A Gentle Drive with Friends\": \"I don't like women, partner. I don't. Not since mammy died.\" According to the Red Dead Wiki, if the player fails the ride of \"Exhuming and Other Fine Hobbies\" several times, Seth says that the last thing he ate was a crow, and that it tasted like the piglet his father killed when he was a boy.",
        "Les jeux ne montrent aucun membre de sa famille. Seth dit avoir perdu sa femme, ses enfants et son affaire (voir Dans ses propres mots, plus haut). De sa mère, il dit dans \"A Gentle Drive with Friends\" : \"I don't like women, partner. I don't. Not since mammy died.\" (j'aime pas les femmes, l'ami, non. Plus depuis que maman est morte). D'après le Red Dead Wiki, si le joueur rate plusieurs fois la chevauchée de \"Exhuming and Other Fine Hobbies\", Seth raconte que la dernière chose qu'il a mangée est une corneille, au goût du porcelet que son père avait tué quand il était enfant.")},
]
