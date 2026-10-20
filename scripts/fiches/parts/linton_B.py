"""Mary Linton, part B: Personality (descriptions, In her own words, Names, Appearance), Relationships
(20 Oct 2026, medium tier). No skills section: Mary has no skills, weapons or horse in the game
(BLOCKS_SKILLS is empty; the module should drop that section).

Sources (register, fetched 20 Oct 2026 via the Red Dead Wiki API, saved in scratchpad cov/linton/ and fc/):
- Rockstar's character descriptions of September 2018 cover the Van der Linde gang only; Mary is not
  among them. No official guide biography page for her was found.
- Red Dead Wiki EN "Mary Linton" (infobox: née Gillis, family, voice Julie Jesneck; Quotes list; Appearance;
  Trivia: camp remarks by Susan, Tilly, Mary-Beth, Karen, Abigail, John). FR "Mary Linton".
- No transcript of "We Loved Once and True I-III" or "Fatherhood and Other Dreams" exists on the wiki
  ("/dialogues" pages missing). Mary's own lines are quoted ONLY from the wiki's Quotes list, cross-checked
  with the trivia of the "We Loved Once and True I & II" mission page (same words).
- Mission pages: "We Loved Once and True I & II" (Susan, letter, Chadwick Farm, older woman with a gun),
  "We Loved Once and True III", "Fatherhood and Other Dreams" (Ashton, brooch, trivia: Mary's remark on
  Arthur's weight), "No, No and Thrice, No".
- Transcript: "Money Lending and Other Sins III" (alternate scene after Mary's letter; told in part A).
- Wiki pages "Mr. Gillis" (voice Robert Newman; Mrs. Gillis, wife, dead), "Jamie Gillis" (voice Adrian
  Enscoe), "Arthur Morgan/Relationships".
- Fact-checked fiches reused as is: arthur_A (engagement, Jamie taught to ride, Barry Linton, pneumonia,
  Calderón), abigail_B (dominoes), susan_A/B, tilly_A/B, mary_A/C ("Well, she was a fool then, Arthur."),
  leopold_A, john_B.

Ownership (FIX_RULES): Mary's own quoted lines below ("Don't make me beg you, Arthur."; "I understand if
you don't wanna help me, but... but... I think of you often."; "I've... You're... Oh, you'll never change.
I know that.") live HERE; parts A and C must NOT repeat them. Names (Gillis, Linton) and appearance live
HERE (the "Linton" naming of her father and brother in the game files is in part D, Cut content). Camp
remarks about Mary (Susan, Tilly, Mary-Beth, Karen, Abigail, John) live in the relationship
entries; Strauss, Miss Chadwick and Barry Linton are told in part A and only pointed to here. Narrative events (letters, Chadwick Farm, Jamie's rescue, the brooch, the theater, the trolley
talk, the ring, the grave) live in part A; relationship entries point to them in one clause.
The letters are told ONCE, in part A: this part quotes none of them.

WIKI-ONLY (kept, attributed): Susan's, Tilly's and Karen's remarks and Abigail's liking for Mary (wiki
trivia, no transcript); John bringing Mary up in "The Sheep and the Goats" (no transcript; content not
given); Mary-Beth's private conversations; Mr. Gillis's habits; the voice credits of Mr. Gillis and Jamie;
Arthur's words to Sister Calderón (paraphrased).

Excluded: "well-meaning", "tries to see the best in people", "lenient views on her family" (wiki
interpretation); "she still loved him enough to overlook his faults" (wiki inference from the grave scene);
the wiki's inference that the relationship lasted until at least 1894 (deduction from Abigail's arrival);
the v2 page's Dutch and John entries ("Dutch's hold on Arthur is why...", "John, unlike Arthur, leaves the
outlaw life": interpretation, no exchange with Mary); "She represents the ordinary, settled life Arthur
gave up" (v2 analysis); Jamie meeting Dutch, Hosea, Annabelle and Bessie ("implied" on the wiki); the
outfit catalogue of the wiki's Appearance section (reduced to three sentences).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the members of the Van der Linde gang, and Mary is not among them.",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur les membres du gang Van der Linde, et Mary n'en fait pas partie.")},
    {"h4": two("In her own words", "Dans ses propres mots")},
    {"p": two(
        "No transcript of her scenes is published on the Red Dead Wiki; the lines below come from the wiki's quote list. At Chadwick Farm, when Arthur is slow to hear her out, she tells him: \"Don't make me beg you, Arthur.\" When she asks him to find her brother, she says: \"I understand if you don't wanna help me, but... but... I think of you often.\" Arthur remembers one of these two lines in \"A Fork in the Road\", the first with low honor and the second with high honor. Before boarding the train with Jamie at the end of \"We Loved Once and True III\", she tells him: \"I've... You're... Oh, you'll never change. I know that.\"",
        "Aucune transcription de ses scènes n'est publiée sur le Red Dead Wiki ; les répliques qui suivent viennent de la liste de citations du wiki. À Chadwick Farm, comme Arthur rechigne à l'écouter, elle lui dit : \"Don't make me beg you, Arthur.\" (ne m'oblige pas à te supplier, Arthur). Quand elle lui demande de retrouver son frère, elle ajoute : \"I understand if you don't wanna help me, but... but... I think of you often.\" (je comprends que tu ne veuilles pas m'aider, mais... mais... je pense souvent à toi). L'une de ces deux phrases revient à Arthur dans \"A Fork in the Road\" : la première si son honneur est bas, la seconde s'il est élevé. Avant de monter dans le train avec Jamie, à la fin de \"We Loved Once and True III\", elle lui lance : \"I've... You're... Oh, you'll never change. I know that.\" (j'ai... tu es... oh, tu ne changeras jamais, je le sais bien).")},
    {"p": two(
        "While they follow her father through Saint Denis in \"Fatherhood and Other Dreams\", she comments on Arthur's looks, according to the mission page. If he is above his ideal weight, she says he looks well and recalls how thin he used to be. Otherwise she tells him he looks dirty, however clean he is.",
        "Pendant qu'ils suivent son père dans les rues de Saint-Denis, dans \"Fatherhood and Other Dreams\", elle fait une remarque sur l'allure d'Arthur, d'après la page de la mission. S'il pèse plus que son poids idéal, elle lui trouve bonne mine et se souvient qu'il était autrefois tout maigre. Sinon, elle lui dit qu'il a l'air sale, aussi propre soit-il.")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "She was born Mary Gillis, the name of her father and of her brother Jamie. Linton is her married name, taken from her husband, Barry Linton. The game calls her Mary Linton throughout, and Arthur calls her Mary.",
        "Elle est née Mary Gillis, nom de son père et de son frère Jamie. Linton est son nom d'épouse, celui de son mari, Barry Linton. Le jeu l'appelle Mary Linton d'un bout à l'autre, et Arthur l'appelle Mary.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "Mary has long dark brown hair, brown eyes and a beauty mark on her right cheek. She wears her hair in a low braid at Chadwick Farm and in a low bun in her later scenes. At Arthur's grave, in the end credits, she is dressed for mourning, in a black hat.",
        "Mary a de longs cheveux châtain foncé, les yeux bruns et un grain de beauté sur la joue droite. Elle porte une tresse basse à Chadwick Farm, puis un chignon bas dans ses scènes suivantes. Sur la tombe d'Arthur, pendant le générique de fin, elle est en tenue de deuil, coiffée d'un chapeau noir.")},
]

# ---------------------------------------------------------------- SKILLS
# Mary has no skills, weapons or horse described in the game or on the wiki: drop the section.
BLOCKS_SKILLS = []

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
        "Arthur and Mary were engaged when they were young; the engagement ended before 1899 (see Biography). In 1899 she asks him for help twice, first with her brother and then with her father, and her last letter returns the ring he gave her (see Biography). Before he dies he hands the ring to John with his other belongings (see Biography).",
        "Arthur et Mary se sont fiancés jeunes ; les fiançailles ont pris fin avant 1899 (voir la biographie). En 1899, elle lui demande deux fois son aide, d'abord pour son frère, puis pour son père, et sa dernière lettre lui rend la bague qu'il lui avait offerte (voir la biographie). Avant de mourir, il confie la bague à John avec ses autres affaires (voir la biographie).")},
    {"img": None, "slug": None, "name": "Mr. Gillis", "text": two(
        "Her father opposed her engagement to Arthur. By 1899 he drinks, gambles and sells off family belongings, according to the Red Dead Wiki. In Saint Denis he sells her late mother's brooch (see Biography). The wiki credits Robert Newman as his voice.",
        "Son père s'opposait à ses fiançailles avec Arthur. En 1899, il boit, joue et vend les biens de la famille, d'après le Red Dead Wiki. À Saint-Denis, il vend la broche de la défunte mère de Mary (voir la biographie). Le wiki attribue sa voix à Robert Newman.")},
    {"img": None, "slug": None, "name": "Jamie Gillis", "text": two(
        "Her younger brother has joined the Chelonians, a cult camped in Cumberland Forest, when Mary asks Arthur to bring him back (see Biography). Her second letter gives news of him (see Biography). The Red Dead Wiki credits Adrian Enscoe as his voice.",
        "Son petit frère a rejoint les Chéloniens, une secte installée dans la Cumberland Forest, quand Mary demande à Arthur de le ramener (voir la biographie). Sa deuxième lettre donne de ses nouvelles (voir la biographie). Le Red Dead Wiki attribue sa voix à Adrian Enscoe.")},
    {"img": None, "slug": None, "name": "Barry Linton", "text": two(
        "Mary married him after her engagement to Arthur ended, and took his name. He died of pneumonia before 1899 (see Biography).",
        "Mary l'a épousé après la rupture de ses fiançailles avec Arthur, et a pris son nom. Il est mort d'une pneumonie avant 1899 (voir la biographie).")},
    {"img": None, "slug": None, "name": "Mrs. Gillis", "text": two(
        "Her mother is dead by 1899 and is never named in the game. She gave Mary the brooch that Mr. Gillis sells in Saint Denis (see Biography).",
        "Sa mère est morte avant 1899, et le jeu ne donne jamais son prénom. C'est elle qui avait donné à Mary la broche que M. Gillis vend à Saint-Denis (voir la biographie).")},
    {"img": "susan-grimshaw.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
        "Susan tells Arthur that a letter from Mary has arrived (see Biography). According to the Red Dead Wiki, she says she never liked Mary, which annoys Arthur.",
        "Susan annonce à Arthur qu'une lettre de Mary est arrivée (voir la biographie). D'après le Red Dead Wiki, elle dit n'avoir jamais aimé Mary, ce qui agace Arthur.")},
    {"img": "tilly-jackson.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
        "Tilly hands Arthur Mary's last letter at Beaver Hollow, at the end of \"Goodbye, Dear Friend\" (see Biography). According to the Red Dead Wiki, she tells him Mary is not worth it.",
        "Tilly remet à Arthur la dernière lettre de Mary à Beaver Hollow, à la fin de \"Goodbye, Dear Friend\" (voir la biographie). D'après le Red Dead Wiki, elle lui dit que Mary n'en vaut pas la peine.")},
    {"img": "mary-beth-gaskill.jpeg", "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill", "text": two(
        "At the start of \"No, No and Thrice, No\", Arthur can bring Mary up, and Mary-Beth answers: \"Well, she was a fool then, Arthur.\" With high honor, Arthur remembers the line in \"A Fork in the Road\". According to the Red Dead Wiki, Mary-Beth also mentions Mary in private conversations with Arthur at Horseshoe Overlook and Beaver Hollow.",
        "Au début de \"No, No and Thrice, No\", Arthur peut parler de Mary, et Mary-Beth lui répond : \"Well, she was a fool then, Arthur.\" (eh bien, c'était une idiote, alors, Arthur). Si son honneur est élevé, Arthur se souvient de cette phrase dans \"A Fork in the Road\". D'après le Red Dead Wiki, Mary-Beth évoque aussi Mary dans des conversations en tête à tête avec Arthur à Horseshoe Overlook et à Beaver Hollow.")},
    {"img": "karen-jones.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": two(
        "According to the Red Dead Wiki, Karen asks Arthur whether he will get back together with Mary, and he answers that it is too late.",
        "D'après le Red Dead Wiki, Karen demande à Arthur s'il va se remettre avec Mary, et il répond qu'il est trop tard.")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "According to the Red Dead Wiki, Abigail, unlike the other women in camp, says she always liked Mary. She remembers Arthur and Mary playing dominoes together. In 1907 John proposes to her with the ring Arthur once gave Mary (see Biography).",
        "D'après le Red Dead Wiki, Abigail, contrairement aux autres femmes du camp, dit avoir toujours apprécié Mary. Elle se souvient d'Arthur et de Mary jouant ensemble aux dominos. En 1907, John la demande en mariage avec la bague qu'Arthur avait autrefois offerte à Mary (voir la biographie).")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "According to the Red Dead Wiki, John brings Mary up once while he and Arthur argue about their lives in \"The Sheep and the Goats\". In 1907 he proposes to Abigail with Mary's former engagement ring (see Biography).",
        "D'après le Red Dead Wiki, John parle de Mary une fois, pendant une dispute avec Arthur sur leurs vies respectives, dans \"The Sheep and the Goats\". En 1907, il demande Abigail en mariage avec l'ancienne bague de fiançailles de Mary (voir la biographie).")},
    {"img": "leopold-strauss.jpeg", "slug": "leopold-strauss", "name": "Leopold Strauss", "text": two(
        "Strauss notices that Arthur is lost in thought after reading Mary's first letter, at the start of \"Money Lending and Other Sins III\" (see Biography).",
        "Au début de \"Money Lending and Other Sins III\", Strauss remarque qu'Arthur a l'esprit ailleurs après la lecture de la première lettre de Mary (voir la biographie).")},
    {"img": None, "slug": None, "name": "Miss Chadwick", "text": two(
        "In 1899 Mary rents a room at Chadwick Farm, near Valentine, where Miss Chadwick receives Arthur at the door (see Biography).",
        "En 1899, Mary loue une chambre à Chadwick Farm, près de Valentine, où Miss Chadwick accueille Arthur sur le pas de la porte (voir la biographie).")},
    {"img": None, "slug": None, "name": "Ashton", "text": two(
        "This Saint Denis loan shark buys the brooch of Mary's mother from Mr. Gillis, and Arthur takes it back from him (see Biography).",
        "Cet usurier de Saint-Denis achète à M. Gillis la broche de la mère de Mary, et Arthur la lui reprend (voir la biographie).")},
    {"img": None, "slug": None, "name": "Sister Calderón", "text": two(
        "If Arthur helped her in \"Of Men and Angels\" and his honor is high, he meets her at Emerald Station in \"The Fine Art of Conversation\". According to the Red Dead Wiki, he speaks of Mary to her as a girl who loved him and regrets not running away with her.",
        "Si Arthur l'a aidée dans \"Of Men and Angels\" et que son honneur est élevé, il la retrouve à la gare d'Emerald dans \"The Fine Art of Conversation\". D'après le Red Dead Wiki, il lui parle de Mary comme d'une fille qui l'aimait, et regrette de ne pas être parti avec elle.")},
]
