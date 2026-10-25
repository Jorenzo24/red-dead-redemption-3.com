"""Enter, Pursued by a Memory (RDR2, Chapter 1, mission 2), mission page (24 Oct 2026).

Source register:
- Our v3 Chapter 1 guide, EN story/rdr2-chapter-1-colter/ and FR
  fr/histoire/rdr2-chapitre-1-colter/ (fixed 24 Oct 2026 after two adversarial
  fact-checks and a coverage check): section "2. Enter, Pursued by a Memory",
  the matching row of "Chapter 1 at a glance" (giver, companions, location, Gold
  Medal objectives), "Background: the Blackwater ferry robbery" (Javier's
  account), "Camp life at Colter" (the optional scenes unlocked after this
  mission) and "Trivia" (Red Dead Redemption theme, map boundaries, avalanche,
  Shakespeare title). Story wording and facts are taken from it; the FR text is
  taken from the FR guide.
- Red Dead Wiki mission page "Enter, Pursued by a Memory" (scripts/v3/work/_m/
  Enter_Pursued_by_a_Memory.txt): infobox (start/end Colter, giver listed as
  Abigail Roberts, location Grizzlies West, reward Sawed-Off Shotgun, next
  missions), Gold Medal objectives, mission failure conditions (including the
  replay note on the Sawed-Off Shotgun), trivia (bourbon if no provisions,
  revolver comment, trampling wolves, unique death scene, John's clothes,
  Northern Grizzlies, avalanche), Gold Medal tip on the third wolf, trophies
  (Just a Scratch, Gold Rush, Best in the West).
- Red Dead Wiki transcript "Enter, Pursued by a Memory/dialogues" (scripts/v3/
  work/_m/Enter_Pursued_by_a_Memory_dialogues.txt): every quoted line was
  checked against it ("little John", "dumb as rocks", "the situation were
  reversed", "the right man for this", "That bullet in Blackwater", "a better
  story for that scar", "a new low").

Left out: the "foreshadowing" of John's hunt for Javier in 1911 and the echo of
"keep riding and don't look back" at the end of the game (interpretation), the
Robin Hood reading of "little John" (interpretation), the wiki story's "Bill
and Lenny help John get inside" (the transcript and our guide: they pull him
off the horse so roughly that Javier protests), other Gold Medal tips,
controller settings, the video links.
"""


def two(en, fr): return {"en": en, "fr": fr}


MISSION = {
    "slug": "enter-pursued-by-a-memory",
    "name": "Enter, Pursued by a Memory",
    "game": "rdr2",
    "chapter": 1,
    "number": 2,
    "chapter_total": 6,
    "story_order": 2,
    "publishDate": "2026-10-24",
    "updated": "2026-10-24",
    "prev": {"slug": "outlaws-from-the-west", "name": "Outlaws from the West"},
    "next": {"slug": "the-aftermath-of-genesis", "name": "The Aftermath of Genesis"},

    "meta_desc": two(
        "Enter, Pursued by a Memory, the second mission of Red Dead Redemption 2: Arthur and Javier search the Grizzlies for John Marston, the wolves, rewards, Gold Medal objectives and quotes.",
        "Enter, Pursued by a Memory, deuxième mission de Red Dead Redemption 2 : Arthur et Javier cherchent John Marston dans les Grizzlies, les loups, récompenses, médaille d'or et citations."),
    "og_desc": two(
        "The second mission of Red Dead Redemption 2, step by step: the search for John Marston, the wolves and the return to Colter.",
        "La deuxième mission de Red Dead Redemption 2, étape par étape : la recherche de John Marston, les loups et le retour à Colter."),

    "facts": {
        "giver": [
            {"slug": "abigail-marston", "name": "Abigail Marston"},
        ],
        "giver_note": two("Listed under her 1899 name, Abigail Roberts, on the Red Dead Wiki mission page.",
                     "Sous son nom de 1899, Abigail Roberts, sur la page de la mission du Red Dead Wiki."),
        "location": two("Starts and ends at Colter; Grizzlies West, Ambarino",
                        "Départ et retour à Colter ; Grizzlies West, Ambarino"),
        "characters": [
            {"slug": "arthur-morgan", "name": "Arthur Morgan"},
            {"slug": "javier-escuella", "name": "Javier Escuella"},
            {"slug": "john-marston", "name": "John Marston"},
            {"slug": "abigail-marston", "name": "Abigail Marston", "camp": True},
            {"slug": "hosea-matthews", "name": "Hosea Matthews", "camp": True},
            {"slug": "tilly-jackson", "name": "Tilly Jackson", "camp": True},
            {"slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill", "camp": True},
            {"slug": "bill-williamson", "name": "Bill Williamson", "camp": True},
            {"slug": "lenny-summers", "name": "Lenny Summers", "camp": True},
            {"slug": "leopold-strauss", "name": "Leopold Strauss", "short": "Strauss", "camp": True},
        ],
        "unlocks": two("[[m:the-aftermath-of-genesis|The Aftermath of Genesis]] and [[m:old-friends|Old Friends]], which can be played in either order; the optional camp scenes at Colter",
                       "[[m:the-aftermath-of-genesis|The Aftermath of Genesis]] et [[m:old-friends|Old Friends]], jouables dans l'ordre qu'on veut ; les scènes facultatives du camp de Colter"),
        "rewards": two("Sawed-Off Shotgun; \"Just a Scratch\" trophy",
                       "Fusil à canon scié (Sawed-Off Shotgun) ; trophée \"Just a Scratch\""),
    },

    "intro": [
        two("\"Enter, Pursued by a Memory\" is the second story mission of Red Dead Redemption 2 and the second of the six missions of <a href=\"/story/rdr2-chapter-1-colter/\">Chapter 1: Colter</a>. It is given by [[abigail-marston|Abigail]], starts and ends at Colter and takes place in the Grizzlies West of Ambarino.",
            "\"Enter, Pursued by a Memory\" est la deuxième mission principale de Red Dead Redemption 2 et la deuxième des six missions du <a href=\"/fr/histoire/rdr2-chapitre-1-colter/\">chapitre 1 : Colter</a>. Donnée par [[abigail-marston|Abigail]], elle part de Colter, y revient et se déroule dans les Grizzlies West, en Ambarino."),
        two("[[john-marston|John Marston]] has not come back from scouting for two days. [[arthur-morgan|Arthur Morgan]] and [[javier-escuella|Javier Escuella]] find him on a mountain ledge, his face torn by wolves, and bring him back to camp. The mission follows [[m:outlaws-from-the-west|Outlaws from the West]].",
            "[[john-marston|John Marston]] n'est pas revenu de reconnaissance depuis deux jours. [[arthur-morgan|Arthur Morgan]] et [[javier-escuella|Javier Escuella]] le retrouvent sur une corniche, le visage lacéré par des loups, et le ramènent au camp. La mission suit [[m:outlaws-from-the-west|Outlaws from the West]]."),
    ],

    "sections": {
        "story": [
            {"h3": two("John is missing", "John a disparu")},
            {"p": two("In the main cabin at Colter, Abigail tells Arthur that John has not been seen for two days. Arthur is reluctant and mocks John. He says John may be \"as dumb as rocks and as dull as rusted iron\", but that a snowstorm will not change that. Hosea tells him to at least go and look, and asks Javier to ride out with him, calling them \"the two best fit men we've got.\" Javier agrees, saying that John would look for him if things were reversed. He hands Arthur a sawed-off shotgun.",
                      "Dans la grande cabane de Colter, Abigail apprend à Arthur que John n'a pas reparu depuis deux jours. Arthur traîne des pieds et se moque de John. John est peut-être bête comme ses pieds et terne comme du fer rouillé, dit-il, mais ce n'est pas une tempête de neige qui y changera quoi que ce soit. Hosea lui demande d'aller au moins voir et prie Javier de l'accompagner : ce sont, dit-il, les deux hommes les plus en forme de la bande. Javier accepte, en disant que John le chercherait si les rôles étaient inversés. Il remet un fusil à canon scié à Arthur.")},

            {"h3": two("Up the river", "En remontant la rivière")},
            {"p": two("John was last seen heading up the river. Arthur suggests he may have \"kept riding north and never looked back\", and adds that it would not be the first time; Javier says John would not leave like that. Javier spots smoke, and they find an abandoned campsite with the fire still smoking. Arthur judges it was left \"a few hours ago, at most\" and hopes it is not more of O'Driscoll's boys. They follow horse tracks across a stream and up the mountain.",
                      "John a été vu pour la dernière fois en remontant la rivière. Arthur avance qu'il a peut-être continué vers le nord sans se retourner, et que ce ne serait pas la première fois ; Javier répond que John ne partirait pas comme ça. Javier aperçoit de la fumée, et ils découvrent un campement abandonné dont le feu fume encore. Arthur estime qu'il a été quitté quelques heures plus tôt, tout au plus, et espère que ce ne sont pas encore des hommes d'O'Driscoll. Ils suivent des traces de chevaux, de l'autre côté d'un cours d'eau puis dans la montagne.")},
            {"p": two("On the way, Arthur asks Javier, who was there, what really happened on the boat in Blackwater. Javier answers: \"We had the money, it seemed fine, then suddenly they were everywhere.\" The attackers were Pinkerton agents. Javier also says that [[dutch-van-der-linde|Dutch]] \"killed a girl in a... bad way, but it was a bad situation.\" Arthur answers that it is not like him. The Red Dead Wiki names the young woman Heidi McCourt.",
                      "En chemin, Arthur demande à Javier, qui y était, ce qui s'est vraiment passé sur le bateau à Blackwater. Javier répond : \"We had the money, it seemed fine, then suddenly they were everywhere.\" (On avait l'argent, tout avait l'air d'aller, et d'un coup ils étaient partout.) Les assaillants étaient des agents de la Pinkerton. Javier ajoute que [[dutch-van-der-linde|Dutch]] \"killed a girl in a... bad way, but it was a bad situation\" (a tué une fille, d'une sale manière, mais la situation était mauvaise). Arthur répond que ça ne lui ressemble pas. Le Red Dead Wiki nomme la jeune femme Heidi McCourt.")},
            {"p": two("According to Javier, Davey, Mac and John were all shot, and nobody knows what happened to [[sean-macguire|Sean]]. He adds that the men on the boat \"were only just holding on\" by the time Arthur and the others showed up on the other side of town.",
                      "Selon Javier, Davey, Mac et John ont tous été touchés, et personne ne sait ce qu'est devenu [[sean-macguire|Sean]]. Il ajoute que les hommes du bateau tenaient à peine le coup quand Arthur et les autres sont arrivés de l'autre côté de la ville.")},

            {"h3": two("John's horse and the climb", "Le cheval de John et l'ascension")},
            {"p": two("Higher up, they find John's bay mare, dead and mauled; Javier says John was riding it when they left Blackwater. Javier fires into the air, and John's shouts answer from higher up. The two men leave their horses and climb on foot.",
                      "Plus haut, ils découvrent la jument baie de John, morte et dévorée ; Javier précise que John la montait en quittant Blackwater. Javier tire en l'air, et les cris de John lui répondent, plus haut. Les deux hommes laissent leurs montures et poursuivent à pied.")},
            {"p": two("They find John lying on a ledge, his face torn by wolves. John says: \"Never thought I'd say this, but... it's good to see you, Arthur Morgan.\" Arthur carries John on his shoulder and tells him: \"See, I told Dutch you weren't the right man for this.\"",
                      "Ils trouvent John allongé sur une corniche, le visage lacéré par des loups. John lâche : \"Never thought I'd say this, but... it's good to see you, Arthur Morgan.\" (J'aurais jamais cru dire ça, mais... ça fait plaisir de te voir, Arthur Morgan.) Arthur le charge sur son épaule et lui rappelle qu'il avait prévenu Dutch : John n'était pas l'homme de la situation.")},

            {"h3": two("The wolves", "Les loups")},
            {"p": two("Three wolves appear on the slope. Arthur hands John to Javier, draws the wolves onto himself and kills them. On the ride down, more wolves attack and are shot. John thanks them for coming for him. Javier answers: \"That bullet in Blackwater, now this?\" They ride in the water for a while to lose the scent. Arthur tells John they will need a better story for the scar.",
                      "Trois loups surgissent sur la pente. Arthur confie John à Javier, attire les bêtes sur lui et les abat. Pendant la descente à cheval, d'autres loups attaquent et sont abattus à leur tour. John les remercie d'être venus le chercher. Javier lui répond : \"That bullet in Blackwater, now this?\" (Une balle à Blackwater, et maintenant ça ?) Ils remontent un moment le lit de la rivière pour brouiller la piste. Arthur fait remarquer à John qu'il lui faudra trouver une meilleure histoire pour expliquer sa cicatrice.")},

            {"h3": two("Back at Colter", "Retour à Colter")},
            {"p": two("Back at Colter, [[bill-williamson|Bill]] and [[lenny-summers|Lenny]] pull John off Javier's horse so roughly that Javier calls them idiots and tells them to mind his leg. Abigail thanks the two men and tells John that this is \"a new low, even by your standards.\" Hosea thanks them as well.",
                      "De retour à Colter, [[bill-williamson|Bill]] et [[lenny-summers|Lenny]] descendent John du cheval de Javier si brutalement que Javier les traite d'idiots et leur dit de faire attention à sa jambe. Abigail remercie les deux hommes, puis lance à John qu'il est tombé encore plus bas que d'habitude. Hosea les remercie à son tour.")},
            {"p": two("Arthur asks how the gang will get out of this. Hosea, who has been talking with [[leopold-strauss|Leopold Strauss]], says they will keep heading east when the weather breaks. Arthur is surprised at the idea of moving toward civilization. Hosea answers: \"the west is where our problems are worse.\"",
                      "Arthur demande comment la bande compte se tirer de là. Hosea, qui en discutait avec [[leopold-strauss|Leopold Strauss]], répond qu'il faudra continuer vers l'est dès que le temps le permettra. Arthur s'étonne qu'on aille vers la civilisation. Hosea lui rappelle que c'est dans l'Ouest que leurs ennuis sont les pires.")},
            {"p": two("The mission closes on Arthur writing in his journal: \"We have been running for weeks. We found shelter and been... resting here in some old abandoned mining town... while we wait the thaw. Hardly the spring I had been hoping for.\"",
                      "La mission se termine sur Arthur qui écrit dans son journal : \"We have been running for weeks. We found shelter and been... resting here in some old abandoned mining town... while we wait the thaw. Hardly the spring I had been hoping for.\" (Ça fait des semaines qu'on fuit. On a trouvé un abri, on se repose dans une vieille ville minière abandonnée en attendant le dégel. Pas vraiment le printemps que j'espérais.)")},

            {"h3": two("After the mission: camp life at Colter", "Après la mission : la vie au camp de Colter")},
            {"p": two("After this mission, the player can walk around the camp, though not far from it, according to the mission page. The Camp Events page of the Red Dead Wiki lists a small number of optional scenes at Colter, visible from the end of this mission until the second of [[m:old-friends|Old Friends]] and [[m:the-aftermath-of-genesis|The Aftermath of Genesis]] is finished:",
                      "Après cette mission, le joueur peut se déplacer dans le camp, sans trop s'en éloigner, selon la page de la mission. La page Camp Events du Red Dead Wiki recense quelques scènes facultatives à Colter, visibles dès la fin de cette mission et jusqu'à la fin de la seconde des deux missions [[m:old-friends|Old Friends]] et [[m:the-aftermath-of-genesis|The Aftermath of Genesis]] :")},
            {"ul": [
                two("By the fireplace, Dutch tells Hosea he feels Hosea doubts him. Hosea says he is only worried. Dutch then asks Arthur the same question, and Arthur says he does not doubt him.",
                    "Au coin du feu, Dutch reproche à Hosea de douter de lui. Hosea répond qu'il est seulement inquiet. Dutch pose alors la question à Arthur, qui répond qu'il ne doute pas de lui."),
                two("In the main cabin, [[sadie-adler|Sadie]] sobs over her husband while [[mary-beth-gaskill|Mary-Beth Gaskill]] comforts her. Mary-Beth tells Arthur that Sadie will be alright, and he agrees. Arthur can offer Sadie food; she says she is not hungry.",
                    "Dans la grande cabane, [[sadie-adler|Sadie]] pleure son mari et [[mary-beth-gaskill|Mary-Beth Gaskill]] la console. Mary-Beth assure à Arthur que Sadie s'en remettra, et il approuve. Arthur peut proposer à manger à Sadie, qui refuse."),
                two("[[susan-grimshaw|Susan Grimshaw]] gives the cabin a speech: keep warm, the mountain will be behind them in a few days, and the gang must stick together. [[tilly-jackson|Tilly Jackson]] says she hopes Susan is right. Susan asks Arthur for his opinion, and he agrees with her.",
                    "[[susan-grimshaw|Susan Grimshaw]] harangue la cabane : qu'on reste au chaud, la montagne sera derrière eux d'ici quelques jours, et la bande doit rester soudée. [[tilly-jackson|Tilly Jackson]] espère qu'elle a raison. Susan demande son avis à Arthur, qui lui donne raison."),
                two("[[orville-swanson|Swanson]] reads Isaiah 40:20-31 aloud. [[karen-jones|Karen Jones]] asks what it means; he says he has no idea, but it gives him comfort.",
                    "[[orville-swanson|Swanson]] lit à voix haute Isaïe 40, 20-31. [[karen-jones|Karen Jones]] lui demande ce que ça signifie ; il avoue n'en avoir aucune idée, mais dit que ça le réconforte."),
                two("Abigail scolds the bedridden John for getting himself mauled by wolves. John says he has made his mistakes; Abigail takes offense, calls him annoying and tells him to rest.",
                    "Abigail sermonne John, alité, de s'être fait attaquer par des loups. John concède avoir commis des erreurs ; vexée, Abigail le trouve agaçant et lui dit de se reposer."),
                two("When Arthur approaches, John says \"Oh God no.\" Susan asks Arthur what he wants. He says he came to pay his respects to \"the fallen hero\", and Susan tells him to leave John alone.",
                    "Quand Arthur approche, John soupire \"Oh God no\" (oh non, pas lui). Susan demande à Arthur ce qu'il veut. Il dit, pour plaisanter, être venu rendre hommage au héros tombé au combat, et Susan lui demande de laisser John tranquille."),
                two("Dutch asks Hosea to send someone \"sensible\" to bury Sadie's husband. Arthur can tell Hosea the body is in a wagon in front of the house, and Hosea says he will send someone. Arthur tells Dutch it was a good call; Dutch says it is the least they could do for Sadie. Arthur jokes about sending Micah, then changes his mind.",
                    "Dutch demande à Hosea d'envoyer quelqu'un de raisonnable (\"sensible\") enterrer le mari de Sadie. Arthur peut préciser que le corps est dans un chariot devant la maison, et Hosea promet d'envoyer quelqu'un. Arthur dit à Dutch qu'il a eu raison ; Dutch répond que c'est bien le moins qu'ils pouvaient faire pour Sadie. Arthur propose en plaisantant d'y envoyer Micah, puis se ravise."),
                two("Dutch and Hosea argue about what comes next. Dutch tells Hosea that he was \"the one with the death wish\". Hosea brings up the Pinkertons and bounty hunters; Dutch says nobody would follow them in this storm. He says the plan is to lie low, make money and get out of the country, but admits he does not know where to yet. He ends by saying they are not done yet.",
                    "Dutch et Hosea se disputent sur la suite. Dutch lance froidement à Hosea que c'est lui qui avait des envies de mort. Hosea évoque les Pinkerton et les chasseurs de primes ; Dutch répond que personne ne serait assez fou pour les suivre dans cette tempête. Le plan, dit-il, est de se faire oublier, de gagner de l'argent puis de quitter le pays, mais il avoue ne pas savoir encore pour où. Il finit par crier qu'ils n'ont pas dit leur dernier mot."),
            ]},
            {"p": two("According to the Camp Events page, Bill, Javier, [[charles-smith|Charles]] and [[simon-pearson|Pearson]] have no camp events in this chapter. The Colter page of the wiki adds that Arthur's health drains quickly if he strays too far from the camp during the chapter.",
                      "Selon la page Camp Events, Bill, Javier, [[charles-smith|Charles]] et [[simon-pearson|Pearson]] n'ont aucune scène de camp dans ce chapitre. La page du wiki consacrée à Colter ajoute que la santé d'Arthur fond rapidement s'il s'éloigne trop du camp pendant le chapitre.")},

            {"h3": two("Deaths", "Morts")},
            {"ul": [
                two("John's bay mare: found dead and mauled on the mountain.",
                    "La jument baie de John : retrouvée morte et dévorée dans la montagne."),
                two("The wolves on the slope and on the ride down, killed by Arthur.",
                    "Les loups de la pente et ceux de la descente, abattus par Arthur."),
            ]},
        ],

        "choices": [
            {"h3": two("On the climb", "Pendant l'ascension")},
            {"ul": [
                two("Arthur's stamina core drains on the climb and the game prompts the player to open the satchel. According to the mission page, if the player does not use provisions, a short scene plays in which Javier gives Arthur a swig of Kentucky bourbon.",
                    "Le noyau d'endurance d'Arthur se vide pendant l'ascension et le jeu invite le joueur à ouvrir sa sacoche. D'après la page de la mission, si le joueur ne consomme aucune provision, une courte scène montre Javier qui lui tend une gorgée de bourbon du Kentucky."),
                two("If the player insists on taking the revolver instead of the shotgun, Javier comments on it, according to the same page.",
                    "Si le joueur s'obstine à prendre le revolver plutôt que le fusil, Javier fait une remarque, selon la même page."),
            ]},

            {"h3": two("The wolves", "Les loups")},
            {"ul": [
                two("Some of the wolves can be killed by trampling them with the horse, which saves shotgun ammunition and still counts for the no-damage objective, according to the mission page.",
                    "On peut tuer certains loups en les piétinant avec son cheval, ce qui économise les cartouches et compte quand même pour l'objectif sans dégât, d'après la page de la mission."),
                two("During the ambush by three wolves, the last remaining wolf runs away if the player fails to kill it in a single shot, according to the page's Gold Medal tips.",
                    "Pendant l'embuscade des trois loups, le dernier loup s'enfuit si le joueur ne l'abat pas d'un seul tir, selon les conseils de médaille d'or de la page."),
                two("If the player does not protect Javier and John from the wolves, a unique death scene plays, according to the same page.",
                    "Si le joueur ne protège pas Javier et John des loups, une scène de mort spécifique se déclenche, selon la même page."),
            ]},

            {"h3": two("Mission failure", "Échec de la mission")},
            {"p": two("According to the mission page, the mission fails if the player:",
                      "D'après la page de la mission, la mission échoue si le joueur :")},
            {"ul": [
                two("assaults, kills or abandons Javier or John, or lets either of them be killed;",
                    "agresse, tue ou abandonne Javier ou John, ou laisse l'un des deux se faire tuer ;"),
                two("kills or abandons his horse;", "tue ou abandonne son cheval ;"),
                two("does not have a Sawed-Off Shotgun (the page notes this concerns replays, when the weapon is not in the current loadout);",
                    "n'a pas de fusil à canon scié (la page précise que cela concerne les rejeux, quand l'arme ne figure pas dans l'équipement en cours) ;"),
                two("dies.", "meurt."),
            ]},
        ],

        "gold": {
            "objectives": [
                two("Kill all the wolves without taking any damage.", "Tuer tous les loups sans subir de dégât."),
                two("Complete with at least 80% accuracy.", "Terminer avec une précision d'au moins 80 %."),
            ],
            "after": [
                {"p": two("According to the same page, a wolf bite fails the first objective, but other damage, such as from a fall, does not count against it. The mission counts toward Gold Rush (70 Gold Medals in story missions) and Best in the West (100% completion).",
                          "Selon la même page, une morsure de loup fait échouer le premier objectif, mais les autres dégâts, une chute par exemple, ne comptent pas. La mission compte pour les trophées Gold Rush (70 médailles d'or dans les missions principales) et Best in the West (100 % de complétion).")},
            ],
        },

        "quotes": [
            {"q": "It's little John... he's got himself caught into a scrape again.",
             "src": two("Arthur, to Abigail, in the main cabin", "Arthur, à Abigail, dans la grande cabane"),
             "fr": "C'est le petit John... il s'est encore fourré dans le pétrin."},
            {"q": "That's quite a scratch you got there.",
             "src": two("Arthur, on finding John on the ledge", "Arthur, en découvrant John sur la corniche"),
             "fr": "Belle égratignure que tu as là."},
            {"q": "Don't die just yet, cowboy.",
             "src": two("Arthur, when John says he is freezing", "Arthur, quand John dit qu'il gèle"),
             "fr": "Meurs pas tout de suite, cow-boy."},
            {"q": "I knew a feller, got bit by a dog. Died an hour later.",
             "src": two("John, when Javier tells him his wounds are just like a dog bite", "John, quand Javier lui dit que ses blessures, c'est comme une morsure de chien"),
             "fr": "J'ai connu un type qui s'est fait mordre par un chien. Mort une heure après."},
            {"q": "None of us are lucky right now.",
             "src": two("Javier, when John says Arthur always calls him lucky", "Javier, quand John dit qu'Arthur le trouve toujours chanceux"),
             "fr": "Personne n'a de chance en ce moment."},
            {"q": "So, freezing, bleeding, starving, damn near getting eaten to death, ain't good enough for you?",
             "src": two("John, when Arthur says he needs a better story for his scar", "John, quand Arthur lui dit qu'il lui faudra une meilleure histoire pour sa cicatrice"),
             "fr": "Geler, saigner, crever de faim et manquer de se faire dévorer, ça te suffit pas ?"},
        ],

        "trivia": [
            two("After Arthur picks up John, a short piece of the main theme of Red Dead Redemption plays, according to the mission page.",
                "Après qu'Arthur a chargé John, un court extrait du thème principal de Red Dead Redemption se fait entendre, d'après la page de la mission."),
            two("On the climb, Arthur and Javier briefly leave the normal map boundaries, into what the wiki presumes to be the Northern Grizzlies, an area named only in Arthur's journal.",
                "Pendant l'ascension, Arthur et Javier sortent brièvement des limites habituelles de la carte, dans ce que le wiki suppose être les Northern Grizzlies, une zone citée seulement dans le journal d'Arthur."),
            two("After the mission, an avalanche closes the mountain north of the ravine where John was found, and the area can no longer be reached, according to the mission page.",
                "Après la mission, une avalanche ferme la montagne au nord du ravin où John a été retrouvé, et le secteur devient inaccessible, selon la page de la mission."),
            two("The title plays on the stage direction \"Exit, pursued by a bear\" from Shakespeare's The Winter's Tale, as does the later mission \"Exit Pursued by a Bruised Ego\", according to the wiki.",
                "Le titre détourne la didascalie \"Exit, pursued by a bear\" du Conte d'hiver de Shakespeare, comme plus tard la mission \"Exit Pursued by a Bruised Ego\", selon le wiki."),
            two("Besides the scars, John is left with a torn jacket and trousers after the wolf attack; by the epilogue he has repaired them, according to the mission page.",
                "Outre les cicatrices, l'attaque des loups laisse à John une veste et un pantalon déchirés ; à l'épilogue, il les a raccommodés, selon la page de la mission."),
        ],
    },
}
