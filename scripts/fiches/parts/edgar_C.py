"""Edgar Ross, part C: missions, quotes, trivia, other media.

Sources (Red Dead Wiki EN and FR, Oct 2026): character page "Edgar Ross" (Mission Appearances, Quotes, Trivia,
Gallery captions); FR page "Edgar Ross" (mission list, Anecdotes: Ross does not appear in Undead Nightmare); mission
pages (infobox, story, objectives, mission failure, unlockables, trivia) "A Fisher of Men", "The Battle of Shady Belle",
"Banking, The Old American Art", "Just a Social Call", "Red Dead Redemption (mission)", "Ending Credits",
"Americans at Rest" (trivia: the woman in the Valentine saloon scene), "Exodus in America", "The Gates of El Presidio",
"Bear One Another's Burdens", "Great Men Are Not Always Wise", "And You Will Know The Truth",
"And The Truth Will Set You Free", "The Last Enemy That Shall Be Destroyed", "Remember My Family", "At Home with Dutch";
mission transcripts (all quotes below are checked verbatim against them): "A Fisher of Men/dialogues",
"Red Dead Redemption (mission)/dialogues", "The Gates of El Presidio/dialogues", "Bear One Another's Burdens/dialogues",
"Great Men are Not Always Wise/dialogues", "And You Will Know The Truth/dialogues",
"And The Truth Will Set You Free/dialogues", "Remember My Family/dialogues", "At Home with Dutch/dialogues"; newspaper
articles "Bureau of Investigation Founded" and "Edgar Ross Retires After a Lifetime of Government Service"; wiki pages
"Liars and Cheats", "Archer Fordham" (the 1914 article does not name Fordham), "Lake Don Julio House".
Cross-checked: uncle_C (Ross's 1914 outfit resembles Uncle's; the 2023 and 2024 ports have no multiplayer),
jack_C (Ross and Jack meet twice on screen, rifle in 1899, shotgun in 1914; the 400 dollar loot; the honor rules for
Emily and Phillip), dutch_D (the Damnation group of the Outfitter).

Quotes follow the transcripts where the wiki's quote list differs: "No one's playing games" (the list has "Nobody is"),
"having you put in the electric chair" (list: "putting you in"), "Oh spare me ... already" (list: "will you, old
boy?"), "You can't erase your past" (list: "the past"). The line "we're the bad guys" is not quoted because the
transcript sets it with dashes; its end ("Sure, civilization may be dull ...") is quoted. The Beaver Hollow lines
"They have no way out of there. Find them and kill them." and "Mr. Morgan, Mr. Marston. You are trapped. Surrender and
we will take you alive." are in the transcript (the wiki's list has "You're trapped") and are quoted once, in part A.
Fact-check fixes (20 Oct 2026): the six lines quoted under Personality > In his own words are no longer repeated here;
the two "And You Will Know The Truth" lines on the "noble savage" and the "nature writers" are added from the transcript.

Excluded from trivia: name etymology, height, eye color (part B); Charles Joseph Bonaparte, J. Edgar Hoover and Frank
Tenpenny (part D, development; the Tenpenny and Toreno comparisons are the wiki's reading); the unused Strawberry
cutscene with Sheriff Hanley (cut content, part D); Ross and Fordham's Winchester Repeater (part B, weapons); the
pistol barrel pushed into John's chest as "foreshadowing" (interpretation); Ross "unhappy with his retirement"
(interpretation in the mission trivia); campfire talk of Ross killed by robbers (marked "citation needed"); Blind Man
Cassidy's warning (the man is unnamed); the honor cost of the office safe (the mission page gives two contradictory
statements, so only the safe itself is kept); the mission not appearing if Ross was killed earlier (contradicts his
invulnerability, glitch claim without source).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
EP2 = two("Epilogue 2: Beecher's Hope", "Épilogue 2 : Beecher's Hope")
A1 = two("Act I: New Austin", "Acte I : New Austin")
A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")
A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
E1914 = two("1914 epilogue", "Épilogue de 1914")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Ross appears in six missions of Red Dead Redemption 2 (one by voice only, one in the end credits) and eight of Red Dead Redemption. In Red Dead Redemption, four of them form his own mission strand, from \"Bear One Another's Burdens\" to \"And The Truth Will Set You Free\"; according to the Red Dead Wiki, they are marked on the map with the letter G, for Government, rather than with an initial of his name. The table for Red Dead Redemption adds \"At Home with Dutch\", in which he is only mentioned.",
              "Ross apparaît dans six missions de Red Dead Redemption 2 (dont une où l'on n'entend que sa voix et une limitée au générique de fin) et dans huit missions de Red Dead Redemption. Dans Red Dead Redemption, quatre d'entre elles forment sa propre série de missions, de \"Bear One Another's Burdens\" à \"And The Truth Will Set You Free\" ; d'après le Red Dead Wiki, elles sont signalées sur la carte par la lettre G, pour Government (gouvernement), et non par une initiale de son nom. Le tableau consacré à Red Dead Redemption ajoute \"At Home with Dutch\", où il est seulement cité.")},
    {"h4": two("Red Dead Redemption 2, chapters 2 to 6", "Red Dead Redemption 2, chapitres 2 à 6")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Ross's role", "Rôle de Ross")], "rows": [
        M("A Fisher of Men", C2,
          "First appearance. Arrives with [[andrew-milton|Milton]] while [[arthur-morgan|Arthur]] fishes with [[jack-marston|Jack]], and speaks only to Jack. Arthur then names him to [[dutch-van-der-linde|Dutch]] at camp.",
          "Première apparition. Arrive avec [[andrew-milton|Milton]] pendant qu'[[arthur-morgan|Arthur]] pêche avec [[jack-marston|Jack]], et ne s'adresse qu'à Jack. Arthur le nomme ensuite devant [[dutch-van-der-linde|Dutch]], au camp."),
        M("The Battle of Shady Belle", C3,
          "Walks into Clemens Point with Milton, who introduces him. He does not speak. The gang refuses Milton's offer and moves to Shady Belle.",
          "Entre dans le camp de Clemens Point avec Milton, qui le présente. Il ne dit rien. Le gang rejette l'offre de Milton et s'installe à Shady Belle."),
        M("Banking, The Old American Art", C4,
          "Listed by the wiki. The mission page names only Milton; the character page places Ross beside him when he executes [[hosea-matthews|Hosea]].",
          "Citée par le wiki. La page de la mission ne nomme que Milton ; la page du personnage place Ross à ses côtés quand il exécute [[hosea-matthews|Hosea]]."),
        M("Just a Social Call", C6,
          "Steps off [[leviticus-cornwall|Cornwall]]'s yacht in Annesburg with Milton. Cornwall scolds both agents for their lack of results.",
          "Descend du yacht de [[leviticus-cornwall|Cornwall]] à Annesburg avec Milton. Cornwall reproche aux deux agents leur manque de résultats."),
        M("Red Dead Redemption", C6,
          "Voice only. Commands the Pinkerton assault on Beaver Hollow after Milton's death and orders Arthur and [[john-marston|John]] taken dead or alive.",
          "Voix seulement. Dirige l'assaut des Pinkerton sur Beaver Hollow après la mort de Milton et ordonne qu'on prenne Arthur et [[john-marston|John]] morts ou vifs."),
    ]}},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"table": {"head": [two("Mission", "Mission"), two("Part", "Partie"), two("Ross's role", "Rôle de Ross")], "rows": [
        M("American Venom", EP2,
          "End credits only. With [[archer-fordham|Archer Fordham]], finds [[micah-bell|Micah]]'s body on Mount Hagen, questions people in Valentine and near Rhodes, then watches John and Jack at Beecher's Hope.",
          "Générique de fin uniquement. Avec [[archer-fordham|Archer Fordham]], découvre le corps de [[micah-bell|Micah]] au mont Hagen, interroge des témoins à Valentine et près de Rhodes, puis observe John et Jack à Beecher's Hope."),
    ]}},
    {"h4": two("Red Dead Redemption, 1911", "Red Dead Redemption, 1911")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Ross's role", "Rôle de Ross")], "rows": [
        M("Exodus in America", A1,
          "Opening cutscene. With Fordham, escorts John from the Blackwater ferry to the train for Armadillo.",
          "Cinématique d'ouverture. Avec Fordham, escorte John du ferry de Blackwater jusqu'au train pour Armadillo."),
        M("The Gates of El Presidio", A2,
          "Final scene. Collects [[javier-escuella|Javier Escuella]], alive or dead, near the border bridge. If Javier is captured, handing him over is the last objective.",
          "Scène finale. Récupère [[javier-escuella|Javier Escuella]], mort ou vif, près du pont de la frontière. Si Javier est capturé, le remettre aux agents constitue le dernier objectif."),
        M("Bear One Another's Burdens", A3,
          "Mission giver; the forty-second mission of the game and the first of the West Elizabeth part. Drives to the wreck of the Serendipity and fights beside John when the car breaks down. Unlocks the [[harold-macdougal|Harold MacDougal]] strand. The mission fails if Ross is attacked or killed.",
          "Donneur de mission ; quarante-deuxième mission du jeu et première de la partie West Elizabeth. Se rend à l'épave du Serendipity et combat aux côtés de John quand la voiture tombe en panne. Débloque la série de missions d'[[harold-macdougal|Harold MacDougal]]. La mission échoue si Ross est agressé ou tué."),
        M("At Home with Dutch", A3,
          "Mentioned only: MacDougal says Ross told him about John's past with Dutch.",
          "Simplement cité : MacDougal raconte que Ross lui a parlé du passé de John avec Dutch."),
        M("Great Men Are Not Always Wise", A3,
          "Mission giver. Sets the ambush on Dutch at the Blackwater bank from a rooftop, then leads the chase towards Bearclaw Camp. The mission fails if he is attacked or killed.",
          "Donneur de mission. Tend depuis un toit l'embuscade contre Dutch à la banque de Blackwater, puis mène la poursuite vers Bearclaw Camp. La mission échoue s'il est agressé ou tué."),
        M("And You Will Know The Truth", A3,
          "Mission giver. Rides in the armored truck to the army camp used as bait. He, Fordham and John are slightly hurt when the truck overturns.",
          "Donneur de mission. Monte dans le camion blindé jusqu'au camp de l'armée qui sert d'appât. Fordham, John et lui sont légèrement blessés quand le camion se renverse."),
        M("And The Truth Will Set You Free", A3,
          "Rides to Cochinay with the army and shoots Dutch's body after his fall. Last mission of the West Elizabeth part; it unlocks the Abigail Marston strand.",
          "Chevauche jusqu'à Cochinay avec l'armée et tire sur le corps de Dutch après sa chute. Dernière mission de la partie West Elizabeth ; elle débloque la série de missions d'Abigail Marston."),
        M("The Last Enemy That Shall Be Destroyed", A3,
          "Leads the attack on Beecher's Hope in which [[uncle|Uncle]] and John are killed. The fifty-seventh and last story mission.",
          "Mène l'attaque de Beecher's Hope où meurent [[uncle|Uncle]] et John. Cinquante-septième et dernière mission principale."),
    ]}},
    {"h4": two("Red Dead Redemption, 1914", "Red Dead Redemption, 1914")},
    {"table": {"head": [two("Mission", "Mission"), two("Period", "Période"), two("Ross's role", "Rôle de Ross")], "rows": [
        M("Remember My Family", E1914,
          "Stranger mission given by the agent Howard Sawicki in Blackwater, playable only as Jack. Ross is the target: Jack kills him in a duel on the San Luis River. Rewards: 50 Fame and 100 Honor, and the achievement or trophy \"Nurture or Nature?\".",
          "Mission d'inconnu confiée par l'agent Howard Sawicki à Blackwater, jouable uniquement avec Jack. Ross en est la cible : Jack le tue en duel au bord de la San Luis River. Récompenses : 50 points de renommée, 100 points d'honneur et le succès ou trophée \"Nurture or Nature?\"."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the original English, with the mission and the person addressed. His lines on civilization, the age of the machine and the medal he expects are quoted under Personality (In his own words).",
              "Les répliques ci-dessous sont reproduites dans leur version originale anglaise, avec la mission et la personne à qui elles s'adressent. Ses répliques sur la civilisation, l'âge de la machine et la médaille qu'il attend figurent dans la personnalité (Dans ses propres mots).")},
    {"h4": two("Red Dead Redemption 2 (1899 and 1907)", "Red Dead Redemption 2 (1899 et 1907)")},
    {"quotes": [
        {"q": two("Enjoy your fishing, kid... while you still can.", "Enjoy your fishing, kid... while you still can."),
         "src": two("A Fisher of Men (RDR2, chapter 2), to Jack, as he leaves",
                    "A Fisher of Men (RDR2, chapitre 2), à Jack, en partant. Traduction : « Profite bien de ta pêche, petit... tant que tu le peux encore. »")},
        {"q": two("This is Agent Ross with the Pinkerton Detective Agency. Put your guns down. Lay down your weapons now. We have you surrounded.", "This is Agent Ross with the Pinkerton Detective Agency. Put your guns down. Lay down your weapons now. We have you surrounded."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), to the gang, at the start of the assault on Beaver Hollow",
                    "Red Dead Redemption (RDR2, chapitre 6), au gang, au début de l'assaut sur Beaver Hollow. Traduction : « Ici l'agent Ross, de la Pinkerton Detective Agency. Lâchez vos armes. Déposez vos armes immédiatement. Vous êtes cernés. »")},
        {"q": two("I see Arthur Morgan and John Marston. Drop your weapons, put your hands in the air and we will cease fire.", "I see Arthur Morgan and John Marston. Drop your weapons, put your hands in the air and we will cease fire."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), spotting Arthur and John near the cave",
                    "Red Dead Redemption (RDR2, chapitre 6), en repérant Arthur et John près de la grotte. Traduction : « Je vois Arthur Morgan et John Marston. Jetez vos armes, levez les mains et nous cesserons le feu. »")},
        {"q": two("I want them out of there now, dead or alive. Do you understand me?", "I want them out of there now, dead or alive. Do you understand me?"),
         "src": two("Red Dead Redemption (RDR2, chapter 6), to his agents, as Arthur and John reach the ladder out of the cave",
                    "Red Dead Redemption (RDR2, chapitre 6), à ses agents, quand Arthur et John atteignent l'échelle qui sort de la grotte. Traduction : « Je veux qu'on les sorte de là tout de suite, morts ou vifs. C'est compris ? »")},
        {"q": two("I want all criminals to know that here in America, everyone will eventually pay for what they have done.", "I want all criminals to know that here in America, everyone will eventually pay for what they have done."),
         "src": two("Statement on being sworn in, quoted in the newspaper article \"Bureau of Investigation Founded\" (RDR2, 1907)",
                    "Déclaration lors de sa prestation de serment, citée dans l'article \"Bureau of Investigation Founded\" (RDR2, 1907). Traduction : « Je veux que tous les criminels sachent qu'ici, en Amérique, chacun finira par payer pour ce qu'il a fait. »")},
    ]},
    {"h4": two("Red Dead Redemption, Acts II and III (1911)", "Red Dead Redemption, actes II et III (1911)")},
    {"quotes": [
        {"q": two("Mr. Marston! Fancy seeing you down here.", "Mr. Marston! Fancy seeing you down here."),
         "src": two("The Gates of El Presidio (RDR1, Act II), to John, near the border bridge",
                    "The Gates of El Presidio (RDR1, acte II), à John, près du pont de la frontière. Traduction : « Monsieur Marston ! Qui l'eût cru, vous voir par ici. »")},
        {"q": two("Oh, your wife sends her regards.", "Oh, your wife sends her regards."),
         "src": two("The Gates of El Presidio (RDR1, Act II), to John, before driving off with Javier",
                    "The Gates of El Presidio (RDR1, acte II), à John, avant de repartir avec Javier. Traduction : « Ah, votre femme vous transmet ses amitiés. »")},
        {"q": two("No one's playing games with you, Mr. Marston. But if we were to play some games, there'd be some interesting ones we could play. Like hanging you for murder, or confiscating all your property, like that little farm of yours, or having you put in the electric chair. Those are the sort of games we could play, but we choose to play a different game, so calm down, and play along with us.", "No one's playing games with you, Mr. Marston. But if we were to play some games, there'd be some interesting ones we could play. Like hanging you for murder, or confiscating all your property, like that little farm of yours, or having you put in the electric chair. Those are the sort of games we could play, but we choose to play a different game, so calm down, and play along with us."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), to John, who accuses the agents of playing games with him",
                    "Bear One Another's Burdens (RDR1, acte III), à John, qui accuse les agents de jouer avec lui. Traduction : « Personne ne joue avec vous, monsieur Marston. Mais si nous voulions jouer, il y aurait des jeux intéressants à notre disposition. Vous pendre pour meurtre, par exemple, ou confisquer tous vos biens, comme votre petite ferme, ou vous faire passer sur la chaise électrique. Voilà le genre de jeux auxquels nous pourrions jouer, mais nous avons choisi un autre jeu, alors calmez-vous et jouez le jeu avec nous. »")},
        {"q": two("Mr. Marston, please, I've never insulted your meagre intelligence. Do not insult mine.", "Mr. Marston, please, I've never insulted your meagre intelligence. Do not insult mine."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), to John, who asks again where his wife is",
                    "Bear One Another's Burdens (RDR1, acte III), à John, qui demande encore où se trouve sa femme. Traduction : « Monsieur Marston, je vous en prie, je n'ai jamais insulté votre maigre intelligence. N'insultez pas la mienne. »")},
        {"q": two("Come on, Marston. Moral degeneracy waits for no man. Let's hurry along.", "Come on, Marston. Moral degeneracy waits for no man. Let's hurry along."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), to John, after releasing Nigel West Dickens",
                    "Bear One Another's Burdens (RDR1, acte III), à John, après avoir fait relâcher Nigel West Dickens. Traduction : « Allons, Marston. La dégénérescence morale n'attend personne. Pressons. »")},
        {"q": two("The life you lived...you don't just walk away from that, buy a few chickens and make it all disappear. You should be dead or rotting in a jail cell by now. We are giving you a chance at new life, a chance at redemption. You can't erase your past, Mr. Marston, but we can.", "The life you lived...you don't just walk away from that, buy a few chickens and make it all disappear. You should be dead or rotting in a jail cell by now. We are giving you a chance at new life, a chance at redemption. You can't erase your past, Mr. Marston, but we can."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), to John, who asks where it will end",
                    "Bear One Another's Burdens (RDR1, acte III), à John, qui demande où tout cela s'arrêtera. Traduction : « La vie que vous avez menée... on ne tourne pas le dos à ça en achetant quelques poules pour tout faire disparaître. Vous devriez être mort ou en train de pourrir dans une cellule à l'heure qu'il est. Nous vous offrons une chance de nouvelle vie, une chance de rédemption. Vous ne pouvez pas effacer votre passé, monsieur Marston, mais nous, nous le pouvons. »")},
        {"q": two("You see this, Mr. Fordham. The brooding cowboy. There aren't many of these left, you know. A bit of a cliche, admittedly, but still a dying breed. Like the buffalo, just as dumb but not quite as noble.", "You see this, Mr. Fordham. The brooding cowboy. There aren't many of these left, you know. A bit of a cliche, admittedly, but still a dying breed. Like the buffalo, just as dumb but not quite as noble."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), to Fordham, in the automobile, after John says he is not comfortable",
                    "Bear One Another's Burdens (RDR1, acte III), à Fordham, en automobile, après que John a dit ne pas être à l'aise. Traduction : « Regardez-moi ça, monsieur Fordham. Le cow-boy ténébreux. Il n'en reste plus beaucoup, vous savez. Un peu cliché, je l'admets, mais une espèce en voie de disparition. Comme le bison, tout aussi bête, mais pas tout à fait aussi noble. »")},
        {"q": two("You're a murderer. Actions have consequences, Mr. Marston.", "You're a murderer. Actions have consequences, Mr. Marston."),
         "src": two("Bear One Another's Burdens (RDR1, Act III), to John, who has just called him a coward for taking a man's wife and child",
                    "Bear One Another's Burdens (RDR1, acte III), à John, qui vient de le traiter de lâche pour avoir enlevé la femme et l'enfant d'un homme. Traduction : « Vous êtes un assassin. Les actes ont des conséquences, monsieur Marston. »")},
        {"q": two("Let's just say, our Bureau is tasked with work of special interest to Washington. Work that requires a little more skill and finesse.", "Let's just say, our Bureau is tasked with work of special interest to Washington. Work that requires a little more skill and finesse."),
         "src": two("Great Men are Not Always Wise (RDR1, Act III), to John, who asks whether the agents are lawmen or army",
                    "Great Men are Not Always Wise (RDR1, acte III), à John, qui demande si les agents sont des hommes de loi ou des militaires. Traduction : « Disons que notre Bureau est chargé de missions qui intéressent tout particulièrement Washington. Des missions qui demandent un peu plus de savoir-faire et de doigté. »")},
        {"q": two("Oh spare me the noble savage fall on my sword tripe, already. It's nauseating. You don't wish to be dead. You're an insignificant creature, desperately clinging onto life like the rest of the scum in this town.", "Oh spare me the noble savage fall on my sword tripe, already. It's nauseating. You don't wish to be dead. You're an insignificant creature, desperately clinging onto life like the rest of the scum in this town."),
         "src": two("And You Will Know The Truth (RDR1, Act III), to John, who says he wishes the agents had killed him",
                    "And You Will Know The Truth (RDR1, acte III), à John, qui dit regretter que les agents ne l'aient pas tué. Traduction : « Oh, épargnez-moi ce numéro de noble sauvage prêt à se jeter sur son épée. C'est écœurant. Vous n'avez aucune envie de mourir. Vous êtes une créature insignifiante, qui s'accroche désespérément à la vie comme le reste de la racaille de cette ville. »")},
        {"q": two("He's like one of those nature writers from back East. Only he gets things a tiny little step too far. Rather than just loving the flowers and the animals and the harmony between man and beast, he shoots people in the head for money. And disagreeing with him. [...] Now, I'm not a great intellect, but the metaphysical leap from admiring the flower to shooting a man in the head because he doesn't like the flower, is a leap too far.", "He's like one of those nature writers from back East. Only he gets things a tiny little step too far. Rather than just loving the flowers and the animals and the harmony between man and beast, he shoots people in the head for money. And disagreeing with him. [...] Now, I'm not a great intellect, but the metaphysical leap from admiring the flower to shooting a man in the head because he doesn't like the flower, is a leap too far."),
         "src": two("And You Will Know The Truth (RDR1, Act III), to John, about Dutch",
                    "And You Will Know The Truth (RDR1, acte III), à John, à propos de Dutch. Traduction : « Il est comme ces écrivains naturalistes de l'Est. Sauf qu'il va un tout petit peu trop loin. Au lieu de se contenter d'aimer les fleurs, les animaux et l'harmonie entre l'homme et la bête, il loge des balles dans la tête des gens pour de l'argent. Et parce qu'ils ne sont pas d'accord avec lui. [...] Bon, je ne suis pas un grand esprit, mais le saut métaphysique qui mène de l'admiration d'une fleur à une balle dans la tête d'un homme parce qu'il n'aime pas cette fleur, c'est un saut de trop. »")},
        {"q": two("Good God, this flawed philosophy of yours again. If you wish to argue the finer points of ethics, I suggest you learn to read first.", "Good God, this flawed philosophy of yours again. If you wish to argue the finer points of ethics, I suggest you learn to read first."),
         "src": two("And The Truth Will Set You Free (RDR1, Act III), to John, on the ride to Cochinay",
                    "And The Truth Will Set You Free (RDR1, acte III), à John, en route pour Cochinay. Traduction : « Bon Dieu, encore votre philosophie bancale. Si vous voulez débattre des subtilités de l'éthique, je vous conseille d'apprendre d'abord à lire. »")},
        {"q": two("So, at the end, you didn't have the guts to shoot him?", "So, at the end, you didn't have the guts to shoot him?"),
         "src": two("And The Truth Will Set You Free (RDR1, Act III), to John, at Dutch's body",
                    "And The Truth Will Set You Free (RDR1, acte III), à John, près du corps de Dutch. Traduction : « Alors, au bout du compte, vous n'avez pas eu le cran de l'abattre ? »")},
        {"q": two("Oh trust me, it looks better in the report that way.", "Oh trust me, it looks better in the report that way."),
         "src": two("And The Truth Will Set You Free (RDR1, Act III), after firing John's gun into Dutch's body",
                    "And The Truth Will Set You Free (RDR1, acte III), après avoir tiré avec l'arme de John sur le corps de Dutch. Traduction : « Oh, croyez-moi, ça fait mieux dans le rapport. »")},
        {"q": two("Your wife was killed in a prison riot last week.", "Your wife was killed in a prison riot last week."),
         "src": two("And The Truth Will Set You Free (RDR1, Act III), to John, who asks where his family is",
                    "And The Truth Will Set You Free (RDR1, acte III), à John, qui demande où se trouve sa famille. Traduction : « Votre femme a été tuée dans une émeute à la prison la semaine dernière. »")},
        {"q": two("I'm only joking, dear boy. They were sent back to that scrabble ranch of yours in Beecher's Hope. They're quite safe and sound.", "I'm only joking, dear boy. They were sent back to that scrabble ranch of yours in Beecher's Hope. They're quite safe and sound."),
         "src": two("And The Truth Will Set You Free (RDR1, Act III), once John has drawn his gun on him",
                    "And The Truth Will Set You Free (RDR1, acte III), une fois que John l'a mis en joue. Traduction : « Je plaisante, mon cher. Ils ont été renvoyés dans votre petit ranch miteux de Beecher's Hope. Ils sont sains et saufs. »")},
        {"q": two("Yeah, exactly. See you around. Try to stay out of trouble. Come on, Archer, let's go find somebody else we can annoy.", "Yeah, exactly. See you around. Try to stay out of trouble. Come on, Archer, let's go find somebody else we can annoy."),
         "src": two("And The Truth Will Set You Free (RDR1, Act III), after Fordham thanks John, as the agents leave",
                    "And The Truth Will Set You Free (RDR1, acte III), après les remerciements de Fordham à John, au moment où les agents s'en vont. Traduction : « Oui, exactement. À un de ces jours. Tâchez d'éviter les ennuis. Venez, Archer, allons trouver quelqu'un d'autre à embêter. »")},
    ]},
    {"h4": two("Red Dead Redemption, 1914", "Red Dead Redemption, 1914")},
    {"quotes": [
        {"q": two("I see... I remember your father.", "I see... I remember your father."),
         "src": two("Remember My Family (RDR1, 1914), to Jack, who has just introduced himself as John Marston's son",
                    "Remember My Family (RDR1, 1914), à Jack, qui vient de se présenter comme le fils de John Marston. Traduction : « Je vois... Je me souviens de ton père. »")},
        {"q": two("And you boy, have sure as shit found me.", "And you boy, have sure as shit found me."),
         "src": two("Remember My Family (RDR1, 1914), to Jack, who says he has come for him",
                    "Remember My Family (RDR1, 1914), à Jack, qui annonce être venu pour lui. Traduction : « Et toi, mon garçon, tu m'as bel et bien trouvé, nom de Dieu. »")},
        {"q": two("Your father killed himself with the life he lived.", "Your father killed himself with the life he lived."),
         "src": two("Remember My Family (RDR1, 1914), to Jack, who accuses him of killing John",
                    "Remember My Family (RDR1, 1914), à Jack, qui l'accuse d'avoir tué John. Traduction : « Ton père s'est tué lui-même avec la vie qu'il a menée. »")},
        {"q": two("And I'll shoot you like one too, you little piece of trash! Now get out of here before I kill you as well!", "And I'll shoot you like one too, you little piece of trash! Now get out of here before I kill you as well!"),
         "src": two("Remember My Family (RDR1, 1914), his last words, to Jack, who says he shot his father like a dog",
                    "Remember My Family (RDR1, 1914), ses derniers mots, à Jack, qui lui reproche d'avoir abattu son père comme un chien. Traduction : « Et je vais t'abattre comme un chien toi aussi, petite ordure ! Maintenant, file avant que je te tue toi aussi ! »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Across both games", "Dans les deux jeux")},
    {"ul": [
        two("According to the Red Dead Wiki, Ross and Jack Marston are the only major characters of the series who appear in all four periods of the Redemption story: 1899, 1907, 1911 and 1914.",
            "Selon le Red Dead Wiki, Ross et Jack Marston sont les seuls personnages majeurs de la série présents dans les quatre périodes de l'histoire Redemption : 1899, 1907, 1911 et 1914."),
        two("On screen, Ross and Jack meet only twice, in \"A Fisher of Men\" in 1899 and in \"Remember My Family\" in 1914. Both scenes take place on a riverbank, and Ross holds a long gun both times: a rifle in 1899, a duck-hunting shotgun in 1914.",
            "À l'écran, Ross et Jack ne se croisent que deux fois, dans \"A Fisher of Men\" en 1899 et dans \"Remember My Family\" en 1914. Les deux scènes se passent au bord d'une rivière, et Ross tient chaque fois une arme d'épaule : un fusil en 1899, un fusil de chasse au canard en 1914."),
        two("According to the Red Dead Wiki, Ross's height and eye color differ between the two games: he is much shorter than John and Fordham in Red Dead Redemption but about as tall as Fordham and Milton in Red Dead Redemption 2, and his eyes are blue in the first game and brown in the second.",
            "Selon le Red Dead Wiki, la taille et la couleur des yeux de Ross changent d'un jeu à l'autre : il est bien plus petit que John et Fordham dans Red Dead Redemption, mais à peu près de la taille de Fordham et de Milton dans Red Dead Redemption 2, et ses yeux sont bleus dans le premier jeu, bruns dans le second."),
    ]},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"ul": [
        two("In the 1907 end credits, Ross and Fordham still wear Pinkerton badges, although a newspaper of the epilogue reports Ross's appointment at the head of the new Bureau.",
            "Dans le générique de 1907, Ross et Fordham portent encore des insignes Pinkerton, alors qu'un journal de l'épilogue annonce la nomination de Ross à la tête du nouveau Bureau."),
        two("One of the women Arthur scares away from Javier in the Valentine saloon during \"Americans at Rest\" reappears in the credits scene in which Ross and Fordham question customers of Smithfield's Saloon.",
            "L'une des femmes qu'Arthur fait fuir quand elles parlent avec Javier au saloon de Valentine, dans \"Americans at Rest\", réapparaît dans la scène du générique où Ross et Fordham interrogent des clients du Smithfield's Saloon."),
    ]},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("Nigel West Dickens says to John, during one of his own missions, the same sentence about moral degeneracy that Ross uses in \"Bear One Another's Burdens\" (see Quotes).",
            "Nigel West Dickens adresse à John, lors de l'une de ses propres missions, la même phrase sur la dégénérescence morale que Ross prononce dans \"Bear One Another's Burdens\" (voir les citations)."),
        two("At the start of \"Great Men Are Not Always Wise\", John can go back into Ross's office and crack a safe that is only accessible during this mission.",
            "Au début de \"Great Men Are Not Always Wise\", John peut retourner dans le bureau de Ross et forcer un coffre-fort accessible uniquement pendant cette mission."),
        two("During John's last stand in \"The Last Enemy That Shall Be Destroyed\", aiming at Ross shows a friendly cursor, and he cannot be killed, so the scene always plays out.",
            "Pendant le dernier combat de John dans \"The Last Enemy That Shall Be Destroyed\", viser Ross affiche un réticule allié, et il est impossible de le tuer, si bien que la scène se déroule toujours de la même façon."),
        two("The 1914 newspaper article credits Ross alone with the deaths of the gang members. It does not mention Archer Fordham or the soldiers and marshals present at Beecher's Hope.",
            "L'article de presse de 1914 attribue à Ross seul la mort des membres du gang. Il ne mentionne ni Archer Fordham, ni les soldats et marshals présents à Beecher's Hope."),
        two("Ross's 1914 cabin on Lake Don Julio is the house where Irish sends John to look for a Gatling gun in \"A Frenchman, a Welshman and an Irishman\".",
            "La cabane de Ross au bord du lac Don Julio, en 1914, est la maison où Irish envoie John chercher une mitrailleuse Gatling dans \"A Frenchman, a Welshman and an Irishman\"."),
        two("In \"Remember My Family\", Ross wears clothes similar to Uncle's. He can be heard cursing when he misses the ducks.",
            "Dans \"Remember My Family\", Ross porte une tenue proche de celle d'Uncle. On l'entend jurer quand il rate les canards."),
        two("Aiming at Ross, his wife or his brother through a rifle scope before the duel fails the mission, even without firing. Hogtying Ross also fails it: he must die in the scripted duel. In the duel, aiming at his gun or his hand does not fill the bar, and the player loses.",
            "Viser Ross, sa femme ou son frère à travers une lunette avant le duel fait échouer la mission, même sans tirer. Ligoter Ross la fait aussi échouer : il doit mourir pendant le duel scénarisé. Pendant ce duel, viser son arme ou sa main ne remplit pas la jauge, et le joueur perd."),
        two("Jack can kill Emily and Phillip Ross after talking to them without failing the mission. It costs honor unless he wears the bandana, and killing Edgar Ross restores the honor lost.",
            "Jack peut tuer Emily et Phillip Ross après leur avoir parlé sans faire échouer la mission. Il perd alors de l'honneur, sauf s'il porte le bandana, et tuer Edgar Ross lui rend l'honneur perdu."),
        two("Each time the duel is lost and restarted, Ross hunts with a different shotgun: a double-barreled, a semi-automatic or a pump-action model. Players can use this to get the semi-automatic shotgun for free from his body.",
            "Chaque fois que le duel est perdu puis relancé, Ross chasse avec un fusil de chasse différent : un modèle à deux canons, un semi-automatique ou un fusil à pompe. Les joueurs peuvent s'en servir pour récupérer gratuitement le fusil semi-automatique sur son corps."),
        two("After the closing credits, Ross's body can be looted for 400 dollars. A shot from a powerful weapon can send it into the river, where it can only be looted after being pushed back to the bank on foot.",
            "Après le générique de fin, on peut récupérer 400 dollars sur le corps de Ross. Un tir d'arme puissante peut le projeter dans la rivière, et il faut alors le repousser à pied vers la berge pour le fouiller."),
        two("Once \"Remember My Family\" is completed, its summary text calls Ross an FBI agent. The Bureau of Investigation only took that name in 1935.",
            "Une fois \"Remember My Family\" terminée, son texte de résumé qualifie Ross d'agent du FBI. Le Bureau of Investigation n'a pris ce nom qu'en 1935."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors continuité)")},
    {"ul": [
        two("Ross does not appear in Undead Nightmare. His office in Blackwater is empty, with his diplomas still on the wall.",
            "Ross n'apparaît pas dans Undead Nightmare. Son bureau de Blackwater est vide, ses diplômes toujours accrochés au mur."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Ross became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, released on September 21, 2010 for 9.99 dollars on the PlayStation Network and 800 Microsoft Points on Xbox Live. The pack added fifteen characters from the story. Players select Ross in the Damnation section of the Outfitter, with [[abraham-reyes|Abraham Reyes]], [[agustin-allende|Agustin Allende]], [[bill-williamson|Bill Williamson]], [[dutch-van-der-linde|Dutch van der Linde]], [[harold-macdougal|Harold MacDougal]] and [[irish|Irish]]. The other group, Redemption, includes John, Abigail and Jack Marston. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, do not include the multiplayer mode, so the Ross model is not available in them.",
              "Ross devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, sorti le 21 septembre 2010 au prix de 9,99 dollars sur le PlayStation Network et de 800 Microsoft Points sur le Xbox Live. Le pack ajoute quinze personnages de l'histoire. On choisit Ross dans la section Damnation de l'Outfitter, avec [[abraham-reyes|Abraham Reyes]], [[agustin-allende|Agustin Allende]], [[bill-williamson|Bill Williamson]], [[dutch-van-der-linde|Dutch van der Linde]], [[harold-macdougal|Harold MacDougal]] et [[irish|Irish]]. L'autre groupe, Redemption, réunit notamment John, Abigail et Jack Marston. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, ne comprennent pas le multijoueur : le modèle Ross n'y est donc pas disponible.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("The official artwork of Ross for Red Dead Redemption shows him holding a Colt M1911 pistol. This weapon does not appear in the game. The United States Army adopted the M1911 in March 1911, and full-scale production started in 1912.",
              "L'illustration officielle de Ross pour Red Dead Redemption le montre un pistolet Colt M1911 à la main. Cette arme n'apparaît pas dans le jeu. L'armée américaine a adopté le M1911 en mars 1911, et sa production à grande échelle n'a démarré qu'en 1912.")},
]
