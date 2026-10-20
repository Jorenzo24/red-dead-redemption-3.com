"""Josiah Trelawny, part B: Personality (official descriptions, traits, In his own words, Names, Appearance),
Skills/weapons/horse, Relationships (20 Oct 2026, medium tier).

Sources (register):
- Rockstar character description of 6 Sep 2018 (English text as reprinted by The Hollywood Reporter / Heat
  Vision, 7 Sep 2018, saved in ../uncle/fc/thr_descriptions.txt, line 104; French text from
  rockstargames.com/reddeadredemption2/fr/features/vanderlindegang, as quoted by the French Red Dead Wiki page
  "Josiah Trelawny", josiah/fr.txt).
- A character page from an official guide (wiki file JosiahTrelawnyBio.jpg, captioned "Biography in RDR 2",
  uploaded 12 Nov 2018, downloaded via the API to josiah/fcB/bio.png and read; text copied verbatim in
  josiah/fcB/guide_bio.txt). Wikipedia's "List of Red Dead Redemption 2 characters" cites the same point
  (allowed to move in and out of the gang) to the official guide (Price 2018, p. 375); the edition is not named
  on the page, so the text says "an official guide".
- Transcripts: "Americans at Rest" ("Bill looking well as can be", "Josiah, take Javier", "Look who we found
  sniffing about", "It's you they want, Dutch" / "Always is"); "The First Shall Be Last" ("Much as I love dodging
  the law and sleeping in the dirt with you derelicts, I do have other business to attend to."; "But without me
  you'll not find the caliber of victim that I find."; "Keep your guns away until we know it's Sean, okay? I know
  what you two are like."; Javier's "He hasn't stopped talking since we left you in Valentine. It's the longest
  ride of my life."); "The New South" ("I seem to have gotten myself in a spot of bother."; "silly fancy fop";
  "He is a magician, I know him. He's a fool… but, he is not a bad feller"; "Your idiot friend is free to go";
  "I promise you, this was all just a big misunderstanding."; "I will keep this fellow on the straight and
  narrow"; "Trelawny owes… everyone for something, but his information is good"; "Trelawny's like a bad penny";
  "Everywhere and nowhere"; "maybe there are actually a hundred Trelawnys"; "over-egging the pudding like the
  showman he is").
- Mission pages: "Friends in Very Low Places" (no violence, lock breaker, "discouraged men" as Trelawny calls the
  clerks, card trick seen through binoculars, Bill's message, reaction if Arthur kills the passengers),
  "A Fine Night of Debauchery", "Magicians for Sport".
- Red Dead Wiki EN "Josiah Trelawny" (infobox: alias, family, weapon, horse; quote box "How can romance ever be
  silly? It's all we have."; Personality, Appearance, Trivia) and FR page; wiki pages "Gwydion" and "Appaloosa"
  (horse), "Alden Carruthers", "Camp Events" (../hosea/m/Camp_Events.txt: crow tricks at Clemens Point,
  Uncle and Cornwall at Shady Belle, Saint Denis apartment talk, absence from Jack's party).
- Fact-checked fiches reused as is: arthur_A/B/D (eel line: attributed to the wiki's "Arthur Morgan/Relationships" page only, no source places
  it in the journal), dutch_A/C,
  hosea_B, charles_B, javier_B/C, leopold_B, sean_C, uncle_B, karen_B, mary_B, susan_B, bill_A, micah_D.

Fact-check pass (20 Oct 2026): fishing-ride lines labeled optional; "Well hello gentlemen" is the greeting, "spot of
bother" the reply; said-about-him lines quoted in part C Quotes only (paraphrased here); retold events cut to pointers.

Ownership (FIX_RULES): the Rockstar and guide descriptions live HERE only (part A Origins and part C Marketing
must not quote them). Names (Josiah, the Giuseppe Muldoon alias, "Trelawney" in the files, the surname's meaning)
live HERE only. Appearance (guide portrait, middle age, no winter outfit) lives HERE only. Camp scenes live in ONE
relationship entry each: crow trick with Karen and Susan -> Karen / Susan; crow in Mary-Beth's book -> Mary-Beth;
Cornwall talk -> Uncle; Saint Denis apartment talk with Arthur -> Family; Bill's message -> Bill. Narrative events
(Sean rescue, prison wagon, kidnapping, stagecoach, riverboat, departure) belong to part A; entries here refer to
them in one clause. Real-world material (Gevedon, cut content including the Micah snake encounter, the cut
revolver and the cut "tre2" mission, concept art) belongs to part D.

Lines quoted in this part (parts A and C must NOT repeat them; A paraphrases): the Rockstar and guide
descriptions; "Much as I love dodging the law and sleeping in the dirt with you derelicts, I do have other
business to attend to."; "But without me you'll not find the caliber of victim that I find."; "Keep your guns
away until we know it's Sean, okay? I know what you two are like."; "I seem to have gotten myself in a spot of
bother."; the wiki quote box "How can romance ever be silly? It's all we have."; and, inside relationship
entries, Dutch's, Hosea's, Arthur's, Javier's and Sheriff Gray's lines listed above. Left free for part A: the
parents line ("hogshead of ale"), the Heidi McCourt line, the first greeting in Valentine; for part C: the wiki
quotes about Rhodes, Alden ("A discouraged man is no man at all"), Desmond Blythe, the dime novel, "Everyone is the
author of his own good fortune", and the Red Dead Online lines.

WIKI-ONLY (kept, attributed or paraphrased without quotation marks): the alias, the sons' names, Italian, the
camp-as-office habit, the camp events, the card trick, Gwydion's breed and coat, the Cattleman revolver, the
absence of a winter outfit (stated on the Sean page, as already used in sean_B), the surname's meaning.

Excluded: the wiki's character readings ("willing to do whatever it takes to save himself", "always looking out
for himself", "isn't afraid to get his hands dirty"; judgments with no scene given; the Game Informer staff
say the opposite, so neither is stated as fact); the wiki's description of his accent as a Transatlantic accent
(the wiki's own analysis; the actor's description is in part D); "seemingly eager to end his life" (Red Dead
Online, part C); the claim that Trelawny made sure Javier got a job as a guard on the riverboat (character page
only; the mission page has Javier wearing a guard's stolen uniform); the cut-content page's claim that Charles
mentions a cane Trelawny is never seen with (contradicted by "Magicians for Sport", where the cane is found);
"likely a reference" for Gwydion's name (speculation; the name's mythological meaning is stated without claiming
intent); the Strange Man resemblance and the rare Guarma conversation (part C Trivia); Arthur's wiki quotes "He'd
sell his own sister to save a train fare" and "keeping fish on the line" (context not found in a transcript; left to
part C if verified); Catherine Braithwaite (Red Dead Online only, part C); the outfit catalogue.
"""

def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar Games' official description of Trelawny, published in September 2018, reads: \"A flamboyant conjurer, conman and trickster, Trelawny is a very hard man to pin down but he's always able to bring good leads.\"",
        "La description officielle de Trelawny publiée par Rockstar Games en septembre 2018 dit, dans sa version française : \"Magicien et escroc haut en couleur, la personnalité de Trelawny est difficile à cerner, mais il veille toujours à apporter de bonnes pistes.\"")},
    {"p": two(
        "A character page from an official guide, reproduced on the Red Dead Wiki, expands on it. It calls him a conjurer, conman and trickster \"with a taste for the finer things in life\", and says he \"is one of the only people Dutch allows to drift in and out of the gang\". It adds: \"He pops up out of nowhere and then, just like one of his magic tricks, disappears again. He is a very hard man to pin down, and not always to be trusted, but he consistently brings the gang good leads and provides some entertainment around camp.\" It ends: \"A cockroach in fancy britches, Trelawny is able to get into nooks and crannies that the rest of the gang can't.\"",
        "Une page de personnage tirée d'un guide officiel, reproduite sur le Red Dead Wiki, va plus loin. Elle le présente comme un magicien, escroc et filou \"with a taste for the finer things in life\" (qui a le goût des belles choses), et précise qu'il \"is one of the only people Dutch allows to drift in and out of the gang\" (fait partie des rares que Dutch laisse aller et venir dans la bande). Le guide ajoute qu'il surgit de nulle part puis disparaît, comme dans l'un de ses tours, qu'il est difficile à cerner et pas toujours digne de confiance, mais qu'il apporte régulièrement de bons tuyaux et distrait le camp. Il conclut : \"A cockroach in fancy britches, Trelawny is able to get into nooks and crannies that the rest of the gang can't.\" (un cafard en culotte de soie, capable de se glisser dans des recoins où le reste de la bande ne passe pas).")},
    {"p": two(
        "On jobs he prefers deception to gunfire (see Biography). He talks a great deal, to the annoyance of Javier, who rides with him on the search for Sean (see Javier Escuella). He keeps his life with the gang hidden from his wife and sons (see Biography).",
        "En mission, il préfère la ruse aux coups de feu (voir la biographie). Il parle beaucoup, au grand dam de Javier, qui fait la route avec lui pendant la recherche de Sean (voir Javier Escuella). Il cache à sa femme et à ses fils sa vie au sein de la bande (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "Riding with Arthur in \"The First Shall Be Last\", he explains his long absence: \"Much as I love dodging the law and sleeping in the dirt with you derelicts, I do have other business to attend to.\" A moment later he reminds Arthur what he brings to the gang: \"But without me you'll not find the caliber of victim that I find.\" On the same ride he warns Arthur and Javier: \"Keep your guns away until we know it's Sean, okay? I know what you two are like.\" Locked in Sheriff Gray's prison wagon in \"The New South\", he answers Dutch's greeting with: \"I seem to have gotten myself in a spot of bother.\" The Red Dead Wiki opens its page on him with another of his lines: \"How can romance ever be silly? It's all we have.\"",
        "En chemin avec Arthur, dans \"The First Shall Be Last\", il justifie sa longue absence : \"Much as I love dodging the law and sleeping in the dirt with you derelicts, I do have other business to attend to.\" (j'ai beau adorer fuir la loi et dormir par terre avec vous autres, bande de vauriens, j'ai d'autres affaires à mener). Un peu plus loin, il rappelle à Arthur ce qu'il apporte à la bande : \"But without me you'll not find the caliber of victim that I find.\" (mais sans moi, vous ne trouverez pas des pigeons du calibre de ceux que je déniche). Pendant la même chevauchée, il prévient Arthur et Javier : \"Keep your guns away until we know it's Sean, okay? I know what you two are like.\" (rangez vos armes tant qu'on n'est pas sûrs que c'est Sean, d'accord ? je vous connais, tous les deux). Enfermé dans le fourgon du shérif Gray, dans \"The New South\", il répond au salut moqueur de Dutch par un \"I seem to have gotten myself in a spot of bother.\" (on dirait que je me suis mis dans un petit embarras). Le Red Dead Wiki ouvre sa page sur une autre de ses répliques : \"How can romance ever be silly? It's all we have.\" (comment l'amour pourrait-il être idiot ? c'est tout ce que nous avons).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "He is usually called Trelawny, but Dutch and Arthur also use his first name, Josiah: \"Josiah, take Javier\", says Dutch in \"Americans at Rest\", and \"Javier, Josiah, come on\", says Arthur in \"The First Shall Be Last\". The Red Dead Wiki's infobox lists one alias, Giuseppe Muldoon, used once in Lemoyne, and marks it as uncertain; the French wiki spells it Giuseppe Muldon and ties it to the stagecoach robbery. According to the wiki's page on cut content, the game files sometimes spell his surname Trelawney. The wiki also notes that Trelawny is a variant of that Cornish surname, which it glosses as meaning a person from a town with a church.",
        "On l'appelle le plus souvent Trelawny, mais Dutch et Arthur emploient aussi son prénom, Josiah : \"Josiah, take Javier\", dit Dutch dans \"Americans at Rest\", et \"Javier, Josiah, come on\", lance Arthur dans \"The First Shall Be Last\". L'infobox du Red Dead Wiki lui prête un seul pseudonyme, Giuseppe Muldoon, employé une fois dans le Lemoyne, en le signalant comme incertain ; le wiki français l'écrit Giuseppe Muldon et le rattache au braquage de la diligence. D'après la page du wiki consacrée au contenu coupé, les fichiers du jeu orthographient parfois son nom Trelawney. Le wiki rappelle enfin que Trelawny est une variante de ce nom de famille cornouaillais, qu'il traduit par une personne venue d'un bourg doté d'une église.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "The guide's portrait shows a man with dark hair, light eyes and a thick dark mustache, in a black top hat, a dark coat over a blue paisley vest, a black cravat, white gloves and pale gray-green trousers. The Red Dead Wiki puts him in middle age, with dark brown hair combed back, a trimmed mustache and formal clothes in every scene. According to the wiki, he is one of three gang members, with Sean and Cleet, who have no winter outfit.",
        "Le portrait du guide montre un homme aux cheveux sombres, aux yeux clairs et à l'épaisse moustache brune, coiffé d'un haut-de-forme noir, en redingote sombre sur un gilet bleu à motifs cachemire, avec une cravate noire, des gants blancs et un pantalon gris-vert pâle. Le Red Dead Wiki le dit d'âge mûr, cheveux brun foncé peignés en arrière, moustache taillée, et toujours en tenue habillée. Selon le wiki, il fait partie, avec Sean et Cleet, des trois membres de la bande qui n'ont pas de tenue d'hiver.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Skills, weapons and horse", "Compétences, armes et cheval")},
    {"h4": two("Magic tricks", "Tours de magie")},
    {"p": two(
        "Trelawny performs conjuring tricks in camp: at Clemens Point he makes a crow appear from his hand and another fly out of a book (see Karen Jones and Mary-Beth Gaskill). According to the mission page of \"Friends in Very Low Places\", before the mission starts he can be seen through binoculars doing a trick with a playing card.",
        "Trelawny fait des tours de prestidigitation au camp : à Clemens Point, il fait surgir un corbeau de sa main, puis un autre d'un livre (voir Karen Jones et Mary-Beth Gaskill). D'après la page de la mission \"Friends in Very Low Places\", on peut l'observer aux jumelles, avant le début de la mission, en train de faire un tour avec une carte à jouer.")},
    {"h4": two("Cons, distractions and tips", "Escroqueries, diversions et tuyaux")},
    {"p": two(
        "On each of the three operations he shares with Arthur, his own part is a performance: a staged collapse by the river, a serenade requested at the coach, small talk with Blythe at the riverboat bar (see Biography). His other asset is information. He tracks down where Sean is held, keeps a contact among the tip-selling clerks of the postal service (see Alden Carruthers) and spots the poker game that Desmond Blythe plays aboard the Grand Korrigan. The Red Dead Wiki adds that he speaks some Italian.",
        "Dans chacune des trois opérations qu'il mène avec Arthur, son rôle à lui relève de la comédie : un malaise simulé au bord de la rivière, une sérénade réclamée à la diligence, une conversation avec Blythe au bar du bateau à aubes (voir la biographie). Son autre atout, c'est l'information. Il retrouve l'endroit où Sean est détenu, a ses entrées chez les employés des postes qui vendent des tuyaux (voir Alden Carruthers) et repère la partie de poker de Desmond Blythe à bord du Grand Korrigan. Le Red Dead Wiki ajoute qu'il parle un peu l'italien.")},
    {"h4": two("Weapons and horse", "Armes et cheval")},
    {"p": two(
        "The Red Dead Wiki gives him a Cattleman revolver. His horse is Gwydion, a brown leopard Appaloosa stallion with a small star on his face, according to the wiki's page on the horse. Trelawny rides him in \"The First Shall Be Last\" and \"Friends in Very Low Places\". The wiki notes that a horse with the same coat can be bought at the Tumbleweed stable in the epilogue. Gwydion is also the name of a trickster figure of Welsh mythology.",
        "Le Red Dead Wiki lui attribue un revolver Cattleman. Son cheval s'appelle Gwydion, un étalon Appaloosa à robe léopard brune, marqué d'une petite étoile en tête, selon la page du wiki consacrée au cheval. Trelawny le monte dans \"The First Shall Be Last\" et \"Friends in Very Low Places\". Le wiki relève qu'un cheval à la robe identique est en vente à l'écurie de Tumbleweed pendant l'épilogue. Gwydion est aussi le nom d'une figure de filou de la mythologie galloise.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "Arthur is Trelawny's partner on most of his jobs: the search for Sean, the stagecoach and the riverboat (see Biography). On the fishing ride that can follow \"The New South\", Arthur claims that Trelawny owes him for catching the Anderson boys. If he then asks about Trelawny, he calls him \"like a bad penny\", and after Dutch's outhouse story he jokes that there may be a hundred of him (see Quotes). According to the Red Dead Wiki's page on Arthur's relationships, Arthur once describes him as \"as slippery as an eel in an oil slick\".",
            "Arthur est le partenaire de Trelawny sur la plupart de ses coups : la recherche de Sean, la diligence et le bateau à aubes (voir la biographie). Pendant la partie de pêche qui peut suivre \"The New South\", Arthur estime que Trelawny lui doit une fière chandelle pour la capture des frères Anderson. S'il pose ensuite des questions sur lui, il le compare à une mauvaise pièce qui revient toujours (\"like a bad penny\"), puis, après l'histoire des latrines racontée par Dutch, s'amuse à l'idée qu'il en existe peut-être une centaine (voir Citations). Selon la page du Red Dead Wiki consacrée aux relations d'Arthur, celui-ci le décrit un jour comme \"as slippery as an eel in an oil slick\" (glissant comme une anguille dans une nappe de pétrole)."),
        two(
            "In chapter 6 Arthur lets him leave with his blessing (see Biography).",
            "Au chapitre 6, Arthur le laisse partir avec sa bénédiction (voir la biographie)."),
    ]},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": [
        two(
            "Dutch brings Trelawny to Arthur in Valentine with the words \"Look who we found sniffing about\". When Trelawny reminds him that the law is after him above all, Dutch answers \"Always is\". In \"The New South\" he describes Trelawny to Sheriff Gray as a \"silly fancy fop\", then vouches for him (see Biography). Once Trelawny is free, Dutch promises the sheriff to keep him \"on the straight and narrow\".",
            "Dutch amène Trelawny à Arthur, à Valentine, en lançant \"Look who we found sniffing about\" (regardez qui on a trouvé à fureter dans le coin). Quand Trelawny lui fait remarquer que c'est lui qu'on veut, il répond \"Always is\" (comme toujours). Dans \"The New South\", il parle de Trelawny au shérif Gray comme d'un \"silly fancy fop\" (un petit dandy ridicule), puis se porte garant de lui (voir la biographie). Une fois Trelawny libéré, Dutch promet au shérif de le remettre dans le droit chemin."),
        two(
            "On the optional fishing ride after \"The New South\", if Arthur asks where Trelawny goes, Dutch answers \"Everywhere and nowhere\", grants that the gang would not have got Sean back without him, and tells the outhouse story (see Biography). If Arthur asks about the bounty hunters instead, Dutch dismisses the talk of super agents as \"over-egging the pudding like the showman he is\".",
            "Pendant la partie de pêche facultative qui suit \"The New South\", si Arthur demande où va Trelawny, Dutch répond \"Everywhere and nowhere\" (partout et nulle part), reconnaît que sans lui la bande n'aurait jamais récupéré Sean, et raconte l'histoire des latrines (voir la biographie). Si Arthur l'interroge plutôt sur les chasseurs de primes, Dutch balaie les super agents d'un revers de main : pour lui, Trelawny en rajoute, en vrai showman (\"over-egging the pudding like the showman he is\")."),
    ]},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "Hosea is with Dutch and Arthur when they find Trelawny in the prison wagon in \"The New South\". When Trelawny reports the talk of big bounties, Hosea asks him where he heard it. On the fishing ride that can follow, he grants that Trelawny is in debt to just about everyone but that his information can be trusted (see Quotes).",
        "Hosea accompagne Dutch et Arthur quand ils trouvent Trelawny dans le fourgon de prisonniers, dans \"The New South\". Quand Trelawny parle de grosses primes, Hosea lui demande d'où il tient cela. Pendant la partie de pêche qui peut suivre, il concède que Trelawny a des dettes envers à peu près tout le monde, mais que ses renseignements sont fiables (voir Citations).")},
    {"img": "charles-smith.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
        "Dutch sends Charles, Trelawny and Javier to gather news of Sean in \"Americans at Rest\". In \"Magicians for Sport\" Charles and Arthur track Trelawny from his ransacked caravan to the farm where bounty hunters hold him (see Biography). Charles and Trelawny then ride back to camp together.",
        "Dutch envoie Charles, Trelawny et Javier aux nouvelles de Sean dans \"Americans at Rest\". Dans \"Magicians for Sport\", Charles et Arthur remontent la piste de Trelawny, de sa roulotte saccagée jusqu'à la ferme où des chasseurs de primes le retiennent (voir la biographie). Charles et Trelawny rentrent ensuite ensemble au camp.")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Dutch pairs Javier with Trelawny to look for Sean (see Names). When Arthur catches up with them in \"The First Shall Be Last\" and asks Javier why he is so quiet, Javier blames Trelawny's nonstop talk since Valentine (see Quotes). The two work together again on the riverboat job (see Biography).",
        "Dutch confie Javier à Trelawny pour retrouver Sean (voir Noms). Quand Arthur les rejoint, dans \"The First Shall Be Last\", et demande à Javier pourquoi il est si silencieux, celui-ci accuse Trelawny de n'avoir pas cessé de parler depuis Valentine (voir Citations). Les deux hommes se retrouvent sur le coup du bateau à aubes (voir la biographie).")},
    {"img": "sean-macguire.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
        "Trelawny brings the gang the news that Sean is alive and held by bounty hunters, then helps Arthur and Javier reach him (see Biography).",
        "Trelawny apprend à la bande que Sean est vivant, aux mains de chasseurs de primes, puis aide Arthur et Javier à l'atteindre (voir la biographie).")},
    {"img": "leopold-strauss.jpeg", "slug": "leopold-strauss", "name": "Leopold Strauss", "text": two(
        "Strauss is part of Trelawny's riverboat job, where he helps Arthur at the poker table (see Biography). Neither Trelawny nor Strauss attends the party for Jack's return at Shady Belle, according to the wiki's camp events page.",
        "Strauss fait partie du coup du bateau à aubes monté par Trelawny, où il aide Arthur à la table de poker (voir la biographie). Selon la page du wiki consacrée aux scènes de camp, ni Trelawny ni Strauss n'assistent à la fête du retour de Jack, à Shady Belle.")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "In Valentine Trelawny greets Bill as \"looking well as can be\". According to Hosea, Bill and Arthur were away on another errand the day Dutch found Trelawny in the outhouse (see Biography). When \"Friends in Very Low Places\" is the only story mission still open before \"A Short Walk in a Pretty Town\", Trelawny relays word from Bill: he wants Arthur to join him in Rhodes and do some work for the Grays (mission page).",
        "À Valentine, Trelawny salue Bill en le trouvant \"looking well as can be\" (en aussi bonne forme que possible). D'après Hosea, Bill et Arthur étaient partis ailleurs le jour où Dutch a trouvé Trelawny dans les latrines (voir la biographie). Quand \"Friends in Very Low Places\" est la seule mission principale encore ouverte avant \"A Short Walk in a Pretty Town\", Trelawny transmet un message de Bill : celui-ci attend Arthur à Rhodes pour travailler pour les Gray (page de la mission).")},
    {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
        "By the Shady Belle campfire Uncle asks Trelawny where he comes from. Trelawny first answers the moons of Jupiter, then, once Uncle has made a few guesses, Cornwall, which he calls the home of the original Celts. Asked what it is like, he admits he has never been there. Uncle replies that he comes from Ohio, and has at least been there.",
        "Au coin du feu de Shady Belle, Uncle demande à Trelawny d'où il vient. Trelawny répond d'abord les lunes de Jupiter, puis, après quelques suppositions d'Uncle, les Cornouailles, qu'il présente comme le berceau des vrais Celtes. Quand Uncle lui demande à quoi ça ressemble, il reconnaît n'y être jamais allé. Uncle répond qu'il vient de l'Ohio, et que lui, au moins, y a mis les pieds.")},
    {"img": "karen-jones.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": two(
        "At Clemens Point Trelawny asks Karen about the book she is reading by the wagons, and she calls it a silly romance. When Susan interrupts to ask whether Karen plans to do any work, Trelawny makes a crow appear from his hand; Susan leaves in disgust and Karen laughs.",
        "À Clemens Point, Trelawny demande à Karen quel livre elle lit près des chariots ; elle répond que c'est une romance idiote. Quand Susan les interrompt pour demander si Karen compte travailler un jour, Trelawny fait apparaître un corbeau dans sa main ; Susan s'en va écœurée, et Karen rit.")},
    {"img": "mary-beth-gaskill.jpeg", "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill", "text": two(
        "At Clemens Point Trelawny finds Mary-Beth reading by the wagons and tells her she is as pretty as a picture. He then opens her book and a crow flies out of it. Once he has gone, Karen calls him a devil and Mary-Beth answers that he is a kind one.",
        "À Clemens Point, Trelawny trouve Mary-Beth en train de lire près des chariots et lui dit qu'elle est jolie comme un cœur. Il ouvre ensuite son livre, d'où s'envole un corbeau. Une fois qu'il est parti, Karen le traite de diable, et Mary-Beth répond qu'il est gentil, pour un diable.")},
    {"img": "susan-grimshaw.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
        "Susan is on the receiving end of Trelawny's crow trick at Clemens Point (see Karen Jones).",
        "C'est Susan qui fait les frais du tour du corbeau, à Clemens Point (voir Karen Jones).")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "The two share no scene in the finished game. A camp encounter between them was recorded and cut (see Development and performance).",
        "Les deux hommes ne partagent aucune scène dans le jeu final. Une scène de camp entre eux a été enregistrée puis coupée (voir Conception et interprétation).")},
    {"img": None, "slug": None, "name": "His wife and sons", "text": two(
        "Trelawny has a wife and two sons, named Tarquin and Cornelius according to the Red Dead Wiki, who live in an apartment in Saint Denis, where Arthur can overhear them (see Biography). At Shady Belle Trelawny tells Arthur he knew he had been there. Arthur says he did not know Trelawny was married; Trelawny answers that he loves his wife but cannot stay in one place.",
        "Trelawny a une femme et deux fils, prénommés Tarquin et Cornelius selon le Red Dead Wiki, qui vivent dans un appartement de Saint-Denis, où Arthur peut les entendre (voir la biographie). À Shady Belle, Trelawny dit à Arthur qu'il sait qu'il est passé par là. Arthur avoue qu'il ignorait que Trelawny était marié ; Trelawny répond qu'il aime sa femme, mais qu'il ne tient pas en place.")},
    {"img": None, "slug": None, "name": "Alden Carruthers", "text": two(
        "Alden sells Trelawny and Arthur the stagecoach tip in \"Friends in Very Low Places\" (see Biography). The Red Dead Wiki lists Trelawny among Alden's associates.",
        "Alden vend à Trelawny et à Arthur le tuyau sur la diligence dans \"Friends in Very Low Places\" (voir la biographie). Le Red Dead Wiki range Trelawny parmi les associés d'Alden.")},
    {"img": None, "slug": None, "name": "Leigh Gray", "text": two(
        "The sheriff of Rhodes holds Trelawny in his prison wagon (see Biography). Once Arthur has brought in Anders Anderson, the leader of the escapees, Gray releases Trelawny with the words \"Your idiot friend is free to go\".",
        "Le shérif de Rhodes détient Trelawny dans son fourgon cellulaire (voir la biographie). Une fois qu'Arthur lui a ramené Anders Anderson, le meneur des évadés, Gray libère Trelawny en lançant \"Your idiot friend is free to go\" (votre ami l'imbécile peut partir).")},
]
