"""Nigel West Dickens, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/, copies in
scripts/v3/work/nigel/fc/):
- Character page "Nigel West Dickens" (Mission appearances, Quotes, Trivia, Gallery captions) and FR page
  (Apparitions dans les missions, Anecdotes).
- Mission pages (infobox rewards, order numbers, prerequisites, unlocks, trivia): "Old Swindler Blues" (10th
  mission), "You Shall Not Give False Testimony, Except for Profit" (12th), "Liars, Cheats and Other Proud
  Americans" (16th), "Can a Swindler Change His Spots?" (17th), "The Sport of Kings, and Liars" (18th), "The
  Assault on Fort Mercer" (24th), "We Shall Be Together in Paradise" (25th), "Bear One Another's Burdens",
  "A Cure for Most of What Ails You" and "American Imperialism" (Undead Nightmare, quote boxes, rewards).
- Transcripts used word for word for every mission quote: "Justice in Pike's Basin/dialogues", "Spare the Rod,
  Spoil the Bandit/dialogues", "You Shall Not Give False Testimony, Except for Profit/dialogues", "Liars, Cheats
  and Other Proud Americans/dialogues", "Can a Swindler Change His Spots?/dialogues", "The Sport of Kings, and
  Liars/dialogues", "The Assault on Fort Mercer/dialogues", "Bear One Another's Burdens/dialogues". Mentions:
  "Exhuming and Other Fine Hobbies/dialogues", "A Frenchman, a Welshman and an Irishman/dialogues", "On Shaky's
  Ground/dialogues", "Let the Dead Bury Their Dead/dialogues". Undead Nightmare lines come from the mission
  pages' quote boxes (no transcript exists).
- Other pages: "Nigel West Dickens' Elixir" (Undead Bait recipe, Wilton Glover, bottle locations), "Liars and
  Cheats" (released September 21, 2010, Dickens in the Redemption list), "Undead Nightmare", "Dead Eye Targeting"
  (level 2 from this strand).
- Real world: Liars and Cheats Pack details published by Rockstar on August 27, 2010 and released September 21,
  2010 (as in bonnie_C and jack_C); Red Dead Redemption: The Man from Blackwater, directed by John Hillcoat, aired
  on Fox on May 29, 2010 (as in john_E, which lists the reused missions); RDR1 ports PS4/Switch August 17, 2023
  and PC October 29, 2024 without multiplayer (as in bonnie_C).

VERIFIED POINTS: the "dose of salts" line is in "Can a Swindler Change His Spots?" (transcript), not in "The
Sport of Kings, and Liars"; the skull-miss line is in the transcript ("He is still adjusting to his powerful new
eyes!"; the mission page trivia words it "He is still getting used to his new vision!"); in the "Old Swindler
Blues" transcript Dickens names the Bollard Twins and Walton's Gang, while the character page makes this
depend on John's outfit (both given, attributed); the Blackwater Ledger line "I know a cure for all ailments" is
said in "You Shall Not Give False Testimony, Except for Profit" (transcript), not on leaving the doctor's office
as the wiki says (he says it to John just after).

EXCLUDED: "I'm coming home, Daddy" as proof that his father was dead (inference; the line is kept, attributed);
the Undead Nightmare box "that could be elixir" (speculation); "Let the battle commence!" and "Moral degeneracy
waits for no man" as Dickens's lines (not found in any transcript: the first is kept from the wiki quote list,
attributed; the second is said by Ross in the transcript and is left to the Edgar Ross fiche); W.C. Fields and
Josey Wales comparisons (real-world inspiration, part D, and worded as "seem"); the neck scar (part B,
appearance, and the lynching reading is speculation); the only time he fires a weapon (part B Skills); Rob
Nelson's first recorded cutscene (part D); the scrapped "falling rocks" reading (speculation); glitches;
"Allbright resembles Dickens" (RDR2 mission trivia, interpretation); "Butch the Visionary" (nickname given to
Dutch, unsourced, as in dutch_C); the bottle locations in the Armadillo saloon and Tanner's Reach (minor set
dressing, kept out to stay medium).

OWNERSHIP: narrative events live in part A (one line per mission here). The Moncrief letter and both newspaper
articles are told in part A only. Lines quoted here are not repeated in part B "In his own words"; if part B
uses one, the fixer removes it from one place.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A1 = two("Act I: New Austin", "Acte I : New Austin")
A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
UNM = two("Undead Nightmare", "Undead Nightmare")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Dickens has a strand of five story missions in the first act of Red Dead Redemption, all in New Austin. The first, \"Old Swindler Blues\", becomes available after Leigh Johnson's \"Justice in Pike's Basin\"; the second also requires Bonnie MacFarlane's \"Women and Cattle\" and, once completed, opens the strand of Seth Briars. \"Liars, Cheats and Other Proud Americans\" opens the strand of Irish. \"Liars, Cheats and Other Proud Americans\" and \"The Sport of Kings, and Liars\" are two of the three races of the story, with Bonnie's \"Obstacles in Our Path\"; racing is not offered again in single player. His strand ends with \"The Assault on Fort Mercer\", given by Leigh Johnson. In Undead Nightmare, he gives two missions.",
              "Dickens propose une série de cinq missions principales dans le premier acte de Red Dead Redemption, toutes dans le New Austin. La première, \"Old Swindler Blues\", se débloque après \"Justice in Pike's Basin\", une mission de Leigh Johnson ; la deuxième exige aussi \"Women and Cattle\", de Bonnie MacFarlane, et ouvre une fois terminée la série de Seth Briars. \"Liars, Cheats and Other Proud Americans\" ouvre celle d'Irish. \"Liars, Cheats and Other Proud Americans\" et \"The Sport of Kings, and Liars\" sont deux des trois courses de l'histoire, avec \"Obstacles in Our Path\", de Bonnie ; le mode solo n'en propose plus ensuite. Sa série se conclut avec \"The Assault on Fort Mercer\", confiée par Leigh Johnson. Dans Undead Nightmare, il confie deux missions.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Dickens's role", "Rôle de Dickens")], "rows": [
        M("Old Swindler Blues", A1,
          "Mission giver. Found wounded near his wagon, driven by John to the Armadillo doctor under attack. Rewards: 100 honor and 75 fame; unlocks Liar's Dice.",
          "Donneur de mission. Trouvé blessé près de son chariot, conduit par John chez le médecin d'Armadillo sous les balles. Récompenses : 100 points d'honneur et 75 de célébrité ; débloque le poker menteur."),
        M("You Shall Not Give False Testimony, Except for Profit", A1,
          "Mission giver. Stages a medicine show at Ridgewood Farm with John as his planted volunteer, then sends him to Seth. Rewards: Dead Eye level 2 and 25 fame; Snake Oil goes on sale in shops.",
          "Donneur de mission. Monte un spectacle de vente à Ridgewood Farm avec John comme faux volontaire, puis l'envoie voir Seth. Récompenses : Dead Eye niveau 2 et 25 points de célébrité ; le Snake Oil est mis en vente dans les boutiques."),
        M("Liars, Cheats and Other Proud Americans", A1,
          "Mission giver. Enters John as his driver in the cart race at Gaptooth Breach, then sends him to Irish. Rewards: 3 dollars and 200 fame.",
          "Donneur de mission. Inscrit John comme pilote à la course de chariots de Gaptooth Breach, puis l'envoie voir Irish. Récompenses : 3 dollars et 200 points de célébrité."),
        M("Can a Swindler Change His Spots?", A1,
          "Mission giver. His show in Plainview turns into a chase; he drives the wagon to Cueva Seca while John fights off the crowd. Rewards: 25 dollars and 75 fame.",
          "Donneur de mission. Son spectacle à Plainview tourne à la course-poursuite ; il conduit le chariot jusqu'à Cueva Seca pendant que John repousse la foule. Récompenses : 25 dollars et 75 points de célébrité."),
        M("The Sport of Kings, and Liars", A1,
          "Mission giver. Leads John from Cueva Seca to the horse race at Rathskeller Fork to pay for his wagon's fittings. Rewards: 5 dollars and 200 fame.",
          "Donneur de mission. Emmène John de Cueva Seca à la course de chevaux de Rathskeller Fork pour financer l'équipement de son chariot. Récompenses : 5 dollars et 200 points de célébrité."),
        M("The Assault on Fort Mercer", A1,
          "Drives the wagon that carries John and the Gatling gun into the fort, distracting the gang with a sales pitch.",
          "Conduit dans le fort le chariot où John est caché avec la mitrailleuse Gatling, et distrait la bande par un boniment."),
        M("We Shall Be Together in Paradise", A1,
          "Says goodbye to John at Brittlebrush Trawl before Irish's raft leaves for Mexico.",
          "Fait ses adieux à John à Brittlebrush Trawl avant le départ du radeau d'Irish pour le Mexique."),
        M("Bear One Another's Burdens", A3,
          "Brought into the Blackwater police station under arrest, then released at John's request.",
          "Amené en état d'arrestation au poste de police de Blackwater, puis relâché à la demande de John."),
        M("A Cure for Most of What Ails You", UNM,
          "Mission giver. Sells his tonic at Fort Mercer, then makes a phosphorus coating and a Blunderbuss from what John brings back. Rewards: Undead Bait, Blunderbuss, phosphorus coating.",
          "Donneur de mission. Vend son tonique à Fort Mercer, puis fabrique un enduit au phosphore et un Blunderbuss avec ce que rapporte John. Récompenses : Undead Bait, Blunderbuss, enduit au phosphore."),
        M("American Imperialism", UNM,
          "Mission giver. At Solomon's Folly, tells John about the army train to Mexico and the deserters' uniform. Rewards: U.S. Army Uniform and access to Nuevo Paraíso.",
          "Donneur de mission. À Solomon's Folly, parle à John du train de l'armée pour le Mexique et de l'uniforme des déserteurs. Récompenses : uniforme de l'armée américaine et accès au Nuevo Paraíso."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Link with Dickens", "Lien avec Dickens")], "rows": [
        M("Justice in Pike's Basin", A1,
          "Eli reports him missing to Leigh Johnson.",
          "Eli signale sa disparition à Leigh Johnson."),
        M("Spare the Rod, Spoil the Bandit", A1,
          "Eli drinks his elixir; Johnson, Eli, Jonah and John discuss him.",
          "Eli boit son élixir ; Johnson, Eli, Jonah et John parlent de lui."),
        M("Exhuming and Other Fine Hobbies", A1,
          "John introduces himself to [[seth-briars|Seth]] as a friend of Dickens.",
          "John se présente à [[seth-briars|Seth]] comme un ami de Dickens."),
        M("A Frenchman, a Welshman and an Irishman", A1,
          "John tells [[irish|Irish]] that Dickens sent him for a machine gun.",
          "John explique à [[irish|Irish]] que Dickens l'envoie chercher une mitrailleuse."),
        M("On Shaky's Ground", A1,
          "Irish says Dickens's wagon will soon be rigged.",
          "Irish annonce que le chariot de Dickens sera bientôt équipé."),
        M("Let the Dead Bury Their Dead", A1,
          "Seth arranges to meet John and Dickens at Fort Mercer.",
          "Seth donne rendez-vous à John et à Dickens à Fort Mercer."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the mission transcripts of the Red Dead Wiki. The Undead Nightmare lines come from the quote boxes of the mission pages, as no transcript exists for those missions, and the Fort Mercer battle cry from the wiki's quote list.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Celles d'Undead Nightmare proviennent des encadrés de citation des pages de mission, faute de transcription, et le cri de guerre de Fort Mercer, de la liste de citations du wiki.")},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("Oh, the narcotic and bat piss salesman who cons housewives out of their money with promises of eternal youth.", "Oh, the narcotic and bat piss salesman who cons housewives out of their money with promises of eternal youth."),
         "src": two("Leigh Johnson, Justice in Pike's Basin (RDR1, Act I), when Eli reports Dickens missing",
                    "Leigh Johnson, Justice in Pike's Basin (RDR1, acte I), quand Eli signale la disparition de Dickens. Traduction : « Ah, le marchand de stupéfiants et de pisse de chauve-souris qui soutire leur argent aux ménagères en leur promettant la jeunesse éternelle. »")},
        {"q": two("Jonah: I can't understand a goddamn word he says. / Marston: A more flannel-mouthed bunko artist, I've never met.", "Jonah: I can't understand a goddamn word he says. / Marston: A more flannel-mouthed bunko artist, I've never met."),
         "src": two("Spare the Rod, Spoil the Bandit (RDR1, Act I)",
                    "Spare the Rod, Spoil the Bandit (RDR1, acte I). Traduction : « Jonah : Je comprends pas un traître mot de ce qu'il raconte. / Marston : Je n'ai jamais rencontré d'escroc plus baratineur. »")},
        {"q": two("A bunko, a grave robber and a drunk. How can things possibly go wrong?", "A bunko, a grave robber and a drunk. How can things possibly go wrong?"),
         "src": two("John Marston, The Sport of Kings, and Liars (RDR1, Act I), after Dickens praises the team he has assembled",
                    "John Marston, The Sport of Kings, and Liars (RDR1, acte I), quand Dickens vante l'équipe qu'il a réunie. Traduction : « Un escroc, un pilleur de tombes et un ivrogne. Qu'est-ce qui pourrait mal tourner ? »")},
    ]},
    {"h4": two("Red Dead Redemption, Act I", "Red Dead Redemption, acte I")},
    {"quotes": [
        {"q": two("Marston: And I'm sure for just 2 dollars an ounce, I could live forever. / Nigel: Oh, but for you sir, I'd do a bulk discount rate of 1.95 an ounce, as long as you buy 100 ounces or more. That's a lot of immortality.", "Marston: And I'm sure for just 2 dollars an ounce, I could live forever. / Nigel: Oh, but for you sir, I'd do a bulk discount rate of 1.95 an ounce, as long as you buy 100 ounces or more. That's a lot of immortality."),
         "src": two("You Shall Not Give False Testimony, Except for Profit (RDR1, Act I), outside the doctor's office",
                    "You Shall Not Give False Testimony, Except for Profit (RDR1, acte I), devant le cabinet du médecin. Traduction : « Marston : Et je suppose que pour 2 dollars l'once seulement, je pourrais vivre éternellement. / Nigel : Oh, mais pour vous, monsieur, je ferais un tarif de gros à 1,95 l'once, à partir de 100 onces. Ça fait beaucoup d'immortalité. »")},
        {"q": two("Skepticism is the bastard child of progress, John. Knowledge makes a fool into a doubting Thomas. It's a cross I bear as a pioneer in the fields of commerce and medical research.", "Skepticism is the bastard child of progress, John. Knowledge makes a fool into a doubting Thomas. It's a cross I bear as a pioneer in the fields of commerce and medical research."),
         "src": two("You Shall Not Give False Testimony, Except for Profit (RDR1, Act I), when John points out that the men who attacked him did not look like happy customers",
                    "You Shall Not Give False Testimony, Except for Profit (RDR1, acte I), quand John lui fait remarquer que ses agresseurs n'avaient pas l'air de clients satisfaits. Traduction : « Le scepticisme est l'enfant illégitime du progrès, John. Le savoir change un idiot en saint Thomas. C'est la croix que je porte, en pionnier du commerce et de la recherche médicale. »")},
        {"q": two("Do you think that buxom young girl you see on the Voyach camera posters knows the first thing about photography? Advertising, my boy, is the way of the future.", "Do you think that buxom young girl you see on the Voyach camera posters knows the first thing about photography? Advertising, my boy, is the way of the future."),
         "src": two("You Shall Not Give False Testimony, Except for Profit (RDR1, Act I), when John asks whether the show is a sham",
                    "You Shall Not Give False Testimony, Except for Profit (RDR1, acte I), quand John demande si le spectacle est une arnaque. Traduction : « Tu crois que la jeune fille bien en chair des affiches d'appareils photo Voyach connaît quoi que ce soit à la photographie ? La publicité, mon garçon, c'est l'avenir. »")},
        {"q": two("Wait! He is still adjusting to his powerful new eyes! Try again, friend! The tonic may still be taking hold!", "Wait! He is still adjusting to his powerful new eyes! Try again, friend! The tonic may still be taking hold!"),
         "src": two("You Shall Not Give False Testimony, Except for Profit (RDR1, Act I), if John misses the skull",
                    "You Shall Not Give False Testimony, Except for Profit (RDR1, acte I), si John manque le crâne. Traduction : « Attendez ! Il s'habitue encore à ses nouveaux yeux surpuissants ! Réessayez, mon ami ! Le tonique n'a peut-être pas encore fait tout son effet ! »")},
        {"q": two("A Robin Hood with spurs. How romantic! You expect me to believe that poppycock?", "A Robin Hood with spurs. How romantic! You expect me to believe that poppycock?"),
         "src": two("Liars, Cheats and Other Proud Americans (RDR1, Act I), after John says the gang stole from those who had too much",
                    "Liars, Cheats and Other Proud Americans (RDR1, acte I), quand John affirme que le gang volait ceux qui avaient trop. Traduction : « Un Robin des bois à éperons. Comme c'est romantique ! Et tu veux que je gobe ces sornettes ? »")},
        {"q": two("Me? Oh no, not my thing at all. You've already proven yourself as more than adept at the reins, my dear boy, and under some stress. These races are Byzantine in their ferocity and the terrain is treacherous. People will do just about anything to win. Men die. It's a marvelous spectator sport.", "Me? Oh no, not my thing at all. You've already proven yourself as more than adept at the reins, my dear boy, and under some stress. These races are Byzantine in their ferocity and the terrain is treacherous. People will do just about anything to win. Men die. It's a marvelous spectator sport."),
         "src": two("Liars, Cheats and Other Proud Americans (RDR1, Act I), when John asks why Dickens is not racing himself",
                    "Liars, Cheats and Other Proud Americans (RDR1, acte I), quand John lui demande pourquoi il ne court pas lui-même. Traduction : « Moi ? Oh non, ce n'est pas du tout mon genre. Tu as déjà prouvé que tu tenais très bien les rênes, mon cher garçon, et sous pression. Ces courses sont d'une férocité byzantine et le terrain est traître. Les gens sont prêts à tout pour gagner. Des hommes y meurent. C'est un spectacle merveilleux. »")},
        {"q": two("It always impresses me the speed with which a group of men can turn from passive sheep into murderous wolves.", "It always impresses me the speed with which a group of men can turn from passive sheep into murderous wolves."),
         "src": two("Can a Swindler Change His Spots? (RDR1, Act I), on reaching Cueva Seca",
                    "Can a Swindler Change His Spots? (RDR1, acte I), en arrivant à Cueva Seca. Traduction : « Je suis toujours impressionné par la vitesse à laquelle une bande d'hommes passe de moutons passifs à loups assassins. »")},
        {"q": two("Well, I'm sorry, dear boy, but I'm only an ageing vendor of exotic elixirs, not the bloody U.S. cavalry! Forgive me if matters take some time to prepare.", "Well, I'm sorry, dear boy, but I'm only an ageing vendor of exotic elixirs, not the bloody U.S. cavalry! Forgive me if matters take some time to prepare."),
         "src": two("Can a Swindler Change His Spots? (RDR1, Act I), when John says he is trying his patience",
                    "Can a Swindler Change His Spots? (RDR1, acte I), quand John lui dit qu'il met sa patience à l'épreuve. Traduction : « Désolé, mon cher garçon, mais je ne suis qu'un vieux marchand d'élixirs exotiques, pas la fichue cavalerie américaine ! Pardonne-moi si les préparatifs prennent un peu de temps. »")},
        {"q": two("What would you say if I told you, I could teach you to fly? What would you say if I told you, I could turn a man into a beautiful woman? Impossible? Yes, once but no more!", "What would you say if I told you, I could teach you to fly? What would you say if I told you, I could turn a man into a beautiful woman? Impossible? Yes, once but no more!"),
         "src": two("The Assault on Fort Mercer (RDR1, Act I), his sales pitch to the outlaws inside the fort",
                    "The Assault on Fort Mercer (RDR1, acte I), son boniment aux hors-la-loi à l'intérieur du fort. Traduction : « Que diriez-vous si je vous disais que je peux vous apprendre à voler ? Que diriez-vous si je vous disais que je peux changer un homme en une jolie femme ? Impossible ? Oui, autrefois, mais plus maintenant ! »")},
        {"q": two("Let the battle commence!", "Let the battle commence!"),
         "src": two("The Assault on Fort Mercer (RDR1, Act I), according to the Red Dead Wiki's quote list",
                    "The Assault on Fort Mercer (RDR1, acte I), d'après la liste de citations du Red Dead Wiki. Traduction : « Que la bataille commence ! »")},
        {"q": two("Wonderful! A sweet, peace-loving people, with a love of social justice. May you always find coin in your pocket!", "Wonderful! A sweet, peace-loving people, with a love of social justice. May you always find coin in your pocket!"),
         "src": two("The Assault on Fort Mercer (RDR1, Act I), when John asks what Mexico is like",
                    "The Assault on Fort Mercer (RDR1, acte I), quand John demande à quoi ressemble le Mexique. Traduction : « Merveilleux ! Un peuple doux, pacifique, épris de justice sociale. Puisses-tu toujours avoir une pièce en poche ! »")},
    ]},
    {"h4": two("Red Dead Redemption, Act III", "Red Dead Redemption, acte III")},
    {"quotes": [
        {"q": two("Marston: I thought you were headed to Peking. / West Dickens: So did I...so did I...a long story, but now it seems I'm...being put under arrest and charged with narcotic possession or some other such nonsense.", "Marston: I thought you were headed to Peking. / West Dickens: So did I...so did I...a long story, but now it seems I'm...being put under arrest and charged with narcotic possession or some other such nonsense."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), at the Blackwater police station",
                    "Bear One Another's Burdens (RDR1, acte III), au poste de police de Blackwater. Traduction : « Marston : Je croyais que tu partais pour Pékin. / West Dickens : Moi aussi... moi aussi... c'est une longue histoire, mais il semble que maintenant on m'arrête pour détention de stupéfiants ou je ne sais quelle autre ânerie. »")},
        {"q": two("Because he's a harmless old fraud. The kind of man that built this country. And because he helped me get Williamson.", "Because he's a harmless old fraud. The kind of man that built this country. And because he helped me get Williamson."),
         "src": two("John Marston, Bear One Another's Burdens (RDR1, Act III), when Ross asks why he should release Dickens",
                    "John Marston, Bear One Another's Burdens (RDR1, acte III), quand Ross demande pourquoi il devrait relâcher Dickens. Traduction : « Parce que c'est un vieil escroc inoffensif. Le genre d'homme qui a bâti ce pays. Et parce qu'il m'a aidé à avoir Williamson. »")},
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"quotes": [
        {"q": two("Now, don't be like that. Don't you remember the good times?", "Now, don't be like that. Don't you remember the good times?"),
         "src": two("A Cure for Most of What Ails You (Undead Nightmare), answering John, who asks whether he is back to doing Dickens's dirty work",
                    "A Cure for Most of What Ails You (Undead Nightmare), à John, qui demande s'il en est revenu à faire le sale boulot de Dickens. Traduction : « Allons, ne sois pas comme ça. Tu ne te souviens pas du bon vieux temps ? »")},
        {"q": two("Well... the border is indeed closed. But the Army is sending a train down there. Now, whether it's to help the Mexicans there, or to escape their problems here, I have no idea.", "Well... the border is indeed closed. But the Army is sending a train down there. Now, whether it's to help the Mexicans there, or to escape their problems here, I have no idea."),
         "src": two("American Imperialism (Undead Nightmare)",
                    "American Imperialism (Undead Nightmare). Traduction : « Eh bien... la frontière est fermée, c'est vrai. Mais l'armée envoie un train là-bas. Est-ce pour aider les Mexicains ou pour fuir ses problèmes ici, je n'en ai pas la moindre idée. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("In the Red Dead Wiki transcript of \"Old Swindler Blues\", Dickens names the Bollard Twins and Walton's Gang when he recognizes John. According to the character page of the same wiki, he only mentions a gang when John wears the Walton's Gang Outfit or the Bollard Twins Outfit.",
            "Dans la transcription de \"Old Swindler Blues\" publiée par le Red Dead Wiki, Dickens cite les Bollard Twins et le Walton's Gang quand il reconnaît John. D'après la page du personnage sur ce même wiki, il ne parle d'un gang que si John porte la tenue du Walton's Gang ou celle des Bollard Twins."),
        two("According to the Red Dead Wiki, when he is low on health during \"Old Swindler Blues\", Dickens can say \"I'm coming home, Daddy.\"",
            "D'après le Red Dead Wiki, quand sa santé est au plus bas pendant \"Old Swindler Blues\", Dickens peut dire \"I'm coming home, Daddy.\" (j'arrive, papa)."),
        two("The mission page of \"You Shall Not Give False Testimony, Except for Profit\" notes that its title parodies the commandment against bearing false witness (Exodus 20:16 and Deuteronomy 5:20). According to the same page, Dickens can run over a local with his stagecoach on the way into the farm. After the mission, he stays on his wagon; if John threatens him, he runs away or fires back, but he cannot be killed.",
            "La page de la mission \"You Shall Not Give False Testimony, Except for Profit\" relève que son titre parodie le commandement contre le faux témoignage (Exode 20:16 et Deutéronome 5:20). D'après la même page, Dickens peut renverser un habitant avec sa diligence en arrivant à la ferme. Après la mission, il reste sur son chariot ; si John le menace, il s'enfuit ou riposte, mais il est impossible de le tuer."),
        two("The title \"Can a Swindler Change His Spots?\" refers to Jeremiah 13:23, about the leopard that cannot change its spots. According to the mission page, most of the townspeople Dickens has swindled in that mission belong to the Williamson gang. If the player waits at Cueva Seca at the end of the mission, Dickens urinates on the ground, and keeps going even if knocked over.",
            "Le titre \"Can a Swindler Change His Spots?\" renvoie à Jérémie 13:23 et au léopard qui ne peut changer ses taches. D'après la page de la mission, la plupart des habitants que Dickens a escroqués appartiennent à la bande de Williamson. Si le joueur s'attarde à Cueva Seca à la fin de la mission, Dickens urine par terre, et continue même si on le renverse."),
        two("According to the Red Dead Wiki, Dickens, Agustin Allende and Luisa Fortuna are the only major characters of Red Dead Redemption who never ride a horse.",
            "D'après le Red Dead Wiki, Dickens, Agustin Allende et Luisa Fortuna sont les seuls personnages majeurs de Red Dead Redemption qui ne montent jamais à cheval."),
        two("According to the Red Dead Wiki, Dickens says in conversation that he once tried to sell his elixir at MacFarlane's Ranch and was chased away by [[bonnie-macfarlane|Bonnie MacFarlane]] herself; the wiki does not say in which mission.",
            "D'après le Red Dead Wiki, Dickens raconte avoir un jour tenté de vendre son élixir au ranch MacFarlane, d'où [[bonnie-macfarlane|Bonnie MacFarlane]] l'a chassé en personne ; le wiki ne précise pas dans quelle mission."),
        two("According to the Red Dead Wiki, a man named Wilton Glover says the tonic makes one's chestnuts bleed.",
            "D'après le Red Dead Wiki, un certain Wilton Glover affirme que le tonique fait saigner les bijoux de famille."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"ul": [
        two("In Undead Nightmare, the elixir becomes the Undead Bait; according to the Red Dead Wiki, it is the only way for the player to obtain the tonic. It can be crafted from one Wild Feverfew and one Prairie Poppy. Landon Ricketts combines it with dynamite to make Boom Bait.",
            "Dans Undead Nightmare, l'élixir devient l'Undead Bait ; d'après le Red Dead Wiki, c'est la seule façon pour le joueur de se procurer le tonique. On peut le fabriquer avec une Wild Feverfew et un Prairie Poppy. Landon Ricketts l'associe à de la dynamite pour obtenir le Boom Bait."),
        two("Among the writings on the walls of Blackwater in Undead Nightmare is the sentence \"I know a cure for all ailments\", which Dickens says to John in \"You Shall Not Give False Testimony, Except for Profit\".",
            "Parmi les inscriptions sur les murs de Blackwater dans Undead Nightmare figure la phrase \"I know a cure for all ailments\" (je connais un remède à tous les maux), que Dickens adresse à John dans \"You Shall Not Give False Testimony, Except for Profit\"."),
        two("According to the Red Dead Wiki, Dickens carries a small box that he handles with care and that rattles. The wiki also says that he and Seth are the only uninfected major characters of the expansion who never fight the undead.",
            "D'après le Red Dead Wiki, Dickens transporte une petite boîte qu'il manipule avec précaution et qui fait du bruit quand on la secoue. Le wiki ajoute que Seth et lui sont les seuls personnages majeurs non infectés de l'extension à ne jamais combattre les morts-vivants."),
        two("Completing \"A Cure for Most of What Ails You\" and Seth's \"Get Back in That Hole, Partner\" unlocks the achievement \"Judge A Man By The...\".",
            "Terminer \"A Cure for Most of What Ails You\" et \"Get Back in That Hole, Partner\", la mission de Seth, débloque le succès \"Judge A Man By The...\"."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("The Man from Blackwater (2010)", "The Man from Blackwater (2010)")},
    {"p": two("Dickens appears in Red Dead Redemption: The Man from Blackwater, a short film made with the game's engine, directed by John Hillcoat and broadcast by Fox on May 29, 2010. The film follows the first act, in which John teams up with Leigh Johnson, Dickens and Seth Briars to take Fort Mercer, and reuses scenes from \"Old Swindler Blues\" and \"The Assault on Fort Mercer\" among others.",
              "Dickens apparaît dans Red Dead Redemption: The Man from Blackwater, un court métrage réalisé avec le moteur du jeu par John Hillcoat et diffusé par Fox le 29 mai 2010. Le film reprend le premier acte, où John s'allie à Leigh Johnson, à Dickens et à Seth Briars pour prendre Fort Mercer, et réutilise notamment des scènes de \"Old Swindler Blues\" et de \"The Assault on Fort Mercer\".")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Dickens became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. Players select him in the Redemption section of the Outfitter, alongside [[john-marston|John]], [[abigail-marston|Abigail]], [[jack-marston|Jack]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[leigh-johnson|Leigh Johnson]], [[luisa-fortuna|Luisa Fortuna]] and [[seth-briars|Seth Briars]]. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, do not include the multiplayer mode.",
              "Dickens devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. On le choisit dans la section Redemption de l'Outfitter, aux côtés de [[john-marston|John]], d'[[abigail-marston|Abigail]], de [[jack-marston|Jack]], de [[bonnie-macfarlane|Bonnie MacFarlane]], de [[leigh-johnson|Leigh Johnson]], de [[luisa-fortuna|Luisa Fortuna]] et de [[seth-briars|Seth Briars]]. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, ne comprennent pas le multijoueur.")},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"p": two("Red Dead Redemption 2 does not show Dickens. He is named in a customer's letter in the Wheeler, Rawson and Co. catalogue and in a 1907 newspaper article (see Biography).",
              "Red Dead Redemption 2 ne montre pas Dickens. Il est cité dans la lettre d'une cliente du catalogue Wheeler, Rawson and Co. et dans un article de presse de 1907 (voir la biographie).")},
]
