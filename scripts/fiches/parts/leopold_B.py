"""Leopold Strauss, part B: Personality (official descriptions, traits, In his own words, Names, Appearance),
Skills (bookkeeping and camp ledger, cards, weapons and horse), Relationships (20 Oct 2026, medium tier).

Sources (register):
- Rockstar character description of 6 Sep 2018 (English text as reprinted by The Hollywood Reporter / Heat
  Vision, Sep 2018, saved in ../uncle/fc/thr_descriptions.txt, line 122; French text from
  rockstargames.com/reddeadredemption2/fr/features/vanderlindegang, as quoted by the French Red Dead Wiki page
  "Leopold Strauss", leopold/fr.txt, line 39).
- A character page from an official guide (wiki file LeopoldStraussBio.jpg, uploaded 12 Nov 2018, downloaded to
  leopold/fcB/bio.png and read; text quoted verbatim in leopold/fcB/guide_bio.txt). Wikipedia's "List of Red Dead
  Redemption 2 characters" cites the same facts to the official guide (Price 2018, p. 374); the edition is not
  named on the page, so the text says "an official guide". The Austro-Hungarian anachronism is noted by the Red
  Dead Wiki (Trivia) and by TheGamer (Jerrad Wyche, 5 Sep 2019, leopold/fcB/thegamer.txt).
- Transcripts: "Money Lending and Other Sins I & II" ("Herr Morgan", "Mr. Strauss", "It's legal work, Mr. Morgan.
  Debtors belong in prison... we are doing them a favor.", "Put the debts in the deed box and try not to kill
  them... it's very bad for business.", Chick Matthews "German shouldn't a lent to me then", Arthur to Wrobel "a
  German man", "Leopold Strauss"); "Money Lending and Other Sins III" ("Not so gentle. I don't like his kind.
  Superior."; "people who aren't desperate... don't seem so interested in my propositions"; the "Are you okay?"
  scene after Mary's letter); "Money Lending and Other Sins IV" ("I prefer to call it banking.", "No, but I am the
  one feeding the women and children in the camp. What choice do we have, Mr. Morgan?", Winton Holmes "the
  German-speaking feller"); "Eastward Bound" (Strauss heads into town to "strike up a little business"; "Of
  course, Herr Strauss"; Hosea's "creepy little smile" line); "Enter, Pursued by a Memory" ("Come on, Herr
  Strauss. Let's get warm."); "The New South" (Hosea: Cornwall business "scaring the living daylights out of Mr.
  Strauss"); "Who is Not Without Sin" ("I can smell the whiskey from here.").
- Red Dead Wiki EN "Leopold Strauss" (infobox: mounts Morgan / Tennessee Walker; Personality; Appearance; Trivia:
  revolvers, poker brother, Susan and Pearson at night, reactions to the expulsion, the alternative departure);
  "Camp Events" (Horseshoe Overlook: Edith Downes' visit, Micah at the campfire, Swanson begging, Bill and
  "Australia", desk during Sean's party; Clemens Point: Bill and the Cornwall shooting; Shady Belle: coffee with
  Hosea, absence from Jack's party); "Camps" (camp ledger unlocked by the first debt, ledger next to the donation
  box, "Strauss's wagon" upgrades = tonics and liquors, camp poker players); "Money Lending and Other Sins I/II"
  (donation box unlocks the ledger); "Money Lending and Other Sins VI & VII" (Trivia: Susan and Pearson wake up;
  reactions); "The Sheep and the Goats" (Strauss wrestles the gun from his captor; shot in the leg, put on John's
  horse); "A Fine Night of Debauchery" (Trivia: wine bottle on a guard); "Orville Swanson" (Trivia: begging, Beaver
  Hollow conversation); "Icarus and Friends" (Trivia: Sadie on Strauss's nerves); "Fleeting Joy" (Strauss credits
  Sadie); "Bare Knuckle Friendships" (1907 news); "Horsemen, Apocalypses" (gallery: sheltering in the house).
- Fact-checked fiches reused as is: arthur_D (Strauss entry), dutch_C, hosea_B, bill_B, micah_B, sadie_B, susan_B,
  simon_B, javier_B, charles_B, abigail_A.

Ownership (FIX_RULES): the official descriptions (Rockstar 6 Sep 2018 and the guide page) live HERE only; part A
Origins and part C Marketing must not quote them. Names, appearance, skills (ledger, poker, weapons, horse) and
ALL camp scenes live HERE, each in ONE relationship entry: Edith's camp visit and "sick anyway" -> Downes entry;
Sean's party at the desk -> Arthur (the "Are you okay?" scene and the alternative departure are told in part A); usury trip of
"Eastward Bound", saloon argument -> Dutch; Colter, "creepy little smile", New South joke, coffee -> Hosea;
Germany/Australia, Cornwall leg -> Bill; campfire -> Micah; begging, whiskey line, Beaver Hollow talk -> Swanson;
night expulsion witnesses -> Susan / Pearson; reactions to the expulsion -> each speaker's entry. Narrative mission
events (debt collections, Downes beating, Cornwall ambush, riverboat, expulsion, 1907 news) live in part A;
relationship entries refer to them in one clause.

Lines quoted in this part (parts A and C must NOT repeat them; A paraphrases): the Rockstar and guide descriptions;
"It's legal work, Mr. Morgan. Debtors belong in prison... we are doing them a favor."; "Well, people who aren't
desperate... don't seem so interested in my propositions."; "I prefer to call it banking."; "No, but I am the one
feeding the women and children in the camp. What choice do we have, Mr. Morgan?"; "Not so gentle. I don't like his
kind. Superior."; "Put the debts in the deed box and try not to kill them... it's very bad for business."; "I can
smell the whiskey from here."; the name forms ("Herr Strauss", "Mr. Strauss", "Herr Morgan", "German shouldn't a lent
to me then", "the German-speaking feller"). Part C may still use "Nice watch. Yes, it's a Reutlinger alright.", "I
don't believe in absolutes, just shades of gray. Compromises.", "I rather fancied Australia...", the Anna/brother
line, "You know... they-they say the sick delude themselves. I was your friend." and "Your commitment to your duties
is admirable...".

WIKI-ONLY (kept, attributed or paraphrased without quotation marks): all camp-events material (no transcripts), the
poker remark about his brother, the revolvers, the horses, the wine bottle, Sadie's "bundle of nerves" remark, the
Beaver Hollow distress with Susan and Swanson, the reactions to the expulsion, the alternative departure.

Excluded: the wiki's "thus achieving his own redemption" and "sacrificed himself for the gang" (interpretation);
"likely because it went against their original code" (wiki reading); the wiki's appearance details "long nose, big
ears, thin lips, large mouth" and the outfit catalogue (reduced to the guide portrait); "53-year-old" (derived from
the wiki's own birth estimate); the speculation that he is Jewish and the Leo Strauss name origin (speculation);
that Strauss knew Downes was sick (FR wiki speculation); the FR wiki's "libraire (anciennement)" (no source);
John's 1907 reaction (part A/C); the cut reading-glasses request and unused vest and boots (part D).
"""


def two(en, fr): return {"en": en, "fr": fr}


# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar Games' official description of Strauss, published on September 6, 2018 (see Marketing), reads: \"Originally hailing from Austria, Herr Strauss is responsible for keeping the gang's books and running their money lending operation. A serious, somewhat shifty and unemotional man, he has all the qualities a loan shark needs.\"",
        "La description officielle de Strauss publiée par Rockstar Games le 6 septembre 2018 (voir Promotion) dit, dans sa version française : \"Originaire d'Autriche, Herr Strauss tient les comptes de la bande et gère les entrées comme les sorties d'argent. Son austérité, ses manières louches et son regard impassible lui confèrent toutes les qualités nécessaires à un usurier.\"")},
    {"p": two(
        "A character page from an official guide, reproduced on the Red Dead Wiki, repeats that description and adds his background: \"He grew up very poor in Vienna, in the Austro-Hungarian Empire, and had some serious health problems during childhood. At age 17, the young Strauss was sent on a boat to the New World. After years of scamming the wrong people, he fell in with Dutch mainly for protection and has been with him ever since.\" The Red Dead Wiki and TheGamer (September 5, 2019) both point out that the Austro-Hungarian Empire was only created in 1867, years after the childhood the guide describes.",
        "Une page de personnage tirée d'un guide officiel, reproduite sur le Red Dead Wiki, reprend cette description et y ajoute son passé : \"He grew up very poor in Vienna, in the Austro-Hungarian Empire, and had some serious health problems during childhood. At age 17, the young Strauss was sent on a boat to the New World. After years of scamming the wrong people, he fell in with Dutch mainly for protection and has been with him ever since.\" (il a grandi dans une grande pauvreté à Vienne, dans l'Empire austro-hongrois, et a eu de graves problèmes de santé enfant ; à 17 ans, il est envoyé par bateau vers le Nouveau Monde ; après des années à escroquer les mauvaises personnes, il s'est rangé auprès de Dutch, surtout pour sa protection, et ne l'a plus quitté). Le Red Dead Wiki et TheGamer (5 septembre 2019) relèvent tous deux que l'Empire austro-hongrois n'a été créé qu'en 1867, bien après l'enfance décrite par le guide.")},
    {"p": two(
        "In camp he works at his desk and skips the gang's parties, according to the Red Dead Wiki's camp events page. The wiki also notes a sarcastic wit, aimed mostly at Arthur. After chapter 4, the Red Dead Wiki describes him as increasingly anxious for the gang's safety; at Beaver Hollow he talks to Susan Grimshaw about the situation, stammering as he speaks.",
        "Au camp, il travaille à son bureau et ne se mêle pas aux fêtes de la bande, d'après la page du Red Dead Wiki consacrée aux événements de camp. Le wiki lui prête aussi un humour sarcastique, qui vise surtout Arthur. Après le chapitre 4, le Red Dead Wiki le décrit de plus en plus inquiet pour la sécurité du groupe ; à Beaver Hollow, il fait part de ses craintes à Susan Grimshaw en bégayant.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "When Arthur mocks Dutch's talk of helping people in \"Money Lending and Other Sins I & II\", Strauss answers: \"It's legal work, Mr. Morgan. Debtors belong in prison... we are doing them a favor.\" Told that Thomas Downes is dying and destitute, he replies in \"Money Lending and Other Sins III\": \"Well, people who aren't desperate... don't seem so interested in my propositions.\" Earlier in the same mission, he tells Arthur how to treat Downes: \"Not so gentle. I don't like his kind. Superior.\"",
        "Quand Arthur ironise sur les beaux discours de Dutch sur l'aide aux petites gens, dans \"Money Lending and Other Sins I & II\", Strauss répond : \"It's legal work, Mr. Morgan. Debtors belong in prison... we are doing them a favor.\" (c'est un travail légal, Mr. Morgan ; la place des débiteurs est en prison, nous leur rendons service). Quand Arthur lui apprend que Thomas Downes est mourant et sans le sou, il réplique, dans \"Money Lending and Other Sins III\" : \"Well, people who aren't desperate... don't seem so interested in my propositions.\" (les gens qui ne sont pas aux abois ne s'intéressent guère à mes offres). Plus tôt dans la même mission, il précise comment traiter Downes : \"Not so gentle. I don't like his kind. Superior.\" (pas si gentiment ; je n'aime pas les gens de son espèce, qui se croient supérieurs).")},
    {"p": two(
        "At Clemens Point, in \"Money Lending and Other Sins IV\", Arthur calls his trade sharking. Strauss corrects him: \"I prefer to call it banking.\" When Arthur points out that he is not the one handing out the beatings, Strauss answers: \"No, but I am the one feeding the women and children in the camp. What choice do we have, Mr. Morgan?\"",
        "À Clemens Point, dans \"Money Lending and Other Sins IV\", Arthur qualifie son activité d'usure. Strauss le reprend : \"I prefer to call it banking.\" (je préfère parler de banque). Quand Arthur lui fait remarquer que ce n'est pas lui qui distribue les coups, Strauss rétorque : \"No, but I am the one feeding the women and children in the camp. What choice do we have, Mr. Morgan?\" (non, mais c'est moi qui nourris les femmes et les enfants du camp ; quel autre choix avons-nous, Mr. Morgan ?).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Dutch, Hosea and Arthur address him as \"Herr Strauss\", and Arthur and Hosea also say \"Mr. Strauss\". He calls Arthur \"Herr Morgan\" or \"Mr. Morgan\". His first name is rarely used: Arthur gives his full name, Leopold Strauss, to the debtors Wróbel and Gwyn Hughes. Several debtors take him for a German. Chick Matthews shouts \"German shouldn't a lent to me then\" as he flees, Arthur himself tells Wróbel that he borrowed from \"a German man\", and Winton Holmes calls him \"the German-speaking feller\". Wróbel, in Polish, warns against trusting Prussians.",
        "Dutch, Hosea et Arthur l'appellent \"Herr Strauss\", et Arthur comme Hosea disent aussi \"Mr. Strauss\". Lui appelle Arthur \"Herr Morgan\" ou \"Mr. Morgan\". Son prénom sert rarement : Arthur donne son nom complet, Leopold Strauss, aux débiteurs Wróbel et Gwyn Hughes. Plusieurs débiteurs le prennent pour un Allemand. Chick Matthews lance \"German shouldn't a lent to me then\" (l'Allemand n'avait qu'à pas me prêter) en s'enfuyant, Arthur lui-même dit à Wróbel qu'il a emprunté à \"a German man\" (un Allemand), et Winton Holmes parle du \"German-speaking feller\" (le type qui parle allemand). Wróbel, en polonais, met en garde contre les Prussiens.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "The guide's portrait shows a thin, older man with short gray hair, light eyes and round wire-rimmed glasses, wearing a striped shirt, a blue cravat, a waistcoat and tall boots, holding a ledger in front of his chest. According to the Red Dead Wiki, he wears a colored scarf at Colter, and a gallery picture shows him in pajamas at Horseshoe Overlook.",
        "Le portrait du guide montre un homme âgé et maigre, aux cheveux gris courts, aux yeux clairs et aux lunettes rondes cerclées de métal, vêtu d'une chemise rayée, d'une lavallière bleue, d'un gilet et de hautes bottes, un registre tenu contre la poitrine. D'après le Red Dead Wiki, il porte une écharpe de couleur à Colter, et une image de la galerie du wiki le montre en pyjama à Horseshoe Overlook.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Skills, weapons and horse", "Compétences, armes et cheval")},
    {"h4": two("Money lending and the camp ledger", "Prêts et registre du camp")},
    {"p": two(
        "Strauss lends the gang's money to outsiders and sends Arthur to collect. According to the Red Dead Wiki's mission and camps pages, dropping any of those first debts into the donation box beside Dutch's tent unlocks the camp ledger, which lies next to it. The ledger is used to buy camp upgrades and restock the wagons. One of the wagons is Strauss's: its three upgrades add more kinds of tonics and liquors to the camp's supplies.",
        "Strauss prête l'argent du gang à des gens de l'extérieur et envoie Arthur recouvrer les dettes. D'après les pages du Red Dead Wiki consacrées à la mission et aux camps, déposer l'une de ces premières dettes dans la caisse des dons, près de la tente de Dutch, débloque le registre du camp, posé juste à côté. Le registre sert à acheter des améliorations et à réapprovisionner les chariots. L'un des chariots est celui de Strauss : ses trois améliorations ajoutent davantage de toniques et d'alcools aux réserves du camp.")},
    {"h4": two("Cards", "Cartes")},
    {"p": two(
        "Strauss is one of the camp's poker players, with John, Pearson, Susan, Uncle, Lenny and Swanson, according to the Red Dead Wiki. His card sense is put to use on the riverboat in \"A Fine Night of Debauchery\" (see Biography).",
        "Strauss fait partie des joueurs de poker du camp, avec John, Pearson, Susan, Uncle, Lenny et Swanson, selon le Red Dead Wiki. Son sens du jeu sert sur le bateau à aubes, dans \"A Fine Night of Debauchery\" (voir la biographie).")},
    {"h4": two("Weapons and horse", "Armes et cheval")},
    {"p": two(
        "According to the Red Dead Wiki, Strauss holds a pair of Double-Action revolvers in the game's third trailer and when Agent Milton first comes to the camp. When he leaves the camp in chapter 6, he rides away, according to the wiki, on one of the camp's spare horses, a Morgan or a Tennessee Walker.",
        "D'après le Red Dead Wiki, Strauss tient une paire de revolvers Double-Action dans la troisième bande-annonce du jeu et lors de la première visite de l'agent Milton au camp. Quand il quitte le camp au chapitre 6, il part, toujours selon le wiki, sur l'un des chevaux de réserve du camp, un Morgan ou un Tennessee Walker.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "Arthur collects Strauss's debts from chapter 2 to chapter 6, beats Thomas Downes on his behalf, and can throw him out of the gang at Beaver Hollow (see Biography). During the party for Sean's return Arthur can invite him to join in; Strauss says he is in an excellent mood and stays at his desk.",
            "Arthur recouvre les dettes de Strauss du chapitre 2 au chapitre 6, roue de coups Thomas Downes pour son compte, et peut le chasser du gang à Beaver Hollow (voir la biographie). Pendant la fête du retour de Sean, Arthur peut l'inviter à se joindre à la fête ; Strauss répond qu'il est d'excellente humeur et reste à son bureau."),
    ]},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Strauss keeps the books of Dutch's gang. When he leaves to lend money in Valentine in \"Eastward Bound\", Dutch sees him off with \"Of course, Herr Strauss\". In \"The Sheep and the Goats\" Arthur and John find the two men arguing in Keane's Saloon, and at Lakay Strauss credits Sadie when Dutch returns (see Biography).",
        "Strauss tient les comptes du gang de Dutch. Quand il part prêter de l'argent à Valentine, dans \"Eastward Bound\", Dutch le laisse aller d'un \"Of course, Herr Strauss\" (bien sûr, Herr Strauss). Dans \"The Sheep and the Goats\", Arthur et John trouvent les deux hommes en pleine dispute au Keane's Saloon, et à Lakay, Strauss attribue le mérite à Sadie au retour de Dutch (voir la biographie).")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "At Colter, Hosea leads him away from the cold: \"Come on, Herr Strauss. Let's get warm.\" On the fishing trip of \"The New South\", Hosea jokes that the Cornwall business scared the living daylights out of Mr. Strauss. At Shady Belle Strauss explains to him by the fountain what real coffee is; Hosea answers, sarcastically, that he looks forward to it.",
        "À Colter, Hosea l'entraîne à l'abri du froid : \"Come on, Herr Strauss. Let's get warm.\" (venez, Herr Strauss, allons nous réchauffer). Pendant la partie de pêche de \"The New South\", Hosea plaisante sur l'affaire Cornwall, qui a fait une peur bleue à Mr. Strauss. À Shady Belle, près de la fontaine, Strauss lui explique ce qu'est un vrai café ; Hosea répond, ironique, qu'il a hâte de goûter ça.")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "Held hostage together in Valentine in \"The Sheep and the Goats\", the two men escape on John's horse (see Biography). In 1907 John learns of Strauss's death from Charles (see Charles Smith).",
        "Pris ensemble en otage à Valentine dans \"The Sheep and the Goats\", les deux hommes s'enfuient sur le cheval de John (voir la biographie). En 1907, John apprend la mort de Strauss de la bouche de Charles (voir Charles Smith).")},
    {"img": "charles-smith.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
        "Charles is the one who tells John, in 1907, of Strauss's death in Pinkerton custody (see Biography).",
        "C'est Charles qui apprend à John, en 1907, la mort de Strauss aux mains de la Pinkerton (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Eating with Strauss at Horseshoe Overlook, Bill asks him what people eat in Germany. Strauss corrects him: he is Austrian. Bill then asks what they eat in Australia, and Strauss remarks that it is a miracle Bill does not fall over more often. At Clemens Point Bill tells him he heard Strauss soiled himself during the Cornwall business in Valentine; Strauss corrects him again, saying he was shot in the leg. After the expulsion, according to the Red Dead Wiki, Bill asks Arthur whether he will be thrown out next, and Arthur does not deny it.",
        "En mangeant avec Strauss à Horseshoe Overlook, Bill lui demande ce qu'on mange en Allemagne. Strauss le reprend : il est autrichien. Bill demande alors ce qu'on mange en Australie, et Strauss trouve miraculeux que Bill ne tombe pas plus souvent. À Clemens Point, Bill lui lance qu'il paraît qu'il s'est fait dessus pendant l'affaire Cornwall à Valentine ; Strauss le reprend encore : il a reçu une balle dans la jambe. Après l'expulsion, selon le Red Dead Wiki, Bill demande à Arthur s'il sera le prochain à être chassé, et Arthur ne le dément pas.")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "At the Horseshoe Overlook campfire Micah questions Strauss's methods. Strauss defends his business. Micah answers that he prefers to shoot a man openly rather than play his friend and stab him in the back, at least most of the time. Strauss leaves, uncomfortable. When Arthur throws Strauss out at Beaver Hollow, Micah argues with him, saying Strauss was too much of an asset to lose.",
        "Au coin du feu, à Horseshoe Overlook, Micah critique les méthodes de Strauss. Strauss défend son commerce. Micah rétorque qu'il aime mieux abattre un homme en face que jouer les amis pour le frapper dans le dos, du moins la plupart du temps. Strauss s'éloigne, gêné. Quand Arthur chasse Strauss à Beaver Hollow, Micah s'en prend à lui : pour Micah, Strauss était un atout trop précieux pour s'en séparer.")},
    {"img": "orville-swanson.jpeg", "slug": "orville-swanson", "name": "Orville Swanson", "text": two(
        "At Horseshoe Overlook, Swanson's request for money at Strauss's desk is turned down before he has finished asking, because of what he already owes. When Swanson says he is dying, Strauss wants to know how a dying man would pay him back; Swanson walks off calling him heartless. When Arthur carries the drunk Reverend back to camp in \"Who is Not Without Sin\", Strauss comments: \"I can smell the whiskey from here.\" At Beaver Hollow, according to the Red Dead Wiki, Strauss confides his distress to a now sober Swanson, who answers with hope, and Strauss dismisses him as mad. Swanson approves of the expulsion, saying it was time.",
        "À Horseshoe Overlook, Swanson vient demander de l'argent au bureau de Strauss, qui refuse avant même la fin de sa phrase, vu ce qu'il doit déjà. Quand Swanson dit qu'il va mourir, Strauss veut savoir comment un mourant le rembourserait ; Swanson s'en va en le traitant de sans-cœur. Quand Arthur ramène au camp le révérend ivre mort, dans \"Who is Not Without Sin\", Strauss lâche : \"I can smell the whiskey from here.\" (je sens le whiskey d'ici). À Beaver Hollow, selon le Red Dead Wiki, Strauss confie son angoisse à un Swanson devenu sobre, qui lui répond avec espoir, et Strauss le prend pour un fou. Swanson approuve l'expulsion : selon lui, il était temps.")},
    {"img": "sadie-adler.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
        "Strauss is among the survivors Sadie leads to Lakay while Dutch's group is on Guarma, and he credits her for their safety when Dutch returns (see Biography). According to the Red Dead Wiki, in \"Icarus and Friends\" she tells Arthur that Strauss is a bundle of nerves. When Arthur throws him out, Sadie approves and says she won't miss him.",
        "Strauss fait partie des survivants que Sadie conduit à Lakay pendant que le groupe de Dutch est à Guarma, et il lui attribue leur salut au retour de Dutch (voir la biographie). D'après le Red Dead Wiki, dans \"Icarus and Friends\", elle confie à Arthur que Strauss a les nerfs à vif. Quand Arthur le chasse, Sadie approuve et dit qu'il ne lui manquera pas.")},
    {"img": "susan-grimshaw.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
        "At Beaver Hollow Susan and Pearson sleep next to Strauss. If Arthur throws him out at night, the two wake up and watch, frightened, as Arthur pushes Strauss toward their beds while he packs. According to the Red Dead Wiki, Susan tells Arthur afterward that she knows he did the right thing and will not protest.",
        "À Beaver Hollow, Susan et Pearson dorment à côté de Strauss. Si Arthur le chasse de nuit, tous deux se réveillent et regardent, effrayés, Arthur pousser Strauss vers leurs lits pendant qu'il fait ses bagages. D'après le Red Dead Wiki, Susan dit ensuite à Arthur qu'elle sait qu'il a bien agi et qu'elle ne protestera pas.")},
    {"img": "simon-pearson.jpeg", "slug": "simon-pearson", "name": "Simon Pearson", "text": two(
        "Pearson wakes up beside Susan when Arthur throws Strauss out at night (see Susan Grimshaw). According to the Red Dead Wiki, Pearson tells Arthur afterward that he is disappointed Arthur did not consult the others first.",
        "Pearson se réveille aux côtés de Susan quand Arthur chasse Strauss de nuit (voir Susan Grimshaw). D'après le Red Dead Wiki, Pearson reproche ensuite à Arthur de ne pas avoir consulté les autres.")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "Abigail shelters in the Shady Belle house with him in \"Horsemen, Apocalypses\" (see Biography). According to the Red Dead Wiki, she later tells Arthur, like Pearson, that she is disappointed he threw Strauss out without asking the others.",
        "Abigail s'abrite avec lui dans la maison de Shady Belle, dans \"Horsemen, Apocalypses\" (voir la biographie). D'après le Red Dead Wiki, elle reproche ensuite à Arthur, comme Pearson, d'avoir chassé Strauss sans demander l'avis des autres.")},
    {"img": "tilly-jackson.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
        "After the expulsion, according to the Red Dead Wiki, Tilly asks Arthur whether he means to throw her out too; Arthur assures her he does not.",
        "Après l'expulsion, selon le Red Dead Wiki, Tilly demande à Arthur s'il compte la chasser elle aussi ; Arthur lui assure que non.")},
    {"img": "mary-beth-gaskill.jpeg", "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill", "text": two(
        "According to the Red Dead Wiki, Mary-Beth asks Arthur why he threw Strauss out, and he explains his reasons to her.",
        "D'après le Red Dead Wiki, Mary-Beth demande à Arthur pourquoi il a chassé Strauss, et il lui explique ses raisons.")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "Jack also asks Arthur where Strauss has gone; according to the Red Dead Wiki, Arthur does not tell him.",
        "Jack demande lui aussi à Arthur où est passé Strauss ; d'après le Red Dead Wiki, Arthur ne lui dit rien.")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "On the riverboat of \"A Fine Night of Debauchery\", Strauss can save Javier from a guard who takes aim at his back (see Biography). The four men share the take once ashore.",
        "Sur le bateau à aubes de \"A Fine Night of Debauchery\", Strauss peut sauver Javier d'un garde qui le met en joue dans son dos (voir la biographie). Les quatre hommes se partagent le butin une fois à terre.")},
    {"img": "josiah-trelawny.jpeg", "slug": "josiah-trelawny", "name": "Josiah Trelawny", "text": two(
        "Trelawny plans the riverboat job of \"A Fine Night of Debauchery\", and the two men rig its poker game together, according to the mission page. They escape from the boat with Arthur and Javier (see Biography).",
        "Trelawny monte le coup du bateau à aubes de \"A Fine Night of Debauchery\", et les deux hommes truquent ensemble la partie de poker, d'après la page de la mission. Ils s'échappent du bateau avec Arthur et Javier (voir la biographie).")},
    {"img": "leviticus-cornwall.jpeg", "slug": "leviticus-cornwall", "name": "Leviticus Cornwall", "text": two(
        "In \"The Sheep and the Goats\" the industrialist's guards hold Strauss and John hostage in Valentine to draw Dutch out, after the gang robbed Cornwall's train (see Biography).",
        "Dans \"The Sheep and the Goats\", les gardes de l'industriel prennent Strauss et John en otage à Valentine pour forcer Dutch à se montrer, après le braquage du train de Cornwall par la bande (voir la biographie).")},
    {"img": None, "slug": None, "name": "Thomas and Edith Downes", "text": two(
        "Thomas Downes, a farmer Strauss met in Valentine, is the debtor Arthur beats in \"Money Lending and Other Sins III\" (see Biography). According to the Red Dead Wiki's camp events page, his widow Edith may later come to the Horseshoe Overlook camp with part of the money and tell Strauss of her husband's death. If Arthur is nearby, he can say he did not mean to kill Downes; Strauss remarks, unmoved, that the man was sick anyway. The wiki's character page gives another version, in which Edith curses Strauss and he passes the debt on to her.",
        "Thomas Downes, fermier que Strauss a rencontré à Valentine, est le débiteur qu'Arthur roue de coups dans \"Money Lending and Other Sins III\" (voir la biographie). D'après la page du Red Dead Wiki consacrée aux événements de camp, sa veuve Edith peut ensuite venir au camp de Horseshoe Overlook apporter une partie de l'argent et annoncer à Strauss la mort de son mari. Si Arthur est là, il peut dire qu'il ne voulait pas tuer Downes ; Strauss fait remarquer, impassible, que l'homme était malade de toute façon. La page du personnage sur le wiki donne une autre version, où Edith maudit Strauss et où celui-ci lui transfère la dette.")},
]
