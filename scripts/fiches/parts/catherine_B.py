"""Catherine Braithwaite, part B: Personality (how others describe her, In her own words, Names, Appearance),
The Braithwaite estate (moonshine, horses, the manor and its guards, cribbage), Relationships (22 Oct 2026, medium tier).

Coverage: the Red Dead Wiki "Character" section (Personality, Appearance) and the family/estate facts of the character
page, plus the family members' pages, all rewritten; Catherine's own lines are quoted from a full game transcript.

SOURCE REGISTER (fetched 22 Oct 2026, saved in scripts/v3/work/catherine/fc/ and scripts/v3/work/_m/):
- Full game transcript, "Red Dead Redemption 2 Full Transcript", Game Scripts Wiki (blogspot), Jan 2022
  (fc/gsw.txt). The Red Dead Wiki has no "/dialogues" page for her three missions, so every quoted line of hers
  comes from this transcript, cross-checked where possible with the wiki's quote box ("Ain't no rules in war...")
  and its footnote ("for 120 years"). Scenes used: "American Distillation" (Archibald MacGregor on the Braithwaites:
  "Old cotton family", stills "hidden all over Lemoyne", "in business with" the Lemoyne Raiders, "a rather...
  expensive interest in thoroughbred horses"); "The Course of True Love III" (Beau: "Catherine Braithwaite's got a
  daughter... no one's seen her in years... she weren't right"); "Advertising, The New American Art" (guard, price,
  "Old Sheriff Gray", "Momma!", "promotional expense", cribbage invitation; Hosea "old Ma Braithwaite"; Dutch's
  "Moonshiners... hypocritical"); "Horse Flesh for Dinner" (Tavish: "That hag and her inbred sons"; the stable hand
  names Cerberus, Old Faithful and Old Father Time); "The Fine Joys of Tobacco" (cribbage scene, "as big and as dumb
  as he looks", "we've got money, Mr. Matthews", Bartholomew's "Yankee numbskull"; Sean's insults, "fitting");
  "Blood Feuds, Ancient and Modern" (all lines of the confrontation, "old woman", "hag", "Boys are off limits",
  "I told you she was crazy"); "The Course of True Love V" ("Aunt Catherine").
- Red Dead Wiki EN: "Catherine Braithwaite" (Personality, Appearance), "Braithwaite Family", "Braithwaite Manor"
  (layout, stables, guards that do not respawn in chapters 4 to 6, fishing community by 1907), "Horse Flesh for
  Dinner" (Braithwaite insignia on the stolen horses, sold for 700 dollars), "Gertrude Braithwaite" (outhouse, point
  of interest, name only in the credits, remains in the epilogue), "Penelope Braithwaite", "Bartholomew
  Braithwaite" (Red Dead Online, A Life of 'Shine), "Gareth Braithwaite" (subtitle label), "Gerald Braithwaite".
- Camp Events (scripts/v3/sources/Camp_Events.txt), Shady Belle chapter: Kieran's apology to Abigail.
- Rockstar's character descriptions of 6 Sep 2018 (scripts/v3/sources/thr_descriptions.txt) cover the gang only:
  none for her.
- Fact-checked fiches reused for consistency: hosea_B/hosea_C (cribbage, 10 dollars), dutch_A/dutch_C (Bartholomew
  shot at the start), angelo_A/angelo_B (letter, five years), abigail_B, jack_A, sean_B, javier_A.

OWNERSHIP: lines quoted in "In her own words" must be REMOVED from part C Quotes: "I ain't in the market for what's
already mine."; "Oh, I know exactly who gave you your orders. Old Sheriff Gray."; "So this one... he as big and as
dumb as he looks?"; "We have lived in this house for a hundred and twenty years. We never had no problems 'cept for
Yankees."; "Oh, I know your type. Common scum."; "You stole my liquor. You stole my horses. Ain't no rules in war,
Mr..." Lines left for C: "Dollar a bottle", "promotional expense", the cribbage invitation, "Oh, we've got money,
Mr. Matthews", "You killed my sons", "You filth", "You damn yankee", "I never liked you", "My sons gave him to Angelo
Bronte...". Names quoted here (Momma, old Ma Braithwaite, Aunt Catherine, hag, old woman) are not repeated in C.
Other characters' descriptions of her (Archibald, Dutch, Tavish, Sean) are quoted HERE only; relationship entries
paraphrase. Narrative events (theft of the moonshine, the saloon, the fields, the horse theft, the kidnapping, the
assault, her death, her letter to Bronte) belong to part A; entries below point to them.

WIKI-ONLY (kept, attributed): the outhouse daughter's name, the sanatorium reason and her remains in the epilogue;
the Braithwaite insignia on the horses; the guards' behavior in chapters 4 to 6 and the fishing community of 1907;
Bartholomew's Red Dead Online role; the subtitle label of the son at the door.

EXCLUDED: the wiki's "snobbish elite", "strong sense of superiority", "far from foolish", "prioritize her family's
reputation" and the horse passion "implied ... sentimental value or a show of wealth" (interpretation; Archibald's
own words are quoted instead); the wiki's "self-immolation" (interpretation of her running back into the house);
the Villains Wiki aliases and labels; the breed of the stolen horses (Arabian in the wiki's tips, Turkoman in a video
reference: conflicting); the gold bar in the lockbox near her body and "Catherine's Brooch" (part C, Trivia); the
Red Dead Online horse theft for Trelawny (part C, Other media); the incest and abuse theories about Gertrude (wiki
speculation); the middle son of the letter (part A); the 700 dollars the horses fetch against the 5,000 promised (part A, mission outcome); who fired the shots that killed Gareth and Gerald (HOUSE rule).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include her. In \"American Distillation\", the deputy Archibald MacGregor calls the Braithwaites an \"old cotton family\" turned to moonshine and says that Catherine has \"a rather... expensive interest in thoroughbred horses\". Dutch sums up the family as \"Moonshiners... hypocritical\". Tavish Gray speaks of \"that hag and her inbred sons\". Sean MacGuire insults her at length after the cribbage meeting.",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang Van der Linde et ne la mentionnent pas. Dans \"American Distillation\", l'adjoint Archibald MacGregor présente les Braithwaite comme une \"old cotton family\" (vieille famille de planteurs de coton) reconvertie dans l'alcool de contrebande, et prête à Catherine \"a rather... expensive interest in thoroughbred horses\" (un goût assez coûteux pour les pur-sang). Dutch résume la famille en deux mots : \"Moonshiners... hypocritical\" (des bouilleurs de cru… hypocrites). Tavish Gray parle de \"that hag and her inbred sons\" (cette vieille sorcière et ses fils consanguins). Sean MacGuire, lui, l'insulte copieusement après la partie de cribbage.")},
    {"p": two(
        "In the game she gives the orders: her sons draw their guns, and she tells them to stand down. She answers threats with a laugh and turns a sale she refuses into a paid errand. She knows who is behind the theft of her liquor before anyone tells her. She addresses outsiders with open contempt, and \"Yankee\" is her insult of choice. Even at gunpoint, she meets the gang's questions with insults.",
        "Dans le jeu, c'est elle qui donne les ordres : ses fils dégainent, elle leur fait baisser leurs armes. Elle répond aux menaces par un rire et transforme une vente qu'elle refuse en course rémunérée. Elle sait qui a commandité le vol de son alcool avant qu'on le lui dise. Elle traite les étrangers avec un mépris affiché, et \"Yankee\" est son insulte favorite. Même sous la menace d'une arme, elle répond aux questions du gang par des insultes.")},
    {"h4": two("In her own words", "Dans ses propres mots")},
    {"ul": [
        two("\"I ain't in the market for what's already mine.\" (to Hosea, who offers to sell her back her moonshine)",
            "\"I ain't in the market for what's already mine.\" (je n'achète pas ce qui m'appartient déjà), à Hosea, qui lui propose de racheter son propre alcool."),
        two("\"Oh, I know exactly who gave you your orders. Old Sheriff Gray.\"",
            "\"Oh, I know exactly who gave you your orders. Old Sheriff Gray.\" (oh, je sais très bien qui vous a donné vos ordres : ce vieux shérif Gray)."),
        two("\"So this one... he as big and as dumb as he looks?\" (on meeting Arthur at the cribbage table)",
            "\"So this one... he as big and as dumb as he looks?\" (et celui-là, il est aussi grand et aussi bête qu'il en a l'air ?), en découvrant Arthur à la table de cribbage."),
        two("\"We have lived in this house for a hundred and twenty years. We never had no problems 'cept for Yankees.\"",
            "\"We have lived in this house for a hundred and twenty years. We never had no problems 'cept for Yankees.\" (nous vivons dans cette maison depuis cent vingt ans, et nous n'avons jamais eu d'ennuis, sauf avec les Yankees)."),
        two("\"Oh, I know your type. Common scum.\" (to Dutch)",
            "\"Oh, I know your type. Common scum.\" (oh, je connais votre espèce : de la vulgaire racaille), à Dutch."),
        two("\"You stole my liquor. You stole my horses. Ain't no rules in war, Mr...\" (to Hosea, who tells her that boys are off limits)",
            "\"You stole my liquor. You stole my horses. Ain't no rules in war, Mr...\" (vous avez volé mon alcool, vous avez volé mes chevaux ; il n'y a pas de règles à la guerre, monsieur…), à Hosea, qui lui rappelle qu'on ne touche pas aux enfants."),
    ]},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "The guard at the gate introduces her as \"Mrs. Catherine Braithwaite\", and Hosea calls her Mrs. Braithwaite. One of her sons calls her \"Momma\". After the saloon job, Hosea calls her \"old Ma Braithwaite\". Dutch calls her \"old woman\" and \"hag\", a word Sean and Tavish Gray also use. Her niece Penelope speaks of her as \"Aunt Catherine\". The gang usually refers to her as the Braithwaite woman.",
        "Le garde de l'entrée l'annonce comme \"Mrs. Catherine Braithwaite\", et Hosea l'appelle Mrs. Braithwaite. L'un de ses fils l'appelle \"Momma\" (maman). Après l'épisode du saloon, Hosea parle d'elle comme de \"old Ma Braithwaite\" (la vieille mère Braithwaite). Dutch la traite de \"old woman\" (vieille femme) et de \"hag\" (vieille sorcière), un mot que Sean et Tavish Gray emploient aussi. Sa nièce Penelope l'appelle \"Aunt Catherine\" (tante Catherine). Dans le gang, on la désigne le plus souvent comme la femme Braithwaite.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "She is an elderly woman with gray hair gathered in a bun. At the manor she wears a purple dress with a wide gray collar, fastened at the throat by a brooch set with a blue stone.",
        "C'est une femme âgée aux cheveux gris relevés en chignon. Au manoir, elle porte une robe violette à large col gris, fermée au cou par une broche ornée d'une pierre bleue.")},
]

# ---------------------------------------------------------------- ESTATE (skills equivalent)
BLOCKS_SKILLS = [
    {"h3": two("Moonshine", "L'alcool de contrebande")},
    {"p": two(
        "The family's money now comes from moonshine. According to Archibald MacGregor, the Braithwaites keep stills hidden all over Lemoyne, and a new one appears as soon as the law destroys one. He also says they are in business with the Lemoyne Raiders. Catherine sells her liquor at a dollar a bottle. Her letter to Angelo Bronte, found in the manor, describes him as her most valued customer (see Biography).",
        "L'argent de la famille vient désormais de l'alcool de contrebande. Selon Archibald MacGregor, les Braithwaite cachent des alambics dans tout le Lemoyne, et un nouveau surgit dès que la loi en détruit un. Il ajoute qu'ils font affaire avec les Lemoyne Raiders. Catherine vend son alcool un dollar la bouteille. Sa lettre à Angelo Bronte, retrouvée dans le manoir, le présente comme son client le plus précieux (voir la biographie).")},
    {"h3": two("Horses", "Les chevaux")},
    {"p": two(
        "The family's prized horses are kept in the stables south of the manor. In \"Horse Flesh for Dinner\", the stable hand presents three studs by name: Cerberus, Old Faithful and Old Father Time. According to the Red Dead Wiki, the horses the gang steals carry the Braithwaite insignia on their hindquarters.",
        "Les chevaux de prix de la famille logent dans les écuries situées au sud du manoir. Dans \"Horse Flesh for Dinner\", le palefrenier présente trois étalons par leur nom : Cerberus, Old Faithful et Old Father Time. Selon le Red Dead Wiki, les chevaux volés par le gang portent l'emblème des Braithwaite sur la croupe.")},
    {"h3": two("The manor and its guards", "Le manoir et ses gardes")},
    {"p": two(
        "Braithwaite Manor stands in Scarlett Meadows, in Lemoyne, on a plantation of corn, tobacco and cotton fields with stables, cabins, boathouses and a gazebo by the water. Armed men guard the gate and patrol the grounds. Inside, she receives her visitors in the living room, where she plays cribbage with Hosea and Sean. According to the Red Dead Wiki, guards still hold the burned grounds from chapter 4 to the end of chapter 6 and are not replaced once killed. By 1907 they are gone, and a small fishing community has settled by the old docks.",
        "Braithwaite Manor se dresse dans les Scarlett Meadows, en Lemoyne, au milieu d'une plantation de maïs, de tabac et de coton, avec écuries, cabanes, hangars à bateaux et un kiosque au bord de l'eau. Des hommes armés gardent l'entrée et patrouillent sur le domaine. À l'intérieur, elle reçoit ses visiteurs au salon, où elle joue au cribbage avec Hosea et Sean. D'après le Red Dead Wiki, des gardes occupent encore le domaine incendié du chapitre 4 à la fin du chapitre 6, et ceux qui tombent ne sont pas remplacés. En 1907, ils ont disparu, et une petite communauté de pêcheurs s'est installée près des anciens quais.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "Dutch gives Hosea the Braithwaites to work on. He sells her back her own moonshine, plays cribbage with her and vouches for Arthur, then questions her outside the burning house (see Biography). Hosea mocks her as the fire spreads, and calls her crazy before the gang rides off.",
        "Dutch confie les Braithwaite à Hosea. Il lui revend son propre alcool, joue au cribbage avec elle et se porte garant d'Arthur, puis l'interroge devant la maison en flammes (voir la biographie). Hosea se moque d'elle pendant que le feu gagne, et la traite de folle avant que le gang ne reparte.")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Dutch plans to play the Braithwaites and the Grays against each other and leaves the Braithwaites to Hosea. After Jack's kidnapping he leads the assault on the manor, kills one of her sons in front of her and drags her outside (see Biography). He threatens her and insults her; she calls him a damn Yankee.",
        "Dutch compte monter les Braithwaite et les Gray les uns contre les autres et laisse les Braithwaite à Hosea. Après l'enlèvement de Jack, il mène l'assaut contre le manoir, abat l'un de ses fils sous ses yeux et la traîne dehors (voir la biographie). Il la menace et l'insulte ; elle le traite de sale Yankee.")},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
        "Arthur brings her the moonshine with Hosea, burns the Grays' fields on her behalf, steals her horses for Tavish Gray and breaks into the room where she hides with her sons (see Biography). At their second meeting she asks whether he is as dumb as he looks (see In her own words).",
        "Arthur lui apporte l'alcool avec Hosea, incendie les champs des Gray pour son compte, vole ses chevaux pour Tavish Gray et force la porte de la pièce où elle se cache avec ses fils (voir la biographie). À leur deuxième rencontre, elle demande s'il est aussi bête qu'il en a l'air (voir Dans ses propres mots).")},
    {"img": "sean-macguire.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
        "Sean sits in on the cribbage meeting and keeps quiet. On the way to Caliga Hall he tells Arthur how much he disliked her and her son, and says she wanted the fields burned with her own moonshine because it would be fitting. Once the fields are on fire, he says she got her money's worth.",
        "Sean assiste à la partie de cribbage sans dire un mot. En route pour Caliga Hall, il confie à Arthur tout le mal qu'il pense d'elle et de son fils, et rapporte qu'elle tenait à faire brûler les champs avec son propre alcool, ce qu'elle trouvait approprié. Une fois les champs en feu, il estime qu'elle en a eu pour son argent.")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "Her men take the boy from the gang's camp at Clemens Point, and her sons hand him over to Angelo Bronte (see Biography). Jack is not at the manor when the gang storms it.",
        "Ses hommes enlèvent l'enfant au camp du gang à Clemens Point, et ses fils le livrent à Angelo Bronte (voir la biographie). Jack n'est pas au manoir quand le gang le prend d'assaut.")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "Jack's father steals her horses with Arthur and Javier, then takes part in the assault on the manor to get his son back (see Biography).",
        "Le père de Jack vole ses chevaux avec Arthur et Javier, puis participe à l'assaut contre le manoir pour récupérer son fils (voir la biographie).")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "Jack's mother stays at camp while the gang rides to Braithwaite Manor (see Biography).",
        "La mère de Jack reste au camp pendant que le gang chevauche jusqu'à Braithwaite Manor (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Javier helps steal her prized horses for Tavish Gray, and rides to the manor for the assault (see Biography).",
        "Javier participe au vol de ses chevaux de prix pour Tavish Gray, et se rend au manoir pour l'assaut (voir la biographie).")},
    {"img": "kieran-duffy.jpeg", "slug": "kieran-duffy", "name": "Kieran Duffy", "text": two(
        "According to Hosea, Kieran saw a couple of men near the camp who sounded like Braithwaite sons. At Shady Belle he apologizes to Abigail: he had seen the Braithwaites come to camp and knew Arthur and Hosea were dealing with them, but did not imagine they would take Jack.",
        "D'après Hosea, Kieran a vu près du camp deux hommes qui, à l'entendre, ressemblaient aux fils Braithwaite. À Shady Belle, il s'excuse auprès d'Abigail : il avait vu les Braithwaite venir au camp et savait qu'Arthur et Hosea traitaient avec eux, mais n'imaginait pas qu'ils enlèveraient Jack.")},
    {"img": "angelo-bronte.jpeg", "slug": "angelo-bronte", "name": "Angelo Bronte", "text": two(
        "The Saint Denis crime lord has been doing business with her family for five years, according to her letter to him. Her sons hand Jack over to him, and she gives his name to the gang (see Biography).",
        "Le parrain de Saint-Denis fait affaire avec sa famille depuis cinq ans, d'après la lettre qu'elle lui adresse. Ses fils lui livrent Jack, et elle donne son nom au gang (voir la biographie).")},
    {"img": "tavish-gray.jpeg", "slug": "tavish-gray", "name": "Tavish Gray", "text": two(
        "The head of the rival Gray family hires Arthur, John and Javier to steal her horses. He tells them that she and her sons have ruined the county and killed his uncle.",
        "Le chef de la famille rivale des Gray engage Arthur, John et Javier pour voler ses chevaux. Il leur affirme qu'elle et ses fils ont ruiné le comté et tué son oncle.")},
    {"img": None, "slug": None, "name": "Leigh Gray", "text": two(
        "She knows that the sheriff of Rhodes, a Gray, sent the gang to take her moonshine (see In her own words).",
        "Elle sait que le shérif de Rhodes, un Gray, a envoyé le gang lui prendre son alcool (voir Dans ses propres mots).")},
    {"img": None, "slug": None, "name": "Bartholomew Braithwaite", "text": two(
        "Her son greets Hosea and Arthur with a shotgun until she tells him to pay them, and insults Hosea at the cribbage meeting. Dutch shoots him outside the manor as the assault begins (see Biography). According to the Red Dead Wiki, the subtitles of that scene label him Gareth. He also appears in Red Dead Online, in the moonshine business storyline.",
        "Son fils accueille Hosea et Arthur un fusil à la main jusqu'à ce qu'elle lui ordonne de les payer, et insulte Hosea pendant la partie de cribbage. Dutch l'abat devant le manoir au moment où l'assaut commence (voir la biographie). Selon le Red Dead Wiki, les sous-titres de cette scène le désignent sous le nom de Gareth. Il apparaît aussi dans Red Dead Online, dans l'intrigue des bouilleurs de cru.")},
    {"img": None, "slug": None, "name": "Gareth and Gerald Braithwaite", "text": two(
        "According to the Red Dead Wiki, her two other sons stand with her when Hosea and Arthur first ride in. During the assault they barricade themselves upstairs with her, and both die in that room (see Biography).",
        "Selon le Red Dead Wiki, ses deux autres fils se tiennent à ses côtés à la première visite d'Hosea et d'Arthur. Pendant l'assaut, ils se barricadent avec elle à l'étage, et meurent tous les deux dans cette pièce (voir la biographie).")},
    {"img": None, "slug": None, "name": "Gertrude Braithwaite", "text": two(
        "Beau Gray tells Arthur that Catherine has a daughter nobody has seen for years, who was not right. According to the Red Dead Wiki, this daughter is the woman locked in an outhouse near the manor, a point of interest only Arthur can discover. Penelope tells Arthur that the family kept her there rather than send her to a sanatorium. The wiki adds that her name appears only in the credits and that her remains are still in the outhouse in the epilogue.",
        "Beau Gray confie à Arthur que Catherine a une fille que personne n'a vue depuis des années et qui n'allait pas bien. Selon le Red Dead Wiki, il s'agit de la femme enfermée dans une cabane de latrines près du manoir, un lieu d'intérêt que seul Arthur peut découvrir. Penelope explique à Arthur que la famille l'a gardée là plutôt que de l'envoyer en maison de santé. Le wiki ajoute que son nom n'apparaît qu'au générique et que ses restes se trouvent toujours dans la cabane pendant l'épilogue.")},
    {"img": None, "slug": None, "name": "Penelope Braithwaite", "text": two(
        "Her niece loves Beau Gray, from the rival family. In chapter 6, before eloping with him, she mentions what happened to her aunt and cousins and says the survivors of both families are angrier than ever.",
        "Sa nièce aime Beau Gray, de la famille rivale. Au chapitre 6, avant de s'enfuir avec lui, elle évoque le sort de sa tante et de ses cousins et constate que les survivants des deux familles sont plus en colère que jamais.")},
]
