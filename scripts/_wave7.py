#!/usr/bin/env python3
"""Wave 7 content -> _queue/. Run: python scripts/_wave7.py
Not deployed (scripts/ is excluded from .cpanel.yml).

The RDR2 story cast the chapter guides name without a fiche: Catherine
Braithwaite and Tavish Gray (chapter 3), Alberto Fussar and Hercule Fontaine
(chapter 5), Rains Fall and Eagle Flies (chapter 6), plus Sister Calderon, the
nun who bridges RDR2 and RDR1. Published in story order, one every 3 days,
11 -> 29 Oct 2026, so each fiche can link back to the previous ones.

Factual register, FR written natively. Deliberately narrow where sources are
loose: no named shooter for Sean, no killer named for Gareth and Gerald, no
cause of death for Tavish (the game shows none), no first name or origin for
Calderon, no later fate for Hercule. Fussar's death IS shown in game (Arthur,
cannon, "Paradise Mercifully Departed"); Eagle Flies dies on the reservation,
not at the oil fields.
Images already staged in assets/characters/<slug>/.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fiche import build_to_queue

def two(en, fr): return {"en": en, "fr": fr}

CHARS = [
# ======================== 44. CATHERINE BRAITHWAITE ========================
{
 "order": 44, "slug": "catherine-braithwaite", "name": "Catherine Braithwaite",
 "publishDate": "2026-10-11", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Braithwaite matriarch &middot; RDR2", "reg_role_fr": "Matriarche des Braithwaite &middot; RDR2",
 "gender": "Female", "death": "1899", "nationality": "American",
 "portrait_alt": two("Catherine Braithwaite at the door of Braithwaite Manor in Red Dead Redemption 2",
                     "Catherine Braithwaite sur le seuil de Braithwaite Manor dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Lemoyne", "Personnage &middot; Lemoyne"),
 "meta_desc": two("Catherine Braithwaite: the head of the Braithwaite family in Red Dead Redemption 2. Biography, the feud with the Grays, Jack Marston's kidnapping and the fire at Braithwaite Manor.",
                  "Catherine Braithwaite : la matriarche de la famille Braithwaite dans Red Dead Redemption 2. Biographie, la guerre avec les Gray, l'enlèvement de Jack Marston et l'incendie de Braithwaite Manor."),
 "og_desc": two("The matriarch of Braithwaite Manor, and the woman behind Jack Marston's kidnapping in chapter 3.",
                "La matriarche de Braithwaite Manor, à l'origine de l'enlèvement de Jack Marston au chapitre 3."),
 "schema_desc": two("Matriarch of the Braithwaite family of Braithwaite Manor in Red Dead Redemption 2.",
                    "Matriarche de la famille Braithwaite, à Braithwaite Manor, dans Red Dead Redemption 2."),
 "chips": [two("Braithwaite family", "Famille Braithwaite"), two("Lemoyne", "Lemoyne"),
           two("Died 1899", "Morte en 1899"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Family","Famille"), "value": two("Braithwaite","Braithwaite")},
   {"label": two("Role","Rôle"), "value": two("Matriarch","Matriarche")},
   {"label": two("Residence","Résidence"), "value": two("Braithwaite Manor, near Rhodes","Braithwaite Manor, près de Rhodes")},
   {"label": two("Children","Enfants"), "value": two("Bartholomew, Gareth, Gerald, Gertrude","Bartholomew, Gareth, Gerald, Gertrude")},
   {"label": two("Status","Statut"), "value": two("Died in 1899","Morte en 1899")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Catherine Braithwaite is the head of the Braithwaite family, the owners of Braithwaite Manor near Rhodes, in Red Dead Redemption 2. She is the main antagonist of chapter 3.",
       "Catherine Braithwaite est la matriarche de la famille Braithwaite, propriétaire de Braithwaite Manor près de Rhodes, dans Red Dead Redemption 2. C'est la principale antagoniste du chapitre 3."),
   two("Her family is locked in a feud with the Grays of Caliga Hall. [[dutch-van-der-linde|Dutch van der Linde]] tries to play the two families against each other.",
       "Sa famille est en guerre ouverte avec les Gray de Caliga Hall. [[dutch-van-der-linde|Dutch van der Linde]] tente de monter les deux clans l'un contre l'autre."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The Braithwaite family","La famille Braithwaite")},
     {"p": two("The Braithwaites are an old plantation family of English descent, based at Braithwaite Manor in Scarlett Meadows, Lemoyne. Catherine has three sons, Bartholomew, Gareth and Gerald, and a daughter, Gertrude. The family's feud with the Grays goes back generations.",
               "Les Braithwaite sont une vieille famille de planteurs d'origine anglaise, installée à Braithwaite Manor, dans les Scarlett Meadows, en Lemoyne. Catherine a trois fils, Bartholomew, Gareth et Gerald, et une fille, Gertrude. La guerre avec les Gray dure depuis des générations.")},
     {"h3": two("Dealing with the gang","Les affaires avec le gang")},
     {"p": two("In \"Advertising, The New American Art\", [[hosea-matthews|Hosea]] and [[arthur-morgan|Arthur]] bring her a load of stolen moonshine. Her sons draw their guns, and she orders them to stand down. She already knows that Sheriff Leigh Gray sent the gang after the moonshine. She pays them to hand it out for free in the Grays' saloon in Rhodes.",
               "Dans \"Advertising, The New American Art\", [[hosea-matthews|Hosea]] et [[arthur-morgan|Arthur]] lui apportent un chargement de gnôle volée. Ses fils dégainent, et elle leur ordonne de baisser leurs armes. Elle sait déjà que le shérif Leigh Gray a envoyé le gang voler cette gnôle. Elle les paie pour la distribuer gratuitement dans le saloon des Gray, à Rhodes.")},
     {"p": two("In \"The Fine Joys of Tobacco\", over a game of cribbage with Hosea and [[sean-macguire|Sean MacGuire]], she hires Arthur and Sean to burn the Grays' tobacco fields at Caliga Hall.",
               "Dans \"The Fine Joys of Tobacco\", au cours d'une partie de cribbage avec Hosea et [[sean-macguire|Sean MacGuire]], elle charge Arthur et Sean d'incendier les champs de tabac des Gray à Caliga Hall.")},
   ]},
   {"summary": two("Jack Marston's kidnapping","L'enlèvement de Jack Marston"), "blocks": [
     {"p": two("After the Grays' ambush in Rhodes, in which Sean is killed, the Braithwaites take revenge on the gang by kidnapping [[jack-marston|Jack Marston]].",
               "Après l'embuscade tendue par les Gray à Rhodes, où Sean est tué, les Braithwaite se vengent du gang en enlevant [[jack-marston|Jack Marston]].")},
     {"p": two("In \"Blood Feuds, Ancient and Modern\", the gang storms Braithwaite Manor. Dutch shoots Bartholomew dead at the start of the fight. Gareth and Gerald are killed inside the house. Jack is not there. Dutch orders the manor burned and drags Catherine outside.",
               "Dans \"Blood Feuds, Ancient and Modern\", le gang prend d'assaut Braithwaite Manor. Dutch abat Bartholomew au début de l'affrontement. Gareth et Gerald sont tués dans la maison. Jack n'y est pas. Dutch fait incendier le manoir et traîne Catherine dehors.")},
     {"p": two("She tells them that her sons handed Jack to [[angelo-bronte|Angelo Bronte]], and that the boy is either in Saint Denis or on a boat to Italy.",
               "Elle leur apprend que ses fils ont remis Jack à [[angelo-bronte|Angelo Bronte]], et que l'enfant est soit à Saint-Denis, soit sur un bateau pour l'Italie.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("The gang leaves her alive. She runs back into the burning manor and dies there, in 1899. From chapter 4 onwards, her body can be found in the ruins of Braithwaite Manor.",
               "Le gang la laisse en vie. Elle retourne dans le manoir en flammes et y meurt, en 1899. À partir du chapitre 4, son corps peut être retrouvé dans les ruines de Braithwaite Manor.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Catherine Braithwaite is played by Ellen Harvey. She is also mentioned in Red Dead Online, where Josiah Trelawny asks the player to steal one of her horses.",
               "Catherine Braithwaite est interprétée par Ellen Harvey. Elle est aussi citée dans Red Dead Online, où Josiah Trelawny demande au joueur de voler l'un de ses chevaux.")},
   ]},
 ],
 "relationships": [
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("Plays her family against the Grays, then burns her house down.",
                "Joue sa famille contre les Gray, puis incendie sa maison.")},
   {"name": "Hosea Matthews", "slug": "hosea-matthews", "img": "hosea.jpeg",
    "text": two("Works the Braithwaites on the gang's behalf.",
                "Mène le jeu auprès des Braithwaite pour le compte du gang.")},
   {"name": "Tavish Gray", "slug": None, "img": "tavish.jpeg",
    "text": two("Head of the rival Gray family.",
                "Chef de la famille rivale, les Gray.")},
   {"name": "Angelo Bronte", "slug": "angelo-bronte", "img": "bronte.jpeg",
    "text": two("The Saint Denis crime boss her sons hand Jack to.",
                "Le parrain de Saint-Denis à qui ses fils livrent Jack.")},
   {"name": "Jack Marston", "slug": "jack-marston", "img": "jack.jpeg",
    "text": two("The boy her family kidnaps.",
                "L'enfant que sa famille enlève.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Dutch van der Linde dragging Catherine Braithwaite down the stairs of her manor","Dutch van der Linde traîne Catherine Braithwaite dans l'escalier de son manoir"),
    "cap": two("Dutch drags Catherine out of the manor in \"Blood Feuds, Ancient and Modern\".","Dutch traîne Catherine hors du manoir dans \"Blood Feuds, Ancient and Modern\".")},
 ],
},
# ======================== 45. TAVISH GRAY ========================
{
 "order": 45, "slug": "tavish-gray", "name": "Tavish Gray",
 "publishDate": "2026-10-14", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Gray patriarch &middot; RDR2", "reg_role_fr": "Patriarche des Gray &middot; RDR2",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Tavish Gray on the porch at Caliga Hall in Red Dead Redemption 2",
                     "Tavish Gray sous le porche de Caliga Hall dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Lemoyne", "Personnage &middot; Lemoyne"),
 "meta_desc": two("Tavish Gray: the head of the Gray family of Caliga Hall in Red Dead Redemption 2. Biography, the feud with the Braithwaites, the horse theft, and the letter found beside him.",
                  "Tavish Gray : le patriarche de la famille Gray, à Caliga Hall, dans Red Dead Redemption 2. Biographie, la guerre avec les Braithwaite, le vol de chevaux et la lettre retrouvée à ses côtés."),
 "og_desc": two("The patriarch of Caliga Hall, and the Gray side of the feud Dutch tries to exploit in chapter 3.",
                "Le patriarche de Caliga Hall, côté Gray de la guerre que Dutch tente d'exploiter au chapitre 3."),
 "schema_desc": two("Patriarch of the Gray family of Caliga Hall in Red Dead Redemption 2.",
                    "Patriarche de la famille Gray, à Caliga Hall, dans Red Dead Redemption 2."),
 "chips": [two("Gray family", "Famille Gray"), two("Lemoyne", "Lemoyne"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Family","Famille"), "value": two("Gray","Gray")},
   {"label": two("Role","Rôle"), "value": two("Patriarch, tobacco planter","Patriarche, planteur de tabac")},
   {"label": two("Residence","Résidence"), "value": two("Caliga Hall, east of Rhodes","Caliga Hall, à l'est de Rhodes")},
   {"label": two("Son","Fils"), "value": two("Beau Gray","Beau Gray")},
   {"label": two("Status","Statut"), "value": two("Found dead at Caliga Hall","Retrouvé mort à Caliga Hall")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Tavish Gray is the head of the Gray family, tobacco planters at Caliga Hall near Rhodes, in Red Dead Redemption 2.",
       "Tavish Gray est le patriarche de la famille Gray, planteurs de tabac à Caliga Hall, près de Rhodes, dans Red Dead Redemption 2."),
   two("His family has been feuding with the Braithwaites of [[catherine-braithwaite|Catherine Braithwaite]] for generations. In chapter 3, the Van der Linde gang works for both sides.",
       "Sa famille est en guerre depuis des générations avec les Braithwaite de [[catherine-braithwaite|Catherine Braithwaite]]. Au chapitre 3, le gang Van der Linde travaille pour les deux camps."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The Gray family","La famille Gray")},
     {"p": two("The Grays are a family of Scottish descent who grow tobacco at Caliga Hall, in Bayou Nwa, just east of Rhodes. Tavish is the eldest member of the family. His son, Beau Gray, is secretly in love with Penelope Braithwaite.",
               "Les Gray sont une famille d'origine écossaise qui cultive le tabac à Caliga Hall, dans le Bayou Nwa, juste à l'est de Rhodes. Tavish en est le doyen. Son fils, Beau Gray, aime en secret Penelope Braithwaite.")},
     {"p": two("Leigh Gray, the sheriff of Rhodes, belongs to the same family. The game is inconsistent about the link: Beau calls Leigh his uncle, while Dutch and Arthur refer to Leigh as Tavish's son.",
               "Leigh Gray, le shérif de Rhodes, appartient à la même famille. Le jeu n'est pas cohérent sur ce lien : Beau appelle Leigh son oncle, tandis que Dutch et Arthur le présentent comme le fils de Tavish.")},
     {"h3": two("Horse Flesh for Dinner","Horse Flesh for Dinner")},
     {"p": two("In \"Horse Flesh for Dinner\", Tavish receives [[arthur-morgan|Arthur]], [[john-marston|John]] and [[javier-escuella|Javier]] at Caliga Hall. He asks them to steal the Braithwaites' prize horses, and says the animals will sell for 5,000 dollars. The three men take the horses from Braithwaite Manor. The fence, Clay Davies, pays them 700 dollars.",
               "Dans \"Horse Flesh for Dinner\", Tavish reçoit [[arthur-morgan|Arthur]], [[john-marston|John]] et [[javier-escuella|Javier]] à Caliga Hall. Il leur demande de voler les chevaux de prix des Braithwaite, qui se vendraient selon lui 5 000 dollars. Les trois hommes les dérobent à Braithwaite Manor. Le receleur, Clay Davies, ne leur en donne que 700 dollars.")},
   ]},
   {"summary": two("The Rhodes ambush","L'embuscade de Rhodes"), "blocks": [
     {"p": two("Working for Catherine Braithwaite, Arthur and [[sean-macguire|Sean MacGuire]] set fire to the Grays' tobacco fields. The Grays then realise the gang has been working for both families.",
               "Pour le compte de Catherine Braithwaite, Arthur et [[sean-macguire|Sean MacGuire]] mettent le feu aux champs de tabac des Gray. Les Gray comprennent alors que le gang travaille pour les deux familles.")},
     {"p": two("In \"A Short Walk in a Pretty Town\", the Grays offer the gang a security job in Rhodes. It is a trap. Sean is shot dead as soon as it starts. Leigh Gray takes Bill Williamson hostage, and Arthur kills him outside the sheriff's office. Tavish is not present.",
               "Dans \"A Short Walk in a Pretty Town\", les Gray proposent au gang un travail de protection à Rhodes. C'est un piège. Sean est abattu dès le début. Leigh Gray prend Bill Williamson en otage, et Arthur le tue devant le bureau du shérif. Tavish n'est pas sur place.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Tavish is later found dead in a chair on the back porch of Caliga Hall. Beside him is a letter from Malcolm Moffat, a historian at the University of Edinburgh. It states that his ancestor, Ross Gray, was a paid informer for the Duke of Cumberland, not an exiled Jacobite. The game does not show how Tavish died.",
               "Tavish est retrouvé plus tard mort dans un fauteuil, sous le porche arrière de Caliga Hall. À ses côtés, une lettre de Malcolm Moffat, historien à l'université d'Édimbourg. Elle établit que son ancêtre, Ross Gray, était un informateur payé par le duc de Cumberland, et non un jacobite en exil. Le jeu ne montre pas les circonstances de sa mort.")},
     {"p": two("Arthur's journal entry on the discovery reads: \"Guess the Gray family ain't quite the proud noble Southern patriots they pretended to be.\"",
               "Dans son journal, Arthur note à ce sujet que les Gray ne sont pas tout à fait les fiers et nobles patriotes sudistes qu'ils prétendaient être.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Tavish Gray is played by Madison Arnold, who also voiced Jon Gravelli in Grand Theft Auto IV.",
               "Tavish Gray est interprété par Madison Arnold, qui prêtait aussi sa voix à Jon Gravelli dans Grand Theft Auto IV.")},
   ]},
 ],
 "relationships": [
   {"name": "Catherine Braithwaite", "slug": "catherine-braithwaite", "img": "catherine.jpeg",
    "text": two("Matriarch of the rival family. They never meet on screen.",
                "Matriarche de la famille rivale. Ils ne se croisent jamais à l'écran.")},
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("Courts the Grays while the gang works for the Braithwaites.",
                "Courtise les Gray pendant que le gang travaille pour les Braithwaite.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("Steals the Braithwaites' horses for him, then burns his fields.",
                "Vole pour lui les chevaux des Braithwaite, puis brûle ses champs.")},
   {"name": "Sean MacGuire", "slug": "sean-macguire", "img": "sean.jpeg",
    "text": two("Killed in the Grays' ambush in Rhodes.",
                "Tué dans l'embuscade des Gray à Rhodes.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Aerial view of the Caliga Hall tobacco plantation near Rhodes","Vue aérienne de la plantation de tabac de Caliga Hall, près de Rhodes"),
    "cap": two("Caliga Hall and its tobacco fields, east of Rhodes.","Caliga Hall et ses champs de tabac, à l'est de Rhodes.")},
 ],
},
# ======================== 46. ALBERTO FUSSAR ========================
{
 "order": 46, "slug": "alberto-fussar", "name": "Alberto Fussar",
 "publishDate": "2026-10-17", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Governor of Guarma &middot; RDR2", "reg_role_fr": "Gouverneur de Guarma &middot; RDR2",
 "gender": "Male", "death": "1899", "nationality": None,
 "portrait_alt": two("Alberto Fussar on his plantation in Guarma in Red Dead Redemption 2",
                     "Alberto Fussar sur sa plantation de Guarma dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Guarma", "Personnage &middot; Guarma"),
 "meta_desc": two("Alberto Fussar: the governor of Guarma and the antagonist of chapter 5 of Red Dead Redemption 2. Biography, his sugar regime, his link to Leviticus Cornwall, and his death.",
                  "Alberto Fussar : le gouverneur de Guarma et l'antagoniste du chapitre 5 de Red Dead Redemption 2. Biographie, son régime sucrier, son lien avec Leviticus Cornwall, et sa mort."),
 "og_desc": two("The colonel who rules Guarma through its sugar plantations, and the man standing between the gang and the boat home.",
                "Le colonel qui règne sur Guarma par ses plantations de canne, et l'homme qui sépare le gang du bateau du retour."),
 "schema_desc": two("Colonel and governor of the island of Guarma in Red Dead Redemption 2.",
                    "Colonel et gouverneur de l'île de Guarma dans Red Dead Redemption 2."),
 "chips": [two("Guarma", "Guarma"), two("Governor", "Gouverneur"),
           two("Died 1899", "Mort en 1899"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Role","Rôle"), "value": two("Governor of Guarma","Gouverneur de Guarma")},
   {"label": two("Rank","Grade"), "value": two("Colonel","Colonel")},
   {"label": two("Based at","Base"), "value": two("Aguasdulces","Aguasdulces")},
   {"label": two("Status","Statut"), "value": two("Killed in 1899","Tué en 1899")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Alberto Fussar is the governor of Guarma, a Caribbean island, in Red Dead Redemption 2. He holds the rank of colonel and runs the island's sugar industry.",
       "Alberto Fussar est le gouverneur de Guarma, une île des Caraïbes, dans Red Dead Redemption 2. Il porte le grade de colonel et contrôle l'industrie sucrière de l'île."),
   two("He is the main antagonist of chapter 5, when the Van der Linde gang is shipwrecked on Guarma.",
       "C'est le principal antagoniste du chapitre 5, lorsque le gang Van der Linde fait naufrage sur Guarma."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Governor of Guarma","Gouverneur de Guarma")},
     {"p": two("Fussar runs the sugar plantation and refinery at Aguasdulces. An in-game newspaper describes his rule over the island as quasi-military. His plantation overseer is an American, Levi Simon.",
               "Fussar dirige la plantation et la raffinerie de sucre d'Aguasdulces. Un journal du jeu décrit son pouvoir sur l'île comme quasi militaire. Le contremaître de sa plantation est un Américain, Levi Simon.")},
     {"p": two("He does business with [[leviticus-cornwall|Leviticus Cornwall]]. The newspaper article \"Guarma Island Sugar Boom\" reports that Cornwall has signed an exclusive purchase order with the governor of Guarma, whom he calls \"a great friend of America\".",
               "Il est en affaires avec [[leviticus-cornwall|Leviticus Cornwall]]. L'article \"Guarma Island Sugar Boom\" rapporte que Cornwall a signé un contrat d'achat exclusif avec le gouverneur de Guarma, qu'il qualifie de \"grand ami de l'Amérique\".")},
     {"p": two("Fussar also appears as a guest at Mayor Lemieux's party in Saint Denis, in \"The Gilded Cage\".",
               "Fussar apparaît aussi parmi les invités de la réception du maire Lemieux à Saint-Denis, dans \"The Gilded Cage\".")},
     {"h3": two("The gang on Guarma","Le gang à Guarma")},
     {"p": two("After the Saint Denis bank robbery, [[dutch-van-der-linde|Dutch]], [[arthur-morgan|Arthur]], [[micah-bell|Micah]], [[bill-williamson|Bill]] and [[javier-escuella|Javier]] escape on a steamer, the Antenor. It sinks in a storm, and they wash up on Guarma. Levi Simon's men put them in chains.",
               "Après le braquage de la banque de Saint-Denis, [[dutch-van-der-linde|Dutch]], [[arthur-morgan|Arthur]], [[micah-bell|Micah]], [[bill-williamson|Bill]] et [[javier-escuella|Javier]] s'enfuient à bord d'un vapeur, l'Antenor. Il sombre dans une tempête et ils s'échouent sur Guarma. Les hommes de Levi Simon les enchaînent.")},
     {"p": two("In \"A Kind and Benevolent Despot\", Dutch and Arthur find Fussar and his soldiers mocking Javier while a donkey drags him through the dirt. They set fire to the refinery and free Javier. In \"Hell Hath No Fury\", Fussar calls in a warship from Cuba. Arthur sinks it with a cannon at the fort of Cinco Torres.",
               "Dans \"A Kind and Benevolent Despot\", Dutch et Arthur découvrent Fussar et ses soldats qui se moquent de Javier, traîné au sol par un âne. Ils incendient la raffinerie et libèrent Javier. Dans \"Hell Hath No Fury\", Fussar fait venir un navire de guerre de Cuba. Arthur le coule au canon depuis le fort de Cinco Torres.")},
   ]},
   {"summary": two("Death","Mort"), "blocks": [
     {"p": two("In \"Paradise Mercifully Departed\", the gang and the island's rebels attack Aguasdulces. In a cabin, Arthur, Dutch, Levi Simon and Fussar end up in a standoff. A captive ship captain shoots Simon dead, and Fussar escapes through a window.",
               "Dans \"Paradise Mercifully Departed\", le gang et les rebelles de l'île attaquent Aguasdulces. Dans une cabane, Arthur, Dutch, Levi Simon et Fussar se retrouvent à se tenir en joue. Un capitaine de navire retenu prisonnier abat Simon, et Fussar s'enfuit par une fenêtre.")},
     {"p": two("Fussar takes position with an artillery piece on a tower above the port. Arthur fires a second cannon at the tower and kills him, in 1899. An in-game newspaper later reports the assassination of the governor of Guarma, and the involvement of \"several white men\".",
               "Fussar prend position avec une pièce d'artillerie au sommet d'une tour qui domine le port. Arthur tire sur la tour avec un second canon et le tue, en 1899. Un journal du jeu annonce ensuite l'assassinat du gouverneur de Guarma, et l'implication de \"plusieurs hommes blancs\".")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Alberto Fussar is played by Alfredo Narciso. He appears only in Red Dead Redemption 2.",
               "Alberto Fussar est interprété par Alfredo Narciso. Il n'apparaît que dans Red Dead Redemption 2.")},
   ]},
 ],
 "relationships": [
   {"name": "Leviticus Cornwall", "slug": "leviticus-cornwall", "img": "cornwall.jpeg",
    "text": two("Buys Guarma's sugar under an exclusive contract.",
                "Achète le sucre de Guarma en vertu d'un contrat exclusif.")},
   {"name": "Hercule Fontaine", "slug": None, "img": "hercule.jpeg",
    "text": two("Leads the rebels fighting his regime.",
                "Mène les rebelles qui combattent son régime.")},
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("Joins the rebels against him to get off the island.",
                "S'allie aux rebelles contre lui pour quitter l'île.")},
   {"name": "Javier Escuella", "slug": "javier-escuella", "img": "javier.jpeg",
    "text": two("Held prisoner by his men, then freed by Dutch and Arthur.",
                "Retenu prisonnier par ses hommes, puis libéré par Dutch et Arthur.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("Kills him with a cannon shot at Aguasdulces.",
                "Le tue d'un coup de canon à Aguasdulces.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Alberto Fussar holding a revolver during a standoff in a cabin at Aguasdulces","Alberto Fussar braque un revolver dans une cabane d'Aguasdulces"),
    "cap": two("The standoff at Aguasdulces in \"Paradise Mercifully Departed\".","Le face-à-face d'Aguasdulces dans \"Paradise Mercifully Departed\".")},
 ],
},
# ======================== 47. HERCULE FONTAINE ========================
{
 "order": 47, "slug": "hercule-fontaine", "name": "Hercule Fontaine",
 "publishDate": "2026-10-20", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Guarma rebel leader &middot; RDR2", "reg_role_fr": "Chef rebelle de Guarma &middot; RDR2",
 "gender": "Male", "death": None, "nationality": "Haitian",
 "portrait_alt": two("Hercule Fontaine in the jungle of Guarma in Red Dead Redemption 2",
                     "Hercule Fontaine dans la jungle de Guarma dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Guarma", "Personnage &middot; Guarma"),
 "meta_desc": two("Hercule Fontaine: the Haitian rebel leader of Guarma in Red Dead Redemption 2. Biography, his deal with Dutch, the fight against Alberto Fussar, and the boat off the island.",
                  "Hercule Fontaine : le chef rebelle haïtien de Guarma dans Red Dead Redemption 2. Biographie, son marché avec Dutch, la lutte contre Alberto Fussar, et le bateau qui permet de quitter l'île."),
 "og_desc": two("The rebel leader who offers the gang a way off Guarma, in exchange for its help against Fussar.",
                "Le chef rebelle qui offre au gang un moyen de quitter Guarma, en échange de son aide contre Fussar."),
 "schema_desc": two("Haitian rebel leader and smuggler on the island of Guarma in Red Dead Redemption 2.",
                    "Chef rebelle et contrebandier haïtien sur l'île de Guarma dans Red Dead Redemption 2."),
 "chips": [two("Guarma rebels", "Rebelles de Guarma"), two("Leader", "Chef"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Guarma rebels","Rebelles de Guarma")},
   {"label": two("Role","Rôle"), "value": two("Rebel leader, smuggler","Chef rebelle, contrebandier")},
   {"label": two("Base","Base"), "value": two("Cinco Torres","Cinco Torres")},
   {"label": two("Origin","Origine"), "value": two("Haitian","Haïtien")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Hercule Fontaine is a Haitian rebel leader on the island of Guarma in Red Dead Redemption 2. He fights the regime of [[alberto-fussar|Alberto Fussar]] and also works as a smuggler.",
       "Hercule Fontaine est un chef rebelle haïtien sur l'île de Guarma, dans Red Dead Redemption 2. Il combat le régime d'[[alberto-fussar|Alberto Fussar]] et vit aussi de la contrebande."),
   two("In chapter 5, he offers the shipwrecked Van der Linde gang a way off the island in exchange for its help.",
       "Au chapitre 5, il propose au gang Van der Linde, naufragé, un moyen de quitter l'île en échange de son aide."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Welcome to the New World","Welcome to the New World")},
     {"p": two("In \"Welcome to the New World\", Hercule's men ambush the convoy carrying the chained gang and captured rebels. [[arthur-morgan|Arthur]] grabs a guard's gun and the prisoners free themselves. [[javier-escuella|Javier]] is shot in the leg and recaptured. Arthur, [[dutch-van-der-linde|Dutch]], [[bill-williamson|Bill]] and [[micah-bell|Micah]] escape with Hercule.",
               "Dans \"Welcome to the New World\", les hommes d'Hercule attaquent le convoi qui transporte le gang enchaîné et des rebelles capturés. [[arthur-morgan|Arthur]] s'empare de l'arme d'un garde et les prisonniers se libèrent. [[javier-escuella|Javier]], touché à la jambe, est repris. Arthur, [[dutch-van-der-linde|Dutch]], [[bill-williamson|Bill]] et [[micah-bell|Micah]] s'enfuient avec Hercule.")},
     {"p": two("Hercule leads them to an old building stocked with rifles, where they hold off the soldiers. With the rebel Leon Fuentes, he explains how Fussar runs the island through slave labour on the sugar plantations.",
               "Hercule les conduit dans un vieux bâtiment rempli de fusils, où ils repoussent les soldats. Avec le rebelle Leon Fuentes, il leur explique comment Fussar tient l'île grâce au travail forcé dans les plantations de canne.")},
     {"h3": two("The deal","Le marché")},
     {"p": two("Hercule promises to get the gang off the island if it first helps free workers captured by Fussar's men. Dutch accepts. The rebels' base is the old Spanish fort of Cinco Torres.",
               "Hercule promet de faire quitter l'île au gang s'il l'aide d'abord à libérer des travailleurs capturés par les hommes de Fussar. Dutch accepte. La base des rebelles est le vieux fort espagnol de Cinco Torres.")},
   ]},
   {"summary": two("The fight against Fussar","La lutte contre Fussar"), "blocks": [
     {"p": two("In \"Hell Hath No Fury\", the gang argues with Hercule over the boat he promised. He tells them Fussar has asked Cuba for help and that a warship is on its way, so they cannot leave safely until Fussar is dealt with. The ship and troops attack Cinco Torres. Hercule loads the fort's cannon, and Arthur fires it and sinks the warship.",
               "Dans \"Hell Hath No Fury\", le gang reproche à Hercule le bateau promis. Il répond que Fussar a demandé l'aide de Cuba et qu'un navire de guerre arrive : impossible de partir sans danger tant que Fussar n'est pas réglé. Le navire et des troupes attaquent Cinco Torres. Hercule charge le canon du fort, Arthur fait feu et coule le navire.")},
     {"p": two("In \"Paradise Mercifully Departed\", Hercule, Arthur, Dutch and Micah destroy Fussar's gun batteries. At Aguasdulces, Hercule points out Fussar on a tower above the port, and a second cannon nearby. Arthur uses it to kill Fussar.",
               "Dans \"Paradise Mercifully Departed\", Hercule, Arthur, Dutch et Micah détruisent les batteries de Fussar. À Aguasdulces, Hercule désigne Fussar au sommet d'une tour qui domine le port, ainsi qu'un second canon tout proche. Arthur s'en sert pour tuer Fussar.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Once Fussar is dead, Hercule tells Dutch that he and his men will be gone before anyone arrives. The gang sails back to the mainland. The game does not show what becomes of Hercule afterwards.",
               "Une fois Fussar mort, Hercule annonce à Dutch que ses hommes et lui auront disparu avant l'arrivée des renforts. Le gang regagne le continent par la mer. Le jeu ne montre pas ce que devient Hercule ensuite.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Hercule Fontaine is voiced by Guyviaud Joseph. He appears only in Red Dead Redemption 2.",
               "Hercule Fontaine est doublé par Guyviaud Joseph. Il n'apparaît que dans Red Dead Redemption 2.")},
   ]},
 ],
 "relationships": [
   {"name": "Alberto Fussar", "slug": "alberto-fussar", "img": "fussar.jpeg",
    "text": two("The governor whose regime he fights.",
                "Le gouverneur dont il combat le régime.")},
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("Agrees to his deal: help against Fussar in exchange for a boat.",
                "Accepte son marché : de l'aide contre Fussar, en échange d'un bateau.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("Fights alongside him at Cinco Torres and Aguasdulces.",
                "Combat à ses côtés à Cinco Torres et à Aguasdulces.")},
   {"name": "Micah Bell", "slug": "micah-bell", "img": "micah.jpeg",
    "text": two("Joins the raid on Fussar's gun batteries.",
                "Participe à l'attaque des batteries de Fussar.")},
   {"name": "Javier Escuella", "slug": "javier-escuella", "img": "javier.jpeg",
    "text": two("Recaptured during the escape, he spends most of the chapter as a prisoner.",
                "Repris lors de l'évasion, il passe l'essentiel du chapitre prisonnier.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("The coast of the island of Guarma","La côte de l'île de Guarma"),
    "cap": two("The coast of Guarma, the island where chapter 5 takes place.","La côte de Guarma, l'île où se déroule le chapitre 5.")},
 ],
},
# ======================== 48. RAINS FALL ========================
{
 "order": 48, "slug": "rains-fall", "name": "Rains Fall",
 "publishDate": "2026-10-23", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Wapiti chief &middot; RDR2", "reg_role_fr": "Chef wapiti &middot; RDR2",
 "gender": "Male", "death": None, "nationality": None,
 "portrait_alt": two("Rains Fall, chief of the Wapiti, in Red Dead Redemption 2",
                     "Rains Fall, chef des Wapiti, dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Wapiti", "Personnage &middot; Wapiti"),
 "meta_desc": two("Rains Fall: the chief of the Wapiti in Red Dead Redemption 2. Biography, the fight over the reservation with Leviticus Cornwall and the Army, his son Eagle Flies, and his meeting with Arthur.",
                  "Rains Fall : le chef des Wapiti dans Red Dead Redemption 2. Biographie, la lutte pour la réserve face à Leviticus Cornwall et à l'armée, son fils Eagle Flies, et ses rencontres avec Arthur."),
 "og_desc": two("The Wapiti chief who seeks peace with the Army while his son prepares for war.",
                "Le chef wapiti qui cherche la paix avec l'armée pendant que son fils prépare la guerre."),
 "schema_desc": two("Chief of the Wapiti nation in Red Dead Redemption 2.",
                    "Chef de la nation wapiti dans Red Dead Redemption 2."),
 "chips": [two("Wapiti", "Wapiti"), two("Chief", "Chef"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Nation","Nation"), "value": two("Wapiti","Wapiti")},
   {"label": two("Role","Rôle"), "value": two("Chief","Chef")},
   {"label": two("Home","Lieu de vie"), "value": two("Wapiti Indian Reservation, Grizzlies East","Réserve indienne wapiti, Grizzlies East")},
   {"label": two("Son","Fils"), "value": two("Eagle Flies","Eagle Flies")},
   {"label": two("Status","Statut"), "value": two("Alive in 1907","Vivant en 1907")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Rains Fall is the chief of the Wapiti, a Native American nation living on a reservation in the Grizzlies East, in Red Dead Redemption 2.",
       "Rains Fall est le chef des Wapiti, une nation amérindienne qui vit sur une réserve des Grizzlies East, dans Red Dead Redemption 2."),
   two("He says he has signed three treaties with the United States government, and that all three were broken. He seeks a peaceful way to keep his people's land, while his son Eagle Flies wants to fight the Army.",
       "Il dit avoir signé trois traités avec le gouvernement des États-Unis, tous rompus. Il cherche une voie pacifique pour conserver les terres de son peuple, tandis que son fils Eagle Flies veut combattre l'armée."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Family","Famille")},
     {"p": two("Rains Fall says that his elder son was killed by a drunken soldier, and that a soldier killed his wife. Eagle Flies is his last surviving child. He fought as a young man and now argues for peace.",
               "Rains Fall raconte que son fils aîné a été tué par un soldat ivre, et qu'un soldat a tué sa femme. Eagle Flies est le dernier enfant qui lui reste. Il s'est battu dans sa jeunesse et défend désormais la paix.")},
     {"h3": two("Chapter 4: the reservation claim","Chapitre 4 : la revendication sur la réserve")},
     {"p": two("In \"American Fathers I\", Rains Fall meets [[arthur-morgan|Arthur]] outside the courthouse in Saint Denis, with Eagle Flies and the writer Evelyn Miller. The Wapiti believe [[leviticus-cornwall|Leviticus Cornwall]]'s claim on their reservation may be illegal, and that documents could prove it. Arthur agrees to help.",
               "Dans \"American Fathers I\", Rains Fall rencontre [[arthur-morgan|Arthur]] devant le palais de justice de Saint-Denis, avec Eagle Flies et l'écrivain Evelyn Miller. Les Wapiti pensent que la revendication de [[leviticus-cornwall|Leviticus Cornwall]] sur leur réserve est peut-être illégale, et que des documents pourraient le prouver. Arthur accepte de les aider.")},
     {"h3": two("Chapter 6: the war with the Army","Chapitre 6 : la guerre avec l'armée")},
     {"p": two("In \"Archeology for Beginners\", an optional mission, Rains Fall reproaches Arthur for riding with Eagle Flies on a raid, and notices his cough. Arthur recovers a sacred object for him from a site disturbed by the Army.",
               "Dans \"Archeology for Beginners\", une mission facultative, Rains Fall reproche à Arthur d'avoir participé à un raid avec Eagle Flies, et remarque sa toux. Arthur récupère pour lui un objet sacré sur un site profané par l'armée.")},
     {"p": two("In \"The Fine Art of Conversation\", he comes to the gang's camp at Beaver Hollow and asks Arthur and [[charles-smith|Charles]] to escort him to a truce meeting with Colonel Henry Favours. The talks fail. Favours announces that Captain Monroe, an officer sympathetic to the tribe, will be tried for treason. Arthur and Charles get Monroe out.",
               "Dans \"The Fine Art of Conversation\", il se rend au camp de Beaver Hollow et demande à Arthur et à [[charles-smith|Charles]] de l'accompagner à une rencontre de trêve avec le colonel Henry Favours. Les pourparlers échouent. Favours annonce que le capitaine Monroe, un officier favorable à la tribu, sera jugé pour trahison. Arthur et Charles le font évader.")},
     {"p": two("In \"The King's Son\", Rains Fall says his son is foolish but that he loves him. Arthur and Charles free Eagle Flies from Fort Wallace. In \"My Last Boy\", Rains Fall rides into Beaver Hollow and begs the warriors not to attack the Army. Eagle Flies ignores him. After the battle at the Heartland Oil Fields, Eagle Flies is brought back to the reservation and dies in his father's arms.",
               "Dans \"The King's Son\", Rains Fall dit que son fils est un insensé mais qu'il l'aime. Arthur et Charles libèrent Eagle Flies de Fort Wallace. Dans \"My Last Boy\", Rains Fall arrive à cheval à Beaver Hollow et supplie les guerriers de ne pas attaquer l'armée. Eagle Flies ne l'écoute pas. Après la bataille des champs pétrolifères du Heartland, Eagle Flies est ramené dans la réserve et meurt dans les bras de son père.")},
   ]},
   {"summary": two("After 1899","Après 1899"), "blocks": [
     {"p": two("In the 1907 epilogue, Rains Fall can be met on a bench at the Annesburg train station. He explains that his people have fled to Canada, and that he has come back for a time to mourn Eagle Flies.",
               "Dans l'épilogue de 1907, on peut croiser Rains Fall sur un banc de la gare d'Annesburg. Il explique que son peuple s'est réfugié au Canada, et qu'il est revenu un temps pour pleurer Eagle Flies.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Rains Fall is played by Graham Greene, a Canadian actor of the Oneida Nation, who died on September 1, 2025 in Toronto, at the age of 73. The Wapiti are a fictional nation; the in-game captions identify the language of his non-English lines as Lakota.",
               "Rains Fall est interprété par Graham Greene, acteur canadien de la nation oneida, mort le 1er septembre 2025 à Toronto, à 73 ans. Les Wapiti sont une nation fictive ; les sous-titres du jeu indiquent que ses répliques non anglaises sont en lakota.")},
   ]},
 ],
 "relationships": [
   {"name": "Eagle Flies", "slug": None, "img": "eagle.jpeg",
    "text": two("His son, who rejects his call for peace.",
                "Son fils, qui rejette son appel à la paix.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("Helps the Wapiti in Saint Denis and in chapter 6.",
                "Aide les Wapiti à Saint-Denis puis au chapitre 6.")},
   {"name": "Charles Smith", "slug": "charles-smith", "img": "charles.jpeg",
    "text": two("Escorts him to the truce meeting with Colonel Favours.",
                "L'escorte à la rencontre de trêve avec le colonel Favours.")},
   {"name": "Leviticus Cornwall", "slug": "leviticus-cornwall", "img": "cornwall.jpeg",
    "text": two("The industrialist whose claim threatens the reservation.",
                "L'industriel dont la revendication menace la réserve.")},
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("Backs Eagle Flies' raids to draw the Army's attention away from the gang.",
                "Soutient les raids d'Eagle Flies pour détourner l'attention de l'armée loin du gang.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Three Wapiti riders on a ridge at dawn","Trois cavaliers wapiti sur une crête à l'aube"),
    "cap": two("Wapiti riders on a ridge above the gang's route.","Des cavaliers wapiti sur une crête, au-dessus de la route du gang.")},
 ],
},
# ======================== 49. EAGLE FLIES ========================
{
 "order": 49, "slug": "eagle-flies", "name": "Eagle Flies",
 "publishDate": "2026-10-26", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Wapiti warrior &middot; RDR2", "reg_role_fr": "Guerrier wapiti &middot; RDR2",
 "gender": "Male", "death": "1899", "nationality": None,
 "portrait_alt": two("Eagle Flies outside the courthouse in Saint Denis in Red Dead Redemption 2",
                     "Eagle Flies devant le palais de justice de Saint-Denis dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Wapiti", "Personnage &middot; Wapiti"),
 "meta_desc": two("Eagle Flies: the son of Wapiti chief Rains Fall in Red Dead Redemption 2. Biography, the raid on Cornwall's refinery, Fort Wallace, and his death after the battle at the Heartland Oil Fields.",
                  "Eagle Flies : le fils du chef wapiti Rains Fall dans Red Dead Redemption 2. Biographie, l'attaque de la raffinerie de Cornwall, Fort Wallace, et sa mort après la bataille des champs pétrolifères du Heartland."),
 "og_desc": two("Rains Fall's last son, who chooses war with the Army and dies saving Arthur Morgan.",
                "Le dernier fils de Rains Fall, qui choisit la guerre contre l'armée et meurt en sauvant Arthur Morgan."),
 "schema_desc": two("Wapiti warrior and son of Chief Rains Fall in Red Dead Redemption 2.",
                    "Guerrier wapiti, fils du chef Rains Fall, dans Red Dead Redemption 2."),
 "chips": [two("Wapiti", "Wapiti"), two("Warrior", "Guerrier"),
           two("Died 1899", "Mort en 1899"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Nation","Nation"), "value": two("Wapiti","Wapiti")},
   {"label": two("Father","Père"), "value": two("Rains Fall","Rains Fall")},
   {"label": two("Home","Lieu de vie"), "value": two("Wapiti Indian Reservation, Grizzlies East","Réserve indienne wapiti, Grizzlies East")},
   {"label": two("Status","Statut"), "value": two("Killed in 1899","Tué en 1899")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Eagle Flies is the son of [[rains-fall|Rains Fall]], chief of the Wapiti, in Red Dead Redemption 2. His elder brother and his mother were killed by US soldiers before the game begins.",
       "Eagle Flies est le fils de [[rains-fall|Rains Fall]], chef des Wapiti, dans Red Dead Redemption 2. Son frère aîné et sa mère ont été tués par des soldats américains avant le début du jeu."),
   two("Unlike his father, he wants to fight the Army that is pushing his people off their land.",
       "Contrairement à son père, il veut combattre l'armée qui chasse son peuple de ses terres."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Chapter 4: Cornwall's refinery","Chapitre 4 : la raffinerie de Cornwall")},
     {"p": two("Eagle Flies meets [[arthur-morgan|Arthur]] with his father outside the Saint Denis courthouse, in \"American Fathers I\". In \"American Fathers II\", the two men target Cornwall Kerosene &amp; Tar, the refinery of [[leviticus-cornwall|Leviticus Cornwall]] at the Heartland Oil Fields.",
               "Eagle Flies rencontre [[arthur-morgan|Arthur]] avec son père devant le palais de justice de Saint-Denis, dans \"American Fathers I\". Dans \"American Fathers II\", les deux hommes s'en prennent à Cornwall Kerosene &amp; Tar, la raffinerie de [[leviticus-cornwall|Leviticus Cornwall]] aux champs pétrolifères du Heartland.")},
     {"p": two("Arthur gets inside hidden in a wagon and takes documents from the foreman, Danbury. Eagle Flies blows up an oil well to cover him. They fight their way out together, and Eagle Flies pays Arthur.",
               "Arthur s'introduit caché dans un chariot et prend des documents au contremaître, Danbury. Eagle Flies fait sauter un puits de pétrole pour le couvrir. Ils s'échappent ensemble à travers les tirs, et Eagle Flies paie Arthur.")},
     {"h3": two("Chapter 6: the raids","Chapitre 6 : les raids")},
     {"p": two("In \"A Rage Unleashed\", he comes to the gang's camp at Beaver Hollow to ask for help recovering the tribe's horses, confiscated by the Army. [[dutch-van-der-linde|Dutch]] agrees. With Arthur, [[charles-smith|Charles]] and his companion Paytah, they board an Army boat. Dutch crashes it, and the horses swim back to shore.",
               "Dans \"A Rage Unleashed\", il vient au camp de Beaver Hollow demander de l'aide pour récupérer les chevaux de la tribu, confisqués par l'armée. [[dutch-van-der-linde|Dutch]] accepte. Avec Arthur, [[charles-smith|Charles]] et son compagnon Paytah, ils montent à bord d'un bateau de l'armée. Dutch l'échoue, et les chevaux regagnent la rive à la nage.")},
     {"p": two("In \"Favored Sons\", Eagle Flies and Dutch set a dynamite trap for an Army patrol. Reinforcements arrive. Eagle Flies goes back for the wounded Paytah and is captured. He is held at Fort Wallace. In \"The King's Son\", Arthur and Charles break into the fort at night and free him.",
               "Dans \"Favored Sons\", Eagle Flies et Dutch tendent un piège à la dynamite à une patrouille. Des renforts arrivent. Eagle Flies retourne chercher Paytah, blessé, et se fait capturer. Il est détenu à Fort Wallace. Dans \"The King's Son\", Arthur et Charles s'introduisent de nuit dans le fort et le libèrent.")},
   ]},
   {"summary": two("Death","Mort"), "blocks": [
     {"p": two("In \"My Last Boy\", Eagle Flies rides into Beaver Hollow in war paint and asks the gang to join an attack on the Army at the Heartland Oil Fields. His father begs him not to go. He answers that his father's words mean nothing.",
               "Dans \"My Last Boy\", Eagle Flies arrive à Beaver Hollow peint pour la guerre et demande au gang de se joindre à une attaque contre l'armée aux champs pétrolifères du Heartland. Son père le supplie de renoncer. Il répond que ses paroles ne valent rien.")},
     {"p": two("During the battle, a burst steam pipe stuns Arthur, and Dutch leaves him behind. Eagle Flies kills the soldiers about to shoot Arthur. Colonel Henry Favours then shoots Eagle Flies in the stomach, and Arthur kills Favours.",
               "Pendant la bataille, une conduite de vapeur explose et sonne Arthur, que Dutch abandonne sur place. Eagle Flies abat les soldats qui s'apprêtaient à tirer sur Arthur. Le colonel Henry Favours touche alors Eagle Flies au ventre, et Arthur tue Favours.")},
     {"p": two("Arthur, Charles and Paytah carry Eagle Flies back to the reservation, where he dies in Rains Fall's arms in 1899. His death is part of the main story and does not depend on the player's choices. His grave, west of Donner Falls, can be visited in the epilogue.",
               "Arthur, Charles et Paytah le ramènent dans la réserve, où il meurt dans les bras de Rains Fall, en 1899. Sa mort fait partie de l'histoire principale et ne dépend pas des choix du joueur. Sa tombe, à l'ouest des Donner Falls, peut être visitée dans l'épilogue.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Eagle Flies is played by Jeremiah Bitsui, a Navajo actor also of Omaha descent, known for playing Victor in Breaking Bad.",
               "Eagle Flies est interprété par Jeremiah Bitsui, acteur navajo également d'ascendance omaha, connu pour le rôle de Victor dans Breaking Bad.")},
   ]},
 ],
 "relationships": [
   {"name": "Rains Fall", "slug": "rains-fall", "img": "rains.jpeg",
    "text": two("His father, whose pacifism he rejects.",
                "Son père, dont il rejette le pacifisme.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("Fights beside him from the refinery raid to the oil fields.",
                "Combat à ses côtés, de la raffinerie aux champs pétrolifères.")},
   {"name": "Charles Smith", "slug": "charles-smith", "img": "charles.jpeg",
    "text": two("Frees him from Fort Wallace with Arthur.",
                "Le libère de Fort Wallace avec Arthur.")},
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("Joins his raids to keep the Army busy away from the gang.",
                "Se joint à ses raids pour occuper l'armée loin du gang.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Eagle Flies at night at the end of the refinery raid","Eagle Flies de nuit, à la fin de l'attaque de la raffinerie"),
    "cap": two("Eagle Flies at the end of \"American Fathers II\".","Eagle Flies à la fin de \"American Fathers II\".")},
 ],
},
# ======================== 50. SISTER CALDERON ========================
{
 "order": 50, "slug": "sister-calderon", "name": "Sister Calderón",
 "publishDate": "2026-10-29", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Nun &middot; RDR1 &amp; 2", "reg_role_fr": "Religieuse &middot; RDR1 &amp; 2",
 "gender": "Female", "death": None, "nationality": None,
 "portrait_alt": two("Sister Calderón in Saint Denis in Red Dead Redemption 2",
                     "Sœur Calderón à Saint-Denis dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Saint Denis", "Personnage &middot; Saint-Denis"),
 "meta_desc": two("Sister Calderón: the Catholic nun Arthur Morgan meets in Saint Denis in Red Dead Redemption 2, and the Mother Superior John Marston meets in Mexico in Red Dead Redemption. Biography and key scenes.",
                  "Sœur Calderón : la religieuse catholique qu'Arthur Morgan rencontre à Saint-Denis dans Red Dead Redemption 2, et la mère supérieure que John Marston croise au Mexique dans Red Dead Redemption. Biographie et scènes clés."),
 "og_desc": two("The nun Arthur Morgan confides in at Emerald Station, and one of the few characters in both Red Dead games.",
                "La religieuse à qui Arthur Morgan se confie à Emerald Station, et l'un des rares personnages présents dans les deux Red Dead."),
 "schema_desc": two("Catholic nun in Saint Denis in Red Dead Redemption 2, and Mother Superior in Nuevo Paraiso in Red Dead Redemption.",
                    "Religieuse catholique à Saint-Denis dans Red Dead Redemption 2, et mère supérieure au Nuevo Paraíso dans Red Dead Redemption."),
 "chips": [two("Catholic Church", "Église catholique"), two("Saint Denis", "Saint-Denis"), two("RDR1 &amp; 2", "RDR1 &amp; 2")],
 "facts": [
   {"label": two("Role","Rôle"), "value": two("Nun, later Mother Superior","Religieuse, puis mère supérieure")},
   {"label": two("Church","Église"), "value": two("Church of the Holy Blessed Virgin, Saint Denis","Church of the Holy Blessed Virgin, Saint-Denis")},
   {"label": two("In 1911","En 1911"), "value": two("Las Hermanas convent, Nuevo Paraiso","Couvent de Las Hermanas, Nuevo Paraíso")},
   {"label": two("Status","Statut"), "value": two("Alive in 1911","Vivante en 1911")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2","Red Dead Redemption, Red Dead Redemption 2")},
 ],
 "intro": [
   two("Sister Calderón is a Catholic nun at the Church of the Holy Blessed Virgin in Saint Denis, in Red Dead Redemption 2. No first name is given for her in either game.",
       "Sœur Calderón est une religieuse catholique de la Church of the Holy Blessed Virgin, à Saint-Denis, dans Red Dead Redemption 2. Aucun des deux jeux ne lui donne de prénom."),
   two("She meets [[arthur-morgan|Arthur Morgan]] several times in 1899. In Red Dead Redemption, set in 1911, she is the Mother Superior of a convent in Mexico.",
       "Elle croise [[arthur-morgan|Arthur Morgan]] à plusieurs reprises en 1899. Dans Red Dead Redemption, qui se déroule en 1911, elle est mère supérieure d'un couvent au Mexique."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Brothers and Sisters, One and All","Brothers and Sisters, One and All")},
     {"p": two("In the Stranger mission \"Brothers and Sisters, One and All\", Brother Dorkins introduces Sister Calderón to Arthur while they teach street children to read. A boy steals her crucifix. Arthur gets it back and returns it to her at the cathedral.",
               "Dans la mission d'inconnu \"Brothers and Sisters, One and All\", frère Dorkins présente sœur Calderón à Arthur alors qu'ils apprennent à lire à des enfants des rues. Un garçon lui vole son crucifix. Arthur le récupère et le lui rapporte à la cathédrale.")},
     {"h3": two("Of Men and Angels","Of Men and Angels")},
     {"p": two("In \"Of Men and Angels\", she is collecting money and food for the poor outside the cathedral. Arthur gives either food or 10 dollars. She tells him that she was once like him; he replies that he is not a religious man. The mission is optional and must be completed before \"The Fine Art of Conversation\".",
               "Dans \"Of Men and Angels\", elle collecte de l'argent et de la nourriture pour les pauvres devant la cathédrale. Arthur donne de la nourriture ou 10 dollars. Elle lui confie qu'elle a été comme lui, autrefois ; il répond qu'il n'est pas croyant. Cette mission est facultative et doit être faite avant \"The Fine Art of Conversation\".")},
   ]},
   {"summary": two("Emerald Station","Emerald Station"), "blocks": [
     {"p": two("At the end of \"The Fine Art of Conversation\", in chapter 6, Arthur has a coughing fit at Emerald Station. Sister Calderón is there, boarding a train for Mexico, where she says she has been sent on a mission.",
               "À la fin de \"The Fine Art of Conversation\", au chapitre 6, Arthur est pris d'une quinte de toux à Emerald Station. Sœur Calderón s'y trouve : elle prend un train pour le Mexique, où elle dit être envoyée en mission.")},
     {"p": two("Arthur tells her that he is dying and that he is afraid. She answers: \"Take a gamble that love exists, and do a loving act.\" The scene requires high honor and the completion of \"Of Men and Angels\"; otherwise Reverend Swanson appears in her place. With high honor, her words can come back to Arthur during the final mission.",
               "Arthur lui avoue qu'il va mourir et qu'il a peur. Elle lui répond de parier sur l'existence de l'amour et d'accomplir un acte d'amour. La scène suppose un honneur élevé et la mission \"Of Men and Angels\" terminée ; sinon, c'est le révérend Swanson qui apparaît à sa place. Avec un honneur élevé, ses paroles peuvent revenir à Arthur pendant la dernière mission.")},
   ]},
   {"summary": two("In Red Dead Redemption","Dans Red Dead Redemption"), "blocks": [
     {"p": two("In 1911, she is the Mother Superior of the convent at Las Hermanas, in the Perdido region of Nuevo Paraiso. [[john-marston|John Marston]] can meet her there while she collects money for the poor, and choose to give or to rob her. She also appears in Undead Nightmare (2010), an expansion outside the series' canon.",
               "En 1911, elle est mère supérieure du couvent de Las Hermanas, dans la région de Perdido, au Nuevo Paraíso. [[john-marston|John Marston]] peut l'y croiser pendant qu'elle collecte de l'argent pour les pauvres, et choisir de lui donner ou de la voler. Elle apparaît aussi dans Undead Nightmare (2010), une extension hors de la continuité officielle.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Sister Calderón is voiced by Irene DeBari in Red Dead Redemption 2.",
               "Sœur Calderón est doublée par Irene DeBari dans Red Dead Redemption 2.")},
   ]},
 ],
 "relationships": [
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("Confides in her that he is dying, at Emerald Station.",
                "Lui confie à Emerald Station qu'il va mourir.")},
   {"name": "Orville Swanson", "slug": "orville-swanson", "img": "swanson.jpeg",
    "text": two("Takes her place at the station if Arthur's honor is low.",
                "La remplace à la gare si l'honneur d'Arthur est bas.")},
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("Meets her at Las Hermanas in 1911.",
                "La croise à Las Hermanas en 1911.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("The Mother Superior at the Las Hermanas convent in Red Dead Redemption","La mère supérieure au couvent de Las Hermanas dans Red Dead Redemption"),
    "cap": two("As Mother Superior at Las Hermanas, in Red Dead Redemption (1911).","En mère supérieure à Las Hermanas, dans Red Dead Redemption (1911).")},
 ],
},
]

# "More characters" ccards. Only characters already live on each fiche's publishDate.
RELATED = {
 "catherine-braithwaite": ["angelo-bronte", "jack-marston", "sean-macguire", "dutch-van-der-linde"],
 "tavish-gray":           ["catherine-braithwaite", "sean-macguire", "arthur-morgan", "dutch-van-der-linde"],
 "alberto-fussar":        ["leviticus-cornwall", "javier-escuella", "dutch-van-der-linde", "micah-bell"],
 "hercule-fontaine":      ["alberto-fussar", "dutch-van-der-linde", "micah-bell", "bill-williamson"],
 "rains-fall":            ["charles-smith", "arthur-morgan", "leviticus-cornwall", "dutch-van-der-linde"],
 "eagle-flies":           ["rains-fall", "charles-smith", "arthur-morgan", "dutch-van-der-linde"],
 "sister-calderon":       ["arthur-morgan", "orville-swanson", "john-marston", "rains-fall"],
}

# Characters this wave links to that gen_fiche's base REGISTRY does not carry.
EXTRA_REG = [
 ("jack-marston",       "Jack Marston",       "Marston family &middot; RDR1 &amp; 2", "Famille Marston &middot; RDR1 &amp; 2"),
 ("javier-escuella",    "Javier Escuella",    "Van der Linde gang &middot; RDR1 &amp; 2", "Gang Van der Linde &middot; RDR1 &amp; 2"),
 ("angelo-bronte",      "Angelo Bronte",      "Crime boss &middot; RDR2",          "Parrain &middot; RDR2"),
 ("leviticus-cornwall", "Leviticus Cornwall", "Industrialist &middot; RDR2",       "Industriel &middot; RDR2"),
 ("orville-swanson",    "Orville Swanson",    "Van der Linde gang &middot; RDR2",  "Gang Van der Linde &middot; RDR2"),
 ("sean-macguire",      "Sean MacGuire",      "Van der Linde gang &middot; RDR2",  "Gang Van der Linde &middot; RDR2"),
]

if __name__ == "__main__":
    from gen_fiche import reg
    from characters_registry import CHARACTERS as REG
    roles = {s: (n, en, fr) for s, n, en, fr, _g in REG}
    for slug, name, en, fr in EXTRA_REG:
        n, en, fr = roles.get(slug, (name, en, fr))  # registry wording wins
        reg(slug, n, en, fr)
    for c in CHARS:
        reg(c["slug"], c["name"], c["reg_role_en"], c["reg_role_fr"])
    for c in CHARS:
        c["related"] = RELATED[c["slug"]]
        folder = build_to_queue(c)
        print("wrote", folder)
