"""Abraham Reyes, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/, copies in
scripts/v3/work/reyes/fc/):
- Character page "Abraham Reyes" (Mission appearances, Quotes incl. the Multiplayer list, Trivia, Gallery captions)
  and FR page (Apparitions dans les missions, Anecdotes).
- Mission pages (infobox order numbers, givers, rewards, unlocks, trivia): "Must a Savior Die?" (35th), "Cowards Die
  Many Times" (36th), "The Great Mexican Train Robbery" (37th), "The Gates of El Presidio" (40th; achievement "Sons
  of Mexico"; replay and censorship trivia), "An Appointed Time" (41st; achievement "No More Fancy Words"; unlocks;
  stagecoach trivia), "A Civilized Man" (Undead Nightmare; trivia), "Civilization, at Any Price" (26th), "Father
  Abraham" (38th), "Mother Superior Blues".
- Transcripts used word for word for every mission quote: "Must a Savior Die?/dialogues", "Cowards Die Many
  Times/dialogues", "The Great Mexican Train Robbery/dialogues", "The Gates of El Presidio/dialogues", "An Appointed
  Time/dialogues", "Civilization, at Any Price/dialogues", "Mexican Caesar/dialogues", "The Demon Drink/dialogues",
  "My Sister's Keeper/dialogues", "Landon Ricketts Rides Again/dialogues", "Father Abraham/dialogues", "Captain De
  Santa's Downfall/dialogues". The "Politics" line and the multiplayer lines come from the wiki's quote list on the
  Reyes page; Herbert Moon's line from the quote list of the "Herbert Moon" page.
- Other pages: "Herbert Moon", "Casa Madrugada" (poster in the alley to the shooting gallery), "Escalera" and
  "Reyes' Rebels" (rebels replace the soldiers after "An Appointed Time"), "Drew MacFarlane" (same outfit), "The
  Gunslinger's Tragedy" (gallery caption linking Ricketts's line to Reyes), "Liars and Cheats" (released Tuesday,
  September 21, 2010; Damnation list), "Undead Nightmare" (antagonists list).
- Real world: Liars and Cheats Pack details published by Rockstar on August 27, 2010 and released on September 21,
  2010 (as in bill_C and edgar_C); RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 without multiplayer
  (as in uncle_C, landon_C, leigh_C).

VERIFIED POINTS: the wiki quote "Now find your weapons and let's fight these dogs!" reads "Now find your weapons and
fight these dogs!" in the transcript (not used); the wiki's personality quote "some peasant girl with a tight c*nt,
and the hands of a farmer" reads "some peasant girl with the hands of a farmer" in the transcript (not used here);
"Civilization, at Any Price" escorts a decoy train to draw the rebels out (transcript), Reyes is not seen; Victor's
cheer for Reyes in "Captain De Santa's Downfall" is in the branch where the rebels kill De Santa; the "Politics" line
has no transcript (attributed to the quote list).

EXCLUDED: the Mussolini parallel of the "energy" line and the Damnation category "most likely because he was a
hypocrite" (interpretation); the Madero, Villa, Zapata, Carranza and Bernardo Reyes comparisons and the Ciudad Juárez
and Cuautla parallels (real-world inspiration: part D); the meaning of "Reyes" (part B, Names); the Confederate belt
buckle, the green poncho absent in "An Appointed Time" and weapons (part B; the poncho trivia also gives a
speculative reason); "Laura" as another girl (told in part A); the admiration for Dutch (told in part A); the
glitches (game freeze after the speech, Reyes roaming in front of the palace, the Casa Madrugada animal glitch); the
cut bounty posters (part D, cut content); John's crying in "The Gates of El Presidio" (a Javier/John fact, not his).

OWNERSHIP: narrative events live in part A (one line per mission here). Newspapers are told in part A only. Quotes
picked here avoid the lines most likely used in part B "In his own words" (peasants, marriage, breeding, "one
woman", "inferior race", "delegate", "energy", "Laura's Day"); if part B uses a line given here, the fixer removes
it from one place. The lines of Luisa and De Santa below should not be repeated in their part B relationship entries.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")
UNM = two("Undead Nightmare", "Undead Nightmare")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Reyes appears in five story missions of Red Dead Redemption, all in the second act, set in Nuevo Paraíso. He gives three of them himself, from his base at Agave Viejo or in Escalera. The first two belong to the strands of [[luisa-fortuna|Luisa Fortuna]] and [[vincente-de-santa|Vincente de Santa]]. \"Cowards Die Many Times\" unlocks his own strand, and \"An Appointed Time\", the last mission of the act, opens West Elizabeth and the strand of [[edgar-ross|Edgar Ross]]. In Undead Nightmare, he is the target of the final mission.",
              "Reyes apparaît dans cinq missions principales de Red Dead Redemption, toutes dans le deuxième acte, au Nuevo Paraíso. Il en confie trois lui-même, depuis sa base d'Agave Viejo ou à Escalera. Les deux premières appartiennent aux séries de [[luisa-fortuna|Luisa Fortuna]] et de [[vincente-de-santa|Vincente de Santa]]. \"Cowards Die Many Times\" débloque sa propre série, et \"An Appointed Time\", dernière mission de l'acte, ouvre West Elizabeth et la série d'[[edgar-ross|Edgar Ross]]. Dans Undead Nightmare, il est la cible de la dernière mission.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Reyes's role", "Rôle de Reyes")], "rows": [
        M("Must a Savior Die?", A2,
          "Prisoner of the army at El Presidio; John saves him from the firing squad at Luisa's request. 35th mission, given by Luisa. Rewards: 50 honor and 200 fame; unlocks the stranger mission \"Aztec Gold\".",
          "Prisonnier de l'armée à El Presidio ; John le sauve du peloton d'exécution à la demande de Luisa. 35e mission, confiée par Luisa. Récompenses : 50 points d'honneur et 200 de célébrité ; débloque la mission d'inconnu \"Aztec Gold\"."),
        M("Cowards Die Many Times", A2,
          "Leads the rebel attack on Chuparosa, saves John from execution and cuts his ropes, then gives a victory speech. 36th mission, given by De Santa. Rewards: up to 75 dollars from De Santa's shooting contest, 50 honor and 250 fame; unlocks the Reyes strand.",
          "Mène l'attaque rebelle sur Chuparosa, sauve John de l'exécution et tranche ses liens, puis prononce un discours de victoire. 36e mission, confiée par De Santa. Récompenses : jusqu'à 75 dollars au concours de tir de De Santa, 50 points d'honneur et 250 de célébrité ; débloque la série de Reyes."),
        M("The Great Mexican Train Robbery", A2,
          "Mission giver. Creates the distraction at the Chuparosa station and lets John take the contents of the army train's safe. 37th mission. Rewards: 200 dollars, a Double-action Revolver (or revolver ammunition), a Pardon Letter, 125 honor and 150 fame; Throwing Knives go on sale.",
          "Donneur de mission. Fait diversion à la gare de Chuparosa et laisse à John le contenu du coffre du train de l'armée. 37e mission. Récompenses : 200 dollars, un Double-action Revolver (ou des munitions de revolver), une lettre de grâce, 125 points d'honneur et 150 de célébrité ; les couteaux de lancer sont mis en vente."),
        M("The Gates of El Presidio", A2,
          "Mission giver. Lights the fuse of the TNT wagon, leads the rebels into El Presidio and sends John after Javier Escuella. 40th mission. Rewards: 125 honor and 300 fame; achievement \"Sons of Mexico\".",
          "Donneur de mission. Allume la mèche du chariot de TNT, mène les rebelles dans El Presidio et envoie John à la poursuite de Javier Escuella. 40e mission. Récompenses : 125 points d'honneur et 300 de célébrité ; succès \"Sons of Mexico\"."),
        M("An Appointed Time", A2,
          "Mission giver. Freed by John in Escalera, leads the assault on Allende's villa, chases the stagecoach and shoots whichever of Allende and Bill John spares. 41st mission, last of the act. Rewards: up to 535 honor and 300 fame, access to West Elizabeth; achievement \"No More Fancy Words\".",
          "Donneur de mission. Libéré par John à Escalera, mène l'assaut contre la villa d'Allende, poursuit la diligence et abat celui des deux, Allende ou Bill, que John épargne. 41e mission, la dernière de l'acte. Récompenses : jusqu'à 535 points d'honneur et 300 de célébrité, accès à West Elizabeth ; succès \"No More Fancy Words\"."),
        M("A Civilized Man", UNM,
          "Final mission of the expansion. The undead Reyes attacks John in the Escalera mansion and must be killed before John returns the mask.",
          "Dernière mission de l'extension. Le Reyes mort-vivant attaque John dans la demeure d'Escalera et doit être abattu avant que John ne rapporte le masque."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Link with Reyes", "Lien avec Reyes")], "rows": [
        M("The Gunslinger's Tragedy", A2,
          "[[landon-ricketts|Landon Ricketts]] tells John that another local man is promising the peasants their freedom. He gives no name; the Red Dead Wiki identifies the man as Reyes.",
          "[[landon-ricketts|Landon Ricketts]] raconte à John qu'un autre homme du pays promet la liberté aux paysans. Il ne donne aucun nom ; le Red Dead Wiki y voit Reyes."),
        M("Civilization, at Any Price", A2,
          "De Santa tells John that the outlaws he seeks may be hiding with rebels united under Reyes, insults him at length (see Quotes) and escorts a decoy train to draw the rebels out. 26th mission.",
          "De Santa explique à John que les hors-la-loi qu'il cherche se cachent peut-être chez les rebelles réunis derrière Reyes, l'insulte longuement (voir Citations) et escorte un train-leurre pour attirer les rebelles. 26e mission."),
        M("The Demon Drink", A2,
          "De Santa introduces John to Allende as the man who helped them defeat Reyes.",
          "De Santa présente John à Allende comme l'homme qui les a aidés à battre Reyes."),
        M("Mexican Caesar", A2,
          "Allende says he has heard that Bill and Javier ride with Reyes. Captain Espinoza accuses Reyes of luring Americans with promises (see Quotes).",
          "Allende affirme avoir entendu dire que Bill et Javier chevauchent avec Reyes. Le capitaine Espinoza accuse Reyes d'attirer les Américains à coups de promesses (voir Citations)."),
        M("My Sister's Keeper", A2,
          "Luisa tells John that with Reyes anything is possible.",
          "Luisa assure à John qu'avec Reyes, tout est possible."),
        M("Landon Ricketts Rides Again", A2,
          "Ricketts explains that the army holds Luisa because she is a rebel close to Reyes.",
          "Ricketts explique que l'armée détient Luisa parce qu'elle est une rebelle proche de Reyes."),
        M("Father Abraham", A2,
          "Luisa says Reyes asked personally that John stop Allende's reinforcements before they reach Escalera, and that he wants the convoy destroyed to send a message. 38th mission.",
          "Luisa explique que Reyes a demandé en personne que John arrête les renforts d'Allende avant Escalera, et qu'il veut voir le convoi détruit pour faire passer un message. 38e mission."),
        M("Captain De Santa's Downfall", A2,
          "If the rebels shoot De Santa, Victor Melendez cheers for Reyes. Reyes comments on De Santa's death in the next mission.",
          "Si les rebelles abattent De Santa, Victor Melendez acclame Reyes. Reyes commente la mort de De Santa dans la mission suivante."),
        M("Mother Superior Blues", UNM,
          "The Mother Superior of Las Hermanas sends John to find Reyes in the presidential mansion in Escalera.",
          "La mère supérieure de Las Hermanas envoie John chercher Reyes dans la demeure présidentielle d'Escalera."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the mission transcripts of the Red Dead Wiki. The other lines come from the wiki's quote lists, as no transcript exists for them.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Les autres proviennent des listes de citations du wiki, faute de transcription.")},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("Abraham Reyes? He is a traitor, a liar, a coward and a sinner. A hero who has done nothing. I have more respect for the shit I took this morning than I ever will for that pathetic worm.", "Abraham Reyes? He is a traitor, a liar, a coward and a sinner. A hero who has done nothing. I have more respect for the shit I took this morning than I ever will for that pathetic worm."),
         "src": two("Vincente de Santa, Civilization, at Any Price (RDR1, Act II), when John asks who the rebel leader is",
                    "Vincente de Santa, Civilization, at Any Price (RDR1, acte II), quand John lui demande qui est le chef des rebelles. Traduction : « Abraham Reyes ? C'est un traître, un menteur, un lâche et un pécheur. Un héros qui n'a rien fait. J'ai plus de respect pour la merde que j'ai posée ce matin que je n'en aurai jamais pour ce misérable ver de terre. »")},
        {"q": two("Reyes is a coward, blinded by love for himself. All he does is write poems and songs about winning battles he never fought in.", "Reyes is a coward, blinded by love for himself. All he does is write poems and songs about winning battles he never fought in."),
         "src": two("Vincente de Santa, Cowards Die Many Times (RDR1, Act II), after John says that Reyes rides with his men",
                    "Vincente de Santa, Cowards Die Many Times (RDR1, acte II), après que John a fait remarquer que Reyes chevauche avec ses hommes. Traduction : « Reyes est un lâche, aveuglé par l'amour de lui-même. Il ne fait qu'écrire des poèmes et des chansons sur des batailles qu'il a gagnées sans jamais y prendre part. »")},
        {"q": two("Abraham Reyes is trying hard to recruit gringos to fight for him. His propaganda is everywhere. He promises women, gold. And, of course, you come.", "Abraham Reyes is trying hard to recruit gringos to fight for him. His propaganda is everywhere. He promises women, gold. And, of course, you come."),
         "src": two("Captain Espinoza, Mexican Caesar (RDR1, Act II)",
                    "Le capitaine Espinoza, Mexican Caesar (RDR1, acte II). Traduction : « Abraham Reyes fait tout pour recruter des gringos qui se battent pour lui. Sa propagande est partout. Il promet des femmes, de l'or. Et, bien sûr, vous accourez. »")},
        {"q": two("You know, in our hearts, we are married already, but his family does not approve. How could they, when I am little more than a peasant girl? But that's what makes Abraham Reyes the man he is.", "You know, in our hearts, we are married already, but his family does not approve. How could they, when I am little more than a peasant girl? But that's what makes Abraham Reyes the man he is."),
         "src": two("Luisa Fortuna, Must a Savior Die? (RDR1, Act II), after his capture",
                    "Luisa Fortuna, Must a Savior Die? (RDR1, acte II), après sa capture. Traduction : « Vous savez, dans nos cœurs, nous sommes déjà mariés, mais sa famille n'approuve pas. Comment le pourrait-elle, alors que je ne suis guère plus qu'une paysanne ? Mais c'est justement ce qui fait d'Abraham Reyes l'homme qu'il est. »")},
        {"q": two("Reyes is as revolutionary as Napoleon! He just likes riding horses in a fancy uniform.", "Reyes is as revolutionary as Napoleon! He just likes riding horses in a fancy uniform."),
         "src": two("Herbert Moon, the Armadillo shopkeeper, in free roam (quote list of the wiki's Herbert Moon page)",
                    "Herbert Moon, l'épicier d'Armadillo, en exploration libre (liste de citations de la page Herbert Moon du wiki). Traduction : « Reyes est aussi révolutionnaire que Napoléon ! Il aime juste monter à cheval en uniforme de parade. »")},
    ]},
    {"h4": two("Red Dead Redemption, Act II", "Red Dead Redemption, acte II")},
    {"quotes": [
        {"q": two("Abraham: I am free again! I will write a poem about this day! / Marston: This is from a man who was tied to a post with a gun in his face a few minutes ago. / Abraham: I wish I could see Allende's face when he finds out I have defeated a hundred of his men! / Marston: All you done is get on the back of this horse, my friend.", "Abraham: I am free again! I will write a poem about this day! / Marston: This is from a man who was tied to a post with a gun in his face a few minutes ago. / Abraham: I wish I could see Allende's face when he finds out I have defeated a hundred of his men! / Marston: All you done is get on the back of this horse, my friend."),
         "src": two("Must a Savior Die? (RDR1, Act II), riding out of El Presidio behind John",
                    "Must a Savior Die? (RDR1, acte II), en quittant El Presidio en croupe derrière John. Traduction : « Abraham : Je suis libre ! J'écrirai un poème sur ce jour ! / Marston : Dit l'homme qui était attaché à un poteau, un fusil braqué sur lui, il y a quelques minutes. / Abraham : J'aimerais voir la tête d'Allende quand il apprendra que j'ai vaincu cent de ses hommes ! / Marston : Tout ce que t'as fait, c'est grimper à l'arrière de ce cheval, mon ami. »")},
        {"q": two("Abraham: It is lucky for you, I arrived when I did. / Marston: I guess we're even then. / Abraham: Now find your weapons and fight these dogs!", "Abraham: It is lucky for you, I arrived when I did. / Marston: I guess we're even then. / Abraham: Now find your weapons and fight these dogs!"),
         "src": two("Cowards Die Many Times (RDR1, Act II), after cutting John's ropes in Chuparosa",
                    "Cowards Die Many Times (RDR1, acte II), après avoir tranché les liens de John à Chuparosa. Traduction : « Abraham : Tu as de la chance que je sois arrivé à temps. / Marston : On est quittes, alors. / Abraham : Maintenant, trouve tes armes et combats ces chiens ! »")},
        {"q": two("Soon, we shall be free! Living together in a noble republic, justly ruled by fine men. But, but, but... El trabajo, the job, is not done... our struggle is not over!", "Soon, we shall be free! Living together in a noble republic, justly ruled by fine men. But, but, but... El trabajo, the job, is not done... our struggle is not over!"),
         "src": two("Cowards Die Many Times (RDR1, Act II), speech to the rebels in Chuparosa",
                    "Cowards Die Many Times (RDR1, acte II), discours aux rebelles à Chuparosa. Traduction : « Bientôt, nous serons libres ! Nous vivrons ensemble dans une noble république, gouvernée avec justice par des hommes de valeur. Mais, mais, mais... El trabajo, le travail n'est pas fini... notre lutte n'est pas terminée ! »")},
        {"q": two("Abraham: Sarcasm, my friend...should be beneath a man such as you. Don't you think? / Marston: Very little is beneath a man such as me.", "Abraham: Sarcasm, my friend...should be beneath a man such as you. Don't you think? / Marston: Very little is beneath a man such as me."),
         "src": two("The Great Mexican Train Robbery (RDR1, Act II), at Agave Viejo",
                    "The Great Mexican Train Robbery (RDR1, acte II), à Agave Viejo. Traduction : « Abraham : Le sarcasme, mon ami... devrait être indigne d'un homme tel que toi. Tu ne crois pas ? / Marston : Bien peu de choses sont indignes d'un homme tel que moi. »")},
        {"q": two("Abraham: Now that we are friends, I hope you will give me some warning if you get the sudden urge to kill me. / Marston: You'll be the first to know when I kill you, I promise.", "Abraham: Now that we are friends, I hope you will give me some warning if you get the sudden urge to kill me. / Marston: You'll be the first to know when I kill you, I promise."),
         "src": two("The Great Mexican Train Robbery (RDR1, Act II), on the ride to Chuparosa",
                    "The Great Mexican Train Robbery (RDR1, acte II), sur la route de Chuparosa. Traduction : « Abraham : Maintenant que nous sommes amis, j'espère que tu me préviendras si l'envie te prend soudain de me tuer. / Marston : Tu seras le premier informé quand je te tuerai, promis. »")},
        {"q": two("Abraham: In a country where most people cannot read the newspaper, song is a powerful means of communication. We do what we can to battle the lies and propaganda of the government. / Marston: I know. I've seen your posters.", "Abraham: In a country where most people cannot read the newspaper, song is a powerful means of communication. We do what we can to battle the lies and propaganda of the government. / Marston: I know. I've seen your posters."),
         "src": two("The Great Mexican Train Robbery (RDR1, Act II), about the corridos written about him",
                    "The Great Mexican Train Robbery (RDR1, acte II), au sujet des corridos écrits sur lui. Traduction : « Abraham : Dans un pays où la plupart des gens ne savent pas lire le journal, la chanson est un puissant moyen de communication. Nous faisons ce que nous pouvons pour combattre les mensonges et la propagande du gouvernement. / Marston : Je sais. J'ai vu tes affiches. »")},
        {"q": two("Abraham: In the capital, they are already talking about my legendary escape from El Presidio. How I fought off a thousand Mexican soldiers with my bare hands! / Marston: Finally the people have the truth.", "Abraham: In the capital, they are already talking about my legendary escape from El Presidio. How I fought off a thousand Mexican soldiers with my bare hands! / Marston: Finally the people have the truth."),
         "src": two("The Great Mexican Train Robbery (RDR1, Act II)",
                    "The Great Mexican Train Robbery (RDR1, acte II). Traduction : « Abraham : À Mexico, on parle déjà de ma légendaire évasion d'El Presidio. Comment j'ai repoussé mille soldats mexicains à mains nues ! / Marston : Enfin, le peuple connaît la vérité. »")},
        {"q": two("Marston: Escuella was always a torn man. A cynic who desperately wanted to be a romantic. / Abraham: Whereas you, John, are a romantic who wants to be a cynic.", "Marston: Escuella was always a torn man. A cynic who desperately wanted to be a romantic. / Abraham: Whereas you, John, are a romantic who wants to be a cynic."),
         "src": two("The Gates of El Presidio (RDR1, Act II), on the wagon ride",
                    "The Gates of El Presidio (RDR1, acte II), sur le chariot. Traduction : « Marston : Escuella a toujours été un homme déchiré. Un cynique qui rêvait désespérément d'être un romantique. / Abraham : Alors que toi, John, tu es un romantique qui voudrait être un cynique. »")},
        {"q": two("Abraham: Have you ever known power, John? / Marston: I'm a semi-literate farmer and hired killer. I ain't in the power game.", "Abraham: Have you ever known power, John? / Marston: I'm a semi-literate farmer and hired killer. I ain't in the power game."),
         "src": two("The Gates of El Presidio (RDR1, Act II), on the wagon ride",
                    "The Gates of El Presidio (RDR1, acte II), sur le chariot. Traduction : « Abraham : As-tu déjà connu le pouvoir, John ? / Marston : Je suis un fermier qui sait à peine lire et un tueur à gages. Le pouvoir, très peu pour moi. »")},
        {"q": two("Allow me some silence on the journey. I have the weight of a nation on my shoulders.", "Allow me some silence on the journey. I have the weight of a nation on my shoulders."),
         "src": two("The Gates of El Presidio (RDR1, Act II), as they near the fort",
                    "The Gates of El Presidio (RDR1, acte II), à l'approche du fort. Traduction : « Laisse-moi un peu de silence pendant le trajet. Je porte le poids d'une nation sur mes épaules. »")},
        {"q": two("Marston: That sounds crazy! How long is the fuse? / Abraham: Yes. Like I say, fun times. It's plenty long enough I think? I'll see you in there, amigo.", "Marston: That sounds crazy! How long is the fuse? / Abraham: Yes. Like I say, fun times. It's plenty long enough I think? I'll see you in there, amigo."),
         "src": two("The Gates of El Presidio (RDR1, Act II), lighting the fuse of the TNT wagon",
                    "The Gates of El Presidio (RDR1, acte II), en allumant la mèche du chariot de TNT. Traduction : « Marston : C'est de la folie ! Elle fait quelle longueur, la mèche ? / Abraham : Oui. Comme je disais, on va s'amuser. Elle est bien assez longue, je crois ? On se retrouve à l'intérieur, amigo. »")},
        {"q": two("Two old friends reunited. It is a beautiful thing.", "Two old friends reunited. It is a beautiful thing."),
         "src": two("The Gates of El Presidio (RDR1, Act II), as John carries Javier Escuella out, alive or dead",
                    "The Gates of El Presidio (RDR1, acte II), quand John emmène Javier Escuella, vivant ou mort. Traduction : « Deux vieux amis réunis. C'est une belle chose. »")},
        {"q": two("Welcome to México. My brothers and I are just discussing the future of our country!", "Welcome to México. My brothers and I are just discussing the future of our country!"),
         "src": two("An Appointed Time (RDR1, Act II), to John, while Zubieta's men beat him in Escalera",
                    "An Appointed Time (RDR1, acte II), à John, pendant que les hommes de Zubieta le rouent de coups à Escalera. Traduction : « Bienvenue au Mexique. Mes frères et moi discutions justement de l'avenir de notre pays ! »")},
        {"q": two("Abraham: Allende is dead...Mexico is mine! My people are free, and it is all thanks to you, John. / Marston: And to the people who laid down their lives. People like Luisa.", "Abraham: Allende is dead...Mexico is mine! My people are free, and it is all thanks to you, John. / Marston: And to the people who laid down their lives. People like Luisa."),
         "src": two("An Appointed Time (RDR1, Act II), on the road outside Escalera",
                    "An Appointed Time (RDR1, acte II), sur la route à la sortie d'Escalera. Traduction : « Abraham : Allende est mort... Le Mexique est à moi ! Mon peuple est libre, et c'est grâce à toi, John. / Marston : Et à ceux qui ont donné leur vie. Des gens comme Luisa. »")},
        {"q": two("Abraham: Well, I must say I will miss you, John Marston. / Marston: I doubt you'll even remember me, Abraham, but it's been an experience. Good luck with the revolution. If you win power, remember why you wanted it.", "Abraham: Well, I must say I will miss you, John Marston. / Marston: I doubt you'll even remember me, Abraham, but it's been an experience. Good luck with the revolution. If you win power, remember why you wanted it."),
         "src": two("An Appointed Time (RDR1, Act II), their farewell",
                    "An Appointed Time (RDR1, acte II), leurs adieux. Traduction : « Abraham : Eh bien, je dois dire que tu vas me manquer, John Marston. / Marston : Je doute que tu te souviennes seulement de moi, Abraham, mais ça a été une expérience. Bonne chance pour la révolution. Si tu prends le pouvoir, rappelle-toi pourquoi tu le voulais. »")},
    ]},
    {"h4": two("Other lines", "Autres répliques")},
    {"quotes": [
        {"q": two("Politics, my friend, is for fools. That's why it plays such an important role in this country.", "Politics, my friend, is for fools. That's why it plays such an important role in this country."),
         "src": two("Red Dead Redemption (quote list of the wiki, no mission given)",
                    "Red Dead Redemption (liste de citations du wiki, sans mission précisée). Traduction : « La politique, mon ami, c'est pour les imbéciles. C'est pour cela qu'elle joue un si grand rôle dans ce pays. »")},
    ]},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"quotes": [
        {"q": two("They will write about these days.", "They will write about these days."),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « On écrira sur ces jours-ci. »")},
        {"q": two("Look at all those men and women... They would all die for me!", "Look at all those men and women... They would all die for me!"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki)",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki). Traduction : « Regarde tous ces hommes et ces femmes... Ils mourraient tous pour moi ! »")},
        {"q": two("Soy el libertador de México.", "Soy el libertador de México."),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"I'm the liberator of Mexico.\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Je suis le libérateur du Mexique. »")},
        {"q": two("Nadie puede matar a Abraham Reyes.", "Nadie puede matar a Abraham Reyes."),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"No one can kill Abraham Reyes.\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Personne ne peut tuer Abraham Reyes. »")},
        {"q": two("La Revolución es imparable.", "La Revolución es imparable."),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"The revolution is unstoppable.\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « La révolution est imparable. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("According to the Red Dead Wiki, the opening of \"The Gates of El Presidio\" is the only sex scene shown on screen in Red Dead Redemption. According to the mission page, the Game of the Year Edition covered the woman's breasts with clothing, a change reverted in later versions of the game.",
            "D'après le Red Dead Wiki, l'ouverture de \"The Gates of El Presidio\" est la seule scène de sexe montrée à l'écran dans Red Dead Redemption. D'après la page de la mission, l'édition Game of the Year couvrait la poitrine de la femme, une censure annulée dans les versions ultérieures du jeu."),
        two("When \"The Gates of El Presidio\" is replayed, Reyes always speaks as if the rebels, not John, had killed De Santa, according to the mission page.",
            "Quand on rejoue \"The Gates of El Presidio\", Reyes parle toujours comme si les rebelles, et non John, avaient tué De Santa, d'après la page de la mission."),
        two("According to the mission pages, \"Must a Savior Die?\" and \"The Great Mexican Train Robbery\" are the only two missions in which Reyes does not fight. In the first, hitting Reyes with the horse while picking him up fails the mission for being too aggressive.",
            "D'après les pages des missions, \"Must a Savior Die?\" et \"The Great Mexican Train Robbery\" sont les deux seules missions où Reyes ne se bat pas. Dans la première, heurter Reyes avec le cheval en venant le chercher fait échouer la mission, jugée trop brutale."),
        two("According to the mission page of \"The Great Mexican Train Robbery\", if John fires his gun inside the armored car, Reyes asks him whether he is shooting at imaginary soldiers.",
            "D'après la page de la mission \"The Great Mexican Train Robbery\", si John tire à l'intérieur du wagon blindé, Reyes lui demande s'il vise des soldats imaginaires."),
        two("According to the mission page of \"An Appointed Time\", Reyes keeps firing at the stagecoach if John ties up its drivers instead of killing them. If John lassoes Bill while Allende holds him, Reyes shoots both men, which can block the mission. In rare cases, when John shoots Bill, Allende begs, runs into the brush and is shot in the back by Reyes outside of any cutscene.",
            "D'après la page de la mission \"An Appointed Time\", Reyes continue de tirer sur la diligence si John ligote ses cochers au lieu de les tuer. Si John prend Bill au lasso pendant qu'Allende le tient, Reyes abat les deux hommes, ce qui peut bloquer la mission. Il arrive aussi, quand John abat Bill, qu'Allende supplie, s'enfuie dans les broussailles et que Reyes l'abatte d'une balle dans le dos, hors de toute cinématique."),
        two("After \"An Appointed Time\", Reyes's rebels replace the army as the armed force of Escalera and most of Nuevo Paraíso, and the last scrap of the Reyes' Rebels outfit goes on sale at the Escalera general store.",
            "Après \"An Appointed Time\", les rebelles de Reyes remplacent l'armée comme force armée d'Escalera et de la plus grande partie du Nuevo Paraíso, et la dernière pièce de la tenue des rebelles de Reyes est mise en vente au magasin général d'Escalera."),
        two("According to the Red Dead Wiki, posters of Reyes can be found in Casa Madrugada (in the alley leading to the shooting gallery), three in Escalera, one in Tesoro Azul, and, north of the border, at Solomon's Folly, at Benedict Point and on the assay office in Tumbleweed.",
            "D'après le Red Dead Wiki, on trouve des affiches de Reyes à Casa Madrugada (dans la ruelle qui mène au stand de tir), trois à Escalera, une à Tesoro Azul et, au nord de la frontière, à Solomon's Folly, à Benedict Point et sur le bureau d'essai des métaux de Tumbleweed."),
        two("According to the Red Dead Wiki, Drew MacFarlane sometimes wears the same outfit as Reyes in \"Must a Savior Die?\" and \"An Appointed Time\".",
            "D'après le Red Dead Wiki, Drew MacFarlane porte parfois la même tenue que Reyes dans \"Must a Savior Die?\" et \"An Appointed Time\"."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"ul": [
        two("According to the Red Dead Wiki, the undead Reyes is the thinnest of all the Bruisers in the game. He is also the only undead with two sets of sounds: he groans like the ordinary undead while idle, and roars like the Bruisers when he charges.",
            "D'après le Red Dead Wiki, le Reyes mort-vivant est le plus maigre de tous les Bruisers du jeu. C'est aussi le seul mort-vivant doté de deux jeux de sons : au repos, il grogne comme les morts-vivants ordinaires, et il rugit comme les Bruisers quand il charge."),
        two("According to the mission page of \"A Civilized Man\", the undead Reyes's body cannot be searched: after the cutscene that follows his death it stays inside the mansion, whose doors are locked until the mission is over. In the catacombs, John picks up a Semi-auto Shotgun and remarks that Reyes brought protection.",
            "D'après la page de la mission \"A Civilized Man\", on ne peut pas fouiller le corps du Reyes mort-vivant : après la cinématique qui suit sa mort, il reste dans la demeure, dont les portes sont verrouillées jusqu'à la fin de la mission. Dans les catacombes, John ramasse un fusil Semi-auto Shotgun et remarque que Reyes avait apporté de quoi se protéger."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Reyes became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. Players select him in the Damnation section of the Outfitter, with [[agustin-allende|Agustin Allende]], [[bill-williamson|Bill Williamson]], [[dutch-van-der-linde|Dutch van der Linde]], [[edgar-ross|Edgar Ross]], [[harold-macdougal|Harold MacDougal]] and [[irish|Irish]]. According to the Red Dead Wiki, he sometimes speaks of himself in the third person in multiplayer, and many of his lines are in Spanish (see Quotes). The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the Reyes model is not available in them.",
              "Reyes devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. On le choisit dans la section Damnation de l'Outfitter, aux côtés d'[[agustin-allende|Agustin Allende]], de [[bill-williamson|Bill Williamson]], de [[dutch-van-der-linde|Dutch van der Linde]], d'[[edgar-ross|Edgar Ross]], d'[[harold-macdougal|Harold MacDougal]] et d'[[irish|Irish]]. D'après le Red Dead Wiki, il lui arrive de parler de lui à la troisième personne en multijoueur, et une bonne partie de ses répliques sont en espagnol (voir Citations). Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle de Reyes n'y est donc pas disponible.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Reyes for Red Dead Redemption, and pre-release screenshots that show him, one of them with John. According to the Red Dead Wiki, his goatee and hair are slightly shorter in these screenshots than in the final game. Reyes does not appear in Red Dead Redemption 2 or in Red Dead Online, which are set before 1911; the Red Dead Wiki lists him only in Red Dead Redemption and Undead Nightmare.",
              "Rockstar a diffusé une illustration officielle de Reyes pour Red Dead Redemption, ainsi que des captures d'avant la sortie où il apparaît, dont l'une avec John. D'après le Red Dead Wiki, son bouc et ses cheveux y sont un peu plus courts que dans le jeu final. Reyes n'apparaît ni dans Red Dead Redemption 2 ni dans Red Dead Online, qui se déroulent avant 1911 ; le Red Dead Wiki ne le recense que dans Red Dead Redemption et Undead Nightmare.")},
]
