"""Mary-Beth Gaskill, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/mary/, cov/mary/m/ and
cov/mary/w/):
- Red Dead Wiki EN "Mary-Beth Gaskill" (Mission Appearances, Trivia, Gallery) and FR "Mary-Beth Gaskill" (fr.txt:
  eleven missions, cites Rockstar's French "vanderlindegang" page, archived on July 6, 2022).
- Transcripts "/dialogues": Outlaws from the West; Enter, Pursued by a Memory; Eastward Bound; Polite Society,
  Valentine Style; Who is Not Without Sin; Pouring Forth Oil I; Blessed are the Peacemakers; American Venom (credits
  list). Every quoted mission line below is checked word for word against them. "Well, she was a fool then, Arthur"
  is checked against the quote lists of the mission pages "No, No and Thrice, No" (trivia) and "A Fork in the Road"
  (recalled lines). No transcript exists on the wiki for No, No and Thrice, No; Horsemen, Apocalypses; Visiting Hours;
  That's Murfree Country; A Rage Unleashed; Angelo Bronte, A Man of Honor; Our Best Selves; the Coach Robbery; the
  epilogue encounter (checked 20 Oct 2026). The local transcript of The Battle of Shady Belle has no Mary-Beth line.
- Mission pages: Coach Robbery (Sean MacGuire) (reward, deaths, availability, hostage trivia); Pouring Forth Oil IV;
  No, No and Thrice, No (giver: Mary-Beth/Susan); A Fork in the Road and Red Dead Redemption (recalled lines, high
  honor); Horsemen, Apocalypses; Visiting Hours; Our Best Selves; pages "Harry" and "Laurence" (names of the coach
  driver and co-driver); "Valentine Station"; "Romance Novel Proves Best Seller"; "The Lady of the Manor" (book text);
  "Letter from Tilly"; "Ending Credits"; "Camp Events" (availability).
- Real world: Rockstar's character portraits and descriptions posted on Twitter on September 6, 2018, reproduced by
  The Hollywood Reporter on September 7, 2018 (../uncle/fc/thr_descriptions.txt: "Mary-Beth Gaskill" entry present);
  Wikipedia "List of Red Dead Redemption 2 characters" (caption of the 23-member composite: front row, between Molly
  and Karen).
Ownership (FIX_RULES), left to other parts: all narrative (A); personality, the Rockstar and guide descriptions as
text, names and pen names, the notebook, the fountain pen and ring, appearance, skills, camp scenes and camp lines
(the "lost" line, "Maybe it's a sign", Kieran, Karen, Tilly, Susan, Dutch, Sean's party) (B); Samantha Strelitz,
interviews, cut content, reception (D).
Quotes: mission lines only, each in ONE place; part A paraphrases them. Tilly's letter and the newspaper headline are
quoted here only.
Kills: the character page has no "Murders Committed" section; in the Coach Robbery the deaths are credited to Arthur
and Sean, not to her: no kills table.
Excluded: the Diane Lane / Lonesome Dove outfit inspiration and the Leslie A. Dupont nod (wiki trivia, both
speculative: "may have been inspired", "possibly a nod"); Arthur's estimate of her age and her mother from New
Hanover (camp, part B); the wiki trivia that she and Charles are the only members Arthur tells about his illness
(part B, and contradicted elsewhere: Arthur also tells others in camp according to the fact-checked arthur parts);
"implicitly fallen in love" with Kieran (interpretation); the FR wiki's "her words are the last heard" on the last
ride (contradicted by the mission page list).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
EP = two("Epilogue", "Épilogue")
EP2 = two("Epilogue 2: Beecher's Hope", "Épilogue 2 : Beecher's Hope")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists fifteen story missions of Red Dead Redemption 2 for Mary-Beth, two of them as voice only and one as credits only, plus her epilogue encounter and one companion activity. The French Red Dead Wiki lists eleven of the same missions. The first table follows the English list and adds the missions in which she has a line in camp or is mentioned; the second covers the epilogue.",
              "Le Red Dead Wiki anglais recense quinze missions principales de Red Dead Redemption 2 pour Mary-Beth, dont deux où l'on n'entend que sa voix et une où elle n'apparaît qu'au générique, ainsi que sa rencontre de l'épilogue et une activité avec un compagnon. Le Red Dead Wiki français en cite onze. Le premier tableau suit la liste anglaise et y ajoute les missions où elle a une réplique au camp ou est mentionnée ; le second couvre l'épilogue.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 to 6", "Red Dead Redemption 2, chapitres 1 à 6")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Mary-Beth's role", "Rôle de Mary-Beth")], "rows": [
        M("Outlaws from the West", C1,
          "At Colter. [[susan-grimshaw|Susan Grimshaw]] tells her to light the fire in the main cabin.",
          "À Colter. [[susan-grimshaw|Susan Grimshaw]] lui demande d'allumer le feu dans la cabane principale."),
        M("Enter, Pursued by a Memory", C1,
          "Sits by the fire with [[tilly-jackson|Tilly]] and [[abigail-marston|Abigail]] when [[arthur-morgan|Arthur]] comes in; no line.",
          "Assise devant le feu avec [[tilly-jackson|Tilly]] et [[abigail-marston|Abigail]] quand [[arthur-morgan|Arthur]] entre ; aucune réplique."),
        M("Eastward Bound", C1,
          "Told by Susan to put her book away and help load the wagons before the move to Horseshoe Overlook.",
          "Susan lui ordonne de ranger son livre et d'aider à charger les chariots avant le départ pour Horseshoe Overlook."),
        M("Polite Society, Valentine Style", C2,
          "Rides to Valentine with Arthur, [[uncle|Uncle]], [[karen-jones|Karen]] and Tilly. Brings back the tip about a train of rich tourists and spots the Foreman man who grabs Tilly.",
          "Part pour Valentine avec Arthur, [[uncle|Uncle]], [[karen-jones|Karen]] et Tilly. Rapporte le tuyau sur un train de riches touristes et repère l'homme des Foreman qui s'en prend à Tilly."),
        M("Who is Not Without Sin", C2,
          "At camp. Can answer if Arthur greets her while carrying a drunk [[orville-swanson|Reverend Swanson]] to his tent. Not listed by the wiki.",
          "Au camp. Peut répondre si Arthur la salue en ramenant sous sa tente le [[orville-swanson|révérend Swanson]], ivre. Mission non citée par le wiki."),
        M("Pouring Forth Oil I", C2,
          "Mentioned. [[john-marston|John]] passes on her tip about the train, relayed by Uncle. Not listed by the wiki.",
          "Mentionnée. [[john-marston|John]] transmet son tuyau sur le train, relayé par Uncle. Mission non citée par le wiki."),
        M(two("Coach Robbery (Sean MacGuire)", "Coach Robbery (Sean MacGuire)"), C3,
          "Companion activity. Stops a Boles Overland banking coach near Face Rock by pretending to have lost her memory, while Arthur and [[sean-macguire|Sean]] shoot the escort. Take: 305 dollars, 55 for the player.",
          "Activité avec un compagnon. Arrête une diligence de banque de la Boles Overland près de Face Rock en jouant les amnésiques, pendant qu'Arthur et [[sean-macguire|Sean]] abattent l'escorte. Butin : 305 dollars, dont 55 pour le joueur."),
        M("Blessed are the Peacemakers", C3,
          "At camp. First to call out to Arthur when he collapses after escaping the O'Driscolls, before Karen and [[dutch-van-der-linde|Dutch]].",
          "Au camp. La première à appeler Arthur quand il s'effondre après avoir échappé aux O'Driscoll, avant Karen et [[dutch-van-der-linde|Dutch]]."),
        M("The Battle of Shady Belle", C3,
          "Listed by the Red Dead Wiki; not named in the mission page or transcript.",
          "Citée par le Red Dead Wiki ; ni la page ni la transcription ne la nomment."),
        M("Angelo Bronte, A Man of Honor", C4,
          "At camp for the party that celebrates [[jack-marston|Jack]]'s return.",
          "Au camp pour la fête qui célèbre le retour de [[jack-marston|Jack]]."),
        M("No, No and Thrice, No", C4,
          "Co-giver with Susan. Shares a cigarette with Arthur until Susan announces that Tilly has been kidnapped.",
          "Donneuse de la mission avec Susan. Fume une cigarette avec Arthur jusqu'à ce que Susan annonce l'enlèvement de Tilly."),
        M("Horsemen, Apocalypses", C4,
          "Screams on recognizing [[kieran-duffy|Kieran Duffy]]'s body, then takes cover in the house during the O'Driscoll attack.",
          "Hurle en reconnaissant le corps de [[kieran-duffy|Kieran Duffy]], puis s'abrite dans la maison pendant l'attaque des O'Driscoll."),
        M("A Fork in the Road", C5,
          "Voice only. With high honor, Arthur remembers her remark about [[mary-linton|Mary Linton]].",
          "Voix seulement. Avec un honneur élevé, Arthur se souvient de sa remarque sur [[mary-linton|Mary Linton]]."),
        M("That's Murfree Country", C5,
          "Listed by the Red Dead Wiki; not named in the mission page.",
          "Citée par le Red Dead Wiki ; la page de la mission ne la nomme pas."),
        M("Visiting Hours", C6,
          "After John's rescue, wakes Arthur to tell him Dutch wants him in Annesburg.",
          "Après l'évasion de John, réveille Arthur pour lui dire que Dutch l'attend à Annesburg."),
        M("A Rage Unleashed", C6,
          "Listed by the Red Dead Wiki; not named in the mission page.",
          "Citée par le Red Dead Wiki ; la page de la mission ne la nomme pas."),
        M("Our Best Selves", C6,
          "Absent. Dutch names her, with Uncle and [[simon-pearson|Pearson]], among the cowards who have run off. Not listed by the wiki.",
          "Absente. Dutch la cite, avec Uncle et [[simon-pearson|Pearson]], parmi les lâches qui se sont enfuis. Mission non citée par le wiki."),
        M("Red Dead Redemption", C6,
          "Voice only. With high honor, Arthur remembers two lines from their camp conversations on his last ride.",
          "Voix seulement. Avec un honneur élevé, Arthur se souvient de deux répliques de leurs conversations au camp pendant sa dernière chevauchée."),
    ]}},
    {"h4": two("Red Dead Redemption 2, epilogue", "Red Dead Redemption 2, épilogue")},
    {"table": {"head": [two("Mission or document", "Mission ou document"), two("Chapter", "Chapitre"), two("Mary-Beth's role", "Rôle de Mary-Beth")], "rows": [
        M(two("Encounter at Valentine station", "Rencontre à la gare de Valentine"), EP,
          "Talks with John on the platform, gives him a copy of \"The Lady of the Manor\" and boards a train.",
          "Discute avec John sur le quai, lui offre un exemplaire de \"The Lady of the Manor\" et monte dans un train."),
        M(two("Romance Novel Proves Best Seller", "Romance Novel Proves Best Seller"), EP,
          "Newspaper article on the success of Leslie Dupont, her pen name.",
          "Article de presse sur le succès de Leslie Dupont, son nom de plume."),
        M(two("Letter from Tilly", "Lettre de Tilly"), EP2,
          "Tilly writes to Abigail and John that she still sees Mary-Beth, now a novelist.",
          "Tilly écrit à Abigail et à John qu'elle voit toujours Mary-Beth, devenue romancière."),
        M("American Venom", EP2,
          "Credits only. The end credits show her writing at a desk.",
          "Générique seulement. Le générique de fin la montre en train d'écrire à un bureau."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the context. Her camp lines are given in other sections of this profile.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et le contexte. Ses répliques de camp figurent dans d'autres sections de cette fiche.")},
    {"h4": two("Valentine, chapter 2", "Valentine, chapitre 2")},
    {"quotes": [
        {"q": two("We're bored out of our minds. Been cooped up here for two weeks now. Karen's about ready to murder Grimshaw.", "We're bored out of our minds. Been cooped up here for two weeks now. Karen's about ready to murder Grimshaw."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), to Arthur, backing up Karen's request to come along",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à Arthur, pour appuyer la demande de Karen. Traduction : « On s'ennuie à mourir. Ça fait deux semaines qu'on est enfermées ici. Karen est à deux doigts d'assassiner Grimshaw. »")},
        {"q": two("Look at all that snow on the mountains. Sure don't want to be back up there.", "Look at all that snow on the mountains. Sure don't want to be back up there."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), arriving in Valentine",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), à l'arrivée à Valentine. Traduction : « Regardez toute cette neige sur les montagnes. Je n'ai vraiment pas envie d'y retourner. »")},
        {"q": two("Gentlemen. I think I've got something good. I snuck into this fancy house... and acted like a servant girl... usually works.", "Gentlemen. I think I've got something good. I snuck into this fancy house... and acted like a servant girl... usually works."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), joining Arthur and Uncle on the bench outside the general store",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), en rejoignant Arthur et Uncle sur le banc devant le magasin général. Traduction : « Messieurs. Je crois que je tiens quelque chose. Je me suis glissée dans une belle maison... en me faisant passer pour une domestique... ça marche presque toujours. »")},
        {"q": two("Train full of rich tourists, heading to Saint Denis... and then cruising off to Brazil.", "Train full of rich tourists, heading to Saint Denis... and then cruising off to Brazil."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), describing the tip she overheard",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), en décrivant le tuyau qu'elle a surpris. Traduction : « Un train rempli de riches touristes, direction Saint-Denis... et ensuite une croisière jusqu'au Brésil. »")},
        {"q": two("Oh, there's Tilly over there... that does not look ideal.", "Oh, there's Tilly over there... that does not look ideal."),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), spotting Tilly in a struggle near the hotel. She adds: \"That's one of them Foreman boys.\"",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), en apercevant Tilly aux prises avec un homme près de l'hôtel. Elle ajoute : \"That's one of them Foreman boys.\" Traduction : « Oh, voilà Tilly là-bas... ça n'a pas l'air idéal. » (« C'est un des frères Foreman. »)")},
        {"q": two("Hey, who's that guy over there looking at us?", "Hey, who's that guy over there looking at us?"),
         "src": two("Polite Society, Valentine Style (RDR2, chapter 2), noticing Jimmy Brooks, who then claims he saw Arthur in Blackwater",
                    "Polite Society, Valentine Style (RDR2, chapitre 2), en remarquant Jimmy Brooks, qui affirme ensuite avoir vu Arthur à Blackwater. Traduction : « Hé, c'est qui, le type là-bas qui nous regarde ? »")},
    ]},
    {"h4": two("At camp and Shady Belle, chapters 2 and 4", "Au camp et à Shady Belle, chapitres 2 et 4")},
    {"quotes": [
        {"q": two("Oh, Reverend...", "Oh, Reverend..."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), if Arthur greets her while carrying a drunk Reverend Swanson through camp",
                    "Who is Not Without Sin (RDR2, chapitre 2), si Arthur la salue en traversant le camp avec le révérend Swanson, ivre. Traduction : « Oh, révérend... »")},
        {"q": two("Well, she was a fool then, Arthur.", "Well, she was a fool then, Arthur."),
         "src": two("No, No and Thrice, No (RDR2, chapter 4), about Mary Linton, at the start of the mission. Arthur remembers the line in A Fork in the Road if his honor is high.",
                    "No, No and Thrice, No (RDR2, chapitre 4), au sujet de Mary Linton, au début de la mission. Arthur se souvient de cette phrase dans A Fork in the Road si son honneur est élevé. Traduction : « Eh bien, c'était une idiote, alors, Arthur. »")},
    ]},
    {"h4": two("Said about her", "Ce qu'on dit d'elle")},
    {"quotes": [
        {"q": two("Miss Gaskill... get that fire lit quick.", "Miss Gaskill... get that fire lit quick."),
         "src": two("Susan Grimshaw, Outlaws from the West (RDR2, chapter 1), on entering the Colter cabin",
                    "Susan Grimshaw, Outlaws from the West (RDR2, chapitre 1), en entrant dans la cabane de Colter. Traduction : « Mademoiselle Gaskill... allumez-moi ce feu, et vite. »")},
        {"q": two("Oh, for Lord's sake. Put that book away and go help. Oh... Mary-Beth.", "Oh, for Lord's sake. Put that book away and go help. Oh... Mary-Beth."),
         "src": two("Susan Grimshaw, Eastward Bound (RDR2, chapter 1), as the gang loads the wagons to leave Colter",
                    "Susan Grimshaw, Eastward Bound (RDR2, chapitre 1), pendant que la bande charge les chariots pour quitter Colter. Traduction : « Oh, pour l'amour du ciel. Range ce livre et va aider. Oh... Mary-Beth. »")},
        {"q": two("Mary-Beth overheard something about a train... full of wealthy folk...", "Mary-Beth overheard something about a train... full of wealthy folk..."),
         "src": two("John Marston to Arthur, Pouring Forth Oil I (RDR2, chapter 2)",
                    "John Marston à Arthur, Pouring Forth Oil I (RDR2, chapitre 2). Traduction : « Mary-Beth a entendu parler d'un train... plein de gens riches... »")},
        {"q": two("I still see my darling Mary Beth, who is now a lady novelist which both surprised me and did not surprise me at all, if that makes any sense.", "I still see my darling Mary Beth, who is now a lady novelist which both surprised me and did not surprise me at all, if that makes any sense."),
         "src": two("Tilly Jackson, letter to Abigail and John Marston (RDR2, epilogue 2, 1907), signed \"Yours, Tilly\"",
                    "Tilly Jackson, lettre à Abigail et John Marston (RDR2, épilogue 2, 1907), signée \"Yours, Tilly\". Traduction : « Je vois toujours ma chère Mary Beth, qui est maintenant romancière, ce qui m'a à la fois surprise et pas surprise du tout, si ça a un sens. »")},
        {"q": two("Overnight success. Author Leslie Dupont's fourth tome proving very successful.", "Overnight success. Author Leslie Dupont's fourth tome proving very successful."),
         "src": two("Headline of the article \"Romance Novel Proves Best Seller\" (RDR2, epilogue, 1907), printed in capitals in the Blackwater Ledger, the New Hanover Gazette and the Saint Denis Times",
                    "Titre de l'article \"Romance Novel Proves Best Seller\" (RDR2, épilogue, 1907), imprimé en capitales dans le Blackwater Ledger, la New Hanover Gazette et le Saint Denis Times. Traduction : « Succès immédiat. Le quatrième ouvrage de l'auteure Leslie Dupont fait un triomphe. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("The Red Dead Wiki gives the text of chapter 6 of \"The Lady of the Manor\", titled \"A Twist of the Knife of Time\". In it, Susan Grade, Lady of Leicester, faces David Vincent, a highwayman known as the Black Knight, who has killed her husband, while a police inspector, Mr. Mellon, waits outside. Vincent puts her yellow silk gown on a mop and holds it out of the window, where it draws five shots, then leads her away across the castle rooftops.",
            "Le Red Dead Wiki reproduit le chapitre 6 de \"The Lady of the Manor\", intitulé \"A Twist of the Knife of Time\". Susan Grade, Lady of Leicester, y fait face à David Vincent, un bandit de grand chemin surnommé le Chevalier noir, qui a tué son mari, pendant qu'un inspecteur de police, Mr. Mellon, attend dehors. Vincent enfile sa robe de soie jaune sur un balai et la tend par la fenêtre, où elle essuie cinq coups de feu, puis l'entraîne sur les toits du château."),
        two("The in-game description of \"The Lady of the Manor\" calls it an audacious new romance by Leslie Dupont.",
            "Dans le jeu, la description de \"The Lady of the Manor\" présente le livre comme une nouvelle romance audacieuse signée Leslie Dupont."),
        two("The coach driver and co-driver of the Coach Robbery are named Laurence and Harry on the Red Dead Wiki.",
            "Le Red Dead Wiki nomme Laurence et Harry le cocher et son second dans le Coach Robbery."),
        two("Attacking, killing or abandoning Mary-Beth fails \"Polite Society, Valentine Style\", as it does for Uncle, Tilly and Karen. In \"Horsemen, Apocalypses\", the mission fails if any member of the gang is attacked, abandoned or killed.",
            "Attaquer, tuer ou abandonner Mary-Beth fait échouer \"Polite Society, Valentine Style\", comme pour Uncle, Tilly et Karen. Dans \"Horsemen, Apocalypses\", la mission échoue si un membre de la bande est attaqué, abandonné ou tué."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Mary-Beth for Red Dead Redemption 2. On September 6, 2018, it posted her portrait and character description (quoted under Personality) on Twitter, in a series covering the members of the gang; The Hollywood Reporter reproduced the series on September 7, 2018. The same descriptions appear on a page of Rockstar's website presenting the Van der Linde gang; the French version, cited by the French Red Dead Wiki, was archived on July 6, 2022. In the composite image of the 23 gang members that opens Wikipedia's list of the game's characters, Mary-Beth stands in the front row, between [[molly-oshea|Molly]] and [[karen-jones|Karen]].",
              "Rockstar a publié une illustration officielle de Mary-Beth pour Red Dead Redemption 2. Le 6 septembre 2018, l'éditeur diffuse sur Twitter son portrait et sa description (citée dans Personnalité), dans une série consacrée aux membres de la bande ; The Hollywood Reporter reprend la série le 7 septembre 2018. Les mêmes descriptions figurent sur une page du site de Rockstar qui présente la bande Van der Linde ; la version française, citée par le Red Dead Wiki français, a été archivée le 6 juillet 2022. Sur l'image réunissant les 23 membres de la bande, en tête de la liste des personnages du jeu sur Wikipédia, Mary-Beth figure au premier rang, entre [[molly-oshea|Molly]] et [[karen-jones|Karen]].")},
]
