"""Irish, reference fiche, PART D: base data, Development and performance, Reception (21 Oct 2026, medium tier).

His live page (characters/irish/) was generated from the v2 entry in scripts/_wave6.py (order 37, "slug": "irish"; no
entry in _enrich.py). publishDate 2026-09-30 kept (git 9a02fb5, drip publish of irish, 30 Sep 2026). Eyebrow kept as
on the live page ("Character &middot; New Austin"); reg_role matches characters_registry.py ("Gunrunner &middot; RDR1"
/ "Trafiquant d'armes &middot; RDR1").
Corrections to the v2 base:
- v2 "one of the three men John Marston recruits in New Austin to take Fort Mercer": John does not recruit him; Nigel
  West Dickens sends John to him ("Liars, Cheats and Other Proud Americans" transcript), and the Fort Mercer posse also
  includes Leigh Johnson and his deputies (HOUSE_FACTS). Rewritten.
- v2 "after a detour that nearly gets both of them killed": the false lead at Lake Don Julio endangers John alone;
  Irish disappears before the shooting (transcript and mission page). Rewritten.
- v2 "takes John to contacts who turn out to be hostile, and to places that turn out to be ambushes": only the lake
  cabin and the Mexican bank fit; replaced by the facts.
- v2 "Irish turns up again in Nuevo Paraiso, where he... keeps trading in weapons. His drinking is worse": false.
  He crosses the river with John in "We Shall Be Together in Paradise", leaves him on the Mexican bank and is never
  seen again; no arms trading in Mexico is shown.
- v2 relationship "Seth... plays the corpse at the gate": false (HOUSE_FACTS: Seth dances on the wall and welcomes
  the wagon). Relationships rebuilt in part B.
- v2 "death": None with no mention of 1914: the Blackwater Ledger & Sentinel No. 213 (1914) prints a notice about an
  "Irish male, of unknown name" who died by the accidental discharge of a gun in a Thieves' Landing outhouse
  (_m/Blackwater_Ledger_No_213.txt). The notice does not name him; the Red Dead Wiki attributes it to Irish. Kept as
  attributed, not as a fact: "death" stays None.
- v2 "Region: New Austin, later Nuevo Paraiso": he only lands in Nuevo Paraíso and leaves at once; replaced.
- v2 chips "RDR1" and "Irish immigrant": replaced by role, region, last appearance and voice.
- v2 "Behind the scenes" paragraph had no actor: K. Harrison Sweeney added (Wikipedia credit).

SOURCE REGISTER (read 21 Oct 2026; notes in scripts/v3/work/irish/fc/):
- Wikipedia "Red Dead Redemption" (landon/fc/wp_rdr.txt): "an alcoholic arms smuggler known as "Irish" (K. Harrison
  Sweeney)".
- Red Dead Wiki user blog by Spawny0908, "Spawny0908 interviews K Harrison Sweeney voice of Irish!", created
  10 Nov 2011 per the page history (fc/sweeney_interview_reddeadwiki_blog.txt): audition, Rod Edge, shoot dates
  (January 2009, June 2009, booth sessions October 2009, last session in New York), ad-libs, extra one-liners
  including a Mexican colonel, motion capture ("my first crack at it"), Undead Nightmare, the stereotype controversy,
  Wyoming, German/Scandinavian ancestry. A fan interview conducted in writing: attributed to Sweeney and to the blog.
- Kotaku, Kirk Hamilton, 27 Jan 2012 (fc/kotaku_2012-01-27.txt): "From the Trailer to the Grave".
- Game Informer, Matt Bertz, "Red Dead Trailer Introduces A Cast of Vagabonds", 25 Mar 2010 (WebFetch).
- Herald.ie, Cormac Byrne, "Irish 'drunk' sours launch of hit game", 20 May 2010, read in full on the Wayback Machine
  copy of 23 May 2010 (fc/herald_2010-05-20.txt).
- Sportskeeda, Aniket Mukherjee, "10 best characters in the Red Dead Redemption franchise", page modified 13 Aug 2023
  (landon/fc/sportskeeda_2023-08-13.txt): Irish ninth.
- Liars and Cheats pack: released 21 Sep 2010 (_m/Liars_and_Cheats.txt); Irish is a Damnation model there. Facts grid
  only; the detail belongs to part C (Other media).
- Transcripts of the five missions (_m/*_dialogues.txt) for the intro and essentials.

Excluded: the Herald's "town drunk" as our own description (quoted as the article's words only); "biggest video game in
10 years" and the sales forecast (not about Irish); whether "From the Trailer to the Grave" was ever completed or
released (no source found: only the 2012 announcement is given); IMDb credits (not read); Sweeney's joke answers
(Rob Wiethoff "sandbagged" him, the "full-blooded Aborigine" line) except as clearly framed; the identity of the
Mexican colonel Sweeney says he voiced (he does not name him); a Rockstar marketing page for the "teller of tall
tales" description (not found; part B quotes it through the wiki).
DUPLICATE ownership: the actor, the recording, the Undead Nightmare absence and its explanation live HERE; part C
(Trivia, Other media) must not repeat the absence from Undead Nightmare or the actor.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Wikipedia credits K. Harrison Sweeney as the voice of Irish in Red Dead Redemption (2010). Sweeney described his casting in a written interview published on a Red Dead Wiki user blog on November 10, 2011. According to him, his agent put him forward for an interactive game set in the Old West, and his audition called for an Irishman. The casting associates warned the actors in the waiting room that the producers were British, and that anyone not from Ireland or Wales should not bother. Sweeney says he can switch between five Irish dialects. The actors were asked to walk across the room so the casting team could see how they moved, then to improvise dialogue in front of a camera.",
              "Wikipédia attribue la voix d'Irish dans Red Dead Redemption (2010) à K. Harrison Sweeney. Sweeney a raconté son recrutement dans un entretien écrit, publié sur un blog d'utilisateur du Red Dead Wiki le 10 novembre 2011. D'après lui, son agent l'a proposé pour un jeu interactif situé dans le Far West, et son audition portait sur un rôle d'Irlandais. Les assistants de casting ont prévenu les acteurs dans la salle d'attente que les producteurs étaient britanniques, et que ceux qui ne venaient ni d'Irlande ni du pays de Galles pouvaient s'épargner la peine. Sweeney affirme pouvoir passer d'un accent irlandais à l'autre parmi cinq. Les candidats devaient traverser la pièce pour montrer leur façon de bouger, puis improviser des dialogues face à une caméra.")},
    {"p": two("Sweeney says he grew up in Wyoming and that his ancestry is mostly German and Scandinavian. He recalls that the director, Rod Edge, a Briton, and the producers were taken aback when they learned he was American.",
              "Sweeney dit avoir grandi dans le Wyoming et avoir des origines surtout allemandes et scandinaves. Il se souvient que le réalisateur, le Britannique Rod Edge, et les producteurs ont été surpris d'apprendre qu'il était américain.")},
    {"h3": two("Recording", "L'enregistrement")},
    {"p": two("In the same interview, Sweeney says the actors only received the lines of their own scenes. He shot for a few days in January 2009, came back for more missions in June 2009, and recorded the ambient lines, such as walking around or riding drunk, in a voice-over booth in October 2009; the last session took place in New York. He names some of his improvisations that were kept: Irish checking the horses, his mockery of Shaky's stutter and the exclamation that follows it. According to Sweeney, Edge reworked the oath Irish mutters after John knocks him down in front of the nuns.",
              "Dans le même entretien, Sweeney explique que les acteurs ne recevaient que les répliques de leurs propres scènes. Il a tourné quelques jours en janvier 2009, est revenu pour d'autres missions en juin 2009, puis a enregistré en cabine, en octobre 2009, les répliques d'ambiance, comme les déplacements ou les chevauchées en état d'ivresse ; la dernière séance a eu lieu à New York. Il cite plusieurs de ses improvisations conservées au montage : Irish qui examine les chevaux, ses moqueries sur le bégaiement de Shaky et l'exclamation qui suit. Selon Sweeney, Edge a retravaillé le juron qu'Irish lâche après que John l'a mis à terre devant les religieuses.")},
    {"p": two("Sweeney calls the role his first opportunity to do motion capture and thanks Rockstar Games for it. He adds that the producers, having heard him play with voices between takes, had him record a few one-line parts for characters they had not cast, including a Mexican colonel he does not name.",
              "Sweeney présente ce rôle comme sa première expérience de la capture de mouvement, et en remercie Rockstar Games. Il ajoute que les producteurs, qui l'avaient entendu s'amuser avec des voix entre deux prises, lui ont fait enregistrer quelques répliques isolées pour des personnages qu'ils n'avaient pas encore distribués, dont un colonel mexicain qu'il ne nomme pas.")},
    {"h3": two("Absence from Undead Nightmare", "L'absence dans Undead Nightmare")},
    {"p": two("Irish does not appear in Undead Nightmare, the 2010 expansion of Red Dead Redemption. Asked why in the 2011 interview, Sweeney first answers with a joke, then explains that he had booked another job while Rockstar was shooting the expansion, and says he would have loved to be in it.",
              "Irish n'apparaît pas dans Undead Nightmare, l'extension de Red Dead Redemption sortie en 2010. Interrogé à ce sujet en 2011, Sweeney répond d'abord par une plaisanterie, puis explique qu'il avait accepté un autre tournage pendant que Rockstar enregistrait l'extension, et qu'il aurait adoré en être.")},
    {"h3": two("After the game", "Après le jeu")},
    {"p": two("On January 27, 2012, Kotaku (Kirk Hamilton) relayed an announcement by Steve J. Palmer, the voice of Bill Williamson: a redneck zombie romantic comedy titled From the Trailer to the Grave, written by Sweeney, was to be shot in Wyoming in the fall of 2012 with five actors from Red Dead Redemption, among them Sweeney, Rob Wiethoff (John Marston), Brad Carter (Jonah) and Anthony De Longis (Leigh Johnson). In his 2011 interview, Sweeney already said he had written parts in the film for several members of the cast.",
              "Le 27 janvier 2012, Kotaku (Kirk Hamilton) relaie une annonce de Steve J. Palmer, la voix de Bill Williamson : une comédie romantique de zombies chez les rednecks, From the Trailer to the Grave, écrite par Sweeney, devait être tournée dans le Wyoming à l'automne 2012 avec cinq acteurs de Red Dead Redemption, dont Sweeney, Rob Wiethoff (John Marston), Brad Carter (Jonah) et Anthony De Longis (Leigh Johnson). Dans son entretien de 2011, Sweeney disait déjà avoir écrit des rôles pour plusieurs membres de la distribution.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Before and at launch", "Avant et pendant la sortie")},
    {"p": two("On March 25, 2010, Game Informer (Matt Bertz) described a new Rockstar teaser presenting the morally questionable inhabitants of the game's world, listing \"a drunken, gun-wielding Irishman\" among them and comparing the cast to that of the HBO series Deadwood. On May 20, 2010, the day before the game's release in Ireland and Britain, the Dublin newspaper Herald.ie published an article by Cormac Byrne titled \"Irish 'drunk' sours launch of hit game\". It warned that \"the stereotype of the drunken Paddy\" would again be exploited, since the game's \"town drunk\" was called Irish, and quoted a description of the character taken from a gaming forum.",
              "Le 25 mars 2010, Game Informer (Matt Bertz) décrit un nouveau teaser de Rockstar consacré aux personnages peu recommandables du jeu, parmi lesquels il relève \"a drunken, gun-wielding Irishman\" (un Irlandais ivre et armé), et compare cette galerie de personnages à celle de la série Deadwood, sur HBO. Le 20 mai 2010, la veille de la sortie du jeu en Irlande et au Royaume-Uni, le quotidien dublinois Herald.ie publie un article de Cormac Byrne intitulé \"Irish 'drunk' sours launch of hit game\" (un ivrogne irlandais gâche la sortie d'un jeu à succès). L'article regrette que \"the stereotype of the drunken Paddy\" (le cliché de l'Irlandais ivrogne) soit de nouveau exploité, puisque le \"town drunk\" (l'ivrogne du coin) du jeu s'appelle Irish, et cite une description du personnage tirée d'un forum de joueurs.")},
    {"h3": two("The actor's response", "La réponse de l'acteur")},
    {"p": two("Asked about the criticism in the November 2011 interview, Sweeney answered that people worried about the stereotype should relax: \"It's FICTION, people.\" He went on to advise critics, in a joking tone, to relax and play the game.",
              "Interrogé sur ces critiques dans l'entretien de novembre 2011, Sweeney répond que ceux que le cliché inquiète devraient se détendre : \"It's FICTION, people.\" (c'est de la fiction, les gars). Il conseille ensuite aux critiques, sur le ton de la plaisanterie, de se détendre et de jouer au jeu.")},
    {"h3": two("Character lists", "Classements de personnages")},
    {"p": two("In a list of the ten best characters of the Red Dead Redemption franchise published by Sportskeeda (page last modified on August 13, 2023), Aniket Mukherjee ranked Irish ninth, just behind Seth Briars, and called him \"the rowdy and always tipsy arms dealer\".",
              "Dans une liste des dix meilleurs personnages de la série Red Dead Redemption publiée par Sportskeeda (page modifiée pour la dernière fois le 13 août 2023), Aniket Mukherjee classe Irish neuvième, juste derrière Seth Briars, et le décrit comme \"the rowdy and always tipsy arms dealer\" (le trafiquant d'armes chahuteur et toujours éméché).")},
]


BASE = {
    "slug": "irish", "name": "Irish",
    "publishDate": "2026-09-30", "updated": "2026-10-21", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Gunrunner &middot; RDR1", "reg_role_fr": "Trafiquant d'armes &middot; RDR1",
    "gender": "Male", "birth": None, "death": None, "nationality": "Irish",
    "portrait_alt": two("Irish, revolver in hand, in Red Dead Redemption", "Irish, revolver à la main, dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; New Austin", "Personnage &middot; New Austin"),
    "meta_desc": two("Irish, the drunken arms dealer of Red Dead Redemption: the Gatling gun for Fort Mercer, Shaky's ammunition, the raft to Mexico, El Rato, K. Harrison Sweeney.",
                     "Irish, le trafiquant d'armes ivrogne de Red Dead Redemption : la Gatling de Fort Mercer, les munitions de Shaky, le radeau vers le Mexique, El Rato, K. Harrison Sweeney."),
    "og_desc": two("The complete reference on Irish: life, missions, quotes, development and reception.",
                   "La référence complète sur Irish : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Irish arms and contraband dealer in New Austin who, in 1911, finds the Gatling gun and its ammunition for John Marston's assault on Fort Mercer, then takes him across the river to Mexico by raft, in Red Dead Redemption.",
                       "Trafiquant d'armes et de contrebande irlandais du New Austin qui, en 1911, procure à John Marston la mitrailleuse Gatling et ses munitions pour l'assaut de Fort Mercer, puis lui fait passer le fleuve jusqu'au Mexique en radeau, dans Red Dead Redemption."),
    "chips": [two("Arms dealer", "Trafiquant d'armes"), two("New Austin", "New Austin"),
              two("Last seen in <strong>1911</strong>", "Vu pour la dernière fois en <strong>1911</strong>"),
              two("Voiced by <strong>K. Harrison Sweeney</strong>", "Voix : <strong>K. Harrison Sweeney</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Irish (nickname; no other name is given in the game)", "Irish (surnom ; le jeu ne lui donne aucun autre nom)")},
        {"label": two("Also known as", "Autres noms"), "value": two("El Rato, by his own account", "El Rato, à l'en croire")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Status", "Statut"), "value": two("Last seen in Nuevo Paraíso in 1911; the Red Dead Wiki attributes to him the 1914 notice of an Irishman of unknown name killed by his own gun in a Thieves' Landing outhouse", "Vu pour la dernière fois au Nuevo Paraíso en 1911 ; le Red Dead Wiki lui attribue l'avis de 1914 annonçant la mort d'un Irlandais au nom inconnu, tué par sa propre arme dans des latrines de Thieves' Landing")},
        {"label": two("Nationality", "Nationalité"), "value": two("Irish", "Irlandaise")},
        {"label": two("Residence", "Résidence"), "value": two("No fixed home; found in Armadillo, Benedict Point and Thieves' Landing (1911)", "Sans domicile fixe ; on le trouve à Armadillo, Benedict Point et Thieves' Landing (1911)")},
        {"label": two("Occupation", "Activité"), "value": two("Arms and contraband dealer", "Trafiquant d'armes et de contrebande")},
        {"label": two("Family", "Famille"), "value": two("A father who had his throat slit and a mother, by his own account; a brother, according to the Red Dead Wiki", "Un père mort égorgé et une mère, à l'en croire ; un frère, selon le Red Dead Wiki")},
        {"label": two("Associates", "Fréquentations"), "value": two("[[john-marston|John Marston]], [[nigel-west-dickens|Nigel West Dickens]], Shaky; formerly Welsh and French", "[[john-marston|John Marston]], [[nigel-west-dickens|Nigel West Dickens]], Shaky ; autrefois Welsh et French")},
        {"label": two("Weapons", "Armes"), "value": two("Cattleman Revolver; Repeater Carbine (Red Dead Wiki)", "Cattleman Revolver ; Repeater Carbine (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption; multiplayer model (Liars and Cheats pack, 2010)", "Red Dead Redemption ; modèle multijoueur (pack Liars and Cheats, 2010)")},
        {"label": two("Voiced by", "Voix"), "value": two("K. Harrison Sweeney", "K. Harrison Sweeney")},
    ],
    "intro": [
        two("Irish is an Irish arms dealer and heavy drinker in Red Dead Redemption (2010), set in 1911. [[nigel-west-dickens|Nigel West Dickens]] sends [[john-marston|John Marston]] to him for the firepower needed against Fort Mercer, the hideout of [[bill-williamson|Bill Williamson]]'s gang. John saves him from two former friends who are drowning him in Armadillo. Irish first sends John to an empty cabin, then leads him to the Gatling gun hidden in a mine at Gaptooth Breach, and later to the ammunition held by his contact Shaky in Thieves' Landing. He promises to fight at Fort Mercer but arrives only once the fight is over.",
            "Irish est un trafiquant d'armes irlandais et un gros buveur de Red Dead Redemption (2010), dont l'action se déroule en 1911. [[nigel-west-dickens|Nigel West Dickens]] envoie [[john-marston|John Marston]] le trouver pour obtenir la puissance de feu nécessaire contre Fort Mercer, repaire de la bande de [[bill-williamson|Bill Williamson]]. John le tire des mains de deux anciens amis qui le noient à Armadillo. Irish l'envoie d'abord vers une cabane vide, puis le conduit jusqu'à la mitrailleuse Gatling cachée dans une mine de Gaptooth Breach, et enfin jusqu'aux munitions que détient son contact Shaky à Thieves' Landing. Il promet de se battre à Fort Mercer, mais n'arrive qu'une fois le combat terminé."),
        two("He then takes John across the river to Mexico on his raft, under fire from gunmen on the Mexican bank, where he admits there is a bounty on his head, and leaves him on the other bank. A 1914 newspaper notice, which the Red Dead Wiki attributes to him, reports the accidental death of an Irishman of unknown name in Thieves' Landing. He is voiced by K. Harrison Sweeney.",
            "Il fait ensuite traverser le fleuve à John jusqu'au Mexique sur son radeau, sous le feu d'hommes armés postés sur la rive mexicaine, pays où sa tête est mise à prix, de son propre aveu, puis le laisse sur l'autre rive. Un avis paru dans un journal de 1914, que le Red Dead Wiki lui attribue, signale la mort accidentelle d'un Irlandais au nom inconnu à Thieves' Landing. Il a la voix de K. Harrison Sweeney."),
    ],
    "essentials": [
        two("In \"A Frenchman, a Welshman and an Irishman\", John saves him from Welsh and French in Armadillo; Irish then sends him to a cabin at Lake Don Julio where the gun is not.",
            "Dans \"A Frenchman, a Welshman and an Irishman\", John le sauve de Welsh et French à Armadillo ; Irish l'envoie ensuite vers une cabane du lac Don Julio où l'arme ne se trouve pas."),
        two("In \"Man is Born Unto Trouble\", he leads John to the Gatling gun in a mine at Gaptooth Breach and works the lift that brings it up.",
            "Dans \"Man is Born Unto Trouble\", il conduit John jusqu'à la mitrailleuse Gatling, dans une mine de Gaptooth Breach, et actionne le monte-charge qui la remonte."),
        two("In \"On Shaky's Ground\", John catches him robbing two nuns in Thieves' Landing; Irish then takes him to Shaky and drives the ammunition to MacFarlane's Ranch.",
            "Dans \"On Shaky's Ground\", John le surprend en train de dévaliser deux religieuses à Thieves' Landing ; Irish le mène ensuite à Shaky et conduit les munitions jusqu'au ranch MacFarlane."),
        two("He misses \"The Assault on Fort Mercer\" and turns up only at the end.",
            "Il rate \"The Assault on Fort Mercer\" et ne se montre qu'à la fin."),
        two("In \"We Shall Be Together in Paradise\", he takes John across the river to Mexico by raft; it is his last appearance.",
            "Dans \"We Shall Be Together in Paradise\", il fait passer le fleuve à John en radeau jusqu'au Mexique ; c'est sa dernière apparition."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["john-marston", "nigel-west-dickens", "seth-briars", "bonnie-macfarlane"],
}
