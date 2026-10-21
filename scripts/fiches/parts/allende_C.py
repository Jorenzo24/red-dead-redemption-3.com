"""Agustin Allende, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/; copies in
scripts/v3/work/allende/fc/):
- Character page "Agustin Allende" (Mission appearances, Quotes incl. the Multiplayer list, Trivia, Gallery captions)
  and FR page (Apparitions dans les missions, Anecdotes).
- Mission pages (infobox order numbers, givers, rewards, unlocks, achievements, trivia): "The Demon Drink" (27th),
  "Mexican Caesar" (29th; Allende vomits; villa gates locked until "An Appointed Time"; non-payment), "Cowards Die Many
  Times" (36th), "An Appointed Time" (41st; achievement "No More Fancy Words"; corpse, lasso, rare brush escape, random
  encounter, 1914 gates), "We Shall Be Together in Paradise" (25th, last mission of New Austin), "Civilization, at Any
  Price" (26th), "Empty Promises" (28th), "The Gunslinger's Tragedy" (30th), "Landon Ricketts Rides Again" (31st), "The
  Mexican Wagon Train" (33rd), "Must a Savior Die?" (35th), "The Great Mexican Train Robbery" (37th), "Father Abraham"
  (38th), "Captain De Santa's Downfall" (39th), "The Gates of El Presidio" (40th).
- Transcripts used word for word for every mission quote: "The Demon Drink/dialogues", "Mexican Caesar/dialogues",
  "Cowards Die Many Times/dialogues", "An Appointed Time/dialogues", "Civilization, at Any Price/dialogues", "The
  Gunslinger's Tragedy/dialogues", "The Mexican Wagon Train/dialogues", "Father Abraham/dialogues", "The Great Mexican
  Train Robbery/dialogues", "The Gates of El Presidio/dialogues", "Captain De Santa's Downfall/dialogues", "We Shall Be
  Together in Paradise/dialogues". The multiplayer lines (and their English translations) come from the quote list of
  the Allende page; Herbert Moon's lines from the quote list of the "Herbert Moon" page.
- Other pages: "Escalera" (gates closed after "The Gates of El Presidio"), "Ignacio Sanchez" (rebel propaganda posters
  in Nosalida, gallery captions), "Undead Nightmare" (Reyes moved into Allende's mansion), "Liars and Cheats"
  (released Tuesday, September 21, 2010; Damnation list), "Herbert Moon".
- Real world: Liars and Cheats Pack details published by Rockstar on August 27, 2010 and released on September 21,
  2010 (as in reyes_C, bill_C and edgar_C); RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 without
  multiplayer (as in reyes_C, uncle_C, landon_C, leigh_C).

VERIFIED POINTS: Allende appears on screen in four missions, all in Act II, and gives none (mission infoboxes: De
Santa gives the first three, Reyes the fourth); the quote list's "Don't shoot! Here, take Williamson..." is labelled
"last words" by the wiki, but the transcript has a later line ("Esta noche, duermo en tu cama, cabrón."): no line is
called his last words here; the gallery caption "Nobody takes them before I get them!" differs from the transcript
("nobody tastes them before Allende!"): the transcript is followed and the line is not used as a quote; Irish's line
is quoted from the transcript, not from the gallery caption; the gates: the Mexican Caesar page says they are locked
from that mission on, the Escalera page dates the closing after "The Gates of El Presidio": both given, attributed.

EXCLUDED: "It is implied that his family is of Spanish origin" and the Communist Manifesto allusion with the "radical
idealist" claim (speculation; the "idealist" line is in no transcript); the real-world name models (Salvador Allende,
Pinochet, Huerta, a border town) and the Ricardo Diaz resemblance (speculative "likely" / "may", and pre-release
artwork belongs to part D); the voice actor's accent and Spanish errors (part D, performance); the pre-release artwork
(part D); the sabre, revolver and armored stagecoach as equipment (part B; the stagecoach is told in part A); the
Zubieta page's "only soldiers with medals" (appearance, part B); the Full Metal Jacket "reference" of a multiplayer
line (interpretation); the FR wiki's comparison with Alberto Fussar (interpretation) and its Japanese voice "Risa
Taneda" (no source; the game was not dubbed in Japanese as far as any source here says, so the claim is left out);
the "hangover" reading of the vomiting and the "$500 in 1911" pesos conversion (wiki inferences); the Wild Bunch
allusion of the Train Robbery page ("perhaps"); the "Damnation" category reading (interpretation); Allende's single
lines likely used in part B "In his own words" ("We brought them God", "Force must be used", "Sorry? Why be sorry?",
"Qué será, será", "patriot", "Take Williamson. Just let me live").

OWNERSHIP: narrative events live in part A (one line per mission here). The newspaper is told in part A only. Quotes
here are exchanges and lines by other characters; if part B uses one of them, the fixer removes it from one place.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A1 = two("Act I: New Austin", "Acte I : New Austin")
A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Allende appears on screen in four story missions of Red Dead Redemption, all in the second act, set in Nuevo Paraíso. He gives none of them: Captain [[vincente-de-santa|Vincente de Santa]] gives the first three and [[abraham-reyes|Abraham Reyes]] the last. According to the Red Dead Wiki, he is the only major character of the game who never gives [[john-marston|John Marston]] a mission directly. His name comes up in many other missions of the act, on both sides of the war, and once at the end of the first act.",
              "Allende apparaît à l'écran dans quatre missions principales de Red Dead Redemption, toutes dans le deuxième acte, au Nuevo Paraíso. Il n'en confie aucune : le capitaine [[vincente-de-santa|Vincente de Santa]] donne les trois premières et [[abraham-reyes|Abraham Reyes]] la dernière. D'après le Red Dead Wiki, c'est le seul personnage majeur du jeu qui ne confie jamais directement de mission à [[john-marston|John Marston]]. Son nom revient dans beaucoup d'autres missions de l'acte, dans les deux camps, et une fois à la fin du premier acte.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Allende's role", "Rôle d'Allende")], "rows": [
        M("The Demon Drink", A2,
          "First meeting with John at his mansion in Escalera; he sends him to Tesoro Azul with De Santa. 27th mission, given by De Santa. Rewards: 50 dollars, a Fire Bottle, 350 fame; the Tesoro Azul hideout becomes available.",
          "Première rencontre avec John, devant sa demeure d'Escalera ; il l'envoie à Tesoro Azul avec De Santa. 27e mission, confiée par De Santa. Récompenses : 50 dollars, une bouteille incendiaire (Fire Bottle), 350 points de célébrité ; la planque de Tesoro Azul devient accessible."),
        M("Mexican Caesar", A2,
          "Receives two women brought by De Santa and has De Santa offer John 20,000 pesos and information on Javier Escuella to escort an army train; never pays. 29th mission, given by De Santa. Rewards: 75 dollars and 200 fame; dynamite goes on sale and Butter Bridge is rebuilt.",
          "Reçoit deux femmes amenées par De Santa et fait proposer à John 20 000 pesos et des renseignements sur Javier Escuella pour escorter un train de l'armée ; ne paie jamais. 29e mission, confiée par De Santa. Récompenses : 75 dollars et 200 points de célébrité ; la dynamite est mise en vente et le pont Butter Bridge est reconstruit."),
        M("Cowards Die Many Times", A2,
          "Tells John that Bill Williamson and Javier Escuella have been captured in Chuparosa and sends him there with De Santa, who betrays him. 36th mission, given by De Santa. Rewards: up to 75 dollars from De Santa's shooting contest, 50 honor and 250 fame; unlocks the Reyes strand.",
          "Annonce à John que Bill Williamson et Javier Escuella ont été capturés à Chuparosa et l'y envoie avec De Santa, qui le trahit. 36e mission, confiée par De Santa. Récompenses : jusqu'à 75 dollars au concours de tir de De Santa, 50 points d'honneur et 250 de célébrité ; débloque la série de Reyes."),
        M("An Appointed Time", A2,
          "Flees the rebel assault on his mansion in an armored stagecoach with Bill, offers Bill to John for his life, and is shot by John or by Reyes. 41st mission, last of the act, given by Reyes. Rewards: up to 535 honor and 300 fame, access to West Elizabeth; achievement \"No More Fancy Words\".",
          "Fuit l'assaut des rebelles sur sa demeure dans une diligence blindée avec Bill, livre Bill à John en échange de sa vie et tombe sous les balles de John ou de Reyes. 41e mission, la dernière de l'acte, confiée par Reyes. Récompenses : jusqu'à 535 points d'honneur et 300 de célébrité, accès à West Elizabeth ; succès \"No More Fancy Words\"."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Link with Allende", "Lien avec Allende")], "rows": [
        M("We Shall Be Together in Paradise", A1,
          "[[irish|Irish]] suggests John try the provincial governor based in Escalera, a colonel whose name he has forgotten, and says he played cards with him (see Quotes). 25th mission, last of New Austin.",
          "[[irish|Irish]] conseille à John de s'adresser au gouverneur de la province, un colonel installé à Escalera dont il a oublié le nom, et dit avoir joué aux cartes avec lui (voir Citations). 25e mission, la dernière du New Austin."),
        M("Civilization, at Any Price", A2,
          "John asks for the commander at Allende's manor; De Santa defends the colonel (see Quotes) and has John escort a decoy train out of Chuparosa. 26th mission.",
          "John demande à voir le commandant à la demeure d'Allende ; De Santa prend la défense du colonel (voir Citations) et fait escorter à John un train leurre au départ de Chuparosa. 26e mission."),
        M("Empty Promises", A2,
          "De Santa leads John to the rebel-held fort of Torquemada on the colonel's urgent orders: to kill them all. 28th mission.",
          "De Santa conduit John au fort de Torquemada, tenu par les rebelles, sur ordre urgent du colonel : les tuer tous. 28e mission."),
        M("The Gunslinger's Tragedy", A2,
          "[[landon-ricketts|Landon Ricketts]] tells John that Allende runs the region like a feudal king (see Quotes). 30th mission.",
          "[[landon-ricketts|Landon Ricketts]] explique à John qu'Allende règne sur la région en seigneur féodal (voir Citations). 30e mission."),
        M("Landon Ricketts Rides Again", A2,
          "Ricketts says that [[luisa-fortuna|Luisa Fortuna]]'s looks are normally enough to interest Allende. 31st mission.",
          "Ricketts affirme que la beauté de [[luisa-fortuna|Luisa Fortuna]] suffit d'ordinaire à attirer l'attention d'Allende. 31e mission."),
        M("The Mexican Wagon Train", A2,
          "Luisa reports that Allende is sending untried prisoners to their deaths; Ricketts says that for once he agrees with Allende (see Quotes). 33rd mission.",
          "Luisa rapporte qu'Allende envoie à la mort des prisonniers jamais jugés ; Ricketts répond que, pour une fois, il est d'accord avec Allende (voir Citations). 33e mission."),
        M("Must a Savior Die?", A2,
          "The executioner at El Presidio condemns Reyes for wanting to overthrow Allende; Reyes says he took John for the American working for Allende. 35th mission.",
          "Le bourreau d'El Presidio condamne Reyes pour avoir voulu renverser Allende ; Reyes avoue avoir pris John pour l'Américain qui travaille pour Allende. 35e mission."),
        M("The Great Mexican Train Robbery", A2,
          "Reyes asks John what he thinks of Allende and calls him a puppet of Sanchez (see Quotes); the rebels rob an army supply train. 37th mission.",
          "Reyes demande à John ce qu'il pense d'Allende et le traite de marionnette de Sanchez (voir Citations) ; les rebelles attaquent un train de ravitaillement de l'armée. 37e mission."),
        M("Father Abraham", A2,
          "Luisa blames Allende for her father's death and says Reyes wants Allende's reinforcements stopped before Escalera; John says Allende betrayed him (see Quotes). 38th mission.",
          "Luisa accuse Allende de la mort de son père et explique que Reyes veut arrêter les renforts d'Allende avant Escalera ; John affirme qu'Allende l'a trahi (voir Citations). 38e mission."),
        M("Captain De Santa's Downfall", A2,
          "De Santa executes a rebel at El Sepulcro in the name of Allende's government; Victor says the rebels must now move on Allende. 39th mission.",
          "De Santa exécute un rebelle à El Sepulcro au nom du gouvernement d'Allende ; Victor estime que les rebelles doivent maintenant marcher sur Allende. 39e mission."),
        M("The Gates of El Presidio", A2,
          "Reyes says Bill and Javier paid Allende to hide them; if captured, Javier says Bill is with Allende. 40th mission.",
          "Reyes affirme que Bill et Javier ont payé Allende pour qu'il les cache ; s'il est capturé, Javier dit que Bill est avec Allende. 40e mission."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the mission transcripts of the Red Dead Wiki. The multiplayer lines and Herbert Moon's lines come from the wiki's quote lists, as no transcript exists for them.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Celles du multijoueur et d'Herbert Moon proviennent des listes de citations du wiki, faute de transcription.")},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("Failing that you could try the provincial governor, Colonel something or other...some Spanish name...he's based out of Escalera. I played Three Card Stud with him...or was it Four Card Monty? I forget. He was a real nice chap or maybe he was a real bastard. I was real drunk last time, John.", "Failing that you could try the provincial governor, Colonel something or other...some Spanish name...he's based out of Escalera. I played Three Card Stud with him...or was it Four Card Monty? I forget. He was a real nice chap or maybe he was a real bastard. I was real drunk last time, John."),
         "src": two("Irish, We Shall Be Together in Paradise (RDR1, Act I), when John asks whether he knows people in Mexico",
                    "Irish, We Shall Be Together in Paradise (RDR1, acte I), quand John lui demande s'il connaît du monde au Mexique. Traduction : « Sinon, tu pourrais essayer le gouverneur de la province, le colonel machin-chose... un nom espagnol... il est installé à Escalera. J'ai joué au Three Card Stud avec lui... ou c'était au Four Card Monty ? J'ai oublié. C'était un type vraiment charmant, ou peut-être un vrai salaud. J'étais drôlement saoul la dernière fois, John. »")},
        {"q": two("Local government, foul bunch. Colonel Allende, he runs this place like a feudal king. He's an awful individual.", "Local government, foul bunch. Colonel Allende, he runs this place like a feudal king. He's an awful individual."),
         "src": two("Landon Ricketts, The Gunslinger's Tragedy (RDR1, Act II), in Chuparosa",
                    "Landon Ricketts, The Gunslinger's Tragedy (RDR1, acte II), à Chuparosa. Traduction : « Le gouvernement local, une sale engeance. Le colonel Allende dirige le coin comme un roi féodal. C'est un individu épouvantable. »")},
        {"q": two("Marston: Even I've heard about the Colonel down here. He's not famous for his compassion. / Vincente: This is the point. Have you met Coronel Allende? Do you know him? No, like a papagayo, you just repeat lies you heard. / Marston: Maybe. / Vincente: Allende is a good man, a strong man. He carries the weight of a million problems on his shoulders. / Marston: Am I supposed to pity him?", "Marston: Even I've heard about the Colonel down here. He's not famous for his compassion. / Vincente: This is the point. Have you met Coronel Allende? Do you know him? No, like a papagayo, you just repeat lies you heard. / Marston: Maybe. / Vincente: Allende is a good man, a strong man. He carries the weight of a million problems on his shoulders. / Marston: Am I supposed to pity him?"),
         "src": two("Civilization, at Any Price (RDR1, Act II), at the table outside the manor in Escalera",
                    "Civilization, at Any Price (RDR1, acte II), attablés devant la demeure d'Escalera. Traduction : « Marston : Même moi, j'ai entendu parler du colonel, par ici. Il n'est pas réputé pour sa compassion. / Vincente : Justement. Avez-vous rencontré le coronel Allende ? Le connaissez-vous ? Non, comme un papagayo, un perroquet, vous répétez les mensonges que vous avez entendus. / Marston : Peut-être. / Vincente : Allende est un homme bon, un homme fort. Il porte sur ses épaules le poids d'un million de problèmes. / Marston : Je suis censé le plaindre ? »")},
        {"q": two("Marston: Pressure to find young girls? / Vincente: The Colonel needs recreation like anybody else. He does not have time to court women. He's waging a war on ignorance, and is impatient for victory. He is trying to inspire wisdom in those more stupid than himself.", "Marston: Pressure to find young girls? / Vincente: The Colonel needs recreation like anybody else. He does not have time to court women. He's waging a war on ignorance, and is impatient for victory. He is trying to inspire wisdom in those more stupid than himself."),
         "src": two("The Demon Drink (RDR1, Act II), on the ride to Tesoro Azul",
                    "The Demon Drink (RDR1, acte II), sur la route de Tesoro Azul. Traduction : « Marston : La pression pour trouver des jeunes filles ? / Vincente : Le colonel a besoin de se distraire, comme tout le monde. Il n'a pas le temps de faire la cour aux femmes. Il mène une guerre contre l'ignorance, et il est pressé de la gagner. Il essaie d'inspirer la sagesse à des gens plus bêtes que lui. »")},
        {"q": two("Espinoza: De Santa licks the Colonel's boots and plays with his waiter friend. That is all. I am Allende's brazo derecho. His right arm. I am one of the few men he respects. / Marston: Is that right? You and him have something special do you?", "Espinoza: De Santa licks the Colonel's boots and plays with his waiter friend. That is all. I am Allende's brazo derecho. His right arm. I am one of the few men he respects. / Marston: Is that right? You and him have something special do you?"),
         "src": two("Captain Espinoza, Mexican Caesar (RDR1, Act II), on the road to Chuparosa",
                    "Le capitaine Espinoza, Mexican Caesar (RDR1, acte II), sur la route de Chuparosa. Traduction : « Espinoza : De Santa lèche les bottes du colonel et s'amuse avec son ami le serveur. C'est tout. Moi, je suis le brazo derecho d'Allende. Son bras droit. Je suis l'un des rares hommes qu'il respecte. / Marston : Tiens donc. Il y a quelque chose de spécial entre vous deux ? »")},
        {"q": two("Marston: Does your brave Colonel ever leave his villa? I haven't seen him anywhere near a fight yet. / De Santa: He is the military commander, but he also governs the province. He must be protected, kept out of harm's way.", "Marston: Does your brave Colonel ever leave his villa? I haven't seen him anywhere near a fight yet. / De Santa: He is the military commander, but he also governs the province. He must be protected, kept out of harm's way."),
         "src": two("Cowards Die Many Times (RDR1, Act II), on the wagon to Chuparosa",
                    "Cowards Die Many Times (RDR1, acte II), sur le chariot qui les mène à Chuparosa. Traduction : « Marston : Il quitte parfois sa villa, ton courageux colonel ? Je ne l'ai encore jamais vu près d'un combat. / De Santa : Il est le commandant militaire, mais il gouverne aussi la province. Il doit être protégé, tenu à l'abri du danger. »")},
        {"q": two("Marston: Are you married? Or do you rape young girls like your Colonel? / De Santa: No, I could never touch a woman like that! It is not my way! But, for them, it is an honor to please their leader.", "Marston: Are you married? Or do you rape young girls like your Colonel? / De Santa: No, I could never touch a woman like that! It is not my way! But, for them, it is an honor to please their leader."),
         "src": two("Cowards Die Many Times (RDR1, Act II), during De Santa's shooting contest",
                    "Cowards Die Many Times (RDR1, acte II), pendant le concours de tir de De Santa. Traduction : « Marston : Tu es marié ? Ou tu violes des jeunes filles, comme ton colonel ? / De Santa : Non, je ne pourrais jamais toucher une femme de cette façon ! Ce n'est pas mon genre ! Mais pour elles, c'est un honneur de faire plaisir à leur chef. »")},
        {"q": two("Landon: Writers and government officials. For once, I agree with Allende. Some men need to be killed. / Luisa: Mr. Ricketts!", "Landon: Writers and government officials. For once, I agree with Allende. Some men need to be killed. / Luisa: Mr. Ricketts!"),
         "src": two("The Mexican Wagon Train (RDR1, Act II), after Luisa reports the executions without trial",
                    "The Mexican Wagon Train (RDR1, acte II), après que Luisa a dénoncé les exécutions sans procès. Traduction : « Landon : Des écrivains et des fonctionnaires. Pour une fois, je suis d'accord avec Allende. Il y a des hommes qu'il faut tuer. / Luisa : Monsieur Ricketts ! »")},
        {"q": two("Marston: Allende betrayed me, and I saw him do bad things. Things that disgust even me. / Luisa: Allende es pura maldad. One day I will cut his heart out.", "Marston: Allende betrayed me, and I saw him do bad things. Things that disgust even me. / Luisa: Allende es pura maldad. One day I will cut his heart out."),
         "src": two("Father Abraham (RDR1, Act II), by the campfire. Luisa's Spanish line means \"Allende is pure evil.\"",
                    "Father Abraham (RDR1, acte II), au coin du feu. Traduction : « Marston : Allende m'a trahi, et je l'ai vu faire des choses horribles. Des choses qui dégoûtent même un type comme moi. / Luisa : Allende es pura maldad (Allende, c'est le mal à l'état pur). Un jour, je lui arracherai le cœur. »")},
        {"q": two("Abraham: I have to know. What did you think of Agustin Allende, John? / Marston: I saw enough to know he ain't a good man. / Abraham: It is bad enough he beats the people he swore to protect. But it is worse that he enjoys it. / Marston: Something must have made him that way. / Abraham: Cowardice made him that way, my friend. That and Sánchez, of course.", "Abraham: I have to know. What did you think of Agustin Allende, John? / Marston: I saw enough to know he ain't a good man. / Abraham: It is bad enough he beats the people he swore to protect. But it is worse that he enjoys it. / Marston: Something must have made him that way. / Abraham: Cowardice made him that way, my friend. That and Sánchez, of course."),
         "src": two("Abraham Reyes, The Great Mexican Train Robbery (RDR1, Act II), on the ride to Chuparosa",
                    "Abraham Reyes, The Great Mexican Train Robbery (RDR1, acte II), sur la route de Chuparosa. Traduction : « Abraham : Il faut que je sache. Qu'as-tu pensé d'Agustin Allende, John ? / Marston : J'en ai assez vu pour savoir que ce n'est pas quelqu'un de bien. / Abraham : C'est déjà grave qu'il batte le peuple qu'il a juré de protéger. Mais c'est pire encore qu'il y prenne plaisir. / Marston : Quelque chose a dû le rendre comme ça. / Abraham : La lâcheté, mon ami. La lâcheté, et Sánchez, bien sûr. »")},
        {"q": two("Abraham: Soon it will be me sleeping on those silk sheets, and the colonel lying with the cucarachas! / Marston: From what I've seen of Allende, you might want to wash those sheets. / Abraham: You might be right, my friend.", "Abraham: Soon it will be me sleeping on those silk sheets, and the colonel lying with the cucarachas! / Marston: From what I've seen of Allende, you might want to wash those sheets. / Abraham: You might be right, my friend."),
         "src": two("The Gates of El Presidio (RDR1, Act II), on the wagon ride",
                    "The Gates of El Presidio (RDR1, acte II), sur le chariot. Traduction : « Abraham : Bientôt, c'est moi qui dormirai dans ces draps de soie, et le colonel couchera avec les cucarachas ! / Marston : Vu ce que j'ai vu d'Allende, tu ferais bien de laver ces draps. / Abraham : Tu as peut-être raison, mon ami. »")},
        {"q": two("Allende is scared, and making mistakes. We are closer to victory than you think.", "Allende is scared, and making mistakes. We are closer to victory than you think."),
         "src": two("Victor, Captain De Santa's Downfall (RDR1, Act II), on the ride to El Sepulcro",
                    "Victor, Captain De Santa's Downfall (RDR1, acte II), sur la route d'El Sepulcro. Traduction : « Allende a peur, et il commet des erreurs. Nous sommes plus près de la victoire que tu ne le crois. »")},
        {"q": two("Ya know, if Johns is elected Governor, he's gonna open the rail lines to Allende.", "Ya know, if Johns is elected Governor, he's gonna open the rail lines to Allende."),
         "src": two("Herbert Moon, the Armadillo shopkeeper, in free roam (quote list of the wiki's Herbert Moon page)",
                    "Herbert Moon, l'épicier d'Armadillo, en exploration libre (liste de citations de la page Herbert Moon du wiki). Traduction : « Tu sais, si Johns est élu gouverneur, il va ouvrir les lignes de chemin de fer à Allende. »")},
    ]},
    {"h4": two("Red Dead Redemption, Act II", "Red Dead Redemption, acte II")},
    {"quotes": [
        {"q": two("Allende: Hola, gringo. So you are the bounty hunter, huh? Have you found your prey yet? / Marston: No, sir. / Allende: Ah, perhaps you come to hunt me, eh? Your country loves to make trouble in mine. / Marston: Perhaps, but it isn't so. / Allende: Ah, perhaps I should tie you to a horse and let it drag you around town, or let the dogs fight you, huh. Then, see what you say? / Marston: I'd say the same thing. I'm here to bring two men to justice. Nothing more. Your politics or ideas of entertainment are not my concern.", "Allende: Hola, gringo. So you are the bounty hunter, huh? Have you found your prey yet? / Marston: No, sir. / Allende: Ah, perhaps you come to hunt me, eh? Your country loves to make trouble in mine. / Marston: Perhaps, but it isn't so. / Allende: Ah, perhaps I should tie you to a horse and let it drag you around town, or let the dogs fight you, huh. Then, see what you say? / Marston: I'd say the same thing. I'm here to bring two men to justice. Nothing more. Your politics or ideas of entertainment are not my concern."),
         "src": two("The Demon Drink (RDR1, Act II), first meeting with John in Escalera",
                    "The Demon Drink (RDR1, acte II), première rencontre avec John à Escalera. Traduction : « Allende : Hola, gringo. Alors c'est toi, le chasseur de primes ? Tu as trouvé ta proie ? / Marston : Non, monsieur. / Allende : Ah, tu es peut-être venu me chasser, moi ? Ton pays adore semer le trouble dans le mien. / Marston : Peut-être, mais ce n'est pas le cas. / Allende : Ah, je devrais peut-être t'attacher à un cheval et le laisser te traîner dans toute la ville, ou te jeter aux chiens. On verrait bien ce que tu dirais, après ? / Marston : Je dirais la même chose. Je suis ici pour livrer deux hommes à la justice. Rien de plus. Votre politique et vos idées de divertissement ne me regardent pas. »")},
        {"q": two("Allende: Now, perhaps you can do me a favor, while I find these men for you. / Marston: After we find the men, then I'll help in any way I can. / Allende: You are in no position to negotiate.", "Allende: Now, perhaps you can do me a favor, while I find these men for you. / Marston: After we find the men, then I'll help in any way I can. / Allende: You are in no position to negotiate."),
         "src": two("The Demon Drink (RDR1, Act II), before sending John to Tesoro Azul",
                    "The Demon Drink (RDR1, acte II), avant d'envoyer John à Tesoro Azul. Traduction : « Allende : Maintenant, tu pourrais peut-être me rendre un service, pendant que je te trouve ces hommes. / Marston : Une fois qu'on aura trouvé les hommes, je vous aiderai comme je pourrai. / Allende : Tu n'es pas en position de négocier. »")},
        {"q": two("Anyways it is good to see you, amigo. Good to see you. You know, you are a rare find. A gringo who is also a friend of our country. Bienvenido. We welcome you.", "Anyways it is good to see you, amigo. Good to see you. You know, you are a rare find. A gringo who is also a friend of our country. Bienvenido. We welcome you."),
         "src": two("Cowards Die Many Times (RDR1, Act II), on his patio, before announcing the capture of Bill and Javier",
                    "Cowards Die Many Times (RDR1, acte II), sur son patio, avant d'annoncer la capture de Bill et de Javier. Traduction : « Bref, je suis content de te voir, amigo. Content de te voir. Tu sais, tu es une perle rare. Un gringo qui est aussi un ami de notre pays. Bienvenido. Sois le bienvenu. »")},
        {"q": two("Marston: Thank you. If it's all the same, I'd like to collect the men. I have a wife and son at home whom I miss. / Allende: Don't we all, amigo, don't we all?", "Marston: Thank you. If it's all the same, I'd like to collect the men. I have a wife and son at home whom I miss. / Allende: Don't we all, amigo, don't we all?"),
         "src": two("Cowards Die Many Times (RDR1, Act II), after offering John more of his hospitality",
                    "Cowards Die Many Times (RDR1, acte II), après avoir proposé à John de profiter encore de son hospitalité. Traduction : « Marston : Merci. Si ça ne vous dérange pas, je préfère aller chercher les hommes. J'ai chez moi une femme et un fils qui me manquent. / Allende : Comme nous tous, amigo, comme nous tous. »")},
        {"q": two("Allende: Come on! We can still get to my stagecoach! / Bill: Go, then! I'll cover you!", "Allende: Come on! We can still get to my stagecoach! / Bill: Go, then! I'll cover you!"),
         "src": two("An Appointed Time (RDR1, Act II), as the rebels break down the door of his mansion",
                    "An Appointed Time (RDR1, acte II), pendant que les rebelles enfoncent la porte de sa demeure. Traduction : « Allende : Vite ! On peut encore rejoindre ma diligence ! / Bill : Vas-y, alors ! Je te couvre ! »")},
        {"q": two("Bill: What the hell are you doing? / Allende: Buying my freedom, pendejo! Now shut up, you dumb ape, and get out of the wagon!", "Bill: What the hell are you doing? / Allende: Buying my freedom, pendejo! Now shut up, you dumb ape, and get out of the wagon!"),
         "src": two("An Appointed Time (RDR1, Act II), once the stagecoach is stopped",
                    "An Appointed Time (RDR1, acte II), une fois la diligence arrêtée. Traduction : « Bill : Qu'est-ce que tu fous ? / Allende : J'achète ma liberté, pendejo ! Maintenant tais-toi, espèce de singe abruti, et descends de là ! »")},
        {"q": two("Esta noche, duermo en tu cama, cabrón.", "Esta noche, duermo en tu cama, cabrón."),
         "src": two("An Appointed Time (RDR1, Act II), his last recorded line in the transcript, in Spanish, while Bill and John trade insults. Translation: \"Tonight, I sleep in your bed, bastard.\"",
                    "An Appointed Time (RDR1, acte II), dernière réplique qui lui soit attribuée dans la transcription, en espagnol, pendant que Bill et John échangent des insultes. Traduction : « Ce soir, je dors dans ton lit, salaud. »")},
    ]},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"quotes": [
        {"q": two("El poder nunca será tuyo!", "El poder nunca será tuyo!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"The power will never be yours!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Le pouvoir ne sera jamais à toi ! »")},
        {"q": two("Ja ja, no has ganado nada!", "Ja ja, no has ganado nada!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"Ha ha, you haven't won anything!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Ha ha, tu n'as rien gagné du tout ! »")},
        {"q": two("Eres un cobarde!", "Eres un cobarde!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"You are a coward!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Tu es un lâche ! »")},
        {"q": two("No eres un hombre de pueblo!", "No eres un hombre de pueblo!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"You're not a man of the people!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Tu n'es pas un homme du peuple ! »")},
        {"q": two("¡Vámonos! Date prisa cabrón!", "¡Vámonos! Date prisa cabrón!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"Come on! Hurry up, asshole!\" He shouts a similar line in the transcript of \"An Appointed Time\" as he flees.",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Allez ! Grouille-toi, connard ! » Il crie une réplique semblable dans la transcription de \"An Appointed Time\", au moment de sa fuite.")},
        {"q": two("Get away from me!", "Get away from me!"),
         "src": two("Red Dead Redemption multiplayer (quote list of the wiki), one of his few lines in English",
                    "Multijoueur de Red Dead Redemption (liste de citations du wiki), l'une de ses rares répliques en anglais. Traduction : « Éloigne-toi de moi ! »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("According to the mission page of \"Mexican Caesar\", Allende bends over and vomits at the end of the opening cutscene.",
            "D'après la page de la mission \"Mexican Caesar\", Allende se plie en deux et vomit à la fin de la cinématique d'ouverture."),
        two("According to the same mission page, the gates of Allende's villa stay locked from \"Mexican Caesar\" until \"An Appointed Time\", and the player cannot enter. The wiki's page on Escalera dates the closing to after \"The Gates of El Presidio\" and says soldiers then patrol the town in greater numbers.",
            "D'après la même page de mission, les grilles de la villa d'Allende restent fermées de \"Mexican Caesar\" jusqu'à \"An Appointed Time\", et le joueur ne peut pas y entrer. La page du wiki consacrée à Escalera situe cette fermeture après \"The Gates of El Presidio\" et précise que les soldats patrouillent alors en plus grand nombre dans la ville."),
        two("According to the Red Dead Wiki, rebel propaganda posters in Nuevo Paraíso attack Allende: one calls him the lapdog of General Ignacio Sanchez, another the puppet of the dictator Sanchez. The wiki's page on Sanchez places these posters in Nosalida.",
            "D'après le Red Dead Wiki, des affiches de propagande rebelles s'en prennent à Allende au Nuevo Paraíso : l'une le traite de petit chien du général Ignacio Sanchez, une autre de marionnette du dictateur Sanchez. La page du wiki consacrée à Sanchez situe ces affiches à Nosalida."),
        two("According to the mission page of \"An Appointed Time\", if the player lassoes Bill while Allende is pinning him down, Reyes shoots both men, which can sometimes make the mission impossible to complete.",
            "D'après la page de la mission \"An Appointed Time\", si le joueur prend Bill au lasso pendant qu'Allende le maintient au sol, Reyes abat les deux hommes, ce qui peut parfois rendre la mission impossible à terminer."),
        two("According to the same page, in rare cases, when John shoots Bill, Reyes does not shoot Allende at once: Allende pleads, runs off into the brush beside the road and is shot in the back by Reyes, outside of any cutscene. In other cases, Allende runs off and Reyes does not shoot him either, which leaves the player stuck until the last checkpoint is reloaded.",
            "D'après la même page, il arrive, quand John abat Bill, que Reyes ne tue pas Allende tout de suite : Allende supplie, s'enfuit dans les broussailles au bord de la route et reçoit une balle dans le dos, hors de toute cinématique. Dans d'autres cas, Allende s'enfuit sans que Reyes ne tire, et le joueur reste bloqué jusqu'à ce qu'il recharge le dernier point de contrôle."),
        two("According to the mission page, Allende's body sometimes stays on the road east of Escalera after the mission, wherever the stagecoach was stopped. It cannot be searched, but if it is set on fire with fire bottles, screams come from the body.",
            "D'après la page de la mission, le corps d'Allende reste parfois sur la route à l'est d'Escalera après la mission, quel que soit l'endroit où la diligence a été arrêtée. On ne peut pas le fouiller, mais si on y met le feu avec des bouteilles incendiaires, il en sort des cris."),
        two("According to the Red Dead Wiki, Allende's portrait still hangs inside his villa after his death.",
            "D'après le Red Dead Wiki, le portrait d'Allende reste accroché dans sa villa après sa mort."),
        two("According to the mission page of \"An Appointed Time\", the gates of Allende's mansion are still lying on the ground in pieces when the player returns to Escalera in 1914.",
            "D'après la page de la mission \"An Appointed Time\", les grilles de la demeure d'Allende gisent toujours en morceaux sur le sol quand le joueur revient à Escalera en 1914."),
        two("According to the same page, shortly after the mission, a random encounter can show army soldiers executing rebels for speaking out against Allende, although he is already dead.",
            "D'après la même page, peu après la mission, une rencontre aléatoire peut montrer des soldats de l'armée en train d'exécuter des rebelles pour avoir critiqué Allende, alors qu'il est déjà mort."),
        two("Allende does not appear in Undead Nightmare, the non-canon expansion. According to the wiki's Undead Nightmare page, Reyes has moved into Allende's former mansion in Escalera by then.",
            "Allende n'apparaît pas dans Undead Nightmare, l'extension hors canon. D'après la page du wiki consacrée à Undead Nightmare, Reyes s'est alors installé dans l'ancienne demeure d'Allende à Escalera."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Allende became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. Players select him in the Damnation section of the Outfitter, with [[abraham-reyes|Abraham Reyes]], [[bill-williamson|Bill Williamson]], [[dutch-van-der-linde|Dutch van der Linde]], [[edgar-ross|Edgar Ross]], [[harold-macdougal|Harold MacDougal]] and [[irish|Irish]]. Most of his multiplayer lines are in Spanish (see Quotes). The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the Allende model is not available in them.",
              "Allende devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. On le choisit dans la section Damnation de l'Outfitter, aux côtés d'[[abraham-reyes|Abraham Reyes]], de [[bill-williamson|Bill Williamson]], de [[dutch-van-der-linde|Dutch van der Linde]], d'[[edgar-ross|Edgar Ross]], d'[[harold-macdougal|Harold MacDougal]] et d'[[irish|Irish]]. La plupart de ses répliques en multijoueur sont en espagnol (voir Citations). Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle d'Allende n'y est donc pas disponible.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Allende for Red Dead Redemption, and an alternate artwork of him appears in the Red Dead Wiki's gallery. According to the wiki, he stands next to John Marston on the cover art of the Game of the Year Edition. Allende does not appear in Red Dead Redemption 2 or in Red Dead Online, which are set before 1911; the Red Dead Wiki lists him only in Red Dead Redemption.",
              "Rockstar a diffusé une illustration officielle d'Allende pour Red Dead Redemption, et une autre illustration de lui figure dans la galerie du Red Dead Wiki. D'après le wiki, il se tient à côté de John Marston sur la jaquette de l'édition Game of the Year. Allende n'apparaît ni dans Red Dead Redemption 2 ni dans Red Dead Online, qui se déroulent avant 1911 ; le Red Dead Wiki ne le recense que dans Red Dead Redemption.")},
]
