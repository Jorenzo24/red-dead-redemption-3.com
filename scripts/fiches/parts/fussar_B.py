"""Alberto Fussar, part B: Personality (descriptions, In his own words, Names, Appearance), Power on Guarma
(office, plantation, soldiers and navy, weapons), Relationships (22 Oct 2026, medium tier).

Sources (register, fetched 22 Oct 2026):
- Rockstar published no 6 Sep 2018 character description of Fussar (scripts/v3/sources/thr_descriptions.txt covers
  the Van der Linde gang only); no official guide biography page was found for him.
- Full fan transcript of RDR2, Game Scripts Wiki (game-scripts-wiki.blogspot.com/2022/01/red-dead-redemption-2.html,
  saved locally as scripts/v3/work/fussar/fc/gsw.txt, gitignored): "The Gilded Cage" (Bronte on the balcony),
  "Welcome to the New World" (Levi Simon, Hercule, Leon Fuentes), "A Kind and Benevolent Despot" (Arthur and Dutch,
  Fussar, Javier, Fussar's speech; Fussar's lines to his men are labeled "In Spanish", i.e. English subtitles),
  "Hell Hath No Fury" (Hercule, Bill, Micah, Dutch), "Paradise Mercifully Departed" (Micah, Hercule, standoff,
  tower), chapter 6 Dutch on Cornwall's sugar business. The Red Dead Wiki has no "/dialogues" page for any of
  Fussar's three missions.
- Red Dead Wiki EN "Alberto Fussar" (infobox: aka Colonel Fussar, Mr. Fussar; weapons Schofield Revolver and sabre;
  quote box and Quotes list; Appearance; Trivia), FR "Alberto Fussar" (Gatling gun on the tower), mission pages
  "The Gilded Cage", "A Kind and Benevolent Despot", "Paradise Mercifully Departed" (Gatling gun; "either destroys the
  tower ... with a cannon or shoots him"), pages "Levi Simon", "Leon Fuentes", "Hercule Fontaine", "Cuban Military"
  (Angel as Fussar's interrogator), "Aguasdulces", "Guarma", "Guarma Rebels".
- In-game newspapers: "Guarma Island Sugar Boom" (Blackwater Ledger No. 67, New Hanover Gazette No. 32, Saint Denis
  Times No. 48), "Leader of Guarma Assassinated" (Blackwater Ledger No. 68, Saint Denis Times No. 49, New Hanover
  Gazette No. 33).
- Live portrait and gallery images (assets/characters/alberto-fussar/) for the Appearance sentences.
- Fact-checked fiches reused: leviticus_B (sugar article, "a great friend of America"), angelo_A/B (Bronte's balcony
  scene), javier_A/B/C, arthur_C/D, dutch_B/C/D, micah_A/B, bill_A.

Ownership: the descriptive phrases of the two newspapers ("controversial figure", "flamboyant at times and cruel at
others", "quasi-military rule", the obituary's praise), Leon's "tyrant" line, Bronte's "whore and despoil" line,
Micah's "thorough, nasty and vindictive" and Arthur's "This goddamn idiot" are quoted HERE (Personality) and must not
be quoted in A or C. In his own words takes three Fussar lines: the mule line, the striking-workers speech up to "our
duty is to be fierce", and the cowards line; part C Quotes must use other lines ("You maggots are going to die.",
"The US Navy is on the way.", "The last few days ...", "I always loved... Mexicans", "Does anyone believe him?").
Quoted in Power on Guarma (not elsewhere): Simon's "third most productive sugar plantation in the Northern
Caribbean" and "a lot of very powerful friends", Hercule's "He will have the money to get more", "fourteen hour
shifts" wording (paraphrased), "reportedly feared across the island". The narrative of the assassination article
(coup, "several white men") and of "Unrest in the Tropics" (1907, McKnight) belongs to part A.

WIKI-ONLY (attributed): aliases list; Schofield revolver and sabre; nationality Cuban and the name "Cuban Military";
Angel as interrogator; layout of the Aguasdulces estate (manor, cages, mill); one-shot kill trivia.

Excluded: service in the Spanish army and transfer to the Cuban army (wiki inference from medals, source = a Reddit
post); "born in Cuba, long before the American occupation" ("likely" in the wiki); "enslaved nearly the entirety of the
population" and "anyone opposing him would be tortured and executed" (wiki wording, beyond what the game shows:
Leon's "little more than slaves" is quoted instead); "takes pleasure", "open delight", "arrogant and prideful"
(wiki interpretation); the Allende comparison (fan analysis, wiki trivia); the wiki's "black jeans" outfit detail
(outfit catalogue, gallery captions instead); "his bondage methods the most brutal in the franchise" (Hate Sink Wiki,
fan site).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include Fussar. The in-game newspaper article \"Guarma Island Sugar Boom\", published in chapter 4, reports that his detractors call him \"a controversial figure who is flamboyant at times and cruel at others\", and that he holds Guarma \"under a quasi-military rule\". After his death, \"Leader of Guarma Assassinated\" reports that American business leaders describe him as \"a kind and effective leader who brought peace and prosperity to the region\". The same article says they saw him as \"a progressive leader and humanitarian\" who supported workers' rights.",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang Van der Linde et ne comprennent pas Fussar. L'article de presse \"Guarma Island Sugar Boom\", paru dans le jeu au chapitre 4, rapporte que ses détracteurs voient en lui \"a controversial figure who is flamboyant at times and cruel at others\" (une figure controversée, tantôt flamboyante, tantôt cruelle), et qu'il tient Guarma \"under a quasi-military rule\" (sous un régime quasi militaire). Après sa mort, \"Leader of Guarma Assassinated\" relaie l'avis des milieux d'affaires américains, pour qui il était \"a kind and effective leader who brought peace and prosperity to the region\" (un dirigeant bienveillant et efficace qui a apporté la paix et la prospérité à la région). Le même article ajoute qu'ils le tenaient pour \"a progressive leader and humanitarian\" (un dirigeant progressiste et humaniste), défenseur des droits des travailleurs.")},
    {"p": two(
        "The people of Guarma describe him otherwise. Asked by Dutch who Fussar is, the rebel Leon Fuentes answers: \"A tyrant, driven by nothing but power and greed. Our only purpose is to work ourselves to death... to make him rich.\" In Saint Denis, Angelo Bronte says the governor \"comes here to whore and despoil himself\". Before the last attack on Aguasdulces, Micah says: \"I like the man's style... he's thorough, nasty and vindictive.\" When Fussar opens fire from the tower, Arthur calls him \"This goddamn idiot\".",
        "Les habitants de Guarma en donnent une autre image. Quand Dutch demande qui est ce Fussar, le rebelle Leon Fuentes répond : \"A tyrant, driven by nothing but power and greed. Our only purpose is to work ourselves to death... to make him rich.\" (un tyran, que seuls le pouvoir et la cupidité font avancer ; notre seule raison d'être, c'est de nous tuer à la tâche pour l'enrichir). À Saint-Denis, Angelo Bronte affirme que le gouverneur \"comes here to whore and despoil himself\" (vient ici courir les filles et se vautrer dans la débauche). Avant l'ultime attaque contre Aguasdulces, Micah lâche : \"I like the man's style... he's thorough, nasty and vindictive.\" (j'aime son style : il est méticuleux, méchant et rancunier). Quand Fussar ouvre le feu depuis la tour, Arthur le traite de \"This goddamn idiot\" (ce foutu crétin).")},
    {"p": two(
        "On Guarma, Fussar addresses his soldiers in Spanish and speaks English to his prisoner and to the gang. He questions a captive in front of his troops and turns to them for their verdict. In a speech to his men, he holds up the United States as a model of order (see In his own words). In the cabin standoff, he is the one who breaks away and runs (see Biography).",
        "À Guarma, Fussar s'adresse à ses soldats en espagnol et parle anglais à son prisonnier comme à la bande. Il interroge un captif devant sa troupe et la prend à témoin. Dans un discours à ses hommes, il érige les États-Unis en modèle d'ordre (voir Dans ses propres mots). Lors du face-à-face dans la cabane, c'est lui qui rompt et s'enfuit (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "No transcript of his scenes is published on the Red Dead Wiki; the lines below are checked against a fan transcript of the game and against the wiki's quote list. His lines to the soldiers are spoken in Spanish and quoted here from the English subtitles. To Javier, who claims he never met the other castaways, he says: \"Mr. Simon doesn't believe you... even the mule doesn't believe you.\" To his troops at Aguasdulces: \"Men... I was just in America... do you know how they deal with striking workers there? Do you know? They shoot them! That is civilization. That is future. That is law and order and that is what we must bring to this place. And this is how we will deal with them here... our duty is to be fierce.\" A little later, in the same speech: \"...cowards are the worst traitors of all, for they don't mean their betrayal, but it is betrayal all the same.\"",
        "Le Red Dead Wiki ne publie aucune transcription de ses scènes ; les répliques suivantes sont vérifiées sur une transcription du jeu réalisée par des fans et sur la liste de citations du wiki. Ce qu'il dit à ses soldats est prononcé en espagnol et cité ici d'après les sous-titres anglais. À Javier, qui jure n'avoir jamais vu les autres naufragés, il répond : \"Mr. Simon doesn't believe you... even the mule doesn't believe you.\" (M. Simon ne vous croit pas... même la mule ne vous croit pas). À sa troupe, à Aguasdulces : \"Men... I was just in America... do you know how they deal with striking workers there? Do you know? They shoot them! That is civilization. That is future. That is law and order and that is what we must bring to this place. And this is how we will deal with them here... our duty is to be fierce.\" (Messieurs, je reviens d'Amérique... vous savez comment ils traitent les ouvriers en grève, là-bas ? Vous le savez ? Ils les abattent ! Voilà la civilisation. Voilà l'avenir. Voilà la loi et l'ordre, et c'est ce que nous devons apporter ici. Et c'est ainsi que nous les traiterons... notre devoir est d'être impitoyables). Un peu plus loin, dans le même discours : \"...cowards are the worst traitors of all, for they don't mean their betrayal, but it is betrayal all the same.\" (les lâches sont les pires des traîtres, car ils ne trahissent pas exprès, mais c'est une trahison quand même).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "His full name, Alberto Fussar, is given by Bronte at the party and by the newspapers. Hercule calls him Colonel Fussar. His overseer Levi Simon, Dutch and Micah say Mr. Fussar; Micah adds a sarcastic \"Nice Mr. Fussar\". The newspapers call him the governor of Guarma. The Red Dead Wiki lists Colonel Fussar and Mr. Fussar as his aliases.",
        "Son nom complet, Alberto Fussar, est donné par Bronte lors de la réception et par les journaux. Hercule l'appelle le colonel Fussar. Son contremaître Levi Simon, Dutch et Micah disent Mr. Fussar ; Micah y ajoute un \"Nice Mr. Fussar\" ironique (ce brave M. Fussar). Les journaux le désignent comme le gouverneur de Guarma. Le Red Dead Wiki retient Colonel Fussar et Mr. Fussar comme surnoms.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "Fussar has dark hair combed straight back, a curled, waxed mustache and stubble. At the mayor's party he wears a uniform decorated with medals. On Guarma he wears a blue vest over a white shirt, with a watch chain and a sabre at his side.",
        "Fussar a les cheveux bruns plaqués en arrière, une moustache cirée aux pointes recourbées et une barbe de quelques jours. À la réception du maire, il porte un uniforme couvert de médailles. À Guarma, il est en gilet bleu sur une chemise blanche, chaîne de montre au gilet et sabre au côté.")},
]

# ---------------------------------------------------------------- SKILLS (section title: "Power on Guarma")
BLOCKS_SKILLS = [
    {"h4": two("Governor and colonel", "Gouverneur et colonel")},
    {"p": two(
        "Fussar holds two titles: governor of Guarma, in the newspapers, and colonel, in Hercule's mouth. The Red Dead Wiki places him at the head of the Cuban Military on the island and gives his nationality as Cuban; the game itself never states it. The article \"Guarma Island Sugar Boom\" describes the sugar that Leviticus Cornwall imports from the island as Cuban sugar. His seat is Aguasdulces, which Hercule points out to the gang as \"Fussar's compound\". According to the Red Dead Wiki, the estate is enclosed by a stone wall and includes a manor, cages for prisoners, a sugar factory and a mill.",
        "Fussar porte deux titres : gouverneur de Guarma, dans les journaux, et colonel, dans la bouche d'Hercule. Le Red Dead Wiki le place à la tête de l'armée cubaine sur l'île et lui attribue la nationalité cubaine ; le jeu, lui, ne la précise jamais. L'article \"Guarma Island Sugar Boom\" présente le sucre que Leviticus Cornwall importe de l'île comme du sucre cubain. Il siège à Aguasdulces, qu'Hercule désigne à la bande comme le \"Fussar's compound\" (le domaine de Fussar). D'après le Red Dead Wiki, la propriété est ceinte d'un mur de pierre et comprend un manoir, des cages pour les prisonniers, une sucrerie et un moulin.")},
    {"h4": two("The sugar plantation", "La plantation sucrière")},
    {"p": two(
        "Levi Simon introduces himself as \"Senior Overseer for Alberto Fussar\" and boasts: \"We run the third most productive sugar plantation in the Northern Caribbean.\" Hercule explains that the cane cut by the workers is processed in the factory at Aguasdulces. Leon Fuentes says the workers are \"little more than slaves shipped in from other islands\", and that a group of them has just fled into the jungle. \"Guarma Island Sugar Boom\" reports that plantation workers often put in 14-hour shifts, and that his security force is \"reportedly feared across the island\". Cornwall buys the island's sugar under an exclusive purchase order (see Relationships).",
        "Levi Simon se présente comme \"Senior Overseer for Alberto Fussar\" (contremaître en chef d'Alberto Fussar) et se vante : \"We run the third most productive sugar plantation in the Northern Caribbean.\" (nous faisons tourner la troisième plantation sucrière la plus productive des Caraïbes du Nord). Hercule explique que la canne coupée par les ouvriers est traitée dans la sucrerie d'Aguasdulces. Leon Fuentes décrit des travailleurs \"little more than slaves shipped in from other islands\" (guère plus que des esclaves amenés d'autres îles), dont un groupe vient de s'enfuir dans la jungle. Selon \"Guarma Island Sugar Boom\", les ouvriers des plantations enchaînent souvent des journées de 14 heures, et sa milice serait \"reportedly feared across the island\" (redoutée, dit-on, dans toute l'île). Cornwall achète le sucre de l'île en vertu d'une commande exclusive (voir Relations).")},
    {"h4": two("Soldiers, navy and guns", "Soldats, marine et canons")},
    {"p": two(
        "Fussar commands uniformed soldiers who patrol the island, chain prisoners and guard Aguasdulces. Simon warns Dutch that \"Mr. Fussar has a lot of very powerful friends\". The Red Dead Wiki names one of his men, Angel, as his interrogator. Hercule tells the gang that Fussar knows who they are and the price on their heads, and that he has called in the navy from Cuba; a warship then shells the fort of Cinco Torres. After it sinks, Micah reports that Fussar holds the ship's captain and has set up gun positions to fire on any boat that tries to sail. During the fighting, Arthur asks how many men Fussar has, and Hercule answers: \"It doesn't matter how many we kill. He will have the money to get more.\"",
        "Fussar commande des soldats en uniforme qui patrouillent sur l'île, enchaînent les prisonniers et gardent Aguasdulces. Simon prévient Dutch que \"Mr. Fussar has a lot of very powerful friends\" (M. Fussar a beaucoup d'amis très puissants). Le Red Dead Wiki désigne l'un de ses hommes, Angel, comme son interrogateur. Hercule apprend à la bande que Fussar sait qui ils sont et combien vaut leur tête, et qu'il a fait venir la marine de Cuba ; un navire de guerre bombarde ensuite le fort de Cinco Torres. Une fois le bateau coulé, Micah rapporte que Fussar retient le capitaine du navire et a installé des pièces d'artillerie pour tirer sur toute embarcation qui tenterait de partir. Pendant les combats, Arthur demande combien d'hommes a Fussar, et Hercule répond : \"It doesn't matter how many we kill. He will have the money to get more.\" (peu importe combien on en tue, il aura l'argent pour en trouver d'autres).")},
    {"h4": two("Weapons", "Armes")},
    {"p": two(
        "The Red Dead Wiki gives him a Schofield revolver and a sabre. He draws a revolver on Dutch in the cabin standoff and fires several shots into the air as he flees. Sources differ on the gun he uses from the tower over the harbor: the Red Dead Wiki's page on Fussar and the stage notes of the fan transcript speak of a cannon, while the wiki's mission page and the French Red Dead Wiki describe a Gatling gun. According to the mission page, Arthur can either bring down the tower with a cannon or shoot Fussar directly. The character page adds that a single shot from any gun kills him if the player finds the right angle.",
        "Le Red Dead Wiki lui attribue un revolver Schofield et un sabre. Il braque un revolver sur Dutch lors du face-à-face dans la cabane et tire plusieurs coups en l'air en s'enfuyant. Les sources divergent sur l'arme qu'il utilise du haut de la tour qui domine le port : la page du Red Dead Wiki consacrée à Fussar et les indications scéniques de la transcription des fans parlent d'un canon, tandis que la page de la mission et le Red Dead Wiki francophone décrivent une mitrailleuse Gatling. D'après la page de la mission, Arthur peut soit abattre la tour d'un coup de canon, soit tirer directement sur Fussar. La page du personnage ajoute qu'une seule balle, de n'importe quelle arme, suffit à le tuer si le joueur trouve le bon angle.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "leviticus-cornwall.jpeg", "slug": "leviticus-cornwall", "name": "Leviticus Cornwall", "text": two(
        "The industrialist buys Guarma's sugar from Fussar under an exclusive purchase order, after two trips to tour the island's plantations, according to \"Guarma Island Sugar Boom\". The same article reports that Cornwall called the governor \"a great friend of America\". In chapter 6, Dutch tells Arthur that Cornwall's sugar business is destroying the people of Guarma.",
        "L'industriel achète le sucre de Guarma à Fussar en vertu d'une commande exclusive, après deux voyages pour visiter les plantations de l'île, selon \"Guarma Island Sugar Boom\". Le même article rapporte que Cornwall a qualifié le gouverneur de \"a great friend of America\" (un grand ami de l'Amérique). Au chapitre 6, Dutch dit à Arthur que le commerce sucrier de Cornwall détruit le peuple de Guarma.")},
    {"img": None, "slug": None, "name": "Levi Simon", "text": two(
        "The overseer of the plantation, an American according to the Red Dead Wiki, is Fussar's right-hand man. His patrol arrests the castaways, and he stands at Fussar's side while Javier is questioned. He dies in the cabin standoff, shot by the ship's captain (see Biography).",
        "Le contremaître de la plantation, un Américain selon le Red Dead Wiki, est le bras droit de Fussar. Sa patrouille arrête les naufragés, et il se tient aux côtés de Fussar pendant l'interrogatoire de Javier. Il meurt lors du face-à-face dans la cabane, abattu par le capitaine du navire (voir la biographie).")},
    {"img": "hercule-fontaine.jpeg", "slug": "hercule-fontaine", "name": "Hercule Fontaine", "text": two(
        "The Haitian smuggler moves goods on and off the island behind the colonel's back and backs the rebels against him. He promises the gang a boat if they help him silence Fussar. Before the attack on Aguasdulces, he says he will fight Fussar every day he can. He draws Fussar's fire at the harbor so that Arthur can reach a cannon (see Biography).",
        "Ce contrebandier haïtien fait entrer et sortir des marchandises de l'île dans le dos du colonel et soutient les rebelles qui le combattent. Il promet un bateau à la bande si elle l'aide à faire taire Fussar. Avant l'attaque d'Aguasdulces, il assure qu'il combattra Fussar chaque jour où il le pourra. Au port, il attire sur lui le feu de Fussar pour permettre à Arthur d'atteindre un canon (voir la biographie).")},
    {"img": None, "slug": None, "name": "Leon Fuentes", "text": two(
        "This rebel is chained with the castaways after his arrest by Fussar's soldiers, then freed in Hercule's ambush. He wants the island's people to rise against Fussar; his description of the colonel is quoted under Personality.",
        "Ce rebelle est enchaîné avec les naufragés après son arrestation par les soldats de Fussar, puis libéré lors de l'embuscade d'Hercule. Il voudrait que la population de l'île se soulève contre Fussar ; le portrait qu'il fait du colonel est cité dans la rubrique Personnalité.")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Captured by Fussar's soldiers, Javier is dragged into Aguasdulces and questioned in front of Fussar, who mocks his claim never to have met the other castaways. Dutch and Arthur free him the same day (see Biography). When the tower falls, Arthur says he got Fussar for Javier.",
        "Capturé par les soldats de Fussar, Javier est traîné jusqu'à Aguasdulces et interrogé devant Fussar, qui se moque de lui quand il jure n'avoir jamais vu les autres naufragés. Dutch et Arthur le libèrent le jour même (voir la biographie). Quand la tour s'effondre, Arthur déclare qu'il a eu Fussar pour Javier.")},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
        "On the way into Aguasdulces, Arthur remembers that Fussar was one of the guests Bronte pointed out at the party in Saint Denis. He is held at gunpoint by Simon in the cabin standoff, then kills Fussar with a cannon shot at the tower (see Biography).",
        "En route vers Aguasdulces, Arthur se souvient que Fussar faisait partie des invités désignés par Bronte à la réception de Saint-Denis. Tenu en joue par Simon lors du face-à-face dans la cabane, il tue ensuite Fussar d'un coup de canon tiré sur la tour (voir la biographie).")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Dutch gives Simon a false name to keep Fussar from learning who the castaways are. On the beach of Cinco Torres, when the warship's shells hit Fussar's own soldiers, he thanks \"Mr. Fussar\" sarcastically. In the cabin he faces Fussar and Simon with a revolver in each hand (see Biography).",
        "Dutch donne un faux nom à Simon pour empêcher Fussar de savoir qui sont les naufragés. Sur la plage de Cinco Torres, quand les obus du navire de guerre touchent les propres soldats de Fussar, il remercie ironiquement \"Mr. Fussar\". Dans la cabane, il tient tête à Fussar et à Simon, un revolver dans chaque main (voir la biographie).")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "When the warship appears, Micah remarks that one has to hand it to Fussar. Sent to meet the captain, he comes back to report that Fussar's men hold him and have set up gun positions, and rigs the batteries with dynamite (see Biography). His verdict on Fussar is quoted under Personality.",
        "Quand le navire de guerre apparaît, Micah reconnaît qu'il faut bien le laisser à Fussar. Envoyé à la rencontre du capitaine, il revient annoncer que les hommes de Fussar le retiennent et ont installé de l'artillerie, et piège les batteries à la dynamite (voir la biographie). Son jugement sur Fussar est cité dans la rubrique Personnalité.")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Bill fights Fussar's soldiers on the beach of Cinco Torres and cheers Arthur on at the cannon against the warship. He stays aboard the ship to guard Javier during the attack on Aguasdulces (see Biography).",
        "Bill combat les soldats de Fussar sur la plage de Cinco Torres et encourage Arthur au canon contre le navire de guerre. Il reste à bord du bateau pour veiller sur Javier pendant l'attaque d'Aguasdulces (voir la biographie).")},
    {"img": None, "slug": None, "name": "The ship's captain", "text": two(
        "The captain Hercule finds for the gang is seized by Fussar's men and held in the workers' cabin at Aguasdulces. In the standoff, Arthur kicks him a rifle and he shoots Simon dead. Before sailing, he says he wants no more surprise interviews with local officials (see Biography).",
        "Le capitaine trouvé par Hercule pour la bande est capturé par les hommes de Fussar et retenu dans la cabane des ouvriers d'Aguasdulces. Lors du face-à-face, Arthur lui envoie un fusil du pied et il abat Simon. Avant d'appareiller, il dit ne plus vouloir d'interrogatoires surprises par les autorités locales (voir la biographie).")},
    {"img": "angelo-bronte.jpeg", "slug": "angelo-bronte", "name": "Angelo Bronte", "text": two(
        "On a balcony at the mayor's party in \"The Gilded Cage\", Bronte points Fussar out to Dutch and Arthur as a sugar planter from the island (see Biography). His remark on Fussar's visits is quoted under Personality.",
        "Sur un balcon, lors de la réception du maire dans \"The Gilded Cage\", Bronte désigne Fussar à Dutch et à Arthur comme un planteur de sucre de l'île (voir la biographie). Sa remarque sur les visites de Fussar est citée dans la rubrique Personnalité.")},
    {"img": None, "slug": None, "name": "Henri Lemieux", "text": two(
        "The mayor of Saint Denis hosts the party where Fussar appears as a guest in chapter 4.",
        "Le maire de Saint-Denis organise la réception où Fussar figure parmi les invités, au chapitre 4.")},
    {"img": None, "slug": None, "name": "Angel", "text": two(
        "The Red Dead Wiki presents this soldier as Fussar's interrogator. Arthur, knocked out by a dart in the jungle, wakes up tied to a chair in front of him and frees himself (see Biography).",
        "Le Red Dead Wiki présente ce soldat comme l'interrogateur de Fussar. Endormi par une fléchette dans la jungle, Arthur se réveille ligoté sur une chaise face à lui, puis se libère (voir la biographie).")},
]
