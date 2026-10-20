"""Tilly Jackson, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/tilly/, cov/tilly/m/ and
cov/tilly/w/):
- Red Dead Wiki EN "Tilly Jackson" (Mission Appearances, Companion Activities, Murders Committed, Trivia) and FR
  "Tilly Jackson" (fr.txt: Apparitions dans les missions).
- Mission pages: Outlaws from the West; Enter, Pursued by a Memory; Eastward Bound; Polite Society, Valentine Style
  (trivia: the Valentine man is Anthony Foreman, post-mission camp talk); Who is Not Without Sin; Coach Robbery (Bill
  Williamson) (take 307.50 dollars, 82.50 for the player); The Battle of Shady Belle; No, No and Thrice, No (deaths,
  failure conditions, trivia); Horsemen, Apocalypses (trivia: Tilly absent); Fleeting Joy; That's Murfree Country;
  Goodbye, Dear Friend (trivia: Mary's letter); Money Lending and Other Sins VI/VII (trivia); Our Best Selves; Red Dead
  Redemption (mission); Ending Credits; American Venom (credits list). Wiki pages "Dominoes" (chapter 3 partner list),
  "Errand Boy" (necklace request), "Valentine Doctor's Office" (Tilly's tip), "Letter from Tilly" (text, missable,
  save/load warning), "Anthony Foreman" (1907 bounty), "Camp Events" (absence from Jack's return party;
  unavailability once "No, No and Thrice, No" is unlocked).
- Transcripts "/dialogues" (every quoted line checked word for word): Outlaws from the West, Enter, Pursued by a
  Memory, Polite Society, Valentine Style, Who is Not Without Sin, Red Dead Redemption (mission). No transcript exists
  on the wiki for No, No and Thrice, No, Fleeting Joy, That's Murfree Country, Our Best Selves, Goodbye, Dear Friend,
  the coach robbery or the 1907 Saint Denis meeting (checked Oct 2026): no line from them is quoted.
- Real world: Rockstar's character portraits and descriptions posted on Twitter on September 6, 2018 and reproduced by
  The Hollywood Reporter on September 7, 2018 (../uncle/fc/thr_descriptions.txt: Tilly has an entry; its text is quoted
  in part B only); Wikipedia "List of Red Dead Redemption 2 characters" (m/wp_list.txt: composite of the 23 gang
  members, front row "Pearson, Uncle, Swanson, Sean, Tilly, Grimshaw, Sadie..."); the Red Dead Wiki "Anthony Foreman"
  page (Red Dead Online appearances).
Ownership (FIX_RULES), left to other parts: all narrative events, her backstory, the 1907 meeting and letter content
(A); personality, names, appearance, the Carbine Repeater, camp scenes and camp lines (Susan, Kieran, Molly, Karen,
Mary-Beth, Javier's song, Lenny, dominoes conversation, reaction to Molly's death), the Rockstar description and the
guide (B); Meeya Davis, interviews, reception (D).
Quotes: each line in ONE place; part A paraphrases them without quotation marks. Susan's Eastward Bound line ("Miss
Jackson... I've seen shit with more common sense than you") is left to part B (Susan entry) and not quoted here.
Lines from the 1907 meeting are known only through Screen Rant (not a transcript) and are not quoted. The letter is
quoted from the wiki's "Letter from Tilly" page, which reproduces the in-game document.
Kills: the character page lists one, Malcolm Foreman, before the events of the game.
Fact-check fixes (20 Oct 2026): quotes already in part B "In her own words" (civilization, kiss a damn snake) and
Names ("Tilly Jackson as I was...") removed here; the letter lines about Jack/Abigail and about the people she misses
moved here from part B relationship entries; Shady Belle and Fleeting Joy rows say only "listed by the wiki"; the
coach robbery share moved to part A; Mary's letter handed over "at the end of" Goodbye, Dear Friend.
Excluded: the Carbine Repeater glitch (weapons, part B); the dominoes "foreshadowing" of Molly's death on the That's
Murfree Country page (interpretation); "Tilly" and "Dominoes - Tilly Jackson" as separately named activities (the
wiki's list item "Tilly" has no page; covered by the 1907 meeting row); Mr. Pierre's "second child" (single source,
contradicted by the letter).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]
K = lambda name, mission, en, fr: [name, mission, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
E2 = two("Epilogue II", "Épilogue II")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists ten story missions of Red Dead Redemption 2 for Tilly, the ending credits, her 1907 meeting with John and two companion activities. The table below also includes the missions in which she appears without being listed, or in which she is only talked about.",
              "Le Red Dead Wiki anglais recense pour Tilly dix missions principales de Red Dead Redemption 2, le générique de fin, sa rencontre avec John en 1907 et deux activités de compagnon. Le tableau ci-dessous intègre aussi les missions où elle apparaît sans être recensée, ou dont elle n'est que le sujet.")},
    {"h4": two("Red Dead Redemption 2, story missions", "Red Dead Redemption 2, missions principales")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Tilly's role", "Rôle de Tilly")], "rows": [
        M("Outlaws from the West", C1,
          "Flees Blackwater with the gang. At Colter, [[dutch-van-der-linde|Dutch]] asks her and [[karen-jones|Karen]] to warm up [[sadie-adler|Sadie]].",
          "Fuit Blackwater avec la bande. À Colter, [[dutch-van-der-linde|Dutch]] lui demande, ainsi qu'à [[karen-jones|Karen]], de réchauffer [[sadie-adler|Sadie]]."),
        M("Enter, Pursued by a Memory", C1,
          "By the fire, she reassures [[abigail-marston|Abigail]] about the missing [[john-marston|John]].",
          "Près du feu, elle rassure [[abigail-marston|Abigail]] au sujet de [[john-marston|John]], porté disparu."),
        M("Eastward Bound", C1,
          "At a table with [[uncle|Uncle]] when Dutch reaches Horseshoe Overlook; [[susan-grimshaw|Susan]] criticizes her work.",
          "Attablée avec [[uncle|Uncle]] quand Dutch arrive à Horseshoe Overlook ; [[susan-grimshaw|Susan]] critique son travail."),
        M("Polite Society, Valentine Style", C2,
          "Rides to Valentine with [[arthur-morgan|Arthur]], Uncle, Karen and [[mary-beth-gaskill|Mary-Beth]]. A man from the Foreman Brothers, Anthony Foreman according to the wiki, grabs her in the street until Arthur steps in.",
          "Part pour Valentine avec [[arthur-morgan|Arthur]], Uncle, Karen et [[mary-beth-gaskill|Mary-Beth]]. Un homme des frères Foreman, Anthony Foreman selon le wiki, l'agrippe en pleine rue jusqu'à ce qu'Arthur intervienne."),
        M("Who is Not Without Sin", C2,
          "Not listed by the wiki. At camp, if Arthur greets her while carrying a drunk [[orville-swanson|Reverend Swanson]], she asks whether he is all right.",
          "Non recensée par le wiki. Au camp, si Arthur la salue en portant le [[orville-swanson|révérend Swanson]] ivre, elle demande s'il va bien."),
        M("The Battle of Shady Belle", C3,
          "Listed by the wiki; not named in the mission page. In this mission [[andrew-milton|Milton]] and [[edgar-ross|Ross]] come to the Clemens Point camp, and the gang moves to Shady Belle.",
          "Recensée par le wiki, mais absente de la page de la mission. Dans cette mission, [[andrew-milton|Milton]] et [[edgar-ross|Ross]] entrent dans le camp de Clemens Point, et la bande s'installe à Shady Belle."),
        M("No, No and Thrice, No", C4,
          "Kidnapped by the Foreman Brothers and held at Radley's House, Scarlett Meadows. Freed by Arthur and Susan, she asks for Anthony Foreman to be brought back alive. The mission fails if she is killed.",
          "Enlevée par les frères Foreman et retenue à Radley's House, à Scarlett Meadows. Libérée par Arthur et Susan, elle demande qu'on lui ramène Anthony Foreman vivant. La mission échoue si elle est tuée."),
        M("Fleeting Joy", C5,
          "Listed by the wiki; not named in the mission page. In this mission the survivors of Guarma return to the Lakay camp and the Pinkertons attack.",
          "Recensée par le wiki, mais absente de la page de la mission. Dans cette mission, les rescapés de Guarma reviennent au camp de Lakay et la Pinkerton attaque."),
        M("That's Murfree Country", C5,
          "Listed by the wiki. In this mission the gang moves to Beaver Hollow, where Susan shoots [[molly-oshea|Molly O'Shea]].",
          "Recensée par le wiki. Dans cette mission, la bande s'installe à Beaver Hollow, où Susan abat [[molly-oshea|Molly O'Shea]]."),
        M("Goodbye, Dear Friend", C6,
          "At the end of the mission, back at Beaver Hollow, she hands Arthur a letter from [[mary-linton|Mary Linton]].",
          "À la fin de la mission, de retour à Beaver Hollow, elle remet à Arthur une lettre de [[mary-linton|Mary Linton]]."),
        M("Money Lending and Other Sins VII", C6,
          "Not listed by the wiki. After [[leopold-strauss|Strauss]] is thrown out, she asks Arthur whether she will be next.",
          "Non recensée par le wiki. Après l'expulsion de [[leopold-strauss|Strauss]], elle demande à Arthur si elle sera la prochaine."),
        M("Our Best Selves", C6,
          "Off screen, not listed by the wiki. Milton's men grab Abigail outside camp while she is with Tilly and [[jack-marston|Jack]]; Tilly hides with the boy.",
          "Hors champ, non recensée par le wiki. Les hommes de Milton s'emparent d'Abigail devant le camp, alors qu'elle se trouve avec Tilly et [[jack-marston|Jack]] ; Tilly se cache avec l'enfant."),
        M("Red Dead Redemption", C6,
          "Meets the gang on the road and reports Abigail's capture. Arthur gives her money and sends her with Jack to Copperhead Landing.",
          "Croise la bande sur la route et annonce la capture d'Abigail. Arthur lui donne de l'argent et l'envoie avec Jack à Copperhead Landing."),
    ]}},
    {"h4": two("Red Dead Redemption 2: companion activities, camp request and epilogue", "Red Dead Redemption 2 : activités de compagnon, commande du camp et épilogue")},
    {"table": {"head": [two("Activity", "Activité"), two("Chapter", "Chapitre"), two("Tilly's role", "Rôle de Tilly")], "rows": [
        M("Coach Robbery (Bill Williamson)", C3,
          "Brought along by Arthur as a distraction for [[bill-williamson|Bill]]'s robbery of a Boles Overland banking coach. She argues with Bill and rides off when he opens fire. Available after \"Friends in Very Low Places\" and until \"Blessed are the Peacemakers\".",
          "Emmenée par Arthur pour faire diversion lors de l'attaque d'une diligence bancaire de la Boles Overland montée par [[bill-williamson|Bill]]. Elle se dispute avec Bill et s'en va quand il ouvre le feu. Disponible après \"Friends in Very Low Places\" et jusqu'à \"Blessed are the Peacemakers\"."),
        M(two("Dominoes", "Dominos"), C3,
          "Activity giver. She is the only gang member Arthur can play against in chapter 3.",
          "Donneuse de l'activité. Elle est le seul membre de la bande contre qui Arthur peut jouer au chapitre 3."),
        M(two("Item request", "Commande"), C3,
          "While playing dominoes, she asks Arthur for a necklace. Chapter 3 only; it counts toward the Errand Boy trophy.",
          "Pendant une partie de dominos, elle demande un collier à Arthur. Chapitre 3 uniquement ; la commande compte pour le trophée Errand Boy."),
        M(two("Meeting in Saint Denis", "Rencontre à Saint-Denis"), E2,
          "John can meet her, pregnant, at a trolley stop in Saint Denis. Not a numbered mission.",
          "John peut la croiser, enceinte, à un arrêt de tramway de Saint-Denis. Ce n'est pas une mission numérotée."),
        M(two("Letter from Tilly", "Lettre de Tilly"), E2,
          "Her letter to John and Abigail, readable at Beecher's Hope after the meeting and \"A Quick Favor for an Old Friend\".",
          "Sa lettre à John et Abigail, lisible à Beecher's Hope après la rencontre et \"A Quick Favor for an Old Friend\"."),
        M(two("Bounty: Anthony Foreman", "Prime : Anthony Foreman"), E2,
          "Mentioned, if Arthur spared Foreman. John tells him he is a friend of Tilly's (Red Dead Wiki).",
          "Mentionnée, si Arthur a épargné Foreman. John lui dit être un ami de Tilly (Red Dead Wiki)."),
        M(two("Ending Credits", "Générique de fin"), E2,
          "Seen in a Saint Denis park with her husband and their baby.",
          "Aperçue dans un parc de Saint-Denis avec son mari et leur bébé."),
    ]}},
    {"h3": two("Notable people Tilly kills", "Personnages notables tués par Tilly")},
    {"p": two("The Red Dead Wiki credits Tilly with a single killing, which takes place before the game and is known only from her own account.",
              "Le Red Dead Wiki n'attribue qu'une seule victime à Tilly, tuée avant les événements du jeu et connue uniquement par son propre récit.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K("Malcolm Foreman", two("Before 1899 (told at the Clemens Point camp)", "Avant 1899 (récit au camp de Clemens Point)"),
          "Anthony Foreman's cousin, who had taken her from her mother, according to the Red Dead Wiki's summary of her camp account. She kills him and leaves the Foreman Brothers.",
          "Le cousin d'Anthony Foreman, qui l'avait arrachée à sa mère, d'après le résumé que le Red Dead Wiki donne de son récit au camp. Elle le tue et quitte les frères Foreman."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken or written in the game, in the original English, with the mission and, where relevant, the person addressed.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées ou écrites dans le jeu, en anglais, avec la mission et, le cas échéant, la personne à qui elles s'adressent.")},
    {"h4": two("At Colter", "À Colter")},
    {"quotes": [
        {"q": two("He's strong and he's smart.", "He's strong and he's smart."),
         "src": two("Enter, Pursued by a Memory (RDR2, chapter 1), to Abigail, about John. Abigail answers: \"Strong at least.\"",
                    "Enter, Pursued by a Memory (RDR2, chapitre 1), à Abigail, au sujet de John. Abigail répond : \"Strong at least.\" Traduction : « Il est costaud, et il est malin. » (« Costaud, en tout cas. »)")},
    ]},
    {"h4": two("The trip to Valentine", "La virée à Valentine")},
    {"quotes": [
        {"q": two("Is one of you gonna get that feller's horse?", "Is one of you gonna get that feller's horse?"),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), when a stagecoach loses its horses. Uncle replies: \"Oh, I got lumbago, it's very serious!\"",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), quand une diligence perd ses chevaux. Uncle répond : \"Oh, I got lumbago, it's very serious!\" Traduction : « Y en a un de vous qui va attraper le cheval de ce gars ? » (« Oh, moi j'ai un lumbago, c'est très grave ! »)")},
        {"q": two("Well, Arthur, I'm proud of you.", "Well, Arthur, I'm proud of you."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), if Arthur has helped the driver",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), si Arthur a aidé le cocher. Traduction : « Eh bien, Arthur, je suis fière de toi. »")},
        {"q": two("I imagine Valentine and Paris are easily confused.", "I imagine Valentine and Paris are easily confused."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), after Karen tells the women to imagine they are in Paris",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), après que Karen a proposé aux filles d'imaginer qu'elles sont à Paris. Traduction : « J'imagine qu'on confond facilement Valentine et Paris. »")},
        {"q": two("Just someone I used to know.", "Just someone I used to know."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), when Arthur asks what that was all about",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), quand Arthur lui demande ce qui s'est passé. Traduction : « Juste quelqu'un que j'ai connu. »")},
        {"q": two("Be careful, Arthur.", "Be careful, Arthur."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), as Arthur leaves to chase the man who recognized him from Blackwater. Arthur answers: \"Just a word.\"",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), quand Arthur part poursuivre l'homme qui l'a reconnu de Blackwater. Arthur répond : \"Just a word.\" Traduction : « Fais attention, Arthur. » (« Je vais juste lui dire un mot. »)")},
    ]},
    {"h4": two("The gang's last days", "Les derniers jours de la bande")},
    {"quotes": [
        {"q": two("They came and took Abigail. I saved Jack... we hid, but they took Abigail.", "They came and took Abigail. I saved Jack... we hid, but they took Abigail."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), to the gang on the road back from the train",
                    "Red Dead Redemption (RDR2, chapitre 6), à la bande, sur la route du retour après le train. Traduction : « Ils sont venus et ils ont pris Abigail. J'ai sauvé Jack... on s'est cachés, mais ils ont pris Abigail. »")},
        {"q": two("Agent Milton and his men... took her to Van Horn... to be put on a boat and tried for murder.", "Agent Milton and his men... took her to Van Horn... to be put on a boat and tried for murder."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), when Arthur asks who took Abigail",
                    "Red Dead Redemption (RDR2, chapitre 6), quand Arthur demande qui a emmené Abigail. Traduction : « L'agent Milton et ses hommes... l'ont emmenée à Van Horn... pour la mettre sur un bateau et la faire juger pour meurtre. »")},
        {"q": two("Alright, Arthur. I'll... I'll miss...", "Alright, Arthur. I'll... I'll miss..."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), after Arthur gives her money. With high honor Arthur answers: \"Me too, sweetheart... me too...\"; with low honor: \"No… no don't start with all that.\"",
                    "Red Dead Redemption (RDR2, chapitre 6), après qu'Arthur lui a donné de l'argent. Avec un honneur élevé, Arthur répond : \"Me too, sweetheart... me too...\" ; avec un honneur bas : \"No… no don't start with all that.\" Traduction : « D'accord, Arthur. Tu vas... tu vas me manquer... » (« Toi aussi, ma belle... toi aussi... » ; « Non... non, commence pas avec ça. »)")},
    ]},
    {"h4": two("Said to her", "Ce qu'on lui dit")},
    {"quotes": [
        {"q": two("Miss Tilly, Miss Karen, would you warm her up...give her a drink of something.", "Miss Tilly, Miss Karen, would you warm her up...give her a drink of something."),
         "src": two("Dutch van der Linde, Outlaws from the West (RDR2, chapter 1), on bringing Sadie Adler into the Colter camp",
                    "Dutch van der Linde, Outlaws from the West (RDR2, chapitre 1), en ramenant Sadie Adler au camp de Colter. Traduction : « Mademoiselle Tilly, mademoiselle Karen, vous voulez bien la réchauffer... lui donner quelque chose à boire. »")},
        {"q": two("Get your goddamn hands off of her.", "Get your goddamn hands off of her."),
         "src": two("Arthur Morgan to the Foreman man, Polite Society, Valentine Style (RDR2, chapter 2), if he chooses to intervene. Asked who he is, Tilly answers: \"A friend of mine...\"",
                    "Arthur Morgan à l'homme des Foreman, Polite Society, Valentine Style (RDR2, chapitre 2), s'il choisit d'intervenir. Quand l'homme demande qui il est, Tilly répond : \"A friend of mine...\" Traduction : « Enlève tes sales pattes de là. » (« Un ami à moi... »)")},
        {"q": two("You're a good girl... you live a good life now, you hear?", "You're a good girl... you live a good life now, you hear?"),
         "src": two("Arthur Morgan, Red Dead Redemption (RDR2, chapter 6), with high honor, after sending her to Copperhead Landing with Jack. With low honor: \"Just get out of here and go live your life… this is done.\"",
                    "Arthur Morgan, Red Dead Redemption (RDR2, chapitre 6), avec un honneur élevé, après l'avoir envoyée à Copperhead Landing avec Jack. Avec un honneur bas : \"Just get out of here and go live your life… this is done.\" Traduction : « T'es une brave fille... vis une belle vie maintenant, t'entends ? » (« Va-t'en d'ici et va vivre ta vie... c'est fini. »)")},
    ]},
    {"h4": two("Her letter, 1907", "Sa lettre, 1907")},
    {"quotes": [
        {"q": two("I miss him and I think it was that time I spent being an aunt to him that made me want to be a mother myself. You were quite right, Abigail, it is the greatest feeling alive.", "I miss him and I think it was that time I spent being an aunt to him that made me want to be a mother myself. You were quite right, Abigail, it is the greatest feeling alive."),
         "src": two("Letter from Tilly (RDR2, epilogue), about Jack",
                    "Lettre de Tilly (RDR2, épilogue), au sujet de Jack. Traduction : « Il me manque, et je crois que c'est le temps passé à jouer les tantes pour lui qui m'a donné envie d'être mère à mon tour. Tu avais bien raison, Abigail, c'est le plus beau sentiment qui soit. »")},
        {"q": two("Silly old Miss Grimshaw and angry Mr. Pearson, and kindly Hosea, who was like a father to me, and you both and poor dear Arthur and all them bastards, and Karen who was a sister to me, and who I miss every day. I never heard what happened to her but, deep down I know the drink did for her.", "Silly old Miss Grimshaw and angry Mr. Pearson, and kindly Hosea, who was like a father to me, and you both and poor dear Arthur and all them bastards, and Karen who was a sister to me, and who I miss every day. I never heard what happened to her but, deep down I know the drink did for her."),
         "src": two("Letter from Tilly (RDR2, epilogue), on the people she misses from the old days",
                    "Lettre de Tilly (RDR2, épilogue), sur les gens du passé qui lui manquent. Traduction : « Cette vieille bécasse de Miss Grimshaw et ce grincheux de M. Pearson, et ce bon Hosea, qui a été comme un père pour moi, et vous deux, et ce pauvre cher Arthur, et tous ces salauds, et Karen, qui était une sœur pour moi et qui me manque chaque jour. Je n'ai jamais su ce qu'elle était devenue mais, au fond, je sais que la boisson l'a emportée. »")},
        {"q": two("I feel like the biggest fraud alive, but my husband, who is a very understanding man, tells me everyone is a fraud and we are all the same underneath, and I know he speaks the truth.", "I feel like the biggest fraud alive, but my husband, who is a very understanding man, tells me everyone is a fraud and we are all the same underneath, and I know he speaks the truth."),
         "src": two("Letter from Tilly (RDR2, epilogue)",
                    "Lettre de Tilly (RDR2, épilogue). Traduction : « J'ai l'impression d'être la plus grande imposture qui soit, mais mon mari, un homme très compréhensif, me dit que tout le monde joue la comédie et qu'au fond nous sommes tous pareils, et je sais qu'il a raison. »")},
        {"q": two("I just wanted to share my happy news with you for you are my family, only one I really got, aside from my husband and baby girl.", "I just wanted to share my happy news with you for you are my family, only one I really got, aside from my husband and baby girl."),
         "src": two("Letter from Tilly (RDR2, epilogue), closing lines",
                    "Lettre de Tilly (RDR2, épilogue), dernières lignes. Traduction : « Je voulais simplement partager mon bonheur avec vous, parce que vous êtes ma famille, la seule que j'aie vraiment, en dehors de mon mari et de ma petite fille. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("In a camp conversation during chapter 2, Tilly can tell Arthur about an illegal O'Driscoll business run from the back room of the Valentine Doctor's Office, which Arthur can then rob. According to the wiki's page on the building, the player can also learn about it by looking through a back window, by watching lawmen take a bribe at the back door, or by knocking on one of its locked doors.",
            "Lors d'une conversation au camp, au chapitre 2, Tilly peut parler à Arthur d'un trafic des O'Driscoll installé dans l'arrière-boutique du cabinet du médecin de Valentine, qu'Arthur peut ensuite dévaliser. D'après la page du bâtiment sur le wiki, le joueur peut aussi le découvrir en regardant par une fenêtre de derrière, en surprenant des hommes de loi qui touchent un pot-de-vin à la porte de service, ou en frappant à l'une des portes verrouillées."),
        two("According to the wiki's list of camp events, Tilly, Mary-Beth and Susan are unavailable in camp once \"No, No and Thrice, No\" is unlocked. Tilly misses the party for Jack's return at Shady Belle; if she has already been rescued, she is asleep inside the house.",
            "D'après la liste des scènes de camp du wiki, Tilly, Mary-Beth et Susan ne sont plus disponibles au camp dès que \"No, No and Thrice, No\" est débloquée. Tilly manque la fête donnée à Shady Belle pour le retour de Jack ; si elle a déjà été libérée, elle dort à l'intérieur de la maison."),
        two("The mission page of \"Horsemen, Apocalypses\" notes that Tilly, along with Micah, Lenny, Bill, Javier, Trelawny and Uncle, does not appear during the O'Driscoll attack on Shady Belle, and that the game never explains their absence.",
            "La page de la mission \"Horsemen, Apocalypses\" relève que Tilly, comme Micah, Lenny, Bill, Javier, Trelawny et Uncle, n'apparaît pas pendant l'attaque des O'Driscoll contre Shady Belle, et que le jeu n'explique jamais leur absence."),
        two("Tilly's letter is missable content. The wiki warns that it disappears if the player saves and reloads before reading it, and it cannot be kept among the player's documents.",
            "La lettre de Tilly fait partie des contenus manquables. Le wiki prévient qu'elle disparaît si le joueur sauvegarde et recharge sa partie avant de la lire, et qu'elle ne peut pas être conservée parmi les documents du joueur."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("On September 6, 2018, Rockstar posted Tilly Jackson's portrait and character description on Twitter, in a series covering the members of the gang, and The Hollywood Reporter reproduced the series the next day. In the composite of 23 gang members' official art designs that illustrates Wikipedia's list of the game's characters, she stands in the front row, between Sean MacGuire and Susan Grimshaw.",
              "Le 6 septembre 2018, Rockstar publie sur Twitter le portrait de Tilly Jackson et sa description, dans une série consacrée aux membres de la bande, et The Hollywood Reporter reprend la série le lendemain. Sur le montage des illustrations officielles de 23 membres de la bande qui ouvre la liste des personnages du jeu sur Wikipédia, elle figure au premier rang, entre Sean MacGuire et Susan Grimshaw.")},
    {"h4": two("Red Dead Online", "Red Dead Online")},
    {"p": two("The Red Dead Wiki lists Tilly in Red Dead Redemption 2 only. Anthony Foreman, the outlaw who hunts her in 1899, returns in Red Dead Online as a stranger who offers jobs to the player at Radley's House or Doyle's Tavern in Saint Denis, and later as part of the Blood Money update.",
              "Le Red Dead Wiki ne mentionne Tilly que dans Red Dead Redemption 2. Anthony Foreman, le hors-la-loi qui la traque en 1899, revient dans Red Dead Online comme inconnu proposant des contrats au joueur à Radley's House ou au Doyle's Tavern de Saint-Denis, puis dans la mise à jour Blood Money.")},
]
