"""Sister Calderón (Mother Superior Calderón), reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia,
Other media.

SOURCE REGISTER
- Red Dead Wiki EN, character page "Mother Superior Calderón" (Mission appearances, Quotes, Trivia; en.txt) and FR page
  "Mère Supérieure Calderón" (fr.txt: Apparitions dans les missions).
- Wiki mission pages: "Brothers and Sisters, One and All" (infobox chapter 4, giver Brother Dorkins/Sister Calderón,
  previous "Help a Brother Out"; gold medal objective; trivia), "Of Men and Angels" (availability chapter 5 or 6,
  prerequisites, food or 10 dollars, part II automatic, "Lending a Hand"; trivia 1 Corinthians 13:1), "The Fine Art of
  Conversation" (chapter 6, trivia: conditional meeting, PC replay), "Red Dead Redemption (mission)" and its
  /dialogues (high-honor last-ride line), "I Know You" (part 2 objectives, prerequisites, honor rewards, trivia: more
  than 300 dollars if robbed), "Mother Superior Blues" (two parts, giver, rewards, prerequisites, failure conditions,
  quote box, trivia, achievement "The Superior Dance").
- Wiki pages "Las Hermanas" (trivia: she and five unnamed nuns present during "Mother Superior Blues", not defending),
  "Doyle's Tavern" (checked: no nun line there; the "Spanish nun" remark is from the character page only).
- Transcripts used word for word: fc/gsw.txt (Game Scripts Wiki fan transcript of RDR2: "Brothers and Sisters, One and
  All", "The Fine Art of Conversation"), "Of Men and Angels/dialogues", "I Know You/dialogues". The Undead Nightmare
  line comes from the quote box of the "Mother Superior Blues" page (no transcript exists for that mission).
- Real world: Red Dead Redemption released May 18, 2010; Undead Nightmare 2010; Red Dead Redemption 2 October 26, 2018;
  RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 with the story and Undead Nightmare, no multiplayer
  (same wording as desanta_C, luisa_C). scripts/v3/sources/thr_descriptions.txt (Rockstar, 6 Sep 2018): no entry for
  her.

QUOTES HERE (B must not repeat them in quotation marks): "It's like swimming..."; "You know, a long time ago... I was
like you." + "No, I did terrible things..."; "Religion is just a word..."; "To me... God is people..."; "Don't worry so
much about your heart..."; "Oh, I meant wonderful, but... so very frightening..."; "Forgive me, but... that's the
problem. You don't know you."; "My husband died a long time ago. Life is full of pain..."; "Be grateful that for the
first time... you see your life clearly."; "Often neither do I..."; "There is nothing to be afraid of..."; "Yes, life is
much simpler than we make it..."; "México is an old country..." (quote box).
The FAoC line "We've all lived [bad] lives" is garbled in both sources ("had lives" in the transcript, "live bad lives"
in the wiki list): not quoted.

FIXES (22 Oct 2026, after fc_report1/2 and coverage_report): "Of Men and Angels" = chapter 5 or 6 (mission page);
last-ride condition completed (FAoC trivia: no Mary-Beth random encounter); "Mary" removed from a quote context (Arthur
does not name her); Trivia cut: Rains Fall/Isaac, lawmen, PC replay, 300 dollars (B owns them), "Spanish nun" (B Names)
and the repeated "Gracias, señor"; closing-cutscene trivia reworded; Other media: identity attributed to the wiki,
Rockstar 2018 descriptions sentence cut (B Personality owns it).

EXCLUDED
- The cut lasso (hogtie) dialogue: cut content, part D.
- Swanson's "Catholic lady" camp line (wiki: "implied to be Sister Calderón"): camp scene, part B (Swanson entry), and
  the identification is an implication.
- Undead Nightmare page: John's grave flask = her holy water (speculation). "Mother Superior Blues" title "could refer"
  to "Old Swindler Blues" (speculation); "Superior Blue" car paint (irrelevant).
- FR wiki: appearance in "Eva in Peril" (EN mission page: the nun is Sister Ana Calomarde).
- Red Dead Online: the wiki lists her in no other game; no multiplayer model is attested for her.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C4 = two("4. Saint Denis", "4. Saint-Denis")
C56 = two("5 or 6", "5 ou 6")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
A2 = two("RDR1, Act II: Nuevo Paraíso", "RDR1, acte II : Nuevo Paraíso")
UNM = two("Undead Nightmare", "Undead Nightmare")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("In Red Dead Redemption 2 she appears in two optional stranger missions, both honor missions that count toward the Lending a Hand trophy, and conditionally at the end of a story mission of chapter 6. In Red Dead Redemption she appears in one stranger mission, and in Undead Nightmare she gives one two-part mission.",
              "Dans Red Dead Redemption 2, elle apparaît dans deux missions d'inconnu facultatives, deux missions d'honneur qui comptent pour le trophée Lending a Hand, et, sous condition, à la fin d'une mission principale du chapitre 6. Dans Red Dead Redemption, elle figure dans une mission d'inconnu, et dans Undead Nightmare elle confie une mission en deux parties.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter or act", "Chapitre ou acte"), two("Calderón's role", "Rôle de Calderón")], "rows": [
        M("Brothers and Sisters, One and All", C4,
          "Mission giver with Brother Dorkins, after \"Help a Brother Out\". Her crucifix is stolen during a reading lesson; Arthur returns it to her at the cathedral. Reward: honor. Missable.",
          "Donneuse de mission avec frère Dorkins, après \"Help a Brother Out\". Son crucifix est volé pendant une leçon de lecture ; Arthur le lui rapporte à la cathédrale. Récompense : honneur. Peut être manquée."),
        M("Of Men and Angels", C56,
          "Mission giver. Collects for the poor outside the Saint Denis cathedral; Arthur gives food or 10 dollars. Opens after \"A Fork in the Road\" if the previous mission was completed; lost after \"The Fine Art of Conversation\". Reward: honor.",
          "Donneuse de mission. Quête pour les pauvres devant la cathédrale de Saint-Denis ; Arthur donne de la nourriture ou 10 dollars. Disponible après \"A Fork in the Road\" si la mission précédente a été faite ; perdue après \"The Fine Art of Conversation\". Récompense : honneur."),
        M("The Fine Art of Conversation", C6,
          "Determinant. Talks with Arthur at Emerald Station before leaving for Mexico, only if \"Of Men and Angels\" was completed and his honor is high; otherwise Orville Swanson takes her place.",
          "Selon les choix. Parle avec Arthur à Emerald Station avant de partir pour le Mexique, seulement si \"Of Men and Angels\" a été faite et que son honneur est élevé ; sinon, Orville Swanson prend sa place."),
        M("Red Dead Redemption", C6,
          "Voice only, determinant. If Arthur met her at Emerald Station and his honor is high, one of her lines from that scene comes back to him on his last ride; according to the mission page, only if he did not trigger a random encounter conversation with Mary-Beth Gaskill.",
          "Voix seulement, selon les choix. Si Arthur l'a croisée à Emerald Station et que son honneur est élevé, l'une de ses phrases de cette scène lui revient pendant sa dernière chevauchée ; d'après la page de la mission, à condition qu'il n'ait pas déclenché de conversation aléatoire avec Mary-Beth Gaskill."),
        M("I Know You (part 2)", A2,
          "Stranger mission given by the Strange Man. Asks John for alms outside Las Hermanas; he gives 10 dollars or robs her. Requires part 1 and \"We Shall Be Together in Paradise\". Robbing her costs honor; according to the mission page, donating after encouraging the drunk man in part 1 earns 20 honor.",
          "Mission d'inconnu confiée par l'homme mystérieux. Demande l'aumône à John devant Las Hermanas ; il donne 10 dollars ou la dévalise. Exige la première partie et \"We Shall Be Together in Paradise\". La voler coûte de l'honneur ; d'après la page de la mission, donner après avoir encouragé l'ivrogne de la première partie rapporte 20 points d'honneur."),
        M("Mother Superior Blues", UNM,
          "Mission giver. John clears Las Hermanas, brings her a fresh undead and cleanses Sepulcro; she sends him to Escalera. Reward: Holy Water. Part 2 requires \"Filth and Other Entertainment\" and \"Biographies and Lies\". Attacking her or her nuns fails the mission. Completing it unlocks the achievement The Superior Dance.",
          "Donneuse de mission. John libère Las Hermanas, lui ramène un mort-vivant frais et purifie Sepulcro ; elle l'envoie à Escalera. Récompense : eau bénite (Holy Water). La seconde partie exige \"Filth and Other Entertainment\" et \"Biographies and Lies\". L'attaquer, elle ou ses religieuses, fait échouer la mission. La terminer débloque le succès The Superior Dance."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. They are checked against mission transcripts, except the Undead Nightmare line, taken from the mission page of the Red Dead Wiki.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Elles sont vérifiées sur les transcriptions des missions, sauf celle d'Undead Nightmare, tirée de la page de la mission sur le Red Dead Wiki.")},
    {"h4": two("Red Dead Redemption 2, Saint Denis", "Red Dead Redemption 2, Saint-Denis")},
    {"quotes": [
        {"q": two("Oh, you will. It's like swimming, it takes time, but then it is easy... and the whole world opens to you.", "Oh, you will. It's like swimming, it takes time, but then it is easy... and the whole world opens to you."),
         "src": two("Brothers and Sisters, One and All (RDR2, chapter 4), to a street boy who says he does not understand his reading lesson",
                    "Brothers and Sisters, One and All (RDR2, chapitre 4), à un gamin des rues qui dit ne rien comprendre à sa leçon de lecture. Traduction : « Ça viendra. C'est comme nager : ça prend du temps, et puis ça devient facile... et le monde entier s'ouvre à toi. »")},
        {"q": two("You know, a long time ago... I was like you.", "You know, a long time ago... I was like you."),
         "src": two("Of Men and Angels (RDR2, chapter 5 or 6), to Arthur, who chuckles that he very much doubts it",
                    "Of Men and Angels (RDR2, chapitre 5 ou 6), à Arthur, qui répond en riant qu'il en doute fort. Traduction : « Vous savez, il y a bien longtemps... j'étais comme vous. »")},
        {"q": two("No, I did terrible things... awful things... and I could not stop doing terrible things... because I did not believe that goodness existed... and then, one day, I saw that love did exist... and ever since then, doing bad things became... well not impossible but... ridiculous.", "No, I did terrible things... awful things... and I could not stop doing terrible things... because I did not believe that goodness existed... and then, one day, I saw that love did exist... and ever since then, doing bad things became... well not impossible but... ridiculous."),
         "src": two("Of Men and Angels (RDR2, chapter 5 or 6), to Arthur",
                    "Of Men and Angels (RDR2, chapitre 5 ou 6), à Arthur. Traduction : « Si, j'ai fait des choses terribles... des choses affreuses... et je ne pouvais pas m'arrêter... parce que je ne croyais pas que le bien existait... et puis un jour, j'ai vu que l'amour existait bel et bien... et depuis, faire le mal est devenu... pas impossible, non, mais... ridicule. »")},
        {"q": two("Religion is just a word... hearts are rarely pure... but equally they are rarely impure either.", "Religion is just a word... hearts are rarely pure... but equally they are rarely impure either."),
         "src": two("Of Men and Angels (RDR2, chapter 5 or 6), after Arthur says he is not a religious man but an outlaw",
                    "Of Men and Angels (RDR2, chapitre 5 ou 6), après qu'Arthur a dit n'être pas un homme de foi mais un hors-la-loi. Traduction : « La religion n'est qu'un mot... les cœurs sont rarement purs... mais ils sont tout aussi rarement impurs. »")},
        {"q": two("To me... God is people, and people are God, so... we must all do what we can.", "To me... God is people, and people are God, so... we must all do what we can."),
         "src": two("Of Men and Angels (RDR2, chapter 5 or 6), to Arthur",
                    "Of Men and Angels (RDR2, chapitre 5 ou 6), à Arthur. Traduction : « Pour moi... Dieu, ce sont les gens, et les gens sont Dieu, alors... nous devons tous faire ce que nous pouvons. »")},
        {"q": two("Don't worry so much about your heart. The actions will lead... and the heart follows.", "Don't worry so much about your heart. The actions will lead... and the heart follows."),
         "src": two("Of Men and Angels (RDR2, chapter 5 or 6), to Arthur, before he gives food or money for the poor",
                    "Of Men and Angels (RDR2, chapitre 5 ou 6), à Arthur, avant qu'il donne de la nourriture ou de l'argent pour les pauvres. Traduction : « Ne vous inquiétez pas tant de votre cœur. Les actes ouvrent la voie... et le cœur suit. »")},
        {"q": two("Oh, I meant wonderful, but... so very frightening... as you wish. Consider your good deed done for the day.", "Oh, I meant wonderful, but... so very frightening... as you wish. Consider your good deed done for the day."),
         "src": two("Of Men and Angels (RDR2, chapter 5 or 6), after Arthur protests that he is not wonderful",
                    "Of Men and Angels (RDR2, chapitre 5 ou 6), après qu'Arthur a protesté qu'il n'avait rien de merveilleux. Traduction : « Oh, je voulais dire merveilleux, mais... tellement effrayant... comme vous voudrez. Considérez que votre bonne action du jour est faite. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, Emerald Station", "Red Dead Redemption 2, Emerald Station")},
    {"quotes": [
        {"q": two("Forgive me, but... that's the problem. You don't know you.", "Forgive me, but... that's the problem. You don't know you."),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), after Arthur tells her she does not know him",
                    "The Fine Art of Conversation (RDR2, chapitre 6), après qu'Arthur lui a dit qu'elle ne le connaissait pas. Traduction : « Pardonnez-moi, mais... c'est bien le problème. Vous ne vous connaissez pas. »")},
        {"q": two("My husband died a long time ago. Life is full of pain... but there is also love and beauty.", "My husband died a long time ago. Life is full of pain... but there is also love and beauty."),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), after Arthur speaks of his son, a girl who loved him and his parents",
                    "The Fine Art of Conversation (RDR2, chapitre 6), après qu'Arthur a évoqué son fils, une fille qui l'aimait et ses parents. Traduction : « Mon mari est mort il y a longtemps. La vie est pleine de souffrance... mais il y a aussi l'amour et la beauté. »")},
        {"q": two("Be grateful that for the first time... you see your life clearly.", "Be grateful that for the first time... you see your life clearly."),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), when Arthur asks what he should do now; Arthur may hear the line again on his last ride in \"Red Dead Redemption\" (conditions in the Missions table)",
                    "The Fine Art of Conversation (RDR2, chapitre 6), quand Arthur demande ce qu'il doit faire désormais ; Arthur peut réentendre la phrase pendant sa dernière chevauchée, dans \"Red Dead Redemption\" (conditions dans le tableau des Missions). Traduction : « Soyez reconnaissant de voir, pour la première fois... votre vie clairement. »")},
        {"q": two("Often neither do I... but then, I meet someone like you... and everything makes sense.", "Often neither do I... but then, I meet someone like you... and everything makes sense."),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), laughing, after Arthur says he still does not believe in anything",
                    "The Fine Art of Conversation (RDR2, chapitre 6), en riant, après qu'Arthur a dit qu'il ne croyait toujours à rien. Traduction : « Bien souvent, moi non plus... mais je croise quelqu'un comme vous... et tout prend un sens. »")},
        {"q": two("There is nothing to be afraid of, Mr. Morgan. Take a gamble that love exists... and do a loving act.", "There is nothing to be afraid of, Mr. Morgan. Take a gamble that love exists... and do a loving act."),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), after Arthur admits he is afraid",
                    "The Fine Art of Conversation (RDR2, chapitre 6), après qu'Arthur a avoué qu'il avait peur. Traduction : « Il n'y a rien à craindre, monsieur Morgan. Pariez que l'amour existe... et faites un geste d'amour. »")},
    ]},
    {"h4": two("Red Dead Redemption and Undead Nightmare", "Red Dead Redemption et Undead Nightmare")},
    {"quotes": [
        {"q": two("Yes, life is much simpler than we make it. Gracias, señor, and God bless you.", "Yes, life is much simpler than we make it. Gracias, señor, and God bless you."),
         "src": two("I Know You (RDR1), to John, after he drops 10 dollars in her basket and remarks that he never knew life was so simple",
                    "I Know You (RDR1), à John, après qu'il a déposé 10 dollars dans son panier en s'étonnant que la vie soit si simple. Traduction : « Oui, la vie est bien plus simple que nous ne la rendons. Merci, monsieur, et que Dieu vous bénisse. »")},
        {"q": two("México is an old country. Many faiths have lived and died here. Many evil spirits have flourished. I have no idea what is afflicting the people here, but I know it is a sickness of the soul.", "México is an old country. Many faiths have lived and died here. Many evil spirits have flourished. I have no idea what is afflicting the people here, but I know it is a sickness of the soul."),
         "src": two("Mother Superior Blues (Undead Nightmare), to John; quote box of the mission page",
                    "Mother Superior Blues (Undead Nightmare), à John ; citation mise en exergue sur la page de la mission. Traduction : « Le Mexique est un vieux pays. Bien des croyances y sont nées et y sont mortes. Bien des esprits malfaisants y ont prospéré. J'ignore ce qui frappe les gens d'ici, mais je sais que c'est une maladie de l'âme. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("According to the Red Dead Wiki, she is the only minor or side character to appear in Red Dead Redemption, Red Dead Redemption 2 and Undead Nightmare.",
            "D'après le Red Dead Wiki, c'est le seul personnage secondaire présent à la fois dans Red Dead Redemption, Red Dead Redemption 2 et Undead Nightmare."),
        two("She slips Spanish into her speech in both games: \"Por favor\" during the reading lesson in Saint Denis, and her thanks to John at Las Hermanas.",
            "Elle glisse de l'espagnol dans ses répliques dans les deux jeux : \"Por favor\" pendant la leçon de lecture à Saint-Denis, et ses remerciements à John à Las Hermanas."),
        two("The title \"Of Men and Angels\" comes from the first verse of 1 Corinthians 13, according to the mission page.",
            "Le titre \"Of Men and Angels\" vient du premier verset de la première épître aux Corinthiens, chapitre 13, selon la page de la mission."),
        two("The gold medal objective of \"Brothers and Sisters, One and All\" is to find the boy within 19 seconds. With \"Help a Brother Out\", it is one of only two stranger missions of Red Dead Redemption 2 that award gold medals.",
            "L'objectif de la médaille d'or de \"Brothers and Sisters, One and All\" consiste à retrouver le garçon en moins de 19 secondes. Avec \"Help a Brother Out\", c'est l'une des deux seules missions d'inconnu de Red Dead Redemption 2 à attribuer des médailles d'or."),
        two("During \"Mother Superior Blues\", she and five unnamed nuns are at Las Hermanas but take no part in its defense; with them, the settlement counts fourteen survivors instead of eight, according to the Red Dead Wiki. According to the mission page, if Las Hermanas is under attack when John returns, undead can appear in the background of the closing scene in the church.",
            "Pendant \"Mother Superior Blues\", elle et cinq religieuses anonymes se trouvent à Las Hermanas mais ne participent pas à sa défense ; avec elles, le lieu compte quatorze survivants au lieu de huit, d'après le Red Dead Wiki. D'après la page de la mission, si Las Hermanas subit une attaque au retour de John, des morts-vivants peuvent apparaître à l'arrière-plan de la scène finale, dans l'église."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("According to the Red Dead Wiki, which treats the two nuns as one character, Calderón first appears in Red Dead Redemption (2010), as the Mother Superior of Las Hermanas, in the main game and in the Undead Nightmare expansion, and returns eight years later in its prequel, Red Dead Redemption 2 (2018), as the Saint Denis nun, in a story set twelve years earlier. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, include the story and Undead Nightmare, and therefore her scenes.",
              "Pour le Red Dead Wiki, qui fait des deux religieuses un seul personnage, Calderón apparaît d'abord dans Red Dead Redemption (2010), en mère supérieure de Las Hermanas, dans le jeu principal comme dans l'extension Undead Nightmare, puis revient huit ans plus tard dans la préquelle, Red Dead Redemption 2 (2018), en religieuse de Saint-Denis, dans une histoire située douze ans plus tôt. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, comprennent l'histoire et Undead Nightmare, et donc ses scènes.")},
    {"p": two("The Red Dead Wiki lists her in no other game, Red Dead Online included.",
              "Le Red Dead Wiki ne la recense dans aucun autre jeu, Red Dead Online compris.")},
]
