"""Abigail Marston, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched 19 Oct 2026 via the MediaWiki API, saved in
scratchpad cov/abigail/, cov/abigail/m/ and cov/abigail/mc/):
- Red Dead Wiki EN "Abigail Marston" (Mission Appearances, Murders Committed, Quotes,
  Trivia, Gallery captions) and FR "Abigail Marston" (Apparitions dans les missions,
  Anecdotes).
- Mission pages: Outlaws from the West; Enter, Pursued by a Memory; Who the Hell is
  Leviticus Cornwall?; Eastward Bound; A Fisher of Men; Advertising, The New American
  Art; Blood Feuds, Ancient and Modern; The Battle of Shady Belle; Angelo Bronte, a Man
  of Honor; Horsemen, Apocalypses; Banking, The Old American Art; Fleeting Joy; That's
  Murfree Country; Visiting Hours; A Rage Unleashed; Red Dead Redemption (mission); The
  Wheel; Simple Pleasures; Farming, For Beginners; Fatherhood, For Beginners;
  Fatherhood, For Idiots; Old Habits; Jim Milton Rides, Again?; Motherhood; A New
  Jerusalem; The Best of Women; Trying Again; A Really Big Bastard; A New Future
  Imagined; American Venom; Ending Credits; activity pages Errand Boy and Dominoes;
  location page Beecher's Hope (RDR1 and RDR2 sections); document page Letter from
  Abigail. RDR1: The Outlaw's Return; Pestilence; Old Friends, New Problems; By Sweat
  and Toil; A Continual Feast; John Marston and Son; Wolves, Dogs and Sons; Spare the
  Love, Spoil the Child; The Last Enemy That Shall Be Destroyed. Undead Nightmare: Love
  in the Time of Plague; A Civilized Man; On a Pale Horse. DLC page Liars and Cheats.
- Transcripts "/dialogues": Outlaws from the West; Enter, Pursued by a Memory; Who the
  Hell is Leviticus Cornwall?; Eastward Bound; A Fisher of Men; Red Dead Redemption
  (mission); American Venom (with the post-credit scene); The Outlaw's Return;
  Pestilence; Old Friends, New Problems; The Last Enemy That Shall Be Destroyed. Every
  quote is checked word for word against one of them, except: the line from "The
  Wheel" (quote box at the top of the character page), the line from "A New Future
  Imagined" (quote box of the mission page), the Strawberry sign and the sheep lines
  and the multiplayer lines (quote list of the character page). The wiki has no
  transcript for the epilogue missions other than American Venom, nor for Undead
  Nightmare, so no Undead Nightmare line is quoted.
- Real world: Liars and Cheats Pack, released September 21, 2010 (Rockstar Newswire as
  cited by the wiki; "detailed" on August 27, 2010 as established in bill_C); RDR1 ports
  (PS4 and Switch, August 17, 2023; PC, October 29, 2024) without multiplayer, as in
  bill_C and javier_C; character portraits and descriptions posted on Twitter on
  September 6, 2018 and reproduced by The Hollywood Reporter on September 7, 2018
  (fc/thr_descriptions.txt, where the tweet is captioned "Abigail Roberts").
Ownership (FIX_RULES): left to other parts: Origins, birth year, grave inscription and
1914 death, the Yukon years, the guard line paraphrase, Hosea's praise of her acting and
the explosive device, the letter of "Motherhood" in full (A); official descriptions
(Rockstar THR, Complete Official Guide), names and aliases (Abby, Agatha Milton, née
Roberts), appearance and outfits, camp scenes (Micah's advances, Susan, Sadie, Hosea,
Molly, Kieran, John slaps), Arthur's journal entry about her, Uncle's "lucky man" line,
the Bonnie jealousy as a relationship (B); Sophia Marzocchi and Cali Elizabeth Moore,
cut content (unused Abigail kidnapping in RDR1, "ind2" mission, unused RDR2 lines by
Marzocchi, unused cutscene after the Blackwater date) (D). The Old Friends, New Problems
line "The life we led, that doesn't go away. It's never over." is NOT quoted here: the
wiki uses it as the Personality epigraph, so B is expected to own it.
Fact-check pass (19 Oct 2026): the four lines of B "In her own words" ("new low", "corpse",
"good thief", "It's home") are removed from Quotes; the Strawberry and sheep lines move to a
"no mission given" group (the quote list names no mission); "orphaned working girl" and
"illiterate gunslinger" (Pestilence transcript) are added, B paraphrases the first; the 11
remaining multiplayer lines of the quote list are added (coverage #7). Trivia keeps only facts
found nowhere else: height gap (B Appearance), illiteracy and the letter postscript, dominoes
at eight and the ranch chores (B Skills), the first moving picture and the Pestilence cooking
admission (A), the Undead Nightmare plates and bedroom window (A) are cut. The wedding on the
hill is attributed to the wiki's "American Venom" page (the Ending Credits page says "just
outside the ranch"). The THR "Abigail Roberts" caption is left to B Names.
Excluded: the wiki's "Abigail was ultimately correct" reading of the RDR2 ending
(analysis); "it is implied that Bill and Javier wanted to be with Abigail" (stated as an
implication); the Etta Place / Sundance Kid resemblance (interpretation); the "she seems
to believe John was attracted to Bonnie" reading; the "how many times do I have to bury
you" foreshadowing (no transcript, interpretation); the claim in the Pestilence trivia
that she reveals John was also an orphan (the transcript only has her calling herself an
"orphaned working girl"); FR anecdotes on townswomen who resemble her, John looking
annoyed when she talks about the past, the face-model rumor (speculation or rumor), and
her age in 1911 (derived from the birth year, owned by A); the Ending Credits cliff-fall
glitch and other glitches (no value); the "Abigail likely managed to escape" phrasing of
the Banking page (replaced by the fact that she is not seen again in the mission); the
Red Dead Online search (no Abigail-related item found on the wiki).
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
C24 = two("2 and 4", "2 et 4")
EP1 = two("Epilogue 1: Pronghorn Ranch", "Épilogue 1 : Pronghorn Ranch")
EP2 = two("Epilogue 2: Beecher's Hope", "Épilogue 2 : Beecher's Hope")
A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
UNM = two("Undead Nightmare", "Undead Nightmare")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 28 story missions of Red Dead Redemption 2 for Abigail, from the arrival at Colter to the wedding at Beecher's Hope, four missions of Red Dead Redemption and three of Undead Nightmare. The French edition counts 26 missions for Red Dead Redemption 2: it leaves out \"Eastward Bound\", \"Fleeting Joy\" and \"Trying Again\", and adds \"A Kind and Benevolent Despot\", a Guarma mission in which she does not appear; its page mentions her only in Dutch's question about how she escaped the bank. For Red Dead Redemption, it adds four missions at Beecher's Hope. The table below also includes \"Advertising, The New American Art\", whose page names her as one of the two mission givers although neither list includes it.",
              "Le Red Dead Wiki anglais recense pour Abigail 28 missions principales de Red Dead Redemption 2, de l'arrivée à Colter jusqu'au mariage à Beecher's Hope, quatre missions de Red Dead Redemption et trois d'Undead Nightmare. L'édition française compte 26 missions pour Red Dead Redemption 2 : elle omet \"Eastward Bound\", \"Fleeting Joy\" et \"Trying Again\", et ajoute \"A Kind and Benevolent Despot\", une mission de Guarma où elle n'apparaît pas ; sa page ne la cite qu'à travers Dutch, qui se demande comment elle a pu s'échapper de la banque. Pour Red Dead Redemption, elle ajoute quatre missions à Beecher's Hope. Le tableau ci-dessous reprend aussi \"Advertising, The New American Art\" : la page de cette mission la désigne comme l'une des deux donneuses de mission, alors qu'aucune des deux listes ne la retient.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 to 6", "Red Dead Redemption 2, chapitres 1 à 6")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Abigail's role", "Rôle d'Abigail")], "rows": [
        M("Outlaws from the West", C1,
          "Travels with the gang through the snow after Blackwater. Swanson tells Dutch that Abigail says Davey Callander is dying. At Colter, she enters the cabin ahead of Bill and Arthur, who carry Davey's body on a stretcher, and tells the others he is dead.",
          "Fait route avec le gang dans la neige après Blackwater. Swanson rapporte à Dutch qu'Abigail juge Davey Callander mourant. À Colter, elle entre dans la cabane devant Bill et Arthur, qui portent le corps de Davey sur un brancard, et annonce sa mort aux autres."),
        M("Enter, Pursued by a Memory", C1,
          "Mission giver. John has not been seen for two days, and she asks [[arthur-morgan|Arthur]] to go and look for him; [[hosea-matthews|Hosea]] backs her up. When Arthur and [[javier-escuella|Javier]] bring John back, she thanks them both, then tells John he has reached a new low.",
          "Donneuse de mission. John n'a pas reparu depuis deux jours ; elle demande à [[arthur-morgan|Arthur]] d'aller le chercher, et [[hosea-matthews|Hosea]] appuie sa demande. Quand Arthur et [[javier-escuella|Javier]] ramènent John, elle les remercie tous les deux, puis lance à John qu'il est tombé plus bas que jamais."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "Brings [[jack-marston|Jack]], who wanted to see his father, into the cabin where [[john-marston|John]] lies in bed. She exchanges insults with John in front of [[dutch-van-der-linde|Dutch]], then takes Jack out.",
          "Amène [[jack-marston|Jack]], qui voulait voir son père, dans la cabane où [[john-marston|John]] est alité. Elle échange des piques avec John devant [[dutch-van-der-linde|Dutch]], puis ressort avec Jack."),
        M("Eastward Bound", C1,
          "Helps [[charles-smith|Charles]] walk the injured John to a wagon before the gang leaves the mountains. At Horseshoe Overlook, she walks over to [[susan-grimshaw|Susan]] with the others while Arthur and Dutch sit down at a table.",
          "Aide [[charles-smith|Charles]] à conduire John, blessé, jusqu'à un chariot avant que le gang ne quitte la montagne. À Horseshoe Overlook, elle rejoint [[susan-grimshaw|Susan]] avec les autres pendant qu'Arthur et Dutch s'installent à une table."),
        M("A Fisher of Men", C2,
          "Mission giver. She asks Arthur to do something with Jack, who seems down, and he takes the boy fishing. On their return, Jack gives her a flower necklace. She sees that Arthur looks worried and asks what is wrong; he keeps the meeting with [[andrew-milton|Milton]] and [[edgar-ross|Ross]] for Dutch.",
          "Donneuse de mission. Elle demande à Arthur de s'occuper un peu de Jack, qui a l'air abattu, et il l'emmène pêcher. À leur retour, Jack lui offre un collier de fleurs. Elle remarque l'air soucieux d'Arthur et lui demande ce qui ne va pas ; il réserve à Dutch le récit de sa rencontre avec [[andrew-milton|Milton]] et [[edgar-ross|Ross]]."),
        M("Advertising, The New American Art", C3,
          "Mission giver with Hosea, according to the mission page. She tells Arthur that Hosea is waiting for him at the stolen moonshine stash, because Dutch has given John another job.",
          "Donneuse de mission avec Hosea, selon la page de la mission. Elle prévient Arthur que Hosea l'attend près du moonshine volé, Dutch ayant confié une autre tâche à John."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Tells Arthur, back from the Rhodes ambush of \"A Short Walk in a Pretty Town\", that Jack has disappeared. The gang concludes that the Braithwaites took him, and Dutch rides to Braithwaite Manor with seven men to find him.",
          "Apprend à Arthur, de retour de l'embuscade de Rhodes (\"A Short Walk in a Pretty Town\"), que Jack a disparu. Le gang en conclut que les Braithwaite l'ont enlevé, et Dutch part pour Braithwaite Manor avec sept hommes pour le retrouver."),
        M("The Battle of Shady Belle", C3,
          "Listed by the wiki. The mission page mentions her only through John, who worries about how she will react while Jack is still missing.",
          "Citée par le wiki. La page de la mission ne l'évoque qu'à travers John, inquiet de sa réaction tant que Jack reste introuvable."),
        M("Angelo Bronte, a Man of Honor", C4,
          "Overjoyed when Dutch, Arthur and John bring Jack back from [[angelo-bronte|Bronte]]'s house. The gang holds a party at Shady Belle that evening for his return.",
          "Laisse éclater sa joie quand Dutch, Arthur et John ramènent Jack de chez [[angelo-bronte|Bronte]]. Le soir même, le gang fait la fête à Shady Belle pour son retour."),
        M("Horsemen, Apocalypses", C4,
          "Takes cover inside the Shady Belle house with [[mary-beth-gaskill|Mary-Beth]], [[leopold-strauss|Strauss]], Jack and Susan when the O'Driscolls attack the camp.",
          "Se met à l'abri dans la maison de Shady Belle avec [[mary-beth-gaskill|Mary-Beth]], [[leopold-strauss|Strauss]], Jack et Susan quand les O'Driscoll attaquent le camp."),
        M("Banking, The Old American Art", C4,
          "Sets up the diversion with Hosea while the others enter the Lemoyne National Bank. Milton captures Hosea during the diversion; Abigail is not seen again in the mission.",
          "Monte la diversion avec Hosea pendant que les autres entrent dans la Lemoyne National Bank. Milton capture Hosea pendant la diversion ; Abigail ne réapparaît plus dans la mission."),
        M("Fleeting Joy", C5,
          "At Lakay, she tells Dutch, just back from Guarma, that Hosea's and Lenny's bodies were taken from the morgue and buried. She reminds him that John is in prison; when Dutch puts off a rescue, she asks Arthur and [[sadie-adler|Sadie]] to free John, and they agree.",
          "À Lakay, elle apprend à Dutch, de retour de Guarma, que les corps de Hosea et de Lenny ont été repris à la morgue et enterrés. Elle lui rappelle que John est en prison ; comme Dutch remet le sauvetage à plus tard, elle demande à Arthur et à [[sadie-adler|Sadie]] de libérer John, et ils acceptent."),
        M("That's Murfree Country", C5,
          "Listed by the wiki for the gang's move to Beaver Hollow. The mission page gives her no individual action.",
          "Citée par le wiki pour l'installation du gang à Beaver Hollow. La page de la mission ne lui attribue aucune action propre."),
        M("Visiting Hours", C6,
          "At Copperhead Landing, she asks Arthur and Sadie to take her to Sisika. They refuse, saying she would be one more person to worry about; she accepts and thanks them.",
          "À Copperhead Landing, elle demande à Arthur et à Sadie de l'emmener à Sisika. Ils refusent : ce serait une personne de plus à protéger. Elle s'incline et les remercie."),
        M("A Rage Unleashed", C6,
          "Listed by the wiki. The mission page gives her no individual action.",
          "Citée par le wiki. La page de la mission ne lui attribue aucune action propre."),
        M("Red Dead Redemption", C6,
          "Mission giver. Grabbed by Milton's men outside camp while she is with Tilly and Jack, she is held at Van Horn. She frees herself and shoots Milton, who is holding Arthur at gunpoint. Arthur tells her on the ride out that John was killed or captured. Before leaving with Sadie for Copperhead Landing, she gives Arthur the key to Dutch's chest.",
          "Donneuse de mission. Enlevée par les hommes de Milton à l'extérieur du camp, alors qu'elle se trouve avec Tilly et Jack, elle est retenue à Van Horn. Elle se libère et abat Milton, qui tient Arthur en joue. Pendant la fuite, Arthur lui apprend que John a été tué ou capturé. Avant de partir avec Sadie pour Copperhead Landing, elle remet à Arthur la clé du coffre de Dutch."),
    ]}},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"p": two("Abigail is absent from Beecher's Hope during the first missions of the second epilogue. In \"Home Improvement for Beginners\", Uncle mocks John's hopes of winning her back; in \"A New Jerusalem\", John writes her a letter once the house is built. Neither mission shows her.",
              "Abigail est absente de Beecher's Hope pendant les premières missions du second épilogue. Dans \"Home Improvement for Beginners\", Uncle se moque de l'espoir de John de la reconquérir ; dans \"A New Jerusalem\", John lui écrit une lettre une fois la maison construite. Aucune de ces deux missions ne la montre.")},
    {"table": {"head": [two("Mission", "Mission"), two("Part", "Partie"), two("Abigail's role", "Rôle d'Abigail")], "rows": [
        M("The Wheel", EP1,
          "Sits beside John on the wagon as the family moves on once again, and reproaches him for shooting a man. They settle on Strawberry. In town, she finds work cleaning the doctor's office.",
          "Assise à côté de John sur le chariot, alors que la famille doit de nouveau partir, elle lui reproche d'avoir tiré sur un homme. Ils choisissent Strawberry. En ville, elle trouve une place de femme de ménage chez le médecin."),
        M("Simple Pleasures", EP1,
          "Arrives at Pronghorn Ranch with Jack and moves into the cabin. She warns John that his recklessness puts them in danger, and later tells him she is tired of running and wants to settle down.",
          "Arrive à Pronghorn Ranch avec Jack et s'installe dans la cabane. Elle prévient John que son imprudence les met en danger, puis lui confie qu'elle est lasse de fuir et veut se poser."),
        M("Farming, For Beginners", EP1,
          "At breakfast, she tells John about her job at the doctor's office.",
          "Au petit déjeuner, elle parle à John de son travail chez le médecin."),
        M("Fatherhood, For Beginners", EP1,
          "Persuades John to go riding with Jack, on a pony lent by Duncan Geddes.",
          "Convainc John d'aller faire du cheval avec Jack, sur un poney prêté par Duncan Geddes."),
        M("Fatherhood, For Idiots", EP1,
          "Mission giver. She raises the idea of a bank loan to buy Beecher's Hope, and they argue in front of Jack. She asks John to pick up a parcel for her in Strawberry. When he comes back, Jack pushes past her, and John admits that someone who knew him shot at them.",
          "Donneuse de mission. Elle évoque un prêt bancaire pour acheter Beecher's Hope, et le couple se dispute devant Jack. Elle demande à John de lui rapporter un colis de Strawberry. Au retour, Jack la bouscule pour rentrer, et John finit par avouer qu'un homme qui le connaissait leur a tiré dessus."),
        M("Old Habits", EP1,
          "Stops John's fistfight with the Laramie leader, who then harasses her. Afterwards, she reproaches John for breaking his promise of no more violence.",
          "Interrompt la bagarre entre John et le chef des Laramie, qui s'en prend alors à elle. Elle reproche ensuite à John d'avoir rompu sa promesse de renoncer à la violence."),
        M("Jim Milton Rides, Again?", EP1,
          "Angry at John for taking part in the fight against the Laramie raiders. He answers that he had no choice and was doing his job.",
          "En colère contre John, qui a pris part au combat contre les pillards Laramie. Il répond qu'il n'avait pas le choix et qu'il faisait son travail."),
        M("Motherhood", EP1,
          "Absent: she has left Pronghorn Ranch with Jack. John finds her letter and the shirt she left him as a gift.",
          "Absente : elle a quitté Pronghorn Ranch avec Jack. John trouve sa lettre et la chemise qu'elle lui a laissée en cadeau."),
        M("The Best of Women", EP2,
          "Mission giver. A single cutscene: she returns to Beecher's Hope with Jack after months apart and discovers the house John built with Uncle and Charles.",
          "Donneuse de mission. Une seule cinématique : elle revient à Beecher's Hope avec Jack après des mois de séparation et découvre la maison que John a bâtie avec Uncle et Charles."),
        M("Trying Again", EP2,
          "After the fishing trip, she and John reassure Jack that Rufus, bitten by a snake, will recover in a few days.",
          "Après la partie de pêche, John et elle rassurent Jack : Rufus, mordu par un serpent, sera remis dans quelques jours."),
        M("A Really Big Bastard", EP2,
          "Mission giver with Sadie. She invites Sadie, whom she has not seen in eight years, to lunch. She learns that John has been hunting bounties, objects, then lets him take a low-risk job with Sadie. She refuses any hunt for [[micah-bell|Micah]].",
          "Donneuse de mission avec Sadie. Elle invite à déjeuner Sadie, qu'elle n'a pas revue depuis huit ans. Elle apprend que John chasse les primes, s'y oppose, puis le laisse partir avec Sadie sur un contrat sans grand risque. Elle refuse en revanche toute traque de [[micah-bell|Micah]]."),
        M("A New Future Imagined", EP2,
          "Mission giver. After a quarrel with Uncle about his work, she spends a day in Blackwater with John: a photograph at the studio, a moving picture at the Imperial Theatre, then a canoe on the lake, where she accepts his proposal.",
          "Donneuse de mission. Après une dispute avec Uncle sur son peu d'ardeur au travail, elle passe une journée à Blackwater avec John : une photo au studio, un film à l'Imperial Theatre, puis une sortie en canoë sur le lac, où elle accepte sa demande en mariage."),
        M("American Venom", EP2,
          "Mission giver with Sadie. She tries to answer for John when Sadie brings a lead on Micah, then begs him not to go. On his return, she welcomes him. The credits show their wedding and a dance outside the house; in the closing scene, she tells John the ranch is home.",
          "Donneuse de mission avec Sadie. Elle tente de répondre à la place de John quand Sadie apporte une piste vers Micah, puis le supplie de ne pas partir. À son retour, elle l'accueille. Le générique montre leur mariage et une danse devant la maison ; dans la scène finale, elle dit à John que le ranch, c'est chez eux."),
    ]}},
    {"h4": two("Red Dead Redemption 2: other activities", "Red Dead Redemption 2 : autres activités")},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Abigail's role", "Rôle d'Abigail")], "rows": [
        M("Errand Boy", C2,
          "One of the camp members who can ask Arthur for something: she asks for 5 dollars.",
          "Fait partie des membres du camp qui peuvent solliciter Arthur : elle lui demande 5 dollars."),
        M("Dominoes", C24,
          "One of the camp members Arthur can play dominoes with, along with Hosea and Mary-Beth (and Pearson in chapter 4).",
          "Fait partie des membres du camp avec qui Arthur peut jouer aux dominos, avec Hosea et Mary-Beth (et Pearson au chapitre 4)."),
    ]}},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"p": two("Abigail is held by the Bureau with Jack through most of the game, and appears in person only once John has returned to Beecher's Hope. The French wiki also counts \"By Sweat and Toil\", \"A Continual Feast\", \"John Marston and Son\" and \"Wolves, Dogs and Sons\"; their pages name her only among the people the player must not harm, as do the pages of \"Spare the Love, Spoil the Child\".",
              "Retenue par le Bureau avec Jack pendant l'essentiel du jeu, Abigail n'apparaît en personne qu'une fois John revenu à Beecher's Hope. Le wiki français compte aussi \"By Sweat and Toil\", \"A Continual Feast\", \"John Marston and Son\" et \"Wolves, Dogs and Sons\" ; leurs pages ne la citent que parmi les personnes que le joueur ne doit pas blesser, tout comme celle de \"Spare the Love, Spoil the Child\".")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Abigail's role", "Rôle d'Abigail")], "rows": [
        M("The Outlaw's Return", A3,
          "Mission giver. She greets John at the ranch with insults and blows, having thought he was dead. She asks whether he saw Dutch and Bill, and whether he went back to them. This is the first mission in which she appears on screen.",
          "Donneuse de mission. Elle accueille John au ranch à coups d'insultes et de poing : elle le croyait mort. Elle lui demande s'il a revu Dutch et Bill, et s'il est retourné vers eux. C'est la première mission où elle apparaît à l'écran."),
        M("Pestilence", A3,
          "Mission giver. While cooking, she talks with John about Jack's future, then spots crows raiding the silo and sends John to deal with them.",
          "Donneuse de mission. Aux fourneaux, elle parle avec John de l'avenir de Jack, puis aperçoit les corbeaux qui pillent le silo et envoie John s'en occuper."),
        M("Old Friends, New Problems", A3,
          "Mission giver. A telegram from [[bonnie-macfarlane|Bonnie MacFarlane]] asks for corn; Abigail has John read it aloud. She rides with him to MacFarlane's Ranch, questions him about Bonnie on the way, meets her, and on the ride home says she likes her.",
          "Donneuse de mission. Un télégramme de [[bonnie-macfarlane|Bonnie MacFarlane]] réclame du maïs ; Abigail demande à John de le lire à voix haute. Elle l'accompagne au MacFarlane's Ranch, l'interroge sur Bonnie pendant le trajet, fait sa connaissance et, sur le chemin du retour, avoue qu'elle l'apprécie."),
        M("The Last Enemy That Shall Be Destroyed", A3,
          "After [[uncle|Uncle]] is killed, she runs to the barn with Jack. John puts them on a horse; she and John say they love each other before the horse leaves by the back door. When the shooting stops, she tells Jack to ride back. They find John dead and bury him on the hill next to Uncle. The closing scene, in 1914, shows her grave beside John's.",
          "Après la mort d'[[uncle|Uncle]], elle court jusqu'à la grange avec Jack. John les fait monter à cheval ; John et elle se disent leur amour avant que le cheval ne sorte par la porte de derrière. Quand les coups de feu cessent, elle demande à Jack de faire demi-tour. Ils trouvent John mort et l'enterrent sur la colline, à côté d'Uncle. La scène finale, en 1914, montre sa tombe à côté de celle de John."),
    ]}},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors continuité)")},
    {"p": two("Undead Nightmare is set outside the series' continuity. Two of the three missions listed by the wiki take place at Beecher's Hope; the third, in Escalera, ends with John told to go back to his family.",
              "Undead Nightmare se déroule hors de la continuité de la série. Deux des trois missions retenues par le wiki se passent à Beecher's Hope ; la troisième, à Escalera, s'achève quand John reçoit l'ordre de rentrer auprès des siens.")},
    {"table": {"head": [two("Mission", "Mission"), two("Game", "Jeu"), two("Abigail's role", "Rôle d'Abigail")], "rows": [
        M("Love in the Time of Plague", UNM,
          "She thought Uncle was with John and tells him Uncle can look after himself. During the night, the undead Uncle chases her out of the house and bites her. She turns and bites Jack; John hogties them both.",
          "Elle croyait Uncle avec John et lui assure qu'Uncle sait se débrouiller. Dans la nuit, Uncle, devenu mort-vivant, la poursuit hors de la maison et la mord. Elle se transforme et mord Jack ; John les ligote tous les deux."),
        M("A Civilized Man", UNM,
          "Listed by the wiki. She does not appear on the mission page: at the end, Ayauhtéotl's voice tells John to go back to his family.",
          "Citée par le wiki. Elle n'apparaît pas sur la page de la mission : à la fin, la voix d'Ayauhtéotl dit à John de retourner auprès des siens."),
        M("On a Pale Horse", UNM,
          "The character page marks her as only mentioned, but the mission page shows John finding his wife and son still tied up but no longer infected, and holding them.",
          "La page du personnage la dit seulement mentionnée, mais celle de la mission montre John qui retrouve sa femme et son fils, toujours attachés mais libérés de l'infection, et les serre contre lui."),
    ]}},
    # ---------------------------------------------------------- notable kills
    {"h3": two("Notable people Abigail kills", "Personnages notables tués par Abigail")},
    {"p": two("The Red Dead Wiki credits Abigail with a single murder.",
              "Le Red Dead Wiki n'attribue qu'un seul meurtre à Abigail.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K("[[andrew-milton|Andrew Milton]]", "Red Dead Redemption",
          "Storyline. Shot in the head with Sadie's revolver while he struggles with Arthur at Van Horn. The mission page notes that the shot comes whatever the player does during the struggle.",
          "Histoire. Abattu d'une balle dans la tête avec le revolver de Sadie pendant qu'il se bat avec Arthur à Van Horn. La page de la mission précise que le coup part quoi que fasse le joueur pendant la lutte."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Most are checked against the mission transcripts. The lines from \"The Wheel\" and \"A New Future Imagined\" come from quote boxes on the Red Dead Wiki, and the Strawberry, sheep and multiplayer lines from its quote list, which names no mission for them. The lines quoted under Personality, in \"In her own words\", are not repeated here. The wiki has no transcript of Abigail's lines in Undead Nightmare.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. La plupart sont vérifiées sur les transcriptions des missions. Celles de \"The Wheel\" et de \"A New Future Imagined\" proviennent d'encadrés du Red Dead Wiki ; celles sur Strawberry, sur les moutons et celles du multijoueur, de sa liste de citations, qui ne précise pas la mission. Les répliques déjà citées dans la personnalité, sous \"Dans ses propres mots\", ne sont pas reprises ici. Le wiki ne propose aucune transcription des répliques d'Abigail dans Undead Nightmare.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 and 2", "Red Dead Redemption 2, chapitres 1 et 2")},
    {"quotes": [
        {"q": two("Davey's dead.", "Davey's dead."),
         "src": two("Outlaws from the West (RDR2, chapter 1), to the gang gathered around Davey Callander's body in the cabin at Colter",
                    "Outlaws from the West (RDR2, chapitre 1), au gang réuni autour du corps de Davey Callander, dans la cabane de Colter. Traduction : « Davey est mort. »")},
        {"q": two("You're a rotten man, John Marston.", "You're a rotten man, John Marston."),
         "src": two("Who the Hell is Leviticus Cornwall? (RDR2, chapter 1), to John; Dutch adds that he is an idiot and that everyone knows it",
                    "Who the Hell is Leviticus Cornwall? (RDR2, chapitre 1), à John ; Dutch ajoute que c'est un idiot et que tout le monde le sait. Traduction : « Tu es un sale type, John Marston. »")},
        {"q": two("Because he likes you and, well... you know his father's useless.", "Because he likes you and, well... you know his father's useless."),
         "src": two("A Fisher of Men (RDR2, chapter 2), to Arthur, who asks why she chose him to take Jack out; it is one of her two possible answers, the other being that he does what he says",
                    "A Fisher of Men (RDR2, chapitre 2), à Arthur, qui lui demande pourquoi elle le choisit pour sortir Jack ; c'est l'une de ses deux réponses possibles, l'autre étant qu'il fait ce qu'il dit. Traduction : « Parce qu'il t'aime bien et, bon... tu sais que son père est bon à rien. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, chapter 6", "Red Dead Redemption 2, chapitre 6")},
    {"quotes": [
        {"q": two("Horrible man.", "Horrible man."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), after shooting Milton at Van Horn",
                    "Red Dead Redemption (RDR2, chapitre 6), après avoir abattu Milton à Van Horn. Traduction : « Quel homme abominable. »")},
        {"q": two("Call yourself men? You pathetic sons of bitches.", "Call yourself men? You pathetic sons of bitches."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), at the Pinkertons firing on Arthur, Sadie and her during the escape from Van Horn",
                    "Red Dead Redemption (RDR2, chapitre 6), aux Pinkerton qui tirent sur Arthur, Sadie et elle pendant la fuite de Van Horn. Traduction : « Et vous vous dites des hommes ? Pauvres fils de garce. »")},
        {"q": two("The bastards grabbed me outside camp... I was with Tilly and Jack... it happened so fast, I couldn't do anything.", "The bastards grabbed me outside camp... I was with Tilly and Jack... it happened so fast, I couldn't do anything."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), to Sadie, during the same escape",
                    "Red Dead Redemption (RDR2, chapitre 6), à Sadie, pendant la même fuite. Traduction : « Ces salauds m'ont attrapée près du camp... J'étais avec Tilly et Jack... Ça s'est passé si vite que je n'ai rien pu faire. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"quotes": [
        {"q": two("John... I love you. Don't you forget that... not ever now.", "John... I love you. Don't you forget that... not ever now."),
         "src": two("The Wheel (RDR2, epilogue 1), to John (quote box of the wiki's character page)",
                    "The Wheel (RDR2, épilogue 1), à John (encadré de la page du personnage sur le wiki). Traduction : « John... je t'aime. Ne l'oublie pas... plus jamais, maintenant. »")},
        {"q": two("John, I... I never... I didn't know it mattered to you.", "John, I... I never... I didn't know it mattered to you."),
         "src": two("A New Future Imagined (RDR2, epilogue 2), to John, when he proposes on the lake at Blackwater (quote box of the mission page)",
                    "A New Future Imagined (RDR2, épilogue 2), à John, quand il la demande en mariage sur le lac de Blackwater (encadré de la page de la mission). Traduction : « John, je... je n'avais jamais... Je ne savais pas que ça comptait pour toi. »")},
        {"q": two("What's for dinner? Away with you, you no good parasite... you cook.", "What's for dinner? Away with you, you no good parasite... you cook."),
         "src": two("American Venom (RDR2, epilogue 2), to Uncle, who asks what is for dinner; John says it is not a bad idea",
                    "American Venom (RDR2, épilogue 2), à Uncle, qui demande ce qu'il y a pour dîner ; John trouve l'idée plutôt bonne. Traduction : « Ce qu'il y a pour dîner ? Fiche le camp, espèce de parasite bon à rien... C'est toi qui cuisines. »")},
        {"q": two("I'm begging you. No! You'd risk all this? For what? For Micah?!", "I'm begging you. No! You'd risk all this? For what? For Micah?!"),
         "src": two("American Venom (RDR2, epilogue 2), to John, as he takes his guns to ride after Micah with Sadie and Charles",
                    "American Venom (RDR2, épilogue 2), à John, qui prend ses armes pour partir sur la piste de Micah avec Sadie et Charles. Traduction : « Je t'en supplie. Non ! Tu risquerais tout ça ? Pour quoi ? Pour Micah ?! »")},
        {"q": two("Alright, John Marston... since you bought this millstone around our necks, we better try and keep this place going.", "Alright, John Marston... since you bought this millstone around our necks, we better try and keep this place going."),
         "src": two("American Venom (RDR2, epilogue 2), to John, on the hill above the ranch after the credits",
                    "American Venom (RDR2, épilogue 2), à John, sur la colline qui domine le ranch, après le générique. Traduction : « Bon, John Marston... puisque tu nous as mis ce boulet au pied, on ferait bien d'essayer de faire tourner l'endroit. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, no mission given", "Red Dead Redemption 2, sans mission précisée")},
    {"quotes": [
        {"q": two("So, you saved the silly bastard's life then you and him go robbing sheep?", "So, you saved the silly bastard's life then you and him go robbing sheep?"),
         "src": two("Red Dead Redemption 2, to Arthur (quote list of the wiki)",
                    "Red Dead Redemption 2, à Arthur (liste de citations du wiki). Traduction : « Alors tu as sauvé la vie de cet abruti, et ensuite vous partez voler des moutons ensemble ? »")},
        {"q": two("I bet that sign says Strawberry, don't it?", "I bet that sign says Strawberry, don't it?"),
         "src": two("Red Dead Redemption 2 (quote list of the wiki)",
                    "Red Dead Redemption 2 (liste de citations du wiki). Traduction : « Je parie que ce panneau dit Strawberry, pas vrai ? »")},
    ]},
    {"h4": two("Red Dead Redemption, Act III", "Red Dead Redemption, acte III")},
    {"quotes": [
        {"q": two("You no-good, hillbilly, piece of shit. I thought you was dead. I thought you was dead, John.", "You no-good, hillbilly, piece of shit. I thought you was dead. I thought you was dead, John."),
         "src": two("The Outlaw's Return (RDR1, Act III), to John, hitting him as he arrives at the ranch",
                    "The Outlaw's Return (RDR1, acte III), à John, qu'elle frappe à son arrivée au ranch. Traduction : « Espèce de bouseux bon à rien, de sale ordure. Je te croyais mort. Je te croyais mort, John. »")},
        {"q": two("Yes, didn't I say, rather than some prison, they actually kept me incarcerated in a cooking school for young ladies.", "Yes, didn't I say, rather than some prison, they actually kept me incarcerated in a cooking school for young ladies."),
         "src": two("The Outlaw's Return (RDR1, Act III), to John, who hopes she has learned to cook",
                    "The Outlaw's Return (RDR1, acte III), à John, qui espère qu'elle a appris à cuisiner. Traduction : « Mais oui, je ne te l'ai pas dit ? Au lieu d'une prison, ils m'ont enfermée dans une école de cuisine pour jeunes filles. »")},
        {"q": two("The same thing I've been cooking the past 15 years with the hope of poisoning you.", "The same thing I've been cooking the past 15 years with the hope of poisoning you."),
         "src": two("Pestilence (RDR1, Act III), to John, who asks what she is cooking",
                    "Pestilence (RDR1, acte III), à John, qui lui demande ce qu'elle prépare. Traduction : « La même chose que depuis quinze ans, dans l'espoir de t'empoisonner. »")},
        {"q": two("Given what we was and where we came from, I think we've gone and done okay. I look at Jack ...I look at him and, I think we've been blessed. Maybe he can be something more.", "Given what we was and where we came from, I think we've gone and done okay. I look at Jack ...I look at him and, I think we've been blessed. Maybe he can be something more."),
         "src": two("Pestilence (RDR1, Act III), to John, in the kitchen",
                    "Pestilence (RDR1, acte III), à John, dans la cuisine. Traduction : « Vu ce qu'on était et d'où on vient, je trouve qu'on ne s'en est pas si mal sortis. Quand je regarde Jack... quand je le regarde, je me dis qu'on a eu de la chance. Il pourra peut-être devenir quelqu'un. »")},
        {"q": two("And he ain't gonna marry no orphaned working girl running with a bunch of hucksters, neither.", "And he ain't gonna marry no orphaned working girl running with a bunch of hucksters, neither."),
         "src": two("Pestilence (RDR1, Act III), to John, about Jack; John answers that if Jack meets one like her, he hopes he will marry her",
                    "Pestilence (RDR1, acte III), à John, à propos de Jack ; John répond que s'il en rencontre une comme elle, il espère bien qu'il l'épousera. Traduction : « Et il n'épousera pas non plus une orpheline de petite vertu qui traîne avec une bande d'escrocs. »")},
        {"q": two("Stop. For an illiterate gunslinger, you sure know how to make a girl blush.", "Stop. For an illiterate gunslinger, you sure know how to make a girl blush."),
         "src": two("Pestilence (RDR1, Act III), to John, in reply to that compliment",
                    "Pestilence (RDR1, acte III), à John, en réponse à ce compliment. Traduction : « Arrête. Pour un pistolero illettré, tu sais drôlement faire rougir une fille. »")},
        {"q": two("Of Bill? You gotta be kidding me. He was only frightening if you was afraid of dumb fools.", "Of Bill? You gotta be kidding me. He was only frightening if you was afraid of dumb fools."),
         "src": two("Old Friends, New Problems (RDR1, Act III), to John, who says people in New Austin were scared of Bill",
                    "Old Friends, New Problems (RDR1, acte III), à John, qui raconte que les gens de New Austin avaient peur de Bill. Traduction : « De Bill ? Tu te moques de moi. Il ne faisait peur qu'à ceux qui ont peur des imbéciles. »")},
        {"q": two("A family that left you for dead. You knew the truth, John, and they hated you for it.", "A family that left you for dead. You knew the truth, John, and they hated you for it."),
         "src": two("Old Friends, New Problems (RDR1, Act III), to John, who says the gang was still a kind of family",
                    "Old Friends, New Problems (RDR1, acte III), à John, qui dit que le gang restait une sorte de famille. Traduction : « Une famille qui t'a laissé pour mort. Tu voyais clair, John, et ils te l'ont fait payer. »")},
        {"q": two("It ain't the first time I had a gun to my head, John. You're forgettin' your marriage proposal.", "It ain't the first time I had a gun to my head, John. You're forgettin' your marriage proposal."),
         "src": two("Old Friends, New Problems (RDR1, Act III), to John, who asks whether the government men treated her right; he answers \"Very funny.\"",
                    "Old Friends, New Problems (RDR1, acte III), à John, qui lui demande si les hommes du gouvernement l'ont bien traitée ; il répond \"Very funny\" (très drôle). Traduction : « Ce n'est pas la première fois qu'on me braque un pistolet sur la tempe, John. Tu oublies ta demande en mariage. »")},
        {"q": two("I don't know, John. How many times can we start again? An outlaw and a workin' girl. We ain't exactly farmers.", "I don't know, John. How many times can we start again? An outlaw and a workin' girl. We ain't exactly farmers."),
         "src": two("Old Friends, New Problems (RDR1, Act III), to John, who says they will have a ranch like the MacFarlanes' someday",
                    "Old Friends, New Problems (RDR1, acte III), à John, qui promet qu'ils auront un jour un ranch comme celui des MacFarlane. Traduction : « Je ne sais pas, John. Combien de fois peut-on tout recommencer ? Un hors-la-loi et une fille de joie. On n'a rien de fermiers. »")},
        {"q": two("You stay out of trouble, John.", "You stay out of trouble, John."),
         "src": two("The Last Enemy That Shall Be Destroyed (RDR1, Act III), to John, in the barn; he answers \"Ain't no trouble, Abigail. Ain't no trouble. I love you.\"",
                    "The Last Enemy That Shall Be Destroyed (RDR1, acte III), à John, dans la grange ; il répond \"Ain't no trouble, Abigail. Ain't no trouble. I love you.\" (pas d'ennuis, Abigail, pas d'ennuis. Je t'aime). Traduction : « Ne va pas t'attirer d'ennuis, John. »")},
        {"q": two("Did you hear that? Jack, we have to go back for Pa!", "Did you hear that? Jack, we have to go back for Pa!"),
         "src": two("The Last Enemy That Shall Be Destroyed (RDR1, Act III), to Jack, as they ride away from the ranch",
                    "The Last Enemy That Shall Be Destroyed (RDR1, acte III), à Jack, alors qu'ils s'éloignent du ranch à cheval. Traduction : « Tu as entendu ? Jack, il faut retourner chercher papa ! »")},
    ]},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"p": two("The wiki's quote list gives 14 lines for her multiplayer model, reproduced here as listed. One of them, \"You've clearly had one too many blows to the head.\", is close to a line she says to John in \"Old Friends, New Problems\": \"You clearly had one too many blows to the head.\"",
              "La liste de citations du wiki donne 14 répliques pour son modèle multijoueur, reproduites ici telles qu'elles y figurent. L'une d'elles, \"You've clearly had one too many blows to the head.\", est proche d'une phrase qu'elle adresse à John dans \"Old Friends, New Problems\" : \"You clearly had one too many blows to the head.\"")},
    {"quotes": [
        {"q": two("I see you ain't learn no manners.", "I see you ain't learn no manners."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Je vois que tu n'as toujours pas appris les bonnes manières. »")},
        {"q": two("I've had enough of this.", "I've had enough of this."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « J'en ai assez. »")},
        {"q": two("Call yourself a man.", "Call yourself a man."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Et tu te dis un homme. »")},
        {"q": two("What's the matter with you?!", "What's the matter with you?!"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Mais qu'est-ce qui te prend ?! »")},
        {"q": two("You really are a strange man.", "You really are a strange man."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Tu es vraiment un drôle de type. »")},
        {"q": two("You've clearly had one too many blows to the head.", "You've clearly had one too many blows to the head."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Tu as dû prendre un coup de trop sur la tête. »")},
        {"q": two("You damn fool.", "You damn fool."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Espèce d'idiot. »")},
        {"q": two("Oh, ain't you quite the gentlemen all the sudden.", "Oh, ain't you quite the gentlemen all the sudden."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki, spelling as listed)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki, orthographe d'origine). Traduction : « Oh, quel gentleman, tout à coup. »")},
        {"q": two("You think I'm afraid of you.", "You think I'm afraid of you."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Tu crois que j'ai peur de toi. »")},
        {"q": two("I'll kill you mah self!", "I'll kill you mah self!"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Je vais te tuer moi-même ! »")},
        {"q": two("Oh, like hittin women do you?!", "Oh, like hittin women do you?!"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Ah, on aime frapper les femmes, hein ?! »")},
        {"q": two("Are you completely insane?!", "Are you completely insane?!"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Tu as complètement perdu la tête ?! »")},
        {"q": two("You idiot!", "You idiot!"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Imbécile ! »")},
        {"q": two("Clumsy oaf.", "Clumsy oaf."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Gros balourd. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Across the series", "Dans toute la série")},
    {"ul": [
        two("John and Abigail have the same first names as John Adams, second President of the United States, and his wife Abigail Adams.",
            "John et Abigail portent les mêmes prénoms que John Adams, deuxième président des États-Unis, et son épouse Abigail Adams."),
        two("The couple also shares its first names with John Proctor and Abigail Williams, who have a secret affair in Arthur Miller's play The Crucible.",
            "Le couple partage aussi ses prénoms avec John Proctor et Abigail Williams, liés par une liaison secrète dans la pièce d'Arthur Miller Les Sorcières de Salem (The Crucible)."),
        two("The first name Abigail comes from Hebrew; the French Red Dead Wiki glosses it as \"my father rejoices\".",
            "Le prénom Abigail vient de l'hébreu ; le Red Dead Wiki français le traduit par \"mon père se réjouit\"."),
        two("In \"Old Friends, New Problems\" (1911), John tells her that in his darkest hours the thought of her rat meat stews kept him going. In the 1907 epilogue, John says he misses Pearson's cooking.",
            "Dans \"Old Friends, New Problems\" (1911), John lui assure qu'aux pires heures, l'idée de ses ragoûts de rat l'a fait tenir. Dans l'épilogue de 1907, John dit regretter la cuisine de Pearson."),
    ]},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"ul": [
        two("In chapter 2, once \"A Fisher of Men\" is done, Jack can ask Arthur for a thimble to replace one of his mother's that he lost.",
            "Au chapitre 2, une fois \"A Fisher of Men\" terminée, Jack peut demander à Arthur un dé à coudre pour remplacer celui de sa mère, qu'il a perdu."),
        two("Her reply to a greeting changes with the period: to Arthur in 1899 she says she is not doing well, to John in the epilogue that she is.",
            "Sa réponse quand on la salue change avec l'époque : en 1899, elle dit à Arthur que ça ne va pas ; pendant l'épilogue, elle dit à John que ça va."),
        two("Before \"American Venom\", Jack can be heard reading a story to Abigail and Uncle; the book is a Frank Heck dime novel.",
            "Avant \"American Venom\", on peut entendre Jack lire une histoire à Abigail et à Uncle ; le livre est un roman à quatre sous de Frank Heck."),
        two("After the credits, the player can ask for dinner at the Beecher's Hope house between 4 p.m. and 8 p.m.",
            "Après le générique, le joueur peut demander à dîner dans la maison de Beecher's Hope entre 16 h et 20 h."),
        two("John and Abigail talk after the credits on the hill where, according to the wiki's page on \"American Venom\", their wedding takes place during the credits. In Red Dead Redemption, the graves of John, Abigail and Uncle stand on the same hill.",
            "John et Abigail discutent après le générique sur la colline où, selon la page du wiki consacrée à \"American Venom\", se déroule leur mariage pendant le générique. Dans Red Dead Redemption, les tombes de John, d'Abigail et d'Uncle se trouvent sur cette même colline."),
    ]},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("Neither Abigail nor John wears a wedding ring. The French Red Dead Wiki notes that the same goes for every married character in the game.",
            "Ni Abigail ni John ne portent d'alliance. Le Red Dead Wiki français relève qu'il en va de même pour tous les personnages mariés du jeu."),
        two("Killing her in a mission fails it and sends the player back to the last checkpoint. With the invincibility cheat active, killing her, Jack or Uncle triggers a brief earthquake, and the player's next death shows \"You have killed a member of your family\" instead of the normal screen.",
            "La tuer pendant une mission la fait échouer et renvoie le joueur au dernier point de contrôle. Avec le code d'invincibilité actif, tuer Abigail, Jack ou Uncle déclenche un bref tremblement de terre, et la mort suivante du joueur affiche \"You have killed a member of your family\" (vous avez tué un membre de votre famille) à la place de l'écran habituel."),
        two("Before \"The Last Enemy That Shall Be Destroyed\", two marks on the hill at Beecher's Hope show where John's and Abigail's graves will later appear.",
            "Avant \"The Last Enemy That Shall Be Destroyed\", deux marques sur la colline de Beecher's Hope indiquent l'emplacement des futures tombes de John et d'Abigail."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors continuité)")},
    {"ul": [
        two("After the first mission of Undead Nightmare, the player can kill the hogtied Abigail and Jack, but doing so kills the player too.",
            "Après la première mission d'Undead Nightmare, le joueur peut tuer Abigail et Jack, ligotés, mais il meurt lui aussi."),
        two("After the expansion is completed, two black outlines mark the places where Uncle's and Abigail's graves should be, next to John's.",
            "Une fois l'extension terminée, deux contours noirs marquent l'emplacement où devraient se trouver les tombes d'Uncle et d'Abigail, à côté de celle de John."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Abigail became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, released on September 21, 2010. The pack added 15 characters from the story, as well as Poker, Liar's Dice, horse races and the Stronghold mode. Players select Abigail in the Redemption section of the Outfitter, alongside [[john-marston|John]], [[jack-marston|Jack]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[leigh-johnson|Leigh Johnson]], [[luisa-fortuna|Luisa Fortuna]], [[nigel-west-dickens|Nigel West Dickens]] and [[seth-briars|Seth Briars]].",
              "Abigail devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, sorti le 21 septembre 2010. Ce pack ajoute 15 personnages de l'histoire, ainsi que le poker, le poker menteur, des courses de chevaux et le mode Stronghold. On choisit Abigail dans la section Redemption de l'Outfitter, aux côtés de [[john-marston|John]], [[jack-marston|Jack]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[leigh-johnson|Leigh Johnson]], [[luisa-fortuna|Luisa Fortuna]], [[nigel-west-dickens|Nigel West Dickens]] et [[seth-briars|Seth Briars]].")},
    {"p": two("For multiplayer, her model swaps the story's blue-violet top and long pink plaid skirt for blue trousers and a white and blue plaid top, which suit riding. Luisa Fortuna's model is changed in the same way. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the Abigail model is not available in them.",
              "En multijoueur, son modèle troque le haut bleu-violet et la longue jupe à carreaux roses de l'histoire contre un pantalon bleu et un haut à carreaux blancs et bleus, plus commodes pour monter à cheval. Le modèle de Luisa Fortuna est modifié de la même façon. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle d'Abigail n'y est donc pas disponible.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Abigail as an undead for Undead Nightmare. The printed Undead Nightmare map carries, on its back, artwork of her undead in her ranch clothes; in the expansion itself she is undead only in her nightdress.",
              "Rockstar a diffusé une illustration officielle d'Abigail en morte-vivante pour Undead Nightmare. Le verso de la carte imprimée d'Undead Nightmare la montre elle aussi en morte-vivante, mais dans ses vêtements de fermière ; dans l'extension, elle n'est morte-vivante qu'en chemise de nuit.")},
    {"p": two("For Red Dead Redemption 2, Rockstar released new official artwork of her. On September 6, 2018, Rockstar posted the portraits and character descriptions of the gang's members on Twitter, and The Hollywood Reporter reproduced the series the next day. In the composite image of the 23 gang members, she stands in the front row, next to Jack.",
              "Pour Red Dead Redemption 2, Rockstar a publié une nouvelle illustration officielle du personnage. Le 6 septembre 2018, Rockstar publie sur Twitter les portraits et les descriptions des membres du gang, et The Hollywood Reporter reprend la série le lendemain. Sur l'image qui réunit les 23 membres du gang, elle figure au premier rang, à côté de Jack.")},
]
