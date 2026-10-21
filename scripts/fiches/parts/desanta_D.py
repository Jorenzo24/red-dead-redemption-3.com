"""Vincente de Santa, reference fiche, PART D: base data, Development and performance, Reception
(21 Oct 2026, medium tier).

His live page (characters/vincente-de-santa/) was generated from the v2 entry in scripts/_wave6.py (order 33,
"slug": "vincente-de-santa"; no entry in _enrich.py). publishDate 2026-09-18 kept (live byline "Updated September 18,
2026"). Eyebrow kept as on the live page ("Character &middot; Nuevo Paraiso", without the accent in EN); reg_role matches
characters_registry.py ("Mexican Army captain &middot; RDR1" / "Capitaine de l'armée mexicaine &middot; RDR1").
Corrections to the v2 base:
- v2 status "Killed by John Marston in 1911" and "John escapes the firing squad, hunts him down and kills him": the player
  chooses at Sepulcro whether John shoots him or leaves him to the rebels (HOUSE_FACTS; "Captain De Santa's Downfall"
  transcript, both branches). John does not escape on his own: Reyes's rebels save him.
- v2 "De Santa begs for his life first": the transcript has him insult John, give Casa Madrugada and say "Hurry up and kill
  me or just let me go"; dropped.
- v2 "He repeatedly promises to hand over Bill and Javier... finds another errand": the promises come from De Santa and
  Allende ("if you help us, we will help you", 20,000 pesos and Javier's whereabouts in "Mexican Caesar", the Chuparosa
  lie); reworded on the transcripts.
- v2 "executions of suspected rebels, and the hunt for Abraham Reyes": kept only as the games show it (Tesoro Azul,
  Torquemada, Sepulcro).
- v2 "The break ends John's arrangement with the army... commits to the rebel side for the assault on Escalera": the break
  comes at Chuparosa, before Sepulcro; reworded.
- v2 "His name is also written Vicente in some materials": now sourced (Blackwater Ledger No. 58, Spanish wiki, Aldape).
- v2 og_desc/meta_desc "delivers nothing", "the betrayal that gets him killed": replaced by factual descriptions.
- v2 "Behind the scenes" (one sentence) replaced by Development and performance (actor) and Reception.
- v2 facts grid lacked actor, birth, death place, family, weapons: added. Nationality "Mexican" kept.

SOURCE REGISTER (read 21 Oct 2026):
- Wikipedia "Hector Luis Bustamante" (raw wikitext saved as desanta/fc/wp_bustamante.txt): Colombian-American actor, born
  Héctor Luis Bustamante Durango in Medellín, moved to the United States at 12; Video games table: Red Dead Redemption and
  Red Dead Redemption: Undead Nightmare (2010), "Captain Vincente De Santa"; 2009 Imagen Award, outstanding lead actor in a
  made-for-television movie; best known for Little Girl Lost: The Delimar Vera Story (LMN, 2008); Hostage (2005).
- Red Dead Wiki "Hector Luis Bustamante" (_m/Hector_Luis_Bustamante.txt): voice of Vincente de Santa; birth date
  March 12, 1972 (wiki-only, attributed). Red Dead Wiki "Vincente de Santa" infobox: voice = Hector Luis Bustamante.
- Wikipedia "Red Dead Redemption" (landon/fc/wp_rdr.txt): does not name De Santa or Bustamante (checked).
- Red Dead Wiki "Red Dead Redemption Cut Content" (_m/): nothing on him (checked). No pre-release artwork of him in the
  wiki gallery.
- WhatCulture, Matt Thompson, "Red Dead Redemption: Every Villain Ranked From Worst To Best", 7 February 2022 (page 3,
  entry 13, Allende; excerpt saved as desanta/fc/whatculture_villains_p3.txt). De Santa is not ranked himself.
- LGBTQ Video Game Archive, "Quique Montemayor and Captain Vincente de Santa in Red Dead Redemption", published 24 June
  2016 (text saved as desanta/fc/lgbtq_archive_desanta.txt). Tags: Bisexual (implicit), Gay (implicit), Queer Men.
  Citations: Red Dead Wiki pages, Gamer Syndrome blog (2013), IGN forum thread (11 Aug 2010). It misquotes Reyes ("safe";
  the transcript of "The Gates of El Presidio" reads "safer").
- Javier Aldape, "The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1", Revista Panamericana de Comunicación,
  vol. 4, no. 2, 2022 (allende/fc/aldape_mustang_diaries_redalyc.html): "one of his subordinates, Captain Vicente De Santa".
- Base: transcripts of the six RDR1 missions and "The Gates of El Presidio"; Blackwater Ledger No. 58 death notice
  ("Captain Vicente De Santa of the Mexican Army has been reported deceased, age 34 years.", reyes/fc/
  ireddead_newspapers.txt); Red Dead Wiki "Sepulcro" (gravestone "Captain Vincente De Santa / Tender man / Fierce soldier /
  1877-1911", present with Undead Nightmare installed); Red Dead Wiki "Myths and Mavericks" (multiplayer model).
- Checked, nothing found: any interview of Bustamante about the role; any motion-capture credit for De Santa; any review
  of Red Dead Redemption naming De Santa (Game Informer, Bertz, 17 May 2010 names neither officer).

Excluded: the Red Dead Wiki's Brian Jeremy (GTA: The Lost and Damned) and the FR wiki's Tony Montana comparisons (fan
analysis); the Michael De Santa surname coincidence (part C Trivia if kept); the archive's own judgements beyond what it
states (only its title, tags, description and sources are reported); Bustamante's full filmography beyond the lines of
his Wikipedia article; Carne y Arena (not relevant); the Red Dead Wiki's height for the actor.
DUPLICATE ownership: the actor lives HERE (facts grid and chips may name him); the queer reading of the Quique scenes is
reported HERE only (part B gives the lines without reading); the spelling sources are in B Names, Aldape's sentence here.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Captain De Santa appears in Red Dead Redemption and in its expansion Undead Nightmare, both released in 2010. The Red Dead Wiki credits Hector Luis Bustamante as his voice, and the Wikipedia article on the actor lists the role, as \"Captain Vincente De Santa\", in both games. According to Wikipedia, Bustamante is a Colombian-American actor, born Héctor Luis Bustamante Durango in Medellín, whose family moved to the United States when he was 12; the Red Dead Wiki gives his date of birth as March 12, 1972. His television and film roles include the series The Shield and the film Hostage (2005). He won the 2009 Imagen Award for outstanding lead actor in a made-for-television movie, and Wikipedia names Little Girl Lost: The Delimar Vera Story (Lifetime Movie Network, 2008) as his best-known performance.",
              "Le capitaine De Santa apparaît dans Red Dead Redemption et dans son extension Undead Nightmare, sorties toutes deux en 2010. Le Red Dead Wiki attribue sa voix à Hector Luis Bustamante, et l'article de Wikipédia consacré à l'acteur mentionne le rôle, sous le nom de \"Captain Vincente De Santa\", dans les deux jeux. Toujours selon Wikipédia, Bustamante est un acteur américano-colombien, né Héctor Luis Bustamante Durango à Medellín, dont la famille s'est installée aux États-Unis quand il avait 12 ans ; le Red Dead Wiki le fait naître le 12 mars 1972. On l'a vu notamment dans la série The Shield et dans le film Otage (Hostage, 2005). Il a reçu en 2009 l'Imagen Award du meilleur acteur principal dans un téléfilm, et Wikipédia cite Little Girl Lost: The Delimar Vera Story (Lifetime Movie Network, 2008) comme son rôle le plus connu.")},
    {"p": two("No interview in which Bustamante discusses Red Dead Redemption was found. No source consulted names a performer for De Santa's motion capture, and Wikipedia's article on the game does not mention the character. The Red Dead Wiki's page on the game's cut content lists nothing about him.",
              "Aucune interview dans laquelle Bustamante évoque Red Dead Redemption n'a été trouvée. Aucune des sources consultées ne nomme d'interprète pour la capture de mouvement de De Santa, et l'article de Wikipédia consacré au jeu ne cite pas le personnage. La page du Red Dead Wiki sur le contenu coupé du jeu ne mentionne rien à son sujet.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Villain rankings", "Classements de méchants")},
    {"p": two("De Santa does not have an entry in \"Red Dead Redemption: Every Villain Ranked From Worst To Best\", published by WhatCulture on February 7, 2022. In the entry on Allende, ranked 13th, Matt Thompson writes that \"his underling, Captain Vincente de Santa has more of a character evolution after the betrayal\", and regrets that the colonel was not given the same depth.",
              "De Santa n'a pas d'entrée dans \"Red Dead Redemption: Every Villain Ranked From Worst To Best\", publié par WhatCulture le 7 février 2022. Dans la notice consacrée à Allende, classé 13e, Matt Thompson écrit que \"his underling, Captain Vincente de Santa has more of a character evolution after the betrayal\" (son subordonné, le capitaine Vincente de Santa, évolue davantage après la trahison), et regrette que le colonel n'ait pas eu la même profondeur.")},
    {"h3": two("LGBTQ Video Game Archive", "LGBTQ Video Game Archive")},
    {"p": two("The LGBTQ Video Game Archive, a research project led by Adrienne Shaw of Temple University, published an entry titled \"Quique Montemayor and Captain Vincente de Santa in Red Dead Redemption\" on June 24, 2016. It files the pair under implicit gay and implicit bisexual representation. The entry says that the two men seem to be \"openly in an intimate relationship\", that several major characters comment on it, and that De Santa also flirts with women. It quotes, without naming the speaker, Reyes's line on young boys sleeping safely after De Santa's death, and the word mariconcito. Its listed sources are two Red Dead Wiki pages, a 2013 blog post and a 2010 IGN forum thread.",
              "Le LGBTQ Video Game Archive, projet de recherche dirigé par Adrienne Shaw, de l'université Temple, a publié le 24 juin 2016 une notice intitulée \"Quique Montemayor and Captain Vincente de Santa in Red Dead Redemption\". Il y classe les deux personnages dans la représentation gay et bisexuelle implicite. La notice affirme que les deux hommes semblent entretenir une relation intime au grand jour, que plusieurs personnages principaux le relèvent, et que De Santa flirte aussi avec des femmes. Elle cite, sans en nommer l'auteur, la réplique de Reyes sur les jeunes garçons qui dormiront tranquilles après la mort de De Santa, ainsi que le mot mariconcito. Ses sources sont deux pages du Red Dead Wiki, un billet de blog de 2013 et une discussion du forum d'IGN datée de 2010.")},
    {"h3": two("Academic study", "Étude universitaire")},
    {"p": two("In \"The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1\", published in the Revista Panamericana de Comunicación (vol. 4, no. 2, 2022), Javier Aldape, of Texas A&M University, mentions him once, as \"one of his subordinates, Captain Vicente De Santa\", who tells John that Colonel Allende knows where Bill Williamson and Javier Escuella are.",
              "Dans \"The Mustang Diaries: A Study of Mexico in Red Dead Redemption 1\", article paru dans la Revista Panamericana de Comunicación (vol. 4, n° 2, 2022), Javier Aldape, de l'université Texas A&M, ne le cite qu'une fois, comme \"one of his subordinates, Captain Vicente De Santa\" (l'un de ses subordonnés, le capitaine Vicente De Santa), qui annonce à John que le colonel Allende sait où se trouvent Bill Williamson et Javier Escuella.")},
]


BASE = {
    "slug": "vincente-de-santa", "name": "Vincente de Santa",
    "publishDate": "2026-09-18", "updated": "2026-10-21", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Mexican Army captain &middot; RDR1", "reg_role_fr": "Capitaine de l'armée mexicaine &middot; RDR1",
    "gender": "Male", "birth": "1877", "death": "1911", "nationality": "Mexican",
    "portrait_alt": two("Captain Vincente de Santa in his army tunic in Red Dead Redemption",
                        "Le capitaine Vincente de Santa en vareuse militaire dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; Nuevo Paraiso", "Personnage &middot; Nuevo Paraíso"),
    "meta_desc": two("Vincente de Santa, Mexican Army captain under Colonel Allende in Red Dead Redemption: his missions with John Marston, the Chuparosa betrayal, his death at Sepulcro in 1911, Hector Luis Bustamante.",
                     "Vincente de Santa, capitaine de l'armée mexicaine sous les ordres du colonel Allende dans Red Dead Redemption : ses missions avec John Marston, la trahison de Chuparosa, sa mort à Sepulcro en 1911, Hector Luis Bustamante."),
    "og_desc": two("The complete reference on Vincente de Santa: life, missions, quotes, development and reception.",
                   "La référence complète sur Vincente de Santa : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Captain in the Mexican Army under Colonel Agustin Allende, who employs John Marston against the rebels, betrays him in Chuparosa and is killed at Sepulcro in 1911 in Red Dead Redemption.",
                       "Capitaine de l'armée mexicaine sous les ordres du colonel Agustin Allende, qui emploie John Marston contre les rebelles, le trahit à Chuparosa et meurt à Sepulcro en 1911 dans Red Dead Redemption."),
    "chips": [two("Captain, Mexican Army", "Capitaine de l'armée mexicaine"),
              two("Officer of Colonel Allende", "Officier du colonel Allende"),
              two("Died in <strong>1911</strong>", "Mort en <strong>1911</strong>"),
              two("Voiced by <strong>Hector Luis Bustamante</strong>", "Voix : <strong>Hector Luis Bustamante</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Vincente de Santa (Vicente in the Blackwater Ledger)", "Vincente de Santa (Vicente dans le Blackwater Ledger)")},
        {"label": two("Born", "Naissance"), "value": two("1877, according to his gravestone at Sepulcro, present when Undead Nightmare is installed (Red Dead Wiki); the Game of the Year Edition guide, quoted by the wiki, describes him as 33 years old", "1877, d'après sa pierre tombale à Sepulcro, présente quand Undead Nightmare est installé (Red Dead Wiki) ; le guide de l'édition Game of the Year, cité par le wiki, lui donne 33 ans")},
        {"label": two("Died", "Mort"), "value": two("1911, at Sepulcro (\"Captain De Santa's Downfall\"), shot by John Marston or by Reyes's rebels depending on the player; the Blackwater Ledger gives his age as 34", "1911, à Sepulcro (\"Captain De Santa's Downfall\"), abattu par John Marston ou par les rebelles de Reyes selon le joueur ; le Blackwater Ledger lui donne 34 ans")},
        {"label": two("Nationality", "Nationalité"), "value": two("Mexican", "Mexicaine")},
        {"label": two("Occupation", "Activité"), "value": two("Captain in the Mexican Army, under Colonel [[agustin-allende|Agustin Allende]]", "Capitaine de l'armée mexicaine, sous les ordres du colonel [[agustin-allende|Agustin Allende]]")},
        {"label": two("Based at", "Basé à"), "value": two("Allende's mansion in Escalera, Punta Orgullo", "La demeure d'Allende à Escalera, Punta Orgullo")},
        {"label": two("Family", "Famille"), "value": two("An unnamed father and mother", "Un père et une mère dont les noms ne sont pas donnés")},
        {"label": two("Rival", "Rival"), "value": two("Captain Espinoza", "Le capitaine Espinoza")},
        {"label": two("Enemies", "Ennemis"), "value": two("[[abraham-reyes|Abraham Reyes]] and his rebels, [[luisa-fortuna|Luisa Fortuna]], [[john-marston|John Marston]] (after Chuparosa)", "[[abraham-reyes|Abraham Reyes]] et ses rebelles, [[luisa-fortuna|Luisa Fortuna]], [[john-marston|John Marston]] (après Chuparosa)")},
        {"label": two("Weapons and horse", "Armes et monture"), "value": two("Cattleman Revolver, Repeater Carbine, Painted Quarter Horse (Red Dead Wiki)", "Cattleman Revolver, Repeater Carbine, Painted Quarter Horse (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption; Undead Nightmare; multiplayer model (Myths and Mavericks)", "Red Dead Redemption ; Undead Nightmare ; modèle multijoueur (Myths and Mavericks)")},
        {"label": two("Voiced by", "Voix"), "value": two("Hector Luis Bustamante", "Hector Luis Bustamante")},
    ],
    "intro": [
        two("Captain Vincente de Santa is an officer of the Mexican Army in Red Dead Redemption (2010), set in 1911. He serves Colonel [[agustin-allende|Agustin Allende]], governor of Nuevo Paraíso, in the war against the rebels of [[abraham-reyes|Abraham Reyes]]. When [[john-marston|John Marston]] arrives in Escalera looking for [[bill-williamson|Bill Williamson]] and [[javier-escuella|Javier Escuella]], De Santa takes him along against the rebels and promises that the colonel will help him in return. John then fights the rebels with his men on a decoy train escort, at Tesoro Azul and at Torquemada.",
            "Le capitaine Vincente de Santa est un officier de l'armée mexicaine dans Red Dead Redemption (2010), dont l'action se déroule en 1911. Il sert le colonel [[agustin-allende|Agustin Allende]], gouverneur du Nuevo Paraíso, dans la guerre contre les rebelles d'[[abraham-reyes|Abraham Reyes]]. Quand [[john-marston|John Marston]] arrive à Escalera sur la piste de [[bill-williamson|Bill Williamson]] et de [[javier-escuella|Javier Escuella]], De Santa l'emmène combattre les rebelles en lui promettant l'aide du colonel en retour. John combat ensuite les rebelles avec ses hommes, lors de l'escorte d'un train leurre, à Tesoro Azul et à Torquemada."),
        two("De Santa then leads John into a trap in Chuparosa, where Reyes's rebels save him from the firing squad. John catches up with him at Sepulcro, where he has been sent to oversee a massacre of rebels, and he dies there, shot by John or by the rebels. He is voiced by Hector Luis Bustamante.",
            "De Santa attire ensuite John dans un piège à Chuparosa, où les rebelles de Reyes le sauvent du peloton d'exécution. John le rattrape à Sepulcro, où on l'a envoyé superviser un massacre de rebelles, et il y meurt, abattu par John ou par les rebelles. Il a la voix de Hector Luis Bustamante."),
    ],
    "essentials": [
        two("In \"Civilization, at Any Price\", he meets John in Escalera and has him escort a decoy train out of Chuparosa to lure the rebels.",
            "Dans \"Civilization, at Any Price\", il fait la connaissance de John à Escalera et l'emmène escorter, au départ de Chuparosa, un train leurre destiné à attirer les rebelles."),
        two("In \"The Demon Drink\" and \"Empty Promises\", he leads John against the rebels at Tesoro Azul and Torquemada.",
            "Dans \"The Demon Drink\" et \"Empty Promises\", il mène John contre les rebelles à Tesoro Azul et à Torquemada."),
        two("In \"Mexican Caesar\", he offers John 20,000 pesos and Javier's whereabouts, on Allende's behalf, to escort a munitions train with Captain Espinoza.",
            "Dans \"Mexican Caesar\", il propose à John, au nom d'Allende, 20 000 pesos et la cachette de Javier pour escorter un train de munitions avec le capitaine Espinoza."),
        two("In \"Cowards Die Many Times\", he takes John to Chuparosa, where Bill and Javier are said to be prisoners, and has him seized; Reyes's rebels save John.",
            "Dans \"Cowards Die Many Times\", il conduit John à Chuparosa, où Bill et Javier seraient prisonniers, et le fait capturer ; les rebelles de Reyes sauvent John."),
        two("In \"Captain De Santa's Downfall\", John captures him at Sepulcro; he names Casa Madrugada as Javier's hiding place, a trap, and is shot by John or by the rebels.",
            "Dans \"Captain De Santa's Downfall\", John le capture à Sepulcro ; il désigne la Casa Madrugada comme cachette de Javier, un piège, et il est abattu par John ou par les rebelles."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["agustin-allende", "abraham-reyes", "john-marston", "luisa-fortuna"],
}
