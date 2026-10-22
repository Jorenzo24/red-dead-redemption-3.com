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
- Gameplay HERE only: failure conditions, the gun used once, horses and their speed. The undead MacDougal options,
  Nashoba and the strand unlock are told once elsewhere (A, C) after the fix pass of 22 Oct 2026. Multiplayer model: part C (Other media). Actor: part D.
- Told once elsewhere, pointer here: every mission event (A); the father, Yale, the inheritance, the forced sabbatical
  (A Origins); the 1899 paper, the 1913 thesis and the 1914 expulsion (A); the Ledger No. 59 notice on Nastas (A).

WIKI-ONLY (kept, attributed): both official descriptions (incl. the GOTY guide's "writing a book" line, added 22 Oct 2026); Cattleman Revolver, Ardennais and Cleveland Bay (infobox); the
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
        "The Red Dead Wiki quotes Rockstar's description of the character: \"A highly-strung anthropology professor, on a forced sabbatical from Yale.\" It also quotes the Game of the Year Edition guide, which presents him as \"very much, an east coast turn-of-the-century man\" and \"an optimist who loves the American way of life and speaks in large metaphors.\" According to the guide, he is on sabbatical from Yale, \"writing a book about Native Americans and the last days of the old west\". The same guide says he has \"taken his study of opium a little too seriously\" and that his sabbatical may have been forced. In the missions, the drug he names is cocaine (see Origins).",
        "Le Red Dead Wiki cite la description du personnage par Rockstar : \"A highly-strung anthropology professor, on a forced sabbatical from Yale.\" (un professeur d'anthropologie à fleur de peau, en congé sabbatique forcé de Yale). Il cite aussi le guide de l'édition Game of the Year, qui le présente comme \"very much, an east coast turn-of-the-century man\" (un homme de la côte Est du tournant du siècle, et pas qu'un peu) et comme \"an optimist who loves the American way of life and speaks in large metaphors\" (un optimiste qui aime le mode de vie américain et parle par grandes métaphores). D'après ce guide, il profite de son congé sabbatique pour écrire \"a book about Native Americans and the last days of the old west\" (un livre sur les Amérindiens et les derniers jours du vieil Ouest). Le même guide affirme qu'il a pris \"his study of opium a little too seriously\" (son étude de l'opium un peu trop au sérieux) et que son congé a peut-être été imposé. Dans les missions, c'est pourtant la cocaïne qu'il nomme (voir Origines).")},
    {"p": two(
        "He repeats himself (\"Good day, good day\", \"but, but, but\") and stammers when he is nervous or excited. He avoids danger whenever he can (see Biography). He sorts peoples into civilized and savage. He uses the word savage for Native Americans throughout. His conclusions about Native Americans shift from one mission to the next (see Biography).",
        "Il se répète (\"Good day, good day\", \"but, but, but\") et bégaie dès qu'il est nerveux ou surexcité. Il se tient à l'écart du danger chaque fois qu'il le peut (voir la biographie). Il classe les peuples en civilisés et en sauvages. Il désigne les Amérindiens par le mot sauvage du début à la fin. Ses conclusions à leur sujet varient d'une mission à l'autre (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "When John tells him, in \"At Home with Dutch\", not to read too much into his past with Dutch: \"It's my job to read too much into everything, dear boy.\" In the dark woods of Tall Trees, when John asks whether he has ever seen trees: \"Good lord, no. I rarely leave my room. I explore with the mind, Mr. Marston.\" At the foot of the cliffs: \"I'm afraid I don't really have much of a head for heights. More of a head for highs...\"",
        "Quand John lui conseille, dans \"At Home with Dutch\", de ne pas trop interpréter son passé avec Dutch : \"It's my job to read too much into everything, dear boy.\" (mon métier, c'est justement de tout surinterpréter, mon cher). Dans les bois sombres de Tall Trees, quand John lui demande s'il a déjà vu des arbres : \"Good lord, no. I rarely leave my room. I explore with the mind, Mr. Marston.\" (grands dieux, non ; je sors rarement de ma chambre, j'explore par l'esprit, monsieur Marston). Au pied des falaises : \"I'm afraid I don't really have much of a head for heights. More of a head for highs...\" (je crains de ne pas avoir la tête faite pour les hauteurs ; plutôt pour les euphories...).")},
    {"p": two(
        "Back in Blackwater, after Nastas has carried John down the mountain: \"I'm more of a planner than a man of action.\" On the ride home from Bearclaw Camp, in \"For Purely Scientific Purposes\": \"I must say... cocaine can be a cruel mistress.\"",
        "De retour à Blackwater, après que Nastas a redescendu John de la montagne : \"I'm more of a planner than a man of action.\" (je suis plus un stratège qu'un homme d'action). Sur la route du retour depuis Bearclaw Camp, dans \"For Purely Scientific Purposes\" : \"I must say... cocaine can be a cruel mistress.\" (je dois dire que la cocaïne peut être une maîtresse cruelle).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "John and Nastas call him Professor, Edgar Ross calls him Professor MacDougal, and Archer Fordham simply MacDougal. Dutch van der Linde never uses his name: he calls him \"your friend there the professor\" and asks John to send out \"that academic\". The Game of the Year guide, as quoted by the Red Dead Wiki, calls him Dr. MacDougal, and the French-language Red Dead Wiki gives Professeur as his nickname. He signs his notice in Issue No. 59 of the Blackwater Ledger \"Prof. Harold MacDougal Esq.\" He calls John Mr. Marston, \"dear boy\" and once \"old bean\"; held hostage on the roof of the Blackwater Hotel, he calls him by his first name: \"John! Help me, John!\"",
        "John et Nastas l'appellent Professor, Edgar Ross dit Professor MacDougal, et Archer Fordham simplement MacDougal. Dutch van der Linde ne prononce jamais son nom : il parle de \"your friend there the professor\" (ton ami le professeur) et demande à John de faire sortir \"that academic\" (cet universitaire). Le guide de l'édition Game of the Year, cité par le Red Dead Wiki, l'appelle Dr. MacDougal, et le Red Dead Wiki francophone lui donne le surnom de Professeur. Il signe son avis dans le numéro 59 du Blackwater Ledger \"Prof. Harold MacDougal Esq.\" Il appelle John Mr. Marston, \"dear boy\" (mon cher) et une fois \"old bean\" (mon vieux) ; pris en otage sur le toit de l'hôtel de Blackwater, il l'appelle par son prénom : \"John! Help me, John!\" (John ! Aidez-moi, John !).")},
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
        "He works from his room at the Blackwater Hotel, which Fordham calls his office, with a microscope and shelves of books. His method in 1911 is to compare blood samples from Native Americans and white men of the same height, weight and age (see Biography). The Bureau uses him as its intermediary with the Native Americans of the region (see Relationships). His known writings, all mentioned in newspapers of the two games:",
        "Il travaille depuis sa chambre de l'hôtel de Blackwater, que Fordham appelle son bureau, avec un microscope et des rayonnages de livres. Sa méthode, en 1911, consiste à comparer des échantillons de sang d'Amérindiens et d'hommes blancs de même taille, de même poids et de même âge (voir la biographie). Le Bureau se sert de lui comme intermédiaire auprès des Amérindiens de la région (voir Relations). Ses écrits connus, tous cités dans des journaux des deux jeux :")},
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
        "The Red Dead Wiki lists a Cattleman Revolver. According to the mission page, \"For Purely Scientific Purposes\" is the only mission in which he uses his gun, against the grizzly bear (see Biography). He does not fire in any other mission.",
        "Le Red Dead Wiki lui attribue un Cattleman Revolver. Selon la page de la mission, \"For Purely Scientific Purposes\" est la seule mission où il se sert de son arme, contre le grizzli (voir la biographie). Il ne tire dans aucune autre mission.")},
    {"h4": two("Horses", "Chevaux")},
    {"p": two(
        "The Red Dead Wiki lists two mounts, an Ardennais and a Cleveland Bay. He rides with John and Nastas to Tall Trees and to Bearclaw Camp, and with John to the station at Manzanita Post (see the Missions table). Nastas brings the horses round to the front of the building before the second ride. The mission page of \"For Purely Scientific Purposes\" notes, in its trivia, a speed quirk: in that mission the two men's mounts outrun even the American Standardbred and the War Horse.",
        "Le Red Dead Wiki lui attribue deux montures, un Ardennais et un Cleveland Bay. Il chevauche avec John et Nastas jusqu'à Tall Trees et jusqu'à Bearclaw Camp, puis avec John jusqu'à la gare de Manzanita Post (voir le tableau des missions). Avant la deuxième chevauchée, c'est Nastas qui amène les chevaux devant le bâtiment. La page de la mission \"For Purely Scientific Purposes\" relève une bizarrerie : dans cette mission, les montures des deux hommes vont plus vite que l'American Standardbred et même que le War Horse.")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "\"At Home with Dutch\" and \"For Purely Scientific Purposes\" fail if John assaults, kills or abandons MacDougal or Nastas, or kills their horses. \"The Prodigal Son Returns (To Yale)\" fails if John abandons him, if he is killed while held hostage on the roof, or if John harms him while he is held hostage.",
        "\"At Home with Dutch\" et \"For Purely Scientific Purposes\" échouent si John agresse, tue ou abandonne MacDougal ou Nastas, ou s'il tue leurs chevaux. \"The Prodigal Son Returns (To Yale)\" échoue si John l'abandonne, s'il est tué pendant qu'on le tient en otage sur le toit, ou si John le blesse pendant la prise d'otage.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [two(
        "Edgar Ross sends John to help the professor with his study (see Biography). MacDougal sums up John's history with Dutch as a tale of naivety and betrayal.",
        "Edgar Ross envoie John aider le professeur dans ses travaux (voir la biographie). MacDougal résume le passé de John avec Dutch en une histoire de naïveté et de trahison."),
        two(
        "John mocks him openly: he calls him a fool in front of Nastas and jokes about handing him over to Dutch's men (see Quotes). John nonetheless protects him at Bearclaw Camp, on the ride back and in Blackwater, then escorts him to his train (see Biography).",
        "John se moque ouvertement de lui : il le traite d'imbécile devant Nastas et plaisante sur l'idée de le livrer aux hommes de Dutch (voir Citations). John le protège pourtant à Bearclaw Camp, sur le chemin du retour et à Blackwater, puis l'escorte jusqu'à son train (voir la biographie).")]},
    {"img": "nastas.jpeg", "slug": "nastas", "name": "Nastas", "text": [two(
        "Nastas is the Bureau's informant, whom Ross leaves with MacDougal after he is found wounded on the Serendipity (see Biography). Nastas knows the way to Dutch's hideout and arranges the meeting at Bearclaw Camp. The two men argue on the rides (see Biography and Quotes).",
        "Nastas est l'informateur du Bureau, que Ross confie à MacDougal après l'avoir retrouvé blessé sur le Serendipity (voir la biographie). C'est lui qui connaît le chemin du repaire de Dutch et qui organise la rencontre de Bearclaw Camp. Les deux hommes se querellent pendant les chevauchées (voir la biographie et les citations)."),
        two(
        "MacDougal says he is relieved to have Nastas with him on the way to the meeting Nastas arranged at Bearclaw Camp, where Nastas is shot dead. He then publishes a notice on his death in the Blackwater Ledger (see Biography).",
        "MacDougal se dit soulagé de l'avoir à ses côtés en route vers ce rendez-vous de Bearclaw Camp, où Nastas est abattu. Il fait ensuite paraître un avis de décès dans le Blackwater Ledger (voir la biographie).")]},
    {"img": "edgar-ross.jpeg", "slug": "edgar-ross", "name": "Edgar Ross", "text": two(
        "Ross leaves the wounded Nastas with the professor and introduces him to John (see Biography). He has also told MacDougal about John's past with Dutch (see Biography).",
        "Ross confie Nastas blessé au professeur et le présente à John (voir la biographie). Il a aussi parlé à MacDougal du passé de John avec Dutch (voir la biographie).")},
    {"img": "archer-fordham.jpeg", "slug": "archer-fordham", "name": "Archer Fordham", "text": two(
        "Fordham describes MacDougal as an anthropologist who helps the Bureau with the Native Americans of the area, and gives his own account of why he left Yale (see Quotes). He is the one who tasks him with questioning Nastas (see Biography).",
        "Fordham présente MacDougal comme un anthropologue qui aide le Bureau dans ses rapports avec les Amérindiens de la région, et donne sa propre version de son départ de Yale (voir Citations). C'est lui qui le charge d'interroger Nastas (voir la biographie).")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "MacDougal does not want Dutch dead and studies him as a case (see Biography and Quotes). Dutch's men ambush him at Bearclaw Camp, and Dutch then besieges his hotel (see Biography).",
        "MacDougal ne souhaite pas la mort de Dutch, qu'il voudrait étudier (voir la biographie et les citations). Les hommes de Dutch lui tendent un guet-apens à Bearclaw Camp, puis Dutch assiège son hôtel (voir la biographie).")},
    {"img": None, "slug": None, "name": "Enepay, Kosumi, Hinto and Nashoba", "text": two(
        "Members of Dutch's gang. Enepay, Kosumi and Hinto meet MacDougal at Bearclaw Camp, where Enepay rejects his words of peace and shoots Nastas (see Biography). According to the mission pages, Nashoba is the gunman who holds MacDougal hostage on the roof of the Blackwater Hotel; the transcript calls him only an outlaw.",
        "Membres de la bande de Dutch. Enepay, Kosumi et Hinto reçoivent MacDougal à Bearclaw Camp, où Enepay balaie ses paroles de paix et abat Nastas (voir la biographie). Selon les pages de mission, Nashoba est le tireur qui retient MacDougal en otage sur le toit de l'hôtel de Blackwater ; la transcription ne parle que d'un hors-la-loi.")},
    {"img": None, "slug": None, "name": "Lionel Fortisque", "text": two(
        "A fellow academic at Yale, the subject of a minor scandal with MacDougal and, in 1914, of the croquet mallet attack (see Biography).",
        "Un collègue de Yale, mêlé à un petit scandale avec MacDougal, puis frappé au maillet de croquet en 1914 (voir la biographie).")},
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
