"""Luisa Fortuna, part B: Personality (official description, observable traits, In her own words, Names, Appearance),
Weapons and gameplay (the fiche-specific skills section), Relationships (21 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN infobox (aka Laura and "Peasent" by Reyes, family, affiliations, weapons, voice), its
Personality material folded into the History section (devotion to Reyes, the name confusion, her cooling towards John, the
Allende line), the trivia items that belong here (no horse riding, gold cross necklace, Jack's name, meaning of the
surname), the FR wiki infobox (surname Laura, allies, enemy) and anecdote (never rides a horse); the seven RDR1 transcripts
of her missions plus "The Gates of El Presidio" (Reyes on her, without her); the mission pages of her seven missions
(failure conditions, wagon driving, church prayer, body not lootable); the wiki pages of her family, Carlos and Victor.
Narrative events are told in part A; the entries below point to them.

SOURCE REGISTER (read 21 Oct 2026; wiki cache scripts/v3/work/_m/):
- Official description: Rockstar Newswire, "Original Red Dead Redemption Artwork: Luisa Fortuna & Irish", posted
  May 3, 2010 (archived copy saved as scripts/v3/work/luisa/fc/newswire_2010-05-03_artwork_luisa_irish.txt):
  "Luisa Fortuna is a 19-year old Mexican teacher and revolutionary, who knows how to handle a sidearm." Rockstar's
  6 Sep 2018 descriptions cover the RDR2 gang only. The GOTY guide (birth 1892) is cited by the wiki only: facts grid (D).
- Transcripts, her own lines (every quoted line checked): "Landon Ricketts Rides Again/dialogues", "The Mexican Wagon
  Train/dialogues", "My Sister's Keeper/dialogues", "Must a Savior Die?/dialogues", "Father Abraham/dialogues", "Captain
  De Santa's Downfall/dialogues", "An Appointed Time/dialogues".
- Transcripts, what others say of her: the same files (Ricketts, John, Reyes, Carlos, Miranda, Victor) and "The Gates of
  El Presidio/dialogues" (Reyes and John at Agave Viejo).
- Mission pages: "Landon Ricketts Rides Again" (failure: kills Luisa; she is carried out unconscious), "The Mexican Wagon
  Train" (trivia: she prays at the altar of the Chuparosa church), "Must a Savior Die?" (John rides shotgun in her cart;
  failure: assaults, kills or abandons her, kills the horses; she may crash the wagon if the ride is not skipped), "Father
  Abraham" (failure: assaults or kills her, kills the horses of her carriage), "Captain De Santa's Downfall" (failure:
  assaults or kills Luisa or any rebel), "An Appointed Time" (her body cannot be looted).
- Other wiki pages: "Emilio Fortuna" (older brother, stagecoach driver), "Miranda Fortuna" (younger sister), "Mr. Fortuna",
  "Mrs. Fortuna", "Carlos" (butcher of El Matadero, takes her home on horseback), "Victor Melendez", "Raul Zubieta".
- Consistency: reyes_B (Luisa entry), landon_B (Emilio, Carlos), allende_B (Luisa entry), desanta_B (Luisa entry),
  nigel_B (the three major characters who never ride a horse, attributed to the wiki), HOUSE_FACTS (death at Escalera,
  shot by the soldiers guarding Reyes; John's daughter worded "a daughter who died").
- Visual check: live portrait.jpeg (characters/luisa-fortuna/) for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only (parts A and C must not repeat them): the Newswire description; Victor's "She can fight as well as
  any man."; the four "In her own words" lines ("Don't worry about me, Mr. Marston. I am living in history. I am not afraid
  to die.", "Revolutions are always won with blood.", "Be honest with yourself and you will be free.", "Every time Allende
  hits us, we hit him back harder."); in Names: "my young lover, Laura", "Laura, dame la fuerza para luchar", "Laura's
  Day", "little more than a peasant girl", "These peasant girls", "Mi amiga".
- Paraphrased here, left to part C Quotes: "I would rather be dead than a cynic like you", "Your nobility's almost as
  affecting as your naivety", the married-in-our-hearts lines, "I still can't forgive you for helping Allende", "You make a
  choice by not making a choice", "Allende es pura maldad", "That wretched animal, De Santa", the Ricketts lines ("fine
  young woman, teacher", "For once, I agree with Allende"), "Thank you for saving me. You're good men...", "I don't weep
  for myself...", "Great and terrible things!", "My father must not die in vain!", "Déjen mi hombre!", Reyes's lines from
  "The Gates of El Presidio" and "An Appointed Time", John's "People like Luisa".
- Gameplay HERE only: weapons, wagon driving, no horse riding, failure conditions, loot, the church prayer.
- Told once elsewhere, pointer here: every mission event (A); birth year, her schooling and English (A Origins / D facts);
  her father's death (A); Undead Nightmare model (A); multiplayer model and the dress/chaps difference (C Other media);
  actor, pre-release look and the Newswire artwork release (D); WhatCulture and Aldape (D Reception).

WIKI-ONLY (kept, attributed): Cattleman Revolver and Hunting Knife (EN infobox); never rides a horse (EN trivia, FR
anecdote); the gold cross necklace "throughout the game" (EN trivia); Emilio as older brother and stagecoach driver,
Miranda as younger sister (family pages); the church prayer and the wagon crash (mission pages).

Excluded: Reyes's "some peasant girl with a tight c*nt" (EN wiki trivia; in no transcript, Reyes's actual words in "The
Gates of El Presidio" are "some peasant girl with the hands of a farmer"); "uses her for sex", "endlessly faithful",
"unconcerned about how Reyes views her", "her relationship with John deteriorates", "less friendly with him after the Army
missions" (wiki readings; the lines themselves are given); the "irony" of the surname and "a better fate than being
abused" (interpretation); the Flowering Judas parallel (literary comparison, no source); Alejandro Fortuna's grave at
Sepulcro "may be related" (speculation); her father teaching her to read and write Spanish, "we may be poor but we are not
stupid" (Mr. Fortuna page; in no transcript); "she does not even seem to care" when called Laura (wiki reading); the PS3
bugs (Luisa vanishing, running in circles, negative comments after a good detonation); Luisa as "rebel leader" (Miranda
page; she leads men in two missions, said as such).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "When it added her artwork to the official Red Dead Redemption website, Rockstar described her on its Newswire on May 3, 2010: \"Luisa Fortuna is a 19-year old Mexican teacher and revolutionary, who knows how to handle a sidearm.\" On the road to Sepulcro, Victor Melendez, one of the rebels she commands, tells John: \"She can fight as well as any man.\"",
        "En ajoutant son illustration au site officiel de Red Dead Redemption, Rockstar l'a présentée ainsi sur son Newswire, le 3 mai 2010 : \"Luisa Fortuna is a 19-year old Mexican teacher and revolutionary, who knows how to handle a sidearm.\" (Luisa Fortuna, 19 ans, est une institutrice et révolutionnaire mexicaine qui sait se servir d'une arme de poing). Sur la route de Sepulcro, Victor Melendez, l'un des rebelles placés sous ses ordres, glisse à John : \"She can fight as well as any man.\" (elle se bat aussi bien que n'importe quel homme).")},
    {"p": two(
        "In the transcripts, she speaks Spanish with the rebels and her family and English with John and Ricketts, whom she calls Mr. Marston and Mr. Ricketts. She first calls him John during \"Father Abraham\" and greets him by that name in \"Captain De Santa's Downfall\". She speaks of Reyes as Abraham or Abraham Reyes, and of the revolution as a duty owed to the people and to her dead father. She frames it through Mexican history: the wars against Spain, France and the United States, and the province renamed Nuevo Paraíso (New Paradise) after the Spanish left. According to the mission page of \"The Mexican Wagon Train\", she can be seen walking into the Chuparosa church after the opening scene and praying at the altar.",
        "Dans les transcriptions, elle parle espagnol avec les rebelles et sa famille, anglais avec John et Ricketts, qu'elle appelle Mr. Marston et Mr. Ricketts. Elle l'appelle John pour la première fois pendant \"Father Abraham\", et l'accueille par son prénom dans \"Captain De Santa's Downfall\". Elle dit Abraham ou Abraham Reyes quand elle parle de Reyes, et présente la révolution comme un devoir envers le peuple et envers son père mort. Elle la replace dans l'histoire du Mexique : les guerres contre l'Espagne, la France et les États-Unis, et la province rebaptisée Nuevo Paraíso (Nouveau Paradis) après le départ des Espagnols. D'après la page de la mission \"The Mexican Wagon Train\", on peut la voir entrer dans l'église de Chuparosa après la scène d'ouverture et prier devant l'autel.")},
    {"h4": two("In her own words", "Dans ses propres mots")},
    {"p": two(
        "To John, as her family leaves Campo Mirada in \"My Sister's Keeper\": \"Don't worry about me, Mr. Marston. I am living in history. I am not afraid to die.\" On the wagon ride to the Frontera Bridge in \"Father Abraham\", when John asks what comes after the fighting: \"Revolutions are always won with blood.\" A few lines later, when he says that nobody is ever free: \"Be honest with yourself and you will be free.\" As the army convoy reaches the charges: \"Every time Allende hits us, we hit him back harder.\"",
        "À John, pendant que sa famille quitte Campo Mirada, dans \"My Sister's Keeper\" : \"Don't worry about me, Mr. Marston. I am living in history. I am not afraid to die.\" (ne vous inquiétez pas pour moi, Mr. Marston ; je vis l'histoire en marche, je n'ai pas peur de mourir). Dans le chariot qui les mène au pont de Frontera, dans \"Father Abraham\", quand John lui demande ce qui vient après les combats : \"Revolutions are always won with blood.\" (les révolutions se gagnent toujours dans le sang). Un peu plus loin, quand il affirme qu'on n'est jamais libre : \"Be honest with yourself and you will be free.\" (soyez honnête avec vous-même et vous serez libre). Au moment où le convoi de l'armée arrive sur les charges : \"Every time Allende hits us, we hit him back harder.\" (chaque fois qu'Allende nous frappe, nous frappons plus fort).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Fortuna is the Spanish word for fortune or luck. Reyes calls her Laura: he asks John how he knows \"my young lover, Laura\" in \"Must a Savior Die?\", then sings \"Laura, dame la fuerza para luchar\" (Laura, give me the strength to fight) as they ride off together. After her death, in \"An Appointed Time\", he promises her a \"Laura's Day\" and, corrected by John, says he knew a Laura as well. When he recognizes her at the river, he calls her \"Mi amiga\" (my friend). The French-language Red Dead Wiki lists Laura as her nickname; the English-language wiki lists Laura and Peasent (sic), both attributed to Reyes.",
        "Fortuna signifie fortune ou chance en espagnol. Reyes l'appelle Laura : dans \"Must a Savior Die?\", il demande à John comment il connaît \"my young lover, Laura\" (ma jeune maîtresse, Laura), puis il chante \"Laura, dame la fuerza para luchar\" (Laura, donne-moi la force de me battre) en s'éloignant avec elle. Après sa mort, dans \"An Appointed Time\", il lui promet un \"Laura's Day\" (jour de Laura) et, repris par John, explique qu'il a aussi connu une Laura. Quand il la reconnaît au bord de la rivière, il l'appelle \"Mi amiga\" (mon amie). Le Red Dead Wiki francophone donne Laura comme surnom ; le wiki anglophone cite Laura et Peasent (sic, paysanne), tous deux attribués à Reyes.")},
    {"p": two(
        "She calls herself \"little more than a peasant girl\" when she explains why Reyes's family does not approve of them. Reyes, speaking of her to John at Agave Viejo, lumps her with \"These peasant girls\".",
        "Elle se décrit comme \"little more than a peasant girl\" (guère plus qu'une petite paysanne) quand elle explique pourquoi la famille de Reyes n'approuve pas leur union. Reyes, qui parle d'elle à John à Agave Viejo, la range parmi \"These peasant girls\" (ces petites paysannes).")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "She is a young woman with dark hair tied back. She wears a loose white blouse trimmed with blue at the neckline and sleeves. According to the Red Dead Wiki, she wears a gold cross on a beaded necklace throughout the game.",
        "C'est une jeune femme aux cheveux sombres noués en arrière. Elle porte une ample blouse blanche bordée de bleu à l'encolure et aux manches. Selon le Red Dead Wiki, elle garde pendant tout le jeu une croix en or au bout d'un collier de perles.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Section title in the module: "Weapons and gameplay" / "Armes et mécaniques de jeu" (no sub-heading).
BLOCKS_SKILLS = [
    {"p": two(
        "The Red Dead Wiki lists a Cattleman Revolver and a Hunting Knife as her weapons. She has a knife in hand when she runs at the soldiers in Escalera (see Biography). According to the Red Dead Wiki, she is one of three major characters who never ride a horse, with Agustin Allende and Nigel West Dickens; at the end of \"Landon Ricketts Rides Again\", she leaves with Carlos, who, according to his wiki page, takes her home on horseback. She drives the wagon in \"Must a Savior Die?\", with John riding shotgun; according to the mission page, she can crash it if the player watches the journey instead of skipping it. In \"Father Abraham\", John chooses between riding in her wagon and following on his own horse.",
        "Le Red Dead Wiki lui attribue un Cattleman Revolver et un couteau de chasse. Elle a un couteau à la main quand elle se jette sur les soldats à Escalera (voir la biographie). Selon le Red Dead Wiki, elle fait partie des trois personnages majeurs qui ne montent jamais à cheval, avec Agustin Allende et Nigel West Dickens ; à la fin de \"Landon Ricketts Rides Again\", elle part avec Carlos qui, d'après sa page du wiki, la ramène chez elle à cheval. Elle conduit le chariot dans \"Must a Savior Die?\", John étant assis à côté d'elle, fusil en main ; d'après la page de la mission, elle peut le renverser si le joueur suit le trajet au lieu de le passer. Dans \"Father Abraham\", John choisit entre monter dans son chariot et la suivre sur son propre cheval.")},
    {"p": two(
        "In \"Father Abraham\", she says that her rebels have no experience with explosives: John marks the spots for the dynamite on the road and mans the detonator, while she watches for the convoy from the ridge and orders her men to their positions in Spanish. In \"Captain De Santa's Downfall\", she sends her men with John and stays at the camp. The missions she takes part in fail if John kills her (\"Landon Ricketts Rides Again\"), assaults or kills her (\"Must a Savior Die?\", \"Father Abraham\", \"Captain De Santa's Downfall\", where hurting any rebel also counts) or abandons her (\"Must a Savior Die?\"). Killing the horses that pull her wagon also fails \"Must a Savior Die?\" and \"Father Abraham\". According to the mission page of \"An Appointed Time\", her body cannot be looted. The missions she gives are listed in the Missions table.",
        "Dans \"Father Abraham\", elle explique que ses rebelles ne savent pas manier les explosifs : John indique où placer la dynamite sur la route et tient le détonateur, pendant qu'elle guette le convoi depuis la crête et envoie ses hommes à leurs postes en espagnol. Dans \"Captain De Santa's Downfall\", elle confie ses hommes à John et reste au camp. Les missions auxquelles elle participe échouent si John la tue (\"Landon Ricketts Rides Again\"), l'agresse ou la tue (\"Must a Savior Die?\", \"Father Abraham\", \"Captain De Santa's Downfall\", où s'en prendre à un rebelle compte aussi) ou l'abandonne (\"Must a Savior Die?\"). Tuer les chevaux de son attelage fait également échouer \"Must a Savior Die?\" et \"Father Abraham\". D'après la page de la mission \"An Appointed Time\", on ne peut pas fouiller son corps. Les missions qu'elle confie figurent dans le tableau des missions.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "abraham-reyes.jpeg", "slug": "abraham-reyes", "name": "Abraham Reyes", "text": [
        two("The rebel leader she loves and serves. She describes him to John as a true revolutionary who puts others first and fights out of love rather than hate, and says that with him anything is possible. She tells John they are already married in their hearts, but that his family cannot accept a peasant girl (see Quotes). He was captured on his way to meet her, and she sends John to free him at El Presidio (see Biography). In \"Father Abraham\", she passes on his orders and says the rebels will fight harder to win power for him.",
            "Le chef rebelle qu'elle aime et qu'elle sert. Elle le dépeint à John comme un vrai révolutionnaire, qui fait passer les autres avant lui et se bat par amour plutôt que par haine, et assure qu'avec lui tout est possible. Elle confie à John qu'ils sont déjà mariés dans leur cœur, mais que sa famille ne peut accepter une paysanne (voir Citations). Il a été capturé alors qu'il venait la retrouver, et elle envoie John le libérer à El Presidio (voir la biographie). Dans \"Father Abraham\", elle transmet ses ordres et promet que les rebelles se battront plus fort encore pour le porter au pouvoir."),
        two("Reyes confuses her name (see Names). At Agave Viejo, in \"The Gates of El Presidio\", he tells John that she was incredible, recommends her to him and laughs at the idea of marrying a peasant (see Quotes). She dies in Escalera trying to save him, and afterwards he cannot remember who she was (see Biography).",
            "Reyes se trompe sur son prénom (voir Noms). À Agave Viejo, dans \"The Gates of El Presidio\", il raconte à John qu'elle était incroyable, la lui recommande et se moque de l'idée d'épouser une paysanne (voir Citations). Elle meurt à Escalera en tentant de le sauver, et il ne se souvient plus ensuite de qui elle était (voir la biographie)."),
    ]},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [
        two("John and Ricketts free her from the caves near El Matadero (see Biography); she thanks them as friends of the people of this land. In \"My Sister's Keeper\", John calls her naive and she answers that she would rather die than be a cynic like him, then says she knows he is not really like that (see Quotes). She kisses his cheek when he agrees to help free Reyes.",
            "John et Ricketts la tirent des grottes près d'El Matadero (voir la biographie) ; elle les remercie comme des amis du peuple de cette terre. Dans \"My Sister's Keeper\", John la traite de naïve, elle répond qu'elle préfère mourir plutôt que d'être aussi cynique que lui, puis ajoute qu'elle sait qu'il ne pense pas vraiment ainsi (voir Citations). Elle l'embrasse sur la joue quand il accepte de l'aider à libérer Reyes."),
        two("In \"Father Abraham\", she tells him she cannot forgive him for having helped Allende against the rebels, and that refusing to choose a side is a choice; John replies that Allende betrayed him. On the same ride, she asks about his family: he has a son at home and mentions a daughter who died, and he tells her the boy's name, Jack. After her death, John reminds Reyes of people like Luisa who gave their lives (see Quotes).",
            "Dans \"Father Abraham\", elle lui dit qu'elle ne lui pardonne pas d'avoir aidé Allende contre les rebelles, et que refuser de choisir son camp revient à choisir ; John répond qu'Allende l'a trahi. Pendant le même trajet, elle l'interroge sur sa famille : il a un fils à la maison et évoque une fille qui est morte, puis lui donne le prénom du garçon, Jack. Après sa mort, John rappelle à Reyes ceux qui, comme Luisa, ont donné leur vie (voir Citations)."),
    ]},
    {"img": "landon-ricketts.jpeg", "slug": "landon-ricketts", "name": "Landon Ricketts", "text": [
        two("Ricketts learns of her capture from her brother Emilio and rides with John to free her (see Biography). On the way, he describes her as a good woman and a teacher, and swears to make her captors pay if they touch her.",
            "Ricketts apprend sa capture par son frère Emilio et part la libérer avec John (voir la biographie). En chemin, il la décrit comme une femme de bien et une institutrice, et jure de faire payer ses geôliers s'ils osent la toucher."),
        two("In \"The Mexican Wagon Train\", she runs into the Chuparosa hotel looking for him, to report the prisoners Allende is sending to their deaths. When he jokes that for once he agrees with the colonel, she protests and he says he was joking (see Quotes). At the border, he tells John to talk to her, as she is well connected in Mexico and will help him.",
            "Dans \"The Mexican Wagon Train\", elle fait irruption à l'hôtel de Chuparosa pour le prévenir qu'Allende envoie des prisonniers à la mort. Quand il plaisante en disant que, pour une fois, il est d'accord avec le colonel, elle proteste, et il assure qu'il plaisantait (voir Citations). À la frontière, il conseille à John d'aller la voir, car elle a des relations au Mexique et l'aidera."),
    ]},
    {"img": "agustin-allende.jpeg", "slug": "agustin-allende", "name": "Agustin Allende", "text": two(
        "The governor whose army holds her in the caves near El Matadero (see Biography). She blames him for the executions of untried prisoners and for her father's death, calls him pure evil and says she will one day cut his heart out (see Quotes). He is killed on the road out of Escalera in the mission in which she dies (see Biography).",
        "Le gouverneur dont l'armée la détient dans les grottes près d'El Matadero (voir la biographie). Elle le tient pour responsable de l'exécution de prisonniers jamais jugés et de la mort de son père, le qualifie de mal incarné et jure de lui arracher le cœur un jour (voir Citations). Il est tué sur la route à la sortie d'Escalera, dans la mission où elle meurt (voir la biographie).")},
    {"img": "vincente-de-santa.jpeg", "slug": "vincente-de-santa", "name": "Vincente de Santa", "text": two(
        "She learns that the captain has been sent to oversee a massacre at Sepulcro, calls him an animal and vermin, and sends John there with her men to kill him and Allende's other followers (see Biography). She stays behind at the rebel camp.",
        "Elle apprend que le capitaine a été envoyé superviser un massacre à Sepulcro, le traite d'animal et de vermine, et y envoie John avec ses hommes pour l'abattre, lui et les autres partisans d'Allende (voir la biographie). Elle reste au camp des rebelles.")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Just after her rescue, Ricketts asks her whether Javier was one of the men holding her. She does not think so, but says she heard the name in prison, from bad people.",
        "Juste après sa libération, Ricketts lui demande si Javier faisait partie de ses geôliers. Elle ne le pense pas, mais dit avoir entendu ce nom en prison, dans la bouche de mauvaises gens.")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "She never meets him. In \"Father Abraham\", she asks John whether his son is looking after his wife and what the boy is called; John answers Jack, and says he is not much younger than her.",
        "Elle ne le rencontre jamais. Dans \"Father Abraham\", elle demande à John si son fils veille sur sa femme et comment s'appelle le garçon ; John répond Jack, et précise qu'il n'est pas beaucoup plus jeune qu'elle.")},
    {"img": None, "slug": None, "name": "Emilio Fortuna", "text": two(
        "Her brother. In \"Landon Ricketts Rides Again\", he is talking with Ricketts at the Chuparosa hotel and answers only in Spanish. The Red Dead Wiki describes him as her older brother and a stagecoach driver; Miranda says he works as a driver, and she and John take his stagecoach. Luisa first says her parents and her brother are leaving for the hills, then, in \"Father Abraham\", that Emilio will stay and fight like her.",
        "Son frère. Dans \"Landon Ricketts Rides Again\", il discute avec Ricketts à l'hôtel de Chuparosa et ne répond qu'en espagnol. Le Red Dead Wiki en fait son frère aîné, conducteur de diligence ; Miranda explique qu'il travaille comme cocher, et c'est sa diligence qu'elle prend avec John. Luisa annonce d'abord que ses parents et son frère partent dans les collines, puis, dans \"Father Abraham\", qu'Emilio restera se battre comme elle.")},
    {"img": None, "slug": None, "name": "Miranda Fortuna", "text": two(
        "Her sister, younger according to the Red Dead Wiki. Luisa sends her to work for a kind man in the Yucatán, saying she is too young for revolution, and asks John to take her to the docks (see Biography). In \"Father Abraham\", Luisa thanks John for helping Miranda escape.",
        "Sa sœur, la cadette selon le Red Dead Wiki. Luisa l'envoie travailler pour un homme bienveillant au Yucatán, en expliquant qu'elle est trop jeune pour la révolution, et demande à John de l'escorter jusqu'au port (voir la biographie). Dans \"Father Abraham\", Luisa remercie John d'avoir aidé Miranda à s'enfuir.")},
    {"img": None, "slug": None, "name": "Her father", "text": two(
        "His name is not given in the game; the Red Dead Wiki calls him Mr. Fortuna. At Campo Mirada, he thanks John in English for saving his daughter and apologizes for his English. His death at the hands of the army is told under Biography. Luisa tells John she wishes she had sent him away with her mother and sister.",
        "Son nom n'est pas donné dans le jeu ; le Red Dead Wiki l'appelle Mr. Fortuna. À Campo Mirada, il remercie John en anglais d'avoir sauvé sa fille, en s'excusant de mal parler la langue. Sa mort aux mains de l'armée est racontée dans la biographie. Luisa confie à John qu'elle regrette de ne pas l'avoir fait partir avec sa mère et sa sœur.")},
    {"img": None, "slug": None, "name": "Her mother", "text": two(
        "Her name is not given in the game; the Red Dead Wiki calls her Mrs. Fortuna. She weeps on the porch at Campo Mirada as Miranda prepares to leave. In \"My Sister's Keeper\", Luisa says her parents are heading to the hills; in \"Father Abraham\", she says her mother is in the United States and thanks John for helping her mother and Miranda escape. Luisa adds that neither knows of her father's death.",
        "Son nom n'est pas donné dans le jeu ; le Red Dead Wiki l'appelle Mrs. Fortuna. Elle pleure sur le perron de Campo Mirada pendant que Miranda s'apprête à partir. Dans \"My Sister's Keeper\", Luisa explique que ses parents partent dans les collines ; dans \"Father Abraham\", elle dit que sa mère est aux États-Unis et remercie John d'avoir aidé sa mère et Miranda à fuir. Elle ajoute qu'aucune des deux ne sait que son père est mort.")},
    {"img": None, "slug": None, "name": "Carlos", "text": two(
        "The butcher of El Matadero who helps Ricketts and John reach her cell by distracting the guards (see Biography). He thanks God when he sees her alive, and she leaves with him at the end of the mission.",
        "Le boucher d'El Matadero qui aide Ricketts et John à atteindre sa cellule en détournant l'attention des gardes (voir la biographie). Il remercie Dieu en la voyant vivante, et elle repart avec lui à la fin de la mission.")},
    {"img": None, "slug": None, "name": "Victor Melendez", "text": two(
        "One of her rebels, who guides John to Sepulcro on her orders. On the way, he praises her fighting (see Personality) and explains that women and even children must become soldiers if the rebels are to win.",
        "L'un de ses rebelles, qui conduit John à Sepulcro sur ses ordres. En chemin, il vante ses qualités de combattante (voir Personnalité) et explique que les femmes, et même les enfants, doivent devenir soldats si les rebelles veulent gagner.")},
    {"img": None, "slug": None, "name": "Raul Zubieta", "text": two(
        "The army major who is about to execute Reyes in Escalera when she runs at his men with a knife. She is shot dead, and John kills Zubieta in a duel (see Biography).",
        "Le major de l'armée qui s'apprête à exécuter Reyes à Escalera quand elle se jette sur ses hommes, un couteau à la main. Elle est abattue, et John tue Zubieta en duel (voir la biographie).")},
]
