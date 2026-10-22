"""Harold MacDougal, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/, copies in
scripts/v3/work/macdougal/fc/):
- Character page "Harold MacDougal" (Mission appearances, Quotes, Trivia, Gallery captions) and FR page,
  macdougal/en.txt and macdougal/fr.txt.
- Mission pages (infobox rewards, order numbers, prerequisites, unlocks, trivia): "Bear One Another's Burdens"
  (42nd mission, first of West Elizabeth; unlocks the MacDougal strand), "At Home with Dutch" (44th; giver
  MacDougal; binoculars; achievement "A Savage Soul"), "For Purely Scientific Purposes" (45th), "The Prodigal Son
  Returns (To Yale)" (46th; 100 dollars; Luke 15:11-32; Bible packed; Chu Fuk Choi in the same hotel room),
  "Curious Tales from Blackwater" (Undead Nightmare; torch and Repeater Carbine), "Help a Brother Out" (RDR2,
  chapter 4).
- Transcripts used word for word for every mission quote: "Bear One Another's Burdens/dialogues", "At Home with
  Dutch/dialogues", "For Purely Scientific Purposes/dialogues", "The Prodigal Son Returns (To Yale)/dialogues".
  Undead Nightmare lines: character page quote list and "Curious Tales from Blackwater" quotebox (no transcript).
- Newspapers: Blackwater Ledger & Sentinel No. 213 (1914; article list includes "Shocking Report Claims Cocaine Bad
  for Health"), fc/ireddead_Ledger_No213_text.txt.
- Other pages: "Liars and Cheats" (released September 21, 2010; MacDougal in the Damnation list), "Undead Nightmare".
- Real world: Liars and Cheats Pack detailed by Rockstar on August 27, 2010 and released on September 21, 2010 (as in
  allende_C, irish_C); RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 without multiplayer (as in
  irish_C); Wikipedia "Woolsey Hall" (fetched 22 Oct 2026: Yale's main auditorium, opened 1901 for the
  bicentennial), note in fc/web_notes_AC.txt.

VERIFIED POINTS: every quote below is checked against a transcript, except the Undead Nightmare lines (wiki quote
list, attributed). The mission order numbers come from the mission pages. Rewards come from the infoboxes.

EXCLUDED: the wiki's "MacDougal's boots" trivia (appearance, part B); "only mission in which MacDougal uses his gun"
(weapons, part B Skills); the Freudian ego/id remark (commentary); the buffalo-decline debate (real-world commentary
with no bearing on the character); the Mantegazza, Deloria and mad scientist readings, the "irony" and
"foreshadowing" of his Undead Nightmare death, and the Damnation category "due to his bigotry" (interpretations);
"a brilliant savage companion" (not in the transcript); the line about the fence shopkeeper mentioning him in "Help
a Brother Out" (character page only, contradicted by its own trivia, which speaks of a book on the shelf).

OWNERSHIP: lines likely quoted in part B "In his own words" are left out here on purpose ("The savage heart cannot
be conventionally civilized! I was right all along!", "It's my job to read too much into everything, dear boy.",
"I explore with the mind, Mr. Marston.", "I'm more of a planner than a man of action.", "cocaine can be a cruel
mistress", "I'll probably never sleep again", "It's a remarkable drug. It entirely restores the ego..."). Ross's
lines quoted in edgar_B ("Which should tell you something.", "Professor MacDougal has been a good friend to the
U.S. government...") and Dutch's lines quoted in dutch_C are not repeated. Narrative events are in part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
C4 = two("RDR2, chapter 4", "RDR2, chapitre 4")
UN = two("Undead Nightmare", "Undead Nightmare")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("MacDougal has a strand of three story missions in the third act of Red Dead Redemption, numbered 44 to 46 in the story order. It opens after Edgar Ross's \"Bear One Another's Burdens\", the first mission of the West Elizabeth part, and runs alongside Ross's own strand. The last of the three, \"The Prodigal Son Returns (To Yale)\", leads to Ross's \"And You Will Know the Truth\". He also opens a mission of the Undead Nightmare expansion.",
              "MacDougal propose une série de trois missions principales dans le troisième acte de Red Dead Redemption, numérotées de 44 à 46 dans l'ordre de l'histoire. Elle s'ouvre après \"Bear One Another's Burdens\", la mission d'Edgar Ross qui lance la partie West Elizabeth, et se déroule en parallèle de la série de Ross. La dernière des trois, \"The Prodigal Son Returns (To Yale)\", mène à \"And You Will Know the Truth\", une mission de Ross. Il ouvre aussi une mission de l'extension Undead Nightmare.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("MacDougal's role", "Rôle de MacDougal")], "rows": [
        M("Bear One Another's Burdens", A3,
          "Receives the wounded [[nastas|Nastas]] from Ross and Fordham at the end of the mission. Rewards: the High Power Pistol, 150 fame (200 with the Gold Medal) and 25 honor.",
          "Accueille [[nastas|Nastas]], blessé, que lui amènent Ross et Fordham à la fin de la mission. Récompenses : le High Power Pistol, 150 points de célébrité (200 avec la médaille d'or) et 25 d'honneur."),
        M("At Home with Dutch", A3,
          "Mission giver. Rides with John and Nastas towards Cochinay, turns back at the cliffs, then revives John in Blackwater. Rewards: the binoculars, 25 honor, 50 fame for the Gold Medal; the achievement \"A Savage Soul\".",
          "Donneur de mission. Chevauche avec John et Nastas vers Cochinay, rebrousse chemin au pied des falaises, puis ranime John à Blackwater. Récompenses : les jumelles, 25 points d'honneur, 50 de célébrité avec la médaille d'or ; le succès \"A Savage Soul\"."),
        M("For Purely Scientific Purposes", A3,
          "Mission giver. Goes to the meeting with Dutch's men at Bearclaw Camp, where Nastas is killed; John escorts him back to Blackwater. Rewards: 25 honor, 50 fame for the Gold Medal.",
          "Donneur de mission. Se rend au rendez-vous avec les hommes de Dutch à Bearclaw Camp, où Nastas est tué ; John le raccompagne à Blackwater. Récompenses : 25 points d'honneur, 50 de célébrité avec la médaille d'or."),
        M("The Prodigal Son Returns (To Yale)", A3,
          "Mission giver. Escapes the Blackwater Hotel over the rooftops with John and takes the train at Manzanita Post. Rewards: 100 dollars, 25 honor, 50 fame for the Gold Medal.",
          "Donneur de mission. Fuit l'hôtel de Blackwater par les toits avec John et prend le train à Manzanita Post. Récompenses : 100 dollars, 25 points d'honneur, 50 de célébrité avec la médaille d'or."),
        M("Curious Tales from Blackwater", UN,
          "Mission giver (non-canon). Met in deserted Blackwater, then devoured by an undead Nastas. Rewards: the torch and the Repeater Carbine; the achievement \"The Downward Spiral\".",
          "Donneur de mission (hors canon). Retrouvé dans Blackwater déserte, puis dévoré par Nastas devenu mort-vivant. Récompenses : la torche et la Repeater Carbine ; le succès \"The Downward Spiral\"."),
    ]}},
    {"h4": two("Mission in which he is mentioned", "Mission où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with MacDougal", "Lien avec MacDougal")], "rows": [
        M("Help a Brother Out", C4,
          "Not seen. According to the Red Dead Wiki, one of his books is a prop in the fence's shop (see Trivia).",
          "N'apparaît pas. D'après le Red Dead Wiki, l'un de ses livres sert d'accessoire dans la boutique du receleur (voir Anecdotes)."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the transcripts of the Red Dead Wiki. The Undead Nightmare lines come from the wiki's list of his lines, as no transcript exists for that mission.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Celles d'Undead Nightmare proviennent de la liste de ses répliques publiée par le wiki, faute de transcription pour cette mission.")},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("So, this is the office of an anthropologist named MacDougal. He was thrown out of Yale for degeneracy.", "So, this is the office of an anthropologist named MacDougal. He was thrown out of Yale for degeneracy."),
         "src": two("Archer Fordham, Bear One Another's Burdens (RDR1, Act III), on arriving in Blackwater",
                    "Archer Fordham, Bear One Another's Burdens (RDR1, acte III), à l'arrivée à Blackwater. Traduction : « Voilà le bureau d'un anthropologue du nom de MacDougal. Yale l'a mis à la porte pour dépravation. »")},
        {"q": two("They see him and they presume we're all idiot academics.", "They see him and they presume we're all idiot academics."),
         "src": two("Edgar Ross, Bear One Another's Burdens (RDR1, Act III), when Fordham says the professor helps them with the Native Americans",
                    "Edgar Ross, Bear One Another's Burdens (RDR1, acte III), quand Fordham explique que le professeur les aide avec les Amérindiens. Traduction : « En le voyant, ils s'imaginent qu'on est tous des universitaires idiots. »")},
        {"q": two("For a wise man, you are a very stupid man, mister.", "For a wise man, you are a very stupid man, mister."),
         "src": two("Nastas, At Home with Dutch (RDR1, Act III), after MacDougal's story about a Yale acquaintance",
                    "Nastas, At Home with Dutch (RDR1, acte III), après l'anecdote de MacDougal sur une connaissance de Yale. Traduction : « Pour un sage, vous êtes un homme bien bête, monsieur. »")},
        {"q": two("I think they are interested to find out what conclusions a white man was reached on hundreds of years of culture and society from the comfort of his hotel room.", "I think they are interested to find out what conclusions a white man was reached on hundreds of years of culture and society from the comfort of his hotel room."),
         "src": two("Nastas, For Purely Scientific Purposes (RDR1, Act III), when John asks why Dutch's men agreed to meet (transcript wording)",
                    "Nastas, For Purely Scientific Purposes (RDR1, acte III), quand John demande pourquoi les hommes de Dutch ont accepté le rendez-vous (texte de la transcription). Traduction : « Je crois qu'ils sont curieux de savoir à quelles conclusions un Blanc est arrivé sur des siècles de culture et de société, bien installé dans sa chambre d'hôtel. »")},
        {"q": two("Harold: Please, sir, what are you going to do? / Marston: I'm going to hand you over to them and watch them tear you limb from limb. / Harold: What? / Marston: I'm just kidding. We're going to run across the rooftops, get you back to your ivory tower.", "Harold: Please, sir, what are you going to do? / Marston: I'm going to hand you over to them and watch them tear you limb from limb. / Harold: What? / Marston: I'm just kidding. We're going to run across the rooftops, get you back to your ivory tower."),
         "src": two("The Prodigal Son Returns (To Yale) (RDR1, Act III), after Dutch's demand",
                    "The Prodigal Son Returns (To Yale) (RDR1, acte III), après la sommation de Dutch. Traduction : « Harold : Je vous en prie, monsieur, qu'allez-vous faire ? / Marston : Je vais vous livrer à eux et les regarder vous mettre en pièces. / Harold : Quoi ? / Marston : Je plaisante. On va filer par les toits et vous ramener dans votre tour d'ivoire. »")},
    ]},
    {"h4": two("Red Dead Redemption, Act III", "Red Dead Redemption, acte III")},
    {"quotes": [
        {"q": two("They're exactly the same! It's remarkable. It completely refutes my last book, but I'll tell you what, sir, this sabbatical in the field may have been somewhat forced upon me by circumstance, but my scholarship has benefitted enormously!", "They're exactly the same! It's remarkable. It completely refutes my last book, but I'll tell you what, sir, this sabbatical in the field may have been somewhat forced upon me by circumstance, but my scholarship has benefitted enormously!"),
         "src": two("At Home with Dutch (RDR1, Act III), on the blood samples",
                    "At Home with Dutch (RDR1, acte III), à propos des échantillons de sang. Traduction : « Ils sont exactement identiques ! C'est remarquable. Cela réfute entièrement mon dernier livre, mais je vais vous dire, monsieur : ce congé sabbatique sur le terrain m'a peut-être été quelque peu imposé par les circonstances, mais mes travaux en ont énormément profité ! »")},
        {"q": two("Kill him? Good God, no. What is it with your people out here? No, Van der Linde fascinates me. A white man living among natives. A civilized mind turned savage.", "Kill him? Good God, no. What is it with your people out here? No, Van der Linde fascinates me. A white man living among natives. A civilized mind turned savage."),
         "src": two("At Home with Dutch (RDR1, Act III), when John asks whether he too wants Dutch dead",
                    "At Home with Dutch (RDR1, acte III), quand John lui demande s'il veut, lui aussi, la mort de Dutch. Traduction : « Le tuer ? Grand Dieu, non. Qu'avez-vous donc tous, par ici ? Non, Van der Linde me fascine. Un Blanc qui vit parmi les indigènes. Un esprit civilisé devenu sauvage. »")},
        {"q": two("MacDougal: Look, Mr. Marston. Buffalo! What a noble beast! / ... / MacDougal: Who teaches you this nonsense? Extinction is a myth, refuted by Darwin. Species don't die, they evolve. Hunting, in time, will make the buffalo stronger.", "MacDougal: Look, Mr. Marston. Buffalo! What a noble beast! / ... / MacDougal: Who teaches you this nonsense? Extinction is a myth, refuted by Darwin. Species don't die, they evolve. Hunting, in time, will make the buffalo stronger."),
         "src": two("At Home with Dutch (RDR1, Act III), optional scene on the plains (only if the Manifest Destiny achievement is not unlocked)",
                    "At Home with Dutch (RDR1, acte III), scène facultative dans les plaines (seulement si le succès Manifest Destiny n'est pas débloqué). Traduction : « MacDougal : Regardez, monsieur Marston. Des bisons ! Quelle noble bête ! / ... / MacDougal : Qui vous apprend ces sottises ? L'extinction est un mythe, Darwin l'a réfuté. Les espèces ne meurent pas, elles évoluent. Avec le temps, la chasse rendra le bison plus fort. »")},
        {"q": two("Nastas has set up a meeting. A pow-wow, I think they call it. A meeting of minds! Of souls! Indians and whites, academics and criminals, coming together to find a common understanding!", "Nastas has set up a meeting. A pow-wow, I think they call it. A meeting of minds! Of souls! Indians and whites, academics and criminals, coming together to find a common understanding!"),
         "src": two("For Purely Scientific Purposes (RDR1, Act III), on the way to Bearclaw Camp",
                    "For Purely Scientific Purposes (RDR1, acte III), en route vers Bearclaw Camp. Traduction : « Nastas a organisé une rencontre. Un pow-wow, je crois que c'est ainsi qu'ils disent. Une rencontre des esprits ! Des âmes ! Indiens et Blancs, universitaires et criminels, réunis pour trouver un terrain d'entente ! »")},
        {"q": two("Well I guess this completes my research! Finished, done complete. Ship the book with one sentence: The Savage Mind Cannot Be Civilized.", "Well I guess this completes my research! Finished, done complete. Ship the book with one sentence: The Savage Mind Cannot Be Civilized."),
         "src": two("For Purely Scientific Purposes (RDR1, Act III), after the first ambush on the way back",
                    "For Purely Scientific Purposes (RDR1, acte III), après la première embuscade sur le chemin du retour. Traduction : « Eh bien, voilà qui conclut mes recherches ! Terminé, bouclé. Qu'on publie le livre en une seule phrase : l'esprit sauvage ne peut être civilisé. »")},
        {"q": two("Thank you, Mr Marston. I could be boiling in a pot right now, if it wasn't for you.", "Thank you, Mr Marston. I could be boiling in a pot right now, if it wasn't for you."),
         "src": two("For Purely Scientific Purposes (RDR1, Act III), outside his office",
                    "For Purely Scientific Purposes (RDR1, acte III), devant son bureau. Traduction : « Merci, monsieur Marston. Sans vous, je serais peut-être en train de bouillir dans une marmite. »")},
        {"q": two("Not having a bullet in your flipping neck, sir. I'm not cut out for this. No, not cut out for this at all.", "Not having a bullet in your flipping neck, sir. I'm not cut out for this. No, not cut out for this at all."),
         "src": two("The Prodigal Son Returns (To Yale) (RDR1, Act III), naming the thing without which scholarship cannot proceed",
                    "The Prodigal Son Returns (To Yale) (RDR1, acte III), sur la condition sans laquelle aucune recherche n'est possible. Traduction : « Ne pas avoir une fichue balle dans le cou, monsieur. Je ne suis pas fait pour ça. Non, pas fait pour ça du tout. »")},
        {"q": two("Not me, sir. I'm from Connecticut. I'm a professor at Yale! I write books! I do not deserve to die out here!", "Not me, sir. I'm from Connecticut. I'm a professor at Yale! I write books! I do not deserve to die out here!"),
         "src": two("The Prodigal Son Returns (To Yale) (RDR1, Act III), when John says they are all savages",
                    "The Prodigal Son Returns (To Yale) (RDR1, acte III), quand John estime qu'ils sont tous des sauvages. Traduction : « Pas moi, monsieur. Je suis du Connecticut. Je suis professeur à Yale ! J'écris des livres ! Je ne mérite pas de mourir ici ! »")},
        {"q": two("You know, I dreamt of documenting the last days of the Old West. The romance, the honor, the nobility! But it turns out it's just people killing each other.", "You know, I dreamt of documenting the last days of the Old West. The romance, the honor, the nobility! But it turns out it's just people killing each other."),
         "src": two("The Prodigal Son Returns (To Yale) (RDR1, Act III), on the ride to Manzanita Post",
                    "The Prodigal Son Returns (To Yale) (RDR1, acte III), sur la route de Manzanita Post. Traduction : « Vous savez, je rêvais de raconter les derniers jours du vieil Ouest. Le romanesque, l'honneur, la noblesse ! Mais en fin de compte, ce ne sont que des gens qui s'entretuent. »")},
        {"q": two("My research is complete; much as I thought, there's no civilizing this savage land.", "My research is complete; much as I thought, there's no civilizing this savage land."),
         "src": two("The Prodigal Son Returns (To Yale) (RDR1, Act III), at Manzanita Post station",
                    "The Prodigal Son Returns (To Yale) (RDR1, acte III), à la gare de Manzanita Post. Traduction : « Mes recherches sont terminées ; comme je le pensais, impossible de civiliser cette terre sauvage. »")},
        {"q": two("Ah, but they'll give me a prize in New Haven for this. Well, they bloody better. Well...goodbye, Mr. Marston. Best of luck, dear friend.", "Ah, but they'll give me a prize in New Haven for this. Well, they bloody better. Well...goodbye, Mr. Marston. Best of luck, dear friend."),
         "src": two("The Prodigal Son Returns (To Yale) (RDR1, Act III), his last words to John, at the station (he hugs John before the last sentence)",
                    "The Prodigal Son Returns (To Yale) (RDR1, acte III), ses derniers mots à John, sur le quai (il le serre dans ses bras avant la dernière phrase). Traduction : « Ah, mais on me remettra un prix à New Haven pour ça. Ils ont intérêt, bon sang. Bon... au revoir, monsieur Marston. Bonne chance, cher ami. »")},
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"quotes": [
        {"q": two("Well, sir, I'm a man of science, a man of great learning, a thinker, a wise man and I'll be honest with you, sir... I haven't got a fucking clue.", "Well, sir, I'm a man of science, a man of great learning, a thinker, a wise man and I'll be honest with you, sir... I haven't got a fucking clue."),
         "src": two("Curious Tales from Blackwater (Undead Nightmare), when John asks what is going on, according to the Red Dead Wiki",
                    "Curious Tales from Blackwater (Undead Nightmare), quand John lui demande ce qui se passe, d'après le Red Dead Wiki. Traduction : « Eh bien, monsieur, je suis un homme de science, un puits de savoir, un penseur, un sage, et je vais être franc avec vous, monsieur... je n'en ai pas la moindre putain d'idée. »")},
        {"q": two("Could you just wait a sec here, would you please? I'm going to wander down that lonely deserted street and get my bag.", "Could you just wait a sec here, would you please? I'm going to wander down that lonely deserted street and get my bag."),
         "src": two("Curious Tales from Blackwater (Undead Nightmare), to John, according to the Red Dead Wiki",
                    "Curious Tales from Blackwater (Undead Nightmare), à John, d'après le Red Dead Wiki. Traduction : « Vous voulez bien m'attendre une seconde ici, s'il vous plaît ? Je vais descendre cette rue déserte et récupérer ma sacoche. »")},
        {"q": two("Affirmative, a couple of minutes.", "Affirmative, a couple of minutes."),
         "src": two("Curious Tales from Blackwater (Undead Nightmare), his last words, according to the Red Dead Wiki",
                    "Curious Tales from Blackwater (Undead Nightmare), ses derniers mots, d'après le Red Dead Wiki. Traduction : « Affirmatif, deux minutes. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("The title \"The Prodigal Son Returns (To Yale)\" refers to the Parable of the Prodigal Son, told in the Gospel of Luke (15:11-32).",
            "Le titre \"The Prodigal Son Returns (To Yale)\" renvoie à la parabole du fils prodigue, rapportée dans l'Évangile selon Luc (15, 11-32)."),
        two("According to the mission page of \"The Prodigal Son Returns (To Yale)\", MacDougal can be seen packing a Bible into his bag. Later in the game, the same room belongs to Chu Fuk Choi, a stranger, according to the same page. MacDougal's briefcase stays in it; the Bible does not.",
            "D'après la page de mission de \"The Prodigal Son Returns (To Yale)\", on voit MacDougal glisser une Bible dans son sac. Selon la même page, Chu Fuk Choi, un inconnu du jeu, loge plus tard dans cette chambre. La mallette de MacDougal y est restée, mais pas la Bible."),
        two("In Red Dead Redemption 2, according to the Red Dead Wiki, a copy of \"The Scourge of Crossbreeding\" disguises the lever that opens the secret door of the bookcase in the Saint Denis fence's shop, during the stranger mission \"Help a Brother Out\" (chapter 4).",
            "Dans Red Dead Redemption 2, d'après le Red Dead Wiki, un exemplaire de \"The Scourge of Crossbreeding\" dissimule le levier qui ouvre la porte secrète de la bibliothèque, dans la boutique du receleur de Saint-Denis, pendant la mission d'inconnu \"Help a Brother Out\" (chapitre 4)."),
        two("Woolsey Hall, the building whose roof MacDougal climbs in the 1914 article, is a real building: according to Wikipedia, it is Yale's main auditorium, opened in 1901 for the university's bicentennial.",
            "Le Woolsey Hall, sur le toit duquel MacDougal grimpe dans l'article de 1914, existe réellement : d'après Wikipédia, c'est le principal auditorium de Yale, inauguré en 1901 pour le bicentenaire de l'université."),
        two("The 1914 issue that reports his expulsion from Yale also runs an article titled \"Shocking Report Claims Cocaine Bad for Health\".",
            "Le numéro de 1914 qui annonce son renvoi de Yale publie aussi un article intitulé \"Shocking Report Claims Cocaine Bad for Health\" (un rapport choc affirme que la cocaïne est mauvaise pour la santé)."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("MacDougal became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. Players select him in the Damnation section of the Outfitter, with [[abraham-reyes|Abraham Reyes]], [[agustin-allende|Agustin Allende]], [[bill-williamson|Bill Williamson]], [[dutch-van-der-linde|Dutch van der Linde]], [[edgar-ross|Edgar Ross]] and [[irish|Irish]]. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, do not include the multiplayer mode.",
              "MacDougal devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. On le choisit dans la section Damnation de l'Outfitter, aux côtés d'[[abraham-reyes|Abraham Reyes]], d'[[agustin-allende|Agustin Allende]], de [[bill-williamson|Bill Williamson]], de [[dutch-van-der-linde|Dutch van der Linde]], d'[[edgar-ross|Edgar Ross]] et d'[[irish|Irish]]. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, ne comprennent pas le multijoueur.")},
    {"h4": two("Undead Nightmare artwork", "Visuels d'Undead Nightmare")},
    {"p": two("According to the Red Dead Wiki, promotional artwork of an undead MacDougal was made for Undead Nightmare. He also appears on one of the expansion's loading screens: undead, beside the Blackwater Saloon, in pursuit of someone who stays out of frame.",
              "D'après le Red Dead Wiki, une illustration promotionnelle d'Undead Nightmare représente MacDougal en mort-vivant. L'un des écrans de chargement de l'extension le montre aussi sous cette forme, lancé à la poursuite d'une silhouette hors champ près du saloon de Blackwater.")},
]
