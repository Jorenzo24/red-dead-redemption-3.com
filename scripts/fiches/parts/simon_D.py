"""Simon Pearson, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026, medium tier).

His live page (characters/simon-pearson/) was generated from the v2 entry in scripts/_enrich.py
(BATCH1, "slug": "simon-pearson"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the v2 intro paraphrased the official guide ("A former US Navy sailor, he keeps the camp fed
and supplied"); the guide and the Rockstar description now live in part B (Personality, quoted verbatim) and the intro
states events only. The v2 "leaves with Uncle and Mary-Beth" is not kept: the departure is not shown, Dutch announces it
in "Our Best Selves" (uncle FIX_RULES). The v2 "voice and motion capture" claim is kept, attributed to the Red Dead
Wiki. The v2 GTA IV pedestrian claim is kept, attributed (Red Dead Wiki; GTA BOOM). The v2 SacAnime claim is dated
precisely (8 June 2019, from the listing of the panel video "Red Dead Redemption II Cast [SacAnime Summer 2019]";
video not watched, only the guest list and date are used). The v2 GTA VI claim is kept and dated (GTA BOOM, Ray
Ampoloquio, 11 June 2026). Chip "RDR2" replaced by the actor chip (game already in the facts grid). Eyebrow and
reg_role match characters_registry.py ("Gang cook &middot; RDR2"). publishDate 2026-08-23 kept (git: ca0326f,
"chore: drip-publish scheduled character (PUBLISHED simon-pearson)", 23 Aug 2026).

Sources (internal register, checked 20 Oct 2026):
- Red Dead Wiki "Jim Santangeli" (fetched via API 20 Oct 2026): American actor, writer and director, born 20 Dec
  1976 in Easton, Connecticut; known for Our Cartoon President and Paterno; cast as the voice and motion-capture actor
  for Pearson; voiced a pedestrian in Grand Theft Auto IV. Its trivia about his private life (wife's name, city) is
  not used.
- GTA BOOM, Ray Ampoloquio (updated by Matt Gibbs), "Who Is the First Confirmed Actor in GTA 6? Jim Santangeli Speaks
  Out", 11 June 2026: TikTok Live; role described as "a little small bit" and "some cool stuff, but small"; first
  publicly confirmed actor for the game; GTA IV pedestrian.
- SacAnime Summer 2019 panel "Red Dead Redemption II Cast", 8 June 2019, guests listed: Roger Clark, Rob Wiethoff,
  Steve J. Palmer, Peter Blomquist, Alex McKenna, Curzon Dobell, Gabriel Sloyer, Jim Santangeli (video listing).
- Wikipedia "List of Red Dead Redemption 2 characters": production section (motion capture, facial cameras; sessions
  from 2013, 2,200 days, 1,200 actors, 700 sharing 500,000 lines, per Vulture); Pearson section cites the guide
  (Price 2018, p. 376).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../uncle/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt): unused
  pants and sweater identical to the final ones; cut Horseshoe Overlook encounters cchr4 (Pearson and Charles on
  people too lazy to get food; Arthur answers "maybe") and cprs6 (hardtack, "a nautical thing"); poker with Pearson
  among cut activities; concept art of Bill, Karen, Tilly, Uncle, Mary-Beth, Strauss and Pearson; early photos,
  including Pearson's photo, show coach drivers seated on the right. Red Dead Wiki "Simon Pearson" gallery caption:
  hair model before and after the Day One patch.
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  27 Dec 2018 (../uncle/fc/gi_ranking.txt): Pearson 21st of 24, quoted verbatim.
- TheGamer, Jerrad Wyche, "Red Dead Redemption 2: Ranking The Van Der Linde Gang From Worst To First", 10 Aug 2019
  (simon/fcD/thegamer.txt): Pearson 5th of 10 (list counts down from 10, Micah, to 1, Arthur), quoted verbatim.
- Official guide page and Rockstar description of 6 Sep 2018: used in part B only.
- Facts grid: aunt Cathy ("Further Questions of Female Suffrage"), wife Ethel (Red Dead Wiki "Ethel Pearson", unseen,
  heard in the store); Rhodes general store in 1907 (Ending Credits, "American Venom" credits list, wiki "Rhodes General
  Store"); gang photo on the store wall (Ending Credits page).
Excluded: the Wikipedia photo caption (New York Game Awards 2019) as an event; Santangeli's resume link (struck through
on the wiki, not fetched); the wiki trivia on his wife and home city (private life, unverified); the GTA BOOM
remark that he has only played "the Miami one" (anecdote, not about Pearson); speculative fan pieces. No
interview in which Santangeli discusses the role in detail was found (searches 20 Oct 2026), so Development has no
Interviews subsection. Reception uses the two rankings found; Polygon's cliché piece does not discuss Pearson.
DUPLICATE ownership: actor, production context, cut content and concept art live HERE; parts B and C must not retell
them (C may still mention marketing artwork). The guide and Rockstar descriptions belong to part B; origins, the
Colter hunt, the parley, the departure and the 1907 store belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Pearson is played by Jim Santangeli, an American actor, writer and director. According to the Red Dead Wiki, he was born in 1976 in Easton, Connecticut, is known for the series Our Cartoon President and the film Paterno, and was cast as both the voice and the motion capture performer for Pearson. The wiki and GTA BOOM add that he had earlier voiced a pedestrian in Rockstar's Grand Theft Auto IV.",
              "Pearson est interprété par Jim Santangeli, acteur, scénariste et réalisateur américain. D'après le Red Dead Wiki, il est né en 1976 à Easton, dans le Connecticut, s'est fait connaître avec la série Our Cartoon President et le film Paterno, et assure à la fois la voix et la capture de mouvement du personnage. Le wiki et GTA BOOM précisent qu'il avait auparavant prêté sa voix à un passant dans Grand Theft Auto IV, autre jeu de Rockstar.")},
    {"h3": two("After the game", "Après le jeu")},
    {"p": two("On June 8, 2019, Santangeli took part in the Red Dead Redemption 2 cast panel at SacAnime Summer 2019 in Sacramento, with Roger Clark, Rob Wiethoff, Steve J. Palmer, Peter Blomquist, Alex McKenna, Curzon Dobell and Gabriel Sloyer.",
              "Le 8 juin 2019, Santangeli participe à la table ronde consacrée à la distribution de Red Dead Redemption 2 lors de la SacAnime Summer 2019, à Sacramento, aux côtés de Roger Clark, Rob Wiethoff, Steve J. Palmer, Peter Blomquist, Alex McKenna, Curzon Dobell et Gabriel Sloyer.")},
    {"p": two("During a TikTok livestream reported by GTA BOOM on June 11, 2026, he said he has a part in Grand Theft Auto VI, which he described as \"a little small bit\" and \"some cool stuff, but small\". In that article, Ray Ampoloquio called him the first publicly confirmed actor of the game at the time.",
              "Lors d'un direct sur TikTok rapporté par GTA BOOM le 11 juin 2026, il indique tenir un rôle dans Grand Theft Auto VI, qu'il décrit comme \"a little small bit\" (un tout petit rôle) et \"some cool stuff, but small\" (des choses sympas, mais modestes). Dans cet article, Ray Ampoloquio le présente comme le premier acteur du jeu confirmé publiquement à cette date.")},
    {"h3": two("Cut content and concept art", "Contenu coupé et illustrations")},
    {"p": two("The Red Dead Wiki lists unused trousers and a sweater for Pearson in the game files, identical to the ones he wears in the final game. Two camp encounters at Horseshoe Overlook were cut: in one, Pearson tells Charles how lazy some people are about bringing in food, then asks Arthur whether he will help, and Arthur says he might; in the other, Pearson warns Arthur that he may have to start serving hardtack, which Arthur has never heard of, and calls it a nautical thing Arthur would not understand. The same page lists a poker activity with Pearson among cut or reduced content.",
              "Le Red Dead Wiki recense dans les fichiers du jeu un pantalon et un pull inutilisés pour Pearson, identiques à ceux qu'il porte dans la version finale. Deux scènes de camp prévues à Horseshoe Overlook ont été coupées : dans l'une, Pearson se plaint auprès de Charles de la paresse de certains quand il s'agit de rapporter à manger, puis demande à Arthur s'il compte aider, et Arthur répond que ce n'est pas exclu ; dans l'autre, Pearson prévient Arthur qu'il devra peut-être servir du biscuit de mer, dont Arthur n'a jamais entendu parler, et lui explique que c'est une affaire de marins qu'il ne peut pas comprendre. La même page range une partie de poker avec Pearson parmi les contenus supprimés ou réduits.")},
    {"p": two("Concept art published by the wiki shows Pearson with Bill, Karen, Tilly, Uncle, Mary-Beth and Strauss. The wiki also publishes a comparison of his hair model before and after the game's day-one patch. On the gang photograph that hangs in his store in 1907, the coach driver sits on the right, a layout the wiki's cut content page traces to early development, before the driver's seat moved to the left.",
              "Une illustration conceptuelle publiée par le wiki montre Pearson avec Bill, Karen, Tilly, Uncle, Mary-Beth et Strauss. Le wiki publie aussi une comparaison de sa coiffure avant et après le correctif de lancement du jeu. Sur la photo de la bande accrochée dans son magasin en 1907, le cocher est assis à droite, une disposition que la page du wiki consacrée au contenu coupé fait remonter aux débuts du développement, avant que le siège du conducteur ne passe à gauche.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Rankings", "Classements")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on December 27, 2018, Pearson comes 21st. The entry says that, unlike the three members ranked below him, \"Pearson isn't awful. He's just kind of a dork\", and cites his letter to his aunt, which Sadie reads aloud and in which he lies about his accomplishments. It adds that he \"fulfills an important role: feeding everyone, which goes unappreciated by the whole gang\", but that \"Pearson's biggest crime is how uninteresting he is\".",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Pearson arrive 21e. Sa notice estime que, contrairement aux trois membres classés derrière lui, \"Pearson isn't awful. He's just kind of a dork\" (Pearson n'est pas affreux, juste un peu ringard), et cite sa lettre à sa tante, que Sadie lit à voix haute et où il ment sur ses réussites. Elle ajoute qu'il remplit un rôle important, nourrir tout le monde, sans que la bande lui en sache gré, mais que \"Pearson's biggest crime is how uninteresting he is\" (son plus grand crime, c'est d'être si peu intéressant).")},
    {"p": two("TheGamer places him fifth in a list of ten gang members by Jerrad Wyche, published on August 10, 2019. Wyche writes that Pearson first \"comes off as a whiny and needy man who just so happens to be the gang's cook\", that he is \"simply a man not cut out for this lifestyle\", and that he \"only becomes frustrated when his livelihood is directly at stake\".",
              "TheGamer le classe cinquième sur dix membres du gang, dans un article de Jerrad Wyche publié le 10 août 2019. Selon l'auteur, Pearson passe d'abord pour \"a whiny and needy man who just so happens to be the gang's cook\" (un geignard en mal d'attention qui se trouve être le cuisinier de la bande), mais n'est en fait \"simply a man not cut out for this lifestyle\" (qu'un homme pas fait pour cette vie), qui ne s'agace que lorsque sa subsistance est directement en jeu.")},
]


BASE = {
    "slug": "simon-pearson", "name": "Simon Pearson",
    "publishDate": "2026-08-23", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Gang cook &middot; RDR2", "reg_role_fr": "Cuisinier du gang &middot; RDR2",
    "gender": "Male", "death": None, "nationality": "American",
    "portrait_alt": two("Simon Pearson in Red Dead Redemption 2", "Simon Pearson dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Simon Pearson, cook and butcher of the Van der Linde gang in RDR2: former sailor, the O'Driscoll parley, his departure at Beaver Hollow and his Rhodes general store in 1907.",
                     "Simon Pearson, cuisinier et boucher du gang Van der Linde dans RDR2 : ancien marin, la trêve avec les O'Driscoll, son départ de Beaver Hollow et son magasin de Rhodes en 1907."),
    "og_desc": two("The complete reference on Simon Pearson: life, camp scenes, missions, quotes, development and reception.",
                   "La référence complète sur Simon Pearson : vie, scènes de camp, missions, citations, conception et accueil."),
    "schema_desc": two("Cook and butcher of the Van der Linde gang in 1899 and former sailor, who leaves the gang as it falls apart and runs the Rhodes general store by 1907, in Red Dead Redemption 2.",
                       "Cuisinier et boucher du gang Van der Linde en 1899, ancien marin, qui quitte la bande au moment de sa chute et tient le magasin général de Rhodes en 1907, dans Red Dead Redemption 2."),
    "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Cook", "Cuisinier"),
              two("Alive in 1907", "Vivant en 1907"),
              two("Voiced by <strong>Jim Santangeli</strong>", "Voix de <strong>Jim Santangeli</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Simon Pearson", "Simon Pearson")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1907", "Vivant en 1907")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Affiliation", "Affiliation"), "value": two("US Navy (formerly); Van der Linde gang (until 1899)", "Marine américaine (autrefois) ; gang Van der Linde (jusqu'en 1899)")},
        {"label": two("Role", "Rôle"), "value": two("Camp cook and butcher; shopkeeper in Rhodes by 1907", "Cuisinier et boucher du camp ; commerçant à Rhodes en 1907")},
        {"label": two("Family", "Famille"), "value": two("Aunt Cathy; wife Ethel (by 1907)", "Sa tante Cathy ; son épouse Ethel (en 1907)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Jim Santangeli (voice and motion capture)", "Jim Santangeli (voix et capture de mouvement)")},
    ],
    "intro": [
        two("Simon Pearson is a supporting character of Red Dead Redemption 2 (2018), set in 1899. He is the cook and butcher of the Van der Linde gang and a former sailor. With [[susan-grimshaw|Susan Grimshaw]], he sets up each of the gang's camps, and he sends [[arthur-morgan|Arthur Morgan]] out for meat. In \"Blessed are the Peacemakers\", during the Clemens Point chapter, he brings [[dutch-van-der-linde|Dutch]] an offer of a parley from the O'Driscolls, which turns out to be a trap. He is gone from Beaver Hollow by the start of \"Our Best Selves\", when Dutch calls him a coward. By 1907 he is married and runs the general store in Rhodes.",
            "Simon Pearson est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Ancien marin, il est le cuisinier et le boucher du gang Van der Linde. Avec [[susan-grimshaw|Susan Grimshaw]], il installe chacun des camps de la bande, et il envoie [[arthur-morgan|Arthur Morgan]] chercher de la viande. Dans \"Blessed are the Peacemakers\", pendant le chapitre de Clemens Point, il transmet à [[dutch-van-der-linde|Dutch]] une proposition de trêve des O'Driscoll, qui se révèle être un piège. Il a quitté Beaver Hollow au début de \"Our Best Selves\", quand Dutch le traite de lâche. En 1907, il est marié et tient le magasin général de Rhodes."),
        two("He is played by Jim Santangeli, an American actor.",
            "Il est interprété par Jim Santangeli, acteur américain."),
    ],
    "essentials": [
        two("The gang's cook and butcher: he runs the camp kitchen, crafts satchels and camp decorations, and plays the accordion.",
            "Cuisinier et boucher de la bande : il tient la cuisine du camp, fabrique sacoches et aménagements, et joue de l'accordéon."),
        two("At Colter, his warning that food is running out sends Arthur and [[charles-smith|Charles Smith]] on their first hunt in \"The Aftermath of Genesis\".",
            "À Colter, son avertissement sur le manque de vivres envoie Arthur et [[charles-smith|Charles Smith]] à leur première chasse, dans \"The Aftermath of Genesis\"."),
        two("In \"Blessed are the Peacemakers\" he brings back the O'Driscolls' offer of a parley, a trap that ends with Arthur's capture.",
            "Dans \"Blessed are the Peacemakers\", il rapporte l'offre de trêve des O'Driscoll, un piège qui se solde par la capture d'Arthur."),
        two("He leaves the gang at Beaver Hollow; in 1907 he runs the Rhodes general store, where a photograph of the gang hangs on the wall.",
            "Il quitte la bande à Beaver Hollow ; en 1907, il tient le magasin général de Rhodes, où une photo de la bande est accrochée au mur."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["susan-grimshaw", "uncle", "sadie-adler", "charles-smith"],
}
