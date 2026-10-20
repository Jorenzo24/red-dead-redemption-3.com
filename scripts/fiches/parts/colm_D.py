"""Colm O'Driscoll, reference fiche, PART D: base data, Development and performance, Reception
(20 Oct 2026, medium tier).

His live page (characters/colm-odriscoll/) was generated from the v2 entry in scripts/_wave2.py
("slug": "colm-odriscoll"; no entry in _enrich.py). The base below is rebuilt from that entry, with
corrections: the v2 intro called him "patient" and said he spends the game "trading ambushes and
reprisals" (interpretation, dropped); the v2 biography said "Colm's people killed" Annabelle (Dutch
says Colm killed her) and that the execution drew "lawmen alike" as a trap (unsupported, dropped); the
"Deceased" chip duplicated "Died 1899" and is dropped; the facts grid gains Born, Family, Alias, Games
and Voiced by. Eyebrow (kicker) kept as on the live page ("Character &middot; O'Driscoll Boys"); reg_role
matches characters_registry.py. publishDate 2026-07-05 kept (git: 9153fdc, drip publish of
colm-odriscoll, 5 Jul 2026; the live byline shows an older generator date).

Sources (internal register, fetched 20 Oct 2026):
- Red Dead Wiki "Colm O'Driscoll" (infobox: voice Andrew Berg) and "Andrew Berg" (American actor, voice
  and motion capture for Colm; no other credit listed). Wikipedia "List of Red Dead Redemption 2
  characters", Colm section (Andrew Berg in the role; pronunciation; real-life namesake), saved in
  colm/m/wp_List_of_Red_Dead_Redemption_2_characters.txt. GTABase character page (performer Andrew
  Berg; search extract). No interview with Berg was found; IMDb and Behind the Voice Actors refused the
  fetch (403); Rockstar's credits page did not render (scripts).
- PC Gamer, Joshua Wolens, 30 Aug 2024, on Roger Clark's Gamology Q&A (fetched): quote "The only thing
  I regret is saying Colm O'Driscoll incorrectly. Rockstar made me say it wrong. I told them it was
  wrong. They didn't care."; Clark is Irish-American; correct pronunciation closer to "column" than
  "comb"; Arthur would have little reason to know Irish pronunciation (PC Gamer's gloss).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content": Colm had his own unique horse (file
  reinsdefinitions.ymt); the Colm page adds that it was replaced by a generic model and that the
  horse appears only in three short scenes of "Old Friends" and "Blessed are the Peacemakers".
- LADbible, Matthew McGladdery, 7 Nov 2018 (archived copy of 10 Nov 2018, fetched): the real Colm
  O'Driscoll in Ireland, tweet of 3 Nov 2018 ("So it turns out I share the same name as a
  #RedDeadRedemption2 character and now I'm receiving hate mail online"), messages via Twitter and
  Instagram, he does not own an Xbox One or PS4, blocks offensive senders, quote given to Eurogamer.
  The Irish Post, Jack Beresford, 13 Nov 2018 (fetched): "A nefarious gang leader and the main
  antagonist"; a message warned he would be shot on sight.
- Game Rant, Rafly Gilang Pratama, 8 Aug 2020, "Red Dead Redemption: 10 Facts You Didn't Know About Colm
  O'Driscoll" (archived copy of 6 Dec 2021, fetched): "the game's most-hated antagonist"; "an
  old-time, degenerate friend of Dutch".
Excluded: the Red Dead Wiki's account that the Houser brothers personally insisted Arthur say the name
wrong because he is American (wiki only, no source given; PC Gamer says only "Rockstar"); Game Rant's
claims on West Cork ancestry, Tom receiving Colm's blessing, the O'Driscolls never crossing Cornwall
and the Dalton Gang inspiration ("might have taken", speculation); Game Rant's "Instagram" detail about
a single fan exchange (not needed); unused hair and vest models for O'Driscolls at the hanging (not
about Colm); IGN's pre-release playthrough order for Kieran's capture (belongs to the Kieran fiche);
WhatCulture and Fandom ranking pages (did not load, unverified).
Fact-check fixes (20 Oct 2026): Berg's motion capture and nationality attributed to the Red Dead Wiki only
(facts grid "Played by: Andrew Berg", intro without nationality); "only Sean" removed from Development (Names
owns the in-game pronunciation); cut-content sentence rewritten (too close to the wiki); Reception: hate messages
came on Instagram and were reported on Twitter; "never played the game" dropped (no source: The Irish Post only
says he owned neither console; the LADbible page now returns HTTP 410); blocking senders dropped; key fact 1 split.
DUPLICATE ownership: actor, pronunciation decision by Rockstar (Roger Clark), cut horse live HERE;
the namesake hate mail lives in Reception HERE (part C trivia must not repeat it). The in-game
pronunciation quarrel (Sean, Kieran) and the etymology are in part B Names. The Rockstar post of 23
Oct 2018 is in part B Skills. Colm's recurring musical theme (see sadie_C) is left to part C.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Colm O'Driscoll appears only in Red Dead Redemption 2 (2018). He is played by Andrew Berg. According to the Red Dead Wiki, Berg is an American actor and provides both the character's voice and his motion capture. Wikipedia's list of the game's characters also credits him in the role. The wiki lists no other part for him in the series, and no interview in which Berg discusses the role has been found.",
              "Colm O'Driscoll n'apparaît que dans Red Dead Redemption 2 (2018). Il est interprété par Andrew Berg. Selon le Red Dead Wiki, Berg est un acteur américain et prête au personnage à la fois sa voix et ses mouvements (capture de mouvement). La liste des personnages du jeu sur Wikipédia le crédite aussi dans ce rôle. Le wiki ne lui connaît pas d'autre rôle dans la série, et aucun entretien où Berg évoquerait ce personnage n'a été trouvé.")},
    {"h3": two("The pronunciation of his name", "La prononciation de son prénom")},
    {"p": two("Roger Clark, who plays Arthur Morgan, is an Irish-American actor and knows that the Irish name Colm sounds closer to \"column\" than to \"comb\", PC Gamer reported on 30 August 2024. Answering fan questions in an interview with Gamology, he named the way Arthur says the name as the only thing he would change about his performance: \"The only thing I regret is saying Colm O'Driscoll incorrectly. Rockstar made me say it wrong. I told them it was wrong. They didn't care.\" PC Gamer's Joshua Wolens noted that Arthur, as a character, would have had little reason to know how Irish names are pronounced. How the characters say the name in the game is covered under Names.",
              "Roger Clark, l'interprète d'Arthur Morgan, est un acteur irlando-américain et sait que le prénom irlandais Colm se prononce plutôt comme \"column\" que comme \"comb\", rapporte PC Gamer le 30 août 2024. Répondant aux questions de fans dans un entretien avec Gamology, il cite la façon dont Arthur prononce ce prénom comme la seule chose qu'il changerait à sa prestation : \"The only thing I regret is saying Colm O'Driscoll incorrectly. Rockstar made me say it wrong. I told them it was wrong. They didn't care.\" (mon seul regret, c'est d'avoir mal prononcé Colm O'Driscoll ; Rockstar m'a fait le dire de travers ; je leur ai dit que c'était faux ; ça leur était égal). Joshua Wolens, l'auteur de l'article, relève qu'Arthur, en tant que personnage, n'avait guère de raison de connaître la prononciation des prénoms irlandais. La façon dont les personnages prononcent ce prénom dans le jeu est traitée dans la rubrique Noms.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The game files show that Colm was meant to have a horse of his own, a unique model like those prepared for several outlaw gangs. Rockstar gave him a standard horse instead. According to the Red Dead Wiki, it appears in just three brief cutscenes across \"Old Friends\" and \"Blessed are the Peacemakers\".",
              "Les fichiers du jeu montrent que Colm devait avoir un cheval bien à lui, un modèle unique comme ceux prévus pour plusieurs bandes de hors-la-loi. Rockstar lui a finalement attribué un cheval ordinaire. D'après le Red Dead Wiki, celui-ci ne se montre que dans trois brèves cinématiques, réparties entre \"Old Friends\" et \"Blessed are the Peacemakers\".")},
]

BLOCKS_RECEPTION = [
    {"h3": two("A real Colm O'Driscoll", "Un vrai Colm O'Driscoll")},
    {"p": two("In the days after the game's release, an Irishman named Colm O'Driscoll began receiving hostile messages from players on Instagram. On 3 November 2018 he reported it on Twitter: \"So it turns out I share the same name as a #RedDeadRedemption2 character and now I'm receiving hate mail online.\" LADbible reported the story on 7 November 2018, in an article by Matthew McGladdery. He told Eurogamer that he found the whole thing \"kinda funny\", but that the messages were \"starting to get annoying\". The Irish Post covered it on 13 November 2018. The paper noted that he owned neither a PlayStation 4 nor an Xbox One, and that one message warned him he would be shot on sight.",
              "Dans les jours qui suivent la sortie du jeu, un Irlandais nommé Colm O'Driscoll reçoit des messages hostiles de joueurs sur Instagram. Le 3 novembre 2018, il s'en fait l'écho sur Twitter : \"So it turns out I share the same name as a #RedDeadRedemption2 character and now I'm receiving hate mail online.\" (il se trouve que je porte le même nom qu'un personnage de Red Dead Redemption 2, et voilà que je reçois des messages d'insultes). LADbible relate l'affaire le 7 novembre 2018, sous la plume de Matthew McGladdery. Il confie à Eurogamer qu'il trouve la situation \"kinda funny\" (plutôt drôle), mais que les messages commencent à devenir pénibles. The Irish Post reprend l'histoire le 13 novembre 2018. Le journal précise qu'il ne possède ni PlayStation 4 ni Xbox One, et qu'un message le menaçait d'être abattu à vue.")},
    {"h3": two("Assessments", "Regards critiques")},
    {"ul": [
        two("The Irish Post, Jack Beresford, 13 November 2018: the paper presented the character as \"a nefarious gang leader and the main antagonist\" of the game, whose men keep turning up in the open world to start firefights.",
            "The Irish Post, Jack Beresford, 13 novembre 2018 : le journal présente le personnage comme \"a nefarious gang leader and the main antagonist\" (un chef de bande malfaisant et le principal antagoniste) du jeu, dont les hommes surgissent sans cesse dans le monde ouvert pour déclencher des fusillades."),
        two("Game Rant, Rafly Gilang Pratama, 8 August 2020: a list of ten little-known facts about him calls him \"an old-time, degenerate friend of Dutch\" and \"the game's most-hated antagonist\".",
            "Game Rant, Rafly Gilang Pratama, 8 août 2020 : une liste de dix faits méconnus à son sujet le décrit comme \"an old-time, degenerate friend of Dutch\" (un vieil ami dépravé de Dutch) et \"the game's most-hated antagonist\" (l'antagoniste le plus détesté du jeu)."),
    ]},
]


BASE = {
    "slug": "colm-odriscoll", "name": "Colm O'Driscoll",
    "publishDate": "2026-07-05", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "O'Driscoll Boys &middot; RDR2", "reg_role_fr": "Gang O'Driscoll &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": "American",
    "portrait_alt": two("Colm O'Driscoll in Red Dead Redemption 2", "Colm O'Driscoll dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; O'Driscoll Boys", "Personnage &middot; Gang O'Driscoll"),
    "meta_desc": two("Colm O'Driscoll, leader of the O'Driscoll Boys and Dutch van der Linde's old enemy in RDR2: the feud, the parley trap, Arthur's capture, his hanging in Saint Denis in 1899, Andrew Berg.",
                     "Colm O'Driscoll, chef des O'Driscoll Boys et vieil ennemi de Dutch van der Linde dans RDR2 : la vendetta, le piège des pourparlers, la capture d'Arthur, sa pendaison à Saint-Denis en 1899, Andrew Berg."),
    "og_desc": two("The complete reference on Colm O'Driscoll: life, missions, quotes, development and reception.",
                   "La référence complète sur Colm O'Driscoll : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Founder and leader of the O'Driscoll Boys and rival of Dutch van der Linde, who captures Arthur Morgan after a fake parley and is hanged in Saint Denis in 1899, in Red Dead Redemption 2.",
                       "Fondateur et chef des O'Driscoll Boys, rival de Dutch van der Linde, qui capture Arthur Morgan après de faux pourparlers et finit pendu à Saint-Denis en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("O'Driscoll Boys", "Gang O'Driscoll"),
              two("Dutch's rival", "Rival de Dutch"),
              two("Played by <strong>Andrew Berg</strong>", "Interprété par <strong>Andrew Berg</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Colm O'Driscoll", "Colm O'Driscoll")},
        {"label": two("Alias", "Surnom"), "value": two("Mr O'D, in a letter written by one of his men", "Mr O'D, dans une lettre écrite par l'un de ses hommes")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, hanged in Saint Denis in \"Goodbye, Dear Friend\"", "1899, pendu à Saint-Denis dans \"Goodbye, Dear Friend\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédé")},
        {"label": two("Nationality", "Nationalité"), "value": two("American, of Irish descent according to the Red Dead Wiki", "Américaine, d'origine irlandaise selon le Red Dead Wiki")},
        {"label": two("Family", "Famille"), "value": two("A brother, never named, killed by [[dutch-van-der-linde|Dutch van der Linde]] years before 1899", "Un frère, jamais nommé, tué par [[dutch-van-der-linde|Dutch van der Linde]] des années avant 1899")},
        {"label": two("Affiliation", "Affiliation"), "value": two("O'Driscoll Boys (founder and leader). The Red Dead Wiki also lists Dutch van der Linde (formerly) and, for a time, the Pinkerton Agency", "O'Driscoll Boys (fondateur et chef). Le Red Dead Wiki mentionne aussi Dutch van der Linde (autrefois) et, un temps, l'agence Pinkerton")},
        {"label": two("Rival", "Rival"), "value": two("[[dutch-van-der-linde|Dutch van der Linde]] and the Van der Linde gang", "[[dutch-van-der-linde|Dutch van der Linde]] et le gang Van der Linde")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Andrew Berg", "Andrew Berg")},
    ],
    "intro": [
        two("Colm O'Driscoll is the founder and leader of the O'Driscoll Boys, the outlaw gang that has been at war with the Van der Linde gang for years. He is an antagonist of Red Dead Redemption 2 (2018), set in 1899. His feud with [[dutch-van-der-linde|Dutch van der Linde]] goes back to two killings: Dutch killed Colm's brother, and Colm killed Annabelle, the woman Dutch loved. In the Colter chapter the Van der Linde gang raids his camp and steals the train robbery he was planning. In chapter 3 he lures Dutch to a parley and has [[arthur-morgan|Arthur Morgan]] captured, as bait for a trap meant to deliver the whole gang to the law. Arrested later, he is hanged in Saint Denis in chapter 6, under the eyes of Dutch, Arthur and [[sadie-adler|Sadie Adler]].",
            "Colm O'Driscoll est le fondateur et le chef des O'Driscoll Boys, la bande de hors-la-loi en guerre depuis des années contre le gang Van der Linde. C'est l'un des antagonistes de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Sa querelle avec [[dutch-van-der-linde|Dutch van der Linde]] remonte à deux meurtres : Dutch a tué le frère de Colm, et Colm a tué Annabelle, la femme que Dutch aimait. Au chapitre de Colter, le gang Van der Linde attaque son camp et lui vole le coup qu'il préparait contre un train. Au chapitre 3, il attire Dutch à des pourparlers et fait capturer [[arthur-morgan|Arthur Morgan]], appât d'un piège destiné à livrer toute la bande à la loi. Arrêté par la suite, il est pendu à Saint-Denis au chapitre 6, sous les yeux de Dutch, d'Arthur et de [[sadie-adler|Sadie Adler]]."),
        two("He is played by Andrew Berg.",
            "Il est interprété par Andrew Berg."),
    ],
    "essentials": [
        two("He founded the O'Driscoll Boys, around 1889 by the Red Dead Wiki's reckoning, and leads them across several Western states. According to the same wiki, he twice escaped the noose before 1899.",
            "Il a fondé les O'Driscoll Boys, vers 1889 selon le calcul du Red Dead Wiki, et les mène dans plusieurs États de l'Ouest. Selon le même wiki, il a échappé deux fois à la corde avant 1899."),
        two("In \"Old Friends\", [[dutch-van-der-linde|Dutch]] and [[arthur-morgan|Arthur]] watch him strike [[kieran-duffy|Kieran Duffy]] and leave his camp at Ewing Basin, just before the Van der Linde gang wipes it out and takes his plan to rob a train.",
            "Dans \"Old Friends\", [[dutch-van-der-linde|Dutch]] et [[arthur-morgan|Arthur]] le voient frapper [[kieran-duffy|Kieran Duffy]] et quitter son camp d'Ewing Basin, juste avant que le gang Van der Linde ne l'anéantisse et ne lui prenne son projet d'attaque de train."),
        two("In \"Blessed are the Peacemakers\", he meets Dutch for a parley while his men capture Arthur; at Lone Mule Stead he tells Arthur he plans to hand the whole gang to the law, but Arthur escapes.",
            "Dans \"Blessed are the Peacemakers\", il rencontre Dutch pour parlementer pendant que ses hommes capturent Arthur ; à Lone Mule Stead, il explique à Arthur qu'il compte livrer toute la bande à la loi, mais Arthur s'évade."),
        two("Arrested and sentenced to death, he is hanged in Saint Denis in \"Goodbye, Dear Friend\" after Dutch, Arthur and [[sadie-adler|Sadie]] foil his men's rescue attempt.",
            "Arrêté et condamné à mort, il est pendu à Saint-Denis dans \"Goodbye, Dear Friend\", après que Dutch, Arthur et [[sadie-adler|Sadie]] ont fait échouer la tentative de sauvetage de ses hommes."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["dutch-van-der-linde", "arthur-morgan", "sadie-adler", "kieran-duffy"],
}
