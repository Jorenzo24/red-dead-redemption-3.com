"""Rains Fall, reference fiche, PART D: base data, Development and performance, Reception
(22 Oct 2026, medium tier).

His page is still queued (_queue/48-rains-fall/), generated from the v2 entry in scripts/_wave7.py ("slug":
"rains-fall", order 48; no entry in _enrich.py). publishDate 2026-10-23 kept. The base below is rebuilt from that
entry, with corrections:
- v2 "Behind the scenes" said Graham Greene died "in Toronto". His management (manager Gerry Jordan, quoted by Radio
  Canada International, 2 Sep 2025) and CTV News Kitchener (Shelby Knox, 2 Sep 2025) place his death in Stratford,
  Ontario; the Toronto hospital comes from early reports (Deadline, relayed by the Fox stations and RDR2.org). Now
  "Stratford, Ontario", with the discrepancy stated once in Development.
- v2 said Rains Fall meets Arthur in "American Fathers I" with Evelyn Miller "outside the courthouse": kept (transcript).
- v2 said "The Wapiti believe Cornwall's claim on their reservation may be illegal": the transcript has Evelyn Miller
  saying the removal contravenes the treaty signed three years earlier and that prospectors filed reports with
  Cornwall and the State Government; reworded.
- v2 "Eagle Flies dies in his father's arms": the transcript stage note says his father takes him by the hand; now
  "dies in his father's tent on the reservation" (HOUSE_FACTS wording).
- v2 placed "Archeology for Beginners" in chapter 6 as "optional": kept (the mission page lists it after the choice
  offered by Charles; arthur_C: the player can accept or decline).
- v2 og_desc (mood line, "while his son prepares for war") replaced by a factual sentence; schema_desc expanded.
- chips: "Wapiti" and "RDR2" replaced by Alive in 1907 and Played by; facts grid rebuilt (Name, Aliases, Born, Status,
  People, Occupation, Residence, Family, Allies, Adversaries, Games, Played by).
- The Lakota caption point (v2) is kept and now sourced (fan transcript label + Red Dead Wiki), told in Development.
Eyebrow kept as on the queued page ("Character &middot; Wapiti"); reg_role matches characters_registry.py
("Wapiti chief &middot; RDR2"). Links: only fiches live on or before 2026-10-23 (never eagle-flies, published
2026-10-26, nor sister-calderon).

SOURCE REGISTER (fetched 22 Oct 2026, copies in scripts/v3/work/rains/fc/ where noted):
- Wikipedia "Graham Greene (actor)": born June 22, 1952, in Ohsweken, Six Nations of the Grand River, Ontario; Oneida;
  Oscar nomination for Kicking Bird in Dances with Wolves (1990); Thunderheart (1992), Maverick (1994), The Green Mile
  (1999), Wind River (2017), 1883 (2022), Reservation Dogs (2023); RDR2 "Chief Rains Fall, via voice and motion capture".
- Wikipedia "List of Red Dead Redemption 2 characters" (scripts/v3/work/catherine/fc/wp_list_rdr2.txt): Rains Fall
  (Graham Greene); Houser's view cited to Vulture.
- Vulture, Harold Goldberg, "How the West Was Digitized: The making of Rockstar Games' Red Dead Redemption 2",
  14 Oct 2018 (Wayback copy of 13 May 2019, fc/vulture_2018-10-14.html, fc/vulture.txt): "The most famous actor in
  RDR2 is Graham Greene, the Oneida performer..."; Dan Houser quote verified verbatim (including the article's typo
  "bought" for "brought", reproduced with [sic]).
- Radio Canada International, 2 Sep 2025: died Monday in Stratford, Ontario, aged 73, natural causes, per manager
  Gerry Jordan; Oneida, Six Nations. CTV News Kitchener, Shelby Knox, 2 Sep 2025 (headline: dies in Stratford, Ont.).
  CBC News obituary (search snippet: "after a long illness", Stratford). Deadline / Fox stations (2 Sep 2025): "a
  hospital in Toronto" (early report).
- Insider Gaming, Andrew Highton, 2 Sep 2025: "Graham only had one video game role", "Graham absolutely nails the role
  perfectly". RDR2.org, Ray Ampoloquio, 2 Sep 2025 (updated 7 Sep): "voice and motion capture", "a father figure and
  moral compass for Arthur Morgan".
- Polygon, Chris Plante, review, 25 Oct 2018: Rockstar told him the Wapiti are "not modelled on a specific tribe"
  (as quoted in the fact-checked charles_D.py; the Polygon page itself could not be re-fetched on 22 Oct 2026).
- Andrei Nae (University of Bucharest), "The Frontier as American National Identity Narrative in the Red Dead
  Redemption Games", American, British and Canadian Studies, 2025 (DOI 10.2478/abcsj-2025-0014; fc/abcsj.txt):
  quotes checked against the PDF text.
- Fan transcript (fc/gsw.txt): line labeled "Rains Fall In Lakota" in "The Fine Art of Conversation". Red Dead Wiki
  "Rains Fall" and "Wapiti Indians" trivia: in-game captions identify the language as Lakota.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content": "Rains Fall was originally known as Rains Come" (concept art;
  gallery files "Daren-bader-rainscome"); landmark "Cohutta" on the leaked map = the sacred site of "Archeology for
  Beginners"; unused official Mr. Pattison meant for the reservation; Wapiti warriors meant to act as lawmen in
  Ambarino (dispatch.meta).
Searched without result: an interview in which Greene discusses the role; an official Rockstar tribute after his death.

Fixes after fact-check (22 Oct 2026): Houser described as co-writer and co-founder (Vulture does not call him "the
writer"); the Lakota line placed on arrival at the meeting place (gsw l. 12533); "appears only in RDR2" left to Other
media (C); intro: the lobbying is Miller's, Charles leaves the gang after the battle (gsw l. 13296-13300); Family fact
reworded (the soldier is named only for the son in his own speech, gsw l. 13111); the 1907 meeting attributed.

Excluded: the RDR2.org claim that Houser praised Greene "in a Variety interview" (the praise is in Vulture; Variety not
found); search-snippet paraphrases of Houser; the Sitting Bull / Red Cloud models (wiki "appear to be based"); the
Salsabila and Prihatika JELE article (2026; abstract does not name Rains Fall, full text not read); Ashlee Bird's 2023
chapter (not read). DUPLICATE ownership: actor, Houser quote, Lakota, cut content and reviews live HERE; parts B and C
point to them.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Rains Fall is played by Graham Greene, an Oneida actor from the Six Nations of the Grand River reserve in Ontario, born on June 22, 1952. Wikipedia credits Greene with both the voice and the motion capture of the character. Greene was nominated for the Academy Award for Best Supporting Actor for Kicking Bird in Dances with Wolves (1990). His other roles include Thunderheart (1992), Maverick (1994), The Green Mile (1999), Wind River (2017), the series 1883 (2022) and Reservation Dogs (2023). Insider Gaming noted in September 2025 that Rains Fall was his only video game role.",
              "Rains Fall est interprété par Graham Greene, acteur oneida originaire de la réserve des Six Nations de la rivière Grand, en Ontario, né le 22 juin 1952. Wikipédia lui attribue à la fois la voix et la capture de mouvement du personnage. Greene avait été nommé à l'Oscar du meilleur second rôle pour Oiseau Bondissant (Kicking Bird) dans Danse avec les loups (1990). On l'a vu aussi dans Cœur de tonnerre (1992), Maverick (1994), La Ligne verte (1999), Wind River (2017), puis dans les séries 1883 (2022) et Reservation Dogs (2023). Insider Gaming relevait en septembre 2025 que Rains Fall était son seul rôle dans un jeu vidéo.")},
    {"p": two("In a feature on the making of the game published by Vulture on October 14, 2018, Harold Goldberg called Greene \"the most famous actor in RDR2\" and wrote that the role, a small one, was close to the heart of Dan Houser, co-writer of the game and co-founder of Rockstar Games. Houser said: \"He did such a brilliant job of bringing this chief character to life. The government is coming down on him hard. He's losing his rights as an independent king, and he's a gentle soul in that violent world. [Greene] bought [sic] this great depth to [the story].\" In the same article, Houser explained that Rockstar no longer cast well-known actors, preferring performers whose voices players do not recognize.",
              "Dans un long article sur la fabrication du jeu, publié par Vulture le 14 octobre 2018, Harold Goldberg présente Greene comme \"the most famous actor in RDR2\" (l'acteur le plus célèbre de RDR2) et écrit que ce rôle, modeste, tenait à cœur à Dan Houser, coscénariste du jeu et cofondateur de Rockstar Games. Houser déclare : \"He did such a brilliant job of bringing this chief character to life. The government is coming down on him hard. He's losing his rights as an independent king, and he's a gentle soul in that violent world. [Greene] bought [sic] this great depth to [the story].\" (il a fait un travail remarquable pour donner vie à ce personnage de chef ; le gouvernement s'acharne sur lui, il perd ses droits de roi indépendant, et c'est une âme douce dans ce monde violent ; Greene a apporté une vraie profondeur à l'histoire). Dans le même article, Houser explique que Rockstar ne recrute plus d'acteurs connus et leur préfère des comédiens dont le public ne reconnaît pas la voix.")},
    {"p": two("Graham Greene died on September 1, 2025, at the age of 73, after a long illness. According to his manager, Gerry Jordan, quoted by Radio Canada International on September 2, 2025, he died in Stratford, Ontario, which CTV News reported the same day; some early reports had placed his death in a Toronto hospital. Gaming sites including Insider Gaming and RDR2.org marked his death by recalling the role of Rains Fall.",
              "Graham Greene est mort le 1er septembre 2025, à 73 ans, des suites d'une longue maladie. Selon son représentant, Gerry Jordan, cité par Radio Canada International le 2 septembre 2025, il s'est éteint à Stratford, en Ontario, ce que CTV News rapporte le même jour ; les premières dépêches avaient évoqué un hôpital de Toronto. Plusieurs sites de jeu vidéo, dont Insider Gaming et RDR2.org, ont salué sa mémoire en rappelant son rôle de Rains Fall.")},
    {"h3": two("The Wapiti and the Lakota language", "Les Wapiti et la langue lakota")},
    {"p": two("The Wapiti are a fictional people. Chris Plante wrote in Polygon's review, on October 25, 2018, that Rockstar had told him the tribe is \"not modelled on a specific tribe\". In \"The Fine Art of Conversation\", when they reach the meeting place, Rains Fall tells his waiting men that Arthur and Charles are friends, and the subtitle labels his line as Lakota; the Red Dead Wiki notes that the game's captions identify the Wapiti's language as Lakota.",
              "Les Wapiti sont un peuple fictif. Chris Plante, dans le test de Polygon publié le 25 octobre 2018, rapporte que Rockstar lui a indiqué que la tribu n'est \"not modelled on a specific tribe\" (calquée sur aucune tribu précise). Dans \"The Fine Art of Conversation\", en arrivant au lieu de la rencontre, Rains Fall dit aux hommes qui l'attendent qu'Arthur et Charles sont des amis, et le sous-titre indique que sa réplique est en lakota ; le Red Dead Wiki relève que les sous-titres du jeu identifient la langue des Wapiti comme le lakota.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("According to the Red Dead Wiki's page on cut content, concept art shows that Rains Fall was first named Rains Come; the drawings are filed under the name of the artist Daren Bader. The sacred site he visits with Arthur in \"Archeology for Beginners\" was labeled Cohutta on a leaked map, a name the final game does not use. The game files also contain an unused official, Mr. Pattison, meant to appear on the Wapiti reservation, and a cut system in which Wapiti warriors would have acted as lawmen in the Ambarino region.",
              "D'après la page du Red Dead Wiki consacrée au contenu coupé, des dessins préparatoires montrent que Rains Fall s'appelait d'abord Rains Come ; ces dessins sont classés sous le nom de l'illustrateur Daren Bader. Le site sacré qu'il visite avec Arthur dans \"Archeology for Beginners\" portait le nom de Cohutta sur une carte ayant fuité, nom que le jeu final n'utilise pas. Les fichiers du jeu contiennent aussi un fonctionnaire inutilisé, M. Pattison, prévu pour la réserve wapiti, et un système abandonné dans lequel des guerriers wapiti auraient fait office de forces de l'ordre dans la région d'Ambarino.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Critics and scholars", "Critiques et chercheurs")},
    {"p": two("In Polygon's review, Chris Plante wrote that the game's mixing of real peoples, places and groups produced story beats ranging \"from benign to confused to insensitive and harmful\". After Greene's death, Andrew Highton of Insider Gaming wrote on September 2, 2025 that \"Graham absolutely nails the role perfectly\", and Ray Ampoloquio of RDR2.org described Rains Fall as \"a father figure and moral compass for Arthur Morgan\".",
              "Dans le test de Polygon, Chris Plante estime que ce mélange de peuples, de lieux et de groupes réels donne des passages qui vont \"from benign to confused to insensitive and harmful\" (de l'anodin au confus, voire à l'offensant et au blessant). Après la mort de Greene, Andrew Highton écrit dans Insider Gaming, le 2 septembre 2025, que \"Graham absolutely nails the role perfectly\" (Graham est parfait dans le rôle), et Ray Ampoloquio, sur RDR2.org, voit en Rains Fall \"a father figure and moral compass for Arthur Morgan\" (une figure paternelle et une boussole morale pour Arthur Morgan).")},
    {"p": two("In an article published in 2025 in the journal American, British and Canadian Studies, Andrei Nae of the University of Bucharest counts Rains Fall among the three Native American characters who matter to the game's story and play, with Eagle Flies and Charles Smith. He contrasts the two Wapiti: \"While the elder Rains Fall is in favour of diplomatic solutions (in spite of the untrustworthiness of the federal government), the young Eagle Flies, under the negative influence of Dutch van der Linde, advocates for violent resistance.\" He argues that the game, while marking \"a significant shift\" in its portrayal of Native Americans, casts them in \"the stereotype of the noble savage who cannot help themselves and are in need of a white saviour\".",
              "Dans un article paru en 2025 dans la revue American, British and Canadian Studies, Andrei Nae, de l'université de Bucarest, range Rains Fall parmi les trois personnages amérindiens qui comptent dans l'histoire et le jeu, avec Eagle Flies et Charles Smith. Il oppose les deux Wapiti : \"While the elder Rains Fall is in favour of diplomatic solutions (in spite of the untrustworthiness of the federal government), the young Eagle Flies, under the negative influence of Dutch van der Linde, advocates for violent resistance.\" (le vieux Rains Fall privilégie la diplomatie, malgré le peu de confiance que mérite le gouvernement fédéral, tandis que le jeune Eagle Flies, sous la mauvaise influence de Dutch van der Linde, prône la résistance armée). Selon lui, le jeu marque \"a significant shift\" (une évolution notable) dans sa représentation des Amérindiens, mais les enferme dans \"the stereotype of the noble savage who cannot help themselves and are in need of a white saviour\" (le stéréotype du bon sauvage incapable de s'en sortir seul et qui a besoin d'un sauveur blanc).")},
]


BASE = {
    "slug": "rains-fall", "name": "Rains Fall",
    "publishDate": "2026-10-23", "updated": "2026-10-22", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Wapiti chief &middot; RDR2", "reg_role_fr": "Chef wapiti &middot; RDR2",
    "gender": "Male", "death": None, "nationality": None,
    "portrait_alt": two("Rains Fall, chief of the Wapiti, in Red Dead Redemption 2",
                        "Rains Fall, chef des Wapiti, dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Wapiti", "Personnage &middot; Wapiti"),
    "meta_desc": two("Rains Fall, chief of the Wapiti in RDR2: the fight for the reservation, his son Eagle Flies, his rides with Arthur, his exile in Canada in 1907, Graham Greene.",
                     "Rains Fall, chef des Wapiti dans RDR2 : la lutte pour la réserve, son fils Eagle Flies, ses chevauchées avec Arthur, son exil au Canada en 1907, Graham Greene."),
    "og_desc": two("The complete reference on Rains Fall: life, quotes, relationships, development and reception.",
                   "La référence complète sur Rains Fall : vie, citations, relations, conception et accueil."),
    "schema_desc": two("Chief of the Wapiti, a fictional Native American people, who seeks a peaceful settlement with the Army over his tribe's reservation in 1899, loses his son Eagle Flies, and lives in Canada with his people by 1907, in Red Dead Redemption 2.",
                       "Chef des Wapiti, peuple amérindien fictif, qui cherche en 1899 un règlement pacifique avec l'armée au sujet de la réserve de sa tribu, perd son fils Eagle Flies, et vit au Canada avec les siens en 1907, dans Red Dead Redemption 2."),
    "chips": [two("Chief of the Wapiti", "Chef des Wapiti"), two("Alive in <strong>1907</strong>", "En vie en <strong>1907</strong>"),
              two("Played by <strong>Graham Greene</strong>", "Interprété par <strong>Graham Greene</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Rains Fall (his English name)", "Rains Fall (son nom en anglais)")},
        {"label": two("Aliases", "Surnoms"), "value": two("Chief Rains (Colonel Favours)", "Chief Rains (le colonel Favours)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1907", "En vie en 1907")},
        {"label": two("People", "Peuple"), "value": two("Wapiti", "Wapiti")},
        {"label": two("Occupation", "Activité"), "value": two("Chief of the Wapiti", "Chef des Wapiti")},
        {"label": two("Residence", "Résidence"), "value": two("Wapiti Indian Reservation, Ambarino (1899); Canada (1907)", "Réserve indienne wapiti, Ambarino (1899) ; Canada (1907)")},
        {"label": two("Family", "Famille"), "value": two("Eagle Flies (son, died 1899); his wife and an elder son (killed; a drunken soldier killed the son, by his account)", "Eagle Flies (fils, mort en 1899) ; sa femme et un fils aîné (tués ; le fils par un soldat ivre, selon ses dires)")},
        {"label": two("Allies", "Alliés"), "value": two("[[arthur-morgan|Arthur Morgan]], [[charles-smith|Charles Smith]], Captain Lyndon Monroe, Evelyn Miller", "[[arthur-morgan|Arthur Morgan]], [[charles-smith|Charles Smith]], le capitaine Lyndon Monroe, Evelyn Miller")},
        {"label": two("Adversaries", "Adversaires"), "value": two("Colonel Henry Favours and the Army at Fort Wallace", "Le colonel Henry Favours et l'armée de Fort Wallace")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Graham Greene", "Graham Greene")},
    ],
    "intro": [
        two("Rains Fall is the chief of the Wapiti, a fictional Native American people, in Red Dead Redemption 2 (2018), set in 1899. He says he has signed three treaties with the United States government and that each one was broken. When oil is claimed under the tribe's reservation, he looks for a peaceful way to keep the land: he seeks help from officials in Saint Denis with the writer Evelyn Miller, hires [[arthur-morgan|Arthur Morgan]] to obtain proof, and secures a meeting with Colonel Henry Favours of Fort Wallace. His son Eagle Flies chooses war instead, with the encouragement of [[dutch-van-der-linde|Dutch van der Linde]], and dies of a wound received at the oil fields. By 1907 the Wapiti have fled to Canada.",
            "Rains Fall est le chef des Wapiti, un peuple amérindien fictif, dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Il dit avoir signé trois traités avec le gouvernement des États-Unis, tous rompus. Quand on prétend avoir trouvé du pétrole sous la réserve de la tribu, il cherche une issue pacifique pour garder ces terres : il sollicite les élus de Saint-Denis aux côtés de l'écrivain Evelyn Miller, engage [[arthur-morgan|Arthur Morgan]] pour obtenir des preuves et décroche une rencontre avec le colonel Henry Favours, de Fort Wallace. Son fils Eagle Flies choisit au contraire la guerre, encouragé par [[dutch-van-der-linde|Dutch van der Linde]], et meurt d'une blessure reçue aux champs de pétrole. En 1907, les Wapiti se sont réfugiés au Canada."),
        two("[[charles-smith|Charles Smith]] helps his people and leaves the gang to stay with them after the battle. Rains Fall is played by Graham Greene.",
            "[[charles-smith|Charles Smith]] aide les siens et quitte le gang après la bataille pour rester auprès d'eux. Rains Fall est interprété par Graham Greene."),
    ],
    "essentials": [
        two("In \"American Fathers I\", outside the Saint Denis courthouse, he offers to pay [[arthur-morgan|Arthur]] to get hold of documents about the oil under the reservation.",
            "Dans \"American Fathers I\", devant le palais de justice de Saint-Denis, il propose de payer [[arthur-morgan|Arthur]] pour obtenir des documents sur le pétrole de la réserve."),
        two("In \"Archeology for Beginners\", he picks herbs for Arthur's cough and finds his sacred site burned by soldiers; Arthur brings back the stolen Chanupa.",
            "Dans \"Archeology for Beginners\", il cueille des plantes contre la toux d'Arthur et découvre son site sacré incendié par des soldats ; Arthur lui rapporte le Chanupa volé."),
        two("He asks Arthur and [[charles-smith|Charles]] to attend his peace talks with Colonel Favours in \"The Fine Art of Conversation\"; the talks fail.",
            "Il demande à Arthur et à [[charles-smith|Charles]] d'assister à ses pourparlers avec le colonel Favours dans \"The Fine Art of Conversation\" ; ils échouent."),
        two("In \"My Last Boy\", he begs his son Eagle Flies not to attack the oil fields; Eagle Flies dies in his father's tent on the reservation after the battle.",
            "Dans \"My Last Boy\", il supplie son fils Eagle Flies de ne pas attaquer les champs de pétrole ; Eagle Flies meurt sous la tente de son père, sur la réserve, après la bataille."),
        two("In 1907, according to the Red Dead Wiki, [[john-marston|John Marston]] can meet him at the Annesburg train station; he says his people now live in Canada.",
            "En 1907, d'après le Red Dead Wiki, [[john-marston|John Marston]] peut le croiser à la gare d'Annesburg ; il lui dit que son peuple vit désormais au Canada."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["charles-smith", "arthur-morgan", "leviticus-cornwall", "dutch-van-der-linde"],
}
