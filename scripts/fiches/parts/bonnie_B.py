"""Bonnie MacFarlane, part B: Personality (official description, In her own words, Names, Appearance),
Skills, weapons and horses, Relationships (20 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN sections Personality, Appearance, the infobox (weapon, mount, family,
affiliations), the trivia items about weapons, belts, necklace and first-name use, plus the related
pages Drew MacFarlane, Amos, Patrick MacFarlane, MacFarlane Brothers, Nathanial Johnston and the mission
pages listed in bonnie/missions.txt. Narrative events are told in part A; entries below point to them.

SOURCE REGISTER (fetched 20 Oct 2026, wiki cache scripts/v3/work/_m/, notes in bonnie/fc/):
- Official guide: Red Dead Redemption: Game of the Year Edition Guide (BradyGames), description quoted
  by the Red Dead Wiki EN quote box ("Bonnie is the 27-year-old daughter of a prominent rancher...").
  Rockstar's 6 Sep 2018 descriptions (sources/thr_descriptions.txt) cover the RDR2 gang only: none for Bonnie.
- Transcripts (wiki "/dialogues" pages): "Exodus in America", "New Friends, Old Problems", "Obstacles in
  Our Path", "This is Armadillo, USA", "Women and Cattle", "Wild Horses, Tamed Passions", "A Tempest Looms",
  "The Burning", "Hanging Bonnie MacFarlane", "The Outlaw's Return", "Old Friends, New Problems".
  Every quoted line below was checked against them.
- Mission pages: "New Friends, Old Problems" (rewards Repeater Carbine, Cleveland Bay / War Horse,
  Nightwatch job, safehouse; trivia: Bonnie shoots the animals herself), "Obstacles in Our Path"
  (trivia: hard to beat, no bonus, two speech tracks), "Wild Horses, Tamed Passions" (Kentucky
  Saddler), "Paternal Pride" (trivia on John's use of her first name, contradicted by the transcripts: he also says "Bonnie, are you okay?"
  in "Hanging Bonnie MacFarlane"). Obstacles in Our Path page: 20 Fame win or lose; New Friends page: Dead Eye level 1.
- Doctor's name: "NATHANIAL JOHNSTON, M.D." on the in-game sign in Armadillo (wiki file Rdr nathanial johnston sign.jpg).
- Fix pass (20 Oct 2026): relationship entries cut to pointers where the Biography tells the event; Amos scenes split
  (Tempest Looms: John ends the argument; Wild Horses: countrified); "pretty" left to part A; "an unusual start to a
  friendship" and "a woman in a man's world" quoted only in the John entry (A no longer paraphrases them).
- Red Dead Online pages "Recovery", "Delivery", "Caravan Escort", "On The Hunt" (Bonnie's rows).
- Wiki pages "Drew MacFarlane" (voice Chuck Kelley; "has taught his daughter Bonnie how to break horses"),
  "Amos" (head ranch hand, voice Dan Campbell, poker), "Patrick MacFarlane", "MacFarlane Brothers"
  (names, Coot's Chapel graves), "Nathanial Johnston", "Letter to Bonnie MacFarlane".
- Fact-checked fiches kept consistent: john_B/john_D (Amos, the 15 dollars, Kentucky Saddler, "Miss
  MacFarlane"), abigail_B (her Bonnie entry: quotes NOT repeated here), jack_B, bill_B, uncle_B.

OWNERSHIP NOTES FOR THE LEAD (parts A and C must not repeat):
- Lines quoted HERE: "Oh, there's always hope, Mr. Marston...", "There's certain things in this country a
  woman could do much better, if you ask me.", "There's nothing more depressing than a man who's found a
  way to think the bad into good.", "I knew better than to try to change a man." (In her own words);
  "Miss Bonnie MacFarlane", "Ugh, call me Bonnie, you fool. Call me Bonnie.", "Call me Bonnie, you dolt!",
  "I've said too much, Bonnie." (Names); "pretty normal" (Appearance); "that nice Mr. Williamson" (Bill entry);
  "countrified" (Amos entry); "an unusual start to a friendship" (John entry); "a woman in a man's
  world" (John entry). "Frailer than he looks" is paraphrased in A Origins only. Part C Quotes must pick other lines (the
  wiki's "Call me Bonnie, you dolt!" in particular is HERE).
- Weapons, the artwork Winchester Repeater, the two belts, the necklace, the first-name trivia and the
  Red Dead Online mission types live HERE (trivia in C must drop them). Destinations of the RDO missions
  are left to the Missions table (C).
- Age (27 / 29 / 1884) lives in the facts grid (D) and, for the inconsistency, in C Trivia.

WIKI-ONLY (kept, attributed): Drew teaching her to break horses; the infobox weapons and horses; the
two belts and the turquoise necklace; the brothers' names and graves; Patrick's name (residents' talk);
Amos's job title and poker; voices of Drew (Chuck Kelley) and Amos (Dan Campbell); "no extra bonus"
for winning the race; John's use of her first name in "Paternal Pride".

Excluded: the wiki's "compassionate and no-nonsense", "selflessness" (interpretation); "suggested by
Abigail that Bonnie had developed feelings for John" and "the way in which she stared" (inference;
only Abigail's remark is kept, in part A / abigail_B); the FR wiki's claim that she is married by 1914
(no source, contradicted by the EN wiki); the FR wiki's reading of Deek's remarks and of her torn shirt
(insinuation, not shown); the "fraternal twins" guess about Ethan (the wiki says "implies"); the
Drew page's "highly suspicious of outsiders" (interpretation); the Walking Dead comparisons of
"Paternal Pride" (not about Bonnie); "John willingly opens up only to her" (wiki trivia, interpretive;
the conversation itself is told in part A).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "The official Game of the Year Edition guide to Red Dead Redemption introduces her this way: \"Bonnie is the 27-year-old daughter of a prominent rancher. She is unmarried, educated, and a kind-hearted proto feminist. At one point, she takes a romantic interest in Marston, and this evolves into a solid friendship. Some day in the future, she expects to inherit and run the MacFarlane ranch.\" Rockstar's character descriptions of September 2018 concern the gang of Red Dead Redemption 2 and do not include her.",
        "Le guide officiel de l'édition Game of the Year de Red Dead Redemption la présente ainsi : \"Bonnie is the 27-year-old daughter of a prominent rancher. She is unmarried, educated, and a kind-hearted proto feminist. At one point, she takes a romantic interest in Marston, and this evolves into a solid friendship. Some day in the future, she expects to inherit and run the MacFarlane ranch.\" (fille d'un rancher en vue, 27 ans, célibataire, instruite, protoféministe au grand cœur ; elle éprouve un temps de l'attirance pour Marston, qui se mue en solide amitié ; elle compte hériter un jour du ranch et le diriger). Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang de Red Dead Redemption 2 et ne la concernent pas.")},
    {"p": two(
        "In the game she pays for a stranger's treatment and puts him up in exchange for work (see Biography). She speaks bluntly to John: she calls his fight at Fort Mercer stupid, says he talks in riddles and mocks his talk of an outlaw code. She dismisses his picture of New Austin as the last outlaw country as something out of a cheap novel. She worries aloud about the future of the ranch and is wary of the strangers the railroad brings in.",
        "Dans le jeu, elle paie les soins d'un inconnu et l'héberge contre du travail (voir la biographie). Elle parle franchement à John : elle juge stupide son coup d'éclat à Fort Mercer, lui reproche de parler par énigmes et se moque de son code d'honneur de hors-la-loi. Quand il décrit le New Austin comme la dernière terre des hors-la-loi, elle lui répond que ça sort d'un mauvais roman. Elle s'inquiète ouvertement pour l'avenir du ranch et se méfie des inconnus qu'amène le chemin de fer.")},
    {"h4": two("In her own words", "Dans ses propres mots")},
    {"p": two(
        "On the road to Armadillo, in \"This is Armadillo, USA\": \"Oh, there's always hope, Mr. Marston. You can't be a rancher in this kind of country if you don't believe that.\" Riding out with her father in \"Wild Horses, Tamed Passions\": \"There's certain things in this country a woman could do much better, if you ask me.\" When John says that everyone has a code, in \"The Burning\": \"There's nothing more depressing than a man who's found a way to think the bad into good.\" To Abigail, who thanks her for teaching John manners, in \"Old Friends, New Problems\": \"I knew better than to try to change a man.\"",
        "Sur la route d'Armadillo, dans \"This is Armadillo, USA\" : \"Oh, there's always hope, Mr. Marston. You can't be a rancher in this kind of country if you don't believe that.\" (il y a toujours de l'espoir, monsieur Marston ; impossible d'être rancher dans un pays pareil sans y croire). En chevauchant avec son père dans \"Wild Horses, Tamed Passions\" : \"There's certain things in this country a woman could do much better, if you ask me.\" (si vous voulez mon avis, il y a des choses dans ce pays qu'une femme ferait bien mieux). Quand John affirme que chacun a un code, dans \"The Burning\" : \"There's nothing more depressing than a man who's found a way to think the bad into good.\" (rien de plus déprimant qu'un homme qui a trouvé le moyen de faire passer le mal pour le bien). À Abigail, qui la remercie d'avoir appris les bonnes manières à John, dans \"Old Friends, New Problems\" : \"I knew better than to try to change a man.\" (j'ai eu la sagesse de ne pas essayer de changer un homme).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "She introduces herself to John as \"Miss Bonnie MacFarlane\", and he calls her \"Miss MacFarlane\" almost throughout the game. In \"Women and Cattle\" she tells him: \"Ugh, call me Bonnie, you fool. Call me Bonnie.\" In the same scene he uses her first name (\"I've said too much, Bonnie\"), and he uses it again when he cuts her down in \"Hanging Bonnie MacFarlane\" (\"Bonnie, are you okay?\"). In Undead Nightmare, according to the mission page, he also says it in \"Paternal Pride\". When they part in \"The Outlaw's Return\", she repeats the request: \"Call me Bonnie, you dolt!\" She calls him \"Mr. Marston\"; after the barn fire of \"The Burning\" she thanks him as John, then goes back to \"Mr. Marston\" within the same scene. She calls her father \"Pa\" or \"Daddy\".",
        "Elle se présente à John comme \"Miss Bonnie MacFarlane\", et il l'appelle \"Miss MacFarlane\" pendant presque tout le jeu. Dans \"Women and Cattle\", elle lui lance : \"Ugh, call me Bonnie, you fool. Call me Bonnie.\" (appelez-moi Bonnie, idiot, appelez-moi Bonnie). Dans la même scène, il emploie son prénom (\"I've said too much, Bonnie\", j'en ai trop dit, Bonnie), et il le refait en la décrochant dans \"Hanging Bonnie MacFarlane\" (\"Bonnie, are you okay?\", Bonnie, ça va ?). Dans Undead Nightmare, d'après la page de la mission, il le prononce aussi dans \"Paternal Pride\". Quand ils se quittent dans \"The Outlaw's Return\", elle revient à la charge : \"Call me Bonnie, you dolt!\" (appelez-moi Bonnie, espèce d'andouille !). Elle-même lui dit \"Mr. Marston\" ; après l'incendie de la grange, dans \"The Burning\", elle le remercie en l'appelant John, avant de revenir à \"Mr. Marston\" dans la même scène. Son père, elle l'appelle \"Pa\" ou \"Daddy\".")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "According to the Red Dead Wiki, her eyes are blue-green and her dirty blonde hair is tied up in a bun, a looser one in 1911 than in 1898. In both periods she wears a turquoise necklace with a metal charm and, like most male characters, two belts: an ordinary belt and a gunbelt. On the way to the ranch, John describes her to Abigail as \"pretty normal\".",
        "D'après le Red Dead Wiki, elle a les yeux bleu-vert et les cheveux blond foncé, noués en chignon, plus lâche en 1911 qu'en 1898. Aux deux époques, elle porte un collier turquoise à breloque de métal et, comme la plupart des personnages masculins, deux ceintures : une ordinaire et un ceinturon. En route vers le ranch, John la décrit à Abigail comme \"pretty normal\" (plutôt ordinaire).")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Skills, weapons and horses", "Compétences, armes et chevaux")},
    {"h4": two("On the ranch", "Au ranch")},
    {"p": two(
        "Bonnie gives John the first mission strand of the game (see Missions), and each one shows a part of her work. She patrols the property at night with a rifle, and the mission page of \"New Friends, Old Problems\" notes that the player does not need to shoot the rabbits and coyotes because she kills them herself. She races John on horseback in \"Obstacles in Our Path\": according to the Red Dead Wiki, she is hard to beat with John's first horse, the conversation changes with the state of the race, and winning brings no bonus: the reward is 20 Fame either way. She drives the ranch wagon and hands John the reins before they set off for Armadillo. She herds cattle, ropes wild horses and brings the herd home with John through a thunderstorm in \"A Tempest Looms\". According to the wiki's page on Drew MacFarlane, her father taught her to break horses and run the ranch.",
        "Bonnie confie à John la première série de missions du jeu (voir les Missions), et chacune montre une part de son travail. Elle patrouille la nuit sur la propriété, fusil en main, et la page de la mission \"New Friends, Old Problems\" précise que le joueur n'a pas besoin de tirer sur les lapins et les coyotes, puisqu'elle les abat elle-même. Elle défie John à la course dans \"Obstacles in Our Path\" : d'après le Red Dead Wiki, elle est difficile à battre avec le premier cheval de John, la conversation change selon l'état de la course, et la victoire ne rapporte aucun bonus : la récompense est de 20 points de Fame dans tous les cas. Elle conduit le chariot du ranch et en confie les rênes à John avant de partir pour Armadillo. Elle mène le bétail, attrape au lasso des chevaux sauvages et ramène le troupeau avec John en plein orage dans \"A Tempest Looms\". D'après la page du wiki consacrée à Drew MacFarlane, c'est son père qui lui a appris à dresser les chevaux et à tenir le ranch.")},
    {"p": two(
        "She also equips John. \"New Friends, Old Problems\" gives him a horse she picked for him (a Cleveland Bay in the original version, a War Horse in the Game of the Year Edition and later versions) and the Repeater Carbine he uses on the patrol, and it unlocks the first level of Dead Eye. The same mission opens the safehouse at MacFarlane's Ranch and the ranch's Nightwatch job. In \"Wild Horses, Tamed Passions\" she hands him a lasso, and she lets him keep the stallion that broke away from the herd, a Kentucky Saddler, as a thank-you from the family.",
        "Elle équipe aussi John. \"New Friends, Old Problems\" lui vaut un cheval qu'elle a choisi pour lui (un Cleveland Bay dans la version d'origine, un War Horse dans l'édition Game of the Year et les versions suivantes) et la Repeater Carbine dont il se sert pendant la ronde, et débloque le premier niveau du Dead Eye. La même mission ouvre la planque du MacFarlane's Ranch et le travail de veilleur de nuit (Nightwatch) du ranch. Dans \"Wild Horses, Tamed Passions\", elle lui remet un lasso, puis lui laisse en remerciement, au nom de la famille, l'étalon qui s'était échappé du troupeau, un Kentucky Saddler.")},
    {"h4": two("In Red Dead Online, 1898", "Dans Red Dead Online, en 1898")},
    {"p": two(
        "In Red Dead Online she is a Stranger at MacFarlane's Ranch, in New Austin. After her introduction (see Biography), she offers four kinds of free roam missions: Recovery (getting back a stolen wagon), Delivery, Caravan Escort and On The Hunt, in which the player tracks a grizzly bear. According to the Red Dead Wiki, accepting her missions raises the player's honor. Their start and end points are listed in the Missions table.",
        "Dans Red Dead Online, elle fait partie des inconnus (Strangers) du MacFarlane's Ranch, dans le New Austin. Après sa présentation (voir la biographie), elle propose quatre types de missions en mode libre : Recovery (récupérer un chariot volé), Delivery (livraison), Caravan Escort (escorte de convoi) et On The Hunt, où le joueur traque un grizzly. D'après le Red Dead Wiki, accepter ses missions fait monter l'honneur du joueur. Leurs points de départ et d'arrivée figurent dans le tableau des Missions.")},
    {"h4": two("Weapons and horses", "Armes et chevaux")},
    {"p": two(
        "The Red Dead Wiki lists a Cattleman Revolver, a Repeater Carbine and a Double-barreled Shotgun as her weapons. Artwork shows her holding a Winchester Repeater, a weapon she never carries in the game, according to the same wiki. Her horses, as the wiki lists them, are a Painted Quarter Horse, a Standardbred Pinto and a Painted Standardbred.",
        "Le Red Dead Wiki lui attribue un Cattleman Revolver, une Repeater Carbine et un Double-barreled Shotgun. Des illustrations la montrent avec une Winchester Repeater, une arme qu'elle ne porte jamais dans le jeu, selon le même wiki. Ses chevaux, d'après la liste du wiki : un Painted Quarter Horse, un Standardbred Pinto et un Painted Standardbred.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [
        two("Bonnie and her ranch hand Amos find John by the road after Fort Mercer; she takes him to the doctor and lodges him at the ranch in exchange for work (see Biography). She teases him about how quick he is to shoot, about his riddles and about his smell, and he answers with jokes of his own. In \"This is Armadillo, USA\" she calls their meeting \"an unusual start to a friendship\"; John says he did not realize they were friends, and she brushes the remark aside. Her view of him as a possible rancher is quoted under Quotes.",
            "Bonnie et son employé Amos trouvent John au bord de la route après Fort Mercer ; elle l'emmène chez le médecin puis l'héberge au ranch contre du travail (voir la biographie). Elle le taquine sur sa gâchette facile, ses énigmes ou son odeur, et il lui renvoie la balle. Dans \"This is Armadillo, USA\", elle qualifie leur rencontre de \"an unusual start to a friendship\" (un drôle de début pour une amitié) ; John répond qu'il ne savait pas qu'ils étaient amis, et elle balaie la remarque. Ce qu'elle pense de son avenir d'éleveur est cité dans la rubrique Citations."),
        two("In \"Women and Cattle\" John tells her about his family and his years in the gang (see Biography). In \"Wild Horses, Tamed Passions\" he says his wife is like her, \"a woman in a man's world\", a phrase he uses again when Abigail asks him what Bonnie is like. After the barn fire, she says her family owes him a debt, and he asks only that the family sell him cattle once he is home, which it does in 1911 (see Biography). Her last canon scene with him is the corn delivery of \"Old Friends, New Problems\". The official guide's view of their bond is quoted under Personality.",
            "Dans \"Women and Cattle\", John lui raconte sa famille et ses années dans le gang (voir la biographie). Dans \"Wild Horses, Tamed Passions\", il lui dit que sa femme lui ressemble, \"a woman in a man's world\" (une femme dans un monde d'hommes), formule qu'il reprend quand Abigail lui demande comment est Bonnie. Après l'incendie de la grange, elle lui dit que sa famille a une dette envers lui ; il demande seulement que la famille lui vende du bétail une fois rentré chez lui, ce qui sera fait en 1911 (voir la biographie). Leur dernière scène dans le récit canonique est la livraison de maïs de \"Old Friends, New Problems\". Le regard du guide officiel sur leur relation est cité dans la partie Personnalité."),
    ]},
    {"img": None, "slug": None, "name": "Drew MacFarlane", "text": two(
        "Her father owns MacFarlane's Ranch. His account of the family's thirty years on the land, and Bonnie's worries about his debts and his health, are told under Origins. When he fails to come back from a ride in \"The Burning\", she says he is all she has. The Red Dead Wiki credits Chuck Kelley as his voice. In Undead Nightmare, which is not canon, Bonnie loses him in the barn (see Biography).",
        "Son père possède le MacFarlane's Ranch. Ce qu'il raconte des trente ans de la famille sur ces terres, comme les inquiétudes de Bonnie pour ses dettes et sa santé, figure dans la partie Origines. Quand il ne rentre pas d'une tournée à cheval, dans \"The Burning\", elle dit qu'il est tout ce qui lui reste. Le Red Dead Wiki attribue sa voix à Chuck Kelley. Dans Undead Nightmare, hors canon, Bonnie le perd dans la grange (voir la biographie).")},
    {"img": None, "slug": None, "name": "Amos", "text": two(
        "The Red Dead Wiki describes Amos as the head ranch hand of MacFarlane's Ranch. He is with Bonnie when she finds John after Fort Mercer. In \"A Tempest Looms\" the two of them argue over sending the men out into the storm, until John tells Amos to round up his men (see Biography). In \"Wild Horses, Tamed Passions\", when John asks why she never married, she calls Amos a little \"countrified\". Her last scene in the main story ends as she follows him into the general store. The wiki credits Dan Campbell as his voice and notes that he plays poker with the ranch hands.",
        "Le Red Dead Wiki présente Amos comme le chef des employés du MacFarlane's Ranch. Il est avec Bonnie quand elle trouve John après Fort Mercer. Dans \"A Tempest Looms\", ils se disputent sur l'idée d'envoyer les hommes sous l'orage, jusqu'à ce que John demande à Amos de rassembler ses hommes (voir la biographie). Dans \"Wild Horses, Tamed Passions\", quand John lui demande pourquoi elle ne s'est jamais mariée, elle trouve Amos un peu \"countrified\" (rustaud). Sa dernière scène dans l'histoire principale s'achève quand elle le suit dans le magasin général. Le wiki attribue sa voix à Dan Campbell et signale qu'il joue au poker avec les employés du ranch.")},
    {"img": None, "slug": None, "name": "Patrick MacFarlane", "text": two(
        "Her only surviving brother, the banker in New York (see Origins). Bonnie tells John she does not want his help, that she fears a little for his soul, and that she has yet to meet a man wearing a tie whom she could trust.",
        "Son seul frère encore en vie, le banquier de New York (voir Origines). Bonnie dit à John qu'elle ne veut pas de son aide, qu'elle s'inquiète un peu pour son âme et qu'elle n'a encore jamais croisé d'homme en cravate qui lui inspire confiance.")},
    {"img": None, "slug": None, "name": "The MacFarlane brothers", "text": two(
        "Five of her six brothers are dead; their names, graves and causes of death are given under Origins.",
        "Cinq de ses six frères sont morts ; leurs noms, leurs tombes et les causes de leur mort sont donnés dans la partie Origines.")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "The two women meet for the first time in \"Old Friends, New Problems\" (see Biography). When Bonnie asks about her ordeal, Abigail says she has been through worse. When John jokes about Abigail's cooking and both women turn on him, he says he has never felt so outnumbered.",
        "Les deux femmes se rencontrent pour la première fois dans \"Old Friends, New Problems\" (voir la biographie). Quand Bonnie l'interroge sur ce qu'elle a vécu, Abigail répond qu'elle a connu pire. Quand John se moque de la cuisine d'Abigail et que toutes deux s'en prennent à lui, il dit ne s'être jamais senti aussi en minorité.")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "Bonnie meets Jack in \"The Outlaw's Return\" (see Biography). John tells him to say hello to Miss MacFarlane; when John complains about the arrogance of youth, Bonnie replies that the boy must take after his father. In 1914 Jack never sees her (see Biography).",
        "Bonnie fait la connaissance de Jack dans \"The Outlaw's Return\" (voir la biographie). John lui dit de saluer Miss MacFarlane ; quand il se plaint de l'arrogance de la jeunesse, Bonnie répond que le garçon doit tenir de son père. En 1914, Jack ne la croise jamais (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "When she suggests that John see the marshal, Bonnie calls Bill \"that nice Mr. Williamson\". The shooting at Fort Mercer, the barn fire, her kidnapping and John's 1911 answer about Bill are told in the Biography.",
        "Quand elle conseille à John d'aller voir le marshal, Bonnie appelle Bill \"that nice Mr. Williamson\" (ce charmant M. Williamson). La fusillade de Fort Mercer, l'incendie de la grange, son enlèvement et ce que John lui dit de Bill en 1911 sont racontés dans la biographie.")},
    {"img": "leigh-johnson.jpeg", "slug": "leigh-johnson", "name": "Leigh Johnson", "text": two(
        "Bonnie sends John to the marshal and later learns his plans from him (see Biography). On the way to Tumbleweed, Johnson asks John whether he is taking advantage of the MacFarlanes, who, he says, are vulnerable in different ways. He leads the posse that frees her.",
        "Bonnie envoie John chez le marshal et apprend ensuite par lui ce que John compte faire (voir la biographie). En route vers Tumbleweed, Johnson demande à John s'il ne profite pas des MacFarlane, qui sont selon lui vulnérables, chacun à sa manière. C'est lui qui mène la troupe qui la délivre.")},
    {"img": None, "slug": None, "name": "Norman Deek", "text": two(
        "Bill Williamson's right-hand man, held in the Armadillo jail: the prisoner the gang demands in exchange for Bonnie (see Biography).",
        "Bras droit de Bill Williamson détenu à la prison d'Armadillo : c'est le prisonnier que la bande réclame en échange de Bonnie (voir la biographie).")},
    {"img": None, "slug": None, "name": "Nathanial Johnston", "text": two(
        "The Armadillo doctor, whose name is on his sign in town, treats John after Fort Mercer (see Biography). In \"This is Armadillo, USA\", Bonnie tells John to be polite to him, since he saved John's life.",
        "Le médecin d'Armadillo, dont le nom figure sur son enseigne en ville, soigne John après Fort Mercer (voir la biographie). Dans \"This is Armadillo, USA\", Bonnie demande à John d'être poli avec lui, puisqu'il lui a sauvé la vie.")},
    {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
        "Bonnie never meets him. When John tells her in \"This is Armadillo, USA\" that Uncle is looking after his farm, she remarks that he sounds like the perfect person to leave in charge of a whole livelihood, and advises John to get back there.",
        "Bonnie ne le rencontre jamais. Quand John lui explique, dans \"This is Armadillo, USA\", qu'Uncle garde sa ferme, elle ironise : voilà la personne idéale à qui confier tout son gagne-pain. Elle conseille à John d'y retourner au plus vite.")},
    {"img": None, "slug": None, "name": "Bonnie's suitor", "text": two(
        "The shipwreck survivor of Red Dead Redemption 2 carries a love letter addressed to her (see Biography).",
        "Le rescapé du naufrage de Red Dead Redemption 2 porte une lettre d'amour qui lui est adressée (voir la biographie).")},
    {"img": None, "slug": None, "name": "Red Dead Online protagonist", "text": two(
        "In 1898 Bonnie first takes the online protagonist for a robber, then hires them to recover a missing wagon (see Biography), before offering the free roam missions described under Skills.",
        "En 1898, Bonnie prend d'abord le protagoniste de Red Dead Online pour un voleur, puis l'engage pour retrouver un chariot disparu (voir la biographie), avant de lui proposer les missions en mode libre décrites dans la partie Compétences.")},
]
