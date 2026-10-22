"""Sister Calderón, reference fiche, PART D: base data, Development and performance, Reception (22 Oct 2026, medium tier).

Her queued page (_queue/50-sister-calderon/, publishDate 2026-10-29, not yet live) was generated from the v2 entry in
scripts/_wave7.py ("slug": "sister-calderon"; no entry in _enrich.py). The base below is rebuilt from that entry.
publishDate 2026-10-29, the eyebrow ("Character &middot; Saint Denis"), portrait_alt and "related" are kept; reg_role
matches characters_registry.py ("Nun &middot; RDR1 &amp; 2"). schema_game stays "Red Dead Redemption 2".
Changes against v2:
- v2 "Catholic nun at the Church of the Holy Blessed Virgin in Saint Denis" stated as fact: the church's name comes from
  the Red Dead Wiki (in the game, Dorkins mentions "the old church on Gaspar Street in St. Frances" and she is found
  at the cathedral): attributed in the facts grid.
- v2 "In Red Dead Redemption, set in 1911, she is the Mother Superior of a convent in Mexico" stated the identity of the
  two characters as fact. Now worded through the in-game hooks (she gives her name as Calderón in RDR2 and, per guides,
  in Undead Nightmare; she leaves for a mission in Mexico in 1899) and the Red Dead Wiki's treatment of them as one.
- v2 "Irene DeBari in Red Dead Redemption 2": kept, now attributed to cast listings; for Red Dead Redemption the credit
  is the Red Dead Wiki's only (see below).
- v2 Emerald Station quote "Take a gamble that love exists, and do a loving act." moves to part C Quotes (with the
  transcript's ellipsis); the base no longer quotes it.
- Chips: "Catholic Church" replaced by "Nun, later mother superior"; "Played by" chip added. Facts grid gains Name,
  Also called, Born, Nationality, Occupation, Family, Associates, Played by.
- "Behind the scenes" (v2 section) is replaced by Development and performance + Reception.

SOURCE REGISTER (fetched 22 Oct 2026, saved in scripts/v3/work/calderon/fc/):
- English Voice-Over Wiki, cast list "Red Dead Redemption II (2018)" (fc/evo_rdr2.txt): "Sister Calderón - Irene
  DeBari" (beside "Brother Dorkins - Max Eddy"). Cast list "Red Dead Redemption (2010)" (fc/evo_rdr1.txt): no Mother
  Superior entry; "Nun - Begonya Plaza".
- Red Dead Wiki EN "Mother Superior Calderón" (infobox: voice Irene DeBari, one field for all games) and FR "Mère
  Supérieure Calderón" (acteur Irene DeBari). Red Dead Wiki EN "Nun" (RDR1's generic nuns: voice Begonya Plaza).
- GTABase, "Sister Calderón" character page (RDR2, undated): "She is portrayed by Irene DeBari."
- Wikipedia, "Irene DeBari" (raw wikitext, fc/wp_irene_debari.txt): American television actress; career began in 1967;
  played Rosa Calletano in Hill Street Blues, credited as Irena Du Barry; also credited as Irene De Bari and Irene
  Rosetti. No game credit listed. Wikipedia's "List of Red Dead Redemption 2 characters" has no entry for her.
- IMDb (search-result snippet only; the page returns 403): "Red Dead Redemption (Video Game 2010) - Begonya Plaza as
  Nun". MobyGames and Behind The Voice Actors: blocked (403). Summary in fc/voice_sources.txt.
- Undead Nightmare name: ireddead.com walkthrough "Mother Superior Blues" and the Italian localisation line "Madre
  superiora Calderón" quoted by reddead-series.com (fc/undead_nightmare_sources.txt, gathered by the part A drafter).
- Red Dead Wiki EN character page, Trivia: dialogue for being hogtied with the lasso was planned and cut.
- Game Rant, Christian Harrison, "One Life-Changing Moment in Red Dead 2 Happens at a Train Station, and That's No
  Coincidence", feature, 6 Mar 2021 (fc/gr_train.txt): calls her Mother Superior Calderon; contrasts the Swanson
  meeting as "a stark and nihilistic contradiction to Arthur's interaction with Mother Superior Calderón"; reads her
  "There is nothing to be afraid of" as applying to the West.
- RDR2.org, Ray Ampoloquio, "A High School Graduate Just Quoted Red Dead Redemption 2 in Her Speech", 6 Jul 2026
  (fc/rdr2org.txt): the scene is "one of its most quietly powerful"; "a small, unshowy exchange".
- Full RDR2 transcript (fc/gsw.txt) and wiki transcripts for the base facts ("Calderón.", "on my way down to Mexico",
  "My husband died a long time ago").

EXCLUDED: Irene DeBari as the voice of the Red Dead Redemption (2010) Mother Superior stated as fact (no credits list
confirms it; only the Red Dead Wiki says so: attributed); Begonya Plaza as her voice (the credit is for "Nun", which the
Red Dead Wiki gives to the generic nuns); any motion capture claim (no source); DeBari's birth date and place (none
published); the wiki talk pages on the merge (fan discussion, not a source); RDR2.org's remark on Dan Houser (about the
game, not this scene); the graduate's identity (private person); Game Rant's reading of the scene as a metaphor for the
end of the West, beyond the one attributed sentence; the month of June 1899 for her departure (wiki only, part A);
"the convent she was sent to twelve years prior" (wiki reading: not stated in either game).
DUPLICATE ownership: voice credits, the identity hooks, cut content and reviews live HERE; part C Trivia and Other media
must not repeat the cut lasso dialogue or the reviews. Part C "Other media" tells the release history (2010, 2018,
2023, 2024): not repeated here.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Voice", "Voix")},
    {"p": two("In Red Dead Redemption 2 (2018), Sister Calderón is voiced by Irene DeBari, according to the game's cast listings (English Voice-Over Wiki, GTABase) and the Red Dead Wiki. Wikipedia describes DeBari as an American television actress whose career began in 1967. She played Rosa Calletano, the wife of Lieutenant Ray Calletano, in Hill Street Blues, credited at the time as Irena Du Barry; she has also been credited as Irene De Bari and Irene Rosetti.",
              "Dans Red Dead Redemption 2 (2018), sœur Calderón a la voix d'Irene DeBari, d'après les listes de distribution du jeu (English Voice-Over Wiki, GTABase) et le Red Dead Wiki. Wikipédia présente DeBari comme une actrice de télévision américaine dont la carrière a commencé en 1967. Elle a joué Rosa Calletano, l'épouse du lieutenant Ray Calletano, dans Hill Street Blues, créditée à l'époque sous le nom d'Irena Du Barry ; elle a aussi été créditée comme Irene De Bari et Irene Rosetti.")},
    {"p": two("For Red Dead Redemption (2010) and Undead Nightmare, the English and French Red Dead Wikis also credit Irene DeBari, in a single field covering every game. The cast list of the 2010 game consulted for this page has no entry for the Mother Superior; it credits a role named \"Nun\" to Begonya Plaza, whom the Red Dead Wiki gives as the voice of the game's ordinary nuns. No source found for this page says whether the role also involved motion capture.",
              "Pour Red Dead Redemption (2010) et Undead Nightmare, les Red Dead Wiki anglophone et francophone créditent eux aussi Irene DeBari, dans un champ unique qui vaut pour tous les jeux. La liste de distribution du jeu de 2010 consultée pour cette page ne mentionne pas la mère supérieure ; elle attribue un rôle intitulé \"Nun\" (religieuse) à Begonya Plaza, que le Red Dead Wiki donne comme voix des religieuses ordinaires du jeu. Aucune des sources réunies ici ne précise si le rôle a aussi donné lieu à une capture de mouvement.")},
    {"h3": two("From the 2010 game to the prequel", "Du jeu de 2010 à la préquelle")},
    {"p": two("Red Dead Redemption 2 ties its Saint Denis nun to the 2010 character through the dialogue. She gives her name, Calderón, in \"Of Men and Angels\". In \"The Fine Art of Conversation\" she tells Arthur she is on her way down to Mexico, where she is finally being sent on a mission. In Undead Nightmare, the Mother Superior of Las Hermanas introduces herself as Mother Superior Calderón, according to the ireddead.com walkthrough and the expansion's Italian version. The Red Dead Wiki treats the nun of 1899 and the mother superior of 1911 as one character, under the title \"Mother Superior Calderón\".",
              "Red Dead Redemption 2 relie sa religieuse de Saint-Denis au personnage de 2010 par les dialogues. Elle donne son nom, Calderón, dans \"Of Men and Angels\". Dans \"The Fine Art of Conversation\", elle annonce à Arthur qu'elle part pour le Mexique, où on l'envoie enfin en mission. Dans Undead Nightmare, la mère supérieure de Las Hermanas se présente comme la mère supérieure Calderón, d'après la soluce d'ireddead.com et la version italienne de l'extension. Le Red Dead Wiki traite la religieuse de 1899 et la mère supérieure de 1911 comme un seul et même personnage, sous le titre \"Mother Superior Calderón\".")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("According to the Red Dead Wiki, Red Dead Redemption 2 was meant to give her lines for when the player hogties her with the lasso. This dialogue was cut from the final game.",
              "D'après le Red Dead Wiki, Red Dead Redemption 2 devait lui donner des répliques pour le cas où le joueur la ligote au lasso. Ces dialogues ont été retirés du jeu final.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("The Emerald Station scene", "La scène de la gare d'Emerald")},
    {"p": two("Game Rant devoted a feature to her meeting with Arthur, written by Christian Harrison and published on 6 March 2021 under the title \"One Life-Changing Moment in Red Dead 2 Happens at a Train Station, and That's No Coincidence\". The article retells the scene, in which Arthur is honest with himself for the first time about the life he has led. It compares it with the meeting that replaces it when Arthur's honor is low, calling Swanson's advice \"a stark and nihilistic contradiction to Arthur's interaction with Mother Superior Calderón\".",
              "Game Rant a consacré un article de fond à sa rencontre avec Arthur, signé Christian Harrison et publié le 6 mars 2021 sous le titre \"One Life-Changing Moment in Red Dead 2 Happens at a Train Station, and That's No Coincidence\". L'article reprend la scène, où Arthur se montre pour la première fois honnête avec lui-même sur la vie qu'il a menée. Il la compare à la rencontre qui la remplace quand l'honneur d'Arthur est bas, et juge les conseils de Swanson \"a stark and nihilistic contradiction to Arthur's interaction with Mother Superior Calderón\" (en contradiction totale et nihiliste avec l'échange entre Arthur et la mère supérieure Calderón).")},
    {"p": two("On 6 July 2026, RDR2.org reported, in an article by Ray Ampoloquio, that a high school graduate of the class of 2026 had built her commencement speech around the line the nun gives Arthur at the station. The site called the scene \"one of its most quietly powerful\" and \"a small, unshowy exchange\" in a game better known for bank robberies and shootouts.",
              "Le 6 juillet 2026, RDR2.org a rapporté, dans un article de Ray Ampoloquio, qu'une lycéenne de la promotion 2026 avait construit son discours de remise de diplômes autour de la phrase que la religieuse adresse à Arthur à la gare. Pour le site, cette scène est l'une des plus fortes du jeu dans sa retenue (\"one of its most quietly powerful\"), et \"a small, unshowy exchange\" (un échange modeste, sans effets), dans un jeu surtout connu pour ses braquages et ses fusillades.")},
]


BASE = {
    "slug": "sister-calderon", "name": "Sister Calderón",
    "publishDate": "2026-10-29", "updated": "2026-10-22", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Nun &middot; RDR1 &amp; 2", "reg_role_fr": "Religieuse &middot; RDR1 &amp; 2",
    "gender": "Female", "birth": None, "death": None, "nationality": None,
    "portrait_alt": two("Sister Calderón in Saint Denis in Red Dead Redemption 2",
                        "Sœur Calderón à Saint-Denis dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Saint Denis", "Personnage &middot; Saint-Denis"),
    "meta_desc": two("Sister Calderón, the Saint Denis nun Arthur Morgan confides in at Emerald Station in RDR2, and the mother superior of Las Hermanas in Red Dead Redemption: story, quotes, voice.",
                     "Sœur Calderón, la religieuse de Saint-Denis à qui Arthur Morgan se confie à la gare d'Emerald dans RDR2, et la mère supérieure de Las Hermanas dans Red Dead Redemption : histoire, citations, voix."),
    "og_desc": two("The complete reference on Sister Calderón: Saint Denis, Emerald Station, Las Hermanas, quotes, voice and reception.",
                   "La référence complète sur sœur Calderón : Saint-Denis, la gare d'Emerald, Las Hermanas, citations, voix et accueil."),
    "schema_desc": two("Catholic nun in Saint Denis who meets Arthur Morgan in 1899 and leaves for a mission in Mexico in Red Dead Redemption 2; the Red Dead Wiki identifies her with the mother superior of Las Hermanas in Red Dead Redemption.",
                       "Religieuse catholique de Saint-Denis qui croise Arthur Morgan en 1899 et part en mission au Mexique dans Red Dead Redemption 2 ; le Red Dead Wiki l'identifie à la mère supérieure de Las Hermanas dans Red Dead Redemption."),
    "chips": [two("Nun, later mother superior", "Religieuse, puis mère supérieure"),
              two("Saint Denis &middot; Las Hermanas", "Saint-Denis &middot; Las Hermanas"),
              two("RDR1 &amp; 2", "RDR1 &amp; 2"),
              two("Voiced by <strong>Irene DeBari</strong>", "Voix : <strong>Irene DeBari</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Calderón (no first name in the games)", "Calderón (aucun prénom dans les jeux)")},
        {"label": two("Also called", "Autres noms"), "value": two("Sister; Mother Superior; Mother Superior Calderón (Undead Nightmare, Red Dead Wiki)", "Sister ; Mother Superior ; mère supérieure Calderón (Undead Nightmare, Red Dead Wiki)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the games", "Non précisée dans les jeux")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1911", "Vivante en 1911")},
        {"label": two("Nationality", "Nationalité"), "value": two("Not given in the games", "Non précisée dans les jeux")},
        {"label": two("Occupation", "Activité"), "value": two("Catholic nun in Saint Denis (1899); mother superior at Las Hermanas (1911)", "Religieuse catholique à Saint-Denis (1899) ; mère supérieure à Las Hermanas (1911)")},
        {"label": two("Church", "Église"), "value": two("Saint Denis; the Church of the Holy Blessed Virgin, according to the Red Dead Wiki", "Saint-Denis ; la Church of the Holy Blessed Virgin, d'après le Red Dead Wiki")},
        {"label": two("In 1911", "En 1911"), "value": two("Las Hermanas convent, Perdido, Nuevo Paraíso", "Couvent de Las Hermanas, Perdido, Nuevo Paraíso")},
        {"label": two("Family", "Famille"), "value": two("Her mother and her husband, both unnamed and dead before 1899", "Sa mère et son mari, tous deux anonymes et morts avant 1899")},
        {"label": two("Associates", "Proches"), "value": two("Brother Dorkins; Father O'Leary; [[arthur-morgan|Arthur Morgan]]; [[john-marston|John Marston]]", "Frère Dorkins ; le père O'Leary ; [[arthur-morgan|Arthur Morgan]] ; [[john-marston|John Marston]]")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption (2010), Undead Nightmare (2010), Red Dead Redemption 2 (2018)", "Red Dead Redemption (2010), Undead Nightmare (2010), Red Dead Redemption 2 (2018)")},
        {"label": two("Voiced by", "Voix"), "value": two("Irene DeBari (RDR2, cast listings; RDR1 according to the Red Dead Wiki)", "Irene DeBari (RDR2, listes de distribution ; RDR1 d'après le Red Dead Wiki)")},
    ],
    "intro": [
        two("Sister Calderón is a Catholic nun in Saint Denis in Red Dead Redemption 2 (2018), set in 1899. She teaches street children to read with Brother Dorkins and collects money and food for the poor. [[arthur-morgan|Arthur Morgan]] recovers her stolen crucifix in chapter 4 and gives to her collection in an optional mission. If his honor is high, he meets her again at Emerald Station in chapter 6, as she leaves for a mission in Mexico; there he tells her that he is dying. Otherwise, [[orville-swanson|Orville Swanson]] appears in her place.",
            "Sœur Calderón est une religieuse catholique de Saint-Denis dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Elle apprend à lire à des enfants des rues avec frère Dorkins et fait la quête pour les pauvres. [[arthur-morgan|Arthur Morgan]] récupère son crucifix volé au chapitre 4, puis donne à sa quête dans une mission facultative. Si son honneur est élevé, il la retrouve au chapitre 6 à la gare d'Emerald, alors qu'elle part en mission au Mexique ; il lui avoue qu'il va mourir. Sinon, c'est [[orville-swanson|Orville Swanson]] qui apparaît à sa place."),
        two("In Red Dead Redemption (2010), set in 1911, the mother superior of the Las Hermanas convent asks [[john-marston|John Marston]] for alms, and in the non-canon Undead Nightmare she helps him against the plague. The Red Dead Wiki treats the two as one character. Irene DeBari voices her in Red Dead Redemption 2.",
            "Dans Red Dead Redemption (2010), qui se déroule en 1911, la mère supérieure du couvent de Las Hermanas demande l'aumône à [[john-marston|John Marston]] et, dans Undead Nightmare, hors canon, elle l'aide à combattre l'épidémie. Le Red Dead Wiki fait des deux un seul et même personnage. Irene DeBari lui prête sa voix dans Red Dead Redemption 2."),
    ],
    "essentials": [
        two("She gives only her surname, Calderón; no game gives her a first name, a birth date or a nationality.",
            "Elle ne donne que son nom, Calderón ; aucun jeu ne lui attribue de prénom, de date de naissance ni de nationalité."),
        two("In \"Brothers and Sisters, One and All\" (chapter 4), Arthur gets back the crucifix her mother gave her.",
            "Dans \"Brothers and Sisters, One and All\" (chapitre 4), Arthur récupère le crucifix que sa mère lui avait donné."),
        two("In \"Of Men and Angels\", Arthur gives her food or 10 dollars for the poor; the mission must be done before \"The Fine Art of Conversation\".",
            "Dans \"Of Men and Angels\", Arthur lui donne de la nourriture ou 10 dollars pour les pauvres ; la mission doit être faite avant \"The Fine Art of Conversation\"."),
        two("At Emerald Station, with high honor, Arthur tells her he has tuberculosis and is afraid, before she boards a train for Mexico.",
            "À la gare d'Emerald, avec un honneur élevé, Arthur lui avoue qu'il a la tuberculose et qu'il a peur, avant qu'elle ne monte dans un train pour le Mexique."),
        two("In Red Dead Redemption (1911), John can give 10 dollars to the mother superior of Las Hermanas, in Nuevo Paraíso, or rob her (\"I Know You\"); the Red Dead Wiki identifies her with the Saint Denis nun.",
            "Dans Red Dead Redemption (1911), John peut donner 10 dollars à la mère supérieure de Las Hermanas, au Nuevo Paraíso, ou la dévaliser (\"I Know You\") ; le Red Dead Wiki l'identifie à la religieuse de Saint-Denis."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["arthur-morgan", "orville-swanson", "john-marston", "rains-fall"],
}
