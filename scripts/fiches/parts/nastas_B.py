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
  Before, this was all our land." (In his own words); "Kid got shot in the leg, beat up pretty good." and "treacherous
  snake" (Names). Part C Quotes must not repeat these; C keeps "For a wise man...", "This is not what we agreed.",
  the hotel-room line, the bear line, the skin-sample line.
- Gameplay (failure conditions, health gauge, horse, loot, the "bastard" reaction) lives HERE; part C Trivia must not
  repeat it.
- Relationship entries are one-clause pointers to part A (wreck, cliffs, Bearclaw Camp, Ledger notice, Undead
  Nightmare).

WIKI-ONLY (kept, attributed): the Cattleman Revolver, Double-barreled Shotgun and Repeater Carbine (EN infobox; the FR
infobox lists only the Cattleman); the flute; the "bastard" reaction; the loot (4 to 7 dollars on the character page,
"around 7" on the mission page); "Nosstas" / "Nastoss"; the moccasins; the Navajo meaning of the name; the Tobiano
Pinto; the miner's cut to his arm (mission page); the miner model being Quick Tom Candle (mission page trivia).

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
        "A Rockstar character card for Red Dead Redemption, reproduced on the Red Dead Wiki, sums him up in one line: \"A Native American unsure about the joys of life on a reservation.\" In the game, he speaks careful, formal English. He calls the men he works with \"sir\", \"Professor\" and \"Mr. Marston\". He says little, and his answers are short.",
        "Une carte de personnage publiée par Rockstar pour Red Dead Redemption, reproduite sur le Red Dead Wiki, le résume en une ligne : \"A Native American unsure about the joys of life on a reservation.\" (un Amérindien qui doute des joies de la vie dans une réserve). Dans le jeu, il s'exprime dans un anglais soigné et assez formel. Il appelle ceux avec qui il travaille \"sir\", \"Professor\" ou \"Mr. Marston\". Il parle peu, et ses réponses sont brèves.")},
    {"p": two(
        "He corrects Harold MacDougal's assumptions about him calmly, and loses patience only once, when he tells the professor that he is a very stupid man for a wise one (see Quotes). He speaks about the land, the forests and the buffalo whenever the subject comes up, and blames the white man for their loss. He also takes physical risks for others: he leads the climb, fights in the mine and goes back up the mountain for John (see Biography).",
        "Il corrige sans s'emporter les idées toutes faites de Harold MacDougal à son sujet, et ne perd patience qu'une fois, quand il lance au professeur qu'il est bien bête pour un savant (voir Citations). Dès que le sujet se présente, il parle de la terre, des forêts et des bisons, et en impute la perte à l'homme blanc. Il prend aussi des risques physiques pour les autres : il ouvre la voie dans les falaises, se bat dans la mine et remonte la montagne pour aller chercher John (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "When MacDougal greets him with mock metaphors, in \"At Home with Dutch\": \"No, sir. I grew up on a reservation and attended school.\" On the buffalo hunters met on the way to Cochinay: \"But we hunt to eat, not for sport. Soon there will be no buffalo left.\" Riding into Tall Trees: \"Enjoy it while you still can. Soon you will have cut down all of these trees.\" Then: \"There is no respect for the land anymore.\" Back in Blackwater, when MacDougal wants to save the Natives of Dutch's gang from disaster: \"My people have already endured many disasters. Before, this was all our land.\"",
        "Quand MacDougal l'accueille avec des métaphores de pacotille, dans \"At Home with Dutch\" : \"No, sir. I grew up on a reservation and attended school.\" (non, monsieur. J'ai grandi dans une réserve et je suis allé à l'école). Sur les chasseurs de bisons croisés en route vers Cochinay : \"But we hunt to eat, not for sport. Soon there will be no buffalo left.\" (mais nous, nous chassons pour manger, pas pour le plaisir. Bientôt, il n'y aura plus un seul bison). En entrant dans Tall Trees : \"Enjoy it while you still can. Soon you will have cut down all of these trees.\" (profitez-en tant que vous le pouvez. Bientôt, vous aurez abattu tous ces arbres). Puis : \"There is no respect for the land anymore.\" (on ne respecte plus la terre). De retour à Blackwater, quand MacDougal veut sauver d'un désastre les Amérindiens de la bande de Dutch : \"My people have already endured many disasters. Before, this was all our land.\" (mon peuple a déjà subi bien des désastres. Avant, toute cette terre était à nous).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Nastas is the only name the game gives him. The notice of his death in the Blackwater Ledger lists him as \"Nastas (Surname Unknown)\" (see Biography). According to the Red Dead Wiki, Nastas is a Navajo name meaning \"curve-like foxtail grass\". The same wiki notes that John and Fordham pronounce it \"Nosstas\", while MacDougal sometimes says \"Nastoss\". The agents mostly call him the informant, and Ross refers to him as a savage and as \"the Indian\". Carrying him into MacDougal's office, John calls him a kid: \"Kid got shot in the leg, beat up pretty good.\" Enepay calls him a \"treacherous snake\" before shooting him.",
        "Nastas est le seul nom que le jeu lui donne. L'avis de décès paru dans le Blackwater Ledger le désigne comme \"Nastas (Surname Unknown)\", c'est-à-dire sans nom de famille connu (voir la biographie). Selon le Red Dead Wiki, Nastas est un prénom navajo qui signifie \"curve-like foxtail grass\" (herbe à queue de renard incurvée). Le même wiki relève que John et Fordham le prononcent \"Nosstas\", alors que MacDougal dit parfois \"Nastoss\". Les agents parlent surtout de lui comme de l'informateur, et Ross le traite de sauvage avant de l'appeler \"the Indian\" (l'Indien). En le portant dans le bureau de MacDougal, John parle de lui comme d'un gamin : \"Kid got shot in the leg, beat up pretty good.\" (le gamin a pris une balle dans la jambe, et une bonne raclée). Enepay le traite de \"treacherous snake\" (sale serpent, traître) avant de l'abattre.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He has shoulder-length black hair held by a red headband, and wears a turquoise earring and a turquoise necklace. He wears a pale grey jacket over a dark shirt. The Red Dead Wiki notes that his shoes look like moccasins, with stitching visible on the side.",
        "Il a des cheveux noirs mi-longs retenus par un bandeau rouge, une boucle d'oreille et un collier de turquoise. Il porte une veste gris clair sur une chemise sombre. Le Red Dead Wiki remarque que ses chaussures ressemblent à des mocassins, avec des coutures visibles sur le côté.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Suggested section title for the module: "Guide, weapons and horses" / "Guide, armes et chevaux".
BLOCKS_SKILLS = [
    {"h4": two("Guide and informant", "Guide et informateur")},
    {"p": two(
        "The Bureau uses him as an informant on Dutch's new gang, and the agents act on his tip at the wreck of the Serendipity (see Biography). He knows West Elizabeth well: he leads John and MacDougal to Cochinay by a route he says is unguarded, finds a way up the cliffs and spots the mine shaft that leads through the mountain. Because friends of his ride with Dutch, he can also arrange a meeting with some of the gang's men (see Biography). He reads animals: he says the grizzly that crosses their path showed no sign of aggression and would have moved on if left alone (see Quotes). He went to school on the reservation and speaks fluent English: Ross still asks whether he speaks it, and MacDougal addresses him in metaphors until Nastas corrects him.",
        "Le Bureau l'emploie comme informateur sur la nouvelle bande de Dutch, et les agents suivent son renseignement jusqu'à l'épave du Serendipity (voir la biographie). Il connaît bien West Elizabeth : il conduit John et MacDougal jusqu'à Cochinay par un chemin qu'il dit non gardé, trouve un passage dans les falaises et repère la galerie de mine qui traverse la montagne. Comme certains de ses amis ont rejoint Dutch, il est aussi en mesure d'organiser une rencontre avec des hommes de la bande (voir la biographie). Il sait lire le comportement des bêtes : selon lui, le grizzli qui leur barre la route ne montrait aucun signe d'agressivité et serait reparti si on l'avait laissé tranquille (voir Citations). Scolarisé dans la réserve, il parle un anglais courant : Ross lui demande pourtant s'il parle anglais, et MacDougal lui parle par métaphores jusqu'à ce que Nastas le reprenne.")},
    {"h4": two("Weapons", "Armes")},
    {"p": two(
        "The English-language Red Dead Wiki lists a Cattleman Revolver, a Double-barreled Shotgun and a Repeater Carbine; the French-language wiki lists only the Cattleman Revolver. In the mine of \"At Home with Dutch\", he kills the miner who attacks him; according to the mission page, the miner first cuts him in the arm. The wiki's \"Murders Committed\" list counts this miner as his only kill, in self-defense. According to the mission page, the miner uses the model of Quick Tom Candle, a multiplayer character. According to the Red Dead Wiki, Nastas also owns a carved flute of his own, which he plays well.",
        "Le Red Dead Wiki anglophone lui attribue un Cattleman Revolver, un fusil de chasse à deux coups (Double-barreled Shotgun) et une Repeater Carbine ; le wiki francophone ne cite que le Cattleman Revolver. Dans la mine de \"At Home with Dutch\", il tue le mineur qui l'attaque ; d'après la page de la mission, le mineur l'a d'abord entaillé au bras. La liste des meurtres du wiki ne compte que cette victime, tuée en légitime défense. Selon la page de la mission, le mineur reprend le modèle de Quick Tom Candle, un personnage du multijoueur. D'après le Red Dead Wiki, Nastas possède aussi une flûte sculptée qui lui appartient, et dont il joue avec aisance.")},
    {"h4": two("Horses", "Chevaux")},
    {"p": two(
        "He brings the horses round for John and MacDougal in both of MacDougal's missions. According to the mission page of \"At Home with Dutch\", his horse is a Tobiano Pinto. The page of \"For Purely Scientific Purposes\" notes that his horse and MacDougal's are unusually fast in that mission, faster than an American Standardbred or a War Horse, which makes them hard to keep up with.",
        "Dans les deux missions de MacDougal, c'est lui qui amène les chevaux à John et au professeur. D'après la page de la mission \"At Home with Dutch\", il monte un Tobiano Pinto. La page de \"For Purely Scientific Purposes\" relève que son cheval et celui de MacDougal sont anormalement rapides dans cette mission, plus qu'un American Standardbred ou qu'un War Horse, si bien qu'il est difficile de les suivre.")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "In \"Bear One Another's Burdens\", the mission fails if John assaults or kills Nastas or lets Dutch's men kill him. While John carries him, Nastas has his own health gauge and John can shoot with one hand only. \"At Home with Dutch\" and \"For Purely Scientific Purposes\" fail if John assaults, kills or abandons him or kills his horse. In the second, killing his horse after Nastas is dead still fails the mission, according to its page. According to the Red Dead Wiki, if John shoots an animal on the ride to Cochinay, Nastas calls him a bastard. His body can be looted after his death without any loss of honor or failure: the character page gives four to seven dollars, the mission page around seven.",
        "Dans \"Bear One Another's Burdens\", la mission échoue si John agresse ou tue Nastas, ou laisse les hommes de Dutch le tuer. Tant que John le porte, Nastas a sa propre jauge de santé et John ne peut tirer que d'une main. \"At Home with Dutch\" et \"For Purely Scientific Purposes\" échouent si John l'agresse, le tue, l'abandonne ou abat son cheval. Dans la seconde, d'après sa page, tuer son cheval alors que Nastas est déjà mort fait encore échouer la mission. Selon le Red Dead Wiki, si John abat un animal sur la route de Cochinay, Nastas le traite de salaud (bastard). On peut fouiller son corps après sa mort sans perdre d'honneur ni faire échouer la mission : la page du personnage parle de quatre à sept dollars, celle de la mission d'environ sept.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [two(
        "John carries him out of the wreck of the Serendipity, and Nastas later carries John down from the cliffs at Cochinay (see Biography). Nastas addresses him as Mr. Marston and works with him in all three of his missions. When MacDougal talks nonsense about the pow-wow, John turns to Nastas for a straight answer, and Nastas gives it. Back in Blackwater, John thanks both men for the rescue, then leaves Nastas and the professor to their argument.",
        "John le sort de l'épave du Serendipity sur son dos, et Nastas, plus tard, redescend John des falaises de Cochinay (voir la biographie). Nastas l'appelle Mr. Marston et fait équipe avec lui dans ses trois missions. Quand MacDougal se perd dans ses discours sur le \"pow-wow\", c'est à Nastas que John demande une réponse claire, et Nastas la lui donne. De retour à Blackwater, John remercie les deux hommes de l'avoir tiré d'affaire, puis les laisse à leur dispute."),
        two(
        "When Enepay shoots Nastas at Bearclaw Camp, John curses Dutch and kills the three men in the cabin (see Biography).",
        "Quand Enepay abat Nastas à Bearclaw Camp, John maudit Dutch et tue les trois hommes de la cabane (voir la biographie).")]},
    {"img": "harold-macdougal.jpeg", "slug": "harold-macdougal", "name": "Harold MacDougal", "text": [two(
        "Ross leaves the wounded Nastas with the professor, an anthropologist who advises the agents on the Natives of the region (see Biography). MacDougal treats him as a specimen of his theories: he speaks to him in metaphors, wonders whether his anger is a primal emotion and wants skin samples from the gang's feet. Nastas corrects him, contradicts his ideas on the buffalo and on the bear, and calls him a stupid man for a wise one (see Quotes). In the professor's own account, it is Nastas, not he, who carries John down from Cochinay.",
        "Ross confie Nastas, blessé, au professeur, un anthropologue qui conseille les agents sur les Amérindiens de la région (voir la biographie). MacDougal le traite comme un cas d'étude : il lui parle par métaphores, se demande si sa colère est une émotion primitive et voudrait prélever la peau sous les pieds des hommes de la bande. Nastas le reprend, contredit ses idées sur les bisons et sur l'ours, et lui lance qu'il est bien bête pour un savant (voir Citations). De l'aveu même du professeur, c'est Nastas, et non lui, qui a redescendu John de Cochinay."),
        two(
        "On the way to Bearclaw Camp, MacDougal says he is relieved to have Nastas with him. After the ambush, he tells John that his studies, Nastas and the blood samples had led him to believe acculturation was possible, and that he was wrong. He signs the notice of Nastas's death in the Blackwater Ledger (see Biography). In Undead Nightmare, which is not canon, an undead Nastas attacks him in Blackwater (see Biography).",
        "En route vers Bearclaw Camp, MacDougal se dit soulagé d'avoir Nastas à ses côtés. Après l'embuscade, il confie à John que ses recherches, Nastas et les échantillons de sang l'avaient amené à croire l'acculturation possible, et qu'il s'était trompé. C'est lui qui signe l'avis de décès de Nastas dans le Blackwater Ledger (voir la biographie). Dans Undead Nightmare, qui ne fait pas partie du canon, Nastas, devenu mort-vivant, l'attaque à Blackwater (voir la biographie).")]},
    {"img": "edgar-ross.jpeg", "slug": "edgar-ross", "name": "Edgar Ross", "text": two(
        "Nastas is an informant for the Bureau, and Ross acts on his tip about the Serendipity (see Biography). In the car, Ross does not know who he is: he asks whether he is a prisoner, then whether he speaks English. He then has \"the Indian\" taken to MacDougal, saying he cannot communicate with Natives himself.",
        "Nastas renseigne le Bureau, et Ross agit sur son information au sujet du Serendipity (voir la biographie). Dans la voiture, Ross ignore qui il est : il demande si c'est un prisonnier, puis s'il parle anglais. Il le fait ensuite conduire chez MacDougal, en expliquant qu'il n'arrive pas, lui, à communiquer avec les Amérindiens.")},
    {"img": "archer-fordham.jpeg", "slug": "archer-fordham", "name": "Archer Fordham", "text": two(
        "Fordham knows him as \"our informant\". At the empty wreck, he says the informant had better not have lied to them, then recognizes Nastas tied up on the upper deck and orders John to carry him (see Biography). In the car, he tells Ross that Nastas speaks English.",
        "Fordham le connaît comme \"our informant\" (notre informateur). Devant l'épave déserte, il prévient que l'informateur a intérêt à ne pas leur avoir menti, puis reconnaît Nastas ligoté sur le pont supérieur et ordonne à John de le porter (voir la biographie). Dans la voiture, il précise à Ross que Nastas parle anglais.")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "The two men never share a scene. Nastas tells John and MacDougal that Dutch has drawn a following of young men from the reservation, that they are turning to bad things, and that friends of his are among them. Dutch's men beat him and leave him tied up on the Serendipity, where the agents walk into a trap, and other men of the gang kill him at Bearclaw Camp (see Biography). Benjamin Byron Davis voices both characters (see Development and performance).",
        "Les deux hommes n'apparaissent jamais ensemble. Nastas apprend à John et à MacDougal que Dutch a rallié de jeunes hommes de la réserve, qui tournent mal, et que certains de ses amis en font partie. Les hommes de Dutch le rouent de coups et le laissent ligoté sur le Serendipity, où les agents tombent dans un piège, et d'autres membres de la bande le tuent à Bearclaw Camp (voir la biographie). Benjamin Byron Davis prête sa voix aux deux personnages (voir Conception et interprétation).")},
    {"img": None, "slug": None, "name": "Enepay, Kosumi and Hinto", "text": two(
        "Three Native members of Dutch's gang who wait for Nastas, MacDougal and John in the Bearclaw Camp cabin. Enepay calls Nastas a traitor and shoots him; John then kills all three (see Biography). Their names are those given by the mission page and the transcript.",
        "Trois Amérindiens de la bande de Dutch qui attendent Nastas, MacDougal et John dans la cabane de Bearclaw Camp. Enepay traite Nastas de traître et l'abat ; John tue ensuite les trois hommes (voir la biographie). Leurs noms sont ceux de la page de la mission et de la transcription.")},
]
