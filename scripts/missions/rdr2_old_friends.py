"""Old Friends (RDR2, Chapter 1, mission 4 of the wiki's order), mission page (24 Oct 2026).

Can be played before or after "The Aftermath of Genesis" (mission 3/4). Prev/next
follow the order listed by the Red Dead Wiki: 3 = The Aftermath of Genesis,
4 = Old Friends.

Source register:
- Our v3 Chapter 1 guide, EN story/rdr2-chapter-1-colter/ and FR
  fr/histoire/rdr2-chapitre-1-colter/ (fixed 24 Oct 2026 after two adversarial
  fact-checks and a coverage check): section "4. Old Friends", the matching row
  of "Chapter 1 at a glance" (giver, companions, location, Gold Medal
  objectives), "Camp life at Colter" (Kieran tied up in the stable if this
  mission comes first), section "1. Outlaws from the West" (the spared
  O'Driscoll who reappears here), "Trivia" (Branwen). Story wording and facts
  are taken from it; the FR text is taken from the FR guide.
- Red Dead Wiki mission page "Old Friends" (scripts/v3/work/_m/Old_Friends.txt):
  infobox (start/end Colter, giver Bill, location Ewing Basin, Grizzlies West,
  rewards Carbine Repeater, Lasso, Dead Eye Targeting, next mission), Gold Medal
  objectives, mission failure conditions, deaths, trivia (Dead Eye Targeting,
  Carbine Repeater comment, spared O'Driscoll, disarming an O'Driscoll near
  Micah, Colm scolding Kieran, six ally markers, exploring the Grizzlies West
  with Kieran stowed, Kieran in the barn, Branwen, Dead Eye meter, continues
  into "Who the Hell is Leviticus Cornwall?").
- Red Dead Wiki transcript "Old Friends/dialogues" (scripts/v3/work/_m/
  Old_Friends_dialogues.txt): every quoted line was checked against it,
  including "the bastards'll be reunited soon enough", the "hold ground or go
  at them" choice, "Outlaws for life, fellers" and "a real bad day for you,
  Kieran Duffy". In the transcript Dutch reads the name "Mr. Leviticus
  Cornwall" on the plans that Micah brings him.

Left out: the "strikingly similar" line of John in Red Dead Redemption
(comparison), the "foreshadowing" of Dutch's 1911 gang and of the party after
Micah's death (interpretation), the wiki story's "Micah and Bill arguing" (the
transcript: Micah mocks Bill and Lenny, Lenny answers), the order in which Dutch
and Colm lost Annabelle and the brother (told once, on the Dutch fiche, house
rule), the knife-finisher glitch, the early General Store outfit trick, Gold
Medal tips, video links.
"""


def two(en, fr): return {"en": en, "fr": fr}


MISSION = {
    "slug": "old-friends",
    "name": "Old Friends",
    "game": "rdr2",
    "chapter": 1,
    "number": 4,
    "chapter_total": 6,
    "story_order": 4,
    "publishDate": "2026-10-24",
    "updated": "2026-10-24",
    "prev": {"slug": "the-aftermath-of-genesis", "name": "The Aftermath of Genesis"},
    "next": {"slug": "who-the-hell-is-leviticus-cornwall", "name": "Who the Hell is Leviticus Cornwall?"},

    "chips": [two("Playable before or after The Aftermath of Genesis", "Avant ou après The Aftermath of Genesis")],

    "meta_desc": two(
        "Old Friends, a Chapter 1 mission of Red Dead Redemption 2: the raid on the O'Driscoll camp at Ewing Basin, the Cornwall train plans, the capture of Kieran Duffy, Gold Medal objectives and quotes.",
        "Old Friends, mission du chapitre 1 de Red Dead Redemption 2 : l'attaque du camp O'Driscoll d'Ewing Basin, les plans du train de Cornwall, la capture de Kieran Duffy, médaille d'or et citations."),
    "og_desc": two(
        "The raid on Colm O'Driscoll's camp at Ewing Basin, step by step, and the capture of Kieran Duffy.",
        "L'attaque du camp de Colm O'Driscoll à Ewing Basin, étape par étape, et la capture de Kieran Duffy."),

    "facts": {
        "giver": two("[[bill-williamson|Bill Williamson]], in the men's cabin at Colter",
                     "[[bill-williamson|Bill Williamson]], dans la cabane des hommes à Colter"),
        "location": two("Starts and ends at Colter; Ewing Basin, Grizzlies West, Ambarino",
                        "Départ et retour à Colter ; Ewing Basin, Grizzlies West, Ambarino"),
        "characters": two(
            "[[arthur-morgan|Arthur Morgan]], [[dutch-van-der-linde|Dutch van der Linde]], [[micah-bell|Micah Bell]], [[bill-williamson|Bill Williamson]], [[javier-escuella|Javier Escuella]], [[lenny-summers|Lenny Summers]], [[kieran-duffy|Kieran Duffy]]; [[colm-odriscoll|Colm O'Driscoll]] seen through binoculars; at camp, [[uncle|Uncle]] and [[hosea-matthews|Hosea Matthews]]",
            "[[arthur-morgan|Arthur Morgan]], [[dutch-van-der-linde|Dutch van der Linde]], [[micah-bell|Micah Bell]], [[bill-williamson|Bill Williamson]], [[javier-escuella|Javier Escuella]], [[lenny-summers|Lenny Summers]], [[kieran-duffy|Kieran Duffy]] ; [[colm-odriscoll|Colm O'Driscoll]], vu à la jumelle ; au camp, [[uncle|Uncle]] et [[hosea-matthews|Hosea Matthews]]"),
        "unlocks": two("Dead Eye targeting. Played after [[m:the-aftermath-of-genesis|The Aftermath of Genesis]], it continues directly into [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]]; played first, it leaves The Aftermath of Genesis to play",
                       "Le ciblage en Dead Eye. Jouée après [[m:the-aftermath-of-genesis|The Aftermath of Genesis]], elle enchaîne directement sur [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]] ; jouée en premier, il reste The Aftermath of Genesis à faire"),
        "rewards": two("Carbine Repeater, lasso, Dead Eye targeting",
                       "Carbine Repeater, lasso, ciblage en Dead Eye"),
    },

    "intro": [
        two("\"Old Friends\" is a story mission of Red Dead Redemption 2 in <a href=\"/story/rdr2-chapter-1-colter/\">Chapter 1: Colter</a>. It is given by [[bill-williamson|Bill Williamson]], takes place at Ewing Basin, in the Grizzlies West, and ends at Colter. It can be played before or after [[m:the-aftermath-of-genesis|The Aftermath of Genesis]]: the Red Dead Wiki lists it fourth of the chapter's six missions, The Aftermath of Genesis third.",
            "\"Old Friends\" est une mission principale de Red Dead Redemption 2, au <a href=\"/fr/histoire/rdr2-chapitre-1-colter/\">chapitre 1 : Colter</a>. Donnée par [[bill-williamson|Bill Williamson]], elle se déroule à Ewing Basin, dans les Grizzlies West, et se termine à Colter. Elle peut se jouer avant ou après [[m:the-aftermath-of-genesis|The Aftermath of Genesis]] : le Red Dead Wiki la place en quatrième position des six missions du chapitre, The Aftermath of Genesis en troisième."),
        two("[[dutch-van-der-linde|Dutch van der Linde]] leads a raid on [[colm-odriscoll|Colm O'Driscoll]]'s camp. The gang takes dynamite and the plans for a train belonging to [[leviticus-cornwall|Leviticus Cornwall]], and [[arthur-morgan|Arthur Morgan]] captures [[kieran-duffy|Kieran Duffy]].",
            "[[dutch-van-der-linde|Dutch van der Linde]] mène l'attaque du camp de [[colm-odriscoll|Colm O'Driscoll]]. La bande s'empare de dynamite et des plans d'un train appartenant à [[leviticus-cornwall|Leviticus Cornwall]], et [[arthur-morgan|Arthur Morgan]] capture [[kieran-duffy|Kieran Duffy]]."),
    ],

    "sections": {
        "story": [
            {"h3": two("The fight in the men's cabin", "La bagarre dans la cabane des hommes")},
            {"p": two("In the men's cabin, [[micah-bell|Micah]] mocks Bill and [[lenny-summers|Lenny]] for their long faces: \"I ain't never seen so many long faces.\" Bill says people miss the ones who fell. Lenny tells Micah: \"When you fall... there'll be a party.\" Bill laughs. Micah punches Bill in the face; Arthur, [[javier-escuella|Javier]] and Lenny hold the two men apart. Dutch bursts in: \"You fools punching each other... when Colm O'Driscoll's needing punching, hard.\"",
                      "Dans la cabane, [[micah-bell|Micah]] raille Bill et [[lenny-summers|Lenny]] pour leurs mines d'enterrement. Bill répond que les autres pensent à ceux qui sont tombés. Lenny lance à Micah : \"When you fall... there'll be a party.\" (Le jour où tu tomberas, on fera la fête.) Bill éclate de rire. Micah frappe Bill au visage ; Arthur, [[javier-escuella|Javier]] et Lenny séparent les deux hommes. Dutch fait irruption : \"You fools punching each other... when Colm O'Driscoll's needing punching, hard.\" (Bande d'idiots, vous vous tapez dessus... alors que c'est Colm O'Driscoll qu'il faut frapper, et fort.)")},
            {"p": two("Outside, Arthur asks whether a raid is wise when the gang is barely back on its feet, and reminds Dutch that he always said revenge is a luxury they cannot afford. Dutch tells him he is doubting him, and answers that the O'Driscolls \"were talking about trains and detonators\", and that Colm always had good information. He hands Arthur a Carbine Repeater and a lasso. Dutch leaves [[hosea-matthews|Hosea]], [[charles-smith|Charles]] and [[simon-pearson|Pearson]] to watch the camp, and rides out with Arthur, Micah, Bill, Javier and Lenny.",
                      "Dehors, Arthur demande si un raid est bien raisonnable alors que la bande tient à peine debout, et rappelle à Dutch qu'il a toujours dit que la vengeance était un luxe qu'ils ne pouvaient pas se payer. Dutch lui reproche de douter de lui, puis répond que les O'Driscoll parlaient de trains et de détonateurs, et que Colm a toujours eu de bonnes informations. Il remet à Arthur une Carbine Repeater et un lasso. Dutch laisse [[hosea-matthews|Hosea]], [[charles-smith|Charles]] et [[simon-pearson|Pearson]] garder le camp et part avec Arthur, Micah, Bill, Javier et Lenny.")},

            {"h3": two("The ride to Ewing Basin", "La route d'Ewing Basin")},
            {"p": two("They follow horse tracks southwest along the main trail. Dutch says: \"Some things I can forgive, others I can forget. What he did to Annabelle, I can't do neither.\" Arthur reminds him that he killed Colm's brother. Dutch answers: \"Yes, I did. And I hope the bastards'll be reunited soon enough. That's how this'll end.\"",
                      "Ils suivent des traces de chevaux vers le sud-ouest, sur la piste principale. Dutch déclare : \"Some things I can forgive, others I can forget. What he did to Annabelle, I can't do neither.\" (Il y a des choses que je peux pardonner, d'autres que je peux oublier. Ce qu'il a fait à Annabelle, je ne peux ni l'un ni l'autre.) Arthur lui rappelle qu'il a tué le frère de Colm. Dutch répond qu'il espère bien que les deux frères seront bientôt réunis, et que c'est ainsi que ça finira.")},

            {"h3": two("Watching the camp", "Le camp sous surveillance")},
            {"p": two("From a ridge above the camp near the lake, Dutch posts Bill and Micah in a hidden position outside the camp and keeps Lenny and Javier on the high ground. Through binoculars, Dutch and Arthur watch Colm strike one of his men, who rides away; Colm leaves soon after. Dutch says: \"No, Colm can wait. Best to get some of them outta there.\" He adds that it is \"much less fun to rob him and his score if he never finds out about it.\"",
                      "Depuis une crête au-dessus du camp, près du lac, Dutch poste Bill et Micah à couvert aux abords du camp et laisse Lenny et Javier sur les hauteurs. À la jumelle, Dutch et Arthur voient Colm frapper l'un de ses hommes, qui s'éloigne à cheval ; Colm part peu après. Dutch tranche : \"No, Colm can wait. Best to get some of them outta there.\" (Non, Colm peut attendre. Mieux vaut en sortir quelques-uns de là.) Il ajoute qu'il sera bien moins drôle de le dépouiller, lui et son butin, s'il n'en sait jamais rien.")},
            {"p": two("As they creep down, Dutch tells Arthur that the gang needs \"supplies, equipment, and a way out of here.\" Arthur offers to take the lead, since the O'Driscolls are \"going to be gunning for\" Dutch.",
                      "Pendant la descente, Dutch explique à Arthur que la bande a besoin de provisions, de matériel et d'un moyen de partir d'ici. Arthur propose de passer devant, puisque c'est Dutch que les O'Driscoll vont viser.")},

            {"h3": two("The raid", "L'attaque")},
            {"p": two("In cover, Dutch lets Arthur decide who opens fire. The gang kills the O'Driscolls in the camp. While the bodies are searched, Dutch says Colm \"doesn't give a damn about his men\" and only cares about numbers. A second wave then comes out of the trees, and Dutch asks Arthur whether they should hold ground or go at them.",
                      "À couvert, Dutch laisse Arthur décider qui ouvre le feu. La bande abat les O'Driscoll du camp. Pendant qu'on fouille les corps, Dutch affirme que Colm se moque de ses hommes et ne pense qu'au nombre. Une seconde vague sort alors des arbres, et Dutch demande à Arthur s'il faut tenir la position ou leur foncer dessus.")},
            {"p": two("Once the camp is clear, Bill searches a wagon, Micah a building and Arthur another, where he finds a box of dynamite. Micah hands Dutch a roll of paper \"found on one of them\": the plans for a train belonging to a \"Mr. Leviticus Cornwall.\"",
                      "Une fois le camp nettoyé, Bill fouille un chariot, Micah un bâtiment et Arthur un autre, où il trouve une caisse de dynamite. Micah tend à Dutch un rouleau de papier trouvé sur l'un des morts : les plans d'un train appartenant à un certain \"Mr. Leviticus Cornwall\".")},

            {"h3": two("The ride back", "Le retour")},
            {"p": two("On the ride back, Dutch tells the men he is proud that not a man is down: \"Outlaws for life, fellers.\" He promises that John, Mac, Charles and [[sean-macguire|Sean]] will ride with them again. Arthur says the raid \"will hurt him a lot more than any bullet in the head\"; Dutch answers: \"Especially when we rob this train, too.\" When Arthur warns that Colm will come after them, Dutch says the gang allowed itself to get a step behind in Blackwater and that it will not happen again.",
                      "Sur le chemin du retour, Dutch se dit fier qu'il n'y ait aucun blessé : \"Outlaws for life, fellers.\" (Hors-la-loi pour la vie, les gars.) Il promet que John, Mac, Charles et [[sean-macguire|Sean]] chevaucheront de nouveau avec eux. Arthur estime que le raid fera plus de mal à Colm qu'une balle dans la tête ; Dutch renchérit : \"Especially when we rob this train, too.\" (Surtout quand on aura aussi braqué ce train.) Quand Arthur l'avertit que Colm viendra les chercher, Dutch répond que la bande s'est laissé prendre de vitesse à Blackwater et que ça ne se reproduira pas.")},

            {"h3": two("Kieran Duffy", "Kieran Duffy")},
            {"p": two("Near the lake, Dutch spots a lone rider and asks whether he was at the camp with Colm. The man is the one Colm struck. Dutch tells Arthur to bring him back alive. The man flees on his horse, Branwen; Arthur chases him, ropes him off the horse and hogties him. On the ride to Colter, the prisoner first says he does not know his name, then gives it: Kieran Duffy. Arthur tells him: \"this is a real bad day for you, Kieran Duffy.\" Kieran says he has only been riding with the O'Driscolls for a couple of months.",
                      "Près du lac, Dutch repère un cavalier seul et se demande s'il n'était pas au camp avec Colm. C'est l'homme que Colm a frappé. Dutch demande à Arthur de le ramener vivant. L'homme s'enfuit sur son cheval, Branwen ; Arthur le poursuit, le fait tomber de selle au lasso et le ligote. Sur la route de Colter, le prisonnier prétend d'abord ne pas connaître son nom, puis le donne : Kieran Duffy. Arthur lui annonce que c'est un bien mauvais jour pour lui. Kieran assure ne rouler avec les O'Driscoll que depuis deux ou trois mois.")},

            {"h3": two("Back at Colter", "Retour à Colter")},
            {"p": two("At camp, Arthur offers to make him talk. Dutch refuses: \"Oh no, now all we'll get is lies.\" He tells Bill and [[uncle|Uncle]] to tie him up somewhere safe and get him hungry first. He tells Kieran: \"we shoot fellers as need shooting... save fellers as need saving... and feed 'em as need feeding.\" Kieran protests that he is not an O'Driscoll and hates Colm; Dutch answers with sarcasm: \"Oh, whatever you say, son.\" Arthur says he is sorry they missed Colm. Dutch answers that there is \"time enough for that\" and that he must now \"figure out if we can hit that train.\"",
                      "Au camp, Arthur propose de le faire parler. Dutch refuse : \"Oh no, now all we'll get is lies.\" (Oh non, maintenant on n'en tirera que des mensonges.) Il charge Bill et [[uncle|Uncle]] de l'attacher en lieu sûr et de le laisser d'abord avoir faim. Il lance à Kieran sa devise : \"we shoot fellers as need shooting... save fellers as need saving... and feed 'em as need feeding.\" (on abat ceux qu'il faut abattre, on sauve ceux qu'il faut sauver, et on nourrit ceux qu'il faut nourrir.) Kieran proteste qu'il n'est pas un O'Driscoll et qu'il déteste Colm ; Dutch lui répond par l'ironie. Arthur regrette qu'ils aient manqué Colm. Dutch répond qu'ils ont le temps, et qu'il doit maintenant voir s'ils peuvent attaquer ce train.")},

            {"h3": two("Deaths", "Morts")},
            {"ul": [
                two("Numerous O'Driscolls at Ewing Basin, killed by the Van der Linde gang.",
                    "De nombreux O'Driscoll à Ewing Basin, abattus par la bande Van der Linde."),
                two("Kieran's horse Branwen, only if the player kills it during the chase (see Choices and variants).",
                    "Branwen, le cheval de Kieran, seulement si le joueur l'abat pendant la poursuite (voir Choix et variantes)."),
            ]},
        ],

        "choices": [
            {"h3": two("Before the raid", "Avant l'attaque")},
            {"ul": [
                two("If Arthur puts the Carbine Repeater back on his horse after picking it up, Dutch comments on it, according to the mission page.",
                    "Si Arthur remet la Carbine Repeater sur son cheval après l'avoir prise, Dutch fait une remarque, d'après la page de la mission."),
                two("In cover, Arthur can fire the first shot himself or let Dutch do it.",
                    "À couvert, Arthur peut tirer le premier ou laisser Dutch le faire."),
            ]},

            {"h3": two("The second wave", "La seconde vague")},
            {"p": two("When the second wave comes out of the trees, the player chooses between \"Advance\" and holding ground (\"Reckon we're better off holding here\"). In the first case, the gang moves further into the trees.",
                      "Quand la seconde vague sort des arbres, le joueur choisit entre avancer (\"Advance\") et tenir la position (\"Reckon we're better off holding here\", je crois qu'on a intérêt à tenir ici). Dans le premier cas, la bande s'enfonce entre les arbres.")},

            {"h3": two("The O'Driscoll from the Adler Ranch", "L'O'Driscoll de l'Adler Ranch")},
            {"p": two("If the player spared the O'Driscoll in the barn in [[m:outlaws-from-the-west|Outlaws from the West]], he appears in the cabin in front of the gang once Arthur and Dutch are in cover, shouting \"You should've killed me when you had the chance!\", and is killed there, according to the mission page. Before the shootout, he can be heard telling another O'Driscoll about the interrogation, according to the same page.",
                      "Si le joueur a épargné l'O'Driscoll de la grange dans [[m:outlaws-from-the-west|Outlaws from the West]], il apparaît dans la cabane face à la bande une fois Arthur et Dutch à couvert, lance \"You should've killed me when you had the chance!\" (Fallait me tuer quand tu pouvais !) et y est tué, d'après la page de la mission. Avant la fusillade, on peut l'entendre raconter l'interrogatoire à un autre O'Driscoll, selon la même page.")},

            {"h3": two("Disarming an O'Driscoll", "Désarmer un O'Driscoll")},
            {"p": two("According to the mission page, if the player disarms an O'Driscoll and leads him to Micah, the O'Driscoll wrestles one of Micah's guns from his hand, which makes it possible to obtain Micah's Revolver before the epilogue.",
                      "D'après la page de la mission, si le joueur désarme un O'Driscoll et l'amène jusqu'à Micah, l'O'Driscoll arrache l'un de ses revolvers à Micah, ce qui permet d'obtenir le revolver de Micah avant l'épilogue.")},

            {"h3": two("The chase", "La poursuite")},
            {"p": two("The player can kill Kieran's horse Branwen during the chase. According to the mission page, this costs honor and has no effect on the story: Branwen still appears at camp later in the game. Killing Kieran himself fails the mission.",
                      "Le joueur peut abattre Branwen, le cheval de Kieran, pendant la poursuite. D'après la page de la mission, cela coûte de l'honneur sans rien changer à l'histoire : Branwen réapparaît quand même au camp plus tard dans le jeu. Tuer Kieran lui-même fait échouer la mission.")},

            {"h3": two("Order of play: Kieran at Colter", "Ordre des missions : Kieran à Colter")},
            {"p": two("If Old Friends is played before [[m:the-aftermath-of-genesis|The Aftermath of Genesis]], Kieran can be found tied up in the stable at Colter. He tries to scare Arthur with the O'Driscolls who will come looking for him, and learns that his group was not the first the gang has killed. If Arthur leaves and comes back, Kieran asks when he will be released and gets more taunts. Played after The Aftermath of Genesis, the mission continues directly into [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]].",
                      "Si Old Friends est jouée avant [[m:the-aftermath-of-genesis|The Aftermath of Genesis]], Kieran est attaché dans l'écurie de Colter. Il essaie d'intimider Arthur en lui promettant que les O'Driscoll viendront le chercher, et apprend que sa bande n'est pas la première que les Van der Linde ont décimée. Si Arthur sort puis revient, Kieran demande quand on le relâchera et n'obtient que d'autres railleries. Jouée après The Aftermath of Genesis, la mission enchaîne directement sur [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]].")},

            {"h3": two("Mission failure", "Échec de la mission")},
            {"p": two("According to the mission page, the mission fails if the player:",
                      "D'après la page de la mission, la mission échoue si le joueur :")},
            {"ul": [
                two("assaults, kills or abandons any member of the gang, or lets one be killed;",
                    "agresse, tue ou abandonne un membre de la bande, ou laisse l'un d'eux se faire tuer ;"),
                two("alerts the O'Driscolls too early;", "alerte les O'Driscoll trop tôt ;"),
                two("kills the fleeing O'Driscoll, or lets him escape;",
                    "tue l'O'Driscoll en fuite, ou le laisse s'échapper ;"),
                two("kills or abandons his horse;", "tue ou abandonne son cheval ;"),
                two("dies.", "meurt."),
            ]},
        ],

        "gold": {
            "objectives": [
                two("Catch and hogtie Kieran within 45 seconds.", "Attraper et ligoter Kieran en moins de 45 secondes."),
                two("Kill 3 O'Driscolls in the same Dead Eye use.", "Tuer 3 O'Driscoll en une seule utilisation du Dead Eye."),
                two("Complete within 15 minutes and 30 seconds.", "Terminer en moins de 15 minutes et 30 secondes."),
                two("Get 15 headshots.", "Réussir 15 tirs à la tête."),
                two("Complete the mission without taking any health items.", "Terminer la mission sans prendre d'objet de soin."),
            ],
            "after": [
                {"p": two("According to the mission page, the Dead Eye meter does not deplete while it flashes on its first appearance, which helps with the second objective.",
                          "D'après la page de la mission, la jauge de Dead Eye ne se vide pas tant qu'elle clignote lors de sa première apparition, ce qui aide pour le deuxième objectif.")},
            ],
        },

        "quotes": [
            {"q": "When you fall... there'll be a party.",
             "src": two("Lenny, to Micah, in the men's cabin", "Lenny, à Micah, dans la cabane des hommes"),
             "fr": "Le jour où tu tomberas... on fera la fête."},
            {"q": "You fools punching each other... when Colm O'Driscoll's needing punching, hard.",
             "src": two("Dutch, breaking up the fight", "Dutch, en mettant fin à la bagarre"),
             "fr": "Bande d'idiots, vous vous tapez dessus... alors que c'est Colm O'Driscoll qu'il faut frapper, et fort."},
            {"q": "Some things I can forgive, others I can forget. What he did to Annabelle, I can't do neither.",
             "src": two("Dutch, on the ride to Ewing Basin", "Dutch, sur la route d'Ewing Basin"),
             "fr": "Il y a des choses que je peux pardonner, d'autres que je peux oublier. Ce qu'il a fait à Annabelle, je ne peux ni l'un ni l'autre."},
            {"q": "And I hope the bastards'll be reunited soon enough. That's how this'll end.",
             "src": two("Dutch, about Colm and his brother", "Dutch, à propos de Colm et de son frère"),
             "fr": "Et j'espère que ces salauds seront bientôt réunis. C'est comme ça que ça finira."},
            {"q": "No, Colm can wait. Best to get some of them outta there.",
             "src": two("Dutch, watching the camp through binoculars", "Dutch, en observant le camp à la jumelle"),
             "fr": "Non, Colm peut attendre. Mieux vaut en sortir quelques-uns de là."},
            {"q": "Outlaws for life, fellers.",
             "src": two("Dutch, on the ride back", "Dutch, sur le chemin du retour"),
             "fr": "Hors-la-loi pour la vie, les gars."},
            {"q": "This is a real bad day for you, Kieran Duffy.",
             "src": two("Arthur, to his prisoner", "Arthur, à son prisonnier"),
             "fr": "C'est vraiment un sale jour pour toi, Kieran Duffy."},
            {"q": "We shoot fellers as need shooting... save fellers as need saving... and feed 'em as need feeding.",
             "src": two("Dutch, to Kieran, at Colter", "Dutch, à Kieran, à Colter"),
             "fr": "On abat ceux qu'il faut abattre, on sauve ceux qu'il faut sauver, et on nourrit ceux qu'il faut nourrir."},
        ],

        "trivia": [
            two("The mission unlocks Dead Eye targeting, according to the mission page.",
                "La mission débloque le ciblage en Dead Eye, d'après la page de la mission."),
            two("When the gang watches the hideout from a distance, the man Colm scolds is Kieran, according to the mission page.",
                "Quand la bande observe le repaire de loin, l'homme que Colm rabroue est Kieran, d'après la page de la mission."),
            two("After Kieran's capture, the map shows six ally markers at the hideout: one for each participant and one for Hosea, who only appears in the opening and closing cutscenes, according to the mission page.",
                "Après la capture de Kieran, la carte affiche six marqueurs alliés au repaire : un par participant, plus un pour Hosea, qui n'apparaît pourtant que dans les cinématiques de début et de fin, d'après la page de la mission."),
            two("Once Kieran is stowed on Arthur's horse, the snowy parts of the Grizzlies West can be explored; getting too close to West Elizabeth, New Hanover or the Grizzlies East triggers an instant death and fails the mission, according to the mission page.",
                "Une fois Kieran chargé sur le cheval d'Arthur, on peut explorer les zones enneigées des Grizzlies West ; s'approcher trop de West Elizabeth, du New Hanover ou des Grizzlies East provoque une mort instantanée et l'échec de la mission, selon la page de la mission."),
        ],
    },
}
