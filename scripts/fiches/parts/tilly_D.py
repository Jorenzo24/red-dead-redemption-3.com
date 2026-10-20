"""Tilly Jackson, reference fiche, PART D: base data, Development and performance, Reception (20 Oct 2026, medium tier).

Her live page (characters/tilly-jackson/) was generated from the v2 entry in scripts/_enrich.py
(ENRICHED, "slug": "tilly-jackson"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the v2 intro quoted Rockstar's description; that quote now lives in part B (Personality)
only. The v2 Development paragraph is kept and re-verified against both interviews (Fuzzable, 20 Mar 2019;
GamesRadar, 7 Mar 2019), with these corrections: the Fuzzable interview prints the Lenny actor's name as
"Harron Alexander"; the actor is Harron Atkins (lenny fiche, CLAUDE.md), so the text says she went to high school with
the actor who plays Lenny and names him as Harron Atkins without attributing that spelling to Fuzzable. The GamesRadar
"art imitating life" quote is kept with its context (the writers said the pregnancy scene was not written for
her). The v2 chip "RDR2" is dropped (redundant with the eyebrow and facts). Eyebrow and reg_role match
characters_registry.py ("Van der Linde gang &middot; RDR2"). publishDate 2026-08-17 kept (git: 1caf87b,
"chore: drip-publish scheduled character (PUBLISHED tilly-jackson)", 17 Aug 2026).

Sources (internal register, checked 20 Oct 2026):
- Fuzzable, "Exclusive Interview: \"Red Dead Redemption 2\" Actress Meeya Davis", Kay Simpson, 20 Mar 2019 (archived
  copy of 12 Oct 2019 read in full: tilly/fcB/fuzz.txt): born and raised in Detroit, moved to New Jersey in 2012 to
  study acting in college; voice and motion capture for Tilly; went in for "a commercial audition", no character
  background, learned about the character on her shooting days; engaged when she started, later pregnant with her
  son; went to high school with the Lenny actor, also from Detroit; "giving a voice to black gamers"; "strong women
  standing up for themselves"; Sundance; one episode of the final season of Orange Is the New Black (announced, not
  verified as aired: not used).
- GamesRadar+, "Sisterhood, shotguns and slapping: Red Dead Redemption 2's cast talk around the virtual campfire",
  Rachel Weber, 7 Mar 2019 (tilly/fcB/gr.txt): Davis on the campfire scene about killing Anthony Foreman's cousin,
  on the 1907 scene ("seven or eight months pregnant", "art imitating life"); Kaili Vernoff on the rescue mission and
  Susan's bond with Tilly.
- Wikipedia, "List of Red Dead Redemption 2 characters" (../uncle/fc/wp_list_rdr2_characters.txt): Tilly section
  (credited as Meeya Davis-Glover; handmaiden; guide p. 383; Fuzzable and GamesRadar summaries); production section
  (2013, 2,200 days, 1,200 actors, 700 sharing 500,000 lines, per Vulture; motion capture and facial cameras).
- Red Dead Wiki "Meeya Davis" (tilly/fcB/Meeya_Davis.txt): born June 21, 1987, in Detroit; High Maintenance, Crashing.
  Kept attributed to the wiki (no second source for the date).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../uncle/fc/wiki_Red_Dead_Redemption_2_Cut_Content.txt): unused
  leg models for many female characters, Tilly included; concept art of Bill, Karen, Tilly, Uncle, Mary-Beth, Strauss
  and Pearson in its gallery.
- Game Informer, "Ranking All The Members Of Red Dead Redemption II's Van Der Linde Gang", Game Informer Staff,
  27 Dec 2018 (../uncle/fc/gi_ranking.txt): Tilly 9th of 24, quoted verbatim.
- Kotaku, "Red Dead Redemption 2's Depiction Of Jim Crow Racism Doesn't Add Up", Isaac Monterose (freelance),
  5 Aug 2020 (fetched 20 Oct 2026): the Lemoyne conversation with Arthur, quoted verbatim.
- TheGamer, "The Women & Children Of The Van Der Linde Gang, Ranked By Skill", Rafly Gilang, 2 Aug 2020 (fetched
  20 Oct 2026): Tilly 7th of 9.
Excluded: the Orange Is the New Black episode (announced by Davis, not verified); "Davis-Glover appreciated that the
game featured a black woman standing up for herself" kept only as her own words from Fuzzable; the wiki claim that
Tilly is pregnant with a second child (Mr. Pierre page; part A decides); the Eliza cut encounter "a bench away"
from Tilly (about Eliza, not Tilly); the Carbine Repeater glitch (part C trivia). No other interview of Davis about
the role was found (searches 20 Oct 2026); no review discussing Tilly by name was found in IGN, Polygon or PC Gamer.
Fact-check fixes (20 Oct 2026): intro and essentials corrected (Tilly hides with Jack when Milton's men grab Abigail
outside camp, per Abigail's line in the "Red Dead Redemption" mission transcript, not during the Pinkerton assault on
Beaver Hollow; the letter is signed "Yours, Tilly", she only introduces herself as Tilly Pierre); the generic
production paragraph (2013, 2,200 days, 1,200 actors) removed as not specific to Tilly.
DUPLICATE ownership: actress, interviews, production context and cut content live HERE; parts B and C must not retell
them. Official descriptions belong to part B; origins, kidnapping, Beaver Hollow and 1907 belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Tilly is played by Meeya Davis, credited in Wikipedia's list of the game's characters as Meeya Davis-Glover. According to the Red Dead Wiki, she was born in Detroit on June 21, 1987, and has appeared in the series High Maintenance and Crashing. Fuzzable, which interviewed her on March 20, 2019, writes that she grew up in Detroit and moved to New Jersey in 2012 to study acting in college, and that she provided both the voice and the motion capture for Tilly. She told the site she had gone in for \"a commercial audition\", with no background on the character; she realized motion capture was involved when she learned the project was Rockstar's, but only discovered who Tilly was on her actual shooting days. She had just become engaged when she started on the game and later became pregnant with her son during production. She also said she had gone to high school with Harron Atkins, the actor who plays Lenny Summers, who is also from Detroit.",
              "Tilly est interprétée par Meeya Davis, créditée sous le nom de Meeya Davis-Glover dans la liste des personnages du jeu sur Wikipédia. D'après le Red Dead Wiki, elle est née à Detroit le 21 juin 1987 et a joué dans les séries High Maintenance et Crashing. Fuzzable, qui l'a interviewée le 20 mars 2019, indique qu'elle a grandi à Detroit puis s'est installée dans le New Jersey en 2012 pour étudier le jeu d'acteur à l'université, et qu'elle a assuré à la fois la voix et la capture de mouvement de Tilly. Elle y raconte s'être présentée à ce qu'elle croyait être \"a commercial audition\" (une audition pour une publicité), sans rien savoir du personnage ; elle a compris qu'il y aurait de la capture de mouvement en apprenant que le projet était signé Rockstar, mais n'a découvert Tilly qu'aux premiers jours de tournage. Elle venait de se fiancer quand elle a commencé et est tombée enceinte de son fils pendant la production. Elle ajoute qu'elle a fréquenté le même lycée que Harron Atkins, l'interprète de Lenny Summers, lui aussi originaire de Detroit.")},
    {"p": two("Asked by Fuzzable why characters like Tilly matter, Davis spoke of \"giving a voice to black gamers\" and called it \"such an important message to have strong women standing up for themselves\". She described Tilly as a camp girl who had been badly treated by the Foreman Brothers and separated from her mother, and as \"super sweet and super strong\".",
              "Interrogée par Fuzzable sur l'importance de personnages comme Tilly, Meeya Davis évoque le fait de \"giving a voice to black gamers\" (donner une voix aux joueurs noirs) et juge essentiel de montrer des femmes fortes qui se font respecter. Elle décrit Tilly comme une fille du camp maltraitée par les frères Foreman et séparée de sa mère, \"super sweet and super strong\" (d'une grande douceur et d'une grande force).")},
    {"h3": two("Key scenes", "Les scènes marquantes")},
    {"p": two("In GamesRadar's interview with the actresses of the gang, published on March 7, 2019, Davis said the campfire scene in which Tilly tells how she killed Anthony Foreman's cousin made her emotional on set: \"at a young age she went through so much.\" She was seven or eight months pregnant when she shot Tilly's pregnant scene in the epilogue. She asked the writers whether they had written it because of her pregnancy, and they said they had not; she called it \"art imitating life\" and said she was glad Tilly got \"that joyful ending\". In the same article Kaili Vernoff, who plays Susan Grimshaw, said the mission to rescue Tilly shows that Susan \"will go to any lengths to protect these girls\", and that she enjoyed watching Susan become loving with Tilly.",
              "Dans l'entretien de GamesRadar avec les actrices du gang, publié le 7 mars 2019, Meeya Davis raconte que la scène au coin du feu où Tilly explique comment elle a tué le cousin d'Anthony Foreman l'a émue sur le plateau : \"at a young age she went through so much\" (si jeune, elle a traversé tant de choses). Elle était enceinte de sept ou huit mois quand elle a tourné la scène de l'épilogue où Tilly attend un enfant. Elle a demandé aux scénaristes s'ils l'avaient écrite à cause de sa grossesse, ce qu'ils ont démenti ; elle y voit \"art imitating life\" (l'art qui imite la vie) et se réjouit que Tilly ait droit à \"that joyful ending\" (cette fin heureuse). Dans le même article, Kaili Vernoff, l'interprète de Susan Grimshaw, estime que la mission du sauvetage de Tilly montre que Susan \"will go to any lengths to protect these girls\" (est prête à tout pour protéger ces filles), et dit avoir aimé voir Susan devenir affectueuse avec Tilly.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("According to the Red Dead Wiki, the game files contain unused leg models for Tilly, as for many other female characters, made for a camera angle the final game never allows. The wiki's gallery of cut content also includes a sheet of concept art showing Tilly with Bill, Karen, Uncle, Mary-Beth, Strauss and Pearson.",
              "D'après le Red Dead Wiki, les fichiers du jeu contiennent pour Tilly, comme pour de nombreux autres personnages féminins, des modèles de jambes inutilisés, prévus pour un angle de caméra que la version finale ne permet jamais. La galerie du contenu coupé sur le wiki comprend aussi une planche de concept art montrant Tilly avec Bill, Karen, Uncle, Mary-Beth, Strauss et Pearson.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Rankings", "Classements")},
    {"p": two("In Game Informer's staff ranking of the 24 members of the Van der Linde gang, published on December 27, 2018, Tilly comes 9th. The staff wrote that her \"sometimes supportive, sometimes raw conversations with Arthur about the cruelty of hunting animals and hurting people are among the best bits of writing in the game\", and called John's meeting with her in the epilogue, happily married with a child, \"another one of Red Dead Redemption II's rare happy moments\". TheGamer placed her 7th of 9 in a ranking of the gang's women and children by skill, published on August 2, 2020.",
              "Dans le classement des 24 membres du gang Van der Linde établi par la rédaction de Game Informer et publié le 27 décembre 2018, Tilly arrive 9e. La rédaction juge que ses conversations avec Arthur, tantôt bienveillantes, tantôt crues, sur la cruauté de la chasse et le mal fait aux gens comptent \"among the best bits of writing in the game\" (parmi les meilleurs moments d'écriture du jeu), et voit dans ses retrouvailles avec John à l'épilogue, heureuse en ménage et mère, l'un des rares moments heureux de Red Dead Redemption II. TheGamer la place 7e sur 9 dans un classement par compétences des femmes et des enfants du gang, publié le 2 août 2020.")},
    {"h3": two("Race and the South", "La question raciale et le Sud")},
    {"p": two("In an article for Kotaku on August 5, 2020, arguing that the game's depiction of Jim Crow racism is inconsistent, freelance writer Isaac Monterose cites Tilly's camp conversation with Arthur about Lemoyne as an example of Arthur's \"obliviousness about race\". He notes that Arthur first answers that the state \"seems as good a place as any to get chased by the law\", and that Tilly then has to point out to him that she is Black, before he understands and promises to keep her safe.",
              "Dans un article publié par Kotaku le 5 août 2020, qui juge incohérente la façon dont le jeu dépeint le racisme de l'ère Jim Crow, le journaliste indépendant Isaac Monterose cite la conversation de camp entre Tilly et Arthur au sujet du Lemoyne comme un exemple de l'\"obliviousness about race\" (aveuglement sur la question raciale) d'Arthur. Il relève qu'Arthur répond d'abord que cet État \"seems as good a place as any to get chased by the law\" (en vaut bien un autre pour avoir la loi aux trousses), et que Tilly doit alors lui rappeler qu'elle est noire, avant qu'il comprenne et promette de la protéger.")},
]


BASE = {
    "slug": "tilly-jackson", "name": "Tilly Jackson",
    "publishDate": "2026-08-17", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Female", "death": None, "nationality": "American",
    "portrait_alt": two("Tilly Jackson in Red Dead Redemption 2", "Tilly Jackson dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Tilly Jackson, member of the Van der Linde gang in RDR2: her past with the Foreman Brothers, her kidnapping in 1899, hiding with Jack at Beaver Hollow, her life in Saint Denis in 1907, Meeya Davis.",
                     "Tilly Jackson, membre du gang Van der Linde dans RDR2 : son passé chez les frères Foreman, son enlèvement en 1899, sa cachette avec Jack à Beaver Hollow, sa vie à Saint-Denis en 1907, Meeya Davis."),
    "og_desc": two("The complete reference on Tilly Jackson: life, missions, camp scenes, quotes, development and reception.",
                   "La référence complète sur Tilly Jackson : vie, missions, scènes de camp, citations, conception et accueil."),
    "schema_desc": two("Member of the Van der Linde gang in Red Dead Redemption 2, a former member of the Foreman Brothers who survives the gang's fall and lives in Saint Denis as Tilly Pierre in 1907.",
                       "Membre du gang Van der Linde dans Red Dead Redemption 2, ancienne des frères Foreman, qui survit à la chute du gang et vit à Saint-Denis sous le nom de Tilly Pierre en 1907."),
    "chips": [two("Alive in <strong>1907</strong>", "Vivante en <strong>1907</strong>"), two("Van der Linde gang", "Gang Van der Linde"),
              two("Later Tilly Pierre", "Plus tard Tilly Pierre"),
              two("Voiced by <strong>Meeya Davis</strong>", "Voix de <strong>Meeya Davis</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Tilly Jackson; Tilly Pierre after her marriage", "Tilly Jackson ; Tilly Pierre après son mariage")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1907, living in Saint Denis", "Vivante en 1907, installée à Saint-Denis")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Family", "Famille"), "value": two("Mother (a former slave, dead before Tilly joined Dutch); husband, Mr. Pierre, a lawyer from Haiti; a daughter", "Une mère (ancienne esclave, morte avant que Tilly ne rejoigne Dutch) ; un mari, M. Pierre, avocat originaire d'Haïti ; une fille")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Foreman Brothers (former), Van der Linde gang (former)", "Frères Foreman (ancienne), gang Van der Linde (ancienne)")},
        {"label": two("Role", "Rôle"), "value": two("Camp work under Susan Grimshaw", "Travaux du camp sous les ordres de Susan Grimshaw")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Meeya Davis", "Meeya Davis")},
    ],
    "intro": [
        two("Tilly Jackson is a supporting character of Red Dead Redemption 2 (2018), set in 1899. Taken from her mother at 12 by the Foreman Brothers gang, she ran with them for years before killing one of them and fleeing; [[dutch-van-der-linde|Dutch van der Linde]] took her into his gang. In camp she works under [[susan-grimshaw|Susan Grimshaw]] with [[karen-jones|Karen Jones]] and [[mary-beth-gaskill|Mary-Beth Gaskill]]. In the fourth chapter the Foremans kidnap her, and Susan and [[arthur-morgan|Arthur Morgan]] rescue her. When Pinkerton agents seize Abigail outside the Beaver Hollow camp, she hides with [[jack-marston|Jack Marston]]. By 1907 she is married to a lawyer from Haiti and lives in Saint Denis.",
            "Tilly Jackson est un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Arrachée à sa mère à 12 ans par la bande des frères Foreman, elle les suit pendant des années avant de tuer l'un d'eux et de s'enfuir ; [[dutch-van-der-linde|Dutch van der Linde]] l'accueille alors dans son gang. Au camp, elle travaille sous les ordres de [[susan-grimshaw|Susan Grimshaw]] avec [[karen-jones|Karen Jones]] et [[mary-beth-gaskill|Mary-Beth Gaskill]]. Au quatrième chapitre, les Foreman l'enlèvent, et Susan et [[arthur-morgan|Arthur Morgan]] la délivrent. Quand des agents de la Pinkerton s'emparent d'Abigail devant le camp de Beaver Hollow, elle se cache avec [[jack-marston|Jack Marston]]. En 1907, elle a épousé un avocat originaire d'Haïti et vit à Saint-Denis."),
        two("She is played by Meeya Davis, an American actress from Detroit.",
            "Elle est interprétée par Meeya Davis, actrice américaine originaire de Detroit."),
    ],
    "essentials": [
        two("Kidnapped from her mother at 12 by the Foreman Brothers, she kills Anthony Foreman's cousin Malcolm and flees; Dutch takes her in and teaches her to read.",
            "Enlevée à sa mère à 12 ans par les frères Foreman, elle tue Malcolm, le cousin d'Anthony Foreman, et s'enfuit ; Dutch la recueille et lui apprend à lire."),
        two("In Valentine, in \"Polite Society, Valentine Style\", Anthony Foreman grabs her in the street until [[arthur-morgan|Arthur]] drives him off.",
            "À Valentine, dans \"Polite Society, Valentine Style\", Anthony Foreman l'empoigne en pleine rue jusqu'à ce qu'[[arthur-morgan|Arthur]] le chasse."),
        two("In \"No, No and Thrice, No\" the Foremans hold her at Radley's House; [[susan-grimshaw|Susan]] and Arthur free her and bring Anthony back for her to confront.",
            "Dans \"No, No and Thrice, No\", les Foreman la retiennent à Radley's House ; [[susan-grimshaw|Susan]] et Arthur la libèrent et lui ramènent Anthony pour qu'elle l'affronte."),
        two("When Milton's men seize Abigail outside Beaver Hollow, she hides with [[jack-marston|Jack]], then waits with him at Copperhead Landing; in 1907 she writes to John and Abigail, introducing herself as Tilly Pierre, wife of a Haitian lawyer and mother of a girl.",
            "Quand les hommes de Milton s'emparent d'Abigail devant Beaver Hollow, elle se cache avec [[jack-marston|Jack]], puis l'attend avec lui à Copperhead Landing ; en 1907, elle écrit à John et Abigail en se présentant comme Tilly Pierre, épouse d'un avocat haïtien et mère d'une petite fille."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["karen-jones", "mary-beth-gaskill", "susan-grimshaw", "jack-marston"],
}
