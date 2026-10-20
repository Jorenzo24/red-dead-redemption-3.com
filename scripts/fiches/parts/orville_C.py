"""Orville Swanson, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/orville/, cov/orville/m/
and cov/orville/w/):
- Red Dead Wiki EN "Orville Swanson" (Mission Appearances, Quotes, Trivia, Gallery) and FR "Orville Swanson" (fr.txt:
  Apparitions dans les missions, same thirteen missions minus "Red Dead Redemption", Anecdotes: the first line).
- Mission pages: Outlaws from the West; Who the Hell is Leviticus Cornwall?; Eastward Bound; Who is Not Without Sin
  (giver, objectives, Gold Medal objectives, failure conditions, trivia: John 8:7, beating to death if ignored, "A
  Quiet Time" remark, gunshot, riding into camp, the watch, PC/console trivia); A Strange Kindness; Blessed are the
  Peacemakers; Blood Feuds, Ancient and Modern; The Battle of Shady Belle; Horsemen, Apocalypses (trivia: Hosea's
  room); Fleeting Joy; That's Murfree Country; A Rage Unleashed (giver); The Fine Art of Conversation (trivia: honor
  and "Of Men and Angels" condition, recalled lines, PC replay, Swanson and Trelawny gone); Red Dead Redemption
  (mission) (recalled line, transcript list of flashback lines).
- Transcripts "/dialogues": Outlaws from the West, Who the Hell is Leviticus Cornwall?, Eastward Bound, Who is Not
  Without Sin, Blessed are the Peacemakers (every quoted Swanson line is checked word for word against them), and
  Red Dead Redemption (mission)/dialogues, which lists "Save who you can and let the rest rot, and look after
  yourself." among Arthur's recalled lines. "You lived your way, you'll die your way." comes from the quote section of
  the character page and the trivia of "The Fine Art of Conversation" (no transcript exists for that mission, checked
  Oct 2026), as sean_C does for missions without transcripts.
- Real world: Rockstar Games tweets of September 6, 2018 (portrait and description of "Reverend Swanson"), reproduced
  by The Hollywood Reporter on September 7, 2018 (../uncle/fc/thr_descriptions.txt); Wikipedia "List of Red Dead
  Redemption 2 characters" (m/wp_list.txt: caption of the composite of 23 gang members, front row "Pearson, Uncle,
  Swanson, Sean").
Ownership (FIX_RULES): story events (A); Rockstar's description text, the official guide, personality, names,
appearance, the fake bible with its morphine kit, the soiled undergarments, camp scenes and camp lines (Isaiah, the
fire speech, Javier's prayer, Hosea's confession talk, Micah, Strauss, Bill, Uncle, the party, the ghost in the
swamp, the Beaver Hollow talks) go to B; Sean Haberle and reception go to D. Camp lines (the fire speech, "not too late
to repent", "He's doomed") are left to B. Lines quoted here are paraphrased in A without quotation marks.
Kills: the character page has no killings section; no kills table and no claim about it in the text.
Excluded: the claim that Swanson, Pearson and Molly are the only members never shown committing a crime, "excluding
Swanson's attempt to steal from the toll box" (no source for the toll box; judgment); the wiki's reading of "You're
doomed" as foreshadowing Javier's death (interpretation); the soiled undergarments "as a side effect of his
addictions" (interpretation; appearance is part B anyway); the multiplayer or Red Dead Online presence (none found).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
E2 = two("Epilogue 2", "Épilogue 2")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists fourteen missions of Red Dead Redemption 2 for Swanson, two of which he gives himself, and in the last of them only his voice is heard. The French Red Dead Wiki lists the same missions except the last. The table below also includes the missions in which he is only talked about.",
              "Le Red Dead Wiki anglais recense pour Swanson quatorze missions de Red Dead Redemption 2, dont deux qu'il donne lui-même ; dans la dernière, on n'entend que sa voix. Le Red Dead Wiki français cite les mêmes, sauf la dernière. Le tableau ci-dessous intègre aussi les missions où il n'est qu'évoqué.")},
    {"h4": two("Red Dead Redemption 2, story missions", "Red Dead Redemption 2, missions principales")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Swanson's role", "Rôle de Swanson")], "rows": [
        M("Outlaws from the West", C1,
          "In the snowstorm, he tells [[dutch-van-der-linde|Dutch]] that Davey Callander is dying. At Colter, he comforts [[abigail-marston|Abigail]] after Davey's death.",
          "Dans la tempête, il prévient [[dutch-van-der-linde|Dutch]] que Davey Callander est mourant. À Colter, il réconforte [[abigail-marston|Abigail]] après la mort de Davey."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "At the bedside of the wounded [[john-marston|John]] when [[arthur-morgan|Arthur]] speaks to him in the cabin; he leaves after Arthur's joke.",
          "Au chevet de [[john-marston|John]], blessé, quand [[arthur-morgan|Arthur]] lui adresse la parole dans la cabane ; il sort après la plaisanterie d'Arthur."),
        M("Eastward Bound", C1,
          "Loads a wagon with [[bill-williamson|Bill]] before the departure. At Horseshoe Overlook, Dutch tells him and [[uncle|Uncle]] that the gang will carry no more passengers.",
          "Charge un chariot avec [[bill-williamson|Bill]] avant le départ. À Horseshoe Overlook, Dutch lui fait savoir, ainsi qu'à [[uncle|Uncle]], que la bande ne transportera plus de passagers."),
        M("Who is Not Without Sin", C2,
          "Mission giver. Drunk at Flatneck Station, he wanders off, is beaten by a stranger and gets his foot stuck on the railway bridge at Bard's Crossing; Arthur saves him from a train and brings him back to camp. Gold Medal: win two hands of poker and bring him back within 2 minutes 5 seconds. The mission fails if he is assaulted, killed or abandoned.",
          "Donneur de la mission. Ivre à Flatneck Station, il s'éclipse, se fait rosser par un inconnu et se coince le pied sur le pont ferroviaire de Bard's Crossing ; Arthur le sauve d'un train et le ramène au camp. Médaille d'or : gagner deux mains de poker et le ramener en moins de 2 minutes et 5 secondes. La mission échoue s'il est agressé, tué ou abandonné."),
        M("A Strange Kindness", C2,
          "Listed by the Red Dead Wiki; the mission page does not name him. The gang moves to Clemens Point at the end.",
          "Citée par le Red Dead Wiki ; la page de la mission ne le nomme pas. La bande s'installe à Clemens Point à la fin."),
        M("Blessed are the Peacemakers", C3,
          "Called by Dutch when Arthur returns wounded; weeks later, he visits Arthur during his recovery.",
          "Appelé par Dutch quand Arthur revient blessé ; quelques semaines plus tard, il rend visite à Arthur en convalescence."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Listed by the Red Dead Wiki; the mission page does not name him.",
          "Citée par le Red Dead Wiki ; la page de la mission ne le nomme pas."),
        M("The Battle of Shady Belle", C3,
          "Listed by the Red Dead Wiki; the mission page does not name him. [[andrew-milton|Milton]] and [[edgar-ross|Ross]] come to Clemens Point, then the gang moves to Shady Belle.",
          "Citée par le Red Dead Wiki ; la page de la mission ne le nomme pas. [[andrew-milton|Milton]] et [[edgar-ross|Ross]] se présentent à Clemens Point, puis la bande s'installe à Shady Belle."),
        M("Horsemen, Apocalypses", C4,
          "Hides in Hosea's room during the O'Driscoll attack on Shady Belle, then buries [[kieran-duffy|Kieran]] with [[charles-smith|Charles]] and [[simon-pearson|Pearson]] on Dutch's orders.",
          "Se cache dans la chambre d'Hosea pendant l'attaque des O'Driscoll contre Shady Belle, puis enterre [[kieran-duffy|Kieran]] avec [[charles-smith|Charles]] et [[simon-pearson|Pearson]] sur ordre de Dutch."),
        M("Fleeting Joy", C5,
          "Listed by the Red Dead Wiki; the mission page does not name him. According to the wiki, he is sober when Arthur reaches Lakay.",
          "Citée par le Red Dead Wiki ; la page de la mission ne le nomme pas. Selon le wiki, il est sobre quand Arthur arrive à Lakay."),
        M("That's Murfree Country", C5,
          "Listed by the Red Dead Wiki; the mission page does not name him. The gang moves to Beaver Hollow.",
          "Citée par le Red Dead Wiki ; la page de la mission ne le nomme pas. La bande s'installe à Beaver Hollow."),
        M("A Rage Unleashed", C6,
          "Mission giver. He is talking with Arthur in camp when Dutch calls Arthur away.",
          "Donneur de la mission. Il discute avec Arthur au camp quand Dutch appelle ce dernier."),
        M("The Fine Art of Conversation", C6,
          "Only if \"Of Men and Angels\" has not been completed or Arthur's honor is low. At Emerald Station he tells Arthur he is leaving the gang, gives him advice that depends on his honor and boards a train.",
          "Seulement si \"Of Men and Angels\" n'a pas été terminée ou si l'honneur d'Arthur est bas. À Emerald Station, il annonce à Arthur qu'il quitte la bande, lui donne un conseil qui dépend de son honneur et monte dans un train."),
        M("Red Dead Redemption", C6,
          "Voice only. With high honor, Arthur recalls his advice from Emerald Station during his last ride.",
          "Voix seulement. Avec un honneur élevé, Arthur se remémore son conseil d'Emerald Station pendant sa dernière chevauchée."),
        M("Bare Knuckle Friendships", E2,
          "Mentioned. According to the Red Dead Wiki, Charles tells John that Swanson has moved to New York to become a preacher.",
          "Mentionné. Selon le Red Dead Wiki, Charles apprend à John que Swanson est parti à New York pour devenir prédicateur."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent.")},
    {"h4": two("Colter", "Colter")},
    {"quotes": [
        {"q": two("Abigail says he's dying, Dutch. We'll have to stop some place.", "Abigail says he's dying, Dutch. We'll have to stop some place."),
         "src": two("Outlaws from the West (RDR2, chapter 1), to Dutch, about Davey Callander, during the crossing of the Grizzlies in the snowstorm",
                    "Outlaws from the West (RDR2, chapitre 1), à Dutch, à propos de Davey Callander, pendant la traversée des Grizzlies dans la tempête. Traduction : « Abigail dit qu'il est en train de mourir, Dutch. Il va falloir s'arrêter quelque part. »")},
        {"q": two("There was... nothing more you could have done.", "There was... nothing more you could have done."),
         "src": two("Outlaws from the West (RDR2, chapter 1), to Abigail, who has just announced that Davey is dead",
                    "Outlaws from the West (RDR2, chapitre 1), à Abigail, qui vient d'annoncer la mort de Davey. Traduction : « Vous ne pouviez... rien faire de plus. »")},
        {"q": two("I'll mind you to show me some respect, Mr. Morgan.", "I'll mind you to show me some respect, Mr. Morgan."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), to Arthur, who has joked about him reading John his last rites. Arthur answers: \"Mind away, Reverend.\"",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), à Arthur, qui vient de plaisanter sur les derniers sacrements administrés à John. Arthur répond : \"Mind away, Reverend.\" Traduction : « Je vous prierai de me témoigner un peu de respect, monsieur Morgan. » (« Priez toujours, révérend. »)")},
    ]},
    {"h4": two("Flatneck Station and Bard's Crossing", "Flatneck Station et Bard's Crossing")},
    {"quotes": [
        {"q": two("I took your advice, sir. I have removed myself from Morpheus' embrace.", "I took your advice, sir. I have removed myself from Morpheus' embrace."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), to Arthur, at the poker table. Arthur's reply a moment later: \"You don't seem free, friend. You seem drunk.\"",
                    "Who is Not Without Sin (RDR2, chapitre 2), à Arthur, à la table de poker. La réponse d'Arthur, un instant plus tard : \"You don't seem free, friend. You seem drunk.\" Traduction : « J'ai suivi votre conseil, monsieur. Je me suis arraché aux bras de Morphée. » (« T'as pas l'air libre, l'ami. T'as l'air soûl. »)")},
        {"q": two("No more shall I sink, sir. I am free, I am free!", "No more shall I sink, sir. I am free, I am free!"),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), his hands on Arthur's shoulders",
                    "Who is Not Without Sin (RDR2, chapitre 2), les mains sur les épaules d'Arthur. Traduction : « Je ne sombrerai plus, monsieur. Je suis libre, je suis libre ! »")},
        {"q": two("Why can't we all just get along? These are good men, Arthur. They're children of God... they're children of God.", "Why can't we all just get along? These are good men, Arthur. They're children of God... they're children of God."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), as Arthur argues with the card players, just before he collapses",
                    "Who is Not Without Sin (RDR2, chapitre 2), pendant qu'Arthur s'accroche avec les joueurs de cartes, juste avant de s'effondrer. Traduction : « Pourquoi on ne pourrait pas tous s'entendre ? Ce sont des hommes bons, Arthur. Ce sont des enfants de Dieu... des enfants de Dieu. »")},
        {"q": two("It appears to like this place and wants to stay.", "It appears to like this place and wants to stay."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), on the railway bridge, when Arthur asks what he has done with his foot",
                    "Who is Not Without Sin (RDR2, chapitre 2), sur le pont ferroviaire, quand Arthur lui demande ce qu'il a fait de son pied. Traduction : « Il semble se plaire ici et veut rester. »")},
        {"q": two("What the hell is wrong with you? Throwing me off a bridge like that.", "What the hell is wrong with you? Throwing me off a bridge like that."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), after Arthur has pushed him to the ground. Arthur shouts back: \"THERE WAS A GODDAMN TRAIN YOU CRAZY BASTARD!!!\"",
                    "Who is Not Without Sin (RDR2, chapitre 2), après qu'Arthur l'a jeté à terre. Arthur lui hurle : \"THERE WAS A GODDAMN TRAIN YOU CRAZY BASTARD!!!\" Traduction : « Mais qu'est-ce qui vous prend ? Me jeter d'un pont comme ça. » (« IL Y AVAIT UN PUTAIN DE TRAIN, ESPÈCE DE CINGLÉ ! »)")},
        {"q": two("Have I been bad again, Mr. Morgan? I'm sorry.", "Have I been bad again, Mr. Morgan? I'm sorry."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), to Arthur, before breaking down and adding \"I wish I was different.\"",
                    "Who is Not Without Sin (RDR2, chapitre 2), à Arthur, avant de craquer et d'ajouter \"I wish I was different.\" Traduction : « J'ai encore fait des bêtises, monsieur Morgan ? Je suis désolé. » (« J'aimerais être différent. »)")},
        {"q": two("Home... Yeah, that's a wonderful idea. I could have tea with Margaret.", "Home... Yeah, that's a wonderful idea. I could have tea with Margaret."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), when Arthur offers to take him home. Asked who Margaret is, he passes out after one word: \"My...\"",
                    "Who is Not Without Sin (RDR2, chapitre 2), quand Arthur propose de le ramener chez lui. Quand Arthur demande qui est Margaret, il perd connaissance après un seul mot : \"My...\" Traduction : « À la maison... Oui, quelle merveilleuse idée. Je pourrais prendre le thé avec Margaret. » (« Ma... »)")},
    ]},
    {"h4": two("Clemens Point", "Clemens Point")},
    {"quotes": [
        {"q": two("Mr. Morgan... Mr. Morgan, you're safe now.", "Mr. Morgan... Mr. Morgan, you're safe now."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), to Arthur, who has collapsed in camp after escaping the O'Driscolls",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), à Arthur, effondré au camp après s'être échappé de chez les O'Driscoll. Traduction : « Monsieur Morgan... Monsieur Morgan, vous êtes en sécurité, maintenant. »")},
        {"q": two("I thought I'd be burying you, Mr. Morgan.", "I thought I'd be burying you, Mr. Morgan."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), to the recovering Arthur, who answers: \"Not quite yet, Reverend.\"",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), à Arthur, en convalescence, qui répond : \"Not quite yet, Reverend.\" Traduction : « Je pensais que j'allais devoir vous enterrer, monsieur Morgan. » (« Pas tout de suite, révérend. »)")},
    ]},
    {"h4": two("Emerald Station", "Emerald Station")},
    {"quotes": [
        {"q": two("Save who you can and let the rest rot, and look after yourself.", "Save who you can and let the rest rot, and look after yourself."),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), to Arthur, with high honor; Arthur recalls the line during his last ride in \"Red Dead Redemption\"",
                    "The Fine Art of Conversation (RDR2, chapitre 6), à Arthur, avec un honneur élevé ; Arthur se remémore la phrase pendant sa dernière chevauchée, dans \"Red Dead Redemption\". Traduction : « Sauvez ceux que vous pouvez, laissez pourrir les autres, et prenez soin de vous. »")},
        {"q": two("You lived your way, you'll die your way.", "You lived your way, you'll die your way."),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), to Arthur, with low honor",
                    "The Fine Art of Conversation (RDR2, chapitre 6), à Arthur, avec un honneur bas. Traduction : « Vous avez vécu à votre manière, vous mourrez à votre manière. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("The title \"Who is Not Without Sin\" echoes John 8:7, the verse in which Jesus tells those about to stone a woman taken in adultery that the one without sin should cast the first stone.",
            "Le titre \"Who is Not Without Sin\" renvoie à Jean 8:7, le verset où Jésus dit à ceux qui s'apprêtent à lapider une femme adultère que celui qui n'a jamais péché lui jette la première pierre."),
        two("In \"Who is Not Without Sin\", if Arthur does not step in, the stranger beats Swanson to death and the mission fails.",
            "Dans \"Who is Not Without Sin\", si Arthur n'intervient pas, l'inconnu bat Swanson à mort et la mission échoue."),
        two("If \"A Quiet Time\" has already been played, Arthur remarks when he sees Swanson stuck on the tracks that it reminds him of his own drunken night with [[lenny-summers|Lenny Summers]], and, if he escaped the lawmen in that mission, recalls waking up at the same station.",
            "Si \"A Quiet Time\" a déjà été jouée, Arthur, en voyant Swanson coincé sur la voie, fait remarquer que cela lui rappelle sa propre nuit d'ivresse avec [[lenny-summers|Lenny Summers]], et, s'il avait échappé aux hommes de loi dans cette mission, se souvient s'être réveillé dans la même gare."),
        two("On the ride back to camp, if Arthur fires a shot, Swanson wakes up and asks what is happening. With Swanson stowed on his horse, Arthur can ride into and around camp without being told to dismount.",
            "Pendant le retour au camp, si Arthur tire un coup de feu, Swanson se réveille et demande ce qui se passe. Tant que Swanson est en travers de son cheval, Arthur peut entrer dans le camp et y circuler à cheval sans qu'on lui ordonne de descendre."),
        two("After the mission, in a random encounter in camp, Swanson gives Arthur a watch to thank him for saving him.",
            "Après la mission, lors d'une rencontre aléatoire au camp, Swanson offre une montre à Arthur pour le remercier de l'avoir sauvé."),
        two("When \"The Fine Art of Conversation\" is replayed on PC, Swanson appears at Emerald Station by default, whether or not the Sister Calderón stranger missions were completed.",
            "Quand \"The Fine Art of Conversation\" est rejouée sur PC, c'est Swanson qui apparaît par défaut à Emerald Station, que les missions d'étranger de sœur Calderón aient été terminées ou non."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Swanson for Red Dead Redemption 2. On September 6, 2018, Rockstar Games posted his portrait and a short character description under the name \"Reverend Swanson\" on Twitter, in a series covering the members of the gang. The Hollywood Reporter reproduced the series the next day. In the composite of the 23 gang members' official art that illustrates Wikipedia's list of the game's characters, Swanson stands in the front row, between Uncle and Sean.",
              "Rockstar a publié une illustration officielle de Swanson pour Red Dead Redemption 2. Le 6 septembre 2018, Rockstar Games publie sur Twitter son portrait et une courte présentation sous le nom de \"Reverend Swanson\", dans une série consacrée aux membres du gang. The Hollywood Reporter reprend la série le lendemain. Sur le montage des illustrations officielles des 23 membres du gang qui ouvre la liste des personnages du jeu sur Wikipédia, Swanson figure au premier rang, entre Uncle et Sean.")},
]
