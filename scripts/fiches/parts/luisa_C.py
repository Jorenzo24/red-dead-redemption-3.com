"""Luisa Fortuna, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN and FR, fetched Oct 2026; shared cache scripts/v3/work/_m/):
- Character page "Luisa Fortuna" (EN: Mission appearances, Quotes, Trivia, Gallery captions; FR: Apparitions dans les
  missions, Anecdotes incl. the Rockstar website background).
- Mission pages (infobox order numbers, givers, start and end points, prerequisites, rewards, unlocks, failure
  conditions, trivia): "Landon Ricketts Rides Again" (31st), "The Mexican Wagon Train" (33rd), "My Sister's Keeper"
  (34th), "Must a Savior Die?" (35th), "Father Abraham" (38th), "Captain De Santa's Downfall" (39th), "The Gates of
  El Presidio" (40th), "An Appointed Time" (41st).
- Transcripts used word for word for every quote: "Landon Ricketts Rides Again/dialogues", "The Mexican Wagon
  Train/dialogues", "My Sister's Keeper/dialogues", "Must a Savior Die?/dialogues", "Father Abraham/dialogues",
  "Captain De Santa's Downfall/dialogues", "The Gates of El Presidio/dialogues", "An Appointed Time/dialogues".
- Other wiki pages: "Sepulcro" (marked graves: "Alejandro Fortuna / Died August 14, 1909. / \"He died for his
  country.\""), "Liars and Cheats" (third DLC pack, released Tuesday, September 21, 2010; 15 story characters;
  Redemption section of the Outfitter lists Abigail, Bonnie, Jack, John, Leigh Johnson, Luisa, Nigel West Dickens,
  Seth Briars), "Campo Mirada" (house intact in multiplayer).
- Real world: Liars and Cheats Pack detailed by Rockstar on August 27, 2010 and released on September 21, 2010 (as in
  abigail_C, bonnie_C, leigh_C); RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 without multiplayer
  (as in desanta_C, allende_C, landon_C).

VERIFIED POINTS: Luisa gives four missions ("My Sister's Keeper", "Must a Savior Die?", "Father Abraham", "Captain De
Santa's Downfall"); Ricketts gives the first two in which she appears, Reyes the last. "My Sister's Keeper" requires
"Landon Ricketts Rides Again" and "Civilization, at Any Price" (prerequisites section; its infobox says "The Mexican
Wagon Train": the walkthrough section is followed, as in desanta_C, where "Civilization, at Any Price" unlocks her
strand). "Father Abraham" requires "Cowards Die Many Times" and "Must a Savior Die?". The writer's name is "Castillo"
in the transcript and "Castilla" in the mission page's gallery captions and trivia. Every quote below is checked
against a transcript; the wiki quote list's "Déjen mi hombre-" is "Déjen mi hombre!" in the transcript (transcript
followed).

FIX (21 Oct 2026): Quotes now carry the porch lines ("My heart is breaking, but I cry for Mexico"), "in our hearts, we are
married already", "Great and terrible things!", the naive/cynic exchange, "Good actions make you a good man", "Allende es
pura maldad" and Reyes's Agave Viejo lines ("hands of a farmer"), so that every "(see Quotes)" in part B resolves.
Dropped from Quotes (owned by part B): Victor's "She can fight as well as any man" and both "Laura" exchanges.
EXCLUDED: the four lines quoted in part B "In her own words"; the "Flowering Judas"
parallel (interpretation); the surname "luck" irony (interpretation; the meaning belongs to Names, part B); the
pre-release face (cut content, part D); the "tight c*nt" line attributed to Reyes (no transcript); the PS3 bug in
which Luisa vanishes and the other glitches (no bearing on the character); the mission page's "her prompts are not
always accurate" and the "I thought you said you were good with explosives!" line (PS3 note, no transcript; given
without quotation marks); the gallery caption "Luisa is serenaded by Abraham Reyes" (told in part A); the Miranda
page's age speculation.

OWNERSHIP: narrative events live in part A (one line per mission here). Quotes are exchanges and lines by other
characters; Luisa's single-line statements are left to part B. Trivia keeps only facts told nowhere else.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A2 = two("Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Luisa appears in seven story missions of Red Dead Redemption, all in the second act, set in Nuevo Paraíso. Her own strand has four missions, which all start at Campo Mirada. It becomes available after \"Landon Ricketts Rides Again\", given by [[landon-ricketts|Landon Ricketts]], and \"Civilization, at Any Price\", given by [[vincente-de-santa|Vincente de Santa]]. She is also discussed in one mission given by [[abraham-reyes|Abraham Reyes]].",
              "Luisa apparaît dans sept missions principales de Red Dead Redemption, toutes dans le deuxième acte, au Nuevo Paraíso. Sa propre série compte quatre missions, qui partent toutes de Campo Mirada. Elle se débloque après \"Landon Ricketts Rides Again\", confiée par [[landon-ricketts|Landon Ricketts]], et \"Civilization, at Any Price\", confiée par [[vincente-de-santa|Vincente de Santa]]. Il est aussi question d'elle dans une mission confiée par [[abraham-reyes|Abraham Reyes]].")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Luisa's role", "Rôle de Luisa")], "rows": [
        M("Landon Ricketts Rides Again", A2,
          "Prisoner of the army in the caves near El Matadero; freed by Ricketts and [[john-marston|John Marston]], then taken to safety by Carlos. 31st mission, given by Ricketts in Chuparosa. Rewards: 50 honor and 75 fame; with \"Civilization, at Any Price\", opens her strand.",
          "Prisonnière de l'armée dans les grottes près d'El Matadero ; libérée par Ricketts et [[john-marston|John Marston]], puis mise à l'abri par Carlos. 31e mission, confiée par Ricketts à Chuparosa. Récompenses : 50 points d'honneur et 75 de célébrité ; ouvre sa série, avec \"Civilization, at Any Price\"."),
        M("The Mexican Wagon Train", A2,
          "Reports that Allende is sending untried prisoners to their deaths near Escalera, which sets off the convoy raid. 33rd mission, given by Ricketts. Reward: 150 fame.",
          "Annonce qu'Allende envoie des prisonniers à la mort sans procès près d'Escalera, ce qui déclenche l'attaque du convoi. 33e mission, confiée par Ricketts. Récompense : 150 points de célébrité."),
        M("My Sister's Keeper", A2,
          "Mission giver. Asks John to drive her sister Miranda to the docks of Puerto Cuchillo before her boat leaves. 34th mission, from Campo Mirada. Rewards: 100 honor and 75 fame.",
          "Donneuse de mission. Demande à John de conduire sa sœur Miranda jusqu'aux quais de Puerto Cuchillo avant le départ de son bateau. 34e mission, au départ de Campo Mirada. Récompenses : 100 points d'honneur et 75 de célébrité."),
        M("Must a Savior Die?", A2,
          "Mission giver. Drives John to El Presidio to save Reyes from a firing squad and waits for them by the river. 35th mission. Rewards: 50 honor and 200 fame; unlocks the stranger mission \"Aztec Gold\".",
          "Donneuse de mission. Conduit John jusqu'à El Presidio pour sauver Reyes du peloton d'exécution, puis les attend au bord du fleuve. 35e mission. Récompenses : 50 points d'honneur et 200 de célébrité ; débloque la mission d'inconnu \"Aztec Gold\"."),
        M("Father Abraham", A2,
          "Mission giver. Announces her father's death and has John blow up an army supply convoy at the Frontera Bridge. 38th mission; requires \"Cowards Die Many Times\" and \"Must a Savior Die?\". Rewards: 125 honor and 200 fame.",
          "Donneuse de mission. Annonce la mort de son père et fait sauter par John un convoi de ravitaillement de l'armée au pont de Frontera. 38e mission ; exige d'avoir terminé \"Cowards Die Many Times\" et \"Must a Savior Die?\". Récompenses : 125 points d'honneur et 200 de célébrité."),
        M("Captain De Santa's Downfall", A2,
          "Mission giver. Sends John and her men to stop De Santa's massacre at Sepulcro. 39th mission, from Campo Mirada to Casa Madrugada. Rewards: 125 honor and 300 fame.",
          "Donneuse de mission. Envoie John et ses hommes empêcher le massacre de De Santa à Sepulcro. 39e mission, de Campo Mirada à Casa Madrugada. Récompenses : 125 points d'honneur et 300 de célébrité."),
        M("An Appointed Time", A2,
          "Killed in Escalera while trying to save Reyes from execution; John avenges her in a duel with Major Raul Zubieta. 41st mission, given by Reyes, the last of the act. Rewards: 300 fame and up to 535 honor; opens West Elizabeth.",
          "Tuée à Escalera en tentant d'arracher Reyes à son exécution ; John la venge en duel contre le commandant Raul Zubieta. 41e mission, confiée par Reyes, la dernière de l'acte. Récompenses : 300 points de célébrité et jusqu'à 535 points d'honneur ; ouvre le West Elizabeth."),
    ]}},
    {"h4": two("Mission in which she is mentioned", "Mission où elle est évoquée")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Link with Luisa", "Lien avec Luisa")], "rows": [
        M("The Gates of El Presidio", A2,
          "At Agave Viejo, John asks Reyes what Luisa would think of the woman he is with; Reyes laughs at the idea of marrying her (see Biography). 40th mission, given by Reyes.",
          "À Agave Viejo, John demande à Reyes ce que Luisa penserait de la femme qui l'accompagne ; Reyes se moque de l'idée de l'épouser (voir la biographie). 40e mission, confiée par Reyes."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English and checked against the mission transcripts of the Red Dead Wiki. Most are exchanges between Luisa and John Marston, or lines that other characters say about her.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction, et vérifiées sur les transcriptions de missions du Red Dead Wiki. Il s'agit pour l'essentiel d'échanges entre Luisa et John Marston, ou de répliques d'autres personnages à son sujet.")},
    {"h4": two("Red Dead Redemption, Act II", "Red Dead Redemption, acte II")},
    {"quotes": [
        {"q": two("But they do have his sister. Emilio's I mean. She's a fine young woman, teacher, a human being. Not the clothed vermin so many people seemed to have turned into.", "But they do have his sister. Emilio's I mean. She's a fine young woman, teacher, a human being. Not the clothed vermin so many people seemed to have turned into."),
         "src": two("Landon Ricketts, Landon Ricketts Rides Again (RDR1, Act II), at the hotel in Chuparosa",
                    "Landon Ricketts, Landon Ricketts Rides Again (RDR1, acte II), à l'hôtel de Chuparosa. Traduction : « Mais ils détiennent sa sœur. Celle d'Emilio, je veux dire. Une jeune femme bien, institutrice, un être humain. Pas comme cette vermine en habits que tant de gens semblent être devenus. »")},
        {"q": two("Luisa: Thank you for saving me. You're good men. Friends of the people of this land. / Landon: Was someone named Javier Escuella one of the men holding you? / Luisa: No...I don't know. I don't think so. But, I remember that name from prison. Bad people spoke of him.", "Luisa: Thank you for saving me. You're good men. Friends of the people of this land. / Landon: Was someone named Javier Escuella one of the men holding you? / Luisa: No...I don't know. I don't think so. But, I remember that name from prison. Bad people spoke of him."),
         "src": two("Landon Ricketts Rides Again (RDR1, Act II), after the escape from the caves",
                    "Landon Ricketts Rides Again (RDR1, acte II), après la fuite hors des grottes. Traduction : « Luisa : Merci de m'avoir sauvée. Vous êtes des hommes bons. Des amis du peuple de cette terre. / Landon : Est-ce qu'un certain Javier Escuella faisait partie des hommes qui vous retenaient ? / Luisa : Non... Je ne sais pas. Je ne crois pas. Mais je me souviens de ce nom, en prison. Des gens mauvais parlaient de lui. »")},
        {"q": two("Marston: Luisa was pretty shaken up. / Landon: She's angry. This war is getting dirtier by the day. People are being executed just for having an opinion.", "Marston: Luisa was pretty shaken up. / Landon: She's angry. This war is getting dirtier by the day. People are being executed just for having an opinion."),
         "src": two("The Mexican Wagon Train (RDR1, Act II), on the trail to Escalera",
                    "The Mexican Wagon Train (RDR1, acte II), sur la piste d'Escalera. Traduction : « Marston : Luisa était drôlement secouée. / Landon : Elle est en colère. Cette guerre devient plus sale de jour en jour. On exécute des gens rien que pour avoir une opinion. »")},
        {"q": two("Talk to Luisa. She'll help you and she's well-connected in that other land.", "Talk to Luisa. She'll help you and she's well-connected in that other land."),
         "src": two("Landon Ricketts, The Mexican Wagon Train (RDR1, Act II), parting from John on the American side of the border",
                    "Landon Ricketts, The Mexican Wagon Train (RDR1, acte II), en quittant John du côté américain de la frontière. Traduction : « Va voir Luisa. Elle t'aidera, et elle a ses entrées de l'autre côté. »")},
        {"q": two("Luisa: Great and terrible things! The revolution is coming! The country will be in turmoil once more. This time, we hope is the last time. / Marston: Does that seem likely? / Luisa: With Abraham Reyes, anything is possible!", "Luisa: Great and terrible things! The revolution is coming! The country will be in turmoil once more. This time, we hope is the last time. / Marston: Does that seem likely? / Luisa: With Abraham Reyes, anything is possible!"),
         "src": two("My Sister's Keeper (RDR1, Act II), at Campo Mirada, when John asks what is happening",
                    "My Sister's Keeper (RDR1, acte II), à Campo Mirada, quand John demande ce qui se passe. Traduction : « Luisa : De grandes et terribles choses ! La révolution arrive ! Le pays va de nouveau être plongé dans le chaos. Cette fois, nous l'espérons, ce sera la dernière. / Marston : Ça vous paraît probable ? / Luisa : Avec Abraham Reyes, tout est possible ! »")},
        {"q": two("Marston: Your nobility's almost as affecting as your naivety. / Luisa: I would rather be dead than a cynic like you, Mr. Marston. / Marston: I would too... / Luisa: I know you're not really like that. You saved me.", "Marston: Your nobility's almost as affecting as your naivety. / Luisa: I would rather be dead than a cynic like you, Mr. Marston. / Marston: I would too... / Luisa: I know you're not really like that. You saved me."),
         "src": two("My Sister's Keeper (RDR1, Act II), at Campo Mirada, after she tells John not to worry about her",
                    "My Sister's Keeper (RDR1, acte II), à Campo Mirada, après qu'elle a dit à John de ne pas s'inquiéter pour elle. Traduction : « Marston : Votre noblesse est presque aussi touchante que votre naïveté. / Luisa : Je préférerais être morte plutôt que cynique comme vous, Mr. Marston. / Marston : Moi aussi... / Luisa : Je sais que vous n'êtes pas vraiment comme ça. Vous m'avez sauvée. »")},
        {"q": two("Luisa: Mr. Marston, can I ask one more favor of you? Can you take my sister to the docks? We are sending her to work for a kind man in the Yucatán. She is too young for revolution. / Marston: Okay. Anything I can do to help out.", "Luisa: Mr. Marston, can I ask one more favor of you? Can you take my sister to the docks? We are sending her to work for a kind man in the Yucatán. She is too young for revolution. / Marston: Okay. Anything I can do to help out."),
         "src": two("My Sister's Keeper (RDR1, Act II), at Campo Mirada",
                    "My Sister's Keeper (RDR1, acte II), à Campo Mirada. Traduction : « Luisa : Monsieur Marston, puis-je vous demander encore un service ? Pouvez-vous emmener ma sœur jusqu'aux quais ? Nous l'envoyons travailler pour un homme bon dans le Yucatán. Elle est trop jeune pour la révolution. / Marston : D'accord. Si je peux rendre service. »")},
        {"q": two("Luisa: I don't weep for myself, but for my country! Abraham Reyes has been captured! / Marston: He has? / Luisa: He was coming to meet me at Roca Madera. It's a very romantic spot. It was a beautiful night, yet he was ambushed by a patrol. My heart is breaking, but I cry for Mexico.", "Luisa: I don't weep for myself, but for my country! Abraham Reyes has been captured! / Marston: He has? / Luisa: He was coming to meet me at Roca Madera. It's a very romantic spot. It was a beautiful night, yet he was ambushed by a patrol. My heart is breaking, but I cry for Mexico."),
         "src": two("Must a Savior Die? (RDR1, Act II), on the porch of the burned house at Campo Mirada",
                    "Must a Savior Die? (RDR1, acte II), sur le perron de la maison incendiée de Campo Mirada. Traduction : « Luisa : Ce n'est pas sur moi que je pleure, mais sur mon pays ! Abraham Reyes a été capturé ! / Marston : Ah bon ? / Luisa : Il venait me retrouver à Roca Madera. C'est un endroit très romantique. La nuit était belle, et pourtant une patrouille lui a tendu une embuscade. J'ai le cœur brisé, mais c'est pour le Mexique que je pleure. »")},
        {"q": two("El Presidio... You know, in our hearts, we are married already, but his family does not approve.", "El Presidio... You know, in our hearts, we are married already, but his family does not approve."),
         "src": two("Luisa, Must a Savior Die? (RDR1, Act II), when John asks where Reyes is held",
                    "Luisa, Must a Savior Die? (RDR1, acte II), quand John demande où Reyes est détenu. Traduction : « El Presidio... Vous savez, dans nos cœurs, nous sommes déjà mariés, mais sa famille n'approuve pas. »")},
        {"q": two("Marston: Luisa sent me. We have to meet her by the river. / Abraham: Que? / Marston: Luisa. The girl you're marrying. / Abraham: Oh, yes. Such a devoted thing. El amor de mi vida.", "Marston: Luisa sent me. We have to meet her by the river. / Abraham: Que? / Marston: Luisa. The girl you're marrying. / Abraham: Oh, yes. Such a devoted thing. El amor de mi vida."),
         "src": two("Must a Savior Die? (RDR1, Act II), at El Presidio, after John cuts Reyes free",
                    "Must a Savior Die? (RDR1, acte II), à El Presidio, après que John a détaché Reyes. Traduction : « Marston : C'est Luisa qui m'envoie. On doit la rejoindre au bord du fleuve. / Abraham : Quoi ? / Marston : Luisa. La fille que tu vas épouser. / Abraham : Ah, oui. Une petite si dévouée. L'amour de ma vie. »")},
        {"q": two("Luisa: My father must not die in vain! His death must mean something. / Marston: It'll mean that war is brutal and unnecessary and good people die and that's all it will mean. / Luisa: That is not enough.", "Luisa: My father must not die in vain! His death must mean something. / Marston: It'll mean that war is brutal and unnecessary and good people die and that's all it will mean. / Luisa: That is not enough."),
         "src": two("Father Abraham (RDR1, Act II), by the campfire, after she announces her father's death",
                    "Father Abraham (RDR1, acte II), près du feu de camp, après l'annonce de la mort de son père. Traduction : « Luisa : Mon père ne doit pas être mort pour rien ! Sa mort doit avoir un sens. / Marston : Elle voudra dire que la guerre est brutale et inutile, que des gens bien meurent, et c'est tout ce qu'elle voudra dire. / Luisa : Ça ne suffit pas. »")},
        {"q": two("Luisa: We all have problems. This is about the people! My father died for his people. For these men and for millions like them, that they may be free. / Marston: While there are guns and money, there won't be any freedom, Luisa.", "Luisa: We all have problems. This is about the people! My father died for his people. For these men and for millions like them, that they may be free. / Marston: While there are guns and money, there won't be any freedom, Luisa."),
         "src": two("Father Abraham (RDR1, Act II), by the campfire",
                    "Father Abraham (RDR1, acte II), près du feu de camp. Traduction : « Luisa : Nous avons tous des problèmes. Il s'agit du peuple ! Mon père est mort pour son peuple. Pour ces hommes et pour des millions d'autres comme eux, afin qu'ils soient libres. / Marston : Tant qu'il y aura des armes et de l'argent, il n'y aura pas de liberté, Luisa. »")},
        {"q": two("Luisa: Mr. Marston. I have lost my father. My mother is in the United States. My sister has fled. I have no family, just the cause. Please. Good actions make you a good man. / Marston: Then, I'm doomed, but I will help you, out of respect for your loss.", "Luisa: Mr. Marston. I have lost my father. My mother is in the United States. My sister has fled. I have no family, just the cause. Please. Good actions make you a good man. / Marston: Then, I'm doomed, but I will help you, out of respect for your loss."),
         "src": two("Father Abraham (RDR1, Act II), by the campfire, when John says he has his own family to worry about",
                    "Father Abraham (RDR1, acte II), près du feu de camp, quand John répond qu'il a sa propre famille à protéger. Traduction : « Luisa : Mr. Marston. J'ai perdu mon père. Ma mère est aux États-Unis. Ma sœur a fui. Je n'ai plus de famille, seulement la cause. Je vous en prie. Ce sont les bonnes actions qui font un homme bon. / Marston : Alors je suis perdu, mais je vais vous aider, par respect pour votre deuil. »")},
        {"q": two("Marston: Allende betrayed me, and I saw him do bad things. Things that disgust even me. / Luisa: Allende es pura maldad. One day I will cut his heart out.", "Marston: Allende betrayed me, and I saw him do bad things. Things that disgust even me. / Luisa: Allende es pura maldad. One day I will cut his heart out."),
         "src": two("Father Abraham (RDR1, Act II), on the way to the Frontera Bridge; \"Allende es pura maldad\" means \"Allende is pure evil\"",
                    "Father Abraham (RDR1, acte II), en route vers le pont de Frontera ; \"Allende es pura maldad\" est en espagnol dans la version originale. Traduction : « Marston : Allende m'a trahi, et je l'ai vu faire des choses horribles. Des choses qui dégoûtent même un type comme moi. / Luisa : Allende, c'est le mal à l'état pur. Un jour, je lui arracherai le cœur. »")},
        {"q": two("Luisa: You Americans forget too quickly, that is the problem. If it wasn't for your revolution, you would still be making tea for the English. / Marston: At least we knew where we stood. It's more difficult to understand why your own people treat you like shit.", "Luisa: You Americans forget too quickly, that is the problem. If it wasn't for your revolution, you would still be making tea for the English. / Marston: At least we knew where we stood. It's more difficult to understand why your own people treat you like shit."),
         "src": two("Father Abraham (RDR1, Act II), on the way to the Frontera Bridge",
                    "Father Abraham (RDR1, acte II), en route vers le pont de Frontera. Traduction : « Luisa : Vous, les Américains, vous oubliez trop vite, voilà le problème. Sans votre révolution, vous serviriez encore le thé aux Anglais. / Marston : Au moins, on savait où on en était. C'est plus dur de comprendre pourquoi ton propre peuple te traite comme de la merde. »")},
        {"q": two("Luisa: What is his name? / Marston: Jack. Jack Marston. I ain't been much of a father. We tried to hide the bad from him growin' up but he saw things he shouldn't. / Luisa: Children see more than you think / Marston: That's what I'm worried about. I don't want him to become a man like me.", "Luisa: What is his name? / Marston: Jack. Jack Marston. I ain't been much of a father. We tried to hide the bad from him growin' up but he saw things he shouldn't. / Luisa: Children see more than you think / Marston: That's what I'm worried about. I don't want him to become a man like me."),
         "src": two("Father Abraham (RDR1, Act II), on the way to the Frontera Bridge, after she asks John whether he has children",
                    "Father Abraham (RDR1, acte II), en route vers le pont de Frontera, après qu'elle a demandé à John s'il avait des enfants. Traduction : « Luisa : Comment s'appelle-t-il ? / Marston : Jack. Jack Marston. J'ai pas été un bien bon père. On a essayé de lui cacher le pire quand il grandissait, mais il a vu des choses qu'il n'aurait pas dû voir. / Luisa : Les enfants voient plus de choses qu'on ne le croit. / Marston : C'est bien ce qui m'inquiète. Je ne veux pas qu'il devienne un homme comme moi. »")},
        {"q": two("Luisa: No, destroy them! And kill everyone. Abraham wants to send a message. Do you have experience with explosives? / Marston: A little. Been a long time. / Luisa: Good. Because we do not.", "Luisa: No, destroy them! And kill everyone. Abraham wants to send a message. Do you have experience with explosives? / Marston: A little. Been a long time. / Luisa: Good. Because we do not."),
         "src": two("Father Abraham (RDR1, Act II), when John asks whether they are going to steal the army's supplies",
                    "Father Abraham (RDR1, acte II), quand John demande s'ils vont voler le ravitaillement de l'armée. Traduction : « Luisa : Non, les détruire ! Et tuer tout le monde. Abraham veut faire passer un message. Vous avez l'expérience des explosifs ? / Marston : Un peu. Ça remonte. / Luisa : Tant mieux. Parce que nous, non. »")},
        {"q": two("Marston: What would your most loyal follower, Luisa say about that? / Abraham: Who? / Marston: Luisa. The girl from Campo Mirada. / Abraham: Ah, her. A gentleman never tells, but she was a most wonderful, ay... I just say she was incredible, yes. Let me tell you something. I strongly recommend her. You take her when you have the chance, my brother. (...) / Marston: Are you going to marry her? / Abraham: Marry a peasant? My dear boy, don't be absurd. I'm going to be the next president of Mexico. My wife will meet ambassadors, kings, other great men. The very thought that I would marry some peasant girl with the hands of a farmer, well I really don't think so.", "Marston: What would your most loyal follower, Luisa say about that? / Abraham: Who? / Marston: Luisa. The girl from Campo Mirada. / Abraham: Ah, her. A gentleman never tells, but she was a most wonderful, ay... I just say she was incredible, yes. Let me tell you something. I strongly recommend her. You take her when you have the chance, my brother. (...) / Marston: Are you going to marry her? / Abraham: Marry a peasant? My dear boy, don't be absurd. I'm going to be the next president of Mexico. My wife will meet ambassadors, kings, other great men. The very thought that I would marry some peasant girl with the hands of a farmer, well I really don't think so."),
         "src": two("The Gates of El Presidio (RDR1, Act II), at Agave Viejo",
                    "The Gates of El Presidio (RDR1, acte II), à Agave Viejo. Traduction : « Marston : Qu'en dirait ta plus fidèle partisane, Luisa ? / Abraham : Qui ? / Marston : Luisa. La fille de Campo Mirada. / Abraham : Ah, elle. Un gentleman ne raconte pas ces choses-là, mais elle était des plus merveilleuses, ay... Disons simplement qu'elle était incroyable, oui. Laisse-moi te dire une chose : je te la recommande vivement. Prends-la dès que tu en as l'occasion, mon frère. (...) / Marston : Tu vas l'épouser ? / Abraham : Épouser une paysanne ? Mon cher, ne sois pas ridicule. Je vais être le prochain président du Mexique. Ma femme recevra des ambassadeurs, des rois, d'autres grands hommes. L'idée même que j'épouse une petite paysanne aux mains de fermière, non, vraiment, je ne crois pas. »")},
        {"q": two("Abraham: Ya, ya matalo. / Luisa: Déjen mi hombre! / Raul: Ay, Dios mio! Santa Maria! / Marston: You want to settle this now, friend? Or do you want me to shoot you in the head right now, for that poor girl?", "Abraham: Ya, ya matalo. / Luisa: Déjen mi hombre! / Raul: Ay, Dios mio! Santa Maria! / Marston: You want to settle this now, friend? Or do you want me to shoot you in the head right now, for that poor girl?"),
         "src": two("An Appointed Time (RDR1, Act II), in the square of Escalera; Luisa's last words. Reyes's and Luisa's lines are in Spanish in the original",
                    "An Appointed Time (RDR1, acte II), sur la place d'Escalera ; ce sont les derniers mots de Luisa. Les répliques de Reyes et de Luisa sont en espagnol dans la version originale. Traduction : « Abraham : Allez, tue-le. / Luisa : Laissez mon homme ! / Raul : Mon Dieu ! Sainte Marie ! / Marston : Tu veux régler ça maintenant, l'ami ? Ou tu préfères que je te mette une balle dans la tête tout de suite, pour cette pauvre fille ? »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("According to the mission page of \"Father Abraham\", Luisa calls out when to set off the charges, but her timing is not always right. The page says she can also criticize John's handling of the explosives even after a direct hit (noted on PlayStation 3).",
            "D'après la page de la mission \"Father Abraham\", Luisa indique à John le moment de déclencher les charges, mais elle ne tombe pas toujours juste. Toujours selon cette page, elle peut aussi critiquer sa façon de manier les explosifs même après un tir parfait (remarqué sur PlayStation 3)."),
        two("According to the same page, \"Father Abraham\" is the first mission in which John says his son's name aloud.",
            "Selon la même page, \"Father Abraham\" est la première mission où John prononce le prénom de son fils."),
        two("The mission page of \"The Mexican Wagon Train\" spells the writer's name Castilla. None of the prisoners it names seems to be that writer or the official Luisa mentions.",
            "La page de la mission \"The Mexican Wagon Train\" orthographie Castilla le nom de l'écrivain. Aucun des prisonniers qu'elle cite ne semble être cet écrivain, ni le fonctionnaire dont parle Luisa."),
        two("According to the mission page of \"An Appointed Time\", Luisa falls on her back when she is shot, but lies face down once the cutscene ends.",
            "D'après la page de la mission \"An Appointed Time\", Luisa tombe sur le dos quand on l'abat, mais elle est étendue face contre terre une fois la cinématique terminée."),
        two("The cemetery of Sepulcro has a grave in the name of Alejandro Fortuna, who died on August 14, 1909; its epitaph reads \"He died for his country.\" according to the Red Dead Wiki's list of the graves. No dialogue links him to Luisa's family.",
            "Le cimetière de Sepulcro abrite la tombe d'un certain Alejandro Fortuna, mort le 14 août 1909 ; d'après la liste des tombes établie par le Red Dead Wiki, son épitaphe indique \"He died for his country.\" (il est mort pour son pays). Aucun dialogue ne le rattache à la famille de Luisa."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Luisa became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. The pack added 15 characters from the story, as well as Poker, Liar's Dice, horse races and the Stronghold mode. Players select her in the Redemption section of the Outfitter, alongside [[john-marston|John]], [[abigail-marston|Abigail]], [[jack-marston|Jack]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[leigh-johnson|Leigh Johnson]], [[nigel-west-dickens|Nigel West Dickens]] and [[seth-briars|Seth Briars]]. According to the Red Dead Wiki, she wears a dress throughout the story, while her multiplayer model is given chaps, a change also made to Abigail's model. Her family's house at Campo Mirada, which burns in the story, is still standing in multiplayer, according to the wiki.",
              "Luisa devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. Ce pack ajoute 15 personnages de l'histoire, ainsi que le poker, le poker menteur, des courses de chevaux et le mode Stronghold. On la choisit dans la section Redemption de l'Outfitter, aux côtés de [[john-marston|John]], [[abigail-marston|Abigail]], [[jack-marston|Jack]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[leigh-johnson|Leigh Johnson]], [[nigel-west-dickens|Nigel West Dickens]] et [[seth-briars|Seth Briars]]. D'après le Red Dead Wiki, elle porte une robe tout au long de l'histoire, alors que son modèle multijoueur porte des jambières de cuir (chaps), une modification également apportée au modèle d'Abigail. Toujours selon le wiki, la maison familiale de Campo Mirada, incendiée dans l'histoire, est encore debout en multijoueur.")},
    {"p": two("The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, contain the story and Undead Nightmare but not the multiplayer mode, so the Luisa model is not available in them.",
              "Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, mais pas le multijoueur : le modèle de Luisa n'y est donc pas disponible.")},
    {"h4": two("Later games", "Jeux suivants")},
    {"p": two("Luisa does not appear in Red Dead Redemption 2 or in Red Dead Online. The Red Dead Wiki lists her only in Red Dead Redemption, and as a character model in Undead Nightmare (see Biography).",
              "Luisa n'apparaît ni dans Red Dead Redemption 2 ni dans Red Dead Online. Le Red Dead Wiki ne la recense que dans Red Dead Redemption, et comme modèle de personnage dans Undead Nightmare (voir la biographie).")},
]
