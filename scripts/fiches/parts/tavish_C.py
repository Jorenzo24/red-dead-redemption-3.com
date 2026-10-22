"""Tavish Gray, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (fetched Oct 2026; local copies in scripts/v3/work/tavish/ and scripts/v3/work/_m/):
- Red Dead Wiki EN "Tavish Gray" (mission appearances, trivia: Leigh/son inconsistency, Malcolm Moffat surname) and FR
  page.
- Red Dead Wiki mission page "Horse Flesh for Dinner" (mission failure list, trivia: real surname given to Tavish, GTA V
  cut heist). Mission pages and transcripts of "The New South", "American Distillation", "The Course of True Love I",
  "Advertising, The New American Art", "The Fine Joys of Tobacco", "A Short Walk in a Pretty Town" and "The Course of True
  Love V" as used in the fact-checked catherine_C.
- Red Dead Wiki pages "Gray's Secret" (gallery captions quoting Arthur's and John's journal drawings; trivia: the only point
  of interest tied to a mission), "Gray Family History Letter", "Gray Family", "Caliga Hall" (Red Dead Online location),
  "Leigh Gray" (Red Dead Online role).
- TRANSCRIPT: "Red Dead Redemption 2 Full Transcript", Game Scripts Wiki
  (game-scripts-wiki.blogspot.com/2022/01/red-dead-redemption-2.html), saved as scripts/v3/work/tavish/fc/gsw.txt
  (gitignored): source of every quoted line below except the two point-of-interest journal entries (Red Dead Wiki
  captions). Lines checked: Tavish's job lines, Dutch in "Advertising, The New American Art", Beau in "The Course of True
  Love I", John and Clay Davies in "Horse Flesh for Dinner", Arthur's journal at the end of that mission, Dutch introducing
  "Arthur Callahan" to Sheriff Gray in "American Distillation".
- Real world: Sam and Dan Houser's mother is the actress Geraldine Moffat (Wikipedia, "Sam Houser" and "Geraldine
  Moffat" articles).

Ownership: narrative events are in part A (one line per mission here). Tavish's lines about the war, his Scottish family,
"I'm Scottish", "We've got gold, Yankee", the "hag" line and the insults against the Braithwaites are LEFT to part B ("In his
own words"); Quotes here keep his lines about the horse job plus lines by others about him. Part A paraphrases all of them.
The letter is told in part A only (partly quoted there). The body unchanged in 1907 is told in part A only.

Excluded: the cause of death (not shown); the glitch preventing the point of interest if the player is shot while picking
up the letter (bug report, no value); the "No true Scotsman" reading of the letter (wiki analysis); the YouTube trick to
keep a stolen horse (not about Tavish); Arthur removing his deputy badge (not about Tavish, and the wiki's "seemingly" is
interpretation); the Gray family crest inspired by Bully (about the family, not Tavish); Pearson's 1907 line (already
quoted on the Catherine Braithwaite fiche; paraphrased in part A here); Red Dead Online appearance for Tavish (none listed).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C3 = two("3. Clemens Point", "3. Clemens Point")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Tavish Gray appears in one mission of Red Dead Redemption 2, in chapter 3. Other missions take place on his land, involve his family or bring up his feud with the Braithwaites; they are listed in the second table. The events themselves are told in the Biography.",
              "Tavish Gray apparaît dans une seule mission de Red Dead Redemption 2, au chapitre 3. D'autres missions se déroulent sur ses terres, mettent en scène sa famille ou touchent à sa querelle avec les Braithwaite ; elles figurent dans le second tableau. Le déroulé des événements se trouve dans la Biographie.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Tavish's role", "Rôle de Tavish")], "rows": [
        M("Horse Flesh for Dinner", C3,
          "Asks [[arthur-morgan|Arthur]], [[john-marston|John]] and [[javier-escuella|Javier]] to steal [[catherine-braithwaite|Catherine Braithwaite]]'s prized horses, which he values at 5,000 dollars; the fence pays 700.",
          "Demande à [[arthur-morgan|Arthur]], [[john-marston|John]] et [[javier-escuella|Javier]] de voler les chevaux de prix de [[catherine-braithwaite|Catherine Braithwaite]], qu'il estime à 5 000 dollars ; le receleur en donne 700."),
    ]}},
    {"h4": two("Other missions linked to Tavish", "Autres missions liées à Tavish")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Tavish", "Lien avec Tavish")], "rows": [
        M("The New South", C3,
          "Arthur helps Tavish's brother, Sheriff Leigh Gray, catch the Anderson boys.",
          "Arthur aide le frère de Tavish, le shérif Leigh Gray, à rattraper les frères Anderson."),
        M("American Distillation", C3,
          "Leigh Gray deputizes [[dutch-van-der-linde|Dutch]], Arthur and [[bill-williamson|Bill]] to shut down a Braithwaite still.",
          "Leigh Gray fait de [[dutch-van-der-linde|Dutch]], d'Arthur et de [[bill-williamson|Bill]] ses adjoints pour démanteler un alambic des Braithwaite."),
        M("The Course of True Love I", C3,
          "Arthur visits Caliga Hall for the first time and meets Tavish's son Beau.",
          "Arthur se rend pour la première fois à Caliga Hall et rencontre Beau, le fils de Tavish."),
        M("Advertising, The New American Art", C3,
          "Arthur and [[hosea-matthews|Hosea]] give away Braithwaite moonshine in the Grays' saloon in Rhodes.",
          "Arthur et [[hosea-matthews|Hosea]] distribuent gratuitement l'alcool des Braithwaite dans le saloon des Gray, à Rhodes."),
        M("The Fine Joys of Tobacco", C3,
          "Arthur and [[sean-macguire|Sean]] burn Tavish's tobacco fields at Caliga Hall for the Braithwaites.",
          "Arthur et [[sean-macguire|Sean]] brûlent les champs de tabac de Tavish à Caliga Hall pour le compte des Braithwaite."),
        M("A Short Walk in a Pretty Town", C3,
          "Sean is killed in a Gray ambush in Rhodes and Leigh Gray dies; Tavish is not there.",
          "Sean est tué dans une embuscade des Gray à Rhodes et Leigh Gray y meurt ; Tavish n'est pas sur place."),
        M("The Course of True Love V", C6,
          "Arthur helps Beau leave Rhodes by train with Penelope Braithwaite.",
          "Arthur aide Beau à quitter Rhodes en train avec Penelope Braithwaite."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Tavish's words about himself and his family are quoted under Personality.",
              "Les répliques ci-dessous sont citées en version originale. Ce que Tavish dit de lui-même et de sa famille figure dans la rubrique Personnalité.")},
    {"h4": two("The horse job", "L'affaire des chevaux")},
    {"quotes": [
        {"q": two("Enough. These are prized horses I'm talking about... them they'll get you... five thousand.",
                  "Enough. These are prized horses I'm talking about... them they'll get you... five thousand."),
         "src": two("Tavish, asked by Arthur how much gold he means, Horse Flesh for Dinner (RDR2, chapter 3)",
                    "Tavish, à Arthur qui lui demande de combien d'or il parle, Horse Flesh for Dinner (RDR2, chapitre 3). Traduction : « Assez. Ce sont des chevaux de prix, je vous parle... Ceux-là vous rapporteront... cinq mille. »")},
        {"q": two("Over in Clemens Cove. Feller over there will run them out of state... and give you fifty cents on the dollar.",
                  "Over in Clemens Cove. Feller over there will run them out of state... and give you fifty cents on the dollar."),
         "src": two("Tavish, asked where to sell the horses, Horse Flesh for Dinner (RDR2, chapter 3)",
                    "Tavish, à qui l'on demande où vendre les chevaux, Horse Flesh for Dinner (RDR2, chapitre 3). Traduction : « Du côté de Clemens Cove. Il y a un gars là-bas qui les fera sortir de l'État... et vous en donnera cinquante cents par dollar. »")},
        {"q": two("Five thousand dollars for horses? We've been robbing the wrong folk all these years.",
                  "Five thousand dollars for horses? We've been robbing the wrong folk all these years."),
         "src": two("John, riding away from Caliga Hall, Horse Flesh for Dinner (RDR2, chapter 3)",
                    "John, en quittant Caliga Hall, Horse Flesh for Dinner (RDR2, chapitre 3). Traduction : « Cinq mille dollars pour des chevaux ? Ça fait des années qu'on vole les mauvaises personnes. »")},
        {"q": two("Ain't no one round here got five thousand dollars, boys... but nice meeting you.",
                  "Ain't no one round here got five thousand dollars, boys... but nice meeting you."),
         "src": two("The fence Clay Davies, after paying 700 dollars for the horses, Horse Flesh for Dinner (RDR2, chapter 3)",
                    "Le receleur Clay Davies, après avoir payé les chevaux 700 dollars, Horse Flesh for Dinner (RDR2, chapitre 3). Traduction : « Personne dans le coin n'a cinq mille dollars, les gars... mais ravi de vous avoir rencontrés. »")},
        {"q": two("Believed a yarn, spun us by one of that Gray family... and imagined we was gonna be wonderfully rich. At the end of it we felt like prize idiots.",
                  "Believed a yarn, spun us by one of that Gray family... and imagined we was gonna be wonderfully rich. At the end of it we felt like prize idiots."),
         "src": two("Arthur's journal, at the end of Horse Flesh for Dinner (RDR2, chapter 3)",
                    "Journal d'Arthur, à la fin de Horse Flesh for Dinner (RDR2, chapitre 3). Traduction : « On a cru une histoire que nous a racontée un de ces Gray... et on s'imaginait déjà merveilleusement riches. Au bout du compte, on s'est sentis comme des imbéciles de concours. »")},
    ]},
    {"h4": two("About Tavish and the Grays", "Au sujet de Tavish et des Gray")},
    {"quotes": [
        {"q": two("Sheriff Gray kindly put in a word with his father.",
                  "Sheriff Gray kindly put in a word with his father."),
         "src": two("Dutch, when Arthur asks how the gang got in at the Grays' place, Advertising, The New American Art (RDR2, chapter 3)",
                    "Dutch, quand Arthur demande comment la bande a pu entrer chez les Gray, Advertising, The New American Art (RDR2, chapitre 3). Traduction : « Le shérif Gray a eu la gentillesse de glisser un mot à son père. »")},
        {"q": two("I'm Beau Gray, son of Tavish Gray... nephew of Leigh Gray the sheriff... grandson of old Murdo Gray.",
                  "I'm Beau Gray, son of Tavish Gray... nephew of Leigh Gray the sheriff... grandson of old Murdo Gray."),
         "src": two("Beau Gray to Arthur at Caliga Hall, The Course of True Love I (RDR2, chapter 3)",
                    "Beau Gray à Arthur, à Caliga Hall, The Course of True Love I (RDR2, chapitre 3). Traduction : « Je suis Beau Gray, fils de Tavish Gray... neveu de Leigh Gray, le shérif... petit-fils du vieux Murdo Gray. »")},
        {"q": two("Well, well, well. Guess the Gray family ain't quite the proud noble Southern patriots they pretended to be.",
                  "Well, well, well. Guess the Gray family ain't quite the proud noble Southern patriots they pretended to be."),
         "src": two("Arthur's journal, on finding Tavish's body and the letter (RDR2; caption on the Red Dead Wiki's Gray's Secret page)",
                    "Journal d'Arthur, après la découverte du corps de Tavish et de la lettre (RDR2 ; légende de la page Gray's Secret du Red Dead Wiki). Traduction : « Tiens, tiens, tiens. On dirait que les Gray ne sont pas tout à fait les fiers et nobles patriotes sudistes qu'ils prétendaient être. »")},
        {"q": two("Seems that the Gray family, who we had all those fights with all them years ago, weren't quite the proud noble Southern patriots they pretended to be.",
                  "Seems that the Gray family, who we had all those fights with all them years ago, weren't quite the proud noble Southern patriots they pretended to be."),
         "src": two("John's journal, on finding Tavish's body and the letter (RDR2, 1907 epilogue; caption on the Red Dead Wiki's Gray's Secret page)",
                    "Journal de John, après la découverte du corps de Tavish et de la lettre (RDR2, épilogue de 1907 ; légende de la page Gray's Secret du Red Dead Wiki). Traduction : « Il semble que les Gray, avec qui on s'est tant battus il y a toutes ces années, n'étaient pas tout à fait les fiers et nobles patriotes sudistes qu'ils prétendaient être. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("John introduces Arthur to Tavish as \"Arthur Morgan\", his real name. In \"American Distillation\", Dutch had introduced him to Sheriff Gray under the alias Arthur Callahan.",
            "John présente Arthur à Tavish sous son vrai nom, \"Arthur Morgan\". Dans \"American Distillation\", Dutch l'avait présenté au shérif Gray sous le pseudonyme d'Arthur Callahan."),
        two("Attacking or killing Tavish fails \"Horse Flesh for Dinner\".",
            "Agresser ou tuer Tavish fait échouer \"Horse Flesh for Dinner\"."),
        two("According to the Red Dead Wiki, \"Gray's Secret\" is the only point of interest in the game that requires a specific mission to be completed before it can be found.",
            "Selon le Red Dead Wiki, \"Gray's Secret\" est le seul point d'intérêt du jeu qui ne peut être découvert qu'après une mission précise."),
        two("The historian who writes to Tavish, Malcolm Moffat, shares his surname with Geraldine Moffat, the actress who is the mother of Sam and Dan Houser, co-founders of Rockstar Games.",
            "L'historien qui écrit à Tavish, Malcolm Moffat, porte le même nom que Geraldine Moffat, l'actrice qui est la mère de Sam et Dan Houser, cofondateurs de Rockstar Games."),
        two("According to the Red Dead Wiki, \"Horse Flesh for Dinner\" reuses the idea of a heist cut from Grand Theft Auto V, in which the crew poses as buyers interested in a rival's property in order to steal his horses.",
            "Selon le Red Dead Wiki, \"Horse Flesh for Dinner\" reprend l'idée d'un braquage coupé de Grand Theft Auto V, dans lequel l'équipe se fait passer pour des acheteurs intéressés par la propriété d'un rival afin de lui voler ses chevaux."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("The Red Dead Wiki lists Tavish only in Red Dead Redemption 2. Caliga Hall, his estate, is also a location in Red Dead Online, whose story is set in 1898. His brother Leigh Gray appears there as the sheriff of Rhodes, who sells the player a bounty hunter license.",
              "Le Red Dead Wiki ne recense Tavish que dans Red Dead Redemption 2. Caliga Hall, son domaine, figure aussi parmi les lieux de Red Dead Online, dont l'histoire se déroule en 1898. Son frère Leigh Gray y apparaît en shérif de Rhodes, qui vend au joueur une licence de chasseur de primes.")},
]
