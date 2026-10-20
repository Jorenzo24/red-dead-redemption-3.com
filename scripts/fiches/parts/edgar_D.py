"""Edgar Ross, reference fiche, PART D: base data, Development and performance, Reception.

His live page (characters/edgar-ross/) was generated from the v2 entry in scripts/_wave2.py
(slug "edgar-ross"; no ENRICHED entry in _enrich.py); the base below is rebuilt from it, with
corrections. Changes from the v2 page: the intro now covers both games (1899, 1907, 1911, 1914);
the "Deceased" chip duplicated "Died 1914" and is dropped, replaced by the voice actor; the facts
grid gains birth (attributed), family, career and voice; the v2 "Behind the scenes" sentence ("by
design, one of the series' most hated figures") is dropped as unsourced; the v2 personality line
("frames cruelty as the price of progress") is dropped as interpretation. Eyebrow (kicker) kept:
"Character &middot; Red Dead Redemption". reg_role kept identical to characters_registry.py
("Antagonist &middot; RDR1"), although he also appears in RDR2: changing it means changing the
registry. publishDate 2026-07-06 kept (git: 7d14864, drip publish of edgar-ross, 6 Jul 2026).

Sources (internal register, fetched 20 Oct 2026, saved in scratchpad cov/edgar/fc/ unless noted):
- Red Dead Redemption manual (Rockstar, 2010; cov/uncle/fc/rdr1_manual.txt, line 1879): cast
  list "Edgar Ross ... Jim Bentley", "Archer Fordham ... David Wilson Barnes". RDR1 end credits
  (cov/jack/fc/rdr1_credits.txt): Bentley in the list of performers.
- Wikipedia "List of Red Dead Redemption 2 characters" (cov/uncle/fc/wp_list_rdr2_characters.txt):
  "Agent Edgar Ross (Jim Bentley)"; recording sessions from 2013, 2,200 days, led by Rod Edge;
  Robert Whitaker's chapter "The Last Enemy That Shall Be Considered: Law and Order in Red Dead",
  in J. Wills and E. Wright (eds), Red Dead Redemption: History, Myth, and Violence in the Video
  Game West, University of Oklahoma Press, 30 Mar 2023, pp. 59-73 (Hoover comparison, p. 69;
  quoted sentence, p. 70). The book itself was not read: quoted through Wikipedia, said so.
- Red Dead Wiki "Jim Bentley" (wiki_Jim_Bentley.txt): actor, stuntman, stand-up comedian,
  magician; TV and film credits; voice and motion capture of Ross in both games.
- Rockstar Newswire feature "A New National Order: The Power of Federal Law Emerges in Early 20th
  Century America" (series The True West, History that Helped Inspire Red Dead Redemption), cited
  by the Red Dead Wiki; text read on the iRedDead reprint dated 18 June 2010 (Rockstar's page did
  not render its body). Quote checked on the reprint.
- Red Dead Wiki "Red Dead Redemption Cut Content" (cov/jack/fc/): cutscene fbi03 (dialogue), unused
  Ross lines and changes in "The Last Enemy That Shall Be Destroyed". "Red Dead Redemption 2 Cut
  Content": unused gunbelt; cut credits scene in Strawberry with Sheriff Hanley (hedged by the wiki).
- Red Dead Wiki user blog, Spawny0908, first posted 16 Jan 2012, interview with Steve J. Palmer
  (cov/bill/fc/wk_User_blog_...txt): "slime ball", "the TRUE baddy", "Hats off to Jim Bentley".
- Game Informer, Shin Hieftje, 16 Apr 2014, "What Makes A Game Ending Memorable?"
  (cov/jack/fc/gi_ending.txt).
- Game Rant, Joshua Duckworth, 27 Mar 2020 (cov/jack/fc/gamerant_rivalry.txt).
- WhatCulture, Matt Thompson, 7 Feb 2022, "Red Dead Redemption: Every Villain Ranked From Worst To
  Best" (fetched 20 Oct 2026: Ross 3rd, Dutch 2nd, Micah 1st).
- Liars and Cheats (Red Dead Wiki, cov/abigail/fc/wiki_Liars_and_Cheats.txt): released 21 Sep
  2010, Ross in the "Damnation" group (facts grid only; fuller account belongs to part C).
- 1914 newspaper "Edgar Ross Retires After a Lifetime of Government Service" (wiki transcription,
  wiki_Edgar_Ross_Retires...txt): used only for the facts grid (retirement, wife, Lake Don Julio).
Excluded: an interview with Jim Bentley about Ross (none found; no longer said in the text); Bentley's height (wiki only, and
any link to Ross's on-screen height would be speculation); the claim that Ross is "modeled off"
Bonaparte (the Newswire only calls him a representative of the new federal agents) and "appears to
be based off" Hoover (wiki speculation; Whitaker's comparison is given in Reception, attributed);
Tenpenny and Toreno comparisons (wiki analysis); Game Rant's reading of the river scenes as a
rivalry and of Ross's "first and last words" (used in the Jack fiche; not repeated here, and part C
Trivia may own the river parallel); Bentley's TV/film list (wiki wording too close; cut to one
credit, Tequila Sunrise, confirmed by IMDb/RT per the fact-check); the in-game founding date of the Bureau (part A).
DUPLICATE ownership: actor, historical background (Newswire, real Bureau dates) and all cut
content live HERE; parts B and C must not retell them. The GOTY guide description belongs to part
B. The 1907 and 1914 newspapers' narrative content belongs to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Ross is played by Jim Bentley in both games. The cast list printed in the manual of Red Dead Redemption (2010) credits him in the role, next to David Wilson Barnes as Archer Fordham. Wikipedia's list of Red Dead Redemption 2 characters gives Bentley again for Ross in the 2018 prequel. According to the Red Dead Wiki, he provided both the voice and the motion capture of the character. The same wiki describes Bentley as an actor, stuntman and magician whose film credits include Tequila Sunrise. According to Wikipedia, Rockstar hired Rod Edge as full-time director to handle the actors' performances on Red Dead Redemption, and he was motion capture director on Red Dead Redemption 2, whose recording sessions began in 2013 and lasted 2,200 days in total.",
              "Ross est interprété par Jim Bentley dans les deux jeux. La liste des interprètes imprimée dans la notice de Red Dead Redemption (2010) le crédite dans ce rôle, à côté de David Wilson Barnes pour Archer Fordham. La liste des personnages de Red Dead Redemption 2 sur Wikipédia donne de nouveau Bentley pour Ross dans la préquelle de 2018. D'après le Red Dead Wiki, il assure à la fois la voix et la capture de mouvement du personnage. Le même wiki présente Bentley comme un acteur, cascadeur et magicien, dont la filmographie compte notamment Tequila Sunrise. Selon Wikipédia, Rockstar a engagé Rod Edge à plein temps pour diriger le jeu des acteurs de Red Dead Redemption, et il a été directeur de la capture de mouvement de Red Dead Redemption 2, dont les séances d'enregistrement ont commencé en 2013 et totalisé 2 200 jours.")},
    {"h3": two("Historical background", "Contexte historique")},
    {"p": two("In 2010, the year of Red Dead Redemption's release, Rockstar published a series of features on the history behind the game, The True West. One of them, \"A New National Order\", reprinted by the fan site iRedDead on June 18, 2010, traces the growth of federal law enforcement under the Progressive presidents. It presents Charles Joseph Bonaparte, a relative of Napoleon, as the founder of modern federal law enforcement, and names \"Red Dead Redemption's Edgar Ross, a representative of this new breed of Federal Special Agent, who offers Marston a deal he can't refuse.\" The real force of special agents was created in 1908, when Bonaparte was Attorney General under Theodore Roosevelt; it was named the Bureau of Investigation in 1909 and took the name Federal Bureau of Investigation in 1935.",
              "En 2010, l'année de la sortie de Red Dead Redemption, Rockstar publie une série d'articles sur l'histoire qui a inspiré le jeu, The True West. L'un d'eux, \"A New National Order\", repris par le site de fans iRedDead le 18 juin 2010, retrace l'essor de la police fédérale sous les présidents progressistes. Il présente Charles Joseph Bonaparte, parent de Napoléon, comme le fondateur de la police fédérale moderne, et cite \"Red Dead Redemption's Edgar Ross, a representative of this new breed of Federal Special Agent, who offers Marston a deal he can't refuse.\" (Edgar Ross, de Red Dead Redemption, représentant de cette nouvelle race d'agents spéciaux fédéraux, qui propose à Marston un marché qu'il ne peut pas refuser). Le véritable corps d'agents spéciaux est créé en 1908, quand Bonaparte est procureur général sous Theodore Roosevelt ; il prend le nom de Bureau of Investigation en 1909, puis celui de Federal Bureau of Investigation (FBI) en 1935.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The files of Red Dead Redemption contain a cutscene, labeled fbi03, that was not used. In it, Ross mocks a newspaper story about women wanting the vote, and Fordham answers that his Bessie does. When John arrives, Ross jokes about buying a holiday home at Beecher's Hope and says he will need military help in the pursuit of justice. John reminds him that the plan was for John himself to take the public acclaim for killing Dutch; Ross answers that John will kill Dutch, but that a clash between the army and Native Americans would also serve. John objects that those people have lived peacefully there for more than 20 years, and Ross replies that the American public does not need to know it. The scene was to lead into West Dickens's arrest in \"Bear One Another's Burdens\".",
              "Les fichiers de Red Dead Redemption contiennent une cinématique inutilisée, nommée fbi03. Ross s'y moque d'un article de journal sur les femmes qui réclament le droit de vote, et Fordham répond que sa Bessie le réclame. À l'arrivée de John, Ross plaisante sur l'achat d'une maison de vacances à Beecher's Hope et annonce qu'il lui faudra l'aide de l'armée pour faire régner la justice. John lui rappelle que le plan prévoyait de laisser à John lui-même la gloire publique de la mort de Dutch ; Ross répond que John tuera bien Dutch, mais qu'un affrontement entre l'armée et des Amérindiens servirait aussi. John objecte que ces gens vivent en paix dans la région depuis plus de vingt ans, et Ross rétorque que le public américain n'a pas besoin de le savoir. La scène devait déboucher sur l'arrestation de West Dickens dans \"Bear One Another's Burdens\".")},
    {"p": two("According to the Red Dead Wiki, subtitles left in the files of \"The Last Enemy That Shall Be Destroyed\" suggest an earlier version of the mission: a soldier was to kidnap Abigail, John was to fetch his rifle from the kitchen and choose between running, fighting and surrendering, and Fordham was to kill Rufus, the family dog. Ross also has unused lines for that mission. In Red Dead Redemption 2, Ross has an unused gunbelt, and a cutscene of the end credits was meant to show him and Fordham questioning townspeople and Sheriff Hanley in Strawberry; the Red Dead Wiki notes that Hanley may only be a placeholder in the cutscene files.",
              "D'après le Red Dead Wiki, des sous-titres restés dans les fichiers de \"The Last Enemy That Shall Be Destroyed\" laissent deviner une version antérieure de la mission : un soldat devait enlever Abigail, John devait aller chercher son fusil dans la cuisine et choisir entre fuir, se battre ou se rendre, et Fordham devait tuer Rufus, le chien de la famille. Ross dispose aussi de répliques inutilisées pour cette mission. Dans Red Dead Redemption 2, il reste un ceinturon inutilisé à son nom, et une cinématique du générique de fin devait le montrer avec Fordham en train d'interroger des habitants et le shérif Hanley à Strawberry ; le Red Dead Wiki précise que Hanley n'est peut-être qu'un personnage provisoire dans les fichiers de cinématique.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Critics and commentators", "Critiques et commentateurs")},
    {"ul": [
        two("Steve J. Palmer, who plays Bill Williamson, interviewed on the Red Dead Wiki (post first published on January 16, 2012): he said he was surprised that many players saw Bill as the main villain, and that Ross deserved the title: \"That guy was a slime ball, and the TRUE baddy. Hats off to Jim Bentley for a great character.\"",
            "Steve J. Palmer, interprète de Bill Williamson, interrogé sur le Red Dead Wiki (billet publié le 16 janvier 2012) : il se dit surpris que de nombreux joueurs voient en Bill le grand méchant du jeu, alors que le titre revient à Ross : \"That guy was a slime ball, and the TRUE baddy. Hats off to Jim Bentley for a great character.\" (ce type était une ordure, le VRAI méchant ; chapeau à Jim Bentley pour ce grand personnage)."),
        two("Game Informer, April 16, 2014: in a feature on memorable game endings, Shin Hieftje writes that in the final scene \"Ross cockily defends his actions to Jack, making him even more reprehensible.\"",
            "Game Informer, 16 avril 2014 : dans un dossier sur les fins de jeu marquantes, Shin Hieftje écrit que dans la scène finale, Ross justifie ses actes devant Jack avec arrogance, ce qui le rend encore plus détestable."),
        two("Game Rant, March 27, 2020: Joshua Duckworth writes that Ross believes in government, civilization and society \"as long as it benefits him\", that he is \"not a man of his word\", and that he betrays John \"to pad his own accomplishments\".",
            "Game Rant, 27 mars 2020 : Joshua Duckworth écrit que Ross croit au gouvernement, à la civilisation et à la société \"as long as it benefits him\" (tant qu'il y trouve son compte), qu'il n'a pas de parole (\"not a man of his word\"), et qu'il trahit John pour gonfler son propre palmarès."),
        two("WhatCulture, February 7, 2022: Matt Thompson ranks Ross third among the villains of the series, behind Dutch and Micah. He cites the kidnapping of Abigail and Jack, the joke about Abigail's death and the broken deal, and concludes: \"Because Ross is so slimy, so reprehensible, and so unapologetic; it makes him all the better a villain to put six heavy bullets in.\"",
            "WhatCulture, 7 février 2022 : Matt Thompson classe Ross troisième des méchants de la série, derrière Dutch et Micah. Il cite l'enlèvement d'Abigail et de Jack, la plaisanterie sur la mort d'Abigail et le marché trahi, et conclut que, Ross étant si visqueux, si répugnant et si dépourvu de remords, on a d'autant plus envie de lui loger six balles dans le corps."),
    ]},
    {"h3": two("Academic analysis", "Analyse universitaire")},
    {"p": two("In a chapter on law and order in the series, published on March 30, 2023 in the collection Red Dead Redemption: History, Myth, and Violence in the Video Game West (University of Oklahoma Press, edited by John Wills and Esther Wright), the historian Robert Whitaker compares Ross's handling of gangsters and of public perception of law enforcement to the methods of J. Edgar Hoover. Wikipedia's list of Red Dead Redemption 2 characters quotes his conclusion: \"the duplicity, viciousness, and consistency of Edgar Ross's character makes him an incredibly effective villain, and also a deeply satisfying final enemy\". The same list, citing Game Rant and Whitaker, presents Ross as standing for civilization, the end of the Wild West and the corruption of government and police in that era.",
              "Dans un chapitre consacré à la loi et à l'ordre dans la série, paru le 30 mars 2023 dans l'ouvrage collectif Red Dead Redemption: History, Myth, and Violence in the Video Game West (University of Oklahoma Press, sous la direction de John Wills et Esther Wright), l'historien Robert Whitaker compare la façon dont Ross traite les bandits et façonne l'image des forces de l'ordre aux méthodes de J. Edgar Hoover. La liste des personnages de Red Dead Redemption 2 sur Wikipédia cite sa conclusion : \"the duplicity, viciousness, and consistency of Edgar Ross's character makes him an incredibly effective villain, and also a deeply satisfying final enemy\" (la duplicité, la cruauté et la constance du personnage d'Edgar Ross en font un méchant d'une efficacité remarquable, et aussi un ennemi final profondément satisfaisant). La même liste, s'appuyant sur Game Rant et sur Whitaker, voit en Ross l'incarnation de la civilisation, de la fin du Far West et de la corruption de l'État et de la police à cette époque.")},
]


BASE = {
    "slug": "edgar-ross", "name": "Edgar Ross",
    "publishDate": "2026-07-06", "updated": "2026-10-20", "schema_game": "Red Dead Redemption",
    "reg_role_en": "Antagonist &middot; RDR1", "reg_role_fr": "Antagoniste &middot; RDR1",
    "gender": "Male", "death": "1914", "nationality": "American",
    "portrait_alt": two("Edgar Ross in Red Dead Redemption", "Edgar Ross dans Red Dead Redemption"),
    "eyebrow": two("Character &middot; Red Dead Redemption", "Personnage &middot; Red Dead Redemption"),
    "meta_desc": two("Edgar Ross, the Pinkerton agent of RDR2 who becomes head of the Bureau of Investigation, forces John Marston to hunt his old gang in RDR1 and is killed by Jack in 1914.",
                     "Edgar Ross, l'agent Pinkerton de RDR2 devenu chef du Bureau of Investigation, qui force John Marston à traquer son ancien gang dans RDR1 et que Jack tue en 1914."),
    "og_desc": two("The complete reference on Edgar Ross: life, missions, quotes, development and reception.",
                   "La référence complète sur Edgar Ross : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Pinkerton agent under Andrew Milton in 1899, then head of the Bureau of Investigation, who forces John Marston to hunt down his former gang in 1911, has him killed, and is shot dead by Jack Marston in 1914, in Red Dead Redemption and Red Dead Redemption 2.",
                       "Agent de la Pinkerton sous les ordres d'Andrew Milton en 1899, puis chef du Bureau of Investigation, qui force John Marston à traquer son ancien gang en 1911, le fait abattre, et meurt sous les balles de Jack Marston en 1914, dans Red Dead Redemption et Red Dead Redemption 2."),
    "chips": [two("Died <strong>1914</strong>", "Mort en <strong>1914</strong>"),
              two("Bureau of Investigation", "Bureau of Investigation"),
              two("Main antagonist (RDR1)", "Antagoniste principal (RDR1)"),
              two("Voiced by <strong>Jim Bentley</strong>", "Voix de <strong>Jim Bentley</strong>")],
    "facts": [
        {"label": two("Born", "Naissance"), "value": two("Around 1861 (Red Dead Wiki, from the Game of the Year Edition guide of Red Dead Redemption)", "Vers 1861 (Red Dead Wiki, d'après le guide de l'édition Game of the Year de Red Dead Redemption)")},
        {"label": two("Died", "Mort"), "value": two("1914, on the bank of the San Luis River in Nuevo Paraíso, killed by Jack Marston in a duel in \"Remember My Family\"", "1914, sur la rive du San Luis, au Nuevo Paraíso, tué en duel par Jack Marston dans \"Remember My Family\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédé")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Family", "Famille"), "value": two("Emily Ross (wife), Phillip Ross (brother)", "Emily Ross (épouse), Phillip Ross (frère)")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Pinkerton National Detective Agency (1899); National Bureau of Criminal Identification; Bureau of Investigation (head from 1907, retired around 1913)", "Pinkerton National Detective Agency (1899) ; National Bureau of Criminal Identification ; Bureau of Investigation (à sa tête à partir de 1907, retraité vers 1913)")},
        {"label": two("Role", "Rôle"), "value": two("Pinkerton agent under Andrew Milton (1899); federal agent based in Blackwater (1907 to 1913)", "Agent de la Pinkerton sous les ordres d'Andrew Milton (1899) ; agent fédéral en poste à Blackwater (1907 à 1913)")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption (also a multiplayer character with the Liars and Cheats pack, 2010), Red Dead Redemption 2", "Red Dead Redemption (aussi personnage jouable en multijoueur avec le pack Liars and Cheats, 2010), Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Jim Bentley (both games)", "Jim Bentley (dans les deux jeux)")},
    ],
    "intro": [
        two("Edgar Ross is an American lawman and the main antagonist of Red Dead Redemption (2010), set in 1911 and 1914. He also appears in Red Dead Redemption 2 (2018), set in 1899 and 1907. In 1899 he is a Pinkerton agent working under [[andrew-milton|Andrew Milton]] against the Van der Linde gang; by 1907 he heads the newly created Bureau of Investigation. In 1911 he holds [[abigail-marston|Abigail]] and [[jack-marston|Jack Marston]] to force [[john-marston|John Marston]] to hunt down his former companions, then leads the attack on John's ranch in which John is killed. In 1914, retired, he is killed in a duel by Jack.",
            "Edgar Ross est un homme de loi américain et l'antagoniste principal de Red Dead Redemption (2010), dont l'action se déroule en 1911 et 1914. Il apparaît aussi dans Red Dead Redemption 2 (2018), qui se passe en 1899 et 1907. En 1899, il est agent de la Pinkerton sous les ordres d'[[andrew-milton|Andrew Milton]], à la poursuite du gang Van der Linde ; en 1907, il dirige le tout nouveau Bureau of Investigation. En 1911, il retient [[abigail-marston|Abigail]] et [[jack-marston|Jack Marston]] pour contraindre [[john-marston|John Marston]] à traquer ses anciens compagnons, puis mène l'assaut sur le ranch au cours duquel John est tué. En 1914, à la retraite, il meurt en duel face à Jack."),
        two("He is played by Jim Bentley in both games.",
            "Jim Bentley l'interprète dans les deux jeux."),
    ],
    "essentials": [
        two("In 1899 he works for the Pinkertons under [[andrew-milton|Andrew Milton]]. The two agents confront [[arthur-morgan|Arthur Morgan]] at the river in \"A Fisher of Men\" and the whole gang at Clemens Point in \"The Battle of Shady Belle\".",
            "En 1899, il travaille pour la Pinkerton sous les ordres d'[[andrew-milton|Andrew Milton]]. Les deux agents abordent [[arthur-morgan|Arthur Morgan]] au bord de la rivière dans \"A Fisher of Men\", puis toute la bande à Clemens Point dans \"The Battle of Shady Belle\"."),
        two("After Milton's death, he commands the Pinkertons who storm the camp at Beaver Hollow and orders Arthur and John taken dead or alive.",
            "Après la mort de Milton, il commande les Pinkerton qui donnent l'assaut au camp de Beaver Hollow et ordonne de prendre Arthur et John morts ou vifs."),
        two("In 1907, at the head of the Bureau of Investigation, he finds [[micah-bell|Micah Bell]]'s body with [[archer-fordham|Archer Fordham]] and traces the killer to [[john-marston|John Marston]] at Beecher's Hope.",
            "En 1907, à la tête du Bureau of Investigation, il découvre avec [[archer-fordham|Archer Fordham]] le corps de [[micah-bell|Micah Bell]] et remonte la piste du tueur jusqu'à [[john-marston|John Marston]], à Beecher's Hope."),
        two("In 1911 he holds John's wife and son until John has dealt with [[bill-williamson|Bill Williamson]], [[javier-escuella|Javier Escuella]] and [[dutch-van-der-linde|Dutch van der Linde]], then leads the soldiers and agents who kill John and [[uncle|Uncle]] at the ranch.",
            "En 1911, il retient la femme et le fils de John jusqu'à ce que celui-ci ait réglé le sort de [[bill-williamson|Bill Williamson]], de [[javier-escuella|Javier Escuella]] et de [[dutch-van-der-linde|Dutch van der Linde]], puis mène les soldats et les agents qui tuent John et [[uncle|Uncle]] au ranch."),
        two("Retired with medals by 1914, he is tracked down by [[jack-marston|Jack Marston]] while duck hunting by the San Luis River and killed in a duel.",
            "Retraité et couvert de médailles en 1914, il est retrouvé par [[jack-marston|Jack Marston]] alors qu'il chasse le canard au bord du San Luis, et tué en duel."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["john-marston", "jack-marston", "archer-fordham", "andrew-milton"],
}
