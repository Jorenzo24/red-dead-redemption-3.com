"""Sean MacGuire, reference fiche, PART D: base data, Development and performance, Reception.

His live page (characters/sean-macguire/) was generated from the v2 entry in scripts/_enrich.py
(ENRICHED, "slug": "sean-macguire"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the Rockstar description of 6 Sep 2018 and the official guide's account of his
father are removed from the intro (they belong to part B, Personality, and part A, Origins); the v2
Development paragraphs are kept, re-verified and expanded (Mellamphy's background, the Interesting
Podcast facts as summarized by Wikipedia, the panel title and date, cut content); the Reception section
keeps Eurogamer (now quoted from the article itself) and adds IGN and Game Informer. The "Deceased" chip
duplicated "Died 1899" and is dropped. Eyebrow and reg_role match characters_registry.py ("Van der Linde
gang &middot; RDR2"). publishDate 2026-06-26 kept (git: c654da4, drip publish of sean-macguire,
26 Jun 2026).

Sources (internal register, checked 19 Oct 2026, saved in scratchpad cov/sean/fc/):
- Wikipedia, "List of Red Dead Redemption 2 characters" (sean/m/wp_List_of_Red_Dead_Redemption_2_characters.txt),
  Sean section: Mellamphy second actor cast, replacing the previous actor later in production (ref: cast
  panel at SacAnime, Sacramento, 8 Jun 2019); three years on the game, did not know at first that Sean
  was in the gang, thought the audition was for an IRA member, learned Sean's fate about halfway through
  production while recording audio, "little brother" (ref: The Interesting Podcast, ep. 92, Brian
  Ballance, 8 Aug 2019); Eurogamer summary (ref: Cian Maher, 16 Nov 2018).
- Eurogamer, Cian Maher, "Why Red Dead Redemption 2's Sean MacGuire is the best Irish character in a
  video game yet", 16 Nov 2018 (fetched, eurogamer_maher_2018.txt): "Cork man Michael Mellamphy"; Dublin
  accent; Cait (Fallout 4), Sean Devlin (The Saboteur), Moira (Overwatch); Irish in RDR "just another
  stereotypical whiskey-drinking idiot"; GTA IV McReary family; Famine figures; "a video game character
  who's actually Irish".
- TheGamer, Cian Maher, 20 Jan 2021 (fetched): panel "Irish Redemption: An Irish Invasion of Video Games",
  Origin Theatre's 1st Irish Festival, first shown 15 Jan 2021, with Roger Clark and Penny O'Brien; Ben
  Davis's "Mick, my man. Sean's part of the gang."; "There was just something very Dublin about [Sean] -
  working class, a bit of fun."; the party he missed by going hunting.
- Irish Echo, 2023 Arts & Culture Awards honoree page (fetched): Irish Repertory Theatre company member,
  artistic director of Origin Theatre Company, "The Smuggler" (Ronan Noone), TV credits (I Know This Much
  Is True, Law and Order, SVU, The Good Wife), "Red Dead Redemption 2 and Red Dead Online".
  Irish Stew podcast guest page (fetched; episode S4E17, 23 Jan 2023): "A native of Cork Ireland",
  New York actor, founder of The Pigeon Theatre Company, former owner of the bar Ryan's Daughter.
- Red Dead Wiki "Michael Mellamphy" (wiki_Michael_Mellamphy.txt) and "Red Dead Redemption 2 Cut Content"
  (../uncle/fc/): unused hat texture, two unused vests, robbery outfit, wound model; cut drinking activity;
  concept art of Sean, Trelawny, Sadie, Lenny and Micah. Character page trivia: unused black leather duster.
- IGN review, Luke Reilly, 25 Oct 2018 (quoted as in charles_D, fact-checked).
- Game Informer staff ranking of the gang, 27 Dec 2018 (../uncle/fc/gi_ranking.txt): Sean 12th of 24.
Excluded: Mellamphy's birth date 1 Jun 1977 (wiki only); the name of the first actor (not given by any
source); the SacAnime and podcast details beyond what Wikipedia summarizes (recordings not checked);
Maher's guess that Sean's mother was from Dublin and his "da" came over as a boy (speculation); Maher's
reading of the party as a "drinking culture" and Sean as "always up for a party" (kept only as attributed
opinion, short); the wiki's "Sean appears to have a Dublin accent although from Donegal" (kept only
through Mellamphy and Maher); the theory that "Social Calls With Mr. MacGuire" began as a main mission
(wiki speculation); Red Dead Online stranger missions and Blood Money (part C, Other media; the facts
grid only lists the game).
Fact-check 19 Oct 2026: Family fact attributes the Darragh link to the wiki (name from the in-game scrap);
TV credits per the Irish Echo (Law & Order and Law & Order: SVU); robbery outfit and duster merged (one item);
Maher's Moira judgment corrected ("a little better"); party essential: Sean goes off with Karen during the party.
DUPLICATE ownership: actor, interviews, cut content (incl. the cut drinking activity and unused outfits)
live HERE; parts B and C must not retell them. Rockstar's 6 Sep 2018 description and the guide page
belong to part B; the father's story and the recruitment belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Sean is played by Michael \"Mick\" Mellamphy, who provides both his voice and his motion capture. Mellamphy is an actor from County Cork, in Ireland, based in New York: Eurogamer called him a \"Cork man\" in November 2018, and the Irish Stew podcast introduces him as a native of Cork. He is a company member of the Irish Repertory Theatre in New York and the artistic director of Origin Theatre Company, and his television credits include I Know This Much Is True, Law & Order, Law & Order: SVU and The Good Wife, according to the Irish Echo, which honored him at its 2023 Arts & Culture Awards. The Echo credits him as Sean in both Red Dead Redemption 2 and Red Dead Online.",
              "Sean est interprété par Michael \"Mick\" Mellamphy, qui lui prête sa voix et assure sa capture de mouvement. Mellamphy est un acteur originaire du comté de Cork, en Irlande, installé à New York : Eurogamer le présente en novembre 2018 comme un \"Cork man\" (un gars de Cork), et le podcast Irish Stew comme un natif de Cork. Il fait partie de la troupe de l'Irish Repertory Theatre de New York et dirige artistiquement l'Origin Theatre Company ; à la télévision, il a joué notamment dans I Know This Much Is True, New York, police judiciaire, New York, unité spéciale et The Good Wife, d'après l'Irish Echo, qui l'a distingué lors de ses Arts & Culture Awards 2023. Le journal le crédite dans le rôle de Sean pour Red Dead Redemption 2 comme pour Red Dead Online.")},
    {"p": two("Mellamphy was not the first actor cast as Sean: Wikipedia's list of the game's characters, citing a cast panel held at SacAnime in Sacramento on 8 June 2019, says he replaced another actor later in production. According to the same list, which draws on an August 2019 episode of The Interesting Podcast, he worked on the game for three years, during which the character developed significantly. At the original audition he thought he was being asked to play a member of the Irish Republican Army, and for a while he did not know that Sean belonged to the Van der Linde gang. He learned the character's fate about halfway through production, while recording audio, and described Sean as the player's \"little brother\".",
              "Mellamphy n'est pas le premier acteur à avoir tenu le rôle : la liste des personnages du jeu sur Wikipédia, qui cite une table ronde de la distribution tenue à la SacAnime de Sacramento le 8 juin 2019, indique qu'il a remplacé un autre interprète en cours de production. Selon la même liste, qui s'appuie sur un épisode de The Interesting Podcast diffusé en août 2019, il a travaillé trois ans sur le jeu, période pendant laquelle le personnage a beaucoup évolué. Lors de l'audition, il pensait qu'on lui demandait de jouer un membre de l'Armée républicaine irlandaise, et il a longtemps ignoré que Sean faisait partie du gang Van der Linde. Il a découvert le sort du personnage vers la moitié de la production, lors d'une séance d'enregistrement audio, et a décrit Sean comme le \"little brother\" (petit frère) du joueur.")},
    {"h3": two("The 2021 panel", "La table ronde de 2021")},
    {"p": two("In January 2021 Mellamphy, Roger Clark (Arthur) and Penny O'Brien (Molly O'Shea) took part in \"Irish Redemption: An Irish Invasion of Video Games\", an online panel of Origin Theatre's 1st Irish Festival first shown on 15 January. TheGamer reported on it on 20 January 2021, in an article by Cian Maher. Mellamphy recalled having a beer with the cast while still unsure whether Sean was part of the gang, and being told by Benjamin Byron Davis, who plays Dutch: \"Mick, my man. Sean's part of the gang.\" On the character's accent, he said: \"There was just something very Dublin about [Sean] - working class, a bit of fun.\"",
              "En janvier 2021, Mellamphy, Roger Clark (Arthur) et Penny O'Brien (Molly O'Shea) participent à \"Irish Redemption: An Irish Invasion of Video Games\", une table ronde en ligne du 1st Irish Festival de l'Origin Theatre, diffusée pour la première fois le 15 janvier. TheGamer en rend compte le 20 janvier 2021, sous la plume de Cian Maher. Mellamphy raconte avoir pris une bière avec la distribution alors qu'il ne savait toujours pas si Sean faisait partie du gang, et s'être entendu répondre par Benjamin Byron Davis, l'interprète de Dutch : \"Mick, my man. Sean's part of the gang.\" (Mick, mon vieux, Sean fait partie du gang). Sur l'accent du personnage, il explique : \"There was just something very Dublin about [Sean] - working class, a bit of fun.\" (Sean avait quelque chose de très dublinois : un gars du peuple, qui aime rigoler).")},
    {"p": two("He also told the panel that the party for Sean's return was one of his favorite things in the game, yet as a player he missed it: he took Arthur hunting, came back to camp the next morning to find everyone hungover, and so skipped the two or three months of work he had spent on the scene singing songs and with Karen in the tent.",
              "Il raconte aussi que la fête du retour de Sean compte parmi ses passages préférés du jeu, mais qu'en tant que joueur il l'a ratée : parti chasser avec Arthur, il est revenu au camp le lendemain matin pour trouver tout le monde avec la gueule de bois, passant ainsi à côté des deux ou trois mois de travail consacrés à la scène, entre les chansons et la tente de Karen.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("According to the Red Dead Wiki, the files of Red Dead Redemption 2 contain an unused hat texture for Sean, two unused vests, a robbery outfit and a wound model. The wiki's page on Sean describes that outfit as a black leather duster with visible stitching, of the kind the gang wears on robberies. Drinking with Sean is among the activities with gang members that were cut or reduced, and a piece of concept art shows him with Trelawny, Sadie, Lenny and Micah.",
              "D'après le Red Dead Wiki, les fichiers de Red Dead Redemption 2 contiennent pour Sean une texture de chapeau inutilisée, deux gilets inutilisés, une tenue de braquage et un modèle de blessure. La page du wiki consacrée à Sean décrit cette tenue comme un long manteau de cuir noir aux coutures apparentes, du type de ceux que porte la bande pendant les braquages. Boire un verre avec Sean figure parmi les activités avec les membres du gang qui ont été supprimées ou réduites, et une illustration conceptuelle le montre aux côtés de Trelawny, Sadie, Lenny et Micah.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Reviews and rankings", "Critiques et classements")},
    {"p": two("In IGN's review of 25 October 2018, Luke Reilly said the gang's members came from many cultures, \"from Irish thug Sean Macguire to Native American brawler Charles Smith\", and that \"they all feel like credible human beings and not caricatures.\" In Game Informer's staff ranking of the 24 gang members, published on 27 December 2018, Sean comes 12th. The staff called him \"the life of the party\" and \"a proud Irish immigrant\" who mocks his companions in colorful language, and described his death as \"the first truly shocking moment in the story\", the one that sends the gang's decline into overdrive.",
              "Dans la critique d'IGN du 25 octobre 2018, Luke Reilly note que les membres du gang viennent d'horizons très divers, \"from Irish thug Sean Macguire to Native American brawler Charles Smith\" (du voyou irlandais Sean MacGuire au bagarreur amérindien Charles Smith), et que tous ont l'air d'êtres humains crédibles plutôt que de caricatures. Dans le classement des 24 membres du gang établi par la rédaction de Game Informer et publié le 27 décembre 2018, Sean arrive 12e. Elle le décrit comme \"the life of the party\" (le boute-en-train) et comme un immigré irlandais fier de ses origines, qui se moque de ses compagnons dans une langue fleurie, et voit dans sa mort \"the first truly shocking moment in the story\" (le premier moment vraiment choquant de l'histoire), celui qui précipite le déclin de la bande.")},
    {"h3": two("Eurogamer: an Irish character", "Eurogamer : un personnage irlandais")},
    {"p": two("On 16 November 2018 Eurogamer published a feature by Cian Maher, a writer from Dublin, titled \"Why Red Dead Redemption 2's Sean MacGuire is the best Irish character in a video game yet\". Maher wrote that Sean speaks with a genuine inner-city Dublin accent and that he is \"a Dub, born and bred\". He set him against earlier Irish characters: Cait in Fallout 4, an alcoholic with an accent from no real region of Ireland in his view; Sean Devlin in The Saboteur, whose greetings he called a cliché nobody in Ireland uses; Moira in Overwatch, \"a little better\" but with an accent he did not find to be Dublin's; the McReary family in Grand Theft Auto IV; and the character called Irish in Red Dead Redemption, whom he described as \"just another stereotypical whiskey-drinking idiot\".",
              "Le 16 novembre 2018, Eurogamer publie un article de Cian Maher, auteur dublinois, intitulé \"Why Red Dead Redemption 2's Sean MacGuire is the best Irish character in a video game yet\" (pourquoi Sean MacGuire est le meilleur personnage irlandais de l'histoire du jeu vidéo). Maher y écrit que Sean parle avec un véritable accent des quartiers populaires de Dublin et qu'il est \"a Dub, born and bred\" (un Dublinois pur jus). Il l'oppose aux précédents personnages irlandais : Cait dans Fallout 4, alcoolique dotée selon lui d'un accent qui n'existe dans aucune région d'Irlande ; Sean Devlin dans The Saboteur, aux salutations clichés qu'aucun Irlandais n'emploie ; Moira dans Overwatch, \"a little better\" (un peu mieux), mais dont l'accent n'a rien de dublinois à ses yeux ; la famille McReary dans Grand Theft Auto IV ; et le personnage nommé Irish dans Red Dead Redemption, qu'il décrit comme \"just another stereotypical whiskey-drinking idiot\" (un énième idiot stéréotypé porté sur le whisky).")},
    {"p": two("Maher also placed an Irishman in 1899 America in his historical context, recalling that the Great Famine drove some 1.5 million people from Ireland between 1845 and 1855, 250,000 of them in 1847 alone. He contrasted Sean's behavior at his homecoming party with the solitary drinkers of other games, and concluded that Sean is \"a video game character who's actually Irish\".",
              "Maher replace aussi la présence d'un Irlandais dans l'Amérique de 1899 dans son contexte historique, en rappelant que la Grande Famine a poussé quelque 1,5 million de personnes à quitter l'Irlande entre 1845 et 1855, dont 250 000 pour la seule année 1847. Il oppose l'attitude de Sean pendant la fête de son retour à celle des buveurs solitaires d'autres jeux, et conclut que Sean est \"a video game character who's actually Irish\" (un personnage de jeu vidéo vraiment irlandais).")},
]


BASE = {
    "slug": "sean-macguire", "name": "Sean MacGuire",
    "publishDate": "2026-06-26", "updated": "2026-10-19", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": "Irish",
    "portrait_alt": two("Sean MacGuire in Red Dead Redemption 2", "Sean MacGuire dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Sean MacGuire, the young Irish thief of the Van der Linde gang in RDR2: his rescue from bounty hunters, the Gray feud, his death in Rhodes in 1899, and Michael Mellamphy's performance.",
                     "Sean MacGuire, le jeune voleur irlandais du gang Van der Linde dans RDR2 : son sauvetage, la guerre des Gray, sa mort à Rhodes en 1899 et l'interprétation de Michael Mellamphy."),
    "og_desc": two("The complete reference on Sean MacGuire: life, missions, camp scenes, quotes, development and reception.",
                   "La référence complète sur Sean MacGuire : vie, missions, scènes de camp, citations, conception et accueil."),
    "schema_desc": two("Young Irish thief and stick-up man of the Van der Linde gang, rescued from bounty hunters and shot dead in a Gray family ambush in Rhodes in 1899, in Red Dead Redemption 2.",
                       "Jeune voleur et braqueur irlandais du gang Van der Linde, tiré des griffes de chasseurs de primes puis abattu dans une embuscade de la famille Gray à Rhodes en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Van der Linde gang", "Gang Van der Linde"),
              two("Irish", "Irlandais"),
              two("Voiced by <strong>Michael Mellamphy</strong>", "Voix de <strong>Michael Mellamphy</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Sean MacGuire (also written Macguire)", "Sean MacGuire (aussi écrit Macguire)")},
        {"label": two("Born", "Naissance"), "value": two("Ireland; year not given in the game. In camp he speaks of an old neighbor in Donegal", "Irlande ; année non précisée dans le jeu. Au camp, il évoque un ancien voisin dans le Donegal")},
        {"label": two("Died", "Mort"), "value": two("1899, Rhodes, shot by a sniper in the Gray family ambush of \"A Short Walk in a Pretty Town\"", "1899, à Rhodes, abattu par un tireur embusqué dans le guet-apens des Gray, dans \"A Short Walk in a Pretty Town\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased; buried by Bill, his grave lies just north of Clemens Point", "Décédé ; enterré par Bill, sa tombe se trouve juste au nord de Clemens Point")},
        {"label": two("Nationality", "Nationalité"), "value": two("Irish", "Irlandaise")},
        {"label": two("Family", "Famille"), "value": two("His father, a wanted man, fled with him to America and was killed by the British (official guide); a newspaper scrap in camp names a Fenian, Darragh Macguire, whom the Red Dead Wiki identifies as his father", "Son père, un homme recherché, a fui avec lui en Amérique avant d'être tué par les Britanniques (guide officiel) ; une coupure de journal au camp évoque un fenian, Darragh Macguire, en qui le Red Dead Wiki voit son père")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang", "Gang Van der Linde")},
        {"label": two("Role", "Rôle"), "value": two("Thief and stick-up man", "Voleur et braqueur")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2, Red Dead Online", "Red Dead Redemption 2, Red Dead Online")},
        {"label": two("Voiced by", "Voix"), "value": two("Michael Mellamphy (voice and motion capture)", "Michael Mellamphy (voix et capture de mouvement)")},
    ],
    "intro": [
        two("Sean MacGuire is a young Irish thief and stick-up man in the Van der Linde gang, a supporting character of Red Dead Redemption 2 (2018), set in 1899. Separated from the gang after the failed ferry robbery in Blackwater, he is captured by bounty hunters and freed by [[arthur-morgan|Arthur Morgan]], [[charles-smith|Charles Smith]] and [[javier-escuella|Javier Escuella]] in the second chapter. He then joins the train job of [[john-marston|John Marston]] and burns the Gray family's tobacco fields with Arthur. In the third chapter he is shot dead by a sniper in Rhodes, in an ambush set by the Grays. He is also a mission giver in Red Dead Online.",
            "Sean MacGuire est un jeune voleur et braqueur irlandais du gang Van der Linde, personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Séparé de la bande après le braquage raté du ferry de Blackwater, il est capturé par des chasseurs de primes, puis délivré par [[arthur-morgan|Arthur Morgan]], [[charles-smith|Charles Smith]] et [[javier-escuella|Javier Escuella]] au deuxième chapitre. Il participe ensuite à l'attaque de train de [[john-marston|John Marston]] et incendie avec Arthur les champs de tabac de la famille Gray. Au troisième chapitre, il est abattu par un tireur embusqué à Rhodes, dans un guet-apens tendu par les Gray. Il confie aussi des missions dans Red Dead Online."),
        two("He is played by Michael Mellamphy, an actor from County Cork based in New York, who replaced the first actor cast in the role during production.",
            "Il est interprété par Michael Mellamphy, acteur originaire du comté de Cork installé à New York, qui a remplacé en cours de production le premier interprète du rôle."),
    ],
    "essentials": [
        two("Joined the gang after a failed attempt to rob [[dutch-van-der-linde|Dutch]] and [[hosea-matthews|Hosea]] in North Elizabeth. Goes missing after the Blackwater ferry robbery and is taken by Ike Skelding's bounty hunters.",
            "Entré dans la bande après avoir tenté, sans succès, de détrousser [[dutch-van-der-linde|Dutch]] et [[hosea-matthews|Hosea]] à North Elizabeth. Disparu après le braquage du ferry de Blackwater, il tombe aux mains des chasseurs de primes d'Ike Skelding."),
        two("Freed in \"The First Shall Be Last\", he is welcomed back at Horseshoe Overlook with a party, during which he goes off with [[karen-jones|Karen Jones]].",
            "Délivré dans \"The First Shall Be Last\", il est accueilli à Horseshoe Overlook par une fête, au cours de laquelle il s'éclipse avec [[karen-jones|Karen Jones]]."),
        two("Invites himself onto John's train robbery in \"Pouring Forth Oil IV\" and is saved by Arthur from a guard in the baggage car.",
            "S'invite à l'attaque de train de John dans \"Pouring Forth Oil IV\" et doit à Arthur d'échapper à un garde dans le fourgon à bagages."),
        two("Works with Arthur for Catherine Braithwaite in \"The Fine Joys of Tobacco\", setting the Grays' fields and barn on fire at Caliga Hall.",
            "Travaille avec Arthur pour Catherine Braithwaite dans \"The Fine Joys of Tobacco\" et incendie les champs et la grange des Gray à Caliga Hall."),
        two("Killed by a sniper's bullet to the head in Rhodes in \"A Short Walk in a Pretty Town\", walking beside Arthur, [[bill-williamson|Bill]] and [[micah-bell|Micah]]. His death sends Karen into heavy drinking.",
            "Tué d'une balle dans la tête par un tireur embusqué à Rhodes, dans \"A Short Walk in a Pretty Town\", alors qu'il marche aux côtés d'Arthur, de [[bill-williamson|Bill]] et de [[micah-bell|Micah]]. Sa mort fait sombrer Karen dans l'alcool."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["karen-jones", "lenny-summers", "arthur-morgan", "bill-williamson"],
}
