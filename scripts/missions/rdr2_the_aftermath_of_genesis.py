"""The Aftermath of Genesis (RDR2, Chapter 1, mission 3 of the wiki's order), mission page (24 Oct 2026).

Can be played before or after "Old Friends" (mission 3/4). Prev/next follow the
order listed by the Red Dead Wiki: 3 = The Aftermath of Genesis, 4 = Old Friends.

Source register:
- Our v3 Chapter 1 guide, EN story/rdr2-chapter-1-colter/ and FR
  fr/histoire/rdr2-chapitre-1-colter/ (fixed 24 Oct 2026 after two adversarial
  fact-checks and a coverage check): section "3. The Aftermath of Genesis", the
  matching row of "Chapter 1 at a glance" (giver, companion, location, Gold
  Medal objectives), "Background" (Pearson's supplies), "Trivia" (first deer
  tracked without Eagle Eye, compendium unlocked). Story wording and facts are
  taken from it; the FR text is taken from the FR guide.
- Red Dead Wiki mission page "The Aftermath of Genesis" (scripts/v3/work/_m/
  The_Aftermath_of_Genesis.txt): infobox (start/end Colter, giver Pearson,
  location Grizzlies West, rewards Bow, 22 arrows, Assorted Salted Offal, Eagle
  Eye, next mission), Gold Medal objectives, mission failure conditions, deaths
  (two deer), trivia (Eagle Eye, honor if a deer bleeds out, other weapon upsets
  Charles, bear cannot be killed, order-dependent dialogue, Hosea at the
  butcher's table, Dead Eye if played after "Old Friends", continues into "Who
  the Hell is Leviticus Cornwall?").
- Red Dead Wiki transcript "The Aftermath of Genesis/dialogues" (scripts/v3/
  work/_m/The_Aftermath_of_Genesis_dialogues.txt): every quoted line was checked
  against it, including Arthur's "we can eat you... you're the fattest", the
  bear lines ("push our luck", "have you seen the size of it?") and the
  skinning scene ("Do I get to skin you?", "they always said you were a
  butcher").

Left out: the wiki's reading of Charles's burned hand as "a reference to Red
Harlow" (interpretation), the frozen-AI glitch, Gold Medal tips, video links.
The wiki story says Charles burned his hand escaping from Blackwater; the
transcript only has "Stupid mistake", so no cause is given.
"""


def two(en, fr): return {"en": en, "fr": fr}


MISSION = {
    "slug": "the-aftermath-of-genesis",
    "name": "The Aftermath of Genesis",
    "game": "rdr2",
    "chapter": 1,
    "number": 3,
    "chapter_total": 6,
    "story_order": 3,
    "publishDate": "2026-10-24",
    "updated": "2026-10-24",
    "prev": {"slug": "enter-pursued-by-a-memory", "name": "Enter, Pursued by a Memory"},
    "next": {"slug": "old-friends", "name": "Old Friends"},

    "chips": [two("Playable before or after Old Friends", "Avant ou après Old Friends")],

    "meta_desc": two(
        "The Aftermath of Genesis, a Chapter 1 mission of Red Dead Redemption 2: Charles teaches Arthur to hunt deer with a bow, the grizzly, rewards, Gold Medal objectives and quotes.",
        "The Aftermath of Genesis, mission du chapitre 1 de Red Dead Redemption 2 : Charles apprend à Arthur à chasser le cerf à l'arc, le grizzly, récompenses, médaille d'or et citations."),
    "og_desc": two(
        "Arthur's first hunt with Charles Smith in the Grizzlies, step by step, and how the dialogue changes with the order of play.",
        "La première chasse d'Arthur avec Charles Smith dans les Grizzlies, étape par étape, et ce qui change selon l'ordre des missions."),

    "facts": {
        "giver": two("[[simon-pearson|Simon Pearson]]", "[[simon-pearson|Simon Pearson]]"),
        "location": two("Starts and ends at Colter; Grizzlies West, Ambarino (deer tracks near Beartooth Beck, according to the mission page)",
                        "Départ et retour à Colter ; Grizzlies West, Ambarino (traces de cerfs près de Beartooth Beck, selon la page de la mission)"),
        "characters": two("[[arthur-morgan|Arthur Morgan]], [[charles-smith|Charles Smith]], [[simon-pearson|Simon Pearson]], [[uncle|Uncle]]",
                          "[[arthur-morgan|Arthur Morgan]], [[charles-smith|Charles Smith]], [[simon-pearson|Simon Pearson]], [[uncle|Uncle]]"),
        "unlocks": two("Eagle Eye. Played after [[m:old-friends|Old Friends]], it continues directly into [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]]; played first, it leaves Old Friends to play",
                       "Eagle Eye. Jouée après [[m:old-friends|Old Friends]], elle enchaîne directement sur [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]] ; jouée en premier, il reste Old Friends à faire"),
        "rewards": two("Bow, 22 arrows, Assorted Salted Offal, Eagle Eye ability",
                       "Arc, 22 flèches, Assorted Salted Offal (abats salés), capacité Eagle Eye"),
    },

    "intro": [
        two("\"The Aftermath of Genesis\" is a story mission of Red Dead Redemption 2 in <a href=\"/story/rdr2-chapter-1-colter/\">Chapter 1: Colter</a>. It is given by [[simon-pearson|Simon Pearson]] and starts and ends at Colter. It can be played before or after [[m:old-friends|Old Friends]]: the Red Dead Wiki lists it third of the chapter's six missions, Old Friends fourth.",
            "\"The Aftermath of Genesis\" est une mission principale de Red Dead Redemption 2, au <a href=\"/fr/histoire/rdr2-chapitre-1-colter/\">chapitre 1 : Colter</a>. Donnée par [[simon-pearson|Simon Pearson]], elle part de Colter et y revient. Elle peut se jouer avant ou après [[m:old-friends|Old Friends]] : le Red Dead Wiki la place en troisième position des six missions du chapitre, Old Friends en quatrième."),
        two("With the camp short of food, [[charles-smith|Charles Smith]] takes [[arthur-morgan|Arthur Morgan]] hunting and teaches him to use a bow. They bring two deer back to Pearson.",
            "Le camp manquant de vivres, [[charles-smith|Charles Smith]] emmène [[arthur-morgan|Arthur Morgan]] à la chasse et lui apprend à tirer à l'arc. Ils rapportent deux cerfs à Pearson."),
    ],

    "sections": {
        "story": [
            {"h3": two("Pearson's kitchen", "La cuisine de Pearson")},
            {"p": two("In the camp's kitchen, Pearson tells Arthur they have a few cans of food and a rabbit for ten or twelve people. He says he could not bring supplies when they ran from Blackwater. Arthur answers that when government agents are hunting you, shopping trips get cut short, and that if need be they can eat Pearson: \"you're the fattest.\" Pearson starts a story about being stranded at sea for fifty days in the Navy, which Arthur refuses to hear. He says he sent [[lenny-summers|Lenny]] and [[bill-williamson|Bill]] hunting and they found nothing. Charles cuts the argument short: \"Enough of this. We'll go find something.\"",
                      "Dans la cuisine du camp, Pearson explique à Arthur qu'il ne reste que quelques conserves et un lapin pour dix ou douze personnes. Il n'a pas pu emporter de provisions en fuyant Blackwater, dit-il. Arthur répond que quand des agents du gouvernement vous traquent, on écourte les courses, et qu'au besoin on pourra toujours manger Pearson : \"you're the fattest\" (c'est toi le plus gras). Pearson entame une histoire de cinquante jours à la dérive du temps où il était dans la marine, qu'Arthur refuse d'écouter. Il ajoute qu'il a envoyé [[lenny-summers|Lenny]] et [[bill-williamson|Bill]] chasser, sans résultat. Charles coupe court : \"Enough of this. We'll go find something.\" (Ça suffit. On va trouver quelque chose.)")},
            {"p": two("Arthur points out Charles's injured hand. Charles says he burned it, a \"stupid mistake\", and expects it to heal in a day or two. Pearson throws Arthur a can of \"Assorted Salted Offal\" for the road. Since Charles cannot draw a bow, he gives his own to Arthur and explains that a gun would scare every animal for miles.",
                      "Arthur lui fait remarquer sa main blessée. Charles explique qu'il se l'est brûlée, une \"stupid mistake\" (une bêtise), et pense guérir d'ici un jour ou deux. Pearson lance à Arthur une boîte d'\"Assorted Salted Offal\", des abats salés, pour la route. Comme il ne peut pas bander un arc, Charles confie le sien à Arthur et lui explique qu'un coup de fusil ferait fuir tout le gibier à des kilomètres.")},

            {"h3": two("The hunt", "La chasse")},
            {"p": two("On the ride, Charles says he still does not really know what happened on the boat; Arthur says [[javier-escuella|Javier]] told him a bit, \"but... it sure weren't good.\" Charles finds deer tracks near a stream, Beartooth Beck according to the mission page, and teaches Arthur to follow them on foot, stay low and aim for the neck or head. He tells Arthur to \"focus\" to see the tracks, which introduces Eagle Eye. Arthur kills two deer, and the two men carry one each to their horses.",
                      "En chemin, Charles avoue ne toujours pas bien savoir ce qui s'est passé sur le bateau ; Arthur répond que [[javier-escuella|Javier]] lui en a raconté un peu, et que ce n'était pas joli. Près d'un cours d'eau, Beartooth Beck selon la page de la mission, Charles repère des traces de cerfs et apprend à Arthur à les suivre à pied, à rester baissé et à viser le cou ou la tête. Pour voir les traces, il lui dit de se concentrer (\"focus\") : c'est l'introduction d'Eagle Eye. Arthur abat deux cerfs, et chacun en charge un sur son cheval.")},

            {"h3": two("The ride back", "Le retour")},
            {"p": two("On the way back, Charles worries that even off the mountain they will \"still have a big price on our heads.\" Arthur answers that it is a big country and that \"Dutch and Hosea will have a plan.\" He complains that Pearson has had a bottle in his hand since Blackwater and did not bring \"a crumb of food.\"",
                      "Au retour, Charles s'inquiète : même une fois descendus de la montagne, ils auront toujours une grosse prime sur la tête. Arthur répond que le pays est grand et que Dutch et Hosea auront un plan. Il se plaint que Pearson n'a pas lâché sa bouteille depuis Blackwater et n'a pas emporté une miette de nourriture.")},
            {"p": two("The next exchange depends on the order of play (see Choices and variants). In both versions Charles says [[sadie-adler|Sadie]] has \"a wild look in her eye\", and Arthur says she has lost her husband, her home and everything she had, and may have family somewhere. Arthur explains that the gang has been fighting the O'Driscolls over scores for years and that [[colm-odriscoll|Colm]] and Dutch \"go way back, and not in a good way.\"",
                      "La suite de l'échange change selon l'ordre des missions (voir Choix et variantes). Dans les deux cas, Charles trouve à [[sadie-adler|Sadie]] \"a wild look in her eye\" (un regard sauvage), et Arthur rappelle qu'elle a perdu son mari, sa maison et tout ce qu'elle avait, et qu'elle a peut-être de la famille quelque part. Arthur explique que la bande se dispute des coups avec les O'Driscoll depuis des années, et que [[colm-odriscoll|Colm]] et Dutch se connaissent de longue date, et pas en bien.")},

            {"h3": two("The grizzly", "Le grizzly")},
            {"p": two("A grizzly bear blocks the trail. Arthur notes that it has a lot of meat on it. Charles answers: \"We've got enough here, no need to push our luck.\" He adds: \"Spring storms like this are the worst for animals that sleep all winter.\" They go around it, off the trail. According to the mission page, the bear cannot be killed in this mission.",
                      "Un grizzly barre le chemin. Arthur fait remarquer qu'il y a de la viande sur une bête pareille. Charles répond : \"We've got enough here, no need to push our luck.\" (On en a assez, inutile de tenter le diable.) Il ajoute : \"Spring storms like this are the worst for animals that sleep all winter.\" (Ces tempêtes de printemps, c'est le pire pour les bêtes qui hibernent.) Ils le contournent en quittant la piste. Selon la page de la mission, l'ours ne peut pas être tué ici.")},

            {"h3": two("Charles and Arthur", "Charles et Arthur")},
            {"p": two("Arthur notes that Charles has been with them for five or six months. Asked whether he expected the Blackwater mess, Charles answers: \"Sooner or later a job's going to go wrong. Nature of life.\" He says he rode alone for a long time and is done with it, and that Dutch treats him fair: \"And for a feller with a black father and an Indian mother, that ain't normally the case.\"",
                      "Arthur fait remarquer que Charles est avec eux depuis cinq ou six mois. Quand Arthur parie qu'il ne s'attendait pas au fiasco de Blackwater, Charles répond : \"Sooner or later a job's going to go wrong. Nature of life.\" (Tôt ou tard, un coup finit par mal tourner. C'est la vie.) Il dit avoir longtemps roulé seul et en avoir fini avec ça, et que Dutch le traite correctement : \"And for a feller with a black father and an Indian mother, that ain't normally the case.\" (Et pour un type né d'un père noir et d'une mère indienne, c'est loin d'être la règle.)")},
            {"p": two("Asked in return, Arthur says he has been with Dutch for \"Twenty years, something like that. Since I was a boy.\" Dutch taught him and [[john-marston|John]] to read, and taught him a few other things, \"him and Hosea.\" Arthur adds: \"Dutch saved me, saved most of us.\"",
                      "À son tour, Arthur dit être avec Dutch depuis \"Twenty years, something like that. Since I was a boy.\" (Vingt ans, à peu près. Depuis que je suis gamin.) Dutch lui a appris à lire, à lui comme à [[john-marston|John]], et quelques autres choses, avec Hosea. Arthur ajoute que Dutch les a sauvés, lui et la plupart des autres.")},
            {"p": two("Charles then asks about Arthur's new horse. Arthur thanks him for lending him Taima. Charles says he does not know what Dutch would do if something happened to his horse, the Count; Arthur says the same of Bill and his horse Brown Jack. Arthur adds that the Count once bucked him off and \"won't take nobody but\" Dutch.",
                      "Charles demande ensuite à Arthur comment va son nouveau cheval. Arthur le remercie de lui avoir prêté Taima. Charles se demande ce que ferait Dutch s'il arrivait quelque chose à son cheval, le Count ; Arthur en dit autant de Bill et de son cheval, Brown Jack. Il raconte que le Count l'a désarçonné le jour où il a voulu le monter, et qu'il n'accepte personne d'autre que Dutch.")},

            {"h3": two("Back at Colter", "Retour à Colter")},
            {"p": two("At Colter, [[uncle|Uncle]] is loitering at Pearson's table and leaves after trading jabs with Arthur. Pearson hands round a bottle of Navy rum. Charles leaves to rest his hand: \"This isn't really a job for a man with a burnt hand.\" Pearson asks Arthur to help with the skinning; Arthur asks: \"Do I get to skin you?\" Arthur skins a deer, and Pearson says: \"they always said you were a butcher.\" He tells Arthur that pelts sell in almost any town, and asks him to bring anything else he catches. Arthur answers that right now he is just looking to get off the mountain alive.",
                      "À Colter, [[uncle|Uncle]] traîne près de l'étal de Pearson et s'en va après quelques piques échangées avec Arthur. Pearson fait circuler une bouteille de rhum de la marine. Charles part reposer sa main : ce n'est pas un travail, dit-il, pour un homme qui a la main brûlée. Pearson demande à Arthur de l'aider à dépecer ; Arthur lui demande s'il a le droit de le dépecer, lui. Arthur dépèce un cerf, et Pearson remarque qu'on a toujours dit de lui qu'il était un boucher. Il lui explique que les peaux se vendent dans presque toutes les villes, et lui demande de lui rapporter tout ce qu'il chassera. Arthur répond que pour l'instant, il cherche surtout à quitter cette montagne vivant.")},

            {"h3": two("Deaths", "Morts")},
            {"ul": [
                two("Two deer, hunted by Arthur at Pearson's request.",
                    "Deux cerfs, chassés par Arthur à la demande de Pearson."),
            ]},
        ],

        "choices": [
            {"h3": two("Order of play: before or after Old Friends", "Ordre des missions : avant ou après Old Friends")},
            {"ul": [
                two("If [[m:old-friends|Old Friends]] is done first, Charles notes on the ride back that the gang has picked up two more mouths to feed, and Arthur says the O'Driscoll prisoner, [[kieran-duffy|Kieran Duffy]], will get nothing but the can of salted offal. Charles adds that Sadie may deal with the O'Driscoll for them.",
                    "Si [[m:old-friends|Old Friends]] a déjà été jouée, Charles note au retour que la bande a deux bouches de plus à nourrir, et Arthur répond que le prisonnier O'Driscoll, [[kieran-duffy|Kieran Duffy]], n'aura rien d'autre que la boîte d'abats. Charles ajoute que Sadie pourrait bien s'occuper elle-même de l'O'Driscoll."),
                two("Played after Old Friends, the mission continues directly into [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]]. Dead Eye is then already unlocked and, according to the mission page, can be used to get clean kills on the deer.",
                    "Jouée après Old Friends, la mission enchaîne directement sur [[m:who-the-hell-is-leviticus-cornwall|Who the Hell is Leviticus Cornwall?]]. Le Dead Eye est alors déjà débloqué et, d'après la page de la mission, peut servir à abattre proprement les cerfs."),
                two("Played before Old Friends, the mission leaves Hosea at the butcher's table, where Arthur can have a conversation with him, according to the mission page.",
                    "Jouée avant Old Friends, la mission laisse Hosea près de l'étal de boucher, où Arthur peut avoir une conversation avec lui, selon la page de la mission."),
            ]},

            {"h3": two("The hunt", "La chasse")},
            {"ul": [
                two("Arthur can use another weapon than the bow to kill the deer without failing the mission, but Charles gets upset, according to the mission page.",
                    "Arthur peut tuer les cerfs avec une autre arme que l'arc sans faire échouer la mission, mais Charles s'en agace, d'après la page de la mission."),
                two("Wounding a deer and letting it bleed out, instead of putting it out of its misery, can lower Arthur's honor, according to the same page.",
                    "Blesser un cerf et le laisser se vider de son sang, au lieu de l'achever, peut faire baisser l'honneur d'Arthur, selon la même page."),
            ]},

            {"h3": two("The grizzly", "Le grizzly")},
            {"p": two("If the player points a weapon at the bear, Charles says: \"That's a bad idea... have you seen the size of it?\" The bear cannot be killed, only scared off, according to the mission page, and Charles is frustrated if the player shoots at it anyway.",
                      "Si le joueur pointe une arme sur l'ours, Charles lance : \"That's a bad idea... have you seen the size of it?\" (Mauvaise idée... t'as vu la taille de la bête ?) L'ours ne peut pas être tué, seulement effrayé, d'après la page de la mission, et Charles s'agace si le joueur lui tire dessus malgré tout.")},

            {"h3": two("Mission failure", "Échec de la mission")},
            {"p": two("According to the mission page, the mission fails if the player:",
                      "D'après la page de la mission, la mission échoue si le joueur :")},
            {"ul": [
                two("assaults, kills or abandons Charles, or lets him be killed;",
                    "agresse, tue ou abandonne Charles, ou le laisse se faire tuer ;"),
                two("lets the deer escape;", "laisse les cerfs s'échapper ;"),
                two("ruins the deer carcasses, for example by shooting them;",
                    "abîme les carcasses des cerfs, par exemple en leur tirant dessus ;"),
                two("kills or abandons his horse;", "tue ou abandonne son cheval ;"),
                two("dies.", "meurt."),
            ]},
        ],

        "gold": {
            "objectives": [
                two("Kill each deer with one arrow.", "Tuer chaque cerf d'une seule flèche."),
                two("Do not spook either deer.", "N'effrayer aucun des deux cerfs."),
                two("Get a clean kill on the second deer.", "Abattre proprement le second cerf."),
            ],
        },

        "quotes": [
            {"q": "We'll survive... we always have... and if needs be, we can eat you... you're the fattest.",
             "src": two("Arthur, to Pearson, about the lack of food", "Arthur, à Pearson, à propos du manque de vivres"),
             "fr": "On survivra... on a toujours survécu... et au besoin, on te mangera, c'est toi le plus gras."},
            {"q": "\"Assorted, salted offal.\" Starving would be preferable.",
             "src": two("Arthur, reading the can Pearson throws him", "Arthur, en lisant la boîte que lui lance Pearson"),
             "fr": "\"Abats salés assortis.\" Je préférerais encore crever de faim."},
            {"q": "Enough of this. We'll go find something.",
             "src": two("Charles, ending the argument in the kitchen", "Charles, pour clore la dispute dans la cuisine"),
             "fr": "Ça suffit. On va trouver quelque chose."},
            {"q": "Use a gun... and we'll scare off every animal for miles around.",
             "src": two("Charles, handing Arthur the bow", "Charles, en confiant l'arc à Arthur"),
             "fr": "Avec un fusil, on fera fuir toutes les bêtes à des kilomètres."},
            {"q": "Spring storms like this are the worst for animals that sleep all winter.",
             "src": two("Charles, about the grizzly", "Charles, à propos du grizzly"),
             "fr": "Ces tempêtes de printemps, c'est le pire pour les bêtes qui hibernent."},
            {"q": "Sooner or later a job's going to go wrong. Nature of life.",
             "src": two("Charles, about Blackwater", "Charles, à propos de Blackwater"),
             "fr": "Tôt ou tard, un coup finit par mal tourner. C'est la vie."},
            {"q": "And for a feller with a black father and an Indian mother, that ain't normally the case.",
             "src": two("Charles, on being treated fair by Dutch", "Charles, sur la façon dont Dutch le traite"),
             "fr": "Et pour un type né d'un père noir et d'une mère indienne, c'est loin d'être la règle."},
            {"q": "Twenty years, something like that. Since I was a boy.",
             "src": two("Arthur, on how long he has been with Dutch", "Arthur, sur ses années auprès de Dutch"),
             "fr": "Vingt ans, à peu près. Depuis que je suis gamin."},
            {"q": "Dutch saved me, saved most of us.",
             "src": two("Arthur, to Charles", "Arthur, à Charles"),
             "fr": "Dutch m'a sauvé, il nous a sauvés presque tous."},
            {"q": "Do I get to skin you?",
             "src": two("Arthur, when Pearson asks for help with the skinning", "Arthur, quand Pearson lui demande de l'aider à dépecer"),
             "fr": "Et toi, j'ai le droit de te dépecer ?"},
        ],

        "trivia": [
            two("The mission unlocks Eagle Eye, but the first deer can be tracked by its prints in the snow without it, according to the mission page.",
                "La mission débloque Eagle Eye, mais on peut pister le premier cerf grâce à ses empreintes dans la neige, sans s'en servir, selon la page de la mission."),
            two("The compendium, which can be opened during [[m:outlaws-from-the-west|Outlaws from the West]], stays locked until this mission, according to the mission page of Outlaws from the West.",
                "Le compendium, consultable pendant [[m:outlaws-from-the-west|Outlaws from the West]], reste verrouillé jusqu'à cette mission, selon la page d'Outlaws from the West."),
            two("When Arthur asks whether they should take the bear for its meat, Charles says the deer are enough and, according to the mission page, that they could not carry both.",
                "Quand Arthur propose de prendre l'ours pour sa viande, Charles répond que les cerfs suffisent et, d'après la page de la mission, qu'ils ne pourraient pas tout porter."),
        ],
    },
}
