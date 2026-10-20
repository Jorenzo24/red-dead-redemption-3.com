"""Karen Jones, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/karen/ and cov/karen/m/):
- Red Dead Wiki EN "Karen Jones" (Mission Appearances, Trivia, Gallery captions) and FR "Karen Jones" (fr.txt: same
  twelve missions; cites Rockstar's French "vanderlindegang" page, archived on July 6, 2022).
- Transcripts "/dialogues": Outlaws from the West; Polite Society, Valentine Style; Who is Not Without Sin; Sodom? Back
  to Gomorrah; Blessed are the Peacemakers. Every quoted line below is checked word for word against them. Enter,
  Pursued by a Memory and Eastward Bound transcripts: no line for Karen. No transcript exists on the wiki for Blood
  Feuds, The Battle of Shady Belle (the local .dlg has no Karen line), Angelo Bronte, Horsemen, That's Murfree
  Country, A Rage Unleashed or Our Best Selves (checked Oct 2026).
- Mission pages: Polite Society (failure conditions, Gold Medal "Find Karen within 45 seconds", deaths, trivia: the
  lyric slip kept from the recording, no weapons in the hotel); Sodom (reward, deaths, failure conditions); Blessed are
  the Peacemakers; Horsemen, Apocalypses (balcony); A Rage Unleashed; My Last Boy and Our Best Selves (trivia: no
  longer at camp); "Letter from Tilly" (tilly/fcB); "Camp Events" (availability: Karen unavailable in camp while
  Sodom is unlocked).
- Real world: Rockstar's character portraits and descriptions posted on Twitter on September 6, 2018, reproduced by
  The Hollywood Reporter on September 7, 2018 (../uncle/fc/thr_descriptions.txt: "Karen Jones" entry present);
  Wikipedia "List of Red Dead Redemption 2 characters" (caption of the 23-member composite: front row, between
  Mary-Beth and Abigail).
Ownership (FIX_RULES), left to other parts: all narrative (A); the Tucson job (A Origins); personality, the Rockstar
and guide descriptions as text, names, appearance (hair over the game, covered face in chapter 1, the robbery costume),
guard duty, songs, camp scenes and camp lines (Sean, Molly, Susan, Micah, John, Kieran, Tilly's worry about her
drinking, the Blackwater memory, the dance) (B); Jo Armeniox, interviews, reception (D).
Quotes: mission lines only, each in ONE place; part A paraphrases them. The two lines quoted in part B "In her own
words" ("Thank you, Arthur...", "You've always been a bad drunk...") are not repeated here. Tilly's "a sister to me" is
quoted in the Tilly relationship entry (B) only. Trivia removed as duplicates (fact-check 20 Oct 2026): the lyric slip
(now in D, Recording) and the shotgun in "A Rage Unleashed" (B, Weapons).
Kills: the character page has no "Murders Committed" section; the only deaths credited to her are unnamed Valentine
lawmen, shared with Arthur, Bill and Lenny (Sodom mission page): no kills table.
Excluded: "nobody plays the drunken harlot quiet like me" (transcript typo for "quite": not quoted); "This is a goddam
robbery!" (inconsistent spelling in the transcript); the wiki trivia on hair, guard duty, covered face, the dance and
the Blackwater memory (part B); the wiki trivia that Tilly's chapter 6 worry "foreshadows" the letter (interpretation;
the Camp Events page also files that scene under the Shady Belle chapter, not chapter 6); "Susan was the only camp
woman who witnessed her departure" (Our Best Selves trivia, unsupported).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
EP2 = two("Epilogue 2: Beecher's Hope", "Épilogue 2 : Beecher's Hope")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English and French Red Dead Wikis list the same twelve story missions of Red Dead Redemption 2 for Karen. The table below adds the mission in which she has a single line in camp, the mission that confirms her departure, and the letter that mentions her in the epilogue.",
              "Les Red Dead Wiki anglais et français recensent les mêmes douze missions principales de Red Dead Redemption 2 pour Karen. Le tableau ci-dessous y ajoute la mission où elle a une seule réplique au camp, celle qui confirme son départ, et la lettre qui parle d'elle dans l'épilogue.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 to 6", "Red Dead Redemption 2, chapitres 1 à 6")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Karen's role", "Rôle de Karen")], "rows": [
        M("Outlaws from the West", C1,
          "At Colter. [[susan-grimshaw|Susan Grimshaw]] sends her for blankets, and [[dutch-van-der-linde|Dutch]] asks her and [[tilly-jackson|Tilly]] to look after [[sadie-adler|Sadie Adler]].",
          "À Colter. [[susan-grimshaw|Susan Grimshaw]] l'envoie chercher des couvertures, et [[dutch-van-der-linde|Dutch]] lui demande, ainsi qu'à [[tilly-jackson|Tilly]], de s'occuper de [[sadie-adler|Sadie Adler]]."),
        M("Enter, Pursued by a Memory", C1,
          "Listed by the Red Dead Wiki; no line in the transcript.",
          "Citée par le Red Dead Wiki ; aucune réplique dans la transcription."),
        M("Eastward Bound", C1,
          "Moves down to Horseshoe Overlook with the gang; no line in the transcript.",
          "Descend à Horseshoe Overlook avec la bande ; aucune réplique dans la transcription."),
        M("Polite Society, Valentine Style", C2,
          "Rides to Valentine with [[arthur-morgan|Arthur]], [[uncle|Uncle]], Tilly and [[mary-beth-gaskill|Mary-Beth]]. A client she tries to rob at the Saints Hotel beats her until Arthur steps in; she learns about the Valentine bank.",
          "Part pour Valentine avec [[arthur-morgan|Arthur]], [[uncle|Uncle]], Tilly et [[mary-beth-gaskill|Mary-Beth]]. Un client qu'elle tente de voler au Saints Hotel la frappe jusqu'à l'intervention d'Arthur ; elle entend parler de la banque de Valentine."),
        M("Who is Not Without Sin", C2,
          "At camp. Comments as Arthur carries a drunk [[orville-swanson|Reverend Swanson]] to his tent. Not listed by the wiki.",
          "Au camp. Réagit quand Arthur ramène sous sa tente le [[orville-swanson|révérend Swanson]], ivre. Mission non citée par le wiki."),
        M("Sodom? Back to Gomorrah", C3,
          "Co-planner. Distracts the bank staff as a lost girl or a drunken harlot, then holds up the Valentine bank with Arthur, [[bill-williamson|Bill]] and [[lenny-summers|Lenny]]. Reward for the player: $2,500 and a Springfield Rifle.",
          "Coorganisatrice. Détourne l'attention du personnel en jeune fille perdue ou en catin ivre, puis braque la banque de Valentine avec Arthur, [[bill-williamson|Bill]] et [[lenny-summers|Lenny]]. Récompense pour le joueur : 2 500 dollars et un fusil Springfield."),
        M("Blessed are the Peacemakers", C3,
          "At camp. Among the first, with Mary-Beth and Dutch, to find Arthur when he collapses after escaping the O'Driscolls.",
          "Au camp. Parmi les premiers, avec Mary-Beth et Dutch, à trouver Arthur quand il s'effondre après avoir échappé aux O'Driscoll."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Listed by the Red Dead Wiki; the mission page gives her no role.",
          "Citée par le Red Dead Wiki ; la page de la mission ne lui attribue aucun rôle."),
        M("The Battle of Shady Belle", C3,
          "Listed by the Red Dead Wiki; moves with the gang to Shady Belle.",
          "Citée par le Red Dead Wiki ; suit la bande à Shady Belle."),
        M("Angelo Bronte, A Man of Honor", C4,
          "At camp for the party that celebrates [[jack-marston|Jack]]'s return.",
          "Au camp pour la fête qui célèbre le retour de [[jack-marston|Jack]]."),
        M("Horsemen, Apocalypses", C4,
          "Fires on the O'Driscolls from the back balcony of Shady Belle during their attack.",
          "Tire sur les O'Driscoll depuis le balcon arrière de Shady Belle pendant leur attaque."),
        M("That's Murfree Country", C5,
          "Present at Beaver Hollow when Susan kills [[molly-oshea|Molly O'Shea]].",
          "Présente à Beaver Hollow quand Susan abat [[molly-oshea|Molly O'Shea]]."),
        M("A Rage Unleashed", C6,
          "Escorts Eagle Flies into camp with [[javier-escuella|Javier]].",
          "Escorte Eagle Flies jusqu'au camp avec [[javier-escuella|Javier]]."),
        M("Our Best Selves", C6,
          "Absent. She has left the camp by the start of the mission; Dutch does not name her among those who ran off.",
          "Absente. Elle a quitté le camp au début de la mission ; Dutch ne la cite pas parmi ceux qui ont filé."),
    ]}},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"table": {"head": [two("Document", "Document"), two("Chapter", "Chapitre"), two("Mention of Karen", "Mention de Karen")], "rows": [
        M(two("Letter from Tilly", "Lettre de Tilly"), EP2,
          "Tilly writes to Abigail and John that she never heard what happened to Karen and believes drink killed her. Available after meeting Tilly in Saint Denis, once \"A Quick Favor for an Old Friend\" is done.",
          "Tilly écrit à Abigail et à John qu'elle n'a jamais su ce qu'était devenue Karen et pense que l'alcool l'a tuée. Disponible après la rencontre avec Tilly à Saint-Denis, une fois \"A Quick Favor for an Old Friend\" terminée."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent.")},
    {"h4": two("Valentine, chapter 2", "Valentine, chapitre 2")},
    {"quotes": [
        {"q": two("What's happened to you, Arthur? Three young healthy women want you to take 'em robbing... you're worried about house chores. Let's go.", "What's happened to you, Arthur? Three young healthy women want you to take 'em robbing... you're worried about house chores. Let's go."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), to Arthur, who has asked whether Miss Grimshaw can spare them",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à Arthur, qui vient de demander si Miss Grimshaw peut se passer d'elles. Traduction : « Qu'est-ce qui t'arrive, Arthur ? Trois jeunes femmes en pleine santé veulent que tu les emmènes voler... et toi, tu t'inquiètes des corvées. Allez, on y va. »")},
        {"q": two("Oh no, Miss O'Shea is far too high and mighty now for the likes of us... or to do any real work. She's a society lady now.", "Oh no, Miss O'Shea is far too high and mighty now for the likes of us... or to do any real work. She's a society lady now."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), when Tilly wonders whether they should have asked Molly to come",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), quand Tilly se demande s'il aurait fallu proposer à Molly de venir. Traduction : « Oh non, Miss O'Shea est bien trop grande dame maintenant pour des filles comme nous... et pour le vrai travail. C'est une femme du monde, désormais. »")},
        {"q": two("Come on ladies... Imagine we're in Paris.", "Come on ladies... Imagine we're in Paris."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), on arriving in Valentine. Tilly answers: \"I imagine Valentine and Paris are easily confused.\"",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à l'arrivée à Valentine. Tilly répond : \"I imagine Valentine and Paris are easily confused.\" Traduction : « Allez, mesdames... Imaginez qu'on est à Paris. » (« Valentine et Paris, c'est facile à confondre, j'imagine. »)")},
        {"q": two("Trying to play him. Not very well.", "Trying to play him. Not very well."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), in room 2B of the Saints Hotel, when Arthur asks what she was doing there",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), dans la chambre 2B du Saints Hotel, quand Arthur lui demande ce qu'elle faisait là. Traduction : « J'essayais de le rouler. Pas très bien. »")},
        {"q": two("Sure, I know small town banks are usually a waste of time, but... this is a livestock town, there's lots of cash sometimes.", "Sure, I know small town banks are usually a waste of time, but... this is a livestock town, there's lots of cash sometimes."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), to Arthur, after the client boasted about the bank",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à Arthur, après les vantardises du client au sujet de la banque. Traduction : « Bien sûr, je sais que les banques de petite ville, c'est souvent du temps perdu, mais... c'est une ville d'élevage, il y a parfois beaucoup de liquide. »")},
        {"q": two("Sure, he only punched me.", "Sure, he only punched me."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), to Tilly, who asks whether she is okay",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à Tilly, qui lui demande si elle va bien. Traduction : « Bien sûr, il m'a juste donné un coup de poing. »")},
    ]},
    {"h4": two("At camp, chapter 2", "Au camp, chapitre 2")},
    {"quotes": [
        {"q": two("That man really needs to learn how to hold his liquor.", "That man really needs to learn how to hold his liquor."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), as Arthur carries a drunk Reverend Swanson through camp",
                    "Who is Not Without Sin (RDR2, chapitre 2), quand Arthur traverse le camp en portant le révérend Swanson, ivre. Traduction : « Cet homme a vraiment besoin d'apprendre à tenir l'alcool. »")},
    ]},
    {"h4": two("The Valentine bank, chapter 3", "La banque de Valentine, chapitre 3")},
    {"quotes": [
        {"q": two("Hit the goddamn bank with us.", "Hit the goddamn bank with us."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), when Arthur asks what they want him to do",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), quand Arthur demande ce qu'on attend de lui. Traduction : « Braque cette foutue banque avec nous. »")},
        {"q": two("It's a bank, Arthur.", "It's a bank, Arthur."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), when Arthur asks whether they all think it is worth the risk",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), quand Arthur demande s'ils pensent tous que le jeu en vaut la chandelle. Traduction : « C'est une banque, Arthur. »")},
        {"q": two("Never can resist a scam those two.", "Never can resist a scam those two."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), optional conversation with Arthur about Dutch, Hosea and the feud between the Grays and the Braithwaites",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), conversation facultative avec Arthur sur Dutch, Hosea et la querelle entre les Gray et les Braithwaite. Traduction : « Ces deux-là ne savent jamais résister à une arnaque. »")},
        {"q": two("So even you long to save the fallen women, eh Arthur? You break my heart... you really do.", "So even you long to save the fallen women, eh Arthur? You break my heart... you really do."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), if Arthur picks the lost girl routine; she says the second sentence in tears",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), si Arthur choisit le numéro de la jeune fille perdue ; elle prononce la seconde phrase en larmes. Traduction : « Alors même toi, tu rêves de sauver les filles perdues, hein, Arthur ? Tu me brises le cœur... vraiment. »")},
        {"q": two("I'm not leaving, 'til I find him, boyo!", "I'm not leaving, 'til I find him, boyo!"),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), playing the drunken harlot, to the teller who asks her to leave",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), dans le rôle de la catin ivre, au caissier qui lui demande de sortir. Traduction : « Je bouge pas d'ici tant que je l'ai pas trouvé, mon gars ! »")},
        {"q": two("Probably.", "Probably."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), when lawmen surround the bank and she offers to go out first. Arthur has asked: \"What, are you insane?\"",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), quand les hommes de loi encerclent la banque et qu'elle propose de sortir la première. Arthur vient de lui demander : \"What, are you insane?\" Traduction : « Probablement. » (« Quoi, tu es folle ? »)")},
        {"q": two("We're shooting our way out of here, boys!", "We're shooting our way out of here, boys!"),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), as the gunfight with the Valentine lawmen begins",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), au début de la fusillade avec les hommes de loi de Valentine. Traduction : « On sort d'ici à coups de flingue, les gars ! »")},
    ]},
    {"h4": two("Said about her", "Ce qu'on dit d'elle")},
    {"quotes": [
        {"q": two("We're bored out of our minds. Been cooped up here for two weeks now. Karen's about ready to murder Grimshaw.", "We're bored out of our minds. Been cooped up here for two weeks now. Karen's about ready to murder Grimshaw."),
         "src": two("Mary-Beth Gaskill to Arthur, Polite Society, Valentine Style (RDR2, chapter 2)",
                    "Mary-Beth Gaskill à Arthur, Polite Society, Valentine Style (RDR2, chapitre 2). Traduction : « On s'ennuie à mourir. Ça fait deux semaines qu'on est enfermées ici. Karen est à deux doigts d'assassiner Grimshaw. »")},
        {"q": two("Oh, well we're gonna send Karen on in ahead... as a distraction. Then we're just gonna rush on in afterwards.", "Oh, well we're gonna send Karen on in ahead... as a distraction. Then we're just gonna rush on in afterwards."),
         "src": two("Bill Williamson to Arthur, Sodom? Back to Gomorrah (RDR2, chapter 3), explaining the plan",
                    "Bill Williamson à Arthur, Sodom? Back to Gomorrah (RDR2, chapitre 3), en exposant le plan. Traduction : « Ben, on va envoyer Karen devant... pour faire diversion. Et nous, on déboule juste après. »")},
        {"q": two("I never heard what happened to her but, deep down I know the drink did for her.", "I never heard what happened to her but, deep down I know the drink did for her."),
         "src": two("Tilly Jackson, letter to Abigail and John Marston (RDR2, epilogue 2, 1907)",
                    "Tilly Jackson, lettre à Abigail et John Marston (RDR2, épilogue 2, 1907). Traduction : « Je n'ai jamais su ce qui lui était arrivé, mais au fond de moi, je sais que c'est la boisson qui l'a eue. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("In \"Polite Society, Valentine Style\", no weapon can be used inside the Saints Hotel. Strangling is the only way for Arthur to kill the man who beats Karen, and her remark to Tilly afterwards changes depending on whether Arthur killed him or knocked him out. One of the Gold Medal objectives is to find Karen in the hotel within 45 seconds.",
            "Dans \"Polite Society, Valentine Style\", aucune arme n'est utilisable dans le Saints Hotel. L'étranglement est le seul moyen pour Arthur de tuer l'homme qui frappe Karen, et la remarque qu'elle fait ensuite à Tilly change selon qu'Arthur l'a tué ou assommé. L'un des objectifs de la médaille d'or consiste à retrouver Karen dans l'hôtel en moins de 45 secondes."),
        two("Attacking, killing or abandoning Karen fails both \"Polite Society, Valentine Style\" and \"Sodom? Back to Gomorrah\"; in the bank mission, letting her be killed also fails it.",
            "Attaquer, tuer ou abandonner Karen fait échouer \"Polite Society, Valentine Style\" comme \"Sodom? Back to Gomorrah\" ; dans la mission de la banque, la laisser mourir entraîne aussi l'échec."),
        two("While \"Sodom? Back to Gomorrah\" is available but not yet played, Karen takes part in no camp scenes, according to the Red Dead Wiki's Camp Events page.",
            "Tant que \"Sodom? Back to Gomorrah\" est disponible sans avoir été jouée, Karen ne participe à aucune scène de camp, d'après la page Camp Events du Red Dead Wiki."),
        two("She is one of the few members of the gang who never ask Arthur to bring back an item for them, according to the Red Dead Wiki.",
            "D'après le Red Dead Wiki, elle fait partie des rares membres de la bande qui ne demandent jamais à Arthur de leur rapporter un objet."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Karen for Red Dead Redemption 2. On September 6, 2018, it posted her portrait and character description on Twitter, in a series covering the members of the gang; The Hollywood Reporter reproduced the series on September 7, 2018. The same descriptions appear on a page of Rockstar's website presenting the Van der Linde gang; the French version, cited by the French Red Dead Wiki, was archived on July 6, 2022. In the composite image of the 23 gang members that opens Wikipedia's list of the game's characters, Karen stands in the front row, between [[mary-beth-gaskill|Mary-Beth]] and [[abigail-marston|Abigail]].",
              "Rockstar a publié une illustration officielle de Karen pour Red Dead Redemption 2. Le 6 septembre 2018, l'éditeur diffuse sur Twitter son portrait et sa description, dans une série consacrée aux membres de la bande ; The Hollywood Reporter reprend la série le 7 septembre 2018. Les mêmes descriptions figurent sur une page du site de Rockstar qui présente la bande Van der Linde ; la version française, citée par le Red Dead Wiki français, a été archivée le 6 juillet 2022. Sur l'image réunissant les 23 membres de la bande, en tête de la liste des personnages du jeu sur Wikipédia, Karen figure au premier rang, entre [[mary-beth-gaskill|Mary-Beth]] et [[abigail-marston|Abigail]].")},
]
