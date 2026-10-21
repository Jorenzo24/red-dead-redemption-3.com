"""Nigel West Dickens, reference fiche, PART D: base data, Development and performance, Reception
(21 Oct 2026, medium tier).

His live page (characters/nigel-west-dickens/) was generated from the v2 entry in scripts/_wave4.py (order 20,
"slug": "nigel-west-dickens"; no entry in _enrich.py). publishDate 2026-08-02 kept (git f640807, drip publish of
nigel-west-dickens, 2 Aug 2026). Eyebrow kept as on the live page ("Character &middot; New Austin"); reg_role matches
characters_registry.py ("Con-artist &middot; RDR1" / "Escroc &middot; RDR1").
Corrections to the v2 base:
- v2 facts "Born c. 1846, Fort Wayne, Indiana": no birth date or birthplace is given in the game. The age (65)
  comes from the Game of the Year Edition guide, quoted by the Red Dead Wiki; Fort Wayne is where he says he grew up
  "mostly", in a conversation the wiki quotes (no cached transcript). Both attributed.
- v2 "his manner is based on the comedian W.C. Fields": Red Dead Wiki trivia worded as an impression ("seem to be
  based upon"), no Rockstar source found. Dropped.
- v2 "Red Dead Redemption (2010) and its 2024 remaster": dropped (the 2023 console port and 2024 PC port are not a
  remaster; ports are not needed here).
- v2 "charming, cowardly fraud", "a central ally", "reluctant ally": interpretation; replaced by the GOTY guide quote
  (part B) and by facts.
- v2 "His elixir is little more than alcohol laced with opium": the only in-game source is the RDR2 letter of
  T. Bernadette Moncrief, who "suspects" laudanum or opium; Leigh Johnson calls him a narcotic salesman. Told in
  part B with attribution, not as a fact.
- v2 scar "implying he was once nearly lynched": speculation, dropped (part B keeps the scar, attributed).
- v2 "Games: Red Dead Redemption": Undead Nightmare and the Red Dead Redemption 2 mentions added.
- v2 relationship "Seth Briars, slug None": Seth is live; links are part B's business.

SOURCE REGISTER (read 21 Oct 2026):
- Wikipedia "Don Creech" (WebFetch): American actor born in New York; Mr. Sweeney in Ned's Declassified School
  Survival Guide (2004-2007); "the snake oil merchant Nigel West Dickens in the 2010 video game Red Dead Redemption";
  video game credits Red Dead Redemption (2010) and Red Dead Redemption: Undead Nightmare (2010); William Stryker in
  X-Men: First Class (2011).
- Red Dead Wiki "Don Creech" (_m/Don_Creech.txt): born October 30, 1948 (attributed); infobox voice credit.
- Wikipedia "Development of Red Dead Redemption" and "John Marston" (WebFetch): "The first scene to be recorded was
  John meeting Nigel West Dickens", citing IGN, Luke Reilly, "Red Dead Redemption 10 Years On: How Rockstar Won the
  West", 22 May 2020. The IGN page itself could not be fetched (blocked): cited through Wikipedia.
  NB: john_D.py attributes the same fact to producer Rob Nelson (Variety, 24 Oct 2018 per john_marston.py); not
  re-verified here. Left for the lead to reconcile; this part names only IGN.
- Red Dead Wiki "Red Dead Redemption Cut Content" (_m/): leftover cutscene "fbi03" (Ross, Fordham, John), after which
  the Dickens scene of "Bear One Another's Burdens" would have played (attributed).
- Red Dead Wiki "Liars and Cheats" (_m/): pack released 21 Sep 2010; 15 story characters added to multiplayer,
  Dickens in the "Redemption" group (part C, Other media, owns the details).
- Newspaper "Man Exposes Medical Frauds" (RDR2: Blackwater Ledger No. 75, New Hanover Gazette No. 40, Saint Denis
  Times No. 56; _m/Man_Exposes_Medical_Frauds.txt), Sawed-Off Shotgun (RDR 2) catalogue letter: used here only for
  the "Games" fact and the essentials.
- Reception: Sportskeeda, Aniket Mukherjee, "10 best characters in the Red Dead Redemption franchise", 13 Aug 2023
  (scripts/v3/work/landon/fc/sportskeeda_2023-08-13.txt, read: Dickens 6th, after Leigh Johnson 7th, before Bill
  Williamson 5th); Gameranx, Dennis Patrick, "Characters We Wouldn't Mind Seeing Again In Red Dead Redemption 2",
  4 Nov 2016 (WebFetch).

Excluded: the W.C. Fields and Mr. Micawber model, The Outlaw Josey Wales "Carpetbagger" (wiki speculation); motion
capture for Dickens (no source names a performer); Creech's height and other credits beyond those Wikipedia names;
"a 2024 remaster"; ranker.com fan votes (not a press source); The Man from Blackwater (2010 machinima) left to part C,
Other media.
DUPLICATE ownership: the actor, the first recorded scene and the cut fbi03 cutscene live HERE; part C (Trivia, Other
media) must not repeat them.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Nigel West Dickens appears in Red Dead Redemption and its expansion Undead Nightmare, both released in 2010. He is voiced by Don Creech, credited in the role by Wikipedia and by the Red Dead Wiki. Creech is an American actor born in New York; the Red Dead Wiki gives 30 October 1948 as his date of birth. According to Wikipedia, his other roles include Mr. Sweeney, the science teacher of the series Ned's Declassified School Survival Guide (2004 to 2007), and William Stryker in the film X-Men: First Class (2011).",
              "Nigel West Dickens apparaît dans Red Dead Redemption et dans son extension Undead Nightmare, sortis tous deux en 2010. Il a la voix de Don Creech, que Wikipédia et le Red Dead Wiki créditent dans ce rôle. Creech est un acteur américain né à New York ; le Red Dead Wiki le fait naître le 30 octobre 1948. Selon Wikipédia, on lui doit aussi le rôle de M. Sweeney, le professeur de sciences de la série Ned's Declassified School Survival Guide (2004 à 2007), et celui de William Stryker dans le film X-Men : Le Commencement (2011).")},
    {"h3": two("Production", "Production")},
    {"p": two("According to IGN's retrospective \"Red Dead Redemption 10 Years On: How Rockstar Won the West\", published by Luke Reilly on 22 May 2020 and cited by Wikipedia, the first scene recorded for the game was John Marston's meeting with Dickens. According to the Red Dead Wiki, the game files contain a cut cutscene with the code name fbi03, in which Edgar Ross briefs John with Archer Fordham present; the Dickens scene of \"Bear One Another's Burdens\" would then have followed.",
              "Selon la rétrospective d'IGN \"Red Dead Redemption 10 Years On: How Rockstar Won the West\", signée Luke Reilly le 22 mai 2020 et citée par Wikipédia, la première scène enregistrée pour le jeu est la rencontre entre John Marston et Dickens. D'après le Red Dead Wiki, les fichiers du jeu conservent une cinématique coupée, de nom de code fbi03, où Edgar Ross donne ses instructions à John en présence d'Archer Fordham ; la scène de Dickens de \"Bear One Another's Burdens\" devait suivre.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Character lists", "Classements de personnages")},
    {"p": two("On 4 November 2016, Dennis Patrick of Gameranx included Dickens among the characters he wanted to see again in Red Dead Redemption 2, describing him as \"a man that John Marston hated to work with but managed to come in handy from time-to-time\". In a list of the ten best characters of the Red Dead Redemption franchise, published by Sportskeeda on 13 August 2023, Aniket Mukherjee ranked him sixth, between Leigh Johnson (seventh) and Bill Williamson (fifth). The author wrote that his \"extravagant schemes and outrageous adventures bring lighthearted humor\" to the game's more serious tone.",
              "Le 4 novembre 2016, Dennis Patrick, de Gameranx, cite Dickens parmi les personnages qu'il aimerait revoir dans Red Dead Redemption 2, en le décrivant comme \"a man that John Marston hated to work with but managed to come in handy from time-to-time\" (un homme avec qui John Marston détestait travailler, mais qui s'est révélé utile de temps à autre). Dans une liste des dix meilleurs personnages de la série Red Dead Redemption publiée par Sportskeeda le 13 août 2023, Aniket Mukherjee le classe sixième, entre Leigh Johnson (septième) et Bill Williamson (cinquième). L'auteur écrit que ses \"extravagant schemes and outrageous adventures bring lighthearted humor\" (combines extravagantes et aventures rocambolesques apportent une touche d'humour) au ton plus grave du jeu.")},
]


BASE = {
    "slug": "nigel-west-dickens", "name": "Nigel West Dickens",
    "publishDate": "2026-08-02", "updated": "2026-10-21", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Con-artist &middot; RDR1", "reg_role_fr": "Escroc &middot; RDR1",
    "gender": "Male", "birth": None, "death": None, "nationality": "American",
    "portrait_alt": two("Nigel West Dickens in Red Dead Redemption", "Nigel West Dickens dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; New Austin", "Personnage &middot; New Austin"),
    "meta_desc": two("Nigel West Dickens, the elixir salesman of Red Dead Redemption: his shows and races with John Marston, the Trojan horse wagon at Fort Mercer, Don Creech.",
                     "Nigel West Dickens, le vendeur d'élixir de Red Dead Redemption : ses spectacles et ses courses avec John Marston, le chariot piégé de Fort Mercer, Don Creech."),
    "og_desc": two("The complete reference on Nigel West Dickens: life, missions, quotes, development and reception.",
                   "La référence complète sur Nigel West Dickens : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Traveling seller of miracle tonics in New Austin who, in 1911, uses John Marston in his shows and races, introduces him to Seth Briars and Irish, and drives him into Fort Mercer hidden in his wagon, in Red Dead Redemption.",
                       "Marchand ambulant de toniques miracles au New Austin qui, en 1911, se sert de John Marston pour ses spectacles et ses courses, lui présente Seth Briars et Irish, et le fait entrer dans Fort Mercer caché dans son chariot, dans Red Dead Redemption."),
    "chips": [two("Elixir salesman", "Vendeur d'élixir"), two("New Austin", "New Austin"),
              two("Alive in <strong>1911</strong>", "Vivant en <strong>1911</strong>"),
              two("Voiced by <strong>Don Creech</strong>", "Voix : <strong>Don Creech</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Nigel West Dickens", "Nigel West Dickens")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game; 65 years old in 1911 according to the Game of the Year Edition guide, quoted by the Red Dead Wiki (about 1846)", "Non précisée dans le jeu ; 65 ans en 1911 selon le guide de l'édition Game of the Year, cité par le Red Dead Wiki (vers 1846)")},
        {"label": two("Grew up", "Enfance"), "value": two("Mostly in Fort Wayne, Indiana, by his own account (conversation quoted by the Red Dead Wiki)", "Surtout à Fort Wayne, dans l'Indiana, à l'en croire (conversation citée par le Red Dead Wiki)")},
        {"label": two("Status", "Statut"), "value": two("Alive at his last appearance (1911)", "Vivant lors de sa dernière apparition (1911)")},
        {"label": two("Nationality", "Nationalité"), "value": two("American (speaks with an English accent)", "Américaine (parle avec un accent anglais)")},
        {"label": two("Residence", "Résidence"), "value": two("Itinerant; a cave at Cueva Seca, New Austin (1911)", "Itinérant ; une grotte à Cueva Seca, au New Austin (1911)")},
        {"label": two("Occupation", "Activité"), "value": two("Traveling seller of tonics and elixirs", "Marchand ambulant de toniques et d'élixirs")},
        {"label": two("Allies", "Alliés"), "value": two("[[john-marston|John Marston]], [[seth-briars|Seth Briars]], [[irish|Irish]]", "[[john-marston|John Marston]], [[seth-briars|Seth Briars]], [[irish|Irish]]")},
        {"label": two("Weapon", "Arme"), "value": two("Cattleman Revolver (Red Dead Wiki)", "Cattleman Revolver (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption, Undead Nightmare; mentioned in Red Dead Redemption 2", "Red Dead Redemption, Undead Nightmare ; cité dans Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Don Creech", "Don Creech")},
    ],
    "intro": [
        two("Nigel West Dickens is a traveling seller of miracle tonics in Red Dead Redemption (2010), set in 1911. [[john-marston|John Marston]] finds him wounded beside his wagon and drives him to the doctor in Armadillo. Dickens then offers to help John against Fort Mercer, the hideout of [[bill-williamson|Bill Williamson]]'s gang. In return John poses as a volunteer in his elixir shows and wins two races for him. Dickens introduces John to [[seth-briars|Seth Briars]] and [[irish|Irish]], has his wagon armored, and drives it into Fort Mercer with John and a machine gun hidden inside. He is last seen in Blackwater, where John has him released after a narcotics arrest.",
            "Nigel West Dickens est un marchand ambulant de toniques miracles dans Red Dead Redemption (2010), dont l'action se déroule en 1911. [[john-marston|John Marston]] le trouve blessé près de son chariot et le conduit chez le médecin d'Armadillo. Dickens propose alors à John de l'aider contre Fort Mercer, repaire de la bande de [[bill-williamson|Bill Williamson]]. En échange, John joue les volontaires dans ses spectacles et remporte deux courses pour lui. Dickens présente John à [[seth-briars|Seth Briars]] et à [[irish|Irish]], fait blinder son chariot et entre avec lui dans Fort Mercer, John et une mitrailleuse cachés à l'intérieur. On le revoit une dernière fois à Blackwater, où John le fait relâcher après une arrestation pour stupéfiants."),
        two("He is voiced by Don Creech. He also appears in Undead Nightmare, and Red Dead Redemption 2 mentions him in a gunsmith's catalogue and in a 1907 newspaper article.",
            "Il a la voix de Don Creech. Il apparaît aussi dans Undead Nightmare, et Red Dead Redemption 2 le cite dans le catalogue d'un armurier et dans un article de journal de 1907."),
    ],
    "essentials": [
        two("In \"Old Swindler Blues\", John finds him wounded beside his wagon and drives him to the Armadillo doctor while fighting off his attackers.",
            "Dans \"Old Swindler Blues\", John le trouve blessé près de son chariot et le conduit chez le médecin d'Armadillo en repoussant ses agresseurs."),
        two("He uses John as a planted volunteer at Ridgewood Farm and as his entrant in two races, at Gaptooth Breach and Rathskeller Fork, to pay for the armor on his wagon.",
            "Il fait de John un faux volontaire à Ridgewood Farm, puis son concurrent dans deux courses, à Gaptooth Breach et à Rathskeller Fork, pour financer le blindage de son chariot."),
        two("In \"The Assault on Fort Mercer\", his wagon gets through the gate with John and a machine gun hidden inside.",
            "Dans \"The Assault on Fort Mercer\", son chariot franchit la porte du fort avec John et une mitrailleuse cachés à l'intérieur."),
        two("In \"Bear One Another's Burdens\", he is brought into the Blackwater police building on a narcotics charge, and Edgar Ross lets him go at John's request.",
            "Dans \"Bear One Another's Burdens\", on l'amène au poste de police de Blackwater pour détention de stupéfiants, et Edgar Ross le relâche à la demande de John."),
        two("In Red Dead Redemption 2, he is mentioned in a 1907 newspaper article and in the letter of an Annesburg woman whose parents bought his medicine.",
            "Dans Red Dead Redemption 2, il est cité dans un article de journal de 1907 et dans la lettre d'une habitante d'Annesburg dont les parents ont acheté sa médecine."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["john-marston", "seth-briars", "irish", "leigh-johnson"],
}
