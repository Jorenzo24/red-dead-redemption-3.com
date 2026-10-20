"""Karen Jones, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026, medium tier).

Her live page (characters/karen-jones/) was generated from the v2 entry in scripts/_enrich.py
(BATCH1, "slug": "karen-jones"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the v2 intro paraphrased the official guide ("skilled scam artist who enjoys the outlaw
life and looks out for the other women"); the guide now lives in part B (Personality, quoted verbatim) and the
intro states events only. The v2 line "She planned the job with Bill" is not kept as such: the camp scene shows
Karen's plan, with Bill brought in later (bill_B, Camp Events); the intro says she starts looking into the bank in chapter 2 (her scouting line is in Sodom), plans the job
with Bill (who says they were preparing it since Horseshoe) and robs it with him, Lenny and Arthur. Fact-check fixes
(20 Oct 2026): drinking dated from the Clemens Point chapter (Camp Events), not from Sean's death; Born uses Arthur's
"Mid twenties, blonde" (Polite Society transcript) with the wiki's mid-1870s attributed; US dates in EN; the generic
Vulture production figures trimmed from Casting; the "in Berryville" lyric slip merged here from part C Trivia.
The v2 "voice and motion capture" claim is kept, attributed to the Red Dead Wiki ("cast as the voice and
motion-capture actor"). The v2 GamesRadar paragraph is kept and dated precisely (7 March 2019, Rachel Weber), and
the Popternative claim is attributed to Wikipedia's summary (video not watched). Chip "RDR2" replaced by the actor
chip (game already in the facts grid). Eyebrow and reg_role match characters_registry.py ("Van der Linde gang
&middot; RDR2"). publishDate 2026-08-14 kept (git: ec727e8, "chore: drip-publish scheduled character (PUBLISHED
karen-jones)", 14 Aug 2026).

Sources (internal register, checked 20 Oct 2026):
- GamesRadar+, Rachel Weber, "Sisterhood, shotguns and slapping: Red Dead Redemption 2's cast talk around the
  virtual campfire", published 7 March 2019 (saved in ../abigail/fc/gr_sisterhood.txt): Armeniox's lines quoted
  verbatim ("beautiful emotional journey"; the scenes with Arthur; "really rare also to have my own time with
  Roger"); Penny O'Brien on Armeniox slapping her "in the face, twice".
- Popternative, Peter Roumeliotis, "Jo Armeniox talks about playing Karen Jones in Red Dead Redemption 2 and much
  more", video, 12 November 2019: NOT watched; used only through Wikipedia's summary in "List of Red Dead
  Redemption 2 characters" (Karen section, ref at 4:46: drew on an "angry, rebellious" side; enjoyed expressing
  strong emotions she would not normally show).
- GameFragger, Josh Wilding, interview with Kaili Vernoff, 21 Feb 2019 (../susan/fc/gamefragger.txt): Karen "is
  the one who will really mouth off to her"; she and Jo found "how far she could push me". Forbes, Heather Newman,
  12 Feb 2019 (../susan/fc/forbes.txt): Vernoff still speaks "almost daily" with Meeya Davis, Sam Strelitz and Jo
  Armeniox.
- Red Dead Wiki "Jo Armeniox" (born Megan Armeniox, Greensboro, North Carolina; voice and motion capture);
  TVmaze person page 15551 (fetched 20 Oct 2026: born 1983; TV credits Mercy, Boardwalk Empire, Blue Bloods, Body
  of Proof, Unforgettable, Chicago Med, Shades of Blue, Bull, City on a Hill; the years TVmaze shows are series
  premieres, so no episode years are given). The wiki gives 8 Aug 1983, TVmaze 9 Aug 1983: only the year is used.
- Wikipedia "List of Red Dead Redemption 2 characters": production section (motion capture, facial cameras; 2013,
  2,200 days, 1,200 actors, 700 sharing 500,000 lines, per Vulture).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (fetched 20 Oct 2026): two unused torsos, a loose blouse,
  hair and knickers; a cut item request listed as "Karen's book"; an unused camp encounter (file csn15.awc) in
  which Susan nervously tells the camp girls that Karen stormed off the night before after telling her to go to
  hell (the wiki's remark that its conditions may be impossible to meet is kept, attributed); concept art of
  Bill, Karen, Tilly, Uncle, Mary-Beth, Strauss and Pearson, and a gang concept piece in which Bill, Javier and
  Karen "appear to be present" (hedge kept). Wiki "Polite Society, Valentine Style" trivia: Karen's lyric mix-up
  was a genuine moment from the recording session, left in the game (transcript confirms the line "I messed it up").
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  27 Dec 2018 (../uncle/fc/gi_ranking.txt): Karen 14th of 24, quoted verbatim; the introduction's "lewd Karen".
- Official guide page and Rockstar description of 6 Sep 2018: used in part B only.
Excluded: IMDb items not read directly (403; only TVmaze and the Red Dead Wiki are used); a precise birth date
(sources disagree); film credits from search snippets only (Beautiful Dreamer, My Best Day, Dropout: not fetched);
the Wikipedia photo caption (New York Game Awards 2019) as an event; any reading of Armeniox's "on a boat and blew
up a building" as cut content (no source links it to cut missions; quoted as she said it); speculative fan pieces
on "where is Karen" (no outlet of record). No review discussing Karen by name was found beyond Game Informer
(searches 20 Oct 2026), so Reception has one paragraph.
DUPLICATE ownership: actor, interviews, production context, cut content and concept art live HERE; parts B and C
must not retell them (C may still mention marketing artwork). The guide and Rockstar descriptions belong to part B;
origins, the Valentine outing, the bank robbery, the departure and Tilly's letter belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Karen is played by Jo Armeniox, an American actress born in 1983; according to the Red Dead Wiki, her birth name is Megan Armeniox and she was born in Greensboro, North Carolina. The wiki says she was cast as both the voice and the motion capture performer for Karen. On television she has appeared in episodes of series including Mercy, Boardwalk Empire, Blue Bloods, Body of Proof, Unforgettable, Chicago Med, Shades of Blue, Bull and City on a Hill.",
              "Karen est interprétée par Jo Armeniox, actrice américaine née en 1983 ; d'après le Red Dead Wiki, elle est née Megan Armeniox, à Greensboro, en Caroline du Nord. Le wiki précise qu'elle assure à la fois la voix et la capture de mouvement du personnage. À la télévision, on l'a vue dans des épisodes de séries comme Mercy, Boardwalk Empire, Blue Bloods, Body of Proof, Unforgettable, Chicago Med, Shades of Blue, Bull ou City on a Hill.")},
    {"p": two("Rockstar recorded the cast's performances with motion capture, with cameras filming the actors' faces for animation, according to Wikipedia's list of the game's characters.",
              "Rockstar a enregistré le jeu des acteurs en capture de mouvement, des caméras filmant leurs visages pour l'animation, selon la liste des personnages du jeu sur Wikipédia.")},
    {"h3": two("Interviews", "Entretiens")},
    {"p": two("In a GamesRadar+ feature by Rachel Weber, published on March 7, 2019, in which the actresses of the gang look back on the shoot, Armeniox called her time with them \"a beautiful emotional journey\". She recalled scenes in which Karen and Arthur \"got wasted together, proclaimed our best friend love for each other, were on a boat and blew up a building together\", and said that, after so much work with the other women, \"it was really rare also to have my own time with Roger [Clark, who plays Arthur] and that was really special.\" In the same piece Penny O'Brien, who plays Molly O'Shea, says that catching up with Armeniox in the green room was one of her best memories, before a scene in which Armeniox had to slap her in the face twice.",
              "Dans un article de Rachel Weber publié par GamesRadar+ le 7 mars 2019, où les actrices du gang reviennent sur le tournage, Jo Armeniox décrit ce temps passé avec elles comme \"a beautiful emotional journey\" (un magnifique voyage émotionnel). Elle évoque des scènes où Karen et Arthur \"got wasted together, proclaimed our best friend love for each other, were on a boat and blew up a building together\" (se soûlaient ensemble, se juraient une amitié éternelle, partaient en barque et faisaient sauter un bâtiment), et ajoute qu'après tant de scènes avec les autres femmes, ses moments en tête-à-tête avec Roger Clark, l'interprète d'Arthur, étaient rares et \"really special\" (vraiment à part). Dans le même article, Penny O'Brien, l'interprète de Molly O'Shea, compte parmi ses meilleurs souvenirs ses retrouvailles avec Jo Armeniox en loge, juste avant une scène où celle-ci devait la gifler deux fois.")},
    {"p": two("Speaking to Peter Roumeliotis of Popternative in a video interview released on November 12, 2019, Armeniox said, as summarized by Wikipedia, that she drew on an \"angry, rebellious\" side of herself for Karen and enjoyed expressing strong emotions she would not usually show in real life.",
              "Dans une interview vidéo accordée à Peter Roumeliotis, de Popternative, et mise en ligne le 12 novembre 2019, Jo Armeniox explique, d'après le résumé qu'en donne Wikipédia, avoir puisé dans une part \"angry, rebellious\" (colérique et rebelle) d'elle-même pour jouer Karen, et avoir aimé exprimer des émotions fortes qu'elle ne montre pas d'ordinaire dans la vie.")},
    {"p": two("Kaili Vernoff, who plays Susan Grimshaw, told Josh Wilding of GameFragger in an interview published on February 21, 2019, that Susan and Karen \"have such a funny dynamic\", since Karen \"is the one who will really mouth off to her\". She said she and Armeniox had fun working out how far Karen could push Susan before Susan struck back. In an interview with Heather Newman of Forbes, published on February 12, 2019, Vernoff named Armeniox, Meeya Davis (Tilly) and Sam Strelitz (Mary-Beth) as the actresses she worked with most closely and said they still spoke \"almost daily\".",
              "Kaili Vernoff, l'interprète de Susan Grimshaw, explique à Josh Wilding, de GameFragger, dans un entretien publié le 21 février 2019, que Susan et Karen ont \"such a funny dynamic\" (une relation très drôle), Karen étant celle qui lui répond le plus effrontément. Elle raconte que Jo Armeniox et elle s'amusaient à chercher jusqu'où Karen pouvait pousser Susan avant que celle-ci ne riposte. Dans un entretien avec Heather Newman, de Forbes, publié le 12 février 2019, Vernoff cite Jo Armeniox, Meeya Davis (Tilly) et Sam Strelitz (Mary-Beth) comme les actrices avec qui elle a le plus travaillé, et dit qu'elles se parlent encore \"almost daily\" (presque tous les jours).")},
    {"h3": two("Recording and cut content", "Enregistrement et contenu coupé")},
    {"p": two("On the wagon ride of \"Polite Society, Valentine Style\", Karen sings \"in Berryville\" where the women's song has \"across the lane\", then says she messed it up. According to the Red Dead Wiki, this was a genuine slip during the recording session that was kept in the game.",
              "Pendant le trajet en chariot de \"Polite Society, Valentine Style\", Karen chante \"in Berryville\" là où la chanson des femmes dit \"across the lane\", puis reconnaît s'être emmêlée. D'après le Red Dead Wiki, il s'agit d'une vraie erreur commise pendant l'enregistrement, conservée telle quelle dans le jeu.")},
    {"p": two("The Red Dead Wiki lists unused assets for Karen in the game files: two torsos, a loose blouse, a hairstyle and knickers. The files also name a cut item request for \"Karen's book\". An unused camp encounter, set after she leaves the gang, has Susan nervously telling the camp's young women that Karen stormed off the night before after telling her to go to hell; the wiki notes that the scene's conditions may be impossible to meet, since Mary-Beth, who takes part in it, leaves at the same time as Karen. Concept art published by the wiki shows Karen with Bill, Tilly, Uncle, Mary-Beth, Strauss and Pearson, and she appears to be present, with Bill and Javier, in another concept piece of the gang.",
              "Le Red Dead Wiki recense des éléments inutilisés pour Karen dans les fichiers du jeu : deux bustes, un chemisier ample, une coiffure et une culotte. Les fichiers mentionnent aussi une commande d'objet abandonnée, intitulée \"Karen's book\" (le livre de Karen). Une scène de camp inutilisée, située après son départ, montre Susan annonçant, mal à l'aise, aux jeunes femmes du camp que Karen est partie furieuse la veille au soir après l'avoir envoyée au diable ; le wiki relève que la scène ne peut sans doute jamais se déclencher, puisque Mary-Beth, qui y participe, s'en va en même temps que Karen. Des illustrations conceptuelles publiées par le wiki montrent Karen avec Bill, Tilly, Uncle, Mary-Beth, Strauss et Pearson, et elle semble figurer, avec Bill et Javier, sur une autre illustration du gang.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Game Informer ranking", "Le classement de Game Informer")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on December 27, 2018, Karen comes 14th. The introduction of the piece lists \"lewd Karen\" among the game's memorable characters. Her entry calls her \"The lewdest, drunkest, most unapologetic member of the group\" and compares her to Pam Poovey, a character of the animated series Archer. The staff wrote that, whether she is acting out a part to distract the tellers during a bank robbery or arguing drunkenly with the rest of the gang, \"Karen steals every scene she's in\", and closed on her disappearance: \"Now if only we could figure out where the hell she went.\"",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Karen arrive 14e. L'introduction de l'article la range parmi les personnages marquants du jeu sous l'étiquette \"lewd Karen\" (Karen la grivoise). Sa notice en fait \"The lewdest, drunkest, most unapologetic member of the group\" (la plus grivoise, la plus soûle et la plus décomplexée de la bande) et la compare à Pam Poovey, un personnage de la série d'animation Archer. Pour la rédaction, qu'elle joue la comédie pour distraire les guichetiers pendant un braquage ou qu'elle se dispute, ivre, avec le reste du gang, \"Karen steals every scene she's in\" (Karen vole la vedette dans chacune de ses scènes) ; l'article conclut sur sa disparition, en regrettant de ne pas savoir où elle a bien pu passer.")},
]


BASE = {
    "slug": "karen-jones", "name": "Karen Jones",
    "publishDate": "2026-08-14", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Female", "death": None, "nationality": "American",
    "portrait_alt": two("Karen Jones in Red Dead Redemption 2", "Karen Jones dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Karen Jones, con artist of the Van der Linde gang in RDR2: the Valentine bank robbery, her night with Sean MacGuire, her drinking, and what Tilly writes in 1907.",
                     "Karen Jones, arnaqueuse du gang Van der Linde dans RDR2 : le braquage de la banque de Valentine, sa nuit avec Sean MacGuire, l'alcool et ce qu'en écrit Tilly en 1907."),
    "og_desc": two("The complete reference on Karen Jones: life, camp scenes, missions, quotes, development and reception.",
                   "La référence complète sur Karen Jones : vie, scènes de camp, missions, citations, conception et accueil."),
    "schema_desc": two("Con artist and gunwoman of the Van der Linde gang who plans the robbery of the Valentine bank in 1899 and leaves the gang as it falls apart, in Red Dead Redemption 2.",
                       "Arnaqueuse et femme de main du gang Van der Linde, qui monte le braquage de la banque de Valentine en 1899 et quitte la bande au moment de sa chute, dans Red Dead Redemption 2."),
    "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Con artist", "Arnaqueuse"),
              two("Fate unknown", "Sort inconnu"),
              two("Voiced by <strong>Jo Armeniox</strong>", "Voix de <strong>Jo Armeniox</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Karen Jones", "Karen Jones")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game (in 1899 Arthur describes her as in her mid-twenties; the Red Dead Wiki gives the mid-1870s)", "Non précisée dans le jeu (en 1899, Arthur lui donne environ vingt-cinq ans ; le Red Dead Wiki indique le milieu des années 1870)")},
        {"label": two("Status", "Statut"), "value": two("Unknown after 1899; in 1907 Tilly Jackson writes that she never heard what happened to her but believes drink killed her", "Inconnu après 1899 ; en 1907, Tilly Jackson écrit qu'elle n'a jamais su ce qu'elle était devenue, mais qu'elle croit que l'alcool l'a tuée")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang (until 1899)", "Gang Van der Linde (jusqu'en 1899)")},
        {"label": two("Role", "Rôle"), "value": two("Con artist and gunwoman", "Arnaqueuse et femme de main")},
        {"label": two("Horse", "Cheval"), "value": two("Old Belle", "Old Belle")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Jo Armeniox (voice and motion capture)", "Jo Armeniox (voix et capture de mouvement)")},
    ],
    "intro": [
        two("Karen Jones is a supporting character of Red Dead Redemption 2 (2018), set in 1899. She is a con artist and gunwoman of the Van der Linde gang. During the Horseshoe Overlook chapter she starts looking into the Valentine bank. She plans the job with [[bill-williamson|Bill Williamson]] and robs the bank with him, [[lenny-summers|Lenny Summers]] and [[arthur-morgan|Arthur Morgan]] in \"Sodom? Back to Gomorrah\", during the Clemens Point chapter. She has a brief affair with [[sean-macguire|Sean MacGuire]]. From the Clemens Point chapter onward she drinks more and more, and she leaves the gang at Beaver Hollow as it falls apart. Her fate is never shown: in 1907 [[tilly-jackson|Tilly Jackson]] writes that she believes drink killed her.",
            "Karen Jones est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Arnaqueuse et femme de main du gang Van der Linde, elle commence à s'intéresser à la banque de Valentine pendant le chapitre de Horseshoe Overlook. Elle prépare le coup avec [[bill-williamson|Bill Williamson]], puis braque la banque avec lui, [[lenny-summers|Lenny Summers]] et [[arthur-morgan|Arthur Morgan]] dans \"Sodom? Back to Gomorrah\", pendant le chapitre de Clemens Point. Elle a une brève liaison avec [[sean-macguire|Sean MacGuire]]. À partir du chapitre de Clemens Point, elle boit de plus en plus, et elle quitte la bande à Beaver Hollow, au moment où tout s'effondre. Son sort n'est jamais montré : en 1907, [[tilly-jackson|Tilly Jackson]] écrit qu'elle croit l'alcool responsable de sa mort."),
        two("She is played by Jo Armeniox, an American actress.",
            "Elle est interprétée par Jo Armeniox, actrice américaine."),
    ],
    "essentials": [
        two("A long-standing scam artist of the gang; according to the Red Dead Wiki, she robbed a bank in Tucson with [[arthur-morgan|Arthur]] and [[javier-escuella|Javier]] in the mid-1890s, dressed as a nun.",
            "Arnaqueuse de longue date du gang ; d'après le Red Dead Wiki, elle a braqué une banque à Tucson avec [[arthur-morgan|Arthur]] et [[javier-escuella|Javier]] au milieu des années 1890, déguisée en religieuse."),
        two("In \"Polite Society, Valentine Style\" a man she tries to rob at the Saints Hotel beats her before Arthur steps in; he had boasted about the town's bank, which becomes her next target.",
            "Dans \"Polite Society, Valentine Style\", un homme qu'elle tente de dépouiller au Saints Hotel la frappe avant qu'Arthur n'intervienne ; il s'était vanté de la banque de la ville, qui devient sa prochaine cible."),
        two("She robs the Valentine bank with [[bill-williamson|Bill]], [[lenny-summers|Lenny]] and Arthur in \"Sodom? Back to Gomorrah\", going in first as a lost girl or a drunken harlot.",
            "Elle braque la banque de Valentine avec [[bill-williamson|Bill]], [[lenny-summers|Lenny]] et Arthur dans \"Sodom? Back to Gomorrah\", en entrant la première, dans le rôle de la jeune fille égarée ou de la prostituée ivre."),
        two("She drinks more and more from the Clemens Point chapter onward; she turns on [[susan-grimshaw|Susan Grimshaw]] after [[molly-oshea|Molly]]'s death and is gone from Beaver Hollow by \"Our Best Selves\".",
            "À partir du chapitre de Clemens Point, elle boit de plus en plus ; elle s'en prend à [[susan-grimshaw|Susan Grimshaw]] après la mort de [[molly-oshea|Molly]], et a quitté Beaver Hollow avant \"Our Best Selves\"."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["tilly-jackson", "sean-macguire", "mary-beth-gaskill", "susan-grimshaw"],
}
