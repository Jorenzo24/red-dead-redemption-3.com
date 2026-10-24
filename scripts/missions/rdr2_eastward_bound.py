"""Eastward Bound (RDR2, Chapter 1, mission 6, last of the chapter), mission page (24 Oct 2026).

Source register:
- Our v3 Chapter 1 guide, EN story/rdr2-chapter-1-colter/ and FR
  fr/histoire/rdr2-chapitre-1-colter/ (fixed 24 Oct 2026 after two adversarial
  fact-checks and a coverage check): section "6. Eastward Bound" (including the
  final scene after the "Chapter II: Horseshoe Overlook" title card), the
  matching row of "Chapter 1 at a glance" (giver, companions, location, Gold
  Medal objectives), "Background" (Hosea on the ferry job). Story wording and
  facts are taken from it; the FR text is taken from the FR guide.
- Red Dead Wiki mission page "Eastward Bound" (scripts/v3/work/_m/
  Eastward_Bound.txt): infobox (start Colter, end Horseshoe Overlook, giver
  Dutch, location the Heartlands, New Hanover, rewards, next missions), Gold
  Medal objectives, mission failure conditions, trivia (Lenny and Micah sent
  scouting west, absences and returns of Bill, Swanson, Charles and Javier,
  Uncle reserved for "Polite Society, Valentine Style", the girls' boredom,
  Strauss and Uncle without new dialogue, two-page journal entry), trophies
  (Back in the Mud, Gold Rush, Best in the West).
- Red Dead Wiki chapter list "Missions in Redemption 2" (scripts/v3/work/_m/
  Missions_in_Redemption_2.txt): "Who is Not Without Sin" is the first mission
  listed for Chapter 2, used as "next" (plain text, no page yet).
- Red Dead Wiki transcript "Eastward Bound/dialogues" (scripts/v3/work/_m/
  Eastward_Bound_dialogues.txt): every quoted line was checked against it,
  including the stage directions (Lake Isabella, the railroad bridge into Big
  Valley, Cumberland Falls), Charles's account of his family, "a long way from
  our dream of virgin land in the west", the full journal entry and Hosea's
  closing lines.
- The Rains Fall line in Saint Denis comes from our guide and the Rains Fall
  fiche (scripts/fiches/parts/rains_*.py).

Left out: the "Homeward Bound" (Simon & Garfunkel) title reading (speculation),
the patch-dependent closed winter coat, the Photo Mode note on Kieran's place in
the wagons ("citation needed"), Micah's return point after "An American
Pastoral Scene" (not cross-checked), music titles, video links.
"""


def two(en, fr): return {"en": en, "fr": fr}


MISSION = {
    "slug": "eastward-bound",
    "name": "Eastward Bound",
    "game": "rdr2",
    "chapter": 1,
    "number": 6,
    "chapter_total": 6,
    "story_order": 6,
    "publishDate": "2026-10-24",
    "updated": "2026-10-24",
    "prev": {"slug": "who-the-hell-is-leviticus-cornwall", "name": "Who the Hell is Leviticus Cornwall?"},
    "next": {"slug": "who-is-not-without-sin", "name": "Who is Not Without Sin"},

    "meta_desc": two(
        "Eastward Bound, the last mission of Red Dead Redemption 2's Chapter 1: the wagon ride from Colter to Horseshoe Overlook, the riders on the cliff, Charles's story, rewards, Gold Medal objectives and quotes.",
        "Eastward Bound, dernière mission du chapitre 1 de Red Dead Redemption 2 : le convoi de Colter à Horseshoe Overlook, les cavaliers de la falaise, l'histoire de Charles, récompenses, médaille d'or et citations."),
    "og_desc": two(
        "The gang leaves the snow for Horseshoe Overlook, near Valentine: the last mission of Chapter 1, step by step.",
        "La bande quitte la neige pour Horseshoe Overlook, près de Valentine : la dernière mission du chapitre 1, étape par étape."),

    "facts": {
        "giver": two("[[dutch-van-der-linde|Dutch van der Linde]]", "[[dutch-van-der-linde|Dutch van der Linde]]"),
        "location": two("Starts at Colter; ends at Horseshoe Overlook, the Heartlands, New Hanover",
                        "Départ de Colter ; arrivée à Horseshoe Overlook, dans les Heartlands, en New Hanover"),
        "characters": two(
            "[[arthur-morgan|Arthur Morgan]], [[hosea-matthews|Hosea Matthews]], [[charles-smith|Charles Smith]], [[javier-escuella|Javier Escuella]], [[dutch-van-der-linde|Dutch van der Linde]], [[micah-bell|Micah Bell]], [[lenny-summers|Lenny Summers]], [[bill-williamson|Bill Williamson]], [[leopold-strauss|Leopold Strauss]], [[simon-pearson|Simon Pearson]], [[susan-grimshaw|Susan Grimshaw]] and the rest of the gang; three riders the Red Dead Wiki identifies as [[rains-fall|Rains Fall]], Eagle Flies and Paytah",
            "[[arthur-morgan|Arthur Morgan]], [[hosea-matthews|Hosea Matthews]], [[charles-smith|Charles Smith]], [[javier-escuella|Javier Escuella]], [[dutch-van-der-linde|Dutch van der Linde]], [[micah-bell|Micah Bell]], [[lenny-summers|Lenny Summers]], [[bill-williamson|Bill Williamson]], [[leopold-strauss|Leopold Strauss]], [[simon-pearson|Simon Pearson]], [[susan-grimshaw|Susan Grimshaw]] et le reste de la bande ; trois cavaliers que le Red Dead Wiki identifie comme [[rains-fall|Rains Fall]], Eagle Flies et Paytah"),
        "unlocks": two("Chapter 2; Horseshoe Overlook becomes the gang's camp, and the mission page lists \"Polite Society, Valentine Style\", \"Americans at Rest\" and \"Who is Not Without Sin\" as the next missions",
                       "Le chapitre 2 ; Horseshoe Overlook devient le camp de la bande, et la page de la mission indique comme suites \"Polite Society, Valentine Style\", \"Americans at Rest\" et \"Who is Not Without Sin\""),
        "rewards": two("Free roam; a camera; 5 ginseng and 5 yarrow; Volcanic Pistol, Varmint Rifle and Springfield Rifle at gunsmiths; \"Back in the Mud\" trophy for completing Chapter 1",
                       "Accès au monde libre ; un appareil photo ; 5 ginsengs et 5 achillées ; Volcanic Pistol, Varmint Rifle et Springfield Rifle chez les armuriers ; trophée \"Back in the Mud\" pour la fin du chapitre 1"),
    },

    "intro": [
        two("\"Eastward Bound\" is the sixth story mission of Red Dead Redemption 2 and the last of the six missions of <a href=\"/story/rdr2-chapter-1-colter/\">Chapter 1: Colter</a>. It is given by [[dutch-van-der-linde|Dutch van der Linde]], starts at Colter and ends at Horseshoe Overlook, in the Heartlands of New Hanover.",
            "\"Eastward Bound\" est la sixième mission principale de Red Dead Redemption 2 et la dernière des six missions du <a href=\"/fr/histoire/rdr2-chapitre-1-colter/\">chapitre 1 : Colter</a>. Donnée par [[dutch-van-der-linde|Dutch van der Linde]], elle part de Colter et s'achève à Horseshoe Overlook, dans les Heartlands, en New Hanover."),
        two("After the robbery of [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]], the gang leaves the snow by wagon. [[arthur-morgan|Arthur Morgan]] drives [[hosea-matthews|Hosea Matthews]], joined by [[charles-smith|Charles Smith]] after a broken wheel, to a new camp near Valentine. It ends with the title card of <a href=\"/story/rdr2-chapter-2-horseshoe-overlook/\">Chapter 2</a>.",
            "Après l'attaque de [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]], la bande quitte la neige en chariot. [[arthur-morgan|Arthur Morgan]] conduit [[hosea-matthews|Hosea Matthews]], rejoint par [[charles-smith|Charles Smith]] après une roue cassée, jusqu'à un nouveau camp près de Valentine. Elle se termine sur le carton du <a href=\"/fr/histoire/rdr2-chapitre-2-horseshoe-overlook/\">chapitre 2</a>."),
    ],

    "sections": {
        "story": [
            {"h3": two("Leaving Colter", "Le départ de Colter")},
            {"p": two("Arthur rides back from the train to find the camp loading the wagons. Dutch says the weather seems stable; Hosea reminds him they just robbed a Cornwall train. Dutch declares: \"the worst is behind us.\" Hosea proposes Horseshoe Overlook, near Valentine: \"We'll be able to hide out there no problem... as long as we keep our noses clean.\" Charles and [[abigail-marston|Abigail]] help [[john-marston|John]] into a wagon. Dutch puts Arthur and Hosea in the same wagon, saying the two like to talk about \"what's gone wrong with old Dutch.\"",
                      "De retour du train, Arthur trouve le camp en train de charger les chariots. Dutch juge le temps stable ; Hosea lui rappelle qu'ils viennent de dévaliser un train de Cornwall. Dutch assure que le pire est derrière eux. Hosea propose Horseshoe Overlook, près de Valentine : la bande pourra s'y cacher sans problème, à condition de ne pas faire de vagues. Charles et [[abigail-marston|Abigail]] aident [[john-marston|John]] à monter dans un chariot. Dutch place Arthur et Hosea dans le même chariot, puisque, dit-il, ils aiment parler du bon vieux temps et de ce qui ne tourne plus rond chez ce vieux Dutch.")},

            {"h3": two("Out of the snow", "La sortie de la neige")},
            {"p": two("According to the stage directions of the wiki's transcript, the convoy passes the frozen Lake Isabella and crosses a stream out of the snow. Dutch then sends [[micah-bell|Micah]] and [[lenny-summers|Lenny]] ahead to check the road. Micah complains about being paired with \"the boy\", then tells Lenny he can buy him a whisky.",
                      "D'après les didascalies de la transcription du wiki, le convoi longe le lac Isabella gelé et franchit un cours d'eau qui le sort de la neige. Dutch envoie alors Micah et Lenny en éclaireurs. [[micah-bell|Micah]] rechigne à faire équipe avec \"the boy\" (le gamin), puis dit à [[lenny-summers|Lenny]] qu'il peut lui payer un whisky.")},
            {"p": two("The convoy later goes under a railroad bridge into Big Valley, in West Elizabeth, and rides into the Dakota River next to Cumberland Falls, on the border with New Hanover, according to the same stage directions.",
                      "Le convoi passe ensuite sous un grand pont de chemin de fer, entre dans Big Valley, en West Elizabeth, et s'engage dans la Dakota à côté des Cumberland Falls, à la frontière du New Hanover, toujours selon ces didascalies.")},

            {"h3": two("The broken wheel", "La roue cassée")},
            {"p": two("Once the wagons are over the river, a wheel comes off Arthur and Hosea's wagon. The wagon ahead, carrying [[bill-williamson|Bill]] and Charles, with [[javier-escuella|Javier]] riding alongside, stops. Hosea turns down Javier's help; Charles stays behind, and he and Hosea hold the wagon up while Arthur puts the wheel back on.",
                      "Une fois la rivière franchie, une roue se détache du chariot d'Arthur et d'Hosea. Le chariot de devant, celui de [[bill-williamson|Bill]] et Charles, que [[javier-escuella|Javier]] escorte à cheval, s'arrête. Hosea décline l'aide de Javier ; Charles reste, et lui et Hosea soulèvent le chariot pendant qu'Arthur remet la roue.")},

            {"h3": two("The riders on the cliff", "Les cavaliers de la falaise")},
            {"p": two("Three riders watch them from a cliff. Charles says: \"If they wanted trouble... we wouldn't have seen them.\" Hosea says: \"Poor bastards... we really screwed them over down here.\" The Red Dead Wiki identifies the riders as [[rains-fall|Rains Fall]], Eagle Flies and Paytah, of the Wapiti tribe. Later in the game, in Saint Denis, Rains Fall tells Arthur: \"We saw you on the wagon train... crossing the river at Cumberland Falls.\"",
                      "Trois cavaliers les observent du haut d'une falaise. Charles remarque : \"If they wanted trouble... we wouldn't have seen them.\" (S'ils cherchaient des ennuis... on ne les aurait pas vus.) Hosea soupire : \"Poor bastards... we really screwed them over down here.\" (Les pauvres... on les a vraiment roulés, par ici.) Le Red Dead Wiki identifie les cavaliers comme [[rains-fall|Rains Fall]], Eagle Flies et Paytah, de la tribu wapiti. Plus tard dans le jeu, à Saint-Denis, Rains Fall dira à Arthur : \"We saw you on the wagon train... crossing the river at Cumberland Falls.\" (On vous a vus avec le convoi, quand vous traversiez la rivière aux Cumberland Falls.)")},

            {"h3": two("Charles's story", "L'histoire de Charles")},
            {"p": two("Charles rides on in their wagon. Hosea explains that the native people of the Heartlands lost the land and were killed or moved to reservations, and that he heard the Army there was particularly harsh. Charles asks: \"How do you rob and kill people pleasantly? We don't, in spite of Dutch's talk.\" Hosea says he was simplifying \"for the benefit of our blockheaded driver\"; Arthur answers that Hosea is \"a conman, Charles, born and bred.\"",
                      "Charles finit le trajet dans leur chariot. Hosea raconte que les peuples autochtones des Heartlands ont perdu leurs terres, ont été tués ou parqués dans des réserves, et qu'il a entendu dire que l'armée s'y était montrée particulièrement brutale. Charles réplique : \"How do you rob and kill people pleasantly? We don't, in spite of Dutch's talk.\" (Comment on vole et on tue les gens gentiment ? Nous non plus, on ne le fait pas, quoi qu'en dise Dutch.) Hosea admet avoir simplifié pour leur cocher à la tête dure ; Arthur prévient Charles qu'Hosea est un escroc de naissance.")},
            {"p": two("Arthur asks Charles about his tribe. Charles says he does not know if he has one. His father was a Black man who lived with his mother's people for a while; when they were forced off their lands, the three fled. Soldiers later took his mother, and they never saw her again. His father drank, and at around thirteen Charles struck out on his own. Hosea says it was about the age they found Arthur: \"A wilder delinquent you never did see. But he learned fast.\" Arthur answers: \"Not as fast as Marston, apparently.\" When Charles asks what the problem is between the two, Arthur says: \"It's a long story.\"",
                      "Arthur interroge Charles sur sa tribu. Charles ne sait pas s'il en a une. Son père était un Noir qui a vécu un temps chez le peuple de sa mère ; chassés de leurs terres, tous les trois ont fui. Des soldats ont plus tard emmené sa mère, qu'ils n'ont jamais revue. Son père buvait, et vers treize ans, Charles est parti seul. Hosea note que c'est à peu près l'âge qu'avait Arthur quand ils l'ont trouvé : \"A wilder delinquent you never did see. But he learned fast.\" (On n'a jamais vu de petit voyou plus sauvage. Mais il apprenait vite.) Arthur réplique : \"Not as fast as Marston, apparently.\" (Moins vite que Marston, apparemment.) Quand Charles demande ce qui ne va pas entre les deux, Arthur répond que c'est une longue histoire.")},

            {"h3": two("Valentine and Dutch", "Valentine et Dutch")},
            {"p": two("Hosea describes Valentine as a livestock town of \"Cowboys, outlaws, working girls.\" He says there are probably O'Driscolls there too, and hopes there are no Pinkertons. He asks Arthur: \"how low do you think Dutch is really going to lie?\" He adds that it \"isn't like Dutch to lose his head like that.\" Arthur answers that things go wrong sometimes and that the three of them must have got it right far more often than wrong. Hosea gives Arthur yarrow and ginseng he has been preparing. At the entrance to the site, Javier waits by a rock, shows them the track and jumps onto the back of the wagon.",
                      "Hosea présente Valentine comme une ville d'élevage peuplée de cow-boys, de hors-la-loi et de filles de joie. Il s'attend à y trouver aussi des O'Driscoll, et espère qu'il n'y aura pas de Pinkerton. Il demande à Arthur jusqu'où il croit vraiment que Dutch va se faire discret. Il ajoute que ce n'est pas le genre de Dutch de perdre la tête ainsi. Arthur répond que les choses tournent mal parfois, et que s'ils sont encore là tous les trois, c'est qu'ils ont eu raison bien plus souvent que tort. Hosea lui donne l'achillée et le ginseng qu'il préparait. À l'entrée du site, Javier attend près d'un rocher, leur indique la piste et grimpe à l'arrière du chariot.")},

            {"h3": two("Horseshoe Overlook", "Horseshoe Overlook")},
            {"p": two("At the new camp, Dutch says: \"Gentlemen, we have survived.\" He adds: \"Now it is time to prosper.\" Hosea answers: \"Arthur and I were about to prosper in Blackwater. We were on to something big... then Micah got you all excited about that ferry and here we are.\" Dutch answers that they have all made mistakes, but that he kept the gang together and \"kept the nooses off our neck.\" Hosea says he does not have long and wants people safe before he goes. He says they are now stuck \"east of the Grizzlies and out of money... and a long way from our dream of virgin land in the west.\"",
                      "Au nouveau camp, Dutch déclare : \"Gentlemen, we have survived.\" (Messieurs, nous avons survécu.) Il ajoute que l'heure est venue de prospérer. Hosea lui répond : \"Arthur and I were about to prosper in Blackwater. We were on to something big... then Micah got you all excited about that ferry and here we are.\" (Arthur et moi, on allait prospérer à Blackwater. On tenait un gros coup... et puis Micah t'a emballé avec ce ferry, et nous voilà.) Dutch répond qu'ils ont tous commis des erreurs, mais que lui a gardé la bande unie et lui a évité la corde. Hosea dit qu'il n'en a plus pour très longtemps et qu'il veut mettre tout le monde à l'abri avant de partir. Les voilà coincés, dit-il, à l'est des Grizzlies, sans le sou et bien loin de leur rêve de terres vierges dans l'Ouest.")},
            {"p": two("Dutch's plan is to make some money, go around the law, \"be west of Uncle Sam\" and buy land within a few months. [[leopold-strauss|Strauss]] leaves for the nearby town to \"strike up a little business.\" Dutch says: \"I prefer robbing banks to usury... seems more dignified somehow.\"",
                      "Le plan de Dutch : gagner un peu d'argent, contourner la loi, passer à l'ouest de l'Oncle Sam et acheter des terres d'ici quelques mois. [[leopold-strauss|Strauss]] part pour la ville voisine, histoire de \"strike up a little business\" (lancer quelques petites affaires). Dutch commente : \"I prefer robbing banks to usury... seems more dignified somehow.\" (Je préfère braquer des banques que pratiquer l'usure... ça me paraît plus digne.)")},
            {"p": two("Dutch gathers the gang. He tells them they are safe but \"far too poor\", and that everyone must get to work. Hosea tells them to stay out of trouble: \"Remember, we are itinerant workers.\" Dutch completes the cover story: \"Laid off when they shut down our factory to the north.\" He adds: \"[[uncle|Uncle]], Reverend [[orville-swanson|Swanson]]... no more passengers.\" Hosea points them to Valentine: \"All mud and morons if I remember right.\" [[simon-pearson|Pearson]] asks for real food every day, and Dutch sets out a box: \"the camp gets its slice.\" [[susan-grimshaw|Susan]] shows Arthur to his tent.",
                      "Dutch rassemble la bande. Ils sont en sécurité, dit-il, mais bien trop pauvres, et tout le monde doit se mettre au travail. Hosea leur recommande de se tenir à carreau : \"Remember, we are itinerant workers.\" (N'oubliez pas, nous sommes des travailleurs itinérants.) Dutch complète la couverture : ils ont été licenciés à la fermeture de leur usine, plus au nord. Il ajoute : \"Uncle, Reverend Swanson... no more passengers.\" (Uncle, révérend Swanson... fini les passagers clandestins.) Hosea leur indique Valentine, qui n'est, si ses souvenirs sont bons, que boue et abrutis. [[simon-pearson|Pearson]] réclame de la vraie nourriture chaque jour, et Dutch dépose une caisse : le camp aura sa part de tout ce que chacun rapportera. [[susan-grimshaw|Susan]] conduit Arthur à sa tente.")},

            {"h3": two("A couple of weeks later", "Quelques semaines plus tard")},
            {"p": two("The title card \"Chapter II: Horseshoe Overlook\" appears, followed by \"A couple of weeks later...\" Arthur writes in his journal: \"We got off the mountain and rode east into some pretty enough country called the Heartlands. Ain't been this far east in many a year. Dutch seems a little better.\" He adds that Dutch's eyes are \"sparkling once more\", that he seems to think a little clearer, and that they all feel a little happier in spite of Blackwater.",
                      "Le titre \"Chapter II: Horseshoe Overlook\" s'affiche, suivi de \"A couple of weeks later...\" (quelques semaines plus tard). Arthur écrit dans son journal : \"We got off the mountain and rode east into some pretty enough country called the Heartlands. Ain't been this far east in many a year. Dutch seems a little better.\" (On est descendus de la montagne et on a filé vers l'est, dans un assez joli coin qu'on appelle les Heartlands. Ça faisait des années que je n'étais pas venu si loin à l'est. Dutch a l'air d'aller un peu mieux.) Il ajoute que le regard de Dutch pétille de nouveau, qu'il semble avoir les idées un peu plus claires, et qu'ils se sentent tous un peu plus heureux malgré Blackwater.")},
            {"p": two("Hosea then brings Arthur a cup of a hot drink. He tells him that Bill, Charles and Javier are already in Valentine, that Swanson \"found something\" at the train station by the lake, and that Strauss came back with \"that creepy little smile on his face.\" Asked about his own plans, Hosea says: \"I'm gonna read a book.\" The mission ends there.",
                      "Hosea apporte ensuite à Arthur une tasse de boisson chaude. Il lui apprend que Bill, Charles et Javier sont déjà à Valentine, que Swanson a trouvé quelque chose à la gare près du lac, et que Strauss est rentré avec son petit sourire inquiétant. Quand Arthur lui demande ce qu'il compte faire, Hosea répond : \"I'm gonna read a book.\" (Je vais lire un livre.) La mission s'arrête là.")},
        ],

        "choices": [
            {"h3": two("After the mission: the camp at Horseshoe Overlook", "Après la mission : le camp d'Horseshoe Overlook")},
            {"p": two("According to the mission page:", "D'après la page de la mission :")},
            {"ul": [
                two("Lenny and Micah are at camp right after the mission. If the player saves and reloads, or Arthur leaves camp, they are gone, and Susan tells Arthur they have been sent scouting out west. Lenny does not return until \"A Quiet Time\".",
                    "Lenny et Micah sont au camp juste après la mission. Si le joueur sauvegarde puis recharge, ou si Arthur quitte le camp, ils ont disparu, et Susan lui explique qu'on les a envoyés en reconnaissance vers l'ouest. Lenny ne revient qu'avec \"A Quiet Time\"."),
                two("Swanson, Charles, Javier and Bill are missing from camp. Swanson returns during \"Who is Not Without Sin\", Charles and Javier after \"The First Shall Be Last\", Bill after \"Americans at Rest\".",
                    "Swanson, Charles, Javier et Bill sont absents du camp. Swanson revient pendant \"Who is Not Without Sin\", Charles et Javier après \"The First Shall Be Last\", Bill après \"Americans at Rest\"."),
                two("Uncle is asleep and can only be disturbed to start \"Polite Society, Valentine Style\". With Strauss, he is the only person at camp with no new dialogue after this mission.",
                    "Uncle dort et ne peut être dérangé que pour lancer \"Polite Society, Valentine Style\". Avec Strauss, c'est le seul membre du camp qui n'a aucun nouveau dialogue après cette mission."),
                two("Karen, Tilly and Mary-Beth may tell Arthur they are bored until \"Polite Society, Valentine Style\" is completed, and Hosea may tell Arthur to go and bother Uncle.",
                    "Karen, Tilly et Mary-Beth peuvent confier à Arthur qu'elles s'ennuient, jusqu'à ce que \"Polite Society, Valentine Style\" soit terminée, et Hosea peut l'envoyer embêter Uncle."),
            ]},

            {"h3": two("Mission failure", "Échec de la mission")},
            {"p": two("According to the mission page, the mission fails if the player:",
                      "D'après la page de la mission, la mission échoue si le joueur :")},
            {"ul": [
                two("assaults, kills or abandons Hosea or Charles, or Javier once he is picked up;",
                    "agresse, tue ou abandonne Hosea ou Charles, ou Javier une fois qu'il est monté ;"),
                two("leaves the route to Horseshoe Overlook;", "quitte la route d'Horseshoe Overlook ;"),
                two("destroys or abandons the wagon;", "détruit ou abandonne le chariot ;"),
                two("dies.", "meurt."),
            ]},
        ],

        "gold": {
            "objectives": [
                two("Pick up Javier when entering Horseshoe Overlook.", "Prendre Javier à l'entrée d'Horseshoe Overlook."),
                two("Complete within 6 minutes.", "Terminer en moins de 6 minutes."),
            ],
            "after": [
                {"p": two("According to the same page, the mission counts toward Gold Rush (70 Gold Medals in story missions) and Best in the West (100% completion).",
                          "Selon la même page, la mission compte pour les trophées Gold Rush (70 médailles d'or dans les missions principales) et Best in the West (100 % de complétion).")},
            ],
        },

        "quotes": [
            {"q": "So, we getting out of this hellhole?",
             "src": two("Arthur, back at Colter from the train", "Arthur, de retour du train à Colter"),
             "fr": "Alors, on quitte ce trou perdu ?"},
            {"q": "See... you ain't so useless after all.",
             "src": two("Arthur, to Hosea, once the wheel is back on", "Arthur, à Hosea, une fois la roue remise"),
             "fr": "Tu vois... t'es pas si inutile que ça."},
            {"q": "That depends... are we still heading west, in search of fortune and repose in virgin forests, as we planned? No.",
             "src": two("Hosea, when Arthur asks whether they are still heading the right way", "Hosea, quand Arthur demande s'ils vont toujours dans la bonne direction"),
             "fr": "Ça dépend... est-ce qu'on va toujours vers l'ouest, en quête de fortune et de repos dans des forêts vierges, comme prévu ? Non."},
            {"q": "Here we are, gentlemen. Home sweet home.",
             "src": two("Hosea, arriving at Horseshoe Overlook", "Hosea, à l'arrivée à Horseshoe Overlook"),
             "fr": "Nous y voilà, messieurs. Enfin chez nous."},
            {"q": "Would you just look around you. This world has its consolations.",
             "src": two("Dutch, to Hosea, at the new camp", "Dutch, à Hosea, au nouveau camp"),
             "fr": "Regarde un peu autour de toi. Ce monde a ses consolations."},
            {"q": "Everything apart from my money.",
             "src": two("Arthur, when Susan says most of his things from Blackwater were saved", "Arthur, quand Susan lui dit que la plupart de ses affaires de Blackwater ont été sauvées"),
             "fr": "Tout, sauf mon argent."},
            {"q": "Miss Jackson... I've seen shit with more common sense than you. Do it properly.",
             "src": two("Susan, to Tilly", "Susan, à Tilly"),
             "fr": "Mademoiselle Jackson... j'ai vu des bouses avec plus de jugeote que vous. Faites ça correctement."},
        ],

        "trivia": [
            two("Arthur writes a two-page journal entry after this mission, according to the mission page.",
                "Arthur rédige une entrée de journal de deux pages après cette mission, selon la page de la mission."),
        ],
    },
}
