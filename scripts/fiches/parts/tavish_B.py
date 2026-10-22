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
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include him. He has a single scene, at the Caliga Hall stables in \"Horse Flesh for Dinner\". In it he speaks of a family still struggling since the war and in need of stability. He insists on his Scottish roots and on the value of hard, fair work. He wants the theft done without any public link to his family. He describes the Braithwaites with insults and slurs, and accuses them of ruining the county and killing his uncle (see Quotes). He values the stolen horses at 5,000 dollars; the fence pays 700 (see Biography).",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang Van der Linde et ne le mentionnent pas. Il n'a qu'une scène, aux écuries de Caliga Hall, dans \"Horse Flesh for Dinner\". Il y parle d'une famille qui peine à se relever de la guerre et qui a besoin de stabilité. Il revendique ses racines écossaises et vante le travail dur mais honnête. Il veut que le vol ne puisse en aucun cas être relié publiquement à sa famille. Il couvre les Braithwaite d'insultes, les accuse d'avoir ruiné le comté et tué son oncle (voir Citations). Il estime les chevaux volés à 5 000 dollars ; le receleur en donne 700 (voir la biographie).")},
    {"p": two(
        "Dutch sums up the Grays as \"Scots... degenerates... drunkards\", adds that they are the local law and calls them \"Rich as Croesus\". His son Beau says the Grays have been the Braithwaites' murderers for so long that nobody can explain why, \"Beyond blind loyalty... and stupidity\".",
        "Dutch résume les Gray en trois mots, \"Scots... degenerates... drunkards\" (des Écossais… des dégénérés… des ivrognes), ajoute qu'ils tiennent la loi locale et les dit \"Rich as Croesus\" (riches comme Crésus). Son fils Beau explique que les Gray tuent des Braithwaite depuis si longtemps que plus personne ne sait pourquoi, \"Beyond blind loyalty... and stupidity\" (si ce n'est par loyauté aveugle… et par bêtise).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"ul": [
        two("\"We're an old Scottish family. We work. My daddy taught that to me, I taught my sons. Work hard, but fair.\" (to John)",
            "\"We're an old Scottish family. We work. My daddy taught that to me, I taught my sons. Work hard, but fair.\" (nous sommes une vieille famille écossaise, nous travaillons ; mon père me l'a appris, je l'ai appris à mes fils : travailler dur, mais honnêtement), à John."),
        two("\"We've got gold, Yankee... we've got gold.\" (to John, who asks what the family wants)",
            "\"We've got gold, Yankee... we've got gold.\" (on a de l'or, le Yankee… on a de l'or), à John, qui lui demande ce que veut la famille."),
        two("\"I'm Scottish.\" (after John claims that his own father came over from Scotland)",
            "\"I'm Scottish.\" (je suis écossais), quand John affirme que son propre père est venu d'Écosse."),
        two("\"Just keep us away from this... publicly I mean.\"",
            "\"Just keep us away from this... publicly I mean.\" (surtout, tenez-nous à l'écart de tout ça… publiquement, je veux dire)."),
    ]},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "His first name is given by his son Beau, who introduces himself as the son of Tavish Gray. At the stables John calls him Mr. Gray, and the letter found beside his body opens with \"Dear Mr. Gray\"; in it the historian notes that his correspondent describes himself as a \"Scot in exile\". On the way to Caliga Hall in \"The Fine Joys of Tobacco\", Sean says that \"Old Man Gray\" has doubled security; the game does not name him further. Riding away from the stables, John calls him a \"Crazy old fool\". Dutch and Arthur speak of him as the sheriff's father (see Relationships, Leigh Gray).",
        "Son prénom est donné par son fils Beau, qui se présente comme le fils de Tavish Gray. Aux écuries, John l'appelle Mr. Gray, et la lettre retrouvée près de son corps commence par \"Dear Mr. Gray\" ; l'historien y relève que son correspondant se présente lui-même comme un \"Scot in exile\" (un Écossais en exil). En route pour Caliga Hall dans \"The Fine Joys of Tobacco\", Sean raconte que \"Old Man Gray\" (le vieux Gray) a doublé la garde ; le jeu n'en dit pas plus sur ce personnage. En quittant les écuries, John le traite de \"Crazy old fool\" (vieux fou). Dutch et Arthur parlent de lui comme du père du shérif (voir Relations, Leigh Gray).")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is an elderly man, bald on top, with long gray hair on the sides, heavy dark eyebrows and a thick graying beard. At the stables he wears a dark suit over a white shirt.",
        "C'est un homme âgé, chauve sur le dessus du crâne, aux longs cheveux gris sur les côtés, aux sourcils épais et sombres et à la barbe fournie et grisonnante. Aux écuries, il porte un costume sombre sur une chemise blanche.")},
]

# ---------------------------------------------------------------- CALIGA HALL (skills equivalent)
BLOCKS_SKILLS = [
    {"p": two(
        "Caliga Hall is the Gray family's house and tobacco plantation, just east of Rhodes; the Red Dead Wiki places it on the western edge of Bayou Nwa, in Lemoyne. In \"The New South\", the deputy Archibald MacGregor points out its tobacco fields to Arthur, says the Grays have lived there for generations and that they own all the businesses in Rhodes, including the Rhodes Parlor House. The estate has a main house, stables, barns and cabins for the farmhands, with fields all around.",
        "Caliga Hall est la demeure et la plantation de tabac de la famille Gray, juste à l'est de Rhodes ; le Red Dead Wiki la situe à la lisière ouest du Bayou Nwa, en Lemoyne. Dans \"The New South\", l'adjoint Archibald MacGregor montre ses champs de tabac à Arthur, explique que les Gray y vivent depuis des générations et qu'ils possèdent tous les commerces de Rhodes, dont le saloon Rhodes Parlor House. Le domaine compte une maison de maître, des écuries, des granges et des cabanes pour les ouvriers agricoles, entourées de champs.")},
    {"p": two(
        "Armed guards keep strangers out: in \"The Course of True Love I\", one stops Arthur at the entrance and tells him the property is private. In \"The Fine Joys of Tobacco\", Sean reports that security has been doubled since the saloon incident, and that supply and payroll wagons come and go for the extra men. According to the Red Dead Wiki, the family still owns the estate in 1907, the fields are still worked and guards patrol at night. The same wiki says the house and grounds closely reproduce Shirley Plantation, in Virginia.",
        "Des gardes armés tiennent les étrangers à distance : dans \"The Course of True Love I\", l'un d'eux arrête Arthur à l'entrée et lui rappelle que la propriété est privée. Dans \"The Fine Joys of Tobacco\", Sean rapporte que la garde a été doublée depuis l'incident du saloon, et que les chariots de ravitaillement et de paie défilent pour les hommes recrutés en renfort. D'après le Red Dead Wiki, la famille possède toujours le domaine en 1907, les champs sont encore cultivés et des gardes patrouillent la nuit. Le même wiki indique que la maison et ses abords reproduisent presque à l'identique la plantation Shirley, en Virginie.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": None, "slug": None, "name": "Beau Gray", "text": two(
        "His son. Beau introduces himself to Arthur as the son of Tavish Gray, the nephew of Sheriff Leigh Gray and the grandson of Murdo Gray. He is secretly in love with Penelope Braithwaite, of the rival family, and leaves Rhodes with her in chapter 6 with Arthur's help (see Biography).",
        "Son fils. Beau se présente à Arthur comme le fils de Tavish Gray, le neveu du shérif Leigh Gray et le petit-fils de Murdo Gray. Il aime en secret Penelope Braithwaite, de la famille rivale, et quitte Rhodes avec elle au chapitre 6, avec l'aide d'Arthur (voir la biographie).")},
    {"img": None, "slug": None, "name": "Leigh Gray", "text": two(
        "The sheriff of Rhodes. The game gives two versions of their link. Beau calls Leigh his uncle, which makes him Tavish's brother, and both Red Dead Wikis (EN and FR) list him as such. Dutch, on the other hand, says the sheriff put in a word for the gang with his father, and Arthur asks Tavish whether the sheriff is his son; Tavish does not correct him. Leigh dies in the Rhodes ambush, where Tavish is not present (see Biography).",
        "Le shérif de Rhodes. Le jeu donne deux versions de leur lien. Beau appelle Leigh son oncle, ce qui en fait le frère de Tavish, et les deux Red Dead Wiki (anglais et français) le présentent ainsi. Dutch affirme au contraire que le shérif a recommandé la bande à son père, et Arthur demande à Tavish si le shérif est son fils ; Tavish ne le reprend pas. Leigh meurt dans l'embuscade de Rhodes, à laquelle Tavish n'assiste pas (voir la biographie).")},
    {"img": None, "slug": None, "name": "Murdo Gray", "text": two(
        "His father, according to the Red Dead Wiki; Beau calls himself the grandson of old Murdo Gray. Tavish says his father taught him to work (see In his own words).",
        "Son père, d'après le Red Dead Wiki ; Beau se présente comme le petit-fils du vieux Murdo Gray. Tavish dit tenir de son père le goût du travail (voir Dans ses propres mots).")},
    {"img": None, "slug": None, "name": "Ross Gray", "text": two(
        "The ancestor who left Scotland for the colonies. The letter found beside Tavish's body says he was a paid informer for the Duke of Cumberland, not an exiled Jacobite (see Biography).",
        "L'ancêtre qui a quitté l'Écosse pour les colonies. La lettre retrouvée près du corps de Tavish affirme qu'il était un informateur payé par le duc de Cumberland, et non un jacobite exilé (voir la biographie).")},
    {"img": "catherine-braithwaite.jpeg", "slug": "catherine-braithwaite", "name": "Catherine Braithwaite", "text": two(
        "The head of the rival family. They never share a scene. He calls her a hag, calls her sons inbred and accuses them of killing his uncle (see Quotes). She pays the gang to burn his tobacco fields, while he pays it to steal her horses (see Biography).",
        "La cheffe de la famille rivale. Ils n'apparaissent jamais ensemble. Il la traite de vieille sorcière, dit de ses fils qu'ils sont consanguins et les accuse d'avoir tué son oncle (voir Citations). Elle paie le gang pour incendier ses champs de tabac, pendant que lui le paie pour voler ses chevaux (voir la biographie).")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "John does most of the talking at the stables. He tells Tavish the newcomers lost money in the west on a failed railway speculation, and claims a father who came over from Scotland. He accepts the deal and later takes the 700 dollars the fence offers (see Biography). He calls Tavish a crazy old fool as they ride off (see Names).",
        "C'est John qui mène la discussion aux écuries. Il raconte à Tavish que les nouveaux venus ont perdu de l'argent dans l'Ouest sur une spéculation ferroviaire ratée, et affirme que son père est venu d'Écosse. Il accepte le marché, puis les 700 dollars proposés par le receleur (voir la biographie). En repartant, il traite Tavish de vieux fou (voir Noms).")},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
        "Arthur joins John and Javier at the stables, asks how much gold is on offer and where to sell the horses. He steals them, then burns the Grays' tobacco fields for Catherine Braithwaite with Sean, and can find Tavish's body on a porch of Caliga Hall (see Biography). In his journal he writes after the sale that they felt like prize idiots.",
        "Arthur rejoint John et Javier aux écuries, demande combien d'or est en jeu et où vendre les chevaux. Il les vole, puis incendie les champs de tabac des Gray avec Sean pour le compte de Catherine Braithwaite, et peut découvrir le corps de Tavish sous un porche de Caliga Hall (voir la biographie). Après la vente, il note dans son journal qu'ils se sont sentis comme de parfaits idiots.")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Javier is at the stables with John when Arthur arrives, and helps steal the horses (see Biography). Tavish does not speak to him.",
        "Javier est aux écuries avec John quand Arthur arrive, et participe au vol des chevaux (voir la biographie). Tavish ne lui adresse pas la parole.")},
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
        "Micah rides into Rhodes with Arthur, Bill and Sean for the security job, and fights the Grays' gunmen with Arthur (see Biography). He never meets Tavish.",
        "Micah se rend à Rhodes avec Arthur, Bill et Sean pour le travail de protection, et affronte avec Arthur les hommes armés des Gray (voir la biographie). Il ne rencontre jamais Tavish.")},
    {"img": None, "slug": None, "name": "Clay Davies", "text": two(
        "The fence at Clemens Cove that Tavish recommends, saying he will take the horses out of state for half their value. He pays 700 dollars for the three stallions (see Biography).",
        "Le receleur de Clemens Cove que recommande Tavish, en assurant qu'il fera sortir les chevaux de l'État et en donnera la moitié de leur valeur. Il paie 700 dollars pour les trois étalons (voir la biographie).")},
    {"img": None, "slug": None, "name": "Malcolm Moffat", "text": two(
        "The University of Edinburgh historian who answers a letter from a Mr. Gray about his ancestor. His reply lies beside Tavish's body (see Biography).",
        "L'historien de l'université d'Édimbourg qui répond à la lettre d'un certain Mr. Gray sur son ancêtre. Sa réponse repose à côté du corps de Tavish (voir la biographie).")},
]
