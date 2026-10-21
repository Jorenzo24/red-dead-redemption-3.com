"""Luisa Fortuna, reference fiche, PART D: base data, Development and performance, Reception (21 Oct 2026, medium tier).

Her live page (characters/luisa-fortuna/) was generated from the v2 entry in scripts/_wave6.py (order 34,
"slug": "luisa-fortuna"; no entry in _enrich.py). publishDate 2026-09-21 kept (live byline "Updated September 21,
2026"). Eyebrow kept as on the live page ("Character &middot; Nuevo Paraiso", without the accent in EN); reg_role matches
characters_registry.py ("Revolutionary &middot; RDR1" / "Révolutionnaire &middot; RDR1"). portrait_alt kept (the live
portrait shows Luisa with John).
Corrections to the v2 base:
- v2 "She comes from a farming family" and "a farm girl": the transcripts never say the family farms. She calls herself
  little more than a peasant girl, and Reyes speaks of a peasant girl "with the hands of a farmer"; reworded on the
  transcripts (peasant family of Campo Mirada).
- v2 "whom she describes as her fiance" (intro, relationship): she says they are married in their hearts and that his
  family disapproves; John calls her the girl Reyes is marrying. Reworded.
- v2 "John Marston's contacts on the rebel side ... asks him for help with her own family as well as the cause": kept,
  made precise (Miranda's escort, Reyes's rescue, the bridge ambush, Sepulcro).
- v2 "Luisa's family are ordinary farmers caught between the army and the rebels. She asks John to intervene on their
  behalf": the family is pro-rebel (she says so of her father); only Miranda's escort is asked of John. Reworded.
- v2 "John kills two of them, beats the third, Major Raul Zubieta, in a duel": consistent with the transcript and
  HOUSE_FACTS (shot by the soldiers guarding Reyes); the event itself is told in part A.
- v2 "She dies before the revolution she believed in takes the province": dropped (the rebels take Escalera in the same
  mission); Reyes in power in 1911 and 1914 is a Reyes fact, not repeated.
- v2 status "Killed in Escalera in 1911": kept, mission named.
- v2 facts grid lacked birth, home, family names, occupation, enemies, weapons, actor: added. "Behind the scenes" (one
  sentence) replaced by Development and performance and Reception. v2 og_desc ("does not live to see it win") replaced by
  a factual description.

SOURCE REGISTER (read 21 Oct 2026):
- Red Dead Wiki "Luisa Fortuna" (scripts/v3/work/luisa/en.txt): infobox voice = Francesca Galeas (IMDb link nm2277691);
  birth 1892 from the Game of the Year guidebook (wiki reference; the guide was not read: attributed); trivia: pre-release
  look (darker yellow teeth, unkempt hair, more worn face); Undead Nightmare undead with her model and gold cross; Liars and
  Cheats multiplayer model. FR wiki (fr.txt): actrice Francesca Galeas; Luisa is one of the backgrounds of the official
  site.
- IMDb full credits of Red Dead Redemption (tt1479962) and IMDb name page nm2277691: Francesca Galeas credited as Luisa
  Fortuna (seen through search-engine extracts on 21 Oct 2026; imdb.com refuses direct fetches). Her other screen credits
  could not be checked on a page and are not given.
- Rockstar Newswire, "Original Red Dead Redemption Artwork: Luisa Fortuna & Irish", posted May 3, 2010, author R* Q
  (archived copy saved as luisa/fc/newswire_2010-05-03_artwork_luisa_irish.txt): artwork added to the official website,
  "People of the West" updates, character videos, desktops, backgrounds, icons and avatars on the Downloads page. The
  description sentence itself is quoted in part B only.
- WhatCulture, David Michael Hughes, "5 Most Memorable Red Dead Redemption Characters (Aside From John Marston)",
  page 2, published November 16, 2013 (datePublished 2013-11-16T10:08:00+00:00; text saved as
  luisa/fc/whatculture_2013-11-16_memorable_p2.txt): Luisa ranked 5th. The article misquotes two lines (it has "a man who
  has lost his soul", the transcript of "Father Abraham" has "spirit"; "as long as there are guns and money", the
  transcript has "While there are guns and money"): those quotations are not reproduced.
- Javier Aldape, "The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1", Revista Panamericana de Comunicación,
  vol. 4, no. 2, 2022 (allende/fc/aldape_mustang_diaries_redalyc.html): "a staunch Reyista who firmly believes Abraham is
  the true savior of the country". Its claim that John meets her only after realizing the federales are playing him is
  wrong (he frees her with Ricketts before): not reported.
- Red Dead Wiki "Red Dead Redemption Cut Content" (_m/): nothing on her (checked). Wikipedia "Red Dead Redemption"
  (landon/fc/wp_rdr.txt): does not name Luisa (checked).
- Checked, nothing found: any interview of Francesca Galeas; any motion-capture credit for Luisa; Game Informer's review
  (Bertz, 17 May 2010) names neither Luisa nor Reyes; no newspaper of the game names her (reyes/fc/ireddead_newspapers.txt).
- Base: the seven RDR1 transcripts of her missions and "The Gates of El Presidio"; landon_D, reyes_D, desanta_D for
  consistent wording of shared events; jack_C / nigel_C for the Liars and Cheats dates (detailed Aug 27, released
  Sep 21, 2010).

Excluded: the Flowering Judas (Katherine Anne Porter) parallel (wiki literary comparison, no source ties it to Rockstar);
the WhatCulture judgments beyond the sentences quoted; IMDb's later entry for a 2025 edition of the game (not a new
performance; not checkable); Francesca Galeas's other film credits (only search extracts, identity not confirmed);
"People of the West" page content (archive offline on 21 Oct 2026, not read).
DUPLICATE ownership: the actor lives HERE (facts grid and chips may name her); the Newswire artwork release and the
pre-release look HERE only (part C Other media should not repeat them; part B quotes the Newswire sentence); the
multiplayer model and Undead Nightmare are in parts C and A, the facts grid only lists them.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Luisa Fortuna appears in Red Dead Redemption, released in May 2010. The Red Dead Wiki credits Francesca Galeas as her voice, and the game's credits on IMDb list Galeas in the role. No interview in which Galeas discusses Red Dead Redemption was found. No source consulted names a performer for Luisa's motion capture, and Wikipedia's article on the game does not mention the character.",
              "Luisa Fortuna apparaît dans Red Dead Redemption, sorti en mai 2010. Le Red Dead Wiki attribue sa voix à Francesca Galeas, et la fiche du jeu sur IMDb crédite Galeas dans le rôle. Aucune interview dans laquelle Galeas évoque Red Dead Redemption n'a été trouvée. Aucune des sources consultées ne nomme d'interprète pour la capture de mouvement de Luisa, et l'article de Wikipédia consacré au jeu ne cite pas le personnage.")},
    {"h3": two("Design and promotion", "Conception et promotion")},
    {"p": two("On May 3, 2010, two weeks before the game's release, Rockstar presented on its Newswire two character artworks newly added to the official Red Dead Redemption website, one of Luisa and one of Irish. The post adds that both characters feature in the site's \"People of the West\" updates and in the game's character videos, and that the artworks are available as desktops, backgrounds, icons and avatars on the Downloads page. The French-language Red Dead Wiki notes that she is one of the backgrounds of the official site. According to the Red Dead Wiki, a pre-release version of the game gave her a more worn face, dark yellow teeth and unkempt hair. The Red Dead Wiki's page on the game's cut content does not mention her.",
              "Le 3 mai 2010, deux semaines avant la sortie du jeu, Rockstar a présenté sur son Newswire deux illustrations de personnages ajoutées au site officiel de Red Dead Redemption : Luisa et Irish. Le billet précise que tous deux figurent dans les mises à jour \"People of the West\" du site et dans les vidéos de présentation des personnages, et que les illustrations sont proposées en fonds d'écran, arrière-plans, icônes et avatars dans la rubrique Downloads. Le Red Dead Wiki francophone relève qu'elle sert de fond au site officiel. Selon le Red Dead Wiki, une version du jeu antérieure à sa sortie lui donnait un visage plus marqué, des dents d'un jaune foncé et des cheveux en bataille. La page du Red Dead Wiki sur le contenu coupé du jeu ne la mentionne pas.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Character rankings", "Classements de personnages")},
    {"p": two("WhatCulture ranked her fifth in \"5 Most Memorable Red Dead Redemption Characters (Aside From John Marston)\", by David Michael Hughes, published on November 16, 2013. The entry opens: \"Luisa Fortuna is a rebel who openly opposes Colonel Allende and is willing to suffer or die for the revolution.\" Hughes writes that \"Luisa is nothing if not extremely brave\", and that \"Luisa sacrifices herself for Reyes, the man who cannot even recall her very name and only valued her for sexual pleasure.\" He adds that what she died for was not worth it, in his view, because Reyes becomes as bad a dictator as the man he overthrows.",
              "WhatCulture l'a classée cinquième de \"5 Most Memorable Red Dead Redemption Characters (Aside From John Marston)\", article de David Michael Hughes publié le 16 novembre 2013. La notice s'ouvre ainsi : \"Luisa Fortuna is a rebel who openly opposes Colonel Allende and is willing to suffer or die for the revolution.\" (Luisa Fortuna est une rebelle qui s'oppose ouvertement au colonel Allende et qui est prête à souffrir ou à mourir pour la révolution). Hughes écrit que \"Luisa is nothing if not extremely brave\" (Luisa est avant tout d'un courage extrême), et que \"Luisa sacrifices herself for Reyes, the man who cannot even recall her very name and only valued her for sexual pleasure.\" (Luisa se sacrifie pour Reyes, un homme incapable de se souvenir de son nom et qui ne voyait en elle qu'un plaisir charnel). Il ajoute qu'à ses yeux, la cause pour laquelle elle est morte n'en valait pas la peine, puisque Reyes devient un dictateur aussi néfaste que celui qu'il renverse.")},
    {"h3": two("Academic study", "Étude universitaire")},
    {"p": two("In \"The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1\", published in the Revista Panamericana de Comunicación (vol. 4, no. 2, 2022), Javier Aldape, of Texas A&M University, describes her as \"a staunch Reyista who firmly believes Abraham is the true savior of the country\". In the same passage, he writes that Reyes forgets his followers' names. Aldape also notes, without naming her, that Reyes cares more about the corridos sung about him than about the soldaderas, the women fighters who die for his cause.",
              "Dans \"The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1\", article paru dans la Revista Panamericana de Comunicación (vol. 4, n° 2, 2022), Javier Aldape, de l'université Texas A&M, la décrit comme \"a staunch Reyista who firmly believes Abraham is the true savior of the country\" (une partisane inébranlable de Reyes, convaincue qu'Abraham est le vrai sauveur du pays). Dans le même passage, il relève que Reyes oublie le nom de ceux qui le suivent. Aldape note aussi, sans la nommer, que Reyes se soucie davantage des corridos chantés à sa gloire que des soldaderas, les combattantes qui meurent pour sa cause.")},
]


BASE = {
    "slug": "luisa-fortuna", "name": "Luisa Fortuna",
    "publishDate": "2026-09-21", "updated": "2026-10-21", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Revolutionary &middot; RDR1", "reg_role_fr": "Révolutionnaire &middot; RDR1",
    "gender": "Female", "birth": "1892", "death": "1911", "nationality": "Mexican",
    "portrait_alt": two("Luisa Fortuna and John Marston in Red Dead Redemption",
                        "Luisa Fortuna et John Marston dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; Nuevo Paraiso", "Personnage &middot; Nuevo Paraíso"),
    "meta_desc": two("Luisa Fortuna, the young rebel of Campo Mirada in Red Dead Redemption: her rescue by John Marston and Landon Ricketts, Abraham Reyes, her family, her death in Escalera in 1911, Francesca Galeas.",
                     "Luisa Fortuna, la jeune rebelle de Campo Mirada dans Red Dead Redemption : sa libération par John Marston et Landon Ricketts, Abraham Reyes, sa famille, sa mort à Escalera en 1911, Francesca Galeas."),
    "og_desc": two("The complete reference on Luisa Fortuna: life, missions, quotes, development and reception.",
                   "La référence complète sur Luisa Fortuna : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Young Mexican teacher and rebel in Red Dead Redemption, devoted to Abraham Reyes, who gives John Marston the rebel missions of Nuevo Paraíso and is shot dead in Escalera in 1911 trying to save Reyes.",
                       "Jeune institutrice et rebelle mexicaine dans Red Dead Redemption, dévouée à Abraham Reyes, qui confie à John Marston les missions rebelles du Nuevo Paraíso et meurt abattue à Escalera en 1911 en tentant de sauver Reyes."),
    "chips": [two("Rebel, Reyes's movement", "Rebelle, mouvement de Reyes"),
              two("Teacher", "Institutrice"),
              two("Died in <strong>1911</strong>", "Morte en <strong>1911</strong>"),
              two("Voiced by <strong>Francesca Galeas</strong>", "Voix : <strong>Francesca Galeas</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Luisa Fortuna (called Laura by Reyes)", "Luisa Fortuna (Laura pour Reyes)")},
        {"label": two("Born", "Naissance"), "value": two("1892, according to the Game of the Year Edition guide, cited by the Red Dead Wiki; Rockstar gave her age as 19 in May 2010", "1892, d'après le guide de l'édition Game of the Year, cité par le Red Dead Wiki ; Rockstar lui donnait 19 ans en mai 2010")},
        {"label": two("Died", "Mort"), "value": two("1911, in Escalera (\"An Appointed Time\"), shot by the soldiers guarding Abraham Reyes", "1911, à Escalera (\"An Appointed Time\"), abattue par les soldats qui gardent Abraham Reyes")},
        {"label": two("Nationality", "Nationalité"), "value": two("Mexican", "Mexicaine")},
        {"label": two("Occupation", "Activité"), "value": two("Teacher and revolutionary", "Institutrice et révolutionnaire")},
        {"label": two("Home", "Domicile"), "value": two("The family house at Campo Mirada, Perdido, Nuevo Paraíso", "La maison familiale de Campo Mirada, Perdido, Nuevo Paraíso")},
        {"label": two("Family", "Famille"), "value": two("Her father (killed in 1911) and mother, unnamed in the game; her brother Emilio and her sister Miranda", "Son père (tué en 1911) et sa mère, dont le jeu ne donne pas le nom ; son frère Emilio et sa sœur Miranda")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Reyes' Rebels", "Les rebelles de Reyes (Reyes' Rebels)")},
        {"label": two("Allies", "Alliés"), "value": two("[[abraham-reyes|Abraham Reyes]], [[john-marston|John Marston]], [[landon-ricketts|Landon Ricketts]]", "[[abraham-reyes|Abraham Reyes]], [[john-marston|John Marston]], [[landon-ricketts|Landon Ricketts]]")},
        {"label": two("Enemies", "Ennemis"), "value": two("[[agustin-allende|Agustin Allende]], [[vincente-de-santa|Vincente de Santa]] and the Mexican Army", "[[agustin-allende|Agustin Allende]], [[vincente-de-santa|Vincente de Santa]] et l'armée mexicaine")},
        {"label": two("Weapons", "Armes"), "value": two("Cattleman Revolver, Hunting Knife (Red Dead Wiki)", "Cattleman Revolver, couteau de chasse (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption; her model is used for an undead in Undead Nightmare (Red Dead Wiki); multiplayer model (Liars and Cheats)", "Red Dead Redemption ; son modèle sert à un mort-vivant dans Undead Nightmare (Red Dead Wiki) ; modèle multijoueur (Liars and Cheats)")},
        {"label": two("Voiced by", "Voix"), "value": two("Francesca Galeas", "Francesca Galeas")},
    ],
    "intro": [
        two("Luisa Fortuna is a young Mexican teacher and rebel in Red Dead Redemption (2010), set in 1911. She lives with her family at Campo Mirada, in Nuevo Paraíso, and fights for [[abraham-reyes|Abraham Reyes]], the leader of the revolt against Colonel [[agustin-allende|Agustin Allende]]. [[john-marston|John Marston]] and [[landon-ricketts|Landon Ricketts]] free her from an army jail in the caves near El Matadero. She then gives John the rebel missions of the second act: her sister Miranda's escort to the docks, Reyes's rescue at El Presidio, an ambush on an army convoy and the attack on [[vincente-de-santa|Vincente de Santa]] at Sepulcro.",
            "Luisa Fortuna est une jeune institutrice et rebelle mexicaine dans Red Dead Redemption (2010), dont l'action se déroule en 1911. Elle vit avec sa famille à Campo Mirada, au Nuevo Paraíso, et se bat pour [[abraham-reyes|Abraham Reyes]], qui mène la révolte contre le colonel [[agustin-allende|Agustin Allende]]. [[john-marston|John Marston]] et [[landon-ricketts|Landon Ricketts]] la tirent d'une prison de l'armée, dans les grottes près d'El Matadero. Elle confie ensuite à John les missions rebelles du deuxième acte : l'escorte de sa sœur Miranda jusqu'au port, le sauvetage de Reyes à El Presidio, l'embuscade contre un convoi de l'armée et l'attaque contre [[vincente-de-santa|Vincente de Santa]] à Sepulcro."),
        two("She believes that she and Reyes are married in their hearts; Reyes confuses her name and tells John he will never marry a peasant. In Escalera, she runs at the soldiers about to execute Reyes and is shot dead. She is voiced by Francesca Galeas.",
            "Elle croit qu'elle et Reyes sont déjà mariés dans leur cœur ; Reyes, lui, se trompe sur son prénom et assure à John qu'il n'épousera jamais une paysanne. À Escalera, elle se jette sur les soldats qui s'apprêtent à exécuter Reyes et tombe sous leurs balles. Elle a la voix de Francesca Galeas."),
    ],
    "essentials": [
        two("In \"Landon Ricketts Rides Again\", John and Ricketts break her out of an army jail in the caves near El Matadero.",
            "Dans \"Landon Ricketts Rides Again\", John et Ricketts la font évader d'une prison de l'armée, dans les grottes près d'El Matadero."),
        two("In \"My Sister's Keeper\", she asks John to take her sister Miranda to the docks while her family leaves Campo Mirada.",
            "Dans \"My Sister's Keeper\", elle demande à John d'escorter sa sœur Miranda jusqu'au port pendant que sa famille quitte Campo Mirada."),
        two("In \"Must a Savior Die?\", she drives John to El Presidio, where he saves Reyes from a firing squad.",
            "Dans \"Must a Savior Die?\", elle conduit John jusqu'à El Presidio, où il sauve Reyes du peloton d'exécution."),
        two("In \"Father Abraham\", after the army kills her father, she has John blow up an army convoy near the Frontera Bridge.",
            "Dans \"Father Abraham\", après la mort de son père, tué par l'armée, elle fait sauter par John un convoi militaire près du pont de Frontera."),
        two("In \"Captain De Santa's Downfall\", she sends John and her men to Sepulcro to stop De Santa's massacre.",
            "Dans \"Captain De Santa's Downfall\", elle envoie John et ses hommes à Sepulcro pour arrêter le massacre que supervise De Santa."),
        two("In \"An Appointed Time\", she is shot dead in Escalera trying to save Reyes.",
            "Dans \"An Appointed Time\", elle est abattue à Escalera en tentant de sauver Reyes."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["abraham-reyes", "john-marston", "landon-ricketts", "agustin-allende"],
}
