"""Alberto Fussar, reference fiche, PART D: base data, Development and performance, Reception
(22 Oct 2026, medium tier).

His live page (characters/alberto-fussar/) was generated from the v2 entry in scripts/_wave7.py ("slug":
"alberto-fussar", order 46; no entry in _enrich.py). The base below is rebuilt from that entry, with corrections:
- v2 said he "runs the sugar plantation and refinery" and that "an in-game newspaper describes his rule over the
  island as quasi-military": kept, but the newspaper attributes the phrase to his detractors (now said so in B).
- v2 called Levi Simon "an American" as a fact: wiki-only, now attributed in B.
- v2 said Fussar "escapes through a window" (no source: the transcript says he fires into the air and runs) and that
  he takes position with "an artillery piece" (it is a cannon: transcript stage note, Hercule's "He's shooting",
  FussarCanon screenshot; FIX_RULES 1; told in B Weapons).
- v2 said Arthur sinks the warship "at the fort of Cinco Torres" and that Fussar "calls in a warship from Cuba":
  confirmed by the transcript (Hercule: "Fussar has called in the navy from Cuba").
- v2 og_desc "the man standing between the gang and the boat home" (mood line) replaced by a factual sentence.
- chips: "RDR2" and "Guarma" chips replaced by Colonel and Played by; facts grid gains Name, Born, Died, Nationality
  (not stated in the game; Cuban per the Red Dead Wiki), Occupation, Residence, Allies, Enemies, Played by.
Eyebrow (kicker) kept as on the live page ("Character &middot; Guarma"); reg_role matches characters_registry.py
("Governor of Guarma &middot; RDR2"). publishDate 2026-10-17 kept (live byline "Updated October 17, 2026").

Sources (internal register, fetched 22 Oct 2026, saved in scripts/v3/work/fussar/fc/):
- Wikipedia "List of Red Dead Redemption 2 characters" (copy in scripts/v3/work/catherine/fc/wp_list_rdr2.txt):
  "the controversial Guarman ruler Colonel Alberto Fussar (Alfredo Narciso)", citing the game's credits.
- Red Dead Wiki "Alberto Fussar" (infobox: voice Alfredo Narciso) and "Alfredo Narciso" (stub: American actor born in
  Milwaukee, Wisconsin).
- Wikipedia "Alfredo Narciso" (wp_alfredo_narciso.txt): born in Milwaukee (cited); the birth date July 8, 1973 is
  uncited in the article (BLP sources tag) and is NOT used (FIX_RULES 6); Broadway credits The
  Motherfucker with the Hat and A Streetcar Named Desire; TV credits incl. Law & Order, Person of Interest, Blue Bloods.
  The article does not list the game.
- Alfredo Narciso's website, news post dated November 6, 2018 (Wayback snapshot of 20 Aug 2019,
  narciso_rdr2_post.txt): "Check me out as the villain, Alberto Fussar, in Red Dead Redemption 2! Looks like fun,
  maggots." Website biography (Wayback snapshot of 20 May 2024, narciso_home_2024-05-20.txt): "He can also be heard
  voicing Alberto Fussar in Red Dead Redemption 2"; film credits Demolition, The Dark Tower; TV credits House of Cards,
  Homeland, Manifest; Ambie nomination for The Two Princes.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content": "Madeline Fussar" files (hair, turban, open and closed veil);
  "GulFussars" (apparently Fussar's men) in animation files; unused hair for Fussar; a lady in a turban labeled for
  "A Kind and Benevolent Despot", internal name "FUS1"/"Fussar1"; Leon's niece (cut mission "smg1", audio bank FUS1).
- WhatCulture, Matt Thompson, "Red Dead Redemption: Every Villain Ranked From Worst To Best", 7 Feb 2022, page 1
  (wc_villains_p1.txt): Fussar ranked 15th and last.
Searched without result (22 Oct 2026): any interview in which Narciso discusses the role; any motion-capture credit
(search engines echo a "did motion capture" line that his own site does not contain: his site says "voicing").

Excluded: motion capture by Narciso (not sourced); Narciso's parents' nationalities (not about the role); the Hate
Sink Wiki and Villains Wiki descriptions (fan wikis); the Allende comparison (wiki trivia, interpretation).
DUPLICATE ownership: actor, cut content and the WhatCulture review live HERE; part C trivia must not repeat them.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Alberto Fussar appears only in Red Dead Redemption 2 (2018). He is played by Alfredo Narciso, credited in the role by Wikipedia's list of the game's characters, which cites the game's credits, and by the Red Dead Wiki. Narciso, born in Milwaukee, Wisconsin, is a New York-based stage and screen actor. His Broadway credits include The Motherfucker with the Hat and A Streetcar Named Desire, and his television credits include House of Cards, Homeland and Manifest. On November 6, 2018, shortly after the game's release, he posted on his website: \"Check me out as the villain, Alberto Fussar, in Red Dead Redemption 2! Looks like fun, maggots.\" His later website biography says he \"can also be heard voicing Alberto Fussar\". No interview in which he discusses the role has been found, and no source names him for the character's motion capture.",
              "Alberto Fussar n'apparaît que dans Red Dead Redemption 2 (2018). Il est interprété par Alfredo Narciso, que créditent dans ce rôle la liste des personnages du jeu sur Wikipédia, qui s'appuie sur le générique, et le Red Dead Wiki. Né à Milwaukee, dans le Wisconsin, Narciso est un acteur de théâtre et d'écran installé à New York. Il a joué à Broadway dans The Motherfucker with the Hat et Un tramway nommé Désir, et à la télévision dans House of Cards, Homeland et Manifest. Le 6 novembre 2018, peu après la sortie du jeu, il publie sur son site : \"Check me out as the villain, Alberto Fussar, in Red Dead Redemption 2! Looks like fun, maggots.\" (Venez me voir dans le rôle du méchant, Alberto Fussar, dans Red Dead Redemption 2 ! Ça a l'air amusant, bande de vermines). Sa biographie, plus tard, précise qu'on peut aussi l'entendre \"voicing Alberto Fussar\" (prêter sa voix à Alberto Fussar). Aucun entretien où il évoquerait ce rôle n'a été trouvé, et aucune source ne lui attribue la capture de mouvement du personnage.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The Red Dead Wiki's page on cut content lists several traces of unused material around Fussar in the game files. A character known only as \"Madeline Fussar\" has leftover files, with hair, a turban and an open and a closed veil. Animation files mention characters called \"GulFussars\", which appear to be Fussar's men. Fussar himself has an unused hairstyle. A lady in a turban is labeled for \"A Kind and Benevolent Despot\", whose internal name is \"Fussar1\". The same page describes a cut Guarma mission in which Arthur and Bill would have rescued the niece of the rebel Leon Fuentes; its dialogue sits in the audio bank of \"A Kind and Benevolent Despot\".",
              "La page du Red Dead Wiki consacrée au contenu coupé relève plusieurs traces de matériel inutilisé autour de Fussar dans les fichiers du jeu. Un personnage désigné seulement comme \"Madeline Fussar\" y a laissé des fichiers, avec une coiffure, un turban et une voilette ouverte et fermée. Des fichiers d'animation mentionnent des personnages appelés \"GulFussars\", qui semblent être ses hommes. Fussar lui-même dispose d'une coiffure inutilisée. Une dame en turban est associée à \"A Kind and Benevolent Despot\", mission dont le nom interne est \"Fussar1\". La même page décrit une mission coupée à Guarma, dans laquelle Arthur et Bill auraient sauvé la nièce du rebelle Leon Fuentes ; ses dialogues se trouvent dans la banque audio de \"A Kind and Benevolent Despot\".")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Ranked last in WhatCulture's 2022 list", "Dernier du classement de WhatCulture en 2022")},
    {"p": two("WhatCulture's Matt Thompson ranked fifteen villains of the Red Dead Redemption games on February 7, 2022, and put Fussar fifteenth, in last place. He called chapter 5 \"a lulling low-point in the game\" and wrote that the revolution on Guarma has no impact on the rest of the story. He described Fussar as \"a nothing character; a nameless, almost faceless villain\", whose role as a threat could have been filled by a horde of militiamen. He granted that \"a loose tie to Leviticus Cornwall does make the villain more three-dimensional\". He added that the chapter shows Fussar's cruelty through tortured and amputated rebels, but without letting the player see glee or malice from Fussar himself, and that the game makes more of his right-hand man, Levi Simon.",
              "Matt Thompson, de WhatCulture, a classé quinze méchants des jeux Red Dead Redemption le 7 février 2022 et placé Fussar quinzième, en dernière position. Il qualifie le chapitre 5 de \"a lulling low-point in the game\" (un creux soporifique du jeu) et estime que la révolution de Guarma n'a aucune incidence sur la suite de l'histoire. Il voit en Fussar \"a nothing character; a nameless, almost faceless villain\" (un personnage insignifiant, un méchant sans nom et presque sans visage), dont le rôle de menace aurait pu être tenu par une horde de miliciens. Il concède que \"a loose tie to Leviticus Cornwall does make the villain more three-dimensional\" (un lien ténu avec Leviticus Cornwall donne un peu plus d'épaisseur au personnage). Il ajoute que le chapitre montre la cruauté de Fussar à travers des rebelles torturés et amputés, sans que le joueur voie jamais la jubilation ou la méchanceté de Fussar lui-même, et que le jeu en fait davantage avec son bras droit, Levi Simon.")},
]


BASE = {
    "slug": "alberto-fussar", "name": "Alberto Fussar",
    "publishDate": "2026-10-17", "updated": "2026-10-22", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Governor of Guarma &middot; RDR2", "reg_role_fr": "Gouverneur de Guarma &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": None,
    "portrait_alt": two("Alberto Fussar on his plantation in Guarma in Red Dead Redemption 2",
                        "Alberto Fussar sur sa plantation de Guarma dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Guarma", "Personnage &middot; Guarma"),
    "meta_desc": two("Alberto Fussar, the colonel who governs Guarma in RDR2: his sugar plantation, his deal with Cornwall, Javier's capture, his death at Arthur's hands in 1899, Alfredo Narciso.",
                     "Alberto Fussar, le colonel qui gouverne Guarma dans RDR2 : sa plantation sucrière, son accord avec Cornwall, la capture de Javier, sa mort face à Arthur en 1899, Alfredo Narciso."),
    "og_desc": two("The complete reference on Alberto Fussar: life, rule over Guarma, quotes, development and reception.",
                   "La référence complète sur Alberto Fussar : vie, pouvoir à Guarma, citations, conception et accueil."),
    "schema_desc": two("Colonel and governor of the Caribbean island of Guarma, who runs its sugar plantation, sells its sugar to Leviticus Cornwall and holds the shipwrecked Van der Linde gang on the island until Arthur Morgan kills him in 1899, in Red Dead Redemption 2.",
                       "Colonel et gouverneur de Guarma, île des Caraïbes, qui exploite sa plantation sucrière, vend son sucre à Leviticus Cornwall et retient sur l'île les naufragés du gang Van der Linde jusqu'à ce qu'Arthur Morgan le tue en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Governor of Guarma", "Gouverneur de Guarma"),
              two("Colonel", "Colonel"),
              two("Played by <strong>Alfredo Narciso</strong>", "Interprété par <strong>Alfredo Narciso</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Alberto Fussar", "Alberto Fussar")},
        {"label": two("Aliases", "Surnoms"), "value": two("Colonel Fussar, Mr. Fussar", "Colonel Fussar, Mr. Fussar")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, killed by [[arthur-morgan|Arthur Morgan]] on Guarma in \"Paradise Mercifully Departed\"", "1899, tué par [[arthur-morgan|Arthur Morgan]] à Guarma dans \"Paradise Mercifully Departed\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédé")},
        {"label": two("Nationality", "Nationalité"), "value": two("Not stated in the game; Cuban according to the Red Dead Wiki", "Non précisée dans le jeu ; cubaine selon le Red Dead Wiki")},
        {"label": two("Occupation", "Activité"), "value": two("Governor of Guarma, colonel, sugar plantation owner", "Gouverneur de Guarma, colonel, propriétaire d'une plantation sucrière")},
        {"label": two("Residence", "Résidence"), "value": two("Aguasdulces, Guarma", "Aguasdulces, Guarma")},
        {"label": two("Allies", "Alliés"), "value": two("Levi Simon, his overseer; [[leviticus-cornwall|Leviticus Cornwall]], who buys his sugar", "Levi Simon, son contremaître ; [[leviticus-cornwall|Leviticus Cornwall]], qui lui achète son sucre")},
        {"label": two("Enemies", "Ennemis"), "value": two("[[hercule-fontaine|Hercule Fontaine]] and the Guarma rebels; the Van der Linde gang", "[[hercule-fontaine|Hercule Fontaine]] et les rebelles de Guarma ; le gang Van der Linde")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Alfredo Narciso", "Alfredo Narciso")},
    ],
    "intro": [
        two("Alberto Fussar is the governor of Guarma, a Caribbean island, in Red Dead Redemption 2 (2018), set in 1899. He holds the rank of colonel and runs the island's sugar plantation from his compound at Aguasdulces, with his overseer Levi Simon. He sells the island's sugar to [[leviticus-cornwall|Leviticus Cornwall]] under an exclusive purchase order. In chapter 4 he is a guest at the mayor's party in Saint Denis, where [[angelo-bronte|Angelo Bronte]] points him out to [[dutch-van-der-linde|Dutch]] and [[arthur-morgan|Arthur]]. In chapter 5 the gang is shipwrecked on Guarma; his soldiers capture [[javier-escuella|Javier Escuella]], and he tries to keep the castaways on the island. Arthur kills him with a cannon shot as the gang fights its way to the ship.",
            "Alberto Fussar est le gouverneur de Guarma, une île des Caraïbes, dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Colonel, il dirige la plantation sucrière de l'île depuis son domaine d'Aguasdulces, secondé par son contremaître Levi Simon. Il vend le sucre de l'île à [[leviticus-cornwall|Leviticus Cornwall]] en vertu d'une commande exclusive. Au chapitre 4, il figure parmi les invités de la réception du maire de Saint-Denis, où [[angelo-bronte|Angelo Bronte]] le désigne à [[dutch-van-der-linde|Dutch]] et à [[arthur-morgan|Arthur]]. Au chapitre 5, la bande fait naufrage à Guarma ; ses soldats capturent [[javier-escuella|Javier Escuella]], et il cherche à retenir les naufragés sur l'île. Arthur le tue d'un coup de canon alors que la bande se fraie un chemin jusqu'au bateau."),
        two("He is the main antagonist of the Guarma chapter. He is played by Alfredo Narciso.",
            "C'est le principal antagoniste du chapitre de Guarma. Il est interprété par Alfredo Narciso."),
    ],
    "essentials": [
        two("He governs Guarma as a colonel and runs its sugar plantation; the rebel Leon Fuentes describes its workers as little more than slaves brought from other islands.",
            "Il gouverne Guarma avec le grade de colonel et exploite sa plantation sucrière ; le rebelle Leon Fuentes décrit des ouvriers à peine mieux traités que des esclaves, amenés d'autres îles."),
        two("He sells his sugar to [[leviticus-cornwall|Leviticus Cornwall]], who, according to the newspaper article \"Guarma Island Sugar Boom\", called him a great friend of America.",
            "Il vend son sucre à [[leviticus-cornwall|Leviticus Cornwall]], qui, d'après l'article \"Guarma Island Sugar Boom\", l'a qualifié de grand ami de l'Amérique."),
        two("In \"A Kind and Benevolent Despot\", his soldiers drag the captured [[javier-escuella|Javier]] into Aguasdulces, where he questions him before Dutch and Arthur free him.",
            "Dans \"A Kind and Benevolent Despot\", ses soldats traînent [[javier-escuella|Javier]], prisonnier, jusqu'à Aguasdulces, où il l'interroge avant que Dutch et Arthur ne le libèrent."),
        two("He calls in a warship from Cuba and sets up gun batteries to keep the gang from leaving the island.",
            "Il fait venir un navire de guerre de Cuba et installe des batteries pour empêcher la bande de quitter l'île."),
        two("In \"Paradise Mercifully Departed\", he escapes the cabin standoff in which Levi Simon dies, then opens fire from a tower over the harbor; Arthur brings it down with a cannon shot.",
            "Dans \"Paradise Mercifully Departed\", il s'échappe du face-à-face dans la cabane où meurt Levi Simon, puis ouvre le feu du haut d'une tour qui domine le port ; Arthur l'abat d'un coup de canon."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["leviticus-cornwall", "hercule-fontaine", "javier-escuella", "dutch-van-der-linde"],
}
