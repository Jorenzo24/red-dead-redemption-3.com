"""Leviticus Cornwall, reference fiche, PART D: base data, Development and performance, Reception
(20 Oct 2026, medium tier).

His live page (characters/leviticus-cornwall/) was generated from the v2 entry in scripts/_wave3.py
("slug": "leviticus-cornwall"; no entry in _enrich.py). The base below is rebuilt from that entry, with
corrections: the v2 intro called him "a symbol of the industrial age closing in on the outlaw way of life"
(interpretation, dropped) and said the gang "attacks his oil interests" before he hires the Pinkertons
(wrong order: the Pinkertons are on the gang's trail from chapter 2; the refinery is entered in chapter 4);
the v2 text said the Pinkertons were "led by Agent Milton" on his money and that he regards the gang "as
vermin" (unsupported wording, dropped); the "Deceased" chip duplicated "Died 1899" and is dropped; the
facts grid gains Born, Aliases, Occupation, Companies, Games and Played by. Eyebrow (kicker) kept as on the
live page ("Character &middot; Red Dead Redemption 2"); reg_role matches characters_registry.py.
publishDate 2026-07-10 kept (git: f3512f4, drip publish of leviticus-cornwall, 10 Jul 2026; the live
byline shows an older generator date).

Sources (internal register, fetched 20 Oct 2026):
- Red Dead Wiki "Leviticus Cornwall" (infobox: voice John Rue) and "John Rue" (stub: American actor who
  voiced Cornwall; other credits The Departed, Bridge of Spies, The Post, via IMDb links). Wikipedia "List of
  Red Dead Redemption 2 characters", Cornwall section, credits John Rue (saved in leviticus/m/wp_List_...).
  No interview in which Rue discusses the role was found (web search, 20 Oct 2026); IMDb not fetched.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (saved fcb/cut.txt): Senor Andreas Colon, a cut
  Guarma character, uses face textures similar to Cornwall's; cut mission "ind2" with dynamite under the
  Cornwall Freight and Commodities building (already told in abigail_D and micah_D, same wording checked);
  concept art file for "Who the Hell is Leviticus Cornwall?"; unused vest and hair for the conductor of
  Cornwall's train.
- IGN, Jared Petty, "How Historically Accurate is Red Dead Redemption 2?", 24 Dec 2018 (archived copy of
  24 Dec 2018 fetched with curl, fcb/ign.html): "Business interests in the era made liberal use of private
  agents and gun thugs in enforcing their will, just as Leviticus Cornwall does in the pursuit of Dutch's
  gang."; "Leviticus Cornwall is a parodic caricature of the captains of industry that effectively ruled
  much of the United States during this period, men like J.P. Morgan, Andrew Carnegie, and George
  Vanderbilt".
- Hilary Jane Locke and Thomas Ashley Mackay, "'You Are a True Progressive': Red Dead Redemption 2 and the
  Depiction and Reception of Progressive Era Politics", The Journal of the Gilded Age and Progressive Era,
  vol. 20, no. 1 (January 2021; online 4 Dec 2020), pp. 174-193 (Crossref metadata and abstract fetched;
  full text paywalled). Their reading of Cornwall (metaphor for American capitalism, resemblance to robber
  barons such as Morgan and Rockefeller, p. 185) is given as Wikipedia's summary, attributed. The article's
  notes (visible on Cambridge Core) cite the strike mentioned just before Dutch kills Cornwall.
Excluded: the Red Dead Wiki's composite-character trivia (Carnegie, Stanford, Vanderbilt, Rockefeller,
Harriman and the Wild Bunch: no source given); Rue's motion capture (no source: the wiki and Wikipedia say
only voice / role); Rue's nationality as a fact in the intro (wiki stub only, kept attributed in Development);
Senor Andreas Colon's hat, hair and trousers and the cut bounty missions near the refinery (not about
Cornwall); the "Leviticus" irony (interpretation).
Fact-check fixes (20 Oct 2026): facts label "Nicknames" (insults, not aliases); lead says he imports sugar (no "owns a
sugar trade"); casting "only role" attributed to the wiki; concept art shown on the cut-content page, not said to be in
the files.
DUPLICATE ownership: actor, cut content and the real-world comparisons (IGN, Locke and Mackay) live HERE;
part C trivia must not repeat them. The name's biblical meaning is in part B Names.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Leviticus Cornwall appears only in Red Dead Redemption 2 (2018). He is played by John Rue, who is credited in the role by the Red Dead Wiki and by Wikipedia's list of the game's characters. The wiki describes Rue as an American actor and lists The Departed, Bridge of Spies and The Post among his screen credits. The Red Dead Wiki lists Cornwall as his only role in the series, and no interview in which Rue discusses the role has been found.",
              "Leviticus Cornwall n'apparaît que dans Red Dead Redemption 2 (2018). Il est interprété par John Rue, que le Red Dead Wiki et la liste des personnages du jeu sur Wikipédia créditent dans ce rôle. Le wiki présente Rue comme un acteur américain et cite parmi ses rôles au cinéma Les Infiltrés, Le Pont des espions et Pentagon Papers. Le Red Dead Wiki ne lui connaît pas d'autre rôle dans la série, et aucun entretien où Rue évoquerait ce personnage n'a été trouvé.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The game files keep a few traces of unused material around Cornwall, according to the Red Dead Wiki's page on cut content. A cut Guarma character named Señor Andreas Colon, who would have given missions to the player, shares face textures close to Cornwall's. A cut mission labeled \"ind2\" would have had Arthur plant dynamite under the Cornwall Freight and Commodities building in Saint Denis. The same page also shows concept art for \"Who the Hell is Leviticus Cornwall?\" and lists an unused vest and hairstyle for the conductor of Cornwall's train.",
              "Les fichiers du jeu gardent quelques traces de contenu inutilisé autour de Cornwall, d'après la page du Red Dead Wiki consacrée au contenu coupé. Un personnage coupé de Guarma, Señor Andreas Colon, qui aurait confié des missions au joueur, utilise des textures de visage proches de celles de Cornwall. Une mission coupée, baptisée \"ind2\", devait faire poser par Arthur de la dynamite sous le bâtiment de Cornwall Freight and Commodities, à Saint-Denis. La même page montre aussi un dessin préparatoire pour \"Who the Hell is Leviticus Cornwall?\" et recense un gilet et une coiffure inutilisés pour le chef de train de Cornwall.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("A robber baron on screen", "Un baron voleur à l'écran")},
    {"p": two("IGN's Jared Petty discussed Cornwall in an article on the game's historical accuracy published on 24 December 2018. He wrote that business interests of the era made heavy use of private agents and hired guns, \"just as Leviticus Cornwall does in the pursuit of Dutch's gang\". He called Cornwall \"a parodic caricature of the captains of industry\" of the period, naming J.P. Morgan, Andrew Carnegie and George Vanderbilt. Petty linked their power to industries ranging from oil and coal to Caribbean sugar.",
              "Jared Petty, d'IGN, évoque Cornwall dans un article sur l'exactitude historique du jeu publié le 24 décembre 2018. Il rappelle que les milieux d'affaires de l'époque recouraient largement à des agents privés et à des hommes de main, \"just as Leviticus Cornwall does in the pursuit of Dutch's gang\" (exactement comme Leviticus Cornwall dans sa traque du gang de Dutch). Il qualifie Cornwall de \"parodic caricature of the captains of industry\" (caricature parodique des capitaines d'industrie) de cette période, en citant J.P. Morgan, Andrew Carnegie et George Vanderbilt. Petty rattache leur pouvoir à des secteurs allant du pétrole et du charbon au sucre des Caraïbes.")},
    {"p": two("The scholars Hilary Jane Locke and Thomas Ashley Mackay studied the game's depiction of Progressive Era politics in The Journal of the Gilded Age and Progressive Era (Cambridge University Press, vol. 20, January 2021). According to Wikipedia's summary of their article, they read Cornwall as a metaphor for American capitalism and noted his resemblance to robber barons such as J.P. Morgan and John D. Rockefeller. Their notes point out that a strike is mentioned just before Dutch kills him.",
              "Les universitaires Hilary Jane Locke et Thomas Ashley Mackay ont étudié la manière dont le jeu dépeint la politique de l'ère progressiste dans The Journal of the Gilded Age and Progressive Era (Cambridge University Press, vol. 20, janvier 2021). Selon le résumé qu'en donne Wikipédia, ils voient en Cornwall une métaphore du capitalisme américain et relèvent sa ressemblance avec des barons voleurs comme J.P. Morgan et John D. Rockefeller. Leurs notes soulignent qu'une grève est évoquée juste avant que Dutch ne le tue.")},
]


BASE = {
    "slug": "leviticus-cornwall", "name": "Leviticus Cornwall",
    "publishDate": "2026-07-10", "updated": "2026-10-20", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Industrialist &middot; RDR2", "reg_role_fr": "Industriel &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": "American",
    "portrait_alt": two("Leviticus Cornwall in Red Dead Redemption 2", "Leviticus Cornwall dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Red Dead Redemption 2", "Personnage &middot; Red Dead Redemption 2"),
    "meta_desc": two("Leviticus Cornwall, the railroad, oil and sugar magnate of RDR2: the train robbery, the Valentine ambush, the Pinkertons he pays, his death in Annesburg in 1899, John Rue.",
                     "Leviticus Cornwall, magnat du rail, du pétrole et du sucre dans RDR2 : le train dévalisé, l'embuscade de Valentine, les Pinkerton qu'il paie, sa mort à Annesburg en 1899, John Rue."),
    "og_desc": two("The complete reference on Leviticus Cornwall: life, business empire, quotes, development and reception.",
                   "La référence complète sur Leviticus Cornwall : vie, empire industriel, citations, conception et accueil."),
    "schema_desc": two("Industrialist who owns railroads, an oil refinery and sugar interests, pays the Pinkertons to hunt the Van der Linde gang after it robs his train, and is shot dead by Dutch van der Linde in Annesburg in 1899, in Red Dead Redemption 2.",
                       "Industriel à la tête de chemins de fer, d'une raffinerie de pétrole et d'un commerce de sucre, qui paie les Pinkerton pour traquer le gang Van der Linde après le vol de son train, et que Dutch van der Linde abat à Annesburg en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Industrialist", "Industriel"),
              two("Cornwall Kerosene &amp; Tar", "Cornwall Kerosene &amp; Tar"),
              two("Played by <strong>John Rue</strong>", "Interprété par <strong>John Rue</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Leviticus Cornwall", "Leviticus Cornwall")},
        {"label": two("Nicknames", "Surnoms"), "value": two("Horse's Ass (Henri Lemieux) and Gilded Ape (Arthur Morgan), according to the Red Dead Wiki", "Horse's Ass (Henri Lemieux) et Gilded Ape (Arthur Morgan), selon le Red Dead Wiki")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, shot by [[dutch-van-der-linde|Dutch van der Linde]] in Annesburg in \"Just a Social Call\"", "1899, abattu par [[dutch-van-der-linde|Dutch van der Linde]] à Annesburg dans \"Just a Social Call\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédé")},
        {"label": two("Nationality", "Nationalité"), "value": two("American", "Américaine")},
        {"label": two("Occupation", "Activité"), "value": two("Industrialist: railroads, oil, freight and sugar", "Industriel : chemin de fer, pétrole, fret et sucre")},
        {"label": two("Companies", "Sociétés"), "value": two("Cornwall Kerosene &amp; Tar, Southern &amp; Eastern Railway, Cornwall City Railway, Cornwall Freight &amp; Commodities; a stake in the Annesburg coal mine", "Cornwall Kerosene &amp; Tar, Southern &amp; Eastern Railway, Cornwall City Railway, Cornwall Freight &amp; Commodities ; une part de la mine de charbon d'Annesburg")},
        {"label": two("Allies", "Alliés"), "value": two("The Pinkerton Agency, which he pays to hunt the gang; [[alberto-fussar|Alberto Fussar]], his sugar partner", "L'agence Pinkerton, qu'il paie pour traquer le gang ; [[alberto-fussar|Alberto Fussar]], son partenaire dans le sucre")},
        {"label": two("Enemy", "Ennemi"), "value": two("The Van der Linde gang", "Le gang Van der Linde")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2 (mentioned in Red Dead Online)", "Red Dead Redemption 2 (mentionné dans Red Dead Online)")},
        {"label": two("Played by", "Interprète"), "value": two("John Rue", "John Rue")},
    ],
    "intro": [
        two("Leviticus Cornwall is an American industrialist in Red Dead Redemption 2 (2018), set in 1899. He owns the Southern & Eastern Railway and the Cornwall Kerosene & Tar refinery, and imports sugar from the island of Guarma. In chapter 1 the Van der Linde gang robs his private train, using plans taken from the O'Driscolls. In chapter 2 his men take [[john-marston|John Marston]] and [[leopold-strauss|Leopold Strauss]] hostage in Valentine to draw out [[dutch-van-der-linde|Dutch van der Linde]]. He pays the Pinkerton agents who hunt the gang, among them [[andrew-milton|Andrew Milton]] and [[edgar-ross|Edgar Ross]]. In chapter 6 Dutch confronts him on the dock at Annesburg and shoots him dead.",
            "Leviticus Cornwall est un industriel américain de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Il possède le Southern & Eastern Railway et la raffinerie Cornwall Kerosene & Tar, et importe du sucre de l'île de Guarma. Au chapitre 1, le gang Van der Linde dévalise son train privé grâce à des plans pris aux O'Driscoll. Au chapitre 2, ses hommes prennent en otages [[john-marston|John Marston]] et [[leopold-strauss|Leopold Strauss]] à Valentine pour faire sortir [[dutch-van-der-linde|Dutch van der Linde]]. Il paie les agents Pinkerton lancés aux trousses du gang, parmi lesquels [[andrew-milton|Andrew Milton]] et [[edgar-ross|Edgar Ross]]. Au chapitre 6, Dutch l'affronte sur le quai d'Annesburg et l'abat."),
        two("He is played by John Rue.",
            "Il est interprété par John Rue."),
    ],
    "essentials": [
        two("He runs railroads, an oil refinery in the Heartlands, a freight business and a sugar trade with Guarma, and buys into the Annesburg coal mine.",
            "Il dirige des chemins de fer, une raffinerie de pétrole dans les Heartlands, une affaire de fret et un commerce de sucre avec Guarma, et prend une part dans la mine de charbon d'Annesburg."),
        two("In \"Who the Hell is Leviticus Cornwall?\", the Van der Linde gang stops his private train in the Grizzlies and takes railroad bonds from his car.",
            "Dans \"Who the Hell is Leviticus Cornwall?\", le gang Van der Linde arrête son train privé dans les Grizzlies et emporte des obligations ferroviaires de sa voiture."),
        two("In \"The Sheep and the Goats\", his guards hold [[john-marston|John]] and [[leopold-strauss|Strauss]] at gunpoint in Valentine while he calls for [[dutch-van-der-linde|Dutch]]; the gang shoots its way out of town.",
            "Dans \"The Sheep and the Goats\", ses gardes tiennent en joue [[john-marston|John]] et [[leopold-strauss|Strauss]] à Valentine pendant qu'il réclame [[dutch-van-der-linde|Dutch]] ; la bande quitte la ville sous les balles."),
        two("In \"Just a Social Call\", he scolds the Pinkerton agents he pays, refuses Dutch's demands and is shot dead on the Annesburg dock.",
            "Dans \"Just a Social Call\", il sermonne les agents Pinkerton qu'il paie, refuse les exigences de Dutch et est abattu sur le quai d'Annesburg."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["dutch-van-der-linde", "arthur-morgan", "andrew-milton", "alberto-fussar"],
}
