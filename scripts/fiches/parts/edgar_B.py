"""Edgar Ross, part B: Personality (official description, traits, In his own words, Names,
Appearance), Bureau work, weapons and horses, Relationships (20 Oct 2026).

Sources (register): Red Dead Wiki EN "Edgar Ross" (infobox, Personality, Appearance, Quotes,
Trivia, Gallery captions; the Game of the Year Edition guide description is quoted from it, the
guide itself was not read); FR "Edgar Ross"; wiki pages "Archer Fordham", "Andrew Milton",
"Leviticus Cornwall", "Harold MacDougal", "Emily Ross", "Phillip Ross", "Howard Sawicki",
"Bureau of Investigation", "Edgar Ross Retires After a Lifetime of Government Service" (1914
newspaper text), "The Last Enemy That Shall Be Destroyed", "Remember My Family", "Just a Social
Call", "Ending Credits" (saved in edgar/fc and edgar/m). Transcripts read: A Fisher of Men; The
Battle of Shady Belle; Red Dead Redemption (mission, Beaver Hollow); The Gates of El Presidio (both
branches); Bear One Another's Burdens; Great Men are Not Always Wise; And You Will Know The Truth;
And The Truth Will Set You Free; The Last Enemy That Shall Be Destroyed; Remember My Family.
Fact-checked fiches reused as is: john_B/D/E (High Power Pistol handed over, "old boy", files
and "40" banks), jack_A/B/C, abigail_A/B, dutch_B/C, bill_A/B, javier_A/B, micah_A/B, hosea_B,
arthur_C, uncle_A/B, sadie_B, live fiches nastas, harold-macdougal, nigel-west-dickens.

Ownership (FIX_RULES): the official description (GOTY guide), traits, names, a short
appearance, Bureau methods, weapons, horses, the "G" mission icon, and all one-to-one exchanges
used to characterize a relationship live HERE. Narrative events (Fisher of Men, Clemens Point,
Annesburg, Beaver Hollow, the 1907 credits, the 1911 missions, the prison riot joke, the shot into
Dutch's body, the ranch attack, the 1914 duel, the 1907 and 1914 newspapers, education, birth
year) live in part A; relationship entries refer to them in a short clause.
Lines quoted in this part (parts A and C must NOT repeat them): GOTY guide fragments; "You see we,
me and Archer, we're the bad guys..." through "...is hell."; "Well, I know there's contradictions.
I'm not going to lie to you."; "I don't rightly know, but it sure felt good saying it."; "A new
dawn is breaking, Mr. Marston. This is the age of the machine."; "You know, at the end of this,
you'll probably get a medal. I know I shall."; "Civilization is coming to the West, and we will
clear out the dead wood."; "We are neither, Mr. Marston." / "But I have the authority over both."
(the "special interest to Washington" line is quoted in part C only); "I can't imagine I ever said
anything quite so trite."; "Don't get snarky with me, Fordham."; "A bad workman shouldn't blame
his tools."; "And who is this savage? A prisoner?" / "Do you speak English?"; "I just can't
communicate with them."; "Which should tell you something."; "Professor MacDougal has been a good
friend to the U.S. government, Mr. Marston. Just like you."; "Did you hear that, officer, the
man's a hero. Let him go."; "Fancy seeing you down here"; Emily's "such a sensitive man" and
"talons"; Phillip's "filthy temper"; Sawicki's "Fine man if you wanted results."; "What a role
model." (Dutch); "old boy", "dear boy" (Names). Fact-check fixes (20 Oct 2026): Personality no
longer retells biography events; Authority keeps only authority and methods; the "G" marker lives
in part C (Missions intro); relationship entries cut down to their own angle with pointers.
Left free for part C Quotes: "No one's playing games with you...", "I've never insulted your
meagre intelligence...", "Moral degeneracy waits for no man.", "noble savage... tripe", the
"metaphysical leap" passage, "You can't erase your past, Mr. Marston, but we can.", "Come on,
Archer, let's go find somebody else we can annoy.", "Oh trust me, it looks better in the report
that way." (A or C), Beaver Hollow orders, the 1914 last words (A or C).

WIKI-ONLY (kept, attributed): the GOTY guide description; Hosea's execution with Ross at Milton's
side; the "G" icon; weapons and horses (infobox); appearance by period; Ross giving his card to a
stagecoach passenger (gallery caption).

Excluded: "indifferent, snide, amoral, disloyal, unscrupulous", "only concerned with personal
glory", "may have held prejudicial views", "end justifies the means" (wiki interpretation; the
transcript lines are given instead); "purveyor of modernism" as a label (only his own lines);
Hoover and Tenpenny/Toreno comparisons (speculation; Whitaker's Hoover comparison is in part D
Reception); eye color and height oversights, Pinkerton badge in 1907, 1914 outfit like Uncle's,
"friendly" cursor, $400 loot, Winchester/High Power anachronisms, M1911 artwork (part C Trivia or
excluded); Mac Callander (Milton's account, Ross's presence not stated); Bonnie MacFarlane, Leigh
Johnson, Abraham Reyes, Agustin Allende, Vincente de Santa, Irish, Landon Ricketts (no exchange
with Ross found in any transcript or wiki page); Fordham at the 1911 firing squad (disputed on the
wiki: a marshal is often mistaken for him); Bill killed "per Ross's request" (wiki phrasing,
unsupported); Ross "takes over" Milton's squad (wiki inference: only his presence by voice at
Beaver Hollow is stated); Sadie (no direct exchange).
"""

def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "The Red Dead Wiki quotes the description of Ross printed in the guide to the Game of the Year Edition of Red Dead Redemption. It presents him as the head of a young government agency, \"a man whose faded physical prowess has been supplanted by his mental acuteness\", and \"a cynic who sees the worst in everyone, and who loves the power that the government has recently granted him\". The same text ends: \"He sees himself as an individual who is completely above any law.\"",
        "Le Red Dead Wiki cite la description de Ross imprimée dans le guide de l'édition Game of the Year de Red Dead Redemption. Elle le présente comme le chef d'une jeune agence gouvernementale, \"a man whose faded physical prowess has been supplanted by his mental acuteness\" (un homme dont la vivacité d'esprit a pris le relais d'une vigueur physique déclinante), et comme \"a cynic who sees the worst in everyone, and who loves the power that the government has recently granted him\" (un cynique qui voit le pire en chacun et qui adore le pouvoir que l'État vient de lui confier). Le texte se termine ainsi : \"He sees himself as an individual who is completely above any law.\" (il se considère comme un homme placé au-dessus de toutes les lois).")},
    {"p": two(
        "In the 1911 missions he calls John stupid and \"devoid of intellect\", and answers John's anger with jokes, including one about Abigail's death (see Biography).",
        "Dans les missions de 1911, il traite John d'idiot \"devoid of intellect\" (dépourvu d'intelligence), et répond à la colère de John par des plaisanteries, dont l'une sur la mort d'Abigail (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "In \"And You Will Know The Truth\" he explains his role to John: \"You see we, me and Archer, we're the bad guys. We enforce the rules. Now, while the rules may not be perfect, they're really not so bad.\" Then: \"It's about one man and his gun versus another man. Sure, civilization may be dull, but the alternative, Mr. Marston, is hell.\" When John points out that this civilization is enforced by kidnapping a man's wife and son, Ross concedes: \"Well, I know there's contradictions. I'm not going to lie to you.\" Asked what the speech was for, he answers: \"I don't rightly know, but it sure felt good saying it.\"",
        "Dans \"And You Will Know The Truth\", il expose son rôle à John : \"You see we, me and Archer, we're the bad guys. We enforce the rules. Now, while the rules may not be perfect, they're really not so bad.\" (vous voyez, nous, Archer et moi, nous sommes les méchants ; nous faisons respecter les règles ; elles ne sont peut-être pas parfaites, mais elles ne sont vraiment pas si mauvaises). Puis : \"It's about one man and his gun versus another man. Sure, civilization may be dull, but the alternative, Mr. Marston, is hell.\" (c'est un homme et son arme contre un autre homme ; la civilisation est peut-être ennuyeuse, mais l'autre choix, monsieur Marston, c'est l'enfer). Quand John objecte que cette civilisation passe par l'enlèvement de la femme et du fils d'un homme, Ross admet : \"Well, I know there's contradictions. I'm not going to lie to you.\" (je sais bien qu'il y a des contradictions, je ne vais pas vous mentir). À quoi rimait ce discours, demande John ; Ross répond : \"I don't rightly know, but it sure felt good saying it.\" (je n'en sais trop rien, mais ça fait du bien de le dire).")},
    {"p": two(
        "On the drive to the wreck of the Serendipity, in \"Bear One Another's Burdens\": \"A new dawn is breaking, Mr. Marston. This is the age of the machine.\" On the ride out of Blackwater in \"Great Men are Not Always Wise\": \"Civilization is coming to the West, and we will clear out the dead wood.\" At the end of the same mission, after Dutch has escaped: \"You know, at the end of this, you'll probably get a medal. I know I shall.\"",
        "En route vers l'épave du Serendipity, dans \"Bear One Another's Burdens\" : \"A new dawn is breaking, Mr. Marston. This is the age of the machine.\" (une ère nouvelle se lève, monsieur Marston ; c'est l'âge de la machine). En quittant Blackwater, dans \"Great Men are Not Always Wise\" : \"Civilization is coming to the West, and we will clear out the dead wood.\" (la civilisation arrive dans l'Ouest, et nous allons couper le bois mort). À la fin de la même mission, après la fuite de Dutch : \"You know, at the end of this, you'll probably get a medal. I know I shall.\" (au bout du compte, vous aurez sans doute une médaille ; moi, j'en aurai une, c'est certain).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Milton introduces him as Agent Ross in 1899, and he uses the same title when he calls on the gang to surrender at Beaver Hollow. In Blackwater John asks for Mr. Ross at the police station and Fordham speaks of him as Mr. Ross; in 1914 his wife calls him Edgar, and the Bureau agent Howard Sawicki says Edgar Ross. He addresses John as Mr. Marston, and sometimes as \"old boy\" or \"dear boy\". The Red Dead Wiki lists Agent Ross as his alias.",
        "Milton le présente comme l'agent Ross en 1899, et c'est sous ce titre qu'il somme la bande de se rendre à Beaver Hollow. À Blackwater, John demande M. Ross au poste de police et Fordham parle de lui en l'appelant M. Ross ; en 1914, sa femme l'appelle Edgar et l'agent du Bureau Howard Sawicki parle d'Edgar Ross. Il appelle John monsieur Marston, et parfois \"old boy\" ou \"dear boy\" (mon vieux, mon cher). Le Red Dead Wiki retient Agent Ross comme surnom.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "According to the Red Dead Wiki, in 1899 he has short dark brown hair, a thick mustache and a bowler hat with his Pinkerton suit. In 1907 his hair, now parted in the middle, shows some gray, and he no longer wears a bowler hat. In 1911 he is gray-haired, with a gray mustache and a higher forehead; he wears a beige three-piece suit, a red tie and a black bowler hat. In 1914, retired, he hunts in a shirt and suspenders under a wide-brimmed hat.",
        "D'après le Red Dead Wiki, il a en 1899 les cheveux châtain foncé coupés court, une épaisse moustache et un chapeau melon avec son costume de Pinkerton. En 1907, ses cheveux, désormais séparés par une raie au milieu, commencent à grisonner, et il ne porte plus de melon. En 1911, il a les cheveux et la moustache gris et le front plus haut ; il porte un costume trois pièces beige, une cravate rouge et un melon noir. En 1914, à la retraite, il chasse en chemise et bretelles sous un chapeau à larges bords.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Bureau work, weapons and horses", "Méthodes du Bureau, armes et chevaux")},
    {"h4": two("Authority and methods", "Autorité et méthodes")},
    {"p": two(
        "When John asks in \"Great Men are Not Always Wise\" whether the agents are lawmen or army, Fordham answers \"We are neither, Mr. Marston.\" and Ross adds: \"But I have the authority over both.\" In the same exchange he says that a local lawman with a badge is good enough for saloon drunks but that serious matters need a firmer hand. In 1911 he works through informants (an unnamed informant who tips him off about Dutch's visit to the Blackwater bank, then Nastas), through the academic Harold MacDougal, through local lawmen and through the army. He also relies on new equipment: the automobile mounted with a Gatling gun that carries him, Fordham and John to the army camp is, in Fordham's words, \"a simple prototype\".",
        "Quand John demande, dans \"Great Men are Not Always Wise\", si les agents sont des hommes de loi ou des militaires, Fordham répond \"We are neither, Mr. Marston.\" (ni l'un ni l'autre, monsieur Marston) et Ross ajoute : \"But I have the authority over both.\" (mais j'ai autorité sur les deux). Dans le même échange, il estime qu'un homme de loi de campagne suffit pour les ivrognes de saloon mais que les affaires sérieuses exigent une main plus ferme. En 1911, il s'appuie sur des informateurs (un informateur anonyme qui l'avertit de la visite de Dutch à la banque de Blackwater, puis Nastas), sur l'universitaire Harold MacDougal, sur les hommes de loi locaux et sur l'armée. Il mise aussi sur du matériel nouveau : l'automobile armée d'une mitrailleuse Gatling qui le conduit avec Fordham et John au camp de l'armée n'est guère plus, selon Fordham, qu'un simple prototype.")},
    {"h4": two("Weapons and horses", "Armes et chevaux")},
    {"p": two(
        "The Red Dead Wiki lists the Cattleman Revolver, the Repeating Shotgun, the Pump-Action Shotgun, the High Power Pistol and the Winchester Repeater among his weapons, and three horses: a Dutch Warmblood in 1899, a Kentucky Saddler in 1907 and a Painted Standardbred in 1911.",
        "Le Red Dead Wiki lui attribue le Cattleman Revolver, le Repeating Shotgun, le Pump-Action Shotgun, le High Power Pistol et la Winchester Repeater, ainsi que trois chevaux : un Dutch Warmblood en 1899, un Kentucky Saddler en 1907 et un Painted Standardbred en 1911.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [
        two(
            "Ross first sees John at Clemens Point in 1899, where John gives Milton a false name, Rip Van Winkle; at Beaver Hollow he names him with Arthur among the men cornered near the caves. In 1907 his investigation into Micah's death ends with him watching John at his ranch. In 1911 he holds John's wife and son to make him hunt down Bill, Javier and Dutch, then refuses each time John asks for his family (see Biography). He assures John that he has nothing but John's best intentions at heart.",
            "Ross voit John pour la première fois à Clemens Point en 1899, où John donne à Milton un faux nom, Rip Van Winkle ; à Beaver Hollow, il le nomme avec Arthur parmi les hommes acculés près des grottes. En 1907, son enquête sur la mort de Micah s'achève sur John, qu'il observe à son ranch. En 1911, il retient la femme et le fils de John pour l'obliger à traquer Bill, Javier et Dutch, et refuse chaque fois que John réclame sa famille (voir la biographie). Il lui assure n'avoir à cœur que son intérêt."),
        two(
            "John answers Ross with open hostility. He calls him a coward, tells him he would kill him a hundred times before killing Dutch if he could, and compares him to Dutch as a violent man who confused himself with God. Ross answers by calling him a murderer. After Dutch's death he lets John go home, then leads the attack on Beecher's Hope in which John is shot down (see Biography).",
            "John répond à Ross par une hostilité ouverte. Il le traite de lâche, lui dit qu'il le tuerait cent fois avant de tuer Dutch s'il en avait le choix, et le compare à Dutch, un homme violent qui s'est pris pour Dieu. Ross le traite en retour d'assassin. Après la mort de Dutch, il laisse John rentrer chez lui, puis mène l'assaut sur Beecher's Hope au cours duquel John est abattu (voir la biographie)."),
    ]},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "Ross's only words to Jack in 1899 are his parting line at the river in \"A Fisher of Men\" (see Biography). In 1911 the Bureau holds Jack with his mother. In 1914 Jack tracks Ross down through Howard Sawicki, Emily and Phillip Ross, and kills him in a duel (see Biography). When Jack insists that he saw him kill John, Ross answers: \"You keep saying that.\"",
        "En 1899, les seuls mots de Ross à Jack sont sa réplique en partant, au bord de la rivière, dans \"A Fisher of Men\" (voir la biographie). En 1911, le Bureau retient Jack avec sa mère. En 1914, Jack remonte jusqu'à Ross par Howard Sawicki, Emily et Phillip Ross, et le tue en duel (voir la biographie). Quand Jack insiste sur le fait qu'il l'a vu tuer John, Ross se contente de répondre : \"You keep saying that.\" (tu n'arrêtes pas de le dire).")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "In 1911 the Bureau holds Abigail with Jack. Ross brings her up twice to put pressure on John: on the drive to the Serendipity he mentions that she could become a widow, and after the truck overturns, when John asks what happens if he refuses, he names her as the last person who could appeal to Dutch (see Biography). He also jokes about her death and tells John that she sends her regards (see Quotes).",
        "En 1911, le Bureau retient Abigail avec Jack. Ross se sert d'elle à deux reprises pour faire pression sur John : en route vers le Serendipity, il évoque le risque qu'elle devienne veuve, puis, après le renversement du camion, quand John demande ce qui se passera s'il refuse, il la désigne comme la dernière personne capable de raisonner Dutch (voir la biographie). Il plaisante aussi sur sa mort et dit à John qu'elle lui transmet ses amitiés (voir les citations).")},
    {"img": "archer-fordham.jpeg", "slug": "archer-fordham", "name": "Archer Fordham", "text": two(
        "Fordham is Ross's fellow Bureau agent from 1907 to 1911: they examine Micah's body together, escort John through Blackwater and collect Javier at the border. Ross often puts him down. When Fordham quotes one of his supposed maxims, Ross answers: \"I can't imagine I ever said anything quite so trite.\" He tells him \"Don't get snarky with me, Fordham.\" and, after the automobile breaks down, blames his driving: \"A bad workman shouldn't blame his tools.\"",
        "Fordham est le collègue de Ross au Bureau de 1907 à 1911 : ils examinent ensemble le corps de Micah, escortent John dans Blackwater et récupèrent Javier à la frontière. Ross le rabroue souvent. Quand Fordham cite une de ses prétendues maximes, Ross répond : \"I can't imagine I ever said anything quite so trite.\" (je n'imagine pas avoir jamais dit une chose aussi banale). Il lui lance \"Don't get snarky with me, Fordham.\" (pas d'insolence, Fordham) et, après la panne de l'automobile, s'en prend à sa conduite : \"A bad workman shouldn't blame his tools.\" (un mauvais ouvrier ne devrait pas accuser ses outils).")},
    {"img": "andrew-milton.jpeg", "slug": "andrew-milton", "name": "Andrew Milton", "text": two(
        "Ross is Milton's deputy in 1899; the 1907 newspaper article on the founding of the Bureau says he served for many years as a senior Pinkerton agent under Milton's mentorship. Milton does the talking when the two agents meet Arthur at the river and when they walk into Clemens Point. They come off Cornwall's yacht together in Annesburg. After Abigail kills Milton at Van Horn, Ross is the one heard leading the Pinkertons at Beaver Hollow.",
        "Ross est l'adjoint de Milton en 1899 ; l'article de 1907 sur la création du Bureau précise qu'il a longtemps été agent principal de la Pinkerton sous la tutelle de Milton. C'est Milton qui parle quand les deux agents abordent Arthur au bord de la rivière et quand ils entrent dans le camp de Clemens Point. Ils descendent ensemble du yacht de Cornwall à Annesburg. Après la mort de Milton, tué par Abigail à Van Horn, c'est Ross que l'on entend mener les Pinkerton à Beaver Hollow.")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Ross stands beside Milton when the agents offer Dutch's gang a deal at Clemens Point in 1899. In 1911 he wants John to be the one who kills Dutch (see Biography). During the chase that follows the ambush at the Blackwater bank, he mocks Dutch to John: \"So, that's the great Dutch? What a role model. The man who made who you are.\" In \"And You Will Know The Truth\" he compares Dutch to the nature writers from back East (see Quotes). At Cochinay he fires into Dutch's body (see Biography).",
        "Ross se tient aux côtés de Milton quand les agents proposent un marché à la bande de Dutch à Clemens Point, en 1899. En 1911, il veut que ce soit John qui tue Dutch (voir la biographie). Pendant la poursuite qui suit l'embuscade de la banque de Blackwater, il se moque de Dutch devant John : \"So, that's the great Dutch? What a role model. The man who made who you are.\" (alors c'est ça, le grand Dutch ? Quel modèle. L'homme qui a fait de vous ce que vous êtes). Dans \"And You Will Know The Truth\", il compare Dutch aux écrivains naturalistes de l'Est (voir les citations). À Cochinay, il tire dans le corps de Dutch (voir la biographie).")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "In \"Just a Social Call\", Micah watches with Arthur and Dutch from the Annesburg harbor as Ross and Milton come off Cornwall's yacht. At Beaver Hollow, Ross's announcement that the Pinkertons have the camp surrounded comes just before Micah urges Dutch to flee. In 1907 Ross and Fordham find Micah's body at his hideout on Mount Hagen, and their investigation leads them to John.",
        "Dans \"Just a Social Call\", Micah observe avec Arthur et Dutch, depuis le port d'Annesburg, Ross et Milton descendre du yacht de Cornwall. À Beaver Hollow, Ross annonce que les Pinkerton encerclent le camp juste avant que Micah ne presse Dutch de fuir. En 1907, Ross et Fordham trouvent le corps de Micah à sa planque du mont Hagen, et leur enquête les mène jusqu'à John.")},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
        "Ross meets Arthur face to face twice in 1899, at the river in \"A Fisher of Men\" and at Clemens Point, and does not address him at either meeting. At Beaver Hollow he calls on Arthur and John by name to surrender (see Biography).",
        "Ross se trouve deux fois face à Arthur en 1899, au bord de la rivière dans \"A Fisher of Men\" puis à Clemens Point, sans lui adresser la parole ni l'une ni l'autre fois. À Beaver Hollow, il somme Arthur et John de se rendre en les appelant par leur nom (voir la biographie).")},
    {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
        "In 1911 Uncle keeps Beecher's Hope while Ross's Bureau holds Abigail and Jack. He is the first to spot the soldiers and lawmen riding on the ranch, and he is killed on the porch during the attack (see Biography). In 1914 Jack visits the graves of John, Abigail and Uncle before setting out after Ross.",
        "En 1911, Uncle garde Beecher's Hope pendant que le Bureau de Ross retient Abigail et Jack. C'est lui qui repère le premier les soldats et les hommes de loi qui marchent sur le ranch, et il meurt sur le perron pendant l'assaut (voir la biographie). En 1914, Jack se recueille sur les tombes de John, d'Abigail et d'Uncle avant de partir sur les traces de Ross.")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Bill is the first target Ross sends John after, at Fort Mercer. Even with Bill and Javier dealt with, Ross does not release John's family (see Biography).",
        "Bill est la première cible que Ross assigne à John, à Fort Mercer. Même une fois Bill et Javier réglés, Ross ne rend pas sa famille à John (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "After El Presidio, John hands Javier, alive or dead, to Ross and Fordham near the border bridge (see Biography). In both versions of the scene Ross speaks only to John; it is Fordham who orders a captured Javier into the automobile.",
        "Après El Presidio, John remet Javier, vivant ou mort, à Ross et Fordham près du pont de la frontière (voir la biographie). Dans les deux versions de la scène, Ross ne s'adresse qu'à John ; c'est Fordham qui ordonne à Javier, s'il est vivant, de monter dans l'automobile.")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "Hosea is at the table with Dutch, Arthur and John when Ross and Milton walk into Clemens Point in 1899. Ross's presence at his execution in Saint Denis, reported by the Red Dead Wiki, is covered in the Biography.",
        "Hosea est attablé avec Dutch, Arthur et John quand Ross et Milton entrent dans le camp de Clemens Point, en 1899. La présence de Ross lors de son exécution à Saint-Denis, rapportée par le Red Dead Wiki, est traitée dans la biographie.")},
    {"img": "leviticus-cornwall.jpeg", "slug": "leviticus-cornwall", "name": "Leviticus Cornwall", "text": two(
        "Cornwall pays the Pinkertons who hunt the gang in 1899. Ross comes off Cornwall's yacht with him and Milton in Annesburg, shortly before Dutch kills Cornwall (see Biography).",
        "Cornwall finance les Pinkerton qui traquent la bande en 1899. Ross descend de son yacht avec lui et Milton à Annesburg, peu avant que Dutch ne l'abatte (voir la biographie).")},
    {"img": "nastas.jpeg", "slug": "nastas", "name": "Nastas", "text": two(
        "Nastas is the Bureau's informant on Dutch's new gang. When John and Fordham bring him back wounded from the Serendipity, Ross asks: \"And who is this savage? A prisoner?\" Told that this is the informant, he asks him: \"Do you speak English?\" Ross then has him taken to MacDougal, saying: \"I just can't communicate with them.\"",
        "Nastas est l'informateur du Bureau sur la nouvelle bande de Dutch. Quand John et Fordham le ramènent blessé du Serendipity, Ross demande : \"And who is this savage? A prisoner?\" (et qui est ce sauvage ? un prisonnier ?). Quand on lui répond que c'est l'informateur, il lui demande : \"Do you speak English?\" (vous parlez anglais ?). Ross le fait ensuite conduire chez MacDougal, en expliquant : \"I just can't communicate with them.\" (je n'arrive tout simplement pas à communiquer avec eux).")},
    {"img": "harold-macdougal.jpeg", "slug": "harold-macdougal", "name": "Harold MacDougal", "text": two(
        "Ross relies on the professor to deal with the Native Americans of the region. When Fordham explains that MacDougal was thrown out of Yale, Ross remarks: \"Which should tell you something.\" He then presents him to John: \"Professor MacDougal has been a good friend to the U.S. government, Mr. Marston. Just like you.\" Later, Ross learns from MacDougal that John has been up to Cochinay.",
        "Ross compte sur le professeur pour traiter avec les Amérindiens de la région. Quand Fordham explique que MacDougal a été renvoyé de Yale, Ross commente : \"Which should tell you something.\" (ce qui en dit long). Il le présente ensuite à John : \"Professor MacDougal has been a good friend to the U.S. government, Mr. Marston. Just like you.\" (le professeur MacDougal est un bon ami du gouvernement américain, monsieur Marston ; tout comme vous). Plus tard, c'est par MacDougal que Ross apprend que John est monté jusqu'à Cochinay.")},
    {"img": "nigel-west-dickens.jpeg", "slug": "nigel-west-dickens", "name": "Nigel West Dickens", "text": two(
        "Ross deals with West Dickens only once, at the Blackwater police station (see Biography). When John vouches for him as a harmless old fraud who helped him get Williamson, Ross tells the officer: \"Did you hear that, officer, the man's a hero. Let him go.\"",
        "Ross n'a affaire à West Dickens qu'une seule fois, au poste de police de Blackwater (voir la biographie). Quand John se porte garant de ce vieil escroc inoffensif qui l'a aidé à avoir Williamson, Ross lance au policier : \"Did you hear that, officer, the man's a hero. Let him go.\" (vous avez entendu, agent, cet homme est un héros ; relâchez-le).")},
    {"img": None, "slug": None, "name": "Emily Ross", "text": two(
        "Emily is Ross's wife; in 1914 they live in a cabin by Lake Don Julio (see Biography). When Jack says he has a letter for her husband, she complains that the Bureau \"just won't get its talons out of him\" even though he is retired, and calls Edgar \"such a sensitive man\".",
        "Emily est la femme de Ross ; en 1914, le couple vit dans une cabane au bord du lac Don Julio (voir la biographie). Quand Jack annonce une lettre pour son mari, elle se plaint que le Bureau \"just won't get its talons out of him\" (ne veut pas desserrer ses griffes) alors qu'il est à la retraite, et dit d'Edgar qu'il est \"such a sensitive man\" (un homme si sensible).")},
    {"img": None, "slug": None, "name": "Phillip Ross", "text": two(
        "Phillip is Ross's brother and his hunting companion in 1914. He sends Jack downriver to Edgar (see Biography) and warns him not to get on his brother's bad side, because he has \"a filthy temper\".",
        "Phillip est le frère de Ross, avec qui il chasse en 1914. Il envoie Jack en aval, vers Edgar (voir la biographie), et lui conseille de ne pas contrarier son frère, qui a \"a filthy temper\" (un sale caractère).")},
    {"img": None, "slug": None, "name": "Howard Sawicki", "text": two(
        "Sawicki is a Bureau agent at Blackwater station in 1914. He never worked with Ross but knows his reputation: \"Fine man if you wanted results.\" Jack learns from him where Ross has retired (see Biography).",
        "Sawicki est un agent du Bureau en poste à la gare de Blackwater en 1914. Il n'a jamais travaillé avec Ross mais connaît sa réputation : \"Fine man if you wanted results.\" (un homme de valeur, si l'on voulait des résultats). C'est par lui que Jack apprend où Ross s'est retiré (voir la biographie).")},
]
