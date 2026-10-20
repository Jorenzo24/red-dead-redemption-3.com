"""Leopold Strauss, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026, medium tier).

His live page (characters/leopold-strauss/) was generated from the v2 entry in scripts/_enrich.py
(BATCH3, "slug": "leopold-strauss"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the v2 "death": "1899" and the facts line "Died: 1899, in Pinkerton custody" are dropped,
since no source dates his death: he leaves the gang in 1899 and Charles reports it in 1907 ("death": None, facts
say "between 1899 and 1907"). The v2 intro line "One of those collections is how Arthur catches tuberculosis" is
kept as a sourced event (Downes coughs blood on Arthur; Arthur is later diagnosed with tuberculosis, Wikipedia list,
Downes family section; consistent with arthur_A). The v2 Origins paragraph paraphrased the official guide; the guide
now lives in part B (Personality, quoted verbatim) and the intro states events only. Chips: "Died 1899" and the
"Deceased" duplicate replaced by an actor chip. Eyebrow and reg_role match characters_registry.py ("Van der Linde
gang &middot; RDR2"). publishDate 2026-07-03 kept (git: 2704ec3, "chore: drip-publish scheduled character
(PUBLISHED leopold-strauss)", 3 Jul 2026). The v2 Reception sources are kept and re-verified (Game Informer quote
re-read; Polygon article re-read in the 22 Nov 2018 archive, the quote now complete and dated).

Sources (internal register, checked 20 Oct 2026):
- Wikipedia "List of Red Dead Redemption 2 characters" (../uncle/fc/wp_list_rdr2_characters.txt): "Leopold Strauss
  (Howard Pinhasik)"; production section (motion capture, facial cameras; recording from 2013, 2,200 days, 1,200
  actors, 700 sharing 500,000 lines, per Vulture).
- Red Dead Wiki "Howard Pinhasik" (leopold/fcB/wiki_Howard_Pinhasik.txt): American actor, born 5 June 1953 in
  Chicago, Illinois; cast as the voice and motion-capture actor; credits The Hudson Tribes and The Marvelous Mrs.
  Maisel (wiki-only, attributed).
- TheGamer, Jerrad Wyche, "Red Dead Redemption 2: 10 Facts About The Heartless Bookkeeper, Leopold Strauss",
  published 5 Sep 2019, 6:00 PM EDT (leopold/fcB/thegamer.txt): Pinhasik's facial scan used for the character;
  quotes on the performance and on Strauss's loyalty.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../uncle/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt):
  unused vest and boots; cut item request for reading glasses with an icon left in the files; concept art of
  Bill, Karen, Tilly, Uncle, Mary-Beth, Strauss and Pearson; concept art once shown at the National Museum of
  Scotland in which Strauss is of short stature.
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  27 Dec 2018 (../uncle/fc/gi_ranking.txt): Strauss 23rd of 24, quoted verbatim.
- Polygon, Colin Campbell, "Red Dead Redemption 2 is a confection of cowboy clichés", opinion, 22 Nov 2018
  (archive of the same day, leopold/fcB/polygon.txt): quoted verbatim.
- Official guide page and Rockstar description of 6 Sep 2018: used in part B only.
Fix pass 20 Oct 2026: wiki-only birth date and place and "The Hudson Tribes" dropped; Angels in America kept as
TheGamer's claim; The Marvelous Mrs. Maisel kept (guest role, confirmed independently on TVmaze); the generic motion
capture paragraph cut; the actor sentence lives in the intro only.
Excluded: IMDb credits (not read); the
Leo Strauss name origin and the "possibly Jewish" trivia with its stereotype debate (wiki speculation, no outlet of
record found); the wiki's birth estimate as a fact (kept attributed in the facts grid only).
DUPLICATE ownership: actor, production context, cut content and concept art live HERE; parts B and C must not
retell them. The guide and Rockstar descriptions belong to part B; origins, the debt collections, the Cornwall
ambush, the riverboat, the expulsion and the 1907 news belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("According to the Red Dead Wiki, Pinhasik provides both the voice and the motion capture performance for Strauss. In a list of facts about the character published on September 5, 2019, TheGamer's Jerrad Wyche wrote that Pinhasik's facial scan was used to give Strauss his look. Wyche named the television series Angels in America, in which Pinhasik played a character's father, as his only other notable role. Pinhasik has also appeared as a guest in The Marvelous Mrs. Maisel.",
              "D'après le Red Dead Wiki, Pinhasik assure à la fois la voix et la capture de mouvement du personnage. Dans une liste d'anecdotes sur le personnage publiée le 5 septembre 2019, Jerrad Wyche, de TheGamer, indique que le visage de Strauss a été créé à partir d'un scan de celui de Pinhasik. Il cite comme seul autre rôle marquant de l'acteur celui d'un père dans la série Angels in America. Pinhasik a aussi fait une apparition dans The Marvelous Mrs. Maisel.")},
    {"h3": two("Cut content and concept art", "Contenu coupé et illustrations conceptuelles")},
    {"p": two("The Red Dead Wiki lists an unused vest and unused boots for Strauss in the game files. The files also hold a cut item request in which Strauss was to ask Arthur for reading glasses; its icon is still in the game data. Concept art published by the wiki shows Strauss with Bill, Karen, Tilly, Uncle, Mary-Beth and Pearson. According to the Red Dead Wiki's page on cut content, some of the game's concept art was shown for a time at the National Museum of Scotland, and in it Strauss is drawn as a short man.",
              "Le Red Dead Wiki recense un gilet et des bottes inutilisés pour Strauss dans les fichiers du jeu. Les fichiers contiennent aussi une commande d'objet abandonnée, dans laquelle Strauss devait demander à Arthur des lunettes de lecture ; son icône figure toujours dans les données du jeu. Une illustration conceptuelle publiée par le wiki montre Strauss avec Bill, Karen, Tilly, Uncle, Mary-Beth et Pearson. D'après la page du Red Dead Wiki consacrée au contenu coupé, une partie des illustrations conceptuelles du jeu a été exposée un temps au National Museum of Scotland, et Strauss y apparaît de petite taille.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Game Informer ranking", "Le classement de Game Informer")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on December 27, 2018, Strauss comes 23rd, ahead of Micah Bell only. The entry reads: \"It's bad enough that Strauss is a loan shark. However, it's his cruel business that results in Arthur getting infected with tuberculosis when our antihero goes to collect a debt from the Downes family. It doesn't help he's downright sleazy and seems to derive pleasure from causing others misery.\"",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Strauss arrive 23e, devant le seul Micah Bell. Sa notice rappelle qu'il est usurier et que c'est son commerce cruel qui vaut à Arthur sa tuberculose, quand celui-ci va recouvrer la dette des Downes. Elle ajoute qu'il est \"downright sleazy\" (franchement louche) et qu'il semble prendre plaisir au malheur des autres.")},
    {"h3": two("Other assessments", "Autres avis")},
    {"p": two("In an opinion piece published by Polygon on November 22, 2018, \"Red Dead Redemption 2 is a confection of cowboy clichés\", Colin Campbell cited Strauss among the game's stock characters: \"Leopold Strauss is a slightly sinister money lender complete with a German accent and a taste for cruelty.\" In his list of facts published by TheGamer on September 5, 2019, Jerrad Wyche wrote that Pinhasik \"did an excellent job of bringing the Austrian loan shark to life and was able to toe the line between a heartless crook and loyal gang member\", and that \"no one could ever question Strauss' loyalty to his gang.\"",
              "Dans une tribune publiée par Polygon le 22 novembre 2018, \"Red Dead Redemption 2 is a confection of cowboy clichés\", Colin Campbell range Strauss parmi les personnages de convention du jeu : un usurier vaguement inquiétant, \"complete with a German accent and a taste for cruelty\" (avec accent allemand et goût de la cruauté en prime). Dans sa liste d'anecdotes publiée par TheGamer le 5 septembre 2019, Jerrad Wyche estime que Pinhasik a donné vie à l'usurier autrichien avec beaucoup de justesse, sur la ligne de crête entre l'escroc sans cœur et le membre loyal du gang, et que personne ne pourrait mettre en doute la loyauté de Strauss envers la bande.")},
]


BASE = {
    "slug": "leopold-strauss", "name": "Leopold Strauss",
    "publishDate": "2026-07-03", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Male", "death": None, "nationality": "Austrian",
    "portrait_alt": two("Leopold Strauss in Red Dead Redemption 2", "Leopold Strauss dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Leopold Strauss, the Van der Linde gang's Austrian money lender in RDR2: the debt collections, the Downes debt, his departure from the gang and his death in Pinkerton custody.",
                     "Leopold Strauss, l'usurier autrichien du gang Van der Linde dans RDR2 : les recouvrements de dettes, la dette des Downes, son départ de la bande et sa mort aux mains de la Pinkerton."),
    "og_desc": two("The complete reference on Leopold Strauss: life, camp scenes, missions, quotes, development and reception.",
                   "La référence complète sur Leopold Strauss : vie, scènes de camp, missions, citations, conception et accueil."),
    "schema_desc": two("Austrian bookkeeper and money lender of the Van der Linde gang in Red Dead Redemption 2, who leaves the gang in 1899.",
                       "Comptable et usurier autrichien du gang Van der Linde dans Red Dead Redemption 2, qui quitte la bande en 1899."),
    "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Money lender", "Usurier"),
              two("Deceased", "Décédé"),
              two("Voiced by <strong>Howard Pinhasik</strong>", "Voix de <strong>Howard Pinhasik</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Leopold Strauss", "Leopold Strauss")},
        {"label": two("Origin", "Origine"), "value": two("Vienna, Austria", "Vienne, Autriche")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game (the official guide says he left Vienna for America at 17; the Red Dead Wiki estimates about 1846)", "Non précisée dans le jeu (selon le guide officiel, il quitte Vienne pour l'Amérique à 17 ans ; le Red Dead Wiki avance environ 1846)")},
        {"label": two("Died", "Mort"), "value": two("Between 1899 and 1907, in Pinkerton custody (reported by Charles Smith in 1907)", "Entre 1899 et 1907, aux mains de la Pinkerton (rapporté par Charles Smith en 1907)")},
        {"label": two("Nationality", "Nationalité"), "value": two("Austrian", "Autrichienne")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang (until 1899)", "Gang Van der Linde (jusqu'en 1899)")},
        {"label": two("Role", "Rôle"), "value": two("Bookkeeper and money lender", "Comptable et usurier")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Howard Pinhasik (voice and motion capture)", "Howard Pinhasik (voix et capture de mouvement)")},
    ],
    "intro": [
        two("Leopold Strauss is a character of Red Dead Redemption 2 (2018), set in 1899. An Austrian immigrant, he keeps the books of the Van der Linde gang and runs its money-lending business. From the Horseshoe Overlook chapter onward, he sends [[arthur-morgan|Arthur Morgan]] to collect debts in the \"Money Lending and Other Sins\" missions. One of them takes Arthur to the farmer Thomas Downes, who coughs blood on him; Arthur is later diagnosed with tuberculosis. Strauss also takes part in the riverboat robbery of \"A Fine Night of Debauchery\" with Arthur, [[javier-escuella|Javier Escuella]] and [[josiah-trelawny|Josiah Trelawny]]. At Beaver Hollow he leaves the gang: depending on the player, Arthur throws him out or he leaves on his own. In 1907 [[charles-smith|Charles Smith]] tells John Marston that the Pinkertons arrested Strauss and that he died in their custody without giving up the gang.",
            "Leopold Strauss est un personnage de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Immigré autrichien, il tient les comptes du gang Van der Linde et gère ses prêts d'argent. À partir du chapitre de Horseshoe Overlook, il envoie [[arthur-morgan|Arthur Morgan]] recouvrer des dettes dans les missions \"Money Lending and Other Sins\". L'une d'elles mène Arthur chez le fermier Thomas Downes, qui lui crache du sang au visage ; Arthur apprend plus tard qu'il a la tuberculose. Strauss participe aussi au braquage du bateau à aubes de \"A Fine Night of Debauchery\", avec Arthur, [[javier-escuella|Javier Escuella]] et [[josiah-trelawny|Josiah Trelawny]]. À Beaver Hollow, il quitte la bande : selon les choix du joueur, Arthur le chasse ou il s'en va de lui-même. En 1907, [[charles-smith|Charles Smith]] apprend à John Marston que les Pinkerton ont arrêté Strauss et qu'il est mort entre leurs mains sans livrer le gang."),
        two("He is played by Howard Pinhasik, an American actor.",
            "Il est interprété par Howard Pinhasik, acteur américain."),
    ],
    "essentials": [
        two("The gang's bookkeeper and money lender; he sends Arthur after his debtors in seven \"Money Lending and Other Sins\" missions, from chapter 2 to chapter 6.",
            "Comptable et usurier de la bande ; il envoie Arthur chez ses débiteurs dans sept missions \"Money Lending and Other Sins\", du chapitre 2 au chapitre 6."),
        two("The Downes debt: Thomas Downes coughs blood on Arthur during the collection, and after his death Strauss passes the debt to his widow, Edith.",
            "La dette des Downes : Thomas Downes crache du sang sur Arthur pendant le recouvrement, et à sa mort, Strauss reporte la dette sur sa veuve, Edith."),
        two("Held hostage with John by [[leviticus-cornwall|Leviticus Cornwall]]'s men in Valentine, he is shot in the leg; later he signals to Arthur how to play at the rigged poker table of the Grand Korrigan riverboat.",
            "Pris en otage avec John par les hommes de [[leviticus-cornwall|Leviticus Cornwall]] à Valentine, il reçoit une balle dans la jambe ; plus tard, il indique à Arthur comment jouer à la table de poker truquée du Grand Korrigan."),
        two("Thrown out by Arthur at Beaver Hollow, or leaves on his own, depending on the player; in 1907 Charles reports that he died in Pinkerton custody without talking.",
            "Chassé par Arthur à Beaver Hollow, ou parti de lui-même, selon les choix du joueur ; en 1907, Charles rapporte qu'il est mort aux mains de la Pinkerton sans avoir parlé."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["arthur-morgan", "dutch-van-der-linde", "hosea-matthews", "charles-smith"],
}
