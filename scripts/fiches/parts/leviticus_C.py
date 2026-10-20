"""Leviticus Cornwall, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/leviticus/, m/ and w/):
- Red Dead Wiki EN "Leviticus Cornwall" (Mission appearances: "Who the Hell is Leviticus Cornwall?" (picture only),
  "The Sheep and the Goats", "Just a Social Call"; Quotes; Trivia; Gallery captions) and FR "Leviticus Cornwall"
  (fr.txt: Apparitions dans les missions adds "Une cage dorée"; Red Dead Online paragraph on Etta Doyle; Anecdote).
- Mission pages: Old Friends; Who the Hell is Leviticus Cornwall? (trivia: Granite Pass cutscene, journal entries,
  Valentine station clerk); Eastward Bound; Exit, Pursued by a Bruised Ego; A Fisher of Men; Pouring Forth Oil II
  (via arthur_A, john_A); The Sheep and the Goats (trivia: Dutch's impatience); Blessed are the Peacemakers; The New
  South; An Honest Mistake; Sodom? Back to Gomorrah; The Gilded Cage; American Fathers I and II (via arthur_B); Savagery
  Unleashed (via arthur_C and the wiki pages "Angel" and "Guarma"); Just a Social Call (gold medal objectives, trivia:
  Malvina, Turbinia); The Delights of Van Horn; My Last Boy.
- Transcripts "/dialogues": Who the Hell is Leviticus Cornwall?, A Fisher of Men, The New South, Sodom? Back to
  Gomorrah, Blessed are the Peacemakers. Every line from these missions below is checked word for word against them
  (straight apostrophes replace the transcripts' curly ones).
- Cornwall's own lines: the wiki has no transcript for "The Sheep and the Goats" or "Just a Social Call"; his lines are
  quoted from the character page's quote list and quote boxes, and the mission is given only where the context named
  by the wiki leaves no doubt (hostage threat = Valentine; Milton, Didsbury, Dutch's proposal = Annesburg). "My name is
  Leviticus Cornwall..." has no context beyond "introducing himself": left to part B or out.
- Other pages: "Trains" (unique locomotive), "Valentine" (cigarette card location), "Prominent Americans Card Set",
  newspaper issue lists ("Train Robbed", "Cornwall Murdered"), "Cornwall Freight Yard" and "Etta Doyle" (Red Dead
  Online bounty), "Cornwall Kerosene & Tar" (Kerosene, Tar, and Greed), "The Cornwall Contract" (Blood Money stub);
  Blood Money release date July 13, 2021 as in sean_C.
Ownership: narrative events stay in part A (one line per mission here); Cornwall's lines likely used in part B "In
his own words" are left for the fixer to dedupe. Real-world material (John Rue, the composite character, the Butch
Cassidy and the Sundance Kid parallel, the meaning of the name Leviticus, the Ossian source of "Malvina") goes to D.
Fact-check fixes (20 Oct 2026): the "Cornwall" quote sub-block is removed (all five lines are in part B "In his own
words"); "bygones", "You kill, I kill", "railway magnate", "more than enough to share", Hosea's Pinkerton line and
"Forget about Cornwall" are removed from "About Cornwall" (quoted in parts A or B). Trivia drops the motto, Malvina and
the mission-title item (now in part B); journal item and Kerosene, Tar, and Greed reworded; card location follows the
"Prominent Americans Card Set" page; Etta Doyle's guards not called Cornwall's men.
Excluded: Milton's "On behalf of Cornwall Kerosene & Tar..." (quote list of the Milton page, mission not named); the
Ecclesiastes source of the train motto (not on the wiki pages read); the Red Dead Online freight yard trap details
beyond the Etta Doyle page; the "Easter eggs" claim about 1911 Blackwater newspapers (no in-game text found).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The Red Dead Wiki lists three missions of Red Dead Redemption 2 for Cornwall; he appears in person in two of them, and only in portraits in the chapter 1 train robbery. The French edition adds \"The Gilded Cage\", in which he is heard of only through a telephone call. Many other missions mention him, or set the gang against his companies, guards and agents; they are listed in the second table.",
              "Le Red Dead Wiki recense trois missions de Red Dead Redemption 2 pour Cornwall ; il apparaît en personne dans deux d'entre elles, et seulement sur des portraits lors de l'attaque du train du chapitre 1. L'édition française ajoute \"The Gilded Cage\", où il ne se manifeste que par un appel téléphonique. De nombreuses autres missions le mentionnent ou opposent la bande à ses compagnies, à ses gardes et à ses agents ; elles figurent dans le second tableau.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Cornwall's role", "Rôle de Cornwall")], "rows": [
        M("Who the Hell is Leviticus Cornwall?", C1,
          "The gang robs his private train and takes his railroad bonds. He is seen only in the portraits hanging in his car.",
          "La bande dévalise son train privé et lui prend ses obligations ferroviaires. On ne le voit que sur les portraits accrochés dans sa voiture."),
        M("The Sheep and the Goats", C2,
          "His guards take [[john-marston|John]] and [[leopold-strauss|Strauss]] hostage outside Keane's Saloon in Valentine; he calls for [[dutch-van-der-linde|Dutch]], then leaves before the shooting.",
          "Ses gardes prennent [[john-marston|John]] et [[leopold-strauss|Strauss]] en otages devant le Keane's Saloon, à Valentine ; il somme [[dutch-van-der-linde|Dutch]] de sortir, puis s'en va avant la fusillade."),
        M("Just a Social Call", C6,
          "Scolds Agents [[andrew-milton|Milton]] and [[edgar-ross|Ross]] on the Annesburg docks, refuses Dutch's terms and is shot dead by him.",
          "Sermonne les agents [[andrew-milton|Milton]] et [[edgar-ross|Ross]] sur les quais d'Annesburg, refuse les conditions de Dutch et tombe sous ses balles."),
    ]}},
    {"h4": two("Missions in which he is mentioned or his businesses are involved", "Missions où il est évoqué ou où ses affaires sont en jeu")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Cornwall", "Lien avec Cornwall")], "rows": [
        M("Old Friends", C1,
          "Dutch reads the O'Driscolls' plan for a train belonging to Cornwall, found on a body by [[micah-bell|Micah]].",
          "Dutch lit le plan des O'Driscoll concernant un train de Cornwall, trouvé sur un corps par [[micah-bell|Micah]]."),
        M("Eastward Bound", C1,
          "[[hosea-matthews|Hosea]] reminds Dutch that the gang has just robbed a Cornwall train.",
          "[[hosea-matthews|Hosea]] rappelle à Dutch que la bande vient de dévaliser un train de Cornwall."),
        M("Exit, Pursued by a Bruised Ego", C2,
          "Hosea tells [[arthur-morgan|Arthur]] that the Cornwall bonds are still very hot and that he has a couple of leads.",
          "Hosea confie à [[arthur-morgan|Arthur]] que les titres de Cornwall sont encore brûlants et qu'il a deux ou trois pistes."),
        M("A Fisher of Men", C2,
          "Milton tells Arthur that a man matching Dutch's description robbed Cornwall's train near Granite Pass.",
          "Milton apprend à Arthur qu'un homme correspondant au signalement de Dutch a dévalisé le train de Cornwall près de Granite Pass."),
        M("Pouring Forth Oil II", C2,
          "Arthur steals an oil wagon from the Cornwall Kerosene & Tar refinery.",
          "Arthur vole un chariot de pétrole à la raffinerie de Cornwall Kerosene & Tar."),
        M("The New South", C3,
          "Hosea, Arthur and Dutch talk over the Valentine ambush and the Pinkertons.",
          "Hosea, Arthur et Dutch reparlent de l'embuscade de Valentine et des Pinkerton."),
        M("Blessed are the Peacemakers", C3,
          "Micah names Cornwall among the enemies the gang cannot fight all at once.",
          "Micah range Cornwall parmi les ennemis que la bande ne peut pas affronter tous à la fois."),
        M("An Honest Mistake", C3,
          "The wagon [[uncle|Uncle]] wanted to rob belongs to Cornwall Kerosene & Tar; Cornwall's guards chase the four robbers to a barn.",
          "Le chariot qu'[[uncle|Uncle]] voulait attaquer appartient à Cornwall Kerosene & Tar ; les gardes de Cornwall poursuivent les quatre voleurs jusqu'à une grange."),
        M("Sodom? Back to Gomorrah", C3,
          "On the ride to Valentine, Arthur and [[bill-williamson|Bill]] can discuss the danger Cornwall still poses.",
          "En route pour Valentine, Arthur et [[bill-williamson|Bill]] peuvent discuter de la menace que représente encore Cornwall."),
        M("The Gilded Cage", C4,
          "Cornwall telephones Mayor Lemieux during the party; Arthur steals the documents the mayor was to sign.",
          "Cornwall téléphone au maire Lemieux pendant la réception ; Arthur vole les documents que le maire devait signer."),
        M("American Fathers I and II", C4,
          "Arthur steals papers from the Cornwall Kerosene & Tar refinery for Rains Fall and Eagle Flies.",
          "Arthur vole des papiers à la raffinerie de Cornwall Kerosene & Tar pour Rains Fall et Eagle Flies."),
        M("Savagery Unleashed", C5,
          "According to the Red Dead Wiki, Arthur gives Cornwall's name as his own when Angel questions him.",
          "Selon le Red Dead Wiki, Arthur donne le nom de Cornwall pour le sien quand Angel l'interroge."),
        M("The Delights of Van Horn", C6,
          "Arthur and Bill steal the Annesburg dynamite revealed by the papers taken from Cornwall's secretary.",
          "Arthur et Bill volent la dynamite d'Annesburg révélée par les papiers pris au secrétaire de Cornwall."),
        M("My Last Boy", C6,
          "The Wapiti and the gang attack the Army at the Cornwall Kerosene & Tar refinery; Dutch takes the state bonds kept there.",
          "Les Wapiti et la bande attaquent l'armée à la raffinerie de Cornwall Kerosene & Tar ; Dutch s'empare des obligations d'État qui y sont conservées."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below, spoken about Cornwall by other characters, are given in the original English and checked against the Red Dead Wiki's transcripts of the missions named. Cornwall's own lines, and the lines about him quoted elsewhere on this page, are under Personality, Business empire and Biography.",
              "Les répliques ci-dessous, prononcées par d'autres personnages au sujet de Cornwall, sont citées dans leur version originale anglaise et vérifiées sur les transcriptions des missions indiquées publiées par le Red Dead Wiki. Les paroles de Cornwall lui-même, et les répliques à son sujet déjà citées ailleurs sur cette page, figurent dans les rubriques Personnalité, Un empire industriel et Biographie.")},
    {"quotes": [
        {"q": two("Damn, he's got an army! Who is this guy?", "Damn, he's got an army! Who is this guy?"),
         "src": two("Lenny, fighting Cornwall's train guards, Who the Hell is Leviticus Cornwall? (RDR2, chapter 1)",
                    "Lenny, face aux gardes du train de Cornwall, Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1). Traduction : « Bon sang, il a une armée ! C'est qui, ce type ? »")},
        {"q": two("We don't want to kill you... we just wanna rob your boss.", "We don't want to kill you... we just wanna rob your boss."),
         "src": two("Dutch, to the employees forced out of Cornwall's car, Who the Hell is Leviticus Cornwall? (RDR2, chapter 1)",
                    "Dutch, aux employés sortis de force de la voiture de Cornwall, Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1). Traduction : « On ne veut pas vous tuer... on veut juste voler votre patron. »")},
        {"q": two("That so? Because I heard... a guy fitting his description robbed a train... belonging to Leviticus Cornwall up near Granite Pass.",
                  "That so? Because I heard... a guy fitting his description robbed a train... belonging to Leviticus Cornwall up near Granite Pass."),
         "src": two("Agent Milton to Arthur, A Fisher of Men (RDR2, chapter 2)",
                    "L'agent Milton à Arthur, A Fisher of Men (RDR2, chapitre 2). Traduction : « Vraiment ? Parce qu'on m'a dit... qu'un type correspondant à son signalement avait dévalisé un train... appartenant à Leviticus Cornwall, du côté de Granite Pass. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("Whatever the place where the player actually stops Cornwall's train, the cutscene always shows it halted at Granite Pass, southwest of Window Rock.",
            "Quel que soit l'endroit où le joueur arrête vraiment le train de Cornwall, la cinématique le montre toujours immobilisé à Granite Pass, au sud-ouest de Window Rock."),
        two("The locomotive of Cornwall's private train, in Southern and Eastern Railway colors, is a model with a steel doghouse tender that appears in no other mission, according to the Red Dead Wiki.",
            "Selon le Red Dead Wiki, la locomotive du train privé de Cornwall, aux couleurs de la Southern and Eastern Railway, est un modèle à tender équipé d'une guérite en acier qu'on ne voit dans aucune autre mission."),
        two("The robbery appears twice on the Gang Savings page of Arthur's journal: a first entry with an X, the mark for jobs that brought in nothing, and a second one after Hosea sells the bonds.",
            "L'attaque du train figure deux fois à la page Gang Savings du journal d'Arthur : une première ligne marquée d'une croix, signe des coups qui n'ont rien rapporté, puis une seconde après la vente des obligations par Hosea."),
        two("The clerk at the Valentine train station may bring up the robbery of Cornwall's train.",
            "L'employé de la gare de Valentine peut évoquer l'attaque du train de Cornwall."),
        two("The article \"Train Robbed\" runs in Blackwater Ledger No. 62, New Hanover Gazette No. 27 and Saint Denis Times No. 43; \"Cornwall Murdered\" runs in Blackwater Ledger No. 70, New Hanover Gazette No. 35 and Saint Denis Times No. 51.",
            "L'article \"Train Robbed\" paraît dans le Blackwater Ledger n° 62, la New Hanover Gazette n° 27 et le Saint Denis Times n° 43 ; \"Cornwall Murdered\" paraît dans le Blackwater Ledger n° 70, la New Hanover Gazette n° 35 et le Saint Denis Times n° 51."),
        two("In \"The Sheep and the Goats\", if the player waits too long to shoot the hostage takers, Dutch loses patience and orders Arthur to fire, John and Strauss are killed and the mission fails.",
            "Dans \"The Sheep and the Goats\", si le joueur tarde trop à tirer sur les preneurs d'otages, Dutch perd patience et ordonne à Arthur de faire feu, John et Strauss sont tués et la mission échoue."),
        two("One of the gold medal objectives of \"Just a Social Call\" is to reach the escape horses within 2 minutes and 45 seconds of Cornwall's death.",
            "L'un des objectifs de la médaille d'or de \"Just a Social Call\" consiste à atteindre les chevaux de fuite moins de 2 minutes et 45 secondes après la mort de Cornwall."),
        two("Cornwall's cigarette card, \"Oil Tycoon\", belongs to the Prominent Americans set. According to the Red Dead Wiki's page on the set, it lies on an upturned barrel on the porch of a wooden house southwest of the show tent in Valentine.",
            "La carte de cigarettes de Cornwall, \"Oil Tycoon\", fait partie de la série Prominent Americans. D'après la page du Red Dead Wiki consacrée à la série, elle est posée sur un tonneau retourné, sous le porche d'une maison en bois au sud-ouest du chapiteau de Valentine."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Red Dead Online", "Red Dead Online")},
    {"p": two("Cornwall does not appear in Red Dead Online, but the Red Dead Wiki lists him as mentioned there. According to the French edition of the wiki, the legendary bounty hunter brings him up in the bounty on Etta Doyle, explaining that Cornwall pays bounty hunters to track her down. The mission itself starts at the Cornwall Co. freight yard in Saint Denis, where two armed guards tell the player that a trap has been set for her gang. His refinery is the target of \"Kerosene, Tar, and Greed\", a story mission for dishonorable players. Samson Finch sends the posse to rob industrialists meeting there. The players take over a train carrying Pinkertons to reach the refinery. Cornwall executives have shut themselves in an office upstairs. The Blood Money update, released on July 13, 2021, added a three-part mission sequence called \"The Cornwall Contract\".",
              "Cornwall n'apparaît pas dans Red Dead Online, mais le Red Dead Wiki le compte parmi les personnages mentionnés. Selon l'édition française du wiki, la chasseuse de primes légendaire parle de lui à propos de la prime sur Etta Doyle : c'est Cornwall qui paie les chasseurs de primes lancés à sa poursuite. La mission débute d'ailleurs à la gare de marchandises Cornwall Co. de Saint-Denis, où deux gardes armés préviennent le joueur qu'un piège a été tendu à sa bande. Sa raffinerie est la cible de \"Kerosene, Tar, and Greed\", une mission d'histoire réservée aux joueurs déshonorables. Samson Finch y envoie le groupe dévaliser des industriels réunis sur place. Les joueurs s'emparent d'un train qui transporte des Pinkerton pour atteindre la raffinerie. Des dirigeants de Cornwall se sont barricadés dans un bureau à l'étage. La mise à jour Blood Money, sortie le 13 juillet 2021, a ajouté une série de trois missions intitulée \"The Cornwall Contract\".")},
]
