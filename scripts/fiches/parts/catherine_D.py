"""Catherine Braithwaite, reference fiche, PART D: base data, Development and performance, Reception
(22 Oct 2026, medium tier).

Her live page (characters/catherine-braithwaite/) was generated from the v2 entry in scripts/_wave7.py
("slug": "catherine-braithwaite"; no entry in _enrich.py). The base below is rebuilt from that entry. publishDate
2026-10-11 and the eyebrow ("Character &middot; Lemoyne") are kept as on the live page; reg_role matches
characters_registry.py ("Braithwaite matriarch &middot; RDR2"). Changes against v2:
- v2 said the Braithwaites kidnap Jack "after the Grays' ambush in Rhodes, in which Sean is killed", as revenge for
  it. The game gives another motive: the gang concludes the kidnapping is revenge for the stolen horses, and Catherine
  herself says "You stole my liquor. You stole my horses." (transcript; consistent with jack_A, dutch_A, abigail_A).
- v2 "main antagonist of chapter 3" (the wiki's label) and "Her family is locked in a feud ... for generations" kept
  only as facts the game states (Archibald, Beau, Catherine's "a hundred and twenty years").
- v2 "an old plantation family of English descent": the English origin is the Red Dead Wiki's (family page), so it is
  not stated in the base; "old cotton family" is Archibald's phrase, quoted in part B.
- Chips: "Braithwaite family" and "RDR2" replaced by "Died 1899", "Braithwaite matriarch", "Scarlett Meadows" and the
  actress. Facts grid gains Name, Also called, Born, Died, Nationality, Occupation, Associates, Enemies, Played by.
- "Behind the scenes" (v2 section) is replaced by Development and performance; the Red Dead Online mention moves to
  part C (Other media) and to the facts grid ("mentioned in Red Dead Online").
NOTE FOR THE LEAD (story guide, not fixed here): story/rdr2-chapter-3-clemens-point says that "In the ruins" Catherine
"reveals that she has sold Jack" to Bronte. In the game she speaks outside the burning house and says "My sons gave him
to Angelo Bronte"; "sold" is the wiki's word. Same wording in the guide's key events ("has been sold"). FR to check too.

SOURCE REGISTER (fetched 22 Oct 2026, saved in scripts/v3/work/catherine/fc/):
- Wikipedia, "List of Red Dead Redemption 2 characters" (fc/wp_list_rdr2.txt), citing the game's credits: Catherine
  Braithwaite (Ellen Harvey), Leigh Gray (Tim McGeever), Penelope Braithwaite (Alison Barton), Beau Gray (Bjorn
  Thorstad). Hosea section: Game Informer staff on Hosea mocking Catherine.
- Red Dead Wiki "Ellen Harvey" (scripts/v3/work/_m/Ellen_Harvey.txt): voice and motion-capture actor of Catherine;
  known for House of Cards and Gotham (birth date and place given by the wiki only: not used). Wiki pages
  "Bartholomew Braithwaite" (voice: Michael Cuddire), "Gertrude Braithwaite" (Reyna de Courcy), "Gareth Braithwaite"
  (Beau Baxter): wiki-only credits, attributed.
- BroadwayWorld and Kennedy Center performer pages (search result summaries, 22 Oct 2026): an actress named Ellen
  Harvey with Broadway credits and guest roles in House of Cards (Martha Wilson, 2016) and Gotham (Judge Turnball).
  NOT used to identify the RDR2 actress (no page links her to the game); the identification stays attributed to the
  Red Dead Wiki.
- Twinfinite, Ed McGlone, "Red Dead Redemption 2 Interview: The Actor Behind Dutch Discusses 'The Plan', Pivotal Story
  Moments, & Reprising His Role", 19 Feb 2019 (archived copy of 5 May 2019, fc/twinf.txt). Question: "What was the
  turning point that puts him on the path of being the villain?" Benjamin Byron Davis: "Dutch keeps encountering men
  who occupy the states that Dutch imagines he wants to occupy. He encounters this sort of queen in Catherine
  Braithwaite, and most notably when the game gets to Saint Denis ... Bronte".
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (scratchpad cov/abigail/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt):
  unused hair for Catherine; a cut Braithwaite servant and maid; an unused vest for the Braithwaite butler; Gray and
  Braithwaite family members originally encountered in free roam.
- WhatCulture, Matt Thompson, "Red Dead Redemption: Every Villain Ranked From Worst To Best", 7 Feb 2022 (all 15 pages
  fetched, fc/wc_*.html; page 10 = Catherine, fc/wc_10.txt): 6th of 15, between Colm O'Driscoll (7th) and the Murfree
  Brood (5th) in a countdown list (fix pass 22 Oct 2026). Quotes: "the cantankerous head of an estate that once thrived off slavery"; "The malice and
  vitriol of Catherine Braithwaite is so ripe with anger, we almost want her to keep around longer"; the assault
  "still ranks as one of RDR2 fans' biggest and best missions".
- Game Informer staff, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", 27 Dec 2018
  (scratchpad cov/abigail/fc/gi_ranking.txt): Hosea "mocks Catherine Braithwaite as her life burns down around her".
- WatchMojo, Mathew Arter, "The 10 Most Satisfying Kills In Red Dead Redemption 2", 15 Mar 2023 (fc/wm.txt): "This
  old biddy is the worst!"; "She is tough, we'll give her that".
- In-game transcript (fc/gsw.txt, see part B) for the base facts: "Mrs. Catherine Braithwaite", "Aunt Catherine",
  "You stole my liquor. You stole my horses.", "My sons gave him to Angelo Bronte".

EXCLUDED: Davis's remark in the same Twinfinite interview about forgiving "someone who will kill a woman's son in front
of her" (he names no one; linking it to Catherine would be our inference); Ellen Harvey's birth date and place (Red
Dead Wiki only); "motion capture" stated as fact (only the Red Dead Wiki says so: attributed); WhatCulture's
claim that the family "supposedly dabbles heavily in incest" and WatchMojo's claim that she let her daughter starve
(neither is shown in the game); the "unused leg models" item of the cut content page (not specific to her); the
second trailer showing the burning manor (part C, Other media); the Villains Wiki (not a usable source).
DUPLICATE ownership: actress, Davis's remark, cut content and reviews live HERE; part C trivia must not repeat them.
Reception does not repeat Davis's remark.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Catherine Braithwaite appears only in Red Dead Redemption 2 (2018). The game's credits, as listed by Wikipedia, give the role to Ellen Harvey. The Red Dead Wiki presents her as an actress known for House of Cards and Gotham, and says she provided both the voice and the motion capture of the character.",
              "Catherine Braithwaite n'apparaît que dans Red Dead Redemption 2 (2018). Le générique du jeu, tel que le reprend Wikipédia, attribue le rôle à Ellen Harvey. Le Red Dead Wiki la présente comme une actrice connue pour House of Cards et Gotham, et indique qu'elle a prêté au personnage sa voix et ses mouvements en capture de mouvement.")},
    {"p": two("The rest of the family is cast as follows. Wikipedia's list, based on the credits, gives Penelope Braithwaite to Alison Barton. The Red Dead Wiki credits Michael Cuddire as Bartholomew, Beau Baxter as Gareth and Reyna de Courcy as Gertrude.",
              "Pour le reste de la famille, la liste de Wikipédia, établie d'après le générique, attribue Penelope Braithwaite à Alison Barton. Le Red Dead Wiki crédite Michael Cuddire pour Bartholomew, Beau Baxter pour Gareth et Reyna de Courcy pour Gertrude.")},
    {"h3": two("Benjamin Byron Davis on Catherine", "Benjamin Byron Davis à propos de Catherine")},
    {"p": two("Benjamin Byron Davis, who plays Dutch, spoke about her in an interview with Twinfinite published on 19 February 2019. Asked about the turning point that sets Dutch on the path of the villain, he said that Dutch keeps meeting people who hold the position he imagines for himself. \"He encounters this sort of queen in Catherine Braithwaite\", he said, before naming Angelo Bronte in Saint Denis as the clearest case.",
              "Benjamin Byron Davis, interprète de Dutch, l'évoque dans un entretien publié par Twinfinite le 19 février 2019. Interrogé sur le moment où Dutch bascule vers le rôle du méchant, il explique que Dutch ne cesse de croiser des gens qui occupent la place dont il rêve pour lui-même. \"He encounters this sort of queen in Catherine Braithwaite\" (il rencontre une sorte de reine en la personne de Catherine Braithwaite), dit-il, avant de citer Angelo Bronte, à Saint-Denis, comme l'exemple le plus net.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The Red Dead Wiki's page on cut content lists an unused hair model for Catherine. It also mentions a Braithwaite servant and maid removed from the game and an unused vest for the Braithwaite butler. According to the same page, members of the Gray and Braithwaite families could originally be met in free roam.",
              "La page du Red Dead Wiki consacrée au contenu coupé signale une coiffure inutilisée pour Catherine. Elle mentionne aussi un domestique et une femme de chambre des Braithwaite retirés du jeu, ainsi qu'un gilet inutilisé pour le majordome de la famille. Selon la même page, il devait à l'origine être possible de croiser des membres des familles Gray et Braithwaite en exploration libre.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Villain rankings", "Classements des méchants")},
    {"p": two("WhatCulture's Matt Thompson ranked her sixth of the fifteen villains of the series in a list published on 7 February 2022. The list counts down from fifteenth to first, and she is placed between Colm O'Driscoll (seventh) and the Murfree Brood (fifth). He called her \"the cantankerous head of an estate that once thrived off slavery\". He wrote that \"the malice and vitriol of Catherine Braithwaite is so ripe with anger, we almost want her to keep around longer\". He added that the assault on her manor \"still ranks as one of RDR2 fans' biggest and best missions\".",
              "Matt Thompson, de WhatCulture, la classe sixième des quinze méchants de la série dans une liste publiée le 7 février 2022. Le classement part de la quinzième place pour remonter jusqu'à la première ; elle s'y intercale entre Colm O'Driscoll (septième) et la Murfree Brood (cinquième). Il la décrit comme \"the cantankerous head of an estate that once thrived off slavery\" (la revêche maîtresse d'un domaine qui prospérait autrefois grâce à l'esclavage). Il écrit que \"the malice and vitriol of Catherine Braithwaite is so ripe with anger, we almost want her to keep around longer\" (la malveillance et le fiel de Catherine Braithwaite sont si chargés de colère qu'on voudrait presque la garder plus longtemps). Il ajoute que l'assaut contre son manoir \"still ranks as one of RDR2 fans' biggest and best missions\" (reste, pour les fans, l'une des plus grandes et des meilleures missions de RDR2).")},
    {"p": two("WatchMojo included her end in \"The 10 Most Satisfying Kills In Red Dead Redemption 2\", written by Mathew Arter and published on 15 March 2023. The entry opens with \"This old biddy is the worst!\" and concedes: \"She is tough, we'll give her that\".",
              "WatchMojo fait figurer sa fin dans \"The 10 Most Satisfying Kills In Red Dead Redemption 2\", un classement signé Mathew Arter et publié le 15 mars 2023. L'entrée s'ouvre sur \"This old biddy is the worst!\" (cette vieille bique est la pire de toutes) et concède : \"She is tough, we'll give her that\" (elle est coriace, on doit le lui reconnaître).")},
    {"h3": two("Hosea's mockery", "Les moqueries d'Hosea")},
    {"p": two("In its ranking of the members of the Van der Linde gang, published on 27 December 2018, Game Informer's staff placed Hosea fourth. They found him most interesting when his kind facade cracks, citing the moment he \"mocks Catherine Braithwaite as her life burns down around her\".",
              "Dans son classement des membres du gang Van der Linde, publié le 27 décembre 2018, la rédaction de Game Informer place Hosea quatrième. Elle le juge plus intéressant quand sa façade bienveillante se fissure, et cite le moment où il \"mocks Catherine Braithwaite as her life burns down around her\" (se moque de Catherine Braithwaite pendant que toute sa vie part en fumée).")},
]


BASE = {
    "slug": "catherine-braithwaite", "name": "Catherine Braithwaite",
    "publishDate": "2026-10-11", "updated": "2026-10-22", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Braithwaite matriarch &middot; RDR2", "reg_role_fr": "Matriarche des Braithwaite &middot; RDR2",
    "gender": "Female", "death": "1899", "nationality": "American",
    "portrait_alt": two("Catherine Braithwaite at the door of Braithwaite Manor in Red Dead Redemption 2",
                        "Catherine Braithwaite sur le seuil de Braithwaite Manor dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Lemoyne", "Personnage &middot; Lemoyne"),
    "meta_desc": two("Catherine Braithwaite, the matriarch of Braithwaite Manor in RDR2: the moonshine, the feud with the Grays, Jack Marston's kidnapping, the fire at the manor in 1899, Ellen Harvey.",
                     "Catherine Braithwaite, matriarche de Braithwaite Manor dans RDR2 : l'alcool de contrebande, la guerre avec les Gray, l'enlèvement de Jack Marston, l'incendie du manoir en 1899, Ellen Harvey."),
    "og_desc": two("The complete reference on Catherine Braithwaite: life, family, estate, quotes, development and reception.",
                   "La référence complète sur Catherine Braithwaite : vie, famille, domaine, citations, conception et accueil."),
    "schema_desc": two("Matriarch of the Braithwaite family of Braithwaite Manor, in Lemoyne, whose sons kidnap Jack Marston and hand him to Angelo Bronte, and who dies in the fire of her manor in 1899, in Red Dead Redemption 2.",
                       "Matriarche de la famille Braithwaite, à Braithwaite Manor, en Lemoyne, dont les fils enlèvent Jack Marston et le livrent à Angelo Bronte, et qui meurt dans l'incendie de son manoir en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Morte en <strong>1899</strong>"), two("Braithwaite matriarch", "Matriarche des Braithwaite"),
              two("Scarlett Meadows", "Scarlett Meadows"),
              two("Played by <strong>Ellen Harvey</strong>", "Interprétée par <strong>Ellen Harvey</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Catherine Braithwaite", "Catherine Braithwaite")},
        {"label": two("Also called", "Autres noms"), "value": two("Mrs. Braithwaite; Momma (one of her sons); Aunt Catherine (Penelope Braithwaite)", "Mrs. Braithwaite ; Momma (l'un de ses fils) ; Aunt Catherine (Penelope Braithwaite)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, at Braithwaite Manor, after running back into the burning house in \"Blood Feuds, Ancient and Modern\"", "1899, à Braithwaite Manor, après être retournée dans la maison en flammes dans \"Blood Feuds, Ancient and Modern\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédée")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Residence", "Résidence"), "value": two("Braithwaite Manor, Scarlett Meadows, Lemoyne", "Braithwaite Manor, Scarlett Meadows, Lemoyne")},
        {"label": two("Occupation", "Activité"), "value": two("Head of the Braithwaite family; plantation owner and moonshine seller", "Cheffe de la famille Braithwaite ; propriétaire d'une plantation et vendeuse d'alcool de contrebande")},
        {"label": two("Family", "Famille"), "value": two("Sons Bartholomew, Gareth and Gerald; a daughter, Gertrude according to the Red Dead Wiki; niece Penelope", "Ses fils Bartholomew, Gareth et Gerald ; une fille, Gertrude selon le Red Dead Wiki ; sa nièce Penelope")},
        {"label": two("Associate", "Associé"), "value": two("[[angelo-bronte|Angelo Bronte]], her customer for five years according to her letter", "[[angelo-bronte|Angelo Bronte]], son client depuis cinq ans d'après sa lettre")},
        {"label": two("Enemies", "Ennemis"), "value": two("The Gray family of [[tavish-gray|Tavish Gray]]; the Van der Linde gang", "La famille Gray de [[tavish-gray|Tavish Gray]] ; le gang Van der Linde")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2 (mentioned in Red Dead Online)", "Red Dead Redemption 2 (mentionnée dans Red Dead Online)")},
        {"label": two("Played by", "Interprète"), "value": two("Ellen Harvey", "Ellen Harvey")},
    ],
    "intro": [
        two("Catherine Braithwaite is the head of the Braithwaite family, owners of Braithwaite Manor in Scarlett Meadows, in Red Dead Redemption 2 (2018), set in 1899. Her family sells moonshine and has long feuded with the Grays of Caliga Hall. In chapter 3 the Van der Linde gang works for both families: [[hosea-matthews|Hosea Matthews]] and [[arthur-morgan|Arthur Morgan]] do jobs for her while the gang steals her horses for [[tavish-gray|Tavish Gray]]. Her men then kidnap [[jack-marston|Jack Marston]]. The gang storms the manor and sets it on fire, and she reveals that her sons gave the boy to [[angelo-bronte|Angelo Bronte]]. Left alive, she runs back into the burning house and dies there.",
            "Catherine Braithwaite est la cheffe de la famille Braithwaite, propriétaire de Braithwaite Manor dans les Scarlett Meadows, dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Sa famille vit de l'alcool de contrebande et mène une guerre ancienne contre les Gray de Caliga Hall. Au chapitre 3, le gang Van der Linde travaille pour les deux camps : [[hosea-matthews|Hosea Matthews]] et [[arthur-morgan|Arthur Morgan]] lui rendent des services pendant que la bande vole ses chevaux pour le compte de [[tavish-gray|Tavish Gray]]. Ses hommes enlèvent alors [[jack-marston|Jack Marston]]. Le gang prend le manoir d'assaut et y met le feu, et elle révèle que ses fils ont livré l'enfant à [[angelo-bronte|Angelo Bronte]]. Laissée en vie, elle retourne dans la maison en flammes et y meurt."),
        two("She is played by Ellen Harvey.",
            "Elle est interprétée par Ellen Harvey."),
    ],
    "essentials": [
        two("She runs Braithwaite Manor, a plantation in Scarlett Meadows whose family now lives off moonshine, and she has been doing business with Angelo Bronte for five years.",
            "Elle dirige Braithwaite Manor, une plantation des Scarlett Meadows dont la famille vit désormais de l'alcool de contrebande, et fait affaire avec Angelo Bronte depuis cinq ans."),
        two("In \"Advertising, The New American Art\", she pays Hosea and Arthur to hand out her stolen moonshine for free in a Gray saloon in Rhodes.",
            "Dans \"Advertising, The New American Art\", elle paie Hosea et Arthur pour distribuer gratuitement son alcool volé dans un saloon des Gray, à Rhodes."),
        two("In \"The Fine Joys of Tobacco\", after a game of cribbage, she hires Arthur and [[sean-macguire|Sean MacGuire]] to burn the Grays' tobacco fields at Caliga Hall.",
            "Dans \"The Fine Joys of Tobacco\", après une partie de cribbage, elle charge Arthur et [[sean-macguire|Sean MacGuire]] d'incendier les champs de tabac des Gray à Caliga Hall."),
        two("In \"Blood Feuds, Ancient and Modern\", the gang kills her sons, burns the manor and learns from her that Jack is with Bronte, in Saint Denis or on a boat to Italy.",
            "Dans \"Blood Feuds, Ancient and Modern\", le gang tue ses fils, incendie le manoir et apprend d'elle que Jack est chez Bronte, à Saint-Denis ou sur un bateau pour l'Italie."),
        two("She dies in 1899 after running back into her burning house; her body can be found in the ruins from chapter 4.",
            "Elle meurt en 1899 après être retournée dans sa maison en flammes ; son corps peut être retrouvé dans les ruines à partir du chapitre 4."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["angelo-bronte", "tavish-gray", "jack-marston", "hosea-matthews"],
}
