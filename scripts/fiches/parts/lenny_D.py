"""Lenny Summers, reference fiche, PART D: base data, Development and performance, Reception.

His live page (characters/lenny-summers/) was generated from the v2 entry in scripts/_enrich.py
(ENRICHED, "slug": "lenny-summers"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the birth year 1880 is no longer stated as a fact (no game line gives it;
the facts grid gives the Red Dead Wiki estimate, attributed, and the schema birthDate is dropped); the
"1880-1899" and "Deceased" chips are replaced (the second duplicated the death); the v2 intro called
him "the youngest gunman" (unsourced superlative, removed) and said he joined after three years on
the run (kept in part A, Origins); the v2 Development section is kept and expanded (actor's stage
work, the recording of "A Quiet Time" with outlet and author, cut content); the v2 Reception is kept
and expanded with three more dated, attributed articles. Corrections of attribution: the Game
Informer piece is by Jason Guisao, 18 Feb 2019 (the 2022 republication is credited to "Game Informer
Editorial"); the Slate article is by Jonathan S. Jones, 4 Feb 2019, and the phrase "overt commentary
about the brutality of life under slavery and Jim Crow" is Jones's description of the game, not of
Lenny alone (the v2 text was right, Wikipedia's wording is looser). publishDate 2026-06-27 kept
(git: 7c38ebe, drip publish of lenny-summers, 27 Jun 2026). reg_role matches characters_registry.py
("Van der Linde gang &middot; RDR2").

Sources (internal register, fetched 19 Oct 2026, saved in scratchpad cov/lenny/fc/):
- Red Dead Wiki "Harron Atkins" (Harron_Atkins.txt): American actor, voice and motion capture for
  Lenny. American Theatre, "Ensemble Studio Theatre Announces New Youngblood Members", 16 Oct 2017
  (fetched): Atkins among the 2017-18 members of EST/Youngblood, a collective for emerging
  playwrights under 30. Wikipedia "List of Red Dead Redemption 2 characters" (m/wp_List...txt):
  credits Atkins; cites the Complete Official Guide, Collector's Edition (Piggyback, 2018), p. 378.
- Twinfinite, Hayes Madsen, 19 Feb 2019, "Red Dead Redemption 2 Interview: The Actor Behind Arthur
  Morgan Talks About Becoming the Main Character, Lenny Scene & More" (archived copy of
  24 Dec 2024, tw.html; quotes checked).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (Red_Dead_Redemption_2_Cut_Content.txt):
  unused hands, vest, two gunbelts; Bill and Lenny planned for "Pouring Forth Oil IV" (screenshot
  LennyBeta.png); unused Micah encounter (file ccm14.awc); cut carriage lines for Bill, Lenny and
  Dutch after the tailor scene; item request "bf"; concept art of Sean, Trelawny, Sadie, Lenny and
  Micah; pre-release shot with an unused horse for Lenny; First Look screenshot with a beta Maggie.
  Wiki "Lenny Summers" gallery caption: first trailer look (grey coat, red trousers, paisley
  bandana, buckskin stallion, Litchfield Repeater).
- Polygon, Chris Plante, 25 Oct 2018, review (../bill/fc/polygon.txt; quotes checked).
- USgamer, Mike Williams, 30 Oct 2018, "Red Dead Redemption 2's Arthur Morgan Is the Wokest Outlaw"
  (archived copy, datePublished 2018-10-30; quotes checked).
- Game Informer staff, 27 Dec 2018, gang ranking (../uncle/fc/gi_ranking.txt): Lenny 7th of 24.
- Slate (Brow Beat), Jonathan S. Jones, 4 Feb 2019, "Red Dead Redemption 2 Confronts the U.S.'s
  Racist Past and Lets You Do Something About It" (slate.html; quotes checked; the HNN roundup
  spells the author "Jonathon").
- Game Informer, Jason Guisao, 18 Feb 2019, "Celebrating Ten Respectful Representations Of Blackness
  In Gaming" (archived copy of 18 Feb 2019, gi2019_arch.html; quotes checked); republished 14 Feb
  2022 under "Game Informer Editorial" (gi2019.html).
Excluded: Atkins's birth date and birthplace (13 Dec 1992, Detroit: wiki only) and the Michigan
Poetry Out Loud title (wiki reference page not retrievable); his IMDb credits (search extract only);
Curzon Dobell naming Lenny as his favorite character (panel captions do not identify the speaker,
as in hosea_D); the wiki's guess that the Micah encounter was cut "to avoid controversy"
(speculation); Game Informer's "LEMNY" joke (not explained in the text); Polygon's and USgamer's
transcriptions of Lenny's lines on the ride to Shady Belle (mission dialogue: part C if quoted, from
a transcript); Slate's transcription of the Raiders line (same reason).
DUPLICATE ownership: actor, recording, cut content and pre-release looks live HERE; parts B and C
must not retell them. Rockstar's 6 Sep 2018 description and the official guide page belong to part
B. Reception does not repeat Development. The first-trailer look lives in part C (Marketing), not here.
Fact-check of 19 Oct 2026 applied: "son of former slaves" attributed to the Red Dead Wiki in intro and
essentials; Valentine placed in the Clemens Point chapter (the town is in New Hanover, not Lemoyne);
the Valentine night is no longer listed among "jobs"; "shot down" (not "shot dead"); the cut carriage
sequence attributed to the wiki as an inference from leftover lines.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Lenny is played by Harron Atkins, an American actor who provides both his voice and his motion capture, according to the Red Dead Wiki; Wikipedia's list of the game's characters also credits him in the role. Atkins also writes for the stage: American Theatre reported on 16 October 2017 that he was one of the ten new members of Youngblood, the collective that Ensemble Studio Theatre in New York runs for emerging playwrights under 30, for the 2017-18 season.",
              "Lenny est interprété par Harron Atkins, acteur américain qui lui prête à la fois sa voix et ses mouvements, selon le Red Dead Wiki ; la liste des personnages du jeu sur Wikipédia le crédite aussi dans ce rôle. Atkins écrit également pour le théâtre : le 16 octobre 2017, American Theatre annonçait qu'il figurait parmi les dix nouveaux membres de Youngblood, le collectif que l'Ensemble Studio Theatre de New York consacre aux jeunes dramaturges de moins de 30 ans, pour la saison 2017-2018.")},
    {"h3": two("Recording \"A Quiet Time\"", "Le tournage de \"A Quiet Time\"")},
    {"p": two("In an interview with Hayes Madsen published by Twinfinite on 19 February 2019, Roger Clark, who plays Arthur Morgan, said the saloon scene with Lenny was shot \"over like two or three days\", at a time when he already knew Atkins \"very well\". He recalled that the team told him they wanted \"some really frenetic editing that's not going to be characteristic with the rest of the game\", to convey drunkenness. The shoot was made of many short pieces: the actors ran from one part of the capture stage to another, told to start punching each other, then to dance the can-can. Clark described the work as \"very episodic\" and \"a lot of fun\".",
              "Dans un entretien avec Hayes Madsen publié par Twinfinite le 19 février 2019, Roger Clark, l'interprète d'Arthur Morgan, explique que la scène du saloon avec Lenny a été tournée en deux ou trois jours, à un moment où il connaissait déjà très bien Atkins. Il se souvient que l'équipe lui avait annoncé un montage volontairement frénétique, sans équivalent dans le reste du jeu, pour rendre l'ivresse. Le tournage s'est fait par petits morceaux : les acteurs couraient d'un coin à l'autre du plateau de capture, avec pour consigne de se mettre à se battre, puis de danser le french cancan. Clark parle d'un travail \"very episodic\" (très décousu) et très amusant.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The files of Red Dead Redemption 2 contain unused hands, an unused vest and two unused gun belts for Lenny. According to the Red Dead Wiki, he and Bill were originally meant to take part in \"Pouring Forth Oil IV\", a mission in which neither appears in the released game; the wiki shows a screenshot of Lenny in that mission. According to the Red Dead Wiki, lines for Bill, Lenny and Dutch suggest a cut follow-up in which the player boards the carriage after a cut scene at the Saint Denis tailor, before \"The Gilded Cage\". An item request from Lenny, labeled only with the initials \"bf\", was cut as well; what it referred to is unknown.",
              "Les fichiers de Red Dead Redemption 2 contiennent des mains, un gilet et deux ceinturons inutilisés pour Lenny. D'après le Red Dead Wiki, Bill et lui devaient à l'origine participer à \"Pouring Forth Oil IV\", une mission où aucun des deux n'apparaît dans le jeu final ; le wiki montre une capture de Lenny dans cette mission. D'après le Red Dead Wiki, des répliques de Bill, Lenny et Dutch laissent penser qu'une séquence coupée prévoyait que le joueur monte dans la voiture après une scène, elle aussi coupée, chez le tailleur de Saint-Denis, avant \"The Gilded Cage\". Une demande d'objet de Lenny, désignée seulement par les initiales \"bf\", a également été supprimée ; on ignore à quoi elle correspondait.")},
    {"p": two("The same wiki describes an unused camp encounter, found in the file ccm14, in which Micah calls Lenny boy; when Lenny objects, Micah asks what he should call him instead, uses a racial slur, and Lenny walks off angry. Early images released before the game show him on an unused horse and on a beta version of Maggie. A piece of concept art groups him with Sean, Trelawny, Sadie and Micah.",
              "Le même wiki décrit une scène de camp inutilisée, retrouvée dans le fichier ccm14, où Micah appelle Lenny boy (le garçon) ; quand Lenny proteste, Micah lui demande comment il devrait l'appeler, lâche une insulte raciste, et Lenny s'en va, furieux. Des images diffusées avant la sortie du jeu le montrent sur un cheval inutilisé et sur une version bêta de Maggie. Une illustration conceptuelle le réunit avec Sean, Trelawny, Sadie et Micah.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("At release", "À la sortie")},
    {"p": two("In his review for Polygon, published on 25 October 2018, Chris Plante wrote that the gang's members of color \"carry the additional burden\" of showing Arthur, and the player, how America treats them, and cited Lenny having to explain to an \"impossibly naïve\" Arthur that plantation owners would consider lynching him. He also criticized the aftermath of the night in Valentine: Lenny is mobbed by the police, yet the next time Arthur sees him all is well, and Lenny talks about the night \"the way a frat boy flippantly jokes\" about a blackout.",
              "Dans sa critique pour Polygon, publiée le 25 octobre 2018, Chris Plante écrit que les membres non blancs de la bande portent un fardeau supplémentaire : faire découvrir à Arthur, et au joueur, la façon dont l'Amérique les traite. Il cite Lenny, contraint d'expliquer à un Arthur d'une naïveté invraisemblable que les planteurs envisageraient de le lyncher. Il reproche aussi au jeu la suite de la nuit de Valentine : Lenny se fait malmener par la police, mais tout va bien la fois suivante, et Lenny évoque la soirée comme un étudiant qui plaisante d'une beuverie dont il ne se souvient plus.")},
    {"p": two("On 30 October 2018, Mike Williams of USgamer called the saloon night with Lenny \"one of the better moments\" of the game and wrote that he kept expecting Lenny to end up \"at the hands of a mob\", which does not happen. He used Arthur and Lenny's conversation on the way to Shady Belle as an example of Arthur listening to Lenny's problems, in an article about Arthur's open-mindedness.",
              "Le 30 octobre 2018, Mike Williams, sur USgamer, range la soirée au saloon avec Lenny parmi les meilleurs moments du jeu et dit s'être attendu tout du long à voir Lenny finir entre les mains d'une foule, ce qui n'arrive pas. Dans un article consacré à l'ouverture d'esprit d'Arthur, il prend la conversation entre Arthur et Lenny sur la route de Shady Belle comme exemple d'un Arthur qui écoute les problèmes de Lenny.")},
    {"p": two("Game Informer's staff ranked Lenny 7th of the 24 members of the Van der Linde gang on 27 December 2018. They called the drinking mission the game's \"comedic high point\", praised his conversations, from talking to Arthur about white privilege to teaching Sean to read, and described his death in the Saint Denis bank robbery as \"one of the cruelest gut punches in a game filled with them\".",
              "Le 27 décembre 2018, la rédaction de Game Informer classe Lenny 7e des 24 membres du gang Van der Linde. Elle voit dans la mission de beuverie le sommet comique du jeu, salue ses conversations, qu'il parle à Arthur du privilège blanc ou apprenne à lire à Sean, et juge sa mort pendant le braquage de Saint-Denis comme l'un des coups les plus cruels d'un jeu qui n'en manque pas.")},
    {"h3": two("Later commentary", "Analyses ultérieures")},
    {"p": two("In an article for Slate published on 4 February 2019, the historian Jonathan S. Jones wrote that the game's \"subtle racial undertones\" in Lemoyne give way to \"more overt commentary about the brutality of life under slavery and Jim Crow\", and that \"the most revealing example\" comes from the conversations between Arthur and \"his protégé, Lenny\". He mentioned Lenny's campfire talk about the scars on his father's back and about enslaved women raped by slaveholders, and the tip from Black residents of Rhodes that leads to the Lemoyne Raiders.",
              "Dans un article pour Slate publié le 4 février 2019, l'historien Jonathan S. Jones écrit qu'en Lemoyne les sous-entendus raciaux discrets du jeu laissent place à un commentaire plus direct sur la brutalité de l'esclavage et des lois Jim Crow, dont l'exemple le plus parlant tient aux conversations entre Arthur et \"his protégé, Lenny\" (son protégé, Lenny). Il cite les propos de Lenny, au coin du feu, sur les cicatrices du dos de son père et les viols d'esclaves par leurs maîtres, ainsi que le renseignement venu d'habitants noirs de Rhodes qui mène aux Lemoyne Raiders.")},
    {"p": two("Game Informer's Jason Guisao opened his list of ten \"respectful representations of blackness in gaming\", published on 18 February 2019, with Lenny. He called him \"a vocal reminder of the heightened racial tensions that plagued the wild frontier\" and found \"Preaching Forgiveness as He Went\" \"particularly striking\" for the way Lenny tells Arthur what it is to be Black in a hateful America. The magazine republished the entry in February 2022.",
              "Jason Guisao, de Game Informer, ouvre avec Lenny sa liste de dix représentations respectueuses des Noirs dans le jeu vidéo, publiée le 18 février 2019. Il voit en lui \"a vocal reminder of the heightened racial tensions that plagued the wild frontier\" (un rappel explicite des tensions raciales exacerbées qui empoisonnaient la Frontière) et juge \"Preaching Forgiveness as He Went\" particulièrement marquante, pour la façon dont Lenny explique à Arthur ce que c'est d'être noir dans une Amérique haineuse. Le magazine a republié ce texte en février 2022.")},
]


BASE = {
    "slug": "lenny-summers", "name": "Lenny Summers",
    "publishDate": "2026-06-27", "updated": "2026-10-19", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": "American",
    "portrait_alt": two("Lenny Summers in Red Dead Redemption 2", "Lenny Summers dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Lenny Summers, the young gunman of the Van der Linde gang in Red Dead Redemption 2: his past, the night in Valentine with Arthur, the Shady Belle raid and his death in Saint Denis. Biography, missions, actor.",
                     "Lenny Summers, le jeune tireur du gang Van der Linde dans Red Dead Redemption 2 : son passé, la nuit de Valentine avec Arthur, le raid de Shady Belle et sa mort à Saint-Denis. Biographie, missions, interprète."),
    "og_desc": two("The complete reference on Lenny Summers: life, missions, quotes, development and reception.",
                   "La référence complète sur Lenny Summers : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Young gunman of the Van der Linde gang in 1899, on the run since he killed his father's murderers at fifteen, who is shot down during the Saint Denis bank robbery in Red Dead Redemption 2.",
                       "Jeune tireur du gang Van der Linde en 1899, en fuite depuis qu'il a tué les meurtriers de son père à quinze ans, abattu pendant le braquage de la banque de Saint-Denis dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Van der Linde gang", "Gang Van der Linde"),
              two("Saint Denis", "Saint-Denis"),
              two("Played by <strong>Harron Atkins</strong>", "Interprété par <strong>Harron Atkins</strong>")],
    "facts": [
        {"label": two("Full name", "Nom complet"), "value": two("Leonard Summers (the name on his father's letter)", "Leonard Summers (le prénom figure sur la lettre de son père)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game (Red Dead Wiki estimate: around 1880)", "Non précisée dans le jeu (estimation du Red Dead Wiki : vers 1880)")},
        {"label": two("Died", "Mort"), "value": two("1899, Saint Denis, shot by Pinkerton riflemen on the rooftops in \"Banking, The Old American Art\"", "1899, à Saint-Denis, abattu par des tireurs de la Pinkerton sur les toits dans \"Banking, The Old American Art\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased; buried beside Hosea Matthews in Bluewater Marsh", "Décédé ; enterré auprès d'Hosea Matthews dans le Bluewater Marsh")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Family", "Famille"), "value": two("Father (killed when Lenny was fifteen), mother; an uncle who helped educate him, according to an official guide", "Un père (tué quand Lenny avait quinze ans), une mère ; un oncle qui a contribué à son instruction, d'après un guide officiel")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang (a recent recruit in 1899)", "Gang Van der Linde (recrue récente en 1899)")},
        {"label": two("Role", "Rôle"), "value": two("Gunman of the gang", "Tireur de la bande")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Harron Atkins (voice and motion capture)", "Harron Atkins (voix et capture de mouvement)")},
    ],
    "intro": [
        two("Lenny Summers is a young gunman of the Van der Linde gang in Red Dead Redemption 2 (2018), set in 1899. According to the Red Dead Wiki, his parents were former slaves. Educated by his father, he has been on the run since he killed the men who murdered his father when he was fifteen. A recent recruit, he takes part in most of the gang's big jobs of 1899 alongside [[arthur-morgan|Arthur Morgan]], from the robbery of Cornwall's train to the raid on Shady Belle and the Valentine bank. He is shot down on a rooftop in Saint Denis during the gang's failed bank robbery, on the same day as [[hosea-matthews|Hosea Matthews]].",
            "Lenny Summers est un jeune tireur du gang Van der Linde dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Selon le Red Dead Wiki, ses parents étaient d'anciens esclaves. Instruit par son père, il est en fuite depuis qu'il a tué, à quinze ans, les hommes qui avaient assassiné celui-ci. Recrue récente, il participe aux côtés d'[[arthur-morgan|Arthur Morgan]] à la plupart des grands coups du gang en 1899, de l'attaque du train de Cornwall au raid de Shady Belle et à la banque de Valentine. Il est abattu sur un toit de Saint-Denis pendant le braquage raté de la banque, le même jour qu'[[hosea-matthews|Hosea Matthews]]."),
        two("He is played by Harron Atkins, who provides his voice and motion capture.",
            "Il est interprété par Harron Atkins, qui lui prête sa voix et ses mouvements."),
    ],
    "essentials": [
        two("Son of former slaves according to the Red Dead Wiki, and educated by his father; at fifteen he killed the men who had murdered his father, and spent the next three years on the run before joining the Van der Linde gang.",
            "Fils d'anciens esclaves selon le Red Dead Wiki, instruit par son père ; à quinze ans, il tue les hommes qui ont assassiné son père, puis passe trois ans en fuite avant de rejoindre le gang Van der Linde."),
        two("He boards Cornwall's moving train with [[arthur-morgan|Arthur]] in \"Who the Hell is Leviticus Cornwall?\", then brings the news of [[micah-bell|Micah]]'s arrest in Strawberry, which Dutch answers by sending Arthur to take him drinking in Valentine (\"A Quiet Time\").",
            "Il monte avec [[arthur-morgan|Arthur]] dans le train en marche de Cornwall dans \"Who the Hell is Leviticus Cornwall?\", puis rapporte la nouvelle de l'arrestation de [[micah-bell|Micah]] à Strawberry ; Dutch envoie alors Arthur l'emmener boire à Valentine (\"A Quiet Time\")."),
        two("During the Clemens Point chapter he leads Arthur to the Lemoyne Raiders' weapons at Shady Belle and robs the Valentine bank with Arthur, [[bill-williamson|Bill]] and [[karen-jones|Karen]].",
            "Pendant le chapitre de Clemens Point, il conduit Arthur jusqu'aux armes des Lemoyne Raiders à Shady Belle et braque la banque de Valentine avec Arthur, [[bill-williamson|Bill]] et [[karen-jones|Karen]]."),
        two("In Saint Denis he drives the coach to the mayor's party and escapes the trolley station trap with Dutch and Arthur. He is shot down on the rooftops during \"Banking, The Old American Art\" and buried beside [[hosea-matthews|Hosea]] in Bluewater Marsh.",
            "À Saint-Denis, il conduit la voiture qui mène à la réception du maire et échappe avec Dutch et Arthur au piège de la gare de tramways. Il est abattu sur les toits pendant \"Banking, The Old American Art\" et enterré auprès d'[[hosea-matthews|Hosea]] dans le Bluewater Marsh."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["arthur-morgan", "hosea-matthews", "micah-bell", "sean-macguire"],
}
