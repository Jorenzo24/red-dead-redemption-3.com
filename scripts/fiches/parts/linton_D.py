"""Mary Linton, reference fiche, PART D: base data, Development and performance (20 Oct 2026, medium tier).

Her live page (characters/mary-linton/) was generated from the v2 entry in scripts/_wave2.py
("slug": "mary-linton"; no entry of her own in _enrich.py). The base below is rebuilt from that entry, with
corrections: the v2 intro called her Arthur's "great love" and said she "represents the ordinary, settled
life Arthur gave up for the gang" (interpretation, dropped); the v2 text called her father "ailing" (he is
not shown ill: he drinks, gambles and pawns family property) and said their reunions are "warm but
painful" (mood prose, dropped); the v2 "Behind the scenes" paragraph called her missions "companion
missions" (they are Stranger/honor story missions given by her) and is replaced by a sourced Development
section. The facts grid gains Born name, Family, Played by and the end-credits status; the "Widow" chip is
kept. Eyebrow (kicker) kept as on the live page ("Character &middot; Red Dead Redemption 2"); reg_role
matches characters_registry.py. publishDate 2026-07-02 kept (git: 143dfeb, drip publish of mary-linton,
2 Jul 2026; the live byline shows an older generator date).

Sources (internal register, fetched 20 Oct 2026):
- Red Dead Wiki "Mary Linton" (infobox: voice Julie Jesneck; family Mr. Gillis, unnamed mother (dead),
  Jamie Gillis, Arthur Morgan (ex-fiancé), Barry Linton (husband, dead); nationality American).
  Wikipedia "List of Red Dead Redemption 2 characters", Supporting characters: "Arthur's former partner,
  Mary Linton (Julie Jesneck)" (saved in linton/fc/wp_list.txt). No Wikipedia article on Jesneck; no
  interview in which she discusses the role was found (web searches, 20 Oct 2026).
- Roger Clark on performing Mary's grave scene in motion capture: reported by Vida Extra on 26 Nov 2024,
  already used in the fact-checked arthur_F.py; also reported by GamePro (Germany; page behind Cloudflare,
  date not read, so not cited). Wiki trivia cites two YouTube shorts by Clark.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (saved fc/Red_Dead_Redemption_2_Cut_Content.txt):
  Rhodes saloon meeting ("MRY2", "FLME"; she "may kill her" line paraphrased; "rflme_debt_man" model),
  unused Chelonian for "We Loved Once and True" ("msp_mary1_males_01"), two unused hats, Leon Fuentes's
  niece (same dress model and textures, near-identical funeral hat with a veil; Mary's funeral outfit uses
  the niece's hair), "Gunslinger's Widow" (hair, boots, funeral hat similar to Mary's), Mr. Gillis named
  "Mr. Linton" and Jamie referred to as a "Linton" in the files.
Reception: no review or article discussing Mary was found (searches 20 Oct 2026: reviews, Kotaku, Polygon,
GamesRadar, PC Gamer; only fan blogs and forums); BLOCKS_RECEPTION is empty and the section is omitted.
Excluded: the wiki's reading that the debt-collector model means the men "would've been debtors" (it
"appears"; only the model name is given); Edith Downes wearing Mary's hat in a trailer (not about Mary);
Jesneck's other credits (database listings only, no reliable source); motion capture by Jesneck herself
(no source states it; the credits and wiki say voice).
DUPLICATE ownership: actress, the Clark grave-scene anecdote and cut content (including the "Linton" file
names of Mr. Gillis and Jamie) live HERE; part C trivia must not repeat them.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Mary is played by Julie Jesneck, who is credited in the role by the Red Dead Wiki and by Wikipedia's list of the game's characters.",
              "Mary est interprétée par Julie Jesneck, que le Red Dead Wiki et la liste des personnages du jeu sur Wikipédia créditent dans ce rôle.")},
    {"p": two("Mary's last scene, her visit to Arthur's grave during the end credits, has no dialogue. Roger Clark, who plays Arthur, told IGN that Jesneck was not available for that scene and that he performed Mary's movements in motion capture himself; a scene without dialogue, he explained, can be played by another actor (reported by Juan Sanmartín in Vida Extra on November 26, 2024).",
              "La dernière scène de Mary, sa visite sur la tombe d'Arthur pendant le générique de fin, ne comporte aucun dialogue. Roger Clark, l'interprète d'Arthur, a expliqué à IGN que Jesneck n'était pas disponible pour cette scène et qu'il a donc joué lui-même les gestes de Mary en capture de mouvement ; une scène sans dialogue, précise-t-il, peut être tenue par un autre acteur (propos rapportés par Juan Sanmartín dans Vida Extra le 26 novembre 2024).")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The game files keep traces of an unused meeting between Arthur and Mary at the saloon in Rhodes, where she has rented a room, according to the Red Dead Wiki's page on cut content. Its text and animations are filed under the labels \"MRY2\" and \"FLME\". An unused letter left in the files has Mary ask Arthur to help her in Rhodes, and the leftover text has her say that the people she is hiding from may kill her if he does not. According to the wiki, a character model named \"rflme_debt_man\" suggests that those men were after a debt. The files also hold an unused Chelonian intended for \"We Loved Once and True\" and two unused hats for Mary.",
              "Les fichiers du jeu gardent la trace d'une rencontre inutilisée entre Arthur et Mary au saloon de Rhodes, où elle a loué une chambre, d'après la page du Red Dead Wiki consacrée au contenu coupé. Ses textes et ses animations sont classés sous les étiquettes \"MRY2\" et \"FLME\". Une lettre inutilisée restée dans les fichiers montre Mary demandant à Arthur de venir l'aider à Rhodes, et le texte restant lui fait dire que les gens qu'elle fuit risquent de la tuer s'il ne l'aide pas. D'après le wiki, un modèle de personnage nommé \"rflme_debt_man\" laisse penser que ces hommes venaient réclamer une dette. Les fichiers contiennent aussi un Chélonien inutilisé prévu pour \"We Loved Once and True\" et deux chapeaux inutilisés pour Mary.")},
    {"p": two("Two cut characters wear clothes identical or close to hers. The niece of Leon Fuentes, who was to be rescued on Guarma by Arthur and Bill, wears the same dress model and textures as Mary and a funeral hat almost identical to hers, with a veil added. Mary's funeral outfit in turn uses the niece's hairstyle. A character labeled \"Gunslinger's Widow\" has hair, boots and a funeral hat similar to Mary's. In the files, her father is named \"Mr. Linton\" instead of Mr. Gillis, and her brother Jamie is also referred to as a Linton.",
              "Deux personnages coupés portent des vêtements identiques ou proches des siens. La nièce de Leon Fuentes, qu'Arthur et Bill devaient secourir à Guarma, porte le même modèle de robe et les mêmes textures que Mary, ainsi qu'un chapeau de deuil presque identique au sien, voilette en plus. La tenue de deuil de Mary reprend en retour la coiffure de cette nièce. Un personnage baptisé \"Gunslinger's Widow\" (la veuve du pistolero) dispose de cheveux, de bottes et d'un chapeau de deuil proches de ceux de Mary. Dans les fichiers, son père s'appelle \"Mr. Linton\" et non M. Gillis, et son frère Jamie est lui aussi désigné sous le nom de Linton.")},
]

BLOCKS_RECEPTION = []


BASE = {
    "slug": "mary-linton", "name": "Mary Linton",
    "publishDate": "2026-07-02", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Arthur's former love &middot; RDR2", "reg_role_fr": "Ancien amour d'Arthur &middot; RDR2",
    "gender": "Female", "death": None, "nationality": None,
    "portrait_alt": two("Mary Linton in Red Dead Redemption 2", "Mary Linton dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Red Dead Redemption 2", "Personnage &middot; Red Dead Redemption 2"),
    "meta_desc": two("Mary Linton (née Gillis), Arthur Morgan's former fiancée in RDR2: her brother Jamie and the Chelonians, her father in Saint Denis, her last letter and the ring, Julie Jesneck.",
                     "Mary Linton (née Gillis), l'ancienne fiancée d'Arthur Morgan dans RDR2 : son frère Jamie et les Chéloniens, son père à Saint-Denis, sa dernière lettre et la bague, Julie Jesneck."),
    "og_desc": two("The complete reference on Mary Linton: life, letters, relationships, quotes and development.",
                   "La référence complète sur Mary Linton : vie, lettres, relations, citations et conception."),
    "schema_desc": two("Former fiancée of Arthur Morgan, widowed by 1899, who asks him to bring her brother back from a cult and to help with her father, then returns his engagement ring by letter, in Red Dead Redemption 2.",
                       "Ancienne fiancée d'Arthur Morgan, veuve en 1899, qui lui demande de ramener son frère d'une secte et de l'aider avec son père, puis lui renvoie sa bague de fiançailles par lettre, dans Red Dead Redemption 2."),
    "chips": [two("Arthur's former fiancée", "Ancienne fiancée d'Arthur"), two("Widow", "Veuve"),
              two("Alive", "En vie"),
              two("Played by <strong>Julie Jesneck</strong>", "Interprétée par <strong>Julie Jesneck</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Mary Linton", "Mary Linton")},
        {"label": two("Born name", "Nom de naissance"), "value": two("Mary Gillis", "Mary Gillis")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Status", "Statut"), "value": two("Alive; seen at Arthur's grave in the end credits", "En vie ; aperçue sur la tombe d'Arthur pendant le générique de fin")},
        {"label": two("Nationality", "Nationalité"), "value": two("Not stated in the game (American according to the Red Dead Wiki)", "Non précisée dans le jeu (américaine selon le Red Dead Wiki)")},
        {"label": two("Family", "Famille"), "value": two("Mr. Gillis (father), her mother (deceased), Jamie Gillis (younger brother), Barry Linton (husband, deceased)", "M. Gillis (père), sa mère (décédée), Jamie Gillis (petit frère), Barry Linton (mari, décédé)")},
        {"label": two("Former fiancé", "Ancien fiancé"), "value": two("[[arthur-morgan|Arthur Morgan]]", "[[arthur-morgan|Arthur Morgan]]")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Julie Jesneck", "Julie Jesneck")},
    ],
    "intro": [
        two("Mary Linton, born Mary Gillis, is a supporting character in Red Dead Redemption 2 (2018), set in 1899. She was engaged to [[arthur-morgan|Arthur Morgan]] when they were young, and the engagement ended years before the game. She later married Barry Linton, who has since died. In chapter 2 she writes to Arthur from Valentine and asks him to bring her brother Jamie back from the Chelonians, a cult. In chapter 4 she asks for his help with her father in Saint Denis. In chapter 6 her last letter returns the engagement ring Arthur gave her. During the end credits she is seen at Arthur's grave.",
            "Mary Linton, née Mary Gillis, est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Elle a été fiancée à [[arthur-morgan|Arthur Morgan]] dans leur jeunesse, et les fiançailles ont pris fin des années avant le jeu. Elle a ensuite épousé Barry Linton, mort depuis. Au chapitre 2, elle écrit à Arthur depuis Valentine et lui demande de ramener son frère Jamie de chez les Chéloniens, une secte. Au chapitre 4, elle sollicite son aide à Saint-Denis au sujet de son père. Au chapitre 6, sa dernière lettre renvoie à Arthur la bague de fiançailles qu'il lui avait offerte. Pendant le générique de fin, on la voit sur la tombe d'Arthur."),
        two("She is played by Julie Jesneck.",
            "Elle est interprétée par Julie Jesneck."),
    ],
    "essentials": [
        two("She and Arthur were engaged when young; her family, her father above all, disapproved, and the engagement ended before 1899.",
            "Arthur et elle se sont fiancés jeunes ; sa famille, son père en tête, désapprouvait, et les fiançailles ont pris fin avant 1899."),
        two("In \"We Loved Once and True\", she asks Arthur to bring her brother Jamie back from the Chelonians; the player can refuse.",
            "Dans \"We Loved Once and True\", elle demande à Arthur de ramener son frère Jamie de chez les Chéloniens ; le joueur peut refuser."),
        two("In \"Fatherhood and Other Dreams\", in Saint Denis, Arthur recovers her late mother's brooch, sold by her father to a loan shark.",
            "Dans \"Fatherhood and Other Dreams\", à Saint-Denis, Arthur récupère la broche de sa défunte mère, vendue par son père à un usurier."),
        two("Her last letter returns Arthur's engagement ring; in 1907 [[john-marston|John Marston]] proposes to [[abigail-marston|Abigail]] with it.",
            "Sa dernière lettre rend à Arthur sa bague de fiançailles ; en 1907, [[john-marston|John Marston]] demande [[abigail-marston|Abigail]] en mariage avec cette bague."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["arthur-morgan", "abigail-marston", "john-marston", "mary-beth-gaskill"],
}
