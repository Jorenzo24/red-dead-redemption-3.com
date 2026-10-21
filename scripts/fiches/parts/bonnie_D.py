"""Bonnie MacFarlane, reference fiche, PART D: base data, Development and performance, Reception
(20 Oct 2026, medium tier).

Her live page (characters/bonnie-macfarlane/) was generated from the v2 entry in scripts/_wave4.py
("slug": "bonnie-macfarlane"; no entry of her own in _enrich.py). The base below is rebuilt from that
entry, with corrections:
- intro: "becomes John's closest ally during his time in the territory" (interpretation) and "nurses him
  back to health" (a doctor treats him; she pays and lodges him) are replaced by facts;
- facts grid: "Alive (end of RDR1)" replaced (she is last seen in 1911; in 1914 the ranch still operates
  and Jack never sees her); "Nationality: American" kept only as an attributed wiki statement (the game
  never states it; "nationality" set to None as on other fiches); added Family, Home, Occupation,
  Played by, Games with years;
- the v2 Personality line "practical, tough and proud of the ranch her family built" (interpretation)
  and "the one person John willingly tells about his outlaw past" are dropped (part B gives the
  official guide's description; the conversation is in part A);
- the v2 "Behind the scenes" paragraph (wrongly dating the remaster to 2024: the PS4 / Switch port came
  out in 2023, PC in 2024) is replaced by a sourced Development section; a Reception section is added;
- the v2 trivia line "named after the aunt of a Rockstar San Diego designer" moves to Development.
Kept: eyebrow "Character &middot; New Austin" (as on the live page), reg_role "Rancher &middot; RDR1" /
"Ranchère &middot; RDR1" (characters_registry.py), publishDate 2026-07-27 (git 7befaea, drip publish).

SOURCE REGISTER (fetched 20 Oct 2026; notes in scripts/v3/work/bonnie/fc/web_sources_BD.txt and
fc/wp_rdr_refs.txt; wiki cache scripts/v3/work/_m/):
- Red Dead Wiki "Bonnie MacFarlane" (infobox voice Kimberly Irion; trivia: Rob Hanson naming, motion
  capture of the train scene by Steve J. Palmer, Game Informer list, PlayStation Home, fold-out map),
  "Kimberly Irion" (Kimberly Irion Yungfleisch; RDR, Undead Nightmare, Liars and Cheats multiplayer
  variant, Red Dead Online), "Red Dead Redemption Cut Content" (surname "MacFarling" marked {{Citation
  needed}}; ranch once "Hennigan's Ranch" and "MacFarling's Ranch"; unused Penny Dreadful item),
  "MacFarlane's Ranch", "Kidnapped Woman Found Alive" (Blackwater Ledger No. 55: "a spinster of 29 years").
- Wikipedia "Red Dead Redemption": cast line "local rancher Bonnie MacFarlane (Kimberly Irion)"; analysis
  citing Sara Humphreys, Western American Literature 47(2), 2012, pp. 207-208, and Matt Margini,
  Red Dead Redemption, Boss Fight Books, 2020, p. 56.
- Game Informer, "December Cover Revealed", 5 Nov 2010 (cover of the "30 Characters Who Defined a
  Decade" issue: "Bonnie's hand rests on John Marston's shoulder"); list reproduced by Nintendo
  Everything, 13 Nov 2010 (John 2nd, Bonnie 29th).
- Game Informer, Javy Gwaltney, "A Surprising, Familiar Face Returns In Red Dead Online", 28 Nov 2018.
- PC Games (Germany), Olaf Bleich, Benedikt Plass-Flessenkaemper and Maria Beyer-Fistrich,
  "10 Jahre Red Dead Redemption", 4 Apr 2020.
- Transcripts for intro/essentials: "Exodus in America", "New Friends, Old Problems", "The Burning",
  "Hanging Bonnie MacFarlane", "The Outlaw's Return", "Old Friends, New Problems" (a telegram, not a letter).
Fix pass (20 Oct 2026): academic reception attributed to Wikipedia's summary (Humphreys article not read); Hanson naming
sentence recast; one of Bill's men fires; age 27 attributed to the guide and the wiki.
No interview with Kimberly Irion about the role was found (web searches, 20 Oct 2026). No source beyond
the wiki was found for the Rob Hanson anecdote or the Steve J. Palmer motion capture: both attributed.

OWNERSHIP: actress, motion capture, naming, cut content and Game Informer / PC Games / academic
reception live HERE; part C (Trivia, Other media) must not repeat them. The Game Informer cover and the
Gwaltney article are Reception, not Trivia. PlayStation Home, the fold-out map and the Liars and Cheats
multiplayer model are left to part C.

Excluded: Irion's birth year and height (wiki people page only); RDR2.org's article (fan site); the
French wiki's claim that she is married by 1914 (unsourced, contradicted by the EN wiki); the wiki's
guess that the age gap is "plausibly an in-story misreporting" (speculation); Margini's and Humphreys's
wider arguments beyond the two points Wikipedia summarizes (books not read directly).
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting and motion capture", "Interprétation et capture de mouvement")},
    {"p": two(
        "Bonnie is played by Kimberly Irion, credited in the role by Wikipedia's article on Red Dead Redemption and by the Red Dead Wiki. According to the wiki, Irion plays her in the main game and in Undead Nightmare (2010), voices the multiplayer version of the character added by the Liars and Cheats pack, and returns to the role in Red Dead Online, where Bonnie is a minor mission giver. No interview in which Irion discusses the role was found. The Red Dead Wiki states that Bonnie's motion capture for the opening train scene was performed by Steve J. Palmer, the actor who plays Bill Williamson.",
        "Bonnie est interprétée par Kimberly Irion, que l'article de Wikipédia sur Red Dead Redemption et le Red Dead Wiki créditent dans ce rôle. D'après le wiki, Irion la joue dans le jeu principal et dans Undead Nightmare (2010), prête sa voix à la version multijoueur du personnage ajoutée par le pack Liars and Cheats, et reprend le rôle dans Red Dead Online, où Bonnie confie quelques missions. Aucune interview dans laquelle Irion parle du rôle n'a été trouvée. Le Red Dead Wiki indique que la capture de mouvement de Bonnie pour la scène du train, au début du jeu, a été réalisée par Steve J. Palmer, l'interprète de Bill Williamson.")},
    {"h3": two("Name", "Le nom")},
    {"p": two(
        "According to the Red Dead Wiki, Bonnie is named after an aunt of Rob Hanson, a former designer at Rockstar San Diego. The same unsourced account says that Hanson, who had designed the ranch, chose both its name and hers before leaving Rockstar San Diego.",
        "D'après le Red Dead Wiki, Bonnie doit son nom à une tante de Rob Hanson, ancien concepteur chez Rockstar San Diego. Toujours selon ce récit sans source, c'est Hanson, auteur du ranch, qui a choisi le nom du domaine comme celui de Bonnie avant son départ de Rockstar San Diego.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two(
        "The Red Dead Wiki's page on the game's cut content states that the family's original surname was MacFarling, a claim the page itself marks as needing a citation. The same page says the ranch was called \"Hennigan's Ranch\" at one stage, then \"MacFarling's Ranch\". The game files also contain an unused Penny Dreadful item, the kind of novel Bonnie says her brother used to read; its intended purpose is unknown.",
        "La page du Red Dead Wiki consacrée au contenu coupé du jeu affirme que le nom d'origine de la famille était MacFarling, une affirmation que la page signale elle-même comme dépourvue de source. La même page indique que le ranch s'est appelé un temps \"Hennigan's Ranch\", puis \"MacFarling's Ranch\". Les fichiers du jeu contiennent aussi un objet Penny Dreadful inutilisé, le genre de roman populaire que lisait l'un des frères de Bonnie selon elle ; on ignore à quoi il devait servir.")},
]

BLOCKS_RECEPTION = [
    {"p": two(
        "Game Informer ranked Bonnie 29th in its list of the 30 characters who defined the decade, published in its December 2010 issue; John Marston came second. The cover art commissioned for the feature, revealed by the magazine on November 5, 2010, shows Bonnie's hand resting on John's shoulder.",
        "Game Informer a classé Bonnie 29e de sa liste des 30 personnages qui ont marqué la décennie, parue dans son numéro de décembre 2010 ; John Marston y figure à la deuxième place. L'illustration commandée pour ce dossier, dévoilée par le magazine le 5 novembre 2010, montre la main de Bonnie posée sur l'épaule de John.")},
    {"p": two(
        "According to Wikipedia's summary of her 2012 article in Western American Literature, Sara Humphreys describes Bonnie as \"insightful and resourceful\" rather than \"a woman masquerading as a male figure\", while noting that she defers to simple domestic tasks when her father is present. The same summary cites Matt Margini, whose 2020 book on the game for Boss Fight Books points out that on one occasion she becomes a damsel in distress. In a retrospective for the game's tenth anniversary, on April 4, 2020, the German magazine PC Games called her a modern woman, assertive and direct.",
        "D'après le résumé qu'en donne Wikipédia, Sara Humphreys, dans un article paru en 2012 dans la revue Western American Literature, voit en Bonnie un personnage \"insightful and resourceful\" (perspicace et pleine de ressources) plutôt que \"a woman masquerading as a male figure\" (une femme déguisée en figure masculine), tout en relevant qu'elle s'en remet aux simples tâches domestiques en présence de son père. Le même résumé cite Matt Margini, qui note dans son livre de 2020 sur le jeu, paru chez Boss Fight Books, qu'elle devient, à une occasion, une demoiselle en détresse. Dans une rétrospective publiée pour les dix ans du jeu, le 4 avril 2020, le magazine allemand PC Games la décrit comme une femme moderne, affirmée et directe.")},
    {"p": two(
        "Her return in Red Dead Online drew coverage at the launch of the online beta. On November 28, 2018, Javy Gwaltney of Game Informer described finding MacFarlane's Ranch deserted in the story of Red Dead Redemption 2, then meeting Bonnie online, \"years before meeting John Marston\", with a mission to find a wagon.",
        "Son retour dans Red Dead Online a été relevé dès le lancement de la bêta en ligne. Le 28 novembre 2018, Javy Gwaltney, de Game Informer, raconte avoir trouvé le MacFarlane's Ranch désert dans l'histoire de Red Dead Redemption 2, puis avoir croisé Bonnie en ligne, des années avant sa rencontre avec John Marston, avec une mission consistant à retrouver un chariot.")},
]


BASE = {
    "slug": "bonnie-macfarlane", "name": "Bonnie MacFarlane",
    "publishDate": "2026-07-27", "updated": "2026-10-20", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Rancher &middot; RDR1", "reg_role_fr": "Ranchère &middot; RDR1",
    "gender": "Female", "birth": "1884", "death": None, "nationality": None,
    "portrait_alt": two("Bonnie MacFarlane in Red Dead Redemption", "Bonnie MacFarlane dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; New Austin", "Personnage &middot; New Austin"),
    "meta_desc": two("Bonnie MacFarlane in Red Dead Redemption: the rancher who finds John Marston shot after Fort Mercer, the barn fire, her kidnapping at Tumbleweed, the corn delivery, Kimberly Irion.",
                     "Bonnie MacFarlane dans Red Dead Redemption : la ranchère qui trouve John Marston blessé après Fort Mercer, l'incendie de la grange, son enlèvement à Tumbleweed, le maïs, Kimberly Irion."),
    "og_desc": two("The complete reference on Bonnie MacFarlane: life, missions, relationships, quotes and development.",
                   "La référence complète sur Bonnie MacFarlane : vie, missions, relations, citations et conception."),
    "schema_desc": two("Rancher's daughter of MacFarlane's Ranch, in New Austin, who has John Marston treated after he is shot at Fort Mercer and gives him work on the ranch in 1911, in Red Dead Redemption.",
                       "Fille de rancher du MacFarlane's Ranch, dans le New Austin, qui fait soigner John Marston blessé à Fort Mercer et lui donne du travail au ranch en 1911, dans Red Dead Redemption."),
    "chips": [two("Rancher", "Ranchère"), two("Born <strong>c. 1884</strong>", "Née <strong>v. 1884</strong>"),
              two("Alive in 1911", "En vie en 1911"),
              two("Played by <strong>Kimberly Irion</strong>", "Interprétée par <strong>Kimberly Irion</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Bonnie MacFarlane", "Bonnie MacFarlane")},
        {"label": two("Born", "Naissance"), "value": two("Around 1884 (27 in 1911 according to the official guide and the Red Dead Wiki; the Blackwater Ledger calls her 29)", "Vers 1884 (27 ans en 1911 selon le guide officiel et le Red Dead Wiki ; le Blackwater Ledger lui en donne 29)")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1911; not seen in 1914, when the ranch is still running", "En vie en 1911 ; absente en 1914, quand le ranch tourne toujours")},
        {"label": two("Nationality", "Nationalité"), "value": two("Not stated in the game (American according to the Red Dead Wiki)", "Non précisée dans le jeu (américaine selon le Red Dead Wiki)")},
        {"label": two("Home", "Domicile"), "value": two("MacFarlane's Ranch, Hennigan's Stead, New Austin", "MacFarlane's Ranch, Hennigan's Stead, New Austin")},
        {"label": two("Occupation", "Activité"), "value": two("Works her father's cattle ranch", "Travaille au ranch d'élevage de son père")},
        {"label": two("Family", "Famille"), "value": two("Drew MacFarlane (father); six brothers, five of them dead, one a banker in New York", "Drew MacFarlane (père) ; six frères, dont cinq morts et un banquier à New York")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption and Undead Nightmare (2010); Red Dead Online (2018); mentioned in Red Dead Redemption 2", "Red Dead Redemption et Undead Nightmare (2010) ; Red Dead Online (2018) ; mentionnée dans Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Kimberly Irion", "Kimberly Irion")},
    ],
    "intro": [
        two("Bonnie MacFarlane is a character in Red Dead Redemption (2010), set in 1911. She is the daughter of Drew MacFarlane, owner of MacFarlane's Ranch in Hennigan's Stead, New Austin. With her ranch hand Amos, she finds [[john-marston|John Marston]] by the road after one of [[bill-williamson|Bill Williamson]]'s men shoots him at Fort Mercer, takes him to the doctor and gives him room and board in exchange for work. Bill's gang later burns the ranch barn and kidnaps her; John and [[leigh-johnson|Marshal Leigh Johnson]] free her at Tumbleweed. After John's return home, the MacFarlanes sell him cattle, and he and [[abigail-marston|Abigail]] later bring her corn.",
            "Bonnie MacFarlane est un personnage de Red Dead Redemption (2010), dont l'action se déroule en 1911. Elle est la fille de Drew MacFarlane, propriétaire du MacFarlane's Ranch, à Hennigan's Stead, dans le New Austin. Avec son employé Amos, elle trouve [[john-marston|John Marston]] au bord de la route après qu'un homme de [[bill-williamson|Bill Williamson]] lui a tiré dessus à Fort Mercer ; elle l'emmène chez le médecin et le loge et le nourrit contre du travail. La bande de Bill incendie ensuite la grange du ranch et l'enlève ; John et [[leigh-johnson|le marshal Leigh Johnson]] la délivrent à Tumbleweed. Une fois John rentré chez lui, les MacFarlane lui vendent du bétail, puis John et [[abigail-marston|Abigail]] viennent lui apporter du maïs."),
        two("She also appears in Undead Nightmare and, in 1898, as a Stranger in Red Dead Online; she is only mentioned in Red Dead Redemption 2. She is played by Kimberly Irion.",
            "Elle apparaît aussi dans Undead Nightmare et, en 1898, parmi les inconnus de Red Dead Online ; Red Dead Redemption 2 ne fait que la mentionner. Elle est interprétée par Kimberly Irion."),
    ],
    "essentials": [
        two("She and Amos find John shot outside Fort Mercer; she pays the 15-dollar doctor's bill and puts him to work on the ranch.",
            "Avec Amos, elle trouve John blessé devant Fort Mercer ; elle règle les 15 dollars de médecin et le fait travailler au ranch."),
        two("She gives the game's first mission strand: night patrol, a horse race, a ride to Armadillo, herding, breaking horses, a thunderstorm and the search for her father.",
            "Elle confie la première série de missions du jeu : ronde de nuit, course à cheval, trajet jusqu'à Armadillo, conduite du bétail, dressage, orage et recherche de son père."),
        two("In \"Hanging Bonnie MacFarlane\", Bill's gang offers her in exchange for Norman Deek and tries to hang her at Tumbleweed.",
            "Dans \"Hanging Bonnie MacFarlane\", la bande de Bill propose de l'échanger contre Norman Deek et tente de la pendre à Tumbleweed."),
        two("In 1911 she helps John and [[jack-marston|Jack]] drive the cattle they buy at the ranch, then meets Abigail when the Marstons bring her corn after a telegram.",
            "En 1911, elle aide John et [[jack-marston|Jack]] à emmener le bétail qu'ils achètent au ranch, puis rencontre Abigail quand les Marston lui apportent du maïs à la suite d'un télégramme."),
        two("Game Informer ranked her 29th among the 30 characters who defined the 2000s (December 2010).",
            "Game Informer l'a classée 29e des 30 personnages qui ont marqué les années 2000 (décembre 2010)."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["john-marston", "abigail-marston", "leigh-johnson", "bill-williamson"],
}
