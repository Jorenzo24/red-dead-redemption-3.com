"""Sister Calderón, part B: Personality (descriptions, observable traits, In her own words, Names, Appearance),
Charity work and gameplay (skills equivalent), Relationships (22 Oct 2026, medium tier).

Coverage: the Red Dead Wiki "Character" section (Personality, Appearance), the infobox (aka, occupation, weapon,
affiliations, family), the gameplay items of its Trivia (lawmen, loot, the Doyle's Tavern drunk, Swanson's prayer) and
the gameplay facts of the mission pages, all rewritten. Her lines are quoted from transcripts only.

SOURCE REGISTER (fetched 22 Oct 2026; files in scripts/v3/work/_m/ and scripts/v3/work/calderon/fc/):
- Full RDR2 fan transcript, Game Scripts Wiki (blogspot), fc/gsw.txt: "Brothers and Sisters, One and All" (reading
  lesson, crucifix, cathedral scene with the Father) and "The Fine Art of Conversation" (Emerald Station). The stage
  direction calls her "An old nun from Saint Denis". The transcript labels her "Sister" only.
- Red Dead Wiki "Of Men and Angels/dialogues" (_m/Of_Men_and_Angels_dialogues.txt): she gives her name ("Hello,
  Sister..." / "Calderón."), "Well, what fun!", Sister Ethel's stew, Brother Dorkins wanting to be a missionary.
- Red Dead Wiki "I Know You/dialogues" (_m/I_Know_You_dialogues.txt): Strange Man ("an old nun is traveling from the
  monastery, taking the money she raised to the bank"); her lines to John; John's "There you are, sister."
- Red Dead Wiki pages: "Mother Superior Calderón" (en.txt), FR "Mère Supérieure Calderón" (fr.txt), "Brothers and
  Sisters, One and All", "Of Men and Angels", "The Fine Art of Conversation" (PC replay trivia), "I Know You" (robbery
  sum, random nun encounters), "Mother Superior Blues" (Undead Nightmare: repeater, mortal sin worry, quote box),
  "Brother Dorkins", "Father O'Leary" (lawmen and loot trivia, sign), "Ayauhtéotl", "Las Hermanas", "Mary Linton"
  (API, 22 Oct 2026: Arthur's "a girl who loved me" is placed in Mary's story), "Nun".
- Rockstar's character descriptions of 6 Sep 2018 (scripts/v3/sources/thr_descriptions.txt): gang only, nothing on her.
- Fact-checked fiches reused for consistency: arthur_A/C/D/F (Isaac told to Rains Fall and to her), orville_A/B
  (Swanson told Arthur about Dorkins; "prayed with a nun" attributed to the wiki), linton_A/B, reyes_A/C, desanta_A/C,
  john_C (Mother Superior Blues).

OWNERSHIP: lines quoted HERE must not be repeated in part C Quotes: "Please give what you can."; "Don't hurt him,
please!"; "Every day, it's a new challenge, Father..."; "Well, what fun!"; "I shall pray for you."; "Perhaps you could
help somebody? Helping makes you really happy."; "Alms for the poor! Oh, sir, could you find it in your heart...";
(part C already quotes "Oh, you will. It's like swimming..." and "Yes, life is much simpler...": left to C, not here); "an old nun" (Strange Man, Names);
"There you are, sister." (John, Names); "Sister, my friend, Mr. Morgan." (Dorkins, Names); "Calderón." (Names).
Lines deliberately LEFT for C (paraphrased here, never quoted): "I was like you" / "terrible things"; "Religion is just
a word"; "God is people"; "The actions will lead"; "very nasty terms"; "You are wonderful"; "we all sin... You don't
know you"; "Life is full of pain"; "Be grateful..."; "Often neither do I"; "Take a gamble that love exists"; the
Undead Nightmare quote box ("México is an old country...").
DUPLICATES TO RESOLVE (lead): part C Trivia currently repeats three gameplay items owned here by OWNERSHIP.md
(lawmen shooting her and O'Leary; the PC replay default; the 300 dollars if robbed): cut them from C. The "Spanish nun"
remark is a name (B Names), not C trivia. Also in C Trivia: Rains Fall / Isaac (told in the Rains Fall
relationship here: cut from C or keep in C and shorten here). The five unnamed nuns of Mother Superior Blues: C only. The Las Hermanas daily routine is told in part A only (dropped here).
Undead Nightmare name: ireddead.com guide + Italian localisation line (fc/undead_nightmare_sources.txt), attributed.
Narrative events (crucifix chase, the collection, the station talk, I Know You, Mother Superior Blues) belong to part A;
entries below point to them. Her own backstory (husband, mother, the crucifix, "I was like you") = part A Origins;
one clause at most here. The cut hogtie dialogue = part D.

FIXES (22 Oct 2026, after fc_report1/2 and coverage_report): Personality reduced to traits + pointers (retold events
cut); Appearance reworded (no fan-transcript stage direction, no wiki word order); Sister Ethel and Gaspar Street cut
from Skills; Emerald conditions sentence cut from Skills (Biography + table own it); "refusing costs honor" dropped
(the mission page's honor loss is for not donating in the mission); 300 dollars attributed to the mission page (I Know
You trivia); Las Hermanas daily routine moved here from A, reworded; holy water retelling cut; Arthur/John entries
reduced to pointers; O'Leary: she tells him Dorkins "found him" and "was fantastic" (gsw.txt L8756); Rains Fall:
"among the few" (FIX_RULES 9, as arthur_F); Reyes insult told once in A; Ayauhtéotl "can see her" cut (speculative);
Swanson's prayer partner = "a Catholic lady", as in orville_B.

WIKI-ONLY (kept, attributed): the Doyle's Tavern drunk calling her a Spanish nun; lawmen shooting her and Father
O'Leary, two shots, lootable body; loot = Burdock Root; Winchester Repeater (Undead Nightmare); daily routine at Las
Hermanas (work, meals on the second floor); the robbery sum (over 300 dollars); random nun encounters after a donation;
Swanson praying with a nun; Reyes as a vain, ambitious and repugnant parasite and a philanderer (Undead Nightmare);
Ayauhtéotl as the nun who speaks to her; "Mother Superior Calderón" as the wiki's title; the PC replay default.

EXCLUDED: the wiki's "kind and bittersweet personality", "one of the only characters ... with such a special mindset",
"showing compassion, love, understanding, hope and empathy during every encounter" (interpretation); "implied to be
Sister Calderón" for Swanson's prayer partner (speculation: kept only as an unnamed nun); her nationality or origin
("Spanish nun" is a drunk's remark; "Por favor" and "Gracias, señor" are given as lines, not as an origin); a first
name (none in the games); the wiki trivia reading of the "half witted friends" line (interpretation of John's reply);
the FR wiki claim that she is the nun at the altar in "Eva in Peril" (the EN mission page says only "the nun praying at
the altar": contradiction, left out).
"""


def two(en, fr): return {"en": en, "fr": fr}


# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of 6 September 2018 cover the Van der Linde gang only and do not include her. When Arthur brings back her crucifix, her first question is about the boy who stole it (see Biography). The transcripts show her laughing in each of her three conversations with Arthur: at Dorkins's grammar lesson, at Arthur's claim to be an outlaw and at his admission that he believes in nothing. She tells Arthur that actions lead and the heart follows (see Quotes). In Red Dead Redemption (1911) she meets John Marston's objection to her appeal for alms with an answer of her own (see Biography). In Undead Nightmare, outside the series' canon, she is armed and uses her weapon (see Biography).",
        "Les descriptions de personnages publiées par Rockstar le 6 septembre 2018 portent sur le seul gang Van der Linde et ne la concernent pas. Quand Arthur lui rapporte son crucifix, sa première question porte sur le garçon qui l'a volé (voir la biographie). D'après les transcriptions, elle rit dans chacune de ses trois conversations avec Arthur : pendant la leçon de grammaire de Dorkins, quand Arthur se dit hors-la-loi et quand il avoue ne croire à rien. Elle lui explique que les actes ouvrent la voie et que le cœur suit (voir Citations). Dans Red Dead Redemption (1911), elle répond du tac au tac à l'objection de John Marston quand elle lui demande l'aumône (voir la biographie). Dans Undead Nightmare, hors de la continuité de la série, elle est armée et se sert de son arme (voir la biographie).")},
    {"h4": two("In her own words", "Dans ses propres mots")},
    {"ul": [
        two("\"Please give what you can.\" (outside the cathedral, as Arthur walks up in \"Of Men and Angels\")",
            "\"Please give what you can.\" (Donnez ce que vous pouvez.) Devant la cathédrale, quand Arthur s'approche, dans \"Of Men and Angels\"."),
        two("\"Don't hurt him, please!\" (as Arthur runs after the boy who stole her crucifix)",
            "\"Don't hurt him, please!\" (Ne lui faites pas de mal, je vous en prie !) Au moment où Arthur se lance à la poursuite du garçon qui a volé son crucifix."),
        two("\"Every day, it's a new challenge, Father. When I was younger, those challenges used to frustrate me.\" (to the priest at the cathedral, just before Arthur returns)",
            "\"Every day, it's a new challenge, Father. When I was younger, those challenges used to frustrate me.\" (Chaque jour apporte son défi, mon père. Plus jeune, ces défis me mettaient en colère.) Au prêtre de la cathédrale, juste avant le retour d'Arthur."),
        two("\"Well, what fun!\" (when Arthur tells her he is an outlaw, \"Of Men and Angels\")",
            "\"Well, what fun!\" (Comme c'est amusant !) Quand Arthur lui annonce qu'il est hors-la-loi, dans \"Of Men and Angels\"."),
        two("\"Perhaps you could help somebody? Helping makes you really happy.\" (to Arthur, at Emerald Station)",
            "\"Perhaps you could help somebody? Helping makes you really happy.\" (Peut-être pourriez-vous aider quelqu'un ? Aider rend vraiment heureux.) À Arthur, à la gare d'Emerald."),
        two("\"Alms for the poor! Oh, sir, could you find it in your heart to donate some money for the poor? Perhaps cast a little sunlight into their lives?\" (to John, outside Las Hermanas, \"I Know You\")",
            "\"Alms for the poor! Oh, sir, could you find it in your heart to donate some money for the poor? Perhaps cast a little sunlight into their lives?\" (L'aumône pour les pauvres ! Monsieur, auriez-vous le cœur de donner un peu d'argent pour eux ? D'apporter un rayon de soleil dans leur vie ?) À John, devant Las Hermanas, dans \"I Know You\"."),
        two("\"I shall pray for you.\" (when Arthur says he only hopes for a dignified exit, \"Of Men and Angels\")",
            "\"I shall pray for you.\" (Je prierai pour vous.) Quand Arthur dit n'espérer qu'une sortie digne, dans \"Of Men and Angels\"."),
    ]},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Calderón is the only name the games give her. In \"Of Men and Angels\", Arthur greets her as \"Sister\" and she supplies the rest: \"Calderón.\" No first name is ever given. Brother Dorkins introduces Arthur to her with \"Sister, my friend, Mr. Morgan.\", and Arthur only ever calls her Sister. In Red Dead Redemption, the Strange Man speaks of \"an old nun\" and John, after his donation, says \"There you are, sister.\"; the dialogue reproduced by the Red Dead Wiki labels her Mother Superior. In Undead Nightmare, when John calls her sister, she corrects him: she is the Mother Superior, Mother Superior Calderón, according to the ireddead.com walkthrough and the expansion's Italian version. The Red Dead Wiki titles her page \"Mother Superior Calderón\" and also lists the name Sister Calderón. According to the same wiki, a drunk at Doyle's Tavern in Saint Denis refers to her as a Spanish nun.",
        "Calderón est le seul nom que les jeux lui donnent. Dans \"Of Men and Angels\", Arthur la salue d'un \"Sister\" et elle complète d'elle-même : \"Calderón.\" Aucun prénom n'est jamais mentionné. Frère Dorkins lui présente Arthur par un \"Sister, my friend, Mr. Morgan.\" (Ma sœur, mon ami, M. Morgan), et Arthur ne l'appelle jamais autrement que « ma sœur ». Dans Red Dead Redemption, l'Étranger (Strange Man) parle d'\"an old nun\" (une vieille religieuse) et John, après son don, lui lance \"There you are, sister.\" (Voilà pour vous, ma sœur) ; les dialogues reproduits par le Red Dead Wiki la désignent comme la mère supérieure. Dans Undead Nightmare, quand John l'appelle « ma sœur », elle le reprend : elle est la mère supérieure, la mère supérieure Calderón, d'après la soluce d'ireddead.com et la version italienne de l'extension. Le wiki anglophone intitule sa page \"Mother Superior Calderón\" et mentionne aussi le nom de Sister Calderón ; le francophone l'appelle \"Mère Supérieure Calderón\". D'après le Red Dead Wiki, un ivrogne du Doyle's Tavern, à Saint-Denis, parle d'elle comme d'une religieuse espagnole.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "She is an elderly woman. Her habit is that of a Catholic nun, with a black veil over a white coif and a black tunic. In Undead Nightmare she keeps the habit and carries a rifle (see Charity work and gameplay).",
        "C'est une femme âgée. Elle porte l'habit des religieuses catholiques : un voile noir sur une guimpe blanche, et une tunique noire. Dans Undead Nightmare, elle garde l'habit et porte une carabine (voir Œuvres de charité et gameplay).")},
]

# ---------------------------------------------------------------- CHARITY WORK AND GAMEPLAY (skills equivalent)
# Proposed section title: "Charity work and gameplay" / "Œuvres de charité et gameplay"
BLOCKS_SKILLS = [
    {"h3": two("Saint Denis (1899)", "Saint-Denis (1899)")},
    {"p": two(
        "Her work in Saint Denis has two sides: reading lessons for street children, given with Brother Dorkins, and collections of money and food for the hungry outside the cathedral. The missions that come out of this work are listed in the Missions table. After \"Brothers and Sisters, One and All\", the Red Dead Wiki places her near Father O'Leary. If Arthur is wanted and leads lawmen to the pair, the same wiki says, they can kill her and the priest. She usually dies from two shots, and her body can then be searched; according to the wiki, she always carries Burdock Root.",
        "Son travail à Saint-Denis a deux volets : des leçons de lecture pour les enfants des rues, données avec frère Dorkins, et des quêtes d'argent et de nourriture pour les affamés devant la cathédrale. Les missions nées de ce travail figurent dans le tableau des Missions. Après \"Brothers and Sisters, One and All\", le Red Dead Wiki la situe près du père O'Leary. Si Arthur, recherché, entraîne les forces de l'ordre jusqu'à eux, celles-ci peuvent les abattre tous les deux, selon le même wiki. Deux balles suffisent en général à la tuer, et son corps peut ensuite être fouillé ; d'après le wiki, on y trouve toujours de la bardane (Burdock Root).")},
    {"p": two(
        "According to the mission page, when \"The Fine Art of Conversation\" is replayed on PC, Reverend Swanson appears at the end by default, whether or not the stranger mission was completed.",
        "D'après la page de la mission, quand on rejoue \"The Fine Art of Conversation\" sur PC, c'est le révérend Swanson qui apparaît à la fin, que la mission d'inconnu ait été faite ou non.")},
    {"h3": two("Las Hermanas (1911)", "Las Hermanas (1911)")},
    {"p": two(
        "In Red Dead Redemption she collects alms outside the convent of Las Hermanas, in Perdido. In the second part of \"I Know You\", John can give her 10 dollars or rob her; according to the mission page, she carries well over 300 dollars. If John gives, nuns later approach him in random encounters to ask for donations. The Red Dead Wiki adds that she is present at Las Hermanas outside the mission, at her daily work, and that she can be seen at her meal upstairs in the church.",
        "Dans Red Dead Redemption, elle demande l'aumône devant le couvent de Las Hermanas, dans le Perdido. Dans la deuxième partie de \"I Know You\", John peut lui donner 10 dollars ou la dévaliser ; d'après la page de la mission, elle a sur elle bien plus de 300 dollars. Si John donne, d'autres religieuses viennent ensuite le solliciter lors de rencontres aléatoires. Le Red Dead Wiki ajoute qu'on la croise aussi à Las Hermanas en dehors de la mission, occupée à ses tâches quotidiennes, et qu'on peut la voir prendre ses repas à l'étage de l'église.")},
    {"h3": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"p": two(
        "In Undead Nightmare she is armed: according to the Red Dead Wiki, she uses a Winchester Repeater. The Holy Water that \"Mother Superior Blues\" unlocks for John is listed in the Missions table.",
        "Dans Undead Nightmare, elle est armée : d'après le Red Dead Wiki, elle se sert d'une Winchester Repeater. L'eau bénite que \"Mother Superior Blues\" débloque pour John figure dans le tableau des Missions.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "In Saint Denis, Brother Dorkins introduces Arthur to her; Dorkins has already told her about the good turn Arthur did him in \"Help a Brother Out\". Arthur recovers her stolen crucifix in chapter 4. Later he finds her collecting outside the cathedral, and she greets him by name; he gives food or money for the poor (see Biography).",
            "À Saint-Denis, frère Dorkins lui présente Arthur ; Dorkins lui a déjà raconté le service qu'Arthur lui a rendu dans \"Help a Brother Out\". Arthur récupère son crucifix volé au chapitre 4. Plus tard, il la trouve en train de quêter devant la cathédrale, et elle l'accueille par son nom ; il donne de la nourriture ou de l'argent pour les pauvres (voir la biographie)."),
        two(
            "Their last meeting is at Emerald Station, if \"Of Men and Angels\" was completed and his honor is high. There he tells her that he is dying (see Biography).",
            "Leur dernière rencontre a lieu à la gare d'Emerald, si \"Of Men and Angels\" a été terminée et que son honneur est élevé. Il lui avoue alors qu'il va mourir (voir la biographie)."),
    ]},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "If the Red Dead Wiki's identification is followed, John meets her twelve years later in Red Dead Redemption, outside Las Hermanas, sent there by the Strange Man in \"I Know You\". He questions her appeal for alms, then gives or robs her (see Biography). In Undead Nightmare, outside the canon, she becomes his ally against the plague and sends him on to Sepulcro and Escalera (see Biography).",
        "Si l'on suit le Red Dead Wiki, John la croise douze ans plus tard dans Red Dead Redemption, devant Las Hermanas, où l'Étranger l'a envoyé dans \"I Know You\". Il discute sa demande d'aumône, puis lui donne ou la dévalise (voir la biographie). Dans Undead Nightmare, hors canon, elle devient son alliée contre l'épidémie et l'envoie à Sepulcro, puis à Escalera (voir la biographie).")},
    {"img": "orville-swanson.jpeg", "slug": "orville-swanson", "name": "Orville Swanson", "text": two(
        "The gang's reverend is the one who first tells Arthur about Brother Dorkins, the path that leads Arthur to her. At the end of \"The Fine Art of Conversation\", Swanson takes her place at Emerald Station if \"Of Men and Angels\" was not completed or if Arthur's honor is low. According to the Red Dead Wiki, a sober Swanson tells Arthur in chapter 6 that he has prayed with a Catholic lady; the game does not say who she is.",
        "C'est le révérend du gang qui, le premier, parle à Arthur de frère Dorkins, le chemin qui mène Arthur jusqu'à elle. À la fin de \"The Fine Art of Conversation\", Swanson prend sa place à la gare d'Emerald si \"Of Men and Angels\" n'a pas été faite ou si l'honneur d'Arthur est bas. D'après le Red Dead Wiki, un Swanson sobre raconte à Arthur, au chapitre 6, qu'il a prié avec une dame catholique ; le jeu ne dit pas de qui il s'agit.")},
    {"img": "rains-fall.jpeg", "slug": "rains-fall", "name": "Rains Fall", "text": two(
        "The Wapiti chief asks Arthur to come to the peace talks with Colonel Favours in \"The Fine Art of Conversation\", the mission at whose end she appears; the two never meet on screen. According to the Red Dead Wiki, they are among the few characters to whom Arthur speaks of his late son, Isaac: at length to Rains Fall in \"Archeology for Beginners\", in a single sentence to her at the station.",
        "Le chef des Wapiti demande à Arthur de l'accompagner aux pourparlers de paix avec le colonel Favours dans \"The Fine Art of Conversation\", la mission à la fin de laquelle elle apparaît ; tous deux ne se croisent jamais à l'écran. D'après le Red Dead Wiki, ils font partie des rares personnages à qui Arthur parle de son fils disparu, Isaac : longuement à Rains Fall dans \"Archeology for Beginners\", en une seule phrase à elle, à la gare.")},
    {"img": "mary-linton.jpeg", "slug": "mary-linton", "name": "Mary Linton", "text": two(
        "At Emerald Station, Arthur tells her about a girl who loved him and whom he gave up, without naming her. The Red Dead Wiki's page on Mary Linton places this line in Mary's story.",
        "À la gare d'Emerald, Arthur lui parle d'une fille qui l'aimait et qu'il a laissée partir, sans la nommer. La page du Red Dead Wiki consacrée à Mary Linton rattache cette réplique à l'histoire de Mary.")},
    {"img": "abraham-reyes.jpeg", "slug": "abraham-reyes", "name": "Abraham Reyes", "text": two(
        "The two have no scene together in the canon. In Undead Nightmare, after John has cleansed Sepulcro, she tells him that a woman connected the plague to something Reyes did, sends him to Escalera, and speaks of Reyes with contempt (see Biography).",
        "Les deux personnages n'ont aucune scène commune dans le canon. Dans Undead Nightmare, une fois Sepulcro purifié par John, elle lui apprend qu'une femme a relié l'épidémie à un acte de Reyes, l'envoie à Escalera et parle de Reyes avec mépris (voir la biographie).")},
    {"img": "vincente-de-santa.jpeg", "slug": "vincente-de-santa", "name": "Vincente de Santa", "text": two(
        "No canon scene links them. In Undead Nightmare she asks John to cleanse the cemetery of Sepulcro, east of Las Hermanas, where the undead De Santa rises from his grave when the cemetery is nearly cleared (see Biography).",
        "Aucune scène du canon ne les réunit. Dans Undead Nightmare, elle demande à John de purifier le cimetière de Sepulcro, à l'est de Las Hermanas, où De Santa sort de sa tombe en mort-vivant quand le cimetière est presque nettoyé (voir la biographie).")},
    {"img": None, "slug": None, "name": "Brother Dorkins", "text": two(
        "The Saint Denis monk teaches the street children to read with her (see Biography). In \"Of Men and Angels\" she calls him \"a lovely man\" and tells Arthur that Dorkins is a little frustrated with the workings of their order and keeps trying to be sent overseas, perhaps as a missionary. According to the Red Dead Wiki, his first name is Aldred.",
        "Le moine de Saint-Denis apprend à lire aux enfants des rues avec elle (voir la biographie). Dans \"Of Men and Angels\", elle le décrit comme \"a lovely man\" (un homme charmant) et raconte à Arthur que Dorkins, un peu agacé par le fonctionnement de leur ordre, cherche sans cesse à partir outre-mer, peut-être comme missionnaire. D'après le Red Dead Wiki, son prénom est Aldred.")},
    {"img": None, "slug": None, "name": "Father O'Leary", "text": two(
        "The priest of the church where Arthur finds her is with her when Arthur returns the crucifix. He has no line. As Arthur leaves, she tells him that Brother Dorkins found Arthur and that Dorkins was fantastic. His name is on the sign in front of the church, according to the Red Dead Wiki.",
        "Le prêtre de l'église où Arthur la retrouve est avec elle quand Arthur rapporte le crucifix. Il ne dit pas un mot. Au départ d'Arthur, elle lui glisse que c'est frère Dorkins qui l'a trouvé, et que Dorkins a été formidable. Son nom figure sur le panneau devant l'église, d'après le Red Dead Wiki.")},
    {"img": None, "slug": None, "name": "Sister Ethel", "text": two(
        "A nun of her community, mentioned once: in \"Of Men and Angels\", after Arthur's donation, she tells him that Sister Ethel makes a fabulous stew and that the poor will be so happy.",
        "Religieuse de sa communauté, citée une seule fois : dans \"Of Men and Angels\", après le don d'Arthur, elle lui confie que sœur Ethel prépare un ragoût fabuleux et que les pauvres seront ravis.")},
    {"img": None, "slug": None, "name": "Strange Man", "text": two(
        "In \"I Know You\", the mysterious stranger points John toward an old nun carrying money to the bank and leaves him to help or rob her (see Biography).",
        "Dans \"I Know You\", le mystérieux inconnu signale à John une vieille religieuse qui porte de l'argent à la banque, et le laisse libre de l'aider ou de la dévaliser (voir la biographie).")},
    {"img": None, "slug": None, "name": "Ayauhtéotl", "text": two(
        "Undead Nightmare only. According to the Red Dead Wiki, the woman who reveals herself as Ayauhtéotl at the end of Undead Nightmare appears at Las Hermanas dressed as a nun, and she is the one who points the Mother Superior toward Reyes.",
        "Uniquement dans Undead Nightmare. D'après le Red Dead Wiki, la femme qui se révèle être Ayauhtéotl à la fin d'Undead Nightmare apparaît à Las Hermanas en habit de religieuse, et c'est elle qui oriente la mère supérieure vers Reyes.")},
    {"img": None, "slug": None, "name": "Her mother and her husband", "text": two(
        "Neither is named. Her mother gave her the crucifix the boy steals, and her husband died long before 1899 (see Biography).",
        "Aucun des deux n'est nommé. Sa mère lui a offert le crucifix que vole le garçon, et son mari est mort bien avant 1899 (voir la biographie).")},
]
