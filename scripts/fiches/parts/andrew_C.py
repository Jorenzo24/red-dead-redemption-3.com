"""Andrew Milton, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, Red Dead Wiki EN fetched Oct 2026, saved in scratchpad cov/andrew/ and cov/andrew/m/):
- Character page "Andrew Milton" (Mission appearances: "A Fisher of Men", "The Battle of Shady Belle", "Banking, The
  Old American Art", "Fleeting Joy", "A Fork in the Road" (voice only), "Just a Social Call", "Red Dead Redemption";
  Quotes; Trivia). FR wiki page (same list, without "A Fork in the Road").
- Transcripts: "A Fisher of Men/dialogues", "The Battle of Shady Belle/dialogues", "Red Dead Redemption
  (mission)/dialogues": every line quoted below from these missions is checked word for word against them.
- The two "Fleeting Joy" lines have no transcript on the wiki: they are taken verbatim from the quote list of the
  character page and labeled as such.
- Mission pages: "A Fisher of Men" (trivia: the invisible horses), "The Battle of Shady Belle" (subtitle typo
  "Mathews"), "A Fork in the Road" (low-honor memories: "You will die... savagely... all of you!" and "Who made you
  the messiah to these lost souls?"), "Red Dead Redemption (mission)" (trivia: the grapple prompt, Milton's loot and
  hat), "Who the Hell is Leviticus Cornwall?", "Our Best Selves".
Chapters: "Fleeting Joy" and "A Fork in the Road" are chapter 5 missions (infobox of both pages); "The Battle of Shady
Belle" is chapter 3.
Ownership: events stay in part A (one line per mission here); names, weapons (the Cattleman at Hosea's execution),
appearance and the "Dear Uncle Tacitus" remark go to part B; the name first appearing in the 1907 article and the
ending credits is a names fact (part B); John Hickok and marketing to part D.
Excluded: the Steve Haines comparison and the name etymology (analysis, not about the game); the A Fisher of Men trivia
reading the scene as foreshadowing (interpretation); "Arthur explicitly tells few characters about his tuberculosis"
(ranking with no source list); the "Murders committed" list (both killings are in part A).
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
    {"p": two("The Red Dead Wiki lists seven story missions in which he appears or is heard, from chapter 2 to chapter 6. The French edition of the wiki gives the same list without \"A Fork in the Road\". Two other missions are linked to him without showing him; they are listed in the second table.",
              "Le Red Dead Wiki recense sept missions de l'histoire où on le voit ou l'entend, du chapitre 2 au chapitre 6. L'édition française du wiki donne la même liste, sans \"A Fork in the Road\". Deux autres missions sont liées à lui sans qu'il y apparaisse ; elles figurent dans le second tableau.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Milton's role", "Rôle de Milton")], "rows": [
        M("A Fisher of Men", C2,
          "Confronts [[arthur-morgan|Arthur]] and [[jack-marston|Jack]] by the Dakota River with [[edgar-ross|Ross]], offers Arthur his life for Dutch and describes the death of Mac Callander.",
          "Aborde [[arthur-morgan|Arthur]] et [[jack-marston|Jack]] au bord de la Dakota River avec [[edgar-ross|Ross]], propose à Arthur la vie sauve contre Dutch et raconte la mort de Mac Callander."),
        M("The Battle of Shady Belle", C3,
          "Walks into the Clemens Point camp with Ross and offers the others three days to disappear if [[dutch-van-der-linde|Dutch]] comes with him.",
          "Entre dans le camp de Clemens Point avec Ross et offre aux autres trois jours pour disparaître si [[dutch-van-der-linde|Dutch]] le suit."),
        M("Banking, The Old American Art", C4,
          "Captures [[hosea-matthews|Hosea]] during the diversion and shoots him outside the Lemoyne National Bank.",
          "Capture [[hosea-matthews|Hosea]] pendant la diversion et l'abat devant la Lemoyne National Bank."),
        M("Fleeting Joy", C5,
          "Leads the Pinkerton attack on the gang's camp at Lakay.",
          "Dirige l'attaque des Pinkerton contre le camp de la bande à Lakay."),
        M("A Fork in the Road", C5,
          "Voice only: with low honor, Arthur remembers two of Milton's lines after his tuberculosis diagnosis, one from \"A Fisher of Men\", given on the wiki's mission page as \"You will die... savagely... all of you!\", and one from \"The Battle of Shady Belle\".",
          "Voix seulement : avec un honneur bas, Arthur se souvient de deux répliques de Milton après le diagnostic de sa tuberculose, l'une tirée de \"A Fisher of Men\", que la page de la mission sur le wiki cite sous la forme \"You will die... savagely... all of you!\" (vous mourrez... dans la sauvagerie... tous autant que vous êtes !), l'autre de \"The Battle of Shady Belle\"."),
        M("Just a Social Call", C6,
          "Steps off [[leviticus-cornwall|Cornwall]]'s yacht at Annesburg with Ross and is berated by Cornwall, shortly before Dutch kills Cornwall.",
          "Descend du yacht de [[leviticus-cornwall|Cornwall]] à Annesburg avec Ross et se fait réprimander par Cornwall, peu avant que Dutch n'abatte ce dernier."),
        M("Red Dead Redemption", C6,
          "Holds [[abigail-marston|Abigail]] at Van Horn, names [[micah-bell|Micah]] as the informant to Arthur and is shot dead by Abigail.",
          "Retient [[abigail-marston|Abigail]] à Van Horn, désigne [[micah-bell|Micah]] comme le mouchard devant Arthur et est abattu par Abigail."),
    ]}},
    {"h4": two("Missions linked to him", "Missions liées à lui")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Milton", "Lien avec Milton")], "rows": [
        M("Who the Hell is Leviticus Cornwall?", C1,
          "The gang robs Cornwall's train near Granite Pass, the robbery Milton later brings up with Arthur.",
          "La bande attaque le train de Cornwall près de Granite Pass, le braquage que Milton évoque ensuite devant Arthur."),
        M("Our Best Selves", C6,
          "While the gang robs an army payroll train, Milton's men seize Abigail outside the Beaver Hollow camp (off screen).",
          "Pendant que la bande attaque un train de la solde de l'armée, les hommes de Milton enlèvent Abigail devant le camp de Beaver Hollow (hors champ)."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Those from \"A Fisher of Men\", \"The Battle of Shady Belle\" and \"Red Dead Redemption\" are checked against the Red Dead Wiki's transcripts of these missions. The wiki has no transcript of \"Fleeting Joy\": the two lines from that mission are taken from the quote list of its page on Milton.",
              "Les répliques ci-dessous sont citées en anglais, dans leur version originale. Celles de \"A Fisher of Men\", \"The Battle of Shady Belle\" et \"Red Dead Redemption\" sont vérifiées sur les transcriptions de ces missions publiées par le Red Dead Wiki. Le wiki ne propose pas de transcription de \"Fleeting Joy\" : les deux répliques tirées de cette mission proviennent de la liste de citations de sa page consacrée à Milton.")},
    {"quotes": [
        {"q": two("You're a wanted man, Mr. Morgan. There's five thousand dollars for your head alone.", "You're a wanted man, Mr. Morgan. There's five thousand dollars for your head alone."),
         "src": two("A Fisher of Men (RDR2, chapter 2), to Arthur by the Dakota River",
                    "A Fisher of Men (RDR2, chapitre 2), à Arthur au bord de la Dakota River. Traduction : « Vous êtes recherché, monsieur Morgan. Votre tête vaut cinq mille dollars à elle seule. »")},
        {"q": two("Listen... this is my offer, Mr. Morgan... bring in Van der Linde... and you have my word, you won't swing.", "Listen... this is my offer, Mr. Morgan... bring in Van der Linde... and you have my word, you won't swing."),
         "src": two("A Fisher of Men (RDR2, chapter 2), to Arthur",
                    "A Fisher of Men (RDR2, chapitre 2), à Arthur. Traduction : « Écoutez... voici mon offre, monsieur Morgan... livrez-nous Van der Linde... et vous avez ma parole, vous ne serez pas pendu. »")},
        {"q": two("But I came to make a deal. It's time. You come with me, and I give the rest of ya three days to run off, disappear and go live like human beings someplace else.", "But I came to make a deal. It's time. You come with me, and I give the rest of ya three days to run off, disappear and go live like human beings someplace else."),
         "src": two("The Battle of Shady Belle (RDR2, chapter 3), to Dutch at Clemens Point",
                    "The Battle of Shady Belle (RDR2, chapitre 3), à Dutch, à Clemens Point. Traduction : « Mais je suis venu conclure un marché. Il est temps. Vous venez avec moi, et je laisse aux autres trois jours pour filer, disparaître et aller vivre comme des êtres humains ailleurs. »")},
        {"q": two("I'm afraid I can't. And when I return I'll be with fifty men. All of you will die. Run away from this place, you fools! Run!", "I'm afraid I can't. And when I return I'll be with fifty men. All of you will die. Run away from this place, you fools! Run!"),
         "src": two("The Battle of Shady Belle (RDR2, chapter 3), after Dutch asks him to stop following the gang",
                    "The Battle of Shady Belle (RDR2, chapitre 3), après que Dutch lui a demandé de cesser de suivre la bande. Traduction : « J'ai bien peur de ne pas pouvoir. Et quand je reviendrai, ce sera avec cinquante hommes. Vous mourrez tous. Fuyez d'ici, bande d'idiots ! Fuyez ! »")},
        {"q": two("This is Agent Milton with the Pinkerton Detective Agency. On behalf of Cornwall Kerosene & Tar... the United States Government... and the Commonwealth of West Elizabeth... we are here to arrest you. Come out with your hands up.", "This is Agent Milton with the Pinkerton Detective Agency. On behalf of Cornwall Kerosene & Tar... the United States Government... and the Commonwealth of West Elizabeth... we are here to arrest you. Come out with your hands up."),
         "src": two("Fleeting Joy (RDR2, chapter 5), to the gang at Lakay (Red Dead Wiki quote list)",
                    "Fleeting Joy (RDR2, chapitre 5), à la bande, à Lakay (liste de citations du Red Dead Wiki). Traduction : « Ici l'agent Milton, de la Pinkerton Detective Agency. Au nom de Cornwall Kerosene & Tar... du gouvernement des États-Unis... et du Commonwealth de West Elizabeth... nous sommes ici pour vous arrêter. Sortez les mains en l'air. »")},
        {"q": two("You fools weren't listening to me, were you? I showed mercy... You mistook it for weakness. Now I will show strength and you may mistake it for brutality. There is no escape for any of you. I shall hunt you to the ends of the earth and the end of time! I've killed your friends and I've enjoyed killing them... and now I'm gonna kill each and every one of you!", "You fools weren't listening to me, were you? I showed mercy... You mistook it for weakness. Now I will show strength and you may mistake it for brutality. There is no escape for any of you. I shall hunt you to the ends of the earth and the end of time! I've killed your friends and I've enjoyed killing them... and now I'm gonna kill each and every one of you!"),
         "src": two("Fleeting Joy (RDR2, chapter 5), after ordering his men to cease fire (Red Dead Wiki quote list)",
                    "Fleeting Joy (RDR2, chapitre 5), après avoir fait cesser le feu (liste de citations du Red Dead Wiki). Traduction : « Vous ne m'écoutiez pas, bande d'idiots, n'est-ce pas ? J'ai fait preuve de clémence... Vous l'avez prise pour de la faiblesse. Je vais maintenant faire preuve de force, et vous la prendrez peut-être pour de la brutalité. Aucun de vous ne m'échappera. Je vous traquerai jusqu'au bout du monde et jusqu'à la fin des temps ! J'ai tué vos amis et j'ai aimé les tuer... et maintenant, je vais vous tuer jusqu'au dernier ! »")},
        {"q": two("Molly O'Shea? We sweated her a couple of times... never talked a word, had to let her go. Micah Bell... we picked him up... when you boys came back from the Caribbean... and he's been a good boy ever since.", "Molly O'Shea? We sweated her a couple of times... never talked a word, had to let her go. Micah Bell... we picked him up... when you boys came back from the Caribbean... and he's been a good boy ever since."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), to Arthur at Van Horn, after Arthur asks whether he means Molly",
                    "Red Dead Redemption (RDR2, chapitre 6), à Arthur, à Van Horn, après qu'Arthur lui a demandé s'il parlait de Molly. Traduction : « Molly O'Shea ? On l'a cuisinée deux ou trois fois... elle n'a pas dit un mot, on a dû la relâcher. Micah Bell... on l'a ramassé... quand vous êtes revenus des Caraïbes... et il se tient bien sage depuis. »")},
        {"q": two("You're losing your strength, Mr. Morgan.", "You're losing your strength, Mr. Morgan."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), his last words, laughing as Arthur fails to turn his revolver against him",
                    "Red Dead Redemption (RDR2, chapitre 6), ses derniers mots, en riant, alors qu'Arthur n'arrive pas à retourner son revolver contre lui. Traduction : « Vous perdez vos forces, monsieur Morgan. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("In the opening scene of \"The Battle of Shady Belle\", the subtitles spell Hosea's surname \"Mathews\" when Milton greets him.",
            "Dans la scène d'ouverture de \"The Battle of Shady Belle\", les sous-titres écrivent le nom d'Hosea \"Mathews\" quand Milton le salue."),
        two("In \"A Fisher of Men\", Milton's and Ross's horses are present but invisible while Arthur and Jack are fishing. According to the mission page, the player can still search their saddlebags and be kicked by them.",
            "Dans \"A Fisher of Men\", les chevaux de Milton et de Ross sont présents mais invisibles pendant qu'Arthur et Jack pêchent. D'après la page de la mission, le joueur peut tout de même fouiller leurs sacoches et recevoir une ruade."),
        two("In the Van Horn cutscene of \"Red Dead Redemption\", pressing the on-screen grapple prompt changes nothing: Abigail always shoots Milton before he can fire.",
            "Dans la cinématique de Van Horn de \"Red Dead Redemption\", appuyer ou non sur la touche de lutte affichée à l'écran ne change rien : Abigail abat toujours Milton avant qu'il puisse tirer."),
        two("After that cutscene, Milton's body can be looted. It holds random items (a tonic, money, a watch or ammunition), never anything unique.",
            "Après cette cinématique, on peut fouiller le corps de Milton. Il contient des objets aléatoires (un tonique, de l'argent, une montre ou des munitions), jamais rien d'unique."),
        two("The player can also pick up Milton's hat and wear it, but the game takes it off Arthur's head shortly before the cutscene in which he puts on his own hat for his final ride.",
            "Le joueur peut aussi ramasser le chapeau de Milton et le porter, mais le jeu le retire de la tête d'Arthur peu avant la cinématique où celui-ci remet son propre chapeau pour sa dernière chevauchée."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("The Red Dead Wiki lists no appearance of Milton outside the story mode of Red Dead Redemption 2: he is absent from Red Dead Redemption (2010), set in 1911, and his character page names no role in Red Dead Online. Ross, his partner, carries the hunt on after his death: in 1911, as a Bureau of Investigation agent, he forces John Marston to hunt down the last members of the gang, and in 1914 Jack Marston kills him.",
              "Le Red Dead Wiki ne mentionne aucune apparition de Milton en dehors du mode histoire de Red Dead Redemption 2 : il est absent de Red Dead Redemption (2010), qui se déroule en 1911, et sa fiche ne lui attribue aucun rôle dans Red Dead Online. Ross, son coéquipier, poursuit la traque après sa mort : en 1911, devenu agent du Bureau of Investigation, il contraint John Marston à traquer les derniers membres de la bande, et en 1914 Jack Marston l'abat.")},
]
