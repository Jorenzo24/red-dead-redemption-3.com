"""Kieran Duffy, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/kieran/ and cov/kieran/m/):
- Red Dead Wiki EN "Kieran Duffy" (Mission Appearances, Companion Activities, Murders Committed, Trivia, Gallery
  captions) and FR "Kieran Duffy" (fr.txt: Apparitions dans les missions, which adds "Eastward Bound", "Money Lending
  and Other Sins I" and "The New South").
- Mission pages: Old Friends; The Aftermath of Genesis (trivia); Eastward Bound (trivia, flagged "citation needed");
  Paying a Social Call (rewards, deaths, quote box, trivia); Who is Not Without Sin; Blood Feuds, Ancient and Modern;
  The Battle of Shady Belle; No, No and Thrice, No (trivia); Horsemen, Apocalypses (deaths, quote box); Goodbye, Dear
  Friend (quote box); companion activity "Fishing (Kieran Duffy)" (quote box, trivia, category Missable Content);
  wiki pages "Errand Boy" (burdock roots, chapter 3 only), "Branwen", "Six Point Cabin", "Paying Respects" (via
  arthur_C), "Camp Events" (tree interactions disabled after "Americans at Rest").
- Transcripts "/dialogues": Old Friends (every Kieran line from the capture is checked word for word against it) and
  Who is Not Without Sin ("Who's that? The Reverend?"). No transcript exists on the wiki for Paying a Social Call,
  Horsemen, Apocalypses, Goodbye, Dear Friend or the fishing activity (checked Oct 2026): the three lines from those
  come from the quote boxes of the mission pages, as in sean_C.
- Real world: Rockstar's series of character portraits and descriptions posted on Twitter on September 6, 2018 and
  reproduced by The Hollywood Reporter on September 7, 2018 (../uncle/fc/thr_descriptions.txt: no entry for Kieran);
  Wikipedia "List of Red Dead Redemption 2 characters" (m/wp_list.txt: caption of the composite of the 23 gang
  members, which does not include him).
Ownership (FIX_RULES), left to other parts: backstory, burial, grave location, Arthur's journal, the Valentine
O'Driscolls, Susan's remark, Bill's warning on the ride (A); personality, names ("O'Driscoll" as a nickname, the
Irish meaning of his names), appearance, weapons (custom Cattleman and its unknown origin, knife), the horse Branwen
as his mount and the look-alike horse sold in Tumbleweed, camp scenes and camp lines (Karen's "baby" line, Mary-Beth,
Bill, Javier, Sean, Jack, the party, the reactions to his death), the infobox quote "folks all seem to die" (B); Pico
Alexander, the IGN preview of the capture, the official guide (D).
Quotes: each line in ONE place; part A paraphrases them without quotation marks. Dutch's Colter lines to him
("Welcome to your new home", "we shoot fellers as need shooting") are not quoted here, so that part B can use them.
Kills: the character page lists one, the unnamed O'Driscoll at Six Point Cabin.
Excluded: the Saint Denis martyr and Dullahan readings of his death (interpretation); the "lose your balls first"
foreshadowing (interpretation; the line has no transcript); the "crush" readings of Bill (speculation); the claim that
he took his revolver from a dead O'Driscoll (the wiki says "it is possible"); Kieran tied up in a wagon in "Eastward
Bound" (unsourced trivia, mentioned only as such in the table); Tom's nickname "Fat Tommy" attributed to Kieran with a
question mark on Tom's page (unverified).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]
K = lambda name, mission, en, fr: [name, mission, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists five story missions of Red Dead Redemption 2 for Kieran, from his capture to the attack that follows his death, and one companion activity. The French Red Dead Wiki adds three more. The table below also includes the missions in which he is only talked about.",
              "Le Red Dead Wiki anglais recense pour Kieran cinq missions principales de Red Dead Redemption 2, de sa capture à l'attaque qui suit sa mort, ainsi qu'une activité de compagnon. Le Red Dead Wiki français en ajoute trois. Le tableau ci-dessous intègre aussi les missions où il n'est qu'évoqué.")},
    {"h4": two("Red Dead Redemption 2, story missions", "Red Dead Redemption 2, missions principales")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Kieran's role", "Rôle de Kieran")], "rows": [
        M("Old Friends", C1,
          "Captured. Seen with [[colm-odriscoll|Colm]] at the O'Driscoll camp, he is chased down and lassoed by [[arthur-morgan|Arthur]] on the way back, then tied up at Colter on [[dutch-van-der-linde|Dutch]]'s orders.",
          "Capturé. Aperçu avec [[colm-odriscoll|Colm]] au camp des O'Driscoll, il est poursuivi et pris au lasso par [[arthur-morgan|Arthur]] sur le chemin du retour, puis attaché à Colter sur ordre de [[dutch-van-der-linde|Dutch]]."),
        M("The Aftermath of Genesis", C1,
          "Mentioned, if the mission is played after \"Old Friends\". Arthur and [[charles-smith|Charles]] talk about the prisoner while hunting.",
          "Mentionné, si la mission est jouée après \"Old Friends\". Arthur et [[charles-smith|Charles]] parlent du prisonnier pendant la chasse."),
        M("Eastward Bound", C1,
          "Listed by the French Red Dead Wiki only. The English mission page mentions him in a single trivia note that gives no source.",
          "Citée par le seul Red Dead Wiki français. La page anglaise de la mission ne le mentionne que dans une anecdote sans source."),
        M("Money Lending and Other Sins I", C2,
          "Listed by the French Red Dead Wiki only; the mission page and its transcript do not mention him.",
          "Citée par le seul Red Dead Wiki français ; ni la page de la mission ni sa transcription ne le mentionnent."),
        M("Paying a Social Call", C2,
          "Mission giver. Threatened with castration, he leads Arthur, [[john-marston|John]] and [[bill-williamson|Bill]] to Six Point Cabin, shoots the O'Driscoll who jumps Arthur in the cabin and is allowed to join the gang. Reward for the player: 110 dollars, a throwing knife and a Double-Barreled Shotgun.",
          "Donneur de la mission. Menacé de castration, il conduit Arthur, [[john-marston|John]] et [[bill-williamson|Bill]] à Six Point Cabin, abat l'O'Driscoll qui se jette sur Arthur dans la cabane et obtient le droit de rejoindre la bande. Récompense pour le joueur : 110 dollars, un couteau de lancer et un fusil à double canon."),
        M("Who is Not Without Sin", C2,
          "At camp. He is one of the gang members who comment as Arthur carries a drunk [[orville-swanson|Reverend Swanson]] to his tent.",
          "Au camp. Il fait partie des membres de la bande qui réagissent quand Arthur ramène sous sa tente le [[orville-swanson|révérend Swanson]], ivre."),
        M("The New South", C3,
          "Listed by the French Red Dead Wiki only.",
          "Citée par le seul Red Dead Wiki français."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Stays behind with [[micah-bell|Micah]] to guard the Clemens Point camp while the others ride to Braithwaite Manor.",
          "Reste avec [[micah-bell|Micah]] pour garder le camp de Clemens Point pendant que les autres chevauchent jusqu'au manoir Braithwaite."),
        M("The Battle of Shady Belle", C3,
          "Present at camp, according to the character page, when [[andrew-milton|Milton]] and [[edgar-ross|Ross]] come to Clemens Point. He moves with the gang to Shady Belle.",
          "Présent au camp, d'après la page du personnage, quand [[andrew-milton|Milton]] et [[edgar-ross|Ross]] se présentent à Clemens Point. Il suit la bande à Shady Belle."),
        M("No, No and Thrice, No", C4,
          "Mentioned, if the mission is played after Jack's return. [[susan-grimshaw|Susan Grimshaw]] notes that he has not been seen for a while.",
          "Mentionné, si la mission est jouée après le retour de Jack. [[susan-grimshaw|Susan Grimshaw]] remarque qu'on ne l'a pas vu depuis un moment."),
        M("Horsemen, Apocalypses", C4,
          "Killed before the mission. His mutilated body is sent into the Shady Belle camp on a horse, just before the O'Driscolls attack. Dutch has him buried afterwards.",
          "Tué avant la mission. Son corps mutilé est renvoyé à cheval dans le camp de Shady Belle, juste avant l'attaque des O'Driscoll. Dutch le fait enterrer ensuite."),
        M("Goodbye, Dear Friend", C6,
          "Mentioned. Before Colm's hanging, Dutch names him to [[sadie-adler|Sadie]] among those the gang has lost because of Colm.",
          "Mentionné. Avant la pendaison de Colm, Dutch le cite à [[sadie-adler|Sadie]] parmi ceux que la bande a perdus à cause de Colm."),
    ]}},
    {"h4": two("Red Dead Redemption 2: companion activity and camp request", "Red Dead Redemption 2 : activité de compagnon et commande du camp")},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Kieran's role", "Rôle de Kieran")], "rows": [
        M("Fishing (Kieran Duffy)", C3,
          "Activity giver. He takes Arthur fishing at Radley's Pasture, on Flat Iron Lake, where a naked swimmer tells them about a giant fish, the Legendary Bluegill. Available after \"The New South\".",
          "Donneur de l'activité. Il emmène Arthur pêcher à Radley's Pasture, sur le lac Flat Iron, où un baigneur nu leur parle d'un poisson géant, le crapet arlequin légendaire. Disponible après \"The New South\"."),
        M(two("Item request", "Commande"), C3,
          "He asks Arthur for two burdock roots for the camp horses. Chapter 3 only; it counts toward the Errand Boy trophy.",
          "Il demande à Arthur deux racines de bardane pour les chevaux du camp. Chapitre 3 uniquement ; la commande compte pour le trophée Errand Boy."),
    ]}},
    {"h3": two("Notable people Kieran kills", "Personnages notables tués par Kieran")},
    {"p": two("The Red Dead Wiki credits Kieran with a single killing.",
              "Le Red Dead Wiki n'attribue qu'une seule victime à Kieran.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K(two("Unnamed O'Driscoll", "O'Driscoll anonyme"), "Paying a Social Call",
          "Shot in the stomach as he holds Arthur on the floor of the cabin at Six Point Cabin.",
          "Abattu d'une balle dans le ventre alors qu'il tient Arthur à terre dans la cabane de Six Point Cabin."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent.")},
    {"h4": two("The capture", "La capture")},
    {"quotes": [
        {"q": two("You got me mixed up with someone else.", "You got me mixed up with someone else."),
         "src": two("Old Friends (RDR2, chapter 1), to Arthur, who has just hogtied him and tells him he is coming along",
                    "Old Friends (RDR2, chapitre 1), à Arthur, qui vient de le ligoter et lui annonce qu'il l'emmène. Traduction : « Vous me confondez avec quelqu'un d'autre. »")},
        {"q": two("It's Kieran.", "It's Kieran."),
         "src": two("Old Friends (RDR2, chapter 1), after first claiming not to know his own name. Once he has given his surname, Arthur answers: \"Well, I ain't gonna lie to you... this is a real bad day for you, Kieran Duffy.\"",
                    "Old Friends (RDR2, chapitre 1), après avoir d'abord prétendu ne pas connaître son propre nom. Une fois qu'il a donné son nom de famille, Arthur répond : \"Well, I ain't gonna lie to you... this is a real bad day for you, Kieran Duffy.\" Traduction : « C'est Kieran. » (« Bon, je vais pas te mentir... c'est vraiment un sale jour pour toi, Kieran Duffy. »)")},
        {"q": two("Why? What are you gonna do to me?", "Why? What are you gonna do to me?"),
         "src": two("Old Friends (RDR2, chapter 1), to Arthur, who replies that it is something he will not like and advises him to save his breath for screaming",
                    "Old Friends (RDR2, chapitre 1), à Arthur, qui lui répond que ça ne va pas lui plaire et lui conseille de garder son souffle pour hurler. Traduction : « Pourquoi ? Qu'est-ce que vous allez me faire ? »")},
        {"q": two("Come on, mister, p-please!", "Come on, mister, p-please!"),
         "src": two("Old Friends (RDR2, chapter 1), tied across Arthur's horse on the ride to Colter",
                    "Old Friends (RDR2, chapitre 1), ligoté en travers du cheval d'Arthur, sur la route de Colter. Traduction : « Allez, m'sieur, s-s'il vous plaît ! »")},
        {"q": two("I've only been running with them a couple of months. I don't know nothing real about them, honest!", "I've only been running with them a couple of months. I don't know nothing real about them, honest!"),
         "src": two("Old Friends (RDR2, chapter 1), to Arthur, who answers: \"Are you trying to test me, is that it? Because I will break every bone in your body.\"",
                    "Old Friends (RDR2, chapitre 1), à Arthur, qui répond : \"Are you trying to test me, is that it? Because I will break every bone in your body.\" Traduction : « Je roule avec eux que depuis deux ou trois mois. Je sais rien de vrai sur eux, je vous jure ! » (« Tu cherches à me tester, c'est ça ? Parce que je vais te briser tous les os du corps. »)")},
        {"q": two("Okay, okay!", "Okay, okay!"),
         "src": two("Old Friends (RDR2, chapter 1), after Arthur forbids him to say one more word. Arthur replies: \"That's two bones, right there.\"",
                    "Old Friends (RDR2, chapitre 1), après qu'Arthur lui a interdit de dire un mot de plus. Arthur réplique : \"That's two bones, right there.\" Traduction : « D'accord, d'accord ! » (« Ça fait deux os, ça. »)")},
        {"q": two("Don't hurt me, please.", "Don't hurt me, please."),
         "src": two("Old Friends (RDR2, chapter 1), as Arthur carries him into the Colter camp. Arthur answers: \"Oh, don't worry, they're real nice.\"",
                    "Old Friends (RDR2, chapitre 1), quand Arthur le porte dans le camp de Colter. Arthur répond : \"Oh, don't worry, they're real nice.\" Traduction : « Me faites pas de mal, s'il vous plaît. » (« Oh, t'en fais pas, ils sont vraiment gentils. »)")},
    ]},
    {"h4": two("In the gang", "Dans la bande")},
    {"quotes": [
        {"q": two("Who's that? The Reverend?", "Who's that? The Reverend?"),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), as Arthur carries a drunk Reverend Swanson through camp",
                    "Who is Not Without Sin (RDR2, chapitre 2), quand Arthur traverse le camp en portant le révérend Swanson, ivre. Traduction : « C'est qui, ça ? Le révérend ? »")},
    ]},
    {"h4": two("Said to him and about him", "Ce qu'on lui dit, ce qu'on dit de lui")},
    {"quotes": [
        {"q": two("See? This is why you're an O'Driscoll, O'Driscoll. Colm's a sneak thief and a killer... Dutch is... Dutch is more like a teacher.", "See? This is why you're an O'Driscoll, O'Driscoll. Colm's a sneak thief and a killer... Dutch is... Dutch is more like a teacher."),
         "src": two("John Marston to Kieran, Paying a Social Call (RDR2, chapter 2), on the ride to Six Point Cabin (quote box of the mission page)",
                    "John Marston à Kieran, Paying a Social Call (RDR2, chapitre 2), sur la route de Six Point Cabin (citation en exergue de la page de la mission). Traduction : « Tu vois ? C'est pour ça que t'es un O'Driscoll, l'O'Driscoll. Colm, c'est un voleur sournois et un tueur... Dutch, lui... Dutch, c'est plutôt un professeur. »")},
        {"q": two("You lost your husband. I lost my darling, Annabelle. That poor boy, Kieran. We've all lost something because of Colm. And that is why we will shepherd him to eternity.", "You lost your husband. I lost my darling, Annabelle. That poor boy, Kieran. We've all lost something because of Colm. And that is why we will shepherd him to eternity."),
         "src": two("Dutch van der Linde to Sadie Adler, Goodbye, Dear Friend (RDR2, chapter 6), before Colm's hanging (quote box of the mission page)",
                    "Dutch van der Linde à Sadie Adler, Goodbye, Dear Friend (RDR2, chapitre 6), avant la pendaison de Colm (citation en exergue de la page de la mission). Traduction : « Vous avez perdu votre mari. J'ai perdu ma chère Annabelle. Ce pauvre Kieran. Nous avons tous perdu quelque chose à cause de Colm. Et c'est pour ça que nous allons le conduire jusqu'à l'éternité. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("The O'Driscoll character models and the prostitutes seen at Six Point Cabin in \"Paying a Social Call\" appear in that mission only. When Arthur comes back to the hideout later, ordinary O'Driscolls occupy it, and a new gunfight is possible until chapter 6, when the place is empty.",
            "Les modèles de personnages des O'Driscoll et les prostituées présents à Six Point Cabin dans \"Paying a Social Call\" n'apparaissent que dans cette mission. Si Arthur revient plus tard dans la planque, il y trouve des O'Driscoll ordinaires et peut de nouveau les affronter, jusqu'au chapitre 6, où les lieux sont déserts."),
        two("If Arthur later returns alone to the spot where he and Kieran met the swimmer and starts fishing, the man appears again and tells him about another unusually large fish. According to the activity page of the Red Dead Wiki, a giant largemouth bass can then be caught in the same area.",
            "Si Arthur revient seul à l'endroit où Kieran et lui ont croisé le baigneur et se remet à pêcher, l'homme réapparaît et lui parle d'un autre poisson d'une taille inhabituelle. D'après la page de l'activité sur le Red Dead Wiki, un achigan à grande bouche géant peut alors être pêché dans le même secteur."),
        two("In his fishing trip, the naked swimmer only mentions the giant fish if Arthur greets him. If Arthur insults him instead of greeting him, the swimmer says nothing about the fish, and Kieran finds the second spot on his own.",
            "Pendant la partie de pêche, le baigneur nu ne parle du poisson géant que si Arthur le salue. Si Arthur l'insulte au lieu de le saluer, le baigneur ne dit rien du poisson, et Kieran trouve lui-même le second coin de pêche."),
        two("The Red Dead Wiki classes the fishing trip, a chapter 3 activity, as missable content.",
            "Le Red Dead Wiki range la partie de pêche, une activité du chapitre 3, parmi les contenus manquables."),
        two("His camp scenes tied to the tree stop for good after \"Americans at Rest\", and all his camp scenes end after \"Angelo Bronte, A Man of Honor\".",
            "Ses scènes de camp attaché à l'arbre disparaissent définitivement après \"Americans at Rest\", et toutes ses scènes de camp prennent fin après \"Angelo Bronte, A Man of Honor\"."),
        two("Kieran's grave is one of those that count toward the Paying Respects trophy.",
            "La tombe de Kieran fait partie de celles qui comptent pour le trophée Paying Respects."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Kieran was left out of the series of character portraits and descriptions that Rockstar posted on Twitter on September 6, 2018, and that The Hollywood Reporter reproduced the next day. He is also absent from the composite of 23 gang members' official art designs that illustrates Wikipedia's list of the game's characters. The Red Dead Wiki notes that, apart from Davey Callander, Cleet and Joe, he is the only gang member seen alive in the game who did not get promotional artwork with a quote of his own.",
              "Kieran ne figure pas dans la série de portraits et de descriptions de personnages que Rockstar publie sur Twitter le 6 septembre 2018 et que The Hollywood Reporter reprend le lendemain. Il manque aussi au montage des illustrations officielles de 23 membres de la bande qui ouvre la liste des personnages du jeu sur Wikipédia. Le Red Dead Wiki relève qu'à part Davey Callander, Cleet et Joe, il est le seul membre de la bande vu vivant dans le jeu à ne pas avoir eu d'illustration promotionnelle accompagnée d'une de ses répliques.")},
]
