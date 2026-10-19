"""Lenny Summers, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/lenny/, cov/lenny/m/,
cov/lenny/t/ and cov/lenny/fc/):
- Red Dead Wiki EN "Lenny Summers" (Mission Appearances, Trivia, Gallery captions) and FR "Lenny Summers" (fr.txt:
  Apparitions dans les missions, same 13 missions; Anecdotes). The wiki has no Quotes or Dialogues subpage for Lenny
  (both return "missingtitle"), so every quote below comes from a mission transcript.
- Mission pages: Outlaws from the West; Old Friends; Who the Hell is Leviticus Cornwall?; Eastward Bound; A Quiet Time;
  Preaching Forgiveness as He Went; Sodom? Back to Gomorrah; Blood Feuds, Ancient and Modern; The Battle of Shady
  Belle; The Gilded Cage; Horsemen, Apocalypses; Urban Pleasures; Revenge is a Dish Best Eaten; Banking, The Old
  American Art; A Kind and Benevolent Despot; Fleeting Joy; companion activities Coach Robbery (Lenny Summers) and Five
  Finger Fillet (camp opponents by chapter).
- Transcripts "/dialogues": Outlaws from the West; Enter, Pursued by a Memory; The Aftermath of Genesis; Old Friends;
  Who the Hell is Leviticus Cornwall?; Eastward Bound; Exit, Pursued by a Bruised Ego; Sodom? Back to Gomorrah; The
  Battle of Shady Belle; Red Dead Redemption (mission). Every quote is checked word for word against one of them
  (stage directions in parentheses removed; inner double quotes turned into single quotes).
- Real world: Rockstar tweet "Lenny Summers" of September 6, 2018, reproduced by The Hollywood Reporter on September 7,
  2018 (../charles/fc/thr_descriptions.txt; the description itself is NOT quoted here, part B); composite of the 23
  gang members (Wikipedia caption, m/wp_list.txt: back row "Javier, Lenny, Micah"); first trailer two days after the
  October 18, 2016 announcement (as in the other C parts), third trailer May 2, 2018 (as in uncle_C). Trailer details
  come from the wiki's gallery captions and are attributed.
Ownership (FIX_RULES), left to other parts: background (birth, parents, grandmother, father's letter and death, watch,
Blackwater, joining the gang), every mission event, the Paying Respects grave, the newspaper article (A); official
descriptions (guide, THR), names ("Leonard" in "Preaching Forgiveness as He Went", "kid", "boy", "big man"), personality,
appearance (orange bandana, outfits), weapons (Cattleman, Rolling Block, Carbine Repeater) and horse Maggie (including
riding Maggie after "Preaching Forgiveness as He Went"), camp scenes (Bill and "boy", Micah's taunts, Sean's reading,
Evelyn Miller, Pearson's cooking, the burial wish with Hosea, the Jenny Kirk talk, Five Finger Fillet teasing),
throwing Arthur out of camp (B); Harron Atkins, cut content (Pouring Forth Oil IV, unused encounter, First Look
images), Curzon Dobell's favorite character, reception (D).
Quotes: mission lines only, each in ONE place. Deliberately left out so that part B can use them: "'Course I'm ready."
(cited by the wiki's Personality section), the infobox line "Before me, at least six generations were born in
chains..." (camp line), "Just happy we're back at'em, Dutch.", "At first, I thought, 'bad idea...'" and "next time
I'll know what you mean by 'a couple of drinks.'" (all three in B, "In his own words"; removed here on 19 Oct 2026).
A paraphrases every line quoted here. Fact-check of 19 Oct 2026 also applied: no page-referring lines, no "(transcript)"
tag, third-trailer still dropped (wiki file named after Escuela, grey bandana: identification uncertain), composite
image attributed to Wikipedia's character list, Coach Robbery availability left to B, gang reactions reworded.
No kills table: the character page lists no murders for Lenny. The only people he is known to have killed by name
are the men who killed his father (unnamed, official guide, told in A); in missions he kills unnamed guards, Raiders,
lawmen and marshals alongside Arthur.
Excluded from Trivia: "appears to be still alive and breathing" after being shot (impression from a video); the
"foreshadowing" readings (party line, burial wish) and the Hosea/Lenny vs Arthur/John comparison (interpretation);
the wiki's reading of the gang's reactions to his death as clues to their personalities (interpretation, only the
observable part is kept); the letter "mentions his own abandonment of his family" (contradicted by the letter text);
the "Lemmy" reference to Lemmy Kilmister ("possibly", speculation; the misspelling itself is kept); Urban Pleasures
invulnerable-Lenny and hat glitches (no value).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 13 story missions of Red Dead Redemption 2 for Lenny, from the arrival at Colter to the Saint Denis bank robbery in which he dies, plus two companion activities. The French edition gives the same 13 missions. Every mission on the list shows him on screen. The second table adds missions in which he appears without being listed, or in which other characters talk about him. Lenny does not appear in Red Dead Redemption, set after his death. The character page records no named victim for him; in missions he fights unnamed guards, Raiders, lawmen and marshals alongside Arthur.",
              "Le Red Dead Wiki anglais recense pour Lenny 13 missions principales de Red Dead Redemption 2, de l'arrivée à Colter jusqu'au braquage de la banque de Saint-Denis où il meurt, ainsi que deux activités de compagnon. L'édition française donne les 13 mêmes missions. Chacune des missions de la liste le montre à l'écran. Le second tableau ajoute les missions où il apparaît sans être cité, ou dans lesquelles d'autres personnages parlent de lui. Lenny n'apparaît pas dans Red Dead Redemption, qui se déroule après sa mort. Sa fiche sur le wiki ne lui attribue aucune victime nommée ; en mission, il affronte aux côtés d'Arthur des gardes, des Raiders, des hommes de loi et des marshals anonymes.")},
    {"h4": two("Missions listed by the Red Dead Wiki", "Missions recensées par le Red Dead Wiki")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Lenny's role", "Rôle de Lenny")], "rows": [
        M("Outlaws from the West", C1,
          "On watch at Colter. Spots the riders, recognizes [[dutch-van-der-linde|Dutch]] and calls the camp out, then takes his horse.",
          "De garde à Colter. Repère les cavaliers, reconnaît [[dutch-van-der-linde|Dutch]] et appelle le camp, puis prend son cheval."),
        M("Old Friends", C1,
          "Mocked by [[micah-bell|Micah]] in the men's cabin, helps separate him from [[bill-williamson|Bill]]. Covers the raid on the O'Driscoll camp from the heights with [[javier-escuella|Javier]].",
          "Raillé par [[micah-bell|Micah]] dans la cabane des hommes, aide à le séparer de [[bill-williamson|Bill]]. Couvre l'attaque du camp O'Driscoll depuis les hauteurs avec [[javier-escuella|Javier]]."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "Jumps onto Cornwall's train with [[arthur-morgan|Arthur]], fights through the cars with him and reads the papers found in the private car's safe.",
          "Saute sur le train de Cornwall avec [[arthur-morgan|Arthur]], traverse les voitures avec lui sous le feu et lit les papiers trouvés dans le coffre de la voiture privée."),
        M("Eastward Bound", C1,
          "Loads the wagons, then rides ahead of the convoy with Micah to scout the road.",
          "Charge les chariots, puis part en éclaireur devant le convoi avec Micah."),
        M("A Quiet Time", C2,
          "Brings the news of Micah's arrest in Strawberry, then spends a drunken night with Arthur at Smithfield's Saloon in Valentine and is arrested.",
          "Rapporte la nouvelle de l'arrestation de Micah à Strawberry, puis passe une nuit d'ivresse avec Arthur au Smithfield's Saloon de Valentine et se fait arrêter."),
        M("Preaching Forgiveness as He Went", C3,
          "Mission giver. Leads Arthur to the Lemoyne Raiders at Shady Belle; the two kill them and steal a wagon of weapons.",
          "Donneur de mission. Conduit Arthur jusqu'aux Lemoyne Raiders de Shady Belle ; les deux hommes les abattent et volent un chariot d'armes."),
        M("Sodom? Back to Gomorrah", C3,
          "Robs the Valentine bank with Arthur, Bill and [[karen-jones|Karen]]: holds up the room, hands Karen the key and guards the hostages.",
          "Braque la banque de Valentine avec Arthur, Bill et [[karen-jones|Karen]] : tient la salle en respect, donne la clé à Karen et surveille les otages."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Rides to Braithwaite Manor with the gang to get [[jack-marston|Jack]] back.",
          "Chevauche avec la bande jusqu'au manoir Braithwaite pour récupérer [[jack-marston|Jack]]."),
        M("The Battle of Shady Belle", C3,
          "Warns Dutch of the arrival of [[andrew-milton|Milton]] and [[edgar-ross|Ross]], shows them out and is sent to follow them.",
          "Prévient Dutch de l'arrivée de [[andrew-milton|Milton]] et de [[edgar-ross|Ross]], les raccompagne et reçoit l'ordre de les suivre."),
        M("The Gilded Cage", C4,
          "Drives the coach to and from Mayor Lemieux's garden party.",
          "Conduit la voiture à l'aller et au retour de la garden-party du maire Lemieux."),
        M("Urban Pleasures", C4,
          "Robs the trolley station with Dutch and Arthur, spots the police and drives the getaway wagon.",
          "Braque la station de tramways avec Dutch et Arthur, repère la police et conduit le chariot de la fuite."),
        M("Revenge is a Dish Best Eaten", C4,
          "Takes part in the assault on [[angelo-bronte|Bronte]]'s mansion.",
          "Participe à l'assaut du manoir de [[angelo-bronte|Bronte]]."),
        M("Banking, The Old American Art", C4,
          "Part of the crew at the Lemoyne National Bank. Shot down by two Pinkerton riflemen on the rooftops during the escape.",
          "Membre de l'équipe de la Lemoyne National Bank. Abattu par deux tireurs de la Pinkerton sur les toits pendant la fuite."),
    ]}},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Lenny's role", "Rôle de Lenny")], "rows": [
        M("Five Finger Fillet", C2,
          "Camp opponent, available in chapter 2 according to the wiki's Five Finger Fillet page.",
          "Adversaire au camp, disponible au chapitre 2 d'après la page Five Finger Fillet du wiki."),
        M("Coach Robbery (Lenny Summers)", C4,
          "Activity giver. Brings Arthur a tip on a Boles Overland banking coach south of Bolger Glade, which turns out to be a trap set with U.S. Marshals.",
          "Donneur de l'activité. Apporte à Arthur un tuyau sur une diligence bancaire de la Boles Overland au sud de Bolger Glade, qui se révèle être un piège tendu avec des U.S. Marshals."),
    ]}},
    {"h4": two("Other missions", "Autres missions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Lenny's role", "Rôle de Lenny")], "rows": [
        M("Enter, Pursued by a Memory", C1,
          "With Bill, pulls the wounded [[john-marston|John]] off Javier's horse and carries him to a bed.",
          "Avec Bill, descend [[john-marston|John]], blessé, du cheval de Javier et le porte jusqu'à un lit."),
        M("The Aftermath of Genesis", C1,
          "Mentioned only. [[simon-pearson|Pearson]] says Lenny and Bill came back from hunting with nothing.",
          "Seulement cité. [[simon-pearson|Pearson]] raconte que Lenny et Bill sont rentrés bredouilles de la chasse."),
        M("Exit, Pursued by a Bruised Ego", C2,
          "Mentioned only. Arthur and [[hosea-matthews|Hosea]] talk about the scouting trip with Micah and about Jenny Kirk.",
          "Seulement cité. Arthur et [[hosea-matthews|Hosea]] parlent de sa reconnaissance avec Micah et de Jenny Kirk."),
        M("Horsemen, Apocalypses", C4,
          "Mentioned only. Arthur proposes him as the third man for the trolley station job.",
          "Seulement cité. Arthur le propose comme troisième homme pour le coup de la station de tramways."),
        M("A Kind and Benevolent Despot", C5,
          "Mentioned only. On Guarma, Dutch wonders why Hosea and Lenny were killed at the bank.",
          "Seulement cité. À Guarma, Dutch se demande pourquoi Hosea et Lenny ont été tués à la banque."),
        M("Fleeting Joy", C5,
          "Mentioned only. [[abigail-marston|Abigail]] tells Dutch that the gang took his body from the morgue and buried him.",
          "Seulement cité. [[abigail-marston|Abigail]] apprend à Dutch que la bande a repris son corps à la morgue pour l'enterrer."),
        M("The King's Son", C6,
          "Mentioned only. [[charles-smith|Charles]] names him among the dead who had no time to make amends.",
          "Seulement cité. [[charles-smith|Charles]] le cite parmi les morts qui n'ont pas eu le temps de se racheter."),
        M("Red Dead Redemption", C6,
          "Mentioned only. Arthur names him among the people the gang has lost, on the ride with [[sadie-adler|Sadie]].",
          "Seulement cité. Arthur le cite parmi ceux que la bande a perdus, en chevauchant avec [[sadie-adler|Sadie]]."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. All are mission lines checked against the transcripts of the Red Dead Wiki, which has no separate quote list for Lenny. Lines already quoted under Personality and Relationships do not appear again here.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Ce sont toutes des répliques de mission, vérifiées sur les transcriptions du Red Dead Wiki, qui ne propose pas de liste de citations propre à Lenny. Les répliques déjà citées dans les rubriques Personnalité et Relations ne sont pas reprises ici.")},
    {"h4": two("Chapter 1: Colter", "Chapitre 1 : Colter")},
    {"quotes": [
        {"q": two("Looks like it's Dutch. Hey everybody, Dutch is back.", "Looks like it's Dutch. Hey everybody, Dutch is back."),
         "src": two("Outlaws from the West (RDR2, chapter 1), on watch at Colter, as the riders come in",
                    "Outlaws from the West (RDR2, chapitre 1), de garde à Colter, à l'arrivée des cavaliers. Traduction : « On dirait que c'est Dutch. Hé, tout le monde, Dutch est rentré. »")},
        {"q": two("When you fall...there'll be a party.", "When you fall...there'll be a party."),
         "src": two("Old Friends (RDR2, chapter 1), to Micah, who says he wants no fuss when he falls",
                    "Old Friends (RDR2, chapitre 1), à Micah, qui dit ne vouloir aucune histoire le jour où il tombera. Traduction : « Le jour où tu tomberas... on fera la fête. »")},
        {"q": two("Thanks for helping, Arthur... really appreciate that.", "Thanks for helping, Arthur... really appreciate that."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), sarcastically, if Arthur leaves him to climb onto the train alone",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), avec ironie, si Arthur le laisse remonter seul sur le train. Traduction : « Merci du coup de main, Arthur... vraiment, j'apprécie. »")},
        {"q": two("You and me, big man.", "You and me, big man."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), to Arthur, on the roof of the train, once Javier has fallen",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), à Arthur, sur le toit du train, une fois Javier tombé. Traduction : « Toi et moi, mon grand. »")},
        {"q": two("What the hell was Bill doing? He had long enough to set that charge.", "What the hell was Bill doing? He had long enough to set that charge."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), to Arthur, who wired the detonator",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), à Arthur, qui a lui-même branché le détonateur. Traduction : « Qu'est-ce qu'il foutait, Bill ? Il avait tout le temps de poser cette charge. »")},
        {"q": two("Damn, he's got an army! Who is this guy?", "Damn, he's got an army! Who is this guy?"),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), as more of Cornwall's guards come out of the cars",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), alors que d'autres gardes de Cornwall sortent des wagons. Traduction : « Bon sang, il a une armée ! C'est qui, ce type ? »")},
        {"q": two("Look at this place. It's like a palace.", "Look at this place. It's like a palace."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), entering Cornwall's private car",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), en entrant dans la voiture privée de Cornwall. Traduction : « Regarde-moi ça. On dirait un palais. »")},
        {"q": two("Shut up. Me and Arthur did all the work.", "Shut up. Me and Arthur did all the work."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), to Micah, who orders him to pour a brandy",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), à Micah, qui lui ordonne de lui servir un brandy. Traduction : « La ferme. C'est Arthur et moi qui avons fait tout le boulot. »")},
        {"q": two("Not really. Sugar imports from the Spanish West Indies... a lot of sugar. Some fancy new boat he's ordered from Europe.", "Not really. Sugar imports from the Spanish West Indies... a lot of sugar. Some fancy new boat he's ordered from Europe."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), reading the papers from Cornwall's safe",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), en lisant les papiers du coffre de Cornwall. Traduction : « Pas vraiment. Des importations de sucre des Antilles espagnoles... beaucoup de sucre. Un nouveau bateau de luxe qu'il a commandé en Europe. »")},
    ]},
    {"h4": two("Chapter 3: Clemens Point", "Chapitre 3 : Clemens Point")},
    {"quotes": [
        {"q": two("If we didn't rob this bank, we really would be slipping.", "If we didn't rob this bank, we really would be slipping."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), to Arthur, on the ride to Valentine",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), à Arthur, sur la route de Valentine. Traduction : « Si on ne braquait pas cette banque, là, on se laisserait vraiment aller. »")},
        {"q": two("Hey, keep still. If I see that leg move again, you get a bullet in it.", "Hey, keep still. If I see that leg move again, you get a bullet in it."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), to a hostage in the Valentine bank",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), à un otage de la banque de Valentine. Traduction : « Hé, bouge pas. Si je vois encore cette jambe remuer, tu prends une balle dedans. »")},
        {"q": two("Hey Dutch. We got a problem.", "Hey Dutch. We got a problem."),
         "src": two("The Battle of Shady Belle (RDR2, chapter 3), as Milton and Ross walk into Clemens Point",
                    "The Battle of Shady Belle (RDR2, chapitre 3), quand Milton et Ross entrent dans le camp de Clemens Point. Traduction : « Hé, Dutch. On a un problème. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("In \"Who the Hell is Leviticus Cornwall?\", pulling Lenny up when he hangs from the side of the train is a gold medal objective; leaving him to climb up alone costs Arthur honor. If Lenny gets ahead of Arthur near the locomotive, the engineer ambushes him instead, and Arthur has to save him.",
            "Dans \"Who the Hell is Leviticus Cornwall?\", hisser Lenny quand il pend au flanc du train est un objectif de la médaille d'or ; le laisser remonter seul coûte de l'honneur à Arthur. Si Lenny devance Arthur près de la locomotive, c'est lui que le mécanicien attaque, et Arthur doit le tirer d'affaire."),
        two("On the ride into Valentine in \"A Quiet Time\", Lenny draws his revolver and shoots dead any passer-by whom Arthur antagonizes until he turns hostile.",
            "Sur la route de Valentine, dans \"A Quiet Time\", Lenny dégaine son revolver et abat tout passant qu'Arthur a provoqué au point de le rendre hostile."),
        two("When Arthur is very drunk in \"A Quiet Time\", the prompts that show Lenny's name are scrambled into versions such as \"Lemmy\", \"Lennie\", \"Lneny\" and \"ynneL\".",
            "Quand Arthur est ivre mort dans \"A Quiet Time\", les commandes affichant le nom de Lenny se brouillent en variantes comme \"Lemmy\", \"Lennie\", \"Lneny\" ou \"ynneL\"."),
        two("One gold medal objective of \"A Quiet Time\" is called \"Catch Lenny in the act\". On the third search, Arthur has to open the wrong door upstairs: he sees Lenny's face on both a prostitute and her client, and all three scream in horror.",
            "Un objectif de la médaille d'or de \"A Quiet Time\" s'intitule \"Catch Lenny in the act\". Lors de la troisième recherche, Arthur doit ouvrir la mauvaise porte à l'étage : il voit le visage de Lenny à la fois sur une prostituée et sur son client, et tous trois hurlent d'effroi."),
        two("In \"Preaching Forgiveness as He Went\", if Arthur takes another route to avoid the last group of Raiders, Lenny remarks that they should have met someone by now. If Arthur has already been to Shady Belle on his own, he tells Lenny so on arrival.",
            "Dans \"Preaching Forgiveness as He Went\", si Arthur prend un autre chemin pour éviter le dernier groupe de Raiders, Lenny remarque qu'ils auraient déjà dû croiser quelqu'un. Si Arthur est déjà passé seul à Shady Belle, il le dit à Lenny en arrivant."),
        two("In \"Sodom? Back to Gomorrah\", the ride conversation about Shady Belle is only available if \"Preaching Forgiveness as He Went\" has been played first.",
            "Dans \"Sodom? Back to Gomorrah\", la conversation sur Shady Belle pendant le trajet n'est accessible que si \"Preaching Forgiveness as He Went\" a été jouée avant."),
        two("For the coach robbery, Lenny plans the job on the first Jack Hall Gang Map. The lawmen of the ambush call themselves marshals but wear sheriff's badges. According to the Red Dead Wiki, Arthur remarks during the activity that Lenny is not even twenty.",
            "Pour l'attaque de la diligence, Lenny prépare le coup sur la première carte du gang de Jack Hall. Les hommes de loi de l'embuscade se présentent comme des marshals mais portent des insignes de shérif. D'après le Red Dead Wiki, Arthur fait remarquer pendant l'activité que Lenny n'a même pas vingt ans."),
        two("Lenny's death is the only death of a gang member in Red Dead Redemption 2 that happens outside a cutscene. He cannot be saved: the two Pinkerton riflemen who shoot him cannot be killed before they fire.",
            "La mort de Lenny est la seule mort d'un membre de la bande, dans Red Dead Redemption 2, qui survient en dehors d'une cinématique. Il est impossible de le sauver : les deux tireurs de la Pinkerton qui l'abattent ne peuvent pas être tués avant d'avoir tiré."),
        two("According to the Red Dead Wiki, only Arthur and Charles stop at Lenny's body; Javier looks back, while Dutch, who cries out, Bill and Micah keep running.",
            "D'après le Red Dead Wiki, seuls Arthur et Charles s'arrêtent près du corps de Lenny ; Javier se retourne, tandis que Dutch, qui pousse un cri, Bill et Micah continuent de courir."),
        two("According to the Red Dead Wiki, Arthur writes in his journal that Lenny was shot in the head, while the scene shows him hit in the body.",
            "D'après le Red Dead Wiki, Arthur écrit dans son journal que Lenny a reçu une balle dans la tête, alors que la scène le montre touché au corps."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Lenny appears in the first trailer of Red Dead Redemption 2, released on October 20, 2016, two days after the game's announcement. According to the caption of the still on the Red Dead Wiki, his look differs from the final game: a gray coat, red trousers and a paisley bandana, a buckskin stallion and a Litchfield Repeater. Rockstar also released promotional artwork of him. On September 6, 2018, Rockstar posted his portrait and character description on Twitter, in a series covering the members of the gang, and The Hollywood Reporter reproduced the series the next day. In the composite of the character art of the 23 gang members shown on Wikipedia's list of the game's characters, Lenny stands in the back row, between Javier and Micah.",
              "Lenny apparaît dans la première bande-annonce de Red Dead Redemption 2, publiée le 20 octobre 2016, deux jours après l'annonce du jeu. D'après la légende de l'image sur le Red Dead Wiki, son allure diffère de celle du jeu final : manteau gris, pantalon rouge et bandana à motif cachemire, étalon isabelle et Litchfield Repeater. Rockstar a aussi diffusé une illustration promotionnelle du personnage. Le 6 septembre 2018, Rockstar publie sur Twitter son portrait et sa description, dans une série consacrée aux membres du gang, et The Hollywood Reporter reprend la série le lendemain. Sur le montage des portraits des 23 membres du gang qui illustre la liste des personnages du jeu sur Wikipédia, Lenny figure au dernier rang, entre Javier et Micah.")},
]
