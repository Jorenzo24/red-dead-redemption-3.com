"""Bill Williamson, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched 16 Oct 2026 via the MediaWiki API, saved in
scratchpad cov/bill/ and cov/bill/m/):
- Red Dead Wiki EN "Bill Williamson" (Mission Appearances, Notable Murders Committed,
  Quotes, Trivia, Gallery captions) and FR "Bill Williamson" (Apparitions dans les
  missions, Citations, Anecdotes, infobox).
- Mission pages: Outlaws from the West, Old Friends, Who the Hell is Leviticus
  Cornwall?, Eastward Bound, Americans at Rest, Paying a Social Call, American
  Distillation, An Honest Mistake, Sodom? Back to Gomorrah, Coach Robbery (Bill
  Williamson), A Short Walk in a Pretty Town, Blood Feuds, Ancient and Modern, The
  Battle of Shady Belle, The Gilded Cage, Coach Robbery (Micah Bell), Revenge is a Dish
  Best Eaten, Banking, The Old American Art, Lost and Not Quite Found, Welcome to the
  New World, Hell Hath No Fury, Paradise Mercifully Departed, Fleeting Joy, That's
  Murfree Country, The Delights of Van Horn, My Last Boy, Our Best Selves, Red Dead
  Redemption (mission); RDR1: Exodus in America, Spare the Rod, Spoil the Bandit, The
  Assault on Fort Mercer, An Appointed Time; location page Fort Mercer.
- Transcripts "/dialogues": Outlaws from the West, Old Friends, Who the Hell is
  Leviticus Cornwall?, Eastward Bound, Americans at Rest, Sodom? Back to Gomorrah,
  Red Dead Redemption (mission), Exodus in America, Spare the Rod, Spoil the Bandit,
  An Appointed Time, The Assault on Fort Mercer. Every quote below is checked word for
  word against one of them, except the two camp lines and the multiplayer lines, which
  come from the character page's quote list.
- Newspapers in the game: Blackwater Ledger No. 53 "Williamson Gang Reign Of Terror"
  and No. 58 (RDR1), "Notorious Bad Man Alive" (RDR2, 1907), as cited by the wiki.
- Real world: Liars and Cheats Pack, released September 21, 2010 on Xbox Live and
  PlayStation Network (Engadget and Game Informer, August 27, 2010); SacAnime Summer
  2019 cast panel (cited by the wiki); RDR2 trailer and portrait dates as established
  in charles_C / hosea_C / micah_C; RDR1 ports (PS4 and Switch, August 17, 2023; PC,
  October 29, 2024), released without the multiplayer mode.
Fact-check pass (16 Oct 2026, fc_report1/2/3 + coverage): Old Friends raid (Dutch sends Bill
and Micah into the camp from another side); Cornwall train boarded on foot from above the
tunnel (transcript); Bill stumbles into the Valentine saloon drunk; Bill's coach (Tilly
offended, Bill opens fire, the shooting makes Tilly ride off); Micah AND Bill plan the Bayou Nwa
coach; the "A, D, C, B & S" reading attributed to the wiki; quote contexts corrected (John
offers help; "from the cliffs"; Allende holds Bill down); added, transcript-checked: Bill's
"What the hell are you doing?" and "You always was a traitor, you bastard orphan!" (An
Appointed Time dialogues l.113 and l.125) and John's "Williamson is a proud fool..." (The
Assault on Fort Mercer dialogues l.29, transcript wording, not the mission page's). Dutch's
"Like Colonel Waxman on a jolly?" quoted as on the mission page (the "jolly boat" reading is
the wiki's). Liars and Cheats "detailed" (not announced) on Aug 27, 2010. Bollard models only in
Spare the Rod; Banditos already in the fort before the assault.
Ownership (FIX_RULES): removed here because owned elsewhere: Personality "In his own words"
lines ("I guess... that fell", "How come every time...": part B); names (Marion, William
Williamson, Albert Danielson: part B); hat pin (part B); guide descriptions (part B);
Blackwater Ledger No. 53 and "Notorious Bad Man Alive" (part A); bounty-hunter capture (part
A); Karen "sweet on him", camp fetch and throw-out (part B); Van Horn roles, Lenny's dynamite
remark, Cuba question, Six Point ride talk, Gilded Cage guests, Jack insult (part A or B);
birth year 1866 dropped (unsupported). Trivia keeps only facts that appear nowhere else.
Not added (VERIFY items without a transcript): "I always knew you were a coward", "Would you
hurry up?", "Billy the Cowboy", "Dynamite Williamson", the rape at Ridgewood Farm, the sun
trivia, the FR-only Lakay accusation; extra multiplayer lines (optional, skipped).
Excluded: the whole sexuality bullet list of the wiki Trivia (interpretation and
speculation); the "foreshadowing" readings (army and power, Paying a Social Call,
Welcome to the New World); "seemingly unaware that the sun rises in the east" (no line
found); the Bill Dalton name theory (wiki says "could be"); the guess that nobody
outside the gang knew the name Marion; the guess that Bill and Javier fled together
(only their absence is stated); the train driver "possibly killed" by Bill (Our Best
Selves); the "I fucked with Abigail" taunt (kept out of the quote list, vulgar, and the
page only paraphrases it); his weapons, rifle preference and horse (part B); his
harassment of Javier, Lenny, Kieran, Pearson and Charles (relationships, part B); the
Steve J. Palmer interview with The Gaming Liberty / Retroplayer (2010), the fact that
the Exodus in America exchange was the first scene captured for RDR1, and Palmer
doing Charles's motion capture in Americans at Rest (development and performance,
part D); Bill "reporting there is barely any track left" in Our Best Selves and Dutch
berating him about "savagery" in Revenge is a Dish Best Eaten (character page only,
absent from the mission pages); the bank manager interrogation in Banking, The Old
American Art (character page only; the fact-checked Charles fiche gives crowd control).
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
A1 = two("Act I: New Austin", "Acte I : New Austin")
A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 25 story missions of Red Dead Redemption 2 for Bill, from the arrival at Colter to the standoff at Beaver Hollow, plus two companion activities: the coach robberies he runs with Arthur and Tilly, then with Micah and Arthur. The French edition also counts 25 story missions, but its list differs: it adds \"Dear Uncle Tacitus\", the crossing back from Guarma, and leaves out \"Lost and Not Quite Found\". Bill appears in no mission of the epilogue. In Red Dead Redemption, the wiki lists three missions. Bill is also the target of \"The Assault on Fort Mercer\" in Act I, but he has already left for Mexico when John's posse storms the fort. Bill is never playable in either story mode.",
              "Le Red Dead Wiki anglais recense 25 missions principales de Red Dead Redemption 2 pour Bill, de l'arrivée à Colter jusqu'à l'affrontement de Beaver Hollow, plus deux activités de compagnon : les attaques de diligence qu'il mène avec Arthur et Tilly, puis avec Micah et Arthur. L'édition française en compte aussi 25, mais sa liste diffère : elle ajoute \"Dear Uncle Tacitus\", la traversée de retour depuis Guarma, et omet \"Lost and Not Quite Found\". Bill n'apparaît dans aucune mission de l'épilogue. Pour Red Dead Redemption, le wiki retient trois missions. Bill est aussi la cible de \"The Assault on Fort Mercer\", à l'acte I, mais il est déjà parti pour le Mexique quand la troupe de John prend le fort d'assaut. Bill n'est jamais jouable dans le mode histoire des deux jeux.")},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Bill's role", "Rôle de Bill")], "rows": [
        M("Outlaws from the West", C1,
          "Arrives at Colter with the gang's caravan in the blizzard. With Arthur, he brings Davey Callander, already dead, into the cabin on a stretcher.",
          "Arrive à Colter avec le convoi du gang, en pleine tempête de neige. Avec Arthur, il porte sur un brancard Davey Callander, déjà mort, jusque dans la cabane."),
        M("Old Friends", C1,
          "Listed as mission giver by the wiki. Micah punches him in the men's shack after he laughs at Lenny's joke. During the raid on the O'Driscoll camp, Dutch sends him and Micah down into the camp from another side; he then searches a wagon and takes the dynamite Arthur finds. Back at Colter, Dutch has him tie up [[kieran-duffy|Kieran]] with [[uncle|Uncle]].",
          "Donneur de mission selon le wiki. Micah le frappe dans la cabane des hommes parce qu'il a ri de la plaisanterie de Lenny. Lors de l'attaque du camp O'Driscoll, Dutch l'envoie avec Micah descendre dans le camp par un autre côté ; il fouille ensuite un chariot et récupère la dynamite trouvée par Arthur. De retour à Colter, Dutch le charge d'attacher [[kieran-duffy|Kieran]] avec [[uncle|Uncle]]."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "Sent ahead by Dutch to lay the charge on the tracks by the water tower, before the tunnel. Arthur helps him wire the detonator, but the dynamite does not go off; Arthur, Javier and Lenny run to the tunnel and jump onto the train from above. Bill later hands Arthur and [[charles-smith|Charles]] the dynamite for the door of Cornwall's private car.",
          "Envoyé en avant par Dutch pour poser la charge sur les rails près du château d'eau, avant le tunnel. Arthur l'aide à brancher le détonateur, mais la dynamite n'explose pas ; Arthur, Javier et Lenny courent jusqu'au tunnel et sautent sur le train depuis le haut. Bill remet ensuite à Arthur et à [[charles-smith|Charles]] la dynamite destinée à la porte de la voiture privée de Cornwall."),
        M("Eastward Bound", C1,
          "Loads the wagons with Lenny and [[orville-swanson|Swanson]], then drives down from the mountains in a wagon with Charles. When the wheel of Arthur and [[hosea-matthews|Hosea]]'s wagon comes off, he calls back to check on them. He is then absent from Horseshoe Overlook until after \"Americans at Rest\".",
          "Charge les chariots avec Lenny et [[orville-swanson|Swanson]], puis descend de la montagne dans un chariot avec Charles. Quand la roue du chariot d'Arthur et de [[hosea-matthews|Hosea]] se détache, il leur demande si tout va bien. Il disparaît ensuite de Horseshoe Overlook jusqu'à la fin de \"Americans at Rest\"."),
        M("Americans at Rest", C2,
          "Stumbles drunk into the Valentine saloon, bumps into a customer, headbutts him and starts the brawl. He tells Arthur to help [[javier-escuella|Javier]] against Tommy. When Dutch hands out tasks to find Sean, Bill asks what he should do and Dutch makes fun of him.",
          "Entre ivre au saloon de Valentine en titubant, bouscule un client, lui assène un coup de tête et déclenche la bagarre. Il demande à Arthur d'aller aider [[javier-escuella|Javier]] face à Tommy. Quand Dutch répartit les tâches pour retrouver Sean, Bill demande ce qu'il doit faire, et Dutch se moque de lui."),
        M("Paying a Social Call", C2,
          "Ordered by Dutch to geld Kieran, he picks up a pair of red-hot tongs, and Kieran gives up Six Point Cabin. He rides there with Arthur and [[john-marston|John]], having slipped throwing knives into Arthur's saddle, and kills O'Driscoll lookouts with Arthur. He backs Kieran when Arthur accuses him of a setup, then takes him back to camp with John.",
          "Sur ordre de Dutch, il s'empare d'une pince chauffée au rouge pour castrer Kieran, qui livre aussitôt Six Point Cabin. Il s'y rend avec Arthur et [[john-marston|John]], après avoir glissé des couteaux de lancer dans la sacoche d'Arthur, et élimine avec lui des sentinelles O'Driscoll. Il prend le parti de Kieran quand Arthur l'accuse d'un piège, puis le ramène au camp avec John."),
        M("American Distillation", C3,
          "Made a temporary deputy in Rhodes with Dutch and Arthur. He knocks out moonshiners with Arthur, fights off the Lemoyne Raiders who come to buy the liquor, then drives the wagon of moonshine back to camp.",
          "Nommé adjoint temporaire à Rhodes avec Dutch et Arthur. Il assomme des bouilleurs de cru avec Arthur, repousse les Lemoyne Raiders venus acheter l'alcool, puis ramène au camp le chariot de moonshine."),
        M("An Honest Mistake", C3,
          "Rides with Uncle, Arthur and Charles to rob a wagon that belongs to Cornwall Kerosene & Tar. Hiding in a barn at night, he knocks over a bucket and gives away their position. He escapes through the woods with Charles.",
          "Accompagne Uncle, Arthur et Charles pour dévaliser un chariot qui appartient à Cornwall Kerosene & Tar. Caché la nuit dans une grange, il renverse un seau et trahit leur présence. Il s'enfuit par les bois avec Charles."),
        M("Sodom? Back to Gomorrah", C3,
          "Mission giver. He planned the Valentine bank robbery with [[karen-jones|Karen]] and brings in Arthur and [[lenny-summers|Lenny]]. On the ride, he mentions the deals he is working on with the Gray family. He holds up the bank with Arthur and Lenny and covers the escape.",
          "Donneur de mission. Il a préparé le braquage de la banque de Valentine avec [[karen-jones|Karen]] et embarque Arthur et [[lenny-summers|Lenny]]. En route, il parle des affaires qu'il négocie avec la famille Gray. Il braque la banque avec Arthur et Lenny et couvre la fuite."),
        M("Coach Robbery (companion activity)", C3,
          "Mission giver. Plans the robbery of a Boles Overland banking coach west of Dewberry Creek; Arthur brings [[tilly-jackson|Tilly]] as a distraction. Bill and Tilly argue on the way; one of his remarks offends her, Bill opens fire on the guards, and the shooting makes Tilly ride off. Total take: 307.50 dollars, 82.50 of them for Arthur.",
          "Donneur de mission. Prépare l'attaque d'une diligence bancaire de la Boles Overland à l'ouest de Dewberry Creek ; Arthur emmène [[tilly-jackson|Tilly]] pour faire diversion. Bill et Tilly se disputent en chemin ; une de ses remarques la vexe, Bill ouvre le feu sur les gardes, et la fusillade fait fuir Tilly. Butin : 307,50 dollars, dont 82,50 pour Arthur."),
        M("A Short Walk in a Pretty Town", C3,
          "Mission giver. He set up the supposed security job with the Grays and meets Arthur, [[micah-bell|Micah]] and [[sean-macguire|Sean]] in Rhodes. In the ambush, a sniper kills Sean and Bill is hit in the shoulder, then captured by Sheriff Leigh Gray. Arthur kills the sheriff, who is holding a gun to Bill's head. Arthur then tells Bill to bury Sean properly.",
          "Donneur de mission. C'est lui qui a monté le prétendu contrat de protection pour les Gray, et il retrouve Arthur, [[micah-bell|Micah]] et [[sean-macguire|Sean]] à Rhodes. Dans l'embuscade, un tireur embusqué tue Sean et Bill est touché à l'épaule, puis capturé par le shérif Leigh Gray. Arthur abat le shérif, qui tient Bill en joue. Arthur demande ensuite à Bill d'enterrer Sean dignement."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Rides with Dutch, Arthur, Hosea, John, Charles, Javier and Lenny to Braithwaite Manor to get [[jack-marston|Jack]] back.",
          "Accompagne Dutch, Arthur, Hosea, John, Charles, Javier et Lenny à Braithwaite Manor pour récupérer [[jack-marston|Jack]]."),
        M("The Battle of Shady Belle", C3,
          "Present at Clemens Point with the gang when [[andrew-milton|Milton]] and [[edgar-ross|Ross]] come to the camp, the morning after the attack on Braithwaite Manor.",
          "Présent à Clemens Point avec le gang quand [[andrew-milton|Milton]] et [[edgar-ross|Ross]] se présentent au camp, au lendemain de l'attaque de Braithwaite Manor."),
        M("The Gilded Cage", C4,
          "Goes to the mayor's party in Saint Denis with Dutch, Arthur and Hosea, in a tuxedo, under an alias. He mingles with the guests while Dutch and Arthur meet Bronte. On the way back, he calls the evening torture.",
          "Se rend à la réception du maire de Saint-Denis avec Dutch, Arthur et Hosea, en smoking, sous un nom d'emprunt. Il se mêle aux invités pendant que Dutch et Arthur rencontrent Bronte. Au retour, il qualifie la soirée de torture."),
        M("Coach Robbery (companion activity)", C4,
          "Plans with Micah the robbery of a Boles Overland banking coach in Bayou Nwa, and the two bring Arthur along. Micah places dynamite on the road and Arthur sets it off with a shot as the coach rolls over it. Total take: 305 dollars, 55 of them for Arthur.",
          "Prépare avec Micah l'attaque d'une diligence bancaire de la Boles Overland dans le Bayou Nwa, et tous deux emmènent Arthur. Micah pose de la dynamite sur la route, et Arthur la fait exploser d'un tir au passage de la diligence. Butin : 305 dollars, dont 55 pour Arthur."),
        M("Revenge is a Dish Best Eaten", C4,
          "Lands by boat near [[angelo-bronte|Bronte]]'s mansion with Dutch, Arthur, John and Lenny, and helps storm it.",
          "Débarque en barque près du manoir de [[angelo-bronte|Bronte]] avec Dutch, Arthur, John et Lenny, et participe à l'assaut."),
        M("Banking, The Old American Art", C4,
          "Keeps the people in the Lemoyne National Bank under control with Charles and Micah. He escapes over the rooftops, hides with the other survivors until nightfall and boards the ship at the docks with Dutch, Arthur, Micah and Javier.",
          "Tient en respect les occupants de la Lemoyne National Bank avec Charles et Micah. Il s'enfuit par les toits, se cache avec les autres survivants jusqu'à la nuit et embarque sur les quais avec Dutch, Arthur, Micah et Javier."),
        M("Lost and Not Quite Found", C4,
          "Caught in the storm aboard the Antenor. He reaches a lifeboat with Dutch, Micah and Javier, while Arthur is cut off by falling crates.",
          "Pris dans la tempête à bord de l'Antenor. Il gagne un canot de sauvetage avec Dutch, Micah et Javier, tandis qu'Arthur est bloqué par la chute de caisses."),
        M("Welcome to the New World", C5,
          "Found by Arthur at a campfire on the beach of Guarma with Dutch, Micah and Javier. Levi Simon's militia chains them up; Hercule Fontaine's ambush frees them, and Bill fights the guards alongside the others.",
          "Retrouvé par Arthur autour d'un feu, sur une plage de Guarma, avec Dutch, Micah et Javier. La milice de Levi Simon les enchaîne ; l'embuscade d'Hercule Fontaine les libère, et Bill combat les gardes avec les autres."),
        M("Hell Hath No Fury", C5,
          "Defends the fort at Cinco Torres and guards the cannon on the roof with Micah. After the battle, he goes with Dutch to fetch Javier.",
          "Défend le fort de Cinco Torres et garde le canon sur le toit avec Micah. Après la bataille, il part avec Dutch chercher Javier."),
        M("Paradise Mercifully Departed", C5,
          "Listed as mission giver by the wiki. While the others go off to destroy the gun batteries, he remains with Javier, who is still recovering; he then sails back to America with the gang.",
          "Donneur de mission selon le wiki. Pendant que les autres partent détruire les batteries, il reste auprès de Javier, encore convalescent, puis repart vers l'Amérique avec le gang."),
        M("Fleeting Joy", C5,
          "The last to reach the gang's camp at Lakay, after Dutch, complaining that he asked everywhere to find them. When the Pinkertons attack, he helps Arthur and [[sadie-adler|Sadie]] hold them off.",
          "Le dernier à rejoindre le camp de Lakay, après Dutch, en se plaignant d'avoir dû demander partout pour retrouver le gang. Quand les Pinkerton attaquent, il aide Arthur et [[sadie-adler|Sadie]] à les repousser."),
        M("That's Murfree Country", C5,
          "At Beaver Hollow when Uncle brings in a drunk [[molly-oshea|Molly]]. After [[susan-grimshaw|Susan]] shoots her, Susan orders Bill and [[simon-pearson|Pearson]] to burn the body.",
          "Présent à Beaver Hollow quand Uncle ramène [[molly-oshea|Molly]], ivre. Après l'avoir abattue, [[susan-grimshaw|Susan]] ordonne à Bill et à [[simon-pearson|Pearson]] de brûler le corps."),
        M("The Delights of Van Horn", C6,
          "Sent by Micah with Arthur to steal army dynamite. He stops Micah from mocking Arthur's illness. At Van Horn, he plays a drunk lying in the road, shoots the rider sent to move him, and drives the wagon while Arthur, who took Bill's Carcano rifle, holds off the pursuers.",
          "Envoyé par Micah avec Arthur pour voler de la dynamite de l'armée. Il fait taire Micah, qui se moque de la maladie d'Arthur. À Van Horn, il joue l'ivrogne couché sur la route, abat le cavalier venu le déplacer et conduit le chariot pendant qu'Arthur, armé du fusil Carcano de Bill, repousse les poursuivants."),
        M("My Last Boy", C6,
          "Rides with Dutch's group, which attacks the soldiers at the Cornwall oil fields from another side, while Arthur, Charles and Sadie go to rescue Eagle Flies. In Arthur's journal, the take of the job is credited to \"A, D, C, B & S\", which the Red Dead Wiki reads as including Bill.",
          "Fait partie du groupe de Dutch, qui attaque les soldats des champs pétrolifères de Cornwall par un autre côté, pendant qu'Arthur, Charles et Sadie partent secourir Eagle Flies. Dans le journal d'Arthur, le butin de l'opération est attribué à \"A, D, C, B & S\", initiales dans lesquelles le Red Dead Wiki compte Bill."),
        M("Our Best Selves", C6,
          "Takes part in the army train robbery. When a carriage catches fire, John jumps onto the back of Bill's horse to get past it. After John falls from the train, Bill stays with Arthur, Sadie and Cleet to fight off the soldiers.",
          "Participe à l'attaque du train de l'armée. Quand une voiture prend feu, John saute en croupe derrière Bill pour la dépasser. Après la chute de John, Bill reste avec Arthur, Sadie et Cleet pour repousser les soldats."),
        M("Red Dead Redemption", C6,
          "Sides with Dutch and Micah in the standoff at Beaver Hollow and aims his gun at Arthur and John. Arthur asks him and Javier to think for themselves. When the Pinkertons attack, Bill is not among the men who chase Arthur and John.",
          "Se range derrière Dutch et Micah lors de l'affrontement de Beaver Hollow et braque son arme sur Arthur et John. Arthur lui demande, ainsi qu'à Javier, de réfléchir par eux-mêmes. Quand les Pinkerton attaquent, Bill ne fait pas partie des hommes qui poursuivent Arthur et John."),
    ]}},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Bill's role", "Rôle de Bill")], "rows": [
        M("Exodus in America", A1,
          "From the walls of Fort Mercer, he refuses John's offer to surrender and mocks him. When John reaches for his revolver, one of Bill's men shoots him, and the gang leaves him for dead.",
          "Du haut des murs de Fort Mercer, il refuse l'offre de reddition de John et se moque de lui. Quand John porte la main à son revolver, un des hommes de Bill lui tire dessus, et la bande l'abandonne pour mort."),
        M("Spare the Rod, Spoil the Bandit", A1,
          "Spotted on the cliffs near Mercer Station by John, [[leigh-johnson|Marshal Johnson]] and his deputies after his gang's raid on Ridgewood Farm. He taunts John, sends his men to attack and rides off. His right-hand man, Norman Deek, is captured.",
          "Repéré sur les falaises près de Mercer Station par John, le [[leigh-johnson|marshal Johnson]] et ses adjoints après le raid de sa bande sur Ridgewood Farm. Il nargue John, lance ses hommes à l'attaque et s'enfuit. Son bras droit, Norman Deek, est capturé."),
        M("An Appointed Time", A2,
          "Flees the rebel assault on Escalera in an armored stagecoach with [[agustin-allende|Allende]]. When the coach stops, Allende pushes him out and offers him to John in exchange for his own life. Bill is killed by John or, if the player does not shoot, by [[abraham-reyes|Reyes]].",
          "Fuit l'assaut des rebelles sur Escalera dans une diligence blindée avec [[agustin-allende|Allende]]. Quand la diligence s'arrête, Allende le pousse dehors et le livre à John en échange de sa propre vie. Bill est tué par John ou, si le joueur ne tire pas, par [[abraham-reyes|Reyes]]."),
    ]}},
    # ---------------------------------------------------------- notable kills
    {"h3": two("Notable people Bill kills", "Personnages notables tués par Bill")},
    {"p": two("The Red Dead Wiki lists a single notable murder for Bill, the guard Eric at Van Horn. The table adds the other victims that the mission pages attribute to him by name or individually. Lawmen, Raiders, Cornwall guards, Cuban soldiers and Pinkertons killed in gunfights alongside Arthur are not listed one by one. In Red Dead Redemption, the shot that wounds John at Fort Mercer is fired by one of Bill's men, not by Bill.",
              "Le Red Dead Wiki ne retient qu'un meurtre notable pour Bill : le garde Eric, à Van Horn. Le tableau y ajoute les autres victimes que les pages des missions lui attribuent nommément ou individuellement. Les représentants de la loi, Raiders, gardes de Cornwall, soldats cubains et Pinkerton abattus aux côtés d'Arthur lors des fusillades ne sont pas détaillés. Dans Red Dead Redemption, le tir qui blesse John à Fort Mercer vient d'un des hommes de Bill, et non de Bill lui-même.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K(two("Eric", "Eric"), "The Delights of Van Horn",
          "Storyline. A rider of the dynamite convoy, shot when he tries to drag Bill, who is pretending to be drunk, off the road.",
          "Histoire. Cavalier du convoi de dynamite, abattu quand il tente de traîner hors de la route Bill, qui fait semblant d'être ivre."),
        K(two("O'Driscoll lookout", "Sentinelle O'Driscoll"), "Paying a Social Call",
          "Storyline. One of the two guards near Six Point Cabin, killed by Bill while Arthur takes the other.",
          "Histoire. L'un des deux gardes postés près de Six Point Cabin, tué par Bill pendant qu'Arthur s'occupe de l'autre."),
        K(two("O'Driscoll relieving himself", "O'Driscoll en train d'uriner"), "Paying a Social Call",
          "Determinant. The first O'Driscoll can be killed silently by Bill if Arthur sends him instead of taking the lead.",
          "Selon le joueur. Le premier O'Driscoll peut être éliminé en silence par Bill si Arthur l'envoie au lieu de passer devant."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. The camp lines and the multiplayer lines come from the Red Dead Wiki's quote list, which names no mission for them. Other lines of Bill's appear in the Personality section.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Les répliques du camp et du multijoueur proviennent de la liste de citations du Red Dead Wiki, qui ne précise pas de mission. D'autres répliques de Bill figurent dans la section Personnalité.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 and 2", "Red Dead Redemption 2, chapitres 1 et 2")},
    {"quotes": [
        {"q": two("Looks fine... smells good.",
                  "Looks fine... smells good."),
         "src": two("Old Friends (RDR2, chapter 1), to Arthur, about the dynamite found in the O'Driscoll camp",
                    "Old Friends (RDR2, chapitre 1), à Arthur, à propos de la dynamite trouvée dans le camp O'Driscoll. Traduction : « Elle a l'air bien... elle sent bon. »")},
        {"q": two("Alright, that should do it. You head back up to the others, I've got it from here.",
                  "Alright, that should do it. You head back up to the others, I've got it from here."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), to Arthur, once the detonator is wired",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), à Arthur, une fois le détonateur branché. Traduction : « Bon, ça devrait aller. Retourne avec les autres, je m'occupe du reste. »")},
        {"q": two("Unless you got a death wish, I'd step back, fellers.",
                  "Unless you got a death wish, I'd step back, fellers."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), before the door of Cornwall's private car is blown",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), avant que la porte de la voiture privée de Cornwall ne saute. Traduction : « À moins d'avoir envie de mourir, je reculerais, les gars. »")},
        {"q": two("I said this'd be fun, didn't I?",
                  "I said this'd be fun, didn't I?"),
         "src": two("Americans at Rest (RDR2, chapter 2), during Arthur's fight with Tommy",
                    "Americans at Rest (RDR2, chapitre 2), pendant le combat d'Arthur contre Tommy. Traduction : « Je vous avais dit qu'on allait s'amuser, non ? »")},
        {"q": two("Well, what about me?",
                  "Well, what about me?"),
         "src": two("Americans at Rest (RDR2, chapter 2), to Dutch, who has given tasks to everyone else; Dutch answers: \"Well exactly, what about you?\"",
                    "Americans at Rest (RDR2, chapitre 2), à Dutch, qui vient de confier une tâche à tous les autres ; Dutch répond : \"Well exactly, what about you?\" (justement, et toi ?). Traduction : « Et moi, alors ? »")},
    ]},
    {"h4": two("Red Dead Redemption 2, chapter 3", "Red Dead Redemption 2, chapitre 3")},
    {"quotes": [
        {"q": two("Surprised you ain't already ribbed me about that dynamite again. One mistake, and I'll never live it down.",
                  "Surprised you ain't already ribbed me about that dynamite again. One mistake, and I'll never live it down."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), to Arthur, in optional dialogue on the ride to Valentine",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), à Arthur, dans un dialogue facultatif sur la route de Valentine. Traduction : « Ça m'étonne que tu ne m'aies pas encore charrié avec cette histoire de dynamite. Une seule erreur, et on me la ressortira toute ma vie. »")},
        {"q": two("That's the genius of it. Folk never look at what's right under their nose.",
                  "That's the genius of it. Folk never look at what's right under their nose."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), to Arthur, who worries about going back to Valentine",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), à Arthur, qui s'inquiète de retourner à Valentine. Traduction : « C'est ça qui est génial. Les gens ne regardent jamais ce qu'ils ont sous le nez. »")},
        {"q": two("What's happened to you? You're getting real nervy in your old age.",
                  "What's happened to you? You're getting real nervy in your old age."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), to Arthur",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), à Arthur. Traduction : « Qu'est-ce qui t'arrive ? Tu deviens drôlement nerveux en vieillissant. »")},
    ]},
    {"h4": two("Camp", "Camp")},
    {"quotes": [
        {"q": two("So what do they eat in Australia?",
                  "So what do they eat in Australia?"),
         "src": two("Camp (RDR2), to [[leopold-strauss|Leopold Strauss]], who has just corrected him: Strauss is Austrian, not German",
                    "Au camp (RDR2), à [[leopold-strauss|Leopold Strauss]], qui vient de le reprendre : il est autrichien, pas allemand. Traduction : « Et qu'est-ce qu'on mange en Australie ? »")},
        {"q": two("So what's wrong with you, you old fool?",
                  "So what's wrong with you, you old fool?"),
         "src": two("Camp (RDR2), drunk, to Hosea, asking how he is",
                    "Au camp (RDR2), ivre, à Hosea, pour prendre de ses nouvelles. Traduction : « Alors, qu'est-ce qui ne va pas chez toi, vieux fou ? »")},
    ]},
    {"h4": two("Red Dead Redemption, Act I", "Red Dead Redemption, acte I")},
    {"quotes": [
        {"q": two("Go away now, John. Don't make me kill you.",
                  "Go away now, John. Don't make me kill you."),
         "src": two("Exodus in America (RDR1, Act I), to John, outside Fort Mercer",
                    "Exodus in America (RDR1, acte I), à John, devant Fort Mercer. Traduction : « Va-t'en, John. Ne m'oblige pas à te tuer. »")},
        {"q": two("You must think I was born yesterday. You always did think I was an idiot.",
                  "You must think I was born yesterday. You always did think I was an idiot."),
         "src": two("Exodus in America (RDR1, Act I), to John",
                    "Exodus in America (RDR1, acte I), à John. Traduction : « Tu dois me prendre pour un perdreau de l'année. Tu m'as toujours pris pour un idiot. »")},
        {"q": two("Well, you never tried to save me before. You only seemed to save yourself.",
                  "Well, you never tried to save me before. You only seemed to save yourself."),
         "src": two("Exodus in America (RDR1, Act I), to John, who offers to help him",
                    "Exodus in America (RDR1, acte I), à John, qui lui propose son aide. Traduction : « Tu n'as jamais essayé de me sauver avant. Tu n'avais l'air de sauver que ta peau. »")},
        {"q": two("You implore me? You implore me? You always were one for fancy words. Well, things are different now, John. Now, I'm in charge! No more Dutch, and no more you.",
                  "You implore me? You implore me? You always were one for fancy words. Well, things are different now, John. Now, I'm in charge! No more Dutch, and no more you."),
         "src": two("Exodus in America (RDR1, Act I), to John, who has just said \"I implore you\"",
                    "Exodus in America (RDR1, acte I), à John, qui vient de lui dire \"I implore you\" (je t'en conjure). Traduction : « Tu m'en conjures ? Tu m'en conjures ? Toi et tes grands mots. Eh bien, les choses ont changé, John. Maintenant, c'est moi le chef ! Fini Dutch, et fini toi. »")},
        {"q": two("Poor John.",
                  "Poor John."),
         "src": two("Exodus in America (RDR1, Act I), after one of his men shoots John",
                    "Exodus in America (RDR1, acte I), après qu'un de ses hommes a tiré sur John. Traduction : « Pauvre John. »")},
        {"q": two("You always did have a high opinion of yourself, John. Dutch always said you were an arrogant son of a bitch! I guess he was about right. Get 'em boys!",
                  "You always did have a high opinion of yourself, John. Dutch always said you were an arrogant son of a bitch! I guess he was about right. Get 'em boys!"),
         "src": two("Spare the Rod, Spoil the Bandit (RDR1, Act I), to John, from the cliffs",
                    "Spare the Rod, Spoil the Bandit (RDR1, acte I), à John, du haut des falaises. Traduction : « Tu as toujours eu une haute opinion de toi-même, John. Dutch disait toujours que tu étais un fils de pute arrogant ! Faut croire qu'il avait raison. Allez-y, les gars ! »")},
        {"q": two("Williamson is a proud fool. Question is...which one will win out between his pride and his instinct for survival.",
                  "Williamson is a proud fool. Question is...which one will win out between his pride and his instinct for survival."),
         "src": two("John Marston about Bill, The Assault on Fort Mercer (RDR1, Act I), to Marshal Johnson, before the assault",
                    "John Marston à propos de Bill, The Assault on Fort Mercer (RDR1, acte I), au marshal Johnson, avant l'assaut. Traduction : « Williamson est un imbécile orgueilleux. Reste à savoir ce qui l'emportera chez lui, l'orgueil ou l'instinct de survie. »")},
    ]},
    {"h4": two("Red Dead Redemption, Act II", "Red Dead Redemption, acte II")},
    {"quotes": [
        {"q": two("Go, then! I'll cover you!",
                  "Go, then! I'll cover you!"),
         "src": two("An Appointed Time (RDR1, Act II), to Allende, as they flee Escalera",
                    "An Appointed Time (RDR1, acte II), à Allende, au moment de fuir Escalera. Traduction : « Vas-y, alors ! Je te couvre ! »")},
        {"q": two("You're a coward, Marston. A government dog.",
                  "You're a coward, Marston. A government dog."),
         "src": two("An Appointed Time (RDR1, Act II), to John, during the stagecoach chase",
                    "An Appointed Time (RDR1, acte II), à John, pendant la poursuite de la diligence. Traduction : « T'es un lâche, Marston. Un chien du gouvernement. »")},
        {"q": two("What the hell are you doing?",
                  "What the hell are you doing?"),
         "src": two("An Appointed Time (RDR1, Act II), to Allende, when the colonel stops the coach to hand him over",
                    "An Appointed Time (RDR1, acte II), à Allende, quand le colonel arrête la diligence pour le livrer. Traduction : « Qu'est-ce que tu fous ? »")},
        {"q": two("Dutch wanted you dead. We all did.",
                  "Dutch wanted you dead. We all did."),
         "src": two("An Appointed Time (RDR1, Act II), to John, while Allende holds Bill down on the ground",
                    "An Appointed Time (RDR1, acte II), à John, pendant qu'Allende le maintient au sol. Traduction : « Dutch voulait ta mort. On la voulait tous. »")},
        {"q": two("You always was a traitor, you bastard orphan!",
                  "You always was a traitor, you bastard orphan!"),
         "src": two("An Appointed Time (RDR1, Act II), to John, who has just said he will go after Dutch next",
                    "An Appointed Time (RDR1, acte II), à John, qui vient d'annoncer qu'il s'en prendra ensuite à Dutch. Traduction : « T'as toujours été un traître, espèce de bâtard d'orphelin ! »")},
        {"q": two("Alright, John. I - I - I'll come quietly.",
                  "Alright, John. I - I - I'll come quietly."),
         "src": two("An Appointed Time (RDR1, Act II), his last words, before he grabs Allende's gun",
                    "An Appointed Time (RDR1, acte II), ses derniers mots, avant de saisir l'arme d'Allende. Traduction : « D'accord, John. Je... je... je vais te suivre sans faire d'histoires. »")},
    ]},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"quotes": [
        {"q": two("This was the way it was always going to be, old friend.",
                  "This was the way it was always going to be, old friend."),
         "src": two("Red Dead Redemption multiplayer, line of the Bill Williamson character model",
                    "Multijoueur de Red Dead Redemption, réplique du modèle de personnage Bill Williamson. Traduction : « Ça devait forcément finir comme ça, mon vieil ami. »")},
        {"q": two("I always was cleverer than you, hahahahaha!",
                  "I always was cleverer than you, hahahahaha!"),
         "src": two("Red Dead Redemption multiplayer, line of the Bill Williamson character model",
                    "Multijoueur de Red Dead Redemption, réplique du modèle de personnage Bill Williamson. Traduction : « J'ai toujours été plus malin que toi, ha ha ha ha ha ! »")},
    ]},
]

BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Across the series", "Dans toute la série")},
    {"ul": [
        two("At the Red Dead Redemption II cast panel of SacAnime Summer 2019, Roger Clark, who plays Arthur, said he did not think the name Marion was a coincidence, since it was the real first name of John Wayne (Marion Robert Morrison). Steve J. Palmer, who plays Bill, called the choice a great homage to the Western genre. The Red Dead Wiki cites the recording of that panel and a live stream with Clark.",
            "Lors de la table ronde des acteurs de Red Dead Redemption II à la SacAnime de l'été 2019, Roger Clark, l'interprète d'Arthur, a dit ne pas croire au hasard pour le prénom Marion, qui était le vrai prénom de John Wayne (Marion Robert Morrison). Steve J. Palmer, l'interprète de Bill, y a vu un bel hommage au genre du western. Le Red Dead Wiki cite l'enregistrement de cette table ronde et un direct avec Clark."),
    ]},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"ul": [
        two("According to the Red Dead Wiki, Bill says in a camp conversation that he joined Dutch's cause because the army had shown him what power does to people.",
            "Selon le Red Dead Wiki, Bill explique lors d'une conversation au camp qu'il a rejoint la cause de Dutch parce que l'armée lui avait montré ce que le pouvoir fait aux gens."),
        two("In the dim opening cutscene of \"Outlaws from the West\", Bill rides The Count, Dutch's horse.",
            "Dans la cinématique d'ouverture de \"Outlaws from the West\", très sombre, Bill monte The Count, le cheval de Dutch."),
        two("In \"Who the Hell is Leviticus Cornwall?\", the bundle of dynamite left on the tracks explodes if the player shoots it, something Bill never tries.",
            "Dans \"Who the Hell is Leviticus Cornwall?\", le paquet de dynamite laissé sur les rails explose si le joueur tire dessus, ce que Bill ne tente jamais."),
        two("In \"Paying a Social Call\", Arthur can leave an O'Driscoll to Bill or John; if Arthur then steps in himself, they comment on it.",
            "Dans \"Paying a Social Call\", Arthur peut laisser Bill ou John s'occuper d'un O'Driscoll ; s'il intervient finalement lui-même, ils le lui font remarquer."),
        two("In \"American Distillation\", the player can follow Bill instead of racing Dutch. Bill then parks the moonshine wagon near the camp and walks in.",
            "Dans \"American Distillation\", le joueur peut suivre Bill au lieu de faire la course avec Dutch. Bill gare alors le chariot de moonshine près du camp et finit à pied."),
        two("In \"An Honest Mistake\", if Arthur alerts the guard in the barn before Bill does, Bill criticizes him during the fight.",
            "Dans \"An Honest Mistake\", si Arthur alerte le garde de la grange avant Bill, celui-ci le lui reproche pendant la fusillade."),
        two("At the mayor's party in \"The Gilded Cage\", Bill is the only member of the group whose dress trousers are too short.",
            "À la réception du maire, dans \"The Gilded Cage\", Bill est le seul du groupe dont le pantalon de soirée est trop court."),
        two("On the ship out of Saint Denis, when Bill asks whether the Pinkertons will follow them, Dutch answers: \"Like Colonel Waxman on a jolly?\" The Red Dead Wiki links the line to Waxman's recent victory at San Juan Hill, on Guarma.",
            "Sur le navire qui quitte Saint-Denis, quand Bill demande si les Pinkerton vont les suivre, Dutch répond : \"Like Colonel Waxman on a jolly?\" (comme le colonel Waxman sur sa chaloupe ?). Le Red Dead Wiki y voit une allusion à la récente victoire de Waxman à San Juan Hill, sur Guarma."),
        two("At the end of \"Hell Hath No Fury\", the map marks the next mission, \"Paradise Mercifully Departed\", as given by Bill, but that mission begins automatically once the walk is over, so the player never needs the marker.",
            "À la fin de \"Hell Hath No Fury\", la carte signale la mission suivante, \"Paradise Mercifully Departed\", comme confiée par Bill ; or cette mission démarre toute seule à la fin de la marche, et le joueur n'a jamais besoin du marqueur."),
        two("In \"The Delights of Van Horn\", if Arthur kills a civilian with the rifle, Bill scolds him afterwards.",
            "Dans \"The Delights of Van Horn\", si Arthur abat un civil au fusil, Bill le lui reproche ensuite."),
        two("In \"Red Dead Redemption\", Bill and Javier never show up as allies on the minimap during the escape from the caves.",
            "Dans \"Red Dead Redemption\", Bill et Javier n'apparaissent jamais comme alliés sur la mini-carte pendant la fuite hors des grottes."),
    ]},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("Rains Fall uses the word \"implore\" in \"My Last Boy\" (1899), trying to hold back Eagle Flies with John nearby, as John does to Bill at Fort Mercer in 1911. Neither plea works.",
            "Rains Fall emploie le mot \"implore\" (conjurer) dans \"My Last Boy\" (1899) pour tenter de retenir Eagle Flies, en présence de John, comme John le fera avec Bill à Fort Mercer en 1911. Aucune des deux supplications n'aboutit."),
        two("According to the Red Dead Wiki, a camp event in Red Dead Redemption 2 shows Bill present when Dutch warns John against being arrogant, the reproach Bill throws back at John in \"Spare the Rod, Spoil the Bandit\".",
            "D'après le Red Dead Wiki, un événement de camp de Red Dead Redemption 2 montre Bill présent quand Dutch reproche à John son arrogance, le reproche même que Bill renvoie à John dans \"Spare the Rod, Spoil the Bandit\"."),
        two("In \"Spare the Rod, Spoil the Bandit\", Bill's men use the character models of the Bollard Twins gang, and two Bollard members, Harry Dobbing and Irvin Pennick, also appear in \"The Assault on Fort Mercer\".",
            "Dans \"Spare the Rod, Spoil the Bandit\", les hommes de Bill reprennent les modèles de personnages de la bande des Bollard Twins, et deux membres des Bollard, Harry Dobbing et Irvin Pennick, apparaissent aussi dans \"The Assault on Fort Mercer\"."),
        two("Bill's hat usually hides that he is partly bald. Three situations show it: the hat falling when Allende pushes him out of the coach, a shot that knocks the hat off, and a seat at his table in multiplayer Poker or Liar's Dice.",
            "Son chapeau cache d'ordinaire que Bill est en partie chauve. Trois situations le révèlent : le chapeau qui tombe quand Allende le pousse hors de la diligence, un tir qui fait sauter le chapeau, et une partie de poker ou de poker menteur à sa table en multijoueur."),
        two("If the player lassoes Bill while Allende pins him down, Reyes shoots both men, which can sometimes make the mission impossible to complete. In rare cases, when John shoots Bill, Reyes does not shoot Allende at once: Allende begs, runs into the brush and is shot in the back.",
            "Si le joueur prend Bill au lasso pendant qu'Allende le plaque au sol, Reyes abat les deux hommes, ce qui peut parfois bloquer la mission. Plus rarement, quand John tire sur Bill, Reyes n'abat pas Allende tout de suite : celui-ci supplie, s'enfuit dans les broussailles et reçoit une balle dans le dos."),
        two("Banditos already hold part of Fort Mercer before \"The Assault on Fort Mercer\", and the fort later becomes their hideout. Across the game's modes, the fort is held by five different groups: Bill's gang and the Banditos in the story, the Bollard Twins gang in Free Roam, criminals in cooperative mode and the U.S. Army in Undead Nightmare.",
            "Des Banditos occupent déjà une partie de Fort Mercer avant \"The Assault on Fort Mercer\", et le fort devient ensuite leur repaire. Selon les modes de jeu, le fort est tenu par cinq groupes différents : la bande de Bill puis les Banditos dans l'histoire, la bande des Bollard Twins en Free Roam, des criminels en mode coopératif et l'armée américaine dans Undead Nightmare."),
    ]},
    {"h4": two("Undead Nightmare", "Undead Nightmare")},
    {"ul": [
        two("Bill does not appear in Undead Nightmare. John mentions him in a conversation with the Mother Superior at Las Hermanas.",
            "Bill n'apparaît pas dans Undead Nightmare. John parle de lui lors d'une conversation avec la mère supérieure de Las Hermanas."),
        two("In Blackwater, one of the writings on the walls reads \"Things are different now\". Bill says those words to John at Fort Mercer, moments before one of his men shoots John.",
            "À Blackwater, l'une des inscriptions sur les murs proclame \"Things are different now\" (les choses ont changé). Ce sont les mots que Bill adresse à John à Fort Mercer, juste avant qu'un de ses hommes ne lui tire dessus."),
    ]},
]

BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Bill became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010 on Xbox Live and PlayStation Network. The pack also added Poker, Liar's Dice and horse races. Players select Bill in the Damnation section of the Outfitter. His model wears a regular gunbelt with a holster, which he does not have in the story. According to the Red Dead Wiki, most of his multiplayer lines are aimed at John.",
              "Bill devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010 sur Xbox Live et PlayStation Network. Ce pack ajoute aussi le poker, le poker menteur et les courses de chevaux. On choisit Bill dans la section Damnation de l'Outfitter. Son modèle porte un vrai ceinturon avec étui, qu'il n'a pas dans l'histoire. D'après le Red Dead Wiki, la plupart de ses répliques en multijoueur visent John.")},
    {"p": two("The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the Bill Williamson model is not available in them. In Red Dead Online, the Dedham outfit is based on one of Bill's main outfits from Red Dead Redemption 2.",
              "Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle Bill Williamson n'y est donc pas disponible. Dans Red Dead Online, la tenue Dedham s'inspire de l'une des tenues principales de Bill dans Red Dead Redemption 2.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released promotional artwork of Bill for Red Dead Redemption, and new official artwork for Red Dead Redemption 2. The second trailer of Red Dead Redemption 2, released on September 28, 2017, shows him walking away from the burning Braithwaite Manor with Arthur and Hosea. The third trailer, released on May 2, 2018, also features him. On September 6, 2018, Rockstar posted the portraits and character descriptions of the gang's members on Twitter, Bill among them; in the composite of the series he stands in the back row, next to Charles.",
              "Rockstar a diffusé une illustration promotionnelle de Bill pour Red Dead Redemption, puis une nouvelle illustration officielle pour Red Dead Redemption 2. La deuxième bande-annonce de Red Dead Redemption 2, publiée le 28 septembre 2017, le montre s'éloignant de Braithwaite Manor en flammes avec Arthur et Hosea. La troisième, publiée le 2 mai 2018, le montre aussi. Le 6 septembre 2018, Rockstar publie sur Twitter les portraits et les descriptions des membres du gang, dont les siens ; dans la composition réunissant la série, il figure au dernier rang, à côté de Charles.")},
]
