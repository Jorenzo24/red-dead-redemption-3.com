"""Simon Pearson, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/simon/ and cov/simon/m/):
- Red Dead Wiki EN "Simon Pearson" (Mission Appearances, Companion Activities, Quotes, Trivia, Gallery captions) and
  FR "Simon Pearson" (fr.txt: Apparitions dans les missions, same thirteen missions as the EN list minus the credits).
- Mission pages: Outlaws from the West; The Aftermath of Genesis; Old Friends; Eastward Bound; A Strange Kindness;
  Further Questions of Female Suffrage; Blessed are the Peacemakers; The Battle of Shady Belle; Horsemen, Apocalypses;
  Banking, The Old American Art (trivia); Fleeting Joy; That's Murfree Country; Visiting Hours; Money Lending and Other
  Sins VI & VII (trivia); My Last Boy (trivia); Our Best Selves (story and trivia); Revenge is a Dish Best Eaten
  (trivia); Ending Credits; companion activity "Hunting (Simon Pearson)" (rewards, trivia, category Missable Content);
  wiki pages "Errand Boy" (rabbit and naval compass requests), "Dominoes" (chapter 4 partners), "Cain" (trivia),
  "Rhodes General Store" (trivia), "Ethel Pearson".
- Transcripts "/dialogues": Outlaws from the West, The Aftermath of Genesis, Old Friends, Eastward Bound, Who is Not
  Without Sin, Blessed are the Peacemakers, The Battle of Shady Belle (.dlg). Every mission line below is checked word
  for word against one of them. No transcript exists on the wiki for Further Questions of Female Suffrage, Fleeting
  Joy, A Strange Kindness, Visiting Hours, My Last Boy, Our Best Selves, the Hunting activity or the 1907 store
  conversations (checked Oct 2026): the two lines from the swamp and from 1907 come from the quote list of the
  character page, and are labeled as such.
- Real world: Rockstar's series of character portraits and descriptions posted on Twitter on September 6, 2018 and
  reproduced by The Hollywood Reporter on September 7, 2018 (../abigail/fc/thr_descriptions.txt: entry "Pearson";
  the description itself is NOT quoted here, part B); Wikipedia "List of Red Dead Redemption 2 characters"
  (m/wp_list.txt: composite of the 23 gang members, front row "Pearson, Uncle, Swanson"; section "Mr. Pearson").
Ownership (FIX_RULES), left to other parts: backstory, mission narrative, the 1907 store and Ethel (A); personality,
official descriptions, names and the Tacitus Kilgore alias, appearance (anchor tattoo, the winter coat in 1907, the
day-one patch hair model), the crafting upgrades and the satchels sold by fences in the epilogue (skills), camp scenes
and camp lines ("Nothing like good honest labour", the self-pity speech to Susan, "the only thing I cannot cook is
air", Hosea and the jokes, Sean and the songs), relationships (B); Jim Santangeli and the reception (D).
Quotes: each line in ONE place; part A paraphrases them without quotation marks. Camp lines are left to part B.
"Like a cornered tiger" is quoted here inside the full mission line; part B should paraphrase it if it uses it.
Kills: none. No page credits Pearson with a killing; the Red Dead Wiki has no "Murders committed" section for him,
so no kills table is given.
Excluded: the wiki trivia that he "seems to get along very well with Hosea" (relationship, part B); the satchels at
fences and the winter coat (part B); the reading of the gang photograph through Bessie Matthews's absence
(speculation); the FR wiki's claim that he leaves "sans prévenir personne" (unsourced); the wiki's "plague" ship
(unsourced wording); Tilly as the person told of the departure (unsupported).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
E2 = two("Epilogue II", "Épilogue II")
C234 = two("2, 3 and 4", "2, 3 et 4")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists thirteen story missions of Red Dead Redemption 2 for Pearson, plus the end credits and one companion activity. The French Red Dead Wiki gives the same thirteen missions. The table below also includes the missions in which he only speaks a line, is talked about, or in which his absence is noted.",
              "Le Red Dead Wiki anglais recense pour Pearson treize missions principales de Red Dead Redemption 2, plus le générique de fin et une activité de compagnon. Le Red Dead Wiki français donne les mêmes treize missions. Le tableau ci-dessous intègre aussi les missions où il ne prononce qu'une réplique, n'est qu'évoqué, ou dont la page signale son absence.")},
    {"h4": two("Red Dead Redemption 2, story missions", "Red Dead Redemption 2, missions principales")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Pearson's role", "Rôle de Pearson")], "rows": [
        M("Outlaws from the West", C1,
          "Sent by [[susan-grimshaw|Susan]] to check the food supplies at Colter; [[dutch-van-der-linde|Dutch]] then asks him and Susan to turn the place into a camp.",
          "Envoyé par [[susan-grimshaw|Susan]] faire l'inventaire des vivres à Colter ; [[dutch-van-der-linde|Dutch]] lui demande ensuite, avec Susan, de transformer l'endroit en camp."),
        M("The Aftermath of Genesis", C1,
          "Mission start. Tells [[arthur-morgan|Arthur]] the camp is out of food, gives him a can of salted offal, then shares his rum and has Arthur skin a deer.",
          "Point de départ de la mission. Annonce à [[arthur-morgan|Arthur]] que le camp n'a plus de vivres, lui donne une boîte d'abats salés, puis partage son rhum et lui fait dépecer un cerf."),
        M("Old Friends", C1,
          "Left at Colter with [[hosea-matthews|Hosea]] and [[charles-smith|Charles]] to guard the camp while the others raid the O'Driscolls.",
          "Laissé à Colter avec [[hosea-matthews|Hosea]] et [[charles-smith|Charles]] pour garder le camp pendant que les autres attaquent les O'Driscoll."),
        M("Eastward Bound", C1,
          "Loads supplies, rides in the lead wagon with Dutch to Horseshoe Overlook and asks for fresh food every day.",
          "Charge les provisions, voyage dans le chariot de tête avec Dutch jusqu'à Horseshoe Overlook et réclame de la nourriture fraîche chaque jour."),
        M("Who is Not Without Sin", C2,
          "At camp. Comments as Arthur carries a drunk [[orville-swanson|Reverend Swanson]] to his tent. Not in the wiki's list.",
          "Au camp. Lâche un commentaire quand Arthur ramène sous sa tente le [[orville-swanson|révérend Swanson]], ivre. Absente de la liste du wiki."),
        M("A Strange Kindness", C2,
          "Listed by both wikis; the mission page does not describe his role. The gang packs up the Horseshoe Overlook camp.",
          "Citée par les deux wikis ; la page de la mission ne décrit pas son rôle. La bande lève le camp de Horseshoe Overlook."),
        M("Further Questions of Female Suffrage", C3,
          "Argues with [[sadie-adler|Sadie]] in the kitchen, gives Arthur a letter for his aunt Cathy, then unloads the supplies with them.",
          "Se dispute avec [[sadie-adler|Sadie]] en cuisine, confie à Arthur une lettre pour sa tante Cathy, puis décharge les provisions avec eux."),
        M("Blessed are the Peacemakers", C3,
          "Reports the O'Driscolls' offer of a parley; Dutch refuses to take him along. Apologizes to the wounded Arthur and helps carry him to his tent.",
          "Rapporte l'offre de pourparlers des O'Driscoll ; Dutch refuse de l'emmener. Présente ses excuses à Arthur, blessé, et aide à le porter jusqu'à sa tente."),
        M("The Battle of Shady Belle", C3,
          "Arrives with the caravan; Dutch asks him and Susan to set up the Shady Belle camp.",
          "Arrive avec le convoi ; Dutch lui demande, avec Susan, d'installer le camp de Shady Belle."),
        M("Horsemen, Apocalypses", C4,
          "After the O'Driscoll attack, buries [[kieran-duffy|Kieran]] with Charles and Swanson on Dutch's orders.",
          "Après l'attaque des O'Driscoll, enterre [[kieran-duffy|Kieran]] avec Charles et Swanson sur ordre de Dutch."),
        M("Banking, The Old American Art", C4,
          "Absent. The mission page lists him among the gang members who do not take part in the bank robbery.",
          "Absent. La page de la mission le range parmi les membres de la bande qui ne participent pas au braquage de la banque."),
        M("Fleeting Joy", C5,
          "At Lakay. Welcomes Arthur back, according to the character page, before the Pinkerton attack.",
          "À Lakay. Accueille Arthur à son retour, d'après la page du personnage, avant l'attaque de la Pinkerton."),
        M("That's Murfree Country", C5,
          "After Susan shoots [[molly-oshea|Molly]] at Beaver Hollow, ordered with [[bill-williamson|Bill]] to burn the body.",
          "Après que Susan a abattu [[molly-oshea|Molly]] à Beaver Hollow, reçoit l'ordre de brûler le corps avec [[bill-williamson|Bill]]."),
        M("Visiting Hours", C6,
          "Listed by both wikis; the mission page does not describe his role.",
          "Citée par les deux wikis ; la page de la mission ne décrit pas son rôle."),
        M("Money Lending and Other Sins VI & VII", C6,
          "Woken up if Arthur throws [[leopold-strauss|Strauss]] out at night; later asks where Strauss has gone. Not in the wiki's list.",
          "Réveillé si Arthur chasse [[leopold-strauss|Strauss]] de nuit ; demande ensuite où Strauss est passé. Absente de la liste du wiki."),
        M("My Last Boy", C6,
          "Last mission with Pearson at camp; he is gone once it is completed.",
          "Dernière mission où Pearson se trouve au camp ; il est parti une fois qu'elle est terminée."),
        M("Our Best Selves", C6,
          "Mentioned. Dutch tells Arthur that Pearson, Uncle and Mary-Beth have run off and calls them cowards. Not in the wiki's list.",
          "Mentionné. Dutch annonce à Arthur que Pearson, Uncle et Mary-Beth ont pris la fuite et les traite de lâches. Absente de la liste du wiki."),
        M("Ending Credits", E2,
          "Seen running the general store in Rhodes and looking at a photograph of the gang.",
          "Montré à la tête du magasin général de Rhodes, les yeux sur une photographie de la bande."),
    ]}},
    {"h4": two("Red Dead Redemption 2: companion activity, requests and camp games", "Red Dead Redemption 2 : activité de compagnon, commandes et jeux au camp")},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Pearson's role", "Rôle de Pearson")], "rows": [
        M("Hunting (Simon Pearson)", C4,
          "Activity giver: crayfish, then alligator eggs, in the swamp east of Shady Belle (see Biography). Available after \"Angelo Bronte, A Man of Honor\". Rewards: three crayfish and up to ten alligator eggs.",
          "Donneur de l'activité : écrevisses, puis œufs d'alligator, dans le marais à l'est de Shady Belle (voir la biographie). Disponible après \"Angelo Bronte, A Man of Honor\". Récompenses : trois écrevisses et jusqu'à dix œufs d'alligator."),
        M(two("Item request: a rabbit", "Commande : un lapin"), C2,
          "He asks Arthur for a rabbit. According to the Red Dead Wiki's page on the Errand Boy trophy, the request is rare and mostly appears in chapter 2; it rewards a unique blue denim scouting jacket and counts toward the trophy.",
          "Il demande un lapin à Arthur. D'après la page du Red Dead Wiki consacrée au trophée Errand Boy, la commande est rare et apparaît surtout au chapitre 2 ; elle rapporte une veste d'éclaireur unique en denim bleu et compte pour le trophée."),
        M(two("Item request: a naval compass", "Commande : un compas de marine"), C234,
          "According to the Errand Boy page, he asks for it only during a poker game with him. A naval compass can be found in the boathouse of Braithwaite Manor, or in the lockbox of Ashton's stagecoach during \"Fatherhood and Other Dreams\". It also counts toward the trophy.",
          "D'après la page Errand Boy, il ne le réclame que pendant une partie de poker avec lui. On trouve un compas de marine dans le hangar à bateaux du manoir Braithwaite, ou dans le coffre de la diligence d'Ashton pendant \"Fatherhood and Other Dreams\". La commande compte aussi pour le trophée."),
        M(two("Dominoes", "Dominos"), C4,
          "One of the gang members Arthur can play dominoes with at Shady Belle, along with Hosea, Abigail and Mary-Beth.",
          "L'un des membres de la bande avec qui Arthur peut jouer aux dominos à Shady Belle, avec Hosea, Abigail et Mary-Beth."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent.")},
    {"h4": two("Colter and the road east", "Colter et la route vers l'est")},
    {"quotes": [
        {"q": two("We have a few cans of food and a rabbit... for what, ten, twelve people?", "We have a few cans of food and a rabbit... for what, ten, twelve people?"),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), to Arthur, in the shed where he cooks",
                    "The Aftermath of Genesis (RDR2, chapitre 1), à Arthur, dans la remise où il cuisine. Traduction : « On a quelques conserves et un lapin... pour quoi, dix, douze personnes ? »")},
        {"q": two("We were stranded at sea... for fifty days.", "We were stranded at sea... for fifty days."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), to Arthur, who has just said he does not wish to hear about the Navy. Arthur answers: \"And you unfortunately survived...\"",
                    "The Aftermath of Genesis (RDR2, chapitre 1), à Arthur, qui vient de dire qu'il ne veut rien entendre sur la marine. Arthur répond : \"And you unfortunately survived...\" Traduction : « On est restés bloqués en mer... pendant cinquante jours. » (« Et tu as malheureusement survécu... »)")},
        {"q": two("You're gonna need something to eat out there.", "You're gonna need something to eat out there."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), throwing Arthur a can of assorted salted offal. Arthur reads the label and says: \"Starving would be preferable.\"",
                    "The Aftermath of Genesis (RDR2, chapitre 1), en lançant à Arthur une boîte d'abats salés assortis. Arthur lit l'étiquette et lâche : \"Starving would be preferable.\" Traduction : « Il va vous falloir quelque chose à manger, là-bas. » (« Je préférerais mourir de faim. »)")},
        {"q": two("Navy rum, sir... it's the only thing... the only thing. Keeps you sane, it does.", "Navy rum, sir... it's the only thing... the only thing. Keeps you sane, it does."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), after Arthur, handed the bottle, asks what it is",
                    "The Aftermath of Genesis (RDR2, chapitre 1), après qu'Arthur, la bouteille à la main, a demandé ce que c'était. Traduction : « Du rhum de la marine, monsieur... il n'y a que ça... que ça. Ça garde la tête sur les épaules, ça. »")},
        {"q": two("Not too bad, Mr. Morgan. Yeah, they always said you were a butcher.", "Not too bad, Mr. Morgan. Yeah, they always said you were a butcher."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), watching Arthur skin the deer",
                    "The Aftermath of Genesis (RDR2, chapitre 1), en regardant Arthur dépecer le cerf. Traduction : « Pas mal du tout, monsieur Morgan. Eh oui, on a toujours dit que vous étiez un boucher. »")},
        {"q": two("Heck, Arthur Morgan's first decent bit of hunting, after all these years.", "Heck, Arthur Morgan's first decent bit of hunting, after all these years."),
         "src": two("The Aftermath of Genesis (RDR2, chapter 1), as Arthur hangs the deer skin on a rack",
                    "The Aftermath of Genesis (RDR2, chapitre 1), pendant qu'Arthur accroche la peau du cerf à un séchoir. Traduction : « Ça alors, la première chasse digne de ce nom d'Arthur Morgan, après toutes ces années. »")},
        {"q": two("And... we need food... real food... that means every day, one of you.", "And... we need food... real food... that means every day, one of you."),
         "src": two("Eastward Bound (RDR2, chapter 1), speaking up from the crowd after Dutch tells the gang to earn their keep at Horseshoe Overlook",
                    "Eastward Bound (RDR2, chapitre 1), depuis le groupe, après que Dutch a demandé à chacun de gagner sa croûte à Horseshoe Overlook. Traduction : « Et... il nous faut à manger... de la vraie nourriture... ça veut dire tous les jours, l'un d'entre vous. »")},
        {"q": two("Somebody had a good time.", "Somebody had a good time."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), as Arthur carries a drunk Reverend Swanson through camp",
                    "Who is Not Without Sin (RDR2, chapitre 2), quand Arthur traverse le camp en portant le révérend Swanson, ivre. Traduction : « Y en a un qui s'est bien amusé. »")},
    ]},
    {"h4": two("The parley", "Les pourparlers")},
    {"quotes": [
        {"q": two("It's peace, Dutch... the O'Driscolls... I mean, I think there's a way.", "It's peace, Dutch... the O'Driscolls... I mean, I think there's a way."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), to Dutch, after Micah tells him to speak up",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), à Dutch, après que Micah lui a dit de parler. Traduction : « C'est la paix, Dutch... les O'Driscoll... enfin, je crois qu'il y a moyen. »")},
        {"q": two("I met a couple of the O'Driscoll boys on the road into town... things were about to get ugly... but you know how I am in a fight, huh? Like a cornered tiger. Anyway... somehow it didn't, but... we got to talking... and they suggested a parley... to end things... like gentlemen.", "I met a couple of the O'Driscoll boys on the road into town... things were about to get ugly... but you know how I am in a fight, huh? Like a cornered tiger. Anyway... somehow it didn't, but... we got to talking... and they suggested a parley... to end things... like gentlemen."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), to Dutch, Arthur and Micah. Dutch answers: \"Gentlemen? Colm O'Driscoll? Have you lost your minds?\"",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), à Dutch, Arthur et Micah. Dutch répond : \"Gentlemen? Colm O'Driscoll? Have you lost your minds?\" Traduction : « J'ai croisé deux gars des O'Driscoll sur la route de la ville... ça allait mal tourner... mais vous savez comment je suis dans une bagarre, hein ? Comme un tigre acculé. Bref... allez savoir pourquoi, ça n'a pas dégénéré, mais... on s'est mis à discuter... et ils ont proposé des pourparlers... pour en finir... entre gentlemen. » (« Des gentlemen ? Colm O'Driscoll ? Vous avez perdu la tête ? »)")},
        {"q": two("What about me?", "What about me?"),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), when Dutch decides to go with Micah and Arthur only. Dutch replies: \"This ain't the time for tigers, my friend.\"",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), quand Dutch décide de n'emmener que Micah et Arthur. Dutch lui répond : \"This ain't the time for tigers, my friend.\" Traduction : « Et moi ? » (« Ce n'est pas le moment des tigres, mon ami. »)")},
        {"q": two("I'm sorry, Arthur.", "I'm sorry, Arthur."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), as the wounded Arthur collapses back at Clemens Point. Dutch cuts in: \"It's a bit late for apologies...\"",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), quand Arthur, blessé, s'effondre de retour à Clemens Point. Dutch l'interrompt : \"It's a bit late for apologies...\" Traduction : « Je suis désolé, Arthur. » (« C'est un peu tard pour les excuses... »)")},
    ]},
    {"h4": two("Said to him and about him", "Ce qu'on lui dit, ce qu'on dit de lui")},
    {"quotes": [
        {"q": two("Mr. Pearson... Miss Grimshaw... I need you to turn this place into a camp. We may be here for a few days.", "Mr. Pearson... Miss Grimshaw... I need you to turn this place into a camp. We may be here for a few days."),
         "src": two("Dutch van der Linde, Outlaws from the West (RDR2, chapter 1), in the Colter cabin",
                    "Dutch van der Linde, Outlaws from the West (RDR2, chapitre 1), dans la cabane de Colter. Traduction : « Monsieur Pearson... Miss Grimshaw... j'ai besoin que vous transformiez cet endroit en camp. Nous risquons de rester ici quelques jours. »")},
        {"q": two("You noticed how Pearson's had a bottle in his hand ever since we fled Blackwater? We give the camp cook five minutes to grab the essentials and go, and he doesn't even bring a crumb of food.", "You noticed how Pearson's had a bottle in his hand ever since we fled Blackwater? We give the camp cook five minutes to grab the essentials and go, and he doesn't even bring a crumb of food."),
         "src": two("Arthur Morgan to Charles Smith, The Aftermath of Genesis (RDR2, chapter 1), on the ride back from the hunt",
                    "Arthur Morgan à Charles Smith, The Aftermath of Genesis (RDR2, chapitre 1), sur le chemin du retour de la chasse. Traduction : « T'as remarqué que Pearson a une bouteille à la main depuis qu'on a fui Blackwater ? On laisse cinq minutes au cuisinier du camp pour prendre l'essentiel et filer, et il n'emporte même pas une miette de nourriture. »")},
        {"q": two("I love it! Miss Grimshaw, Mr. Pearson, would you two kindly work your magic?", "I love it! Miss Grimshaw, Mr. Pearson, would you two kindly work your magic?"),
         "src": two("Dutch van der Linde, The Battle of Shady Belle (RDR2, chapter 3), on arriving at Shady Belle",
                    "Dutch van der Linde, The Battle of Shady Belle (RDR2, chapitre 3), en arrivant à Shady Belle. Traduction : « J'adore ! Miss Grimshaw, monsieur Pearson, auriez-vous l'amabilité d'opérer votre magie ? »")},
    ]},
    {"h4": two("From the quote list of the Red Dead Wiki", "D'après la liste de citations du Red Dead Wiki")},
    {"quotes": [
        {"q": two("You see that swamp, Arthur? That's God's own pantry.", "You see that swamp, Arthur? That's God's own pantry."),
         "src": two("To Arthur, about the swamp around Shady Belle (RDR2, chapter 4; quote list of the character page)",
                    "À Arthur, à propos du marais qui entoure Shady Belle (RDR2, chapitre 4 ; liste de citations de la page du personnage). Traduction : « Vous voyez ce marais, Arthur ? C'est le garde-manger du Bon Dieu. »")},
        {"q": two("You know, sometimes people here still talk about the brutal demise of the Grays and the Braithwaites. I just smile and keep quiet.", "You know, sometimes people here still talk about the brutal demise of the Grays and the Braithwaites. I just smile and keep quiet."),
         "src": two("To John Marston in his store in Rhodes (RDR2, 1907 epilogue; quote list of the character page)",
                    "À John Marston, dans son magasin de Rhodes (RDR2, épilogue de 1907 ; liste de citations de la page du personnage). Traduction : « Vous savez, les gens d'ici parlent encore parfois de la fin brutale des Gray et des Braithwaite. Moi, je souris et je me tais. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("Dutch uses the insult \"repulsive little maggot\" on [[angelo-bronte|Angelo Bronte]] as he drowns him in \"Revenge is a Dish Best Eaten\". The mission page notes that Pearson says the same words to Uncle (see Relationships).",
            "Dutch traite [[angelo-bronte|Angelo Bronte]] de \"repulsive little maggot\" (sale petit asticot répugnant) en le noyant, dans \"Revenge is a Dish Best Eaten\". La page de la mission relève que Pearson adresse les mêmes mots à Uncle (voir Relations)."),
        two("During the crayfish activity, Arthur can shoot the alligators instead of waiting for Pearson to draw them away. Pearson is then angry and waits for him at the boat, but the activity carries on as planned.",
            "Pendant la sortie aux écrevisses, Arthur peut abattre les alligators au lieu d'attendre que Pearson les éloigne. Pearson, fâché, l'attend alors à la barque, mais l'activité se poursuit normalement."),
        two("Up to eleven alligator eggs can be collected during the activity; one is automatically handed to Pearson at the end, which leaves Arthur ten at most. If Arthur has already done the \"Duchesses and Other Animals\" errand for Algernon Wasp, which also involves alligator eggs, he mentions that earlier errand, according to the activity page.",
            "Jusqu'à onze œufs d'alligator peuvent être ramassés pendant l'activité ; l'un d'eux est automatiquement remis à Pearson à la fin, ce qui en laisse dix au plus à Arthur. Si Arthur a déjà accompli pour Algernon Wasp la course \"Duchesses and Other Animals\", qui porte elle aussi sur des œufs d'alligator, il évoque cette course, d'après la page de l'activité."),
        two("The Red Dead Wiki classes the crayfish activity, a chapter 4 activity, as missable content.",
            "Le Red Dead Wiki range la sortie aux écrevisses, une activité du chapitre 4, parmi les contenus manquables."),
        two("The Marstons' dog, Cain, can sometimes be seen sniffing and licking the food on Pearson's table.",
            "Cain, le chien des Marston, vient parfois renifler et lécher la nourriture posée sur la table de Pearson."),
        two("The Rhodes general store is the only general store in the game whose owner changes between 1899 and 1907. According to the wiki's page on the store, A.J. Banks, its owner in 1899, moved east to start other businesses.",
            "Le magasin général de Rhodes est le seul du jeu à changer de propriétaire entre 1899 et 1907. D'après la page du wiki consacrée au magasin, A.J. Banks est parti monter d'autres affaires dans l'Est."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Pearson is one of the gang members presented by Rockstar in the series of character portraits and descriptions posted on Twitter on September 6, 2018 (see Personality), which The Hollywood Reporter reproduced on September 7, 2018. The Red Dead Wiki's gallery also includes a promotional artwork of him. He is in the front row of the composite of 23 gang members' official art designs that illustrates Wikipedia's list of the game's characters, where his section is titled \"Mr. Pearson\".",
              "Pearson fait partie des membres de la bande présentés par Rockstar dans la série de portraits et de descriptions de personnages publiée sur Twitter le 6 septembre 2018 (voir Personnalité) et reprise le 7 septembre 2018 par The Hollywood Reporter. La galerie du Red Dead Wiki comprend aussi une illustration promotionnelle de lui. Il figure au premier rang du montage des illustrations officielles de 23 membres de la bande qui ouvre la liste des personnages du jeu sur Wikipédia, où la section qui lui est consacrée s'intitule \"Mr. Pearson\".")},
]
