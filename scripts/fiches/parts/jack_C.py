"""Jack Marston, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad
cov/jack/, cov/jack/m/ and cov/jack/fc1/):
- Red Dead Wiki EN "Jack Marston" (Mission appearances, Murders committed, Quotes,
  Gameplay, Trivia, Gallery captions), its quote subpage "Jack Marston/Quotes"
  (fc1/Jack_Marston_Quotes.txt), and FR "Jack Marston" (Apparitions dans les missions,
  Anecdotes).
- Mission pages: Outlaws from the West; Enter, Pursued by a Memory; Who the Hell is
  Leviticus Cornwall?; A Fisher of Men; Who is Not Without Sin; Blood Feuds, Ancient and
  Modern; Angelo Bronte, a Man of Honor; Horsemen, Apocalypses; Fleeting Joy; That's
  Murfree Country; Visiting Hours; Red Dead Redemption (mission); The Wheel; Simple
  Pleasures; Farming, For Beginners; Fatherhood, For Beginners; Fatherhood, For Idiots;
  Old Habits; Jim Milton Rides, Again?; Motherhood; Home Improvement for Beginners; A New
  Jerusalem; The Best of Women; Trying Again; A Really Big Bastard; American Venom; Ending
  Credits; activity page Errand Boy. RDR1: The Outlaw's Return; John Marston and Son;
  Wolves, Dogs and Sons; Spare the Love, Spoil the Child; The Last Enemy That Shall Be
  Destroyed; Remember My Family. Undead Nightmare: Love in the Time of Plague; On a Pale
  Horse. DLC page Liars and Cheats.
- Transcripts "/dialogues": A Fisher of Men; Outlaws from the West; Who the Hell is
  Leviticus Cornwall?; Who is Not Without Sin; Red Dead Redemption (mission); American
  Venom; The Outlaw's Return; John Marston and Son; Wolves, Dogs and Sons; The Last Enemy
  That Shall Be Destroyed; Remember My Family; Spare the Love, Spoil the Child
  (m/Spare_the_Love_Spoil_the_Child_dialogues.txt). Every mission quote is checked word for
  word against one of them; the free-roam lines of 1914 and the RDR2 camp lines come from
  the quote subpage. The wiki has no transcript of Undead Nightmare, so no Undead Nightmare
  line is quoted.
- Real world: Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released
  on September 21, 2010 (as established in bill_C); RDR1 ports (PS4 and Switch, August
  17, 2023; PC, October 29, 2024) without multiplayer, as in bill_C, javier_C, abigail_C;
  Rockstar's tweet "Jack Marston" of September 6, 2018, reproduced by The Hollywood
  Reporter on September 7, 2018 (../abigail/fc/thr_descriptions.txt); the composite image
  of the 23 gang members (Wikipedia caption, m/wp_list.txt: front row "... Abigail, Jack,
  Strauss ..."). Achievements "Into the Sunset" and "Nurture or Nature?" from the mission
  pages. GTA V book from the Other Media trivia of the character page.
Ownership (FIX_RULES), left to other parts: birth year, ages, Yukon years, the 1914 grave
scene and Abigail's death, Bronte's treatment of Jack (toys, baths, spaghetti, Italian
words as such), the sister, Ross's "Enjoy your fishing" line, Arthur's "be brave" line
(A); official descriptions (Rockstar THR text, guides), names and aliases (John Marston
Jr., Jackie, Lancelot Milton, "Papa Bronte", "Little Jacky Marston"), appearance (1899
coat, freckles, missing tooth, outfits, Cowboy Outfit, law outfits), swimming, Dead Eye,
weapons and horses, camp scenes (stones at Kieran, Hosea's reading lesson, crying at
Horseshoe Overlook, Cain at Beaver Hollow, Micah's insult, knights with John, joke on
Uncle), honor-based behavior and prostitutes, NPC routine at Beecher's Hope (B); Josh
Blaylock, Marissa Buccianti, Ted Sutherland, Fred Midgley, Rob Wiethoff's duel mocap,
the Blaylock voice glitch, reception (Mashable, Game Rant) (D).
Quotes (fact-check fixes, 19 Oct 2026): each line sits in one place only. Lines quoted in
part B (Personality, In his own words, Names, Relationships) were removed from this block:
"Fishing sure is boring", "Do you wish I was more like you?", "I must be a disappointment",
"Ah no, they were okay... government man", "Well I could be both", "Don't make no more
promises", "You can't just decide", "only room for one hero", "I'm John Marston - Jr.", "Go
ahead!", "And I was gonna be a writer.", "My ma would turn in her grave", "Name's Marston".
Replacements from the quote subpage: "I'm John Marston's boy!", "Somebody taught me well!"
(Combat), "Sorry, friend. My father was a killer, nothing more!", "That old feller Uncle used
to told me stories like that." (Miscellaneous). Kept HERE only: "No! Uncle! Please!...", "My pa
knew Landon Ricketts, friend!", "Arthur's being mean to me!" (Defuse), "I hate you, Uncle
Arthur!" (Antagonized), "Why did you lie about where Uncle Dutch is?".
Trivia keeps only what is nowhere else: the cheat code, grunts and the ride as sixteen-year-
old (with loot/consumables, from the Last Enemy mission page) are in part B Skills; Cielito
Lindo is in the Javier relationship (B); Ross's weapon and the two river meetings are here
only; John's tense-back advice matching Ricketts' is here only (cut from B). Undead Nightmare:
"Jack cannot be found after John's death" cut (canon mixing, biography owns the ending).
Added: RDR2 audio glitch (EN trivia, attributed, wiki-only).
Excluded: "Jack's favorite Western novel foreshadows his future confrontation with Ross"
and the Isaac/Lancelot/Galsworthy/airplane "foreshadowing" readings (interpretation);
"it's possible that Jack took inspiration from John and Arthur for his outfit"
(speculation); the FR anecdotes "sympathique mais s'énerve facilement", "peu ou pas
d'amis", the reading-lessons claim (unsourced) and "son premier meurtre était un cerf"
(contradicted: the John Marston and Son transcript and page have elk); "only Red Dead
protagonist with no facial scars" (contradicted in part by the Spare the Love page, which
says he keeps scars from the bear) and "only protagonist with freckles" (appearance, B);
"Jack and Ross meet only two times" is kept but limited to on-screen meetings, since the
Bureau holds Jack in 1911; the wiki says Ross holds a shotgun in "A Fisher of Men", the
transcript says a rifle: the transcript is followed (said once, in Trivia); the Undead Nightmare glitches and other glitches
(no value); "Abigail's dialogue implies Jack was returned to normal after her" (stated as
an implication).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]
K = lambda name, mission, en, fr: [name, mission, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
EP1 = two("Epilogue 1: Pronghorn Ranch", "Épilogue 1 : Pronghorn Ranch")
EP2 = two("Epilogue 2: Beecher's Hope", "Épilogue 2 : Beecher's Hope")
A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
E14 = two("Epilogue (1914)", "Épilogue (1914)")
UNM = two("Undead Nightmare", "Undead Nightmare")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 22 story missions of Red Dead Redemption 2 for Jack, from the arrival at Colter to the wedding at Beecher's Hope, six missions of Red Dead Redemption and two of Undead Nightmare. The French edition counts 20 missions for Red Dead Redemption 2: it leaves out \"The Best of Women\" and \"A Really Big Bastard\". For Red Dead Redemption, it leaves out \"Spare the Love, Spoil the Child\" and \"Remember My Family\", and adds a mission in which Jack is only mentioned. Jack is absent from \"Blood Feuds, Ancient and Modern\" and \"The Battle of Shady Belle\", which follow his kidnapping, and neither list includes them. The table below adds \"Who is Not Without Sin\", whose transcript gives him one line.",
              "Le Red Dead Wiki anglais recense pour Jack 22 missions principales de Red Dead Redemption 2, de l'arrivée à Colter jusqu'au mariage à Beecher's Hope, six missions de Red Dead Redemption et deux d'Undead Nightmare. L'édition française compte 20 missions pour Red Dead Redemption 2 : elle omet \"The Best of Women\" et \"A Really Big Bastard\". Pour Red Dead Redemption, elle omet \"Spare the Love, Spoil the Child\" et \"Remember My Family\", et ajoute une mission où Jack n'est que cité. Jack est absent de \"Blood Feuds, Ancient and Modern\" et de \"The Battle of Shady Belle\", qui suivent son enlèvement, et aucune des deux listes ne les retient. Le tableau ci-dessous ajoute \"Who is Not Without Sin\", dont la transcription lui prête une réplique.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 to 6", "Red Dead Redemption 2, chapitres 1 à 6")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Jack's role", "Rôle de Jack")], "rows": [
        M("Outlaws from the West", C1,
          "Travels with the gang through the snow after Blackwater. At the homestead [[arthur-morgan|Arthur]] and [[dutch-van-der-linde|Dutch]] clear of O'Driscolls, Arthur suggests moving the women and Jack down there; Dutch prefers not to split the gang. The mission page gives Jack no action of his own.",
          "Fait route avec le gang dans la neige après Blackwater. Dans la ferme qu'[[arthur-morgan|Arthur]] et [[dutch-van-der-linde|Dutch]] viennent de reprendre aux O'Driscoll, Arthur propose d'y installer les femmes et Jack ; Dutch préfère ne pas diviser le gang. La page de la mission ne lui attribue aucune action propre."),
        M("Enter, Pursued by a Memory", C1,
          "Listed by the wiki. The mission page and its transcript do not mention him.",
          "Citée par le wiki. Ni la page de la mission ni sa transcription ne le mentionnent."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "[[abigail-marston|Abigail]] brings him into the cabin because he wanted to see his father, who lies injured in bed. Dutch greets him, he goes up to [[john-marston|John]], and Abigail takes him out again after trading insults with John.",
          "[[abigail-marston|Abigail]] l'amène dans la cabane parce qu'il voulait voir son père, blessé et alité. Dutch le salue, il s'approche de [[john-marston|John]], puis Abigail le ramène dehors après avoir échangé des piques avec John."),
        M("A Fisher of Men", C2,
          "At Abigail's request, Arthur takes him fishing on the Dakota River with the rod [[hosea-matthews|Hosea]] made him. He asks about the story book left at the Blackwater camp, makes a flower necklace for his mother, and is present when [[andrew-milton|Milton]] and [[edgar-ross|Ross]] confront Arthur. Back at camp he gives Abigail the necklace.",
          "À la demande d'Abigail, Arthur l'emmène pêcher sur la Dakota River avec la canne qu'[[hosea-matthews|Hosea]] lui a fabriquée. Il parle du livre d'histoires oublié au camp de Blackwater, tresse un collier de fleurs pour sa mère et assiste à la confrontation entre Arthur, [[andrew-milton|Milton]] et [[edgar-ross|Ross]]. De retour au camp, il offre le collier à Abigail."),
        M("Who is Not Without Sin", C2,
          "Not in the wiki's list. If Arthur carries the drunk [[orville-swanson|Swanson]] past him in camp, Jack asks whether the Reverend is asleep.",
          "Absente de la liste du wiki. Si Arthur passe devant lui au camp en portant [[orville-swanson|Swanson]], ivre, Jack demande si le révérend dort."),
        M("Angelo Bronte, a Man of Honor", C4,
          "Handed to [[angelo-bronte|Angelo Bronte]] by the Braithwaites, he is returned to Dutch while Arthur and John clear the Saint Denis cemetery of grave robbers. On the ride back he talks fondly of his stay. The gang holds a party at Shady Belle that evening for his return.",
          "Livré à [[angelo-bronte|Angelo Bronte]] par les Braithwaite, il est rendu à Dutch pendant qu'Arthur et John débarrassent le cimetière de Saint-Denis de ses pilleurs de tombes. Sur le chemin du retour, il parle de son séjour avec plaisir. Le soir même, le gang fait la fête à Shady Belle pour son retour."),
        M("Horsemen, Apocalypses", C4,
          "Takes cover inside the Shady Belle house with Abigail, [[mary-beth-gaskill|Mary-Beth]], [[leopold-strauss|Strauss]] and [[susan-grimshaw|Susan]] when the O'Driscolls attack the camp.",
          "Se met à l'abri dans la maison de Shady Belle avec Abigail, [[mary-beth-gaskill|Mary-Beth]], [[leopold-strauss|Strauss]] et [[susan-grimshaw|Susan]] quand les O'Driscoll attaquent le camp."),
        M("Fleeting Joy", C5,
          "Listed by the wiki, but the mission page notes that Jack, Mary-Beth and [[karen-jones|Karen]] are not seen at the Lakay hideout during the mission.",
          "Citée par le wiki, mais la page de la mission relève que Jack, Mary-Beth et [[karen-jones|Karen]] ne sont pas visibles au repaire de Lakay pendant la mission."),
        M("That's Murfree Country", C5,
          "Listed by the wiki for the gang's move to Beaver Hollow. The mission page gives him no action of his own.",
          "Citée par le wiki pour l'installation du gang à Beaver Hollow. La page de la mission ne lui attribue aucune action propre."),
        M("Visiting Hours", C6,
          "Listed by the wiki. The mission page does not mention him.",
          "Citée par le wiki. La page de la mission ne le mentionne pas."),
        M("Red Dead Redemption", C6,
          "[[tilly-jackson|Tilly]] hid with him when Milton's men took Abigail. The two meet the gang on its way back from the train robbery. Arthur gives Tilly a sack of money, tells her to wait with Jack at Copperhead Landing for Abigail and [[sadie-adler|Sadie]], and says goodbye to the boy before riding to Van Horn.",
          "[[tilly-jackson|Tilly]] s'est cachée avec lui quand les hommes de Milton ont emmené Abigail. Tous deux croisent le gang au retour de l'attaque du train. Arthur remet à Tilly un sac d'argent, lui demande d'attendre Abigail et [[sadie-adler|Sadie]] à Copperhead Landing avec Jack, et dit au revoir au garçon avant de partir pour Van Horn."),
    ]}},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"p": two("Jack is absent from Beecher's Hope during the first missions of the second epilogue. Uncle brings up his departure with Abigail in \"Home Improvement for Beginners\", and John's letter in \"A New Jerusalem\" says he misses them both. Neither mission shows him.",
              "Jack est absent de Beecher's Hope pendant les premières missions du second épilogue. Uncle évoque son départ avec Abigail dans \"Home Improvement for Beginners\", et la lettre de John, dans \"A New Jerusalem\", dit qu'ils lui manquent tous les deux. Aucune de ces missions ne le montre.")},
    {"table": {"head": [two("Mission", "Mission"), two("Part", "Partie"), two("Jack's role", "Rôle de Jack")], "rows": [
        M("The Wheel", EP1,
          "Rides in the back of the family wagon through Big Valley and talks with his parents about King Arthur and the Knights of the Round Table. The family heads for Strawberry.",
          "Voyage à l'arrière du chariot familial dans Big Valley et parle avec ses parents du roi Arthur et des chevaliers de la Table ronde. La famille prend la direction de Strawberry."),
        M("Simple Pleasures", EP1,
          "Arrives at Pronghorn Ranch from Strawberry with Abigail. He joins John and the ranch hand Abe at the cattle shed, then helps clean the horse stables. When John mentions Bronte's mansion, Jack does not remember it.",
          "Arrive de Strawberry à Pronghorn Ranch avec Abigail. Il rejoint John et le garçon de ferme Abe à l'étable, puis aide à nettoyer les écuries. Quand John évoque le manoir de Bronte, Jack ne s'en souvient pas."),
        M("Farming, For Beginners", EP1,
          "Has breakfast with his parents on the morning Abigail announces her job at the doctor's office.",
          "Prend le petit déjeuner avec ses parents le matin où Abigail annonce son travail chez le médecin."),
        M("Fatherhood, For Beginners", EP1,
          "Rides along Little Creek River with John on a pony lent by Duncan Geddes. John challenges him to a race back home. The pony can buck him off unless the player tells him to speed up.",
          "Chevauche le long de la Little Creek River avec John, sur un poney prêté par Duncan Geddes. John le défie à la course jusqu'à la maison. Le poney peut le désarçonner si le joueur ne lui dit pas d'accélérer."),
        M("Fatherhood, For Idiots", EP1,
          "Witnesses his parents' argument over a bank loan. He rides with John to Strawberry, learning to drive the wagon on the way, and drives it back. When three riders chase them, he hides while John kills them. On seeing the bodies he breaks down in tears, and back at the cabin he pushes past his mother.",
          "Assiste à la dispute de ses parents au sujet d'un prêt bancaire. Il part avec John à Strawberry, apprend en chemin à conduire le chariot, puis le ramène lui-même. Quand trois cavaliers les prennent en chasse, il se cache pendant que John les abat. À la vue des corps, il fond en larmes, et de retour à la cabane, il bouscule sa mère."),
        M("Old Habits", EP1,
          "Listed by the wiki. The mission page does not mention him.",
          "Citée par le wiki. La page de la mission ne le mentionne pas."),
        M("Jim Milton Rides, Again?", EP1,
          "Listed by the wiki. The mission page does not mention him.",
          "Citée par le wiki. La page de la mission ne le mentionne pas."),
        M("Motherhood", EP1,
          "Absent: Abigail has left Pronghorn Ranch with him. The foreman Tom Dickens tells John he saw the two of them leave with their luggage.",
          "Absent : Abigail a quitté Pronghorn Ranch avec lui. Le contremaître Tom Dickens dit à John les avoir vus partir tous les deux avec leurs bagages."),
        M("The Best of Women", EP2,
          "A single cutscene: he arrives at Beecher's Hope with Abigail after months apart from John.",
          "Une seule cinématique : il arrive à Beecher's Hope avec Abigail après des mois loin de John."),
        M("Trying Again", EP2,
          "Mission giver. John finds him reading and playing with the dog Rufus and takes him fishing. On the way, Jack recalls fishing with Arthur. Rufus is bitten by a snake, John sucks out the venom, and his parents reassure Jack that the dog will recover in a few days.",
          "Donneur de mission. John le trouve en train de lire et de jouer avec le chien Rufus, et l'emmène pêcher. En chemin, Jack se souvient de sa partie de pêche avec Arthur. Rufus se fait mordre par un serpent, John aspire le venin, et ses parents lui assurent que le chien sera remis dans quelques jours."),
        M("A Really Big Bastard", EP2,
          "Calls his parents out to the porch when Sadie arrives at the ranch.",
          "Appelle ses parents sur le perron quand Sadie arrive au ranch."),
        M("American Venom", EP2,
          "Before the mission, he reads a story about the knight Sir Galsworthy aloud to Abigail and [[uncle|Uncle]]. Abigail calls him and Uncle outside when John comes back. In the credits he watches his parents' wedding beside Uncle, sees [[charles-smith|Charles]] off, plays with Rufus, and brushes a horse with John in the corral while Ross and [[archer-fordham|Archer Fordham]] watch through binoculars.",
          "Avant la mission, il lit à voix haute à Abigail et à [[uncle|Uncle]] une histoire du chevalier Sir Galsworthy. Abigail l'appelle dehors avec Uncle au retour de John. Pendant le générique, il assiste au mariage de ses parents à côté d'Uncle, voit partir [[charles-smith|Charles]], joue avec Rufus et brosse un cheval avec John dans l'enclos, sous les jumelles de Ross et d'[[archer-fordham|Archer Fordham]]."),
    ]}},
    {"h4": two("Red Dead Redemption 2: other activities", "Red Dead Redemption 2 : autres activités")},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Jack's role", "Rôle de Jack")], "rows": [
        M("Errand Boy", C2,
          "Two requests for Arthur: a Penny Dreadful book, which he brings up during \"A Fisher of Men\" and which is found in one of five places (Osman Grove, Clawson's Rest, the abandoned schoolhouse in Pleasance, Downes Ranch or Lake Don Julio), and, once that mission is done, a thimble to replace one of Abigail's that he lost.",
          "Deux demandes adressées à Arthur : un roman Penny Dreadful, qu'il évoque pendant \"A Fisher of Men\" et qui se trouve à l'un de cinq endroits (Osman Grove, Clawson's Rest, l'école abandonnée de Pleasance, Downes Ranch ou le lac Don Julio), puis, une fois cette mission terminée, un dé à coudre pour remplacer celui d'Abigail, qu'il a perdu."),
    ]}},
    {"h4": two("Red Dead Redemption, 1911", "Red Dead Redemption, 1911")},
    {"p": two("The Bureau holds Jack and Abigail through most of the game. Until John returns home in Act III, Jack is only mentioned: in John's conversations, and in Bill's taunt during the chase in \"An Appointed Time\". He gives four of the Beecher's Hope missions, the \"Jack Marston\" strand that runs from \"John Marston and Son\" to \"The Last Enemy That Shall Be Destroyed\".",
              "Le Bureau retient Jack et Abigail pendant l'essentiel du jeu. Jusqu'au retour de John chez lui, à l'acte III, Jack n'est que cité : dans les conversations de John, et dans la provocation que lui lance Bill pendant la poursuite de \"An Appointed Time\". Il donne quatre des missions de Beecher's Hope, la série \"Jack Marston\", de \"John Marston and Son\" à \"The Last Enemy That Shall Be Destroyed\".")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Jack's role", "Rôle de Jack")], "rows": [
        M("The Outlaw's Return", A3,
          "First mission in which he appears on screen. He greets John at the ranch and apologizes for the lost chickens and cattle. The next morning he rides with him to MacFarlane's Ranch in Hennigan's Stead, asking many questions. [[bonnie-macfarlane|Bonnie MacFarlane]] helps them get the cattle off her ranch. Jack leads the herd home; when rustlers attack, John tells him to stay back and kills them.",
          "Première mission où il apparaît à l'écran. Il accueille John au ranch et s'excuse pour les poules et le bétail perdus. Le lendemain matin, il l'accompagne au MacFarlane's Ranch, à Hennigan's Stead, en le pressant de questions. [[bonnie-macfarlane|Bonnie MacFarlane]] les aide à sortir le bétail de son ranch. Jack mène le troupeau jusqu'à la maison ; quand des voleurs de bétail attaquent, John lui dit de rester en arrière et les abat."),
        M("John Marston and Son", A3,
          "Mission giver. John finds him reading an adventure novel under a tree and takes him elk hunting with Rufus. Jack shoots and skins an elk himself, and they sell the meat at Manzanita Post.",
          "Donneur de mission. John le trouve en train de lire un roman d'aventures sous un arbre et l'emmène chasser le wapiti avec Rufus. Jack abat et dépèce lui-même un wapiti, et ils vendent la viande à Manzanita Post."),
        M("Wolves, Dogs and Sons", A3,
          "Mission giver. John finds him practicing with a Repeater Carbine and offers help, which Jack refuses. They ride out with Rufus and kill a wolf pack threatening the herd. On the way, Jack asks about John's father and about Uncle, and whether John was a murderer.",
          "Donneur de mission. John le surprend à s'entraîner avec une Repeater Carbine et lui propose son aide, que Jack refuse. Ils partent avec Rufus et abattent une meute de loups qui menace le troupeau. En chemin, Jack interroge John sur son propre père, sur Uncle, et lui demande s'il a été un meurtrier."),
        M("Spare the Love, Spoil the Child", A3,
          "Mission giver. He goes alone to hunt a grizzly. Uncle alerts John, who follows Rufus to Nekoti Rock and finds Jack injured and his horse killed. John kills the bear and takes him home; they argue on the way.",
          "Donneur de mission. Il part seul chasser un grizzly. Uncle prévient John, qui suit Rufus jusqu'à Nekoti Rock et trouve Jack blessé, son cheval tué. John abat l'ours et le ramène à la maison ; ils se disputent en chemin."),
        M("The Last Enemy That Shall Be Destroyed", A3,
          "Mission giver. John finds him working a lathe in the barn. When the army arrives, John sends him into the house, but Jack comes out with a rifle and fights beside John and Uncle. After Uncle's death he runs to the barn with Abigail and rides off with her. The player then controls him on the ride back, and they find John dead.",
          "Donneur de mission. John le trouve au tour à bois, dans la grange. À l'arrivée de l'armée, John l'envoie dans la maison, mais Jack ressort avec un fusil et se bat aux côtés de John et d'Uncle. Après la mort d'Uncle, il court jusqu'à la grange avec Abigail et s'enfuit à cheval avec elle. Le joueur le dirige ensuite sur le chemin du retour, et ils trouvent John mort."),
    ]}},
    {"h4": two("Red Dead Redemption, 1914", "Red Dead Redemption, 1914")},
    {"p": two("Jack is the player character from here on (see Skills for what carries over from John).",
              "Jack est désormais le personnage jouable (voir les compétences pour ce qu'il reprend de John).")},
    {"table": {"head": [two("Mission", "Mission"), two("Part", "Partie"), two("Jack's role", "Rôle de Jack")], "rows": [
        M("Remember My Family", E14,
          "Protagonist. A stranger mission given by the Bureau agent Howard Sawicki in Blackwater, who tells him Ross has retired near Lake Don Julio. Ross's wife Emily sends Jack to his brother Phillip, near Rio del Toro, who points him down the San Luis River. Jack confronts Ross there and kills him in a duel. The credits follow.",
          "Protagoniste. Mission d'inconnu confiée à Blackwater par l'agent du Bureau Howard Sawicki, qui lui apprend que Ross a pris sa retraite près du lac Don Julio. Emily, la femme de Ross, envoie Jack vers son beau-frère Phillip, près de Rio del Toro, qui l'oriente vers l'aval de la San Luis River. Jack y affronte Ross et le tue en duel. Le générique suit."),
    ]}},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors continuité)")},
    {"p": two("Undead Nightmare is set outside the series' continuity. Both missions listed by the wiki take place at Beecher's Hope.",
              "Undead Nightmare se déroule hors de la continuité de la série. Les deux missions retenues par le wiki se passent à Beecher's Hope.")},
    {"table": {"head": [two("Mission", "Mission"), two("Game", "Jeu"), two("Jack's role", "Rôle de Jack")], "rows": [
        M("Love in the Time of Plague", UNM,
          "His book, he tells John at home, is about an Aztec curse that spreads a plague. During the night, after the undead Uncle bites Abigail, he rushes to help her and is infected in turn. He chases Rufus before John hogties him and leaves him in the bedroom with Abigail and some food.",
          "À la maison, il explique à John que son livre parle d'une malédiction aztèque qui répand une épidémie. Dans la nuit, après qu'Uncle, devenu mort-vivant, a mordu Abigail, il se précipite à son secours et se fait contaminer à son tour. Il court après Rufus avant que John ne le ligote et le laisse dans la chambre avec Abigail et de quoi manger."),
        M("On a Pale Horse", UNM,
          "John finds his wife and son cured, though still bound, and hugs them.",
          "John retrouve sa femme et son fils guéris, quoique toujours attachés, et les serre dans ses bras."),
    ]}},
    # ---------------------------------------------------------- notable kills
    {"h3": two("Notable people Jack kills", "Personnages notables tués par Jack")},
    {"p": two("The Red Dead Wiki credits Jack with a single murder. In \"The Last Enemy That Shall Be Destroyed\", he also fires on the unnamed soldiers attacking the ranch, and the mission page notes that he shoots one of their horses. In \"Remember My Family\", the player can also kill Ross's wife and brother; killing them costs honor unless Jack wears the bandana, and killing Ross restores the honor lost.",
              "Le Red Dead Wiki n'attribue qu'un seul meurtre à Jack. Dans \"The Last Enemy That Shall Be Destroyed\", il tire aussi sur les soldats anonymes qui attaquent le ranch, et la page de la mission précise qu'il abat l'un de leurs chevaux. Dans \"Remember My Family\", le joueur peut également tuer la femme et le frère de Ross ; cela coûte de l'honneur, sauf si Jack porte le bandana, et la mort de Ross rend l'honneur perdu.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K("[[edgar-ross|Edgar Ross]]", "Remember My Family",
          "Storyline. Shot in a duel on the bank of the San Luis River, in 1914. The duel requires a lethal shot: aiming at Ross's gun or arm loses it.",
          "Histoire. Abattu en duel sur la rive de la San Luis River, en 1914. Le duel exige un tir mortel : viser l'arme ou le bras de Ross le fait perdre."),
        K("Emily Ross", "Remember My Family",
          "Optional. Can be killed after she tells Jack where her husband is.",
          "Facultatif. Peut être tuée après avoir indiqué à Jack où se trouve son mari."),
        K("Phillip Ross", "Remember My Family",
          "Optional. Can be killed after he points Jack down the river.",
          "Facultatif. Peut être tué après avoir orienté Jack vers l'aval de la rivière."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Mission lines are checked against the mission transcripts of the Red Dead Wiki. The free-roam lines of 1914 and the camp lines of Red Dead Redemption 2 come from the wiki's quote list, which names no mission for them. The wiki has no transcript of Jack's lines in Undead Nightmare. Lines already quoted under Personality do not appear again here.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Celles de l'exploration libre de 1914 et du camp dans Red Dead Redemption 2 proviennent de la liste de citations du wiki, qui ne leur rattache aucune mission. Le wiki ne propose aucune transcription des répliques de Jack dans Undead Nightmare. Les répliques déjà citées dans la rubrique Personnalité ne sont pas reprises ici.")},
    {"h4": two("Red Dead Redemption 2, chapter 2", "Red Dead Redemption 2, chapitre 2")},
    {"quotes": [
        {"q": two("I forgot a story book there. We left so quick.", "I forgot a story book there. We left so quick."),
         "src": two("A Fisher of Men (RDR2, chapter 2), to Arthur, who asks why he wants to go back to the camp near Blackwater",
                    "A Fisher of Men (RDR2, chapitre 2), à Arthur, qui lui demande pourquoi il veut retourner au camp près de Blackwater. Traduction : « J'ai oublié un livre d'histoires là-bas. On est partis tellement vite. »")},
        {"q": two("Why did you lie about where Uncle Dutch is?", "Why did you lie about where Uncle Dutch is?"),
         "src": two("A Fisher of Men (RDR2, chapter 2), to Arthur, on the ride back after Milton and Ross leave",
                    "A Fisher of Men (RDR2, chapitre 2), à Arthur, sur le chemin du retour, après le départ de Milton et de Ross. Traduction : « Pourquoi tu as menti sur l'endroit où est oncle Dutch ? »")},
        {"q": two("Great, we caught a fish... And I made you this necklace.", "Great, we caught a fish... And I made you this necklace."),
         "src": two("A Fisher of Men (RDR2, chapter 2), to Abigail, who asks how the boys got on",
                    "A Fisher of Men (RDR2, chapitre 2), à Abigail, qui demande comment s'est passée la sortie. Traduction : « Super, on a attrapé un poisson... Et je t'ai fait ce collier. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"quotes": [
        {"q": two("So... with the red dragon dead... and Princess Brea rescued, Sir Galsworthy put down his sword and-a took up his plough... He became the greatest apple farmer in the kingdom.", "So... with the red dragon dead... and Princess Brea rescued, Sir Galsworthy put down his sword and-a took up his plough... He became the greatest apple farmer in the kingdom."),
         "src": two("American Venom (RDR2, epilogue 2), reading aloud to Abigail and Uncle as John comes into the house",
                    "American Venom (RDR2, épilogue 2), en lisant à voix haute pour Abigail et Uncle, au moment où John entre dans la maison. Traduction : « Alors... une fois le dragon rouge mort... et la princesse Brea délivrée, Sir Galsworthy posa son épée et prit sa charrue... Il devint le plus grand cultivateur de pommes du royaume. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, camp lines", "Red Dead Redemption 2, répliques au camp")},
    {"p": two("The quote list sorts these lines by Jack's age and by the player's action, without naming a mission. The first is said by the child of 1899 when Arthur antagonizes him, the second when Arthur defuses the exchange; the last is said by the boy of 1907.",
              "La liste de citations classe ces répliques selon l'âge de Jack et l'action du joueur, sans préciser la mission. La première est prononcée par l'enfant de 1899 quand Arthur le provoque, la deuxième quand Arthur apaise l'échange ; la dernière par le garçon de 1907.")},
    {"quotes": [
        {"q": two("I hate you, Uncle Arthur!", "I hate you, Uncle Arthur!"),
         "src": two("Red Dead Redemption 2, 1899, when antagonized by Arthur (quote list of the wiki)",
                    "Red Dead Redemption 2, 1899, quand Arthur le provoque (liste de citations du wiki). Traduction : « Je te déteste, oncle Arthur ! »")},
        {"q": two("Arthur's being mean to me!", "Arthur's being mean to me!"),
         "src": two("Red Dead Redemption 2, 1899, when Arthur defuses (quote list of the wiki)",
                    "Red Dead Redemption 2, 1899, quand Arthur apaise la situation (liste de citations du wiki). Traduction : « Arthur est méchant avec moi ! »")},
        {"q": two("You okay sir? You don't normally dress like that.", "You okay sir? You don't normally dress like that."),
         "src": two("Red Dead Redemption 2, 1907, when John wears an unusual outfit (quote list of the wiki)",
                    "Red Dead Redemption 2, 1907, quand John porte une tenue inhabituelle (liste de citations du wiki). Traduction : « Ça va, monsieur ? D'habitude, vous ne vous habillez pas comme ça. »")},
    ]},
    {"h4": two("Red Dead Redemption, Act III", "Red Dead Redemption, acte III")},
    {"quotes": [
        {"q": two("Coyotes ate all the chickens and, poachers took the cattle. I tried, father, I tried.", "Coyotes ate all the chickens and, poachers took the cattle. I tried, father, I tried."),
         "src": two("The Outlaw's Return (RDR1, Act III), to John, who asks how he has been",
                    "The Outlaw's Return (RDR1, acte III), à John, qui lui demande comment il va. Traduction : « Les coyotes ont mangé toutes les poules et les braconniers ont pris le bétail. J'ai essayé, père, j'ai essayé. »")},
        {"q": two("I don't often get a chance to ask them. Was it a gentleman's complaint? What do they call it, the morning drip?", "I don't often get a chance to ask them. Was it a gentleman's complaint? What do they call it, the morning drip?"),
         "src": two("The Outlaw's Return (RDR1, Act III), to John, who says he was sick and that Jack has a lot of questions; Jack adds that Uncle told him about it",
                    "The Outlaw's Return (RDR1, acte III), à John, qui dit avoir été malade et trouve que Jack pose beaucoup de questions ; Jack ajoute que c'est Uncle qui lui en a parlé. Traduction : « Je n'ai pas souvent l'occasion d'en poser. C'était une maladie de gentleman ? Comment on appelle ça, la goutte du matin ? »")},
        {"q": two("I've never seen you herd anything, Pa. Apart from the odd pack of drunks.", "I've never seen you herd anything, Pa. Apart from the odd pack of drunks."),
         "src": two("The Outlaw's Return (RDR1, Act III), to John, who asks whether he is ready to learn about herding cattle",
                    "The Outlaw's Return (RDR1, acte III), à John, qui lui demande s'il est prêt à apprendre à mener le bétail. Traduction : « Je ne t'ai jamais vu mener quoi que ce soit, papa. À part une bande d'ivrognes de temps en temps. »")},
        {"q": two("No, I'm fine-I'm fine. I-I wasn't scared. Honest.", "No, I'm fine-I'm fine. I-I wasn't scared. Honest."),
         "src": two("The Outlaw's Return (RDR1, Act III), to John, after the rustlers are killed",
                    "The Outlaw's Return (RDR1, acte III), à John, après la mort des voleurs de bétail. Traduction : « Non, ça va, ça va. Je... je n'ai pas eu peur. C'est vrai. »")},
        {"q": two("It's an adventure, sir. Set out in the West, and it tells this amazing story about how people killed the savage redskins and how this man, this brave man, hunts the man who killed his father.", "It's an adventure, sir. Set out in the West, and it tells this amazing story about how people killed the savage redskins and how this man, this brave man, hunts the man who killed his father."),
         "src": two("John Marston and Son (RDR1, Act III), to John, who asks what his book is about",
                    "John Marston and Son (RDR1, acte III), à John, qui lui demande de quoi parle son livre. Traduction : « C'est une aventure, monsieur. Ça se passe dans l'Ouest, et ça raconte une histoire incroyable, comment des gens ont tué les sauvages peaux-rouges et comment un homme, un homme courageux, traque celui qui a tué son père. »")},
        {"q": two("Taller than a boy being taken from his home and locked up in a dungeon?", "Taller than a boy being taken from his home and locked up in a dungeon?"),
         "src": two("John Marston and Son (RDR1, Act III), to John, who calls his story of a girl raised by wolves a tall yarn",
                    "John Marston and Son (RDR1, acte III), à John, qui trouve invraisemblable son histoire de fillette élevée par des loups. Traduction : « Plus invraisemblable qu'un garçon arraché à sa maison et enfermé dans un cachot ? »")},
        {"q": two("What do you mean, \"get\" old. You are old.", "What do you mean, \"get\" old. You are old."),
         "src": two("John Marston and Son (RDR1, Act III), to John, who hopes Jack will look after his parents when they get old",
                    "John Marston and Son (RDR1, acte III), à John, qui espère que Jack s'occupera de ses parents quand ils seront vieux. Traduction : « Comment ça, \"quand\" vous serez vieux ? Tu es vieux. »")},
        {"q": two("You'll show me and you'll just...run off again or something. It's better I teach myself.", "You'll show me and you'll just...run off again or something. It's better I teach myself."),
         "src": two("Wolves, Dogs and Sons (RDR1, Act III), to John, who offers to show him how to hold the rifle",
                    "Wolves, Dogs and Sons (RDR1, acte III), à John, qui propose de lui montrer comment tenir le fusil. Traduction : « Tu vas me montrer et puis tu vas... repartir, ou je ne sais quoi. Mieux vaut que j'apprenne tout seul. »")},
        {"q": two("Just imagine it though! John and Jack Marston, most wanted men in the West!", "Just imagine it though! John and Jack Marston, most wanted men in the West!"),
         "src": two("Wolves, Dogs and Sons (RDR1, Act III), to John, on the ride home; John asks about his mother, then tells him he lives in a dream world",
                    "Wolves, Dogs and Sons (RDR1, acte III), à John, sur le chemin du retour ; John lui demande ce qu'il fait de sa mère, puis lui dit qu'il vit dans un monde de rêve. Traduction : « Imagine un peu ! John et Jack Marston, les hommes les plus recherchés de l'Ouest ! »")},
        {"q": two("I was trying to prove myself.", "I was trying to prove myself."),
         "src": two("Spare the Love, Spoil the Child (RDR1, Act III), to John, who answers \"Prove what? By gettin' yourself killed?\" on the ride home",
                    "Spare the Love, Spoil the Child (RDR1, acte III), à John, qui répond \"Prove what? By gettin' yourself killed?\" (prouver quoi ? en te faisant tuer ?), sur le chemin du retour. Traduction : « J'essayais de faire mes preuves. »")},
        {"q": two("Yeah, maybe I'll do that...\"The day John Marston stopped shooting.\"", "Yeah, maybe I'll do that...\"The day John Marston stopped shooting.\""),
         "src": two("The Last Enemy That Shall Be Destroyed (RDR1, Act III), to John, who suggests he put it in one of his books if he ever finds something he does not like shooting",
                    "The Last Enemy That Shall Be Destroyed (RDR1, acte III), à John, qui lui suggère de le mettre dans un de ses livres s'il trouve un jour quelque chose qu'il n'aime pas abattre. Traduction : « Ouais, je le ferai peut-être... \"Le jour où John Marston arrêta de tirer.\" »")},
        {"q": two("No! Uncle! Please! Oh my God! They killed him!", "No! Uncle! Please! Oh my God! They killed him!"),
         "src": two("The Last Enemy That Shall Be Destroyed (RDR1, Act III), on the porch, when Uncle dies",
                    "The Last Enemy That Shall Be Destroyed (RDR1, acte III), sur le perron, à la mort d'Uncle. Traduction : « Non ! Uncle ! Je vous en prie ! Mon Dieu ! Ils l'ont tué ! »")},
        {"q": two("You're coming with us, Pa.", "You're coming with us, Pa."),
         "src": two("The Last Enemy That Shall Be Destroyed (RDR1, Act III), to John, in the barn, as John puts him on a horse",
                    "The Last Enemy That Shall Be Destroyed (RDR1, acte III), à John, dans la grange, quand John le met à cheval. Traduction : « Tu viens avec nous, papa. »")},
    ]},
    {"h4": two("Red Dead Redemption, 1914", "Red Dead Redemption, 1914")},
    {"quotes": [
        {"q": two("Did you work with a man named Edgar Ross? I have something for him.", "Did you work with a man named Edgar Ross? I have something for him."),
         "src": two("Remember My Family (RDR1, 1914), to Howard Sawicki at Blackwater",
                    "Remember My Family (RDR1, 1914), à Howard Sawicki, à Blackwater. Traduction : « Vous avez travaillé avec un certain Edgar Ross ? J'ai quelque chose pour lui. »")},
        {"q": two("I sure will, ma'am. And don't worry about a thing. I'm sure your husband will be just fine.", "I sure will, ma'am. And don't worry about a thing. I'm sure your husband will be just fine."),
         "src": two("Remember My Family (RDR1, 1914), to Emily Ross, who tells him to be careful crossing the river",
                    "Remember My Family (RDR1, 1914), à Emily Ross, qui lui conseille la prudence pour traverser la rivière. Traduction : « Promis, madame. Et ne vous inquiétez de rien. Je suis sûr que votre mari s'en sortira très bien. »")},
        {"q": two("Forgive me for startling you sir, I have a message for you. My name is Jack Marston, you knew my father.", "Forgive me for startling you sir, I have a message for you. My name is Jack Marston, you knew my father."),
         "src": two("Remember My Family (RDR1, 1914), to Edgar Ross, on the bank of the San Luis River",
                    "Remember My Family (RDR1, 1914), à Edgar Ross, sur la rive de la San Luis River. Traduction : « Pardonnez-moi de vous surprendre, monsieur, j'ai un message pour vous. Je m'appelle Jack Marston, vous avez connu mon père. »")},
        {"q": two("You sent him to do your dirty work, then you shot him like a dog!", "You sent him to do your dirty work, then you shot him like a dog!"),
         "src": two("Remember My Family (RDR1, 1914), to Ross, after Ross says John killed himself with the life he lived and Jack insists he saw him do it",
                    "Remember My Family (RDR1, 1914), à Ross, après que celui-ci a affirmé que John s'était tué lui-même par la vie qu'il menait et que Jack a répété l'avoir vu tirer. Traduction : « Vous l'avez envoyé faire votre sale boulot, et ensuite vous l'avez abattu comme un chien ! »")},
        {"q": two("I ain't going nowhere old man!", "I ain't going nowhere old man!"),
         "src": two("Remember My Family (RDR1, 1914), to Ross, who orders him to leave before he kills him too",
                    "Remember My Family (RDR1, 1914), à Ross, qui lui ordonne de partir avant qu'il ne le tue lui aussi. Traduction : « Je ne vais nulle part, vieillard ! »")},
    ]},
    {"h4": two("Red Dead Redemption, 1914, free roam", "Red Dead Redemption, 1914, exploration libre")},
    {"p": two("The quote list groups Jack's free-roam lines by situation. A selection follows, with the situation the list gives.",
              "La liste de citations regroupe les répliques de Jack en exploration libre selon la situation. En voici une sélection, avec la situation indiquée par la liste.")},
    {"quotes": [
        {"q": two("I'm John Marston's boy!", "I'm John Marston's boy!"),
         "src": two("Red Dead Redemption, in combat (quote list of the wiki)",
                    "Red Dead Redemption, en combat (liste de citations du wiki). Traduction : « Je suis le fils de John Marston ! »")},
        {"q": two("Somebody taught me well!", "Somebody taught me well!"),
         "src": two("Red Dead Redemption, in combat (quote list of the wiki)",
                    "Red Dead Redemption, en combat (liste de citations du wiki). Traduction : « Quelqu'un m'a bien appris ! »")},
        {"q": two("My pa knew Landon Ricketts, friend!", "My pa knew Landon Ricketts, friend!"),
         "src": two("Red Dead Redemption, in combat (quote list of the wiki); [[landon-ricketts|Landon Ricketts]] is also named in one of his Dead Eye lines",
                    "Red Dead Redemption, en combat (liste de citations du wiki) ; [[landon-ricketts|Landon Ricketts]] est aussi cité dans l'une de ses répliques en Dead Eye. Traduction : « Mon père connaissait Landon Ricketts, l'ami ! »")},
        {"q": two("I guess I am my father's son.", "I guess I am my father's son."),
         "src": two("Red Dead Redemption, when slitting the throat of a hogtied person (quote list of the wiki)",
                    "Red Dead Redemption, en égorgeant une personne ligotée (liste de citations du wiki). Traduction : « Faut croire que je suis bien le fils de mon père. »")},
        {"q": two("I did it, Pa.", "I did it, Pa."),
         "src": two("Red Dead Redemption, after killing a bear for the first time (quote list of the wiki)",
                    "Red Dead Redemption, après avoir tué un ours pour la première fois (liste de citations du wiki). Traduction : « J'ai réussi, papa. »")},
        {"q": two("Just like you showed me, pa!", "Just like you showed me, pa!"),
         "src": two("Red Dead Redemption, when skinning an animal (quote list of the wiki); the \"John Marston and Son\" page links it to that mission",
                    "Red Dead Redemption, en dépeçant un animal (liste de citations du wiki) ; la page de \"John Marston and Son\" la rattache à cette mission. Traduction : « Exactement comme tu me l'as montré, papa ! »")},
        {"q": two("Sorry, friend. My father was a killer, nothing more!", "Sorry, friend. My father was a killer, nothing more!"),
         "src": two("Red Dead Redemption, when stealing a horse or a cart (quote list of the wiki)",
                    "Red Dead Redemption, en volant un cheval ou une charrette (liste de citations du wiki). Traduction : « Désolé, l'ami. Mon père n'était qu'un tueur, rien de plus ! »")},
        {"q": two("That old feller Uncle used to told me stories like that.", "That old feller Uncle used to told me stories like that."),
         "src": two("Red Dead Redemption, after a campfire story (quote list of the wiki, grammar as listed)",
                    "Red Dead Redemption, après une histoire au coin du feu (liste de citations du wiki, syntaxe d'origine). Traduction : « Le vieux Uncle me racontait des histoires comme ça. »")},
        {"q": two("The only thing worse than a lawman is a government's man!", "The only thing worse than a lawman is a government's man!"),
         "src": two("Red Dead Redemption, to a lawman, with low honor (quote list of the wiki)",
                    "Red Dead Redemption, à un représentant de la loi, avec un honneur bas (liste de citations du wiki). Traduction : « La seule chose pire qu'un homme de loi, c'est un homme du gouvernement ! »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Across the series", "Dans toute la série")},
    {"ul": [
        two("According to the Red Dead Wiki, Jack and Edgar Ross are the only central characters of the series who appear in all four periods: 1899 and 1907 in Red Dead Redemption 2, 1911 and 1914 in Red Dead Redemption. Ross dies in 1914; Jack is alive at the end of every period.",
            "Selon le Red Dead Wiki, Jack et Edgar Ross sont les seuls personnages centraux de la série présents aux quatre époques : 1899 et 1907 dans Red Dead Redemption 2, 1911 et 1914 dans Red Dead Redemption. Ross meurt en 1914 ; Jack est en vie à la fin de chacune d'elles."),
        two("On screen, Jack and Ross meet only twice, in \"A Fisher of Men\" and \"Remember My Family\". Both meetings take place by a river, and Ross carries a long gun both times: a rifle in the 1899 transcript, a duck-hunting shotgun in 1914.",
            "À l'écran, Jack et Ross ne se croisent que deux fois, dans \"A Fisher of Men\" et \"Remember My Family\". Les deux rencontres ont lieu au bord d'une rivière, et Ross porte chaque fois une arme d'épaule : un fusil dans la transcription de 1899, un fusil de chasse au canard en 1914."),
        two("The Red Dead Wiki ranks Jack as the third youngest playable character in a Rockstar game, after Jimmy Hopkins in Bully and Red Harlow at the start of Red Dead Revolver.",
            "Le Red Dead Wiki classe Jack au troisième rang des plus jeunes personnages jouables d'un jeu Rockstar, après Jimmy Hopkins dans Bully et Red Harlow au début de Red Dead Revolver."),
    ]},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"ul": [
        two("In \"A Fisher of Men\", the horse cannot crash into obstacles while Jack is on board, and riding off a cliff fails the mission at once with the message \"Jack was frightened\". Crossing the deeper part of the Dakota River with him also fails the mission.",
            "Dans \"A Fisher of Men\", le cheval ne peut pas heurter d'obstacle tant que Jack est en selle, et sauter d'une falaise fait échouer la mission aussitôt, avec le message \"Jack was frightened\" (Jack a eu peur). Traverser la partie profonde de la Dakota River avec lui fait aussi échouer la mission."),
        two("If Arthur has already bought Jack new clothes, Jack thanks him for the new pants during the fishing trip. Started at night, the mission opens with Arthur promising to take him fishing in the morning.",
            "Si Arthur a déjà acheté de nouveaux vêtements à Jack, celui-ci le remercie pour son pantalon neuf pendant la partie de pêche. Lancée de nuit, la mission s'ouvre sur Arthur qui lui promet de l'emmener pêcher le lendemain matin."),
        two("On the ride back from Bronte's mansion, Jack says the Italian words for slipper and horse incorrectly: \"pantafòla\" for \"pantòfola\", and a Spanish-sounding pronunciation for \"cavallo\".",
            "Sur le chemin du retour depuis le manoir de Bronte, Jack prononce mal les mots italiens pour pantoufle et cheval : \"pantafòla\" au lieu de \"pantòfola\", et \"cavallo\" à l'espagnole."),
        two("In \"Horsemen, Apocalypses\", throwing dynamite or a fire bottle at the start of the playable section fails the mission because it frightens Jack.",
            "Dans \"Horsemen, Apocalypses\", lancer de la dynamite ou une bouteille incendiaire au début de la phase jouable fait échouer la mission, parce que Jack prend peur."),
        two("In \"Fatherhood, For Idiots\", the mission page notes that one of the three pursuers shoots John if he tries to hogtie them all. If the player still manages it, the cutscene is unchanged and Jack is just as shaken.",
            "Dans \"Fatherhood, For Idiots\", la page de la mission précise que l'un des trois poursuivants abat John s'il tente de les ligoter tous. Si le joueur y parvient malgré tout, la cinématique reste la même et Jack est tout aussi bouleversé."),
        two("Started at night, \"Trying Again\" opens with John knocking on the bathroom door to ask Jack whether he wants to do something the next day.",
            "Lancée de nuit, \"Trying Again\" s'ouvre sur John qui frappe à la porte de la salle de bain pour demander à Jack s'il veut faire quelque chose le lendemain."),
        two("The story Jack reads aloud before \"American Venom\", about the knight Sir Galsworthy, comes from a Frank Heck dime novel.",
            "L'histoire du chevalier Sir Galsworthy que Jack lit à voix haute avant \"American Venom\" est tirée d'un roman à quatre sous de Frank Heck."),
        two("According to the Red Dead Wiki, a random audio glitch in Red Dead Redemption 2 gave the player character a voice very close to Josh Blaylock's Jack. Players speculated about it until the lines were traced to an ordinary non-player character also voiced by Blaylock.",
            "Selon le Red Dead Wiki, un bug sonore aléatoire de Red Dead Redemption 2 prêtait au personnage du joueur une voix très proche de celle de Josh Blaylock dans le rôle de Jack. Les joueurs ont fait des hypothèses jusqu'à ce que ces répliques soient attribuées à un simple personnage non jouable, doublé lui aussi par Blaylock."),
    ]},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("In \"Wolves, Dogs and Sons\", John tells Jack that his tense back is making the rifle jump. [[landon-ricketts|Landon Ricketts]] gives John the same advice in \"The Gunslinger's Tragedy\".",
            "Dans \"Wolves, Dogs and Sons\", John explique à Jack que son dos trop raide fait sauter le fusil. [[landon-ricketts|Landon Ricketts]] donne le même conseil à John dans \"The Gunslinger's Tragedy\"."),
        two("In the opening scene of \"Wolves, Dogs and Sons\", Jack cocks the hammer of his Repeater Carbine by hand, as on the real Spencer carbine. In normal gameplay, the weapon fires by working the lever alone.",
            "Dans la scène d'ouverture de \"Wolves, Dogs and Sons\", Jack arme à la main le chien de sa Repeater Carbine, comme sur la véritable carabine Spencer. En jeu, l'arme tire par le seul jeu du levier."),
        two("Jack's horse in \"Spare the Love, Spoil the Child\" uses the model of a cut \"Dead Horse\". Looking at Jack resting on his bed after the mission shows the bloodied model used in it.",
            "Le cheval de Jack dans \"Spare the Love, Spoil the Child\" reprend le modèle d'un \"Dead Horse\" coupé du jeu. Si l'on regarde Jack allongé sur son lit après la mission, il porte encore le modèle ensanglanté utilisé dans celle-ci."),
        two("Flying machines, which Jack and John discuss at the start of \"The Last Enemy That Shall Be Destroyed\", are also the subject of Jenny's conversation with the preacher on the train in \"Exodus in America\", the game's first mission.",
            "Les machines volantes, dont Jack et John parlent au début de \"The Last Enemy That Shall Be Destroyed\", sont aussi le sujet de la conversation de Jenny avec le prédicateur dans le train, dans \"Exodus in America\", la première mission du jeu."),
        two("Left idle, the playable Jack talks to himself, sometimes addressing his dead father.",
            "Laissé sans consigne, Jack jouable se parle à lui-même, et s'adresse parfois à son père mort."),
        two("In \"Remember My Family\", Jack tells Ross he saw him kill John. In \"The Last Enemy That Shall Be Destroyed\", he was riding away when the shots were fired and found the body afterwards.",
            "Dans \"Remember My Family\", Jack affirme à Ross qu'il l'a vu tuer John. Dans \"The Last Enemy That Shall Be Destroyed\", il s'éloignait à cheval au moment des coups de feu et n'a trouvé le corps qu'ensuite."),
        two("\"Remember My Family\" is the only stranger mission John cannot complete. With \"I Know You\", it is one of two stranger missions that cover all three regions: it starts in West Elizabeth, passes through New Austin and ends in Nuevo Paraíso.",
            "\"Remember My Family\" est la seule mission d'inconnu que John ne peut pas accomplir. Avec \"I Know You\", c'est l'une des deux missions d'inconnus qui traversent les trois régions : elle commence en West Elizabeth, passe par New Austin et s'achève au Nuevo Paraíso."),
        two("Aiming at Ross, his wife or his brother through a rifle scope fails \"Remember My Family\", even without firing. After the credits, Ross's body can be looted for 400 dollars.",
            "Viser Ross, sa femme ou son frère dans une lunette de fusil fait échouer \"Remember My Family\", même sans tirer. Après le générique, on peut récupérer 400 dollars sur le corps de Ross."),
        two("The epilogue outfit shows a bandolier even if the player has not bought it. It stays cosmetic until it is bought, according to the French Red Dead Wiki.",
            "La tenue de l'épilogue affiche une cartouchière même si le joueur ne l'a pas achetée. Selon le Red Dead Wiki français, elle reste purement décorative tant qu'elle n'est pas achetée."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors continuité)")},
    {"ul": [
        two("Rufus appears only once in Undead Nightmare, in the background of \"Love in the Time of Plague\", when Jack chases him.",
            "Rufus n'apparaît qu'une fois dans Undead Nightmare, à l'arrière-plan de \"Love in the Time of Plague\", quand Jack lui court après."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Jack became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. The pack added 15 characters from the story, as well as Poker, Liar's Dice, horse races and the Stronghold mode. Players select Jack in the Redemption section of the Outfitter, alongside [[john-marston|John]], [[abigail-marston|Abigail]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[leigh-johnson|Leigh Johnson]], [[luisa-fortuna|Luisa Fortuna]], [[nigel-west-dickens|Nigel West Dickens]] and [[seth-briars|Seth Briars]].",
              "Jack devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. Ce pack ajoute 15 personnages de l'histoire, ainsi que le poker, le poker menteur, des courses de chevaux et le mode Stronghold. On choisit Jack dans la section Redemption de l'Outfitter, aux côtés de [[john-marston|John]], d'[[abigail-marston|Abigail]], de [[bonnie-macfarlane|Bonnie MacFarlane]], de [[leigh-johnson|Leigh Johnson]], de [[luisa-fortuna|Luisa Fortuna]], de [[nigel-west-dickens|Nigel West Dickens]] et de [[seth-briars|Seth Briars]].")},
    {"p": two("The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the Jack model is not available in them.",
              "Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle de Jack n'y est donc pas disponible.")},
    {"h4": two("Achievements and trophies", "Succès et trophées")},
    {"p": two("Two achievements of Red Dead Redemption are tied to the missions that make Jack the protagonist. \"Into the Sunset\" is awarded for completing \"The Last Enemy That Shall Be Destroyed\", the mission that unlocks Jack as the player character. \"Nurture or Nature?\", an achievement worth 50 Gamerscore (a gold trophy on PlayStation), is awarded for completing \"Remember My Family\". As a stranger mission, \"Remember My Family\" also counts towards \"Strange Things Are Afoot\" and \"People are Still Strange\".",
              "Deux succès de Red Dead Redemption sont liés aux missions qui font de Jack le protagoniste. \"Into the Sunset\" récompense \"The Last Enemy That Shall Be Destroyed\", la mission qui rend Jack jouable. \"Nurture or Nature?\", un succès de 50 points sur Xbox (trophée d'or sur PlayStation), récompense \"Remember My Family\". En tant que mission d'inconnu, \"Remember My Family\" compte aussi pour \"Strange Things Are Afoot\" et \"People are Still Strange\".")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("For Red Dead Redemption 2, Rockstar released official artwork of Jack. On September 6, 2018, Rockstar posted his portrait and character description on Twitter, in a series covering the members of the gang, and The Hollywood Reporter reproduced the series the next day. In the composite image of the 23 gang members, Jack stands in the front row, between Abigail and Strauss.",
              "Pour Red Dead Redemption 2, Rockstar a publié une illustration officielle de Jack. Le 6 septembre 2018, Rockstar publie sur Twitter son portrait et sa description, dans une série consacrée aux membres du gang, et The Hollywood Reporter reprend la série le lendemain. Sur l'image qui réunit les 23 membres du gang, Jack figure au premier rang, entre Abigail et Strauss.")},
    {"h4": two("In other Rockstar games", "Dans d'autres jeux Rockstar")},
    {"p": two("Grand Theft Auto V (2013), another Rockstar game, refers to Jack and to Red Dead Redemption: a book titled \"Red Dead\" by a J. Marston can be found in Franklin's house.",
              "Grand Theft Auto V (2013), un autre jeu Rockstar, fait référence à Jack et à Red Dead Redemption : un livre intitulé \"Red Dead\", signé J. Marston, se trouve dans la maison de Franklin.")},
]
