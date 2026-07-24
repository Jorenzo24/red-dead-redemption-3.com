#!/usr/bin/env python3
"""Wave 4 content -> _queue/. Run: python scripts/_wave4.py
Not deployed (scripts/ is excluded from .cpanel.yml).

Six RDR1 (1911) fiches: Bonnie MacFarlane, Landon Ricketts, Nigel West Dickens,
Seth Briars, Marshal Leigh Johnson, Abraham Reyes. Factual register (no mood-prose),
FR written natively. Images already staged in assets/characters/<slug>/.
Five survive RDR1; only Landon Ricketts dies (off-screen, old age, reported 1914).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fiche import build_to_queue

def two(en, fr): return {"en": en, "fr": fr}

CHARS = [
# ============================ 18. BONNIE MacFARLANE ============================
{
 "order": 18, "slug": "bonnie-macfarlane", "name": "Bonnie MacFarlane",
 "publishDate": "2026-07-27", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Rancher &middot; RDR1", "reg_role_fr": "Ranchère &middot; RDR1",
 "gender": "Female", "death": None, "nationality": "American",
 "portrait_alt": two("Bonnie MacFarlane in Red Dead Redemption", "Bonnie MacFarlane dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; New Austin", "Personnage &middot; New Austin"),
 "meta_desc": two("Bonnie MacFarlane: the rancher's daughter who finds John Marston shot and left for dead and nurses him back to health in Red Dead Redemption. Biography and fate.",
                  "Bonnie MacFarlane : la fille de rancher qui trouve John Marston blessé et laissé pour mort et le remet sur pied dans Red Dead Redemption. Biographie et destin."),
 "og_desc": two("The rancher's daughter who saves John Marston at the start of Red Dead Redemption.",
                "La fille de rancher qui sauve John Marston au début de Red Dead Redemption."),
 "schema_desc": two("Rancher's daughter who rescues John Marston in Red Dead Redemption.",
                    "Fille de rancher qui sauve John Marston dans Red Dead Redemption."),
 "chips": [two("Born <strong>c. 1884</strong>", "Née <strong>v. 1884</strong>"), two("Alive", "Vivante"),
           two("Rancher", "Ranchère"), two("New Austin", "New Austin")],
 "facts": [
   {"label": two("Born","Née"), "value": two("c. 1884","v. 1884")},
   {"label": two("Status","Statut"), "value": two("Alive (end of RDR1)","Vivante (fin de RDR1)")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Home","Domicile"), "value": two("MacFarlane's Ranch, New Austin","MacFarlane's Ranch, New Austin")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Bonnie MacFarlane is the daughter of the rancher Drew MacFarlane and one of the first people [[john-marston|John Marston]] meets in Red Dead Redemption. She finds John shot and left for dead after his failed confrontation with [[bill-williamson|Bill Williamson]] at Fort Mercer, and nurses him back to health at MacFarlane's Ranch.",
       "Bonnie MacFarlane est la fille du rancher Drew MacFarlane et l'une des premières personnes que [[john-marston|John Marston]] rencontre dans Red Dead Redemption. Elle trouve John blessé par balle et laissé pour mort après son échec face à [[bill-williamson|Bill Williamson]] à Fort Mercer, et le remet sur pied à MacFarlane's Ranch."),
   two("She lives and works at the ranch in Hennigan's Stead, in the state of New Austin, and becomes John's closest ally during his time in the territory.",
       "Elle vit et travaille au ranch de Hennigan's Stead, dans l'état de New Austin, et devient l'alliée la plus proche de John pendant son séjour dans le territoire."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Saving John Marston","Elle sauve John Marston")},
     {"p": two("Bonnie finds John wounded near the ranch, pays a doctor fifteen dollars to treat him, and lets him recover in exchange for ranch work. He earns his keep breaking horses, herding cattle and clearing rustlers across Hennigan's Stead.",
               "Bonnie trouve John blessé près du ranch, paie quinze dollars à un médecin pour le soigner, et le laisse se rétablir en échange de travail au ranch. Il gagne son gîte en dressant des chevaux, en menant le bétail et en chassant les voleurs à travers Hennigan's Stead.")},
     {"h3": two("The barn and the hanging","La grange et la pendaison")},
     {"p": two("In \"The Burning\", [[bill-williamson|Williamson]]'s men set the ranch barn on fire and John rescues the horses. In \"Hanging Bonnie MacFarlane\", the gang kidnaps her and tries to hang her at Tumbleweed to trade for a jailed ally; John saves her, and Marshal Leigh Johnson takes her back to Armadillo.",
               "Dans « The Burning », les hommes de [[bill-williamson|Williamson]] mettent le feu à la grange du ranch et John sauve les chevaux. Dans « Hanging Bonnie MacFarlane », le gang l'enlève et tente de la pendre à Tumbleweed pour l'échanger contre un allié emprisonné ; John la sauve, et le marshal Leigh Johnson la ramène à Armadillo.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Bonnie is practical, tough and proud of the ranch her family built. She is the one person John willingly tells about his outlaw past.",
               "Bonnie est pragmatique, endurante et fière du ranch bâti par sa famille. Elle est la seule personne à qui John raconte de son plein gré son passé de hors-la-loi.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Bonnie survives the events of Red Dead Redemption. After [[dutch-van-der-linde|Dutch]] is dealt with, John buys cattle from her and she helps herd them toward Beecher's Hope, where she meets [[abigail-marston|Abigail]]. Her fate is left open; the ranch is still operating in 1914.",
               "Bonnie survit aux événements de Red Dead Redemption. Une fois [[dutch-van-der-linde|Dutch]] réglé, John lui achète du bétail et elle l'aide à le mener vers Beecher's Hope, où elle rencontre [[abigail-marston|Abigail]]. Son destin reste ouvert ; le ranch fonctionne toujours en 1914.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Bonnie MacFarlane appears in Red Dead Redemption (2010) and its 2024 remaster, and returns as a Stranger in Red Dead Online, set in 1898. She is voiced by Kimberly Irion.",
               "Bonnie MacFarlane apparaît dans Red Dead Redemption (2010) et son remaster de 2024, et revient comme personnage secondaire dans Red Dead Online, situé en 1898. Elle est doublée par Kimberly Irion.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("She is named after the aunt of a Rockstar San Diego designer.","Elle porte le nom de la tante d'un concepteur de Rockstar San Diego."),
       two("Game Informer ranked her #29 among characters who defined the decade.","Game Informer l'a classée 29e parmi les personnages ayant marqué la décennie."),
       two("In Red Dead Redemption 2, a dying man near Van Horn carries a letter addressed to her.","Dans Red Dead Redemption 2, un mourant près de Van Horn porte une lettre qui lui est adressée."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("The outlaw she finds shot and nurses back to health; her closest tie in the game.",
                "Le hors-la-loi qu'elle trouve blessé et remet sur pied ; son lien le plus fort dans le jeu.")},
   {"name": "Bill Williamson", "slug": "bill-williamson", "img": "bill.jpeg",
    "text": two("The outlaw whose gang burns her barn and later kidnaps her.",
                "Le hors-la-loi dont le gang brûle sa grange puis l'enlève.")},
   {"name": "Leigh Johnson", "slug": None, "img": "leigh.jpeg",
    "text": two("The marshal who helps rescue her and returns her to Armadillo.",
                "Le marshal qui participe à son sauvetage et la ramène à Armadillo.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Bonnie MacFarlane at MacFarlane's Ranch","Bonnie MacFarlane à MacFarlane's Ranch"),
    "cap": two("Bonnie at the family ranch in Hennigan's Stead.","Bonnie au ranch familial de Hennigan's Stead.")},
 ],
},
# ============================ 19. LANDON RICKETTS ============================
{
 "order": 19, "slug": "landon-ricketts", "name": "Landon Ricketts",
 "publishDate": "2026-07-30", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Gunslinger &middot; RDR1", "reg_role_fr": "Pistolero &middot; RDR1",
 "gender": "Male", "death": "1911", "nationality": "American",
 "portrait_alt": two("Landon Ricketts in Red Dead Redemption", "Landon Ricketts dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; Nuevo Paraíso", "Personnage &middot; Nuevo Paraíso"),
 "meta_desc": two("Landon Ricketts: the ageing legendary gunslinger who mentors John Marston in Mexico in Red Dead Redemption. Biography, missions and death.",
                  "Landon Ricketts : le vieux pistolero légendaire qui forme John Marston au Mexique dans Red Dead Redemption. Biographie, missions et mort."),
 "og_desc": two("The ageing gunslinger who teaches John Marston in Mexico, then dies of old age.",
                "Le vieux pistolero qui forme John Marston au Mexique, avant de mourir de vieillesse."),
 "schema_desc": two("Ageing legendary gunslinger who mentors John Marston in Red Dead Redemption.",
                    "Vieux pistolero légendaire qui forme John Marston dans Red Dead Redemption."),
 "chips": [two("Born <strong>c. 1861</strong>", "Né <strong>v. 1861</strong>"), two("Deceased", "Décédé"),
           two("Gunslinger", "Pistolero"), two("Chuparosa", "Chuparosa")],
 "facts": [
   {"label": two("Born","Né"), "value": two("c. 1861","v. 1861")},
   {"label": two("Died","Mort"), "value": two("c. 1911 (reported 1914)","v. 1911 (rapporté en 1914)")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Landon Ricketts is an ageing, legendary gunslinger living in the town of Chuparosa, in Nuevo Paraíso, Mexico. Past his prime but still the fastest gun around, he acts as the town's unofficial protector and becomes [[john-marston|John Marston]]'s mentor during his time south of the border.",
       "Landon Ricketts est un vieux pistolero légendaire installé dans la ville de Chuparosa, à Nuevo Paraíso, au Mexique. Sur le déclin mais toujours la gâchette la plus rapide des environs, il fait office de protecteur officieux de la ville et devient le mentor de [[john-marston|John Marston]] durant son séjour au sud de la frontière."),
   two("He teaches John the finer points of gunfighting and helps him fight the forces of Colonel Agustín Allende.",
       "Il enseigne à John les subtilités du duel au pistolet et l'aide à combattre les forces du colonel Agustín Allende."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The mentor in Chuparosa","Le mentor de Chuparosa")},
     {"p": two("In \"The Gunslinger's Tragedy\", Ricketts watches [[john-marston|John]] kill three would-be robbers, then gives him a Schofield Revolver and teaches him the third level of Dead Eye. In \"Landon Ricketts Rides Again\", the two break Luisa Fortuna out of a government jail under heavy fire.",
               "Dans « The Gunslinger's Tragedy », Ricketts voit [[john-marston|John]] abattre trois détrousseurs, puis lui offre un revolver Schofield et lui enseigne le troisième niveau de Dead Eye. Dans « Landon Ricketts Rides Again », tous deux font évader Luisa Fortuna d'une prison gouvernementale sous le feu.")},
     {"h3": two("The wagon train","Le convoi")},
     {"p": two("In \"The Mexican Wagon Train\", Ricketts and John ambush a prison convoy sent to execute peasants on Allende's orders, driving the wagons to the US border to free the prisoners. The two then say their goodbyes.",
               "Dans « The Mexican Wagon Train », Ricketts et John tendent une embuscade à un convoi de prisonniers envoyé pour exécuter des paysans sur ordre d'Allende, et conduisent les chariots jusqu'à la frontière américaine pour libérer les captifs. Les deux hommes se disent alors adieu.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Ricketts is calm, principled and world-weary. He kills only when he must, and carries the manner of a man who has outlived the era that made him famous.",
               "Ricketts est calme, droit et las du monde. Il ne tue que lorsqu'il le faut, et porte l'allure d'un homme qui a survécu à l'époque qui l'a rendu célèbre.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Ricketts survives every mission and parts ways with John. He returns to the United States and, according to an 1914 Blackwater Ledger article, dies quietly in his sleep of old age. He is the only one of John's Red Dead Redemption allies to die within the story's span.",
               "Ricketts survit à toutes les missions et se sépare de John. Il rentre aux États-Unis et, d'après un article du Blackwater Ledger de 1914, s'éteint paisiblement dans son sommeil, de vieillesse. Il est le seul des alliés de John dans Red Dead Redemption à mourir dans l'intervalle de l'histoire.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Landon Ricketts appears in Red Dead Redemption (2010) and its 2024 remaster. He is voiced by Ross Hagen, in his final role; Hagen died in 2011. The character is modelled on figures like Wyatt Earp and Wild Bill Hickok.",
               "Landon Ricketts apparaît dans Red Dead Redemption (2010) et son remaster de 2024. Il est doublé par Ross Hagen, dans son dernier rôle ; Hagen est mort en 2011. Le personnage s'inspire de figures comme Wyatt Earp et Wild Bill Hickok.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("His attire is inspired by Lee Van Cleef's character in the western Day of Anger (1967).","Sa tenue s'inspire du personnage de Lee Van Cleef dans le western Le Dernier jour de la colère (1967)."),
       two("His famous kills include the Butcher Brothers, in 1896.","Parmi ses tueries célèbres figurent les Butcher Brothers, en 1896."),
       two("He teaches John the third and final level of the Dead Eye targeting skill.","Il enseigne à John le troisième et dernier niveau de la compétence de visée Dead Eye."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("His pupil in Mexico; Ricketts teaches him gunfighting and rides with him against Allende.",
                "Son élève au Mexique ; Ricketts lui apprend le duel au pistolet et chevauche avec lui contre Allende.")},
   {"name": "Luisa Fortuna", "slug": None, "img": "luisa.jpeg",
    "text": two("The young rebel he and John break out of a government jail.",
                "La jeune rebelle que lui et John font évader d'une prison gouvernementale.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Landon Ricketts in Chuparosa","Landon Ricketts à Chuparosa"),
    "cap": two("Ricketts, the ageing gunslinger of Chuparosa.","Ricketts, le vieux pistolero de Chuparosa.")},
 ],
},
# ============================ 20. NIGEL WEST DICKENS ============================
{
 "order": 20, "slug": "nigel-west-dickens", "name": "Nigel West Dickens",
 "publishDate": "2026-08-02", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Con-artist &middot; RDR1", "reg_role_fr": "Escroc &middot; RDR1",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Nigel West Dickens in Red Dead Redemption", "Nigel West Dickens dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; New Austin", "Personnage &middot; New Austin"),
 "meta_desc": two("Nigel West Dickens: the snake-oil con-artist who becomes John Marston's unlikely ally in Red Dead Redemption. Biography, the Fort Mercer plan and fate.",
                  "Nigel West Dickens : l'escroc vendeur d'élixir qui devient l'allié improbable de John Marston dans Red Dead Redemption. Biographie, le plan de Fort Mercer et destin."),
 "og_desc": two("The snake-oil salesman who connects John Marston's allies for the assault on Fort Mercer.",
                "Le vendeur d'élixir qui réunit les alliés de John Marston pour l'assaut de Fort Mercer."),
 "schema_desc": two("Snake-oil con-artist and reluctant ally of John Marston in Red Dead Redemption.",
                    "Escroc vendeur d'élixir et allié réticent de John Marston dans Red Dead Redemption."),
 "chips": [two("Born <strong>c. 1846</strong>", "Né <strong>v. 1846</strong>"), two("Alive", "Vivant"),
           two("Con-artist", "Escroc"), two("New Austin", "New Austin")],
 "facts": [
   {"label": two("Born","Né"), "value": two("c. 1846, Fort Wayne, Indiana","v. 1846, Fort Wayne, Indiana")},
   {"label": two("Status","Statut"), "value": two("Alive (end of RDR1)","Vivant (fin de RDR1)")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Trade","Métier"), "value": two("Travelling elixir salesman","Vendeur d'élixir itinérant")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Nigel West Dickens is a travelling con-artist who sells fraudulent miracle \"elixirs\" from an ornate stagecoach across New Austin. Despite [[john-marston|John Marston]]'s dislike of him, he becomes a central ally in the plan to assault Fort Mercer.",
       "Nigel West Dickens est un escroc itinérant qui vend de faux élixirs miracles depuis une diligence ornée à travers New Austin. Malgré l'aversion de [[john-marston|John Marston]] à son égard, il devient un allié central dans le plan d'assaut de Fort Mercer."),
   two("An American who affects a fake English accent, he is the man who connects John with Seth Briars and the smuggler Irish.",
       "Américain qui se donne un faux accent anglais, il est l'homme qui met John en relation avec Seth Briars et le contrebandier Irish."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Rescued in the sun","Sauvé en plein soleil")},
     {"p": two("In \"Old Swindler Blues\", [[john-marston|John]] finds Dickens shot and left in the sun near his stagecoach south of Coot's Chapel, and hauls him to the Armadillo doctor while fighting off bandits. Dickens then becomes the networker who assembles John's allies.",
               "Dans « Old Swindler Blues », [[john-marston|John]] trouve Dickens blessé et abandonné en plein soleil près de sa diligence, au sud de Coot's Chapel, et le ramène au médecin d'Armadillo en repoussant des bandits. Dickens devient alors l'entremetteur qui réunit les alliés de John.")},
     {"h3": two("The Trojan horse","Le cheval de Troie")},
     {"p": two("In \"The Assault on Fort Mercer\", Dickens supplies his armoured stagecoach for a Trojan-horse attack that wipes out [[bill-williamson|Williamson]]'s gang, though Williamson has already fled to Mexico. Later, John finds Dickens arrested in Blackwater for narcotics and vouches for him.",
               "Dans « The Assault on Fort Mercer », Dickens fournit sa diligence blindée pour une attaque en cheval de Troie qui anéantit le gang de [[bill-williamson|Williamson]], même si Williamson a déjà fui au Mexique. Plus tard, John trouve Dickens arrêté à Blackwater pour trafic de stupéfiants et se porte garant pour lui.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Dickens is a charming, cowardly fraud who plays the refined English gentleman. His elixir is little more than alcohol laced with opium.",
               "Dickens est un escroc charmeur et lâche qui joue au gentleman anglais raffiné. Son élixir n'est guère plus que de l'alcool additionné d'opium.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Dickens survives Red Dead Redemption. After [[john-marston|John]] vouches for him in Blackwater, [[edgar-ross|Agent Edgar Ross]] sarcastically calls him a hero and he walks free.",
               "Dickens survit à Red Dead Redemption. Après que [[john-marston|John]] s'est porté garant pour lui à Blackwater, [[edgar-ross|l'agent Edgar Ross]] le qualifie ironiquement de héros et il repart libre.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Nigel West Dickens appears in Red Dead Redemption (2010) and its 2024 remaster. He is voiced by Don Creech, and his manner is based on the comedian W.C. Fields.",
               "Nigel West Dickens apparaît dans Red Dead Redemption (2010) et son remaster de 2024. Il est doublé par Don Creech, et ses manières s'inspirent du comique W.C. Fields.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("Red Dead Redemption 2 mentions him in an Annesburg anecdote: a woman runs him out of town with a shotgun after his elixir addicts her elderly parents.","Red Dead Redemption 2 le mentionne dans une anecdote à Annesburg : une femme le chasse de la ville au fusil après que son élixir a rendu ses parents âgés dépendants."),
       two("He has a scar across his neck, implying he was once nearly lynched as a con man.","Il porte une cicatrice au cou, laissant entendre qu'il a failli être lynché comme escroc."),
       two("His fake English accent hides an origin in Fort Wayne, Indiana.","Son faux accent anglais masque une origine à Fort Wayne, dans l'Indiana."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("The gunman he recruits into the Fort Mercer plan, and who later vouches for him in Blackwater.",
                "Le tireur qu'il enrôle dans le plan de Fort Mercer, et qui se porte garant pour lui à Blackwater.")},
   {"name": "Seth Briars", "slug": None, "img": "seth.jpeg",
    "text": two("The grave-robber he introduces to John as part of the plan.",
                "Le pilleur de tombes qu'il présente à John dans le cadre du plan.")},
   {"name": "Edgar Ross", "slug": "edgar-ross", "img": "ross.jpeg",
    "text": two("The Bureau agent who releases him in Blackwater once John speaks for him.",
                "L'agent du Bureau qui le relâche à Blackwater une fois que John a parlé en sa faveur.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Nigel West Dickens and his stagecoach","Nigel West Dickens et sa diligence"),
    "cap": two("Dickens and the armoured coach used to assault Fort Mercer.","Dickens et la diligence blindée servant à l'assaut de Fort Mercer.")},
 ],
},
# ============================ 21. SETH BRIARS ============================
{
 "order": 21, "slug": "seth-briars", "name": "Seth Briars",
 "publishDate": "2026-08-05", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Grave-robber &middot; RDR1", "reg_role_fr": "Pilleur de tombes &middot; RDR1",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Seth Briars in Red Dead Redemption", "Seth Briars dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; New Austin", "Personnage &middot; New Austin"),
 "meta_desc": two("Seth Briars: the deranged grave-robber and treasure hunter who helps John Marston in Red Dead Redemption. Biography, the treasure map and fate.",
                  "Seth Briars : le pilleur de tombes dément et chasseur de trésor qui aide John Marston dans Red Dead Redemption. Biographie, la carte au trésor et destin."),
 "og_desc": two("The unhinged grave-robber who helps John Marston in exchange for chasing a treasure.",
                "Le pilleur de tombes dérangé qui aide John Marston en échange d'une chasse au trésor."),
 "schema_desc": two("Deranged grave-robber and treasure hunter in Red Dead Redemption.",
                    "Pilleur de tombes dément et chasseur de trésor dans Red Dead Redemption."),
 "chips": [two("Born <strong>1870s</strong>", "Né dans les <strong>années 1870</strong>"), two("Alive", "Vivant"),
           two("Grave-robber", "Pilleur de tombes"), two("New Austin", "New Austin")],
 "facts": [
   {"label": two("Born","Né"), "value": two("Early 1870s","Début des années 1870")},
   {"label": two("Status","Statut"), "value": two("Alive (end of RDR1)","Vivant (fin de RDR1)")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Obsession","Obsession"), "value": two("Buried treasure","Trésor enfoui")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Seth Briars is a deranged grave-robber and treasure hunter [[john-marston|John Marston]] recruits for the assault on Fort Mercer. Unstable and obsessive, he agrees to help only if John first recovers his stolen treasure map.",
       "Seth Briars est un pilleur de tombes dément et chasseur de trésor que [[john-marston|John Marston]] recrute pour l'assaut de Fort Mercer. Instable et obsédé, il n'accepte d'aider que si John récupère d'abord sa carte au trésor volée."),
   two("[[nigel-west-dickens|Nigel West Dickens]] points John toward Seth, whom he finds digging up graves in the cemeteries of New Austin.",
       "[[nigel-west-dickens|Nigel West Dickens]] oriente John vers Seth, qu'il trouve en train de déterrer des tombes dans les cimetières de New Austin."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The stolen map","La carte volée")},
     {"p": two("In \"Exhuming and Other Fine Hobbies\", Seth agrees to help [[john-marston|John]] only if John helps recover the half of his treasure map stolen by his former partner Moses Forth. They force the location out of Moses, then escort a wagon of exhumed corpses to Tumbleweed to find the map's other half.",
               "Dans « Exhuming and Other Fine Hobbies », Seth n'accepte d'aider [[john-marston|John]] que si celui-ci l'aide à récupérer la moitié de sa carte au trésor volée par son ancien associé Moses Forth. Ils arrachent la position à Moses, puis escortent un chariot de cadavres exhumés jusqu'à Tumbleweed pour trouver l'autre moitié de la carte.")},
     {"h3": two("The glass eye","L'œil de verre")},
     {"p": two("In \"Let the Dead Bury Their Dead\", the two raid a Tumbleweed mansion for the treasure, only to open the chest and find a single glass eye. Seth is devastated, but honours his word and helps take Fort Mercer.",
               "Dans « Let the Dead Bury Their Dead », les deux hommes pillent un manoir de Tumbleweed pour le trésor, avant d'ouvrir le coffre et d'y trouver un seul œil de verre. Seth est anéanti, mais tient parole et aide à prendre Fort Mercer.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Seth is filthy, obsessive and visibly unwell, talking to corpses and to himself. He says he prefers the dead to the living.",
               "Seth est crasé, obsédé et visiblement malade, parlant aux cadavres et à lui-même. Il dit préférer les morts aux vivants.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Seth survives Red Dead Redemption. An 1914 newspaper reports that he hauled a sack of real gold and jewels into Blackwater, found deep in Tall Trees, at last striking the fortune his obsession promised.",
               "Seth survit à Red Dead Redemption. Un journal de 1914 rapporte qu'il a ramené à Blackwater un sac d'or et de bijoux bien réels, découverts au fond de Tall Trees, trouvant enfin la fortune que son obsession lui promettait.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Seth Briars appears in Red Dead Redemption (2010) and its 2024 remaster. He is voiced by Kevin Glikmann. Rob Wiethoff, who plays John Marston, has named Seth his favourite character in the game.",
               "Seth Briars apparaît dans Red Dead Redemption (2010) et son remaster de 2024. Il est doublé par Kevin Glikmann. Rob Wiethoff, l'interprète de John Marston, a désigné Seth comme son personnage préféré du jeu.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("The treasure chest he chases across the story contains only a glass eye.","Le coffre au trésor qu'il poursuit tout au long de l'histoire ne contient qu'un œil de verre."),
       two("His split-personality behaviour and monologues suggest serious mental illness.","Son comportement à double personnalité et ses monologues évoquent une grave maladie mentale."),
       two("In-game newspapers wrongly credit his former partner Moses Forth for the grave-robbings.","Les journaux du jeu attribuent à tort les pillages de tombes à son ancien associé Moses Forth."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("The gunman who chases his treasure with him in exchange for his help at Fort Mercer.",
                "Le tireur qui traque son trésor avec lui en échange de son aide à Fort Mercer.")},
   {"name": "Nigel West Dickens", "slug": "nigel-west-dickens", "img": "nigel.jpeg",
    "text": two("The con-artist who introduces Seth to John.",
                "L'escroc qui présente Seth à John.")},
   {"name": "Moses Forth", "slug": None, "img": "moses.jpeg",
    "text": two("His former partner, who stole half of the treasure map.",
                "Son ancien associé, qui a volé la moitié de la carte au trésor.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Seth Briars digging at a grave","Seth Briars creusant une tombe"),
    "cap": two("Seth at work in a New Austin cemetery.","Seth à l'œuvre dans un cimetière de New Austin.")},
 ],
},
# ============================ 22. LEIGH JOHNSON ============================
{
 "order": 22, "slug": "leigh-johnson", "name": "Leigh Johnson",
 "publishDate": "2026-08-08", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Marshal &middot; RDR1", "reg_role_fr": "Marshal &middot; RDR1",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Marshal Leigh Johnson in Red Dead Redemption", "Le marshal Leigh Johnson dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; Armadillo", "Personnage &middot; Armadillo"),
 "meta_desc": two("Leigh Johnson: the weary, principled Marshal of Armadillo who partners with John Marston in Red Dead Redemption. Biography, missions and fate.",
                  "Leigh Johnson : le marshal d'Armadillo, las mais intègre, qui fait équipe avec John Marston dans Red Dead Redemption. Biographie, missions et destin."),
 "og_desc": two("The Marshal of Armadillo who helps John Marston clean up New Austin.",
                "Le marshal d'Armadillo qui aide John Marston à nettoyer New Austin."),
 "schema_desc": two("Marshal of Armadillo and ally of John Marston in Red Dead Redemption.",
                    "Marshal d'Armadillo et allié de John Marston dans Red Dead Redemption."),
 "chips": [two("Born <strong>c. 1860</strong>", "Né <strong>v. 1860</strong>"), two("Alive", "Vivant"),
           two("Marshal", "Marshal"), two("Armadillo", "Armadillo")],
 "facts": [
   {"label": two("Born","Né"), "value": two("c. 1860","v. 1860")},
   {"label": two("Status","Statut"), "value": two("Alive (retires 1914)","Vivant (retraité en 1914)")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Role","Rôle"), "value": two("Marshal of Armadillo","Marshal d'Armadillo")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Leigh Johnson is the Marshal of Armadillo, a weary but principled lawman who partners with [[john-marston|John Marston]] in the state of New Austin. He agrees to help John hunt [[bill-williamson|Bill Williamson]] in exchange for John's help cleaning up the territory.",
       "Leigh Johnson est le marshal d'Armadillo, un représentant de la loi las mais intègre qui fait équipe avec [[john-marston|John Marston]] dans l'état de New Austin. Il accepte d'aider John à traquer [[bill-williamson|Bill Williamson]] en échange de son aide pour nettoyer le territoire."),
   two("He works his jurisdiction with two loyal deputies, Jonah and Eli.",
       "Il tient sa juridiction avec deux adjoints fidèles, Jonah et Eli."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("A lawman's bargain","Le marché d'un homme de loi")},
     {"p": two("In \"Political Realities in Armadillo\", Johnson agrees to help [[john-marston|John]] find [[bill-williamson|Williamson]] if John helps clean up New Austin. Together they track Walton's Gang, clear the Bollard Twins from Pike's Basin, and capture Williamson's second-in-command Norman Deek after the Ridgewood Farm raid.",
               "Dans « Political Realities in Armadillo », Johnson accepte d'aider [[john-marston|John]] à retrouver [[bill-williamson|Williamson]] si John l'aide à nettoyer New Austin. Ensemble, ils traquent le gang de Walton, chassent les Bollard Twins de Pike's Basin, et capturent le bras droit de Williamson, Norman Deek, après le raid de Ridgewood Farm.")},
     {"h3": two("Fort Mercer","Fort Mercer")},
     {"p": two("Johnson leads the Tumbleweed prisoner exchange for [[bonnie-macfarlane|Bonnie MacFarlane]], which he correctly reads as a trap, and joins the assault on Fort Mercer. When Williamson is found to have fled to Mexico, Johnson and John part ways.",
               "Johnson mène l'échange de prisonniers de Tumbleweed pour [[bonnie-macfarlane|Bonnie MacFarlane]], qu'il devine à juste titre être un piège, et se joint à l'assaut de Fort Mercer. Lorsqu'on découvre que Williamson a fui au Mexique, Johnson et John se séparent.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Johnson is a tired, cynical southern gentleman who has held his post for years. He is decent under the weariness, and takes the safety of Armadillo seriously.",
               "Johnson est un gentleman du Sud fatigué et cynique, en poste depuis des années. Sous la lassitude, il reste droit, et prend au sérieux la sécurité d'Armadillo.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Johnson survives Red Dead Redemption. He steps down as marshal in 1914 after seventeen years, and says he intends to move as far from Armadillo as he can.",
               "Johnson survit à Red Dead Redemption. Il quitte son poste de marshal en 1914 après dix-sept ans, et dit vouloir partir aussi loin d'Armadillo que possible.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Leigh Johnson appears in Red Dead Redemption (2010) and its 2024 remaster. He is voiced by Anthony De Longis. The Game of the Year guide describes him as a fifty-year-old ageing cynic.",
               "Leigh Johnson apparaît dans Red Dead Redemption (2010) et son remaster de 2024. Il est doublé par Anthony De Longis. Le guide Game of the Year le décrit comme un cynique vieillissant de cinquante ans.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He is a widower; his wife Priscilla died in 1903.","Il est veuf ; sa femme Priscilla est morte en 1903."),
       two("A race course in the Liars and Cheats add-on, \"L. Johnson's Run\", is named after him.","Un circuit de course de l'extension Liars and Cheats, « L. Johnson's Run », porte son nom."),
       two("He works alongside his deputies Jonah and Eli throughout the New Austin missions.","Il agit aux côtés de ses adjoints Jonah et Eli tout au long des missions de New Austin."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("His partner in New Austin; they trade help hunting Williamson for cleaning up the territory.",
                "Son équipier dans New Austin ; ils échangent l'aide pour traquer Williamson contre le nettoyage du territoire.")},
   {"name": "Bill Williamson", "slug": "bill-williamson", "img": "bill.jpeg",
    "text": two("The outlaw they hunt across New Austin before he flees to Mexico.",
                "Le hors-la-loi qu'ils traquent à travers New Austin avant qu'il ne fuie au Mexique.")},
   {"name": "Bonnie MacFarlane", "slug": "bonnie-macfarlane", "img": "bonnie.jpeg",
    "text": two("The rancher he helps rescue at Tumbleweed and returns to Armadillo.",
                "La ranchère qu'il contribue à sauver à Tumbleweed et ramène à Armadillo.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Marshal Leigh Johnson in Armadillo","Le marshal Leigh Johnson à Armadillo"),
    "cap": two("Johnson, the Marshal of Armadillo.","Johnson, le marshal d'Armadillo.")},
 ],
},
# ============================ 23. ABRAHAM REYES ============================
{
 "order": 23, "slug": "abraham-reyes", "name": "Abraham Reyes",
 "publishDate": "2026-08-11", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Revolutionary &middot; RDR1", "reg_role_fr": "Révolutionnaire &middot; RDR1",
 "gender": "Male", "death": None, "nationality": "Mexican",
 "portrait_alt": two("Abraham Reyes in Red Dead Redemption", "Abraham Reyes dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; Nuevo Paraíso", "Personnage &middot; Nuevo Paraíso"),
 "meta_desc": two("Abraham Reyes: the charismatic Mexican revolutionary who allies with John Marston, then becomes a tyrant, in Red Dead Redemption. Biography and the betrayal.",
                  "Abraham Reyes : le révolutionnaire mexicain charismatique qui s'allie à John Marston, puis devient un tyran, dans Red Dead Redemption. Biographie et la trahison."),
 "og_desc": two("The Mexican revolutionary who wins his war, then betrays it and rules as a tyrant.",
                "Le révolutionnaire mexicain qui gagne sa guerre, puis la trahit et règne en tyran."),
 "schema_desc": two("Charismatic Mexican revolutionary leader who becomes a tyrant in Red Dead Redemption.",
                    "Chef révolutionnaire mexicain charismatique qui devient un tyran dans Red Dead Redemption."),
 "chips": [two("Born <strong>c. 1881</strong>", "Né <strong>v. 1881</strong>"), two("Alive", "Vivant"),
           two("Revolutionary", "Révolutionnaire"), two("Nuevo Paraíso", "Nuevo Paraíso")],
 "facts": [
   {"label": two("Born","Né"), "value": two("c. 1881","v. 1881")},
   {"label": two("Status","Statut"), "value": two("Alive (President of Mexico)","Vivant (président du Mexique)")},
   {"label": two("Nationality","Nationalité"), "value": two("Mexican","Mexicaine")},
   {"label": two("Role","Rôle"), "value": two("Revolutionary leader","Chef révolutionnaire")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Abraham Reyes is the charismatic leader of the Mexican revolution in Red Dead Redemption, and an ally of convenience to [[john-marston|John Marston]] in Nuevo Paraíso. Vain and self-serving beneath the speeches, he uses the rebellion to make himself ruler of Mexico.",
       "Abraham Reyes est le chef charismatique de la révolution mexicaine dans Red Dead Redemption, et un allié de circonstance de [[john-marston|John Marston]] à Nuevo Paraíso. Vaniteux et intéressé sous les discours, il se sert de la rébellion pour se faire maître du Mexique."),
   two("His path crosses John's because the rebellion helps John reach the fugitives [[bill-williamson|Bill Williamson]] and [[javier-escuella|Javier Escuella]].",
       "Sa route croise celle de John parce que la rébellion aide ce dernier à atteindre les fugitifs [[bill-williamson|Bill Williamson]] et [[javier-escuella|Javier Escuella]]."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Saved, and saving","Sauvé, et sauveur")},
     {"p": two("In \"Must a Savior Die?\", [[john-marston|John]] rescues Reyes from execution by the Mexican Army at El Presidio. Reyes later returns the favour, sniping the executioner about to kill John in Chuparosa. In \"The Great Mexican Train Robbery\", the two rob an army train, and Reyes speaks admiringly of John's old leader [[dutch-van-der-linde|Dutch van der Linde]].",
               "Dans « Must a Savior Die? », [[john-marston|John]] sauve Reyes d'une exécution par l'armée mexicaine à El Presidio. Reyes lui rend plus tard la pareille, abattant à la carabine le bourreau sur le point de tuer John à Chuparosa. Dans « The Great Mexican Train Robbery », les deux hommes braquent un train de l'armée, et Reyes parle avec admiration de l'ancien chef de John, [[dutch-van-der-linde|Dutch van der Linde]].")},
     {"h3": two("The march on Escalera","La marche sur Escalera")},
     {"p": two("In \"The Gates of El Presidio\", Reyes's rebels storm the fort so John can reach [[javier-escuella|Javier Escuella]]. In \"An Appointed Time\", they march on Escalera to overthrow Colonel Agustín Allende, and chase Allende's coach carrying [[bill-williamson|Bill Williamson]]; the player chooses which man John kills, and Reyes shoots the other.",
               "Dans « The Gates of El Presidio », les rebelles de Reyes prennent le fort d'assaut pour que John puisse atteindre [[javier-escuella|Javier Escuella]]. Dans « An Appointed Time », ils marchent sur Escalera pour renverser le colonel Agustín Allende, et poursuivent la voiture d'Allende transportant [[bill-williamson|Bill Williamson]] ; le joueur choisit lequel des deux John tue, et Reyes abat l'autre.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Reyes is charismatic and a gifted speaker, but vain and self-serving. He repeatedly calls his devoted follower Luisa Fortuna by the wrong name.",
               "Reyes est charismatique et orateur doué, mais vaniteux et intéressé. Il appelle à plusieurs reprises sa fidèle partisane Luisa Fortuna par un prénom qui n'est pas le sien.")},
   ]},
   {"summary": two("The betrayal","La trahison"), "blocks": [
     {"p": two("Reyes overthrows President Ignacio Sanchez, wins over the army with promises of higher pay, and installs himself as President of Mexico in November 1911. By 1914 he has reneged on every promise: he rules as a dictator, delays elections, and is accused of massacring peaceful protesters, while publicly denying he is a tyrant.",
               "Reyes renverse le président Ignacio Sanchez, rallie l'armée par des promesses de meilleure solde, et s'installe président du Mexique en novembre 1911. En 1914, il a renié chacune de ses promesses : il règne en dictateur, repousse les élections, et est accusé d'avoir massacré des manifestants pacifiques, tout en niant publiquement être un tyran.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Abraham Reyes appears in Red Dead Redemption (2010) and its 2024 remaster. He is voiced by Josh Segarra, and is modelled largely on the real revolutionary Francisco Madero.",
               "Abraham Reyes apparaît dans Red Dead Redemption (2010) et son remaster de 2024. Il est doublé par Josh Segarra, et s'inspire largement du révolutionnaire réel Francisco Madero.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("His surname, \"Reyes\", means \"kings\" in Spanish, a pointed nod to his ambitions.","Son nom, « Reyes », signifie « rois » en espagnol, un clin d'œil appuyé à ses ambitions."),
       two("The march on Escalera mirrors the real 1911 Battle of Ciudad Juárez.","La marche sur Escalera fait écho à la bataille réelle de Ciudad Juárez, en 1911."),
       two("He wears a Confederate States belt buckle.","Il porte une boucle de ceinture des États confédérés."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("His ally of convenience during the revolution; they save each other more than once.",
                "Son allié de circonstance pendant la révolution ; ils se sauvent mutuellement plus d'une fois.")},
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("John's former gang leader, whose anti-establishment ideology Reyes openly admires.",
                "L'ancien chef de gang de John, dont Reyes admire ouvertement l'idéologie anti-establishment.")},
   {"name": "Bill Williamson", "slug": "bill-williamson", "img": "bill.jpeg",
    "text": two("A fugitive John hunts; the rebellion's final battle brings them face to face.",
                "Un fugitif que John traque ; la bataille finale de la rébellion les met face à face.")},
   {"name": "Javier Escuella", "slug": "javier-escuella", "img": "javier.jpeg",
    "text": two("Another fugitive John pursues, reached through Reyes's assault on El Presidio.",
                "Un autre fugitif que John poursuit, atteint grâce à l'assaut de Reyes sur El Presidio.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Abraham Reyes in Nuevo Paraíso","Abraham Reyes à Nuevo Paraíso"),
    "cap": two("Reyes, leader of the Mexican revolution.","Reyes, chef de la révolution mexicaine.")},
 ],
},
]

# "More characters" ccards. Mixes the RDR1 wave with John Marston and the RDR2
# antagonists these figures cross paths with. All slugs are registered below.
# "More characters" ccards. Each list uses only characters already live on this
# fiche's publishDate (no forward links, matching the earlier waves) and present in
# the gen_fiche REGISTRY (base RDR2 cast + this wave, pre-registered below).
RELATED = {
 "bonnie-macfarlane":  ["john-marston", "bill-williamson", "dutch-van-der-linde", "arthur-morgan"],
 "landon-ricketts":    ["bonnie-macfarlane", "john-marston", "dutch-van-der-linde", "bill-williamson"],
 "nigel-west-dickens": ["landon-ricketts", "john-marston", "bonnie-macfarlane", "dutch-van-der-linde"],
 "seth-briars":        ["nigel-west-dickens", "john-marston", "bonnie-macfarlane", "landon-ricketts"],
 "leigh-johnson":      ["bonnie-macfarlane", "john-marston", "bill-williamson", "nigel-west-dickens"],
 "abraham-reyes":      ["landon-ricketts", "john-marston", "dutch-van-der-linde", "bill-williamson"],
}

if __name__ == "__main__":
    from gen_fiche import reg
    # Pre-register the whole wave so related ccards can cross-link within it.
    for c in CHARS:
        reg(c["slug"], c["name"], c["reg_role_en"], c["reg_role_fr"])
    for c in CHARS:
        c["related"] = RELATED[c["slug"]]
        folder = build_to_queue(c)
        print("wrote", folder)
