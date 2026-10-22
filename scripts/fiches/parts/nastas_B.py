"""Nastas, part B: Personality (official description, observable traits, In his own words, Names, Appearance),
Guide, weapons and horses (the fiche-specific skills section), Relationships (22 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN infobox (gender, location, affiliations, weapons, nationality, occupation), its quote
box, the Background paragraph (education, view of the gang), the trivia items on his name, the flute, the "bastard"
line, the loot, the pronunciation, the moccasins and the voice; the gallery caption "Nastas' character description";
the FR wiki infobox (arme, allié, ennemi); the mission pages and transcripts listed in nastas/missions.txt.
Narrative events are told in part A; entries below point to them.

SOURCE REGISTER (read 22 Oct 2026; wiki cache scripts/v3/work/_m/; notes in scripts/v3/work/nastas/fc/web_notes_BD.txt):
- Official description: Rockstar character card reproduced on the Red Dead Wiki as "Nastas22.jpg" (uploaded 23 Jun
  2010, caption "Nastas' character description"), read on the image (fc/rockstar_card_Nastas22.png): "A Native
  American unsure about the joys of life on a reservation." Rockstar's 6 Sep 2018 descriptions
  (sources/thr_descriptions.txt) cover the RDR2 gang only: none for Nastas.
- Transcripts (every quoted line checked): "Bear One Another's Burdens/dialogues", "At Home with Dutch/dialogues",
  "For Purely Scientific Purposes/dialogues".
- Mission pages: "Bear One Another's Burdens" (failure conditions, Nastas's health gauge while carried, one-handed
  shooting), "At Home with Dutch" (failure conditions, the miner, the Tobiano Pinto, the "bastard" trivia),
  "For Purely Scientific Purposes" (failure conditions, killing his horse after his death, fast horses, loot of
  around 7 dollars, Enepay/Kosumi/Hinto).
- Red Dead Wiki "Nastas" trivia: name meaning, flute, loot of 4 to 7 dollars, "Nosstas"/"Nastoss", moccasins.
- Blackwater Ledger No. 59 notice (ireddead transcription, reyes/fc/ireddead_newspapers.txt): "Nastas (Surname
  Unknown), of Indian descent" (Names only; the notice itself is told in part A).
- Visual check: live portrait.jpeg (characters/nastas/) and the Rockstar card, for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only: the Rockstar card; "No, sir. I grew up on a reservation and attended school.", "But we hunt to eat,
  not for sport. Soon there will be no buffalo left.", "Enjoy it while you still can. Soon you will have cut down all
  of these trees.", "There is no respect for the land anymore.", "My people have already endured many disasters.
  Before, this was all our land." (In his own words); "Kid got shot in the leg, beat up pretty good.", "You shut your
  mouth, you treacherous snake!", Ross's "this savage" and "the Indian" (Names). Part C Quotes must not repeat these;
  C keeps "For a wise man...", "our informant", "This is not what we agreed.",
  the hotel-room line, the bear line, the skin-sample line.
- Gameplay (failure conditions, health gauge, horse, loot, the "bastard" reaction) lives HERE; part C Trivia must not
  repeat it.
- Relationship entries are one-clause pointers to part A (wreck, cliffs, Bearclaw Camp, Ledger notice, Undead
  Nightmare).

WIKI-ONLY (kept, attributed): the Cattleman Revolver, Double-barreled Shotgun and Repeater Carbine (EN infobox; the FR
infobox lists only the Cattleman); the flute; the "bastard" reaction; the loot (4 to 7 dollars on the character page,
"around 7" on the mission page); "Nosstas" / "Nastoss"; the moccasins; the Navajo meaning of the name; the Tobiano
Pinto; the miner's cut to his arm (mission page); the Tobiano Pinto canter glitch (mission page trivia). Quick Tom Candle is in part C Trivia only.

Excluded: "openly critical of government policy" and "the criminal response of his fellow tribesmen" as our words
(wiki interpretation; his own lines given instead); "It can be assumed that he agreed to infiltrate the gang"
(speculation; the FR wiki even says he was a former gang member: unsupported by any transcript); the Apache theory
(wiki speculation); "John appears to sympathize" / "view Nastas with respect" (interpretation); "Marston identifies
with this" (interpretation); Nastas as a "teenage boy" (mission page walkthrough, contradicted by his adult model;
only John's "Kid" is reported, as John's word); "regarding American civilization with resigned disdain" (wiki
interpretation); "one of the only non-hostile Native Americans" with Hassun and Chogan (left to C if anywhere); the
glitch face (C); "a brilliant savage companion" attributed to MacDougal by the MacDougal wiki page (no transcript line);
the FR wiki's line that Nastas calls MacDougal "a great man, deep down" (no transcript line).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "A Rockstar character card for Red Dead Redemption, reproduced on the Red Dead Wiki, sums him up in one line: \"A Native American unsure about the joys of life on a reservation.\" In the game, he calls the men he works with \"sir\", \"Professor\" and \"Mr. Marston\".",
        "Une carte de personnage publiée par Rockstar pour Red Dead Redemption, reproduite sur le Red Dead Wiki, le résume en une ligne : \"A Native American unsure about the joys of life on a reservation.\" (un Amérindien qui doute des joies de la vie dans une réserve). Dans le jeu, il s'adresse à ceux avec qui il travaille en les appelant \"sir\", \"Professor\" ou \"Mr. Marston\".")},
    {"p": two(
        "He corrects Harold MacDougal's assumptions about him, and tells the professor that he is a very stupid man for a wise one (see Quotes). He speaks about the land, the forests and the buffalo, and blames the white man for their loss.",
        "Il reprend Harold MacDougal quand celui-ci se fait des idées sur lui, et finit par lui dire qu'il est bien bête pour un savant (voir Citations). Il parle de la terre, des forêts et des bisons, dont il impute la disparition à l'homme blanc.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "When MacDougal greets him with mock metaphors, in \"At Home with Dutch\": \"No, sir. I grew up on a reservation and attended school.\" On the buffalo hunters met on the way to Cochinay: \"But we hunt to eat, not for sport. Soon there will be no buffalo left.\" Riding into Tall Trees: \"Enjoy it while you still can. Soon you will have cut down all of these trees.\" Then: \"There is no respect for the land anymore.\" Back in Blackwater, when MacDougal wants to save the Natives of Dutch's gang from disaster: \"My people have already endured many disasters. Before, this was all our land.\"",
        "Quand MacDougal l'accueille avec des métaphores de pacotille, dans \"At Home with Dutch\" : \"No, sir. I grew up on a reservation and attended school.\" (non, monsieur. J'ai grandi dans une réserve et je suis allé à l'école). Sur les chasseurs de bisons croisés en route vers Cochinay : \"But we hunt to eat, not for sport. Soon there will be no buffalo left.\" (mais nous, nous chassons pour manger, pas pour le plaisir. Bientôt, il n'y aura plus un seul bison). En entrant dans Tall Trees : \"Enjoy it while you still can. Soon you will have cut down all of these trees.\" (profitez-en tant que vous le pouvez. Bientôt, vous aurez abattu tous ces arbres). Puis : \"There is no respect for the land anymore.\" (on ne respecte plus la terre). De retour à Blackwater, quand MacDougal veut sauver d'un désastre les Amérindiens de la bande de Dutch : \"My people have already endured many disasters. Before, this was all our land.\" (mon peuple a déjà subi bien des désastres. Avant, toute cette terre était à nous).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Nastas is the only name the game gives him, and the notice of his death in the Blackwater Ledger gives no surname either (see Biography). According to the Red Dead Wiki, Nastas is a Navajo name meaning \"curve-like foxtail grass\". In the game, his name is spoken \"Nosstas\" by John and Fordham and at times \"Nastoss\" by MacDougal, according to the Red Dead Wiki. The agents mostly call him the informant. In the car, Ross asks who \"this savage\" is, then calls him \"the Indian\". Carrying him into MacDougal's office, John calls him a kid: \"Kid got shot in the leg, beat up pretty good.\" Before shooting him, Enepay calls him a snake: \"You shut your mouth, you treacherous snake!\"",
        "Nastas est le seul nom que le jeu lui donne, et l'avis de décès paru dans le Blackwater Ledger ne lui connaît pas de nom de famille (voir la biographie). Selon le Red Dead Wiki, Nastas est un prénom navajo qui signifie \"curve-like foxtail grass\" (herbe à queue de renard incurvée). Toujours d'après ce wiki, John et Fordham disent \"Nosstas\" en le prononçant, et MacDougal, à l'occasion, \"Nastoss\". Pour les agents, il est surtout l'informateur. Dans la voiture, Ross demande qui est \"this savage\" (ce sauvage), puis parle de lui comme de \"the Indian\" (l'Indien). En le portant dans le bureau de MacDougal, John parle de lui comme d'un gamin : \"Kid got shot in the leg, beat up pretty good.\" (le gamin a pris une balle dans la jambe, et une bonne raclée). Avant de l'abattre, Enepay le traite de serpent : \"You shut your mouth, you treacherous snake!\" (ferme-la, sale serpent de traître !)")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He has shoulder-length black hair held by a red headband, and wears a turquoise earring and a turquoise necklace. He wears a pale grey jacket over a dark shirt. According to the Red Dead Wiki, he wears moccasin-style shoes, stitched along the side.",
        "Il a des cheveux noirs mi-longs retenus par un bandeau rouge, une boucle d'oreille et un collier de turquoise. Il porte une veste gris clair sur une chemise sombre. Le Red Dead Wiki lui prête des chaussures de type mocassin, cousues sur le côté.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Suggested section title for the module: "Guide, weapons and horses" / "Guide, armes et chevaux".
BLOCKS_SKILLS = [
    {"h4": two("Guide and informant", "Guide et informateur")},
    {"p": two(
        "The Bureau uses him as an informant on Dutch's new gang, and the agents act on his tip at the wreck of the Serendipity (see Biography). He leads John and MacDougal to Cochinay by a route he says is unguarded, finds a way up the cliffs and takes John through an old mine shaft. He arranges the meeting with some of Dutch's men at the Bear Claw cabin (see Biography). He speaks English, as Fordham tells Ross in the car.",
        "Le Bureau l'emploie comme informateur sur la nouvelle bande de Dutch, et les agents suivent son renseignement jusqu'à l'épave du Serendipity (voir la biographie). Il conduit John et MacDougal vers Cochinay par un chemin qu'il dit non gardé, trouve un passage dans les falaises et fait traverser à John une ancienne galerie de mine. C'est lui qui organise la rencontre avec des hommes de Dutch à la cabane de Bear Claw (voir la biographie). Il parle anglais, comme Fordham le précise à Ross dans la voiture.")},
    {"h4": two("Weapons", "Armes")},
    {"p": two(
        "The English-language Red Dead Wiki lists a Cattleman Revolver, a Double-barreled Shotgun and a Repeater Carbine; the French-language wiki lists only the Cattleman Revolver. In the mine of \"At Home with Dutch\", he kills the miner who attacks him (see Biography). The wiki's \"Murders Committed\" list counts this miner as his only kill, in self-defense. According to the Red Dead Wiki, Nastas also owns a carved flute of his own, which he plays well.",
        "Le Red Dead Wiki anglophone lui attribue un Cattleman Revolver, un fusil de chasse à deux coups (Double-barreled Shotgun) et une Repeater Carbine ; le wiki francophone ne cite que le Cattleman Revolver. Dans la mine de \"At Home with Dutch\", il tue le mineur qui l'attaque (voir la biographie). La liste des meurtres du wiki ne compte que cette victime, tuée en légitime défense. D'après le Red Dead Wiki, Nastas possède aussi une flûte sculptée qui lui appartient, et dont il joue avec aisance.")},
    {"h4": two("Horses", "Chevaux")},
    {"p": two(
        "He brings the horses round for John and MacDougal in both of MacDougal's missions. According to the mission page of \"At Home with Dutch\", his horse is a Tobiano Pinto. The same page notes a glitch in which his Tobiano Pinto sometimes stays at a canter while the other two horses gallop towards Tall Trees. The page of \"For Purely Scientific Purposes\" notes that his horse and MacDougal's are unusually fast in that mission, faster than an American Standardbred or a War Horse, which makes them hard to keep up with.",
        "Dans les deux missions de MacDougal, c'est lui qui amène les chevaux à John et au professeur. D'après la page de la mission \"At Home with Dutch\", il monte un Tobiano Pinto. La même page signale un bug : il arrive que son Tobiano Pinto reste au petit galop pendant que les deux autres chevaux filent au grand galop vers Tall Trees. La page de \"For Purely Scientific Purposes\" relève que son cheval et celui de MacDougal sont anormalement rapides dans cette mission, plus qu'un American Standardbred ou qu'un War Horse, si bien qu'il est difficile de les suivre.")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "In \"Bear One Another's Burdens\", the mission fails if John assaults or kills Nastas or lets Dutch's men kill him. While John carries him, Nastas has his own health gauge and John can shoot with one hand only. \"At Home with Dutch\" and \"For Purely Scientific Purposes\" fail if John assaults, kills or abandons him or kills his horse. In the second, killing his horse after Nastas is dead still fails the mission, according to its page. According to the Red Dead Wiki, if John shoots an animal on the ride to Cochinay, Nastas calls him a bastard. His body can be looted after his death without any loss of honor or failure: the character page gives four to seven dollars, the mission page around seven.",
        "Dans \"Bear One Another's Burdens\", la mission échoue si John agresse ou tue Nastas, ou laisse les hommes de Dutch le tuer. Tant que John le porte, Nastas a sa propre jauge de santé et John ne peut tirer que d'une main. \"At Home with Dutch\" et \"For Purely Scientific Purposes\" échouent si John l'agresse, le tue, l'abandonne ou abat son cheval. Dans la seconde, d'après sa page, tuer son cheval alors que Nastas est déjà mort fait encore échouer la mission. Selon le Red Dead Wiki, si John abat un animal sur la route de Cochinay, Nastas le traite de salaud (bastard). On peut fouiller son corps après sa mort sans perdre d'honneur ni faire échouer la mission : la page du personnage parle de quatre à sept dollars, celle de la mission d'environ sept.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
# One-clause pointers: every event is told in the Biography (part A).
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "John carries him off the wreck of the Serendipity, Nastas later carries John down from the cliffs at Cochinay, and John kills the three men who shoot Nastas at Bearclaw Camp (see Biography).",
        "John le sort de l'épave du Serendipity, Nastas redescend plus tard John des falaises de Cochinay, et John tue les trois hommes qui abattent Nastas à Bearclaw Camp (voir la biographie).")},
    {"img": "harold-macdougal.jpeg", "slug": "harold-macdougal", "name": "Harold MacDougal", "text": two(
        "Ross leaves the wounded Nastas with the professor, who later signs the notice of his death in the Blackwater Ledger (see Biography).",
        "Ross confie Nastas, blessé, au professeur, qui signera plus tard son avis de décès dans le Blackwater Ledger (voir la biographie).")},
    {"img": "edgar-ross.jpeg", "slug": "edgar-ross", "name": "Edgar Ross", "text": two(
        "Ross, who says he cannot communicate with Natives himself, leaves him with MacDougal on the drive back from the Serendipity (see Biography).",
        "Ross, qui avoue ne pas savoir communiquer avec les Amérindiens, décide au retour du Serendipity de le confier à MacDougal (voir la biographie).")},
    {"img": "archer-fordham.jpeg", "slug": "archer-fordham", "name": "Archer Fordham", "text": two(
        "Fordham, who knows him as the Bureau's informant, recognizes him tied up on the wreck of the Serendipity (see Biography).",
        "Fordham, pour qui il est l'informateur du Bureau, le reconnaît ligoté sur l'épave du Serendipity (voir la biographie).")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "The two men never share a scene; Dutch's men leave Nastas tied up on the Serendipity and later kill him at Bearclaw Camp (see Biography). Benjamin Byron Davis voices both characters (see Development and performance).",
        "Les deux hommes n'apparaissent jamais ensemble ; les hommes de Dutch laissent Nastas ligoté sur le Serendipity, puis le tuent à Bearclaw Camp (voir la biographie). Benjamin Byron Davis prête sa voix aux deux personnages (voir Conception et interprétation).")},
    {"img": None, "slug": None, "name": "Enepay, Kosumi and Hinto", "text": two(
        "Three Native members of Dutch's gang who wait in the Bearclaw Camp cabin; Enepay shoots Nastas and John kills all three (see Biography). Their names are those given by the Red Dead Wiki.",
        "Trois Amérindiens de la bande de Dutch qui attendent dans la cabane de Bearclaw Camp ; Enepay abat Nastas, et John tue les trois hommes (voir la biographie). Leurs noms sont ceux que donne le Red Dead Wiki.")},
]
