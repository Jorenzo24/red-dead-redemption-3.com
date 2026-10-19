"""Sean MacGuire, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/sean/ and cov/sean/m/):
- Red Dead Wiki EN "Sean MacGuire" (Mission Appearances incl. Red Dead Online, Notable Murders, Quotes, Trivia,
  Gallery captions) and FR "Sean MacGuire" (fr.txt: Apparitions dans les missions, which adds "A Strange Kindness").
- Mission pages: Outlaws from the West; Enter, Pursued by a Memory; Old Friends; Americans at Rest; Exit, Pursued by
  a Bruised Ego; The First Shall Be Last; Who is Not Without Sin; Pouring Forth Oil IV; A Strange Kindness; The New
  South; The Fine Joys of Tobacco (quote box); A Short Walk in a Pretty Town (quote box, Deaths, Trivia); The Battle of
  Shady Belle; companion activities Social Calls With Mr. MacGuire and Coach Robbery (Sean MacGuire). Wiki pages Hamish,
  Ennis, Darragh MacGuire, Tanner's Reach, Guido Martelli and Blood Money (Sean is one of four Blood Money mission
  givers; Capitale is the Bronte family's system of exchange, per Rockstar's Newswire), Bushwhack, Destroy Supplies, Paid Killing, On The Hunt, Jailbreak, Early
  Execution, Horse Theft (Red Dead Online free roam missions, a section for Sean in each).
- Transcripts "/dialogues": Outlaws from the West; Old Friends; Americans at Rest; Exit, Pursued by a Bruised Ego;
  The First Shall Be Last; Who is Not Without Sin; Pouring Forth Oil IV; The New South; The Battle of Shady Belle.
  Every quote from these missions is checked word for word against them. Two lines come from missions with no
  transcript on the wiki: "rebel stock" (quote box of The Fine Joys of Tobacco) and "Now it don't feel right?" (quote
  box of A Short Walk in a Pretty Town). Fact-check 19 Oct 2026: the lines quoted under Personality / In his own words
  ("Takes an army...", "the joy's back...", "You're toast...", "I'm the future...", "blood in me veins...", "no politics
  was politics") are removed from Quotes; the "no politics" context (Social Calls, British politics) was unverified.
- Real world: Red Dead Online Blood Money update, released July 13, 2021 (MP1st patch notes and PlayStation LifeStyle,
  July 8, 2021); Red Dead Online set in 1898 (as in sadie_C and micah_C); Rockstar tweet "Sean Macguire" of September
  6, 2018, reproduced by The Hollywood Reporter on September 7, 2018 (../charles/fc/thr_descriptions.txt; the
  description itself is NOT quoted here, part B); composite of the 23 gang members (Wikipedia caption, m/wp_list.txt:
  front row "Swanson, Sean, Tilly").
Ownership (FIX_RULES), left to other parts: Origins (Donegal, Darragh MacGuire and the Imperialist of London scrap,
reform school, pocket watch), the burial, the grave's location, Arthur's journal entries and the sketch, the Hamish
knock-out option, the Lonnie's Shack hunter story (A); official descriptions, names and nicknames ("English", "King
Arthur", "Sulky, Angry, Scar Face", "Dead Eye MacGuire", "Irish Terrier"), illiteracy, appearance, missing teeth,
lack of a winter outfit, weapons (custom Cattleman, 1848 knife), horse Ennis as a mount, camp scenes (Karen, Kieran and
the Colm pronunciation, Lenny, Javier and vanity, Micah's "oily turd" and the hanging joke, Molly, Hosea and guard duty,
songs, the dead white rabbit with Jack, Charles's joke "Bill Williamson") (B); Michael Mellamphy, the replaced first
actor, the unused black duster and the second-trailer train robbery cast (D).
Quotes: each line in ONE place. Part A paraphrases every line below without quotation marks. Lines deliberately NOT
used here so that part B can quote them: "I can talk a dog off a meat wagon", "Compare me to that oily turd again...",
"the bigger the box, the smaller the gift", "an old trick me Da taught me", all camp lines.
Kills: the character page lists one notable murder, Hamish (determinant); the coach driver Laurence and co-driver
Harry are credited by the Coach Robbery page to "either Arthur or Sean", so they are listed as determinant.
Excluded: "Sean says the word 'fuck' more than any other member" (an unverified count); the Scottish "Mac" spelling note
(commentary); the knife "probably a gift from his father" (speculation); the "least you ain't got a hole in it" and white
rabbit "foreshadowing" readings (interpretation); the Social Calls "originally a main story mission" theory (the
wiki's supporting facts are kept, the conclusion is not); the "supplies don't magically appear" ledger "nod"
(interpretation); the Bible reading of the mission title (interpretation); Ike Skelding's presence at the camp
("possibly", per his own page).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]
K = lambda name, mission, en, fr: [name, mission, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists four story missions of Red Dead Redemption 2 for Sean, from his rescue to his death, plus two companion activities, and seven types of Red Dead Online free roam missions together with the Blood Money missions. The table below also includes the missions in which he is only talked about, which tell what the gang knows of him while he is missing and after his death.",
              "Le Red Dead Wiki anglais recense pour Sean quatre missions principales de Red Dead Redemption 2, de son sauvetage à sa mort, deux activités de compagnon, ainsi que sept types de missions en monde libre de Red Dead Online et les missions de Blood Money. Le tableau ci-dessous intègre aussi les missions où il n'est qu'évoqué : elles disent ce que la bande sait de lui pendant sa disparition et après sa mort.")},
    {"h4": two("Red Dead Redemption 2, story missions", "Red Dead Redemption 2, missions principales")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Sean's role", "Rôle de Sean")], "rows": [
        M("Outlaws from the West", C1,
          "Mentioned. [[dutch-van-der-linde|Dutch]] counts him among the missing after Blackwater, and tells [[micah-bell|Micah]] they do not know what became of him or of Mac Callander.",
          "Mentionné. [[dutch-van-der-linde|Dutch]] le range parmi les disparus de Blackwater et répond à [[micah-bell|Micah]] qu'on ignore ce que Mac Callander et lui sont devenus."),
        M("Enter, Pursued by a Memory", C1,
          "Mentioned. [[javier-escuella|Javier]] tells [[arthur-morgan|Arthur]] that nobody knows what happened to him on the ferry job.",
          "Mentionné. [[javier-escuella|Javier]] confie à [[arthur-morgan|Arthur]] que personne ne sait ce qui lui est arrivé lors du coup du ferry."),
        M("Old Friends", C1,
          "Mentioned. Dutch says he knows that John, Mac, Charles and Sean will all be back.",
          "Mentionné. Dutch se dit sûr que John, Mac, Charles et Sean reviendront tous."),
        M("Americans at Rest", C2,
          "Mentioned. [[josiah-trelawny|Trelawny]] reports that bounty hunters hold him in Blackwater and may move him.",
          "Mentionné. [[josiah-trelawny|Trelawny]] annonce que des chasseurs de primes le retiennent à Blackwater et pourraient le transférer."),
        M("Exit, Pursued by a Bruised Ego", C2,
          "Mentioned, in optional dialogue. Before the rescue, Arthur tells [[hosea-matthews|Hosea]] he must go and see about Sean; after it, Hosea notes how much Sean has enjoyed his return.",
          "Mentionné, dans un dialogue facultatif. Avant le sauvetage, Arthur dit à [[hosea-matthews|Hosea]] qu'il doit aller s'occuper de Sean ; après, Hosea remarque combien Sean a savouré son retour."),
        M("The First Shall Be Last", C2,
          "Rescued. Arthur, Javier, [[charles-smith|Charles]] and Trelawny follow Ike Skelding's men up the Upper Montana River and free him from a tree in their camp. The gang celebrates his return that night.",
          "Délivré. Arthur, Javier, [[charles-smith|Charles]] et Trelawny suivent les hommes d'Ike Skelding sur l'Upper Montana et le décrochent d'un arbre de leur camp. La bande fête son retour le soir même."),
        M("Who is Not Without Sin", C2,
          "At camp. He is one of the gang members who comment as Arthur carries a drunk [[orville-swanson|Reverend Swanson]] to his tent.",
          "Au camp. Il fait partie des membres de la bande qui commentent l'arrivée d'Arthur portant le [[orville-swanson|révérend Swanson]], ivre, jusqu'à sa tente."),
        M("Pouring Forth Oil IV", C2,
          "Invites himself onto the train robbery with Arthur, [[john-marston|John]] and Charles. He searches for the baggage car, is knocked down by a guard, keeps watch while Arthur loots it, and escapes with about 100 dollars.",
          "S'invite au braquage du train avec Arthur, [[john-marston|John]] et Charles. Il cherche le fourgon à bagages, se fait assommer par un garde, fait le guet pendant qu'Arthur le pille et repart avec une centaine de dollars."),
        M("A Strange Kindness", C2,
          "Listed by the French Red Dead Wiki only; the mission page does not mention him.",
          "Citée par le seul Red Dead Wiki français ; la page de la mission ne le mentionne pas."),
        M("The New South", C3,
          "Mentioned. Dutch says that the gang would not have got Sean back without Trelawny.",
          "Mentionné. Dutch reconnaît que, sans Trelawny, la bande n'aurait jamais récupéré Sean."),
        M("The Fine Joys of Tobacco", C3,
          "Plays cribbage at Braithwaite Manor, then drives the moonshine wagon into Caliga Hall with Arthur hidden in the back. He distracts the guard Hamish, douses the barn and finds the payroll during the escape.",
          "Joue au cribbage à Braithwaite Manor, puis conduit le chariot de gnôle jusqu'à Caliga Hall, Arthur caché à l'arrière. Il occupe le garde Hamish, arrose la grange et trouve la paie pendant la fuite."),
        M("A Short Walk in a Pretty Town", C3,
          "Killed. Walking down the main street of Rhodes with Arthur, [[bill-williamson|Bill]] and Micah, he is shot in the head by a sniper hired by the Grays. He does not appear in the story after this.",
          "Tué. Alors qu'il remonte la grand-rue de Rhodes avec Arthur, [[bill-williamson|Bill]] et Micah, il est abattu d'une balle dans la tête par un tireur embusqué payé par les Gray. Il n'apparaît plus dans l'histoire ensuite."),
        M("The Battle of Shady Belle", C3,
          "Mentioned. On the ride, John lists him among those the gang has lost; at the end, Dutch says that losing Sean has changed his outlook.",
          "Mentionné. En chemin, John le compte parmi ceux que la bande a perdus ; à la fin, Dutch confie que la perte de Sean a changé son regard."),
    ]}},
    {"h4": two("Red Dead Redemption 2: companion activities", "Red Dead Redemption 2 : activités de compagnon")},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Sean's role", "Rôle de Sean")], "rows": [
        M("Social Calls With Mr. MacGuire", C3,
          "Activity giver. He takes Arthur to Lonnie's Shack, in Scarlett Meadows, to rob a gang of drunk train robbers. Reward: 20.50 dollars.",
          "Donneur de l'activité. Il emmène Arthur à Lonnie's Shack, dans les Scarlett Meadows, pour dépouiller une bande de braqueurs de trains ivres. Gain : 20,50 dollars."),
        M("Coach Robbery (Sean MacGuire)", C3,
          "Activity giver. With [[mary-beth-gaskill|Mary-Beth]] as a decoy, he and Arthur rob a Boles Overland banking coach near Face Rock. Total take: 305 dollars, of which the player receives 55. Available after \"Friends in Very Low Places\", from noon, until \"Blessed are the Peacemakers\".",
          "Donneur de l'activité. Avec [[mary-beth-gaskill|Mary-Beth]] pour appât, Arthur et lui attaquent une diligence de banque de la Boles Overland près de Face Rock. Butin total : 305 dollars, dont 55 pour le joueur. Disponible après \"Friends in Very Low Places\", à partir de midi, et jusqu'à \"Blessed are the Peacemakers\"."),
    ]}},
    {"h3": two("Notable people Sean kills", "Personnages notables tués par Sean")},
    {"p": two("The Red Dead Wiki lists a single notable killing for Sean, the Gray guard Hamish, and marks it as determinant. The table adds the two coach men that the Coach Robbery page credits to either Arthur or Sean. The bounty hunters, train guards, lawmen and Gray gunmen killed in gunfights alongside Arthur are not listed one by one.",
              "Le Red Dead Wiki ne retient qu'une victime notable pour Sean, le garde des Gray Hamish, en précisant que l'issue dépend du joueur. Le tableau ajoute les deux hommes de la diligence que la page de \"Coach Robbery\" attribue à Arthur ou à Sean. Les chasseurs de primes, gardes du train, hommes de loi et hommes de main des Gray abattus aux côtés d'Arthur ne sont pas détaillés.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K(two("Hamish", "Hamish"), "The Fine Joys of Tobacco",
          "Determinant. The Caliga Hall guard who rides with Sean to the warehouse is killed silently by Sean or by Arthur, unless Arthur knocks him out with his pistol.",
          "Selon le joueur. Le garde de Caliga Hall qui accompagne Sean jusqu'à l'entrepôt est tué en silence par Sean ou par Arthur, à moins qu'Arthur ne l'assomme d'un coup de crosse."),
        K(two("Laurence, coach driver", "Laurence, cocher"), "Coach Robbery (Sean MacGuire)",
          "Determinant. Killed by Arthur or by Sean when they open fire on the escort.",
          "Selon le joueur. Tué par Arthur ou par Sean quand ils ouvrent le feu sur l'escorte."),
        K(two("Harry, co-driver", "Harry, aide-cocher"), "Coach Robbery (Sean MacGuire)",
          "Determinant. Killed by Arthur or by Sean in the same ambush.",
          "Selon le joueur. Tué par Arthur ou par Sean dans la même embuscade."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent.")},
    {"h4": two("The rescue", "Le sauvetage")},
    {"quotes": [
        {"q": two("You know... you're a lot less ugly from that other angle, Arthur.", "You know... you're a lot less ugly from that other angle, Arthur."),
         "src": two("The First Shall Be Last (RDR2, chapter 2), to Arthur, once cut down from the tree",
                    "The First Shall Be Last (RDR2, chapitre 2), à Arthur, une fois décroché de l'arbre. Traduction : « Tu sais... t'es beaucoup moins moche vu sous cet angle, Arthur. »")},
        {"q": two("Do I get a hug, Arthur? A warm embrace for a lost brother, now found?", "Do I get a hug, Arthur? A warm embrace for a lost brother, now found?"),
         "src": two("The First Shall Be Last (RDR2, chapter 2), to Arthur, who helps him to his feet",
                    "The First Shall Be Last (RDR2, chapitre 2), à Arthur, qui l'aide à se relever. Traduction : « J'ai droit à un câlin, Arthur ? Une chaleureuse accolade pour un frère perdu, enfin retrouvé ? »")},
        {"q": two("Look who it is. I missed that crazy bastard.", "Look who it is. I missed that crazy bastard."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), as Arthur carries a drunk Reverend Swanson through camp",
                    "Who is Not Without Sin (RDR2, chapitre 2), quand Arthur traverse le camp en portant le révérend Swanson, ivre. Traduction : « Regardez qui voilà. Il m'avait manqué, ce cinglé. »")},
    ]},
    {"h4": two("The train robbery", "Le braquage du train")},
    {"quotes": [
        {"q": two("Me and the big cheeses, love it. Can't wait to slit some bastard's throat.", "Me and the big cheeses, love it. Can't wait to slit some bastard's throat."),
         "src": two("Pouring Forth Oil IV (RDR2, chapter 2), climbing onto the wagon after John tells him he was not invited",
                    "Pouring Forth Oil IV (RDR2, chapitre 2), en montant dans le chariot après que John lui a rappelé qu'il n'était pas invité. Traduction : « Moi avec les gros bonnets, j'adore. J'ai hâte d'égorger un salaud. »")},
        {"q": two("It's do or die with you... I like it.", "It's do or die with you... I like it."),
         "src": two("Pouring Forth Oil IV (RDR2, chapter 2), to Arthur, who climbs onto the oil wagon to stop the train",
                    "Pouring Forth Oil IV (RDR2, chapitre 2), à Arthur, qui grimpe sur le chariot-citerne pour arrêter le train. Traduction : « Avec toi, c'est marche ou crève... Ça me plaît. »")},
        {"q": two("Are those tennis rackets in there? Posh bastards.", "Are those tennis rackets in there? Posh bastards."),
         "src": two("Pouring Forth Oil IV (RDR2, chapter 2), keeping watch while Arthur loots the baggage car",
                    "Pouring Forth Oil IV (RDR2, chapitre 2), en faisant le guet pendant qu'Arthur pille le fourgon à bagages. Traduction : « C'est des raquettes de tennis, là-dedans ? Sales richards. »")},
        {"q": two("Whoa! That was fun, boys, real fun! I can see why they call you professionals of the outfit.", "Whoa! That was fun, boys, real fun! I can see why they call you professionals of the outfit."),
         "src": two("Pouring Forth Oil IV (RDR2, chapter 2), after the escape from the lawmen",
                    "Pouring Forth Oil IV (RDR2, chapitre 2), une fois les hommes de loi semés. Traduction : « Ouh ! C'était drôle, les gars, vraiment drôle ! Je comprends pourquoi on dit que vous êtes les pros de la bande. »")},
    ]},
    {"h4": two("Clemens Point", "Clemens Point")},
    {"quotes": [
        {"q": two("I'm rebel stock, boy... I was born burning down manor houses.", "I'm rebel stock, boy... I was born burning down manor houses."),
         "src": two("The Fine Joys of Tobacco (RDR2, chapter 3), to Arthur, who answers: \"Well, burn quietly.\" (quote box of the mission page)",
                    "The Fine Joys of Tobacco (RDR2, chapitre 3), à Arthur, qui répond : \"Well, burn quietly.\" (citation en exergue de la page de la mission). Traduction : « Je suis de souche rebelle, mon gars... Je suis né en brûlant des manoirs. » (« Eh bien, brûle sans bruit. »)")},
        {"q": two("Now it don't feel right? I could'a told you that-", "Now it don't feel right? I could'a told you that-"),
         "src": two("A Short Walk in a Pretty Town (RDR2, chapter 3), his last words, cut short by the sniper's bullet (quote box of the mission page)",
                    "A Short Walk in a Pretty Town (RDR2, chapitre 3), ses derniers mots, interrompus par la balle du tireur embusqué (citation en exergue de la page de la mission). Traduction : « Maintenant, ça sent mauvais ? J'aurais pu vous le dire... »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("Sean is the first member of the gang whose death is shown on screen, if Davey Callander, who dies as soon as he is introduced, is set aside.",
            "Sean est le premier membre de la bande dont la mort est montrée à l'écran, si l'on met à part Davey Callander, qui meurt dès son apparition."),
        two("In \"The First Shall Be Last\", the cutscene in which Arthur frees Sean changes slightly depending on whether the player cuts the rope or shoots it. Shooting the rope is a gold medal objective.",
            "Dans \"The First Shall Be Last\", la cinématique où Arthur libère Sean varie légèrement selon que le joueur tranche la corde ou la coupe d'une balle. Tirer dans la corde fait partie des objectifs de la médaille d'or."),
        two("Micah misses the party for Sean's return: his own return mission, \"An American Pastoral Scene\", cannot unlock before it, even if Arthur has already freed him from Strawberry.",
            "Micah manque la fête du retour de Sean : la mission de son propre retour, \"An American Pastoral Scene\", ne peut pas se débloquer avant, même si Arthur l'a déjà tiré de la prison de Strawberry."),
        two("In the first cutscene of \"Pouring Forth Oil IV\", Sean reloads his Cattleman Revolver by swinging the cylinder out to the side, which that single-action design does not allow. It is the only time he reloads it this way; before and after the cutscene, he loads it through the gate.",
            "Dans la première cinématique de \"Pouring Forth Oil IV\", Sean recharge son Cattleman Revolver en basculant le barillet sur le côté, ce que ce modèle à simple action ne permet pas. C'est la seule fois qu'il le recharge ainsi : avant et après la cinématique, il le remplit par la portière de chargement."),
        two("If Arthur is the one who kills Hamish in \"The Fine Joys of Tobacco\", the following cutscene still shows the body outside with a knife wound, the outcome in which Sean kills him.",
            "Si c'est Arthur qui élimine Hamish dans \"The Fine Joys of Tobacco\", la cinématique suivante montre malgré tout le corps dehors, blessé au couteau, comme dans la version où Sean le tue."),
        two("According to the Red Dead Wiki, \"Social Calls With Mr. MacGuire\" is the only companion activity with its own title, apart from \"High and Low Finance\", and the only one with its own music. Sean is also the only character who gives two companion activities in the same chapter.",
            "D'après le Red Dead Wiki, \"Social Calls With Mr. MacGuire\" est la seule activité de compagnon à porter un titre propre, hormis \"High and Low Finance\", et la seule à avoir sa propre musique. Sean est aussi le seul personnage à proposer deux activités de compagnon dans le même chapitre."),
        two("In \"Social Calls With Mr. MacGuire\", the man standing outside Lonnie's Shack takes Arthur for Sean's father. If Arthur has already robbed the house on his own, he remarks that he had not realized this was the place Sean meant.",
            "Dans \"Social Calls With Mr. MacGuire\", l'homme posté devant Lonnie's Shack prend Arthur pour le père de Sean. Si Arthur a déjà cambriolé la maison seul, il remarque qu'il n'avait pas compris que Sean parlait de cet endroit."),
        two("In his \"Coach Robbery\", Sean asks to take the first shot and is annoyed if Arthur kills the first guards. A guard can take Mary-Beth hostage if the player is too slow.",
            "Lors de son \"Coach Robbery\", Sean demande à tirer le premier et s'agace si Arthur abat les premiers gardes. Un garde peut prendre Mary-Beth en otage si le joueur tarde trop."),
        two("At the start of \"A Short Walk in a Pretty Town\", Bill's and Micah's horses are tied up in Rhodes, but Sean's horse, Ennis, is not there. Ennis is not seen again.",
            "Au début de \"A Short Walk in a Pretty Town\", les chevaux de Bill et de Micah sont attachés à Rhodes, mais celui de Sean, Ennis, n'y est pas. On ne revoit plus Ennis ensuite."),
        two("The mission fails if the player kills Sean before his scripted death in \"A Short Walk in a Pretty Town\". A Double-Barreled Shotgun can be taken from his body.",
            "La mission échoue si le joueur tue Sean avant sa mort scénarisée dans \"A Short Walk in a Pretty Town\". On peut récupérer un fusil à double canon sur son corps."),
        two("His grave north of Clemens Point is one of those that count toward the Paying Respects trophy.",
            "Sa tombe, au nord de Clemens Point, fait partie de celles qui comptent pour le trophée Paying Respects."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Red Dead Online", "Red Dead Online")},
    {"p": two("Sean is one of four members of the Van der Linde gang who appear in Red Dead Online, set in 1898, a year before the story; the others are [[sadie-adler|Sadie Adler]], [[josiah-trelawny|Josiah Trelawny]] and Joe. He is a stranger who gives missions. The player first meets him in the cabin at Tanner's Reach, in the Tall Trees of West Elizabeth. He draws his revolver on the player, calms down, explains that he has been separated from his group, and gives a tip on a stagecoach passing nearby. In the animation of this first meeting he cocks the hammer of his revolver, but the hammer does not move.",
              "Sean fait partie des quatre membres de la bande Van der Linde présents dans Red Dead Online, qui se déroule en 1898, un an avant l'histoire ; les autres sont [[sadie-adler|Sadie Adler]], [[josiah-trelawny|Josiah Trelawny]] et Joe. Il y tient le rôle d'un inconnu qui confie des missions. Le joueur le rencontre d'abord dans la cabane de Tanner's Reach, dans les Tall Trees de West Elizabeth. Il le braque, se calme, explique qu'il a été séparé de son groupe et lui donne un tuyau sur une diligence qui passe non loin. Dans l'animation de cette première rencontre, il arme le chien de son revolver, mais le chien ne bouge pas.")},
    {"p": two("Afterwards he can be found in the cabin or at his camp near Quaker's Cove, southwest of Blackwater. He offers seven types of free roam missions: Bushwhack, Destroy Supplies, Paid Killing, On The Hunt, Jailbreak, Early Execution and Horse Theft. His jobs lower the player's honor. With the Blood Money update, released on July 13, 2021, he becomes one of the four strangers who give Blood Money missions, with Anthony Foreman, James Langton and Joe. In this update Guido Martelli, in Saint Denis, sends the player after Capitale, a means of exchange used by the Bronte family for its most discreet business.",
              "Il se trouve ensuite dans la cabane ou à son camp près de Quaker's Cove, au sud-ouest de Blackwater. Il propose sept types de missions en monde libre : Bushwhack, Destroy Supplies, Paid Killing, On The Hunt, Jailbreak, Early Execution et Horse Theft. Ses contrats font baisser l'honneur du joueur. Avec la mise à jour Blood Money, sortie le 13 juillet 2021, il devient l'un des quatre inconnus qui confient les missions Blood Money, avec Anthony Foreman, James Langton et Joe. Dans cette mise à jour, Guido Martelli, à Saint-Denis, lance le joueur à la recherche du Capitale, une monnaie d'échange réservée aux affaires les plus discrètes de la famille Bronte.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("On September 6, 2018, Rockstar posted Sean's portrait and character description on Twitter, under the spelling \"Sean Macguire\", in a series covering the members of the gang; The Hollywood Reporter reproduced the series the next day. Rockstar also released official artwork of him for Red Dead Redemption 2. In the composite image of the 23 gang members, Sean stands in the front row, between Swanson and [[tilly-jackson|Tilly]].",
              "Le 6 septembre 2018, Rockstar publie sur Twitter le portrait de Sean et sa description, sous l'orthographe \"Sean Macguire\", dans une série consacrée aux membres de la bande ; The Hollywood Reporter reprend la série le lendemain. Rockstar a aussi diffusé une illustration officielle du personnage pour Red Dead Redemption 2. Sur l'image qui réunit les 23 membres de la bande, Sean figure au premier rang, entre Swanson et [[tilly-jackson|Tilly]].")},
]
