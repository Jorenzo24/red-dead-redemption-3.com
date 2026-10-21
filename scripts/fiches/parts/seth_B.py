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
  Partner" (no transcript; failure if Seth, Moses or the dancers are
  assaulted; revolver only if Seth survives dynamite or a fire bottle thrown into the party), "On a Pale Horse".
- Other wiki pages: "Moses Forth", "Aiden O'Leary", "Treasure Hunters" (members resemble Seth; Treasure Hunter
  Outfit), "Undead Nightmare" (the "Freak with a glass eye" lead).
- Newspaper: Blackwater Ledger & Sentinel No. 213 (1914), "Treasure Found", read on the page image
  (seth/fc/Treasure_Found_1914.txt): gives his full name, "Seth Briars" and "Mr. Briars".
- Visual check: the live portrait.jpeg and gallery-1.jpeg for Appearance.

OWNERSHIP NOTES (after the fix pass of 21 Oct 2026, scripts/v3/work/seth/FIX_RULES.md):
- Quoted HERE only: the GOTY description; "Oh, I've lost it all partner..."; "Used to be about the money..."; "No way I
  can stop now..."; "I talk to 'em..."; "I feel less alone with them..." (In his own words); "Seth of the dead",
  "a twistly little freak", "Thanks for all the hard work, Seth!" (Names); "I met some sick bastards...", "I know, I can
  smell you from here." (John); "My partner. My boy. My man.", "Him, me, we the same. The self same." (Moses);
  "Apart from that Aiden O'Leary fella, I never liked him." (Aiden); "Sounds like I need to pay Irish another visit."
  (Irish); "The bastards followed me here!" (Treasure Hunters); "I don't like women, partner..." (family); John's
  undead-looting lines (John entry; cut from C Trivia).
- Paraphrased here, quoted in C Quotes only: "You remind me why I hate people...", "Hunting dead men's treasure...",
  "You and Seth have a lot in common...", "delight and amuse them...", "Seth'd sell his own mother".
- Told once elsewhere, pointer here: crow and piglet (A Origins), Williamson gang special jobs (A Act I), bullets and
  elixir, machine-gun message, Josephine Byrd's grave, origin of the wagon bodies (A), mechanics introduced by each
  mission (C Missions). Pardon letter vs bounty: HERE only. Undead Nightmare revolver and failure condition: HERE only.

WIKI-ONLY (kept, attributed): the GOTY guide description; "Fly! Fly!" when riding (wiki quote list); the Cattleman Revolver and Repeater Carbine (infobox); the
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
        "The Red Dead Wiki quotes the Game of the Year Edition guide of Red Dead Redemption: \"Seth is an American male in his late thirties. He is certifiably insane. He is not unlike an opium addict, only his addiction is money and he has been utterly consumed by it. His gold prospecting partner died on him, with the map to vast riches, and now he digs up graves in search of treasures.\" In the game, his former partner Moses Forth is alive in 1911 (see Biography).",
        "Le Red Dead Wiki cite le guide de l'édition Game of the Year de Red Dead Redemption : \"Seth is an American male in his late thirties. He is certifiably insane. He is not unlike an opium addict, only his addiction is money and he has been utterly consumed by it. His gold prospecting partner died on him, with the map to vast riches, and now he digs up graves in search of treasures.\" (Seth est un Américain qui approche de la quarantaine. Il est fou à lier. Il rappelle un opiomane, sauf que sa drogue à lui, c'est l'argent, qui l'a entièrement dévoré. Son associé dans la prospection d'or est mort en emportant la carte d'un immense trésor, et depuis, il déterre des tombes en quête de richesses.) Dans le jeu, pourtant, son ancien associé Moses Forth est bien vivant en 1911 (voir la biographie).")},
    {"p": two(
        "In the game he talks to the corpses he digs up and carries, and answers himself in a second, higher voice. He often speaks of himself in the third person (\"Seth's gonna be rich\"). He calls the men he deals with partner or mister. When he opens the chest at Tumbleweed, he goes from euphoria to tears within a few seconds (see Biography). In Undead Nightmare, which is not canon, he keeps the undead as company (see Biography).",
        "Dans le jeu, il parle aux cadavres qu'il déterre et transporte, et se répond à lui-même d'une seconde voix, plus aiguë. Il parle souvent de lui à la troisième personne (\"Seth's gonna be rich\", Seth va être riche). Il appelle ses interlocuteurs partner (l'associé) ou mister. Devant le coffre de Tumbleweed, il passe de l'euphorie aux larmes en quelques secondes (voir la biographie). Dans Undead Nightmare, qui n'appartient pas au canon, il fait des morts-vivants sa compagnie (voir la biographie).")},
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
        "John first finds him at work in the cemetery of Coot's Chapel, and later in the cemetery of Tumbleweed. He does not wait for the dead to be buried: he loads the bodies of flu victims onto a wagon and searches them on the move (see Biography).",
        "John le trouve d'abord à l'ouvrage dans le cimetière de Coot's Chapel, puis dans celui de Tumbleweed. Seth n'attend pas que les morts soient enterrés : il charge sur un chariot les corps de victimes de la grippe et les fouille en route (voir la biographie).")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "Seth gives three missions in Red Dead Redemption and one in Undead Nightmare; the Missions table lists them, with the game mechanics each one introduces. Seth has no money and pays John for his help with Moses Forth with a pardon letter, which clears the bounty John gets for stealing a lawman's horse. The player can instead pay the bounty and keep the letter. His missions in Red Dead Redemption fail if he is killed or abandoned.",
        "Seth confie trois missions dans Red Dead Redemption et une dans Undead Nightmare ; le tableau des missions les recense, avec les mécaniques de jeu que chacune introduit. Faute d'argent, Seth rémunère l'aide de John contre Moses Forth avec une lettre de grâce, qui efface la prime due au vol du cheval d'un représentant de la loi. Le joueur peut aussi payer la prime et garder la lettre. Ses missions de Red Dead Redemption échouent s'il est tué ou abandonné.")},
    {"h4": two("Weapons and horse", "Armes et cheval")},
    {"p": two(
        "At Benedict Point he draws a knife to threaten Moses Forth (see Biography). The Red Dead Wiki also lists a Cattleman Revolver and a Repeater Carbine. He rides his own horse to Benedict Point, and the mission fails if that horse is killed. According to the Red Dead Wiki, he shouts \"Fly! Fly!\" when he rides. In Undead Nightmare, which is not canon, assaulting Seth, Moses or the dancing undead fails \"Get Back in That Hole, Partner\". According to the mission page, Seth draws a revolver only if he survives a stick of dynamite or a fire bottle thrown into the party at the end of the mission: he then fires at John and tries to flee.",
        "À Benedict Point, il sort un couteau pour menacer Moses Forth (voir la biographie). Le Red Dead Wiki lui attribue en outre un Cattleman Revolver et une Repeater Carbine. Il se rend à Benedict Point sur son propre cheval, et la mission échoue si ce cheval est tué. D'après le Red Dead Wiki, il crie \"Fly! Fly!\" (file ! file !) quand il chevauche. Dans Undead Nightmare, qui n'appartient pas au canon, s'en prendre à Seth, à Moses ou aux morts-vivants qui dansent fait échouer \"Get Back in That Hole, Partner\". Selon la page de la mission, Seth ne dégaine un revolver que s'il réchappe à un bâton de dynamite ou à un cocktail incendiaire lancé sur la fête à la fin de la mission : il tire alors sur John et tente de s'enfuir.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [two(
        "John comes to Seth for help getting inside Fort Mercer and agrees to recover his map first (see Biography). John makes no secret of his disgust. On the road to Benedict Point he tells him: \"I met some sick bastards in my time, Seth, but you, you're special.\" When Seth lists what he has given up, John answers: \"I know, I can smell you from here.\" In \"A Gentle Drive with Friends\", John calls him a sick man; Seth retorts that John reminds him why he hates people, and that a man who kills so much has an odd problem with the dead (see Quotes).",
        "John vient demander à Seth de l'aider à entrer dans Fort Mercer et accepte de retrouver d'abord sa carte (voir la biographie). John ne cache pas son dégoût. Sur la route de Benedict Point, il lui lance : \"I met some sick bastards in my time, Seth, but you, you're special.\" (j'ai croisé des tordus dans ma vie, Seth, mais toi, tu es un cas à part). Quand Seth énumère tout ce qu'il a abandonné, John répond : \"I know, I can smell you from here.\" (je sais, je te sens d'ici). Dans \"A Gentle Drive with Friends\", John le traite de malade ; Seth lui rétorque qu'il lui rappelle pourquoi il déteste les gens, et que pour un homme qui tue autant, il a un drôle de problème avec les morts (voir Citations)."),
        two(
        "After the glass eye, Seth agrees to help John at Fort Mercer and keeps his word (see Biography). In Undead Nightmare, which is not canon, John seeks him out again (see Biography). According to the Red Dead Wiki, John sometimes says \"Seth, I'm sorry about all the insults\", \"Seth, finally I've joined you\" or \"Seth, how do you enjoy this?\" while searching the bodies of the undead.",
        "Après l'épisode de l'œil de verre, Seth accepte d'aider John à Fort Mercer et tient parole (voir la biographie). Dans Undead Nightmare, qui n'appartient pas au canon, John va de nouveau le trouver (voir la biographie). D'après le Red Dead Wiki, John lâche parfois \"Seth, I'm sorry about all the insults\" (Seth, désolé pour toutes ces insultes), \"Seth, finally I've joined you\" (Seth, me voilà enfin des vôtres) ou \"Seth, how do you enjoy this?\" (Seth, ça te plaît ?) en fouillant les corps des morts-vivants.")]},
    {"img": "nigel-west-dickens.jpeg", "slug": "nigel-west-dickens", "name": "Nigel West Dickens", "text": two(
        "Dickens is the old friend who sends John to Seth at Coot's Chapel. In \"Liars, Cheats and Other Proud Americans\", he speaks warmly of Seth, while John finds him deeply disturbed and compares the two men (see Biography and Quotes). At Fort Mercer, Dickens relies on Seth to keep the outlaws busy long enough for the wagon to get in (see Biography).",
        "Dickens est le vieil ami qui envoie John trouver Seth à Coot's Chapel. Dans \"Liars, Cheats and Other Proud Americans\", il en parle avec chaleur, alors que John le juge profondément dérangé et compare les deux hommes (voir la biographie et les citations). À Fort Mercer, Dickens compte sur Seth pour occuper les hors-la-loi le temps de faire entrer le chariot (voir la biographie).")},
    {"img": None, "slug": None, "name": "Moses Forth", "text": [two(
        "His former partner, whom he blames for taking half of the map. Seth describes him to John as \"My partner. My boy. My man.\", and says of the two of them: \"Him, me, we the same. The self same.\" Hogtied at Benedict Point, Moses tries to turn John against Seth (see Biography for the knife and the confession). In \"A Gentle Drive with Friends\", Seth decides that Moses did not lie to him after all and blames Aiden O'Leary. In 1914, Seth tells the Blackwater press that he has no connection with the grave robberies blamed on Moses (see Biography).",
        "Son ancien associé, qu'il accuse d'avoir pris la moitié de la carte. Seth le présente à John comme \"My partner. My boy. My man.\" (mon associé, mon gars, mon homme) et dit d'eux deux : \"Him, me, we the same. The self same.\" (lui, moi, on est pareils, exactement pareils). Ligoté à Benedict Point, Moses tente de retourner John contre Seth (voir la biographie pour le couteau et les aveux). Dans \"A Gentle Drive with Friends\", Seth conclut que Moses ne lui a pas menti et s'en prend à Aiden O'Leary. En 1914, Seth assure à la presse de Blackwater n'avoir rien à voir avec les pillages de tombes imputés à Moses (voir la biographie)."),
        two(
        "In Undead Nightmare, which is not canon, Moses is one of the undead: he plays cards with Seth at The Old Bacchus Place, then dances with Francine at Seth's party (see Biography).",
        "Dans Undead Nightmare, qui n'appartient pas au canon, Moses est devenu un mort-vivant : il joue aux cartes avec Seth à The Old Bacchus Place, puis danse avec Francine à la fête de Seth (voir la biographie).")]},
    {"img": None, "slug": None, "name": "Aiden O'Leary", "text": two(
        "Seth ends up blaming this man, who said he had the body that carried the missing piece of the map. According to Seth, O'Leary died in the flu epidemic, whose victims were not yet buried (see Biography). Seth adds: \"Apart from that Aiden O'Leary fella, I never liked him.\"",
        "Seth finit par accuser cet homme, qui disait avoir le corps portant le morceau manquant de la carte. D'après Seth, O'Leary a succombé à l'épidémie de grippe, dont les victimes n'étaient pas encore enterrées (voir la biographie). Seth ajoute : \"Apart from that Aiden O'Leary fella, I never liked him.\" (sauf ce type, Aiden O'Leary, je ne l'ai jamais aimé).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Seth knows the gang John is after and offers him a way into Fort Mercer once the map is found (see Biography). On the day of the assault, Seth is already inside and Bill has already left for Mexico (see Biography).",
        "Seth connaît la bande que traque John et lui offre un moyen d'entrer dans Fort Mercer, une fois la carte retrouvée (voir la biographie). Le jour de l'assaut, Seth est déjà dans la place et Bill est déjà parti au Mexique (voir la biographie).")},
    {"img": "irish.jpeg", "slug": "irish", "name": "Irish", "text": two(
        "Both are part of the Fort Mercer plan, but they share no scene. When Seth passes on Dickens's message about the machine gun on the road to Tumbleweed (see Biography), John answers: \"Sounds like I need to pay Irish another visit.\"",
        "Tous deux font partie du plan contre Fort Mercer, sans partager aucune scène. Quand Seth lui transmet, sur la route de Tumbleweed, le message de Dickens au sujet de la mitrailleuse (voir la biographie), John répond : \"Sounds like I need to pay Irish another visit.\" (on dirait que je vais devoir rendre une nouvelle visite à Irish).")},
    {"img": None, "slug": None, "name": "The Treasure Hunters", "text": two(
        "An armed gang after the same treasure. They chase the wagon on the road to Tumbleweed, then attack Seth and John in the town (see Biography). Seth: \"The bastards followed me here!\" According to the Red Dead Wiki, their members share Seth's worn clothes and poor hygiene, and John can later wear a Treasure Hunter Outfit to walk into their hideout unharmed.",
        "Une bande armée lancée sur le même trésor. Elle prend le chariot en chasse sur la route de Tumbleweed, puis attaque Seth et John dans la ville (voir la biographie). Seth : \"The bastards followed me here!\" (ces salauds m'ont suivi jusqu'ici !). D'après le Red Dead Wiki, ses membres partagent les vêtements usés et la crasse de Seth, et John peut plus tard revêtir une tenue de chasseur de trésors (Treasure Hunter Outfit) pour entrer sans risque dans leur repaire.")},
    {"img": None, "slug": None, "name": "His family", "text": two(
        "The games show none of his relatives. Seth says he has lost his wife, his children and his business (see In his own words above). Of his mother, he says in \"A Gentle Drive with Friends\": \"I don't like women, partner. I don't. Not since mammy died.\" For his father, see Origins.",
        "Les jeux ne montrent aucun membre de sa famille. Seth dit avoir perdu sa femme, ses enfants et son affaire (voir Dans ses propres mots, plus haut). De sa mère, il dit dans \"A Gentle Drive with Friends\" : \"I don't like women, partner. I don't. Not since mammy died.\" (j'aime pas les femmes, l'ami, non. Plus depuis que maman est morte). Sur son père, voir Origines.")},
]
