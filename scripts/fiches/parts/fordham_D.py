"""Archer Fordham, reference fiche, PART D: base data, Development and performance, Reception (22 Oct 2026, medium tier).

His live page (characters/archer-fordham/) was generated from the v2 entry in scripts/_wave6.py (order 38, "slug":
"archer-fordham"; no entry in _enrich.py). publishDate 2026-10-03 kept (live byline "Updated October 3, 2026"). Eyebrow
kept as on the live page ("Character &middot; Bureau of Investigation"); reg_role matches characters_registry.py
("Bureau agent &middot; RDR1 &amp; 2" / "Agent du Bureau &middot; RDR1 &amp; 2"). Nationality "American" kept (EN and
FR wiki infoboxes; he is a federal agent who thanks John for doing "your country proud").
Corrections to the v2 base (CLAUDE.md: the live fiche had claims without source):
- v2 "Fordham handles much of the practical side of the operation: the paperwork, the transport, the coordination with
  the army and the local law": no transcript or page supports paperwork or coordination. Only the driving is attested
  (he drives the automobile and the armed vehicle). Dropped; the driving lives in part B.
- v2 "Fordham is the more measured of the two agents. He raises objections to Ross's methods and questions how far the
  operation should go": contradicted by every transcript (he backs Ross, threatens and insults John) and by the GOTY
  guide description ("very ambitious and aggressive"). Dropped.
- v2 "present at nearly every step of John's coerced hunt, from the initial blackmail to the death of Dutch": he is
  absent from the whole of Act I after the opening and from Mexico except the border handover. Rewritten on his seven
  RDR1 missions.
- v2 "Fordham and Ross take John's wife and son into government custody": the abduction is never shown; the Bureau holds
  them (Ross speaks for it). Rewritten as "the Bureau holds".
- v2 chip and fact "Alive" / "Alive at the end of RDR1": unsupported. According to the mission page of "The Last Enemy
  That Shall Be Destroyed", he can be shot in the last Dead Eye sequence at Beecher's Hope; no source tells his fate.
  Replaced by "Fate after 1911: not given in the games".
- v2 schema_desc, meta and og descriptions, intro and facts rewritten on the transcripts; v2 "Behind the scenes" (one
  sentence, no actor) replaced by Development and performance. v2 relationship with Andrew Milton dropped (no link in any
  source); "related" no longer lists Milton.

SOURCE REGISTER (read 22 Oct 2026):
- Red Dead Redemption manual (Rockstar, 2010; scratchpad cov/uncle/fc/rdr1_manual.txt, line 1880): cast list "Archer
  Fordham ... David Wilson Barnes", next to "Edgar Ross ... Jim Bentley" (consistent with edgar_D).
- Wikipedia "Red Dead Redemption" (raw wikitext, scratchpad cov/javier/fc/wp_rdr1.wiki, Plot section): "Edgar Ross (Jim
  Bentley) and Archer Fordham (David Wilson Barnes)".
- Wikipedia "David Wilson Barnes" (WebFetch 22 Oct 2026): born 30 Oct 1972, San Diego; died 30 Jul 2025, New York City,
  of cancer, aged 52; videography: Red Dead Redemption (2010), Archer Fordham, his only video game credit; films Capote
  (2005), The Company Men (2010), The Bourne Legacy (2012), Bridge of Spies (2015); TV Hell on Wheels (2014-2016), The
  Son (2017-2019). The death is sourced there to The Express (Fran Winston, 1 Sep 2025; not fetched: site blocked).
- Red Dead Wiki "David Wilson Barnes" (_m/David_Wilson_Barnes.txt): voice of Fordham; gives his age at death as 53
  (contradicted by the dates: 52, as Wikipedia says). Not used for the age.
- RDR2: no performer credit for Fordham found. Wikipedia "List of Red Dead Redemption 2 characters" does not name him
  or Barnes (WebFetch 22 Oct 2026); MobyGames credits page returned 403; IMDb not read. Said so in the text, nothing
  assumed.
- Red Dead Wiki "Red Dead Redemption Cut Content" (scratchpad cov/jack/fc/): cutscene fbi03 (Fordham's line "My Bessie
  does, sir."); the subtitles of "The Last Enemy That Shall Be Destroyed" (Rufus killed by Fordham). Same wording as
  edgar_D.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (scratchpad cov/andrew/fc_cut.txt): unused red vest, gloves and
  pants for an 1899 appearance, cut hair; the end-credits cutscene in Strawberry with Sheriff Hanley (placeholder
  caveat). Red Dead Wiki "Archer Fordham" (en.txt) trivia: the Pinkerton badge on the unused model.
- Transcripts of his RDR1 missions (_m/*_dialogues.txt), mission pages and the RDR2 "Ending Credits" page, for the
  intro, facts and essentials.
- Reception: searched 22 Oct 2026 (Game Informer, Game Rant, TheGamer, Sportskeeda, general web): no review or article
  about Fordham found. Game Informer (Jeff Cork, 26 Feb 2010) only mentions "the shifty federal agent" as a type,
  without naming him: not used. BLOCKS_RECEPTION is empty and the section is not listed in "sections".

Excluded: any motion-capture claim (no source); any RDR2 performer (no credit found); the wiki's age at death (53,
contradicted); the wiki's "Fordham joined the Bureau in 1907 following its foundation" (wiki-only background; part A
decides); "protégé" and "director" as our words (wiki); the wiki's reading of the 1899 model ("implying he was
originally supposed to be a part of the Pinkerton"): reported as the wiki's inference, not as fact; the YouTube video
cited by the wiki for Beecher's Hope (not a primary source; the mission page is attributed instead).
DUPLICATE ownership: the actor and all cut content live HERE (facts grid and chips may name the actor); parts B and C
must not retell them. The GOTY guide description is quoted in part B only.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("The cast list printed in the manual of Red Dead Redemption (2010) credits David Wilson Barnes as Archer Fordham, next to Jim Bentley as Edgar Ross. Wikipedia's article on the game gives the same credit, and the Red Dead Wiki lists Barnes as his voice. No source consulted credits Barnes with the motion capture of the character. No performer credit for Fordham in Red Dead Redemption 2 (2018) was found; Wikipedia's list of the game's characters does not mention him.",
              "La liste des interprètes imprimée dans la notice de Red Dead Redemption (2010) crédite David Wilson Barnes dans le rôle d'Archer Fordham, à côté de Jim Bentley pour Edgar Ross. L'article de Wikipédia consacré au jeu reprend ce crédit, et le Red Dead Wiki lui attribue la voix du personnage. Aucune des sources consultées ne lui prête la capture de mouvement. Nous n'avons trouvé aucun crédit d'interprète pour Fordham dans Red Dead Redemption 2 (2018) ; la liste des personnages du jeu sur Wikipédia ne le mentionne pas.")},
    {"p": two("According to Wikipedia, David Wilson Barnes was an American actor born on October 30, 1972, in San Diego, California. His film roles include Capote (2005), The Company Men (2010), The Bourne Legacy (2012) and Bridge of Spies (2015), and he had recurring roles in the television series Hell on Wheels and The Son. Red Dead Redemption is the only video game in his Wikipedia credits. He died of cancer in New York City on July 30, 2025, aged 52, a death reported by The Express on September 1, 2025.",
              "D'après Wikipédia, David Wilson Barnes était un acteur américain né le 30 octobre 1972 à San Diego, en Californie. Au cinéma, on l'a vu notamment dans Truman Capote (2005), The Company Men (2010), Jason Bourne : l'héritage (2012) et Le Pont des espions (2015) ; à la télévision, il a tenu des rôles récurrents dans les séries Hell on Wheels et The Son. Red Dead Redemption est le seul jeu vidéo de sa filmographie sur Wikipédia. Il est mort d'un cancer à New York le 30 juillet 2025, à 52 ans, une disparition rapportée par The Express le 1er septembre 2025.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The files of Red Dead Redemption contain a cutscene, labeled fbi03, that was not used. In it, Ross mocks a newspaper story about women wanting the vote, and Fordham answers that his Bessie does; Ross tells him to make sure she stays his Bessie and that he does not become hers. According to the Red Dead Wiki, subtitles left in the files of \"The Last Enemy That Shall Be Destroyed\" suggest an earlier version of the mission in which Fordham was to kill Rufus, the family dog.",
              "Les fichiers de Red Dead Redemption contiennent une cinématique inutilisée, nommée fbi03. Ross s'y moque d'un article de journal sur les femmes qui réclament le droit de vote, et Fordham répond que sa Bessie le réclame ; Ross lui conseille de faire en sorte qu'elle reste sa Bessie, et non l'inverse. D'après le Red Dead Wiki, des sous-titres restés dans les fichiers de \"The Last Enemy That Shall Be Destroyed\" laissent deviner une version antérieure de la mission, dans laquelle Fordham devait tuer Rufus, le chien de la famille.")},
    {"p": two("The files of Red Dead Redemption 2 contain an unused 1899 version of Fordham, with a red vest, gloves, trousers and a different haircut. The Red Dead Wiki notes that this model carries a Pinkerton badge and reads it as a sign that he was first meant to appear as a Pinkerton agent before the epilogue. According to the same wiki, a cutscene of the end credits was meant to show him and Ross questioning townspeople and Sheriff Hanley in Strawberry; the wiki adds that Hanley may only be a placeholder in the cutscene files.",
              "Les fichiers de Red Dead Redemption 2 renferment une version inutilisée de Fordham datée de 1899, avec gilet rouge, gants, pantalon et une autre coupe de cheveux. Le Red Dead Wiki relève que ce modèle porte un insigne Pinkerton, et y voit le signe qu'il devait d'abord apparaître avant l'épilogue en agent de la Pinkerton. Selon le même wiki, une cinématique du générique de fin devait le montrer avec Ross en train d'interroger des habitants et le shérif Hanley à Strawberry ; le wiki ajoute que Hanley n'est peut-être qu'un personnage provisoire dans les fichiers de cinématique.")},
]

# No review or article about Fordham was found (searched 22 Oct 2026): empty, and not listed in BASE["sections"].
BLOCKS_RECEPTION = []


BASE = {
    "slug": "archer-fordham", "name": "Archer Fordham",
    "publishDate": "2026-10-03", "updated": "2026-10-22", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Bureau agent &middot; RDR1 &amp; 2", "reg_role_fr": "Agent du Bureau &middot; RDR1 &amp; 2",
    "gender": "Male", "birth": None, "death": None, "nationality": "American",
    "portrait_alt": two("Agent Archer Fordham beside John Marston indoors in Red Dead Redemption",
                        "L'agent Archer Fordham aux côtés de John Marston, en intérieur, dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; Bureau of Investigation", "Personnage &middot; Bureau of Investigation"),
    "meta_desc": two("Archer Fordham, Edgar Ross's fellow Bureau agent: Micah's body and Beecher's Hope in 1907, John Marston's escort, Javier at the border, the hunt for Dutch van der Linde, David Wilson Barnes.",
                     "Archer Fordham, l'agent du Bureau aux côtés d'Edgar Ross : le corps de Micah et Beecher's Hope en 1907, l'escorte de John Marston, Javier à la frontière, la traque de Dutch van der Linde, David Wilson Barnes."),
    "og_desc": two("The complete reference on Archer Fordham: life, missions, quotes and development.",
                   "La référence complète sur Archer Fordham : vie, missions, citations et conception."),
    "schema_desc": two("Agent of the Bureau of Investigation who works under Edgar Ross: in 1907 he traces Micah Bell's death to John Marston, and in 1911 he escorts John, collects Javier Escuella at the border and joins the hunt for Dutch van der Linde, in Red Dead Redemption and Red Dead Redemption 2.",
                       "Agent du Bureau of Investigation sous les ordres d'Edgar Ross : en 1907, il remonte de la mort de Micah Bell jusqu'à John Marston, et en 1911, il escorte John, récupère Javier Escuella à la frontière et participe à la traque de Dutch van der Linde, dans Red Dead Redemption et Red Dead Redemption 2."),
    "chips": [two("Bureau of Investigation", "Bureau of Investigation"), two("Federal agent", "Agent fédéral"),
              two("RDR1 &amp; RDR2", "RDR1 &amp; RDR2"),
              two("Voiced by <strong>David Wilson Barnes</strong>", "Voix : <strong>David Wilson Barnes</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Archer Fordham", "Archer Fordham")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the games", "Non précisée dans les jeux")},
        {"label": two("Fate", "Sort"), "value": two("Not given after 1911; he can be shot at Beecher's Hope, according to the mission page of \"The Last Enemy That Shall Be Destroyed\"", "Inconnu après 1911 ; il peut être abattu à Beecher's Hope, selon la page de la mission \"The Last Enemy That Shall Be Destroyed\"")},
        {"label": two("Occupation", "Activité"), "value": two("Agent of the Bureau of Investigation", "Agent du Bureau of Investigation")},
        {"label": two("Superior", "Supérieur"), "value": two("[[edgar-ross|Edgar Ross]]", "[[edgar-ross|Edgar Ross]]")},
        {"label": two("Family", "Famille"), "value": two("Maybelle Fordham, mother, died 1900 (Red Dead Wiki)", "Maybelle Fordham, sa mère, morte en 1900 (Red Dead Wiki)")},
        {"label": two("Region", "Région"), "value": two("West Elizabeth (Blackwater); the New Austin border", "West Elizabeth (Blackwater) ; la frontière du New Austin")},
        {"label": two("Weapons", "Armes"), "value": two("Cattleman Revolver, High Power Pistol, Winchester Repeater (Red Dead Wiki)", "Cattleman Revolver, High Power Pistol, Winchester Repeater (Red Dead Wiki)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption (2010); Red Dead Redemption 2 (2018, end credits)", "Red Dead Redemption (2010) ; Red Dead Redemption 2 (2018, générique de fin)")},
        {"label": two("Voiced by", "Voix"), "value": two("David Wilson Barnes (Red Dead Redemption)", "David Wilson Barnes (Red Dead Redemption)")},
    ],
    "intro": [
        two("Archer Fordham is an agent of the Bureau of Investigation who works under [[edgar-ross|Edgar Ross]]. He first appears in Red Dead Redemption (2010), set in 1911, and returns in the end credits of Red Dead Redemption 2 (2018), set in 1907. There, he and Ross find the body of [[micah-bell|Micah Bell]] on Mount Hagen, question witnesses in Valentine and near Rhodes, and end up watching [[john-marston|John Marston]] and his son [[jack-marston|Jack]] at Beecher's Hope.",
            "Archer Fordham est un agent du Bureau of Investigation placé sous les ordres d'[[edgar-ross|Edgar Ross]]. Il apparaît dans Red Dead Redemption (2010), dont l'action se déroule en 1911, et revient dans le générique de fin de Red Dead Redemption 2 (2018), situé en 1907. Ross et lui y découvrent le corps de [[micah-bell|Micah Bell]] sur le mont Hagen, interrogent des témoins à Valentine et près de Rhodes, et finissent par observer [[john-marston|John Marston]] et son fils [[jack-marston|Jack]] à Beecher's Hope."),
        two("In 1911, while the Bureau holds John's wife and son, Fordham and Ross put John on the train for Armadillo, collect [[javier-escuella|Javier Escuella]] from him at the border, then hunt [[dutch-van-der-linde|Dutch van der Linde]] with him in West Elizabeth, up to Dutch's death at Cochinay. He is voiced by David Wilson Barnes.",
            "En 1911, tandis que le Bureau retient la femme et le fils de John, Fordham et Ross le mettent dans le train pour Armadillo, récupèrent [[javier-escuella|Javier Escuella]] de ses mains à la frontière, puis traquent avec lui [[dutch-van-der-linde|Dutch van der Linde]] dans West Elizabeth, jusqu'à la mort de Dutch à Cochinay. Il a la voix de David Wilson Barnes."),
    ],
    "essentials": [
        two("In the 1907 end credits of Red Dead Redemption 2, he and Ross trace Micah's death to John Marston at Beecher's Hope.",
            "Dans le générique de 1907 de Red Dead Redemption 2, Ross et lui remontent de la mort de Micah jusqu'à John Marston, à Beecher's Hope."),
        two("In \"The Gates of El Presidio\", he takes Javier from John near the border bridge, alive or dead depending on the player, and sends John after Bill Williamson.",
            "Dans \"The Gates of El Presidio\", il récupère Javier près du pont de la frontière, vivant ou mort selon le choix du joueur, et envoie John à la poursuite de Bill Williamson."),
        two("In \"Bear One Another's Burdens\", he drives John and Ross to the wreck of the Serendipity and finds the informant [[nastas|Nastas]] there with John.",
            "Dans \"Bear One Another's Burdens\", il conduit John et Ross jusqu'à l'épave du Serendipity, où il trouve avec John l'informateur [[nastas|Nastas]]."),
        two("He takes part in the ambush at the Blackwater bank and in the assault on Cochinay, and thanks John once Dutch is dead.",
            "Il participe à l'embuscade de la banque de Blackwater et à l'assaut de Cochinay, puis remercie John une fois Dutch mort."),
        two("According to the Red Dead Wiki, he is among the men who come for John at Beecher's Hope later in 1911.",
            "Selon le Red Dead Wiki, il fait partie des hommes qui viennent chercher John à Beecher's Hope, plus tard en 1911."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["edgar-ross", "john-marston", "nastas", "harold-macdougal"],
}
