"""Nastas, reference fiche, PART D: base data, Development and performance, Reception (22 Oct 2026, medium tier).

His live page (characters/nastas/) was generated from the v2 entry in scripts/_wave6.py (order 35, "slug": "nastas";
no entry in _enrich.py). publishDate 2026-09-24 kept (live byline "Updated September 24, 2026"). Eyebrow kept as on the
live page ("Character &middot; West Elizabeth"); reg_role matches characters_registry.py ("Guide &middot; RDR1" in both
languages). portrait_alt kept (the live portrait shows Nastas, hands raised, beside John Marston at gunpoint).
Corrections to the v2 base (CLAUDE.md: the live fiche had claims without source):
- v2 "one of the two men Edgar Ross assigns to help John Marston locate Dutch": false. Nastas is the Bureau's informant
  (Fordham: "our informant"); Ross leaves him, wounded, with MacDougal and sends John to help the professor
  ("Bear One Another's Burdens" transcript). Rewritten.
- v2 "works as guide and informant for Professor Harold MacDougal ... MacDougal treats him as a research subject as
  much as an employee": no transcript says MacDougal employs him; he is the agents' informant who then works with
  MacDougal in two missions. Rewritten.
- v2 "He knows Tall Trees and the men Dutch has recruited there, which makes him the only practical way into the
  forest": reduced to what he says (friends of his are with Dutch; he knows an unguarded way to Cochinay).
- v2 "Dutch has gathered a new gang in Tall Trees, made up largely of displaced Native men, and raids banks and coaches
  from a hideout at Cochinay. Nastas ... identifies Dutch's people and narrows down the location of the camp": not in
  his missions; dropped.
- v2 "Nastas is killed during the search, before John reaches Cochinay": imprecise (John has already seen Cochinay
  through the binoculars). Replaced by the mission, place and killer: Enepay, Bearclaw Camp, "For Purely Scientific
  Purposes" (transcript + mission page). "His death removes the one person able to move freely between the two sides"
  (interpretation) dropped.
- v2 nationality "American": not given by the game (he grew up on a reservation; the EN wiki says Native American, the
  FR wiki "Américain"). Set to None; origin given in the facts grid.
- v2 "Behind the scenes" (one sentence, no actor): replaced by Development and performance (Benjamin Byron Davis) and
  Reception. v2 chips, facts, intro, meta and og descriptions rewritten on the transcripts.

SOURCE REGISTER (read 22 Oct 2026; notes in scripts/v3/work/nastas/fc/web_notes_BD.txt):
- Wikipedia "Benjamin Byron Davis" (raw wikitext): videography row "Red Dead Redemption (2010): Dutch van der Linde /
  Nastas"; lead sentence on performance capture for several Rockstar characters (general, not tied to Nastas).
- Game Rant, Sean Mackey, "Red Dead Redemption 2 Voice Actor Also Played Character in Red Dead 1", 14 Jun 2020
  (WebFetch): the double role, pointed out by a Reddit user; no statement from Davis.
- Red Dead Wiki "Nastas" (EN infobox voice = Benjamin Byron Davis; trivia on the shared voice) and FR "Nastas"
  (acteur = Benjamin Byron Davis).
- Red Dead Wiki "Red Dead Redemption Cut Content" (_m/): beta model "NativeAmericanContact".
- Rockstar character card (Red Dead Wiki file "Nastas22.jpg", uploaded 23 Jun 2010): quoted in part B only.
- Game Informer, Jeff Cork, "Red Dead Redemption Crammed With Colorful Characters", 26 Feb 2010 (WebFetch; the
  "loudmouth deputy" contrast as checked by fact-check report 2, 22 Oct 2026).
- NYMGamer, Phill Alexander, "Red Dead Redemption and the Myth of the Noble Savage", 17 Apr 2014 (WebFetch).
- Wikipedia "Red Dead Redemption" (raw wikitext, Themes section) for M. Melissa Elston, "Allegorical Confrontation Meets
  Gaming System: Rhetoric and Trauma within Red Dead Redemption / Undead Nightmare", in C. J. Miller and A. Bowdoin
  Van Riper (eds.), Undead in the West II: They Just Keep Coming, Scarecrow Press, 2013, pp. 142-158 (Nastas p. 149).
  The chapter itself was NOT read: reported through Wikipedia's summary, attributed.
- Myths and Mavericks release (13 Sep 2011, free): consistent with javier_C / uncle_C (Engadget, 27 Jul 2011).
- Undead Nightmare release (October 2010): consistent with part A.
- Transcripts of the three RDR1 missions (_m/*_dialogues.txt) and Blackwater Ledger No. 59 (ireddead transcription)
  for the intro and essentials.

Excluded: any motion-capture claim for Nastas (Wikipedia's sentence is general; no source ties Davis's capture to
Nastas); IMDb credit (page not read, only a search-result title); Twinfinite's Feb 2019 Davis interview (403, not read);
Giant Bomb's page (403); a Chaske Spencer credit mentioned by a search engine summary (no source found, contradicts
every credit read); NYMGamer's "aids with a large portion of the game" (inaccurate: three missions) and its account of
the meeting (not reproduced); the UND "Native Dancer" blog (18 Oct 2022; does not name Nastas); Elston's wording beyond
Wikipedia's summary (chapter not read); the Navajo meaning of the name (part B, Names).
DUPLICATE ownership: the actor and the shared voice with Dutch live HERE (facts grid and chips may name him; part B's
Dutch entry points here); part C Trivia must not repeat the shared voice. The Rockstar card is quoted in B only.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Wikipedia credits Benjamin Byron Davis with two roles in Red Dead Redemption (2010): Dutch van der Linde and Nastas. The English and French Red Dead Wikis also give him as the voice of Nastas. The character he voices is the informant who helps the Bureau hunt down Dutch, the gang leader he also plays. On June 14, 2020, Game Rant (Sean Mackey) reported the double role, noticed by a Reddit user, and called it one of the game's Easter eggs. The article quotes no statement from Davis on Nastas, and none was found. Davis returned as Dutch in Red Dead Redemption 2 (2018).",
              "Wikipédia attribue deux rôles à Benjamin Byron Davis dans Red Dead Redemption (2010) : Dutch van der Linde et Nastas. Les Red Dead Wikis anglophone et francophone lui attribuent aussi la voix de Nastas. Le personnage qu'il double est l'informateur qui aide le Bureau à traquer Dutch, le chef de bande qu'il interprète par ailleurs. Le 14 juin 2020, Game Rant (Sean Mackey) relève ce double rôle, repéré par un utilisateur de Reddit, et le range parmi les clins d'œil du jeu. L'article ne cite aucune déclaration de Davis sur Nastas, et nous n'en avons trouvé aucune. Davis a repris le rôle de Dutch dans Red Dead Redemption 2 (2018).")},
    {"h3": two("Promotion and cut content", "Promotion et contenu coupé")},
    {"p": two("Rockstar presented Nastas with a one-line character card (see Personality); the Red Dead Wiki's copy of it was uploaded on June 23, 2010. According to the wiki's page on the game's cut content, the files contain an earlier version of Nastas under the name \"NativeAmericanContact\", with the same belt and shirt; its high-resolution textures were deleted.",
              "Rockstar présente Nastas au moyen d'une carte de personnage d'une seule ligne (voir Personnalité) ; la copie qu'en conserve le Red Dead Wiki a été mise en ligne le 23 juin 2010. D'après la page du wiki consacrée au contenu coupé du jeu, les fichiers renferment une version antérieure de Nastas, nommée \"NativeAmericanContact\", avec la même ceinture et la même chemise ; ses textures en haute résolution ont été supprimées.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Before release", "Avant la sortie")},
    {"p": two("On February 26, 2010, Game Informer (Jeff Cork) wrote that Rockstar San Diego had filled the game with \"nearly every stock Western character\". He contrasted Nastas with the game's \"loudmouth deputy\", who in his view \"isn't necessarily a different take on what we've seen before\", and wrote: \"Nastas could prove to be an interesting character if he's truly conflicted about his place in the world.\"",
              "Le 26 février 2010, Game Informer (Jeff Cork) estime que Rockstar San Diego a peuplé le jeu de \"nearly every stock Western character\" (presque tous les personnages types du western). Il oppose Nastas au \"loudmouth deputy\" (l'adjoint grande gueule) du jeu, qui \"isn't necessarily a different take on what we've seen before\" (n'apporte pas forcément un regard neuf sur ce qu'on a déjà vu), et écrit : \"Nastas could prove to be an interesting character if he's truly conflicted about his place in the world.\" (Nastas pourrait se révéler un personnage intéressant, s'il est vraiment tiraillé quant à sa place dans le monde).")},
    {"h3": two("Studies of the game's Native Americans", "Les Amérindiens du jeu vus par la critique")},
    {"p": two("In a chapter of the collection Undead in the West II (Scarecrow Press, 2013), M. Melissa Elston discusses Red Dead Redemption and Undead Nightmare. Wikipedia summarizes her reading of Nastas as an example of what the writer Gerald Vizenor calls \"manifest manners\", a false version of the Native experience presented as the truth. On April 17, 2014, Phill Alexander, writing for NYMGamer, described Nastas as \"a sort of guide-meets-confidant\". He wrote that Nastas \"shows some classic Native American traits\", being quiet, not combative and close to nature, \"but he is not presented to the gamer as a cartoon\".",
              "Dans un chapitre du recueil Undead in the West II (Scarecrow Press, 2013), M. Melissa Elston étudie Red Dead Redemption et Undead Nightmare. Selon le résumé qu'en donne Wikipédia, elle voit en Nastas un exemple de ce que l'écrivain Gerald Vizenor appelle les \"manifest manners\", une version fausse de l'expérience amérindienne présentée comme vraie. Le 17 avril 2014, Phill Alexander décrit Nastas, sur le site NYMGamer, comme \"a sort of guide-meets-confidant\" (un mélange de guide et de confident). Il écrit que Nastas \"shows some classic Native American traits\" (présente quelques traits classiques de l'Amérindien), calme, peu combatif et proche de la nature, \"but he is not presented to the gamer as a cartoon\" (mais il n'est pas présenté au joueur comme une caricature).")},
]


BASE = {
    "slug": "nastas", "name": "Nastas",
    "publishDate": "2026-09-24", "updated": "2026-10-22", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Guide &middot; RDR1", "reg_role_fr": "Guide &middot; RDR1",
    "gender": "Male", "birth": None, "death": "1911", "nationality": None,
    "portrait_alt": two("Nastas and John Marston held at gunpoint in Red Dead Redemption",
                        "Nastas et John Marston tenus en joue dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; West Elizabeth", "Personnage &middot; West Elizabeth"),
    "meta_desc": two("Nastas, the Bureau's Native informant in Red Dead Redemption: the Serendipity trap, the climb to Cochinay with John Marston, Harold MacDougal, his death at Bearclaw Camp, Benjamin Byron Davis.",
                     "Nastas, l'informateur amérindien du Bureau dans Red Dead Redemption : le piège du Serendipity, l'ascension vers Cochinay avec John Marston, Harold MacDougal, sa mort à Bearclaw Camp, Benjamin Byron Davis."),
    "og_desc": two("The complete reference on Nastas: life, missions, quotes, development and reception.",
                   "La référence complète sur Nastas : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Native American informant of the Bureau of Investigation in West Elizabeth who, in 1911, guides John Marston towards Dutch van der Linde's hideout at Cochinay and is shot dead by one of Dutch's men at Bearclaw Camp, in Red Dead Redemption.",
                       "Informateur amérindien du Bureau of Investigation dans West Elizabeth qui, en 1911, guide John Marston vers le repaire de Dutch van der Linde à Cochinay, puis est abattu par un homme de Dutch à Bearclaw Camp, dans Red Dead Redemption."),
    "chips": [two("Bureau informant", "Informateur du Bureau"), two("West Elizabeth", "West Elizabeth"),
              two("Died in <strong>1911</strong>", "Mort en <strong>1911</strong>"),
              two("Voiced by <strong>Benjamin Byron Davis</strong>", "Voix : <strong>Benjamin Byron Davis</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Nastas (no surname is given)", "Nastas (aucun nom de famille n'est donné)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1911, at Bearclaw Camp, Tall Trees (\"For Purely Scientific Purposes\"), shot by Enepay", "1911, à Bearclaw Camp, dans Tall Trees (\"For Purely Scientific Purposes\"), abattu par Enepay")},
        {"label": two("Origin", "Origine"), "value": two("Native American; grew up on a reservation and went to school", "Amérindien ; a grandi dans une réserve et est allé à l'école")},
        {"label": two("Occupation", "Activité"), "value": two("Informant for the Bureau of Investigation; guide", "Informateur du Bureau of Investigation ; guide")},
        {"label": two("Region", "Région"), "value": two("West Elizabeth (Blackwater, Tall Trees)", "West Elizabeth (Blackwater, Tall Trees)")},
        {"label": two("Allies", "Alliés"), "value": two("[[john-marston|John Marston]], [[harold-macdougal|Harold MacDougal]], [[edgar-ross|Edgar Ross]], [[archer-fordham|Archer Fordham]]", "[[john-marston|John Marston]], [[harold-macdougal|Harold MacDougal]], [[edgar-ross|Edgar Ross]], [[archer-fordham|Archer Fordham]]")},
        {"label": two("Enemies", "Ennemis"), "value": two("[[dutch-van-der-linde|Dutch van der Linde]]'s gang", "La bande de [[dutch-van-der-linde|Dutch van der Linde]]")},
        {"label": two("Weapons", "Armes"), "value": two("Cattleman Revolver, Double-barreled Shotgun, Repeater Carbine (Red Dead Wiki)", "Cattleman Revolver, fusil de chasse à deux coups, Repeater Carbine (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption (2010); Undead Nightmare (2010, as an undead); multiplayer model (Myths and Mavericks, 2011)", "Red Dead Redemption (2010) ; Undead Nightmare (2010, en mort-vivant) ; modèle multijoueur (Myths and Mavericks, 2011)")},
        {"label": two("Voiced by", "Voix"), "value": two("Benjamin Byron Davis", "Benjamin Byron Davis")},
    ],
    "intro": [
        two("Nastas is a Native American informant for the Bureau of Investigation in Red Dead Redemption (2010), set in 1911. He grew up on a reservation and went to school. His tip sends [[edgar-ross|Edgar Ross]], [[archer-fordham|Archer Fordham]] and [[john-marston|John Marston]] to the wreck of the Serendipity in search of [[dutch-van-der-linde|Dutch van der Linde]], where John and Fordham find him beaten and tied up, and walk into an ambush. Ross leaves him with the anthropologist [[harold-macdougal|Harold MacDougal]] in Blackwater.",
            "Nastas est un informateur amérindien du Bureau of Investigation dans Red Dead Redemption (2010), dont l'action se déroule en 1911. Il a grandi dans une réserve et est allé à l'école. Son renseignement conduit [[edgar-ross|Edgar Ross]], [[archer-fordham|Archer Fordham]] et [[john-marston|John Marston]] jusqu'à l'épave du Serendipity, sur la piste de [[dutch-van-der-linde|Dutch van der Linde]] : John et Fordham l'y trouvent roué de coups et ligoté, et tombent dans une embuscade. Ross le confie ensuite à l'anthropologue [[harold-macdougal|Harold MacDougal]], à Blackwater."),
        two("Nastas then guides John towards Dutch's hideout at Cochinay, and carries him down the mountain after Dutch's shot knocks him out. He sets up a meeting between MacDougal and some of Dutch's men at Bearclaw Camp, where one of them, Enepay, shoots him dead. He is voiced by Benjamin Byron Davis, who also plays Dutch.",
            "Nastas guide ensuite John vers le repaire de Dutch à Cochinay, puis le redescend de la montagne quand un tir de Dutch l'a assommé. Il organise une rencontre entre MacDougal et des hommes de Dutch à Bearclaw Camp, où l'un d'eux, Enepay, l'abat. Il a la voix de Benjamin Byron Davis, qui interprète aussi Dutch."),
    ],
    "essentials": [
        two("In \"Bear One Another's Burdens\", John and Fordham find him tied up on the wreck of the Serendipity; John carries him to the agents' car through Dutch's men.",
            "Dans \"Bear One Another's Burdens\", John et Fordham le trouvent ligoté sur l'épave du Serendipity ; John le porte jusqu'à la voiture des agents à travers les hommes de Dutch."),
        two("In \"At Home with Dutch\", he leads John and MacDougal to Cochinay, is wounded in a mine, then carries the unconscious John back down.",
            "Dans \"At Home with Dutch\", il conduit John et MacDougal vers Cochinay, est blessé dans une mine, puis redescend John inconscient."),
        two("He argues with MacDougal over the buffalo, the forests and the fate of his people.",
            "Il s'oppose à MacDougal au sujet des bisons, des forêts et du sort de son peuple."),
        two("In \"For Purely Scientific Purposes\", Enepay calls him a treacherous snake and kills him at Bearclaw Camp; MacDougal later signs a notice of his death in the Blackwater Ledger.",
            "Dans \"For Purely Scientific Purposes\", Enepay le traite de serpent perfide et l'abat à Bearclaw Camp ; MacDougal signe ensuite un avis de décès dans le Blackwater Ledger."),
        two("In Undead Nightmare, which is not canon, he returns as one of the undead and attacks MacDougal.",
            "Dans Undead Nightmare, hors canon, il revient en mort-vivant et attaque MacDougal."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["harold-macdougal", "john-marston", "dutch-van-der-linde", "archer-fordham"],
}
