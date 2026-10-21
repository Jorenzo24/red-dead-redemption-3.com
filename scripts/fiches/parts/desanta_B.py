"""Vincente de Santa, part B: Personality (official description, observable traits, In his own words, Names, Appearance),
Weapons, horse and gameplay (the fiche-specific skills section), Relationships (21 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN sections Personality (kept only where a transcript supports a trait), the GOTY quote box,
the infobox (aka, weapons, mount, family, affiliations), the trivia on the shoulder patches (colour only), the lazy eye,
the civilian kill, the Quique Montemayor and Reyes remarks (the lines themselves, without the wiki's reading), Victor's
and Reyes's branch lines; the FR wiki infobox (Volcanic Pistol, allies); the six RDR1 transcripts of his missions and the
lines others speak about him in "Must a Savior Die?" and "The Gates of El Presidio". Narrative events are told in part A;
the entries below point to them.

SOURCE REGISTER (read 21 Oct 2026; wiki cache scripts/v3/work/_m/):
- Official description: Red Dead Redemption: Game of the Year Edition guide (BradyGames), quoted in the quote box of the
  Red Dead Wiki EN page "Vincente de Santa" ("A 33-year-old military man. He is Allende's man on the ground..."). The guide
  itself was not read: quoted through the wiki, attributed. Rockstar's 6 Sep 2018 descriptions cover the RDR2 gang only.
- Transcripts, his own lines (every quoted line checked): "Civilization, at Any Price/dialogues", "The Demon Drink/
  dialogues", "Empty Promises/dialogues", "Mexican Caesar/dialogues", "Cowards Die Many Times/dialogues", "Captain De
  Santa's Downfall/dialogues".
- Transcripts, what others say of him: "The Demon Drink/dialogues" and "Mexican Caesar/dialogues" (Allende, Espinoza),
  "Empty Promises/dialogues" (Espinoza), "Captain De Santa's Downfall/dialogues" (Luisa, Victor), "Must a Savior Die?/
  dialogues" and "The Gates of El Presidio/dialogues" (Reyes, John, both branches).
- Mission pages: "The Demon Drink", "Empty Promises", "Cowards Die Many Times" (failure conditions, race objective,
  shooting contest), "Captain De Santa's Downfall" (objectives, chase behaviour, infinite weapons, fist-fight note).
- Other wiki pages: "Quique Montemayor" (waiter, in De Santa's employ), "Espinoza", "Victor Melendez", "Herbert Moon"
  (quote box, as used on the Allende fiche), FR wiki "Vincente De Santa" (infobox), ES wiki title "Vicente De Santa"
  (interwiki of the EN page).
- Newspaper: Blackwater Ledger No. 58 (reyes/fc/ireddead_newspapers.txt): "Captain Vicente De Santa of the Mexican Army
  has been reported deceased, age 34 years." Used here for the spelling only; the notice itself is told in part A.
- Javier Aldape, "The Mustang Diaries" (Revista Panamericana de Comunicación, 2022; allende/fc/): spelling "Vicente".
- Visual check: live portrait.jpeg and the gallery contact sheet (scripts/v3/work/desanta/gal/contact.jpg) for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only (parts A and C must not repeat them): the GOTY description; "Sometimes in the service of what is right,
  you got to do terrible things. It breaks my heart.", "Revolution is always selfish. It is nothing but greed and ego.",
  "The past is all that's real, my friend. It cannot be erased.", "I am married to my country and these rebel traitors,
  they are trying to take it from me." (In his own words); "office boy", "that pathetic little errand boy" (Names);
  "Billy the cowboy and his Mexican friend" (Bill entry). After the fact-check (21 Oct 2026), Reyes's "spending too
  much time with Captain de Santa" and "young boys" lines, John's "dumb and loyal to his awful master", Herbert Moon's
  line, Espinoza's escort lines and Victor's branch lines are quoted in part C Quotes only; the entries below paraphrase.
  Added from the transcripts: Espinoza's "brazo derecho" and "De Santa is that woman" (Mexican Caesar), Allende's
  "you are transparent... impaled" (The Demon Drink, English translation of the transcript).
- Paraphrased here, left to part C Quotes: "My country is in pain...", "I am the government...", "This isn't America...",
  "The peasants are stupid...", "If my men are dead...", "Go get drunk!...", "Mexico loves you, Mr. Marston.", the Reyes
  insult ("traitor, a liar, a coward and a sinner..."), "Colonel Allende controls any situation...", Victor's "hundreds of
  innocent deaths", Luisa's "wretched animal", the Sepulcro lines, Espinoza's lines other than the two names above.
- Gameplay HERE only: weapons, horse, race to Tesoro Azul, shooting contest mechanics (the reward figure stays in the C
  Missions table), failure conditions, the Sepulcro chase and hogtie mechanics, infinite weapons, civilian kill.
- Told once elsewhere, pointer here: every mission event (A); his parents and his English lessons (A Origins); the death
  notice (A); Undead Nightmare and the gravestone (A); multiplayer model (C Other media); actor (D); the queer reading of
  the Quique scenes (D Reception, LGBTQ Video Game Archive, 24 Jun 2016).

WIKI-ONLY (kept, attributed): the GOTY description; Cattleman Revolver, Repeater Carbine and Painted Quarter Horse (EN
infobox); Volcanic Pistol (FR infobox); the lazy eye; the civilian kill; Quique as De Santa's employee and as the waiter of
"Civilization, at Any Price"; the chase details of the "Captain De Santa's Downfall" mission page; Herbert Moon's line.

Excluded: the wiki's "cruel, abusive, and sadistic", "vicious sycophant", "seems to genuinely admire" (wiki judgments; the
GOTY wording and the transcripts are used instead); "implied" relationship with Quique, the gunsmith "as if I were his
brother" line, "possibly bisexual", "rapist", "pedophile", "homophobia on Reyes' behalf" (speculation; the lines are
reported verbatim without reading, the published reading is attributed in D); Victor's "De Santa likes to do a lot of
things to men on their knees" and John's "He'll do a lot of things when men are on their knees" (in no transcript: the
Downfall transcript has John's "I don't like to kill a man on his knees" instead); the burgundy patches as a sign of general
staff (wiki inference); "Office boy" as an infobox alias without speaker (kept as Espinoza's insult); Chico Renovales as
the rebel executed at Sepulcro (the wiki's own Chico page has him alive at Escalera later); Raul Zubieta as an ally (FR
infobox only, no scene); the Scarface / Tony Montana and Brian Jeremy comparisons (fan analysis); "Please, I am begging
you." and "You are the better man." (combat lines with no context; left to C if verified); "Sometimes we must be brutal to
be kind" and "I bleed red, white and green" (wiki lines found in no transcript; left to C to decide with attribution).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "The Red Dead Wiki quotes the Game of the Year Edition guide of Red Dead Redemption: \"A 33-year-old military man. He is Allende's man on the ground. Ambitious and unprincipled, Vincente knows that he is fighting a war that he must win because the rebels have put a price on his head. He will do anything and kill anyone. He also has been tasked with procuring young women for his boss.\"",
        "Le Red Dead Wiki cite le guide de l'édition Game of the Year de Red Dead Redemption : \"A 33-year-old military man. He is Allende's man on the ground. Ambitious and unprincipled, Vincente knows that he is fighting a war that he must win because the rebels have put a price on his head. He will do anything and kill anyone. He also has been tasked with procuring young women for his boss.\" (Un militaire de 33 ans, l'homme d'Allende sur le terrain. Ambitieux et sans scrupules, Vincente sait qu'il doit gagner cette guerre, car les rebelles ont mis sa tête à prix. Il est prêt à tout et à tuer n'importe qui. Il est aussi chargé de fournir des jeunes femmes à son patron.)")},
    {"p": two(
        "In the transcripts, he mixes Spanish into his English and calls John amigo, compadre or my friend. He defends Colonel Allende each time John criticizes him. He calls the rebels traitors, pigs and rats, and describes the peasants as people who can be herded. He blames the poor for their poverty.",
        "Dans les transcriptions, il mêle l'espagnol à son anglais et appelle John amigo, compadre ou mon ami. Il prend la défense du colonel Allende chaque fois que John le critique. Il traite les rebelles de traîtres, de porcs et de rats, et décrit les paysans comme un troupeau qu'on mène. À l'en croire, les pauvres sont responsables de leur propre misère.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "On Allende's rule, at their first meeting in \"Civilization, at Any Price\": \"Sometimes in the service of what is right, you got to do terrible things. It breaks my heart.\" On the rebellion, in the same mission: \"Revolution is always selfish. It is nothing but greed and ego.\" When John says his old friends belong to a past he cannot shake off: \"The past is all that's real, my friend. It cannot be erased.\" On the road to Chuparosa in \"Cowards Die Many Times\": \"I am married to my country and these rebel traitors, they are trying to take it from me.\"",
        "Sur la manière de gouverner d'Allende, lors de leur première rencontre dans \"Civilization, at Any Price\" : \"Sometimes in the service of what is right, you got to do terrible things. It breaks my heart.\" (parfois, pour servir ce qui est juste, il faut faire des choses terribles ; ça me brise le cœur). Sur la rébellion, dans la même mission : \"Revolution is always selfish. It is nothing but greed and ego.\" (la révolution est toujours égoïste ; ce n'est qu'avidité et vanité). Quand John explique que ses anciens amis appartiennent à un passé dont il ne parvient pas à se défaire : \"The past is all that's real, my friend. It cannot be erased.\" (le passé est la seule chose réelle, mon ami ; on ne peut pas l'effacer). Sur la route de Chuparosa, dans \"Cowards Die Many Times\" : \"I am married to my country and these rebel traitors, they are trying to take it from me.\" (je suis marié à mon pays, et ces traîtres de rebelles veulent me l'enlever).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "He introduces himself to John as Capitán Vincente de Santa. John, Reyes and the rebels call him De Santa or Captain De Santa. The Red Dead Wiki and Hector Luis Bustamante's filmography on Wikipedia spell his first name Vincente. The notice of his death in the Blackwater Ledger spells it Vicente, as do the Spanish-language Red Dead Wiki and Javier Aldape's 2022 study of the game (see Reception). Captain Espinoza calls him \"office boy\" in \"Empty Promises\" and \"that pathetic little errand boy\" in \"Mexican Caesar\". Allende insults him in Spanish in front of John: llorón (crybaby) and maricón in \"The Demon Drink\", mariconcito in \"Mexican Caesar\", the last two being homophobic slurs.",
        "Il se présente à John comme le capitán Vincente de Santa. John, Reyes et les rebelles l'appellent De Santa ou capitaine De Santa. Le Red Dead Wiki et la filmographie d'Hector Luis Bustamante sur Wikipédia écrivent son prénom Vincente. L'avis de décès publié par le Blackwater Ledger l'écrit Vicente, tout comme le Red Dead Wiki hispanophone et l'étude que Javier Aldape a consacrée au jeu en 2022 (voir Accueil). Le capitaine Espinoza le traite de \"office boy\" (garçon de bureau) dans \"Empty Promises\" et de \"that pathetic little errand boy\" (ce minable petit coursier) dans \"Mexican Caesar\". Allende l'insulte en espagnol devant John : llorón (pleurnichard) et maricón dans \"The Demon Drink\", mariconcito dans \"Mexican Caesar\", ces deux derniers mots étant des insultes homophobes.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is a clean-shaven man in his thirties, with dark hair cut in a fringe and falling to the back of the neck. He wears a dark army tunic with burgundy shoulder patches, a white cravat and two brown leather straps over the shoulders. According to the Red Dead Wiki, he has a lazy eye, less visible than Eli's.",
        "C'est un homme d'une trentaine d'années, rasé de près, aux cheveux sombres coupés en frange qui tombent sur la nuque. Il porte une vareuse militaire sombre à pattes d'épaule bordeaux, une lavallière blanche et deux sangles de cuir brun sur les épaules. Selon le Red Dead Wiki, il a un œil paresseux, moins visible que celui d'Eli.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Section title in the module: "Weapons, horse and gameplay" / "Armes, monture et mécaniques de jeu" (no sub-heading).
BLOCKS_SKILLS = [
    {"p": two(
        "The Red Dead Wiki lists a Cattleman Revolver and a Repeater Carbine as his weapons, and a Painted Quarter Horse as his mount; the French-language wiki gives him a Volcanic Pistol. In \"The Demon Drink\", he challenges John to a race to Tesoro Azul, which is one of the mission's objectives. In \"Cowards Die Many Times\", he runs a shooting contest on the wagon ride to Chuparosa: each man gets five shots at the local wildlife, and he promises 25 dollars to whoever kills the most. According to the mission page, the contest starts when John shoots an animal and can be won three times (the reward is in the Missions table).",
        "Le Red Dead Wiki lui attribue un Cattleman Revolver et une Repeater Carbine, et un Painted Quarter Horse pour monture ; le wiki francophone lui donne un pistolet Volcanic. Dans \"The Demon Drink\", il défie John à la course jusqu'à Tesoro Azul, l'un des objectifs de la mission. Dans \"Cowards Die Many Times\", il organise un concours de tir pendant le trajet en chariot vers Chuparosa : chacun a droit à cinq balles sur les animaux des environs, et il promet 25 dollars à celui qui en abat le plus. D'après la page de la mission, le concours commence quand John tire sur un animal et peut être remporté trois fois (la récompense figure dans le tableau des missions).")},
    {"p": two(
        "In \"Civilization, at Any Price\", \"The Demon Drink\", \"Empty Promises\" and the first part of \"Cowards Die Many Times\" (before John enters the church), the mission fails if John assaults, kills or abandons him. \"Captain De Santa's Downfall\" fails if he is killed before he is captured and made to talk. At Sepulcro, John must kill his soldiers without hitting him and take him alive (see Biography). According to the mission page, he runs slowly and can steal John's horse; a rider who cuts him off can herd him back like cattle. He may shoot at John; when he is close to the rebels, he fights them and ignores John. He draws a new revolver or rifle each time he is disarmed. If John starts a fistfight with him after the interrogation, the rebels shoot him, and the following dialogue plays as if John had killed him. The Red Dead Wiki adds that killing him counts as a civilian kill.",
        "Dans \"Civilization, at Any Price\", \"The Demon Drink\", \"Empty Promises\" et la première partie de \"Cowards Die Many Times\" (avant que John n'entre dans l'église), la mission échoue si John l'agresse, le tue ou l'abandonne. \"Captain De Santa's Downfall\" échoue s'il meurt avant d'avoir été capturé et d'avoir parlé. À Sepulcro, John doit éliminer ses soldats sans le toucher et le prendre vivant (voir la biographie). D'après la page de la mission, il court lentement et peut voler le cheval de John ; un cavalier qui lui coupe la route peut le rabattre comme du bétail. Il lui arrive de tirer sur John ; s'il se trouve près des rebelles, il les affronte et ne s'occupe plus de John. Il sort un nouveau revolver ou un nouveau fusil chaque fois qu'on le désarme. Si John engage un combat à mains nues après l'interrogatoire, les rebelles l'abattent, et la suite du dialogue se déroule comme si John l'avait tué. Le Red Dead Wiki précise que sa mort compte comme celle d'un civil.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "agustin-allende.jpeg", "slug": "agustin-allende", "name": "Agustin Allende", "text": [
        two("His colonel, the governor of Nuevo Paraíso. De Santa presents him to John as a good and strong man who carries the weight of a million problems. Allende insults him in Spanish in front of John (see Names). At the start of \"The Demon Drink\", he also tells him that he talks of loyalty but is transparent, and that he will be applauding when Allende's head is impaled. In the same scene, he orders him not to stand behind him and tells him he is not his shadow.",
            "Son colonel, gouverneur du Nuevo Paraíso. De Santa le présente à John comme un homme bon et fort, qui porte sur ses épaules le poids d'un million de problèmes. Allende l'insulte en espagnol devant John (voir Noms). Au début de \"The Demon Drink\", il lui reproche aussi de parler de loyauté alors qu'on lit en lui comme dans un livre, et lui lance qu'il applaudira le jour où sa tête, à lui Allende, sera plantée sur une pique. Dans la même scène, il lui interdit de se placer derrière lui : il n'est pas son ombre."),
        two("De Santa brings young women to the mansion for him and defends him when John raises the subject (see Biography). At Sepulcro, he condemns a rebel to death in the name of Colonel Allende's government (see Biography). Both men are reported dead in the same issue of the Blackwater Ledger (see Biography).",
            "De Santa lui amène des jeunes femmes à sa demeure, et prend sa défense quand John aborde le sujet (voir la biographie). À Sepulcro, il condamne un rebelle à mort au nom du gouvernement du colonel Allende (voir la biographie). Les deux hommes sont annoncés morts dans le même numéro du Blackwater Ledger (voir la biographie)."),
    ]},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [
        two("De Santa is John's first contact with the army in Nuevo Paraíso and sends him on every mission of his strand, promising that the colonel will find Bill and Javier in return (see Biography). On their first ride, in \"Civilization, at Any Price\", De Santa asks how much the bounty on the two men is worth; John answers that he is not being paid and is being made to do it. On the road to Chuparosa, in \"Cowards Die Many Times\", De Santa asks why he hunts them; John first says it beats getting a real job, and only later says that his wife and child have been taken from him. In front of Allende, De Santa calls John a friend of Mexico. He betrays him in Chuparosa (see Biography).",
            "De Santa est le premier contact de John avec l'armée au Nuevo Paraíso ; il lui confie toutes les missions de sa série, en lui promettant que le colonel retrouvera Bill et Javier en échange (voir la biographie). Lors de leur premier trajet, dans \"Civilization, at Any Price\", De Santa lui demande combien rapporte la tête des deux hommes ; John répond qu'il n'est pas payé et qu'on le force à le faire. Sur la route de Chuparosa, dans \"Cowards Die Many Times\", De Santa lui demande pourquoi il les traque ; John répond d'abord que c'est toujours mieux qu'un vrai travail, et ce n'est que plus tard qu'il explique qu'on lui a pris sa femme et son enfant. Devant Allende, De Santa présente John comme un ami du Mexique. Il le trahit à Chuparosa (voir la biographie)."),
        two("At Sepulcro, John beats him until he names a hiding place for Javier, then kills him or leaves him to the rebels (see Biography). If the rebels killed him, John later tells Reyes that De Santa was only a dull, faithful servant who followed orders (see Quotes).",
            "À Sepulcro, John le roue de coups jusqu'à ce qu'il lâche une cachette de Javier, puis l'abat ou le laisse aux rebelles (voir la biographie). Si ce sont les rebelles qui l'ont tué, John dit ensuite à Reyes que De Santa n'était qu'un exécutant borné et fidèle (voir Citations)."),
    ]},
    {"img": "abraham-reyes.jpeg", "slug": "abraham-reyes", "name": "Abraham Reyes", "text": [
        two("The rebel leader De Santa is fighting. On their first ride to Chuparosa, De Santa insults him at length (see Quotes), calls him a man born in a golden cradle who pretends to fight for the poor, and says that Reyes only makes speeches from a balcony. In \"Cowards Die Many Times\", he calls him a coward who writes poems and songs about battles he never fought. Reyes's rebels save John from De Santa's firing squad in Chuparosa (see Biography).",
            "Le chef rebelle que combat De Santa. Lors de leur premier trajet vers Chuparosa, De Santa l'injurie longuement (voir Citations), le décrit comme un homme né dans un berceau doré qui fait semblant de se battre pour les pauvres, et affirme que Reyes se contente de discourir depuis un balcon. Dans \"Cowards Die Many Times\", il le traite de lâche qui écrit des poèmes et des chansons sur des batailles qu'il n'a jamais livrées. Les rebelles de Reyes arrachent John au peloton de De Santa à Chuparosa (voir la biographie)."),
        two("When John tells Reyes, in \"Must a Savior Die?\", that he is only after two men, Reyes jokes that John has been spending too much time with De Santa (see Quotes), and John replies that he did not mean it that way. Reyes welcomes De Santa's death at the start of \"The Gates of El Presidio\" (see Biography).",
            "Quand John explique à Reyes, dans \"Must a Savior Die?\", qu'il ne cherche que deux hommes, Reyes lui lance, pour plaisanter, qu'il a passé trop de temps avec le capitaine De Santa (voir Citations). John rétorque qu'il ne l'entendait pas ainsi. Au début de \"The Gates of El Presidio\", Reyes se félicite de la mort de De Santa (voir la biographie)."),
    ]},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "One of the two outlaws John is hunting. De Santa asks about \"Billy the cowboy and his Mexican friend\" on their first ride. In \"Cowards Die Many Times\", he leads John to Chuparosa on the pretext that Bill and Javier have been captured there (see Biography).",
        "L'un des deux hors-la-loi que traque John. Lors de leur première chevauchée, De Santa s'enquiert de \"Billy the cowboy and his Mexican friend\" (Billy le cow-boy et son ami mexicain). Dans \"Cowards Die Many Times\", il conduit John à Chuparosa en prétendant que Bill et Javier y ont été capturés (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "In \"Mexican Caesar\", De Santa offers John, on the colonel's behalf, information on Javier's whereabouts (see Biography). At Sepulcro, beaten by John, he names Casa Madrugada as Javier's hiding place; soldiers are waiting there instead (see Biography).",
        "Dans \"Mexican Caesar\", De Santa propose à John, au nom du colonel, des renseignements sur la cachette de Javier (voir la biographie). À Sepulcro, roué de coups par John, il désigne la Casa Madrugada comme son repaire ; des soldats y attendent John à sa place (voir la biographie).")},
    {"img": "luisa-fortuna.jpeg", "slug": "luisa-fortuna", "name": "Luisa Fortuna", "text": two(
        "Luisa learns that De Santa has been sent to oversee a massacre at Sepulcro and asks John to ride there with her men and kill him and Allende's other followers (see Biography). She calls him an animal and vermin, and stays behind at the rebel camp.",
        "Luisa apprend que De Santa a été envoyé superviser un massacre à Sepulcro et demande à John de s'y rendre avec ses hommes pour l'abattre, lui et les autres partisans d'Allende (voir la biographie). Elle le traite d'animal et de vermine, et reste au camp des rebelles.")},
    {"img": None, "slug": None, "name": "Espinoza", "text": [
        two("A fellow army captain and his rival. When John asks whether they share the same rank, De Santa says Espinoza leads nothing and calls him an angry dog the army lets out from time to time; at Torquemada he tells John to ignore that stupid ape. Espinoza, for his part, mocks him with the names given under Names. In \"Mexican Caesar\", he tells John that De Santa licks the colonel's boots, plays with his waiter friend and flirts with barmen, and that he never saw him fight at Torquemada. In the same mission, he claims to be Allende's right arm himself, and says the colonel needs a maid, a woman he cannot sleep with, and that De Santa is that woman.",
            "Capitaine de l'armée comme lui, et son rival. Quand John demande s'ils ont le même grade, De Santa répond qu'Espinoza ne commande rien et le compare à un chien enragé qu'on lâche de temps en temps ; à Torquemada, il conseille à John d'ignorer ce singe stupide. Espinoza, lui, l'affuble des surnoms cités dans la rubrique Noms. Dans \"Mexican Caesar\", il raconte à John que De Santa lèche les bottes du colonel, s'amuse avec son ami serveur et flirte avec les garçons de café, et qu'il ne l'a jamais vu se battre à Torquemada. Dans la même mission, il se présente lui-même comme le bras droit d'Allende, et affirme que le colonel a besoin d'une bonne, d'une femme avec qui il ne peut pas coucher : De Santa est cette femme."),
        two("During the same escort, he tells John that the squad includes the two men De Santa hates most, and later asks him whether he should kill De Santa himself (see Quotes). In \"Cowards Die Many Times\", De Santa blames Espinoza for that escort. John kills Espinoza in Chuparosa (see Biography).",
            "Pendant cette escorte, il fait remarquer à John que l'escouade compte les deux hommes que De Santa déteste le plus, puis lui demande s'il doit se charger lui-même de tuer De Santa (voir Citations). Dans \"Cowards Die Many Times\", De Santa rejette sur Espinoza la responsabilité de cette escorte. John tue Espinoza à Chuparosa (voir la biographie)."),
    ]},
    {"img": None, "slug": None, "name": "Quique Montemayor", "text": two(
        "A waiter at Allende's mansion in Escalera; the Red Dead Wiki says he works for De Santa and identifies him as the waiter who brings De Santa his tequila in \"Civilization, at Any Price\". In \"Mexican Caesar\", he helps De Santa push two young women into the mansion and insults them in Spanish (see Biography). Espinoza's remarks about the waiter are under the Espinoza entry; a published reading of these scenes is under Reception.",
        "Serveur dans la demeure d'Allende à Escalera ; selon le Red Dead Wiki, il est au service de De Santa, et c'est lui qui apporte sa tequila à De Santa dans \"Civilization, at Any Price\". Dans \"Mexican Caesar\", il aide De Santa à pousser deux jeunes femmes dans la demeure et les insulte en espagnol (voir la biographie). Les remarques d'Espinoza sur le serveur figurent dans l'entrée consacrée à Espinoza ; une lecture publiée de ces scènes est présentée dans la rubrique Accueil.")},
    {"img": None, "slug": None, "name": "Victor Melendez", "text": two(
        "The rebel who leads John to Sepulcro on Luisa's orders. After the interrogation, he asks John who should kill De Santa. His reactions to each outcome are told under Biography and quoted under Quotes.",
        "Le rebelle qui conduit John à Sepulcro sur ordre de Luisa. Après l'interrogatoire, il demande à John qui doit abattre De Santa. Ses réactions, selon le choix du joueur, sont racontées dans la biographie et citées dans la rubrique Citations.")},
    {"img": None, "slug": None, "name": "His parents", "text": two(
        "Neither is named in the game. What he says of his upbringing and of his mother is told under Biography (Origins).",
        "Ni l'un ni l'autre n'est nommé dans le jeu. Ce qu'il raconte de son éducation et de sa mère figure dans la biographie (Origines).")},
    {"img": None, "slug": None, "name": "Herbert Moon", "text": two(
        "The Armadillo shopkeeper names him among the Mexican leaders he lumps together, in a line quoted on the Red Dead Wiki's Herbert Moon page (see Quotes).",
        "Le commerçant d'Armadillo le range parmi les dirigeants mexicains qu'il met dans le même sac, dans une réplique citée sur la page Herbert Moon du Red Dead Wiki (voir Citations).")},
]
