"""Josiah Trelawny, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026, medium tier).

His live page (characters/josiah-trelawny/) was generated from the v2 entry in scripts/_enrich.py
("slug": "josiah-trelawny"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the v2 intro paraphrased the official guide ("allowed to come and go from Dutch's gang as
he pleases"); the guide now lives in part B (Personality, quoted verbatim) and the intro states events only. The v2
"distracts an opera singer" referred to a "chanteur" in FR: Chester Damsen is a woman (Chester Damsen wiki page), so
the FR wording is feminine. The v2 Gevedon paragraph credited Oz and The Deuce without dates; dates and the other
recurring roles now follow Wikipedia's "Stephen Gevedon". The ComiCulture claims are attributed to Wikipedia's
summary (podcast not listened to) and dated precisely (14 October 2019, host Kevin Caldwell). The v2 Polygon line
paraphrased in FR; it is now quoted verbatim in both languages from the article itself, with its title and date.
A second Reception source (Game Informer ranking) is added. Chip "RDR2 & Online" replaced by the actor chip (games
already in the facts grid). Eyebrow and reg_role match characters_registry.py ("Van der Linde gang &middot; RDR2").
publishDate 2026-07-12 kept (git: e7af776, "chore: drip-publish scheduled character (PUBLISHED josiah-trelawny)",
12 Jul 2026). nationality stays None (the games never state it; the wiki's "British" rests on his own claim to be
from Cornwall, which he admits he has never seen).

Sources (internal register, checked 20 Oct 2026):
- Wikipedia "Stephen Gevedon" (fetched 20 Oct 2026, saved in josiah/fcD/wp_gevedon.txt): American actor; recurring
  roles in Oz (1997), Show Me a Hero (2015), Madoff (2016), The Deuce (2017 to 2018); co-wrote Session 9 (2001)
  with Brad Anderson and plays Mike in it; portrays Trelawny through performance capture.
- Wikipedia "List of Red Dead Redemption 2 characters" (fetched 20 Oct 2026, josiah/fcD/wp_list.txt), Trelawny
  section, citing the podcast ComiCulture BEYOND, "Steve J Palmer, Stephen Gevedon, and Dana Schwartz", Kevin
  Caldwell, 14 Oct 2019: did not know the project was a game; expected about a week of recording; told Trelawny
  dressed better and acted more professionally than the others but was "rough around the edges"; accent a "bad
  Katharine Hepburn", partly because he was uncomfortable doing a true English accent around the British crew and
  partly to keep the character mysterious; Rockstar liked the performance and expanded the role; wife and children
  added in the final years of development. Podcast NOT listened to: everything is attributed to Wikipedia's summary.
- Polygon, Colin Campbell, "Red Dead Redemption 2 is a confection of cowboy clichés", 22 Nov 2018 (fetched from
  polygon.com 20 Oct 2026, excerpt in josiah/fcD/polygon_excerpt.txt): "Josiah Trelawny is an affectatious dandy,
  a gentleman thief with swell togs and a crisp English accent." (the same passage names Susan, Sadie, Strauss and Swanson).
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  27 Dec 2018 (../uncle/fc/gi_ranking.txt, line 86-87): Trelawny 8th of 24, quoted verbatim.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../jack/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt):
  cut clothing (sleeveless union suit, three vests, two ties, pants, a torso, legs, boots); cut item request
  (Eagle Talon); cut chapter 3 mission "tre2" given by Trelawny (Arthur and Dutch against bounty hunters on a train,
  "from Boston" per Benjamin Byron Davis in an interview, as in dutch_D); unused Nial Whelan; the cut camp encounter
  with Micah (file ctrl2.awc: "rat", "snake", coral snake from the hat, as in micah_D); the Double-Action revolver
  prop for the gun hand-over scene of "A Fine Night of Debauchery"; concept art (cane, National Museum of Scotland
  display; group art of Sean, Trelawny, Sadie, Lenny and Micah, as in lenny_D and sean_D). Character page trivia:
  custom short-barrel Double-Action with a white grip (wiki screenshot).
- Official guide page and Rockstar description of 6 Sep 2018: used in part B only.
Excluded: the cut-content page's remark that Charles mentions a cane Trelawny is never seen with (the cane is
found in "Magicians for Sport"); the National Museum of Scotland display as a dated event (no date given); the
spelling "Trelawney" in the files (part B, Names); Gevedon's film credits beyond Session 9 (not needed); any
reading of the late addition of the family as a story decision (only the fact, as summarized). No other review
discussing Trelawny by name was found (searches 20 Oct 2026), so Reception has two paragraphs.
DUPLICATE ownership: actor, interview, production context, cut content and concept art live HERE; parts B and C
must not retell them (C may still mention marketing artwork and Red Dead Online). The guide and Rockstar
descriptions, names and appearance belong to part B; the events (Sean, prison wagon, kidnapping, stagecoach,
riverboat, departure) belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Trelawny is played by Stephen Gevedon, an American actor, through performance capture. He co-wrote the horror film Session 9 (2001) with its director, Brad Anderson, and plays Mike in it. On television he has had recurring roles in Oz (1997), Show Me a Hero (2015), Madoff (2016) and The Deuce (2017 to 2018).",
              "Trelawny est interprété par Stephen Gevedon, acteur américain, en capture de performance. Il a coécrit le film d'horreur Session 9 (2001) avec son réalisateur, Brad Anderson, et y joue le rôle de Mike. À la télévision, il a eu des rôles récurrents dans Oz (1997), Show Me a Hero (2015), Madoff (2016) et The Deuce (2017 à 2018).")},
    {"h3": two("Interview", "Entretien")},
    {"p": two("Gevedon talked about the role on the podcast ComiCulture BEYOND, hosted by Kevin Caldwell, in an episode released on October 14, 2019. According to Wikipedia's summary of that episode, he did not know when he was cast that the project was a video game, and expected the recording to take about a week. He was told that Trelawny was unlike the other gang members, better dressed and more professional, but still \"rough around the edges\".",
              "Gevedon a parlé du rôle dans le podcast ComiCulture BEYOND, animé par Kevin Caldwell, dans un épisode mis en ligne le 14 octobre 2019. D'après le résumé qu'en donne Wikipédia, il ignorait, au moment du casting, qu'il s'agissait d'un jeu vidéo, et pensait que l'enregistrement durerait environ une semaine. On lui a présenté Trelawny comme différent des autres membres de la bande, mieux habillé et plus professionnel, mais encore un peu brut de décoffrage (\"rough around the edges\").")},
    {"p": two("He described Trelawny's accent as a \"bad Katharine Hepburn\". He chose it partly because he did not feel comfortable doing a true English accent in front of the British crew, and partly to keep the character mysterious. Rockstar liked his performance enough to expand the role, and Trelawny's wife and children, kept secret in the game, were added in the last years of development.",
              "Il décrit l'accent de Trelawny comme une \"bad Katharine Hepburn\" (une mauvaise imitation de Katharine Hepburn). Il l'a choisi en partie parce qu'il n'était pas à l'aise à l'idée de prendre un véritable accent anglais devant l'équipe britannique, en partie pour garder au personnage son mystère. Rockstar a tant apprécié sa prestation que le rôle a été étoffé, et la femme et les enfants de Trelawny, gardés secrets dans le jeu, ont été ajoutés dans les dernières années du développement.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("According to the Red Dead Wiki, a chapter 3 mission named \"tre2\" in the files was to be given by Trelawny. It had Arthur and Dutch fighting bounty hunters on a train; Benjamin Byron Davis, who plays Dutch, said in an interview that they came from Boston. Animations for the mission show the pair hiding in a bar car, and an unused character, Nial Whelan, being thrown out of a window by Arthur.",
              "D'après le Red Dead Wiki, une mission du chapitre 3, baptisée \"tre2\" dans les fichiers, devait être confiée par Trelawny. Arthur et Dutch y affrontaient des chasseurs de primes à bord d'un train ; Benjamin Byron Davis, l'interprète de Dutch, a précisé en interview qu'ils venaient de Boston. Des animations de la mission montrent les deux hommes cachés dans une voiture-bar, et un personnage inutilisé, Nial Whelan, jeté par une fenêtre par Arthur.")},
    {"p": two("A camp encounter with Micah Bell was also recorded and left out. Micah calls Trelawny a rat, then a snake; Trelawny tells him to look in his hat, and a coral snake falls out of it, to Micah's alarm. The files hold a custom Double-Action revolver for Trelawny, which the wiki describes as short-barreled with a white grip, meant for a cutscene of \"A Fine Night of Debauchery\". They also contain unused clothes for him (a sleeveless union suit, three vests, two ties, trousers, boots) and a cut item request for an eagle talon.",
              "Une scène de camp avec Micah Bell a aussi été enregistrée, puis écartée. Micah y traite Trelawny de rat, puis de serpent ; Trelawny lui conseille de regarder dans son chapeau, d'où tombe un serpent corail, au grand effroi de Micah. Les fichiers contiennent un revolver Double-Action personnalisé pour Trelawny, à canon court et crosse blanche selon le wiki, prévu pour une cinématique de \"A Fine Night of Debauchery\". On y trouve aussi des vêtements inutilisés (une combinaison sans manches, trois gilets, deux cravates, un pantalon, des bottes) et une commande d'objet abandonnée : une serre d'aigle.")},
    {"p": two("Concept art shown by the wiki pictures Trelawny with a walking cane, and another piece groups him with Sean, Sadie, Lenny and Micah.",
              "Une illustration conceptuelle publiée par le wiki montre Trelawny avec une canne, et une autre le réunit avec Sean, Sadie, Lenny et Micah.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Critics", "La critique")},
    {"p": two("In an opinion piece published by Polygon on November 22, 2018, \"Red Dead Redemption 2 is a confection of cowboy clichés\", Colin Campbell listed Trelawny among the gang's stock characters: \"Josiah Trelawny is an affectatious dandy, a gentleman thief with swell togs and a crisp English accent.\" The same passage also names Susan Grimshaw, Sadie Adler, Leopold Strauss and Reverend Swanson.",
              "Dans une tribune publiée par Polygon le 22 novembre 2018, \"Red Dead Redemption 2 is a confection of cowboy clichés\" (Red Dead Redemption 2, une confiserie de clichés de cow-boys), Colin Campbell range Trelawny parmi les personnages types de la bande : \"Josiah Trelawny is an affectatious dandy, a gentleman thief with swell togs and a crisp English accent.\" (Josiah Trelawny est un dandy affecté, un gentleman cambrioleur aux beaux habits et à l'accent anglais impeccable). Le même passage cite aussi Susan Grimshaw, Sadie Adler, Leopold Strauss et le révérend Swanson.")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on December 27, 2018, Trelawny comes 8th. The staff called him \"one of the most interesting members of the gang\" and \"A smooth-talking trickster who comes and goes as he pleases\". They noted that the gang often has to rescue him, but that he pays them back \"with helpful tips and distractions\", and said that players who find his secret in Saint Denis \"are in for a big surprise\".",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Trelawny arrive 8e. La rédaction le juge \"one of the most interesting members of the gang\" (l'un des membres les plus intéressants de la bande) et le décrit comme un filou beau parleur qui va et vient à sa guise. Elle relève que la bande doit souvent le tirer d'affaire, mais qu'il la rembourse en tuyaux et en diversions, et promet une belle surprise aux joueurs qui découvrent son secret à Saint-Denis.")},
]


BASE = {
    "slug": "josiah-trelawny", "name": "Josiah Trelawny",
    "publishDate": "2026-07-12", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Male", "death": None, "nationality": None,
    "portrait_alt": two("Josiah Trelawny in Red Dead Redemption 2", "Josiah Trelawny dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Josiah Trelawny, conman and magician of the Van der Linde gang in RDR2: Sean's rescue, the stagecoach and riverboat jobs, his secret family and his departure.",
                     "Josiah Trelawny, escroc et magicien du gang Van der Linde dans RDR2 : le sauvetage de Sean, la diligence, le bateau à aubes, sa famille cachée et son départ."),
    "og_desc": two("The complete reference on Josiah Trelawny: life, camp scenes, missions, quotes, development and reception.",
                   "La référence complète sur Josiah Trelawny : vie, scènes de camp, missions, citations, conception et accueil."),
    "schema_desc": two("Conman and magician who comes and goes from the Van der Linde gang in 1899, finds its leads and leaves for good as it falls apart, in Red Dead Redemption 2.",
                       "Escroc et magicien qui va et vient dans le gang Van der Linde en 1899, lui trouve ses coups et le quitte pour de bon au moment de sa chute, dans Red Dead Redemption 2."),
    "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Con man", "Escroc"),
              two("Fate unknown", "Sort inconnu"),
              two("Voiced by <strong>Stephen Gevedon</strong>", "Voix de <strong>Stephen Gevedon</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Josiah Trelawny", "Josiah Trelawny")},
        {"label": two("Origin", "Origine"), "value": two("Cornwall, by his own account to Uncle, though he admits he has never been there; the Red Dead Wiki lists him as British, born in Cornwall", "Les Cornouailles, d'après ce qu'il dit à Uncle, tout en avouant n'y être jamais allé ; le Red Dead Wiki le présente comme britannique, né en Cornouailles")},
        {"label": two("Status", "Statut"), "value": two("Alive when he leaves the gang in 1899; afterward he can only be heard at his Saint Denis home", "En vie quand il quitte le gang en 1899 ; ensuite, on ne fait plus que l'entendre chez lui, à Saint-Denis")},
        {"label": two("Family", "Famille"), "value": two("A wife and two sons in Saint Denis (Tarquin and Cornelius, per the Red Dead Wiki)", "Une épouse et deux fils à Saint-Denis (Tarquin et Cornelius, selon le Red Dead Wiki)")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang (comes and goes, until 1899)", "Gang Van der Linde (par intermittence, jusqu'en 1899)")},
        {"label": two("Role", "Rôle"), "value": two("Conman and magician", "Escroc et magicien")},
        {"label": two("Horse", "Cheval"), "value": two("Gwydion", "Gwydion")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2, Red Dead Online", "Red Dead Redemption 2, Red Dead Online")},
        {"label": two("Voiced by", "Voix"), "value": two("Stephen Gevedon (performance capture)", "Stephen Gevedon (capture de performance)")},
    ],
    "intro": [
        two("Josiah Trelawny is a supporting character of Red Dead Redemption 2 (2018), set in 1899, and a stranger who gives missions in Red Dead Online. He is a conman and magician who comes and goes from the Van der Linde gang. During the Horseshoe Overlook chapter he brings word that bounty hunters hold [[sean-macguire|Sean MacGuire]] and helps [[arthur-morgan|Arthur Morgan]] and [[javier-escuella|Javier Escuella]] free him. During the Clemens Point chapter he is released from a sheriff's prison wagon after Arthur recaptures an escaped prisoner, Arthur and [[charles-smith|Charles Smith]] rescue him from bounty hunters, and he and Arthur rob a stagecoach together. In Saint Denis he plans the robbery of the riverboat Grand Korrigan. He leaves the gang for good at Beaver Hollow, with Arthur's blessing.",
            "Josiah Trelawny est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899, et un inconnu qui confie des missions dans Red Dead Online. Escroc et magicien, il va et vient dans le gang Van der Linde. Pendant le chapitre de Horseshoe Overlook, il apprend à la bande que des chasseurs de primes détiennent [[sean-macguire|Sean MacGuire]] et aide [[arthur-morgan|Arthur Morgan]] et [[javier-escuella|Javier Escuella]] à le libérer. Pendant le chapitre de Clemens Point, il sort d'un fourgon de prisonniers après qu'Arthur a rattrapé un évadé, Arthur et [[charles-smith|Charles Smith]] l'arrachent à des chasseurs de primes, puis Arthur et lui attaquent ensemble une diligence. À Saint-Denis, il monte le braquage du bateau à aubes Grand Korrigan. Il quitte la bande pour de bon à Beaver Hollow, avec la bénédiction d'Arthur."),
        two("He is played by Stephen Gevedon, an American actor.",
            "Il est interprété par Stephen Gevedon, acteur américain."),
    ],
    "essentials": [
        two("He finds the gang its leads: Sean's whereabouts after Blackwater, a stagecoach tipster in Rhodes and a high-stakes poker game on a riverboat.",
            "C'est lui qui trouve les pistes de la bande : l'endroit où Sean est retenu après Blackwater, un indicateur des diligences à Rhodes et une partie de poker à gros enjeux sur un bateau à aubes."),
        two("He relies on acting rather than force: he fakes a fit to distract bounty hunters and gets an opera singer to sing while [[arthur-morgan|Arthur]] empties her coach.",
            "Il mise sur la comédie plutôt que sur la force : il simule une crise pour distraire des chasseurs de primes et fait chanter une chanteuse d'opéra pendant qu'[[arthur-morgan|Arthur]] vide sa diligence."),
        two("He has a wife and two sons in Saint Denis; Arthur, who did not know he was married, hears them through an apartment door.",
            "Il a une épouse et deux fils à Saint-Denis ; Arthur, qui ignorait qu'il était marié, les entend derrière la porte d'un appartement."),
        two("He leaves Beaver Hollow for good in \"The Fine Art of Conversation\", after Arthur tells him not to come back.",
            "Il quitte Beaver Hollow pour de bon dans \"The Fine Art of Conversation\", après qu'Arthur lui a dit de ne pas revenir."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["arthur-morgan", "dutch-van-der-linde", "charles-smith", "leopold-strauss"],
}
