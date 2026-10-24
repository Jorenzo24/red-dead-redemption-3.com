"""Who the Hell is Leviticus Cornwall? (RDR2, Chapter 1, mission 5), mission page (24 Oct 2026).

Source register:
- Our v3 Chapter 1 guide, EN story/rdr2-chapter-1-colter/ and FR
  fr/histoire/rdr2-chapitre-1-colter/ (fixed 24 Oct 2026 after two adversarial
  fact-checks and a coverage check): section "5. Who the Hell is Leviticus
  Cornwall?", the matching row of "Chapter 1 at a glance" (giver, companions,
  location, Gold Medal objectives), "Trivia" (Hosea's line on Arthur's last
  ride, Granite Pass cutscene, Micah's Carbine Repeater, "Train Robbed"
  newspapers, Valentine clerk, Gang Savings). Story wording and facts are taken
  from it; the FR text is taken from the FR guide.
- Red Dead Wiki mission page "Who the Hell is Leviticus Cornwall?" (scripts/v3/
  work/_m/Who_the_Hell_is_Leviticus_Cornwall.txt): infobox (start Colter, end
  Granite Pass, giver John Marston / Dutch van der Linde, location Grizzlies
  West, reward Dynamite, previous and next missions), Gold Medal objectives,
  mission failure conditions, deaths, newspaper aftermath, missable items,
  trivia (dynamite bundle explodes when shot, journal entries, clerk, Granite
  Pass, Sawed-Off replaced by the Cattleman, Micah's Carbine Repeater, Charles
  and Bill with double-barreled shotguns, Lenny climbing up alone, engineer
  attacking Lenny, employees running away).
- Red Dead Wiki transcript "Who the Hell is Leviticus Cornwall?/dialogues"
  (scripts/v3/work/_m/Who_the_Hell_is_Leviticus_Cornwall_dialogues.txt): every
  quoted line was checked against it, including the opening scene with Swanson
  ("Mind away, Reverend"), "Of course I do, but... look at you", "a raised spot
  there that should give us good vantage", "You sure you're ready for this,
  kid?", "Least we all know you can read" and Dutch's last lines.

Left out: the wiki "Consequences" line that the robbery leads to Milton and Ross
being assigned to the gang ("not shown directly"; house rule: Cornwall's hiring
of the Pinkertons is never shown), the comparisons with Butch Cassidy and the
Sundance Kid and The Great Train Robbery (interpretation), the "oversight" note
on the shotguns' reloads, the hard-to-hear conversation with the employees, the
claim that the mission may be impossible to fail by not stopping the train, the
failure condition "fails to save Lenny from falling" (contradicted by the same
page's trivia and by our guide: Lenny climbs up alone), music titles, Gold Medal
tips, video links.
"""


def two(en, fr): return {"en": en, "fr": fr}


MISSION = {
    "slug": "who-the-hell-is-leviticus-cornwall",
    "name": "Who the Hell is Leviticus Cornwall?",
    "game": "rdr2",
    "chapter": 1,
    "number": 5,
    "chapter_total": 6,
    "story_order": 5,
    "publishDate": "2026-10-24",
    "updated": "2026-10-24",
    "prev": {"slug": "old-friends", "name": "Old Friends"},
    "next": {"slug": "eastward-bound", "name": "Eastward Bound"},

    "meta_desc": two(
        "Who the Hell is Leviticus Cornwall?, the train robbery of Red Dead Redemption 2's Chapter 1: Hosea's objection, the failed detonator, the bearer bonds, the employees' fate, Gold Medal objectives and quotes.",
        "Who the Hell is Leviticus Cornwall?, l'attaque du train du chapitre 1 de Red Dead Redemption 2 : l'objection d'Hosea, le détonateur raté, les titres au porteur, le sort des employés, médaille d'or et citations."),
    "og_desc": two(
        "The robbery of Leviticus Cornwall's train in the Grizzlies, step by step.",
        "L'attaque du train de Leviticus Cornwall dans les Grizzlies, étape par étape."),

    "facts": {
        "giver": two("[[john-marston|John Marston]] and [[dutch-van-der-linde|Dutch van der Linde]], according to the mission page (it starts in John's cabin, where Dutch announces the job)",
                     "[[john-marston|John Marston]] et [[dutch-van-der-linde|Dutch van der Linde]], selon la page de la mission (elle commence dans la cabane de John, où Dutch annonce le coup)"),
        "location": two("Starts at Colter; Grizzlies West, Ambarino; ends at Granite Pass, according to the mission page",
                        "Départ de Colter ; Grizzlies West, Ambarino ; fin à Granite Pass, selon la page de la mission"),
        "characters": two(
            "[[arthur-morgan|Arthur Morgan]], [[dutch-van-der-linde|Dutch van der Linde]], [[micah-bell|Micah Bell]], [[bill-williamson|Bill Williamson]], [[charles-smith|Charles Smith]], [[javier-escuella|Javier Escuella]], [[lenny-summers|Lenny Summers]]; at camp, [[john-marston|John Marston]], [[orville-swanson|Orville Swanson]], [[abigail-marston|Abigail]], [[jack-marston|Jack]] and [[hosea-matthews|Hosea Matthews]]; [[leviticus-cornwall|Leviticus Cornwall]] named only",
            "[[arthur-morgan|Arthur Morgan]], [[dutch-van-der-linde|Dutch van der Linde]], [[micah-bell|Micah Bell]], [[bill-williamson|Bill Williamson]], [[charles-smith|Charles Smith]], [[javier-escuella|Javier Escuella]], [[lenny-summers|Lenny Summers]] ; au camp, [[john-marston|John Marston]], [[orville-swanson|Orville Swanson]], [[abigail-marston|Abigail]], [[jack-marston|Jack]] et [[hosea-matthews|Hosea Matthews]] ; [[leviticus-cornwall|Leviticus Cornwall]], seulement nommé"),
        "unlocks": two("[[m:eastward-bound|Eastward Bound]], which starts directly after this mission",
                       "[[m:eastward-bound|Eastward Bound]], qui s'enchaîne directement"),
        "rewards": two("Dynamite", "Dynamite"),
    },

    "intro": [
        two("\"Who the Hell is Leviticus Cornwall?\" is the fifth story mission of Red Dead Redemption 2 and the fifth of the six missions of <a href=\"/story/rdr2-chapter-1-colter/\">Chapter 1: Colter</a>. It starts in [[john-marston|John Marston]]'s cabin at Colter, where [[dutch-van-der-linde|Dutch van der Linde]] announces the job, takes place in the Grizzlies West and, according to the mission page, ends at Granite Pass.",
            "\"Who the Hell is Leviticus Cornwall?\" est la cinquième mission principale de Red Dead Redemption 2 et la cinquième des six missions du <a href=\"/fr/histoire/rdr2-chapitre-1-colter/\">chapitre 1 : Colter</a>. Elle commence dans la cabane de [[john-marston|John Marston]], à Colter, où [[dutch-van-der-linde|Dutch van der Linde]] annonce le coup, se déroule dans les Grizzlies West et, selon sa page, s'achève à Granite Pass."),
        two("Using the plans taken from the O'Driscolls in [[m:old-friends|Old Friends]], the gang robs a train belonging to [[leviticus-cornwall|Leviticus Cornwall]] despite [[hosea-matthews|Hosea]]'s objections, and takes railroad bonds. It follows Old Friends or [[m:the-aftermath-of-genesis|The Aftermath of Genesis]], whichever is played second.",
            "Grâce aux plans pris aux O'Driscoll dans [[m:old-friends|Old Friends]], la bande attaque un train de [[leviticus-cornwall|Leviticus Cornwall]] malgré les objections d'[[hosea-matthews|Hosea]] et emporte des obligations ferroviaires. Elle suit Old Friends ou [[m:the-aftermath-of-genesis|The Aftermath of Genesis]], selon celle des deux qui est jouée en second."),
    ],

    "sections": {
        "story": [
            {"h3": two("John's cabin", "La cabane de John")},
            {"p": two("John lies in bed with [[orville-swanson|Swanson]] beside him. Arthur needles the reverend, who tells him to show some respect; Arthur answers \"Mind away, Reverend\", and Swanson leaves. John tells Arthur: \"I owe you.\" Arthur answers: \"And you'll pay me... but for the moment, just rest.\" Dutch comes in and says it is time for the train. John asks to come; Dutch answers: \"Of course I do, but... look at you.\" John tries to get up: \"I was always ugly, Dutch... it's just a scratch.\" Dutch tells him to lie still. [[abigail-marston|Abigail]] brings [[jack-marston|Jack]] to see his father, and the couple trade insults in front of the boy.",
                      "John est alité, Swanson à son chevet. Arthur taquine le révérend, qui lui demande un peu de respect ; Arthur répond \"Mind away, Reverend\" (cause toujours, révérend), et Swanson sort. John dit à Arthur : \"I owe you.\" (Je te dois une fière chandelle.) Arthur répond : \"And you'll pay me... but for the moment, just rest.\" (Et tu me rembourseras... mais pour l'instant, repose-toi.) Dutch entre et annonce que c'est l'heure du train. John demande à venir ; Dutch répond qu'il aimerait bien, mais qu'il n'a qu'à se regarder. John tente de se lever : \"I was always ugly, Dutch... it's just a scratch.\" (J'ai toujours été moche, Dutch... c'est juste une égratignure.) Dutch lui ordonne de rester couché. [[abigail-marston|Abigail]] amène [[jack-marston|Jack]] voir son père, et le couple s'envoie des piques devant l'enfant.")},

            {"h3": two("Hosea's objection", "L'objection d'Hosea")},
            {"p": two("Outside, Dutch sends Bill ahead to set the charge \"at the water tower, just before the tunnel.\" Hosea objects: the weather is breaking, the gang could leave, and the plan was to lie low and head back west. He says: \"I just don't want any more folks to die, Dutch.\" Dutch answers that everything the gang owns is in Blackwater, and asks whether Hosea fancies heading back there.",
                      "Dehors, Dutch envoie Bill en avant poser la charge au château d'eau, juste avant le tunnel. Hosea s'y oppose : le temps se lève, la bande pourrait partir, et le plan était de se faire oublier puis de repartir vers l'ouest. Il lâche : \"I just don't want any more folks to die, Dutch.\" (Je ne veux plus voir personne mourir, Dutch.) Dutch répond que tout ce que possède la bande est resté à Blackwater, et demande à Hosea s'il a envie d'y retourner.")},
            {"p": two("Hosea warns that \"Leviticus Cornwall's no joke\"; when Arthur asks who that is, Hosea describes [[leviticus-cornwall|Cornwall]] as \"a big railway magnate, sugar dealer, oil man.\" Dutch answers that Cornwall \"has more than enough to share\" and tells the gang: \"Gentlemen, it is time to make something of ourselves. Get your horses ready, we have a train to rob.\"",
                      "Hosea prévient que Leviticus Cornwall n'est pas un plaisantin ; quand Arthur demande de qui il s'agit, Hosea décrit [[leviticus-cornwall|Cornwall]] comme \"a big railway magnate, sugar dealer, oil man\" (un gros magnat du rail, négociant en sucre et pétrolier). Dutch ironise : un homme pareil a largement de quoi partager. Puis il lance à la bande : \"Gentlemen, it is time to make something of ourselves. Get your horses ready, we have a train to rob.\" (Messieurs, il est temps de faire quelque chose de nos vies. Sellez vos chevaux, on a un train à braquer.)")},

            {"h3": two("The ride to the tracks", "La route de la voie ferrée")},
            {"p": two("Dutch rides out with Arthur, Micah, Charles, Javier and Lenny. He explains that, according to the O'Driscolls' plans, the train will come north from Big Valley and will be hit after it crosses into the Grizzlies, from \"a raised spot there that should give us good vantage.\" Charles is to watch for outriders. Dutch takes the driver and engineer, Lenny and Javier the two front cars, and Arthur and Micah the private car at the back.",
                      "Dutch part avec Arthur, Micah, Charles, Javier et Lenny. Il explique que, d'après les plans des O'Driscoll, le train remontera vers le nord depuis Big Valley et qu'on l'attaquera une fois entré dans les Grizzlies, depuis une hauteur qui offre une bonne vue. Charles surveillera d'éventuels cavaliers d'escorte. Dutch se réserve le mécanicien et le chauffeur, Lenny et Javier prendront les deux premières voitures, Arthur et Micah la voiture privée à l'arrière.")},
            {"p": two("As they leave the snow, Arthur says: \"Out of the snow, finally.\" Javier asks Lenny: \"You sure you're ready for this, kid?\" Micah keeps asking about going back to Blackwater for the money; Charles says it would be crazy with the town full of Pinkertons, and Dutch ends the discussion. Dutch says that if the O'Driscolls are right, there will be a stack of railroad bonds on the train.",
                      "En sortant de la neige, Arthur lâche : \"Out of the snow, finally.\" (Enfin sortis de la neige.) Javier demande à Lenny s'il est bien prêt, le gamin. Micah revient sans cesse sur l'argent laissé à Blackwater ; Charles répond qu'y retourner serait de la folie, la ville grouillant de Pinkerton, et Dutch clôt le débat. Si les O'Driscoll disent vrai, ajoute Dutch, il y aura une liasse d'obligations ferroviaires à bord.")},

            {"h3": two("The detonator", "Le détonateur")},
            {"p": two("At the ridge above the water tower, Dutch sends Arthur down to check on Bill. Bill has Arthur unspool the wire and set up the detonator by the rocks. Dutch tells the men to cover their faces, and they put on their bandanas. When the train passes, Bill pushes the plunger and nothing happens. Arthur asks Dutch: \"Where did you find that moron?\" Dutch answers: \"You said it was fine.\"",
                      "Depuis la crête au-dessus du château d'eau, Dutch envoie Arthur voir où en est Bill. Bill lui fait dérouler le fil et installer le détonateur près des rochers. Dutch ordonne à ses hommes de se masquer, et chacun remonte son bandana. Au passage du train, Bill enfonce la poignée et rien ne se passe. Arthur demande à Dutch : \"Where did you find that moron?\" (Où est-ce que tu as trouvé cet abruti ?) Dutch rétorque : \"You said it was fine.\" (Tu as dit que c'était bon.)")},

            {"h3": two("Boarding the train", "L'abordage")},
            {"p": two("Arthur, Javier and Lenny run to the far end of the tunnel and jump onto the train from above. Javier misses and is left behind; the mission page says he is hurt in the fall. Lenny ends up hanging from the side of a car (see Choices and variants).",
                      "Arthur, Javier et Lenny courent jusqu'au bout du tunnel et sautent sur le train par le haut. Javier rate son saut et reste en arrière ; la page de la mission précise qu'il se blesse en tombant. Lenny se retrouve suspendu au flanc d'une voiture (voir Choix et variantes).")},
            {"p": two("Inside the first car, Lenny kills a guard with his knife, and the gunfight along the train begins with the next guard (see Choices and variants). Lenny asks what Bill was doing; Arthur says he hooked up the wire himself, \"but we won't mention that.\"",
                      "Dans la première voiture, Lenny tue un garde au couteau, et la fusillade le long du train éclate avec le garde suivant (voir Choix et variantes). Lenny se demande ce que fabriquait Bill ; Arthur avoue avoir branché le fil lui-même, \"but we won't mention that\" (mais on n'en parlera pas).")},

            {"h3": two("Stopping the train", "L'arrêt du train")},
            {"p": two("Near the engine, the engineer comes out of the coal bin and hits Arthur with a shovel. Arthur overpowers the engineer, throws him off the train as it crosses a bridge and stops it. Guards pour out of the cars, and the rest of the gang rides in to help clear them.",
                      "Près de la locomotive, le mécanicien surgit du tender et frappe Arthur avec une pelle. Arthur maîtrise l'homme, le jette du train au passage d'un pont et arrête le convoi. Des gardes jaillissent des voitures, et le reste de la bande arrive à cheval pour les abattre.")},

            {"h3": two("The employees' car", "La voiture des employés")},
            {"p": two("Employees have locked themselves in the last car. One of them calls out: \"I work for Leviticus Cornwall.\" Dutch counts down from five, has the gang fire on the car, then sends Arthur and Charles to blow the door with Bill's dynamite. The employees come out with their hands up; Dutch tells them: \"We don't want to kill you... we just wanna rob your boss.\" He adds that next time, they should \"open the goddamn door\" when he says so. Cornwall himself is not on the train.",
                      "Des employés se sont barricadés dans la dernière voiture. L'un d'eux crie : \"I work for Leviticus Cornwall.\" (Je travaille pour Leviticus Cornwall.) Dutch compte à rebours à partir de cinq, fait tirer la bande sur la voiture, puis envoie Arthur et Charles faire sauter la porte avec la dynamite de Bill. Les employés sortent les mains en l'air ; Dutch leur lance : \"We don't want to kill you... we just wanna rob your boss.\" (On ne veut pas vous tuer... juste dévaliser votre patron.) La prochaine fois, ajoute-t-il, qu'ils ouvrent cette fichue porte quand il le leur demande. Cornwall lui-même n'est pas à bord.")},

            {"h3": two("The private car", "La voiture privée")},
            {"p": two("Arthur, Lenny and Micah search the car, which Lenny compares to a palace. Micah opens the safe and finds only papers. He hands them to Lenny: \"Least we all know you can read.\" He skims railroad contracts and invoices himself. Lenny finds sugar imports from the Spanish West Indies and \"Some fancy new boat he's ordered from Europe.\" Micah laughs that he will not rob another boat as long as he lives. Arthur finds the bonds in the car's cabinets. Dutch calls them bearer bonds and thinks they can be sold easily.",
                      "Arthur, Lenny et Micah fouillent la voiture, que Lenny compare à un palais. Micah ouvre le coffre et n'y trouve que des papiers. Il en tend une partie à Lenny, puisque lui au moins sait lire, et parcourt lui-même des contrats ferroviaires et des factures. Lenny tombe sur des importations de sucre des Antilles espagnoles et sur un bateau neuf commandé en Europe. Micah jure en riant qu'il ne braquera plus jamais un bateau de sa vie. Arthur trouve les obligations dans les placards de la voiture. Dutch y reconnaît des titres au porteur, faciles à écouler selon lui.")},

            {"h3": two("The fate of the employees", "Le sort des employés")},
            {"p": two("Dutch tells Arthur to get rid of the train and leaves the employees to him: \"It's up to you.\" He lists the options: \"Kill em', leave em' here... take 'em with you on the train... Just make sure they don't send no folk after us.\" He tells Arthur that the gang will be moving on when he gets back, and rides off with the others (see Choices and variants). The mission continues directly into [[m:eastward-bound|Eastward Bound]].",
                      "Dutch demande à Arthur de faire disparaître le train et lui laisse le sort des employés : \"It's up to you.\" (C'est toi qui vois.) Il énumère les options : les tuer, les laisser là ou les emmener dans le train, du moment qu'ils n'envoient personne à leurs trousses. Il prévient Arthur que la bande lèvera le camp à son retour, puis repart avec les autres (voir Choix et variantes). La mission enchaîne directement sur [[m:eastward-bound|Eastward Bound]].")},

            {"h3": two("Deaths", "Morts")},
            {"ul": [
                two("The guards of Cornwall's train, killed by the gang.",
                    "Les gardes du train de Cornwall, abattus par la bande."),
                two("The employees of the last car, only if Arthur kills them.",
                    "Les employés de la dernière voiture, seulement si Arthur les tue."),
                two("The engineer, thrown off the train by Arthur as it crosses a bridge; according to the transcript's stage directions, he falls to his death.",
                    "Le mécanicien, jeté du train par Arthur au passage d'un pont ; selon les didascalies de la transcription, la chute le tue."),
            ]},
        ],

        "choices": [
            {"h3": two("On the train", "Dans le train")},
            {"ul": [
                two("Arthur can pull Lenny up when he hangs from the side of a car. If he does not, Lenny climbs up alone and thanks him sarcastically, which costs honor, according to the mission page. Saving Lenny is a Gold Medal objective.",
                    "Arthur peut hisser Lenny quand il pend au flanc d'une voiture. Sinon, Lenny remonte seul et le remercie avec ironie, ce qui coûte de l'honneur, d'après la page de la mission. Sauver Lenny est un objectif de la médaille d'or."),
                two("After the first guard, Arthur chooses whether he or Lenny deals with the next one.",
                    "Après le premier garde, Arthur décide qui, de lui ou de Lenny, s'occupe du suivant."),
                two("According to the mission page, if Lenny is ahead near the engine, the engineer attacks him instead and Arthur has to save him.",
                    "Selon la page de la mission, si Lenny passe devant près de la locomotive, c'est lui que le mécanicien attaque, et Arthur doit le tirer de là."),
            ]},

            {"h3": two("The employees", "Les employés")},
            {"p": two("Arthur can kill the employees, or put them back on the train, start the engine and jump off. According to the mission page, if he does neither, they run away, and the choice only affects the player's honor: it changes nothing in the story or the mission.",
                      "Arthur peut tuer les employés, ou les remettre dans le train, lancer la locomotive et sauter en marche. D'après la page de la mission, s'il ne fait ni l'un ni l'autre, ils s'enfuient, et ce choix ne joue que sur l'honneur du joueur : il ne change rien à l'histoire ni à la mission.")},

            {"h3": two("Missable documents", "Documents à ne pas manquer")},
            {"p": two("Two documents can be missed in the car: the Oil Company Letter to Cornwall and the Mining Company Letter to Cornwall.",
                      "Deux documents peuvent être manqués dans la voiture : l'Oil Company Letter to Cornwall et la Mining Company Letter to Cornwall.")},

            {"h3": two("Mission failure", "Échec de la mission")},
            {"p": two("According to the mission page, the mission fails if the player:",
                      "D'après la page de la mission, la mission échoue si le joueur :")},
            {"ul": [
                two("assaults, kills or abandons any member of the gang, or lets one be killed;",
                    "agresse, tue ou abandonne un membre de la bande, ou laisse l'un d'eux se faire tuer ;"),
                two("fails to board the train, or abandons it;", "ne parvient pas à monter dans le train, ou l'abandonne ;"),
                two("kills or abandons his horse;", "tue ou abandonne son cheval ;"),
                two("dies.", "meurt."),
            ]},
        ],

        "gold": {
            "objectives": [
                two("Save Lenny when he is hanging from the train.", "Sauver Lenny quand il est suspendu au train."),
                two("After stopping the train, take out the guards within 1 minute and 30 seconds.", "Après l'arrêt du train, éliminer les gardes en moins de 1 minute et 30 secondes."),
                two("Take no damage during the shootout.", "Ne subir aucun dégât pendant la fusillade."),
                two("Get 10 headshots.", "Réussir 10 tirs à la tête."),
                two("Complete the mission without taking any health items.", "Terminer la mission sans prendre d'objet de soin."),
            ],
            "after": [
                {"p": two("According to the page's Gold Medal tips, the no-damage objective only applies after the train has stopped.",
                          "Selon les conseils de médaille d'or de la page, l'objectif sans dégât ne s'applique qu'une fois le train arrêté.")},
            ],
        },

        "quotes": [
            {"q": "I thought you was reading him his last rites... now I see you're introducing him to your other passion.",
             "src": two("Arthur, to Swanson, at John's bedside", "Arthur, à Swanson, au chevet de John"),
             "fr": "Je croyais que tu lui donnais l'extrême-onction... je vois que tu lui fais découvrir ton autre passion."},
            {"q": "Guess I was hoping to see a corpse.",
             "src": two("Abigail, to John", "Abigail, à John"),
             "fr": "J'espérais sans doute trouver un cadavre."},
            {"q": "You're a rotten man, John Marston.",
             "src": two("Abigail, to John, in front of Jack", "Abigail, à John, devant Jack"),
             "fr": "T'es un sale type, John Marston."},
            {"q": "Look at you boys. See? This is what I call a crew.",
             "src": two("Dutch, on the ride to the tracks", "Dutch, sur la route de la voie ferrée"),
             "fr": "Regardez-vous, les gars. Vous voyez ? Ça, c'est ce que j'appelle une équipe."},
            {"q": "So it's my fault?",
             "src": two("Arthur, when Dutch blames him for the detonator", "Arthur, quand Dutch lui reproche le détonateur"),
             "fr": "Alors c'est ma faute ?"},
            {"q": "Damn, he's got an army! Who is this guy?",
             "src": two("Lenny, during the gunfight along the train", "Lenny, pendant la fusillade le long du train"),
             "fr": "Bon sang, il a une armée ! C'est qui, ce type ?"},
            {"q": "Seems our friends have gone deaf.",
             "src": two("Dutch, at the end of his countdown", "Dutch, à la fin de son compte à rebours"),
             "fr": "On dirait que nos amis sont devenus sourds."},
            {"q": "Any bright ideas, I'll kill all three of you... so behave.",
             "src": two("Arthur, if he puts the employees back on the train", "Arthur, s'il fait remonter les employés dans le train"),
             "fr": "Au moindre coup tordu, je vous tue tous les trois... alors tenez-vous tranquilles."},
        ],

        "trivia": [
            two("Hosea's plea at Colter (see Story) returns during Arthur's last ride with high honor, according to the wiki's mission pages.",
                "La supplique d'Hosea à Colter (voir Déroulé) revient pendant la dernière chevauchée d'Arthur avec un honneur élevé, d'après les pages de missions du wiki."),
            two("The cutscene always shows the train stopping at Granite Pass, southwest of Window Rock, just before the bridge, even if it stops elsewhere, according to the mission page.",
                "La cinématique montre toujours le train à l'arrêt à Granite Pass, au sud-ouest de Window Rock, juste avant le pont, même s'il s'arrête ailleurs, d'après la page de la mission."),
            two("Micah fires a Carbine Repeater at the employees' car, one of the rare times he uses a longarm. Charles and Bill fire double-barreled shotguns, according to the same page.",
                "Micah tire sur la voiture des employés avec une Carbine Repeater, l'une des rares fois où on le voit avec une arme longue. Charles et Bill tirent au fusil à double canon, selon la même page."),
            two("The dynamite bundle explodes when shot, although Bill does not try this to stop the train, according to the mission page.",
                "Le paquet de dynamite explose si on lui tire dessus, mais Bill n'essaie pas cette méthode pour arrêter le train, selon la page de la mission."),
            two("If Arthur has his Sawed-Off Shotgun holstered, it is replaced with the Cattleman Revolver after the train is stopped, according to the mission page.",
                "Si Arthur porte son fusil à canon scié au côté, il est remplacé par le Cattleman Revolver une fois le train arrêté, d'après la page de la mission."),
            two("The robbery is reported under the headline \"Train Robbed\" in the Blackwater Ledger (No. 62), the New Hanover Gazette (No. 27) and the Saint Denis Times (No. 43). The clerk at Valentine station may mention it.",
                "L'attaque fait l'objet d'un article titré \"Train Robbed\" dans le Blackwater Ledger (n° 62), le New Hanover Gazette (n° 27) et le Saint Denis Times (n° 43). Le guichetier de la gare de Valentine peut en parler."),
            two("Arthur's journal lists the job twice under \"Gang Savings\": first with an X, the mark usually kept for jobs that brought no money, then as a separate entry once Hosea has cashed in the bonds, according to the wiki.",
                "Le journal d'Arthur inscrit le coup deux fois dans la rubrique \"Gang Savings\" : d'abord avec une croix, la marque habituellement réservée aux coups qui n'ont rien rapporté, puis comme une entrée à part, une fois qu'Hosea a encaissé les obligations, selon le wiki."),
        ],
    },
}
