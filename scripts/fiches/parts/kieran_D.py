"""Kieran Duffy, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026, medium tier).

His live page (characters/kieran-duffy/) was generated from the v2 entry in scripts/_enrich.py
(ENRICHED, "slug": "kieran-duffy"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the v2 intro placed his capture in "Old Friends" (correct, chapter 1) but said he was
"kept tied to a tree" only at Horseshoe Overlook: kept, now in part A. The v2 "voice and motion capture" claim
for Pico Alexander is NOT kept as a personal claim (no source names his motion capture); Development now says,
citing Wikipedia, that Rockstar recorded the cast's performances with motion capture. The v2 "Deceased" chip
duplicated "Died 1899" and is dropped. The official-guide line ("several members never fully accept him") moves to
part B (Personality, quoted verbatim from the guide page). Eyebrow and reg_role match characters_registry.py
("Van der Linde gang &middot; RDR2"). publishDate 2026-07-01 kept (git: 0c95592, "drip-publish scheduled character
(PUBLISHED kieran-duffy)", 1 Jul 2026).

Sources (internal register, checked 20 Oct 2026):
- Wikipedia, "Pico Alexander" (fetched 20 Oct 2026): born June 3, 1991, New York City; parents Magdalena Deskur and
  cinematographer Lukasz Jogalla, Polish immigrants from Krakow; Fiorello H. LaGuardia High School; BFA in acting,
  Rutgers University; A Most Violent Year (2014), Indignation (2016), War Machine and Home Again (2017), The Sky Is
  Everywhere (2022); Catch-22 (2019), Dickinson (season 2, 2021); "In 2018, he was featured in Rockstar Games' Red
  Dead Redemption 2, playing Kieran Duffy, a captured member of a rival gang." Red Dead Wiki "Pico Alexander"
  (kieran/fcB/Pico_Alexander.txt) gives the same birth date and place.
- Wikipedia, "List of Red Dead Redemption 2 characters" (../uncle/fc/wp_list_rdr2_characters.txt): Kieran section
  (Pico Alexander; stable boy; guide p. 380); production section (motion capture and facial cameras; recording from
  2013, 2,200 days, 1,200 actors, 700 of them sharing 500,000 lines, per Vulture).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../uncle/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt):
  cut hair model, shirt, coat and neckerchief; cut Colter stable encounter (file cnv_camp@rccol@cnv@cckie3) in which
  Kieran tries to get Jack to fetch him food and Arthur threatens to cut his throat; IGN pre-release playthrough:
  Kieran originally captured just before "Paying a Social Call" (also on the mission page).
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  27 Dec 2018 (../uncle/fc/gi_ranking.txt): Kieran 20th of 24, quoted verbatim.
- Official guide page (kieran/fcB/guide_bio.txt): used in part B only.
Excluded: the wiki's claim that Pico Alexander also plays a stranger attacked by wolves near Strawberry ("citation
needed"); the IGN video itself (not watched: the claim is attributed to the Red Dead Wiki); the wiki's explanation
that the cut timing "would explain the plot discrepancy" (interpretation, kept only as the wiki's own remark in
short form); the absence of a promotional quote artwork for Kieran (marketing trivia: part C); Saint Denis martyr
and Dullahan readings of his death (wiki speculation); "voice and motion capture" (no source); parents' names
beyond the Wikipedia citation (kept, sourced). No interview of Pico Alexander about the role was found
(searches 20 Oct 2026), so Development has no interview paragraph. Reception: only Game Informer found; no
review discussing Kieran by name was found in IGN, Polygon, Kotaku, PC Gamer or GamesRadar searches.
DUPLICATE ownership: actor, production context and cut content live HERE; parts B and C must not retell them. The
guide description belongs to part B; origins, capture, murder and burial belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Kieran is played by Pico Alexander, an American actor born in New York City on June 3, 1991. According to Wikipedia, his parents, Magdalena Deskur and the cinematographer Lukasz Jogalla, are Polish immigrants from Krakow. He attended Fiorello H. LaGuardia High School and earned a BFA in acting at Rutgers University. His film roles include A Most Violent Year (2014), Indignation (2016), War Machine and Home Again (2017) and The Sky Is Everywhere (2022). On television he had a recurring role in Catch-22 (2019) and played Henry \"Ship\" Shipley in the second season of Dickinson (2021). Wikipedia sums up his part in Red Dead Redemption 2 (2018) as Kieran Duffy, \"a captured member of a rival gang\". No interview in which he discusses the role has been found.",
              "Kieran est interprété par Pico Alexander, acteur américain né à New York le 3 juin 1991. D'après Wikipédia, ses parents, Magdalena Deskur et le directeur de la photographie Lukasz Jogalla, sont des immigrés polonais originaires de Cracovie. Il a fréquenté la Fiorello H. LaGuardia High School et obtenu une licence d'art dramatique (BFA) à l'université Rutgers. Au cinéma, on l'a vu notamment dans A Most Violent Year (2014), Indignation (2016), War Machine et Home Again (2017), puis The Sky Is Everywhere (2022). À la télévision, il a tenu un rôle récurrent dans Catch-22 (2019) et joué Henry \"Ship\" Shipley dans la deuxième saison de Dickinson (2021). Wikipédia résume son rôle dans Red Dead Redemption 2 (2018) : Kieran Duffy, \"a captured member of a rival gang\" (un membre capturé d'une bande rivale). Aucun entretien dans lequel il évoque ce rôle n'a été trouvé.")},
    {"p": two("Rockstar recorded the performances of the cast with motion capture, with cameras capturing the actors' facial expressions for animation, according to Wikipedia's list of the game's characters. The same page, citing Vulture, says recording began in 2013 and lasted 2,200 days, with 1,200 actors, 700 of whom share the game's 500,000 lines of dialogue.",
              "Rockstar a enregistré le jeu des acteurs en capture de mouvement, des caméras saisissant leurs expressions faciales pour l'animation, selon la liste des personnages du jeu sur Wikipédia. La même page, citant Vulture, indique que les enregistrements ont commencé en 2013 et se sont étalés sur 2 200 jours, avec 1 200 acteurs, dont 700 se partagent les 500 000 répliques du jeu.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("According to the Red Dead Wiki, the game files contain a cut hair model, shirt, coat and neckerchief for Kieran. They also hold an unused camp encounter at Colter, in which Kieran, held in the stable, tries to persuade Jack to fetch him food, and Arthur steps in and threatens to cut his throat if he speaks to the boy again. The wiki also reports that in IGN's playthrough of the game, shown a few months before release, Kieran was captured just before \"Paying a Social Call\" rather than at the end of chapter 1; the wiki notes that this order would explain how he knows where Colm is after weeks as a prisoner.",
              "D'après le Red Dead Wiki, les fichiers du jeu contiennent pour Kieran une coiffure, une chemise, un manteau et un foulard inutilisés. On y trouve aussi une scène de camp coupée, à Colter : Kieran, enfermé dans l'écurie, tente de convaincre Jack de lui apporter à manger, et Arthur intervient en menaçant de lui trancher la gorge s'il adresse encore la parole à l'enfant. Le wiki rapporte également que, dans la partie présentée par IGN quelques mois avant la sortie, Kieran était capturé juste avant \"Paying a Social Call\" et non à la fin du chapitre 1 ; il relève que cet ordre expliquerait comment Kieran sait où se trouve Colm après des semaines de captivité.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Game Informer ranking", "Le classement de Game Informer")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on 27 December 2018, Kieran comes 20th. The staff wrote that, as a former O'Driscoll trying to find his place in the gang, \"there's a lot of pathos in his struggle for acceptance\", and that \"that journey is cut short just as everyone starts to warm up to him, raising the stakes to take down Colm O'Driscoll.\" Wikipedia's list of the game's characters cites the same ranking for his description as a lowly member of the O'Driscoll gang.",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Kieran arrive 20e. La rédaction écrit que cet ancien O'Driscoll en quête de sa place dans la bande offre, dans sa lutte pour être accepté, \"a lot of pathos\" (beaucoup de pathétique), et que ce parcours s'interrompt au moment où tout le monde commence à l'apprécier, ce qui rend d'autant plus pressant d'abattre Colm O'Driscoll. La liste des personnages du jeu sur Wikipédia s'appuie sur ce même classement pour le présenter comme un membre subalterne de la bande des O'Driscoll.")},
]


BASE = {
    "slug": "kieran-duffy", "name": "Kieran Duffy",
    "publishDate": "2026-07-01", "updated": "2026-10-19", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": "American",
    "portrait_alt": two("Kieran Duffy in Red Dead Redemption 2", "Kieran Duffy dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Kieran Duffy, the captured O'Driscoll who joins the Van der Linde gang in RDR2: Six Point Cabin, life in camp, his murder by the O'Driscolls at Shady Belle in 1899, Pico Alexander.",
                     "Kieran Duffy, l'O'Driscoll capturé qui rejoint le gang Van der Linde dans RDR2 : Six Point Cabin, la vie au camp, son assassinat par les O'Driscoll à Shady Belle en 1899, Pico Alexander."),
    "og_desc": two("The complete reference on Kieran Duffy: life, missions, camp scenes, quotes, development and reception.",
                   "La référence complète sur Kieran Duffy : vie, missions, scènes de camp, citations, conception et accueil."),
    "schema_desc": two("Former O'Driscoll Boys member captured by the Van der Linde gang, who joins it after saving Arthur Morgan's life and is murdered by the O'Driscolls in 1899, in Red Dead Redemption 2.",
                       "Ancien membre des O'Driscoll Boys capturé par le gang Van der Linde, qu'il rejoint après avoir sauvé la vie d'Arthur Morgan, avant d'être assassiné par les O'Driscoll en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Van der Linde gang", "Gang Van der Linde"),
              two("Former O'Driscoll", "Ancien O'Driscoll"),
              two("Voiced by <strong>Pico Alexander</strong>", "Voix de <strong>Pico Alexander</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Kieran Duffy", "Kieran Duffy")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, killed by the O'Driscolls after the party for Jack's return; his body is sent back to Shady Belle in \"Horsemen, Apocalypses\"", "1899, tué par les O'Driscoll après la fête du retour de Jack ; son corps est renvoyé à Shady Belle dans \"Horsemen, Apocalypses\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased; his grave lies in the meadow west of Shady Belle", "Décédé ; sa tombe se trouve dans la prairie à l'ouest de Shady Belle")},
        {"label": two("Nationality", "Nationalité"), "value": two("American, of Irish descent according to the Red Dead Wiki; his father was an Irishman", "Américaine, d'origine irlandaise selon le Red Dead Wiki ; son père était irlandais")},
        {"label": two("Family", "Famille"), "value": two("Father and mother, both dead of cholera when he was young", "Un père et une mère, tous deux morts du choléra quand il était jeune")},
        {"label": two("Affiliation", "Affiliation"), "value": two("United States Army (former, by his own account), O'Driscoll Boys (former), Van der Linde gang", "Armée des États-Unis (ancien, selon ses dires), O'Driscoll Boys (ancien), gang Van der Linde")},
        {"label": two("Role", "Rôle"), "value": two("Looks after the gang's horses", "S'occupe des chevaux de la bande")},
        {"label": two("Horse", "Cheval"), "value": two("Branwen", "Branwen")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Pico Alexander", "Pico Alexander")},
    ],
    "intro": [
        two("Kieran Duffy is a supporting character of Red Dead Redemption 2 (2018), set in 1899. A former low-ranking member of the O'Driscoll Boys, he joins the Van der Linde gang. [[arthur-morgan|Arthur Morgan]] captures him in the first chapter. Threatened with castration by [[dutch-van-der-linde|Dutch van der Linde]], he leads Arthur, [[john-marston|John Marston]] and [[bill-williamson|Bill Williamson]] to an O'Driscoll hideout. There he saves Arthur's life, and he is allowed to stay with the gang, where he looks after the horses. In the fourth chapter, after the party for [[jack-marston|Jack]]'s return at Shady Belle, he is murdered by the O'Driscolls, who send his mutilated body back to the camp before attacking it.",
            "Kieran Duffy est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Ancien sous-fifre des O'Driscoll Boys, il rejoint le gang Van der Linde. [[arthur-morgan|Arthur Morgan]] le capture au premier chapitre. Menacé de castration par [[dutch-van-der-linde|Dutch van der Linde]], il conduit Arthur, [[john-marston|John Marston]] et [[bill-williamson|Bill Williamson]] jusqu'à une planque des O'Driscoll. Il y sauve la vie d'Arthur et obtient le droit de rester dans la bande, où il s'occupe des chevaux. Au quatrième chapitre, après la fête du retour de [[jack-marston|Jack]] à Shady Belle, il est assassiné par les O'Driscoll, qui renvoient son corps mutilé au camp avant de l'attaquer."),
        two("He is played by Pico Alexander, an American actor from New York.",
            "Il est interprété par Pico Alexander, acteur américain originaire de New York."),
    ],
    "essentials": [
        two("An O'Driscoll on the lowest rung of Colm's gang; [[arthur-morgan|Arthur]] lassoes him after the raid on Colm's camp in \"Old Friends\" and brings him back to Colter as a prisoner.",
            "O'Driscoll tout en bas de l'échelle dans la bande de Colm ; [[arthur-morgan|Arthur]] le prend au lasso après l'attaque du camp de Colm dans \"Old Friends\" et le ramène prisonnier à Colter."),
        two("Tied to a tree at Horseshoe Overlook, he gives up Six Point Cabin in \"Paying a Social Call\" when [[dutch-van-der-linde|Dutch]] orders [[bill-williamson|Bill]] to geld him, then shoots the O'Driscoll who has knocked Arthur down in the cabin.",
            "Attaché à un arbre à Horseshoe Overlook, il livre Six Point Cabin dans \"Paying a Social Call\" quand [[dutch-van-der-linde|Dutch]] ordonne à [[bill-williamson|Bill]] de le castrer, puis abat l'O'Driscoll qui a jeté Arthur à terre dans la cabane."),
        two("Accepted into the gang, he works with the horses, takes Arthur fishing and is left to guard Clemens Point with [[micah-bell|Micah]] while the others ride to Braithwaite Manor.",
            "Admis dans la bande, il s'occupe des chevaux, emmène Arthur pêcher et reste garder Clemens Point avec [[micah-bell|Micah]] pendant que les autres partent pour Braithwaite Manor."),
        two("He disappears after the party for [[jack-marston|Jack]]'s return. In \"Horsemen, Apocalypses\" his beheaded body rides into Shady Belle, just before the O'Driscolls attack the camp.",
            "Il disparaît après la fête du retour de [[jack-marston|Jack]]. Dans \"Horsemen, Apocalypses\", son corps décapité arrive à cheval à Shady Belle, juste avant l'attaque des O'Driscoll contre le camp."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["mary-beth-gaskill", "bill-williamson", "arthur-morgan", "colm-odriscoll"],
}
