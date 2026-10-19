"""Uncle, reference fiche, PART D: base data, Development and performance, Reception.

His live page (characters/uncle/) was generated from the v2 entry in scripts/_enrich.py
(ENRICHED, "slug": "uncle"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the Rockstar description of 6 Sep 2018 and the official guide
claims (wives, travels, gunslinger, "terminal lumbago") are removed from the intro and
biography base (they belong to part B, Personality); the v2 Development paragraph is kept
and expanded with sourced facts (manual credit for Spider Madison, O'Creagh's death date and
stage career, the lake's location, cut content); a Reception section is added with dated,
attributed articles (the v2 page had none). The "Deceased" chip duplicated "Died 1911" and
is dropped. Eyebrow and reg_role match characters_registry.py ("Van der Linde gang &middot;
RDR1 &amp; 2"). publishDate 2026-07-14 kept (git: 8579ec0, drip publish of uncle, 14 Jul 2026).

Sources (internal register, fetched 19 Oct 2026, saved in scratchpad cov/uncle/fc/):
- Red Dead Redemption manual (Rockstar, 2010; rdr1_manual.txt): cast list "Uncle ...
  Spider Madison". Red Dead Wiki "Spider Madison" (also Undead Nightmare; the 2005 short
  "Lookin' for Some Posse"), "James McBride" (American actor and producer, voice and motion
  capture for Uncle), "John O'Creagh" (born Jonathan Regis Cray, 5 Jan 1949; died 30 Oct
  2016, blood clot), "O'Creagh's Run" (lake, Grizzlies East, Ambarino, north of the Three
  Sisters), infobox of "Uncle" (O'Creagh credited for singing), "Myths and Mavericks".
- Death notice, The New York Times via Legacy.com (search extract, search_notes.txt):
  Jonathan Regis Cray (O'Creagh), 67, died 30 Oct 2016 at Lenox Hill Hospital, New York,
  complications from a blood clot; last stage roles William Gregson in A Day by the Sea and
  Alfred P. Doolittle in My Fair Lady at Bay Street Theater. Bay Street Theater statement,
  31 Oct 2016 (search extract). BroadwayWorld: Katie Roche (Mint Theater, 2013), West Side
  Story US national tour (2010, Doc).
- Wikipedia "List of Red Dead Redemption 2 characters" (wp_list_rdr2_characters.txt), Uncle
  section: O'Creagh replaced Madison, died in production, replaced by McBride, singing kept,
  O'Creagh's Run named after him (ref: cast panel, Fan Expo Canada, Toronto, 24 Aug 2019).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content": unused torso; cut cutscene in "Bare
  Knuckle Friendships" (ride to Riggs Station); two cut Beecher's Hope encounters (files
  bcunc3, bcunc5: bath, drink); cut drinking activity with Uncle; stand-in horse model in
  trailers; concept art (Bill, Karen, Tilly, Uncle, Mary-Beth, Strauss, Pearson); some unused
  O'Creagh lines left in the files. "Red Dead Redemption Cut Content": nothing on Uncle.
- Game Informer: Jill Grodt, 28 Sep 2018 (gi_returning.txt); staff ranking, 27 Dec 2018
  (gi_ranking.txt, 16th of 24). Ranking quote of the game line checked against the transcript
  of "Home Improvement for Beginners" ("I've had better nightmares than this dream").
- Game Rant, Eric Seitz, 6 Jul 2022, "Red Dead Redemption 2 - What Is Lumbago?"
  (gamerant_lumbago.txt).
Excluded: Uncle's birth in Ohio (wiki, single YouTube reference); Roger Clark's statement that
Madison could not return for health reasons (wiki, single YouTube short, not verifiable);
the claim that Madison played "a similar character" in the 2005 short (interpretation);
the Rawhide "Wishbone" inspiration (wiki: "seem to be based off", speculation); a 2023 Reddit
photo of Madison (irrelevant); O'Creagh's birth date 5 Jan 1949 (wiki only; his age, 67, is
given by the death notice); McBride's birth year 1952 and height (wiki only); Grodt's line
that Uncle "came with" John and Abigail when they left the gang (contradicted by the epilogue:
John finds him in Blackwater in 1907); Game Rant's claim that Uncle never mentions lumbago in
Red Dead Redemption (not checked against RDR1 transcripts) and its speculation that Uncle uses
his "academic knowledge" to fool John; the rustling minigame (not about Uncle himself);
television credits of O'Creagh (search extract only, not checked).
Fact-check fixes (19 Oct 2026): Abigail "around 1894" attributed to the official guide (no "since before 1894"
claim); the An Honest Mistake tip is for a supposedly unguarded wagon that turns out to be Cornwall's; Molly is
brought back "shortly before she is killed" (no source gives the time of day); O'Creagh's Doolittle was "that summer"
(his last role was William Gregson); O'Creagh's Run is named after him per Wikipedia and the wiki's Uncle and O'Creagh
pages, only the lake page hedges; "former thief" added to the Role fact, attributed to the wiki infobox (Thief,
formerly). Roger Clark's statement on Madison's health stays excluded (single YouTube short).
DUPLICATE ownership: actors, O'Creagh's Run and all cut content live HERE; parts B and C must
not retell them (C trivia may not repeat). Rockstar's 6 Sep 2018 description and the official
guide belong to part B. Myths and Mavericks (multiplayer, 2011) is in the facts grid; any
fuller account belongs to part C (Other media).
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("In Red Dead Redemption (2010), Uncle is played by Spider Madison, who is credited in the role in the cast list printed in the game's manual. Madison also plays him in Undead Nightmare, the expansion released the same year. According to the Red Dead Wiki, the character shares the actor's likeness as well as his voice, and Madison had earlier appeared in a 2005 short film, Lookin' for Some Posse. The game's cutscenes and dialogue were directed by Rod Edge, who also led the performance capture of Red Dead Redemption 2.",
              "Dans Red Dead Redemption (2010), Uncle est interprété par Spider Madison, crédité dans ce rôle sur la liste des interprètes imprimée dans la notice du jeu. Madison le joue aussi dans Undead Nightmare, l'extension sortie la même année. D'après le Red Dead Wiki, le personnage reprend les traits de l'acteur en plus de sa voix ; Madison était auparavant apparu dans un court métrage de 2005, Lookin' for Some Posse. Les cinématiques et les dialogues du jeu sont dirigés par Rod Edge, qui dirige aussi la capture de performance de Red Dead Redemption 2.")},
    {"p": two("For Red Dead Redemption 2 (2018), the part was first given to John O'Creagh, an American stage and screen actor born Jonathan Regis Cray. On stage he played Doc in the 2010 US national tour of West Side Story and appeared Off-Broadway in Katie Roche at the Mint Theater in 2013. O'Creagh died on 30 October 2016 at Lenox Hill Hospital in New York, aged 67, of complications from a blood clot, according to the death notice published in The New York Times. Bay Street Theater, in Sag Harbor, where he had played Alfred P. Doolittle in My Fair Lady that summer, announced his death the next day.",
              "Pour Red Dead Redemption 2 (2018), le rôle revient d'abord à John O'Creagh, acteur américain de théâtre et d'écran, né Jonathan Regis Cray. Sur scène, il a joué Doc dans la tournée américaine de West Side Story en 2010 et s'est produit Off-Broadway dans Katie Roche, au Mint Theater, en 2013. O'Creagh meurt le 30 octobre 2016 à l'hôpital Lenox Hill de New York, à 67 ans, des suites d'un caillot sanguin, selon l'avis de décès paru dans The New York Times. Le Bay Street Theater de Sag Harbor, où il avait joué Alfred P. Doolittle dans My Fair Lady cet été-là, annonce sa mort le lendemain.")},
    {"p": two("O'Creagh died while the game was still in production, and the role was recast. James McBride, an American actor and producer, provides Uncle's voice and motion capture in the released game. Part of O'Creagh's work was kept: Uncle's singing is his voice, and the Red Dead Wiki lists him for the singing alongside McBride. According to the same wiki, some unused lines recorded by O'Creagh remain in the game files. Wikipedia's list of the game's characters, which cites a cast panel held at Fan Expo Canada in Toronto on 24 August 2019, gives the same account of the recasting.",
              "O'Creagh meurt alors que le jeu est encore en production, et le rôle change d'interprète. James McBride, acteur et producteur américain, assure la voix et la capture de mouvement d'Uncle dans le jeu final. Une partie du travail d'O'Creagh est conservée : c'est sa voix que l'on entend quand Uncle chante, et le Red Dead Wiki le mentionne pour le chant aux côtés de McBride. D'après le même wiki, des répliques inutilisées enregistrées par O'Creagh subsistent dans les fichiers du jeu. La liste des personnages du jeu sur Wikipédia, qui cite une table ronde des interprètes tenue à la Fan Expo Canada de Toronto le 24 août 2019, rapporte le même changement de distribution.")},
    {"p": two("A lake in the Grizzlies East region of Ambarino, north of the Three Sisters mountains, is called O'Creagh's Run. Wikipedia's list of characters and the Red Dead Wiki's pages on Uncle and on John O'Creagh both state that it is named after the actor; only the wiki's page on the lake itself is more cautious. The lake can also be visited in Red Dead Online.",
              "Un lac des Grizzlies East, dans l'Ambarino, au nord du massif des Three Sisters, porte le nom d'O'Creagh's Run. La liste des personnages de Wikipédia et les pages du Red Dead Wiki consacrées à Uncle et à John O'Creagh affirment toutes qu'il doit son nom à l'acteur ; seule la page du wiki consacrée au lac se montre plus prudente. Le lac figure aussi dans Red Dead Online.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The files of Red Dead Redemption 2 contain an unused torso model for Uncle. In \"Bare Knuckle Friendships\", a cutscene was meant to show John and Uncle riding to Riggs Station; in the released game the mission skips straight to the two men stepping off the train. Two encounters with Uncle were cut from Beecher's Hope: in both, he asks John to leave him alone, saying he needs time to clean himself up with a bath and that he has earned a drink. Drinking with Uncle is also among the activities with gang members that were cut or reduced.",
              "Les fichiers de Red Dead Redemption 2 contiennent un modèle de torse inutilisé pour Uncle. Dans \"Bare Knuckle Friendships\", une cinématique devait montrer John et Uncle chevauchant jusqu'à Riggs Station ; dans le jeu final, la mission passe directement à la descente du train. Deux scènes avec Uncle ont été retirées de Beecher's Hope : dans les deux, il demande à John de le laisser tranquille, en expliquant qu'il a besoin de temps pour se décrasser dans un bain et qu'il a bien mérité un verre. Boire un verre avec Uncle figure aussi parmi les activités avec les membres de la bande qui ont été supprimées ou réduites.")},
    {"p": two("In the trailers released before launch, a generic horse model stands in for Uncle's horse, as it does for several other cutscene horses. A piece of concept art shows Uncle with Bill, Karen, Tilly, Mary-Beth, Strauss and Pearson. The Red Dead Wiki's page on cut content from Red Dead Redemption lists nothing related to Uncle.",
              "Dans les bandes-annonces diffusées avant la sortie, un modèle de cheval générique remplace celui d'Uncle, comme pour plusieurs autres chevaux de cinématique. Une illustration conceptuelle montre Uncle aux côtés de Bill, Karen, Tilly, Mary-Beth, Strauss et Pearson. La page du Red Dead Wiki consacrée au contenu coupé de Red Dead Redemption ne mentionne rien qui concerne Uncle.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Before the release of Red Dead Redemption 2", "Avant la sortie de Red Dead Redemption 2")},
    {"p": two("In a Game Informer feature on the seven characters returning from the first game, published on 28 September 2018, Jill Grodt called Uncle \"a legendary lay-about\" whose real name is unknown. She wrote that he likes to drink and that \"only a fool would depend on him to complete a task\", but that he knows how to get on the good side of important people. She also described him as a kind man, a skilled shot and a competent horseman, whose sarcasm hides his affection for those around him, and added that \"in dire circumstances, he defends his family.\" Her profile ends with his death defending the Marston ranch against the soldiers sent to kill John.",
              "Dans un dossier de Game Informer consacré aux sept personnages du premier jeu qui reviennent dans la préquelle, publié le 28 septembre 2018, Jill Grodt présente Uncle comme \"a legendary lay-about\" (un fainéant légendaire) dont on ignore le vrai nom. Selon elle, il aime boire et seul un imbécile compterait sur lui pour mener une tâche à bien, mais il sait s'attirer les bonnes grâces des gens importants. Elle le décrit aussi comme un homme gentil, bon tireur et cavalier compétent, dont le sarcasme cache l'affection qu'il porte à son entourage et qui, quand la situation l'exige, défend les siens. Son portrait se termine sur sa mort, en défendant le ranch des Marston contre les soldats venus tuer John.")},
    {"h3": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"ul": [
        two("Game Informer, 27 December 2018: 16th of the 24 members of the Van der Linde gang in the staff ranking. The staff wrote that if any face of the game had \"launched a thousand memes\", it was Uncle's, along with \"his tragic case of LUMBAGO\". They noted that the gang treats him as a fool and picks on him as much as Pearson, but argued that he is not that dumb, citing his mockery of the run-down shack John presents as a dream home for Abigail and the line \"I've had better nightmares than this dream.\"",
            "Game Informer, 27 décembre 2018 : 16e des 24 membres du gang Van der Linde dans le classement de la rédaction. Selon elle, si un visage du jeu a \"launched a thousand memes\" (lancé un millier de mèmes), c'est celui d'Uncle et de \"his tragic case of LUMBAGO\" (son tragique cas de lumbago). La rédaction relève que la bande le prend pour un idiot et s'en moque autant que de Pearson, mais estime qu'il n'est pas si bête, comme le montre sa charge contre la cabane délabrée que John présente comme la maison rêvée pour Abigail, avec la réplique \"I've had better nightmares than this dream\" (j'ai fait des cauchemars plus réussis que ce rêve)."),
        two("Game Rant, 6 July 2022: in a piece by Eric Seitz on Uncle's illness, the site explains that lumbago simply means lower back pain, that four out of five people experience it at some point according to the Cleveland Clinic, and that it is not terminal, contrary to what Uncle claims. Seitz writes that whether or not Uncle really suffers from back pain, \"his true ailment is chronic laziness\", and that he is a colorful character who \"brought some much-needed levity\" to the camp.",
            "Game Rant, 6 juillet 2022 : dans un article d'Eric Seitz consacré à la maladie d'Uncle, le site explique que le lumbago désigne simplement une douleur au bas du dos, que quatre personnes sur cinq en souffrent un jour selon la Cleveland Clinic, et qu'il n'a rien de mortel, contrairement à ce qu'affirme Uncle. Seitz écrit que, qu'Uncle ait mal au dos ou non, \"his true ailment is chronic laziness\" (son vrai mal, c'est une paresse chronique), et qu'il s'agit d'un personnage haut en couleur qui a apporté au camp une légèreté bienvenue."),
    ]},
]


BASE = {
    "slug": "uncle", "name": "Uncle",
    "publishDate": "2026-07-14", "updated": "2026-10-19", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR1 &amp; 2", "reg_role_fr": "Gang Van der Linde &middot; RDR1 &amp; 2",
    "gender": "Male", "death": "1911", "nationality": "American",
    "portrait_alt": two("Uncle in Red Dead Redemption 2", "Uncle dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Uncle, the oldest hanger-on of the Van der Linde gang in RDR2 and the Marstons' companion at Beecher's Hope until his death in 1911. Biography, missions, actors.",
                     "Uncle, le plus vieux pilier de comptoir du gang Van der Linde dans RDR2 et le compagnon des Marston à Beecher's Hope jusqu'à sa mort en 1911. Biographie, missions, interprètes."),
    "og_desc": two("The complete reference on Uncle: life, missions, quotes, development and reception.",
                   "La référence complète sur Uncle : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Aging member of the Van der Linde gang in 1899 whose real name is never given, who helps John Marston build the ranch at Beecher's Hope in 1907 and is killed defending it in 1911, in Red Dead Redemption.",
                       "Vieux membre du gang Van der Linde en 1899, dont le vrai nom n'est jamais donné, qui aide John Marston à bâtir le ranch de Beecher's Hope en 1907 et meurt en le défendant en 1911, dans Red Dead Redemption."),
    "chips": [two("Died <strong>1911</strong>", "Mort en <strong>1911</strong>"), two("Van der Linde gang", "Gang Van der Linde"),
              two("Beecher's Hope", "Beecher's Hope"),
              two("Voiced by <strong>Spider Madison</strong> and <strong>James McBride</strong>", "Voix de <strong>Spider Madison</strong> et <strong>James McBride</strong>")],
    "facts": [
        {"label": two("Real name", "Vrai nom"), "value": two("Never given in either game", "Jamais donné, dans aucun des deux jeux")},
        {"label": two("Born", "Naissance"), "value": two("Not given; he is one of the oldest members of the gang", "Non précisée ; c'est l'un des plus vieux membres de la bande")},
        {"label": two("Died", "Mort"), "value": two("1911, Beecher's Hope, shot during the attack on the ranch in \"The Last Enemy That Shall Be Destroyed\"", "1911, à Beecher's Hope, abattu lors de l'assaut du ranch dans \"The Last Enemy That Shall Be Destroyed\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased; buried on the hill at Beecher's Hope", "Décédé ; enterré sur la colline de Beecher's Hope")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang (until 1899); Marston family at Beecher's Hope (1907 to 1911)", "Gang Van der Linde (jusqu'en 1899) ; famille Marston à Beecher's Hope (1907 à 1911)")},
        {"label": two("Role", "Rôle"), "value": two("Hanger-on of the gang (1899); resident and ranch hand at Beecher's Hope (1907 to 1911). The Red Dead Wiki lists him as a former thief", "Pique-assiette de la bande (1899) ; habitant et homme à tout faire du ranch de Beecher's Hope (1907 à 1911). Le Red Dead Wiki le présente comme un ancien voleur")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption (also a multiplayer character with the Myths and Mavericks pack, 2011), Undead Nightmare, Red Dead Redemption 2", "Red Dead Redemption (aussi personnage jouable en multijoueur avec le pack Myths and Mavericks, 2011), Undead Nightmare, Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Spider Madison (Red Dead Redemption, Undead Nightmare); James McBride (Red Dead Redemption 2), with singing by John O'Creagh, first cast in the role, who died in 2016", "Spider Madison (Red Dead Redemption, Undead Nightmare) ; James McBride (Red Dead Redemption 2), avec le chant de John O'Creagh, premier titulaire du rôle, mort en 2016")},
    ],
    "intro": [
        two("Uncle is an aging member of the Van der Linde gang and a companion of the Marston family. His real name is never given: [[john-marston|John Marston]] tells his son that people always called him Uncle, probably because he has always been older than everyone else. He is a supporting character of Red Dead Redemption 2 (2018), set in 1899 and 1907, and of Red Dead Redemption (2010), set in 1911. After the gang breaks up, he helps John and [[charles-smith|Charles Smith]] build the ranch at Beecher's Hope in 1907 and lives there with John, [[abigail-marston|Abigail]] and [[jack-marston|Jack]]. In 1911 he is shot dead defending the ranch against the soldiers and agents led by [[edgar-ross|Edgar Ross]].",
            "Uncle est un vieux membre du gang Van der Linde et un compagnon de la famille Marston. Son vrai nom n'est jamais donné : [[john-marston|John Marston]] explique à son fils qu'on l'a toujours appelé Uncle, sans doute parce qu'il a toujours été plus vieux que tout le monde. C'est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899 et 1907, et de Red Dead Redemption (2010), qui se passe en 1911. Après la dislocation de la bande, il aide John et [[charles-smith|Charles Smith]] à bâtir le ranch de Beecher's Hope en 1907 et y vit avec John, [[abigail-marston|Abigail]] et [[jack-marston|Jack]]. En 1911, il est abattu en défendant le ranch contre les soldats et les agents menés par [[edgar-ross|Edgar Ross]]."),
        two("He is played by Spider Madison in Red Dead Redemption and Undead Nightmare, and by James McBride in Red Dead Redemption 2, a role first given to John O'Creagh, who died during production.",
            "Spider Madison l'interprète dans Red Dead Redemption et Undead Nightmare, James McBride dans Red Dead Redemption 2 ; le rôle avait d'abord été confié à John O'Creagh, mort pendant la production."),
    ],
    "essentials": [
        two("A long-standing member of the Van der Linde gang; according to the official guide to Red Dead Redemption 2, he brings [[abigail-marston|Abigail]] into it around 1894. In 1899 he spends more time drinking and napping in camp than working.",
            "Membre de longue date du gang Van der Linde ; d'après le guide officiel de Red Dead Redemption 2, c'est lui qui y fait entrer [[abigail-marston|Abigail]], vers 1894. En 1899, il passe plus de temps à boire et à dormir au camp qu'à travailler."),
        two("He rides into Valentine with [[arthur-morgan|Arthur Morgan]] in \"Polite Society, Valentine Style\", brings him the tip for a supposedly unguarded wagon, which turns out to belong to Cornwall, in \"An Honest Mistake\", and takes him rustling cattle during the Saint Denis chapter.",
            "Il accompagne [[arthur-morgan|Arthur Morgan]] à Valentine dans \"Polite Society, Valentine Style\", lui apporte dans \"An Honest Mistake\" le tuyau d'un chariot censé rouler sans escorte, qui se révèle appartenir à Cornwall, et l'emmène voler du bétail pendant le chapitre de Saint-Denis."),
        two("At Beaver Hollow he brings a drunk [[molly-oshea|Molly O'Shea]] back to camp shortly before she is killed, then leaves the gang before its collapse.",
            "À Beaver Hollow, il ramène au camp une [[molly-oshea|Molly O'Shea]] ivre, peu avant qu'elle soit abattue, puis quitte la bande avant son effondrement."),
        two("In 1907 he meets [[john-marston|John]] again in Blackwater, leads him to [[charles-smith|Charles]] in Saint Denis and supervises the building of the house at Beecher's Hope. The Skinner Brothers kidnap him and burn his back; John and Charles rescue him.",
            "En 1907, il retrouve [[john-marston|John]] à Blackwater, le conduit jusqu'à [[charles-smith|Charles]] à Saint-Denis et dirige la construction de la maison de Beecher's Hope. Les frères Skinner l'enlèvent et lui brûlent le dos ; John et Charles le délivrent."),
        two("In 1911 he keeps the ranch, badly, while John hunts his former companions. He spots the army coming in \"The Last Enemy That Shall Be Destroyed\", fights beside John and is shot dead on the porch.",
            "En 1911, il garde le ranch, mal, pendant que John traque ses anciens compagnons. Il repère l'armée qui arrive dans \"The Last Enemy That Shall Be Destroyed\", se bat aux côtés de John et meurt abattu sur le porche."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["john-marston", "abigail-marston", "charles-smith", "jack-marston"],
}
