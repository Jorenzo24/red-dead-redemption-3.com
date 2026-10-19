"""Uncle, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad
cov/uncle/, cov/uncle/m/ and cov/uncle/wkC/):
- Red Dead Wiki EN "Uncle" (Mission Appearances, Quotes incl. Multiplayer and the RDR2
  quote list, Trivia, Gallery captions) and FR "L'Oncle" (wkC/fr.txt: Apparitions dans les
  missions, Anecdotes).
- Mission pages: Outlaws from the West; Old Friends; The Aftermath of Genesis; Eastward
  Bound; Polite Society, Valentine Style; A Strange Kindness; An Honest Mistake; Blood
  Feuds, Ancient and Modern; The Battle of Shady Belle; Fleeting Joy; That's Murfree
  Country; Money Lending and Other Sins VI & VII; My Last Boy; Our Best Selves; Home of
  the Gentry?; Bare Knuckle Friendships; Home Improvement for Beginners; The Tool Box; A
  New Jerusalem; A Quick Favor for an Old Friend; Uncle's Bad Day; A Really Big Bastard; A
  New Future Imagined; American Venom; Ending Credits; companion activities High and Low
  Finance and Go Rustling (Uncle). RDR1: This is Armadillo, USA; The Outlaw's Return; By
  Sweat and Toil; A Continual Feast; Wolves, Dogs and Sons; Spare the Love, Spoil the
  Child; The Last Enemy That Shall Be Destroyed. Undead Nightmare: Love in the Time of
  Plague; On a Pale Horse. DLC page Myths and Mavericks; Outfitter page.
- Transcripts "/dialogues": Old Friends; The Aftermath of Genesis; Eastward Bound; Polite
  Society, Valentine Style; Home Improvement for Beginners (table transcript); American
  Venom; This is Armadillo, USA; The Outlaw's Return; By Sweat and Toil; A Continual Feast;
  Wolves, Dogs and Sons; Spare the Love, Spoil the Child; The Last Enemy That Shall Be
  Destroyed. Every mission quote is checked word for word against one of them, except
  two lines quoted on mission pages (A New Jerusalem, A Quick Favor for an Old Friend: no
  transcript on the wiki)
  and the free-roam and multiplayer lines, which come from the quote list. Uncle's last
  words follow the transcript ("You take Jack and Abi... take them and..."), not the
  shorter wording of the character page.
- Real world: Myths and Mavericks Bonus Pack (Engadget, July 27, 2011; released free on
  September 13, 2011), as in javier_C; RDR1 ports (PS4 and Switch, August 17, 2023; PC,
  October 29, 2024) without multiplayer, as in bill_C / jack_C; Rockstar tweet "Uncle" of
  September 6, 2018 reproduced by The Hollywood Reporter on September 7, 2018
  (../abigail/fc/thr_descriptions.txt; the description itself is NOT quoted here, part B);
  composite of the 23 gang members (Wikipedia caption, m/wp_list.txt: front row "Pearson,
  Uncle, Swanson"). Third trailer (May 2, 2018) campfire still: the trailer number comes only from
  the wiki file name "RDR 2 Trailer 3 Bon Fire" (caption names Javier, Uncle, Arthur), said in the text.
Ownership (FIX_RULES), left to other parts: background (Ohio, father, Jeb, parents' death,
wives, Africa, Timbuktu, rancher claim, pimp, Canada bank job, introducing Abigail), the
Keane's Saloon brawl as a story event, the Skinner torture details and recovery, the
wedding and Charles's departure, burial and epitaph (A); official descriptions (THR, Complete
Official Guide), names and nicknames ("Uncle", "Old Man", "one-shot kid", "JM" greetings),
lumbago as a trait, laziness, hidden Dutch conversation, Charles joke scene, British grudge,
camp banjo and drinking routine, smoking at the dinner table, silo ladder and horseshoes
at Beecher's Hope, appearance (beard, rhinophyma, union suit, shirts, glove, hat and its
Levi Simon model, blue bandana), weapons (Schofield, Cattleman, custom shotgun) and horses
(Nell II, Nell IV), "I'll outlive you all" (B); Spider Madison, John O'Creagh, James McBride,
O'Creagh's singing in "Uncle's Bad Day" and his "let's hide in here" line in "An Honest
Mistake", O'Creagh's Run, Madison's 2005 short, the Wishbone/Rawhide likeness, the unused
Riggs Station cutscene (cut content) (D).
Quotes: each line in ONE place. Removed after fact-check (19 Oct 2026): the two lumbago lines
("Oh, I got lumbago..." and "I'm real sick, John. Lumbago...", both in B "In his own words").
"Is that any way to greet an old friend?" and "He loves me really..." live HERE only (B Arthur
entry points here); "I love it, I truly love it." lives HERE (B paraphrases); "camp rat" lives in B
Names only (the Aftermath row and the caption avoid it). Multiplayer: all seven taunts of the
wiki quote list (coverage #14).
Fact-check fixes (19 Oct 2026): chapters of Eastward Bound (1), The Battle of Shady Belle (3) and
That's Murfree Country (5); saloon encounter Valentine as Arthur / Blackwater as John in 1907, the
player's honor; Honest Mistake wagon believed unguarded, Cornwall's discovered later; departure not
shown, Karen gone too. Trivia cut because told elsewhere: store purchases, "good friends" (A),
Go Rustling split (A; night-only in B Skills), Gainful Employment scolding (B Sadie), idle spot (B Skills),
lumbago not fatal (B Personality), Hosea "go bother Uncle" (B Hosea), Jack and prostitutes (B Jack).
No kills table: the character page lists no murders for Uncle. The only named victim in his
missions, Cooperforth in "An Honest Mistake", is credited to "either Arthur or Uncle" by the
mission page, so it is not attributed.
Excluded: "John suggests Uncle has illegitimate children" (Wolves: kept to B, Names, with the
"Folks always did" exchange); John's campfire line about "an old drunk" ("most likely
referring to Uncle": speculation); the "lookout" foreshadowing and "last member of the gang to
die" claim (interpretation, and false: Charles, Sadie and others outlive him); "Uncle can be
viewed as seeking redemption" (interpretation); the High and Low Finance foreshadowing (the line
itself is kept); the Undead Nightmare "developer's choice" and "the family chose not to bury
him" explanations (speculation); the UN appearance paragraph's "suggesting he infected another
victim" (speculation); FR anecdotes "probablement buvaient ensemble" and "similitudes avec
l'Irlandais" (interpretation); "Uncle can be tracked using Eagle Eye" (generic mechanic);
Outlaw's Return unlock bug and grave-standing glitch (no value); Red Dead Online: no outfit,
item or reference to Uncle found on the wiki, so nothing is claimed.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
EP1 = two("Epilogue 1: Pronghorn Ranch", "Épilogue 1 : Pronghorn Ranch")
EP2 = two("Epilogue 2: Beecher's Hope", "Épilogue 2 : Beecher's Hope")
A1 = two("Act I: New Austin", "Acte I : New Austin")
A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
UNM = two("Undead Nightmare", "Undead Nightmare")
FREE = two("Free roam", "Exploration libre")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 23 story missions of Red Dead Redemption 2 for Uncle, from the flight through the snow to the last mission before the credits, plus two companion activities. It lists five missions of Red Dead Redemption and one of Undead Nightmare. The French edition counts 19 missions for Red Dead Redemption 2: it leaves out \"The Aftermath of Genesis\", \"Money Lending and Other Sins VII\", \"Home of the Gentry?\" and \"Bare Knuckle Friendships\". For Red Dead Redemption, it adds \"This is Armadillo, USA\", in which Uncle is only mentioned. Several missions on the English list do not show him in their mission page or transcript; the tables say so case by case. The table for Red Dead Redemption also adds \"Wolves, Dogs and Sons\", whose transcript gives a conversation about him.",
              "Le Red Dead Wiki anglais recense pour Uncle 23 missions principales de Red Dead Redemption 2, de la fuite dans la neige jusqu'à la dernière mission avant le générique, et deux activités de compagnon. Il retient cinq missions de Red Dead Redemption et une d'Undead Nightmare. L'édition française compte 19 missions pour Red Dead Redemption 2 : elle omet \"The Aftermath of Genesis\", \"Money Lending and Other Sins VII\", \"Home of the Gentry?\" et \"Bare Knuckle Friendships\". Pour Red Dead Redemption, elle ajoute \"This is Armadillo, USA\", où Uncle n'est que cité. Plusieurs missions de la liste anglaise ne le montrent ni dans leur page ni dans leur transcription : les tableaux le signalent au cas par cas. Le tableau consacré à Red Dead Redemption ajoute aussi \"Wolves, Dogs and Sons\", dont la transcription rapporte une conversation à son sujet.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 to 6", "Red Dead Redemption 2, chapitres 1 à 6")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Uncle's role", "Rôle d'Uncle")], "rows": [
        M("Outlaws from the West", C1,
          "Listed by the wiki for the gang's flight into the mountains. Neither the mission page nor the transcript names him.",
          "Citée par le wiki pour la fuite du gang dans les montagnes. Ni la page de la mission ni la transcription ne le nomment."),
        M("Old Friends", C1,
          "Comes out of the cabin with [[bill-williamson|Bill]] when [[arthur-morgan|Arthur]] brings back [[kieran-duffy|Kieran Duffy]]. [[dutch-van-der-linde|Dutch]] orders the two of them to tie the prisoner up and let him go hungry.",
          "Sort de la cabane avec [[bill-williamson|Bill]] quand [[arthur-morgan|Arthur]] ramène [[kieran-duffy|Kieran Duffy]]. [[dutch-van-der-linde|Dutch]] leur ordonne d'attacher le prisonnier et de le laisser avoir faim."),
        M("The Aftermath of Genesis", C1,
          "Is in [[simon-pearson|Pearson]]'s kitchen when Arthur and [[charles-smith|Charles]] bring in the deer. Arthur needles him, then sends him out of the cabin (their exchange is under Quotes).",
          "Se trouve dans la cuisine de [[simon-pearson|Pearson]] quand Arthur et [[charles-smith|Charles]] rapportent les cerfs. Arthur le rudoie, puis le met à la porte de la cabane (leur échange figure dans les citations)."),
        M("Eastward Bound", C1,
          "Sits drinking with [[tilly-jackson|Tilly]] when the gang reaches Horseshoe Overlook and gets up, bottle in hand, as Dutch arrives. In his speech, Dutch singles out Uncle and Reverend [[orville-swanson|Swanson]] (see Relationships, Dutch).",
          "Boit avec [[tilly-jackson|Tilly]] à l'arrivée du gang à Horseshoe Overlook et se lève, bouteille à la main, quand Dutch approche. Dans son discours, Dutch prend à partie Uncle et le révérend [[orville-swanson|Swanson]] (voir Relations, Dutch)."),
        M("Polite Society, Valentine Style", C2,
          "Mission giver. Arthur wakes him and they drive a wagon to Valentine with [[karen-jones|Karen]], Tilly and [[mary-beth-gaskill|Mary-Beth]]. He shops at the general store, shares a bottle with Arthur outside, and goes back to camp with the women.",
          "Donneur de mission. Arthur le réveille et ils conduisent un chariot jusqu'à Valentine avec [[karen-jones|Karen]], Tilly et [[mary-beth-gaskill|Mary-Beth]]. Il fait ses courses au magasin général, partage une bouteille avec Arthur devant la boutique et rentre au camp avec les femmes."),
        M("A Strange Kindness", C2,
          "Listed by the wiki. The mission page does not mention him.",
          "Citée par le wiki. La page de la mission ne le mentionne pas."),
        M("An Honest Mistake", C3,
          "Mission giver, with [[molly-oshea|Molly O'Shea]]. He brings Arthur a tip about a wagon he believes unguarded and rides out with Arthur, Charles and Bill. The wagon turns out to belong to Cornwall Kerosene & Tar; the four hide in a barn, then split up in the woods, Uncle staying with Arthur.",
          "Donneur de mission, avec [[molly-oshea|Molly O'Shea]]. Il apporte à Arthur un tuyau sur un chariot qu'il croit sans escorte et part avec Arthur, Charles et Bill. Le chariot se révèle appartenir à Cornwall Kerosene & Tar ; les quatre hommes se cachent dans une grange, puis se séparent dans les bois, Uncle restant avec Arthur."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Listed by the wiki. The mission page does not mention him.",
          "Citée par le wiki. La page de la mission ne le mentionne pas."),
        M("The Battle of Shady Belle", C3,
          "Listed by the wiki for the gang's move to Shady Belle. The mission page does not mention him.",
          "Citée par le wiki pour l'installation du gang à Shady Belle. La page de la mission ne le mentionne pas."),
        M("Fleeting Joy", C5,
          "Listed by the wiki for the gang's stay at Lakay. The mission page does not mention him.",
          "Citée par le wiki pour le séjour du gang à Lakay. La page de la mission ne le mentionne pas."),
        M("That's Murfree Country", C5,
          "Rides into the new camp at Beaver Hollow with a drunk Molly O'Shea.",
          "Arrive au nouveau camp de Beaver Hollow avec Molly O'Shea, ivre."),
        M("Money Lending and Other Sins VII", C6,
          "Listed by the wiki. The mission page does not mention him.",
          "Citée par le wiki. La page de la mission ne le mentionne pas."),
        M("My Last Boy", C6,
          "Last mission in which he is at the camp. Afterwards he is gone, and in \"Our Best Selves\" Dutch tells Arthur that Uncle, Pearson and Mary-Beth have run off; Karen is gone as well. His departure is not shown.",
          "Dernière mission où il se trouve au camp. Ensuite, il n'y est plus, et dans \"Our Best Selves\", Dutch annonce à Arthur qu'Uncle, Pearson et Mary-Beth se sont enfuis ; Karen est partie elle aussi. Son départ n'est pas montré."),
    ]}},
    {"h4": two("Red Dead Redemption 2: companion activities and encounters", "Red Dead Redemption 2 : activités de compagnon et rencontres")},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Uncle's role", "Rôle d'Uncle")], "rows": [
        M("High and Low Finance", C4,
          "Bank robbery available only in the Special and Ultimate editions. Uncle rides with Arthur and Charles to the Bank of Rhodes, whose wall they blow open with dynamite to rob the safes.",
          "Braquage réservé aux éditions Spéciale et Ultime. Uncle accompagne Arthur et Charles à la Bank of Rhodes, dont ils font sauter le mur à la dynamite pour vider les coffres."),
        M("Go Rustling (Uncle)", C4,
          "Offered by Uncle at night. He and Arthur steal cattle from Hill Haven Ranch, whose owner Squears is drunk, and sell them to the Davies twins at Clemens Cove for 100 dollars.",
          "Proposée par Uncle la nuit. Arthur et lui volent du bétail à Hill Haven Ranch, dont le propriétaire, Squears, est ivre, et le vendent 100 dollars aux jumeaux Davies à Clemens Cove."),
        M("Saloon encounter", FREE,
          "A man threatens Uncle outside a saloon, in Valentine (as Arthur) or in Blackwater (as John, in 1907). Stepping in raises the player's honor.",
          "Un homme menace Uncle devant un saloon, à Valentine (avec Arthur) ou à Blackwater (avec John, en 1907). Intervenir fait monter l'honneur du joueur."),
    ]}},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"table": {"head": [two("Mission", "Mission"), two("Part", "Partie"), two("Uncle's role", "Rôle d'Uncle")], "rows": [
        M("Home of the Gentry?", EP1,
          "Runs into [[john-marston|John]] in a Blackwater street after John buys Beecher's Hope, and rides out to the ranch with him.",
          "Tombe sur [[john-marston|John]] dans une rue de Blackwater après l'achat de Beecher's Hope, et l'accompagne jusqu'au ranch."),
        M("Bare Knuckle Friendships", EP2,
          "Mission giver. He tells John that Charles is alive in Saint Denis and takes the train there with him. They find Charles at a fight in the slums, and Uncle leaves to run errands.",
          "Donneur de mission. Il apprend à John que Charles est vivant à Saint-Denis et s'y rend avec lui en train. Ils retrouvent Charles à un combat dans les bas quartiers, et Uncle part faire des courses."),
        M("Home Improvement for Beginners", EP2,
          "Mission giver. At the campfire he mocks the shack, then directs John and Charles as they pull it down with ropes and horses. He sends John to Albert Cakes in Blackwater for a pre-cut house.",
          "Donneur de mission. Près du feu, il se moque de la cabane, puis dirige John et Charles qui l'abattent à l'aide de cordes et de chevaux. Il envoie John chez Albert Cakes, à Blackwater, pour une maison en kit."),
        M("The Tool Box", EP2,
          "Asleep at Beecher's Hope when John and Charles bring the lumber back. He helps John gather the planks.",
          "Dort à Beecher's Hope quand John et Charles rapportent le bois. Il aide John à rassembler les planches."),
        M("A New Jerusalem", EP2,
          "Mission giver. Pleading his lumbago, he gives orders while John and Charles assemble the house, then toasts the finished home.",
          "Donneur de mission. Invoquant son lumbago, il donne les ordres pendant que John et Charles montent la maison, puis porte un toast à la maison terminée."),
        M("A Quick Favor for an Old Friend", EP2,
          "Mission giver. He suggests a pre-cut barn, goes with John to order one from Albert Cakes, then irritates the banker Ansel Atherton. [[sadie-adler|Sadie]] joins them outside the bank.",
          "Donneur de mission. Il propose une grange en kit, accompagne John pour la commander à Albert Cakes, puis agace le banquier Ansel Atherton. [[sadie-adler|Sadie]] les rejoint devant la banque."),
        M("Uncle's Bad Day", EP2,
          "Mission giver. After a night of celebration, the Skinner Brothers carry him off. John and Charles find him at their camp, free him and bring him back to the ranch.",
          "Donneur de mission. Après une nuit de fête, les Skinner Brothers l'enlèvent. John et Charles le retrouvent dans leur camp, le libèrent et le ramènent au ranch."),
        M("A Really Big Bastard", EP2,
          "Listed by the wiki. The mission page does not mention him.",
          "Citée par le wiki. La page de la mission ne le mentionne pas."),
        M("A New Future Imagined", EP2,
          "Opens with [[abigail-marston|Abigail]] scolding him over his work, before the Geddes brothers deliver furniture to the ranch.",
          "S'ouvre sur [[abigail-marston|Abigail]] qui lui reproche son manque d'ardeur au travail, avant que les frères Geddes ne livrent des meubles au ranch."),
        M("American Venom", EP2,
          "Before the mission, he listens to [[jack-marston|Jack]] reading aloud. When John leaves with Sadie and Charles, he agrees to keep an eye on the place. In the credits he plays the banjo at the wedding and stays at the ranch with the family.",
          "Avant la mission, il écoute [[jack-marston|Jack]] lire à voix haute. Quand John part avec Sadie et Charles, il accepte de surveiller le ranch. Pendant le générique, il joue du banjo au mariage et reste au ranch avec la famille."),
    ]}},
    {"h4": two("Red Dead Redemption, 1911", "Red Dead Redemption, 1911")},
    {"p": two("In Red Dead Redemption, Uncle has a mission strand of his own at Beecher's Hope: \"By Sweat and Toil\", then \"A Continual Feast\". Both lead, with the Abigail and Jack strands, to \"The Last Enemy That Shall Be Destroyed\".",
              "Dans Red Dead Redemption, Uncle a sa propre série de missions à Beecher's Hope : \"By Sweat and Toil\", puis \"A Continual Feast\". Toutes deux mènent, avec les séries d'Abigail et de Jack, à \"The Last Enemy That Shall Be Destroyed\".")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Uncle's role", "Rôle d'Uncle")], "rows": [
        M("This is Armadillo, USA", A1,
          "Mentioned only. When [[bonnie-macfarlane|Bonnie MacFarlane]] asks who is looking after John's farm, John names Uncle and says he is not really his uncle.",
          "Seulement cité. Quand [[bonnie-macfarlane|Bonnie MacFarlane]] demande qui s'occupe de la ferme de John, celui-ci nomme Uncle et précise qu'il n'est pas vraiment son oncle."),
        M("The Outlaw's Return", A3,
          "Greets John on his return. The livestock is gone, and Uncle defends himself before any blame.",
          "Accueille John à son retour. Le bétail a disparu, et Uncle se défend avant même d'être accusé."),
        M("By Sweat and Toil", A3,
          "Mission giver. John wakes him and they drive the cattle to pasture. A train robbery stampedes the herd; Uncle and John bring it under control and find new grazing on the plains.",
          "Donneur de mission. John le réveille et ils mènent le bétail au pâturage. L'attaque d'un train affole le troupeau ; Uncle et John le reprennent en main et trouvent un nouveau pâturage dans la plaine."),
        M("A Continual Feast", A3,
          "Mission giver. He spots wild mustangs through a spyglass and rides out with John, who breaks three of them. They bring the horses back to the ranch pen.",
          "Donneur de mission. Il repère des mustangs sauvages à la longue-vue et part avec John, qui en dresse trois. Ils ramènent les chevaux dans l'enclos du ranch."),
        M("Wolves, Dogs and Sons", A3,
          "Not on the wiki's list. On the ride, Jack asks John whether Uncle is really his uncle and why everyone calls him that.",
          "Absente de la liste du wiki. En chemin, Jack demande à John si Uncle est vraiment son oncle et pourquoi tout le monde l'appelle ainsi."),
        M("Spare the Love, Spoil the Child", A3,
          "Alerts John that Jack has gone up to the pass after a grizzly, and says he tried to stop him.",
          "Prévient John que Jack est monté vers le col pour traquer un grizzly, et affirme avoir tenté de l'en empêcher."),
        M("The Last Enemy That Shall Be Destroyed", A3,
          "Sees the soldiers and agents coming through his spyglass and calls John. He fights beside John, is shot on the porch and dies there.",
          "Repère à la longue-vue les soldats et les agents qui approchent et appelle John. Il se bat à ses côtés, est touché sur le perron et y meurt."),
    ]}},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors continuité)")},
    {"p": two("Undead Nightmare is set outside the series' continuity. Uncle appears in a single mission of the expansion, its first one.",
              "Undead Nightmare se déroule hors de la continuité de la série. Uncle n'apparaît que dans une mission de l'extension, la toute première.")},
    {"table": {"head": [two("Mission", "Mission"), two("Game", "Jeu"), two("Uncle's role", "Rôle d'Uncle")], "rows": [
        M("Love in the Time of Plague", UNM,
          "Fails to come home on a stormy night. He later bursts into the bedroom as one of the undead, bites Abigail outside, and John shoots him in the head.",
          "Ne rentre pas un soir d'orage. Il surgit plus tard dans la chambre, devenu mort-vivant, mord Abigail dehors, et John l'abat d'une balle dans la tête."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Mission lines are checked against the mission transcripts of the Red Dead Wiki; two lines from missions without a transcript come from the wiki's mission pages, and the free-roam and multiplayer lines come from the wiki's quote list. Uncle has no spoken lines in Undead Nightmare. Lines already quoted under Personality and Relationships do not appear again here.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki ; deux répliques de missions sans transcription proviennent des pages de mission du wiki, et les répliques d'exploration libre et du multijoueur, de sa liste de citations. Uncle ne prononce aucune réplique dans Undead Nightmare. Les répliques déjà citées dans les rubriques Personnalité et Relations ne sont pas reprises ici.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 and 2", "Red Dead Redemption 2, chapitres 1 et 2")},
    {"quotes": [
        {"q": two("Is that any way to greet an old friend? I feel like we haven't spoken for days.", "Is that any way to greet an old friend? I feel like we haven't spoken for days."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), to Arthur, who greets him with an insult in Pearson's kitchen",
                    "The Aftermath of Genesis (RDR2, chapitre 1), à Arthur, qui l'accueille d'une insulte dans la cuisine de Pearson. Traduction : « C'est une façon d'accueillir un vieil ami ? J'ai l'impression qu'on ne s'est pas parlé depuis des jours. »")},
        {"q": two("He loves me really. It's his sad way of showing affection.", "He loves me really. It's his sad way of showing affection."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), after Arthur says he does his utmost to avoid him",
                    "The Aftermath of Genesis (RDR2, chapitre 1), après qu'Arthur a dit faire tout son possible pour l'éviter. Traduction : « Il m'adore, en vrai. C'est sa triste façon de montrer son affection. »")},
        {"q": two("It's a strange world we live in, Arthur Morgan.", "It's a strange world we live in, Arthur Morgan."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), to Arthur, who points out that he gets to think all day while the others steal and fight",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à Arthur, qui lui fait remarquer qu'il passe ses journées à réfléchir pendant que les autres volent et se battent. Traduction : « C'est un drôle de monde que le nôtre, Arthur Morgan. »")},
        {"q": two("Alright! Here we are, just like I said. The cultural center of civilization. Man at his finest.", "Alright! Here we are, just like I said. The cultural center of civilization. Man at his finest."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), on arriving in Valentine",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à l'arrivée à Valentine. Traduction : « Et voilà ! Nous y sommes, comme promis. Le centre culturel de la civilisation. L'homme dans toute sa splendeur. »")},
        {"q": two("It's a funny world. This time in my career... I pictured myself being married to an heiress.", "It's a funny world. This time in my career... I pictured myself being married to an heiress."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), to Arthur, on the bench outside the general store",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à Arthur, sur le banc devant le magasin général. Traduction : « Drôle de monde. À ce stade de ma carrière... je me voyais marié à une héritière. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"quotes": [
        {"q": two("Feels like old times... It's good to have the old gang back together again.", "Feels like old times... It's good to have the old gang back together again."),
         "src": two("Home Improvement for Beginners (RDR2, epilogue 2), as John joins him and Charles at the campfire",
                    "Home Improvement for Beginners (RDR2, épilogue 2), quand John le rejoint avec Charles près du feu. Traduction : « On se croirait au bon vieux temps... Ça fait plaisir de voir la vieille bande réunie. »")},
        {"q": two("I mean look at you... look at this place... your dream home. I've had better nightmares than this dream.", "I mean look at you... look at this place... your dream home. I've had better nightmares than this dream."),
         "src": two("Home Improvement for Beginners (RDR2, epilogue 2), to John, about the shack",
                    "Home Improvement for Beginners (RDR2, épilogue 2), à John, à propos de la cabane. Traduction : « Non mais regarde-toi... regarde cet endroit... la maison de tes rêves. J'ai fait des cauchemars plus réussis que ce rêve-là. »")},
        {"q": two("Now we head into town... buy ourselves a house right out of a book... same as if it were a bicycle.", "Now we head into town... buy ourselves a house right out of a book... same as if it were a bicycle."),
         "src": two("Home Improvement for Beginners (RDR2, epilogue 2), to John, once the shack is down",
                    "Home Improvement for Beginners (RDR2, épilogue 2), à John, une fois la cabane à terre. Traduction : « Maintenant, on file en ville... on s'achète une maison sur catalogue... comme on achèterait une bicyclette. »")},
        {"q": two("Gentlemen... to this happy home. At least till this fool gets his woman back.", "Gentlemen... to this happy home. At least till this fool gets his woman back."),
         "src": two("A New Jerusalem (RDR2, epilogue 2), toasting John and Charles (mission page of the wiki)",
                    "A New Jerusalem (RDR2, épilogue 2), en trinquant avec John et Charles (page de la mission sur le wiki). Traduction : « Messieurs... à ce foyer heureux. Du moins jusqu'à ce que cet idiot récupère sa femme. »")},
        {"q": two("Oh, you don't build a barn, dumbass. What do you think this is, 1785? You buy one pre-cut, just like the house.", "Oh, you don't build a barn, dumbass. What do you think this is, 1785? You buy one pre-cut, just like the house."),
         "src": two("A Quick Favor for an Old Friend (RDR2, epilogue 2), to John, who expects a barn to take six months to build (mission page of the wiki)",
                    "A Quick Favor for an Old Friend (RDR2, épilogue 2), à John, qui pense qu'une grange demande six mois de travail (page de la mission sur le wiki). Traduction : « Oh, une grange, ça ne se construit pas, crétin. Tu te crois en 1785 ? On l'achète en kit, comme la maison. »")},
        {"q": two("I love it, I truly love it. Abigail, dear, what's for dinner?", "I love it, I truly love it. Abigail, dear, what's for dinner?"),
         "src": two("American Venom (RDR2, epilogue 2), after Jack finishes reading his story aloud",
                    "American Venom (RDR2, épilogue 2), quand Jack termine la lecture de son histoire. Traduction : « J'adore, j'adore vraiment. Abigail, ma chère, qu'est-ce qu'on mange ce soir ? »")},
    ]},
    {"h4": two("Red Dead Redemption 2, free roam", "Red Dead Redemption 2, exploration libre")},
    {"p": two("The quote list sorts these lines by the player's action and names the character addressed, without a mission. The first two answer Arthur in 1899, the last two answer John in 1907.",
              "La liste de citations classe ces répliques selon l'action du joueur et la personne visée, sans préciser de mission. Les deux premières répondent à Arthur en 1899, les deux dernières à John en 1907.")},
    {"quotes": [
        {"q": two("You're interrupting my beauty rest.", "You're interrupting my beauty rest."),
         "src": two("Red Dead Redemption 2, to Arthur, as he goes back to sleep (quote list of the wiki)",
                    "Red Dead Redemption 2, à Arthur, en se rendormant (liste de citations du wiki). Traduction : « Tu interromps ma sieste de beauté. »")},
        {"q": two("Hard to take you seriously, Arthur, with all that blood on you.", "Hard to take you seriously, Arthur, with all that blood on you."),
         "src": two("Red Dead Redemption 2, to a bloodstained Arthur who antagonizes him (quote list of the wiki)",
                    "Red Dead Redemption 2, à Arthur, couvert de sang, qui le provoque (liste de citations du wiki). Traduction : « Difficile de te prendre au sérieux, Arthur, avec tout ce sang sur toi. »")},
        {"q": two("John, we're... we're settled down now. Take the bandana off and stop insulting me!", "John, we're... we're settled down now. Take the bandana off and stop insulting me!"),
         "src": two("Red Dead Redemption 2, to John wearing a bandana (quote list of the wiki)",
                    "Red Dead Redemption 2, à John, qui porte un bandana (liste de citations du wiki). Traduction : « John, on est... on est rangés maintenant. Enlève ce bandana et arrête de m'insulter ! »")},
        {"q": two("Good lord, let an old man sleep.", "Good lord, let an old man sleep."),
         "src": two("Red Dead Redemption 2, to John, when woken up (quote list of the wiki)",
                    "Red Dead Redemption 2, à John, quand on le réveille (liste de citations du wiki). Traduction : « Bon sang, laisse donc dormir un vieil homme. »")},
    ]},
    {"h4": two("Red Dead Redemption, Act III", "Red Dead Redemption, acte III")},
    {"quotes": [
        {"q": two("That's a nice way to greet somebody. Why don't I gets a warm and tender embrace?", "That's a nice way to greet somebody. Why don't I gets a warm and tender embrace?"),
         "src": two("The Outlaw's Return (RDR1, Act III), to John, who has just counted four mouths to feed and no cattle",
                    "The Outlaw's Return (RDR1, acte III), à John, qui vient de compter quatre bouches à nourrir et plus de bétail. Traduction : « Jolie façon d'accueillir les gens. Pourquoi j'ai pas droit à une étreinte chaleureuse et tendre, moi ? »")},
        {"q": two("I did...I did my best. Thing is, there was too many of 'em... I thought you was dead... I wasn't drinking...", "I did...I did my best. Thing is, there was too many of 'em... I thought you was dead... I wasn't drinking..."),
         "src": two("The Outlaw's Return (RDR1, Act III), to John, who reminds him he was meant to look after the place",
                    "The Outlaw's Return (RDR1, acte III), à John, qui lui rappelle qu'il devait s'occuper de la propriété. Traduction : « J'ai fait... j'ai fait de mon mieux. Le problème, c'est qu'ils étaient trop nombreux... Je te croyais mort... Je buvais pas... »")},
        {"q": two("It's easy to pick on the elderly. It's easy but it ain't dignified.", "It's easy to pick on the elderly. It's easy but it ain't dignified."),
         "src": two("By Sweat and Toil (RDR1, Act III), to John, who asks when he meant to take the cattle to pasture",
                    "By Sweat and Toil (RDR1, acte III), à John, qui lui demande quand il comptait mener le bétail au pâturage. Traduction : « C'est facile de s'en prendre aux vieux. C'est facile, mais c'est pas digne. »")},
        {"q": two("Stay away from trouble, John! You don't need it!", "Stay away from trouble, John! You don't need it!"),
         "src": two("By Sweat and Toil (RDR1, Act III), as bandits attack a train near the herd",
                    "By Sweat and Toil (RDR1, acte III), quand des bandits attaquent un train près du troupeau. Traduction : « Ne te mêle pas de ça, John ! T'en as pas besoin ! »")},
        {"q": two("No thanks, you got your pound of flesh from me today.", "No thanks, you got your pound of flesh from me today."),
         "src": two("By Sweat and Toil (RDR1, Act III), when John tells him to watch the herd. The phrase comes from Shakespeare's The Merchant of Venice",
                    "By Sweat and Toil (RDR1, acte III), quand John lui dit de garder le troupeau. L'expression vient du Marchand de Venise de Shakespeare. Traduction : « Non merci, tu as eu ta livre de chair pour aujourd'hui. »")},
        {"q": two("That tone of voice ain't so becoming on you. Makes you seem all pent up and angry, like some Blackwater would-be business tycoon with a bad case of hemorrhoids.", "That tone of voice ain't so becoming on you. Makes you seem all pent up and angry, like some Blackwater would-be business tycoon with a bad case of hemorrhoids."),
         "src": two("A Continual Feast (RDR1, Act III), to John, who mocks his idea of catching mustangs",
                    "A Continual Feast (RDR1, acte III), à John, qui se moque de son idée d'attraper des mustangs. Traduction : « Ce ton ne te va pas très bien. Tu as l'air tout crispé et en colère, comme un apprenti magnat des affaires de Blackwater avec une sale crise d'hémorroïdes. »")},
        {"q": two("That weren't half bad for a couple of old reprobates.", "That weren't half bad for a couple of old reprobates."),
         "src": two("A Continual Feast (RDR1, Act III), to John, after he breaks three horses",
                    "A Continual Feast (RDR1, acte III), à John, après le dressage de trois chevaux. Traduction : « Pas si mal, pour deux vieilles canailles. »")},
        {"q": two("John, come here. John, come here quick! Take a look at that.", "John, come here. John, come here quick! Take a look at that."),
         "src": two("The Last Enemy That Shall Be Destroyed (RDR1, Act III), at his spyglass, as the army approaches the ranch",
                    "The Last Enemy That Shall Be Destroyed (RDR1, acte III), à la longue-vue, quand l'armée approche du ranch. Traduction : « John, viens voir. John, viens vite ! Regarde-moi ça. »")},
        {"q": two("Ain't time, John. I ain't gonna make it off this porch anyhow. You take Jack and Abi... take them and... don't worry about me. Just get 'em out of here!", "Ain't time, John. I ain't gonna make it off this porch anyhow. You take Jack and Abi... take them and... don't worry about me. Just get 'em out of here!"),
         "src": two("The Last Enemy That Shall Be Destroyed (RDR1, Act III), his last words, to John, who promises to get him out safe",
                    "The Last Enemy That Shall Be Destroyed (RDR1, acte III), ses derniers mots, à John, qui promet de le mettre à l'abri. Traduction : « Pas le temps, John. De toute façon, je quitterai pas ce perron. Prends Jack et Abi... prends-les et... t'occupe pas de moi. Emmène-les loin d'ici ! »")},
    ]},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"quotes": [
        {"q": two("I'll bed y'all down!", "I'll bed y'all down!"),
         "src": two("Red Dead Redemption multiplayer, taunt of the Uncle character model",
                    "Multijoueur de Red Dead Redemption, provocation du modèle de personnage Uncle. Traduction : « Je vais tous vous étendre ! »")},
        {"q": two("You ain't gettin' away with this!", "You ain't gettin' away with this!"),
         "src": two("Red Dead Redemption multiplayer, taunt of the Uncle character model",
                    "Multijoueur de Red Dead Redemption, provocation du modèle de personnage Uncle. Traduction : « Tu vas pas t'en tirer comme ça ! »")},
        {"q": two('Back the hell off!', 'Back the hell off!'),
         "src": two("Red Dead Redemption multiplayer, taunt of the Uncle character model",
                    "Multijoueur de Red Dead Redemption, provocation du modèle de personnage Uncle. Traduction : « Recule, bon sang ! »")},
        {"q": two("You're dead, ya son of a bitch!", "You're dead, ya son of a bitch!"),
         "src": two("Red Dead Redemption multiplayer, taunt of the Uncle character model",
                    "Multijoueur de Red Dead Redemption, provocation du modèle de personnage Uncle. Traduction : « T'es mort, fils de pute ! »")},
        {"q": two("You're mine, ya bastard!", "You're mine, ya bastard!"),
         "src": two("Red Dead Redemption multiplayer, taunt of the Uncle character model",
                    "Multijoueur de Red Dead Redemption, provocation du modèle de personnage Uncle. Traduction : « T'es à moi, salopard ! »")},
        {"q": two('Leave us alone!', 'Leave us alone!'),
         "src": two("Red Dead Redemption multiplayer, taunt of the Uncle character model",
                    "Multijoueur de Red Dead Redemption, provocation du modèle de personnage Uncle. Traduction : « Fichez-nous la paix ! »")},
        {"q": two('Come on, then!', 'Come on, then!'),
         "src": two("Red Dead Redemption multiplayer, taunt of the Uncle character model",
                    "Multijoueur de Red Dead Redemption, provocation du modèle de personnage Uncle. Traduction : « Vas-y, approche ! »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"ul": [
        two("After \"Eastward Bound\", Uncle is asleep and, with Strauss, is the only one in camp with no new dialogue.",
            "Après \"Eastward Bound\", Uncle dort et, avec Strauss, c'est le seul membre du camp qui n'a aucun nouveau dialogue."),
        two("In \"Polite Society, Valentine Style\", Arthur kicks Uncle in the leg to wake him if he stands close enough, and shouts at him otherwise.",
            "Dans \"Polite Society, Valentine Style\", Arthur réveille Uncle d'un coup de pied dans la jambe s'il se tient assez près, et lui crie dessus sinon."),
        two("In \"An Honest Mistake\", one gold medal objective is to save Uncle when a guard overpowers him in the woods. If Arthur does not, Uncle scolds him for it afterwards. If the stealth attack on the two guards fails, Uncle still remarks that Bill and Charles had less luck.",
            "Dans \"An Honest Mistake\", l'un des objectifs de la médaille d'or consiste à sauver Uncle quand un garde le maîtrise dans les bois. Si Arthur ne le fait pas, Uncle le lui reproche ensuite. Si l'attaque silencieuse contre les deux gardes échoue, Uncle fait tout de même remarquer que Bill et Charles ont eu moins de chance."),
        two("During \"Home of the Gentry?\", Uncle sticks with John on the ride to Beecher's Hope, even dismounting to walk after him, but he never climbs onto John's horse.",
            "Pendant \"Home of the Gentry?\", Uncle suit John jusqu'à Beecher's Hope, quitte à mettre pied à terre pour le suivre, mais ne monte jamais sur le cheval de John."),
        two("At the end of \"The Tool Box\", Uncle wears his orange shirt instead of his white one and carries Sadie's Carbine Repeater.",
            "À la fin de \"The Tool Box\", Uncle porte sa chemise orange au lieu de la blanche et tient la Carbine Repeater de Sadie."),
        two("Before \"A Quick Favor for an Old Friend\", John can wake Uncle by firing a shot next to him, which locks the mission for a short while.",
            "Avant \"A Quick Favor for an Old Friend\", John peut réveiller Uncle en tirant à côté de lui, ce qui bloque la mission un court moment."),
    ]},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("If John stays with the herd instead of saving the train in \"By Sweat and Toil\", Uncle remarks that he really has changed.",
            "Si John reste avec le troupeau au lieu de sauver le train dans \"By Sweat and Toil\", Uncle remarque qu'il a vraiment changé."),
        two("In the opening cutscene of \"Spare the Love, Spoil the Child\", Jack can be seen walking from the barn towards John and Uncle while Uncle reports that he has gone after a grizzly.",
            "Dans la cinématique d'ouverture de \"Spare the Love, Spoil the Child\", on peut voir Jack marcher de la grange vers John et Uncle au moment même où Uncle annonce qu'il est parti chasser un grizzly."),
        two("John can shoot Uncle's hat off. In the following cutscenes, Uncle appears without it.",
            "John peut faire sauter le chapeau d'Uncle d'un tir. Dans les cinématiques suivantes, Uncle apparaît tête nue."),
        two("Dynamite, fire bottles and throwing knives can kill him. His body cannot be looted after his death scene.",
            "La dynamite, les bouteilles incendiaires et les couteaux de lancer peuvent le tuer. Son corps ne peut pas être fouillé après la scène de sa mort."),
        two("In the stranger mission \"Remember My Family\", Edgar Ross wears clothes similar to Uncle's.",
            "Dans la mission d'inconnu \"Remember My Family\", Edgar Ross porte une tenue proche de celle d'Uncle."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors continuité)")},
    {"ul": [
        two("Uncle is the first undead the player meets in Undead Nightmare.",
            "Uncle est le premier mort-vivant que le joueur rencontre dans Undead Nightmare."),
        two("He is one of the few undead that never run at the player: in \"Love in the Time of Plague\" he keeps walking slowly toward John, whatever the distance or the gunfire. A non-lethal shot sometimes changes this: once back on his feet, he charges like any fresh undead.",
            "C'est l'un des rares morts-vivants à ne jamais foncer sur le joueur : dans \"Love in the Time of Plague\", il continue d'avancer lentement vers John, quelle que soit la distance ou la fusillade. Une balle qui ne le tue pas change parfois la donne : une fois relevé, il charge comme n'importe quel mort-vivant récent."),
        two("The yellowish stain in his beard is replaced by blood in Undead Nightmare.",
            "Dans Undead Nightmare, la tache jaunâtre de sa barbe est remplacée par du sang."),
        two("In the opening cutscene of \"Love in the Time of Plague\", the back door of the house is already boarded up, and every door is found boarded up from outside, before anyone knows the dead have risen.",
            "Dans la cinématique d'ouverture de \"Love in the Time of Plague\", la porte de derrière est déjà condamnée par des planches, et toutes les portes le sont côté extérieur, avant que quiconque sache que les morts se sont relevés."),
        two("In \"On a Pale Horse\", no grave of Uncle is seen next to John's, whereas the main game shows him buried a few yards from John.",
            "Dans \"On a Pale Horse\", aucune tombe d'Uncle n'apparaît près de celle de John, alors que le jeu principal le montre enterré à quelques mètres de lui."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Uncle became a playable character model in the multiplayer mode of Red Dead Redemption with the Myths and Mavericks Bonus Pack. Engadget reported on July 27, 2011 that the pack would come out in September at no cost. It was released free on September 13, 2011 on PlayStation 3 and Xbox 360, with eight new character models, among them [[javier-escuella|Javier Escuella]], [[landon-ricketts|Landon Ricketts]], [[nastas|Nastas]] and [[vincente-de-santa|Vincente de Santa]]. The same pack added Beecher's Hope as a Stronghold map. Players select Uncle in the Revolution section of the Outfitter.",
              "Uncle devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Myths and Mavericks Bonus Pack. Engadget annonce le 27 juillet 2011 que ce pack sortira en septembre, sans frais. Il est publié gratuitement le 13 septembre 2011 sur PlayStation 3 et Xbox 360, avec huit nouveaux modèles de personnages, dont [[javier-escuella|Javier Escuella]], [[landon-ricketts|Landon Ricketts]], [[nastas|Nastas]] et [[vincente-de-santa|Vincente de Santa]]. Le même pack fait de Beecher's Hope une carte du mode Stronghold. On choisit Uncle dans la section Revolution de l'Outfitter.")},
    {"p": two("Like the other characters of the pack, Uncle has only seven taunts, where most multiplayer characters have more. His mouth does not move when he taunts. His multiplayer model wears two gloves, while the story version wears a single glove on the right hand. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the Uncle model is not available in them.",
              "Comme les autres personnages du pack, Uncle ne dispose que de sept provocations, contre davantage pour la plupart des personnages du multijoueur. Sa bouche ne bouge pas quand il provoque. Son modèle multijoueur porte deux gants, alors que la version du mode histoire n'en porte qu'un, à la main droite. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle Uncle n'y est donc pas disponible.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released a promotional screenshot of Uncle for Red Dead Redemption and promotional artwork of the undead Uncle for Undead Nightmare. For Red Dead Redemption 2, Rockstar released new official artwork of him. A still from the third trailer, released on May 2, 2018, shows him at a campfire between Javier and Arthur; the trailer number comes from the file name of the image on the Red Dead Wiki. On September 6, 2018, Rockstar posted his portrait and character description on Twitter, in a series covering the members of the gang, and The Hollywood Reporter reproduced the series the next day. In the composite image of the 23 gang members, Uncle stands in the front row, between Pearson and Swanson.",
              "Rockstar a diffusé une capture promotionnelle d'Uncle pour Red Dead Redemption, puis une illustration promotionnelle d'Uncle en mort-vivant pour Undead Nightmare. Pour Red Dead Redemption 2, Rockstar a publié une nouvelle illustration officielle du personnage. Une image de la troisième bande-annonce, publiée le 2 mai 2018, le montre près d'un feu de camp, entre Javier et Arthur ; le numéro de la bande-annonce vient du nom du fichier de l'image sur le Red Dead Wiki. Le 6 septembre 2018, Rockstar publie sur Twitter son portrait et sa description, dans une série consacrée aux membres du gang, et The Hollywood Reporter reprend la série le lendemain. Sur l'image qui réunit les 23 membres du gang, Uncle figure au premier rang, entre Pearson et Swanson.")},
]
