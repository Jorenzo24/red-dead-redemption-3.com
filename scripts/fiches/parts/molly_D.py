"""Molly O'Shea, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026, medium tier).

Her live page (characters/molly-oshea/) was generated from the v2 pilot entry in scripts/_enrich.py
(ENRICHED, "slug": "molly-oshea", fact-checked 6 Oct 2026); the base below is rebuilt from that entry, with
corrections. publishDate 2026-07-13 kept (git: d589bcf, "chore: drip-publish scheduled character (PUBLISHED
molly-oshea)", 13 Jul 2026). Eyebrow and reg_role match characters_registry.py ("Van der Linde gang &middot; RDR2").
Changes from the v2 page:
- The v2 intro quoted the Rockstar description; descriptions now live in part B (Personality) only, and the intro
  states events only.
- v2 "A grave for Molly exists in the game files" (FR: "une tombe au nom de Molly"): the Red Dead Wiki's cut content
  page says the grave is unmarked, does not bear her name and sits under the map near Beaver Hollow; corrected.
- v2 "In 2019 interviews ... with the instruction to play a 'really Irish' accent": the sources are now named
  (Long Beach Comic Con panel, 1 Sep 2019; Bionic Buzz, 3 Sep 2019; The Nerd Soapbox, 4 Sep 2019), all through
  Wikipedia's summary, since the videos were not watched.
- v2 "a process directed by Rod Edge": Edge is named by the AADA article as the director she worked with, and by
  Wikipedia as the game's motion capture director; worded accordingly.
- "Origin" fact kept (Dublin), now attributed to Rockstar and the official guide; the guide says she CLAIMS a
  well-to-do family (part B), so the wealth is not stated as fact anywhere.
- Chip "Deceased" merged into "Died 1899"; the actor chip added, as on the other v3 fiches.
Fact-check fixes (20 Oct 2026): AADA "2012 graduate" with no campus (no "New York"); "the shoot", not "each shoot";
the "really Irish" audition point attributed to Wikipedia's summary of the LBCC panel (no quotation marks, video not
watched); "about three years" attributed to The Nerd Soapbox (Wikipedia and the Penny O'Brien wiki page cite it there);
intro quarrels named with Karen only; essentials: Karen clashes from Horseshoe Overlook (Camp Events l.106), Dutch
quarrels from Clemens Point; crime fact kept only in Camp life (part B, attributed to the Swanson wiki page); cut
content no longer repeats "never on horseback" (Trivia owns it).

Sources (internal register, checked 20 Oct 2026):
- American Academy of Dramatic Arts, "Alumna Penny O'Brien Brings Her Character To Life in Red Dead Redemption 2",
  9 April 2019 (fetched 20 Oct 2026): from County Wicklow, youngest of four; 2012 graduate; first motion capture
  experience; Molly absent from the first game, "I got to build her from scratch"; secrecy, script given shortly
  before shooting; almost a year before she felt she was discovering Molly; Rod Edge "amazing at pulling a
  primal-like performance out of an actor"; freedom to change what felt uncharacteristic; "Molly is a very
  desperate character set in very extreme circumstances".
- Red Dead Wiki "Penny O'Brien" (molly/fcB/wiki_Penny_O_Brien.txt): Penelope Jane O'Brien; voice and motion
  capture; about three years on the game starting 2015 (citing The Nerd Soapbox).
- Wikipedia, "List of Red Dead Redemption 2 characters" (../uncle/fc/wp_list_rdr2_characters.txt, Molly section and
  refs): audition on Saint Patrick's Day 2015 (Bionic Buzz, LBCC interview, 3 Sep 2019; The Nerd Soapbox, 4 Sep
  2019); "really Irish" accent and personality, had not played the first game, watched videos after being cast,
  director talking to each actor separately before an argument scene, Molly not redeemed (LBCC panel "Bringing Red
  Dead Redemption 2 Life!", 1 Sep 2019); final moments as a cry for help (Nerd Soapbox). Production context: 2013,
  2,200 days, Rod Edge as motion capture director (Vulture, per Wikipedia).
- GamesRadar+, Rachel Weber, "Sisterhood, shotguns and slapping", 7 March 2019 (../abigail/fc/gr_sisterhood.txt):
  O'Brien on Benjamin Byron Davis ("some jokes that were made while we were in our tent that we'll still make
  together when we're sitting at dinner. I'm always perpetually darning his socks."); green room with Jo Armeniox,
  slapped "in the face, twice".
- TheGamer, Cian Maher, "Cowboys, Craic, And Guinness: How Red Dead 2's Irish Cast Became Family", 20 Jan 2021
  (fetched 20 Oct 2026), reporting the Origin Theatre First Irish Festival panel "Irish Redemption: An Irish
  Invasion of Video Games" (first shown 15 Jan 2021): worked with Origin Theatre before; Clark "one of those Irish
  theatre lads"; humor easy to play, "the lyricism and musicality"; the Sean cutscene (looks down her nose).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../uncle/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt,
  lines 164, 356, 635, 643, 1205): "The Gilded Cage" outfit (META_OUTFIT_GALA) and cut dialogue for the mission;
  two shirts, a torso, hair, a coat and two blankets unused; generic horse-riding lines; unmarked grave near Beaver
  Hollow (dis_roa_00_molly_grave), under the map; concept art of Charles, Molly and Javier.
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  27 Dec 2018 (../uncle/fc/gi_ranking.txt): Molly 18th of 24, quoted verbatim.
- MeinMMO, Tarek Zehrer, "5 der tragischsten Charaktere aus eurer Gang in Red Dead Redemption 2", 30 May 2021
  (fetched 20 Oct 2026): Molly among the five.
Excluded: the EverybodyWiki birth date (17 Dec 1990: not a reliable source); IMDb (not read); O'Brien's remark on
working-class Ireland as she summarized it on the LBCC panel beyond Wikipedia's wording; the Nerd Soapbox puppet
video itself (not watched); the "pants and leg models" item of the cut content page (shared by many characters, no
Molly-specific value); fan-site or content-farm pieces on Molly found by search (no outlet of record).
DUPLICATE ownership: actor, interviews, production context, cut content (outfit, dialogue, riding lines, grave,
concept art) live HERE; part C Trivia must not repeat the cut Gilded Cage outfit, the unused grave or the riding
lines (C may keep "never seen riding a horse" as an in-game observation without the files). The guide and Rockstar
descriptions belong to part B; origins, the Beaver Hollow claim and death, Milton's revelation belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Molly is played by Penny O'Brien, an Irish actress from County Wicklow whose full name, according to the Red Dead Wiki, is Penelope Jane O'Brien. She is a 2012 graduate of the American Academy of Dramatic Arts. The Red Dead Wiki says she was cast as both the voice and the motion capture performer for Molly. In an article published by the academy on April 9, 2019, she said it was her first motion capture job, as it was for many other actors on the game.",
              "Molly est interprétée par Penny O'Brien, actrice irlandaise originaire du comté de Wicklow, dont le nom complet est Penelope Jane O'Brien selon le Red Dead Wiki. Elle est diplômée de l'American Academy of Dramatic Arts, promotion 2012. D'après le Red Dead Wiki, elle assure à la fois la voix et la capture de mouvement du personnage. Dans un article publié par l'académie le 9 avril 2019, elle explique que c'était sa première expérience de capture de mouvement, comme pour beaucoup d'autres acteurs du jeu.")},
    {"p": two("According to Wikipedia's list of the game's characters, which cites two interviews of September 2019 (Bionic Buzz and The Nerd Soapbox), her audition took place on Saint Patrick's Day 2015. According to Wikipedia's summary of a Long Beach Comic Con panel on September 1, 2019, she was asked to audition with a really Irish accent and personality, and she had not played the first game but watched videos of it once she got the part. She told The Nerd Soapbox that she worked on the game for about three years. She told the academy that Molly's absence from the first game let her build the character from scratch.",
              "D'après la liste des personnages du jeu sur Wikipédia, qui s'appuie sur deux interviews de septembre 2019 (Bionic Buzz et The Nerd Soapbox), elle passe son audition le jour de la Saint-Patrick 2015. Selon le résumé que Wikipédia donne d'une table ronde du Long Beach Comic Con, le 1er septembre 2019, on lui avait demandé pour l'audition un accent et un tempérament franchement irlandais ; elle n'avait pas joué au premier jeu, mais en a regardé des vidéos une fois le rôle obtenu. Elle a confié à The Nerd Soapbox avoir travaillé sur le jeu pendant environ trois ans. Elle confie à l'académie que l'absence de Molly dans le premier opus lui a permis de construire le personnage de zéro.")},
    {"h3": two("Shooting and performance", "Tournage et interprétation")},
    {"p": two("In the April 2019 academy article, O'Brien described a production kept secret, in which the actors did not get the full script until shortly before the shoot. It took her almost a year of work to feel she was discovering Molly. She credited the director Rod Edge, the game's motion capture director, as \"amazing at pulling a primal-like performance out of an actor\", and said the cast was free to rework anything that felt out of character. She called Molly \"a very desperate character set in very extreme circumstances\".",
              "Dans l'article de l'académie d'avril 2019, Penny O'Brien décrit une production tenue secrète, où les acteurs n'ont eu accès au texte complet que peu avant le tournage. Il lui a fallu près d'un an de travail pour avoir le sentiment de découvrir Molly. Elle salue le réalisateur Rod Edge, directeur de la capture de mouvement du jeu, \"amazing at pulling a primal-like performance out of an actor\" (doué pour tirer d'un acteur un jeu presque primitif), et précise que la troupe pouvait retravailler tout ce qui sonnait faux pour un personnage. Elle qualifie Molly de \"very desperate character set in very extreme circumstances\" (personnage aux abois, plongé dans des circonstances extrêmes).")},
    {"p": two("At the Long Beach panel, as summarized by Wikipedia, she explained that before one of Molly's arguments with Dutch the director spoke to each actor separately about their character's motives without telling the other, and that Benjamin Byron Davis's in-character indifference frustrated her all the more. She said Molly finds no redemption: she had left Ireland to escape its hardships, and tying herself to Dutch cost her that chance. Speaking to The Nerd Soapbox, she said she played Molly's final scene as a cry for help and a plea for Dutch's attention.",
              "Lors de la table ronde de Long Beach, d'après le résumé qu'en donne Wikipédia, elle raconte qu'avant l'une des disputes entre Molly et Dutch, le réalisateur a parlé séparément à chaque acteur des motivations de son personnage, sans rien en dire à l'autre, et que l'indifférence jouée par Benjamin Byron Davis l'a d'autant plus exaspérée. Pour elle, Molly ne trouve aucune rédemption : elle avait quitté l'Irlande pour fuir la dureté de la vie là-bas, et en se liant à Dutch, elle s'est privée de cette chance. Devant The Nerd Soapbox, elle explique avoir joué la dernière scène de Molly comme un appel au secours et une supplique pour attirer l'attention de Dutch.")},
    {"h3": two("Interviews", "Entretiens")},
    {"p": two("In a GamesRadar+ feature by Rachel Weber, published on March 7, 2019, O'Brien said that she spent much of the shoot with Benjamin Byron Davis, who plays Dutch, and that their friendship has lasted: \"some jokes that were made while we were in our tent that we'll still make together when we're sitting at dinner. I'm always perpetually darning his socks.\" One of her best memories was catching up with Jo Armeniox, who plays Karen Jones, in the green room before a scene in which Armeniox had to slap her in the face twice.",
              "Dans un article de Rachel Weber publié par GamesRadar+ le 7 mars 2019, Penny O'Brien raconte avoir passé une grande partie du tournage avec Benjamin Byron Davis, l'interprète de Dutch, et que leur amitié a survécu au jeu : certaines plaisanteries nées sous leur tente de tournage reviennent encore quand ils dînent ensemble, et elle dit passer son temps à \"darning his socks\" (repriser ses chaussettes). L'un de ses meilleurs souvenirs : ses retrouvailles en loge avec Jo Armeniox, l'interprète de Karen Jones, juste avant une scène où celle-ci devait la gifler deux fois.")},
    {"p": two("On January 15, 2021, O'Brien, Roger Clark (Arthur) and Michael Mellamphy (Sean MacGuire) appeared in \"Irish Redemption: An Irish Invasion of Video Games\", an online panel of Origin Theatre's First Irish Festival, reported by Cian Maher for TheGamer on January 20, 2021. O'Brien said she had worked with Origin Theatre before, and that when she was cast she immediately spotted Clark as \"one of those Irish theatre lads\". She said the humor of the writing was easy to play because it is something they grew up with, \"the lyricism and musicality\". She and Mellamphy both recalled a cutscene in which Molly looks down her nose at Sean.",
              "Le 15 janvier 2021, Penny O'Brien, Roger Clark (Arthur) et Michael Mellamphy (Sean MacGuire) participent à \"Irish Redemption: An Irish Invasion of Video Games\", une table ronde en ligne du First Irish Festival de l'Origin Theatre, dont Cian Maher rend compte pour TheGamer le 20 janvier 2021. Penny O'Brien y explique avoir déjà travaillé avec l'Origin Theatre et avoir tout de suite repéré en Roger Clark \"one of those Irish theatre lads\" (un de ces gars du théâtre irlandais) quand elle a obtenu le rôle. L'humour de l'écriture, dit-elle, était facile à jouer, parce qu'ils ont grandi avec, avec \"the lyricism and musicality\" (le lyrisme et la musicalité) qui l'accompagnent. Mellamphy et elle se souviennent tous deux d'une cinématique où Molly toise Sean de haut.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The Red Dead Wiki lists unused material for Molly in the game files. She has an outfit made for \"The Gilded Cage\", the party at the mayor's mansion in Saint Denis, and cut dialogue tied to that mission, which suggests she was once meant to take part in it. The files also hold two unused shirts, a torso, a hairstyle, a coat and two blankets, as well as generic lines for riding a horse. Instead of having her body burned, the developers first planned to bury her in an unmarked grave near Beaver Hollow; the grave is still in the files, under the map, and does not bear her name. Concept art published by the wiki shows Molly with Charles and Javier.",
              "Le Red Dead Wiki recense des éléments inutilisés pour Molly dans les fichiers du jeu. Elle dispose d'une tenue prévue pour \"The Gilded Cage\", la réception au manoir du maire de Saint-Denis, et de répliques coupées liées à cette mission, ce qui laisse penser qu'elle devait y participer. Les fichiers contiennent aussi deux chemisiers, un buste, une coiffure, un manteau et deux couvertures inutilisés, ainsi que des répliques génériques prévues pour les trajets à cheval. Plutôt que de faire brûler son corps, les développeurs avaient d'abord prévu de l'enterrer dans une tombe anonyme près de Beaver Hollow ; la tombe existe toujours dans les fichiers, sous la carte, et ne porte pas son nom. Une illustration conceptuelle publiée par le wiki montre Molly aux côtés de Charles et de Javier.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Critical commentary", "Regards critiques")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on December 27, 2018, Molly comes 18th. The staff wrote that she gets little time as anything more than \"someone begging for Dutch's approval and failing to find it\". They added that the \"stomach-churning scene\" in which she drunkenly claims a betrayal she probably did not commit and is shot by Susan Grimshaw \"is one of the game's biggest moments\".",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Molly arrive 18e. Pour la rédaction, elle n'existe guère qu'en femme qui quémande l'approbation de Dutch sans jamais l'obtenir. L'article ajoute que la scène, \"stomach-churning\" (à vous retourner l'estomac), où, ivre, elle revendique une trahison qu'elle n'a probablement pas commise avant d'être abattue par Susan Grimshaw, \"is one of the game's biggest moments\" (compte parmi les grands moments du jeu).")},
    {"p": two("The German site MeinMMO included her in a list of the five most tragic characters of the gang, by Tarek Zehrer, published on May 30, 2021. The piece recalls her line to Arthur that Dutch is all the company she needs, her drunken confession and her death, and notes that the story later shows she never betrayed the gang.",
              "Le site allemand MeinMMO la fait figurer parmi les cinq personnages les plus tragiques de la bande, dans un article de Tarek Zehrer publié le 30 mai 2021. Le texte rappelle sa réplique à Arthur, pour qui Dutch serait sa seule compagnie nécessaire, sa confession d'ivrogne et sa mort, et souligne que l'histoire révèle plus tard qu'elle n'a jamais trahi le gang.")},
]


BASE = {
    "slug": "molly-oshea", "name": "Molly O'Shea",
    "publishDate": "2026-07-13", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Female", "death": "1899", "nationality": "Irish",
    "portrait_alt": two("Molly O'Shea in Red Dead Redemption 2", "Molly O'Shea dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Molly O'Shea, Dutch van der Linde's Irish companion in RDR2: her life in camp, her false confession at Beaver Hollow, her death and how Agent Milton clears her.",
                     "Molly O'Shea, compagne irlandaise de Dutch van der Linde dans RDR2 : sa vie au camp, son faux aveu à Beaver Hollow, sa mort et sa réhabilitation par l'agent Milton."),
    "og_desc": two("The complete reference on Molly O'Shea: life, camp scenes, missions, quotes, development and reception.",
                   "La référence complète sur Molly O'Shea : vie, scènes de camp, missions, citations, conception et accueil."),
    "schema_desc": two("Irish companion of Dutch van der Linde in the Van der Linde gang, shot dead by Susan Grimshaw in 1899 after falsely claiming to have informed the Pinkertons, in Red Dead Redemption 2.",
                       "Compagne irlandaise de Dutch van der Linde au sein du gang Van der Linde, abattue par Susan Grimshaw en 1899 après avoir faussement prétendu renseigner les Pinkerton, dans Red Dead Redemption 2."),
    "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Dutch's companion", "Compagne de Dutch"),
              two("Died <strong>1899</strong>", "Morte en <strong>1899</strong>"),
              two("Voiced by <strong>Penny O'Brien</strong>", "Voix de <strong>Penny O'Brien</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Molly O'Shea", "Molly O'Shea")},
        {"label": two("Origin", "Origine"), "value": two("Dublin, Ireland (Rockstar description and official guide)", "Dublin, Irlande (description de Rockstar et guide officiel)")},
        {"label": two("Died", "Mort"), "value": two("1899, Beaver Hollow (shot by Susan Grimshaw)", "1899, Beaver Hollow (abattue par Susan Grimshaw)")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédée")},
        {"label": two("Nationality", "Nationalité"), "value": two("Irish", "Irlandaise")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang", "Gang Van der Linde")},
        {"label": two("Relationship", "Relation"), "value": two("[[dutch-van-der-linde|Dutch van der Linde]] (companion)", "[[dutch-van-der-linde|Dutch van der Linde]] (compagne)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Penny O'Brien (voice and motion capture)", "Penny O'Brien (voix et capture de mouvement)")},
    ],
    "intro": [
        two("Molly O'Shea is a supporting character of Red Dead Redemption 2 (2018), set in 1899. A young Irishwoman from Dublin, she is the companion of [[dutch-van-der-linde|Dutch van der Linde]] and lives in his tent, apart from the work of the camp. As the gang moves from camp to camp, Dutch grows distant and she quarrels with him and with [[karen-jones|Karen Jones]]. She disappears after the failed Saint Denis bank robbery. At Beaver Hollow she returns drunk and claims in front of everyone that she informed the Pinkertons, and [[susan-grimshaw|Susan Grimshaw]] shoots her dead. Agent [[andrew-milton|Andrew Milton]] later tells [[arthur-morgan|Arthur Morgan]] that she never talked.",
            "Molly O'Shea est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Jeune Irlandaise de Dublin, elle est la compagne de [[dutch-van-der-linde|Dutch van der Linde]] et vit sous sa tente, à l'écart des tâches du camp. Au fil des déménagements de la bande, Dutch prend ses distances, et elle se dispute avec lui comme avec [[karen-jones|Karen Jones]]. Elle disparaît après l'échec du braquage de la banque de Saint-Denis. À Beaver Hollow, elle revient ivre et affirme devant tout le monde avoir renseigné les Pinkerton ; [[susan-grimshaw|Susan Grimshaw]] l'abat sur-le-champ. L'agent [[andrew-milton|Andrew Milton]] révélera plus tard à [[arthur-morgan|Arthur Morgan]] qu'elle n'a jamais parlé."),
        two("She is played by Penny O'Brien, an Irish actress.",
            "Elle est interprétée par Penny O'Brien, actrice irlandaise."),
    ],
    "essentials": [
        two("Dutch's companion since before 1899; according to an official guide, she says she comes from a well-to-do Irish family.",
            "Compagne de Dutch depuis avant 1899 ; d'après un guide officiel, elle se dit issue d'une famille irlandaise aisée."),
        two("The only woman of the camp who refuses all chores.",
            "Seule femme du camp à refuser toute corvée."),
        two("From the Clemens Point chapter she argues with Dutch, who ignores her more and more. She clashes repeatedly with [[karen-jones|Karen Jones]], from Horseshoe Overlook onward.",
            "À partir du chapitre de Clemens Point, elle se dispute avec Dutch, qui l'ignore de plus en plus. Dès Horseshoe Overlook, elle se heurte à plusieurs reprises à [[karen-jones|Karen Jones]]."),
        two("Shot by Susan at Beaver Hollow after claiming she talked to the Pinkertons; Milton later reveals that the informer was [[micah-bell|Micah Bell]].",
            "Abattue par Susan à Beaver Hollow après avoir prétendu parler aux Pinkerton ; Milton révèle ensuite que l'informateur était [[micah-bell|Micah Bell]]."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["dutch-van-der-linde", "susan-grimshaw", "karen-jones", "arthur-morgan"],
}
