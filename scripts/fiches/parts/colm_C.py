"""Colm O'Driscoll, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/colm/ and cov/colm/m/):
- Red Dead Wiki EN "Colm O'Driscoll" (Mission Appearances: "Old Friends", "Blessed are the Peacemakers",
  "Goodbye, Dear Friend"; Quotes; Trivia), "O'Driscoll Boys" (Red Dead Online section, hideouts), "O'Driscoll
  Captured" (newspaper issues), "Letter to Tom from Colm" (text), "Annabelle" (subtitle spelling).
- Mission pages: Outlaws from the West; Old Friends; Who the Hell is Leviticus Cornwall?; The Aftermath of Genesis;
  Paying a Social Call; Blessed are the Peacemakers; Horsemen, Apocalypses (trivia: the O'Driscoll asking about
  Arthur's shoulder); Icarus and Friends; Goodbye, Dear Friend (failure conditions, gold medal objectives, "Third Time
  Lucky" achievement); Mrs. Sadie Adler, Widow (I and II); Red Dead Redemption (mission).
- Transcripts: Blessed are the Peacemakers/dialogues (every Colm line below is checked word for word against it);
  Old Friends/dialogues, Outlaws from the West/dialogues and The Aftermath of Genesis/dialogues (lines about Colm).
- Fact-checked part sadie_C (the four characters with a recurring musical theme, Colm among them).
Quotes: only transcript-verified lines and the letter text. Colm's last words in "Goodbye, Dear Friend" ("As well you
may. I've been a bad man. These charges...") appear only in the character page's quote list, with no transcript on
the wiki: they are paraphrased, attributed, in part A and not quoted here. The wiki's version of the "fine gun" line
drops the word "ride"; the transcript wording is used. The "Hello, Dutch" exchange line "So, uh... how's your gang
doing?" is formatted under Dutch's name in the transcript by a typo, but follows "Colm:" inside the line.
Ownership: narrative events stay in part A (one line per mission here); Kieran's descriptions of Colm, the name
pronunciation (Sean, Kieran, Roger Clark), appearance, weapons and horse go to part B; Andrew Berg, the cut unique
horse, the real-life Colm O'Driscoll story (LADbible, November 7, 2018) and other real-world material go to part D.
Excluded: the O'Driscoll Boys page's comparison with the Dalton gang (not about Colm); "Colm is one of very few
characters" is kept as a plain statement, without the wiki's "very few" ranking; Arthur's "That man can really hate"
(quote box of the character page only, no transcript; paraphrased in part A).
Fact-check fixes (20 Oct 2026): "Blessed are the Meek?" and "An American Pastoral Scene" added to the second
table (the Biography cites them); Quotes keep only Colm lines NOT quoted in part B "In his own words" ("Lot of heat
on us...", "we lure an angry Dutch in...", two letter lines); "Lot of heat" comes BEFORE Dutch's "Why didn't you
take it?" (transcript l.129-131); the "About Colm" block is dropped (lines live in part B Relationships > Dutch and
part A); trivia on cutscenes and the Red Dead Online paragraph rewritten (too close to the wiki).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The Red Dead Wiki lists three missions of Red Dead Redemption 2 in which Colm appears on screen, one in each of chapters 1, 3 and 6. The French edition gives the same three. In several other missions he is only talked about, or his gang acts in his name; they are listed in the second table.",
              "Le Red Dead Wiki recense trois missions de Red Dead Redemption 2 où Colm apparaît à l'écran, une dans chacun des chapitres 1, 3 et 6. L'édition française retient les trois mêmes. Dans plusieurs autres missions, il n'est qu'évoqué, ou sa bande agit en son nom ; elles figurent dans le second tableau.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Colm's role", "Rôle de Colm")], "rows": [
        M("Old Friends", C1,
          "Seen through binoculars at the O'Driscoll camp in Ewing Basin, where he strikes [[kieran-duffy|Kieran Duffy]]. He leaves before the Van der Linde gang attacks.",
          "Observé à la jumelle au camp O'Driscoll d'Ewing Basin, où il frappe [[kieran-duffy|Kieran Duffy]]. Il s'en va avant l'attaque de la bande Van der Linde."),
        M("Blessed are the Peacemakers", C3,
          "Meets [[dutch-van-der-linde|Dutch]] for a parley used as a decoy, then visits the captured [[arthur-morgan|Arthur]] at Lone Mule Stead.",
          "Rencontre [[dutch-van-der-linde|Dutch]] pour des pourparlers qui servent de leurre, puis rend visite à [[arthur-morgan|Arthur]], capturé, à Lone Mule Stead."),
        M("Goodbye, Dear Friend", C6,
          "Hanged in Saint Denis, after Dutch, Arthur and [[sadie-adler|Sadie Adler]] have foiled his gang's rescue attempt.",
          "Pendu à Saint-Denis, après que Dutch, Arthur et [[sadie-adler|Sadie Adler]] ont déjoué la tentative de sauvetage de sa bande."),
    ]}},
    {"h4": two("Missions in which he is mentioned or his gang acts", "Missions où il est évoqué ou où sa bande intervient")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Colm", "Lien avec Colm")], "rows": [
        M("Outlaws from the West", C1,
          "His men occupy the Adler ranch. A captured O'Driscoll says where Colm is camped and that the gang plans a train robbery.",
          "Ses hommes occupent le ranch Adler. Un O'Driscoll capturé indique où campe Colm et révèle que la bande prépare l'attaque d'un train."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "The Van der Linde gang robs the Cornwall train the O'Driscolls had planned to rob, using their plans.",
          "La bande Van der Linde braque le train de Cornwall que les O'Driscoll comptaient attaquer, en se servant de leurs plans."),
        M("The Aftermath of Genesis", C1,
          "Arthur describes the feud between Colm and Dutch to [[charles-smith|Charles Smith]] on a hunting trip.",
          "Pendant une partie de chasse, Arthur décrit à [[charles-smith|Charles Smith]] la vendetta entre Colm et Dutch."),
        M("Paying a Social Call", C2,
          "Kieran leads Arthur, [[john-marston|John]] and [[bill-williamson|Bill]] to Six Point Cabin, where Colm is supposed to be hiding. He is not there.",
          "Kieran conduit Arthur, [[john-marston|John]] et [[bill-williamson|Bill]] à Six Point Cabin, où Colm est censé se cacher. Il n'y est pas."),
        M("Blessed are the Meek?", C2,
          "Micah, jailed in Strawberry, shoots his O'Driscoll cellmate as he escapes.",
          "Micah, enfermé à Strawberry, abat son codétenu O'Driscoll en s'évadant."),
        M("An American Pastoral Scene", C2,
          "A band of O'Driscolls attacks Arthur and Micah to take the banking coach they have just stolen.",
          "Une troupe d'O'Driscoll attaque Arthur et Micah pour leur reprendre la diligence de banque qu'ils viennent de voler."),
        M("Horsemen, Apocalypses", C4,
          "His gang sends Kieran's mutilated body into Shady Belle and attacks the camp.",
          "Sa bande renvoie le corps mutilé de Kieran à Shady Belle et attaque le camp."),
        M("Icarus and Friends", C6,
          "Sadie tells Arthur that Colm has been caught and sentenced to hang.",
          "Sadie apprend à Arthur que Colm a été arrêté et condamné à la pendaison."),
        M("Mrs. Sadie Adler, Widow", C6,
          "Arthur and Sadie wipe out the last O'Driscolls at Hanging Dog Ranch. Tom, the last of them, carries a letter from Colm.",
          "Arthur et Sadie éliminent les derniers O'Driscoll à Hanging Dog Ranch. Tom, le dernier d'entre eux, a sur lui une lettre de Colm."),
        M("Red Dead Redemption", C6,
          "In one ending, Arthur names Colm among those who were not the informant.",
          "Dans l'une des fins, Arthur cite Colm parmi ceux qui n'étaient pas le mouchard."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken or written in the game, in the original English. Colm's spoken lines come from \"Blessed are the Peacemakers\" and are checked against the Red Dead Wiki's transcript of the mission; the wiki has no transcript of \"Goodbye, Dear Friend\". His other lines from that mission are quoted under Personality, in \"In his own words\". The last two come from the letter he writes to Tom from prison.",
              "Les répliques ci-dessous sont citées telles qu'elles sont prononcées ou écrites dans le jeu, en anglais. Les paroles de Colm proviennent de \"Blessed are the Peacemakers\" et sont vérifiées sur la transcription de la mission publiée par le Red Dead Wiki ; le wiki ne propose pas de transcription de \"Goodbye, Dear Friend\". Ses autres répliques de cette mission figurent dans la rubrique Personnalité, sous \"Dans ses propres mots\". Les deux dernières citations sont tirées de la lettre qu'il écrit à Tom depuis sa prison.")},
    {"quotes": [
        {"q": two("Lot of heat on us this time. Both of us. Whole heap of trouble.", "Lot of heat on us this time. Both of us. Whole heap of trouble."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), to Dutch at the parley, just before telling him that he has been offered a price to bring him in",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), à Dutch lors des pourparlers, juste avant de lui apprendre qu'on lui a proposé une somme pour le livrer. Traduction : « Ça chauffe pour nous, cette fois. Pour nous deux. Un sacré paquet d'ennuis. »")},
        {"q": two("Oh, I know you would... but see... we lure an angry Dutch in to rescue ya... grab all of ya and hand ya in... then disappear.", "Oh, I know you would... but see... we lure an angry Dutch in to rescue ya... grab all of ya and hand ya in... then disappear."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), to Arthur at Lone Mule Stead, after Arthur advises him to run as soon as he has the money",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), à Arthur, à Lone Mule Stead, après qu'Arthur lui a conseillé de filer dès qu'il aurait l'argent. Traduction : « Oh, je sais que toi, tu le ferais... mais vois-tu... on attire un Dutch furieux qui viendra te délivrer... on vous attrape tous, on vous livre... et on disparaît. »")},
        {"q": two("The day of my execution draws near and I somewhat look forward to it.", "The day of my execution draws near and I somewhat look forward to it."),
         "src": two("Letter to Tom from Colm, written in his cell in Saint Denis (RDR2, chapter 6)",
                    "Lettre de Colm à Tom, écrite dans sa cellule de Saint-Denis (RDR2, chapitre 6). Traduction : « Le jour de mon exécution approche et je l'attends avec une certaine impatience. »")},
        {"q": two("I will see you in this world or the next.", "I will see you in this world or the next."),
         "src": two("Letter to Tom from Colm, closing line",
                    "Lettre de Colm à Tom, dernière ligne. Traduction : « Je te reverrai dans ce monde ou dans l'autre. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("Several of Colm's cutscenes take place away from the player character: Arthur sees his camp in \"Old Friends\" through binoculars and follows the parley through his rifle sights.",
            "Plusieurs cinématiques de Colm se déroulent loin du personnage du joueur : Arthur découvre son camp à la jumelle dans \"Old Friends\" et suit les pourparlers à travers la lunette de son fusil."),
        two("The subtitles of \"Blessed are the Peacemakers\" spell Annabelle's name \"Annabel\".",
            "Les sous-titres de \"Blessed are the Peacemakers\" écrivent le prénom d'Annabelle \"Annabel\"."),
        two("In \"Horsemen, Apocalypses\", one of the attacking O'Driscolls can be heard taunting Arthur by asking about his shoulder.",
            "Dans \"Horsemen, Apocalypses\", on peut entendre l'un des O'Driscoll qui attaquent le camp narguer Arthur en lui demandant des nouvelles de son épaule."),
        two("The article \"O'Driscoll Captured\" runs in three newspapers: Blackwater Ledger No. 69, New Hanover Gazette No. 34 and Saint Denis Times No. 50.",
            "L'article \"O'Driscoll Captured\" paraît dans trois journaux : le Blackwater Ledger n° 69, la New Hanover Gazette n° 34 et le Saint Denis Times n° 50."),
        two("\"Goodbye, Dear Friend\" fails if the player shoots Colm. One of its gold medal objectives is to find Colm's backup within 45 seconds.",
            "\"Goodbye, Dear Friend\" échoue si le joueur tire sur Colm. L'un des objectifs de la médaille d'or consiste à repérer les renforts de Colm en moins de 45 secondes."),
        two("Completing \"Goodbye, Dear Friend\" unlocks the bronze trophy and achievement \"Third Time Lucky\".",
            "Terminer \"Goodbye, Dear Friend\" débloque le trophée et succès de bronze \"Third Time Lucky\"."),
        two("Colm's letter to Tom can only be looted from Tom's body in part II of \"Mrs. Sadie Adler, Widow\", which is played only if Arthur agrees to help Sadie.",
            "La lettre de Colm à Tom ne se récupère que sur le corps de Tom, dans la deuxième partie de \"Mrs. Sadie Adler, Widow\", qui n'est jouée que si Arthur accepte d'aider Sadie."),
        two("Colm is one of only four characters in Red Dead Redemption 2 given a recurring musical theme of their own, with [[sadie-adler|Sadie Adler]], [[john-marston|John Marston]] and [[angelo-bronte|Angelo Bronte]].",
            "Colm est l'un des quatre seuls personnages de Red Dead Redemption 2 dotés d'un thème musical récurrent, avec [[sadie-adler|Sadie Adler]], [[john-marston|John Marston]] et [[angelo-bronte|Angelo Bronte]]."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Red Dead Online", "Red Dead Online")},
    {"p": two("Colm's character page on the Red Dead Wiki lists no appearance in Red Dead Online, but his gang survives him there as one of the hostile gangs of the online mode. Colter and Millesani Claim are among their hideouts that players can clear. O'Driscolls also attack players in random encounters and stranger missions, and when they deliver Trader goods. In a recovery mission, the Strawberry station clerk Hector Barlow asks the player to take back a stagecoach from the O'Driscolls at Hanging Dog Ranch without harming them, calling them good friends of his.",
              "La fiche de Colm sur le Red Dead Wiki ne mentionne aucune apparition dans Red Dead Online, mais sa bande lui survit dans ce mode, où elle compte parmi les gangs hostiles. Colter et Millesani Claim font partie des repaires O'Driscoll que les joueurs peuvent nettoyer. Les O'Driscoll s'en prennent aussi aux joueurs lors de rencontres aléatoires et de missions d'inconnus, ainsi qu'au moment des livraisons de Négociant. Dans une mission de récupération, Hector Barlow, employé de la gare de Strawberry, demande au joueur de reprendre une diligence aux O'Driscoll de Hanging Dog Ranch sans leur faire de mal, en les présentant comme de bons amis.")},
]
