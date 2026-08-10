#!/usr/bin/env python3
"""Wave 5 content -> _queue/. Run: python scripts/_wave5.py
Not deployed (scripts/ is excluded from .cpanel.yml).

Completes the Van der Linde gang: the camp members still without a fiche.
Six... no, FIVE fiches: Karen Jones, Tilly Jackson, Mary-Beth Gaskill,
Simon Pearson (the cook), Reverend Orville Swanson (the chaplain).
Factual register (no mood-prose), FR written natively. All five SURVIVE RDR2;
Karen's death is only Tilly's epilogue speculation (never stated as fact).
Images already staged in assets/characters/<slug>/.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fiche import build_to_queue

def two(en, fr): return {"en": en, "fr": fr}

CHARS = [
# ============================ 24. KAREN JONES ============================
{
 "order": 24, "slug": "karen-jones", "name": "Karen Jones",
 "publishDate": "2026-08-14", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": None, "nationality": "American",
 "portrait_alt": two("Karen Jones in Red Dead Redemption 2", "Karen Jones dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Karen Jones: the con-artist and robber of the Van der Linde gang in Red Dead Redemption 2. Biography, her romance with Sean MacGuire, and her uncertain fate.",
                  "Karen Jones : l'arnaqueuse et braqueuse du gang Van der Linde dans Red Dead Redemption 2. Biographie, sa romance avec Sean MacGuire, et son destin incertain."),
 "og_desc": two("The con-artist of the Van der Linde gang, and the mind behind the Valentine bank robbery.",
                "L'arnaqueuse du gang Van der Linde, et la tête du braquage de la banque de Valentine."),
 "schema_desc": two("Con-artist and robber of the Van der Linde gang in Red Dead Redemption 2.",
                    "Arnaqueuse et braqueuse du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Con-artist", "Arnaqueuse"),
           two("Fate unknown", "Destin inconnu"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Con-artist and robber","Arnaqueuse et braqueuse")},
   {"label": two("Status","Statut"), "value": two("Unknown (leaves the gang)","Inconnu (quitte le gang)")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Karen Jones is a con-artist and robber in the Van der Linde gang in Red Dead Redemption 2. She works the scams and holdups, and is one of only two women in the gang, with [[sadie-adler|Sadie Adler]], to take camp guard duty.",
       "Karen Jones est une arnaqueuse et braqueuse du gang Van der Linde dans Red Dead Redemption 2. Elle mène les escroqueries et les hold-up, et est l'une des deux seules femmes du gang, avec [[sadie-adler|Sadie Adler]], à assurer la garde du camp."),
   two("She is the one who sets up the Valentine bank robbery, and her arc across the game is one of hard drinking and growing disillusion as the gang falls apart.",
       "C'est elle qui monte le braquage de la banque de Valentine, et son parcours dans le jeu est celui d'une femme qui boit de plus en plus et se désillusionne à mesure que le gang se délite."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The Valentine bank robbery","Le braquage de la banque de Valentine")},
     {"p": two("In Chapter 3, Karen initiates the robbery of the bank in Valentine, recruiting [[arthur-morgan|Arthur]], Lenny and Bill and posing as a distressed woman to get the drop on the staff. Earlier, in Valentine, [[arthur-morgan|Arthur]] rescues her when a mark she tries to rob punches her.",
               "Au chapitre 3, Karen lance le braquage de la banque de Valentine, en recrutant [[arthur-morgan|Arthur]], Lenny et Bill et en se faisant passer pour une femme en détresse afin de surprendre le personnel. Plus tôt, à Valentine, [[arthur-morgan|Arthur]] la sauve lorsqu'un homme qu'elle tente de détrousser la frappe.")},
     {"h3": two("Drinking and disillusion","L'alcool et la désillusion")},
     {"p": two("As the gang deteriorates, Karen's drinking worsens. At Beaver Hollow she turns bitter and openly berates [[susan-grimshaw|Susan Grimshaw]] for killing [[molly-oshea|Molly O'Shea]]. She is close to the gang's other women, Tilly Jackson and Mary-Beth Gaskill.",
               "À mesure que le gang se délite, Karen boit davantage. À Beaver Hollow, elle devient amère et reproche ouvertement à [[susan-grimshaw|Susan Grimshaw]] d'avoir tué [[molly-oshea|Molly O'Shea]]. Elle est proche des autres femmes du gang, Tilly Jackson et Mary-Beth Gaskill.")},
   ]},
   {"summary": two("Karen and Sean","Karen et Sean"), "blocks": [
     {"p": two("Karen has a brief romance with [[sean-macguire|Sean MacGuire]], beginning with a drunken night at his homecoming party. She later pushes him away, but after his death she gives him a campfire-song sendoff alongside [[susan-grimshaw|Susan Grimshaw]].",
               "Karen a une brève romance avec [[sean-macguire|Sean MacGuire]], qui commence par une nuit d'ivresse lors de la fête de son retour. Elle le repousse ensuite, mais après sa mort elle lui rend hommage par une chanson au coin du feu, aux côtés de [[susan-grimshaw|Susan Grimshaw]].")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Karen abandons the gang at Beaver Hollow, alongside Simon Pearson, Mary-Beth Gaskill and Uncle. After the gang falls, she disappears from view. In an epilogue letter, Tilly Jackson writes that she fears Karen drank herself to death, but the game never confirms it. Her fate is left unknown.",
               "Karen abandonne le gang à Beaver Hollow, en même temps que Simon Pearson, Mary-Beth Gaskill et Uncle. Après la chute du gang, elle disparaît. Dans une lettre de l'épilogue, Tilly Jackson écrit qu'elle craint que Karen ne se soit tuée à force de boire, mais le jeu ne le confirme jamais. Son destin reste inconnu.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Karen Jones appears in Red Dead Redemption 2 (2018). She is voiced by Jo Armeniox.",
               "Karen Jones apparaît dans Red Dead Redemption 2 (2018). Elle est doublée par Jo Armeniox.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("She and Sadie Adler are the only gang women to take guard duty.","Sadie Adler et elle sont les seules femmes du gang à assurer la garde."),
       two("As her drinking worsens through the game, her hair grows progressively unkempt.","À mesure qu'elle boit davantage, sa coiffure se défait peu à peu au fil du jeu."),
       two("She is the only gang member whose face is not seen in Chapter 1.","Elle est le seul membre du gang dont on ne voit pas le visage au chapitre 1."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "Sean MacGuire", "slug": "sean-macguire", "img": "sean.jpeg",
    "text": two("The young gang member she has a brief, volatile romance with.",
                "Le jeune membre du gang avec qui elle vit une romance brève et houleuse.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("Fellow gang member who backs her scams and pulls her out of trouble in Valentine.",
                "Compagnon de gang qui soutient ses arnaques et la tire d'affaire à Valentine.")},
   {"name": "Susan Grimshaw", "slug": "susan-grimshaw", "img": "susan.jpeg",
    "text": two("The camp's matriarch, whom Karen turns on after she kills Molly O'Shea.",
                "La matriarche du camp, contre qui Karen se retourne après qu'elle a tué Molly O'Shea.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Karen Jones at the campfire in Horseshoe Overlook","Karen Jones au coin du feu à Horseshoe Overlook"),
    "cap": two("Karen at camp in Horseshoe Overlook.","Karen au camp de Horseshoe Overlook.")},
 ],
},
# ============================ 25. TILLY JACKSON ============================
{
 "order": 25, "slug": "tilly-jackson", "name": "Tilly Jackson",
 "publishDate": "2026-08-17", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": None, "nationality": "American",
 "portrait_alt": two("Tilly Jackson in Red Dead Redemption 2", "Tilly Jackson dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Tilly Jackson: the Van der Linde gang member raised by Dutch in Red Dead Redemption 2. Biography, her past with the Foreman Brothers, and the life she builds after the gang.",
                  "Tilly Jackson : la membre du gang Van der Linde élevée par Dutch dans Red Dead Redemption 2. Biographie, son passé avec les Foreman Brothers, et la vie qu'elle bâtit après le gang."),
 "og_desc": two("The gang member Dutch raised, who survives to build an honest life after the gang.",
                "La membre du gang que Dutch a élevée, et qui survit pour bâtir une vie honnête après le gang."),
 "schema_desc": two("Van der Linde gang member in Red Dead Redemption 2, raised by Dutch van der Linde.",
                    "Membre du gang Van der Linde dans Red Dead Redemption 2, élevée par Dutch van der Linde."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Alive", "Vivante"),
           two("Outlaw", "Hors-la-loi"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Status","Statut"), "value": two("Alive (survives RDR2)","Vivante (survit à RDR2)")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Later name","Nom d'épouse"), "value": two("Tilly Pierre","Tilly Pierre")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Tilly Jackson is a member of the Van der Linde gang in Red Dead Redemption 2. The daughter of a former slave, she was taken in and raised by [[dutch-van-der-linde|Dutch van der Linde]], who taught her to read, and she looks on him as a surrogate father.",
       "Tilly Jackson est une membre du gang Van der Linde dans Red Dead Redemption 2. Fille d'une ancienne esclave, elle a été recueillie et élevée par [[dutch-van-der-linde|Dutch van der Linde]], qui lui a appris à lire, et elle le considère comme un père de substitution."),
   two("She is one of the gang's most level-headed members, and one of the few whose story ends well.",
       "Elle est l'une des membres les plus posées du gang, et l'une des rares dont l'histoire finit bien."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The Foreman Brothers","Les Foreman Brothers")},
     {"p": two("Before the gang, Tilly was taken at twelve by the Foreman Brothers gang. She killed Malcolm Foreman when he made advances on her, then left. In Chapter 4, the Foreman Brothers kidnap her again; [[susan-grimshaw|Susan Grimshaw]] sends [[arthur-morgan|Arthur]] to rescue her, and Tilly asks him to spare Anthony Foreman.",
               "Avant le gang, Tilly a été enlevée à douze ans par le gang des Foreman Brothers. Elle a tué Malcolm Foreman quand il lui a fait des avances, puis elle est partie. Au chapitre 4, les Foreman Brothers l'enlèvent à nouveau ; [[susan-grimshaw|Susan Grimshaw]] envoie [[arthur-morgan|Arthur]] la sauver, et Tilly lui demande d'épargner Anthony Foreman.")},
     {"h3": two("Loyal to the end","Fidèle jusqu'au bout")},
     {"p": two("Tilly rides with [[arthur-morgan|Arthur]] on stagecoach jobs and confides in him about life as a Black woman in the hostile South. At Beaver Hollow she hides a young [[jack-marston|Jack Marston]] from the Pinkerton raid and flees with him. In the final chapter, Arthur gives her his share of the money and tells her to live a good life.",
               "Tilly accompagne [[arthur-morgan|Arthur]] sur des braquages de diligences et se confie à lui sur sa vie de femme noire dans un Sud hostile. À Beaver Hollow, elle cache le jeune [[jack-marston|Jack Marston]] du raid des Pinkerton et fuit avec lui. Dans le dernier chapitre, Arthur lui donne sa part de l'argent et lui dit de vivre une bonne vie.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Tilly is calm, kind and loyal. She dreams of having children of her own, inspired by her time looking after [[jack-marston|Jack]].",
               "Tilly est calme, bienveillante et loyale. Elle rêve d'avoir ses propres enfants, inspirée par le temps passé à s'occuper de [[jack-marston|Jack]].")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Tilly survives Red Dead Redemption 2. In the epilogue she has married a lawyer named Pierre and has a daughter, and [[john-marston|John]] meets her on a bench in Saint Denis. She writes to John that her family lives well, and that she still sees Mary-Beth Gaskill often.",
               "Tilly survit à Red Dead Redemption 2. Dans l'épilogue, elle a épousé un avocat nommé Pierre et a une fille, et [[john-marston|John]] la retrouve sur un banc à Saint-Denis. Elle écrit à John que sa famille vit bien, et qu'elle voit encore souvent Mary-Beth Gaskill.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Tilly Jackson appears in Red Dead Redemption 2 (2018). She is voiced by Meeya Davis.",
               "Tilly Jackson apparaît dans Red Dead Redemption 2 (2018). Elle est doublée par Meeya Davis.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("Dutch found her in trouble, took her in and taught her to read.","Dutch l'a trouvée en difficulté, l'a recueillie et lui a appris à lire."),
       two("Her one confirmed kill before the gang is Malcolm Foreman.","Son seul meurtre confirmé avant le gang est celui de Malcolm Foreman."),
       two("By 1907 she is expecting a second child.","En 1907, elle attend un deuxième enfant."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("The gang leader who raised her and taught her to read; a surrogate father.",
                "Le chef de gang qui l'a élevée et lui a appris à lire ; un père de substitution.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("Fellow gang member she rides with and confides in; he gives her his money at the end.",
                "Compagnon de gang qu'elle accompagne et à qui elle se confie ; il lui donne son argent à la fin.")},
   {"name": "Karen Jones", "slug": "karen-jones", "img": "karen.jpeg",
    "text": two("One of the gang's three women, alongside her and Mary-Beth.",
                "L'une des trois femmes du gang, avec elle et Mary-Beth.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Tilly Jackson in Red Dead Redemption 2","Tilly Jackson dans Red Dead Redemption 2"),
    "cap": two("Tilly Jackson, member of the Van der Linde gang.","Tilly Jackson, membre du gang Van der Linde.")},
 ],
},
# ============================ 26. MARY-BETH GASKILL ============================
{
 "order": 26, "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill",
 "publishDate": "2026-08-20", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": None, "nationality": "American",
 "portrait_alt": two("Mary-Beth Gaskill in Red Dead Redemption 2", "Mary-Beth Gaskill dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Mary-Beth Gaskill: the pickpocket and camp bookworm of the Van der Linde gang in Red Dead Redemption 2, who becomes a novelist. Biography and fate.",
                  "Mary-Beth Gaskill : la pickpocket et rat de bibliothèque du gang Van der Linde dans Red Dead Redemption 2, qui devient romancière. Biographie et destin."),
 "og_desc": two("The gang's pickpocket and bookworm, who survives to become a published novelist.",
                "La pickpocket et lectrice du gang, qui survit pour devenir romancière publiée."),
 "schema_desc": two("Pickpocket and thief of the Van der Linde gang in Red Dead Redemption 2, later a novelist.",
                    "Pickpocket et voleuse du gang Van der Linde dans Red Dead Redemption 2, plus tard romancière."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Alive", "Vivante"),
           two("Thief / novelist", "Voleuse / romancière"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Pickpocket and thief","Pickpocket et voleuse")},
   {"label": two("Status","Statut"), "value": two("Alive (survives RDR2)","Vivante (survit à RDR2)")},
   {"label": two("Later","Plus tard"), "value": two("Novelist (\"Leslie Dupont\")","Romancière (« Leslie Dupont »)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Mary-Beth Gaskill is a pickpocket and thief in the Van der Linde gang in Red Dead Redemption 2, and the camp's bookworm, almost always found reading a romance novel. The gang took her in after rescuing her from the victims of her thieving.",
       "Mary-Beth Gaskill est une pickpocket et voleuse du gang Van der Linde dans Red Dead Redemption 2, et la lectrice du camp, presque toujours un roman à la main. Le gang l'a recueillie après l'avoir tirée des mains des victimes de ses vols."),
   two("She is one of the gentler members of the gang, and one of the few [[arthur-morgan|Arthur]] confides in.",
       "Elle est l'une des membres les plus douces du gang, et l'une des rares à qui [[arthur-morgan|Arthur]] se confie."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The camp bookworm","La lectrice du camp")},
     {"p": two("Mary-Beth finds the lead on the gang's lucrative train robbery, and helps [[arthur-morgan|Arthur]] and Sean rob a stagecoach in Chapter 3. She grows close to [[kieran-duffy|Kieran Duffy]], and is the first to see his mutilated body when the O'Driscolls send it back to camp, begging Arthur to avenge him.",
               "Mary-Beth trouve la piste du lucratif braquage de train du gang, et aide [[arthur-morgan|Arthur]] et Sean à dévaliser une diligence au chapitre 3. Elle se rapproche de [[kieran-duffy|Kieran Duffy]], et est la première à voir son corps mutilé quand les O'Driscoll le renvoient au camp, suppliant Arthur de le venger.")},
     {"h3": two("Arthur's confidante","La confidente d'Arthur")},
     {"p": two("At Beaver Hollow, [[arthur-morgan|Arthur]] tells Mary-Beth that he has tuberculosis; she is one of only two members he confides in, with [[charles-smith|Charles Smith]]. Her words of encouragement are among those Arthur can recall on his final ride. [[dutch-van-der-linde|Dutch]] flirts with her and asks after her books.",
               "À Beaver Hollow, [[arthur-morgan|Arthur]] confie à Mary-Beth qu'il a la tuberculose ; elle est l'une des deux seules personnes à qui il se confie, avec [[charles-smith|Charles Smith]]. Ses mots d'encouragement figurent parmi ceux qu'Arthur peut se remémorer lors de sa dernière chevauchée. [[dutch-van-der-linde|Dutch]] la courtise et s'enquiert de ses livres.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Mary-Beth survives Red Dead Redemption 2. By 1907 she is a romance novelist writing under the pen name Leslie Dupont. [[john-marston|John]] meets her at the Valentine train station, where she gives him a copy of her book, \"The Lady of the Manor\". She stays in close contact with Tilly Jackson.",
               "Mary-Beth survit à Red Dead Redemption 2. En 1907, elle est romancière sous le pseudonyme de Leslie Dupont. [[john-marston|John]] la retrouve à la gare de Valentine, où elle lui offre un exemplaire de son livre, « The Lady of the Manor ». Elle reste très proche de Tilly Jackson.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Mary-Beth Gaskill appears in Red Dead Redemption 2 (2018). She is voiced by Samantha Strelitz.",
               "Mary-Beth Gaskill apparaît dans Red Dead Redemption 2 (2018). Elle est doublée par Samantha Strelitz.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("She is one of only two members Arthur tells about his tuberculosis.","Elle est l'une des deux seules personnes à qui Arthur parle de sa tuberculose."),
       two("Her novel is reported as a best-seller in an in-game newspaper.","Son roman est présenté comme un best-seller dans un journal du jeu."),
       two("She tells Arthur he is the only one of the gang who knows how lost he is.","Elle dit à Arthur qu'il est le seul du gang à savoir à quel point il est perdu."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "Kieran Duffy", "slug": "kieran-duffy", "img": "kieran.jpeg",
    "text": two("The former O'Driscoll she grows close to, and whose death devastates her.",
                "L'ancien O'Driscoll dont elle se rapproche, et dont la mort la bouleverse.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("The gang member she comforts, and one of the two people he tells about his illness.",
                "Le membre du gang qu'elle réconforte, et l'une des deux personnes à qui il confie sa maladie.")},
   {"name": "Tilly Jackson", "slug": "tilly-jackson", "img": "tilly.jpeg",
    "text": two("Her closest friend in the gang, and long after it.",
                "Sa plus proche amie dans le gang, et longtemps après.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Mary-Beth Gaskill in Red Dead Redemption 2","Mary-Beth Gaskill dans Red Dead Redemption 2"),
    "cap": two("Mary-Beth Gaskill, the gang's pickpocket and reader.","Mary-Beth Gaskill, la pickpocket et lectrice du gang.")},
 ],
},
# ============================ 27. SIMON PEARSON ============================
{
 "order": 27, "slug": "simon-pearson", "name": "Simon Pearson",
 "publishDate": "2026-08-23", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Gang cook &middot; RDR2", "reg_role_fr": "Cuisinier du gang &middot; RDR2",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Simon Pearson in Red Dead Redemption 2", "Simon Pearson dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Simon Pearson: the cook of the Van der Linde gang in Red Dead Redemption 2, a former Navy sailor. Biography, his role in camp, and the store he runs after the gang.",
                  "Simon Pearson : le cuisinier du gang Van der Linde dans Red Dead Redemption 2, ancien marin. Biographie, son rôle au camp, et l'épicerie qu'il tient après le gang."),
 "og_desc": two("The gang's cook and butcher, a former Navy sailor who runs a store after the gang.",
                "Le cuisinier et boucher du gang, un ancien marin qui tient une épicerie après le gang."),
 "schema_desc": two("The cook and butcher of the Van der Linde gang in Red Dead Redemption 2.",
                    "Le cuisinier et boucher du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Alive", "Vivant"),
           two("Cook", "Cuisinier"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Cook and butcher","Cuisinier et boucher")},
   {"label": two("Status","Statut"), "value": two("Alive (survives RDR2)","Vivant (survit à RDR2)")},
   {"label": two("Past","Passé"), "value": two("Former US Navy sailor","Ancien marin de l'US Navy")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Simon Pearson is the cook and butcher of the Van der Linde gang in Red Dead Redemption 2. A former US Navy sailor from a family of whalers, he runs the camp's chuckwagon and crafts the gang's satchels from the pelts [[arthur-morgan|Arthur]] brings in.",
       "Simon Pearson est le cuisinier et boucher du gang Van der Linde dans Red Dead Redemption 2. Ancien marin de l'US Navy issu d'une famille de baleiniers, il tient la cantine du camp et fabrique les sacoches du gang à partir des peaux que [[arthur-morgan|Arthur]] rapporte."),
   two("The gang took him in after saving him from loan sharks, and he became their provisioner.",
       "Le gang l'a recueilli après l'avoir sauvé d'usuriers, et il en est devenu l'intendant."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The camp cook","Le cuisinier du camp")},
     {"p": two("Pearson runs the stew pot and the camp's crafting, turning donated perfect pelts into satchels up to the Legend of the East Satchel. In Chapter 3 he clashes with [[sadie-adler|Sadie Adler]] over being stuck cooking, and later relays the O'Driscoll parley that [[micah-bell|Micah]] pushes, which turns out to be a trap.",
               "Pearson tient la marmite et l'artisanat du camp, transformant les peaux parfaites données en sacoches, jusqu'à la sacoche Legend of the East. Au chapitre 3, il se dispute avec [[sadie-adler|Sadie Adler]] parce qu'il est cantonné à la cuisine, puis relaie la trêve proposée par les O'Driscoll que [[micah-bell|Micah]] pousse à accepter, et qui se révèle être un piège.")},
     {"h3": two("Leaving the gang","Le départ du gang")},
     {"p": two("At Beaver Hollow, [[susan-grimshaw|Susan Grimshaw]] orders Pearson and Bill to burn [[molly-oshea|Molly O'Shea]]'s body. He leaves the gang with Mary-Beth Gaskill and Uncle, and [[dutch-van-der-linde|Dutch]] brands him a coward for it.",
               "À Beaver Hollow, [[susan-grimshaw|Susan Grimshaw]] ordonne à Pearson et Bill de brûler le corps de [[molly-oshea|Molly O'Shea]]. Il quitte le gang avec Mary-Beth Gaskill et Uncle, et [[dutch-van-der-linde|Dutch]] le traite de lâche pour cela.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Pearson survives Red Dead Redemption 2. In the epilogue he runs the general store in Rhodes, married to a woman named Ethel, and keeps a photograph of the gang by his counter. [[john-marston|John]] can visit him there.",
               "Pearson survit à Red Dead Redemption 2. Dans l'épilogue, il tient l'épicerie de Rhodes, marié à une femme nommée Ethel, et garde une photo du gang près de son comptoir. [[john-marston|John]] peut lui rendre visite.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Simon Pearson appears in Red Dead Redemption 2 (2018). He is voiced by Jim Santangeli.",
               "Simon Pearson apparaît dans Red Dead Redemption 2 (2018). Il est doublé par Jim Santangeli.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He has a Navy anchor tattoo and is nostalgic for Navy rum.","Il a un tatouage d'ancre de la Navy et regrette le rhum de la marine."),
       two("He crafts the gang's satchels, including the Legend of the East Satchel.","Il fabrique les sacoches du gang, dont la sacoche Legend of the East."),
       two("He is one of the few members never shown committing a crime beyond gang association.","Il est l'un des rares membres qu'on ne voit jamais commettre de crime au-delà de son appartenance au gang."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "Susan Grimshaw", "slug": "susan-grimshaw", "img": "susan.jpeg",
    "text": two("Fellow camp manager, forever pushing back at his self-pity.",
                "Co-gestionnaire du camp, qui rembarre sans cesse son apitoiement.")},
   {"name": "Hosea Matthews", "slug": "hosea-matthews", "img": "hosea.jpeg",
    "text": two("The gang elder he gets on with, often sharing a joke.",
                "L'ancien du gang avec qui il s'entend bien, souvent à plaisanter.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("The hunter he relies on to keep the camp fed.",
                "Le chasseur sur qui il compte pour nourrir le camp.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Simon Pearson at the gang camp","Simon Pearson au camp du gang"),
    "cap": two("Pearson, the gang's cook and butcher.","Pearson, le cuisinier et boucher du gang.")},
 ],
},
# ============================ 28. ORVILLE SWANSON ============================
{
 "order": 28, "slug": "orville-swanson", "name": "Orville Swanson",
 "publishDate": "2026-08-26", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Gang chaplain &middot; RDR2", "reg_role_fr": "Aumônier du gang &middot; RDR2",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Reverend Orville Swanson in Red Dead Redemption 2", "Le révérend Orville Swanson dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Reverend Orville Swanson: the chaplain of the Van der Linde gang in Red Dead Redemption 2, a fallen preacher who gets sober. Biography and his redemption.",
                  "Le révérend Orville Swanson : l'aumônier du gang Van der Linde dans Red Dead Redemption 2, un prêtre déchu qui se sèvre. Biographie et sa rédemption."),
 "og_desc": two("The gang's addict chaplain, who sobers up and becomes a preacher again.",
                "L'aumônier toxicomane du gang, qui se sèvre et redevient pasteur."),
 "schema_desc": two("The chaplain of the Van der Linde gang in Red Dead Redemption 2, a former clergyman.",
                    "L'aumônier du gang Van der Linde dans Red Dead Redemption 2, un ancien homme d'Église."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Alive", "Vivant"),
           two("Chaplain", "Aumônier"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Chaplain","Aumônier")},
   {"label": two("Status","Statut"), "value": two("Alive (survives RDR2)","Vivant (survit à RDR2)")},
   {"label": two("Past","Passé"), "value": two("Former clergyman","Ancien homme d'Église")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Reverend Orville Swanson is the chaplain of the Van der Linde gang in Red Dead Redemption 2. A former clergyman who lost his job, his family and his faith to drink and morphine, he is kept in the gang because he once saved [[dutch-van-der-linde|Dutch van der Linde]]'s life.",
       "Le révérend Orville Swanson est l'aumônier du gang Van der Linde dans Red Dead Redemption 2. Ancien homme d'Église qui a perdu son poste, sa famille et sa foi à cause de l'alcool et de la morphine, il est gardé dans le gang parce qu'il a jadis sauvé la vie de [[dutch-van-der-linde|Dutch van der Linde]]."),
   two("His story is one of the few genuine redemption arcs in the game.",
       "Son histoire est l'un des rares vrais arcs de rédemption du jeu."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The drunken reverend","Le révérend ivrogne")},
     {"p": two("Swanson speaks the very first line of dialogue in the game, at Colter. In Chapter 2, in \"Who is Not Without Sin\", [[arthur-morgan|Arthur]] has to free a drunk Swanson whose foot is caught on the railroad tracks before a train arrives. His \"bible\" is a painted box hiding alcohol and morphine.",
               "Swanson prononce la toute première réplique du jeu, à Colter. Au chapitre 2, dans « Who is Not Without Sin », [[arthur-morgan|Arthur]] doit libérer un Swanson ivre dont le pied est coincé sur les rails avant l'arrivée d'un train. Sa « bible » est une boîte peinte dissimulant de l'alcool et de la morphine.")},
     {"h3": two("Getting sober","Le sevrage")},
     {"p": two("By the time the gang returns from Guarma, Swanson has sobered up and kicked his morphine addiction, becoming clear-eyed and sensible. He sees through [[dutch-van-der-linde|Dutch]]'s decline, saying he will not die for the nonsense of a fool.",
               "Au retour du gang de Guarma, Swanson s'est sevré de l'alcool et de la morphine, et retrouve la lucidité. Il voit clair dans le déclin de [[dutch-van-der-linde|Dutch]], disant qu'il ne mourra pas pour les inepties d'un imbécile.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Swanson survives Red Dead Redemption 2, a reformed man. In the epilogue, [[charles-smith|Charles]] tells [[john-marston|John]] that Swanson moved to New York to become a preacher, and an in-game newspaper reports him as minister of the First Congregational Church of New York.",
               "Swanson survit à Red Dead Redemption 2, un homme changé. Dans l'épilogue, [[charles-smith|Charles]] apprend à [[john-marston|John]] que Swanson est parti à New York pour devenir pasteur, et un journal du jeu le présente comme ministre de la First Congregational Church de New York.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Orville Swanson appears in Red Dead Redemption 2 (2018). He is voiced by Sean Haberle.",
               "Orville Swanson apparaît dans Red Dead Redemption 2 (2018). Il est doublé par Sean Haberle.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He speaks the first line of dialogue in Red Dead Redemption 2.","Il prononce la première réplique de Red Dead Redemption 2."),
       two("His hollow \"bible\" hides a syringe, morphine and alcohol.","Sa « bible » creuse cache une seringue, de la morphine et de l'alcool."),
       two("He gives Arthur an honour-based parting assessment at Emerald Station.","Il livre à Arthur un jugement d'adieu selon son honneur, à Emerald Station."),
     ]},
   ]},
 ],
 "relationships": [
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("The gang leader whose life he once saved, his reason for being in the gang.",
                "Le chef de gang dont il a jadis sauvé la vie, sa raison d'être dans le gang.")},
   {"name": "Hosea Matthews", "slug": "hosea-matthews", "img": "hosea.jpeg",
    "text": two("The gang elder he confides in at the campfire.",
                "L'ancien du gang à qui il se confie au coin du feu.")},
   {"name": "Arthur Morgan", "slug": "arthur-morgan", "img": "arthur.jpeg",
    "text": two("The gang member who pulls him off the railroad tracks, and whom he sizes up at the end.",
                "Le membre du gang qui le tire des rails, et qu'il juge à la fin.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Reverend Swanson's hollowed bible hiding morphine and alcohol","La bible creuse du révérend Swanson dissimulant morphine et alcool"),
    "cap": two("Swanson's \"bible\", a painted box hiding his addictions.","La « bible » de Swanson, une boîte peinte cachant ses addictions.")},
 ],
},
]

# "More characters" ccards. Only characters already live on each fiche's publishDate,
# and present in the gen_fiche REGISTRY (base RDR2 cast + this wave, pre-registered below).
RELATED = {
 "karen-jones":       ["arthur-morgan", "dutch-van-der-linde", "sadie-adler", "hosea-matthews"],
 "tilly-jackson":     ["karen-jones", "arthur-morgan", "dutch-van-der-linde", "sadie-adler"],
 "mary-beth-gaskill": ["tilly-jackson", "karen-jones", "arthur-morgan", "dutch-van-der-linde"],
 "simon-pearson":     ["arthur-morgan", "hosea-matthews", "dutch-van-der-linde", "sadie-adler"],
 "orville-swanson":   ["dutch-van-der-linde", "hosea-matthews", "arthur-morgan", "john-marston"],
}

if __name__ == "__main__":
    from gen_fiche import reg
    for c in CHARS:
        reg(c["slug"], c["name"], c["reg_role_en"], c["reg_role_fr"])
    for c in CHARS:
        c["related"] = RELATED[c["slug"]]
        folder = build_to_queue(c)
        print("wrote", folder)
