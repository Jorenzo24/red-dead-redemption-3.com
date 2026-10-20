"""Mary-Beth Gaskill, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026,
medium tier).

Her live page (characters/mary-beth-gaskill/) was generated from the v2 entry in scripts/_enrich.py
(ENRICHED, "slug": "mary-beth-gaskill"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the v2 intro quoted the Rockstar description ("which makes her the perfect criminal");
the descriptions now live in part B (Personality, quoted verbatim) and the intro states events only. The v2
"Long Beach native based in New York" is kept and now attributed to its source (Long Beach Post, 29 Aug 2019,
read in the Wayback Machine copy of 31 Aug 2019). The v2 GamesRadar paragraph is kept and dated precisely (7 March
2019, Rachel Weber). The v2 Game Informer paragraph is kept, with the date (27 Dec 2018) and verbatim quotes. The
v2 "voice and motion capture" claim is attributed to the Red Dead Wiki. Chip "RDR2" replaced by the actor chip (game
already in the facts grid). Eyebrow and reg_role match characters_registry.py ("Van der Linde gang &middot; RDR2").
publishDate 2026-08-20 kept (git: b576e33, "chore: drip-publish scheduled character (PUBLISHED mary-beth-gaskill)",
20 Aug 2026).

Sources (internal register, checked 20 Oct 2026):
- Long Beach Post, Steve Lowery, "PODCAST: Red Dead Redemption 2's Samantha Strelitz (Mary-Beth Gaskill) and Long
  Beach Comic Con", episode 13 of "Can You Hear Me, Long Beach?", 29 Aug 2019 (page text read via
  web.archive.org/web/20190831035733, saved in mary/fcB/lbarch.html): "a Long Beach native", "now lives in New
  York", the making of the game "led to an additional career as a gaming commentator", Long Beach Comic Con (31
  Aug to 1 Sep 2019) a first for her. The audio was NOT heard: her "gets lost in the world of her books" is used
  only through Wikipedia's summary.
- Wikipedia "List of Red Dead Redemption 2 characters" (Mary-Beth section, saved in ../uncle/fc/
  wp_list_rdr2_characters.txt): summaries of The Nerd Soapbox (3 Sep 2019: worked on the game around three to four
  years), We're All Psychos Podcast no. 28 (Dylan Palladino, 15 Mar 2019: "the Danielle Steel of 1899"),
  the Long Beach Comic Con panel "Bringing Red Dead Redemption 2 Life!: The Performance Capture
  Panel" with Penny O'Brien and Steve J. Palmer, 1 Sep 2019 (reference list). None of these videos was watched;
  each is attributed to Wikipedia's summary. Production context (motion capture, facial cameras).
- GamesRadar+, Rachel Weber, "Sisterhood, shotguns and slapping: Red Dead Redemption 2's cast talk around the
  virtual campfire", 7 March 2019 (../abigail/fc/gr_sisterhood.txt): both Strelitz quotes verbatim (the scene with
  Kaili Vernoff, "about vanity and it's about ageing"; the illness scene, "such an innocence").
- GameFragger, Josh Wilding, interview with Kaili Vernoff, 21 Feb 2019 (../susan/fc/gamefragger.txt): the mirror
  scene ("Time will get you too and they'll stop looking."). Forbes, Heather Newman, 12 Feb 2019
  (../susan/fc/forbes.txt): Vernoff still speaks "almost daily" with Meeya Davis, Sam Strelitz and Jo Armeniox.
- Red Dead Wiki "Samantha Strelitz" (born 19 Oct 1986; DieRy and Vinyl; cast as voice and motion-capture actor);
  TVmaze person 117802 (fetched 20 Oct 2026: guest credit in "Pilot" of Vinyl, aired 14 Feb 2016). Only the
  birth year is used.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../javier/fc/wk_Red_Dead_Redemption_2_Cut_Content.txt):
  three unused hairstyles, a head model and two eyelash models; a cut item request "as" (meaning unknown); the
  unused Karen encounter in which Mary-Beth takes part; concept art of Bill, Karen, Tilly, Uncle, Mary-Beth,
  Strauss and Pearson.
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  27 Dec 2018 (../uncle/fc/gi_ranking.txt): Mary-Beth 13th of 24, quoted verbatim.
- Facts grid: Arthur's guess "21 or 22" and her rebuke are from the Red Dead Wiki trivia (no transcript), kept here
  only (part B does not repeat them). Mother's death of typhoid: official guide (part B quotes the page).
Excluded: the wiki's 2014 Golden Egg Film Festival nomination for "Circles" (wiki only, no outlet read); a birth
place (IMDb not read directly; search snippets say Los Angeles, the Long Beach Post says Long Beach native: not
contradictory but not needed); a precise birth date (single source); the Diane Lane outfit and the Leslie A.
Dupont nod (wiki speculation, "may have been", "possibly"); the reading of Strelitz's scene with Vernoff as the
mirror scene (the two interviews do not say they are the same scene: they are given side by side, not merged);
the Popternative summary (Wikipedia's "reflects her personality" is ambiguous: hers or the
character's); any other review: no review discussing Mary-Beth by name was found beyond Game Informer (searches 20 Oct 2026),
so Reception has one paragraph.
DUPLICATE ownership: actor, interviews, production context and cut content live HERE; parts B and C must not
retell them. The Rockstar and guide descriptions belong to part B; origins, missions, the departure, the 1907
encounter and Tilly's letter belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Mary-Beth is played by Samantha Strelitz, an American actress born in 1986 according to the Red Dead Wiki, which says she was cast as both the voice and the motion capture performer for the character. On television she appeared in the pilot episode of the HBO series Vinyl, aired in February 2016; the wiki also credits her in DieRy. In an episode of the Long Beach Post podcast \"Can You Hear Me, Long Beach?\", published on August 29, 2019, Steve Lowery presented her as a Long Beach native who now lives in New York, and noted that the game had led her to a second career as a gaming commentator. That weekend she made her first appearance at Long Beach Comic Con, where on September 1, 2019 she sat on a performance capture panel with Penny O'Brien (Molly O'Shea) and Steve J. Palmer (Bill Williamson).",
              "Mary-Beth est interprétée par Samantha Strelitz, actrice américaine née en 1986 selon le Red Dead Wiki, qui précise qu'elle assure à la fois la voix et la capture de mouvement du personnage. À la télévision, on l'a vue dans le pilote de la série Vinyl, sur HBO, diffusé en février 2016 ; le wiki la crédite aussi dans DieRy. Dans un épisode du podcast du Long Beach Post \"Can You Hear Me, Long Beach?\", publié le 29 août 2019, Steve Lowery la présente comme une enfant de Long Beach installée à New York, et relève que le jeu lui a ouvert une seconde carrière de commentatrice de jeux vidéo. Le week-end suivant, elle fait sa première apparition au Long Beach Comic Con, où elle participe le 1er septembre 2019 à une table ronde sur la capture de performance avec Penny O'Brien (Molly O'Shea) et Steve J. Palmer (Bill Williamson).")},
    {"p": two("Rockstar recorded the cast's performances with motion capture, with cameras filming the actors' faces for animation, according to Wikipedia's list of the game's characters. The same list, summarizing a video interview with The Nerd Soapbox published on September 3, 2019, says Strelitz worked on the game for around three to four years.",
              "Rockstar a enregistré le jeu des acteurs en capture de mouvement, des caméras filmant leurs visages pour l'animation, selon la liste des personnages du jeu sur Wikipédia. Cette même liste, qui résume une interview vidéo accordée à The Nerd Soapbox et mise en ligne le 3 septembre 2019, indique que Samantha Strelitz a travaillé sur le jeu pendant trois à quatre ans environ.")},
    {"h3": two("Interviews", "Entretiens")},
    {"p": two("Wikipedia's list of the game's characters summarizes several of her interviews. On the Long Beach Post podcast she described Mary-Beth as a sweet girl who \"gets lost in the world of her books\". On the We're All Psychos Podcast, in an episode released on March 15, 2019, she called her \"the Danielle Steel of 1899\" because of her love of romance novels.",
              "La liste des personnages du jeu sur Wikipédia résume plusieurs de ses entretiens. Dans le podcast du Long Beach Post, elle décrit Mary-Beth comme une jeune femme douce qui \"gets lost in the world of her books\" (se perd dans l'univers de ses livres). Dans le We're All Psychos Podcast, dans un épisode mis en ligne le 15 mars 2019, elle la surnomme \"the Danielle Steel of 1899\" (la Danielle Steel de 1899), en raison de sa passion pour les romans sentimentaux.")},
    {"p": two("In a GamesRadar+ feature by Rachel Weber, published on March 7, 2019, in which the actresses of the gang look back on the shoot, Strelitz singled out a scene she played with Kaili Vernoff, who plays Susan Grimshaw: \"it's about vanity and it's about ageing and it's about these two women struggling with how they connect with each other, and how they connect with women.\" She also said she is \"always very overwhelmed\" when she sees the scene in which Arthur tells Mary-Beth that he is dying. Part of her wished she had known, while shooting it, how much the scene would weigh for players, she said, while another part loved \"such an innocence to that scene\", asking: \"if someone tells you that how do you even take that all in?\"",
              "Dans un article de Rachel Weber publié par GamesRadar+ le 7 mars 2019, où les actrices du gang reviennent sur le tournage, Samantha Strelitz retient une scène jouée avec Kaili Vernoff, l'interprète de Susan Grimshaw, une scène qui parle, dit-elle, de vanité, de vieillissement et de deux femmes qui peinent à trouver le lien entre elles, et avec les autres femmes. Elle confie aussi être \"always very overwhelmed\" (toujours très émue) quand elle revoit la scène où Arthur annonce à Mary-Beth qu'il va mourir. Une part d'elle regrette de ne pas avoir mesuré, au tournage, le poids que cette scène aurait pour les joueurs ; une autre aime \"such an innocence to that scene\" (toute l'innocence de cette scène) : quand quelqu'un vous annonce une chose pareille, demande-t-elle, comment l'encaisser ?")},
    {"p": two("Kaili Vernoff described a scene between Susan and Mary-Beth to Josh Wilding of GameFragger, in an interview published on February 21, 2019: Susan catches Mary-Beth looking at herself in a mirror and tells her that vanity will get her nowhere, with the line \"Time will get you too and they'll stop looking.\" Vernoff said it showed why Susan is so hard on the younger women. In an interview with Heather Newman of Forbes, published on February 12, 2019, Vernoff named Strelitz, Meeya Davis (Tilly) and Jo Armeniox (Karen) as the actresses she worked with most closely and said they still spoke \"almost daily\".",
              "Kaili Vernoff a décrit une scène entre Susan et Mary-Beth à Josh Wilding, de GameFragger, dans un entretien publié le 21 février 2019 : Susan surprend Mary-Beth en train de se regarder dans un miroir et lui fait comprendre que la coquetterie ne la mènera nulle part, avec cette réplique : \"Time will get you too and they'll stop looking.\" (le temps te rattrapera, toi aussi, et ils cesseront de te regarder). Selon Vernoff, la scène explique pourquoi Susan est si dure avec les jeunes femmes. Dans un entretien avec Heather Newman, de Forbes, publié le 12 février 2019, Vernoff cite Samantha Strelitz, Meeya Davis (Tilly) et Jo Armeniox (Karen) comme les actrices avec qui elle a le plus travaillé, et dit qu'elles se parlent encore \"almost daily\" (presque tous les jours).")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The Red Dead Wiki lists unused assets for Mary-Beth in the game files: three hairstyles, a head model and two sets of eyelashes. The files also name a cut item request labeled only \"as\", whose meaning is unknown. She also takes part in an unused camp encounter in which Susan tells the young women that Karen stormed off the night before; the wiki doubts the scene can ever play, because Karen and Mary-Beth are gone from the gang at the same point in the story. Concept art published by the wiki shows Mary-Beth with Bill, Karen, Tilly, Uncle, Strauss and Pearson.",
              "Le Red Dead Wiki recense des éléments inutilisés pour Mary-Beth dans les fichiers du jeu : trois coiffures, un modèle de tête et deux jeux de cils. Les fichiers mentionnent aussi une commande d'objet abandonnée, désignée par les seules lettres \"as\", dont le sens reste inconnu. Elle figure en outre dans une scène de camp inutilisée où Susan annonce aux jeunes femmes que Karen est partie furieuse la veille au soir ; le wiki doute que la scène puisse jamais se jouer, Karen et Mary-Beth disparaissant de la bande au même moment de l'histoire. Des illustrations conceptuelles publiées par le wiki montrent Mary-Beth avec Bill, Karen, Tilly, Uncle, Strauss et Pearson.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Game Informer ranking", "Le classement de Game Informer")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on December 27, 2018, Mary-Beth comes 13th, one place ahead of Karen. The staff acknowledged that her \"quiet demeanor and absence during the story missions\" might make the ranking surprising, but wrote that players who talk to her in their free time \"will know she's secretly one of the most interesting characters for Arthur to interact with\". They described her as \"A con woman who's sweet on Arthur\", said their conversations \"have an honest, gentle quality to them\" and mentioned the dance the two can share at a party. They called her epilogue scene, in which John learns she has become a successful novelist, her best moment: \"A necessary bright spot in this epic, dark tale.\"",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Mary-Beth arrive 13e, une place devant Karen. La rédaction reconnaît que sa discrétion et son absence des missions principales peuvent surprendre à ce rang, mais estime que les joueurs qui prennent le temps de lui parler savent qu'elle est \"secretly one of the most interesting characters for Arthur to interact with\" (en secret, l'un des personnages les plus intéressants à côtoyer pour Arthur). Elle la décrit comme \"A con woman who's sweet on Arthur\" (une arnaqueuse qui a un faible pour Arthur), juge que leurs conversations ont \"an honest, gentle quality\" (quelque chose de sincère et de doux) et cite la danse qu'ils peuvent partager lors d'une fête. Pour la rédaction, son meilleur moment est la scène d'épilogue où John apprend qu'elle est devenue une romancière à succès : \"A necessary bright spot in this epic, dark tale.\" (une éclaircie nécessaire dans ce récit épique et sombre).")},
]


BASE = {
    "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill",
    "publishDate": "2026-08-20", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Female", "death": None, "nationality": "American",
    "portrait_alt": two("Mary-Beth Gaskill in Red Dead Redemption 2", "Mary-Beth Gaskill dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Mary-Beth Gaskill, pickpocket of the Van der Linde gang in RDR2: the Valentine train tip, Kieran's death, Arthur's confession, and her career as novelist Leslie Dupont.",
                     "Mary-Beth Gaskill, pickpocket du gang Van der Linde dans RDR2 : le tuyau du train à Valentine, la mort de Kieran, la confidence d'Arthur et sa carrière de romancière sous le nom de Leslie Dupont."),
    "og_desc": two("The complete reference on Mary-Beth Gaskill: life, camp scenes, missions, quotes, development and reception.",
                   "La référence complète sur Mary-Beth Gaskill : vie, scènes de camp, missions, citations, conception et accueil."),
    "schema_desc": two("Pickpocket of the Van der Linde gang in Red Dead Redemption 2 who leaves the gang in 1899 and, by 1907, publishes romance novels under the pen name Leslie Dupont.",
                       "Pickpocket du gang Van der Linde dans Red Dead Redemption 2, qui quitte la bande en 1899 et publie, en 1907, des romans sentimentaux sous le pseudonyme de Leslie Dupont."),
    "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Pickpocket", "Pickpocket"),
              two("Novelist in 1907", "Romancière en 1907"),
              two("Voiced by <strong>Samantha Strelitz</strong>", "Voix de <strong>Samantha Strelitz</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Mary-Beth Gaskill", "Mary-Beth Gaskill")},
        {"label": two("Pen name", "Pseudonyme"), "value": two("Leslie Dupont (1907)", "Leslie Dupont (1907)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game (according to the Red Dead Wiki, Arthur guesses she is 21 or 22, and she tells him it is rude to talk about her age)", "Non précisée dans le jeu (d'après le Red Dead Wiki, Arthur lui donne 21 ou 22 ans, et elle lui fait remarquer qu'il est impoli de parler de son âge)")},
        {"label": two("Family", "Famille"), "value": two("Her mother, who died of typhoid", "Sa mère, morte de la typhoïde")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1907", "Vivante en 1907")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang (until 1899)", "Gang Van der Linde (jusqu'en 1899)")},
        {"label": two("Role", "Rôle"), "value": two("Pickpocket and con artist; novelist by 1907", "Pickpocket et arnaqueuse ; romancière en 1907")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Samantha Strelitz (voice and motion capture)", "Samantha Strelitz (voix et capture de mouvement)")},
    ],
    "intro": [
        two("Mary-Beth Gaskill is a supporting character of Red Dead Redemption 2 (2018), set in 1899. She is a young pickpocket of the Van der Linde gang who reads romance novels and wants to write her own. During the Horseshoe Overlook chapter she brings back from Valentine the lead on a train of wealthy passengers that the gang robs in \"Pouring Forth Oil IV\". She helps [[arthur-morgan|Arthur Morgan]] and [[sean-macguire|Sean MacGuire]] rob a stagecoach, and she screams on recognizing the body of [[kieran-duffy|Kieran Duffy]] when the O'Driscolls send it back to Shady Belle. At Beaver Hollow Arthur can tell her that he is dying of tuberculosis. She leaves the gang before its end. By 1907 she publishes romance novels under the pen name Leslie Dupont, and [[john-marston|John Marston]] can meet her at Valentine station.",
            "Mary-Beth Gaskill est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Jeune pickpocket du gang Van der Linde, elle dévore les romans sentimentaux et rêve d'écrire les siens. Pendant le chapitre de Horseshoe Overlook, elle rapporte de Valentine la piste d'un train de voyageurs fortunés que la bande attaque dans \"Pouring Forth Oil IV\". Elle aide [[arthur-morgan|Arthur Morgan]] et [[sean-macguire|Sean MacGuire]] à dévaliser une diligence, et elle hurle en reconnaissant le corps de [[kieran-duffy|Kieran Duffy]] quand les O'Driscoll le renvoient à Shady Belle. À Beaver Hollow, Arthur peut lui apprendre qu'il est condamné par la tuberculose. Elle quitte la bande avant sa fin. En 1907, elle publie des romans sentimentaux sous le pseudonyme de Leslie Dupont, et [[john-marston|John Marston]] peut la croiser à la gare de Valentine."),
        two("She is played by Samantha Strelitz, an American actress.",
            "Elle est interprétée par Samantha Strelitz, actrice américaine."),
    ],
    "essentials": [
        two("A pickpocket who joined the gang after its members came across her as men she had robbed were chasing her, according to the Red Dead Wiki.",
            "Pickpocket, elle a rejoint la bande après que ses membres sont tombés sur elle alors qu'elle était poursuivie par des hommes qu'elle avait volés, d'après le Red Dead Wiki."),
        two("In \"Polite Society, Valentine Style\" she finds the lead on a train of rich tourists that leads to the gang's train robbery, in which she takes no part.",
            "Dans \"Polite Society, Valentine Style\", elle trouve la piste d'un train de riches touristes qui mène à l'attaque du train par la bande, à laquelle elle ne participe pas."),
        two("She is one of the few people [[arthur-morgan|Arthur]] tells about his tuberculosis, and is gone from Beaver Hollow by \"Our Best Selves\", when Dutch names her among those who ran off.",
            "Elle fait partie des rares personnes à qui [[arthur-morgan|Arthur]] parle de sa tuberculose, et a quitté Beaver Hollow avant \"Our Best Selves\", quand Dutch la cite parmi ceux qui ont filé."),
        two("By 1907 she is a novelist writing as Leslie Dupont, author of \"The Lady of the Manor\", and still close to [[tilly-jackson|Tilly Jackson]].",
            "En 1907, elle est romancière sous le nom de Leslie Dupont, autrice de \"The Lady of the Manor\", et toujours proche de [[tilly-jackson|Tilly Jackson]]."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["tilly-jackson", "karen-jones", "kieran-duffy", "arthur-morgan"],
}
