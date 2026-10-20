"""Josiah Trelawny, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/josiah/, cov/josiah/m/ and
cov/josiah/x/):
- Red Dead Wiki EN "Josiah Trelawny" (Mission Appearances incl. Red Dead Online, Quotes, Trivia, Events of Red Dead
  Online, Gallery captions) and FR "Josiah Trelawny" (fr.txt: same eight story missions).
- Mission pages: Americans at Rest; The First Shall Be Last; The New South; Magicians for Sport; Friends in Very Low
  Places (rewards, trivia); Blood Feuds, Ancient and Modern (no mention of him); A Fine Night of Debauchery (rewards,
  quote box, trivia); The Fine Art of Conversation (giver, trivia); A Short Walk in a Pretty Town (trivia: Bill's
  message); Of Men and Angels (must be played before "The Fine Art of Conversation"); Horsemen, Apocalypses (trivia:
  absent from the attack); Blackwater Massacre (trivia: Arthur's journal).
- Transcripts "/dialogues": Americans at Rest, The First Shall Be Last, The New South, Exit Pursued by a Bruised Ego.
  Every line from those three missions is checked word for word against them. No transcript exists on the wiki for
  Magicians for Sport, Friends in Very Low Places, A Fine Night of Debauchery or The Fine Art of Conversation (checked
  Oct 2026): lines from those come from the quote list of the character page or the quote box of the mission page,
  and say so.
- Red Dead Online: wiki pages "Trelawny's Caravan" (1898 and 1907), "Horse Theft", "Rescue", "Caravan Escort",
  "On The Hunt", "Destroy Supplies" (start and end locations), "Catherine Braithwaite" (trivia: the horse is delivered
  to Hill Haven Ranch), "Joe" and "Sean MacGuire" (trivia: the four gang members in Red Dead Online).
- Real world: Rockstar's character portraits and descriptions posted on Twitter on September 6, 2018 and reproduced by
  The Hollywood Reporter on September 7, 2018 (cov/javier/fc/thr_descriptions.txt: entry for Trelawny, not quoted here,
  part B owns it); Wikipedia "List of Red Dead Redemption 2 characters" (m/wp_list.txt: caption of the composite of
  23 gang members, Trelawny last in the front row).
Ownership (FIX_RULES), left to other parts: the narrative of each mission, the caravan, the apartment in Saint Denis,
the departure (A); personality, the Rockstar description, names (Giuseppe Muldoon, the Cornish surname), appearance
(outfits, the Strange Man look-alike as a matter of looks, no winter outfit), the cane, the horse Gwydion and the
look-alike sold in Tumbleweed, family, camp scenes and camp lines (Karen, Mary-Beth, Susan, Uncle, the apartment
follow-up, "the office") (B); Stephen Gevedon, development, the cut Micah snake scene, the cut custom revolver, reception
(D). Lines quoted here are paraphrased in part A without quotation marks.
Kills: the character page lists none; no table.
Fact-check pass (20 Oct 2026): the four lines quoted in part B "In his own words" are removed from Quotes; the
wrong trivia "one of the few surviving members, with Swanson, not seen in 1907" is removed (Bill, Karen, Strauss and
Javier are not seen either, and his fate is unknown); the journal line is "heard talk" (X_Strange_Man l.83), with no
Blackwater placement; card trick (part B Skills), lock breaker (part A), Bill's message and Jack's party (part B
relationships) now live in one place each.
Excluded: the Arturo Bullard oyster theory ("Icarus and Friends", fan theory); the "presumably intentional" reading of
his absence from "Fleeting Joy" (interpretation); the "educated assumption" reading of the dime novel line (interpretation,
and the line has no transcript: paraphrased in A); the Italian he is said to speak (video reference only); Arthur's
lines "He'd sell his own sister..." and "lucky and unlucky" are kept, attributed to the wiki's quote list, because the
wiki gives no mission for them.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English and French Red Dead Wikis list the same eight story missions of Red Dead Redemption 2 for Trelawny, three of which he gives to Arthur. The table below also includes the mission in which he is only talked about. The Red Dead Wiki lists no killings by Trelawny.",
              "Les Red Dead Wiki anglais et français recensent les huit mêmes missions principales de Red Dead Redemption 2 pour Trelawny, dont trois qu'il confie lui-même à Arthur. Le tableau ci-dessous intègre aussi la mission où il n'est qu'évoqué. Le Red Dead Wiki ne lui attribue aucune victime.")},
    {"h4": two("Red Dead Redemption 2, story missions", "Red Dead Redemption 2, missions principales")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Trelawny's role", "Rôle de Trelawny")], "rows": [
        M("Americans at Rest", C2,
          "First appearance. He arrives in Valentine with [[dutch-van-der-linde|Dutch]] after the saloon brawl and reports that [[sean-macguire|Sean]] is alive and held by bounty hunters.",
          "Première apparition. Il arrive à Valentine avec [[dutch-van-der-linde|Dutch]] après la bagarre du saloon et annonce que [[sean-macguire|Sean]] est vivant, aux mains de chasseurs de primes."),
        M("Exit Pursued by a Bruised Ego", C2,
          "Mentioned. On the ride out to the lake, [[arthur-morgan|Arthur]] tells [[hosea-matthews|Hosea]] that John \"ain't Trelawny\"; if Sean has not yet been rescued (optional dialogue), he also says the news about Sean comes from Trelawny.",
          "Mentionné. Sur la route du lac, [[arthur-morgan|Arthur]] dit à [[hosea-matthews|Hosea]] que John \"ain't Trelawny\" ; si Sean n'a pas encore été sauvé (dialogue facultatif), il précise aussi que la nouvelle concernant Sean vient de Trelawny."),
        M("The First Shall Be Last", C2,
          "Scout. He learns where Sean is being taken, guides Arthur and [[javier-escuella|Javier]] along the river and distracts two guards by faking a fit, then leaves before the gunfight.",
          "Éclaireur. Il apprend où Sean est emmené, guide Arthur et [[javier-escuella|Javier]] le long de la rivière et détourne l'attention de deux gardes en simulant une crise, puis s'en va avant la fusillade."),
        M("The New South", C3,
          "Prisoner. Found in Sheriff Leigh Gray's prison wagon, accused of a gold mining investment scam, he is released once Arthur has caught Anders Anderson, the leader of the escapees.",
          "Prisonnier. Retrouvé dans le chariot cellulaire du shérif Leigh Gray, accusé d'une escroquerie à l'investissement minier, il est libéré une fois qu'Arthur a capturé Anders Anderson, le meneur des évadés."),
        M("Magicians for Sport", C3,
          "Kidnapped. Held by bounty hunters near Braithwaite Manor, he is freed by Arthur and [[charles-smith|Charles]] and moves into the gang's camp.",
          "Enlevé. Retenu par des chasseurs de primes près du manoir Braithwaite, il est libéré par Arthur et [[charles-smith|Charles]] et s'installe au camp de la bande."),
        M("Friends in Very Low Places", C3,
          "Mission giver. He buys a tip from Alden Carruthers at the Rhodes post office and distracts the opera singer Chester Damsen while Arthur empties the coach's strongbox. Reward for the player: 206.65 dollars and a lock breaker.",
          "Donneur de la mission. Il achète un tuyau à Alden Carruthers, à la poste de Rhodes, et occupe la chanteuse d'opéra Chester Damsen pendant qu'Arthur vide le coffre de la diligence. Récompense pour le joueur : 206,65 dollars et un crochet."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Listed by the character pages of both wikis; the mission page does not mention him.",
          "Citée par les pages du personnage des deux wikis ; la page de la mission ne le mentionne pas."),
        M("A Fine Night of Debauchery", C4,
          "Mission giver. He plans the robbery of the Grand Korrigan, dresses Arthur for the poker game against Desmond Blythe and swims ashore with the others after the gunfight. Reward for the player: 825 dollars and the Reutlinger pocket watch.",
          "Donneur de la mission. Il monte le braquage du Grand Korrigan, habille Arthur pour la partie de poker contre Desmond Blythe et regagne la rive à la nage avec les autres après la fusillade. Récompense pour le joueur : 825 dollars et la montre de poche Reutlinger."),
        M("The Fine Art of Conversation", C6,
          "Departure. Listed with Rains Fall as the mission's giver, he leaves the gang for good at the start of the mission, with Arthur's blessing.",
          "Départ. Indiqué avec Rains Fall comme donneur de la mission, il quitte définitivement la bande au début de celle-ci, avec la bénédiction d'Arthur."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Lines from missions that have no transcript on the Red Dead Wiki are marked as taken from its quote list.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Celles qui viennent de missions sans transcription sur le Red Dead Wiki sont signalées comme tirées de sa liste de citations.")},
    {"h4": two("Return to the gang", "Retour dans la bande")},
    {"quotes": [
        {"q": two("Making new friends again I see, Arthur.", "Making new friends again I see, Arthur."),
         "src": two("Americans at Rest (RDR2, chapter 2), his first line in the game, to Arthur after the fight with Tommy",
                    "Americans at Rest (RDR2, chapitre 2), sa première réplique du jeu, à Arthur après le combat contre Tommy. Traduction : « Toujours à te faire de nouveaux amis, à ce que je vois, Arthur. »")},
        {"q": two("And miss all this glamour? You must be joking.", "And miss all this glamour? You must be joking."),
         "src": two("Americans at Rest (RDR2, chapter 2), to Arthur, who thought he had gone to New York",
                    "Americans at Rest (RDR2, chapitre 2), à Arthur, qui le croyait parti pour New York. Traduction : « Et rater tout ce glamour ? Vous plaisantez. »")},
        {"q": two("I went to Blackwater looking for you gentlemen. You're not very popular there it seems.", "I went to Blackwater looking for you gentlemen. You're not very popular there it seems."),
         "src": two("Americans at Rest (RDR2, chapter 2), to Arthur and Dutch",
                    "Americans at Rest (RDR2, chapitre 2), à Arthur et Dutch. Traduction : « Je suis allé à Blackwater vous chercher, messieurs. On dirait que vous n'y êtes pas très populaires. »")},
        {"q": two("It's you they want, Dutch.", "It's you they want, Dutch."),
         "src": two("Americans at Rest (RDR2, chapter 2), when the gang discusses going into Blackwater for Sean",
                    "Americans at Rest (RDR2, chapitre 2), quand la bande envisage d'aller chercher Sean à Blackwater. Traduction : « C'est vous qu'ils veulent, Dutch. »")},
    ]},
    {"h4": two("The rescue of Sean", "Le sauvetage de Sean")},
    {"quotes": [
        {"q": two("Oh it must be wonderful to have such trust in one's parents. Mine would have sold me for a hogshead of ale... in fact I think they tried.", "Oh it must be wonderful to have such trust in one's parents. Mine would have sold me for a hogshead of ale... in fact I think they tried."),
         "src": two("The First Shall Be Last (RDR2, chapter 2), to Arthur, who has just said that Dutch and Hosea know where the money is",
                    "The First Shall Be Last (RDR2, chapitre 2), à Arthur, qui vient de dire que Dutch et Hosea savent où est l'argent. Traduction : « Oh, ce doit être merveilleux d'avoir une telle confiance en ses parents. Les miens m'auraient vendu pour une barrique de bière... d'ailleurs, je crois qu'ils ont essayé. »")},
        {"q": two("Gentlemen, gentlemen! Excuse me, dear brothers, my wife has taken ill, gravely ill!", "Gentlemen, gentlemen! Excuse me, dear brothers, my wife has taken ill, gravely ill!"),
         "src": two("The First Shall Be Last (RDR2, chapter 2), to the two bounty hunters guarding the river, before faking a fit",
                    "The First Shall Be Last (RDR2, chapitre 2), aux deux chasseurs de primes qui gardent la rivière, avant de simuler une crise. Traduction : « Messieurs, messieurs ! Excusez-moi, chers frères, ma femme est tombée malade, gravement malade ! »")},
        {"q": two("A pleasure as always, gentlemen. I think you have it from here.", "A pleasure as always, gentlemen. I think you have it from here."),
         "src": two("The First Shall Be Last (RDR2, chapter 2), to Arthur and Javier, before riding away",
                    "The First Shall Be Last (RDR2, chapitre 2), à Arthur et Javier, avant de repartir. Traduction : « Un plaisir, comme toujours, messieurs. Je crois que vous pouvez vous débrouiller sans moi. »")},
    ]},
    {"h4": two("Rhodes and Saint Denis", "Rhodes et Saint-Denis")},
    {"quotes": [
        {"q": two("I promise you, this was all just a big misunderstanding. However, I want to thank you from the bottom of my heart.", "I promise you, this was all just a big misunderstanding. However, I want to thank you from the bottom of my heart."),
         "src": two("The New South (RDR2, chapter 3), to Sheriff Leigh Gray, as he is let out of the cage in Rhodes",
                    "The New South (RDR2, chapitre 3), au shérif Leigh Gray, au moment de sortir de la cage à Rhodes. Traduction : « Je vous assure, tout cela n'était qu'un grand malentendu. Cela dit, je tiens à vous remercier du fond du cœur. »")},
        {"q": two("The whole town is trapped in this interminable feud between the two families.", "The whole town is trapped in this interminable feud between the two families."),
         "src": two("The New South (RDR2, chapter 3), to Dutch, about the Grays and the Braithwaites",
                    "The New South (RDR2, chapitre 3), à Dutch, au sujet des Gray et des Braithwaite. Traduction : « Toute la ville est prisonnière de cette interminable querelle entre les deux familles. »")},
        {"q": two("You know me, I like to make friends in low places.", "You know me, I like to make friends in low places."),
         "src": two("Friends in Very Low Places (RDR2, chapter 3), to Arthur (quote list of the Red Dead Wiki)",
                    "Friends in Very Low Places (RDR2, chapitre 3), à Arthur (liste de citations du Red Dead Wiki). Traduction : « Tu me connais, j'aime me faire des amis dans les bas-fonds. »")},
        {"q": two("A discouraged man is no man at all, Alden... no man at all.", "A discouraged man is no man at all, Alden... no man at all."),
         "src": two("To Alden Carruthers, the Rhodes post office clerk (quote list of the Red Dead Wiki)",
                    "À Alden Carruthers, le guichetier de la poste de Rhodes (liste de citations du Red Dead Wiki). Traduction : « Un homme découragé n'est pas un homme, Alden... pas un homme du tout. »")},
        {"q": two("Everyone is the author of his own good fortune.", "Everyone is the author of his own good fortune."),
         "src": two("A Fine Night of Debauchery (RDR2, chapter 4), to Arthur (quote list of the Red Dead Wiki)",
                    "A Fine Night of Debauchery (RDR2, chapitre 4), à Arthur (liste de citations du Red Dead Wiki). Traduction : « Chacun est l'artisan de sa propre fortune. »")},
        {"q": two("There's plenty I don't like about you but I have the good manners to keep my mouth shut.", "There's plenty I don't like about you but I have the good manners to keep my mouth shut."),
         "src": two("To Desmond Blythe (quote list of the Red Dead Wiki)",
                    "À Desmond Blythe (liste de citations du Red Dead Wiki). Traduction : « Il y a bien des choses que je n'aime pas chez vous, mais j'ai la politesse de me taire. »")},
    ]},
    {"h4": two("Said about him", "Ce qu'on dit de lui")},
    {"quotes": [
        {"q": two("He hasn't stopped talking since we left you in Valentine. It's the longest ride of my life.", "He hasn't stopped talking since we left you in Valentine. It's the longest ride of my life."),
         "src": two("Javier Escuella to Arthur, The First Shall Be Last (RDR2, chapter 2), when Arthur asks why he is so quiet",
                    "Javier Escuella à Arthur, The First Shall Be Last (RDR2, chapitre 2), quand Arthur s'étonne de son silence. Traduction : « Il n'a pas arrêté de parler depuis qu'on t'a laissé à Valentine. C'est la plus longue chevauchée de ma vie. »")},
        {"q": two("He is a magician, I know him. He's a fool... but, he is not a bad feller.", "He is a magician, I know him. He's a fool... but, he is not a bad feller."),
         "src": two("Dutch van der Linde to Sheriff Leigh Gray, The New South (RDR2, chapter 3)",
                    "Dutch van der Linde au shérif Leigh Gray, The New South (RDR2, chapitre 3). Traduction : « C'est un magicien, je le connais. C'est un imbécile... mais ce n'est pas un mauvais bougre. »")},
        {"q": two("Trelawny owes... everyone for something, but his information is good.", "Trelawny owes... everyone for something, but his information is good."),
         "src": two("Hosea Matthews to Arthur and Dutch, The New South (RDR2, chapter 3), on the fishing ride that can follow the mission, after Arthur says Trelawny owes him for catching the Anderson boys",
                    "Hosea Matthews à Arthur et Dutch, The New South (RDR2, chapitre 3), pendant la partie de pêche qui peut suivre la mission, après qu'Arthur a dit que Trelawny lui devait une fière chandelle pour la capture des frères Anderson. Traduction : « Trelawny doit... quelque chose à tout le monde, mais ses renseignements sont bons. »")},
        {"q": two("Hey, maybe there are actually a hundred Trelawnys.", "Hey, maybe there are actually a hundred Trelawnys."),
         "src": two("Arthur Morgan, The New South (RDR2, chapter 3), on the optional fishing ride, after Dutch's outhouse story. Hosea answers: \"What a terrible thought.\"",
                    "Arthur Morgan, The New South (RDR2, chapitre 3), pendant la partie de pêche facultative, après l'histoire des latrines racontée par Dutch. Hosea répond : \"What a terrible thought.\" Traduction : « Hé, peut-être qu'il y a en fait cent Trelawny. » (« Quelle idée épouvantable. »)")},
        {"q": two("I ain't too sure. This is what tends to happen when you leave Trelawny in charge of planning. All garnish, no meat.", "I ain't too sure. This is what tends to happen when you leave Trelawny in charge of planning. All garnish, no meat."),
         "src": two("Arthur Morgan, A Fine Night of Debauchery (RDR2, chapter 4), when Javier asks how they will get off the Grand Korrigan (quote box of the mission page)",
                    "Arthur Morgan, A Fine Night of Debauchery (RDR2, chapitre 4), quand Javier demande comment ils vont quitter le Grand Korrigan (citation en exergue de la page de la mission). Traduction : « J'en sais trop rien. Voilà ce qui arrive quand on confie la préparation à Trelawny. Que de la garniture, pas de viande. »")},
        {"q": two("Of course he'll talk. He'd sell his own sister to save a train fare! He don't know how not to talk...", "Of course he'll talk. He'd sell his own sister to save a train fare! He don't know how not to talk..."),
         "src": two("Arthur Morgan about Trelawny (quote list of the Red Dead Wiki, which gives no mission)",
                    "Arthur Morgan à propos de Trelawny (liste de citations du Red Dead Wiki, qui ne précise pas la mission). Traduction : « Bien sûr qu'il va parler. Il vendrait sa propre sœur pour économiser un billet de train ! Il sait pas se taire... »")},
        {"q": two("He somehow manages to be both lucky and unlucky at the same time. But he always finds some way to pay us back. I guess that's his special talent... keeping fish on the line.", "He somehow manages to be both lucky and unlucky at the same time. But he always finds some way to pay us back. I guess that's his special talent... keeping fish on the line."),
         "src": two("Arthur Morgan about Trelawny (quote list of the Red Dead Wiki, which gives no mission)",
                    "Arthur Morgan à propos de Trelawny (liste de citations du Red Dead Wiki, qui ne précise pas la mission). Traduction : « Il arrive à avoir de la chance et de la malchance en même temps. Mais il trouve toujours un moyen de nous rembourser. C'est sans doute son talent particulier... garder le poisson au bout de la ligne. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("According to the Red Dead Wiki, Trelawny's name can appear in the camp ledger as the donor of an item even before he first comes to the Clemens Point camp.",
            "D'après le Red Dead Wiki, le nom de Trelawny peut figurer dans le registre du camp comme donateur d'un objet avant même sa première venue au camp de Clemens Point."),
        two("Before the ferry robbery, Arthur writes in his journal that he has heard talk of a man who sounded like Trelawny, whom the gang had not seen for months. The Red Dead Wiki notes how closely Trelawny resembles the Strange Man of Red Dead Redemption.",
            "Avant le braquage du ferry, Arthur note dans son journal qu'on lui a parlé d'un homme qui ressemblait à Trelawny, que la bande n'avait pas revu depuis des mois. Le Red Dead Wiki relève la forte ressemblance de Trelawny avec l'Homme mystérieux de Red Dead Redemption."),
        two("In \"Friends in Very Low Places\", the player can gun down Chester Damsen and the others on the coach while Trelawny keeps them busy. According to the mission page, Trelawny then curses the amateurs he works with and rides off; Arthur later meets him at a crossroads, where he voices his disappointment that his orders were not followed.",
            "Dans \"Friends in Very Low Places\", le joueur peut abattre Chester Damsen et les autres occupants de la diligence pendant que Trelawny les distrait. D'après la page de la mission, Trelawny peste alors contre les amateurs avec qui il travaille et s'en va ; Arthur le retrouve plus tard à un carrefour, où il se dit déçu qu'on n'ait pas respecté ses consignes."),
        two("If Arthur is already wearing a suit when \"A Fine Night of Debauchery\" starts, Trelawny tells him that it is not fit for the occasion. The newspaper in that opening scene is the Saint Denis Times No. 47, which the player can buy.",
            "Si Arthur porte déjà un costume au début de \"A Fine Night of Debauchery\", Trelawny lui fait savoir qu'il ne convient pas pour l'occasion. Le journal de cette scène d'ouverture est le Saint Denis Times n° 47, que le joueur peut acheter."),
        two("Trelawny is one of the gang members, with Micah, Lenny, Bill, Javier, Tilly and Uncle, who do not appear during the O'Driscoll attack on Shady Belle in \"Horsemen, Apocalypses\"; the game never explains their absence.",
            "Trelawny fait partie des membres de la bande, avec Micah, Lenny, Bill, Javier, Tilly et Uncle, absents lors de l'attaque des O'Driscoll contre Shady Belle dans \"Horsemen, Apocalypses\" ; le jeu n'explique jamais leur absence."),
        two("According to the Red Dead Wiki, there is a very rare chance that Trelawny tries to talk to Arthur about Guarma at Beaver Hollow.",
            "D'après le Red Dead Wiki, il existe une très faible probabilité que Trelawny tente de parler de Guarma avec Arthur à Beaver Hollow."),
        two("The stranger mission \"Of Men and Angels\" must be completed before \"The Fine Art of Conversation\", the mission in which Trelawny leaves, or it is no longer available.",
            "La mission d'inconnu \"Of Men and Angels\" doit être terminée avant \"The Fine Art of Conversation\", la mission du départ de Trelawny, faute de quoi elle n'est plus disponible."),
        two("His caravan on the edge of Rhodes can still be visited in 1907, run down and without a tenant.",
            "Sa roulotte, à la sortie de Rhodes, peut encore être visitée en 1907, délabrée et sans locataire."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Red Dead Online", "Red Dead Online")},
    {"p": two("Trelawny is one of the strangers who give missions in Red Dead Online, whose story is set in 1898, a year before the main game. The Red Dead Wiki names four members of the Van der Linde gang who appear in the online mode: Trelawny, [[sadie-adler|Sadie Adler]], Joe and [[sean-macguire|Sean MacGuire]]; Sadie and Joe have not yet joined the gang at that point. The player finds Trelawny on the porch of his rented caravan on the edge of Rhodes.",
              "Trelawny fait partie des inconnus qui proposent des missions dans Red Dead Online, dont l'histoire se déroule en 1898, un an avant le jeu principal. Le Red Dead Wiki cite quatre membres de la bande Van der Linde présents dans le mode en ligne : Trelawny, [[sadie-adler|Sadie Adler]], Joe et [[sean-macguire|Sean MacGuire]] ; Sadie et Joe n'ont pas encore rejoint la bande à ce moment-là. Le joueur trouve Trelawny sur le perron de la roulotte qu'il loue à la sortie de Rhodes.")},
    {"p": two("At their first meeting, Trelawny asks whether his wife sent the player, then says it is a long story. He raises a Cattleman Revolver to his own head, saying he cannot take it anymore, then thinks better of it, and the revolver becomes a bird and flies off. He declares his love for his family, describes himself as lost, then moves on and offers a job he presents as entirely legal: stealing a horse that belongs to [[catherine-braithwaite|Catherine Braithwaite]] and delivering it to his contact at Hill Haven Ranch, in Scarlett Meadows. Afterwards he offers further jobs from the caravan. According to the Red Dead Wiki, most of them earn the player positive honor.",
              "Lors de leur première rencontre, Trelawny demande au joueur si c'est sa femme qui l'envoie, puis explique que c'est une longue histoire. Il pointe un revolver Cattleman sur sa propre tempe en disant qu'il n'en peut plus, puis se ravise, et le revolver se change en oiseau et s'envole. Il clame son amour pour sa famille, se dit perdu, puis passe à autre chose et de proposer un travail qu'il présente comme parfaitement légal : voler un cheval appartenant à [[catherine-braithwaite|Catherine Braithwaite]] et le livrer à son contact au ranch Hill Haven, à Scarlett Meadows. Il propose ensuite d'autres missions depuis sa roulotte. D'après le Red Dead Wiki, la plupart rapportent au joueur de l'honneur positif.")},
    {"table": {"head": [two("Free roam mission", "Mission d'exploration"), two("What the player does", "Ce que fait le joueur")], "rows": [
        ["Horse Theft", two("Steals a horse and delivers it; Trelawny's version starts and ends in Rhodes.", "Vole un cheval et le livre ; la version de Trelawny part de Rhodes et s'y termine.")],
        ["Rescue", two("Frees a captive and brings them back; Trelawny's version runs from Rhodes to Trapper's Cabin.", "Libère un captif et le ramène ; la version de Trelawny va de Rhodes à Trapper's Cabin.")],
        ["Caravan Escort", two("Escorts two wagons and defends them from bandits; Trelawny's version runs from Rhodes to Lagras.", "Escorte deux chariots et les défend contre des bandits ; la version de Trelawny va de Rhodes à Lagras.")],
        ["On The Hunt", two("Tracks down a predator that threatens locals.", "Traque un prédateur qui menace les habitants.")],
        ["Destroy Supplies", two("Destroys crates or wagons of supplies; Trelawny's versions run from Rhodes to Caliga Hall or Bolger Glade.", "Détruit des caisses ou des chariots de marchandises ; les versions de Trelawny vont de Rhodes à Caliga Hall ou à Bolger Glade.")],
    ]}},
    {"quotes": [
        {"q": two("The truth is... I just can't take it anymore! Oh... no, that's not the truth. I don't know the bloody truth. I'm lost. I'm a lost soul, my friend.", "The truth is... I just can't take it anymore! Oh... no, that's not the truth. I don't know the bloody truth. I'm lost. I'm a lost soul, my friend."),
         "src": two("Red Dead Online, to the player at the first meeting (quote list of the Red Dead Wiki)",
                    "Red Dead Online, au joueur lors de leur première rencontre (liste de citations du Red Dead Wiki). Traduction : « La vérité, c'est que... je n'en peux plus ! Oh... non, ce n'est pas la vérité. Je ne connais pas cette fichue vérité. Je suis perdu. Je suis une âme perdue, mon ami. »")},
    ]},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Trelawny for Red Dead Redemption 2. On September 6, 2018, Rockstar posted his portrait and character description on Twitter, in a series covering the members of the gang, and The Hollywood Reporter reproduced the series the next day. In the composite image of the 23 gang members that opens Wikipedia's list of the game's characters, Trelawny is the last figure in the front row, next to Strauss.",
              "Rockstar a publié une illustration officielle de Trelawny pour Red Dead Redemption 2. Le 6 septembre 2018, Rockstar diffuse sur Twitter son portrait et sa description, dans une série consacrée aux membres de la bande, et The Hollywood Reporter reprend la série le lendemain. Sur l'image qui réunit les 23 membres de la bande, en tête de la liste des personnages du jeu sur Wikipédia, Trelawny est le dernier personnage du premier rang, à côté de Strauss.")},
]
