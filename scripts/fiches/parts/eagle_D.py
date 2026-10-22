"""Eagle Flies, reference fiche, PART D: base data, Development and performance, Reception
(22 Oct 2026, medium tier).

His page is still queued (_queue/49-eagle-flies/), generated from the v2 entry in scripts/_wave7.py ("slug":
"eagle-flies", order 49; no entry in _enrich.py). publishDate 2026-10-26 kept. The base below is rebuilt from that
entry, with corrections:
- v2 intro: "His elder brother and his mother were killed by US soldiers". The only in-game source is his father's
  speech in "My Last Boy" (gsw l. 13111): the elder brother "had his head smashed by a drunken soldier", the wife "had her
  throat slit" (killer not named). Now worded from that speech (the wiki's "by the U.S. Army" is not used for the mother).
- v2 "Dutch crashes it, and the horses swim back to shore": the transcript has the boat run onto rocks and the men ride
  the horses ashore (gsw l. 12270-12278; dutch_D). Left to part A; the essentials say "take them back from an Army boat".
- v2 "dies in Rains Fall's arms": the transcript stage note says his father takes him by the hand; now "dies in his
  father's tent on the reservation" (HOUSE_FACTS wording).
- v2 Biography h3 "Chapter 4: Cornwall's refinery": kept as fact (American Fathers I and II = chapter 4, mission pages).
- v2 "Behind the scenes": Jeremiah Bitsui, "a Navajo actor also of Omaha descent": confirmed by Wikipedia; now with the
  voice AND motion capture credit and the three-year figure, both sourced.
- v2 og_desc ("chooses war ... dies saving Arthur Morgan") replaced by the house formula; schema_desc expanded.
- chips: "Wapiti", "Warrior", "RDR2" replaced by Son of Rains Fall / Died 1899 / Played by; facts grid rebuilt.
Eyebrow kept as on the queued page ("Character &middot; Wapiti"); reg_role matches characters_registry.py ("Wapiti
warrior &middot; RDR2"). Links: only fiches live on or before 2026-10-26 (rains-fall, published 2026-10-23, is allowed;
never sister-calderon, published 2026-10-29; never eagle-flies itself).

SOURCE REGISTER (fetched 22 Oct 2026, copies in scripts/v3/work/eagle/fc/ where noted):
- Wikipedia "Jeremiah Bitsui": Navajo and of Omaha descent, born in Chinle, Arizona (1979 or 1980); "voice role and
  motion capture performance as the character Eagle Flies"; Natural Born Killers (1994), Victor in Breaking Bad
  (2009-2011) and Better Call Saul (2017-2022), Bosch (2019-2020), Dark Winds (2022).
- Wikipedia "List of Red Dead Redemption 2 characters" (scripts/v3/work/catherine/fc/wp_list_rdr2.txt): Eagle Flies
  (Jeremiah Bitsui); "Bitsui worked on the game for about three years", citing "Jeremiah Bitsui talks Breaking Bad, Red
  Dead Redemption 2 & New Baby", The Colt Balok Show (YouTube), 31 Oct 2018. Video not watched: attributed through
  Wikipedia. Same figure on the Red Dead Wiki page "Jeremiah Bitsui" (_m/Jeremiah_Bitsui.txt).
- IGN, Jared Petty, "How Historically Accurate is Red Dead Redemption 2?", posted 24 Dec 2018 (archived copy,
  fc/ign_petty_2018-12-24.txt): quotes checked verbatim.
- Andrei Nae (University of Bucharest), "The Frontier as American National Identity Narrative in the Red Dead Redemption
  Games", American, British and Canadian Studies, 2025 (DOI 10.2478/abcsj-2025-0014; scripts/v3/work/rains/fc/abcsj.txt):
  quotes checked against the text.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (_m/Red_Dead_Redemption_2_Cut_Content.txt): ntv0 mission (same
  wording as charles_D, authoritative), alternate trailer appearance in his final mission, unused eye caps.
- Fan transcript (fc/gsw.txt, gitignored) for the base facts (father's speech, Fort Wallace, refinery, tent).
Searched without result: a written interview in which Bitsui discusses the role; an official Rockstar description.

Excluded: Bitsui's exact birth date (Wikipedia gives 1979 or 1980, the Red Dead Wiki 25 Sep 1980: not needed); his role
name in Dark Winds (not checked); the Wikipedia list's "while trying to rescue his friend Paytah, Eagle Flies is
captured" (summary; part A owns the capture); the RDR2.org character page (fan site, nothing beyond the wiki); the
wiki's Nastas comparison (interpretation). DUPLICATE ownership: actor, cut content and reviews live HERE; Rains Fall's
fiche (rains_D) already quotes Nae's sentence contrasting father and son and Polygon's review: not repeated here.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Eagle Flies is played by Jeremiah Bitsui, a Navajo actor of Omaha descent born in Chinle, Arizona. Wikipedia credits Bitsui with both the voice and the motion capture of the character. Bitsui is best known as Victor, the henchman he played in Breaking Bad (2009-2011) and again in Better Call Saul (2017-2022). His other roles include a child part in Natural Born Killers (1994), the series Bosch (2019-2020) and Dark Winds (2022). Wikipedia's list of the game's characters states that he worked on Red Dead Redemption 2 for about three years, citing an interview he gave to The Colt Balok Show on October 31, 2018, a few days after the game's release.",
              "Eagle Flies est interprété par Jeremiah Bitsui, acteur navajo d'ascendance omaha, né à Chinle, en Arizona. Wikipédia lui attribue à la fois la voix et la capture de mouvement du personnage. Bitsui est surtout connu pour Victor, l'homme de main qu'il a joué dans Breaking Bad (2009-2011) puis dans Better Call Saul (2017-2022). On l'a vu aussi enfant dans Tueurs nés (Natural Born Killers, 1994), puis dans les séries Bosch (2019-2020) et Dark Winds (2022). Selon la liste des personnages du jeu publiée sur Wikipédia, il a travaillé environ trois ans sur Red Dead Redemption 2, d'après un entretien accordé à l'émission The Colt Balok Show le 31 octobre 2018, quelques jours après la sortie du jeu.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("According to the Red Dead Wiki's page on cut content, the files hold an unfinished chapter 4 mission, labelled \"ntv0\", in which Arthur, Charles and Eagle Flies were to ambush an army convoy carrying Native American children to a boarding school. Its surviving animations show a Native American pleading for his life because he has a family, and a soldier who claims he only obeyed orders and tries to kill him. The opening dialogue between Arthur and Charles survives in a shorter form, as the rare chapter 4 camp scene described under Relationships. The same page notes that the game's trailer showed Eagle Flies with a different appearance in his final mission, and that unused eye models for him remain in the files.",
              "D'après la page du Red Dead Wiki consacrée au contenu coupé, les fichiers contiennent une mission inachevée du chapitre 4, baptisée \"ntv0\", dans laquelle Arthur, Charles et Eagle Flies devaient tendre une embuscade à un convoi de l'armée conduisant des enfants amérindiens vers un pensionnat. Les animations conservées montrent un Amérindien qui implore qu'on l'épargne parce qu'il a une famille, et un soldat qui affirme n'avoir fait qu'obéir aux ordres avant de tenter de le tuer. Le dialogue d'ouverture entre Arthur et Charles subsiste sous une forme raccourcie : c'est la scène de camp, rare, du chapitre 4 évoquée dans la partie Relations. La même page relève que la bande-annonce du jeu montrait Eagle Flies avec une autre apparence dans sa dernière mission, et que des modèles d'yeux inutilisés subsistent pour lui dans les fichiers.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Critics and scholars", "Critiques et chercheurs")},
    {"p": two("In an IGN feature on the game's historical accuracy, posted on December 24, 2018, Jared Petty compared the Wapiti storyline to the seizure of the Black Hills in the 1870s and to the treatment of the Osage in the 1920s. He summarized Eagle Flies's arc in these terms: he \"comes to believe that the situation is simply too impossible for peace to accomplish anything and declares war on the invading army forces, against the wishes of his father\", coaxed by Dutch. Petty added that \"Young warriors following their passionate, angry peer against the wishes of an authority figure is another common theme in American tribal culture\", since chiefs often led by reputation rather than by legal power.",
              "Dans un dossier d'IGN sur la vraisemblance historique du jeu, publié le 24 décembre 2018, Jared Petty rapproche l'intrigue des Wapiti de la saisie des Black Hills dans les années 1870 et du sort réservé aux Osages dans les années 1920. Il résume ainsi le parcours d'Eagle Flies : il \"comes to believe that the situation is simply too impossible for peace to accomplish anything and declares war on the invading army forces, against the wishes of his father\" (finit par juger la situation trop désespérée pour que la paix serve à quoi que ce soit, et déclare la guerre à l'armée d'invasion contre l'avis de son père), poussé par Dutch. Petty ajoute que \"Young warriors following their passionate, angry peer against the wishes of an authority figure is another common theme in American tribal culture\" (de jeunes guerriers qui suivent l'un des leurs, fougueux et en colère, contre l'avis d'une autorité, c'est un autre thème fréquent de la culture tribale américaine), les chefs tirant souvent leur autorité de leur réputation plus que d'un pouvoir légal.")},
    {"p": two("In an article published in 2025 in the journal American, British and Canadian Studies, Andrei Nae of the University of Bucharest counts Eagle Flies among the three Native American characters who matter to the game's story and play, with Rains Fall and Charles Smith. He writes that Eagle Flies \"advocates for violent resistance and often engages in violent action against the government and capitalist interests\", that Arthur's task is \"to rein in the violent impulses of the young Native American\", and that \"The narrative arc of Eagle Flies is a cautionary tale warning against Native Americans using violence\" in a game whose mechanics are defined by violence.",
              "Dans un article paru en 2025 dans la revue American, British and Canadian Studies, Andrei Nae, de l'université de Bucarest, range Eagle Flies parmi les trois personnages amérindiens qui comptent dans l'histoire et le jeu, avec Rains Fall et Charles Smith. Selon lui, Eagle Flies \"advocates for violent resistance and often engages in violent action against the government and capitalist interests\" (prône la résistance armée et passe souvent à l'action violente contre le gouvernement et les intérêts capitalistes), la tâche d'Arthur consiste \"to rein in the violent impulses of the young Native American\" (à brider les élans violents du jeune Amérindien), et \"The narrative arc of Eagle Flies is a cautionary tale warning against Native Americans using violence\" (le parcours d'Eagle Flies est une mise en garde contre le recours des Amérindiens à la violence), dans un jeu dont les mécaniques reposent sur la violence.")},
]


BASE = {
    "slug": "eagle-flies", "name": "Eagle Flies",
    "publishDate": "2026-10-26", "updated": "2026-10-22", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Wapiti warrior &middot; RDR2", "reg_role_fr": "Guerrier wapiti &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": None,
    "portrait_alt": two("Eagle Flies outside the courthouse in Saint Denis in Red Dead Redemption 2",
                        "Eagle Flies devant le palais de justice de Saint-Denis dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Wapiti", "Personnage &middot; Wapiti"),
    "meta_desc": two("Eagle Flies, son of the Wapiti chief Rains Fall in RDR2: the Cornwall refinery, the horse raid, Fort Wallace, his death after the battle at the oil fields, Jeremiah Bitsui.",
                     "Eagle Flies, fils du chef wapiti Rains Fall dans RDR2 : la raffinerie de Cornwall, le raid sur les chevaux, Fort Wallace, sa mort après la bataille des champs pétrolifères, Jeremiah Bitsui."),
    "og_desc": two("The complete reference on Eagle Flies: life, quotes, relationships, development and reception.",
                   "La référence complète sur Eagle Flies : vie, citations, relations, conception et accueil."),
    "schema_desc": two("Son of Rains Fall, chief of the Wapiti, a fictional Native American people, who helps Arthur Morgan steal proof from Cornwall's refinery, chooses armed resistance against the Army in 1899 with the encouragement of Dutch van der Linde, and dies of a wound received at the Heartland Oil Fields, in Red Dead Redemption 2.",
                       "Fils de Rains Fall, chef des Wapiti, peuple amérindien fictif, qui aide Arthur Morgan à voler des preuves dans la raffinerie de Cornwall, choisit en 1899 la lutte armée contre l'armée avec les encouragements de Dutch van der Linde, et meurt d'une blessure reçue aux Heartland Oil Fields, dans Red Dead Redemption 2."),
    "chips": [two("Son of Rains Fall", "Fils de Rains Fall"), two("Died in <strong>1899</strong>", "Mort en <strong>1899</strong>"),
              two("Played by <strong>Jeremiah Bitsui</strong>", "Interprété par <strong>Jeremiah Bitsui</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Eagle Flies (his English name)", "Eagle Flies (son nom en anglais)")},
        {"label": two("Aliases", "Surnoms"), "value": two("The impetuous Prince (his father)", "The impetuous Prince, le prince impétueux (son père)")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, Wapiti Indian Reservation (shot by Colonel Favours at the Heartland Oil Fields)", "1899, réserve indienne wapiti (touché par le colonel Favours aux Heartland Oil Fields)")},
        {"label": two("People", "Peuple"), "value": two("Wapiti", "Wapiti")},
        {"label": two("Residence", "Résidence"), "value": two("Wapiti Indian Reservation, Ambarino", "Réserve indienne wapiti, Ambarino")},
        {"label": two("Family", "Famille"), "value": two("[[rains-fall|Rains Fall]] (father); an elder brother and his mother (killed; the brother by a drunken soldier, by his father's account)", "[[rains-fall|Rains Fall]] (père) ; un frère aîné et sa mère (tués ; le frère par un soldat ivre, selon son père)")},
        {"label": two("Allies", "Alliés"), "value": two("Paytah, [[arthur-morgan|Arthur Morgan]], [[charles-smith|Charles Smith]], [[dutch-van-der-linde|Dutch van der Linde]]", "Paytah, [[arthur-morgan|Arthur Morgan]], [[charles-smith|Charles Smith]], [[dutch-van-der-linde|Dutch van der Linde]]")},
        {"label": two("Adversaries", "Adversaires"), "value": two("Colonel Henry Favours and the Army at Fort Wallace", "Le colonel Henry Favours et l'armée de Fort Wallace")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Played by", "Interprète"), "value": two("Jeremiah Bitsui", "Jeremiah Bitsui")},
    ],
    "intro": [
        two("Eagle Flies is the son of [[rains-fall|Rains Fall]], chief of the Wapiti, a fictional Native American people, in Red Dead Redemption 2 (2018), set in 1899. His elder brother and his mother were killed before the story begins. Where his father seeks a peaceful settlement over the tribe's reservation, Eagle Flies predicts war and wants to fight the Army. In 1899 he helps [[arthur-morgan|Arthur Morgan]] steal a report on the oil under the reservation from the Cornwall refinery, then turns to raids against the Army with the support of [[dutch-van-der-linde|Dutch van der Linde]], who sees in the conflict a distraction for the gang.",
            "Eagle Flies est le fils de [[rains-fall|Rains Fall]], chef des Wapiti, un peuple amérindien fictif, dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Son frère aîné et sa mère ont été tués avant le début de l'histoire. Là où son père cherche un règlement pacifique au sujet de la réserve de la tribu, Eagle Flies annonce la guerre et veut combattre l'armée. En 1899, il aide [[arthur-morgan|Arthur Morgan]] à voler dans la raffinerie de Cornwall un rapport sur le pétrole de la réserve, puis se lance dans des raids contre l'armée avec l'appui de [[dutch-van-der-linde|Dutch van der Linde]], qui voit dans ce conflit une diversion pour le gang."),
        two("Captured after an ambush on an Army patrol, he is freed from Fort Wallace by Arthur and [[charles-smith|Charles Smith]]. He then leads an attack on the Heartland Oil Fields against his father's wishes, saves Arthur there and is shot by Colonel Henry Favours; he dies in his father's tent on the reservation. Eagle Flies is played by Jeremiah Bitsui.",
            "Capturé après une embuscade contre une patrouille de l'armée, il est libéré de Fort Wallace par Arthur et [[charles-smith|Charles Smith]]. Il mène ensuite une attaque contre les Heartland Oil Fields malgré l'opposition de son père, y sauve Arthur et reçoit une balle du colonel Henry Favours ; il meurt sous la tente de son père, sur la réserve. Eagle Flies est interprété par Jeremiah Bitsui."),
    ],
    "essentials": [
        two("In \"American Fathers I\", he meets [[arthur-morgan|Arthur]] outside the Saint Denis courthouse with his father; in \"American Fathers II\" he guides Arthur into the Cornwall Kerosene & Tar refinery to steal the Leland Oil Development Company report, and pays him.",
            "Dans \"American Fathers I\", il rencontre [[arthur-morgan|Arthur]] avec son père devant le palais de justice de Saint-Denis ; dans \"American Fathers II\", il guide Arthur jusqu'à la raffinerie Cornwall Kerosene & Tar pour y voler le rapport de la Leland Oil Development Company, puis le paie."),
        two("In \"A Rage Unleashed\", he asks the gang for help after the Army seizes the tribe's horses; with [[dutch-van-der-linde|Dutch]], Arthur, [[charles-smith|Charles]] and Paytah he takes them back from an Army boat near Van Horn.",
            "Dans \"A Rage Unleashed\", il demande l'aide du gang après la saisie des chevaux de la tribu par l'armée ; avec [[dutch-van-der-linde|Dutch]], Arthur, [[charles-smith|Charles]] et Paytah, il les reprend sur un bateau de l'armée près de Van Horn."),
        two("In \"Favored Sons\", an ambush on an Army patrol in Cumberland Forest ends in a battle and his capture; in \"The King's Son\", Arthur and Charles free him from Fort Wallace.",
            "Dans \"Favored Sons\", une embuscade contre une patrouille de l'armée dans la forêt de Cumberland tourne à la bataille et se termine par sa capture ; dans \"The King's Son\", Arthur et Charles le libèrent de Fort Wallace."),
        two("In \"My Last Boy\", he ignores his father's plea and leads the attack on the Heartland Oil Fields; he saves Arthur, is shot by Colonel Favours, and dies in his father's tent on the reservation.",
            "Dans \"My Last Boy\", il passe outre la supplique de son père et mène l'attaque des Heartland Oil Fields ; il sauve Arthur, reçoit une balle du colonel Favours et meurt sous la tente de son père, sur la réserve."),
        two("He is played by Jeremiah Bitsui, known for the role of Victor in Breaking Bad, who provided his voice and motion capture.",
            "Il est interprété par Jeremiah Bitsui, connu pour le rôle de Victor dans Breaking Bad, qui lui prête sa voix et ses mouvements."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["rains-fall", "charles-smith", "arthur-morgan", "dutch-van-der-linde"],
}
