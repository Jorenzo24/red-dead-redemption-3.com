"""Javier Escuella, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched via the MediaWiki API, saved in scratchpad
cov/javier/ and cov/javier/m/):
- Red Dead Wiki EN "Javier Escuella" (Mission Appearances, Notable Murders Committed,
  Quotes, Trivia, Gallery captions) and FR "Javier Escuella" (Apparitions dans les
  missions, Anecdotes).
- Mission pages: Enter, Pursued by a Memory; Old Friends; Who the Hell is Leviticus
  Cornwall?; Eastward Bound; Americans at Rest; The First Shall Be Last; A Strange
  Kindness; Horse Flesh for Dinner; Blood Feuds, Ancient and Modern; The Battle of Shady
  Belle; A Fine Night of Debauchery; Banking, The Old American Art; Lost and Not Quite
  Found; Welcome to the New World; A Kind and Benevolent Despot; Hell Hath No Fury;
  Paradise Mercifully Departed; Fleeting Joy; That's Murfree Country; A Rage Unleashed;
  My Last Boy; Our Best Selves; Red Dead Redemption (mission); companion activities
  Rob a Homestead (Javier Escuella) and Fishing (Javier Escuella); RDR1: The Gates of
  El Presidio, The Assault on Fort Mercer.
- Transcripts "/dialogues": Enter, Pursued by a Memory; Old Friends; Who the Hell is
  Leviticus Cornwall?; Eastward Bound; Americans at Rest; The First Shall Be Last; Red
  Dead Redemption (mission); The Gates of El Presidio; The Assault on Fort Mercer;
  Bear One Another's Burdens. Every quote is checked word for word against one of them,
  except the Swanson camp line (camp events page), the two RDR1 "wounded" chase lines and
  the multiplayer lines, which come from the character page's quote list. Added 18 Oct 2026
  from the El Presidio transcript: "I've always loved you, even now", three chase taunts,
  the "One day" exchange and John's "unless they choose to hang you" (in a src context). Where the quote list and the El Presidio
  transcript differ ("Go back to your farm, John!" vs "Get back to your farm!"), the
  transcript wording is used.
- Real world: Myths and Mavericks Bonus Pack, announced for September (Engadget, July
  27, 2011) and released free on September 13, 2011 for PlayStation 3 and Xbox 360,
  with Javier among the new character models (fan site iRedDead, roster listing).
  RDR2 trailer and portrait dates as established in charles_C / hosea_C / micah_C; RDR1
  ports (PS4 and Switch, August 17, 2023; PC, October 29, 2024) without multiplayer, as
  in bill_C.
Ownership (FIX_RULES): left to other parts: Origins and the 1907/1914 newspapers, the
1914 "eliminated" mention and John's "They're all dead" line (A); official descriptions,
John's "torn man" / "passion, but no love" assessment, camp scenes (Micah punch, Bill
"greaser" knife, Sean "fillet", Swanson prayer, Kieran, songs on the guitar), fishing
skill, weapons and horse, appearance (B); Gabriel Sloyer's standoff choice and his
father, Antonio Jaramillo, cut content (D). Quotes do not repeat B's "In his own words"
lines (snow, longest ride, rainbow). Trivia keeps only facts found nowhere else (fact-check
of 18 Oct 2026: Wiethoff pronunciation, New Game icon, poisoned knives, wanted poster,
"cabron", Abigail "creep", knife holster cut as duplicates). Marketing only says the
character descriptions were published; the text is quoted in B.
Excluded: the "foreshadowing" readings (Swanson's "doomed", "if the situation were
reversed"), the wanted poster read as pride, the guess that Javier rode off with the draft
horses in Outlaws from the West, the guess that he and Bill fled together, the "escollo"
reading of his surname, the daughter-continuity theory built on "rot in hell", the
"possibly an oversight" gun-aim frame at Beaver Hollow, the Zapata inspiration claim
(no source given), the revolver modelled on a Smith & Wesson of the 1893 exposition
(source page unreachable, and weapons belong to B), the Banking side-entrance post
(character page only, absent from the mission page), the FR cannon trick at El Presidio
(effect unclear).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]
K = lambda name, mission, en, fr: [name, mission, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C23 = two("2 or 3", "2 ou 3")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 23 story missions of Red Dead Redemption 2 for Javier, from the search for John in the Grizzlies to the standoff at Beaver Hollow, plus two companion activities: a homestead robbery and a fishing trip with Arthur. The French edition also counts 23 story missions, but its list is not the same: it adds \"Dear Uncle Tacitus\", the crossing back from Guarma, leaves out \"Lost and Not Quite Found\" and gives no companion activity. Javier appears in no mission of the epilogue. He gives Arthur two story missions, \"Americans at Rest\" and \"The First Shall Be Last\". In Red Dead Redemption, the wiki lists one mission, \"The Gates of El Presidio\". Javier is never playable in either story mode.",
              "Le Red Dead Wiki anglais recense 23 missions principales de Red Dead Redemption 2 pour Javier, de la recherche de John dans les Grizzlies jusqu'à l'affrontement de Beaver Hollow, plus deux activités de compagnon : le cambriolage d'une ferme et une partie de pêche avec Arthur. L'édition française compte aussi 23 missions, mais sa liste n'est pas identique : elle ajoute \"Dear Uncle Tacitus\", la traversée de retour depuis Guarma, omet \"Lost and Not Quite Found\" et ne mentionne aucune activité de compagnon. Javier n'apparaît dans aucune mission de l'épilogue. C'est lui qui confie à Arthur deux missions de l'histoire, \"Americans at Rest\" et \"The First Shall Be Last\". Pour Red Dead Redemption, le wiki ne retient qu'une mission, \"The Gates of El Presidio\". Javier n'est jouable dans le mode histoire d'aucun des deux jeux.")},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Javier's role", "Rôle de Javier")], "rows": [
        M("Enter, Pursued by a Memory", C1,
          "Asked by Hosea to ride out with Arthur to look for John, he hands Arthur a Sawed-Off Shotgun. He reads the tracks in the snow, fires a shot into the air to locate John and carries him to his horse while Arthur deals with the wolves.",
          "Hosea lui demande de partir avec Arthur à la recherche de John ; il remet à Arthur un fusil à canon scié. Il suit les traces dans la neige, tire un coup de feu en l'air pour localiser John et le porte jusqu'à son cheval pendant qu'Arthur s'occupe des loups."),
        M("Old Friends", C1,
          "With Arthur and Lenny, he breaks up the fight between Micah and Bill in the men's cabin. During the raid on the O'Driscoll camp, Dutch posts him on a hill with [[lenny-summers|Lenny]] to pick off enemies, then the two bring the horses down to the camp.",
          "Avec Arthur et Lenny, il sépare Micah et Bill, qui se battent dans la cabane des hommes. Lors de l'attaque du camp O'Driscoll, Dutch le poste sur une hauteur avec [[lenny-summers|Lenny]] pour abattre les ennemis à distance, puis tous deux descendent les chevaux jusqu'au camp."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "Assigned by Dutch to the two front cars with Lenny. When the dynamite fails, he jumps onto the train from the top of the tunnel with Arthur and Lenny, misses and is left behind. He rides in later with Dutch, Bill, Charles and Micah to help with the remaining guards.",
          "Dutch lui confie les deux premières voitures avec Lenny. Quand la dynamite ne part pas, il saute sur le train depuis le haut du tunnel avec Arthur et Lenny, rate son saut et reste en arrière. Il revient ensuite à cheval avec Dutch, Bill, Charles et Micah pour aider à venir à bout des derniers gardes."),
        M("Eastward Bound", C1,
          "Rides next to the wagon of Bill and Charles on the way down from the mountains. When the wheel of Arthur and [[hosea-matthews|Hosea]]'s wagon comes off, he offers to help. He waits at the entrance of Horseshoe Overlook, jumps onto the back of the wagon and tells Hosea the spot is a good one.",
          "Accompagne à cheval le chariot de Bill et Charles pendant la descente de la montagne. Quand la roue du chariot d'Arthur et d'[[hosea-matthews|Hosea]] se détache, il propose son aide. Il attend à l'entrée de Horseshoe Overlook, saute à l'arrière du chariot et assure à Hosea que l'endroit est bon."),
        M("Americans at Rest", C2,
          "Mission giver. He drinks at Smithfield's Saloon in Valentine with [[charles-smith|Charles]] and two women until Bill starts a brawl. Tommy beats him until Arthur steps in. Dutch then sends him with [[josiah-trelawny|Trelawny]] to look for news of [[sean-macguire|Sean]].",
          "Donneur de mission. Il boit au Smithfield's Saloon de Valentine avec [[charles-smith|Charles]] et deux femmes jusqu'à ce que Bill déclenche une bagarre. Tommy le roue de coups jusqu'à l'intervention d'Arthur. Dutch l'envoie ensuite avec [[josiah-trelawny|Trelawny]] chercher des nouvelles de [[sean-macguire|Sean]]."),
        M("The First Shall Be Last", C2,
          "Mission giver. From a cliff above Blackwater, he reports Pinkertons, bounty hunters and wanted posters of Dutch and Hosea. He kills one of the two bounty hunters by the river while Trelawny distracts them, fights up the canyon with Arthur and escorts the freed Sean back to camp.",
          "Donneur de mission. Depuis une falaise qui domine Blackwater, il signale les Pinkerton, les chasseurs de primes et les avis de recherche de Dutch et d'Hosea. Il élimine l'un des deux chasseurs de primes postés au bord de la rivière pendant que Trelawny détourne leur attention, remonte le canyon en combattant avec Arthur et ramène au camp Sean, enfin libéré."),
        M("A Strange Kindness", C2,
          "Listed by the wiki. The mission page gives him no individual action.",
          "Cité par le wiki. La page de la mission ne lui attribue aucune action propre."),
        M("Horse Flesh for Dinner", C3,
          "Hired with Arthur and John by [[tavish-gray|Tavish Gray]] to steal the Braithwaites' prize horses. At the stable, he can knock out the stablehand if Arthur does not deal with him. He ties the three horses together and rides the lead one during the escape. The horses sell for 700 dollars instead of the 5,000 promised.",
          "Engagé avec Arthur et John par [[tavish-gray|Tavish Gray]] pour voler les chevaux de prix des Braithwaite. À l'écurie, il peut assommer le palefrenier si Arthur ne s'en charge pas. Il attache les trois chevaux ensemble et monte celui de tête pendant la fuite. Les bêtes sont vendues 700 dollars, loin des 5 000 promis."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Rides with Dutch, Arthur, Hosea, John, Charles, Bill and Lenny to Braithwaite Manor to get [[jack-marston|Jack]] back.",
          "Accompagne Dutch, Arthur, Hosea, John, Charles, Bill et Lenny à Braithwaite Manor pour récupérer [[jack-marston|Jack]]."),
        M("The Battle of Shady Belle", C3,
          "Listed by the wiki. The mission page gives him no individual action.",
          "Cité par le wiki. La page de la mission ne lui attribue aucune action propre."),
        M("A Fine Night of Debauchery", C4,
          "Boards the riverboat with Arthur, Trelawny and [[leopold-strauss|Strauss]], disguised in a guard's uniform. He leads Arthur and the pit boss to the vault, knocks out a guard and holds the pit boss at gunpoint. When the guard whose clothes he took raises the alarm, he fights to the deck with the others and jumps into the river.",
          "Monte à bord du bateau à aubes avec Arthur, Trelawny et [[leopold-strauss|Strauss]], déguisé avec l'uniforme d'un garde. Il conduit Arthur et le chef de salle jusqu'au coffre, assomme un garde et tient le chef de salle en joue. Quand le garde dont il a pris les vêtements donne l'alerte, il gagne le pont avec les autres en combattant et saute dans le fleuve."),
        M("Banking, The Old American Art", C4,
          "Takes part in the robbery of the Lemoyne National Bank. He escapes over the rooftops, hides with Dutch, Arthur, Micah, Bill and Charles until nightfall and boards the ship at the docks.",
          "Participe au braquage de la Lemoyne National Bank. Il s'enfuit par les toits, se cache avec Dutch, Arthur, Micah, Bill et Charles jusqu'à la nuit et embarque sur les quais."),
        M("Lost and Not Quite Found", C4,
          "Caught in the storm aboard the Antenor. He reaches a lifeboat with Dutch, Micah and Bill, while falling crates cut Arthur off from them.",
          "Pris dans la tempête à bord de l'Antenor. Il gagne un canot de sauvetage avec Dutch, Micah et Bill, tandis que la chute de caisses coupe Arthur du groupe."),
        M("Welcome to the New World", C5,
          "Found by Arthur at a campfire on the beach with Dutch, Micah and Bill. Chained by Levi Simon's militia, he is shot in the leg and recaptured when Hercule Fontaine's ambush frees the others.",
          "Retrouvé par Arthur autour d'un feu, sur la plage, avec Dutch, Micah et Bill. Enchaîné par la milice de Levi Simon, il est touché à la jambe et repris quand l'embuscade d'Hercule Fontaine libère les autres."),
        M("A Kind and Benevolent Despot", C5,
          "Dragged behind a donkey and mocked by [[alberto-fussar|Fussar]] and his soldiers outside Aguasdulces. Dutch and Arthur set fire to the refinery as a diversion and free him; Dutch carries him, unconscious, through the cane fields.",
          "Traîné derrière un âne et raillé par [[alberto-fussar|Fussar]] et ses soldats devant Aguasdulces. Dutch et Arthur incendient la raffinerie pour faire diversion et le libèrent ; Dutch l'emporte, inconscient, à travers les champs de canne."),
        M("Hell Hath No Fury", C5,
          "Absent from the battle at Cinco Torres while he recovers. Once it is over, Dutch and Bill go to fetch him.",
          "Absent de la bataille de Cinco Torres, le temps de se remettre. Une fois le combat terminé, Dutch et Bill vont le chercher."),
        M("Paradise Mercifully Departed", C5,
          "Stays behind under Bill's guard, still recovering, while the others destroy the gun batteries. He then sails back to America with the gang.",
          "Reste en arrière sous la garde de Bill, encore convalescent, pendant que les autres détruisent les batteries. Il repart ensuite vers l'Amérique avec le gang."),
        M("Fleeting Joy", C5,
          "Reaches the gang's camp at Lakay with Micah, off screen, before Dutch and Bill arrive.",
          "Rejoint le camp du gang à Lakay avec Micah, hors champ, avant l'arrivée de Dutch puis de Bill."),
        M("That's Murfree Country", C5,
          "Listed by the wiki for the gang's arrival at Beaver Hollow. The mission page gives him no individual action.",
          "Cité par le wiki pour l'installation du gang à Beaver Hollow. La page de la mission ne lui attribue aucune action propre."),
        M("A Rage Unleashed", C6,
          "Escorts Eagle Flies into Beaver Hollow with [[karen-jones|Karen]], when the young Wapiti comes to say the Army has taken his tribe's horses.",
          "Escorte Eagle Flies jusqu'à Beaver Hollow avec [[karen-jones|Karen]], quand le jeune Wapiti vient annoncer que l'armée a confisqué les chevaux de sa tribu."),
        M("My Last Boy", C6,
          "Listed by the wiki for the battle at the Cornwall oil fields alongside the Wapiti.",
          "Cité par le wiki pour la bataille des champs pétrolifères de Cornwall, aux côtés des Wapiti."),
        M("Our Best Selves", C6,
          "Takes part in the army train robbery. After John is shot and falls from the train, Dutch says he will go back for him and leaves with Javier, Micah and Joe. The four return without John, and Dutch and Micah tell Arthur he did not make it.",
          "Participe à l'attaque du train de l'armée. Après la chute de John, touché par balle, Dutch annonce qu'il va le chercher et repart avec Javier, Micah et Joe. Les quatre reviennent sans lui, et Dutch et Micah annoncent à Arthur que John n'a pas survécu."),
        M("Red Dead Redemption", C6,
          "Arrives during the standoff at Beaver Hollow to warn that Pinkertons are coming; the warning distracts [[susan-grimshaw|Susan]], and Micah shoots her. Arthur asks him and Bill to think for themselves. He sides with Dutch, and he is not among the men who chase Arthur and John once the Pinkertons attack.",
          "Surgit pendant l'affrontement de Beaver Hollow pour prévenir que les Pinkerton arrivent ; l'avertissement détourne l'attention de [[susan-grimshaw|Susan]], que Micah abat. Arthur lui demande, ainsi qu'à Bill, de réfléchir par eux-mêmes. Il se range derrière Dutch, et ne fait pas partie des hommes qui poursuivent Arthur et John quand les Pinkerton attaquent."),
    ]}},
    {"h4": two("Red Dead Redemption 2: companion activities", "Red Dead Redemption 2 : activités de compagnon")},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Javier's role", "Rôle de Javier")], "rows": [
        M("Rob a Homestead", C23,
          "Offered at Horseshoe Overlook or Clemens Point, once \"The First Shall Be Last\" is done. He takes Arthur to Chez Porter, warns him that the family speaks its own kind of English, sets fire to the stables to draw them out and shoots it out with them. He then has Arthur help him move a crate that hides the stash. Reward: 175 dollars.",
          "Proposée à Horseshoe Overlook ou à Clemens Point, une fois \"The First Shall Be Last\" terminée. Il emmène Arthur à Chez Porter, le prévient que la famille parle un anglais bien à elle, met le feu aux écuries pour faire sortir ses membres et les affronte à l'arme à feu. Il demande ensuite à Arthur de l'aider à déplacer une caisse qui cache le magot. Gain : 175 dollars."),
        M("Fishing", C3,
          "Available after \"The New South\". He rides with Arthur to Ringneck Creek to catch smallmouth bass. When Arthur has no luck, Javier gives him crickets as bait, then heads home; the player can keep fishing or ride back with him.",
          "Disponible après \"The New South\". Il part avec Arthur à Ringneck Creek pêcher l'achigan à petite bouche. Comme Arthur ne prend rien, Javier lui donne des grillons comme appât, puis rentre ; le joueur peut continuer à pêcher ou repartir avec lui."),
    ]}},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"p": two("Javier is named long before he appears. In \"The Assault on Fort Mercer\" (Act I), a captured gang member says Bill has fled to Mexico, and John concludes that he has gone to see Javier Escuella. Through Act II, John looks for both men in Nuevo Paraíso, where Colonel Allende is sheltering them.",
              "Javier est nommé bien avant d'apparaître. Dans \"The Assault on Fort Mercer\" (acte I), un membre de la bande fait prisonnier révèle que Bill a fui au Mexique, et John en déduit qu'il est allé retrouver Javier Escuella. Pendant tout l'acte II, John recherche les deux hommes au Nuevo Paraíso, où le colonel Allende les protège.")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Javier's role", "Rôle de Javier")], "rows": [
        M("The Gates of El Presidio", A2,
          "Found by John in a storeroom of El Presidio during the rebel assault. He offers to give up Bill and Dutch, pushes a crate onto John and escapes through a window. The player then either kills him or captures him alive; dead or captured, he is handed over to [[edgar-ross|Ross]] and [[archer-fordham|Fordham]] at the border.",
          "Retrouvé par John dans une réserve d'El Presidio pendant l'assaut des rebelles. Il propose de livrer Bill et Dutch, renverse une caisse sur John et s'enfuit par une fenêtre. Le joueur choisit ensuite de l'abattre ou de le capturer vivant ; mort ou prisonnier, il est remis à [[edgar-ross|Ross]] et à [[archer-fordham|Fordham]] près de la frontière."),
    ]}},
    # ---------------------------------------------------------- notable kills
    {"h3": two("Notable people Javier kills", "Personnages notables tués par Javier")},
    {"p": two("The Red Dead Wiki lists the members of the Porter family as Javier's only notable murders. The mission page of \"Rob a Homestead\" names five of them, each killed by Arthur or by Javier depending on how the fight goes. The table adds the bounty hunter killed in \"The First Shall Be Last\". O'Driscolls, Braithwaite guards, Grand Korrigan guards and soldiers killed in gunfights alongside Arthur are not listed one by one. In \"Horse Flesh for Dinner\", Javier only knocks out the stablehand. He kills no one in Red Dead Redemption.",
              "Le Red Dead Wiki ne retient comme meurtres notables de Javier que les membres de la famille Porter. La page de \"Rob a Homestead\" en nomme cinq, tués par Arthur ou par Javier selon le déroulé du combat. Le tableau y ajoute le chasseur de primes abattu dans \"The First Shall Be Last\". Les O'Driscoll, les gardes des Braithwaite et du Grand Korrigan et les soldats tués aux côtés d'Arthur lors des fusillades ne sont pas détaillés. Dans \"Horse Flesh for Dinner\", Javier se contente d'assommer le palefrenier. Il ne tue personne dans Red Dead Redemption.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K(two("Pappy, Newt, Finney, Mal and Edie Porter", "Pappy, Newt, Finney, Mal et Edie Porter"), "Rob a Homestead",
          "Determinant. Each of the five can fall to Arthur or to Javier in the gunfight that follows the fire in the stables. Other, unnamed members of the family are killed by the two men.",
          "Selon le joueur. Chacun des cinq peut tomber sous les balles d'Arthur ou de Javier lors de la fusillade qui suit l'incendie des écuries. D'autres membres de la famille, sans nom, sont tués par les deux hommes."),
        K(two("Skelding bounty hunter", "Chasseur de primes de Skelding"), "The First Shall Be Last",
          "Storyline. One of the two men guarding the river, killed with a knife by Javier while Trelawny fakes a seizure and Arthur takes the other.",
          "Histoire. L'un des deux hommes qui gardent la rivière, tué au couteau par Javier pendant que Trelawny simule une crise et qu'Arthur s'occupe de l'autre."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. The camp line comes from the Red Dead Wiki's camp events page; two lines from the chase at El Presidio and the multiplayer lines come from its quote list, which names no mission for most of them. The other lines are checked against the mission transcripts. Lines already quoted in the Personality section are not repeated here.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. La réplique du camp provient de la page du Red Dead Wiki consacrée aux scènes de camp ; deux répliques de la poursuite d'El Presidio et celles du multijoueur sont tirées de sa liste de citations, qui ne précise le plus souvent pas de mission. Les autres sont vérifiées sur les transcriptions des missions. Les répliques déjà citées dans la section Personnalité ne sont pas reprises ici.")},
    {"h4": two("Red Dead Redemption 2, chapter 1", "Red Dead Redemption 2, chapitre 1")},
    {"quotes": [
        {"q": two("We had the money, it seemed fine, then suddenly they were everywhere.",
                  "We had the money, it seemed fine, then suddenly they were everywhere."),
         "src": two("Enter, Pursued by a Memory (RDR2, chapter 1), to Arthur, who asks what happened on the ferry in Blackwater",
                    "Enter, Pursued by a Memory (RDR2, chapitre 1), à Arthur, qui lui demande ce qui s'est passé sur le ferry de Blackwater. Traduction : « On avait l'argent, tout avait l'air d'aller, et d'un coup ils étaient partout. »")},
        {"q": two("Dutch killed a girl in a... bad way, but it was a bad situation.",
                  "Dutch killed a girl in a... bad way, but it was a bad situation."),
         "src": two("Enter, Pursued by a Memory (RDR2, chapter 1), to Arthur, about Heidi McCourt; Arthur answers that it is not like Dutch",
                    "Enter, Pursued by a Memory (RDR2, chapitre 1), à Arthur, à propos d'Heidi McCourt ; Arthur répond que ça ne ressemble pas à Dutch. Traduction : « Dutch a tué une fille d'une... sale manière, mais la situation était mauvaise. »")},
        {"q": two("You'll be fine. It's just like a... a dog bite.",
                  "You'll be fine. It's just like a... a dog bite."),
         "src": two("Enter, Pursued by a Memory (RDR2, chapter 1), to John, wounded by the wolves, on the ride down; John replies that he knew a man who died an hour after a dog bite",
                    "Enter, Pursued by a Memory (RDR2, chapitre 1), à John, blessé par les loups, pendant la descente ; John répond qu'il a connu un homme mort une heure après une morsure de chien. Traduction : « Tu vas t'en remettre. C'est comme une... une morsure de chien. »")},
        {"q": two("Ay, careful idiotas, it's his leg.",
                  "Ay, careful idiotas, it's his leg."),
         "src": two("Enter, Pursued by a Memory (RDR2, chapter 1), to Bill and Lenny, who pull John off the horse at Colter",
                    "Enter, Pursued by a Memory (RDR2, chapitre 1), à Bill et Lenny, qui descendent John de cheval sans ménagement à Colter. Traduction : « Ay, doucement, idiotas, c'est sa jambe. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, chapters 2 and 6", "Red Dead Redemption 2, chapitres 2 et 6")},
    {"quotes": [
        {"q": two("Well, I must say... you got a fine way with the women, amigo.",
                  "Well, I must say... you got a fine way with the women, amigo."),
         "src": two("Americans at Rest (RDR2, chapter 2), to Arthur, who has just driven off the two women at the bar",
                    "Americans at Rest (RDR2, chapitre 2), à Arthur, qui vient de faire fuir les deux femmes du comptoir. Traduction : « Eh bien, je dois dire... tu sais t'y prendre avec les femmes, amigo. »")},
        {"q": two("Place is crawling with Pinkertons... bounty hunters... pictures of Dutch and Hosea.",
                  "Place is crawling with Pinkertons... bounty hunters... pictures of Dutch and Hosea."),
         "src": two("The First Shall Be Last (RDR2, chapter 2), to Arthur, about Blackwater",
                    "The First Shall Be Last (RDR2, chapitre 2), à Arthur, à propos de Blackwater. Traduction : « La ville grouille de Pinkerton... de chasseurs de primes... de portraits de Dutch et d'Hosea. »")},
        {"q": two("There's Pinkertons coming, fast.",
                  "There's Pinkertons coming, fast."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), during the standoff at Beaver Hollow, just before Micah shoots Susan",
                    "Red Dead Redemption (RDR2, chapitre 6), pendant l'affrontement de Beaver Hollow, juste avant que Micah n'abatte Susan. Traduction : « Les Pinkerton arrivent, et vite. »")},
    ]},
    {"h4": two("Camp", "Camp")},
    {"quotes": [
        {"q": two("Oh, well, in that case, I'm sure there's priests who will happily take your confession.",
                  "Oh, well, in that case, I'm sure there's priests who will happily take your confession."),
         "src": two("Camp (RDR2), to the Reverend [[orville-swanson|Swanson]], who has told him it is \"not too late to repent\"",
                    "Au camp (RDR2), au révérend [[orville-swanson|Swanson]], qui vient de lui dire qu'il n'est \"not too late to repent\" (pas trop tard pour se repentir). Traduction : « Ah, dans ce cas, je suis sûr que des prêtres se feront un plaisir d'entendre ta confession. »")},
    ]},
    {"h4": two("Red Dead Redemption, Act II", "Red Dead Redemption, acte II")},
    {"quotes": [
        {"q": two("Hello, brother. It's good to see you. I heard you was coming. You took your time, no?",
                  "Hello, brother. It's good to see you. I heard you was coming. You took your time, no?"),
         "src": two("The Gates of El Presidio (RDR1, Act II), to John, who finds him in a storeroom of the fort",
                    "The Gates of El Presidio (RDR1, acte II), à John, qui le découvre dans une réserve du fort. Traduction : « Salut, mon frère. Content de te voir. J'avais entendu dire que tu venais. Tu as pris ton temps, hein ? »")},
        {"q": two("So now you do the government's work?",
                  "So now you do the government's work?"),
         "src": two("The Gates of El Presidio (RDR1, Act II), to John, who answers: \"And what do you do? You just work for a different government.\"",
                    "The Gates of El Presidio (RDR1, acte II), à John, qui répond : \"And what do you do? You just work for a different government.\" (et toi, tu fais quoi ? Tu travailles juste pour un autre gouvernement). Traduction : « Alors maintenant, tu fais le sale boulot du gouvernement ? »")},
        {"q": two("We thought you was dead, brother. I promise. I'm telling the truth. Besides, I can give you Bill. And Dutch... Dutch is in Colombia. I can take you straight to him.",
                  "We thought you was dead, brother. I promise. I'm telling the truth. Besides, I can give you Bill. And Dutch... Dutch is in Colombia. I can take you straight to him."),
         "src": two("The Gates of El Presidio (RDR1, Act II), to John, who has just told him that \"it might as well be you\"",
                    "The Gates of El Presidio (RDR1, acte II), à John, qui vient de lui dire \"it might as well be you\" (autant que ce soit toi). Traduction : « On te croyait mort, mon frère. Je te le jure. Je dis la vérité. Et puis je peux te livrer Bill. Et Dutch... Dutch est en Colombie. Je peux t'emmener droit à lui. »")},
        {"q": two("You got it all wrong, brother. I've always loved you, even now.",
                  "You got it all wrong, brother. I've always loved you, even now."),
         "src": two("The Gates of El Presidio (RDR1, Act II), to John, who has asked: \"You left me to die, to save your own skin and now you expect me to care about you?\" Javier then pushes a crate onto him and leaps out of a window",
                    "The Gates of El Presidio (RDR1, acte II), à John, qui vient de lui demander : \"You left me to die, to save your own skin and now you expect me to care about you?\" (tu m'as laissé mourir pour sauver ta peau, et maintenant tu voudrais que je me soucie de toi ?). Javier renverse ensuite une caisse sur lui et saute par la fenêtre. Traduction : « Tu n'as rien compris, mon frère. Je t'ai toujours aimé, même aujourd'hui. »")},
        {"q": two("Go back to your farm, John!",
                  "Go back to your farm, John!"),
         "src": two("The Gates of El Presidio (RDR1, Act II), after jumping out of the window",
                    "The Gates of El Presidio (RDR1, acte II), après avoir sauté par la fenêtre. Traduction : « Retourne à ta ferme, John ! »")},
        {"q": two("You do not have the heart to kill me!",
                  "You do not have the heart to kill me!"),
         "src": two("The Gates of El Presidio (RDR1, Act II), shouted at John during the chase",
                    "The Gates of El Presidio (RDR1, acte II), lancé à John pendant la poursuite. Traduction : « Tu n'as pas le cran de me tuer ! »")},
        {"q": two("You won't get me alive, John!",
                  "You won't get me alive, John!"),
         "src": two("The Gates of El Presidio (RDR1, Act II), shouted at John during the chase",
                    "The Gates of El Presidio (RDR1, acte II), lancé à John pendant la poursuite. Traduction : « Tu ne m'auras pas vivant, John ! »")},
        {"q": two("You were always weak, John!",
                  "You were always weak, John!"),
         "src": two("The Gates of El Presidio (RDR1, Act II), shouted at John during the chase",
                    "The Gates of El Presidio (RDR1, acte II), lancé à John pendant la poursuite. Traduction : « Tu as toujours été faible, John ! »")},
        {"q": two("Tell...tell your wife it's the Lord I praise.",
                  "Tell...tell your wife it's the Lord I praise."),
         "src": two("The Gates of El Presidio (RDR1, Act II), when wounded during the chase (Red Dead Wiki quote list)",
                    "The Gates of El Presidio (RDR1, acte II), une fois blessé pendant la poursuite (liste de citations du Red Dead Wiki). Traduction : « Dis... dis à ta femme que c'est le Seigneur que je loue. »")},
        {"q": two("Finish me, you coward!",
                  "Finish me, you coward!"),
         "src": two("The Gates of El Presidio (RDR1, Act II), when wounded during the chase (Red Dead Wiki quote list)",
                    "The Gates of El Presidio (RDR1, acte II), une fois blessé pendant la poursuite (liste de citations du Red Dead Wiki). Traduction : « Achève-moi, espèce de lâche ! »")},
    ]},
    {"h4": two("Red Dead Redemption, Act II: if John captures him", "Red Dead Redemption, acte II : si John le capture")},
    {"quotes": [
        {"q": two("It's a little late for revenge, John.",
                  "It's a little late for revenge, John."),
         "src": two("The Gates of El Presidio (RDR1, Act II), hogtied, to John, who has just told him: \"You're going to be locked up for a hell of a long time, unless they choose to hang you.\"",
                    "The Gates of El Presidio (RDR1, acte II), ligoté, à John, qui vient de lui annoncer : \"You're going to be locked up for a hell of a long time, unless they choose to hang you.\" (tu vas rester enfermé un sacré bout de temps, à moins qu'ils décident de te pendre). Traduction : « C'est un peu tard pour la vengeance, John. »")},
        {"q": two("Go to hell, you pathetic fool. Dutch never liked you, you know?",
                  "Go to hell, you pathetic fool. Dutch never liked you, you know?"),
         "src": two("The Gates of El Presidio (RDR1, Act II), hogtied, to John, who has just called him and Bill \"two crazy men\"",
                    "The Gates of El Presidio (RDR1, acte II), ligoté, à John, qui vient de les traiter, Bill et lui, de \"two crazy men\" (deux cinglés). Traduction : « Va au diable, pauvre imbécile. Dutch ne t'a jamais aimé, tu sais ? »")},
        {"q": two("Ah, you piece of shit. I hope you sure know what you're doing, brother. You sold me out. Didn't that life we had mean nothing to you?",
                  "Ah, you piece of shit. I hope you sure know what you're doing, brother. You sold me out. Didn't that life we had mean nothing to you?"),
         "src": two("The Gates of El Presidio (RDR1, Act II), as John carries him into the fort's jail",
                    "The Gates of El Presidio (RDR1, acte II), pendant que John le conduit à la prison du fort. Traduction : « Ah, espèce d'ordure. J'espère que tu sais ce que tu fais, mon frère. Tu m'as vendu. La vie qu'on a eue, ça ne comptait donc pas pour toi ? »")},
        {"q": two("Ah, ah, you puto. Ah. One day, one day I promise you, you're gonna regret this.",
                  "Ah, ah, you puto. Ah. One day, one day I promise you, you're gonna regret this."),
         "src": two("The Gates of El Presidio (RDR1, Act II), in the cell, after John throws him onto the stone floor; John answers: \"One day is about all you got left.\"",
                    "The Gates of El Presidio (RDR1, acte II), dans la cellule, après que John l'a jeté sur le sol de pierre ; John répond : \"One day is about all you got left.\" (un jour, c'est à peu près tout ce qu'il te reste). Traduction : « Ah, ah, espèce de puto. Ah. Un jour, un jour, je te le promets, tu le regretteras. »")},
        {"q": two("What I knew was that you was always a puto. And you're still a puto!",
                  "What I knew was that you was always a puto. And you're still a puto!"),
         "src": two("The Gates of El Presidio (RDR1, Act II), in the cell, to John, who has said their old life \"was just an excuse and we all knew\"",
                    "The Gates of El Presidio (RDR1, acte II), dans la cellule, à John, qui vient de dire que leur ancienne vie \"was just an excuse and we all knew\" (n'était qu'un prétexte, et on le savait tous). Traduction : « Ce que je savais, c'est que tu as toujours été un puto. Et que tu es toujours un puto ! »")},
        {"q": two("Yeah, go with your puto!",
                  "Yeah, go with your puto!"),
         "src": two("The Gates of El Presidio (RDR1, Act II), his last line in the game in this branch, as Reyes calls John away",
                    "The Gates of El Presidio (RDR1, acte II), sa dernière réplique du jeu dans ce cas de figure, quand Reyes appelle John. Traduction : « C'est ça, va rejoindre ton puto ! »")},
    ]},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"quotes": [
        {"q": two("Hahahaha... you still hit like a child!",
                  "Hahahaha... you still hit like a child!"),
         "src": two("Red Dead Redemption multiplayer, line of the Javier Escuella character model",
                    "Multijoueur de Red Dead Redemption, réplique du modèle de personnage Javier Escuella. Traduction : « Ha ha ha ha... tu frappes toujours comme un gamin ! »")},
        {"q": two("So you think you're tough now, eh? Hahaha.",
                  "So you think you're tough now, eh? Hahaha."),
         "src": two("Red Dead Redemption multiplayer, line of the Javier Escuella character model",
                    "Multijoueur de Red Dead Redemption, réplique du modèle de personnage Javier Escuella. Traduction : « Alors comme ça, tu te crois costaud maintenant, hein ? Ha ha ha. »")},
    ]},
]

BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Across the series", "Dans toute la série")},
    {"ul": [
        two("His surname is close to \"escuela\", the Spanish word for school. A Rockstar character from Grand Theft Auto IV (2008), Manny Escuela, has a near identical name.",
            "Son nom de famille est proche de \"escuela\", qui signifie école en espagnol. Un personnage de Grand Theft Auto IV (2008), un autre jeu Rockstar, porte un nom presque identique : Manny Escuela."),
    ]},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"ul": [
        two("Javier rides with the caravan in the opening cutscene of \"Outlaws from the West\", but neither he nor his horse can be found at Colter during the mission. The gang's eight draft horses are not at Colter either.",
            "Javier chevauche avec le convoi dans la cinématique d'ouverture de \"Outlaws from the West\", mais ni lui ni son cheval ne se trouvent à Colter pendant la mission. Les huit chevaux de trait du gang n'y sont pas non plus."),
        two("In \"Enter, Pursued by a Memory\", a unique death scene plays if the player lets the wolves reach Javier and John.",
            "Dans \"Enter, Pursued by a Memory\", une scène de mort spécifique se déclenche si le joueur laisse les loups atteindre Javier et John."),
        two("One of the two women Javier drinks with before the brawl in \"Americans at Rest\" appears again in a scene of the end credits, with Edgar Ross and Archer Fordham.",
            "L'une des deux femmes avec qui Javier boit avant la bagarre de \"Americans at Rest\" réapparaît dans une scène du générique de fin, en compagnie d'Edgar Ross et d'Archer Fordham."),
        two("In \"Rob a Homestead\", Javier fights the Porters with whatever long gun he has on him, if any, rather than his custom revolver. Arthur's cough can be heard at the end of the activity, when the two men move the crate; the activity can be played as early as chapter 2.",
            "Dans \"Rob a Homestead\", Javier affronte les Porter avec l'arme longue qu'il a sur lui, s'il en a une, plutôt qu'avec son revolver personnalisé. La toux d'Arthur se fait entendre à la fin de l'activité, quand les deux hommes déplacent la caisse ; l'activité peut se jouer dès le chapitre 2."),
        two("The Lancaster Repeater Javier throws to Arthur in \"Banking, The Old American Art\" is Arthur's own, with any upgrades already applied.",
            "La Lancaster Repeater que Javier lance à Arthur dans \"Banking, The Old American Art\" est celle d'Arthur, avec les améliorations déjà installées."),
        two("In \"A Kind and Benevolent Despot\", opening fire on Fussar or his soldiers once Javier is seen being dragged by the donkey fails the mission, and a cutscene shows the guards killing Javier.",
            "Dans \"A Kind and Benevolent Despot\", ouvrir le feu sur Fussar ou ses soldats une fois que l'on a vu Javier traîné par l'âne fait échouer la mission ; une cinématique montre alors les gardes en train de l'abattre."),
        two("In \"Red Dead Redemption\", after Arthur and John come out of the caves, Bill and Javier are not among the riders who chase them, and neither appears on the minimap.",
            "Dans \"Red Dead Redemption\", une fois Arthur et John sortis des grottes, Bill et Javier ne font pas partie des cavaliers lancés à leur poursuite, et aucun des deux n'apparaît sur la mini-carte."),
    ]},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("Of the old gang members John hunts in 1911, Javier is the only one the player can deliver alive.",
            "Parmi les anciens du gang que John traque en 1911, Javier est le seul que le joueur peut livrer vivant."),
        two("The cuffs on a hogtied Javier are either copper or rusted iron.",
            "Une fois Javier ligoté, ses menottes sont soit en cuivre, soit en fer rouillé."),
        two("His 1911 outfit resembles those of Ramiro de la Torre and Benito Penagarza, in other colors and without their two bandoliers. He wears Mexican Cavalry boots, and his sombrero has a slightly broader brim than the Bandito Outfit's.",
            "Sa tenue de 1911 ressemble à celles de Ramiro de la Torre et de Benito Penagarza, dans d'autres couleurs et sans leurs deux cartouchières. Il porte des bottes de la cavalerie mexicaine, et le bord de son sombrero est un peu plus large que celui de la tenue Bandito."),
        two("Javier does not appear in Undead Nightmare.",
            "Javier n'apparaît pas dans Undead Nightmare."),
    ]},
]

BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Javier became a playable character model in the multiplayer mode of Red Dead Redemption with the Myths and Mavericks Bonus Pack. Engadget reported on July 27, 2011 that the pack would come out in September at no cost. It was released free on September 13, 2011 on PlayStation 3 and Xbox 360, with new character models, among them [[landon-ricketts|Landon Ricketts]], [[vincente-de-santa|Vincente de Santa]], [[nastas|Nastas]] and [[uncle|Uncle]], and new map locations for Shootout, Gang Shootout, Grab the Bag, Gold Rush, Hold Your Own and Stronghold. Players select Javier in the Revolution section of the Outfitter, where his model inspects a knife. The multiplayer model has a far narrower sombrero than his story outfit.",
              "Javier devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Myths and Mavericks Bonus Pack. Engadget annonce le 27 juillet 2011 que ce pack sortira en septembre, sans frais. Il est publié gratuitement le 13 septembre 2011 sur PlayStation 3 et Xbox 360, avec de nouveaux modèles de personnages, dont [[landon-ricketts|Landon Ricketts]], [[vincente-de-santa|Vincente de Santa]], [[nastas|Nastas]] et [[uncle|Uncle]], et de nouveaux lieux de jeu pour les modes Shootout, Gang Shootout, Grab the Bag, Gold Rush, Hold Your Own et Stronghold. On choisit Javier dans la section Revolution de l'Outfitter, où son modèle examine un couteau. Le sombrero du modèle multijoueur est nettement moins large que celui de sa tenue du mode histoire.")},
    {"p": two("The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the Javier Escuella model is not available in them. In Red Dead Online, the Zapatero outfit is based on one of Javier's outfits, and one of the saddles sold at the stables carries promotional artwork of him.",
              "Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle Javier Escuella n'y est donc pas disponible. Dans Red Dead Online, la tenue Zapatero s'inspire de l'une des tenues de Javier, et l'une des selles vendues à l'écurie porte une illustration promotionnelle à son effigie.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Javier appears in the official teaser artwork of Red Dead Redemption 2 and in promotional artwork of his own. The third trailer, released on May 2, 2018, also shows him. On September 6, 2018, Rockstar posted the portraits and character descriptions of the gang's members on Twitter, Javier among them; The Hollywood Reporter reproduced the series the next day.",
              "Javier figure sur l'illustration officielle d'annonce de Red Dead Redemption 2 et sur une illustration promotionnelle qui lui est consacrée. La troisième bande-annonce, publiée le 2 mai 2018, le montre également. Le 6 septembre 2018, Rockstar publie sur Twitter les portraits et les descriptions des membres du gang, dont les siens ; The Hollywood Reporter reprend la série le lendemain.")},
]
