"""Andrew Milton, reference fiche, PART D: base data, Development and performance, Reception
(20 Oct 2026, medium tier).

His live page (characters/andrew-milton/) was generated from the v2 entry in scripts/_wave3.py
("slug": "andrew-milton"; no ENRICHED entry in _enrich.py, which only mentions him in Molly's entry).
The base below is rebuilt from that entry, with corrections: the v2 intro called him "Calm, relentless
and self-righteous" and "the human face of the law" (interpretation, dropped); the v2 biography said the
agents confront Arthur and Dutch "several times" (they meet Dutch once, at Clemens Point) and is replaced
by part A; the v2 personality and "Behind the scenes" lines ("more chilling than any hot-headed lawman",
"the recurring, patient antagonist") are dropped as unsourced; the v2 Leviticus Cornwall fiche in
_wave3.py says he dies "at Annesburg" in a confrontation with the gang (that sentence is about Cornwall,
not Milton, and is out of scope here). The "Deceased" chip duplicated "Died 1899" and is dropped; the
"Red Dead Redemption 2" chip is replaced by the actor; the facts grid gains Name, Alias, Born, Backer,
Partner and Played by. Eyebrow (kicker) kept as on the live page ("Character &middot; Pinkerton Agency");
reg_role matches characters_registry.py. publishDate 2026-07-11 kept (git: 1697169, drip publish of
andrew-milton, 11 Jul 2026; the live byline shows an older generator date, June 23, 2026).

Sources (internal register, fetched 20 Oct 2026):
- Red Dead Wiki "Andrew Milton" (infobox: voice John Hickok) and "John Hickok" (American actor, born
  August 31, 1957; "cast as the voice and motion-capture actor" for Milton; no other series credit).
  FR wiki infobox: acteur John Hickok. Wikipedia "List of Red Dead Redemption 2 characters" (Milton
  section: "Agent Andrew Milton (John Hickok)"; Roger Clark on Gamology, video of July 31, 2024, at 2:09:
  Hickok is related to Wild Bill Hickok; Robert Whitaker, "The Last Enemy That Shall Be Considered: Law
  and Order in Red Dead", in J. Wills and E. Wright (eds), Red Dead Redemption: History, Myth, and
  Violence in the Video Game West, University of Oklahoma Press, 30 Mar 2023, p. 68; Slate), saved in
  colm/m/wp_List_of_Red_Dead_Redemption_2_characters.txt. Whitaker's book and the Gamology video were not
  consulted directly: both are cited through Wikipedia, and the text says so.
- IMDb (nm1947605, search extract): born August 31, 1957; Red Dead Redemption II, Law & Order: Special
  Victims Unit, The Blacklist. IBDB (person 45085, search extract): Accomplice (1990, standby), Our
  Country's Good (1991), Parade (1998-1999, Governor Slaton), Aida (2000-2004, Zoser), Little Women (2005,
  Professor Bhaer, original cast per WCSU and Playbill), Man and Boy (2011, understudy). Western Connecticut State University, Theatre Arts
  faculty page (fetched): adjunct professor (performance techniques, Meisner, directing); "originated the
  roles of Governor Slaton in Parade, Zoser in Elton John's Aida"; guest roles on "all the Law & Orders",
  Blacklist, Body of Proof; "Most importantly, he plays the role of Agent Milton in Red Dead Redemption 2."
  No interview in which Hickok discusses the role was found.
- Slate, Rebecca Onion, "Who Were the Pinkertons?", February 1, 2019 (fetched): "Agent Milton is
  pockmarked and sinister, and the actor (John Hickok) delivers his lines in a hammed-up, insinuating
  tone"; the Lakay scene ("a serious arsenal that includes a Gatling gun"); "This historical scene at the
  James' farm is reminiscent of a battle between the Pinkertons and the Van der Linde gang in Red Dead 2.";
  the dispute (cease-and-desist in December 2018, Take-Two's suit of January 11, 2019, demand for
  royalties); Jack Zahran: "Is it open season on companies that have achieved longevity? What's next? A
  game where Coca-Cola poisons mankind?"
- Game Informer, Imran Khan, April 11, 2019, "Rockstar Drops Lawsuit Against Pinkertons" (fetched): the
  suit was voluntarily withdrawn on April 11, 2019; no settlement announced.
- TheGamer, Rafly Gilang, page on the real-life faces of RDR2's cast, updated March 11, 2021 (fetched):
  "John Hickok deserves credit for making the villain both hateable and menacing."
- WhatCulture, Matt Thompson, February 7, 2022, "Red Dead Redemption: Every Villain Ranked From Worst To
  Best" (fetched, page 12 of the slideshow): Milton 4th of 15; "he was just as lawless as the "savages" he
  seeks to hunt down"; "an argument could be made that he is the main villain".
Excluded: IMDb's and TheGamer's credit lists beyond what IBDB and WCSU confirm; the Wikipedia list's
"amnesty" wording for the Clemens Point offer (the transcript gives three days to flee if Dutch gives
himself up); Pinkerton's demand as reported by Game Informer (removal of the agency and halt of sales),
which differs from Slate's account (royalties): only Slate's version is given, attributed; the TV Tropes
"Hero Antagonist" reading (fan wiki); the wiki's Steve Haines comparison (wiki analysis); "Milton
Andrews" in the game files (owned by part B, Names); the 2015 Reddit leak about a Pinkerton spy (not
about Milton, unverifiable).
DUPLICATE ownership: actor, Broadway career and the Wild Bill Hickok remark live HERE; Slate's
description of Milton and the Pinkerton dispute live in Reception HERE (part C trivia must not repeat
them). Milton's appearance and names are in part B.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Andrew Milton is played by John Hickok, an American actor born on August 31, 1957. According to the Red Dead Wiki's page on Hickok, he was cast as both the voice and the motion-capture actor for the character. Wikipedia's list of the game's characters also credits him in the role. The wiki lists no other part for him in the series, and no interview in which Hickok discusses the role has been found.",
              "Andrew Milton est interprété par John Hickok, un acteur américain né le 31 août 1957. Selon la page du Red Dead Wiki consacrée à Hickok, l'acteur a été choisi à la fois pour la voix et pour la capture de mouvement du personnage. La liste des personnages du jeu sur Wikipédia le crédite aussi dans ce rôle. Le wiki ne lui connaît pas d'autre rôle dans la série, et aucun entretien où Hickok évoquerait ce personnage n'a été trouvé.")},
    {"h3": two("The actor", "L'acteur")},
    {"p": two("Hickok's career is mostly on stage. The Internet Broadway Database lists six Broadway productions between 1990 and 2011. He created the roles of Governor Slaton in the musical Parade (1998), Zoser in Elton John and Tim Rice's Aida (2000) and Professor Bhaer in the musical Little Women (2005). On television he has made guest appearances in the Law & Order series, The Blacklist and Body of Proof. He teaches performance and directing as an adjunct professor at Western Connecticut State University, whose faculty page says: \"Most importantly, he plays the role of Agent Milton in Red Dead Redemption 2.\"",
              "La carrière de Hickok s'est surtout faite sur scène. L'Internet Broadway Database recense six productions à Broadway entre 1990 et 2011. Il y a créé trois rôles : le gouverneur Slaton dans la comédie musicale Parade (1998), Zoser dans Aida, d'Elton John et Tim Rice (2000), et le professeur Bhaer dans la comédie musicale Little Women (2005). À la télévision, il a fait des apparitions dans les séries Law & Order, The Blacklist et Body of Proof. Il enseigne le jeu et la mise en scène comme professeur associé à la Western Connecticut State University, dont la page consacrée à ses enseignants précise : \"Most importantly, he plays the role of Agent Milton in Red Dead Redemption 2.\" (surtout, il joue le rôle de l'agent Milton dans Red Dead Redemption 2).")},
    {"p": two("Roger Clark, who plays Arthur Morgan, said in a video for the Gamology channel published on July 31, 2024 that Hickok is related to the frontier lawman Wild Bill Hickok, according to Wikipedia's list of the game's characters.",
              "Roger Clark, l'interprète d'Arthur Morgan, a affirmé dans une vidéo de la chaîne Gamology publiée le 31 juillet 2024 que Hickok est apparenté à Wild Bill Hickok, figure de la loi de l'Ouest, selon la liste des personnages du jeu sur Wikipédia.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("The Pinkertons on trial", "Les Pinkerton au tribunal")},
    {"p": two("The game's portrayal of the agency led to a legal dispute shortly after release. According to Slate (February 1, 2019), Pinkerton Consulting and Investigations, the company that now carries the name, sent Take-Two Interactive a cease-and-desist letter in December 2018 and asked for royalties for the use of its trademark. Take-Two filed suit on January 11, 2019, asking a court to confirm its right to depict the historical agency. Pinkerton's president, Jack Zahran, was quoted as asking: \"Is it open season on companies that have achieved longevity? What's next? A game where Coca-Cola poisons mankind?\" Game Informer reported on April 11, 2019 that Take-Two had voluntarily withdrawn its suit; no settlement was announced.",
              "La façon dont le jeu dépeint l'agence débouche sur un litige peu après la sortie. Selon Slate (1er février 2019), Pinkerton Consulting and Investigations, la société qui porte aujourd'hui ce nom, adresse à Take-Two Interactive une mise en demeure en décembre 2018 et réclame des redevances pour l'usage de sa marque. Take-Two saisit la justice le 11 janvier 2019 pour faire reconnaître son droit de représenter l'agence historique. Le président de Pinkerton, Jack Zahran, est cité en ces termes : \"Is it open season on companies that have achieved longevity? What's next? A game where Coca-Cola poisons mankind?\" (la chasse est-elle ouverte contre les entreprises qui ont su durer ? Et ensuite ? Un jeu où Coca-Cola empoisonne l'humanité ?). Game Informer annonce le 11 avril 2019 que Take-Two a retiré sa plainte de son plein gré ; aucun accord n'a été annoncé.")},
    {"h3": two("Assessments", "Regards critiques")},
    {"ul": [
        two("Slate, Rebecca Onion, February 1, 2019: \"Agent Milton is pockmarked and sinister, and the actor (John Hickok) delivers his lines in a hammed-up, insinuating tone.\" The article compares the attack on Lakay, with \"a serious arsenal that includes a Gatling gun\", to the Pinkertons' 1875 raid on the farm of Jesse James's family.",
            "Slate, Rebecca Onion, 1er février 2019 : \"Agent Milton is pockmarked and sinister, and the actor (John Hickok) delivers his lines in a hammed-up, insinuating tone.\" (l'agent Milton a le visage grêlé et l'air sinistre, et l'acteur, John Hickok, dit son texte sur un ton outré et insinuant). L'article rapproche l'attaque de Lakay, menée avec \"a serious arsenal that includes a Gatling gun\" (un sérieux arsenal, mitrailleuse Gatling comprise), du raid des Pinkerton de 1875 contre la ferme de la famille de Jesse James."),
        two("TheGamer, Rafly Gilang, article updated on March 11, 2021: in a feature on the real faces behind the cast, \"John Hickok deserves credit for making the villain both hateable and menacing.\"",
            "TheGamer, Rafly Gilang, article mis à jour le 11 mars 2021 : dans un dossier sur les vrais visages des interprètes, on lit que John Hickok mérite d'être salué pour avoir rendu ce méchant à la fois détestable et menaçant."),
        two("WhatCulture, Matt Thompson, February 7, 2022: Milton ranks fourth of fifteen villains of the series. Thompson writes that \"he was just as lawless as the 'savages' he seeks to hunt down\", and that an argument could be made that he is the main villain of the game.",
            "WhatCulture, Matt Thompson, 7 février 2022 : Milton se classe quatrième des quinze méchants de la série. Thompson écrit qu'il était \"just as lawless as the 'savages' he seeks to hunt down\" (tout aussi hors-la-loi que les sauvages qu'il entend traquer), et qu'on pourrait voir en lui le principal méchant du jeu."),
    ]},
    {"h3": two("Academic analysis", "Analyse universitaire")},
    {"p": two("In a chapter on law and order in the series, published on March 30, 2023 in the collection Red Dead Redemption: History, Myth, and Violence in the Video Game West (University of Oklahoma Press, edited by John Wills and Esther Wright), the historian Robert Whitaker links Milton's methods to those of the real agency. According to Wikipedia's list of the game's characters, he sees Milton's use of spying and infiltration as a reminder of real Pinkerton techniques, including the agency's role against the Molly Maguires, a secret society of Irish-American miners. Like Slate, he compares Milton's violence to the 1875 raid on the James farm, and also to the Homestead strike of 1892.",
              "Dans un chapitre consacré à la loi et à l'ordre dans la série, paru le 30 mars 2023 dans l'ouvrage collectif Red Dead Redemption: History, Myth, and Violence in the Video Game West (University of Oklahoma Press, sous la direction de John Wills et Esther Wright), l'historien Robert Whitaker rattache les méthodes de Milton à celles de l'agence réelle. D'après la liste des personnages du jeu sur Wikipédia, il voit dans le recours de Milton à l'espionnage et à l'infiltration un rappel des pratiques des vrais Pinkerton, notamment de leur action contre les Molly Maguires, une société secrète de mineurs irlando-américains. Comme Slate, il compare la violence de Milton au raid de 1875 contre la ferme des James, ainsi qu'à la grève de Homestead, en 1892.")},
]


BASE = {
    "slug": "andrew-milton", "name": "Andrew Milton",
    "publishDate": "2026-07-11", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Pinkerton agent &middot; RDR2", "reg_role_fr": "Agent Pinkerton &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": "American",
    "portrait_alt": two("Agent Andrew Milton in Red Dead Redemption 2", "L'agent Andrew Milton dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Pinkerton Agency", "Personnage &middot; Agence Pinkerton"),
    "meta_desc": two("Andrew Milton, the Pinkerton agent who hunts the Van der Linde gang in RDR2: the Clemens Point offer, Hosea's execution, Lakay, his death at Van Horn in 1899, John Hickok.",
                     "Andrew Milton, l'agent Pinkerton qui traque le gang Van der Linde dans RDR2 : l'offre de Clemens Point, l'exécution d'Hosea, Lakay, sa mort à Van Horn en 1899, John Hickok."),
    "og_desc": two("The complete reference on Andrew Milton: life, missions, quotes, development and reception.",
                   "La référence complète sur Andrew Milton : vie, missions, citations, conception et accueil."),
    "schema_desc": two("Pinkerton agent paid by Leviticus Cornwall to hunt the Van der Linde gang, who executes Hosea Matthews in Saint Denis and is shot dead by Abigail Marston at Van Horn in 1899, in Red Dead Redemption 2.",
                       "Agent de la Pinkerton payé par Leviticus Cornwall pour traquer le gang Van der Linde, qui exécute Hosea Matthews à Saint-Denis et meurt sous les balles d'Abigail Marston à Van Horn en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Pinkerton Agency", "Agence Pinkerton"),
              two("Hunts the Van der Linde gang", "Traque le gang Van der Linde"),
              two("Played by <strong>John Hickok</strong>", "Interprété par <strong>John Hickok</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Andrew Milton (first name given only in a 1907 newspaper and, according to the Red Dead Wiki, the ending credits)", "Andrew Milton (prénom donné seulement par un journal de 1907 et, selon le Red Dead Wiki, le générique de fin)")},
        {"label": two("Alias", "Surnom"), "value": two("Agent Milton; Agent Moron, for Dutch", "Agent Milton ; Agent Moron (agent Crétin), pour Dutch")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, at Van Horn Trading Post, shot by [[abigail-marston|Abigail Marston]] in \"Red Dead Redemption\"", "1899, à Van Horn Trading Post, abattu par [[abigail-marston|Abigail Marston]] dans \"Red Dead Redemption\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédé")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Pinkerton National Detective Agency, \"seconded to the United States Government\" in his own words. The Red Dead Wiki also lists the U.S. Marshals and the Blackwater Police Department", "Pinkerton National Detective Agency, \"seconded to the United States Government\" (détachée auprès du gouvernement des États-Unis), selon ses propres mots. Le Red Dead Wiki mentionne aussi les U.S. Marshals et la police de Blackwater")},
        {"label": two("Backer", "Commanditaire"), "value": two("[[leviticus-cornwall|Leviticus Cornwall]]", "[[leviticus-cornwall|Leviticus Cornwall]]")},
        {"label": two("Partner", "Coéquipier"), "value": two("[[edgar-ross|Edgar Ross]], his protégé", "[[edgar-ross|Edgar Ross]], son protégé")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("John Hickok", "John Hickok")},
    ],
    "intro": [
        two("Andrew Milton is a Pinkerton agent and one of the antagonists of Red Dead Redemption 2 (2018), set in 1899. Paid by the industrialist [[leviticus-cornwall|Leviticus Cornwall]], whose train the gang robbed, he hunts the Van der Linde gang with his partner [[edgar-ross|Edgar Ross]]. In chapter 2 he approaches [[arthur-morgan|Arthur Morgan]] by a river and asks him to hand over [[dutch-van-der-linde|Dutch van der Linde]]. In chapter 3 he walks into the camp at Clemens Point and offers the others three days to flee if Dutch gives himself up. In chapter 4 he kills [[hosea-matthews|Hosea Matthews]] in front of the bank in Saint Denis. In chapter 6 his men seize [[abigail-marston|Abigail Marston]]; at Van Horn he tells Arthur that [[micah-bell|Micah Bell]] is his informant, just before Abigail shoots him dead.",
            "Andrew Milton est un agent de la Pinkerton et l'un des antagonistes de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Payé par l'industriel [[leviticus-cornwall|Leviticus Cornwall]], dont la bande a attaqué le train, il traque le gang Van der Linde avec son coéquipier [[edgar-ross|Edgar Ross]]. Au chapitre 2, il aborde [[arthur-morgan|Arthur Morgan]] au bord d'une rivière et lui demande de livrer [[dutch-van-der-linde|Dutch van der Linde]]. Au chapitre 3, il entre dans le camp de Clemens Point et propose aux autres trois jours pour disparaître si Dutch se rend. Au chapitre 4, il abat [[hosea-matthews|Hosea Matthews]] devant la banque de Saint-Denis. Au chapitre 6, ses hommes s'emparent d'[[abigail-marston|Abigail Marston]] ; à Van Horn, il révèle à Arthur que [[micah-bell|Micah Bell]] est son informateur, juste avant qu'Abigail ne l'abatte."),
        two("He is played by John Hickok.",
            "Il est interprété par John Hickok."),
    ],
    "essentials": [
        two("In \"A Fisher of Men\", he finds [[arthur-morgan|Arthur]] fishing with [[jack-marston|Jack Marston]] and offers him his life in exchange for Dutch; he also tells him that he killed Mac Callander.",
            "Dans \"A Fisher of Men\", il trouve [[arthur-morgan|Arthur]] en train de pêcher avec [[jack-marston|Jack Marston]] et lui offre la vie sauve en échange de Dutch ; il lui apprend aussi qu'il a tué Mac Callander."),
        two("In \"The Battle of Shady Belle\", he gives the gang three days to disappear if [[dutch-van-der-linde|Dutch]] surrenders; Dutch refuses, and Milton promises to come back with fifty men.",
            "Dans \"The Battle of Shady Belle\", il laisse à la bande trois jours pour disparaître si [[dutch-van-der-linde|Dutch]] se rend ; Dutch refuse, et Milton promet de revenir avec cinquante hommes."),
        two("In \"Banking, The Old American Art\", he catches [[hosea-matthews|Hosea]] during the diversion and shoots him in the street; in \"Fleeting Joy\", his agents attack Lakay with a machine gun.",
            "Dans \"Banking, The Old American Art\", il capture [[hosea-matthews|Hosea]] pendant la diversion et l'abat en pleine rue ; dans \"Fleeting Joy\", ses agents attaquent Lakay à la mitrailleuse."),
        two("In \"Red Dead Redemption\", he holds [[abigail-marston|Abigail]] at Van Horn, names [[micah-bell|Micah]] as the gang's informant and says [[molly-oshea|Molly O'Shea]] never talked; Abigail kills him with [[sadie-adler|Sadie]]'s revolver.",
            "Dans \"Red Dead Redemption\", il retient [[abigail-marston|Abigail]] à Van Horn, désigne [[micah-bell|Micah]] comme l'informateur de la bande et affirme que [[molly-oshea|Molly O'Shea]] n'a jamais parlé ; Abigail l'abat avec le revolver de [[sadie-adler|Sadie]]."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["dutch-van-der-linde", "arthur-morgan", "hosea-matthews", "edgar-ross"],
}
