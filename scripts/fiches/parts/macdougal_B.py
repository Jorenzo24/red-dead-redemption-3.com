"""Harold MacDougal, part B: Personality (official descriptions, observable traits, In his own words, Names, Appearance),
Research, weapons and horses (the fiche-specific skills section), Relationships (22 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN sections Background (the GOTY guide quote box), Personality, Bibliography, the Rockstar
quote box, the infobox (aka, weapon, mounts, family, affiliations, occupation, location), the trivia items on his boots,
the gun used once, the horses' speed, the undead MacDougal after "Curious Tales from Blackwater"; the FR wiki infobox
(surnom "Professeur", allies) and anecdotes (cocaine, insomnia); the pages "Nashoba", "Enepay", "Newlywed",
"Newspaper Characters" (Lionel Fortisque) and the mission pages listed in macdougal/missions.txt. Narrative events are
told in part A; the entries below point to them.

SOURCE REGISTER (read 22 Oct 2026; wiki cache scripts/v3/work/_m/, notes in scripts/v3/work/macdougal/fc/):
- Official descriptions: (1) the quote box of the Red Dead Wiki EN page labelled "Rockstar Games' description of Harold
  MacDougal for Red Dead Redemption" ("A highly-strung anthropology professor, on a forced sabbatical from Yale."); the
  original Rockstar page was not found (web search 22 Oct 2026, fc/web_notes_BD.txt): quoted through the wiki,
  attributed. (2) The Game of the Year Edition guide description, quoted by the same wiki page; the guide itself was not
  read: attributed. Rockstar's 6 Sep 2018 descriptions (sources/thr_descriptions.txt) cover the RDR2 gang only.
- Transcripts (every quoted line checked): "Bear One Another's Burdens/dialogues", "At Home with Dutch/dialogues",
  "For Purely Scientific Purposes/dialogues", "The Prodigal Son Returns (To Yale)/dialogues". No transcript exists for
  "Curious Tales from Blackwater" (wiki page missing).
- Mission pages: failure conditions of "At Home with Dutch", "For Purely Scientific Purposes", "The Prodigal Son Returns
  (To Yale)"; the "only mission in which MacDougal will use his gun" and the speed of his and Nastas's horses (trivia of
  "For Purely Scientific Purposes"); Nashoba as the hostage taker (mission details of "The Prodigal Son Returns (To
  Yale)", and the page "Nashoba"); the undead MacDougal after the opening cutscene ("Curious Tales from Blackwater"
  trivia); "Bear One Another's Burdens" unlocks his strand.
- Newspapers: Blackwater Ledger No. 59 (fc/ireddead_Ledger_No59_text.txt: the hotel attack article and the notice signed
  "Prof. Harold MacDougal Esq."); Blackwater Ledger & Sentinel No. 213, "Anthropologist Turns Savage"
  (fc/ireddead_Ledger_No213_text.txt; FR wiki copy fc/fr_wiki_new_haven_1914.txt); RDR2 "Prominent Yale Scientist Speaks
  Out" (_m/Prominent_Yale_Scientist_Speaks_Out.txt: "The Scourge of Crossbreeding", the "Savage Minds" paper, Benjamin
  Fortescue).
- Consistency: edgar_B (MacDougal entry), dutch_B / dutch_C (Nastas, Bearclaw, the hotel), john_B / john_C / john_D.
- Visual check: live portrait.jpeg and gallery-1.jpeg (characters/harold-macdougal/) for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only (parts A and C must not repeat them): the two official descriptions (Personality); "It's my job to
  read too much into everything, dear boy.", "Good lord, no. I rarely leave my room. I explore with the mind, Mr.
  Marston.", "I'm afraid I don't really have much of a head for heights. More of a head for highs...", "I'm more of a
  planner than a man of action.", "I must say... cocaine can be a cruel mistress." (In his own words); "that academic",
  "old bean", "dear boy", "John! Help me, John!", "Prof. Harold MacDougal Esq." (Names); the terms "reverse integration"
  and "regressive acculturation" (Dutch entry).
- Paraphrased here, left to part C Quotes: "For a wise man, you are a very stupid man, mister.", "Species don't die, they
  evolve...", "The savage heart cannot be conventionally civilized!", "I could be boiling in a pot right now...", the
  watch-them-tear-you-limb-from-limb joke, "Best of luck, dear friend.", Ross's and Fordham's lines on degeneracy, the
  farewell lines, the Undead Nightmare lines.
- Gameplay HERE only: failure conditions, the gun used once, horses and their speed, the hostage rule, the undead
  MacDougal options. Multiplayer model: part C (Other media). Actor: part D.
- Told once elsewhere, pointer here: every mission event (A); the father, Yale, the inheritance, the forced sabbatical
  (A Origins); the 1899 paper, the 1913 thesis and the 1914 expulsion (A); the Ledger No. 59 notice on Nastas (A).

WIKI-ONLY (kept, attributed): both official descriptions; Cattleman Revolver, Ardennais and Cleveland Bay (infobox); the
boots (trivia); the horses' speed and the gun used once (mission trivia); Nashoba's name (the transcript says "Outlaw");
the undead MacDougal options (character and mission trivia, which differ: both given); his father's disapproval (pointer
only).

Excluded: "naive and small-minded", "incompetent in practical matters", "bigotry", "racist" as our own words (wiki
readings; the observable facts and his own lines are given); "develops a sense of respect for Nastas" (reading; the
notice is told in A); Mantegazza, Boas, Tylor, Malinowski and Vine Deloria as influences (wiki "may have been", "could
possibly"); the "mad scientist" resemblance (interpretation); the Protestant/hypocrisy trivia and the reason for the
Damnation category (speculation); "away with the fairies" read as a drug reference (his own words are paraphrased only);
the wiki's "Harold MacDougal MacDougal" (typo); "Wolf" as the meaning of Nashoba's name (wiki etymology, irrelevant here);
Ross learning from MacDougal that John went to Cochinay (edgar_B says so; no line in the four transcripts or in "Great
Men are Not Always Wise/dialogues": not used, flagged to the lead).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "The Red Dead Wiki quotes Rockstar's description of the character: \"A highly-strung anthropology professor, on a forced sabbatical from Yale.\" It also quotes the Game of the Year Edition guide, which presents him as \"very much, an east coast turn-of-the-century man\" and \"an optimist who loves the American way of life and speaks in large metaphors.\" The same guide says he has \"taken his study of opium a little too seriously\" and that his sabbatical may have been forced. In the missions, the drug he names and injects is cocaine.",
        "Le Red Dead Wiki cite la description du personnage par Rockstar : \"A highly-strung anthropology professor, on a forced sabbatical from Yale.\" (un professeur d'anthropologie à fleur de peau, en congé sabbatique forcé de Yale). Il cite aussi le guide de l'édition Game of the Year, qui le présente comme \"very much, an east coast turn-of-the-century man\" (un homme de la côte Est du tournant du siècle, et pas qu'un peu) et comme \"an optimist who loves the American way of life and speaks in large metaphors\" (un optimiste qui aime le mode de vie américain et parle par grandes métaphores). Le même guide affirme qu'il a pris \"his study of opium a little too seriously\" (son étude de l'opium un peu trop au sérieux) et que son congé a peut-être été imposé. Dans les missions, la drogue qu'il nomme et s'injecte est la cocaïne.")},
    {"p": two(
        "He talks fast, repeats himself and stammers when he is afraid. He uses cocaine openly, by syringe, offers some to John at their second meeting and credits the drug with helping his thinking. After a day of shooting he tells John that he will probably never sleep again. He avoids danger: he turns back before the climb at Cochinay and, under fire, begs John not to leave him behind. He sorts peoples into civilized and savage, uses the word savage for Native Americans throughout, and changes his conclusions after each mission (see Biography).",
        "Il parle vite, se répète et bégaie quand il a peur. Il consomme de la cocaïne sans s'en cacher, à la seringue, en propose à John dès leur deuxième rencontre et affirme que la drogue l'aide à réfléchir. Après une journée de fusillades, il confie à John qu'il ne dormira sans doute plus jamais. Il fuit le danger : il fait demi-tour avant l'escalade de Cochinay et, sous les balles, supplie John de ne pas l'abandonner. Il range les peuples en civilisés et en sauvages, emploie le mot sauvage pour parler des Amérindiens d'un bout à l'autre et révise ses conclusions après chaque mission (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "When John tells him, in \"At Home with Dutch\", not to read too much into his past with Dutch: \"It's my job to read too much into everything, dear boy.\" In the dark woods of Tall Trees, when John asks whether he has ever seen trees: \"Good lord, no. I rarely leave my room. I explore with the mind, Mr. Marston.\" At the foot of the cliffs: \"I'm afraid I don't really have much of a head for heights. More of a head for highs...\"",
        "Quand John lui conseille, dans \"At Home with Dutch\", de ne pas trop interpréter son passé avec Dutch : \"It's my job to read too much into everything, dear boy.\" (mon métier, c'est justement de tout surinterpréter, mon cher). Dans les bois sombres de Tall Trees, quand John lui demande s'il a déjà vu des arbres : \"Good lord, no. I rarely leave my room. I explore with the mind, Mr. Marston.\" (grands dieux, non ; je sors rarement de ma chambre, j'explore par l'esprit, monsieur Marston). Au pied des falaises : \"I'm afraid I don't really have much of a head for heights. More of a head for highs...\" (je crains de ne pas avoir la tête faite pour les hauteurs ; plutôt pour les euphories...).")},
    {"p": two(
        "Back in Blackwater, after Nastas has carried John down the mountain: \"I'm more of a planner than a man of action.\" On the ride home from Bearclaw Camp, in \"For Purely Scientific Purposes\": \"I must say... cocaine can be a cruel mistress.\"",
        "De retour à Blackwater, après que Nastas a redescendu John de la montagne : \"I'm more of a planner than a man of action.\" (je suis plus un stratège qu'un homme d'action). Sur la route du retour depuis Bearclaw Camp, dans \"For Purely Scientific Purposes\" : \"I must say... cocaine can be a cruel mistress.\" (je dois dire que la cocaïne peut être une maîtresse cruelle).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "John and Nastas call him Professor, Edgar Ross calls him Professor MacDougal, and Archer Fordham simply MacDougal. Dutch van der Linde never names him: he asks John to send out \"that academic\". The Game of the Year guide, as quoted by the Red Dead Wiki, calls him Dr. MacDougal, and the French-language Red Dead Wiki gives Professeur as his nickname. He signs his notice in Issue No. 59 of the Blackwater Ledger \"Prof. Harold MacDougal Esq.\" He calls John Mr. Marston, \"dear boy\" and once \"old bean\"; held hostage on the roof of the Blackwater Hotel, he calls him by his first name: \"John! Help me, John!\"",
        "John et Nastas l'appellent Professor, Edgar Ross dit Professor MacDougal, et Archer Fordham simplement MacDougal. Dutch van der Linde ne le nomme jamais : il demande à John de faire sortir \"that academic\" (cet universitaire). Le guide de l'édition Game of the Year, cité par le Red Dead Wiki, l'appelle Dr. MacDougal, et le Red Dead Wiki francophone lui donne le surnom de Professeur. Il signe son avis dans le numéro 59 du Blackwater Ledger \"Prof. Harold MacDougal Esq.\" Il appelle John Mr. Marston, \"dear boy\" (mon cher) et une fois \"old bean\" (mon vieux) ; pris en otage sur le toit de l'hôtel de Blackwater, il l'appelle par son prénom : \"John! Help me, John!\" (John ! Aidez-moi, John !).")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He has untidy reddish-blond hair, a thin mustache curled at the ends, stubble and round wire-rimmed spectacles. In Blackwater he wears a white shirt with a loose bow tie. According to the Red Dead Wiki, his boots are close to the US Army model but lace up at the front.",
        "Il a des cheveux blond roux en bataille, une fine moustache aux pointes recourbées, une barbe de quelques jours et des lunettes rondes cerclées de métal. À Blackwater, il porte une chemise blanche et un nœud papillon dénoué. D'après le Red Dead Wiki, ses bottes ressemblent au modèle de l'armée américaine, mais se lacent sur le devant.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Suggested section title for the module: "Research, weapons and horses" / "Recherches, armes et chevaux".
BLOCKS_SKILLS = [
    {"h4": two("Research and writings", "Recherches et publications")},
    {"p": two(
        "He works from his room at the Blackwater Hotel, which Fordham calls his office, with a microscope and shelves of books. His method in 1911 is to compare blood samples from Native Americans and white men of the same height, weight and age (see Biography). Before the meeting at Bearclaw Camp, he wonders aloud whether he could ask the gang members for a skin sample from the soles of their feet; Nastas advises against it. He tells John that he explores with the mind rather than in the field, and the Bureau uses him as its intermediary with the Native Americans of the region (see Relationships). His known writings, all mentioned in newspapers of the two games:",
        "Il travaille depuis sa chambre de l'hôtel de Blackwater, que Fordham appelle son bureau, avec un microscope et des rayonnages de livres. Sa méthode, en 1911, consiste à comparer des échantillons de sang d'Amérindiens et d'hommes blancs de même taille, de même poids et de même âge (voir la biographie). Avant la rencontre de Bearclaw Camp, il se demande à voix haute s'il pourrait solliciter des membres de la bande un échantillon de peau prélevé sous la plante des pieds ; Nastas le lui déconseille. Il explique à John qu'il explore par l'esprit plutôt que sur le terrain, et le Bureau se sert de lui comme intermédiaire auprès des Amérindiens de la région (voir Relations). Ses écrits connus, tous cités dans des journaux des deux jeux :")},
    {"ul": [
        two("The Scourge of Crossbreeding, a book published before 1899, named in the Red Dead Redemption 2 article \"Prominent Yale Scientist Speaks Out\".",
            "The Scourge of Crossbreeding, un livre paru avant 1899, cité dans l'article \"Prominent Yale Scientist Speaks Out\" de Red Dead Redemption 2."),
        two("Savage Minds: The Racial Continuum Between Animal and God, a paper presented to colleagues at a symposium in 1899 (see Biography).",
            "Savage Minds: The Racial Continuum Between Animal and God, une communication présentée à des confrères lors d'un colloque en 1899 (voir la biographie)."),
        two("A thesis on the impossibility of taming the savage mind, published in 1913 and left untitled by the 1914 Blackwater Ledger & Sentinel (see Biography).",
            "Une thèse sur l'impossibilité de dompter l'esprit sauvage, publiée en 1913, dont le Blackwater Ledger & Sentinel de 1914 ne donne pas le titre (voir la biographie)."),
    ]},
    {"h4": two("Weapons", "Armes")},
    {"p": two(
        "The Red Dead Wiki lists a Cattleman Revolver. According to the mission page, \"For Purely Scientific Purposes\" is the only mission in which he uses his gun: he and John open fire on the grizzly bear on the road to Bearclaw Camp. During the fighting at the cabin, on the ride back and in Blackwater, he takes cover and leaves the shooting to John. The Red Dead Wiki notes that he is unarmed when John meets him in Undead Nightmare.",
        "Le Red Dead Wiki lui attribue un Cattleman Revolver. Selon la page de la mission, \"For Purely Scientific Purposes\" est la seule mission où il se sert de son arme : John et lui ouvrent le feu sur le grizzli croisé sur la route de Bearclaw Camp. Pendant la fusillade de la cabane, sur le chemin du retour et à Blackwater, il se met à l'abri et laisse John tirer. Le Red Dead Wiki précise qu'il n'est pas armé quand John le retrouve dans Undead Nightmare.")},
    {"h4": two("Horses", "Chevaux")},
    {"p": two(
        "The Red Dead Wiki lists two mounts, an Ardennais and a Cleveland Bay. He rides with John and Nastas to Tall Trees and to Bearclaw Camp, and with John to the station at Manzanita Post (see the Missions table). Nastas brings the horses round to the front of the building before the second ride. According to the trivia of \"For Purely Scientific Purposes\", his horse and Nastas's are extremely fast in that mission, faster than the American Standardbred and the War Horse.",
        "Le Red Dead Wiki lui attribue deux montures, un Ardennais et un Cleveland Bay. Il chevauche avec John et Nastas jusqu'à Tall Trees et jusqu'à Bearclaw Camp, puis avec John jusqu'à la gare de Manzanita Post (voir le tableau des missions). Avant la deuxième chevauchée, c'est Nastas qui amène les chevaux devant le bâtiment. D'après les anecdotes de \"For Purely Scientific Purposes\", son cheval et celui de Nastas sont extrêmement rapides dans cette mission, plus que l'American Standardbred et le War Horse.")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "His mission strand opens once \"Bear One Another's Burdens\" is completed. \"At Home with Dutch\" and \"For Purely Scientific Purposes\" fail if John assaults, kills or abandons MacDougal or Nastas, or kills their horses. \"The Prodigal Son Returns (To Yale)\" fails if John abandons him, if he is killed while held hostage on the roof, or if John harms him while he is held hostage; the mission pages name the hostage taker Nashoba. In Undead Nightmare, a player who does not kill the undead MacDougal after the opening cutscene of \"Curious Tales from Blackwater\" may meet him again while clearing Blackwater, or outside the cemetery. The character page says he can then be killed or hogtied, or left to wander outside the cemetery; the mission page says he must be killed in town to finish the mission.",
        "Sa série de missions s'ouvre une fois \"Bear One Another's Burdens\" terminée. \"At Home with Dutch\" et \"For Purely Scientific Purposes\" échouent si John agresse, tue ou abandonne MacDougal ou Nastas, ou s'il tue leurs chevaux. \"The Prodigal Son Returns (To Yale)\" échoue si John l'abandonne, s'il est tué pendant qu'on le tient en otage sur le toit, ou si John le blesse pendant la prise d'otage ; les pages de mission donnent au preneur d'otage le nom de Nashoba. Dans Undead Nightmare, un joueur qui n'abat pas le MacDougal mort-vivant après la cinématique d'ouverture de \"Curious Tales from Blackwater\" peut le recroiser en nettoyant Blackwater, ou devant le cimetière. Selon la page du personnage, on peut alors le tuer ou le ligoter, voire le laisser errer devant le cimetière ; selon la page de la mission, il faut l'abattre en ville pour terminer la mission.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [two(
        "Edgar Ross sends John to help the professor with his study (see Biography). At their second meeting, MacDougal tells John that he would make an interesting case for his theory, a white man with a savage spirit, and offers him cocaine, which John declines. He also says that Ross told him about John's history with Dutch, which he sums up as a tale of naivety and betrayal.",
        "Edgar Ross envoie John aider le professeur dans ses travaux (voir la biographie). À leur deuxième rencontre, MacDougal explique à John qu'il ferait un cas intéressant pour sa théorie, un homme blanc à l'esprit sauvage, et lui propose de la cocaïne, que John refuse. Il ajoute que Ross lui a parlé du passé de John avec Dutch, qu'il résume en une histoire de naïveté et de trahison."),
        two(
        "John mocks him openly: he calls him a fool in front of Nastas and jokes about handing him over to Dutch's men (see Quotes). John nonetheless protects him at Bearclaw Camp, on the ride back and in Blackwater, then escorts him to his train. MacDougal thanks him for his life after Bearclaw Camp and parts from him with a hug at Manzanita Post (see Biography).",
        "John se moque ouvertement de lui : il le traite d'imbécile devant Nastas et plaisante sur l'idée de le livrer aux hommes de Dutch (voir Citations). John le protège pourtant à Bearclaw Camp, sur le chemin du retour et à Blackwater, puis l'escorte jusqu'à son train. MacDougal le remercie de lui avoir sauvé la vie après Bearclaw Camp et le quitte en le serrant dans ses bras à Manzanita Post (voir la biographie).")]},
    {"img": "nastas.jpeg", "slug": "nastas", "name": "Nastas", "text": [two(
        "Nastas is the Bureau's informant; Ross has him taken to MacDougal's room after he is found wounded on the Serendipity (see Biography). MacDougal first speaks to him in simple metaphors, and Nastas answers that he grew up on a reservation and went to school. On the rides, they argue about the buffalo, which Nastas says the white man is hunting to extinction, and about the trees and the land. Nastas tells him that, for a wise man, he is a very stupid man (see Quotes).",
        "Nastas est l'informateur du Bureau ; Ross le fait conduire dans la chambre de MacDougal après qu'on l'a retrouvé blessé sur le Serendipity (voir la biographie). MacDougal commence par lui parler en métaphores simplistes, et Nastas lui répond qu'il a grandi dans une réserve et qu'il est allé à l'école. En route, ils se disputent au sujet des bisons, que l'homme blanc chasse jusqu'à l'extinction selon Nastas, puis des arbres et de la terre. Nastas lui lance que, pour un sage, il est bien bête (voir Citations)."),
        two(
        "MacDougal says he is relieved to have Nastas with him on the way to the meeting he arranged at Bearclaw Camp, where Nastas is shot dead (see Biography). He then publishes a notice on his death in the Blackwater Ledger (see Biography). In Undead Nightmare, he says he left his bags with Nastas and is killed by him (see Biography).",
        "MacDougal se dit soulagé d'avoir Nastas à ses côtés en route vers la rencontre qu'il a organisée à Bearclaw Camp, où Nastas est abattu (voir la biographie). Il publie ensuite un avis de décès dans le Blackwater Ledger (voir la biographie). Dans Undead Nightmare, il dit avoir laissé ses bagages à Nastas, qui le tue (voir la biographie).")]},
    {"img": "edgar-ross.jpeg", "slug": "edgar-ross", "name": "Edgar Ross", "text": two(
        "Ross uses the professor because, he says, he cannot communicate with Native Americans himself, and brings the wounded Nastas to him (see Biography). When Fordham mentions why MacDougal left Yale, Ross remarks that this says something about him; he then presents him to John as a good friend of the U.S. government, like John.",
        "Ross a recours au professeur parce que, dit-il, il n'arrive pas à communiquer lui-même avec les Amérindiens, et lui amène Nastas blessé (voir la biographie). Quand Fordham rappelle pourquoi MacDougal a quitté Yale, Ross commente que cela en dit long ; il le présente ensuite à John comme un bon ami du gouvernement américain, tout comme John.")},
    {"img": "archer-fordham.jpeg", "slug": "archer-fordham", "name": "Archer Fordham", "text": two(
        "Fordham introduces MacDougal to John as an anthropologist thrown out of Yale for degeneracy who has been helping the Bureau deal with the Native Americans of the area. He asks him to find out what Nastas knows about Dutch van der Linde and warns him to make sure he does.",
        "Fordham présente MacDougal à John comme un anthropologue renvoyé de Yale pour dépravation, qui aide le Bureau dans ses rapports avec les Amérindiens de la région. Il lui demande de découvrir ce que Nastas sait de Dutch van der Linde, et l'avertit qu'il a intérêt à y parvenir.")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "MacDougal does not want Dutch dead: he is fascinated by a white man living among Native Americans, a civilized mind turned savage, and tries out names for the process, \"reverse integration\" or \"regressive acculturation\". Dutch's men turn the meeting at Bearclaw Camp into an ambush, and Dutch then besieges his hotel to show him what they think of anthropology (see Biography). The Blackwater Ledger reports the hotel attack and names Dutch as the suspected leader of the gang.",
        "MacDougal ne souhaite pas la mort de Dutch : il est fasciné par cet homme blanc qui vit parmi les Amérindiens, un esprit civilisé devenu sauvage, et cherche un nom au phénomène, \"reverse integration\" (intégration inversée) ou \"regressive acculturation\" (acculturation régressive). Les hommes de Dutch transforment la rencontre de Bearclaw Camp en guet-apens, puis Dutch assiège son hôtel pour lui montrer ce qu'ils pensent de l'anthropologie (voir la biographie). Le Blackwater Ledger rend compte de l'attaque de l'hôtel et désigne Dutch comme le chef présumé de la bande.")},
    {"img": None, "slug": None, "name": "Enepay, Kosumi, Hinto and Nashoba", "text": two(
        "Members of Dutch's gang. Enepay, Kosumi and Hinto meet MacDougal at Bearclaw Camp, where Enepay rejects his words of peace and shoots Nastas (see Biography). According to the mission pages, Nashoba is the gunman who holds MacDougal hostage on the roof of the Blackwater Hotel; the transcript calls him only an outlaw.",
        "Membres de la bande de Dutch. Enepay, Kosumi et Hinto reçoivent MacDougal à Bearclaw Camp, où Enepay balaie ses paroles de paix et abat Nastas (voir la biographie). Selon les pages de mission, Nashoba est le tireur qui retient MacDougal en otage sur le toit de l'hôtel de Blackwater ; la transcription ne parle que d'un hors-la-loi.")},
    {"img": None, "slug": None, "name": "Lionel Fortisque", "text": two(
        "A fellow academic at Yale. MacDougal tells John that he argued with Fortisque about the nature of the savage soul and that it caused a minor scandal. In 1914, the Blackwater Ledger & Sentinel reports that MacDougal beat him with a croquet mallet at a garden party (see Biography).",
        "Un collègue universitaire de Yale. MacDougal raconte à John qu'il s'est disputé avec Fortisque sur la nature de l'âme sauvage, et que l'affaire a fait un petit scandale. En 1914, le Blackwater Ledger & Sentinel rapporte que MacDougal l'a frappé avec un maillet de croquet lors d'une garden-party (voir la biographie).")},
    {"img": None, "slug": None, "name": "Benjamin Fortescue", "text": two(
        "The colleague who, according to the Red Dead Redemption 2 article \"Prominent Yale Scientist Speaks Out\", criticized MacDougal's 1899 paper for lacking empirical evidence (see Biography). The newspapers of the two games spell the names Fortescue and Fortisque and give different first names; the games never say whether they are the same man.",
        "Le collègue qui, selon l'article \"Prominent Yale Scientist Speaks Out\" de Red Dead Redemption 2, reproche à la communication de MacDougal de 1899 de manquer de preuves empiriques (voir la biographie). Les journaux des deux jeux écrivent Fortescue et Fortisque, avec des prénoms différents ; les jeux ne disent jamais s'il s'agit du même homme.")},
    {"img": None, "slug": None, "name": "The newlyweds", "text": two(
        "A couple in the room next to MacDougal's at the Blackwater Hotel. When he and John burst in to reach the roof, MacDougal greets them politely and the husband protests (see Biography).",
        "Un couple installé dans la chambre voisine de celle de MacDougal, à l'hôtel de Blackwater. Quand John et lui font irruption pour gagner le toit, MacDougal les salue poliment et le mari proteste (voir la biographie).")},
    {"img": None, "slug": None, "name": "His father", "text": two(
        "The game never shows him. According to the Red Dead Wiki, he did not consider anthropology a real profession (see Origins).",
        "Le jeu ne le montre jamais. D'après le Red Dead Wiki, il ne tenait pas l'anthropologie pour un vrai métier (voir Origines).")},
]
