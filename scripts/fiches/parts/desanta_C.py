"""Vincente de Santa, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/; copies in
scripts/v3/work/desanta/fc/):
- Character page "Vincente de Santa" (Mission appearances, Quotes incl. the Multiplayer list, Trivia, Gallery
  captions) and FR page "Vincente De Santa" (Apparitions dans les missions, Citations, Anecdotes).
- Mission pages (infobox order numbers, givers, rewards, unlocks, failure conditions, tips, trivia): "Civilization, at
  Any Price" (26th), "The Demon Drink" (27th), "Empty Promises" (28th), "Mexican Caesar" (29th), "Cowards Die Many
  Times" (36th), "Captain De Santa's Downfall" (39th), "Must a Savior Die?" (35th), "The Gates of El Presidio" (40th),
  "Mother Superior Blues" (Undead Nightmare).
- Transcripts used word for word for every mission quote: "Civilization, at Any Price/dialogues", "The Demon
  Drink/dialogues", "Empty Promises/dialogues", "Mexican Caesar/dialogues", "Cowards Die Many Times/dialogues",
  "Captain De Santa's Downfall/dialogues", "Must a Savior Die?/dialogues", "The Gates of El Presidio/dialogues". The
  lines with no transcript (lines when injured, the threat, the Spanish insult) and the multiplayer lines with their
  English translations come from the quote list of the character page; Herbert Moon's line from the quote list of the
  "Herbert Moon" page.
- Other pages: "Myths and Mavericks" (release September 13, 2011 via Xbox LIVE and PlayStation Network; Newswire posts
  of June 6, July 27 and September 1, 2011 cited there; eight Revolution characters; last DLC of the game; gallery
  caption of the Torquemada Stronghold image), "Sepulcro", "Escalera" (all missions of the De Santa strand begin there),
  "Espinoza". Extract in desanta/fc/sepulcro_grave_and_misc.txt.
- Real world: Myths and Mavericks free release on September 13, 2011 on PlayStation 3 and Xbox 360 (as in landon_C,
  javier_C); RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 without multiplayer (as in allende_C,
  reyes_C, landon_C).

VERIFIED POINTS: De Santa gives the five missions of his strand (infoboxes); "Captain De Santa's Downfall" is given by
Luisa Fortuna, "Cowards Die Many Times" also needs "Must a Savior Die?". The wiki's "If my men are dead..." and "Go get
drunk!..." lines match the transcripts and are left to part B; the wiki's "El nombre es Colonel Allende, ahora cavar
su tumba maldita arriba" differs from the transcript of the Sepulcro execution and is not used. The quote list's "You
are the better man", "Please, I am begging you", "If you kill me I will sent the entire Mexican Army after you" and
"Marston ya hijo de puta!" have no transcript: given as quote-list lines, with the wiki's spelling. The Reyes line of
"The Gates of El Presidio" is "sleep safer" in the transcript ("sleep safe" on the character page): transcript followed.

EXCLUDED: the lines most likely quoted in part B "In his own words" ("Sometimes in the service of what is right...",
"My country is in pain...", "I am the government...", "This isn't America...", "The peasants are stupid...", "I bleed
red, white and green...", "Sometimes we must be brutal to be kind...", "When I put on this uniform...", "Go get
drunk!...", "If my men are dead...", "Mexico loves you, Mr. Marston"); Victor's "men on their knees" line and every
trivia item on his sexuality (no transcript or interpretation); the burgundy shoulder patches "meaning" (inference);
the lazy eye (appearance, part B); the Brian Jeremy comparison (interpretation, "possibly"); the Julius Caesar
"reference to De Santa killed twice" (speculation); the FR wiki's Scarface model and "more in the field than Irish or
Dickens" (no source); the "Captain dead next to the cart" bug (it concerns Espinoza's mission, not De Santa); the
punch glitch of the Downfall page (bug with no bearing on the character).

OWNERSHIP: narrative events live in part A (one line per mission here). The newspaper notice and the gravestone are
told in part A only. Quotes here are exchanges and lines by other characters.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")
UNM = two("Undead Nightmare", "Undead Nightmare")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("De Santa appears in six story missions of Red Dead Redemption, all in the second act, set in Nuevo Paraíso, and in one mission of Undead Nightmare. He gives the five missions of his own strand, all of which begin in Escalera. The sixth, in which he dies, belongs to the strand of [[luisa-fortuna|Luisa Fortuna]]. [[abraham-reyes|Abraham Reyes]] mentions him in two other missions of the act.",
              "De Santa apparaît dans six missions principales de Red Dead Redemption, toutes dans le deuxième acte, au Nuevo Paraíso, ainsi que dans une mission d'Undead Nightmare. Il confie les cinq missions de sa propre série, qui commencent toutes à Escalera. La sixième, où il trouve la mort, appartient à la série de [[luisa-fortuna|Luisa Fortuna]]. [[abraham-reyes|Abraham Reyes]] parle de lui dans deux autres missions de l'acte.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("De Santa's role", "Rôle de De Santa")], "rows": [
        M("Civilization, at Any Price", A2,
          "Mission giver. Meets [[john-marston|John Marston]] at the manor in Escalera and has him escort a decoy train out of Chuparosa. 26th mission. Rewards: 50 dollars and 250 fame; unlocks the Luisa Fortuna strand and the stranger mission \"Poppycock\".",
          "Donneur de mission. Reçoit [[john-marston|John Marston]] à la demeure d'Escalera et lui fait escorter un train leurre au départ de Chuparosa. 26e mission. Récompenses : 50 dollars et 250 points de célébrité ; débloque la série de Luisa Fortuna et la mission d'inconnu \"Poppycock\"."),
        M("The Demon Drink", A2,
          "Mission giver. Introduces John to [[agustin-allende|Agustin Allende]] and races him to Tesoro Azul, where the village is cleared and burned. 27th mission. Rewards: 50 dollars, a Fire Bottle and 350 fame; the Tesoro Azul hideout becomes available.",
          "Donneur de mission. Présente John à [[agustin-allende|Agustin Allende]] et fait la course avec lui jusqu'à Tesoro Azul, où le village est nettoyé puis incendié. 27e mission. Récompenses : 50 dollars, une bouteille incendiaire (Fire Bottle) et 350 points de célébrité ; la planque de Tesoro Azul devient accessible."),
        M("Empty Promises", A2,
          "Mission giver. Takes John on his wagon to the rebel-held fort of Torquemada, then puts off his questions. 28th mission. Rewards: 100 dollars, a Rolling Block Rifle (gift) and 300 fame; unlocks the stranger missions \"Love is the Opiate\" and \"Funny Man\" (part 4).",
          "Donneur de mission. Emmène John sur son chariot jusqu'au fort de Torquemada, tenu par les rebelles, puis élude ses questions. 28e mission. Récompenses : 100 dollars, un Rolling Block Rifle (offert) et 300 points de célébrité ; débloque les missions d'inconnu \"Love is the Opiate\" et \"Funny Man\" (quatrième partie)."),
        M("Mexican Caesar", A2,
          "Mission giver. Brings two women to Allende and offers John 20,000 pesos and information on Javier Escuella to escort an army train; stays behind while John rides with Espinoza. 29th mission. Rewards: 75 dollars and 200 fame; dynamite goes on sale and Butter Bridge is rebuilt.",
          "Donneur de mission. Amène deux femmes à Allende et propose à John 20 000 pesos et des renseignements sur Javier Escuella pour escorter un train de l'armée ; reste en arrière pendant que John part avec Espinoza. 29e mission. Récompenses : 75 dollars et 200 points de célébrité ; la dynamite est mise en vente et le pont Butter Bridge est reconstruit."),
        M("Cowards Die Many Times", A2,
          "Mission giver. Takes John to Chuparosa on the pretext that Bill and Javier are held in the church, holds a shooting contest on the way, then has him knocked out and set before a firing squad. 36th mission; also requires \"Must a Savior Die?\". Rewards: up to 75 dollars from the contest, 50 honor and 250 fame; unlocks the Reyes strand and \"Father Abraham\".",
          "Donneur de mission. Conduit John à Chuparosa sous prétexte que Bill et Javier sont détenus dans l'église, organise un concours de tir en chemin, puis le fait assommer et placer devant un peloton. 36e mission ; exige aussi d'avoir terminé \"Must a Savior Die?\". Récompenses : jusqu'à 75 dollars au concours de tir, 50 points d'honneur et 250 de célébrité ; débloque la série de Reyes et \"Father Abraham\"."),
        M("Captain De Santa's Downfall", A2,
          "Target. Executes a rebel at Sepulcro, is hogtied and beaten by John, names Casa Madrugada, and is shot by John or by the rebels (player's choice). 39th mission, given by Luisa Fortuna, from Campo Mirada to Casa Madrugada. Rewards: 125 honor and 300 fame.",
          "Cible. Exécute un rebelle à Sepulcro, se fait ligoter et rouer de coups par John, désigne Casa Madrugada, puis tombe sous les balles de John ou des rebelles (au choix du joueur). 39e mission, confiée par Luisa Fortuna, de Campo Mirada à Casa Madrugada. Récompenses : 125 points d'honneur et 300 de célébrité."),
        M("Mother Superior Blues", UNM,
          "Rises from his grave as the undead boss of the Sepulcro cemetery. Mission given by the Mother Superior of Las Hermanas. Reward: Holy Water.",
          "Sort de sa tombe en boss mort-vivant du cimetière de Sepulcro. Mission confiée par la mère supérieure de Las Hermanas. Récompense : eau bénite (Holy Water)."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Link with De Santa", "Lien avec De Santa")], "rows": [
        M("Must a Savior Die?", A2,
          "Freed by John at El Presidio, Reyes jokes that John has been spending too much time with Captain De Santa (see Quotes). 35th mission, given by Luisa.",
          "Libéré par John à El Presidio, Reyes plaisante : John a passé trop de temps avec le capitaine De Santa (voir Citations). 35e mission, confiée par Luisa."),
        M("The Gates of El Presidio", A2,
          "Reyes has heard of De Santa's death at Sepulcro; his lines and John's answers differ depending on who shot him (see Biography). 40th mission, given by Reyes.",
          "Reyes a appris la mort de De Santa à Sepulcro ; ses répliques et les réponses de John varient selon qui l'a abattu (voir la biographie). 40e mission, confiée par Reyes."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the mission transcripts of the Red Dead Wiki. The lines with no transcript, the multiplayer lines and Herbert Moon's line come from the wiki's quote lists.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Celles qui n'ont pas de transcription, celles du multijoueur et celle d'Herbert Moon proviennent des listes de citations du wiki.")},
    {"h4": two("Red Dead Redemption, Act II", "Red Dead Redemption, acte II")},
    {"quotes": [
        {"q": two("Marston: Where can I find this Reyes? / Vincente: If I knew I would be there, hunting him with everything that is true within me. Reyes finds you. / Marston: Like cholera. / Vincente: Something like that.", "Marston: Where can I find this Reyes? / Vincente: If I knew I would be there, hunting him with everything that is true within me. Reyes finds you. / Marston: Like cholera. / Vincente: Something like that."),
         "src": two("Civilization, at Any Price (RDR1, Act II), at the table outside the manor in Escalera",
                    "Civilization, at Any Price (RDR1, acte II), à la table dressée devant la demeure d'Escalera. Traduction : « Marston : Où est-ce que je peux trouver ce Reyes ? / Vincente : Si je le savais, j'y serais, à le traquer de tout ce qu'il y a de sincère en moi. C'est Reyes qui vous trouve. / Marston : Comme le choléra. / Vincente : Quelque chose comme ça. »")},
        {"q": two("Vincente: The past is all that's real, my friend. It cannot be erased. That is the problem with the people here. They spend too much time dreaming about imaginary futures. / Marston: I know I can't change the past but I'm sure gonna do somethin' about the future. / Vincente: Whatever helps you sleep at night, amigo.", "Vincente: The past is all that's real, my friend. It cannot be erased. That is the problem with the people here. They spend too much time dreaming about imaginary futures. / Marston: I know I can't change the past but I'm sure gonna do somethin' about the future. / Vincente: Whatever helps you sleep at night, amigo."),
         "src": two("Civilization, at Any Price (RDR1, Act II), on the wagon to Chuparosa, after John says that Bill and Javier were his friends",
                    "Civilization, at Any Price (RDR1, acte II), sur le chariot qui mène à Chuparosa, après que John a raconté que Bill et Javier étaient ses amis. Traduction : « Vincente : Le passé est la seule chose réelle, mon ami. On ne peut pas l'effacer. C'est le problème des gens d'ici. Ils passent trop de temps à rêver d'avenirs imaginaires. / Marston : Je sais que je ne peux pas changer le passé, mais je compte bien faire quelque chose de l'avenir. / Vincente : Si ça peut vous aider à dormir, amigo. »")},
        {"q": two("Vincente: Are you a revolutionary? Is that why you are here? / Marston: I was once, I suppose, in a twisted kind of way. Thought I could change something if I fought hard enough. / Vincente: Change what? / Marston: I don't know. Maybe that was the problem.", "Vincente: Are you a revolutionary? Is that why you are here? / Marston: I was once, I suppose, in a twisted kind of way. Thought I could change something if I fought hard enough. / Vincente: Change what? / Marston: I don't know. Maybe that was the problem."),
         "src": two("Civilization, at Any Price (RDR1, Act II), on the same ride",
                    "Civilization, at Any Price (RDR1, acte II), pendant le même trajet. Traduction : « Vincente : Vous êtes un révolutionnaire ? C'est pour ça que vous êtes ici ? / Marston : Je l'ai été, je suppose, d'une manière un peu tordue. Je croyais pouvoir changer quelque chose si je me battais assez fort. / Vincente : Changer quoi ? / Marston : Je ne sais pas. C'était peut-être ça, le problème. »")},
        {"q": two("Marston: So I finally met your great leader. He certainly lives up to his reputation. / Vincente: What would you know about leadership? / Marston: Only that most can't handle power. / Vincente: It is easy to criticize power, when you have never had it yourself.", "Marston: So I finally met your great leader. He certainly lives up to his reputation. / Vincente: What would you know about leadership? / Marston: Only that most can't handle power. / Vincente: It is easy to criticize power, when you have never had it yourself."),
         "src": two("The Demon Drink (RDR1, Act II), on the ride to Tesoro Azul, after the meeting with Allende",
                    "The Demon Drink (RDR1, acte II), sur la route de Tesoro Azul, après la rencontre avec Allende. Traduction : « Marston : J'ai enfin rencontré ton grand chef. Il est à la hauteur de sa réputation, pas de doute. / Vincente : Qu'est-ce que tu connais au commandement ? / Marston : Seulement que la plupart des gens ne supportent pas le pouvoir. / Vincente : Il est facile de critiquer le pouvoir quand on ne l'a jamais eu. »")},
        {"q": two("Marston: Was he that deranged captain at Tesoro Azul? Is he leadin' this attack? / De Santa: Leading? Espinoza does not lead anything! / Marston: I thought you was the same rank? / De Santa: He is an angry dog we let out to run sometimes. That is all. I'm in charge here.", "Marston: Was he that deranged captain at Tesoro Azul? Is he leadin' this attack? / De Santa: Leading? Espinoza does not lead anything! / Marston: I thought you was the same rank? / De Santa: He is an angry dog we let out to run sometimes. That is all. I'm in charge here."),
         "src": two("Empty Promises (RDR1, Act II), at the army camp below Torquemada",
                    "Empty Promises (RDR1, acte II), au camp de l'armée, au pied de Torquemada. Traduction : « Marston : C'est lui, le capitaine dérangé de Tesoro Azul ? C'est lui qui mène l'attaque ? / De Santa : Qui mène ? Espinoza ne mène rien du tout ! / Marston : Je croyais que vous aviez le même grade ? / De Santa : C'est un chien enragé qu'on laisse courir de temps en temps. C'est tout. Ici, c'est moi qui commande. »")},
        {"q": two("Marston: What's going on here, Captain De Santa? / Vincente: Just a little recruitment. Nothing for you to be concerned about. / Marston: You boys using women soldiers now? / Vincente: Our customs are none of your concern. / Marston: Apparently not.", "Marston: What's going on here, Captain De Santa? / Vincente: Just a little recruitment. Nothing for you to be concerned about. / Marston: You boys using women soldiers now? / Vincente: Our customs are none of your concern. / Marston: Apparently not."),
         "src": two("Mexican Caesar (RDR1, Act II), as De Santa and Quique Montemayor bring two young women to the manor",
                    "Mexican Caesar (RDR1, acte II), quand De Santa et Quique Montemayor amènent deux jeunes femmes à la demeure. Traduction : « Marston : Qu'est-ce qui se passe ici, capitaine De Santa ? / Vincente : Un petit recrutement, rien de plus. Rien qui vous concerne. / Marston : Vous prenez des femmes dans l'armée, maintenant ? / Vincente : Nos coutumes ne vous regardent pas. / Marston : Visiblement pas. »")},
        {"q": two("Marston: Like the 20,000 pesos you promised, when you sent me on a suicide mission with Espinoza? / De Santa: Yes, it has been a busy time for you in Mexico. / Marston: What do you mean? / De Santa: I mean, you have built quite a reputation for yourself.", "Marston: Like the 20,000 pesos you promised, when you sent me on a suicide mission with Espinoza? / De Santa: Yes, it has been a busy time for you in Mexico. / Marston: What do you mean? / De Santa: I mean, you have built quite a reputation for yourself."),
         "src": two("Cowards Die Many Times (RDR1, Act II), on the wagon to Chuparosa, after De Santa promises that his men have the prisoners surrounded",
                    "Cowards Die Many Times (RDR1, acte II), sur le chariot qui mène à Chuparosa, après que De Santa a promis que ses hommes encerclaient les prisonniers. Traduction : « Marston : Comme les 20 000 pesos que tu m'avais promis, quand tu m'as envoyé en mission suicide avec Espinoza ? / De Santa : Oui, tu as été bien occupé, au Mexique. / Marston : Qu'est-ce que tu veux dire ? / De Santa : Je veux dire que tu t'es fait une sacrée réputation. »")},
        {"q": two("Marston: Why are they in the church? / De Santa: It is as good a place, as any, to judge a man, wouldn't you say? / Marston: Are they armed? / De Santa: No, they are prisoners. Take a deep breath. Calm yourself, it will be like lambs to the slaughter.", "Marston: Why are they in the church? / De Santa: It is as good a place, as any, to judge a man, wouldn't you say? / Marston: Are they armed? / De Santa: No, they are prisoners. Take a deep breath. Calm yourself, it will be like lambs to the slaughter."),
         "src": two("Cowards Die Many Times (RDR1, Act II), on arriving in Chuparosa",
                    "Cowards Die Many Times (RDR1, acte II), à l'arrivée à Chuparosa. Traduction : « Marston : Pourquoi est-ce qu'ils sont dans l'église ? / De Santa : C'est un endroit aussi bon qu'un autre pour juger un homme, tu ne crois pas ? / Marston : Ils sont armés ? / De Santa : Non, ce sont des prisonniers. Respire un bon coup. Calme-toi, ce sera comme mener des agneaux à l'abattoir. »")},
        {"q": two("Marston. Hey! Marston. You have betrayed this land enough. I hope you have a clear conscience, 'cause you are about to meet God.", "Marston. Hey! Marston. You have betrayed this land enough. I hope you have a clear conscience, 'cause you are about to meet God."),
         "src": two("Cowards Die Many Times (RDR1, Act II), after John is pulled out of the horse trough",
                    "Cowards Die Many Times (RDR1, acte II), après qu'on a sorti la tête de John de l'abreuvoir. Traduction : « Marston. Hé ! Marston. Tu as assez trahi ce pays. J'espère que tu as la conscience tranquille, parce que tu vas bientôt rencontrer Dieu. »")},
        {"q": two("Vincente: You fucking pig! Go back to your country. / Marston: Where is Javier Escuella? / Vincente: Wait, wait, wait. Okay. Alright! Alright... Shit... Alright. Casa Madrugada. He's holed up there. Hurry up and kill me or just let me go. Okay?", "Vincente: You fucking pig! Go back to your country. / Marston: Where is Javier Escuella? / Vincente: Wait, wait, wait. Okay. Alright! Alright... Shit... Alright. Casa Madrugada. He's holed up there. Hurry up and kill me or just let me go. Okay?"),
         "src": two("Captain De Santa's Downfall (RDR1, Act II), as John beats him at the entrance of the Sepulcro cemetery",
                    "Captain De Santa's Downfall (RDR1, acte II), pendant que John le roue de coups à l'entrée du cimetière de Sepulcro. Traduction : « Vincente : Espèce de sale porc ! Rentre dans ton pays. / Marston : Où est Javier Escuella ? / Vincente : Attends, attends, attends. D'accord. D'accord ! D'accord... Merde... D'accord. Casa Madrugada. Il se planque là-bas. Maintenant dépêche-toi de me tuer, ou laisse-moi partir. D'accord ? »")},
    ]},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("Marston: Why didn't De Santa come with us? / Espinoza: Why do you think? Because he is hardly a soldier. I'm sure has other important business, like mailing letters or sweeping floors or flirting with barmen. / Marston: He fought with you at Torquemada. / Espinoza: Are you defending that pathetic little errand boy? I did not see him fight. Without me, we would have lost the battle. He knows less than nothing of how to lead men.", "Marston: Why didn't De Santa come with us? / Espinoza: Why do you think? Because he is hardly a soldier. I'm sure has other important business, like mailing letters or sweeping floors or flirting with barmen. / Marston: He fought with you at Torquemada. / Espinoza: Are you defending that pathetic little errand boy? I did not see him fight. Without me, we would have lost the battle. He knows less than nothing of how to lead men."),
         "src": two("Captain Espinoza, Mexican Caesar (RDR1, Act II), on the road to Chuparosa",
                    "Le capitaine Espinoza, Mexican Caesar (RDR1, acte II), sur la route de Chuparosa. Traduction : « Marston : Pourquoi De Santa n'est pas venu avec nous ? / Espinoza : À ton avis ? Parce que ce n'est pas vraiment un soldat. Il a sûrement d'autres affaires importantes, comme poster des lettres, balayer par terre ou flirter avec les garçons de café. / Marston : Il s'est battu avec toi à Torquemada. / Espinoza : Tu défends ce pitoyable petit coursier ? Je ne l'ai pas vu se battre. Sans moi, on aurait perdu la bataille. Il en sait moins que rien sur l'art de commander. »")},
        {"q": two("We have already been ambushed. Our squad is made up of new recruits and the two men De Santa hates the most. I think it is right to be anxious.", "We have already been ambushed. Our squad is made up of new recruits and the two men De Santa hates the most. I think it is right to be anxious."),
         "src": two("Captain Espinoza, Mexican Caesar (RDR1, Act II), on the train, after John calls him anxious",
                    "Le capitaine Espinoza, Mexican Caesar (RDR1, acte II), dans le train, après que John l'a trouvé nerveux. Traduction : « On est déjà tombés dans une embuscade. Notre escouade se compose de nouvelles recrues et des deux hommes que De Santa déteste le plus. Je crois qu'il y a de quoi être nerveux. »")},
        {"q": two("Marston: I don't think De Santa expected us to come back from this. / Espinoza: Did you want to kill him, or should I? / Marston: No, until I find Escuella, he's more use to me alive.", "Marston: I don't think De Santa expected us to come back from this. / Espinoza: Did you want to kill him, or should I? / Marston: No, until I find Escuella, he's more use to me alive."),
         "src": two("Mexican Caesar (RDR1, Act II), at the end of the train escort",
                    "Mexican Caesar (RDR1, acte II), à la fin de l'escorte du train. Traduction : « Marston : Je ne crois pas que De Santa s'attendait à nous voir revenir. / Espinoza : Tu veux le tuer toi-même, ou je m'en charge ? / Marston : Non. Tant que je n'ai pas trouvé Escuella, il m'est plus utile vivant. »")},
        {"q": two("Marston: I'm here for two men, and that's it. / Abraham: You have been spending too much time with Captain de Santa. / Marston: Very funny. Not like that. I'll explain later.", "Marston: I'm here for two men, and that's it. / Abraham: You have been spending too much time with Captain de Santa. / Marston: Very funny. Not like that. I'll explain later."),
         "src": two("Abraham Reyes, Must a Savior Die? (RDR1, Act II), after Reyes offers John money, women or Luisa as a reward",
                    "Abraham Reyes, Must a Savior Die? (RDR1, acte II), après que Reyes a proposé à John de l'argent, des femmes ou Luisa en récompense. Traduction : « Marston : Je suis là pour deux hommes, un point c'est tout. / Abraham : Tu as passé trop de temps avec le capitaine De Santa. / Marston : Très drôle. Pas dans ce sens-là. Je t'expliquerai plus tard. »")},
        {"q": two("Can we kill this piece of shit now, señor, or would you like the pleasure yourself?", "Can we kill this piece of shit now, señor, or would you like the pleasure yourself?"),
         "src": two("Victor, Captain De Santa's Downfall (RDR1, Act II), after De Santa names Casa Madrugada",
                    "Victor, Captain De Santa's Downfall (RDR1, acte II), après que De Santa a désigné Casa Madrugada. Traduction : « On peut tuer ce tas de merde, maintenant, señor, ou vous voulez avoir ce plaisir vous-même ? »")},
        {"q": two("Victor: That man is responsible for hundreds of innocent deaths, maybe even thousands. He will burn in hell. / Marston: We all will, my friend.", "Victor: That man is responsible for hundreds of innocent deaths, maybe even thousands. He will burn in hell. / Marston: We all will, my friend."),
         "src": two("Captain De Santa's Downfall (RDR1, Act II), after De Santa's death, in both versions of the player's choice",
                    "Captain De Santa's Downfall (RDR1, acte II), après la mort de De Santa, quel que soit le choix du joueur. Traduction : « Victor : Cet homme est responsable de centaines de morts innocentes, peut-être même de milliers. Il brûlera en enfer. / Marston : Comme nous tous, mon ami. »")},
        {"q": two("Marston: I don't blame you. But Captain De Santa said he was here. / Woman: And you believed him? You must be more stupid than you look. Go shoot up some place else.", "Marston: I don't blame you. But Captain De Santa said he was here. / Woman: And you believed him? You must be more stupid than you look. Go shoot up some place else."),
         "src": two("A woman of Casa Madrugada, Captain De Santa's Downfall (RDR1, Act II), after the army ambush",
                    "Une femme de Casa Madrugada, Captain De Santa's Downfall (RDR1, acte II), après l'embuscade de l'armée. Traduction : « Marston : Je ne vous en veux pas. Mais le capitaine De Santa m'a dit qu'il était ici. / La femme : Et vous l'avez cru ? Vous devez être encore plus bête que vous n'en avez l'air. Allez donc tirer ailleurs. »")},
        {"q": two("Abraham: I am happy it was your bullet, John, after what he did to you in Chuparosa. / Marston: I wasn't goin' to give him a second chance to kill me. / Abraham: It must have felt good. / Marston: Not particularly. He was hardly worth a bullet.", "Abraham: I am happy it was your bullet, John, after what he did to you in Chuparosa. / Marston: I wasn't goin' to give him a second chance to kill me. / Abraham: It must have felt good. / Marston: Not particularly. He was hardly worth a bullet."),
         "src": two("The Gates of El Presidio (RDR1, Act II), on the wagon, if John killed De Santa himself",
                    "The Gates of El Presidio (RDR1, acte II), sur le chariot, si John a tué De Santa lui-même. Traduction : « Abraham : Je suis heureux que ce soit ta balle, John, après ce qu'il t'a fait à Chuparosa. / Marston : Je n'allais pas lui laisser une seconde chance de me tuer. / Abraham : Ça a dû te faire du bien. / Marston : Pas spécialement. Il valait à peine une balle. »")},
        {"q": two("De Santa was only following orders. He was dumb and loyal to his awful master, but that's all he was.", "De Santa was only following orders. He was dumb and loyal to his awful master, but that's all he was."),
         "src": two("John Marston, The Gates of El Presidio (RDR1, Act II), if the rebels killed De Santa",
                    "John Marston, The Gates of El Presidio (RDR1, acte II), si ce sont les rebelles qui ont tué De Santa. Traduction : « De Santa ne faisait qu'obéir aux ordres. C'était un imbécile, loyal envers un maître abominable, mais il n'était rien de plus. »")},
        {"q": two("Sanchez, Allende, De Santa, Reyes; all the same! They just want Armadillo rail rides.", "Sanchez, Allende, De Santa, Reyes; all the same! They just want Armadillo rail rides."),
         "src": two("Herbert Moon, the Armadillo shopkeeper, about the railroads in Mexico (quote list of the wiki's Herbert Moon page)",
                    "Herbert Moon, l'épicier d'Armadillo, à propos des chemins de fer au Mexique (liste de citations de la page Herbert Moon du wiki). Traduction : « Sanchez, Allende, De Santa, Reyes, tous pareils ! Tout ce qu'ils veulent, c'est le train jusqu'à Armadillo. »")},
    ]},
    {"h4": two("Lines from the wiki's quote list", "Répliques de la liste de citations du wiki")},
    {"quotes": [
        {"q": two("You are the better man.", "You are the better man."),
         "src": two("Red Dead Redemption, when injured (quote list of the wiki; no transcript)",
                    "Red Dead Redemption, quand il est blessé (liste de citations du wiki ; pas de transcription). Traduction : « Tu vaux mieux que moi. »")},
        {"q": two("Please, I am begging you.", "Please, I am begging you."),
         "src": two("Red Dead Redemption, when injured (quote list of the wiki; no transcript)",
                    "Red Dead Redemption, quand il est blessé (liste de citations du wiki ; pas de transcription). Traduction : « Je t'en prie, je t'en supplie. »")},
        {"q": two("If you kill me I will sent the entire Mexican Army after you.", "If you kill me I will sent the entire Mexican Army after you."),
         "src": two("Red Dead Redemption, threatening John (quote list of the wiki, spelling as given there; no transcript)",
                    "Red Dead Redemption, en menaçant John (liste de citations du wiki, orthographe d'origine ; pas de transcription). Traduction : « Si tu me tues, je lance toute l'armée mexicaine à tes trousses. »")},
        {"q": two("Marston ya hijo de puta!", "Marston ya hijo de puta!"),
         "src": two("Red Dead Redemption, in Spanish (quote list of the wiki; no transcript). Translation given by the wiki: \"Marston you son of a bitch!\"",
                    "Red Dead Redemption, en espagnol (liste de citations du wiki ; pas de transcription). Traduction : « Marston, fils de pute ! »")},
    ]},
    {"h4": two("Red Dead Redemption multiplayer", "Multijoueur de Red Dead Redemption")},
    {"quotes": [
        {"q": two("Tu fin ha llegado, ¡Pendejo!", "Tu fin ha llegado, ¡Pendejo!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"Your end has come, asshole!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Ta fin est arrivée, connard ! »")},
        {"q": two("No sabes con quién estás tratando.", "No sabes con quién estás tratando."),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"You don't know who you're dealing with.\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Tu ne sais pas à qui tu as affaire. »")},
        {"q": two("¡Van todos al infierno!", "¡Van todos al infierno!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"You all go to hell!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Vous irez tous en enfer ! »")},
        {"q": two("Ríndanse!", "Ríndanse!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"Give up!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Rendez-vous ! »")},
        {"q": two("Eres mío, ¡Hijo de puta!", "Eres mío, ¡Hijo de puta!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"You're mine, son of a bitch!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Tu es à moi, fils de pute ! »")},
        {"q": two("Estás muerto!", "Estás muerto!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"You're dead!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « T'es mort ! »")},
        {"q": two("¡Ya basta cabrón!", "¡Ya basta cabrón!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"Stop it, you bastard!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Ça suffit, salaud ! »")},
        {"q": two("¡Te voy a hacer pedazos!", "¡Te voy a hacer pedazos!"),
         "src": two("Red Dead Redemption multiplayer, in Spanish (quote list of the wiki). Translation: \"I will smash you to pieces!\"",
                    "Multijoueur de Red Dead Redemption, en espagnol (liste de citations du wiki). Traduction : « Je vais te mettre en pièces ! »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("According to their mission pages, \"Civilization, at Any Price\", \"The Demon Drink\", \"Empty Promises\" and \"Cowards Die Many Times\" fail if the player assaults, kills or abandons De Santa. \"Captain De Santa's Downfall\" fails if he is killed before he is captured and made to talk.",
            "D'après leurs pages de mission, \"Civilization, at Any Price\", \"The Demon Drink\", \"Empty Promises\" et \"Cowards Die Many Times\" échouent si le joueur agresse, tue ou abandonne De Santa. \"Captain De Santa's Downfall\" échoue s'il est tué avant d'avoir été capturé et d'avoir parlé."),
        two("According to the Red Dead Wiki, if the player kills De Santa, the game counts him as a civilian kill.",
            "D'après le Red Dead Wiki, si le joueur tue De Santa, le jeu le comptabilise comme un civil."),
        two("According to the mission page of \"Civilization, at Any Price\", the player can climb onto the train during the escort. De Santa then shouts at John to get off, but the mission does not fail, and he eventually stops.",
            "D'après la page de la mission \"Civilization, at Any Price\", le joueur peut grimper sur le train pendant l'escorte. De Santa crie alors à John d'en descendre, mais la mission n'échoue pas, et il finit par se taire."),
        two("According to the mission page of \"The Demon Drink\", if the player disarms Espinoza during the shootout at Tesoro Azul, Espinoza asks: \"Did De Santa make you do this?\"",
            "D'après la page de la mission \"The Demon Drink\", si le joueur désarme Espinoza pendant la fusillade de Tesoro Azul, celui-ci lui demande : \"Did De Santa make you do this?\" (c'est De Santa qui t'a fait faire ça ?)."),
        two("According to the mission page of \"Cowards Die Many Times\", a round of the shooting contest is won by killing five animals with five bullets, and the contest can be played three times.",
            "D'après la page de la mission \"Cowards Die Many Times\", on remporte une manche du concours de tir en abattant cinq animaux avec cinq balles, et le concours peut se disputer trois fois."),
        two("According to the mission page of \"Captain De Santa's Downfall\", De Santa can steal John's horse or shoot at John while he flees. If John rides in front of him, he turns back, so he can be herded like cattle. When disarmed, he keeps drawing a new revolver or rifle. If he is close to the rebels, he fights them and ignores John.",
            "D'après la page de la mission \"Captain De Santa's Downfall\", De Santa peut voler le cheval de John ou lui tirer dessus pendant sa fuite. Si John lui coupe la route à cheval, il fait demi-tour, si bien qu'on peut le rabattre comme du bétail. Désarmé, il sort sans cesse un nouveau revolver ou un nouveau fusil. S'il se trouve près des rebelles, il les affronte et ignore John."),
        two("According to the same page, if the player starts a fistfight with De Santa after the interrogation, the rebels open fire on him, but the following dialogue plays as if John had killed him.",
            "D'après la même page, si le joueur engage un combat à mains nues avec De Santa après l'interrogatoire, les rebelles ouvrent le feu sur lui, mais la suite des dialogues se déroule comme si John l'avait tué."),
        two("According to the mission page of \"The Gates of El Presidio\", when the mission is replayed, Reyes always speaks as if the rebels, not John, had killed De Santa.",
            "D'après la page de la mission \"The Gates of El Presidio\", quand on rejoue la mission, Reyes parle toujours comme si les rebelles, et non John, avaient tué De Santa."),
        two("According to the Red Dead Wiki, when De Santa speaks of the colonel, the subtitles write \"Coronel\", the Spanish word, instead of \"Colonel\".",
            "D'après le Red Dead Wiki, quand De Santa parle du colonel, les sous-titres écrivent \"Coronel\", le mot espagnol, au lieu de \"Colonel\"."),
        two("The mission title \"Cowards Die Many Times\" comes from a line of Shakespeare's Julius Caesar, \"Cowards die many times before their deaths\", according to the mission page.",
            "Le titre de la mission \"Cowards Die Many Times\" vient d'une réplique du Jules César de Shakespeare, \"Cowards die many times before their deaths\" (les lâches meurent plusieurs fois avant leur mort), d'après la page de la mission."),
        two("De Santa shares his surname with Michael De Santa, one of the three playable characters of Grand Theft Auto V (Rockstar, 2013). In that game, De Santa is a false name: the character was born Michael Townley.",
            "De Santa porte le même nom que Michael De Santa, l'un des trois personnages jouables de Grand Theft Auto V (Rockstar, 2013). Dans ce jeu, De Santa est un faux nom : le personnage est né Michael Townley."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("De Santa became a playable character model in the multiplayer mode of Red Dead Redemption with the Myths and Mavericks Bonus Pack. According to the Red Dead Wiki, Rockstar first hinted at this free pack on June 6, 2011, set a September release on July 27 and gave the date and contents on September 1. It was released free on September 13, 2011 on PlayStation 3 and Xbox 360; according to the same wiki, it was the last downloadable content released for the game. It added eight characters to the Revolution section of the Outfitter: Drew MacFarlane, Eli, [[javier-escuella|Javier Escuella]], Jonah, [[landon-ricketts|Landon Ricketts]], [[nastas|Nastas]], [[uncle|Uncle]] and De Santa. His multiplayer lines are in Spanish (see Quotes).",
              "De Santa devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Myths and Mavericks Bonus Pack. D'après le Red Dead Wiki, Rockstar évoque ce pack gratuit pour la première fois le 6 juin 2011, annonce une sortie en septembre le 27 juillet, puis en dévoile la date et le contenu le 1er septembre. Il sort gratuitement le 13 septembre 2011 sur PlayStation 3 et Xbox 360 ; selon le même wiki, c'est le dernier contenu téléchargeable publié pour le jeu. Il ajoute huit personnages à la section Revolution de l'Outfitter : Drew MacFarlane, Eli, [[javier-escuella|Javier Escuella]], Jonah, [[landon-ricketts|Landon Ricketts]], [[nastas|Nastas]], [[uncle|Uncle]] et De Santa. Ses répliques en multijoueur sont en espagnol (voir Citations).")},
    {"p": two("According to its caption on the wiki, a promotional image of the pack shows De Santa in a Stronghold match at Torquemada with Javier Escuella, Drew MacFarlane and Eli. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the De Santa model is not available in them.",
              "D'après sa légende sur le wiki, une image promotionnelle du pack montre De Santa dans une partie de Stronghold à Torquemada, avec Javier Escuella, Drew MacFarlane et Eli. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle de De Santa n'y est donc pas disponible.")},
    {"h4": two("Later games", "Jeux suivants")},
    {"p": two("De Santa does not appear in Red Dead Redemption 2 or in Red Dead Online. The Red Dead Wiki lists him only in Red Dead Redemption and Undead Nightmare.",
              "De Santa n'apparaît ni dans Red Dead Redemption 2 ni dans Red Dead Online. Le Red Dead Wiki ne le recense que dans Red Dead Redemption et Undead Nightmare.")},
]
