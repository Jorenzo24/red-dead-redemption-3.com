"""Charles Smith, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched 15 Oct 2026 via the MediaWiki API, saved in
scratchpad cov/charles/, cov/charles/m/, cov/charles/m/c/, cov/arthur/m/):
- Red Dead Wiki EN "Charles Smith" (Mission appearances, Quotes, Trivia, Gallery
  captions) and FR "Charles Smith" (Apparitions dans les missions, Anecdotes).
- Mission pages: Outlaws from the West, The Aftermath of Genesis, Old Friends, Who the
  Hell is Leviticus Cornwall?, Eastward Bound, Americans at Rest, The First Shall Be
  Last, Pouring Forth Oil IV, A Strange Kindness, An Honest Mistake, Magicians for
  Sport, Blood Feuds, Ancient and Modern, The Battle of Shady Belle, Horsemen,
  Apocalypses, Banking, The Old American Art, Fleeting Joy, That's Murfree Country,
  A Rage Unleashed, The Fine Art of Conversation, The King's Son, My Last Boy, Red Dead
  Redemption (mission), Bare Knuckle Friendships, Home Improvement for Beginners, The
  Tool Box, A New Jerusalem, Uncle's Bad Day, American Venom, Hunting (Charles Smith).
- Transcripts "/dialogues": Outlaws from the West, The Aftermath of Genesis, Old
  Friends, Who the Hell is Leviticus Cornwall?, Eastward Bound, Americans at Rest, The
  First Shall Be Last, Pouring Forth Oil IV, Red Dead Redemption (mission), American
  Venom. No transcript exists for the chapter 3 to 6 missions nor for the epilogue
  missions other than American Venom: quotes from them come from the quote boxes of the
  mission pages or from the character page's Quotes section.
- Other wiki pages: Notorious Bad Man Alive (1907 newspaper), Arthur's journal (gang
  savings, via the My Last Boy page).
- Real world: Wikipedia "List of Red Dead Redemption 2 characters" (Charles section,
  Piggyback Complete Official Guide p. 359; composite of the gang portraits);
  SacAnime Summer 2019 cast Q&A (cited by both wiki editions); trailer and portrait
  dates as established in hosea_C / micah_C / sadie_C.
Excluded: all cut content (Development covers it: the chapter 4 rescue mission, the
Bill tripping encounter, the unused Taima line); his sawed-off shotgun, the Cattleman
Revolver he holsters, the knife worn like John's (weapons, part B); being the only
member whose horse Arthur rides (horse, part B); the FR note that he backs Arthur
against Dutch (relationship and interpretation); the Sekiro "Wolf" parallel (actor);
the wiki's reading of the "A, D, C, B & S" ledger entry (speculation); the
"pretty hillside" line in quotation marks (only a trivia paraphrase with a dash, not
a transcript); minor AI glitches (barn fight in Magicians for Sport, fire bottle).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]
K = lambda name, mission, en, fr: [name, mission, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
E2 = two("Epilogue, part 2", "Épilogue, partie 2")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 28 story missions of Red Dead Redemption 2 for Charles: 21 from the opening of chapter 1 to the end of chapter 6, six in the second part of the epilogue, and one in which only his voice is heard. The French edition lists 27: it leaves out the voice-only appearance in \"Red Dead Redemption\". The table follows the English list in story order and adds the bison hunt, a companion activity he offers in chapter 2. Charles is never playable. He is the mission giver of \"The King's Son\" and of the hunting activity, and he appears in no mission of the first part of the epilogue.",
              "Le Red Dead Wiki anglais recense 28 missions principales de Red Dead Redemption 2 pour Charles : 21 du début du chapitre 1 à la fin du chapitre 6, six dans la seconde partie de l'épilogue, et une où l'on n'entend que sa voix. L'édition française en compte 27 : elle omet l'apparition vocale dans \"Red Dead Redemption\". Le tableau reprend la liste anglaise dans l'ordre du récit et y ajoute la chasse au bison, une activité de compagnon qu'il propose au chapitre 2. Charles n'est jamais jouable. Il est le donneur de \"The King's Son\" et de l'activité de chasse, et n'apparaît dans aucune mission de la première partie de l'épilogue.")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Charles's role", "Rôle de Charles")], "rows": [
        M("Outlaws from the West", C1,
          "Turns up in the blizzard at Colter with two horses for [[dutch-van-der-linde|Dutch]] and [[arthur-morgan|Arthur]], who ride out on them to Adler Ranch. Dutch orders him indoors to rest his injured hand.",
          "Surgit dans le blizzard à Colter avec deux chevaux pour [[dutch-van-der-linde|Dutch]] et [[arthur-morgan|Arthur]], qui partent avec eux vers Adler Ranch. Dutch lui ordonne de rentrer se reposer à cause de sa main blessée."),
        M("The Aftermath of Genesis", C1,
          "Cuts short a discussion between Arthur and [[simon-pearson|Pearson]] about the lack of food and takes Arthur hunting. Unable to draw a bow because of his burnt hand, he gives Arthur his own and teaches him to track and kill two deer, then helps carry them back to camp.",
          "Coupe court à une discussion entre Arthur et [[simon-pearson|Pearson]] sur le manque de vivres et emmène Arthur chasser. Incapable de bander un arc à cause de sa main brûlée, il lui confie le sien, lui apprend à pister et abattre deux cerfs, puis l'aide à les rapporter au camp."),
        M("Old Friends", C1,
          "Stays at Colter with Pearson and [[hosea-matthews|Hosea]] while the others raid the O'Driscoll camp. On the way back, Dutch names him among the men he wants riding with the gang again.",
          "Reste à Colter avec Pearson et [[hosea-matthews|Hosea]] pendant que les autres attaquent le camp O'Driscoll. Au retour, Dutch le cite parmi les hommes qu'il veut revoir en selle avec le gang."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "Keeps lookout for outriders during the robbery of the Cornwall train, on Dutch's orders. He then joins the gunfight and places the dynamite on the train door of Cornwall's private car with Arthur.",
          "Surveille les éventuels cavaliers d'escorte pendant l'attaque du train de Cornwall, sur ordre de Dutch. Il prend ensuite part à la fusillade et pose avec Arthur la dynamite sur la porte de la voiture privée de Cornwall."),
        M("Eastward Bound", C1,
          "Rides down from the mountains in a wagon with [[bill-williamson|Bill]]. When Arthur's wagon loses a wheel, he holds it up with Hosea, then rides on with them and tells them about his parents and how he left home at around thirteen.",
          "Descend de la montagne dans un chariot avec [[bill-williamson|Bill]]. Quand le chariot d'Arthur perd une roue, il le soulève avec Hosea, puis fait la route avec eux et leur parle de ses parents et de son départ, vers l'âge de treize ans."),
        M("Americans at Rest", C2,
          "Drinks at the bar of the Valentine saloon with [[javier-escuella|Javier]] and two women. He throws a chair in the brawl started by Bill and cheers Arthur on during his fight against Tommy. Dutch then sends him to gather information on Sean.",
          "Boit au comptoir du saloon de Valentine avec [[javier-escuella|Javier]] et deux femmes. Il lance une chaise dans la bagarre déclenchée par Bill et encourage Arthur pendant son combat contre Tommy. Dutch l'envoie ensuite se renseigner sur Sean."),
        M("Hunting (companion activity)", C2,
          "Mission giver. Takes Arthur bison hunting in the Heartlands, follows a trail of carcasses left to rot and shoots one of the two poachers responsible. Not listed among the story missions by the wiki.",
          "Donneur de mission. Emmène Arthur chasser le bison dans les Heartlands, suit une piste de carcasses laissées à pourrir et abat l'un des deux braconniers responsables. Le wiki ne la compte pas parmi les missions principales."),
        M("The First Shall Be Last", C2,
          "Watches Blackwater from a clifftop with Javier and refuses Arthur's idea of abandoning [[sean-macguire|Sean]]. He covers the others from the north side of the valley, joins them at Ike Skelding's camp and rides back to camp separately.",
          "Observe Blackwater depuis une falaise avec Javier et refuse l'idée d'Arthur d'abandonner [[sean-macguire|Sean]]. Il couvre les autres depuis le versant nord de la vallée, les rejoint au camp d'Ike Skelding et rentre au camp de son côté."),
        M("Pouring Forth Oil IV", C2,
          "Joins the train robbery organised by [[john-marston|John]] with Arthur and Sean. He knocks out the engineer, then helps fight off the lawmen.",
          "Participe à l'attaque de train organisée par [[john-marston|John]], avec Arthur et Sean. Il assomme le mécanicien, puis aide à repousser les représentants de la loi."),
        M("A Strange Kindness", C2,
          "Scouts Dewberry Creek with Arthur as a possible camp. He convinces Arthur to look for the missing husband of a German woman, tracks him down and fights off his captors. He then leads the gang to Clemens Point instead.",
          "Explore Dewberry Creek avec Arthur à la recherche d'un nouveau camp. Il convainc Arthur de partir à la recherche du mari disparu d'une Allemande, retrouve sa trace et repousse ses ravisseurs. Il conduit ensuite le gang à Clemens Point."),
        M("An Honest Mistake", C3,
          "Rides with [[uncle|Uncle]], Arthur and Bill to rob a wagon that turns out to belong to Cornwall Kerosene & Tar. He shoots the guard Lowe as soon as their cover is blown, shelters in a barn that is set on fire and escapes through the woods with Bill.",
          "Accompagne [[uncle|Uncle]], Arthur et Bill pour dévaliser un chariot qui appartient en fait à Cornwall Kerosene & Tar. Il abat le garde Lowe dès que leur couverture tombe, se réfugie dans une grange incendiée et s'enfuit par les bois avec Bill."),
        M("Magicians for Sport", C3,
          "Goes with Arthur to look for [[josiah-trelawny|Trelawny]], kidnapped by bounty hunters working for Cole Stoudemire. In the Braithwaite corn fields he kills the hunter holding Arthur hostage, then rides back to camp with Trelawny.",
          "Part avec Arthur à la recherche de [[josiah-trelawny|Trelawny]], enlevé par des chasseurs de primes à la solde de Cole Stoudemire. Dans les champs de maïs des Braithwaite, il tue celui qui retient Arthur en otage, puis rentre au camp avec Trelawny."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Rides with Dutch, Arthur, Hosea, John, Bill, Javier and [[lenny-summers|Lenny]] to Braithwaite Manor to get [[jack-marston|Jack]] back.",
          "Accompagne Dutch, Arthur, Hosea, John, Bill, Javier et [[lenny-summers|Lenny]] à Braithwaite Manor pour récupérer [[jack-marston|Jack]]."),
        M("The Battle of Shady Belle", C3,
          "Present at Clemens Point when [[andrew-milton|Milton]] and [[edgar-ross|Ross]] confront the gang. Milton offers the others three days to disappear if Dutch surrenders; the gang reaches for its weapons and Susan tells him to leave. Charles has no line.",
          "Présent à Clemens Point quand [[andrew-milton|Milton]] et [[edgar-ross|Ross]] viennent trouver le gang. Milton laisse trois jours aux autres pour disparaître si Dutch se rend ; le gang prend les armes et Susan lui ordonne de partir. Charles ne dit rien."),
        M("Horsemen, Apocalypses", C4,
          "Defends Shady Belle against the O'Driscolls from a post given by Dutch. He kills one of them with a machete, then buries [[kieran-duffy|Kieran]] with [[orville-swanson|Swanson]] and Pearson.",
          "Défend Shady Belle contre les O'Driscoll depuis le poste que lui attribue Dutch. Il tue l'un d'eux à la machette, puis enterre [[kieran-duffy|Kieran]] avec [[orville-swanson|Swanson]] et Pearson."),
        M("Banking, The Old American Art", C4,
          "Handles crowd control during the robbery with Bill and [[micah-bell|Micah]] and holds off the police wagons with Arthur. He hides with the five other survivors, then draws the Pinkertons away at the docks so that the others can board the ship. He returns to Shady Belle on a stagecoach.",
          "Contrôle la foule pendant le braquage avec Bill et [[micah-bell|Micah]], puis repousse les chariots de police avec Arthur. Il se cache avec les cinq autres survivants, puis attire les Pinkerton à l'écart sur les quais pour que les autres puissent embarquer. Il regagne Shady Belle caché dans une diligence."),
        M("Fleeting Joy", C5,
          "At Lakay with the gang, which he and [[sadie-adler|Sadie]] moved there, when Arthur, then Dutch, return from Guarma. He is still there when the Pinkertons attack the village.",
          "À Lakay avec le gang, qu'il y a installé avec [[sadie-adler|Sadie]], quand Arthur puis Dutch reviennent de Guarma. Il est toujours là quand les Pinkerton attaquent le village."),
        M("That's Murfree Country", C5,
          "Scouts Beaver Hollow with Arthur, on horseback or by canoe. The two clear the Murfree Brood out of the cave; Arthur takes their captive home to Annesburg while Charles leads the gang to the new camp.",
          "Part en reconnaissance à Beaver Hollow avec Arthur, à cheval ou en canoë. Les deux hommes chassent la Murfree Brood de la grotte ; Arthur ramène leur captive à Annesburg pendant que Charles conduit le gang au nouveau camp."),
        M("A Rage Unleashed", C6,
          "At Beaver Hollow when Karen and Javier escort Eagle Flies into camp. He reminds Eagle Flies of his promise to Rains Fall not to fight over horses, but goes along with Arthur, Dutch and Eagle Flies to take back the Wapiti horses from an army boat. Afterwards he asks Arthur to visit Rains Fall.",
          "Présent à Beaver Hollow quand Karen et Javier escortent Eagle Flies jusqu'au camp. Il lui rappelle sa promesse faite à Rains Fall de ne pas se battre pour des chevaux, mais accompagne Arthur, Dutch et Eagle Flies pour reprendre les chevaux des Wapiti sur un bateau de l'armée. Il demande ensuite à Arthur de rendre visite à Rains Fall."),
        M("The Fine Art of Conversation", C6,
          "Escorts Rains Fall to his meeting with Colonel Favours with Arthur, whom he persuaded to come. When Captain Monroe is accused of treason, the two take soldiers hostage, carry Monroe off and put him on a train at Emerald Station.",
          "Escorte Rains Fall à sa rencontre avec le colonel Favours en compagnie d'Arthur, qu'il a convaincu de venir. Quand le capitaine Monroe est accusé de trahison, les deux hommes prennent des soldats en otage, emmènent Monroe et le mettent dans un train à Emerald Station."),
        M("The King's Son", C6,
          "Mission giver. On the ride to Fort Wallace, before the rescue, Arthur tells him he is dying. Charles leads the rescue of Eagle Flies: he climbs the wall with a grappling hook, kills the prison guard and escapes with Arthur, Eagle Flies riding behind him on Taima, then by canoe. He takes Eagle Flies back to the reservation.",
          "Donneur de mission. Sur la route de Fort Wallace, avant l'évasion, Arthur lui apprend qu'il est condamné. Charles dirige l'évasion d'Eagle Flies : il escalade le mur avec un grappin, tue le gardien de la prison et s'enfuit avec Arthur, Eagle Flies en croupe derrière lui sur Taima, puis en canoë. Il ramène Eagle Flies à la réserve."),
        M("My Last Boy", C6,
          "Rides with Arthur, Sadie and a few Wapiti to rescue Eagle Flies at the Cornwall oil fields and refuses his share of the money. After Eagle Flies is mortally wounded, he brings him back to the reservation with Arthur and Paytah, decides to stay with the Wapiti and says goodbye to Arthur.",
          "Accompagne Arthur, Sadie et quelques Wapiti pour secourir Eagle Flies aux champs pétrolifères de Cornwall, et refuse sa part de l'argent. Une fois Eagle Flies mortellement blessé, il le ramène à la réserve avec Arthur et Paytah, choisit de rester avec les Wapiti et fait ses adieux à Arthur."),
        M("Red Dead Redemption (voice only)", C6,
          "Heard in Arthur's memories during his last ride, with high Honor: his line \"In a way, you were lucky\" from \"The King's Son\".",
          "Entendu dans les souvenirs d'Arthur lors de sa dernière chevauchée, avec un honneur élevé : sa réplique \"In a way, you were lucky\" (d'une certaine façon, tu as eu de la chance), tirée de \"The King's Son\"."),
        M("Bare Knuckle Friendships", E2,
          "Found by John and Uncle at a fight in the Saint Denis slums in 1907. He beats Simon of Wales after promising Guido Martelli's men to lose, kills Martelli's four men at the docks with John and drives the wagon out of the city.",
          "Retrouvé par John et Uncle lors d'un combat dans les bas quartiers de Saint-Denis en 1907. Il bat Simon of Wales après avoir promis aux hommes de Guido Martelli de perdre, abat avec John les quatre hommes de Martelli sur les quais et conduit le chariot hors de la ville."),
        M("Home Improvement for Beginners", E2,
          "Waits with Uncle at the campfire at Beecher's Hope and helps John tear down the old shack. He stays with Uncle while John goes to Blackwater for a pre-cut house.",
          "Attend avec Uncle près du feu à Beecher's Hope et aide John à démolir la vieille cabane. Il reste avec Uncle pendant que John part à Blackwater acheter une maison en kit."),
        M("The Tool Box", E2,
          "Escorts the lumber from Blackwater, by way of the tools at Manzanita Post, with John and two hired guns, Mr. Wayne and Mr. Devon. After a Skinner Brothers ambush, he and John find Wayne dead; Charles takes the body to be buried.",
          "Escorte le bois depuis Blackwater, en passant prendre les outils à Manzanita Post, avec John et deux hommes de main, M. Wayne et M. Devon. Après une embuscade des Skinner Brothers, John et lui retrouvent Wayne mort ; Charles emporte le corps pour le faire enterrer."),
        M("A New Jerusalem", E2,
          "Builds the house at Beecher's Hope with John over several weeks, from the foundations to the roof, and toasts its completion with John and Uncle.",
          "Construit la maison de Beecher's Hope avec John pendant plusieurs semaines, des fondations au toit, et trinque à son achèvement avec John et Uncle."),
        M("Uncle's Bad Day", E2,
          "Wakes John after the celebration to report that Uncle is missing. They track the Skinners to their camp; Charles carries the burnt Uncle out and nurses him at the ranch.",
          "Réveille John après la fête pour lui annoncer la disparition d'Uncle. Ils suivent les Skinner jusqu'à leur camp ; Charles porte Uncle, brûlé, jusqu'aux chevaux et le soigne au ranch."),
        M("American Venom", E2,
          "Rides with Sadie and John to Strawberry, then to Mount Hagen, where a sniper hits him in the shoulder. He follows the others slowly and shoots the man who stabs Sadie. After the wedding, the ending credits show him leaving Beecher's Hope.",
          "Accompagne Sadie et John à Strawberry, puis au mont Hagen, où un tireur embusqué le touche à l'épaule. Il suit les autres à distance et abat l'homme qui poignarde Sadie. Après le mariage, le générique de fin le montre quittant Beecher's Hope."),
    ]}},
    # ---------------------------------------------------------- notable kills
    {"h3": two("Notable people Charles kills", "Personnages notables tués par Charles")},
    {"p": two("The Red Dead Wiki has no list of notable murders for Charles. The table gathers the named or singled-out victims that the mission pages attribute to him. Soldiers, bounty hunters, Murfrees, Skinners and members of Micah's gang killed in gunfights alongside Arthur or John are not listed one by one.",
              "Le Red Dead Wiki ne dresse pas de liste des meurtres notables de Charles. Le tableau réunit les victimes nommées ou clairement identifiées que les pages des missions lui attribuent. Les soldats, chasseurs de primes, Murfree, Skinner et hommes de Micah abattus aux côtés d'Arthur ou de John lors des fusillades ne sont pas détaillés.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K(two("Bison poacher", "Braconnier de bisons"), "Hunting (companion activity)",
          "Shot with his sawed-off shotgun when the man becomes aggressive at the poachers' camp. The second poacher can be killed or spared by Arthur.",
          "Abattu au fusil à canon scié quand l'homme se montre agressif au camp des braconniers. Le second peut être tué ou épargné par Arthur."),
        K(two("Lowe", "Lowe"), "An Honest Mistake",
          "Storyline. A Cornwall Kerosene & Tar guard, killed as soon as the gang's cover is blown.",
          "Histoire. Garde de Cornwall Kerosene & Tar, abattu dès que la couverture du gang tombe."),
        K(two("Bounty hunter", "Chasseur de primes"), "Magicians for Sport",
          "Storyline. Killed with a thrown weapon while holding Arthur hostage in the corn fields.",
          "Histoire. Tué d'une arme de jet alors qu'il tient Arthur en otage dans les champs de maïs."),
        K(two("O'Driscoll", "O'Driscoll"), "Horsemen, Apocalypses",
          "Storyline. Knocked down and killed with a machete after Charles leaps out of a side door of the house.",
          "Histoire. Renversé et tué à la machette après que Charles a surgi par une porte latérale de la maison."),
        K(two("Fort Wallace prison guard", "Gardien de la prison de Fort Wallace"), "The King's Son",
          "Storyline. Killed by Charles so that Arthur can take the keys to Eagle Flies's cell.",
          "Histoire. Tué par Charles pour qu'Arthur puisse prendre les clés de la cellule d'Eagle Flies."),
        K(two("Jackson", "Jackson"), "The King's Son",
          "Determinant. The soldier can be killed by Arthur or by Charles, unless Arthur already killed him in \"The Fine Art of Conversation\".",
          "Selon le joueur. Ce soldat peut être tué par Arthur ou par Charles, sauf si Arthur l'a déjà tué dans \"The Fine Art of Conversation\"."),
        K(two("Member of Micah's gang", "Homme de Micah"), "American Venom",
          "Storyline. Shot while stabbing Sadie on Mount Hagen; John finishes him off.",
          "Histoire. Abattu alors qu'il poignarde Sadie sur le mont Hagen ; John l'achève."),
    ]}},
]

BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. The last three come from the Red Dead Wiki's quote list, which names no mission for them.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Les trois dernières proviennent de la liste de citations du Red Dead Wiki, qui ne précise pas de mission.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 and 2", "Red Dead Redemption 2, chapitres 1 et 2")},
    {"quotes": [
        {"q": two("You're never too old to learn... I imagine.",
                  "You're never too old to learn... I imagine."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), to Arthur, who has never used a bow",
                    "The Aftermath of Genesis (RDR2, chapitre 1), à Arthur, qui ne s'est jamais servi d'un arc. Traduction : « On n'est jamais trop vieux pour apprendre... j'imagine. »")},
        {"q": two("Sooner or later a job's going to go wrong. Nature of life.",
                  "Sooner or later a job's going to go wrong. Nature of life."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), to Arthur, about the failed Blackwater robbery",
                    "The Aftermath of Genesis (RDR2, chapitre 1), à Arthur, à propos du braquage raté de Blackwater. Traduction : « Tôt ou tard, un coup finit par mal tourner. C'est la vie. »")},
        {"q": two("I did that for a long time. I'm done with it. Always wondering if someone's gonna kill you in your sleep.",
                  "I did that for a long time. I'm done with it. Always wondering if someone's gonna kill you in your sleep."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), to Arthur, who asks whether he would rather move on alone",
                    "The Aftermath of Genesis (RDR2, chapitre 1), à Arthur, qui lui demande s'il préférerait repartir seul. Traduction : « Je l'ai fait pendant longtemps. J'en ai fini. À toujours se demander si quelqu'un va te tuer dans ton sommeil. »")},
        {"q": two("He treats me fair. Most of you do. And for a feller with a black father and an Indian mother, that ain't normally the case.",
                  "He treats me fair. Most of you do. And for a feller with a black father and an Indian mother, that ain't normally the case."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), to Arthur, about Dutch",
                    "The Aftermath of Genesis (RDR2, chapitre 1), à Arthur, à propos de Dutch. Traduction : « Il me traite correctement. Comme la plupart d'entre vous. Et pour un type avec un père noir et une mère indienne, c'est rarement le cas. »")},
        {"q": two("Unpleasant? How do you rob and kill people pleasantly? We don't, in spite of Dutch's talk.",
                  "Unpleasant? How do you rob and kill people pleasantly? We don't, in spite of Dutch's talk."),
         "src": two("Eastward Bound (RDR2, chapter 1), to Hosea, who says part of the army was particularly unpleasant in driving the Native Americans off the Heartlands",
                    "Eastward Bound (RDR2, chapitre 1), à Hosea, qui explique qu'une partie de l'armée s'est montrée particulièrement déplaisante en chassant les Amérindiens des Heartlands. Traduction : « Désagréable ? Comment on vole et on tue les gens agréablement ? On ne le fait pas, quoi qu'en dise Dutch. »")},
        {"q": two("If they wanted trouble... we wouldn't have seen them.",
                  "If they wanted trouble... we wouldn't have seen them."),
         "src": two("Eastward Bound (RDR2, chapter 1), to Arthur and Hosea, about the Native riders watching them from a cliff",
                    "Eastward Bound (RDR2, chapitre 1), à Arthur et Hosea, à propos des cavaliers amérindiens qui les observent depuis une falaise. Traduction : « S'ils cherchaient les ennuis... on ne les aurait pas vus. »")},
        {"q": two("We're not cutting anyone loose.",
                  "We're not cutting anyone loose."),
         "src": two("The First Shall Be Last (RDR2, chapter 2), to Arthur, who considers leaving Sean to his fate",
                    "The First Shall Be Last (RDR2, chapitre 2), à Arthur, qui envisage d'abandonner Sean à son sort. Traduction : « On ne laisse tomber personne. »")},
        {"q": two("Why do you have to speak so much? It's... incessant.",
                  "Why do you have to speak so much? It's... incessant."),
         "src": two("Pouring Forth Oil IV (RDR2, chapter 2), to Sean, on the way to the train",
                    "Pouring Forth Oil IV (RDR2, chapitre 2), à Sean, en route vers le train. Traduction : « Pourquoi tu parles autant ? C'est... incessant. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, chapter 6", "Red Dead Redemption 2, chapitre 6")},
    {"quotes": [
        {"q": two("You know I told your father I will not fight over some horses.",
                  "You know I told your father I will not fight over some horses."),
         "src": two("A Rage Unleashed (RDR2, chapter 6), to Eagle Flies, who asks the gang to help recover the tribe's horses",
                    "A Rage Unleashed (RDR2, chapitre 6), à Eagle Flies, qui demande au gang de l'aider à reprendre les chevaux de la tribu. Traduction : « Tu sais que j'ai promis à ton père de ne pas me battre pour des chevaux. »")},
        {"q": two("Any day we can die. We're about to break an Indian Chief's son out of a cavalry fort. We can both die tonight.",
                  "Any day we can die. We're about to break an Indian Chief's son out of a cavalry fort. We can both die tonight."),
         "src": two("The King's Son (RDR2, chapter 6), to Arthur, on the way to Fort Wallace",
                    "The King's Son (RDR2, chapitre 6), à Arthur, en route vers Fort Wallace. Traduction : « On peut mourir n'importe quel jour. On s'apprête à faire évader le fils d'un chef indien d'un fort de cavalerie. On peut mourir tous les deux ce soir. »")},
        {"q": two("You're lucky. You got the chance to... to do something better... My guess is maybe that's why you're here now.",
                  "You're lucky. You got the chance to... to do something better... My guess is maybe that's why you're here now."),
         "src": two("The King's Son (RDR2, chapter 6), to Arthur, after he reveals that he is dying",
                    "The King's Son (RDR2, chapitre 6), à Arthur, qui vient de lui apprendre qu'il est condamné. Traduction : « Tu as de la chance. Tu as l'occasion de... de faire quelque chose de mieux... Je me dis que c'est peut-être pour ça que tu es là. »")},
        {"q": two("Those money, those bonds, whatever it is... I don't want a cent. There's too much blood on it.",
                  "Those money, those bonds, whatever it is... I don't want a cent. There's too much blood on it."),
         "src": two("My Last Boy (RDR2, chapter 6), refusing his share of the take from the oil refinery",
                    "My Last Boy (RDR2, chapitre 6), en refusant sa part du butin de la raffinerie. Traduction : « Cet argent, ces obligations, peu importe... Je n'en veux pas un sou. Il y a trop de sang dessus. »")},
        {"q": two("The time has come for us to draw our own lines, Arthur. Decide where we go from here.",
                  "The time has come for us to draw our own lines, Arthur. Decide where we go from here."),
         "src": two("My Last Boy (RDR2, chapter 6), to Arthur",
                    "My Last Boy (RDR2, chapitre 6), à Arthur. Traduction : « Le moment est venu de tracer nos propres limites, Arthur. De décider où on va maintenant. »")},
    ]},
    {"h4": two("Epilogue", "Épilogue")},
    {"quotes": [
        {"q": two("Mm-hmm. When I'm not killing old friends.",
                  "Mm-hmm. When I'm not killing old friends."),
         "src": two("American Venom (RDR2, epilogue), to Sadie, who has heard that he is building houses",
                    "American Venom (RDR2, épilogue), à Sadie, qui a entendu dire qu'il construisait des maisons. Traduction : « Mm-hmm. Quand je ne tue pas de vieux amis. »")},
        {"q": two("No, that work ain't for me. I... I think I might get out of here. Go North. Canada. Find a woman. Start a family, if I can. I see how that life... well, I'd like to try it.",
                  "No, that work ain't for me. I... I think I might get out of here. Go North. Canada. Find a woman. Start a family, if I can. I see how that life... well, I'd like to try it."),
         "src": two("American Venom (RDR2, epilogue), to Sadie, who offers him bounty hunting work",
                    "American Venom (RDR2, épilogue), à Sadie, qui lui propose de chasser les primes avec elle. Traduction : « Non, ce travail n'est pas pour moi. Je... je crois que je vais partir d'ici. Aller vers le nord. Le Canada. Trouver une femme. Fonder une famille, si je peux. Je vois ce que c'est, cette vie... eh bien, j'aimerais essayer. »")},
        {"q": two("I will be... but go on... go on now! Move fast... or they'll come down that hill and kill us all...",
                  "I will be... but go on... go on now! Move fast... or they'll come down that hill and kill us all..."),
         "src": two("American Venom (RDR2, epilogue), to John and Sadie, after the sniper's shot on Mount Hagen",
                    "American Venom (RDR2, épilogue), à John et Sadie, après le tir du sniper sur le mont Hagen. Traduction : « Ça ira... mais allez-y... allez-y maintenant ! Faites vite... ou ils vont descendre de cette colline et nous tuer tous... »")},
    ]},
    {"h4": two("Camp and activities", "Camp et activités")},
    {"quotes": [
        {"q": two("Where the bison went, my people went. They were the center of all life... we couldn't survive without them. They provide us with everything... food, clothing, shelter, tools. There was a lot of respect...",
                  "Where the bison went, my people went. They were the center of all life... we couldn't survive without them. They provide us with everything... food, clothing, shelter, tools. There was a lot of respect..."),
         "src": two("Hunting (RDR2, chapter 2), to Arthur, during the bison hunt",
                    "Activité de chasse (RDR2, chapitre 2), à Arthur, pendant la chasse au bison. Traduction : « Là où allaient les bisons, mon peuple allait. Ils étaient au centre de toute vie... on ne pouvait pas survivre sans eux. Ils nous donnaient tout... la nourriture, les vêtements, l'abri, les outils. Il y avait beaucoup de respect... »")},
        {"q": two("Other human beings seem to understand why they were born, but, for me... it seems like I was born to hurt and suffer myself. That doesn't always seem like a really good reason. Uh... I wish there was another way. But here, in this land, uh... I feel very stuck.",
                  "Other human beings seem to understand why they were born, but, for me... it seems like I was born to hurt and suffer myself. That doesn't always seem like a really good reason. Uh... I wish there was another way. But here, in this land, uh... I feel very stuck."),
         "src": two("Camp (RDR2), during a campfire conversation",
                    "Au camp (RDR2), lors d'une conversation au coin du feu. Traduction : « Les autres semblent comprendre pourquoi ils sont nés, mais moi... on dirait que je suis né pour souffrir et me faire du mal. Ça ne me semble pas toujours une très bonne raison. Euh... j'aimerais qu'il y ait un autre chemin. Mais ici, sur cette terre, euh... je me sens vraiment coincé. »")},
    ]},
    {"h4": two("Lines without a mission", "Répliques hors mission")},
    {"quotes": [
        {"q": two("I don't kill for fun. I kill when I need to.",
                  "I don't kill for fun. I kill when I need to."),
         "src": two("Red Dead Redemption 2, line listed by the Red Dead Wiki without a mission",
                    "Red Dead Redemption 2, réplique recensée par le Red Dead Wiki sans indication de mission. Traduction : « Je ne tue pas pour le plaisir. Je tue quand il le faut. »")},
        {"q": two("All this death and for what? Just so we can have enough money to be able to run from what we've done?",
                  "All this death and for what? Just so we can have enough money to be able to run from what we've done?"),
         "src": two("Red Dead Redemption 2, on the state of the gang, according to the Red Dead Wiki's quote list",
                    "Red Dead Redemption 2, sur l'état du gang, d'après les citations recensées par le Red Dead Wiki. Traduction : « Toutes ces morts, et pour quoi ? Juste pour avoir assez d'argent pour fuir ce qu'on a fait ? »")},
        {"q": two("We lived a very bad path...",
                  "We lived a very bad path..."),
         "src": two("Red Dead Redemption 2, on his years in the Van der Linde gang, according to the Red Dead Wiki's quote list",
                    "Red Dead Redemption 2, sur ses années dans le gang Van der Linde, d'après les citations recensées par le Red Dead Wiki. Traduction : « On a suivi un bien mauvais chemin... »")},
    ]},
]

BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Story and characters", "Histoire et personnages")},
    {"ul": [
        two("Charles has a burnt hand at Colter. In \"The Aftermath of Genesis\" he tells Arthur: \"I'm okay, apart from this hand. Stupid mistake.\" The Red Dead Wiki links the injury to Red Harlow, the part Native American hero of Red Dead Revolver (2004), whose story also begins with a burnt hand.",
            "Charles a la main brûlée à Colter. Dans \"The Aftermath of Genesis\", il dit à Arthur : \"I'm okay, apart from this hand. Stupid mistake.\" (ça va, à part cette main, une bêtise). Le Red Dead Wiki rapproche cette blessure de Red Harlow, héros en partie amérindien de Red Dead Revolver (2004), dont l'histoire commence aussi par une main brûlée."),
        two("In \"Americans at Rest\", Charles throws a chair when the saloon brawl breaks out. According to the Red Dead Wiki, that shot was motion-captured by Benjamin Byron Davis, the actor who plays Dutch; the reason is not known.",
            "Dans \"Americans at Rest\", Charles lance une chaise quand la bagarre éclate au saloon. Selon le Red Dead Wiki, c'est Benjamin Byron Davis, l'interprète de Dutch, qui a joué ce geste en capture de mouvement ; on ignore pourquoi."),
        two("Scouting for a new camp in \"A Strange Kindness\", Arthur assures Charles that hiding in a cave goes against everything Dutch stands for. In chapter 5 the gang's last camp, Beaver Hollow, is a cave.",
            "En quête d'un nouveau camp dans \"A Strange Kindness\", Arthur assure à Charles que se terrer dans une grotte est contraire à tout ce que défend Dutch. Au chapitre 5, le dernier camp du gang, Beaver Hollow, est justement une grotte."),
        two("In the \"Gang Savings\" section of Arthur's journal, the take from \"My Last Boy\" is credited to \"A, D, C, B & S\" (Arthur, Dutch, Charles, Bill and Sadie), although Charles refuses his share in the mission. John and Javier, who also took part, are not listed.",
            "Dans la rubrique \"Gang Savings\" du journal d'Arthur, le butin de \"My Last Boy\" est attribué à \"A, D, C, B & S\" (Arthur, Dutch, Charles, Bill et Sadie), alors que Charles refuse sa part dans la mission. John et Javier, qui y ont participé, ne figurent pas dans la liste."),
        two("In \"Bare Knuckle Friendships\", John asks the barman or the fence about \"a boxer\", although the game had never shown Charles boxing before. If John bets on Charles, he wins 40 dollars.",
            "Dans \"Bare Knuckle Friendships\", John interroge le barman ou le receleur au sujet d'\"un boxeur\", alors que le jeu n'avait jamais montré Charles en train de boxer. S'il parie sur Charles, John gagne 40 dollars."),
        two("In the dockside shootout of the same mission, Martelli's men carry Mauser Pistols, which surprises John; Charles answers that new inventions come quickly. A remix of \"The Outlaw's Return\", from the score of Red Dead Redemption, plays as the two men leave the city.",
            "Lors de la fusillade sur les quais, les hommes de Martelli sont armés de pistolets Mauser, ce qui étonne John ; Charles lui répond que les inventions vont vite. Un remix de \"The Outlaw's Return\", tiré de la bande originale de Red Dead Redemption, accompagne leur fuite hors de la ville."),
        two("In \"American Venom\", while John and Sadie threaten Cleet with hanging in Strawberry, Charles keeps the townspeople back with lines such as \"My boss is a licensed bounty hunter. She can do what she wants.\"",
            "Dans \"American Venom\", pendant que John et Sadie menacent de pendre Cleet à Strawberry, Charles tient les habitants à distance avec des répliques comme \"My boss is a licensed bounty hunter. She can do what she wants.\" (ma patronne est chasseuse de primes agréée, elle fait ce qu'elle veut)."),
    ]},
    {"h4": two("Lines that depend on Arthur's Honor", "Répliques selon l'honneur d'Arthur")},
    {"ul": [
        two("In \"Bare Knuckle Friendships\", Charles's assessment of Arthur depends on his Honor at death. With high Honor, Charles calls him \"a good man\" whose illness gave him an understanding of what his life was about; with low Honor, he says Arthur \"wasn't a good man\" and that the illness gave him something to cling to. The low Honor version also plays when the mission is replayed. John's account refers to Arthur's choice between the money and helping John escape.",
            "Dans \"Bare Knuckle Friendships\", le jugement de Charles sur Arthur dépend de son honneur au moment de sa mort. Avec un honneur élevé, Charles dit que c'était \"a good man\" (un homme bien) et que sa maladie lui avait fait comprendre le sens de sa vie ; avec un honneur bas, qu'il \"wasn't a good man\" (n'était pas un homme bien) et que la maladie lui avait donné quelque chose à quoi se raccrocher. La version de l'honneur bas est aussi celle de la rejouabilité. Le récit de John évoque le choix d'Arthur entre l'argent et la fuite de John."),
        two("In \"American Venom\", on the ride to Strawberry, Charles wonders whether Arthur cared about revenge at the end if his Honor was high, or says that revenge is something Arthur could have understood if it was low. Sadie's answer changes in the same way.",
            "Dans \"American Venom\", sur la route de Strawberry, Charles se demande si Arthur tenait encore à la vengeance à la fin, si son honneur était élevé, ou estime qu'Arthur aurait pu la comprendre, s'il était bas. La réponse de Sadie varie de la même façon."),
    ]},
    {"h4": two("Gameplay", "Jeu")},
    {"ul": [
        two("In \"The Aftermath of Genesis\", Charles gets upset if Arthur kills the deer with a gun rather than the bow. When Arthur remarks on the grizzly they meet, Charles answers: \"We've got enough here, no need to push our luck.\" If the player attacks the bear anyway, he shouts: \"What are you doing? Shoot!\" Their talk about the new mouths to feed changes depending on whether \"Old Friends\" has been completed.",
            "Dans \"The Aftermath of Genesis\", Charles s'agace si Arthur abat les cerfs au fusil plutôt qu'à l'arc. Quand Arthur s'intéresse au grizzly qu'ils croisent, Charles répond : \"We've got enough here, no need to push our luck.\" (on en a assez, inutile de tenter le sort). Si le joueur attaque l'ours malgré tout, il crie : \"What are you doing? Shoot!\" (qu'est-ce que tu fais ? Tire !). Leur échange sur les nouvelles bouches à nourrir varie selon que \"Old Friends\" a été terminée ou non."),
        two("After \"Eastward Bound\", Charles is absent from Horseshoe Overlook until \"The First Shall Be Last\" is completed. After \"Pouring Forth Oil IV\", although Arthur tells everyone to split up, Charles, Sean and John ride back to camp together.",
            "Après \"Eastward Bound\", Charles est absent de Horseshoe Overlook jusqu'à la fin de \"The First Shall Be Last\". Après \"Pouring Forth Oil IV\", bien qu'Arthur ait ordonné de se séparer, Charles, Sean et John rentrent ensemble au camp."),
        two("The bison hunt can also be played in chapter 3, when the longer ride from Clemens Point adds dialogue.",
            "La chasse au bison peut aussi se jouer au chapitre 3 : le trajet, plus long depuis Clemens Point, ajoute alors des dialogues."),
        two("In \"A Strange Kindness\", the player can track the missing man with Eagle Eye; if Arthur finds the trail fast enough, he points out the direction before Charles does. Earlier in the mission, Charles speaks his line about the dead man in the dry creek bed as if he had found the body himself, even when the player reached it first.",
            "Dans \"A Strange Kindness\", le joueur peut pister l'homme disparu avec Eagle Eye ; si Arthur trouve la piste assez vite, c'est lui qui indique la direction avant Charles. Plus tôt dans la mission, Charles prononce sa réplique sur le mort du lit de la rivière asséchée comme s'il avait découvert le corps lui-même, même quand le joueur l'a atteint le premier."),
        two("\"That's Murfree Country\" offers a choice between riding to Beaver Hollow and paddling there. If the player hesitates, Charles loses patience and settles on the canoes. On that route the last stretch is covered on Tennessee Walkers borrowed from the village.",
            "\"That's Murfree Country\" laisse le choix entre gagner Beaver Hollow à cheval ou en canoë. Si le joueur tarde à se décider, Charles s'impatiente et choisit les canoës. Par cette voie, la fin du trajet se fait sur des Tennessee Walker empruntés au village."),
        two("In \"Uncle's Bad Day\", the player can kill the Skinner driving the wagon instead of following him to the hideout; the mission continues, but Charles is disappointed.",
            "Dans \"Uncle's Bad Day\", le joueur peut abattre le Skinner qui conduit le chariot au lieu de le suivre jusqu'au repaire ; la mission se poursuit, mais Charles se montre déçu."),
        two("According to the French edition of the wiki, a bug can bring Charles back to Beecher's Hope after the epilogue, during the family dinner. If John speaks to him, he talks about the Skinner Brothers as he did before leaving the ranch.",
            "D'après l'édition française du wiki, un bug peut faire réapparaître Charles à Beecher's Hope après l'épilogue, pendant le repas de famille. Si John lui parle, il évoque les Skinner Brothers comme avant son départ du ranch."),
    ]},
]

BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar's character description of Charles is quoted in the Personality section above. He appears in the official teaser artwork and in promotional artwork drawing his bow. The second trailer, released on September 28, 2017, shows him on horseback saying \"We need an extra gun.\" The third trailer, released on May 2, 2018, shows him with the rest of the gang. On September 6, 2018, Rockstar posted the portraits of the gang's members on Twitter, Charles among them; the composite of the series places him in the back row, between Hosea and Bill.",
              "La description du personnage par Rockstar est citée plus haut, dans la partie Personnalité. Il figure sur l'illustration officielle du teaser et sur une illustration promotionnelle où il bande son arc. La deuxième bande-annonce, publiée le 28 septembre 2017, le montre à cheval en train de dire \"We need an extra gun.\" (il nous faut un fusil de plus). La troisième, publiée le 2 mai 2018, le montre avec le reste du gang. Le 6 septembre 2018, Rockstar publie sur Twitter les portraits des membres du gang, dont le sien ; la composition réunissant la série le place au dernier rang, entre Hosea et Bill.")},
    {"p": two("Red Dead Redemption 2: The Complete Official Guide, published by Piggyback on October 26, 2018, gives him a profile on page 359.",
              "Le guide officiel de Piggyback, Red Dead Redemption 2: The Complete Official Guide, paru le 26 octobre 2018, lui consacre une fiche en page 359.")},
    {"h4": two("In the game world", "Dans l'univers du jeu")},
    {"p": two("In 1907, the newspaper article \"Notorious Bad Man Alive\" reports that Dutch's gang was believed to have broken up in 1899, after Hosea Matthews and Arthur Morgan were killed in separate Pinkerton raids. It names Bill Williamson, Micah Bell, John Marston and Charles Smith as members still believed to be at large, and says that Javier Escuella is thought to live in the mountains of Mexico. Sadie, who rode with the gang in 1899, is not mentioned.",
              "En 1907, l'article \"Notorious Bad Man Alive\" rapporte que le gang de Dutch passait pour dissous depuis 1899, après la mort de Hosea Matthews et d'Arthur Morgan lors de deux descentes distinctes des Pinkerton. Il cite Bill Williamson, Micah Bell, John Marston et Charles Smith comme des membres que l'on croit toujours en fuite, et indique que Javier Escuella vivrait dans les montagnes du Mexique. Sadie, qui faisait pourtant partie du gang en 1899, n'est pas mentionnée.")},
    {"h4": two("Appearances", "Apparitions")},
    {"p": two("At the Red Dead Redemption II cast panel of SacAnime Summer 2019, in Sacramento in June 2019, Roger Clark, who plays Arthur Morgan, named Charles as his favourite character. Both the English and French editions of the Red Dead Wiki cite the recording of that question and answer session.",
              "Lors de la table ronde consacrée aux acteurs de Red Dead Redemption II à la SacAnime de l'été 2019, à Sacramento en juin 2019, Roger Clark, l'interprète d'Arthur Morgan, a désigné Charles comme son personnage préféré. Les éditions anglaise et française du Red Dead Wiki citent toutes deux l'enregistrement de cette séance de questions et réponses.")},
]
