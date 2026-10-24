"""Outlaws from the West (RDR2, Chapter 1, mission 1), pilot mission page (24 Oct 2026).

Source register:
- Our v3 Chapter 1 guide, EN story/rdr2-chapter-1-colter/ and FR
  fr/histoire/rdr2-chapitre-1-colter/ (fixed 24 Oct 2026 after two adversarial
  fact-checks and a coverage check): section "1. Outlaws from the West", the
  matching row of "Chapter 1 at a glance" (giver, companions, location, Gold
  Medal objectives), "Background: the Blackwater ferry robbery" (Dutch's speech,
  the ride questions), "Camp life at Colter" (horse offered back to Sadie),
  "Trivia" (Davey's grave, Hosea's line in "A Fork in the Road", map/lantern/
  compendium, Taima) and the in-game opening text. Story wording and facts are
  taken from it; the FR text is taken from the FR guide.
- Red Dead Wiki mission page "Outlaws from the West" (scripts/v3/work/_m/
  Outlaws_from_the_West.txt): infobox (start/end Colter, giver Dutch, location
  Adler Ranch, Grizzlies West, Ambarino, reward Mahogany Bay Tennessee Walker,
  next mission), Gold Medal objectives, deaths list, mission failure conditions,
  trivia (map markers during the intro, invisible wall after the barn, the
  O'Driscolls' horses, Dutch's remark on wrong cover, Micah shooting if Arthur
  does not), trophies (Gold Rush, Best in the West).
- Red Dead Wiki transcript "Outlaws from the West/dialogues" (scripts/v3/work/
  _m/Outlaws_from_the_West_dialogues.txt): every quoted line was checked against
  it, and both ride dialogue options (the "trap" answer also says the money was
  stashed in town).

Left out: the wiki's "Reservoir Dogs" comparison (speculation), the "prophetic"
link with "American Venom" (interpretation), Javier's absence from Colter "it is
implied" (speculation), the claim that Dutch's speech is repeated at Horseshoe
Overlook (contradicted by the Eastward Bound transcript, see the guide), the
Standard Horse / The Count "oversight" note, glitches, mods findings, music
titles, Gold Medal tips, the Micah "be a good boy" line (not found in that
context in the transcript), the Red Dead Online "oversight" about the horse.
"""


def two(en, fr): return {"en": en, "fr": fr}


MISSION = {
    "slug": "outlaws-from-the-west",
    "name": "Outlaws from the West",
    "game": "rdr2",
    "chapter": 1,
    "number": 1,
    "chapter_total": 6,
    "story_order": 1,
    "publishDate": "2026-10-24",
    "updated": "2026-10-24",
    "prev": None,
    "next": {"slug": "enter-pursued-by-a-memory", "name": "Enter, Pursued by a Memory"},

    "meta_desc": two(
        "Outlaws from the West, the first mission of Red Dead Redemption 2: the arrival at Colter, the O'Driscoll shootout at the Adler Ranch, Sadie Adler, choices, Gold Medal objectives and quotes.",
        "Outlaws from the West, première mission de Red Dead Redemption 2 : l'arrivée à Colter, la fusillade contre les O'Driscoll à l'Adler Ranch, Sadie Adler, choix, médaille d'or et citations."),
    "og_desc": two(
        "The first mission of Red Dead Redemption 2, step by step: Colter, the Adler Ranch, the O'Driscolls and Sadie Adler.",
        "La première mission de Red Dead Redemption 2, étape par étape : Colter, l'Adler Ranch, les O'Driscoll et Sadie Adler."),

    "hero": {
        "src": "assets/story/rdr2-chapter-1-colter/scene-1.jpeg",
        "alt": two("Three riders crossing deep snow at night, one carrying a lantern",
                   "Trois cavaliers dans la neige profonde, de nuit, dont l'un porte une lanterne"),
        "cap": two("Dutch, Arthur and Micah ride through the snowstorm toward the Adler Ranch.",
                   "Dutch, Arthur et Micah chevauchent dans la tempête vers l'Adler Ranch."),
    },

    "facts": {
        "giver": two("[[dutch-van-der-linde|Dutch van der Linde]]", "[[dutch-van-der-linde|Dutch van der Linde]]"),
        "location": two("Starts and ends at Colter; Adler Ranch, Grizzlies West, Ambarino",
                        "Départ et retour à Colter ; Adler Ranch, Grizzlies West, Ambarino"),
        "characters": two(
            "[[arthur-morgan|Arthur Morgan]], [[dutch-van-der-linde|Dutch van der Linde]], [[micah-bell|Micah Bell]], [[sadie-adler|Sadie Adler]]; at camp, [[hosea-matthews|Hosea Matthews]], [[charles-smith|Charles Smith]], [[susan-grimshaw|Susan Grimshaw]] and the rest of the gang",
            "[[arthur-morgan|Arthur Morgan]], [[dutch-van-der-linde|Dutch van der Linde]], [[micah-bell|Micah Bell]], [[sadie-adler|Sadie Adler]] ; au camp, [[hosea-matthews|Hosea Matthews]], [[charles-smith|Charles Smith]], [[susan-grimshaw|Susan Grimshaw]] et le reste de la bande"),
        "unlocks": two("[[m:enter-pursued-by-a-memory|Enter, Pursued by a Memory]], which starts directly after this mission",
                       "[[m:enter-pursued-by-a-memory|Enter, Pursued by a Memory]], qui s'enchaîne directement"),
        "rewards": two("Mahogany Bay Tennessee Walker (the horse from the barn)",
                       "Tennessee Walker bai acajou (Mahogany Bay), le cheval de la grange"),
    },

    "intro": [
        two("\"Outlaws from the West\" is the first story mission of Red Dead Redemption 2 and the first of the six missions of <a href=\"/story/rdr2-chapter-1-colter/\">Chapter 1: Colter</a>. It is given by [[dutch-van-der-linde|Dutch van der Linde]], starts and ends at Colter, and takes [[arthur-morgan|Arthur Morgan]] to the Adler Ranch, in the Grizzlies West of Ambarino.",
            "\"Outlaws from the West\" est la première mission principale de Red Dead Redemption 2 et la première des six missions du <a href=\"/fr/histoire/rdr2-chapitre-1-colter/\">chapitre 1 : Colter</a>. Donnée par [[dutch-van-der-linde|Dutch van der Linde]], elle part de Colter, y revient et mène [[arthur-morgan|Arthur Morgan]] à l'Adler Ranch, dans les Grizzlies West, en Ambarino."),
        two("After the failed Blackwater ferry robbery, the gang shelters in the abandoned mining town of Colter. Dutch, Arthur and [[micah-bell|Micah Bell]] kill a band of O'Driscolls at a homestead and bring back the widow [[sadie-adler|Sadie Adler]].",
            "Après l'échec du braquage du ferry de Blackwater, la bande se réfugie dans la ville minière abandonnée de Colter. Dutch, Arthur et [[micah-bell|Micah Bell]] abattent une bande d'O'Driscoll dans une ferme et ramènent [[sadie-adler|Sadie Adler]], devenue veuve."),
    ],

    "sections": {
        "story": [
            {"h3": two("Before the mission: Blackwater", "Avant la mission : Blackwater")},
            {"p": two("The game opens on white text over a black screen: \"By 1899, the age of outlaws and gunslingers was at an end. America was becoming a land of laws... Even the west had mostly been tamed. A few gangs still roamed but they were being hunted down and destroyed.\"",
                      "Le jeu s'ouvre sur un texte blanc sur fond noir : \"By 1899, the age of outlaws and gunslingers was at an end. America was becoming a land of laws... Even the west had mostly been tamed. A few gangs still roamed but they were being hunted down and destroyed.\" (En 1899, l'ère des hors-la-loi et des as de la gâchette touche à sa fin. L'Amérique devient une terre de lois, et même l'Ouest est en grande partie dompté. Quelques bandes sévissent encore, mais elles sont traquées et anéanties.)")},
            {"p": two("The mission follows a failed ferry robbery in Blackwater, which the Red Dead Wiki dates to April 1899. The robbery itself is never shown. The gang has fled into the Grizzlies, where a late spring storm has caught it.",
                      "La mission fait suite à l'échec d'un braquage de ferry à Blackwater, que le Red Dead Wiki date d'avril 1899. Le braquage n'est jamais montré. La bande a fui dans les Grizzlies, où la surprend une tempête de fin de printemps.")},

            {"h3": two("The storm and Colter", "La tempête et Colter")},
            {"p": two("At night, the gang's wagons push through a snowstorm in the Grizzlies. Reverend [[orville-swanson|Orville Swanson]] tells Dutch that Abigail says Davey is dying and that they must stop. [[hosea-matthews|Hosea]] adds: \"If we don't stop soon, we'll all be dying. This weather, it's May...\" Arthur, sent ahead by Dutch, rides back and reports an abandoned mining town nearby. He leads the wagons there. The title card \"Chapter I: Colter\" follows.",
                      "De nuit, les chariots de la bande avancent dans une tempête de neige, au cœur des Grizzlies. Le révérend [[orville-swanson|Orville Swanson]] prévient Dutch qu'Abigail juge Davey mourant et qu'il faut s'arrêter. [[hosea-matthews|Hosea]] renchérit : \"If we don't stop soon, we'll all be dying. This weather, it's May...\" (Si on ne s'arrête pas bientôt, on va tous y rester. Ce temps-là, en mai...) Arthur, que Dutch avait envoyé en éclaireur, revient annoncer une ville minière abandonnée à proximité et y conduit le convoi. Le titre \"Chapter I: Colter\" s'affiche alors.")},
            {"p": two("Hosea opens the first cabin, revolver drawn. [[abigail-marston|Abigail]] walks in first, followed by [[bill-williamson|Bill Williamson]] and Arthur, who carry Davey Callander on a stretcher. [[susan-grimshaw|Susan Grimshaw]] sends Mary-Beth to light the fire, Karen to fetch blankets and Pearson to check the food. Abigail says: \"Davey's dead.\" Swanson tells her there was nothing more she could have done, and Hosea asks how they will get supplies. Dutch announces that he sent John and Micah ahead to scout and that he and Arthur will ride out to find one of them.",
                      "Hosea ouvre la première cabane, revolver à la main. [[abigail-marston|Abigail]] entre la première, suivie de [[bill-williamson|Bill Williamson]] et d'Arthur, qui portent Davey Callander sur une civière. [[susan-grimshaw|Susan Grimshaw]] charge Mary-Beth d'allumer le feu, Karen d'apporter les couvertures et Pearson de faire l'inventaire des vivres. Abigail lâche : \"Davey's dead.\" (Davey est mort.) Swanson lui assure qu'elle ne pouvait rien faire de plus, et Hosea demande comment ils vont se ravitailler. Dutch annonce qu'il a envoyé John et Micah en reconnaissance, et qu'il part avec Arthur retrouver l'un des deux.")},
            {"p": two("Dutch then addresses the gang. He names the people they have lost or cannot account for: Davey, Jenny Kirk, [[sean-macguire|Sean MacGuire]] and Mac Callander, saying of Sean and Mac: \"they may be okay, we don't know.\" He says: \"There ain't nobody following us through a storm like this one.\" He adds that they may be at Colter for a few days, and asks Pearson and Susan to turn the place into a camp. He ends with: \"Stay strong. Stay with me. We ain't done yet!\"",
                      "Dutch s'adresse ensuite à toute la bande. Il cite ceux qu'ils ont perdus ou dont ils sont sans nouvelles : Davey, Jenny Kirk, [[sean-macguire|Sean MacGuire]] et Mac Callander ; pour Sean et Mac, il précise qu'ils sont peut-être en vie, qu'on n'en sait rien. Personne, assure-t-il, ne les suivra par une tempête pareille, et ils resteront peut-être quelques jours à Colter. Il demande à Pearson et à Susan de transformer l'endroit en camp. Il conclut : \"Stay strong. Stay with me. We ain't done yet!\" (Tenez bon. Restez avec moi. On n'a pas dit notre dernier mot !)")},

            {"h3": two("The ride to the homestead", "La route de la ferme")},
            {"p": two("Outside, Arthur asks what really happened on the boat. Dutch answers: \"We missed you, that's what happened.\" [[charles-smith|Charles Smith]] brings them two horses; Dutch tells him to get indoors and rest his hand. Arthur rides Charles's mare, Taima. On the trail, Arthur says he cannot believe they lost Davey too. Dutch answers: \"He's the last one, Arthur. No more.\" He tells Arthur he is the only one he can rely on to stay strong. The player can then ask about the money or about whether Blackwater was a trap (see Choices and variants).",
                      "Dehors, Arthur demande ce qui s'est vraiment passé sur le bateau. Dutch répond : \"We missed you, that's what happened.\" (Tu nous as manqué, voilà ce qui s'est passé.) [[charles-smith|Charles Smith]] leur amène deux chevaux ; Dutch lui ordonne de rentrer se reposer la main. Arthur monte Taima, la jument de Charles. En route, Arthur n'en revient pas d'avoir aussi perdu Davey. Dutch répond : \"He's the last one, Arthur. No more.\" (C'est le dernier, Arthur. Plus personne.) Il lui confie qu'il est le seul sur qui il peut compter pour rester solide. Le joueur peut alors l'interroger sur l'argent, ou lui demander si Blackwater était un piège (voir Choix et variantes).")},
            {"p": two("They meet Micah Bell, who has found a homestead \"blazing with light and noise\", where it sounds like a party. Dutch tells him that Davey and Jenny did not make it. Micah has not seen John since the storm came in.",
                      "Ils tombent sur Micah Bell, qui a repéré une ferme illuminée et bruyante, où l'on semble faire la fête. Dutch lui apprend que Davey et Jenny n'ont pas survécu. Micah n'a pas vu John depuis le début de la tempête.")},

            {"h3": two("The shootout at the Adler Ranch", "La fusillade de l'Adler Ranch")},
            {"p": two("At the homestead, Dutch sends Micah behind a wagon and Arthur behind a shed. He goes to the door alone: \"One lonely man is a lot less intimidating than three nasty-looking degenerates.\" He poses as a lost traveler and asks for a few cans of food. Micah finds a body under a sheet in the wagon. One of the men recognizes Dutch and shouts: \"It's goddamn Dutch van der Linde, you morons!\" The men are [[colm-odriscoll|Colm O'Driscoll]]'s gang. Arthur or Micah fires first, and the three outlaws kill the O'Driscolls at the house. The mission page names two of the dead, Billy and Declan.",
                      "À la ferme, Dutch envoie Micah derrière un chariot et Arthur derrière une remise. Il se présente seul à la porte : \"One lonely man is a lot less intimidating than three nasty-looking degenerates.\" (Un homme seul fait bien moins peur que trois dégénérés à la mine patibulaire.) Il se fait passer pour un voyageur égaré et demande quelques conserves. Micah découvre un cadavre sous une bâche, dans le chariot. L'un des hommes reconnaît Dutch et s'écrie : \"It's goddamn Dutch van der Linde, you morons!\" (C'est ce foutu Dutch van der Linde, bande d'abrutis !) Ce sont des hommes de [[colm-odriscoll|Colm O'Driscoll]]. Arthur ou Micah tire le premier, et les trois hors-la-loi abattent les O'Driscoll présents. La page de la mission nomme deux des morts, Billy et Declan.")},
            {"p": two("Dutch and Arthur search the cabin for food, medicine and ammunition. Arthur points out a large pool of blood on the floor. Arthur notes that there is a large price on Colm's head; Dutch answers that wanting Colm dead \"is about the only thing me and Uncle Sam agree on.\" Arthur suggests moving the women and Jack to the house, but Dutch does not want the gang to split up.",
                      "Dutch et Arthur fouillent la maison à la recherche de nourriture, de remèdes et de munitions. Arthur signale une grande flaque de sang sur le plancher. Arthur rappelle que la tête de Colm est mise à prix ; Dutch répond que vouloir Colm mort est à peu près le seul point sur lequel il s'entend avec l'Oncle Sam. Arthur propose d'installer les femmes et Jack dans la maison, mais Dutch ne veut pas diviser la bande.")},

            {"h3": two("The barn", "La grange")},
            {"p": two("In the barn, an O'Driscoll who hid during the shootout jumps Arthur from the loft, shouting: \"You bastards shot my cousin!\" Arthur beats him while Dutch watches. Under questioning, the man says the others are at an old mining camp southwest of the ranch, near a lake, and that they plan to rob a train and blow the tracks. Dutch leaves his fate to Arthur (see Choices and variants). Arthur then calms a Tennessee Walker in the barn, and Dutch tells him to keep it.",
                      "Dans la grange, un O'Driscoll caché pendant la fusillade saute sur Arthur depuis le grenier en criant : \"You bastards shot my cousin!\" (Salauds, vous avez descendu mon cousin !) Arthur le roue de coups sous le regard de Dutch. Interrogé, l'homme révèle que les autres sont dans un ancien camp minier au sud-ouest, près d'un lac, et qu'ils préparent l'attaque d'un train en faisant sauter les rails. Dutch laisse Arthur décider de son sort (voir Choix et variantes). Arthur calme ensuite un Tennessee Walker resté dans la grange, et Dutch lui dit de le garder.")},

            {"h3": two("Sadie Adler", "Sadie Adler")},
            {"p": two("A woman screams inside the house. Micah has found her hiding in the cellar and insists she is one of the O'Driscolls. She throws a bottle at him, then holds him off with a knife from the table. Dutch tells Micah: \"No, she ain't, Micah. Look at her.\" Micah flips the table, a lantern falls and the house catches fire. Dutch and Arthur push Micah away, and Dutch calms the woman and leads everyone outside. She says the men came three days earlier and killed her husband. Arthur helps her onto Dutch's horse and tells her: \"We're bad men, but... we ain't them.\" On the ride back she gives her name: Sadie Adler. The house burns with her husband Jake's body still in the wagon.",
                      "Un cri de femme retentit dans la maison. Micah l'a trouvée cachée dans la cave et soutient qu'elle fait partie des O'Driscoll. Elle lui lance une bouteille, puis le tient à distance avec un couteau pris sur la table. Dutch reprend Micah : \"No, she ain't, Micah. Look at her.\" (Mais non, Micah. Regarde-la.) Micah renverse la table, une lanterne tombe et la maison prend feu. Dutch et Arthur repoussent Micah, puis Dutch calme la femme et fait sortir tout le monde. Elle explique que les hommes sont arrivés trois jours plus tôt et ont tué son mari. Arthur l'aide à monter sur le cheval de Dutch et la rassure : \"We're bad men, but... we ain't them.\" (On n'est pas des enfants de chœur, mais on n'est pas comme eux.) Sur le chemin du retour, elle dit son nom : Sadie Adler. La maison brûle, le corps de son mari, Jake, toujours dans le chariot.")},

            {"h3": two("Back at Colter", "Retour à Colter")},
            {"p": two("At Colter, [[lenny-summers|Lenny Summers]] is on watch and calls the others out. Dutch tells Hosea that O'Driscolls are in the area, scouting a train; Hosea answers: \"That's the last thing we need right now, Dutch.\" Dutch asks [[tilly-jackson|Tilly]] and [[karen-jones|Karen]] to look after Sadie. He tells Abigail: \"They turned her into a widow... animals.\" He says he has not slept in three days. Susan hands out the rooms. Micah protests that Arthur gets a room to himself while he shares a bunk room with Bill and others, using a racial slur, and Hosea sends him to bed. The mission continues directly into [[m:enter-pursued-by-a-memory|Enter, Pursued by a Memory]].",
                      "À Colter, [[lenny-summers|Lenny Summers]], de garde, appelle les autres. Dutch annonce à Hosea que des O'Driscoll rôdent dans le secteur et repèrent un train ; Hosea soupire que c'est bien la dernière chose dont ils avaient besoin. Dutch confie Sadie à [[tilly-jackson|Tilly]] et à [[karen-jones|Karen]]. Il glisse à Abigail : \"They turned her into a widow... animals.\" (Ils en ont fait une veuve... des bêtes.) Il avoue n'avoir pas dormi depuis trois jours. Susan répartit les chambres. Micah proteste d'avoir un lit superposé à côté de Bill et d'autres alors qu'Arthur a une chambre à lui, avec une insulte raciste, et Hosea l'envoie se coucher. La mission enchaîne directement sur [[m:enter-pursued-by-a-memory|Enter, Pursued by a Memory]].")},

            {"h3": two("Deaths", "Morts")},
            {"ul": [
                two("Davey Callander: carried into Colter already dead, from wounds suffered at Blackwater.",
                    "Davey Callander : il arrive mort à Colter, des suites de ses blessures de Blackwater."),
                two("Jenny Kirk: already dead when the mission begins; Dutch tells Micah she did not make it.",
                    "Jenny Kirk : déjà morte au début de la mission ; Dutch apprend à Micah qu'elle n'a pas survécu."),
                two("Jake Adler: killed by the O'Driscolls three days before the gang reaches the ranch.",
                    "Jake Adler : tué par les O'Driscoll trois jours avant l'arrivée de la bande au ranch."),
                two("The O'Driscolls at the house, two of them named Billy and Declan by the mission page, killed by Arthur, Dutch or Micah; the O'Driscoll in the barn only if Arthur kills him.",
                    "Les O'Driscoll de la maison, dont deux que la page de la mission nomme Billy et Declan, tués par Arthur, Dutch ou Micah ; l'O'Driscoll de la grange seulement si Arthur le tue."),
            ]},
        ],

        "choices": [
            {"h3": two("On the ride: the money or Blackwater", "En route : l'argent ou Blackwater")},
            {"p": two("On the ride to the Adler Ranch, the player picks one of two questions.",
                      "Sur la route de l'Adler Ranch, le joueur choisit l'une de deux questions.")},
            {"ul": [
                two("\"What about the money?\": Dutch says the money is \"stashed with the rest of the money in town\" and that the gang cannot go back for it any time soon.",
                    "\"What about the money?\" (Et l'argent ?) : Dutch explique qu'il a caché l'argent avec le reste de leurs économies en ville et que la bande ne pourra pas aller le chercher de sitôt."),
                two("\"Was it a trap?\": Dutch answers about the Pinkertons, \"That many men? Oh, they knew we were coming\", and adds that there was money on the boat, which he stashed in town before they fled.",
                    "\"Was it a trap?\" (C'était un piège ?) : à propos des Pinkerton, Dutch répond \"That many men? Oh, they knew we were coming\" (Autant d'hommes ? Ils savaient qu'on venait, crois-moi), puis ajoute qu'il y avait bien de l'argent sur le bateau et qu'il l'a caché en ville avant leur fuite."),
            ]},
            {"p": two("In one of two optional exchanges with Arthur on the same ride, Micah says the gang has \"too many mouths to feed.\"",
                      "Dans l'un des deux échanges facultatifs avec Arthur sur la même route, Micah se plaint qu'il y a \"too many mouths to feed\" (trop de bouches à nourrir).")},

            {"h3": two("The shootout and the search", "La fusillade et la fouille")},
            {"ul": [
                two("Arthur or Micah fires the first shot. According to the Red Dead Wiki, if Arthur does not shoot to protect Dutch, Micah does it instead, and Dutch comments if Arthur takes cover in the wrong spot.",
                    "Arthur ou Micah tire le premier. Selon le Red Dead Wiki, si Arthur ne tire pas pour protéger Dutch, c'est Micah qui s'en charge, et Dutch fait une remarque si Arthur se met à couvert au mauvais endroit."),
                two("According to the mission page, Arthur can find a wedding photograph of the couple in the house and remark that \"the poor bastard was married too\"; if Dutch is still in the room, he tells Arthur to put down anything they cannot eat or drink.",
                    "D'après la page de la mission, Arthur peut trouver dans la maison une photo de mariage du couple et constater que le pauvre bougre était marié ; si Dutch est encore dans la pièce, il lui dit de reposer tout ce qui ne se mange pas ou ne se boit pas."),
            ]},

            {"h3": two("The O'Driscoll in the barn", "L'O'Driscoll de la grange")},
            {"p": two("After the interrogation, Dutch leaves the man's fate to Arthur, who can kill him, knock him out or let him go. According to the mission page, a spared O'Driscoll reappears in [[m:old-friends|Old Friends]], shouting \"You should've killed me when you had the chance!\", and is killed there.",
                      "Après l'interrogatoire, Dutch laisse Arthur décider du sort de l'homme : le tuer, l'assommer ou le laisser filer. D'après la page de la mission, l'O'Driscoll épargné réapparaît dans [[m:old-friends|Old Friends]], où il lance \"You should've killed me when you had the chance!\" (Fallait me tuer quand tu pouvais !) avant d'y être tué.")},

            {"h3": two("The horse from the barn", "Le cheval de la grange")},
            {"p": two("According to the mission page, Arthur can later offer to give the horse from the barn back to Sadie at Colter; she says it belonged to an O'Driscoll.",
                      "D'après la page de la mission, Arthur peut ensuite proposer à Sadie, à Colter, de lui rendre le cheval de la grange ; elle répond qu'il appartenait à un O'Driscoll.")},

            {"h3": two("Mission failure", "Échec de la mission")},
            {"p": two("According to the mission page, the mission fails if the player:",
                      "D'après la page de la mission, la mission échoue si le joueur :")},
            {"ul": [
                two("aggravates, assaults, kills or abandons Dutch or Micah, or lets either of them be killed;",
                    "provoque, agresse, tue ou abandonne Dutch ou Micah, ou laisse l'un des deux se faire tuer ;"),
                two("abandons the homestead;", "abandonne la ferme ;"),
                two("assaults, kills or abandons his own horse or the horse in the barn;",
                    "agresse, tue ou abandonne son propre cheval ou celui de la grange ;"),
                two("dies.", "meurt."),
            ]},
        ],

        "gold": {
            "objectives": [
                two("Take no damage during the shootout.", "Ne subir aucun dégât pendant la fusillade."),
                two("Loot 6 or more items from Adler Ranch.", "Piller au moins 6 objets à l'Adler Ranch."),
                two("Complete with at least 80% accuracy.", "Terminer avec une précision d'au moins 80 %."),
            ],
            "after": [
                {"p": two("According to the same page, the mission counts toward the Gold Rush trophy (70 Gold Medals in story missions) and Best in the West (100% completion).",
                          "Selon la même page, la mission compte pour les trophées Gold Rush (70 médailles d'or dans les missions principales) et Best in the West (100 % de complétion).")},
            ],
        },

        "quotes": [
            {"q": "If we don't stop soon, we'll all be dying. This weather, it's May...",
             "src": two("Hosea, in the opening storm", "Hosea, dans la tempête d'ouverture"),
             "fr": "Si on ne s'arrête pas bientôt, on va tous y rester. Ce temps-là, en mai..."},
            {"q": "Stay strong. Stay with me. We ain't done yet!",
             "src": two("Dutch, ending his speech to the gang at Colter", "Dutch, à la fin de son discours à la bande, à Colter"),
             "fr": "Tenez bon. Restez avec moi. On n'a pas dit notre dernier mot !"},
            {"q": "He's the last one, Arthur. No more.",
             "src": two("Dutch, about Davey, on the trail", "Dutch, à propos de Davey, en chemin"),
             "fr": "C'est le dernier, Arthur. Plus personne."},
            {"q": "One lonely man is a lot less intimidating than three nasty-looking degenerates.",
             "src": two("Dutch, before going to the door of the homestead", "Dutch, avant d'aller frapper à la porte de la ferme"),
             "fr": "Un homme seul fait bien moins peur que trois dégénérés à la mine patibulaire."},
            {"q": "It's goddamn Dutch van der Linde, you morons!",
             "src": two("An O'Driscoll at the Adler Ranch", "Un O'Driscoll, à l'Adler Ranch"),
             "fr": "C'est ce foutu Dutch van der Linde, bande d'abrutis !"},
            {"q": "Wanting Colm dead is about the only thing me and Uncle Sam agree on.",
             "src": two("Dutch, searching the cabin with Arthur", "Dutch, en fouillant la maison avec Arthur"),
             "fr": "Vouloir Colm mort, c'est à peu près la seule chose sur laquelle l'Oncle Sam et moi sommes d'accord."},
            {"q": "We're bad men, but... we ain't them.",
             "src": two("Arthur, to Sadie Adler", "Arthur, à Sadie Adler"),
             "fr": "On n'est pas des enfants de chœur, mais on n'est pas comme eux."},
            {"q": "They turned her into a widow... animals.",
             "src": two("Dutch, to Abigail, back at Colter", "Dutch, à Abigail, de retour à Colter"),
             "fr": "Ils en ont fait une veuve... des bêtes."},
        ],

        "trivia": [
            two("Hosea's line \"If we don't stop soon, we'll all be dying\" is the one Arthur remembers in [[m:a-fork-in-the-road|A Fork in the Road]] with high honor, according to the wiki's mission pages.",
                "La réplique d'Hosea \"If we don't stop soon, we'll all be dying\" est celle dont Arthur se souvient dans [[m:a-fork-in-the-road|A Fork in the Road]] avec un honneur élevé, d'après les pages de missions du wiki."),
            two("Davey Callander's grave is in a small graveyard at Colter and counts toward the \"Paying Respects\" trophy, according to the Red Dead Wiki.",
                "La tombe de Davey Callander, dans un petit cimetière de Colter, compte pour le trophée \"Paying Respects\", selon le Red Dead Wiki."),
            two("The opening scene of the caravan in the storm takes place outside the playable map, northwest of Spider Gorge, according to the mission page.",
                "La scène d'ouverture du convoi dans la tempête se déroule hors de la carte jouable, au nord-ouest de Spider Gorge, selon la page de la mission."),
            two("The map can be opened during the opening cutscene; Micah, Charles and Dutch have markers on it, according to the mission page.",
                "La carte peut être ouverte pendant la cinématique d'ouverture ; Micah, Charles et Dutch y ont chacun un marqueur, selon la page de la mission."),
            two("The Old Lantern exists only in this mission, and the compendium can be opened during it, then stays locked until [[m:the-aftermath-of-genesis|The Aftermath of Genesis]], according to the mission page.",
                "L'Old Lantern n'existe que dans cette mission, et le compendium, consultable pendant celle-ci, reste ensuite verrouillé jusqu'à [[m:the-aftermath-of-genesis|The Aftermath of Genesis]], selon la page de la mission."),
            two("Charles's mare Taima is the only gang member's horse the player rides in a mission, according to the mission page.",
                "Taima, la jument de Charles, est le seul cheval d'un membre de la bande que le joueur monte pendant une mission, d'après la page de la mission."),
            two("A few of the O'Driscolls' horses stand outside the barn and run off during the shootout. Once Arthur has led the horse out of the barn, an invisible wall stops him from going back in, according to the mission page.",
                "Quelques chevaux des O'Driscoll attendent devant la grange et s'enfuient pendant la fusillade. Une fois qu'Arthur a fait sortir le cheval de la grange, un mur invisible l'empêche d'y retourner, selon la page de la mission."),
        ],
    },
}
