"""Harold MacDougal, reference fiche, PART D: base data, Development and performance, Reception (22 Oct 2026, medium tier).

His live page (characters/harold-macdougal/) was generated from the v2 entry in scripts/_wave6.py (order 36,
"slug": "harold-macdougal"; no entry in _enrich.py). publishDate 2026-09-27 kept (git 59bddc5, drip publish of
harold-macdougal, 27 Sep 2026). Eyebrow and portrait_alt kept as on the live page ("Character &middot; West
Elizabeth"); reg_role matches characters_registry.py ("Anthropologist &middot; RDR1" / "Anthropologue &middot; RDR1").
Corrections to the v2 base:
- v2 "Edgar Ross sends John Marston to him because his research has brought him closer to Dutch van der Linde's new gang
  than the Bureau has managed": no transcript says so. Ross and Fordham bring the wounded informant Nastas to him so he
  can find out what Nastas knows, and Ross tells John to help him in "his study of the native problem" ("Bear One
  Another's Burdens" transcript). Rewritten.
- v2 "He employs Nastas as a guide" (intro, relationship "His guide and informant, and the man who does the fieldwork for
  him"): Nastas is the Bureau's informant (Fordham: "That informant better not have been lying to us"; "This is the
  informant, sir"); Ross has him taken to MacDougal. No line makes MacDougal his employer. Rewritten.
- v2 "his study of the region's Native population is what makes the hunt through Tall Trees possible": Nastas, not the
  study, leads John to Cochinay. Rewritten.
- v2 "heavy user of cocaine and alcohol, and his condition worsens over the course of the story" and "several of the
  missions he sends John on go wrong because of it": cocaine is shown; alcohol only in the 1914 article ("drunken
  brawl"); the worsening and the causal link are readings. Dropped; cocaine kept as a fact.
- v2 "His theories are the racial pseudo-science of the period": our own judgement; replaced by what he says and writes.
- v2 "He funds and directs the work himself, with Nastas doing the fieldwork that MacDougal will not do": the inheritance
  is his own claim (part A); the rest is a reading. Dropped.
- v2 "The three are captured at one point and held at gunpoint before they get clear" and the gallery caption "taken
  during the search through Tall Trees": the hold-up happens at Bearclaw Camp, not in Tall Trees, and ends with Nastas
  shot. Reworded in the essentials; the caption belongs to the gallery pass (flagged to the lead).
- v2 facts grid lacked status, residence, family, weapons, actor and the 1914 expulsion; v2 "Behind the scenes" had no
  actor: Joe Ochman added (Wikipedia credits). v2 "Leaving the West ... John sees him off at the train": kept.
- v2 og_desc ("whose research, and whose guide, put John Marston on the trail") rewritten on the same grounds.

SOURCE REGISTER (read 22 Oct 2026; notes in scripts/v3/work/macdougal/fc/web_notes_BD.txt):
- Wikipedia "Joe Ochman" (page last edited 14 Oct 2026): American actor most active in voice-over; credits for Red Dead
  Redemption ("Professor Harold MacDougal, Government Clerk") and Undead Nightmare (Professor Harold MacDougal,
  uncredited); other roles listed (Jiminy Cricket, Will A. Zeppeli, Zeno Zoldyck, William Price, Andre Bourgeois).
- Wikipedia "Red Dead Redemption: Undead Nightmare" (landon/fc/wp_un.txt): "Professor Harold MacDougal (Joe Ochman)".
- Wikipedia "Red Dead Redemption" (read 22 Oct 2026): does not mention MacDougal or Ochman.
- K. Harrison Sweeney, written interview on a Red Dead Wiki user blog, 10 Nov 2011 (irish/fc/sweeney_interview_
  reddeadwiki_blog.txt): Sweeney says he has been talking with Anthony DeLongis, Joe Ochman and Frank Noon about possibly
  being in "From the Trailer to the Grave".
- WhatCulture, Ewan Paterson, "Red Dead Redemption 2: 18 Easter Eggs And References You Totally Missed", 10 Nov 2018,
  entry 17 "Harold MacDougal" (WebFetch).
- Red Dead Wiki EN infobox (voice, mounts, weapon, location) and FR infobox (acteur Joe Ochman, statut vivant 1914).
- Transcripts of the four RDR1 missions and the mission page of "Curious Tales from Blackwater" for intro and essentials;
  Blackwater Ledger No. 59 and Blackwater Ledger & Sentinel No. 213 (macdougal/fc/) for status and residence.
- Liars and Cheats pack (released 21 Sep 2010, _m/Liars_and_Cheats.txt; nigel/fc/Liars_and_Cheats.txt lists MacDougal):
  facts grid only; the detail belongs to part C (Other media).

Excluded: the "and motion-captured" in a search-engine summary of Wikipedia (no footnote, not in the Wikipedia text
read): no motion capture claim; Ochman's birth date (Red Dead Wiki only, August 24, 1954: not needed and unsourced
elsewhere); IMDb credits (not read); any interview by Ochman about the role (none found); cut content (none found;
the wiki's scrapped-bounty note concerns Nashoba and Enepay, not MacDougal, and is tagged {{fact}}); a Rockstar page for
"A highly-strung anthropology professor" (not found; part B quotes it through the wiki); academic studies of the
depiction of Native Americans in Red Dead Redemption (they discuss Nastas, not MacDougal, in what was found); a GameFAQs
thread on MacDougal and L.A. Noire (403, unread; fan forum anyway).
Reception is thin: one 2018 article. Development is limited to the credit and one mention by Sweeney.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Wikipedia credits Joe Ochman as Professor Harold MacDougal in Red Dead Redemption (2010), where the same credit line also lists him as a government clerk. Its article on Undead Nightmare, the expansion released later in 2010, names Ochman as MacDougal again; his own Wikipedia page marks that second performance as uncredited. Wikipedia describes Ochman as an American actor who works mostly in voice-over for animation, film and video games. His other roles listed there include Jiminy Cricket in Kingdom Hearts III, Will A. Zeppeli in JoJo's Bizarre Adventure, Zeno Zoldyck in Hunter x Hunter and William Price in Life Is Strange (2015).",
              "Wikipédia attribue à Joe Ochman le rôle du professeur Harold MacDougal dans Red Dead Redemption (2010), la même ligne de crédit le citant aussi pour un employé du gouvernement. Son article sur Undead Nightmare, l'extension sortie plus tard la même année, nomme de nouveau Ochman pour MacDougal ; sa propre page Wikipédia précise que cette seconde prestation n'est pas créditée. Wikipédia présente Ochman comme un acteur américain qui travaille surtout le doublage, pour l'animation, le cinéma et le jeu vidéo. Parmi ses autres rôles figurent Jiminy Cricket dans Kingdom Hearts III, Will A. Zeppeli dans JoJo's Bizarre Adventure, Zeno Zoldyck dans Hunter x Hunter et William Price dans Life Is Strange (2015).")},
    {"h3": two("After the game", "Après le jeu")},
    {"p": two("In a written interview published on a Red Dead Wiki user blog on November 10, 2011, K. Harrison Sweeney, the voice of Irish, said he had been talking with Anthony De Longis, Joe Ochman and Frank Noon about possibly appearing in From the Trailer to the Grave, a comedy he had written and planned to shoot with actors from Red Dead Redemption.",
              "Dans un entretien écrit publié sur un blog d'utilisateur du Red Dead Wiki le 10 novembre 2011, K. Harrison Sweeney, la voix d'Irish, disait avoir discuté avec Anthony De Longis, Joe Ochman et Frank Noon d'une possible participation à From the Trailer to the Grave, une comédie qu'il avait écrite et comptait tourner avec des acteurs de Red Dead Redemption.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Coverage", "Dans la presse")},
    {"p": two("On November 10, 2018, WhatCulture published a list by Ewan Paterson of eighteen easter eggs and references in Red Dead Redemption 2. Entry 17 is Harold MacDougal. Paterson calls him \"an eccentric (read: racist drug addict)\" from the closing stages of the first game, a Yale professor who studies the Native American population \"only in the interest of furthering his own bigoted perspective\". He notes that MacDougal does not appear in person in the sequel but is mentioned in dialogue and in the game's printed material.",
              "Le 10 novembre 2018, WhatCulture publie une liste d'Ewan Paterson consacrée à dix-huit clins d'œil et références de Red Dead Redemption 2. L'entrée 17 est Harold MacDougal. Paterson le décrit comme \"an eccentric (read: racist drug addict)\" (un excentrique, comprendre : un toxicomane raciste) des derniers moments du premier jeu, un professeur de Yale qui étudie la population amérindienne \"only in the interest of furthering his own bigoted perspective\" (dans le seul but de conforter ses préjugés). Il relève que MacDougal n'apparaît pas en personne dans la suite, mais qu'il y est cité dans des dialogues et des imprimés du jeu.")},
]


BASE = {
    "slug": "harold-macdougal", "name": "Harold MacDougal",
    "publishDate": "2026-09-27", "updated": "2026-10-22", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Anthropologist &middot; RDR1", "reg_role_fr": "Anthropologue &middot; RDR1",
    "gender": "Male", "birth": None, "death": None, "nationality": "American",
    "portrait_alt": two("Professor Harold MacDougal in the streets of Blackwater in Red Dead Redemption",
                        "Le professeur Harold MacDougal dans les rues de Blackwater dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; West Elizabeth", "Personnage &middot; West Elizabeth"),
    "meta_desc": two("Harold MacDougal, the Yale anthropologist of Red Dead Redemption: Nastas, the hunt for Dutch van der Linde, Bearclaw Camp, the escape from Blackwater, his 1914 expulsion, Joe Ochman.",
                     "Harold MacDougal, l'anthropologue de Yale de Red Dead Redemption : Nastas, la traque de Dutch van der Linde, Bearclaw Camp, la fuite de Blackwater, son renvoi en 1914, Joe Ochman."),
    "og_desc": two("The complete reference on Harold MacDougal: life, missions, quotes, development and reception.",
                   "La référence complète sur Harold MacDougal : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Yale anthropology professor who studies the Native Americans of West Elizabeth from a Blackwater hotel room in 1911, helps John Marston and Nastas find Dutch van der Linde, then flees back to Yale, in Red Dead Redemption.",
                       "Professeur d'anthropologie de Yale qui étudie les Amérindiens de West Elizabeth depuis une chambre d'hôtel de Blackwater en 1911, aide John Marston et Nastas à retrouver Dutch van der Linde, puis regagne Yale en catastrophe, dans Red Dead Redemption."),
    "chips": [two("Anthropologist", "Anthropologue"), two("Yale University", "Université de Yale"),
              two("Blackwater, <strong>1911</strong>", "Blackwater, <strong>1911</strong>"),
              two("Voiced by <strong>Joe Ochman</strong>", "Voix : <strong>Joe Ochman</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Harold MacDougal", "Harold MacDougal")},
        {"label": two("Also known as", "Autres noms"), "value": two("Professor, Professor MacDougal; Dr. MacDougal in the Game of the Year guide (Red Dead Wiki)", "Professor, Professor MacDougal ; Dr. MacDougal dans le guide Game of the Year (Red Dead Wiki)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game; 42 years old according to the Game of the Year guide, cited by the Red Dead Wiki, which places his birth around 1869", "Non précisée dans le jeu ; 42 ans selon le guide Game of the Year, cité par le Red Dead Wiki, qui en déduit une naissance vers 1869")},
        {"label": two("Status", "Statut"), "value": two("Alive in 1914, when the Blackwater Ledger & Sentinel reports his expulsion from Yale; killed by an undead Nastas in Undead Nightmare (non-canon)", "En vie en 1914, quand le Blackwater Ledger & Sentinel annonce son renvoi de Yale ; tué par Nastas, devenu mort-vivant, dans Undead Nightmare (hors canon)")},
        {"label": two("Nationality", "Nationalité"), "value": two("American (from Connecticut)", "Américaine (originaire du Connecticut)")},
        {"label": two("Residence", "Résidence"), "value": two("A room at the Blackwater Hotel (1911); New Haven, Connecticut", "Une chambre de l'hôtel de Blackwater (1911) ; New Haven, Connecticut")},
        {"label": two("Occupation", "Activité"), "value": two("Professor of anthropology at Yale, on a sabbatical in 1911; expelled in 1914", "Professeur d'anthropologie à Yale, en congé sabbatique en 1911 ; renvoyé en 1914")},
        {"label": two("Family", "Famille"), "value": two("A father, according to the Red Dead Wiki", "Un père, selon le Red Dead Wiki")},
        {"label": two("Associates", "Fréquentations"), "value": two("[[nastas|Nastas]], [[john-marston|John Marston]], [[edgar-ross|Edgar Ross]], [[archer-fordham|Archer Fordham]]", "[[nastas|Nastas]], [[john-marston|John Marston]], [[edgar-ross|Edgar Ross]], [[archer-fordham|Archer Fordham]]")},
        {"label": two("Weapon", "Arme"), "value": two("Cattleman Revolver (Red Dead Wiki)", "Cattleman Revolver (Red Dead Wiki)")},
        {"label": two("Horses", "Chevaux"), "value": two("Ardennais, Cleveland Bay (Red Dead Wiki)", "Ardennais, Cleveland Bay (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption; Undead Nightmare; mentioned in Red Dead Redemption 2; multiplayer model (Liars and Cheats pack, 2010)", "Red Dead Redemption ; Undead Nightmare ; cité dans Red Dead Redemption 2 ; modèle multijoueur (pack Liars and Cheats, 2010)")},
        {"label": two("Voiced by", "Voix"), "value": two("Joe Ochman", "Joe Ochman")},
    ],
    "intro": [
        two("Harold MacDougal is a Yale anthropology professor in Red Dead Redemption (2010), set in 1911. On a sabbatical he admits was forced on him, he studies the Native Americans of West Elizabeth from his room at the Blackwater Hotel. [[edgar-ross|Edgar Ross]] and [[archer-fordham|Archer Fordham]] bring him the Bureau's wounded informant, [[nastas|Nastas]], and Ross tells [[john-marston|John Marston]] to help him. MacDougal rides with John and Nastas towards the hideout of [[dutch-van-der-linde|Dutch van der Linde]] at Cochinay, then to a meeting with Dutch's men at Bearclaw Camp, where Nastas is shot dead.",
            "Harold MacDougal est un professeur d'anthropologie de Yale dans Red Dead Redemption (2010), dont l'action se déroule en 1911. En congé sabbatique, qu'il reconnaît lui avoir été imposé, il étudie les Amérindiens de West Elizabeth depuis sa chambre de l'hôtel de Blackwater. [[edgar-ross|Edgar Ross]] et [[archer-fordham|Archer Fordham]] lui confient l'informateur blessé du Bureau, [[nastas|Nastas]], et Ross demande à [[john-marston|John Marston]] de l'aider. MacDougal chevauche avec John et Nastas vers le repaire de [[dutch-van-der-linde|Dutch van der Linde]], à Cochinay, puis jusqu'à une rencontre avec des hommes de Dutch à Bearclaw Camp, où Nastas est abattu."),
        two("When Dutch's gang attacks his hotel, John gets him across the rooftops and escorts him to the train at Manzanita Post, and he leaves for Yale. In 1914, a newspaper reports that Yale has expelled him after he beat a colleague with a croquet mallet. In Undead Nightmare, which is not canon, he is killed by an undead Nastas. He is voiced by Joe Ochman.",
            "Quand la bande de Dutch attaque son hôtel, John lui fait traverser les toits et l'escorte jusqu'au train de Manzanita Post, et il repart pour Yale. En 1914, un journal annonce que Yale l'a renvoyé après qu'il a frappé un collègue avec un maillet de croquet. Dans Undead Nightmare, qui ne relève pas du canon, il est tué par Nastas devenu mort-vivant. Il a la voix de Joe Ochman."),
    ],
    "essentials": [
        two("In \"Bear One Another's Burdens\", Ross, Fordham and John bring the wounded Nastas to his room in Blackwater, and Fordham asks him to find out what Nastas knows about Dutch.",
            "Dans \"Bear One Another's Burdens\", Ross, Fordham et John amènent Nastas blessé dans sa chambre de Blackwater, et Fordham le charge de découvrir ce que Nastas sait de Dutch."),
        two("In \"At Home with Dutch\", he rides with John and Nastas to the cliffs below Cochinay, then turns back to Blackwater.",
            "Dans \"At Home with Dutch\", il chevauche avec John et Nastas jusqu'aux falaises sous Cochinay, puis rebrousse chemin vers Blackwater."),
        two("In \"For Purely Scientific Purposes\", the meeting with Dutch's men at Bearclaw Camp turns into an ambush in which Nastas is killed; John brings MacDougal back to Blackwater.",
            "Dans \"For Purely Scientific Purposes\", la rencontre avec des hommes de Dutch à Bearclaw Camp tourne au guet-apens et Nastas y est tué ; John ramène MacDougal à Blackwater."),
        two("In \"The Prodigal Son Returns (To Yale)\", Dutch's gang besieges his hotel; John frees him on the roof and puts him on the train at Manzanita Post.",
            "Dans \"The Prodigal Son Returns (To Yale)\", la bande de Dutch assiège son hôtel ; John le libère sur le toit et le met dans le train à Manzanita Post."),
        two("In 1914, the Blackwater Ledger & Sentinel reports his expulsion from Yale.",
            "En 1914, le Blackwater Ledger & Sentinel annonce son renvoi de Yale."),
        two("In \"Curious Tales from Blackwater\" (Undead Nightmare), he is killed by an undead Nastas.",
            "Dans \"Curious Tales from Blackwater\" (Undead Nightmare), il est tué par Nastas devenu mort-vivant."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["nastas", "john-marston", "edgar-ross", "dutch-van-der-linde"],
}
