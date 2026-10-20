"""Orville Swanson, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026, medium tier).

His live page (characters/orville-swanson/) was generated from the v2 entry in scripts/_enrich.py (BATCH2,
"slug": "orville-swanson"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the v2 intro paraphrased Rockstar's description; that description now lives in part B
(Personality, quoted verbatim) and the intro states events only. The v2 "Davey Callahan" is corrected to Davey
Callander (transcript of "Outlaws from the West", wiki). The v2 claim that Haberle "provided the voice and the motion
capture" is kept, attributed to the Red Dead Wiki. The v2 Reception paragraph is kept, each source re-read and dated
precisely (Game Informer 27 Dec 2018; Polygon, Colin Campbell, 22 Nov 2018; GamesRadar+, Paul Walker-Emig, 1 Apr
2019). Chip "RDR2" replaced by the actor chip (game already in the facts grid). Eyebrow and reg_role match
characters_registry.py ("Gang chaplain &middot; RDR2" / "Aumônier du gang &middot; RDR2"). publishDate 2026-08-26 kept
(git: 31a1148, "chore: drip-publish scheduled character (PUBLISHED orville-swanson)", 26 Aug 2026).

Sources (internal register, checked 20 Oct 2026):
- Red Dead Wiki "Sean Haberle" (fetched through the API, orville/fcB/haberle_wiki.txt): born Sean Michael Haberle,
  July 3, 1963, Arlington, Virginia; American actor; "cast as the voice and motion-capture actor for Orville
  Swanson". Wikipedia "List of Red Dead Redemption 2 characters" (Reverend Swanson section, ../jack/fc/
  wp_List_of_Red_Dead_Redemption_2_characters.wiki): "Reverend Orville Swanson (Sean Haberle)"; production section
  (motion capture, facial cameras). Wiki infoboxes EN and FR also give Haberle. Two independent sources: CONFIRMED.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../abigail/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt):
  line 179 (cut arm, another arm, stomach, hair, half chaps; eyes originally blue; files HairEyeColor.PNG and
  Swansonchaps.PNG in the gallery); line 682 (Micah "God is dead" encounter, m15.awc); line 687 (four Colter
  encounters labeled "CCSW"); line 705 (drinking with Swanson among the cut or reduced activities); line 1203
  (concept art of Swanson, Grimshaw and Hosea).
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  December 27, 2018 (../uncle/fc/gi_ranking.txt, line 65-66; date per Wikipedia's citation and archive): Swanson
  17th, quoted verbatim.
- Polygon, Colin Campbell, "Red Dead Redemption 2's story is a confection of cowboy clichés", November 22, 2018
  (../susan/fc/polygon_campbell.txt, lines 60-62 byline and date, line 102): "Reverend Swanson is the drunken,
  self-loathing padre".
- GamesRadar+, Paul Walker-Emig, "How Red Dead Redemption 2 lays down a path to utopia", April 1, 2019 (archived
  copy of 1 Apr 2019, orville/fcB/gr_utopia.txt, line 43): "The community takes up the slack for addicts like Uncle
  and the Reverend Swanson (admittedly, with some reluctance), offering protection, providing shelter and meeting
  their basic needs".
- Official guide page and Rockstar description of 6 Sep 2018: used in part B only.
Excluded: Wikipedia's photo caption (New York Game Awards 2019) as an event; TV or stage credits for Haberle (TVmaze
has a person page, 21013, with no credits; IMDb not read: no list is given); any interview with Haberle about Swanson
(none found, searches 20 Oct 2026); the cut-content note on the higher class sleeping car used when Swanson boards
the train (a train asset, not Swanson content); the wiki's "Possibly" style readings. Reception has three sources,
no review discussing Swanson beyond them was found.
DUPLICATE ownership: actor, production context, cut content and concept art live HERE; parts B and C must not
retell them (part F of Arthur already quotes the cut "we're not alone" line for Arthur's fiche; here it is
paraphrased). The guide and Rockstar descriptions belong to part B; origins, the missions, the departure and the 1907
newspaper belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Swanson is played by Sean Haberle, an American actor. According to the Red Dead Wiki, his full name is Sean Michael Haberle and he was born on July 3, 1963, in Arlington, Virginia. The wiki says he was cast as both the voice and the motion capture performer for Swanson.",
              "Swanson est interprété par Sean Haberle, acteur américain. D'après le Red Dead Wiki, il s'appelle Sean Michael Haberle et il est né le 3 juillet 1963 à Arlington, en Virginie. Le wiki précise qu'il assure à la fois la voix et la capture de mouvement du personnage.")},
    {"p": two("Rockstar recorded the cast's performances with motion capture, with cameras filming the actors' faces for animation, according to Wikipedia's list of the game's characters.",
              "Rockstar a enregistré le jeu des acteurs en capture de mouvement, des caméras filmant leurs visages pour l'animation, selon la liste des personnages du jeu sur Wikipédia.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The Red Dead Wiki lists four camp encounters with Swanson that were cut from Colter, labeled \"CCSW\" in the game files. One shows him outside in the cold, refusing to come in and calling transubstantiation a heresy. In another, Arthur tries to wake him, and Swanson says he is awake and thinking that they are not alone. In a third, Arthur catches him injecting morphine; Swanson vomits as Arthur tries to stop him. In the last, woken again, he mourns beautiful things he once saw and that are now gone.",
              "Le Red Dead Wiki recense quatre scènes de camp avec Swanson coupées à Colter, identifiées par le code \"CCSW\" dans les fichiers du jeu. L'une le montre dehors, dans le froid, refusant de rentrer et traitant la transsubstantiation d'hérésie. Dans une autre, Arthur tente de le réveiller ; Swanson répond qu'il ne dort pas et qu'il songe au fait qu'ils ne sont pas seuls. Dans une troisième, Arthur le surprend en train de s'injecter de la morphine ; Swanson vomit pendant qu'Arthur essaie de l'en empêcher. Dans la dernière, réveillé une fois de plus, il pleure les belles choses qu'il a vues autrefois et qui ont disparu.")},
    {"p": two("Another unused encounter has Micah declare that God is dead, and Swanson assure him that he is wrong. The wiki also counts drinking with Swanson among the activities with gang members that were cut or reduced. In the files, Swanson has unused models for an arm, a second arm, a stomach, a hairstyle and half chaps, and his eyes were originally blue. Concept art published by the wiki shows him with Susan Grimshaw and Hosea.",
              "Une autre scène inutilisée montre Micah affirmer que Dieu est mort, et Swanson lui assurer qu'il se trompe. Le wiki range aussi les tournées de boisson avec Swanson parmi les sorties avec les membres du gang qui ont été supprimées ou réduites. Dans les fichiers, Swanson dispose de modèles inutilisés : un bras, un second bras, un ventre, une coiffure et des demi-jambières ; ses yeux étaient bleus à l'origine. Une illustration conceptuelle publiée par le wiki le montre avec Susan Grimshaw et Hosea.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Critical reception", "Accueil critique")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on December 27, 2018, Swanson comes 17th. The magazine calls him an interesting character in that \"he bounces back and forth between a wise man and fool\", giving useful advice to the gang as often as he needs rescuing from his drinking. It also singles out his campfire speech, which it gives as \"You've got to love yourself a fire\".",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Swanson arrive 17e. Le magazine le juge intéressant parce qu'il \"bounces back and forth between a wise man and fool\" (oscille sans cesse entre le sage et le fou), prodiguant au gang de bons conseils aussi souvent qu'il faut le tirer de ses beuveries. L'article salue aussi son discours au coin du feu, cité sous la forme \"You've got to love yourself a fire\".")},
    {"p": two("In a Polygon article published on November 22, 2018, Colin Campbell argues that the game's story is built from cowboy clichés. In his list of stock figures, \"Reverend Swanson is the drunken, self-loathing padre\".",
              "Dans un article de Polygon publié le 22 novembre 2018, Colin Campbell soutient que le scénario du jeu est un assemblage de clichés de western. Dans sa liste de personnages types, \"Reverend Swanson is the drunken, self-loathing padre\" (le révérend Swanson est le prêtre ivrogne qui se méprise).")},
    {"p": two("In a GamesRadar+ feature published on April 1, 2019, Paul Walker-Emig cites Swanson as an example of the gang's egalitarian side: \"The community takes up the slack for addicts like Uncle and the Reverend Swanson (admittedly, with some reluctance), offering protection, providing shelter and meeting their basic needs\".",
              "Dans un article de GamesRadar+ publié le 1er avril 2019, Paul Walker-Emig cite Swanson pour illustrer le côté égalitaire du gang : la communauté prend en charge des dépendants comme Uncle et le révérend Swanson, \"admittedly, with some reluctance\" (certes, avec une certaine réticence), en leur offrant protection et abri et en subvenant à leurs besoins essentiels.")},
]


BASE = {
    "slug": "orville-swanson", "name": "Orville Swanson",
    "publishDate": "2026-08-26", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Gang chaplain &middot; RDR2", "reg_role_fr": "Aumônier du gang &middot; RDR2",
    "gender": "Male", "death": None, "nationality": None,
    "portrait_alt": two("Reverend Orville Swanson in Red Dead Redemption 2", "Le révérend Orville Swanson dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Reverend Orville Swanson, the fallen clergyman of the Van der Linde gang in RDR2: his addictions, Arthur's rescue, his sobriety and his New York church in 1907.",
                     "Le révérend Orville Swanson, homme d'Église déchu du gang Van der Linde dans RDR2 : ses addictions, son sauvetage par Arthur, sa sobriété et son église new-yorkaise en 1907."),
    "og_desc": two("The complete reference on Reverend Swanson: life, camp scenes, missions, quotes, development and reception.",
                   "La référence complète sur le révérend Swanson : vie, scènes de camp, missions, citations, conception et accueil."),
    "schema_desc": two("Former clergyman of the Van der Linde gang, addicted to alcohol and morphine, who gets sober in 1899, leaves the gang before its collapse and becomes a minister in New York by 1907, in Red Dead Redemption 2.",
                       "Ancien homme d'Église du gang Van der Linde, dépendant à l'alcool et à la morphine, qui retrouve la sobriété en 1899, quitte la bande avant sa chute et devient pasteur à New York en 1907, dans Red Dead Redemption 2."),
    "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Reverend", "Révérend"),
              two("Alive in 1907", "Vivant en 1907"),
              two("Voiced by <strong>Sean Haberle</strong>", "Voix de <strong>Sean Haberle</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Orville Swanson", "Orville Swanson")},
        {"label": two("Also known as", "Autre nom"), "value": two("Reverend Swanson", "Révérend Swanson")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1907", "Vivant en 1907")},
        {"label": two("Nationality", "Nationalité"), "value": two("American according to the Red Dead Wiki", "Américaine selon le Red Dead Wiki")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang (until 1899); First Congregational Church of New York (1907)", "Gang Van der Linde (jusqu'en 1899) ; First Congregational Church de New York (1907)")},
        {"label": two("Role", "Rôle"), "value": two("Former clergyman; minister in New York by 1907", "Ancien homme d'Église ; pasteur à New York en 1907")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Sean Haberle (voice and motion capture)", "Sean Haberle (voix et capture de mouvement)")},
    ],
    "intro": [
        two("Reverend Orville Swanson is a supporting character of Red Dead Redemption 2 (2018), set in 1899. He is a former clergyman who travels with the Van der Linde gang and is addicted to alcohol and morphine. He speaks the game's first line, in the snowstorm that opens the story. During the Horseshoe Overlook chapter, [[arthur-morgan|Arthur Morgan]] finds him drunk at Flatneck Station and saves him from a train in \"Who is Not Without Sin\". At Shady Belle, Dutch has him bury [[kieran-duffy|Kieran Duffy]] with [[charles-smith|Charles Smith]] and [[simon-pearson|Simon Pearson]]. He is sober by the time Arthur returns from Guarma, and he leaves the gang at Beaver Hollow before its collapse. A 1907 in-game newspaper article reports that he has become minister of the First Congregational Church of New York.",
            "Le révérend Orville Swanson est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Ancien homme d'Église, il suit le gang Van der Linde et dépend de l'alcool et de la morphine. C'est lui qui prononce la première réplique du jeu, dans la tempête de neige qui ouvre l'histoire. Pendant le chapitre de Horseshoe Overlook, [[arthur-morgan|Arthur Morgan]] le retrouve ivre à Flatneck Station et le sauve d'un train dans \"Who is Not Without Sin\". À Shady Belle, Dutch le charge d'enterrer [[kieran-duffy|Kieran Duffy]] avec [[charles-smith|Charles Smith]] et [[simon-pearson|Simon Pearson]]. Il est sobre quand Arthur revient de Guarma, et il quitte le gang à Beaver Hollow, avant sa chute. En 1907, un article de presse annonce qu'il est devenu pasteur de la First Congregational Church de New York."),
        two("He is played by Sean Haberle, an American actor.",
            "Il est interprété par Sean Haberle, acteur américain."),
    ],
    "essentials": [
        two("A former clergyman addicted to alcohol and morphine; he once saved [[dutch-van-der-linde|Dutch]]'s life, which is why the gang keeps him.",
            "Ancien homme d'Église dépendant à l'alcool et à la morphine ; il a jadis sauvé la vie de [[dutch-van-der-linde|Dutch]], ce qui explique que le gang le garde."),
        two("In \"Who is Not Without Sin\" [[arthur-morgan|Arthur]] brings him back from Flatneck Station and pulls him off the tracks of Bard's Crossing just before a train passes.",
            "Dans \"Who is Not Without Sin\", [[arthur-morgan|Arthur]] le ramène de Flatneck Station et le tire des rails de Bard's Crossing juste avant le passage d'un train."),
        two("Sober by the time Arthur returns from Guarma, he leaves the gang at Beaver Hollow; Arthur may meet him a last time at Emerald Station.",
            "Sobre au retour d'Arthur de Guarma, il quitte le gang à Beaver Hollow ; Arthur peut le croiser une dernière fois à Emerald Station."),
        two("In 1907 a newspaper reports that he leads the First Congregational Church of New York.",
            "En 1907, un journal annonce qu'il dirige la First Congregational Church de New York."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["arthur-morgan", "dutch-van-der-linde", "hosea-matthews", "susan-grimshaw"],
}
