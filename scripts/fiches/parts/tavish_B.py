"""Tavish Gray, part B: Personality (how others describe him, In his own words, Names, Appearance), Caliga Hall
(skills equivalent), Relationships (22 Oct 2026, medium tier).

Coverage: the Red Dead Wiki page "Tavish Gray" has no Personality or Appearance section; its family facts (infobox:
brother Leigh, son Beau, father Murdo, ancestors Ross and Douglas, "Scottish descent") and its Leigh/Tavish trivia item
are covered in Names and Relationships. Everything he says comes from his only scene, in "Horse Flesh for Dinner".

SOURCE REGISTER (fetched 22 Oct 2026):
- Full game transcript, "Red Dead Redemption 2 Full Transcript", Game Scripts Wiki (blogspot), fan transcript of the
  cutscenes (scripts/v3/work/tavish/fc/gsw.txt, not committed). Scenes used: "Horse Flesh for Dinner" (all of Tavish's
  lines; the transcript labels him "Stranger" until John says "Mr. Gray"; John's "Crazy old fool"; Arthur's journal
  "Believed a yarn, spun us by one of that Gray family"); "The Course of True Love I + II" (Beau: "son of Tavish Gray...
  nephew of Leigh Gray the sheriff... grandson of old Murdo Gray"; the Caliga Hall guard: "This is private property,
  interlopers are not permitted"); "Advertising, The New American Art" (Dutch: "Scots... degenerates... drunkards....
  the local law... Rich as Croesus"; "Sheriff Gray kindly put in a word with his father"); "The Fine Joys of Tobacco"
  (Sean: "Old Man Gray's doubled security after that business at the saloon"; extra muscle and supply wagons);
  "The New South" (Archibald MacGregor on Caliga Hall, the tobacco fields, "they own all the businesses in town",
  the Rhodes Parlor House); "A Short Walk in a Pretty Town" (Micah: "They spoke to Bill about a job... needing security").
- Camp Events (scripts/v3/sources/Camp_Events.txt), Shady Belle chapter: Dutch swears to make the Grays bleed (rare line).
- Red Dead Wiki EN: "Tavish Gray" (en.txt), "Gray Family", "Caliga Hall" (location, layout, 1907 state, Shirley
  Plantation), "Leigh Gray", "Beau Gray", "Gray's Secret" (Arthur's and John's journal drawings), "Gray Family
  History Letter" (addressed "Dear Mr. Gray"; "a 'Scot in exile' as you describe yourself"). Red Dead Wiki FR
  "Tavish Gray" (fr.txt): brother of the sheriff, father of Beau.
- Rockstar's character descriptions of 6 Sep 2018 (scripts/v3/sources/thr_descriptions.txt) cover the gang only: none
  for him. No official-guide description of him was found.
- Live portrait (assets/characters/tavish-gray/portrait.jpeg) for Appearance.
- Fact-checked fiches reused for consistency: catherine_A/B/C (the "hag" line stays a paraphrase here), hosea_B,
  javier_B, micah_B, sean_B, arthur_B, john_A.

OWNERSHIP: lines quoted in "In his own words" must be REMOVED from part C Quotes: "We're an old Scottish family. We
work. My daddy taught that to me, I taught my sons. Work hard, but fair."; "We've got gold, Yankee... we've got gold.";
"I'm Scottish."; "Just keep us away from this... publicly I mean." Quoted in Names (not to be repeated in C):
"Crazy old fool" (John), "Old Man Gray" (Sean), "Scot in exile" (letter). Quoted in Personality: Dutch's "Scots...
degenerates... drunkards" line and Beau's "blind loyalty... and stupidity". Left to C: "We haven't recovered as much as
I'd hoped from the war..." (wiki quote box), "That hag and her inbred sons...", "Enough. These are prized horses...",
"Over in Clemens Cove...", "Go to the stables on the south side...", Arthur's journal lines. Narrative events (the
horse theft, the 700 dollars, the fire, the Rhodes ambush, the body and the letter) belong to part A; entries point to
them. The family history (1755 emigration, Douglas and Lucille, 1806 gold) is part A Origins. The Shirley Plantation
model and the 1907 state of the estate are HERE (C Trivia must not repeat them).

WIKI-ONLY (kept, attributed): Leigh as Tavish's brother (infobox EN and FR; Beau's line makes Leigh Beau's uncle, which
is what the wiki relies on); Caliga Hall in Bayou Nwa; the estate still worked and guarded in 1907; Shirley Plantation.

EXCLUDED: the cause of death (wiki pages disagree: suicide on "Gray's Secret" and "Caliga Hall", heart attack "more
likely" on "Tavish Gray"; nothing shown); the wiki's "likely a developer oversight" and "plausible that the gang
received false information" on the Leigh question (interpretation); Joe Butler's claims about the Grays (Union spies,
"fifty years ago": about the family, wiki-only, part A at most); the Villains Wiki; Hamish's "Mr. Gray's got a heap of
problems" (the game does not say which Gray he means); Jock, Iain and Scott Gray (no link to Tavish shown); his
slurs against the Braithwaites quoted verbatim (paraphrased).

FIX PASS (22 Oct 2026): the "That hag and her inbred sons..." line and "Who are you?" are now quoted in C Quotes (B
paraphrases). Added "We haven't recovered as much as I'd hoped from the war..." (gsw l.7438) to In his own words.
"Old Man Gray": the game does not say which Gray (never given as Tavish's nickname). Leigh, Beau, John, Arthur entries and
Caliga Hall reduced to summaries (the Biography owns the telling, including the 1907 estate). Appearance re-read on the
portrait and gallery-1 (bald crown, dark hair streaked with gray, patterned vest). No "not an exiled Jacobite".
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include him. He has a single scene, at the Caliga Hall stables in \"Horse Flesh for Dinner\". In it he is first wary of the newcomers. He talks about the war, his family and his Scottish roots (see In his own words). He speaks of the Braithwaites only through insults (see Quotes).",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang Van der Linde et ne le mentionnent pas. Il n'a qu'une scène, aux écuries de Caliga Hall, dans \"Horse Flesh for Dinner\". Il commence par se méfier des nouveaux venus. Il y parle de la guerre, de sa famille et de ses racines écossaises (voir Dans ses propres mots). Il n'évoque les Braithwaite qu'à coups d'insultes (voir Citations).")},
    {"p": two(
        "Dutch sums up the Grays as \"Scots... degenerates... drunkards\", adds that they are the local law and calls them \"Rich as Croesus\". His son Beau says the Grays have been the Braithwaites' murderers for so long that nobody can explain why, \"Beyond blind loyalty... and stupidity\".",
        "Dutch résume les Gray en trois mots, \"Scots... degenerates... drunkards\" (des Écossais… des dégénérés… des ivrognes), ajoute qu'ils tiennent la loi locale et les dit \"Rich as Croesus\" (riches comme Crésus). Son fils Beau explique que les Gray tuent des Braithwaite depuis si longtemps que plus personne ne sait pourquoi, \"Beyond blind loyalty... and stupidity\" (si ce n'est par loyauté aveugle… et par bêtise).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"ul": [
        two("\"We haven't recovered as much as I'd hoped from the war. My family try... my sons are good boys, but it's been hard. Like I said, some people in the area will hold us back for ever. We need stability.\" (to John)",
            "\"We haven't recovered as much as I'd hoped from the war. My family try... my sons are good boys, but it's been hard. Like I said, some people in the area will hold us back for ever. We need stability.\" (on ne s'est pas relevés de la guerre autant que je l'espérais ; ma famille fait des efforts, mes fils sont de bons garçons, mais ça a été dur ; je le répète, certains dans la région nous mettront toujours des bâtons dans les roues ; il nous faut de la stabilité), à John."),
        two("\"We're an old Scottish family. We work. My daddy taught that to me, I taught my sons. Work hard, but fair.\" (to John)",
            "\"We're an old Scottish family. We work. My daddy taught that to me, I taught my sons. Work hard, but fair.\" (nous sommes une vieille famille écossaise, nous travaillons ; mon père me l'a appris, je l'ai appris à mes fils : travailler dur, mais honnêtement), à John."),
        two("\"We've got gold, Yankee... we've got gold.\" (to John)",
            "\"We've got gold, Yankee... we've got gold.\" (on a de l'or, le Yankee… on a de l'or), à John."),
        two("\"I'm Scottish.\" (after John claims that his own father came over from Scotland)",
            "\"I'm Scottish.\" (je suis écossais), quand John affirme que son propre père est venu d'Écosse."),
        two("\"Just keep us away from this... publicly I mean.\"",
            "\"Just keep us away from this... publicly I mean.\" (surtout, tenez-nous à l'écart de tout ça… publiquement, je veux dire)."),
    ]},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "His first name is given by his son Beau (see Quotes). At the stables John calls him Mr. Gray, and the letter found beside his body opens with \"Dear Mr. Gray\"; in it the historian notes that his correspondent describes himself as a \"Scot in exile\". Riding away from the stables, John calls him a \"Crazy old fool\". Sean speaks of an \"Old Man Gray\" on the way to Caliga Hall in \"The Fine Joys of Tobacco\"; the game does not say which Gray he means.",
        "Son prénom est donné par son fils Beau (voir Citations). Aux écuries, John l'appelle Mr. Gray, et la lettre retrouvée près de son corps commence par \"Dear Mr. Gray\" ; l'historien y relève que son correspondant se présente lui-même comme un \"Scot in exile\" (un Écossais en exil). En quittant les écuries, John le traite de \"Crazy old fool\" (vieux fou). En route pour Caliga Hall dans \"The Fine Joys of Tobacco\", Sean parle d'un \"Old Man Gray\" (le vieux Gray), sans que le jeu précise de quel Gray il s'agit.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is an elderly man with a bald crown, dark hair streaked with gray on the sides and back, heavy dark eyebrows and a full graying beard. At the stables he wears a dark coat over a white shirt, a dark tie and a patterned vest.",
        "C'est un homme âgé, au sommet du crâne dégarni, aux cheveux sombres striés de gris sur les côtés et à l'arrière, aux sourcils épais et noirs, et à la barbe fournie qui grisonne. Aux écuries, il porte une veste sombre, une chemise blanche, une cravate foncée et un gilet à motifs.")},
]

# ---------------------------------------------------------------- CALIGA HALL (skills equivalent)
BLOCKS_SKILLS = [
    {"p": two(
        "Caliga Hall is the Gray family's house and tobacco plantation, just east of Rhodes; the Red Dead Wiki places it on the western edge of Bayou Nwa, in Lemoyne. In \"The New South\", the deputy Archibald MacGregor points out its tobacco fields to Arthur on the road to Rhodes (see Biography). The estate has a main house, stables, barns and cabins for the farmhands, with fields all around.",
        "Caliga Hall est la demeure et la plantation de tabac de la famille Gray, juste à l'est de Rhodes ; le Red Dead Wiki la situe à la lisière ouest du Bayou Nwa, en Lemoyne. Dans \"The New South\", sur la route de Rhodes, l'adjoint Archibald MacGregor montre ses champs de tabac à Arthur (voir la biographie). Le domaine compte une maison de maître, des écuries, des granges et des cabanes pour les ouvriers agricoles, entourées de champs.")},
    {"p": two(
        "Armed guards keep strangers out: in \"The Course of True Love I\", one stops Arthur at the entrance and tells him the property is private. According to Sean, wagons bring supplies, equipment and pay to the estate, which has taken on extra guards (see Biography for its state in 1907). The Red Dead Wiki says the house and grounds closely reproduce Shirley Plantation, in Virginia.",
        "Des gardes armés tiennent les étrangers à distance : dans \"The Course of True Love I\", l'un d'eux arrête Arthur à l'entrée et lui rappelle que la propriété est privée. D'après Sean, des chariots y livrent sans cesse vivres, matériel et paie, d'autant que le domaine a embauché des gardes en renfort (voir la biographie pour son état en 1907). Le Red Dead Wiki indique que la maison et ses abords reproduisent presque à l'identique la plantation Shirley, en Virginie.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": None, "slug": None, "name": "Beau Gray", "text": two(
        "His son (see Quotes for how he introduces himself). He is secretly in love with Penelope Braithwaite, of the rival family, and leaves Rhodes with her in chapter 6 with Arthur's help (see Biography).",
        "Son fils (voir Citations pour la façon dont il se présente). Il aime en secret Penelope Braithwaite, de la famille rivale, et quitte Rhodes avec elle au chapitre 6, avec l'aide d'Arthur (voir la biographie).")},
    {"img": None, "slug": None, "name": "Leigh Gray", "text": two(
        "The sheriff of Rhodes, killed in the Rhodes ambush: Tavish's brother according to Beau and both Red Dead Wikis, his son according to Dutch and Arthur (see Biography).",
        "Le shérif de Rhodes, tué dans l'embuscade de Rhodes : frère de Tavish pour Beau et les deux Red Dead Wiki, son fils pour Dutch et Arthur (voir la biographie).")},
    {"img": None, "slug": None, "name": "Murdo Gray", "text": two(
        "His father: Beau calls himself the grandson of old Murdo Gray, and the Red Dead Wiki lists Murdo as Tavish's father. Tavish says his father taught him to work (see In his own words).",
        "Son père : Beau se présente comme le petit-fils du vieux Murdo Gray, et le Red Dead Wiki fait de Murdo le père de Tavish. Tavish dit tenir de son père le goût du travail (voir Dans ses propres mots).")},
    {"img": None, "slug": None, "name": "Ross Gray", "text": two(
        "The ancestor who left Scotland for the colonies. The letter found beside Tavish's body says he was a paid informer for the Duke of Cumberland and stayed in Scotland until 1755 (see Biography).",
        "L'ancêtre qui a quitté l'Écosse pour les colonies. La lettre retrouvée près du corps de Tavish affirme qu'il était un informateur à la solde du duc de Cumberland et qu'il n'a quitté l'Écosse qu'en 1755 (voir la biographie).")},
    {"img": "catherine-braithwaite.jpeg", "slug": "catherine-braithwaite", "name": "Catherine Braithwaite", "text": two(
        "The head of the rival family. They never share a scene. He insults her and her sons and accuses them of killing his uncle (see Quotes). She hires the gang to burn his tobacco fields, while he sends it to steal her horses and sell them to a fence (see Biography).",
        "La cheffe de la famille rivale. Ils n'apparaissent jamais ensemble. Il l'insulte, elle et ses fils, et les accuse d'avoir tué son oncle (voir Citations). Elle engage le gang pour incendier ses champs de tabac, tandis que lui l'envoie voler ses chevaux pour les revendre à un receleur (voir la biographie).")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "John does most of the talking at the stables, accepts the deal and takes the fence's 700 dollars (see Biography).",
        "C'est John qui mène la discussion aux écuries ; il accepte le marché, puis empoche les 700 dollars du receleur (voir la biographie).")},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
        "Arthur joins John and Javier at the stables, asks how much gold is on offer and where to sell the horses. He steals them, then burns the Grays' tobacco fields for Catherine Braithwaite with Sean, and can find Tavish's body on a porch of Caliga Hall (see Biography).",
        "Arthur rejoint John et Javier aux écuries, demande combien d'or est en jeu et où vendre les chevaux. Il les vole, puis incendie les champs de tabac des Gray avec Sean pour le compte de Catherine Braithwaite, et peut découvrir le corps de Tavish sous un porche de Caliga Hall (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Javier is at the stables with John when Arthur arrives, and helps steal the horses (see Biography). He says nothing to Tavish at the stables.",
        "Javier est aux écuries avec John quand Arthur arrive, et participe au vol des chevaux (voir la biographie). Aux écuries, il ne dit pas un mot à Tavish.")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Dutch plans to make each family believe the gang is on its side, then rob both. He tells Arthur that the sheriff put in a word with his father, which is how John and Javier get the meeting at Caliga Hall. He never meets Tavish on screen. After Sean's death, in a rare camp line, Dutch swears the gang will make the Grays bleed.",
        "Dutch compte faire croire à chaque famille que le gang est de son côté, puis les dépouiller toutes les deux. Il explique à Arthur que le shérif a glissé un mot à son père, ce qui vaut à John et Javier leur rendez-vous à Caliga Hall. Il ne rencontre jamais Tavish à l'écran. Après la mort de Sean, dans une réplique rare au camp, Dutch jure que le gang fera saigner les Gray.")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "Hosea never shares a scene with Tavish. He works the Braithwaite side, and his dealings with Catherine lead to the fire in Tavish's fields (see Biography).",
        "Hosea n'apparaît jamais avec Tavish. Il s'occupe du côté Braithwaite, et ses tractations avec Catherine mènent à l'incendie des champs de Tavish (voir la biographie).")},
    {"img": "sean-macguire.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
        "Sean drives the wagon that gets Arthur into Caliga Hall and helps burn the fields (see Biography). He is shot dead in the Grays' ambush in Rhodes; the shooter is not named, and Tavish is not there.",
        "Sean conduit le chariot qui fait entrer Arthur à Caliga Hall et participe à l'incendie des champs (voir la biographie). Il est abattu dans l'embuscade des Gray à Rhodes ; le tireur n'est pas nommé, et Tavish n'est pas sur place.")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Bill says he has been making deals with the Gray men, and it is to him that they offer the security job in Rhodes. The job is the ambush in which Leigh Gray takes him hostage (see Biography).",
        "Bill affirme avoir monté des affaires avec les hommes des Gray, et c'est à lui qu'ils proposent le travail de protection à Rhodes. Ce travail est l'embuscade où Leigh Gray le prend en otage (voir la biographie).")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "Micah waits in Rhodes with Bill and Sean for Arthur before the security job, and fights the Grays' gunmen with Arthur (see Biography). He never meets Tavish.",
        "Micah attend Arthur à Rhodes avec Bill et Sean avant le travail de protection, et affronte avec Arthur les hommes armés des Gray (voir la biographie). Il ne rencontre jamais Tavish.")},
    {"img": None, "slug": None, "name": "Clay Davies", "text": two(
        "The fence at Clemens Cove that Tavish recommends, saying he will take the horses out of state for half their value. He pays 700 dollars for the three stallions (see Biography).",
        "Le receleur de Clemens Cove que recommande Tavish, en assurant qu'il fera sortir les chevaux de l'État et en donnera la moitié de leur valeur. Il paie 700 dollars pour les trois étalons (voir la biographie).")},
    {"img": None, "slug": None, "name": "Malcolm Moffat", "text": two(
        "The University of Edinburgh historian who answers a letter from Mr. Gray about his ancestor. His reply lies beside Tavish's body (see Biography).",
        "L'historien de l'université d'Édimbourg qui répond à la lettre de Mr. Gray sur son ancêtre. Sa réponse repose à côté du corps de Tavish (voir la biographie).")},
]
