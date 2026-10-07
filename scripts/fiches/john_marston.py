"""John Marston, full template (pilot, 7 Oct 2026).

Fact base: two research passes (RDR2 / RDR1 + Undead Nightmare + real world),
each fact tagged CONFIRMED (2 independent sources or an in-game transcript /
original interview) or WIKI-ONLY. Only CONFIRMED facts are stated as fact.
Sources (internal register, not published): Red Dead Wiki EN/FR + mission
transcripts, English Wikipedia "John Marston" (GA), PowerPyx and IGN
walkthroughs, Polygon (Stafford, 19 Jun 2013), IU features (Whitaker, Feb 2021),
USA Today (Snider/Houser, 26 May 2010), GameSpot (Carson, Feb 2010), Variety
(Crecente/Nelson, 24 Oct 2018), THR (Shanley, 8 Nov 2018), IGN (Reilly, 22 May
2020), NYT (Schiesel, 16 May 2010), Engadget (DICE, 11 Feb 2011), Destructoid
(Spike VGA nominees, 17 Nov 2010), GamesRadar (Oct 2013), VG247 (26 May 2010),
RDR1 PS3 manual.
Left out (wiki-only or contested): scar side, 1898 departure, Illinois, the
daughter's cause of death, who fires at Bill/Allende, "holy water", outfit names.
"""

def two(en, fr): return {"en": en, "fr": fr}

def build(cl, CH):
    BH = "Beecher's Hope"
    def ch(n, en, fr): return {"h4": two(en, fr), "chapter": CH[n]}
    R2 = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]
    return {
 "slug": "john-marston", "name": "John Marston",
 "publishDate": "2026-06-23", "updated": "2026-10-07", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Van der Linde gang &middot; RDR1", "reg_role_fr": "Gang Van der Linde &middot; RDR1",
 "gender": "Male", "birth": "1873", "death": "1911", "nationality": "American",
 "portrait_alt": two("John Marston in Red Dead Redemption 2", "John Marston dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("John Marston, protagonist of Red Dead Redemption: full biography from 1873 to 1911, every mission in RDR2 and RDR1, the epilogue, Undead Nightmare, Rob Wiethoff's performance and awards.",
                  "John Marston, héros de Red Dead Redemption : biographie complète de 1873 à 1911, toutes ses missions dans RDR2 et RDR1, l'épilogue, Undead Nightmare, l'interprétation de Rob Wiethoff et ses récompenses."),
 "og_desc": two("The complete reference on John Marston: life, missions, quotes, development and reception.",
                "La référence complète sur John Marston : vie, missions, citations, conception et accueil."),
 "schema_desc": two("Protagonist of Red Dead Redemption and of the epilogue of Red Dead Redemption 2.",
                    "Héros de Red Dead Redemption et de l'épilogue de Red Dead Redemption 2."),
 "chips": [two("<strong>1873&ndash;1911</strong>", "<strong>1873&ndash;1911</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Voiced by <strong>Rob Wiethoff</strong>", "Voix de <strong>Rob Wiethoff</strong>")],
 "facts": [
   {"label": two("Born","Naissance"), "value": two("1873","1873")},
   {"label": two("Died","Mort"), "value": two("1911, Beecher's Hope","1911, Beecher's Hope")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang (1885-1899)","Gang Van der Linde (1885-1899)")},
   {"label": two("Family","Famille"), "value": two("[[abigail-marston|Abigail Marston]] (wife), [[jack-marston|Jack Marston]] (son)","[[abigail-marston|Abigail Marston]] (épouse), [[jack-marston|Jack Marston]] (fils)")},
   {"label": two("Alias","Alias"), "value": two("Jim Milton (1907)","Jim Milton (1907)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Undead Nightmare, Red Dead Redemption 2","Red Dead Redemption, Undead Nightmare, Red Dead Redemption 2")},
   {"label": two("Voiced by","Voix"), "value": two("Rob Wiethoff","Rob Wiethoff")},
 ],
 "intro": [
   two("John Marston is the protagonist of Red Dead Redemption (2010) and of its expansion Undead Nightmare, a major character of Red Dead Redemption 2 (2018), and the playable character of that game's epilogue. A member of Dutch van der Linde's gang from the age of twelve, he is forced in 1911 to hunt down his former companions.",
       "John Marston est le héros de Red Dead Redemption (2010) et de son extension Undead Nightmare, un personnage majeur de Red Dead Redemption 2 (2018) et le personnage jouable de son épilogue. Membre du gang de Dutch van der Linde depuis ses douze ans, il est contraint en 1911 de traquer ses anciens compagnons."),
   two("He is played by Rob Wiethoff in both games.",
       "Il est interprété par Rob Wiethoff dans les deux jeux."),
 ],
 "essentials": [
   two("Born in 1873; saved from the gallows at twelve by [[dutch-van-der-linde|Dutch van der Linde]], who raised him in his gang.",
       "Né en 1873 ; sauvé de la potence à douze ans par [[dutch-van-der-linde|Dutch van der Linde]], qui l'élève dans son gang."),
   two("1899: arrested in Saint Denis, freed from Sisika, left for dead by Dutch, he survives the gang's collapse thanks to [[arthur-morgan|Arthur Morgan]].",
       "1899 : arrêté à Saint-Denis, libéré de Sisika, laissé pour mort par Dutch, il survit à l'effondrement du gang grâce à [[arthur-morgan|Arthur Morgan]]."),
   two("1907: settles at Beecher's Hope with Abigail and Jack, and kills [[micah-bell|Micah Bell]] with Dutch on Mount Hagen.",
       "1907 : s'installe à Beecher's Hope avec Abigail et Jack, et tue [[micah-bell|Micah Bell]] avec Dutch au mont Hagen."),
   two("1911: forced by the Bureau of Investigation to hunt Bill Williamson, Javier Escuella and Dutch, then killed at his ranch by [[edgar-ross|Edgar Ross]]'s men.",
       "1911 : contraint par le Bureau of Investigation de traquer Bill Williamson, Javier Escuella et Dutch, puis tué dans son ranch par les hommes d'[[edgar-ross|Edgar Ross]]."),
   two("Rob Wiethoff's performance won Outstanding Character Performance at the 2011 D.I.C.E. Awards.",
       "Le jeu de Rob Wiethoff remporte le prix de la meilleure interprétation d'un personnage aux D.I.C.E. Awards 2011."),
 ],
 "rel_after": 0,
 "sections": [
   # ---------------------------------------------------------------- origins
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("John was born in 1873, the year carved on his grave. In Red Dead Redemption, he tells Bonnie MacFarlane that his mother, a prostitute, died giving birth to him, and that his father, \"an illiterate Scot, born on the boat into New York\", was blinded in a bar fight and died when John was eight. Sent to an orphanage, he ran away.",
               "John naît en 1873, l'année gravée sur sa tombe. Dans Red Dead Redemption, il raconte à Bonnie MacFarlane que sa mère, une prostituée, est morte en le mettant au monde, et que son père, un Écossais illettré né sur le bateau qui l'amenait à New York, a été aveuglé dans une bagarre de bar avant de mourir quand John avait huit ans. Placé dans un orphelinat, il s'en enfuit.")},
     {"p": two("According to the official guide, he was about to be hanged for theft at twelve when [[dutch-van-der-linde|Dutch]] saved him. Dutch raised him in his gang alongside [[arthur-morgan|Arthur Morgan]] and taught him to read. [[abigail-marston|Abigail Roberts]] later joined the gang, and their son [[jack-marston|Jack]] was born. In Red Dead Redemption, John also mentions a daughter who died.",
               "D'après le guide officiel, il va être pendu pour vol à douze ans lorsque [[dutch-van-der-linde|Dutch]] le sauve. Dutch l'élève dans son gang aux côtés d'[[arthur-morgan|Arthur Morgan]] et lui apprend à lire. [[abigail-marston|Abigail Roberts]] rejoint ensuite le gang, et leur fils [[jack-marston|Jack]] voit le jour. Dans Red Dead Redemption, John évoque aussi une fille, morte.")},
     # ------------------------------------------------------------ RDR2 1899
     {"h3": two("Red Dead Redemption 2 (1899)","Red Dead Redemption 2 (1899)")},
     ch(1, "Chapter 1: Colter", "Chapitre 1 : Colter"),
     {"p": two("After the failed ferry robbery in Blackwater, the gang flees into the snow. John, sent ahead to scout, goes missing for two days. In \"Enter, Pursued by a Memory\", Arthur and [[javier-escuella|Javier]] find his dead horse, then John himself on a ledge, wounded and surrounded by wolves, which have scarred his face. Bedridden, he stays out of the train robbery against [[leviticus-cornwall|Leviticus Cornwall]], and leaves Colter on a stretcher in a wagon.",
               "Après le braquage raté du ferry de Blackwater, le gang fuit dans la neige. Parti en éclaireur, John disparaît deux jours. Dans \"Enter, Pursued by a Memory\", Arthur et [[javier-escuella|Javier]] retrouvent son cheval mort, puis John lui-même sur une corniche, blessé et cerné par les loups, qui lui ont lacéré le visage. Alité, il ne participe pas à l'attaque du train de [[leviticus-cornwall|Leviticus Cornwall]], et quitte Colter sur une civière, dans un chariot.")},
     ch(2, "Chapter 2: Horseshoe Overlook", "Chapitre 2 : Horseshoe Overlook"),
     {"p": two("John raids an O'Driscoll safehouse with Arthur, Bill and [[kieran-duffy|Kieran Duffy]], and with Bill persuades Arthur to keep Kieran with the gang. The plan to stop a train by parking a stolen oil wagon across the tracks is his; he then robs the Scarlett Meadows train with Arthur, [[charles-smith|Charles]] and [[sean-macguire|Sean]]. In \"The Sheep and the Goats\", he plans the theft of sheep from Emerald Ranch and talks the Valentine auctioneer's cut down from 25 to 18 percent, before Cornwall's men take him and [[leopold-strauss|Strauss]] hostage.",
               "John attaque une planque des O'Driscoll avec Arthur, Bill et [[kieran-duffy|Kieran Duffy]], puis convainc Arthur, avec Bill, de garder Kieran dans le gang. C'est lui qui imagine d'arrêter un train en garant un wagon-citerne volé en travers des voies ; il attaque ensuite le train de Scarlett Meadows avec Arthur, [[charles-smith|Charles]] et [[sean-macguire|Sean]]. Dans \"The Sheep and the Goats\", il organise le vol de moutons d'Emerald Ranch et fait baisser la commission du commissaire-priseur de Valentine de 25 à 18 %, avant que les hommes de Cornwall ne le prennent en otage avec [[leopold-strauss|Strauss]].")},
     ch(3, "Chapter 3: Clemens Point", "Chapitre 3 : Clemens Point"),
     {"p": two("In \"Horse Flesh for Dinner\", John, Arthur and Javier steal the Braithwaites' horses for Tavish Gray; the animals fetch 700 dollars instead of the 5,000 promised. After Jack's kidnapping, he takes part in the attack on Braithwaite Manor. In \"The Battle of Shady Belle\", he clears Lemoyne Raiders out of the plantation with Arthur, and admits on the way that he has been a bad father.",
               "Dans \"Horse Flesh for Dinner\", John, Arthur et Javier volent les chevaux des Braithwaite pour Tavish Gray ; les bêtes rapportent 700 dollars au lieu des 5 000 promis. Après l'enlèvement de Jack, il participe à l'assaut de Braithwaite Manor. Dans \"The Battle of Shady Belle\", il chasse avec Arthur les Lemoyne Raiders de la plantation, et reconnaît en chemin avoir été un mauvais père.")},
     ch(4, "Chapter 4: Saint Denis", "Chapitre 4 : Saint-Denis"),
     {"p": two("John goes with Dutch and Arthur to [[angelo-bronte|Angelo Bronte]]'s mansion, and Jack is returned to his parents. He later knocks Bronte out before Dutch drowns him. During the robbery of the Saint Denis bank, John is arrested by the Pinkertons and sent to Sisika Penitentiary. He spends chapter 5 in prison while the others are shipwrecked on Guarma.",
               "John accompagne Dutch et Arthur au manoir d'[[angelo-bronte|Angelo Bronte]], et Jack est rendu à ses parents. Il assomme plus tard Bronte, avant que Dutch ne le noie. Lors du braquage de la banque de Saint-Denis, John est arrêté par les Pinkerton et envoyé au pénitencier de Sisika. Il passe le chapitre 5 en prison pendant que les autres font naufrage à Guarma.")},
     ch(6, "Chapter 6: Beaver Hollow", "Chapitre 6 : Beaver Hollow"),
     {"p": two("In \"Visiting Hours\", Arthur and [[sadie-adler|Sadie]] get John out of Sisika by trading him for a captured guard, to Dutch's displeasure. With Arthur, he blows up the Bacchus Bridge; Arthur urges him to take his family and leave. During the army payroll robbery, in \"Our Best Selves\", John is shot and falls from the train, and Dutch says he did not make it.",
               "Dans \"Visiting Hours\", Arthur et [[sadie-adler|Sadie]] font sortir John de Sisika en l'échangeant contre un gardien capturé, au grand déplaisir de Dutch. Avec Arthur, il fait sauter le pont de Bacchus ; Arthur le presse de partir avec sa famille. Lors de l'attaque du convoi de la solde de l'armée, dans \"Our Best Selves\", John est touché et tombe du train, et Dutch affirme qu'il n'a pas survécu.")},
     {"p": two("In the final mission, \"Red Dead Redemption\", John returns to Beaver Hollow (\"You left me... you left me to die!\") and sides with Arthur and [[susan-grimshaw|Susan Grimshaw]] against Micah. The Pinkertons attack and the two men flee. Whatever Arthur's last choice, he gives John his hat and satchel and stays behind; John rejoins Abigail and Jack.",
               "Lors de la dernière mission, \"Red Dead Redemption\", John revient à Beaver Hollow, reprochant à Dutch de l'avoir laissé mourir, et se range avec Arthur et [[susan-grimshaw|Susan Grimshaw]] contre Micah. Les Pinkerton attaquent et les deux hommes s'enfuient. Quel que soit le dernier choix d'Arthur, celui-ci confie à John son chapeau et sa sacoche et reste en arrière ; John rejoint Abigail et Jack.")},
     # ------------------------------------------------------------ RDR2 epilogue 1907
     {"h3": two("Red Dead Redemption 2: the epilogue (1907)","Red Dead Redemption 2 : l'épilogue (1907)")},
     ch("E1", "Epilogue I: Pronghorn Ranch", "Épilogue I : Pronghorn Ranch"),
     {"p": two("In 1907, the player controls John, who works at Pronghorn Ranch under the name Jim Milton. He recovers a stolen wagon from the Laramie Gang, then the ranch's cattle at Hanging Dog Ranch, where he kills the gang's leader. In Strawberry, he gives his real name at the post office. On the way back, three riders, one of them the brother of a man John killed earlier in Roanoke Ridge, attack him in front of Jack, and John kills them. Abigail leaves with Jack. John borrows money from a banker to buy land at Beecher's Hope, and [[uncle|Uncle]] joins him.",
               "En 1907, le joueur incarne John, qui travaille au Pronghorn Ranch sous le nom de Jim Milton. Il reprend un chariot volé au gang Laramie, puis le bétail du ranch à Hanging Dog Ranch, où il tue le chef du gang. À Strawberry, il donne son vrai nom au bureau de poste. Sur le chemin du retour, trois cavaliers, dont le frère d'un homme que John a tué plus tôt dans le Roanoke Ridge, l'attaquent sous les yeux de Jack, et John les abat. Abigail part avec Jack. John emprunte à un banquier pour acheter un terrain à Beecher's Hope, où [[uncle|Uncle]] le rejoint.")},
     ch("E2", "Epilogue II: Beecher's Hope", "Épilogue II : Beecher's Hope"),
     {"p": two("John finds [[charles-smith|Charles]] in Saint Denis, takes on bounties with Sadie, and builds a house at Beecher's Hope with Charles and Uncle. Abigail and Jack return. While capturing a bounty, he is mauled by a grizzly, and tells Sadie he wants to marry Abigail; he proposes to her in a rowboat.",
               "John retrouve [[charles-smith|Charles]] à Saint-Denis, accepte des primes avec Sadie, et bâtit une maison à Beecher's Hope avec Charles et Uncle. Abigail et Jack reviennent. En capturant un fugitif, il est attaqué par un grizzly, puis confie à Sadie vouloir épouser Abigail ; il la demande en mariage sur une barque.")},
     {"p": two("In \"American Venom\", John, Sadie and Charles track Micah to Mount Hagen, where Dutch is with him. Dutch shoots Micah in the chest and John finishes him. John takes the gang's money, pays off his debts and marries Abigail. The game ends with Edgar Ross and Archer Fordham watching the ranch.",
               "Dans \"American Venom\", John, Sadie et Charles retrouvent Micah au mont Hagen, où Dutch se trouve aussi. Dutch tire sur Micah, en pleine poitrine, et John l'achève. John récupère l'argent du gang, rembourse ses dettes et épouse Abigail. Le jeu se clôt sur Edgar Ross et Archer Fordham, qui observent le ranch.")},
     # ------------------------------------------------------------ RDR1
     {"h3": two("Red Dead Redemption (1911-1914)","Red Dead Redemption (1911-1914)")},
     ch("A1", "Act I: New Austin", "Acte I : New Austin"),
     {"p": two("In 1911, the Bureau of Investigation holds Abigail and Jack. Agents [[edgar-ross|Edgar Ross]] and [[archer-fordham|Archer Fordham]] put John on a train in Blackwater, sending him to New Austin to hunt down [[bill-williamson|Bill Williamson]]. At Fort Mercer, Bill refuses to surrender and one of his men shoots John, who is left for dead. [[bonnie-macfarlane|Bonnie MacFarlane]] takes him in, and he works on her ranch. He recruits [[leigh-johnson|Marshal Leigh Johnson]], [[nigel-west-dickens|Nigel West Dickens]], [[seth-briars|Seth Briars]] and [[irish|Irish]], then storms Fort Mercer from Dickens's wagon with a Gatling gun. Bill has already fled to Mexico.",
               "En 1911, le Bureau of Investigation retient Abigail et Jack. Les agents [[edgar-ross|Edgar Ross]] et [[archer-fordham|Archer Fordham]] mettent John dans un train à Blackwater, direction le New Austin, pour traquer [[bill-williamson|Bill Williamson]]. À Fort Mercer, Bill refuse de se rendre et l'un de ses hommes tire sur John, laissé pour mort. [[bonnie-macfarlane|Bonnie MacFarlane]] le recueille, et il travaille dans son ranch. Il recrute [[leigh-johnson|le marshal Leigh Johnson]], [[nigel-west-dickens|Nigel West Dickens]], [[seth-briars|Seth Briars]] et [[irish|Irish]], puis prend Fort Mercer d'assaut depuis le chariot de Dickens, armé d'une mitrailleuse Gatling. Bill s'est déjà enfui au Mexique.")},
     ch("A2", "Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso"),
     {"p": two("In Mexico, John works both for the government side, [[agustin-allende|Colonel Allende]] and [[vincente-de-santa|Captain de Santa]], and for the rebels of [[abraham-reyes|Abraham Reyes]] and [[luisa-fortuna|Luisa Fortuna]]; [[landon-ricketts|Landon Ricketts]] trains him. Betrayed by the army, he joins the rebels. During the attack on El Presidio, [[javier-escuella|Javier Escuella]] escapes on horseback; at the end of the chase, the player chooses whether to capture him alive or kill him. Allende and Bill flee Escalera by stagecoach; once John stops it, each is shot by John or by Reyes, depending on the player's choices.",
               "Au Mexique, John travaille à la fois pour le camp gouvernemental, [[agustin-allende|le colonel Allende]] et [[vincente-de-santa|le capitaine de Santa]], et pour les rebelles d'[[abraham-reyes|Abraham Reyes]] et de [[luisa-fortuna|Luisa Fortuna]] ; [[landon-ricketts|Landon Ricketts]] l'entraîne. Trahi par l'armée, il rejoint les rebelles. Lors de l'attaque d'El Presidio, [[javier-escuella|Javier Escuella]] s'enfuit à cheval ; au terme de la poursuite, le joueur choisit de le capturer vivant ou de le tuer. Allende et Bill fuient Escalera en diligence ; une fois la voiture arrêtée, chacun est abattu par John ou par Reyes, selon les choix du joueur.")},
     ch("A3", "Act III: West Elizabeth and the return home", "Acte III : West Elizabeth et le retour"),
     {"p": two("Ross then demands Dutch. Helped by [[harold-macdougal|Professor MacDougal]] and [[nastas|Nastas]], John tracks him to his hideout at Cochinay. Cornered on a cliff, Dutch tells him \"Our time is passed, John\" and lets himself fall. Ross shoots the body, saying \"it looks better in the report that way\".",
               "Ross exige ensuite Dutch. Aidé du [[harold-macdougal|professeur MacDougal]] et de [[nastas|Nastas]], John le retrouve dans son repaire de Cochinay. Acculé au bord d'une falaise, Dutch lui dit que leur temps est révolu et se laisse tomber. Ross tire sur le corps, jugeant que \"ça fait mieux dans le rapport\".")},
     {"p": two("John returns to Beecher's Hope, to Abigail, Jack and Uncle. He works the ranch and saves Jack from a bear. In \"The Last Enemy That Shall Be Destroyed\", soldiers and agents led by Ross attack the ranch. Uncle is killed. John sends Abigail and Jack away on horseback, steps out of the barn alone and is shot dead. He is buried on the hill beside Uncle.",
               "John retrouve Beecher's Hope, Abigail, Jack et Uncle. Il travaille au ranch et sauve Jack d'un ours. Dans \"The Last Enemy That Shall Be Destroyed\", des soldats et des agents menés par Ross attaquent le ranch. Uncle est tué. John fait fuir Abigail et Jack à cheval, sort seul de la grange et tombe sous les balles. Il est enterré sur la colline, près d'Uncle.")},
     {"h4": two("1914","1914")},
     {"p": two("Three years later, Abigail dies and Jack buries her beside John. In \"Remember My Family\", Jack finds the retired Ross and kills him in a duel.",
               "Trois ans plus tard, Abigail meurt et Jack l'enterre près de John. Dans \"Remember My Family\", Jack retrouve Ross, à la retraite, et le tue en duel.")},
     # ------------------------------------------------------------ Undead Nightmare
     {"h3": two("Undead Nightmare (outside the canon)","Undead Nightmare (hors continuité)")},
     {"p": two("Undead Nightmare (2010) is an expansion outside the series' canon. A plague turns the dead into zombies: a zombified Uncle bites Abigail, who bites Jack. John ties them up and sets out to find a cure. His search leads him to Mexico, where he kills an undead Abraham Reyes and learns that the rebel leader had stolen an Aztec mask. Returning the mask to its catacomb ends the plague. In the last mission, Seth steals the mask again, and John rises from his grave as an undead man who has kept his soul.",
               "Undead Nightmare (2010) est une extension hors de la continuité officielle. Une épidémie relève les morts : Uncle, devenu zombie, mord Abigail, qui mord Jack. John les ligote et part chercher un remède. Sa quête le mène au Mexique, où il abat Reyes, devenu mort-vivant, et apprend que le chef rebelle avait volé un masque aztèque. Remettre le masque dans sa crypte met fin à l'épidémie. Dans la dernière mission, Seth vole de nouveau le masque, et John sort de sa tombe en mort-vivant qui a gardé son âme.")},
   ]},
   # ---------------------------------------------------------------- Missions
   {"summary": two("Missions","Missions"), "blocks": [
     {"h3": two("Red Dead Redemption 2 (1899)","Red Dead Redemption 2 (1899)")},
     {"table": {"head": [two("Mission","Mission"), two("Ch.","Ch."), two("John's role","Rôle de John")], "rows": [
       R2("Outlaws from the West", "1", "Missing in the snow", "Disparu dans la neige"),
       R2("Enter, Pursued by a Memory", "1", "Rescued from the wolves", "Sauvé des loups"),
       R2("Who the Hell is Leviticus Cornwall?", "1", "Bedridden, stays behind", "Alité, reste au camp"),
       R2("Eastward Bound", "1", "Carried out on a stretcher", "Évacué sur une civière"),
       R2("Paying a Social Call", "2", "Raids Six Point Cabin", "Attaque de Six Point Cabin"),
       R2("Pouring Forth Oil I, III, IV", "2", "Plans and robs the train", "Monte et exécute l'attaque du train"),
       R2("The Sheep and the Goats", "2", "Sheep theft, taken hostage", "Vol de moutons, pris en otage"),
       R2("Horse Flesh for Dinner", "3", "Steals the Braithwaite horses", "Vole les chevaux des Braithwaite"),
       R2("Blood Feuds, Ancient and Modern", "3", "Attack on Braithwaite Manor", "Assaut de Braithwaite Manor"),
       R2("The Battle of Shady Belle", "3", "Clears the plantation", "Libère la plantation"),
       R2("Angelo Bronte, A Man of Honor", "4", "Jack is returned", "Retour de Jack"),
       R2("Horsemen, Apocalypses", "4", "Defends the camp", "Défend le camp"),
       R2("Revenge is a Dish Best Eaten", "4", "Knocks out Bronte", "Assomme Bronte"),
       R2("Banking, The Old American Art", "4", "Arrested", "Arrêté"),
       R2("Visiting Hours", "6", "Freed from Sisika", "Libéré de Sisika"),
       R2("The Bridge to Nowhere", "6", "Blows up the Bacchus Bridge", "Fait sauter le pont de Bacchus"),
       R2("My Last Boy", "6", "Battle at the oil fields", "Bataille des champs pétrolifères"),
       R2("Our Best Selves", "6", "Shot, falls from the train", "Touché, tombe du train"),
       R2("Red Dead Redemption", "6", "Returns and escapes", "Revient et s'échappe"),
     ]}},
     {"p": two("In the epilogue, every mission is played as John: The Wheel, Simple Pleasures, Farming, for Beginners, Fatherhood, for Beginners, Old Habits, Fatherhood, for Idiots, Jim Milton Rides, Again?, Motherhood, Gainful Employment, The Landowning Classes and Home of the Gentry? (Pronghorn Ranch); then Bare Knuckle Friendships, Home Improvement for Beginners, An Honest Day's Labors, The Tool Box, A New Jerusalem, A Quick Favor for an Old Friend, Uncle's Bad Day, The Best of Women, Trying Again, A Really Big Bastard, A New Future Imagined and American Venom (Beecher's Hope).",
               "Dans l'épilogue, toutes les missions se jouent avec John : The Wheel, Simple Pleasures, Farming, for Beginners, Fatherhood, for Beginners, Old Habits, Fatherhood, for Idiots, Jim Milton Rides, Again?, Motherhood, Gainful Employment, The Landowning Classes et Home of the Gentry? (Pronghorn Ranch) ; puis Bare Knuckle Friendships, Home Improvement for Beginners, An Honest Day's Labors, The Tool Box, A New Jerusalem, A Quick Favor for an Old Friend, Uncle's Bad Day, The Best of Women, Trying Again, A Really Big Bastard, A New Future Imagined et American Venom (Beecher's Hope).")},
     {"h3": two("Red Dead Redemption (1911): the 57 story missions","Red Dead Redemption (1911) : les 57 missions principales")},
     {"table": {"head": [two("Act","Acte"), two("Mission giver","Donneur"), two("Missions","Missions")], "rows": [
       ["I", "John", "Exodus in America"],
       ["I", "[[bonnie-macfarlane|Bonnie MacFarlane]]", "New Friends, Old Problems · Obstacles in Our Path · This is Armadillo, USA · Women and Cattle · Wild Horses, Tamed Passions · A Tempest Looms · The Burning"],
       ["I", "[[leigh-johnson|Leigh Johnson]]", "Political Realities in Armadillo · Justice in Pike's Basin · Spare the Rod, Spoil the Bandit · Hanging Bonnie MacFarlane · The Assault on Fort Mercer"],
       ["I", "[[nigel-west-dickens|Nigel West Dickens]]", "Old Swindler Blues · You Shall Not Give False Testimony, Except for Profit · Liars, Cheats and Other Proud Americans · Can a Swindler Change His Spots? · The Sport of Kings, and Liars"],
       ["I", "[[seth-briars|Seth Briars]]", "Exhuming and Other Fine Hobbies · A Gentle Drive with Friends · Let the Dead Bury Their Dead"],
       ["I", "[[irish|Irish]]", two("A Frenchman, a Welshman and an Irishman · Man is Born Unto Trouble · On Shaky's Ground · We Shall Be Together in Paradise (counted as Act II in the game's statistics)", "A Frenchman, a Welshman and an Irishman · Man is Born Unto Trouble · On Shaky's Ground · We Shall Be Together in Paradise (comptée dans l'acte II par les statistiques du jeu)")],
       ["II", "[[vincente-de-santa|Vincente de Santa]]", "Civilization, at Any Price · The Demon Drink · Empty Promises · Mexican Caesar · Cowards Die Many Times"],
       ["II", "[[landon-ricketts|Landon Ricketts]]", "The Gunslinger's Tragedy · Landon Ricketts Rides Again · Lucky in Love · The Mexican Wagon Train"],
       ["II", "[[luisa-fortuna|Luisa Fortuna]]", "My Sister's Keeper · Must a Savior Die? · Father Abraham · Captain De Santa's Downfall"],
       ["II", "[[abraham-reyes|Abraham Reyes]]", "The Great Mexican Train Robbery · The Gates of El Presidio · An Appointed Time"],
       ["III", "[[edgar-ross|Edgar Ross]]", "Bear One Another's Burdens · Great Men are Not Always Wise · And You Will Know The Truth · And The Truth Will Set You Free"],
       ["III", "[[harold-macdougal|Harold MacDougal]]", "At Home with Dutch · For Purely Scientific Purposes · The Prodigal Son Returns (To Yale)"],
       ["III", "[[abigail-marston|Abigail Marston]]", "The Outlaw's Return · Pestilence · Old Friends, New Problems"],
       ["III", "[[uncle|Uncle]]", "By Sweat and Toil · A Continual Feast"],
       ["III", "[[jack-marston|Jack Marston]]", "John Marston and Son · Wolves, Dogs and Sons · Spare the Love, Spoil the Child · The Last Enemy That Shall Be Destroyed"],
     ]}},
   ]},
   # ---------------------------------------------------------------- appearance & skills
   {"summary": two("Appearance and skills","Apparence et compétences"), "blocks": [
     {"ul": [
       two("His facial scars come from the wolf attack in chapter 1 of Red Dead Redemption 2. He still bears them in 1907, when Micah calls him \"scarface\".",
           "Ses cicatrices au visage viennent de l'attaque des loups au chapitre 1 de Red Dead Redemption 2. Il les porte toujours en 1907, quand Micah le traite de \"balafré\"."),
       two("He can read: Dutch taught him, as he taught Arthur.",
           "Il sait lire : Dutch le lui a appris, comme à Arthur."),
       two("He is a planner as well as a gunman: the oil wagon parked across the tracks to stop a train in 1899 is his idea.",
           "Il sait monter un coup autant que tirer : l'idée du wagon-citerne garé en travers des voies pour arrêter un train, en 1899, vient de lui."),
       two("He struggles to keep an alias: in 1907, he gives his real name at the Strawberry post office and to the banker who lends him money.",
           "Il peine à tenir un faux nom : en 1907, il donne sa véritable identité au bureau de poste de Strawberry et au banquier qui lui prête de l'argent."),
     ]},
   ]},
   # ---------------------------------------------------------------- quotes
   {"summary": two("Quotes","Citations"), "blocks": [
     {"quotes": [
       {"q": two("Never thought I'd say this, but... it's good to see you, Arthur Morgan.","Never thought I'd say this, but... it's good to see you, Arthur Morgan."),
        "src": two("Enter, Pursued by a Memory (RDR2, chapter 1)","Enter, Pursued by a Memory (RDR2, chapitre 1). Traduction : « J'aurais jamais cru dire ça, mais... ça fait plaisir de te voir, Arthur Morgan. »")},
       {"q": two("I was always ugly, Dutch... it's just a scratch.","I was always ugly, Dutch... it's just a scratch."),
        "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1)","Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1). Traduction : « J'ai toujours été moche, Dutch... c'est qu'une égratignure. »")},
       {"q": two("You left me... you left me to die!","You left me... you left me to die!"),
        "src": two("Red Dead Redemption (RDR2, chapter 6)","Red Dead Redemption (RDR2, chapitre 6). Traduction : « Tu m'as laissé... tu m'as laissé crever ! »")},
       {"q": two("I head down there, I'm dead in five minutes. I got a family, that's more important.","I head down there, I'm dead in five minutes. I got a family, that's more important."),
        "src": two("Red Dead Redemption (RDR2, chapter 6)","Red Dead Redemption (RDR2, chapitre 6). Traduction : « Si j'y retourne, je suis mort en cinq minutes. J'ai une famille, c'est plus important. »")},
       {"q": two("It's over, Abigail. It's all over.","It's over, Abigail. It's all over."),
        "src": two("American Venom (RDR2, epilogue)","American Venom (RDR2, épilogue). Traduction : « C'est fini, Abigail. Tout est fini. »")},
     ]},
   ]},
   # ---------------------------------------------------------------- development
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"h3": two("Red Dead Redemption","Red Dead Redemption")},
     {"p": two("Rob Wiethoff, from Seymour, Indiana, lived in Los Angeles for about ten years, tending bar between rare acting jobs. He told Polygon in 2013 that his agent called him one night in December for an audition for an \"untitled video game project\", where he was handed his lines and a basket of laundry; he got the part a few days later. Recording ran for a couple of weeks at a time, followed by a month or two off, over two years, and he kept bartending throughout. \"The storyline was still being written as we were shooting\", he said.",
               "Rob Wiethoff, originaire de Seymour, dans l'Indiana, a vécu une dizaine d'années à Los Angeles, barman entre de rares rôles. Il raconte à Polygon en 2013 que son agent l'a appelé un soir de décembre pour une audition pour un \"projet de jeu vidéo sans titre\", où on lui a remis son texte et un panier de linge à plier ; il a obtenu le rôle quelques jours plus tard. Les enregistrements s'enchaînaient par périodes de deux semaines, entrecoupées d'un ou deux mois de pause, pendant deux ans, et il a continué à servir derrière le bar. L'histoire s'écrivait encore pendant le tournage, précise-t-il.")},
     {"p": two("According to producer Rob Nelson, the very first cutscene shot was John finding Nigel West Dickens injured on the prairie. The game's manual credits Wiethoff together with three other performers for John's motion capture. Technical director Ted Carson told GameSpot in 2010 that John \"has a foot in both the old world and the world that was to come\", and that the team wanted \"a nuanced character, as opposed to a straightforward hero or villain\". Dan Houser told USA Today: \"John is a family man.\"",
               "D'après le producteur Rob Nelson, la toute première cinématique tournée est celle où John trouve Nigel West Dickens blessé dans la prairie. Le manuel du jeu crédite Wiethoff et trois autres interprètes pour la capture de mouvement de John. Le directeur technique Ted Carson explique à GameSpot en 2010 que John a un pied dans l'ancien monde et un dans celui qui vient, et que l'équipe voulait un personnage nuancé plutôt qu'un héros ou un méchant tout d'une pièce. Dan Houser résume à USA Today : John est un père de famille.")},
     {"h3": two("Red Dead Redemption 2","Red Dead Redemption 2")},
     {"p": two("Rockstar called Wiethoff back in 2014. Told he would be needed for about a year and would not be the playable character, he used up his leave at a construction job, then quit, and ended up working on the game for nearly four years, according to a 2021 feature by Indiana University. Producer Rob Nelson told Variety the writers \"had to be careful not to John it up too much\". Wiethoff told The Hollywood Reporter he drew on the older friends of his sister to play a younger John.",
               "Rockstar rappelle Wiethoff en 2014. Annoncé pour un an environ, et pas comme personnage jouable, le rôle l'oblige à épuiser ses congés sur un chantier, puis à démissionner ; il travaillera finalement près de quatre ans sur le jeu, selon un portrait publié par l'université de l'Indiana en 2021. Le producteur Rob Nelson explique à Variety que les scénaristes ont pris garde à ne pas trop mettre John en avant. Wiethoff confie au Hollywood Reporter s'être inspiré des amis plus âgés de sa sœur pour jouer un John plus jeune.")},
   ]},
   # ---------------------------------------------------------------- reception
   {"summary": two("Reception","Accueil"), "blocks": [
     {"ul": [
       two("2011 D.I.C.E. Awards: won Outstanding Character Performance (Rob Wiethoff).",
           "D.I.C.E. Awards 2011 : prix de la meilleure interprétation d'un personnage (Rob Wiethoff)."),
       two("2010 Spike Video Game Awards: nominated for Best Performance by a Human Male (Wiethoff) and for Character of the Year (John Marston).",
           "Spike Video Game Awards 2010 : nommé pour la meilleure interprétation masculine (Wiethoff) et pour le personnage de l'année (John Marston)."),
     ]},
     {"p": two("Reviewing the game in The New York Times in May 2010, Seth Schiesel wrote that \"the leading edge of interactive media has a new face. It is filthy, crudely scarred and belongs to John Marston\". Game Informer placed him second in its December 2010 list of \"30 Characters Who Defined a Decade\", and GamesRadar fifth in its 2013 ranking of the best characters of the generation. In 2018, Game Informer's Javy Gwaltney called him \"the best of the best\" among Rockstar's protagonists.",
               "Dans sa critique du New York Times, en mai 2010, Seth Schiesel écrit que le jeu vidéo a un nouveau visage, sale, grossièrement balafré, celui de John Marston. Game Informer le place deuxième de sa liste des 30 personnages qui ont marqué la décennie, en décembre 2010, et GamesRadar cinquième de son classement des meilleurs personnages de la génération, en 2013. En 2018, Javy Gwaltney, dans Game Informer, le juge le meilleur des héros de Rockstar.")},
   ]},
   # ---------------------------------------------------------------- other media
   {"summary": two("Other media","Autres médias"), "blocks": [
     {"p": two("John is the central character of Red Dead Redemption: The Man from Blackwater, a 30-minute film directed by John Hillcoat with the game's assets and broadcast on Fox on May 29, 2010.",
               "John est le personnage central de Red Dead Redemption: The Man from Blackwater, un film de 30 minutes réalisé par John Hillcoat avec les ressources du jeu, diffusé sur Fox le 29 mai 2010.")},
   ]},
   # ---------------------------------------------------------------- trivia
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He is about 26 in 1899, 34 in 1907 and 38 when he dies in 1911.",
           "Il a environ 26 ans en 1899, 34 en 1907 et 38 à sa mort, en 1911."),
       two("The gang's Blackwater money, which John recovers on Mount Hagen in 1907, pays off the Beecher's Hope loan.",
           "C'est l'argent du braquage de Blackwater, récupéré par John au mont Hagen en 1907, qui rembourse l'emprunt de Beecher's Hope."),
       two("After his death, the player controls Jack in Red Dead Redemption's final section.",
           "Après sa mort, le joueur incarne Jack dans la dernière partie de Red Dead Redemption."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "abigail.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
     "His partner, then his wife from 1907.", "Sa compagne, puis son épouse à partir de 1907.")},
   {"img": "jack.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
     "His son, who avenges him in 1914.", "Son fils, qui le venge en 1914.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Saves him from the wolves, from Sisika, then helps him escape.", "Le sauve des loups, de Sisika, puis l'aide à fuir.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Saves him at twelve, leaves him for dead in 1899, dies before him in 1911.", "Le sauve à douze ans, le laisse pour mort en 1899, meurt devant lui en 1911.")},
   {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
     "Builds Beecher's Hope with him and dies defending it.", "Bâtit Beecher's Hope avec lui et meurt en le défendant.")},
   {"img": "sadie.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
     "Frees him from Sisika, then hunts Micah with him.", "Le fait évader de Sisika, puis traque Micah avec lui.")},
   {"img": "ross.jpeg", "slug": "edgar-ross", "name": "Edgar Ross", "text": two(
     "Coerces him in 1911, then leads the attack that kills him.", "Le contraint en 1911, puis mène l'assaut qui le tue.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Official Red Dead Redemption artwork of John Marston","Artwork officiel de Red Dead Redemption représentant John Marston"),
    "cap": two("Official Red Dead Redemption key art.","Artwork officiel de Red Dead Redemption.")},
   {"img": "gallery-2.jpeg", "alt": two("John Marston on horseback at dusk","John Marston à cheval au crépuscule"),
    "cap": two("John on the trail.","John sur les pistes.")},
 ],
 "related": ["arthur-morgan", "abigail-marston", "jack-marston", "dutch-van-der-linde"],
}
