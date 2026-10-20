"""Mary Linton, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

Sources (Red Dead Wiki EN, Oct 2026, saved in scratchpad cov/linton/, m/ and w/):
- Character page "Mary Linton" (Mission appearances, Quotes, Trivia) and FR page (fr.txt: Apparitions dans les missions).
- Mission pages: "We Loved Once and True I & II" (infobox, trivia: hat, timer, recalled lines), "We Loved Once and True
  III" (gold medal objectives, trivia), "Fatherhood and Other Dreams" (gold medal objectives, trivia: $100 brooch and
  honor, weight remark, naval compass), "A Fork in the Road" (chapter 5; quote list of recalled lines), "Goodbye, Dear
  Friend" (chapter 6; rewards), "The Fine Art of Conversation" (chapter 6; trivia on the conditional meeting),
  "Red Dead Redemption (mission)/dialogues" (last ride lines), "No, No and Thrice, No" (chapter 4; Mary-Beth's line),
  "Money Lending and Other Sins III/dialogues", "The Sheep and the Goats", "A Really Big Bastard", "A New Future
  Imagined" (Epilogue part 2), "Ending Credits".
- Pages "Documents in Redemption 2" (the three letters, Young Mary & Arthur Photograph), "Mr. Gillis" (trivia: "Mr Linton"
  in the PC files), "Chadwick Farm" (interior closed after the mission).
Quotation marks: Mary's lines come from the quote list of the character page and the quote lists of "A Fork in the Road"
and "Red Dead Redemption (mission)/dialogues" (no transcript exists for her own missions); Mary-Beth's line from the
quote list of "A Fork in the Road" (also used verbatim in mary_C). Chapter numbers follow the mission infoboxes.
Ownership: narrative events and the letters stay in part A (one line per mission here); the two sentences of the goodbye
letter that Arthur recalls are quoted in part A, not repeated here. Camp women's opinions of Mary (Susan, Tilly, Karen,
Abigail, Mary-Beth's camp talks) belong to Relationships (part B); Mary-Beth's recalled line is kept here only as a quote.
Roger Clark's motion capture and the cut Rhodes meeting go to part D.
Excluded: glitches (Jamie's duplicated horse, the hotel balcony exploit, the Sawed-Off softlock), John's mention of Mary
in "The Sheep and the Goats" and Karen's question (wiki-only, no transcript, camp talk: left to part B).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
E2 = two("Epilogue 2", "Épilogue 2")
CR = two("End credits", "Générique de fin")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Mary appears only in Red Dead Redemption 2. She gives Arthur two optional mission strands, both missable: \"We Loved Once and True\" in chapter 2 and \"Fatherhood and Other Dreams\" in chapter 4. Completing them counts toward the honor story missions needed for the Lending a Hand trophy. Outside those missions she is heard only through her letters and through lines Arthur remembers.",
              "Mary n'apparaît que dans Red Dead Redemption 2. Elle confie à Arthur deux séries de missions facultatives, qu'il est possible de manquer : \"We Loved Once and True\" au chapitre 2 et \"Fatherhood and Other Dreams\" au chapitre 4. Les terminer compte parmi les missions d'honneur exigées pour le trophée Lending a Hand. En dehors de ces missions, on ne l'entend qu'à travers ses lettres et les répliques dont Arthur se souvient.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Mary's role", "Rôle de Mary")], "rows": [
        M("We Loved Once and True I", C2,
          "Voice only. Her first letter reaches Arthur through [[susan-grimshaw|Susan]].",
          "Voix seulement. Sa première lettre parvient à Arthur par l'intermédiaire de [[susan-grimshaw|Susan]]."),
        M("We Loved Once and True II", C2,
          "Receives Arthur at Chadwick Farm and asks him to bring her brother Jamie back from the Chelonians.",
          "Reçoit Arthur à Chadwick Farm et lui demande de ramener son frère Jamie, parti chez les Chéloniens."),
        M("We Loved Once and True III", C2,
          "Meets Arthur and Jamie at Valentine station and leaves with her brother by train.",
          "Retrouve Arthur et Jamie à la gare de Valentine et repart en train avec son frère."),
        M("Fatherhood and Other Dreams I", C4,
          "Voice only. Her second letter calls Arthur to the Hotel Grand in Saint Denis.",
          "Voix seulement. Sa deuxième lettre appelle Arthur à l'Hotel Grand de Saint-Denis."),
        M("Fatherhood and Other Dreams II", C4,
          "Follows her father with Arthur, gets her mother's brooch back, goes to the theater with him and asks him to run away with her.",
          "Suit son père avec Arthur, récupère la broche de sa mère, va au théâtre avec lui et lui propose de partir avec elle."),
        M("A Fork in the Road", C5,
          "Voice only. One of her lines comes back to Arthur after his diagnosis, depending on his honor.",
          "Voix seulement. L'une de ses répliques revient à Arthur après le diagnostic, selon son honneur."),
        M("Goodbye, Dear Friend", C6,
          "Voice only. Her goodbye letter, with the ring and a photograph, is handed to Arthur by [[tilly-jackson|Tilly]].",
          "Voix seulement. Sa lettre d'adieu, avec la bague et une photographie, est remise à Arthur par [[tilly-jackson|Tilly]]."),
        M("The Fine Art of Conversation", C6,
          "Mentioned, not named: Arthur speaks of her to Sister Calderón (only after \"Of Men and Angels\" and with high honor).",
          "Évoquée sans être nommée : Arthur parle d'elle à sœur Calderón (seulement après \"Of Men and Angels\" et avec un honneur élevé)."),
        M("Red Dead Redemption", C6,
          "Voice only. A sentence from her goodbye letter comes back to Arthur during his last ride.",
          "Voix seulement. Une phrase de sa lettre d'adieu revient à Arthur pendant sa dernière chevauchée."),
        M("End credits", CR,
          "Seen in mourning at Arthur's grave.",
          "Apparaît en deuil sur la tombe d'Arthur."),
    ]}},
    {"h4": two("Missions in which she is mentioned", "Missions où elle est évoquée")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Mary", "Lien avec Mary")], "rows": [
        M("Money Lending and Other Sins III", C2,
          "If Arthur has just read her first letter, [[leopold-strauss|Strauss]] finds him lost in thought.",
          "Si Arthur vient de lire sa première lettre, [[leopold-strauss|Strauss]] le trouve perdu dans ses pensées."),
        M("No, No and Thrice, No", C4,
          "Arthur can talk about her with [[mary-beth-gaskill|Mary-Beth]] at the start of the mission.",
          "Arthur peut parler d'elle avec [[mary-beth-gaskill|Mary-Beth]] au début de la mission."),
        M("A Really Big Bastard", E2,
          "[[john-marston|John]] tells [[sadie-adler|Sadie]] he will propose to Abigail with the ring Arthur gave Mary.",
          "[[john-marston|John]] confie à [[sadie-adler|Sadie]] qu'il demandera Abigail en mariage avec la bague qu'Arthur avait offerte à Mary."),
        M("A New Future Imagined", E2,
          "John proposes to [[abigail-marston|Abigail]] with her ring.",
          "John demande [[abigail-marston|Abigail]] en mariage avec sa bague."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. No transcript of Mary's missions is published by the Red Dead Wiki; they are checked against the quote lists of the Red Dead Wiki's pages on Mary, on \"A Fork in the Road\" and on the mission \"Red Dead Redemption\". The sentences from her letters are under Biography.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise. Le Red Dead Wiki ne publie aucune transcription des missions de Mary ; elles sont vérifiées sur les listes de citations de ses pages consacrées à Mary, à \"A Fork in the Road\" et à la mission \"Red Dead Redemption\". Les phrases tirées de ses lettres figurent dans la Biographie.")},
    {"h4": two("Mary", "Mary")},
    {"quotes": [
        {"q": two("Don't make me beg you, Arthur.", "Don't make me beg you, Arthur."),
         "src": two("Mary, when Arthur is reluctant to hear her out, We Loved Once and True II (RDR2, chapter 2). Arthur remembers the line in A Fork in the Road if his honor is low.",
                    "Mary, quand Arthur rechigne à l'écouter, We Loved Once and True II (RDR2, chapitre 2). Arthur se souvient de cette phrase dans A Fork in the Road si son honneur est bas. Traduction : « Ne m'oblige pas à te supplier, Arthur. »")},
        {"q": two("I understand if you don't wanna help me, but... but... I think of you often.", "I understand if you don't wanna help me, but... but... I think of you often."),
         "src": two("Mary, asking Arthur to find her brother, We Loved Once and True II (RDR2, chapter 2). Arthur remembers the line in A Fork in the Road if his honor is high.",
                    "Mary, en demandant à Arthur de retrouver son frère, We Loved Once and True II (RDR2, chapitre 2). Arthur se souvient de cette phrase dans A Fork in the Road si son honneur est élevé. Traduction : « Je comprends que tu ne veuilles pas m'aider, mais... mais... je pense souvent à toi. »")},
        {"q": two("I've... You're... Oh, you'll never change. I know that.", "I've... You're... Oh, you'll never change. I know that."),
         "src": two("Mary to Arthur, before boarding the train with Jamie, We Loved Once and True III (RDR2, chapter 2)",
                    "Mary à Arthur, avant de monter dans le train avec Jamie, We Loved Once and True III (RDR2, chapitre 2). Traduction : « J'ai... Tu es... Oh, tu ne changeras jamais. Je le sais. »")},
    ]},
    {"h4": two("About Mary", "À propos de Mary")},
    {"quotes": [
        {"q": two("Well, she was a fool then, Arthur.", "Well, she was a fool then, Arthur."),
         "src": two("Mary-Beth to Arthur, about Mary, No, No and Thrice, No (RDR2, chapter 4). Arthur remembers the line in A Fork in the Road if his honor is high.",
                    "Mary-Beth à Arthur, au sujet de Mary, No, No and Thrice, No (RDR2, chapitre 4). Arthur se souvient de cette phrase dans A Fork in the Road si son honneur est élevé. Traduction : « Eh bien, c'était une idiote, alors, Arthur. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("During the meeting at Chadwick Farm, Arthur takes off his hat and holds it if he is wearing one, and puts it back on when the conversation ends.",
            "Pendant l'entrevue de Chadwick Farm, Arthur ôte son chapeau et le garde à la main s'il en porte un, puis le remet à la fin de la conversation."),
        two("According to the Red Dead Wiki, the interior of Chadwick Farm, where Mary rents her room, can be entered only before \"We Loved Once and True I & II\".",
            "D'après le Red Dead Wiki, on ne peut entrer dans Chadwick Farm, où Mary loue sa chambre, qu'avant \"We Loved Once and True I & II\"."),
        two("The gold medal objectives of \"We Loved Once and True III\" are to persuade the Chelonians to let Jamie go without violence and to bring him back to Mary within two minutes.",
            "Les objectifs de la médaille d'or de \"We Loved Once and True III\" consistent à convaincre les Chéloniens de laisser partir Jamie sans violence et à le ramener à Mary en moins de deux minutes."),
        two("While they follow Mr. Gillis in \"Fatherhood and Other Dreams\", Mary comments on Arthur's looks: if he is above his ideal weight, she says he looks well and remarks that he used to be so skinny; otherwise she tells him he looks dirty.",
            "Pendant qu'ils suivent Mr. Gillis dans \"Fatherhood and Other Dreams\", Mary commente l'allure d'Arthur : s'il dépasse son poids idéal, elle le trouve en forme et rappelle qu'il était autrefois tout maigre ; sinon, elle lui dit qu'il a l'air sale."),
        two("Paying Ashton the $100 he asks for Mary's brooch raises Arthur's honor; beating him into a discount brings no honor, and killing him lowers it.",
            "Payer à Ashton les 100 $ qu'il demande pour la broche de Mary fait monter l'honneur d'Arthur ; le frapper pour obtenir un rabais n'en rapporte pas, et le tuer le fait baisser."),
        two("Taking Mary to the theater is one of the gold medal objectives of \"Fatherhood and Other Dreams\", along with catching Ashton's wagon and driving it to the secluded spot within 1 minute 45 seconds.",
            "Emmener Mary au théâtre fait partie des objectifs de la médaille d'or de \"Fatherhood and Other Dreams\", avec le fait de rattraper le chariot d'Ashton et de le conduire à l'endroit isolé en moins d'1 minute 45."),
        two("The three letters from Mary and the \"Young Mary & Arthur Photograph\" are listed among the documents of Red Dead Redemption 2: the first can be taken from Arthur's tent in chapter 2, the second from his room in chapter 4.",
            "Les trois lettres de Mary et la photographie \"Young Mary & Arthur Photograph\" figurent parmi les documents de Red Dead Redemption 2 : la première peut être récupérée dans la tente d'Arthur au chapitre 2, la deuxième dans sa chambre au chapitre 4."),
        two("According to the Red Dead Wiki, Mary's father is named \"Mr Linton\" in the PC files of the game, although he is Mr. Gillis in the story.",
            "D'après le Red Dead Wiki, le père de Mary s'appelle \"Mr Linton\" dans les fichiers de la version PC, alors qu'il est Mr. Gillis dans l'histoire."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("Mary Linton exists only in Red Dead Redemption 2 (2018). She does not appear in Red Dead Redemption (2010), set in 1911, and the Red Dead Wiki lists her in no other game, Red Dead Online included. Her family is seen only in her own missions: her brother Jamie in \"We Loved Once and True III\", her father in \"Fatherhood and Other Dreams\".",
              "Mary Linton n'existe que dans Red Dead Redemption 2 (2018). Elle n'apparaît pas dans Red Dead Redemption (2010), qui se déroule en 1911, et le Red Dead Wiki ne la recense dans aucun autre jeu, Red Dead Online compris. Sa famille n'est visible que dans ses propres missions : son frère Jamie dans \"We Loved Once and True III\", son père dans \"Fatherhood and Other Dreams\".")},
]
