"""Simon Pearson, part B: Personality (official descriptions, traits, In his own words, Names, Appearance),
Skills (cooking, camp crafting, music, item requests), Relationships (20 Oct 2026, medium tier).

Sources (register):
- Rockstar character description of 6 Sep 2018 (English text as reprinted by The Hollywood Reporter / Heat Vision,
  Sep 2018, saved in ../uncle/fc/thr_descriptions.txt, line 134; French text from
  rockstargames.com/reddeadredemption2/fr/features/vanderlindegang, as quoted by the French Red Dead Wiki page
  "Simon Pearson", simon/fr.txt line 43).
- A character page from an official guide (wiki file PearsonBio.jpg, captioned "Biography in RDR 2", uploaded
  12 Nov 2018 by Blaff 60, downloaded through the wiki API to simon/fcB/PearsonBio.png and read; text quoted verbatim
  in simon/fcB/guide_bio.txt). Wikipedia's "List of Red Dead Redemption 2 characters" cites the same facts to the
  official guide (Price 2018, p. 376); the edition is not named on the page, so the text says "an official guide".
  NB: the guide says "a short stint at sea"; Rockstar's 2018 text says "in the navy". Both are quoted as written.
- Red Dead Wiki EN "Simon Pearson" (infobox, quote box, Personality, Appearance, Crafting Upgrades tables, Quotes,
  Trivia) and FR "Simon Pearson"; "Camp Events" (../hosea/m/Camp_Events.txt: Horseshoe Overlook, Sean's Return
  Party, Clemens Point, Shady Belle, Jack's Return Party); "Errand Boy" (item requests); "Dominoes" (chapter 4
  partners); "Hunting (Simon Pearson)"; "Revenge is a Dish Best Eaten" (trivia: the "repulsive little maggot" line);
  "Leopold Strauss" and "Money Lending and Other Sins VI & VII" (Strauss's expulsion, sleeping scene); "Orville
  Swanson" (trivia: members not shown committing crimes); "Susan Grimshaw" (defends his cooking); "Ethel Pearson",
  "Rhodes General Store" (fetched 20 Oct 2026); "Letter from Tilly" (fetched 20 Oct 2026, verbatim "angry Mr.
  Pearson").
- Transcripts: "Outlaws from the West" (Susan: "Mr. Pearson, see what we've got in terms of food"); "The Aftermath of
  Genesis" (Pearson's complaint about Lenny and Bill, the can of offal, rum shared after the hunt); "Blessed are the
  Peacemakers" (Micah: "you tell him, fat man", "Get the words out properly, fat man", "old Mr. Pearson"); "Old
  Friends" (Dutch leaves "Mr. Matthews, Mr. Smith, Mr. Pearson" to watch the camp).
- Fact-checked fiches reused as is: arthur_B, charles_B, bill_B, hosea_B, javier_B, lenny_B, kieran_B, susan_B,
  sean_B, sadie_B, micah_B, abigail_B, jack_B, tilly_B, uncle_B, dutch_B, karen_B.

Ownership (FIX_RULES): the official descriptions (Rockstar 6 Sep 2018 and the guide page) live HERE only; part A
Origins and part C Marketing must not quote them (C may say Rockstar published descriptions on 6 Sep 2018). Names
(Pearson, Mr. Pearson, "fat man", "angry Mr. Pearson", Tacitus Kilgore per the wiki), appearance, skills (cooking and
food appeals, satchels and camp decorations, item requests, accordion and songs, dominoes) and ALL camp scenes live
HERE, each in ONE relationship entry: gazebo talk and the cooking defence -> Susan; Navy confession, dominoes ->
Arthur; worst-life argument, Congo, Brazil, "maggot" -> Uncle; songs (Skills), "get some food", white rabbit ->
Sean; vegetables and cleaver -> Sadie; Tahiti/Bali/Java and "best actress" -> Hosea; fish and punch -> Bill; money
thrown -> Micah; mud and Watson's Cabin -> Javier; Jack missing on the dock -> Abigail; mockery of his cooking ->
Mary-Beth (Lenny pointer); shark story -> Kieran; sleeping next to Strauss and the expulsion -> Strauss; dish
debate about Susan -> Karen. Narrative mission events (Colter hunt, Old Friends guard duty, the parley in "Blessed
are the Peacemakers", the apology, the crayfish outing, Lakay, Molly's body, Kieran's burial, the departure, the
1907 store and John's visits) live in part A; relationship entries refer to them in one clause.

Lines quoted in this part (parts A and C must NOT repeat them; A paraphrases): the Rockstar and guide descriptions;
the wiki quote box "I once saw the cape from a forty foot swell..." (Shady Belle, to Susan); "the only thing I cannot
cook is air" (camp speech, wiki quote list); "You know you could trade these or sell these in pretty much any town..."
(pelts, wiki quote list); "Mr. Pearson" (Outlaws from the West), "fat man" (Blessed are the Peacemakers), "angry Mr.
Pearson" (Letter from Tilly). Part C keeps the mission lines: "Like a cornered tiger", "stranded at sea... for fifty
days", "Navy rum, sir", "we need food... real food", "God's own pantry", "Nothing like good honest labour" and the
1907 line about the Grays and the Braithwaites.

WIKI-ONLY (kept, attributed or paraphrased without quotation marks): all camp events (no transcripts), the cleaver
and "watch her mouth" (wiki Personality), the Sumatra mention, the crafting tables (game content), item requests,
the "maggot" exchange, the hunting knife, the anchor tattoo and 1907 look, the Tacitus Kilgore alias, Ethel's
details (second wife, upstairs, told too much while drunk, mean nature), the ex-wife Michele (infobox only), the
Strauss disappointment, the "no crimes" remark.

Excluded: the wiki's "in denial" and "loud and jolly degenerate" as the wiki's own judgment (Rockstar's and the
guide's wording is quoted instead); "though whether this is just an exaggeration is unclear" (interpretation);
"he seems to get along very well with Hosea" kept only as attributed in the Hosea entry; the wiki claim that
Pearson, Mary-Beth and Uncle told Tilly they were leaving (uncle FIX_RULES: departure not shown; Dutch's
announcement is in part A); "It can also be assumed that he lives in Scarlett Meadows" (assumption); the epilogue
winter coat "despite Lemoyne being one of the hottest regions" (judgment; coat itself left to part C trivia if
wanted); the outfit catalogue (reduced to the guide portrait and the 1907 apron); item requests and dominoes (moved to the
Missions table in part C, where the poker condition of the compass request is attributed to the Errand Boy page); a horse (none sourced); the epilogue line about John
missing Pearson's cooking (the wiki's Abigail page gives it without a scene); Sean "ordering" to eat kept as
written by the camp events page.
"""

def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar Games introduced Pearson on September 6, 2018 with a short description: \"The camp's butcher and cook, Pearson served a short stint in the navy that he likes to talk about at length. A loud, jolly degenerate who is somewhat in denial about the turn his life has taken.\"",
        "Rockstar Games présente Pearson le 6 septembre 2018 dans un court texte. La version française publiée par Rockstar dit : \"Boucher et cuisinier du camp, Pearson pourrait parler des heures de son passage éclair dans la marine. Éternel optimiste un peu simplet, il ne semble pas s'être rendu compte du tournant qu'a pris sa vie.\"")},
    {"p": two(
        "A character page from an official guide, reproduced on the Red Dead Wiki, gives a longer version: \"The gang's butcher and camp cook, Pearson did a short stint at sea that he likes to talk about at length. His father and grandfather were both sperm whale hunters and he was going to follow in their footsteps but, by the time he left school, nobody wanted whale oil any more. He came out west and got in some bad trouble with some men who were shaking him down for money. Dutch found him at his wit's end and took him under his wing. He is a loud, jolly degenerate who puts on a brave face, but is somewhat in denial about the turn his life has taken.\"",
        "Une page de personnage tirée d'un guide officiel, reproduite sur le Red Dead Wiki, en donne une version plus longue. Pearson y est le boucher et le cuisinier du camp, qui a passé peu de temps en mer mais en parle volontiers et longuement. Son père et son grand-père chassaient tous deux le cachalot, et il comptait prendre leur suite ; à sa sortie de l'école, plus personne ne voulait d'huile de baleine. Parti vers l'Ouest, il s'y est attiré de graves ennuis avec des hommes qui le rackettaient. \"Dutch found him at his wit's end and took him under his wing\" (Dutch l'a trouvé à bout de ressources et l'a pris sous son aile). Le guide conclut : \"He is a loud, jolly degenerate who puts on a brave face, but is somewhat in denial about the turn his life has taken.\" (un bon vivant bruyant et dissipé, qui fait bonne figure mais refuse un peu de voir le tour qu'a pris sa vie).")},
    {"p": two(
        "In camp he worries out loud about the food supply and asks the others to bring in meat, fish or vegetables. He often talks about his years at sea (see Origins), to the point of presenting sardines as the sea monsters he fought. Uncle, Hosea and Mary-Beth hear some of them in camp scenes (see Relationships). He drinks often (see Biography).",
        "Au camp, il s'inquiète à voix haute des réserves et demande aux autres de rapporter viande, poisson ou légumes. Il parle souvent de ses années en mer (voir Origines), au point de faire des sardines les monstres marins qu'il a combattus. Uncle, Hosea et Mary-Beth en entendent certaines dans des scènes de camp (voir Relations). Il boit souvent (voir la biographie).")},
    {"p": two(
        "The move to Shady Belle weighs on him. He complains about the mud and the swamp (see Hosea Matthews and Susan Grimshaw). On a rainy night there, drunk, he walks around the camp saying that he does not want to die like an animal but like a gentleman cook (see Skills for the song that follows). He does not take part in the gang's robberies: the Red Dead Wiki counts him, with Reverend Swanson and Molly O'Shea, among the only members never shown taking part in a crime.",
        "Le déménagement à Shady Belle lui pèse. Il se plaint de la boue et du marais (voir Hosea Matthews et Susan Grimshaw). Un soir de pluie, ivre, il fait le tour du camp en répétant qu'il ne veut pas mourir comme une bête, mais en cuisinier digne de ce nom (la chanson qui suit est citée dans Compétences). Il ne prend pas part aux braquages : le Red Dead Wiki le range, avec le révérend Swanson et Molly O'Shea, parmi les seuls membres qu'on ne voit jamais prendre part à un crime.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "The Red Dead Wiki opens its page on him with what he tells Susan Grimshaw in the gazebo at Shady Belle: \"I once saw the cape from a forty foot swell. I once crossed the equator during a meteor shower, I rode into harbors surrounded by beautiful maidens selling pineapple, and colors, colors so brilliant they'd burn your eyes... and now, I live in a swamp, waiting to get shot for riding with outlaws.\" In a speech to the camp listed on the wiki's quote list, he demands more food: \"I'm talking meat, fish, vegetables, I can cook any of these things, the only thing I cannot cook is air.\" About animal pelts, he points out: \"You know you could trade these or sell these in pretty much any town, if you're looking to make a legitimate bit of money of course.\"",
        "Le Red Dead Wiki ouvre sa page sur ce qu'il confie à Susan Grimshaw sous le kiosque de Shady Belle : \"I once saw the cape from a forty foot swell. I once crossed the equator during a meteor shower, I rode into harbors surrounded by beautiful maidens selling pineapple, and colors, colors so brilliant they'd burn your eyes... and now, I live in a swamp, waiting to get shot for riding with outlaws.\" (j'ai vu le cap du haut d'une houle de douze mètres, j'ai passé l'équateur sous une pluie d'étoiles filantes, je suis entré dans des ports pleins de jolies filles qui vendaient des ananas, avec des couleurs si vives qu'elles vous brûlaient les yeux... et maintenant je vis dans un marais, en attendant de me faire abattre pour avoir suivi des hors-la-loi). Dans un discours au camp que recense la liste de citations du wiki, il réclame des vivres : \"I'm talking meat, fish, vegetables, I can cook any of these things, the only thing I cannot cook is air.\" (de la viande, du poisson, des légumes, je sais tout cuisiner, la seule chose que je ne sais pas cuisiner, c'est l'air). À propos des peaux de bêtes, il fait remarquer : \"You know you could trade these or sell these in pretty much any town, if you're looking to make a legitimate bit of money of course.\" (vous savez, on peut les échanger ou les vendre dans à peu près n'importe quelle ville, si on veut gagner un peu d'argent honnêtement, bien sûr).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Rockstar's description and the official guide call him only Pearson; the full name Simon Pearson is the one used by the Red Dead Wiki and Wikipedia. In the dialogue he is Pearson or Mr. Pearson: Susan Grimshaw calls him \"Mr. Pearson\" when she hands out the jobs at Colter in \"Outlaws from the West\", and Dutch uses the same form in \"Old Friends\". In \"Blessed are the Peacemakers\", Micah Bell calls him \"fat man\" twice. In her 1907 letter to John and Abigail, Tilly Jackson remembers him as \"angry Mr. Pearson\". The Red Dead Wiki also lists Tacitus Kilgore, the name the gang uses to receive mail, among his aliases; the letters the wiki reproduces under that name are addressed to Arthur.",
        "Rockstar et le guide officiel ne l'appellent que Pearson ; le nom complet de Simon Pearson est celui qu'emploient le Red Dead Wiki et Wikipédia. Dans les dialogues, on dit Pearson ou Mr. Pearson : Susan Grimshaw l'appelle \"Mr. Pearson\" en distribuant les tâches à Colter, dans \"Outlaws from the West\", et Dutch fait de même dans \"Old Friends\". Dans \"Blessed are the Peacemakers\", Micah Bell le traite deux fois de \"fat man\" (le gros). Dans sa lettre de 1907 à John et Abigail, Tilly Jackson se souvient de lui comme d'\"angry Mr. Pearson\" (ce grincheux de M. Pearson). Le Red Dead Wiki range aussi parmi ses alias Tacitus Kilgore, le nom sous lequel la bande reçoit son courrier ; les lettres que le wiki reproduit à ce nom sont toutefois adressées à Arthur.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "The guide's portrait shows a heavy-set man with long dark hair and a thick mustache, wearing a black top hat with a red band, a worn dark knit sweater over a white shirt, dark trousers and tall black boots. According to the Red Dead Wiki, the anchor tattooed on the back of his hand dates from his Navy years. By 1907, the wiki adds, his hair has turned gray and is nearly gone on top, and he wears a striped shirt under a full apron.",
        "Le portrait du guide montre un homme corpulent, aux longs cheveux bruns et à l'épaisse moustache, coiffé d'un haut-de-forme noir à ruban rouge, vêtu d'un pull sombre usé sur une chemise blanche, d'un pantalon foncé et de hautes bottes noires. D'après le Red Dead Wiki, l'ancre tatouée sur le dos de sa main date de ses années dans la marine. En 1907, ajoute le wiki, ses cheveux ont grisonné et le dessus de son crâne est presque chauve, et il porte une chemise rayée sous un grand tablier.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Skills, weapons and horse", "Compétences, armes et cheval")},
    {"h4": two("Cook and butcher", "Cuisinier et boucher")},
    {"p": two(
        "Pearson runs the camp kitchen: he cooks the daily stew at his chuckwagon and butchers the game brought in. Arthur can give him carcasses and other provisions, which go into the camp's food supply. When stocks run low he asks the camp for meat. From \"Our Best Selves\" onward, with Pearson gone, the camp stew is no longer available; the Red Dead Wiki's page on the mission suggests big game meat with herbs instead. The Red Dead Wiki gives him a hunting knife as his weapon.",
        "Pearson tient la cuisine du camp : il prépare chaque jour le ragoût à son chariot-cantine et découpe le gibier qu'on lui rapporte. Arthur peut lui remettre des carcasses et d'autres vivres, qui alimentent les réserves du camp. Quand les stocks baissent, il réclame de la viande. À partir de \"Our Best Selves\", Pearson n'étant plus là, le ragoût du camp n'est plus disponible ; la page du Red Dead Wiki consacrée à la mission conseille de se rabattre sur la viande de gros gibier aux herbes. Le Red Dead Wiki lui attribue pour arme un couteau de chasse.")},
    {"h4": two("Satchels", "Sacoches")},
    {"p": two(
        "From chapter 2 to chapter 4, and again in chapter 6, Pearson crafts satchels for Arthur and decorations for the camp from pelts and other animal parts. All satchels and four of the decorations require the Leather Working Tools, bought from the camp ledger for $225 ($180 with the high honor discount, according to the Red Dead Wiki). The ledger itself opens once Arthur has collected a debt for \"Money Lending and Other Sins I & II\" and put it in the camp box. Each satchel takes a perfect deer pelt and two other perfect pelts; the Legend of the East Satchel is unlocked by crafting all the others. In the epilogue, Pearson is gone, and John can buy the satchels at any fence without supplying pelts.",
        "Du chapitre 2 au chapitre 4, puis au chapitre 6, Pearson fabrique des sacoches pour Arthur et des aménagements pour le camp à partir de peaux et d'autres parties d'animaux. Toutes les sacoches et quatre des aménagements exigent les outils de maroquinerie (Leather Working Tools), achetés dans le registre du camp pour 225 dollars (180 dollars avec la remise accordée à un honneur élevé, selon le Red Dead Wiki). Le registre lui-même s'ouvre quand Arthur a récupéré une dette de \"Money Lending and Other Sins I & II\" et l'a déposée dans la caisse du camp. Chaque sacoche demande une peau de cerf parfaite et deux autres peaux parfaites ; la sacoche Legend of the East se débloque une fois toutes les autres fabriquées. Dans l'épilogue, Pearson n'est plus là, et John peut acheter les sacoches chez n'importe quel receleur sans fournir de peaux.")},
    {"table": {
        "head": [two("Satchel", "Sacoche"), two("Holds more", "Contenance accrue"), two("Perfect pelts", "Peaux parfaites"), two("Unlocked by", "Condition")],
        "rows": [
            ["Tonics Satchel", two("Tonics", "Toniques"), two("Deer, buck, elk", "Cerf, cerf mâle, wapiti"), two("Two medicine wagon upgrades in the ledger", "Deux améliorations du chariot médical dans le registre")],
            ["Ingredients Satchel", two("Cooking and crafting ingredients", "Ingrédients de cuisine et de fabrication"), two("Deer, badger, squirrel", "Cerf, blaireau, écureuil"), two("Five animal carcasses donated to Pearson", "Cinq carcasses d'animaux données à Pearson")],
            ["Kit Satchel", two("Kit items", "Équipement"), two("Deer, elk, panther", "Cerf, wapiti, panthère"), two("None", "Aucune")],
            ["Provisions Satchel", two("Provisions and cooked meals", "Provisions et plats cuisinés"), two("Deer, bison, raccoon", "Cerf, bison, raton laveur"), two("Two provisions wagon upgrades in the ledger", "Deux améliorations du chariot de provisions dans le registre")],
            ["Materials Satchel", two("Crafting materials", "Matériaux de fabrication"), two("Deer, boar, iguana skin", "Cerf, sanglier, peau d'iguane"), two("Three recipes crafted at the scout campfire", "Trois recettes fabriquées au feu de camp")],
            ["Valuables Satchel", two("Valuables to sell", "Objets de valeur à revendre"), two("Deer, beaver, rabbit", "Cerf, castor, lapin"), two("$50 in cash given to the camp box", "50 dollars en liquide versés à la caisse du camp")],
            ["Legend of the East Satchel", two("All item types", "Tous les types d'objets"), two("Deer, cougar, wolf", "Cerf, couguar, loup"), two("All other satchels crafted", "Toutes les autres sacoches fabriquées")],
        ]}},
    {"h4": two("Camp decorations", "Aménagements du camp")},
    {"p": two(
        "The Red Dead Wiki lists 17 decorations Pearson can make. The four that need the Leather Working Tools are the cougar pelt covering for Arthur's chest, the boar skin table top in Arthur's tent, the pronghorn leather table tops and the snake skin banjo head.",
        "Le Red Dead Wiki recense 17 aménagements que Pearson peut réaliser. Les quatre qui exigent les outils de maroquinerie sont la housse en peau de couguar du coffre d'Arthur, le dessus de table en peau de sanglier de sa tente, les plateaux en cuir de pronghorn et la peau de serpent tendue sur le banjo.")},
    {"table": {
        "head": [two("Place", "Emplacement"), two("Decorations (materials)", "Aménagements (matériaux)")],
        "rows": [
            [two("Arthur's tent", "Tente d'Arthur"), two("Alligator skull (alligator skin); bighorn ram skull (ram carcass); chest cover (2 cougar pelts); table top (boar pelt); rug (2 ox hides)", "Crâne d'alligator (peau d'alligator) ; crâne de mouflon (carcasse de mouflon) ; housse de coffre (2 peaux de couguar) ; dessus de table (peau de sanglier) ; tapis (2 peaux de bœuf)")],
            [two("John's tent", "Tente de John"), two("Rug (4 boar pelts)", "Tapis (4 peaux de sanglier)")],
            [two("Camp tables", "Tables du camp"), two("Two table tops (2 pronghorn hides)", "Deux plateaux (2 peaux de pronghorn)")],
            [two("Pearson's wagon", "Chariot de Pearson"), two("Pronghorn skull (pronghorn carcass)", "Crâne de pronghorn (carcasse de pronghorn)")],
            [two("Main campfire", "Feu de camp principal"), two("Moose antlers; wolf skull (wolf carcass); banjo head (2 snake skins); crate cover (beaver, muskrat and fox pelts); log seat cover (2 wolf pelts); lean-to ground cover (cow hide)", "Bois d'élan ; crâne de loup (carcasse de loup) ; peau de banjo (2 peaux de serpent) ; housse de caisse (peaux de castor, de rat musqué et de renard) ; housse du banc en rondin (2 peaux de loup) ; tapis d'appentis (peau de vache)")],
            [two("Scout campfire", "Feu de camp secondaire"), two("Ground covers (2 goat hides); elk antlers; hanging bones (buck antlers)", "Tapis de sol (2 peaux de chèvre) ; bois de wapiti ; os suspendus (bois de cerf)")],
        ]}},
    {"h4": two("Accordion and songs", "Accordéon et chansons")},
    {"p": two(
        "Pearson plays the accordion. The Red Dead Wiki's camp events page lists the songs he plays or sings: \"Home, Dearie, Home\", \"A Yankee Ship\", \"Blow the Man Down\" and \"John Brown (Glory, Glory Hallelujah)\" with Sean MacGuire; \"Ring Dang Doo\" with Sean and Uncle; \"Poor Lonesome Cowboy\" with Karen Jones and, with Uncle as well, \"Otis Miller\", both to Javier's guitar. At the party for Jack's return he joins Uncle halfway through \"The Cowboy\", and on a rainy night at Shady Belle he sings \"The Old Scout's Lament\" alone.",
        "Pearson joue de l'accordéon. La page du Red Dead Wiki consacrée aux événements de camp recense les chansons qu'il joue ou chante : \"Home, Dearie, Home\", \"A Yankee Ship\", \"Blow the Man Down\" et \"John Brown (Glory, Glory Hallelujah)\" avec Sean MacGuire ; \"Ring Dang Doo\" avec Sean et Uncle ; \"Poor Lonesome Cowboy\" avec Karen Jones puis, avec Uncle en plus, \"Otis Miller\", toutes deux sur la guitare de Javier. À la fête du retour de Jack, il rejoint Uncle au milieu de \"The Cowboy\", et un soir de pluie, à Shady Belle, il chante seul \"The Old Scout's Lament\".")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "susan-grimshaw.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": [
        two(
            "Susan and Pearson set up each new camp together. According to the Red Dead Wiki, when Lenny and Mary-Beth make fun of his cooking, Susan tells them to mind their manners, since Pearson takes good care of them.",
            "Susan et Pearson installent ensemble chaque nouveau camp. D'après le Red Dead Wiki, quand Lenny et Mary-Beth se moquent de sa cuisine, Susan les rappelle aux bonnes manières, Pearson prenant bien soin d'eux."),
        two(
            "At Shady Belle, Susan finds him in the gazebo listing what he saw at sea and complaining about living in a swamp (see In his own words). She says she never took him for the self-pitying sort; he blames the mud, then insists he is fine and goes back to work.",
            "À Shady Belle, Susan le trouve sous le kiosque, énumérant tout ce qu'il a vu en mer et se plaignant de vivre dans un marais (voir Dans ses propres mots). Elle lui dit qu'elle ne l'aurait jamais cru du genre à s'apitoyer sur son sort ; il met cela sur le compte de la boue, puis assure que tout va bien et retourne au travail."),
    ]},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "Pearson relies on Arthur for meat from the first hunt at Colter (see Biography) onward. Arthur teases him and avoids his Navy stories. At Horseshoe Overlook, Pearson tells Arthur how much the world around him excites him and admits he is sometimes glad to be out of the Navy; when Arthur jokes that joining a gang must have been quite a change, Pearson turns serious, says he saw terrible things, and walks off.",
            "Pearson compte sur Arthur pour la viande dès la première chasse à Colter (voir la biographie). Arthur le taquine et esquive ses histoires de marine. À Horseshoe Overlook, Pearson lui confie son émerveillement devant le monde qui l'entoure et avoue être parfois content d'avoir quitté la marine ; quand Arthur plaisante sur le changement que représente l'entrée dans un gang, Pearson redevient sérieux, dit avoir vu des choses terribles et s'éloigne."),
        two(
            "Pearson apologizes to Arthur after the failed parley and takes him crayfishing at Shady Belle (see Biography); he also asks him for items (see Missions).",
            "Pearson présente ses excuses à Arthur après la trêve manquée et l'emmène pêcher l'écrevisse à Shady Belle (voir la biographie) ; il lui passe aussi des commandes (voir Missions)."),
    ]},
    {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
        "Uncle spends much of his time in Pearson's kitchen and at his campfire. At Horseshoe Overlook, Pearson, nearly shouting, insists that things could be worse and recalls a crew stranded at sea and dying; Uncle answers that he would gladly trade, and describes being orphaned at nine in a strange city. Pearson calms down and grants that every life is hard in its own way. Another night, a sea story from Pearson leads to Uncle's tale of getting lost in the Congo. At Clemens Point, Uncle asks whether he misses the sea; Pearson says he does but is too old to go back, and Uncle tells how he once nearly sailed to Brazil with a captain's wife but missed the boat drunk. According to the Red Dead Wiki, when Uncle insults his cooking, Pearson calls him a repulsive little maggot.",
        "Uncle passe une bonne partie de son temps dans la cuisine de Pearson et autour de son feu. À Horseshoe Overlook, Pearson, presque en criant, soutient que leur sort pourrait être pire et évoque un équipage bloqué en mer, à l'agonie ; Uncle répond qu'il échangerait volontiers et raconte s'être retrouvé orphelin à neuf ans, dans une ville inconnue. Pearson se calme et admet que chaque vie est dure à sa façon. Un autre soir, une histoire de marin de Pearson inspire à Uncle celle de la fois où il s'est perdu au Congo. À Clemens Point, Uncle lui demande si la mer lui manque ; Pearson répond que oui, mais qu'il est trop vieux pour y retourner, et Uncle raconte qu'il a failli partir pour le Brésil avec la femme d'un capitaine, mais qu'il a raté le bateau parce qu'il était ivre. D'après le Red Dead Wiki, quand Uncle critique sa cuisine, Pearson le traite de petit asticot répugnant.")},
    {"img": "sean-macguire.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
        "Sean is Pearson's usual singing partner, with Pearson on the accordion (see Skills). When Sean walks past the stew pot at Horseshoe Overlook, Pearson tells him to get some food. At Clemens Point, the white rabbit Sean and Jack find near camp ends up in Pearson's pot.",
        "Sean est le partenaire de chant habituel de Pearson, qui l'accompagne à l'accordéon (voir Compétences). Quand Sean passe devant la marmite à Horseshoe Overlook, Pearson lui ordonne de venir manger. À Clemens Point, le lapin blanc que Sean et Jack trouvent près du camp finit dans la marmite de Pearson.")},
    {"img": "sadie-adler.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
        "After her rescue, Sadie helps Pearson with the cooking at Horseshoe Overlook, without enthusiasm. At Clemens Point she refuses to spend her days chopping vegetables, and their argument leads Arthur to take her to Rhodes with Pearson's letter to his aunt (see Biography). According to the Red Dead Wiki, during one of their quarrels Pearson raises his cleaver and tells her to watch her mouth.",
        "Après son sauvetage, Sadie aide Pearson en cuisine à Horseshoe Overlook, sans entrain. À Clemens Point, elle refuse de passer ses journées à couper des légumes, et leur dispute pousse Arthur à l'emmener à Rhodes avec la lettre de Pearson pour sa tante (voir la biographie). D'après le Red Dead Wiki, lors d'une de leurs querelles, Pearson brandit son couperet et lui ordonne de surveiller son langage.")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "According to the Red Dead Wiki, Pearson and Hosea get on well and often joke together. Pearson is among those Hosea offers a drink at Clemens Point after a big win at cards. At Shady Belle, Hosea asks him whether he is ready for Tahiti; Pearson says he has never been there but has seen Bali and Java, including a man no bigger than a coconut who spoke seven languages. Hosea tells him that Abigail played her part in town so well that she is the best actress he has ever seen. Asked whether the bank job will work, Hosea tells him to get ready to leave, and Pearson says he is relieved, since the swamp is not for him.",
        "D'après le Red Dead Wiki, Pearson et Hosea s'entendent bien et plaisantent souvent ensemble. Pearson fait partie de ceux à qui Hosea offre à boire à Clemens Point après un gros gain aux cartes. À Shady Belle, Hosea lui demande s'il est prêt pour Tahiti ; Pearson répond qu'il n'y est jamais allé, mais qu'il a vu Bali et Java, dont un homme pas plus grand qu'une noix de coco qui parlait sept langues. Hosea lui raconte qu'Abigail a si bien joué son rôle en ville qu'il n'a jamais vu meilleure actrice. Quand Pearson demande si le coup de la banque va marcher, Hosea lui dit de se préparer au départ, et Pearson se dit soulagé, le marais n'étant pas fait pour lui.")},
    {"img": "charles-smith.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
        "At Colter, Pearson's worry about food sends Charles and Arthur on their first hunt (see Biography). In \"Old Friends\", Dutch leaves Pearson, Charles and Hosea to watch the camp.",
        "À Colter, l'inquiétude de Pearson pour les vivres envoie Charles et Arthur à leur première chasse (voir la biographie). Dans \"Old Friends\", Dutch confie la garde du camp à Pearson, Charles et Hosea.")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "At Horseshoe Overlook, Bill brings fish to the kitchen and loudly demands gratitude; Pearson answers that he has already thanked him and asks whether he is hard of hearing. Drinking together at Shady Belle, Bill tells him his whole problem is that he is a drunk; Pearson shoves him and calls him all talk, and Bill knocks him down with a punch. The scene can play again at the party for Jack's return.",
        "À Horseshoe Overlook, Bill apporte du poisson en cuisine et réclame bruyamment des remerciements ; Pearson lui répond qu'il l'a déjà remercié et lui demande s'il est dur d'oreille. Un soir où ils boivent ensemble à Shady Belle, Bill lui lance que tout son problème, c'est qu'il est ivrogne ; Pearson le bouscule et le traite de grande gueule, et Bill l'envoie au sol d'un coup de poing. La scène peut se rejouer à la fête du retour de Jack.")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "Micah calls Pearson \"fat man\" (see Names) and pushes him to tell Dutch about the O'Driscolls' offer of a parley in \"Blessed are the Peacemakers\" (see Biography). At Clemens Point, after a score, Micah throws money at Pearson and orders him to go buy food; Pearson timidly walks off while Micah laughs. In another version of the scene, Micah hands him the money and puts the rest in the camp box.",
        "Micah traite Pearson de \"fat man\" (voir Noms) et le pousse à parler à Dutch de l'offre de trêve des O'Driscoll dans \"Blessed are the Peacemakers\" (voir la biographie). À Clemens Point, après un coup, Micah lui jette de l'argent à la figure et lui ordonne d'aller acheter à manger ; Pearson s'éloigne timidement sous les rires de Micah. Dans une autre version de la scène, Micah lui tend l'argent et met le reste dans la caisse du camp.")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Dutch took Pearson into the gang when men were shaking him down for money (see Personality). In \"Blessed are the Peacemakers\", Pearson brings him the O'Driscolls' offer of a parley and is told to stay behind; Dutch later calls him a coward for running off (see Biography).",
        "Dutch a recueilli Pearson dans la bande à l'époque où des hommes le rackettaient (voir Personnalité). Dans \"Blessed are the Peacemakers\", Pearson lui transmet l'offre de trêve des O'Driscoll et reçoit l'ordre de rester au camp ; Dutch le traitera plus tard de lâche pour avoir filé (voir la biographie).")},
    {"img": "karen-jones.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": two(
        "Karen sings with Pearson at the poker table (see Skills). At Horseshoe Overlook she tells Susan that, back at Colter, she had thought of eating her, and that she and Pearson could not agree on the best dish.",
        "Karen chante avec Pearson à la table de poker (voir Compétences). À Horseshoe Overlook, elle raconte à Susan qu'à Colter elle avait songé à la manger, et que Pearson et elle n'étaient pas d'accord sur la meilleure recette.")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "At the Horseshoe Overlook stew pot, Pearson and Javier compare mud with snow. Pearson passes on a tip about a woman and some outlaws at Watson's Cabin who keep money hidden there; Javier says he will let him know if he finds anything, and Pearson makes the same offer to Arthur if he is nearby. Javier plays the guitar for several of Pearson's songs (see Skills).",
        "Près de la marmite de Horseshoe Overlook, Pearson et Javier comparent la boue et la neige. Pearson lui refile un tuyau : une femme et quelques hors-la-loi de Watson's Cabin y cacheraient de l'argent ; Javier promet de le tenir au courant s'il trouve quelque chose, et Pearson fait la même proposition à Arthur s'il passe par là. Javier accompagne à la guitare plusieurs des chansons de Pearson (voir Compétences).")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "While Jack is missing at Shady Belle, Abigail finds Pearson smoking on the dock and asks where her son is; Pearson says Jack is a smart kid who always turns up. If Arthur mentions the boy's disappearance, Pearson asks whether anyone could blame him for running off, and Arthur agrees. At Lakay, Pearson and Abigail welcome Arthur back from Guarma (see Biography).",
        "Pendant la disparition de Jack, à Shady Belle, Abigail trouve Pearson en train de fumer sur le ponton et lui demande où est son fils ; Pearson répond que Jack est un garçon malin, qui finit toujours par revenir. Si Arthur évoque la disparition de l'enfant, Pearson lui demande qui pourrait lui reprocher d'avoir filé, et Arthur en convient. À Lakay, Pearson et Abigail accueillent Arthur à son retour de Guarma (voir la biographie).")},
    {"img": "mary-beth-gaskill.jpeg", "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill", "text": two(
        "According to the Red Dead Wiki, Mary-Beth and Lenny mock Pearson's cooking until Susan steps in (see Susan Grimshaw). At Shady Belle she asks Pearson where Kieran is (see Kieran Duffy).",
        "D'après le Red Dead Wiki, Mary-Beth et Lenny se moquent de la cuisine de Pearson jusqu'à ce que Susan intervienne (voir Susan Grimshaw). À Shady Belle, elle demande à Pearson où est passé Kieran (voir Kieran Duffy).")},
    {"img": "lenny-summers.jpeg", "slug": "lenny-summers", "name": "Lenny Summers", "text": two(
        "When Pearson tells Arthur at Colter that Lenny found nothing to hunt (see Biography), Arthur answers that Lenny is more into reading books than hunting. Lenny also mocks Pearson's cooking (see Susan Grimshaw).",
        "Quand Pearson raconte à Arthur, à Colter, que Lenny n'a rien trouvé à chasser (voir la biographie), Arthur répond que Lenny préfère les livres à la chasse. Lenny se moque aussi de la cuisine de Pearson (voir Susan Grimshaw).")},
    {"img": "kieran-duffy.jpeg", "slug": "kieran-duffy", "name": "Kieran Duffy", "text": two(
        "When Kieran goes missing after the party for Jack's return, Mary-Beth asks Pearson where he is. Pearson does not know and tries to change the subject with the story of a shark he once saw eat several men. After the O'Driscoll attack on Shady Belle, Pearson is one of the three men who bury Kieran (see Biography).",
        "Quand Kieran disparaît après la fête du retour de Jack, Mary-Beth demande à Pearson où il se trouve. Pearson n'en sait rien et tente de détourner la conversation avec l'histoire d'un requin qu'il a vu dévorer plusieurs hommes. Après l'attaque des O'Driscoll contre Shady Belle, Pearson fait partie des trois hommes qui enterrent Kieran (voir la biographie).")},
    {"img": "leopold-strauss.jpeg", "slug": "leopold-strauss", "name": "Leopold Strauss", "text": two(
        "At Beaver Hollow, Pearson and Susan sleep next to Strauss and are woken if Arthur throws him out at night (see Biography). According to the Red Dead Wiki, Pearson and Abigail afterward tell Arthur they are disappointed that he did not consult the others.",
        "À Beaver Hollow, Pearson et Susan dorment à côté de Strauss, et se réveillent si Arthur le chasse en pleine nuit (voir la biographie). D'après le Red Dead Wiki, Pearson et Abigail reprochent ensuite à Arthur de ne pas avoir consulté les autres.")},
    {"img": "molly-oshea.jpeg", "slug": "molly-oshea", "name": "Molly O'Shea", "text": two(
        "After Susan shoots Molly at the end of \"That's Murfree Country\", Pearson and Bill are ordered to burn her body (see Biography).",
        "Après que Susan a abattu Molly, à la fin de \"That's Murfree Country\", Pearson et Bill reçoivent l'ordre de brûler son corps (voir la biographie).")},
    {"img": "orville-swanson.jpeg", "slug": "orville-swanson", "name": "Orville Swanson", "text": two(
        "In \"Who is Not Without Sin\", Pearson has a remark for the drunk Swanson as Arthur carries him through camp (see Biography). The Red Dead Wiki groups the two men together among the members never shown taking part in a crime (see Personality).",
        "Dans \"Who is Not Without Sin\", Pearson lâche un commentaire au passage de Swanson, ivre, qu'Arthur porte à travers le camp (voir la biographie). Le Red Dead Wiki range les deux hommes parmi les membres de la bande qu'on ne voit jamais prendre part à un crime (voir Personnalité).")},
    {"img": "tilly-jackson.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
        "In her 1907 letter to John and Abigail, Tilly lists Pearson among the people from the gang she misses (see Names).",
        "Dans sa lettre de 1907 à John et Abigail, Tilly cite Pearson parmi les membres de la bande qui lui manquent (voir Noms).")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "In 1907 John can visit Pearson several times at the Rhodes general store and give him news of his new life (see Biography).",
        "En 1907, John peut rendre visite à Pearson à plusieurs reprises au magasin général de Rhodes et lui donner des nouvelles de sa nouvelle vie (voir la biographie).")},
    {"img": None, "slug": None, "name": "Ethel Pearson", "text": two(
        "Ethel is Pearson's wife in 1907. She is never seen, but she can be heard when John talks to Pearson in the Rhodes general store; according to the Red Dead Wiki, she lives upstairs. The wiki calls her his second wife and says Pearson admits she has a mean streak but loves her. The wiki's infobox lists an ex-wife named Michele, a name it does not tie to any scene in the game.",
        "Ethel est l'épouse de Pearson en 1907. On ne la voit jamais, mais on l'entend quand John parle à Pearson dans le magasin général de Rhodes ; d'après le Red Dead Wiki, elle occupe l'étage. Le wiki en fait sa seconde épouse et indique que Pearson lui reconnaît mauvais caractère, mais assure l'aimer. L'encadré du wiki mentionne une ex-épouse prénommée Michele, sans rattacher ce nom à la moindre scène du jeu.")},
    {"img": None, "slug": None, "name": "Aunt Cathy", "text": two(
        "Cathy is Pearson's aunt. In \"Further Questions of Female Suffrage\", he gives Arthur a letter to post to her, which Sadie reads aloud on the way to Rhodes (see Biography).",
        "Cathy est la tante de Pearson. Dans \"Further Questions of Female Suffrage\", il confie à Arthur une lettre à lui poster, que Sadie lit à voix haute sur la route de Rhodes (voir la biographie).")},
]
