"""Alberto Fussar, part C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (fetched Oct 2026; wiki pages cached in scripts/v3/work/_m/, other material in scripts/v3/work/fussar/fc/):
- Red Dead Wiki EN "Alberto Fussar" (en.txt): Mission appearances ("The Gilded Cage", "A Kind and Benevolent Despot",
  "Paradise Mercifully Departed"), Quotes, Trivia, quote boxes. Red Dead Wiki FR "Alberto Fussar" (fr.txt): Anecdote
  (he cannot be spoken to at the party and is only there while Dutch and Arthur are with Bronte).
- Mission pages: "The Gilded Cage" (chapter 4), "Welcome to the New World", "Savagery Unleashed" (via the wiki page
  "Guarma"), "A Kind and Benevolent Despot" (trivia: firing on Fussar or his soldiers fails the mission), "Hell Hath No
  Fury", "Paradise Mercifully Departed" (Gold Medal objectives and tips; trivia: the standoff recurs in "American
  Venom"). Chapter numbers from the infoboxes (all Guarma missions = chapter 5).
- TRANSCRIPT: "Red Dead Redemption 2 Full Transcript", Game Scripts Wiki (game-scripts-wiki.blogspot.com), fan
  transcript, scripts/v3/work/fussar/fc/gsw.txt (not committed). Every quote below is checked word for word against it
  (curly apostrophes and ellipsis characters normalized to straight apostrophes and "..."). The wiki has no
  "/dialogues" page for these missions.
- Wiki pages "Aguasdulces" (Fussar's estate), "Newspapers" / "Mayor's Gala Was Grand" (Blackwater Ledger No. 67 issue
  list; the gala article's guest list), "Guarma" (trivia: Red Dead Online flag), "Arthur Morgan" kill list (via arthur_E:
  Fussar among the three named deaths the story imposes on Arthur).

OWNERSHIP: narrative events are told in part A (one line per mission here). Fussar's own lines (Javier's interrogation,
the speech on striking workers, "cowards are the worst traitors", "You maggots are going to die", "The US Navy is on the
way") are left to part B "In his own words"; the quotes below are lines spoken ABOUT him, as in leviticus_C. Part A
paraphrases every line quoted here. The kill by gunshot instead of the cannon is in part B Weapons (not repeated in Trivia).
Fix pass (22 Oct 2026): Bronte, Simon, Leon, Hercule ("more money") and Micah quotes dropped (quoted in part B,
FIX_RULES 3); added Hercule's "desperate to find you" and "behind Colonel Fussar's back" and the tower exchange
(transcript, Welcome to the New World / Paradise Mercifully Departed). Trivia: estate item dropped (in B); standoff item
kept for the "American Venom" repeat only.

EXCLUDED
- Wiki trivia comparing Fussar with Agustin Allende (interpretation; also dropped in allende_C).
- Wiki trivia that Guarma is "even worse" after his death (the 1907 article makes no comparison).
- The wiki quote list's label "last words" for "You maggots are going to die. The US Navy is on the way.": he speaks again
  only through gunfire afterwards, but the lines belong to part B in any case.
DEDUPE WATCH (for the fixer): Leon's "A tyrant..." and Micah's "I like the man's style..." are wiki quote boxes and may
  also be picked by part B (Personality); if so, cut them here.
- Any Red Dead Online presence of Fussar himself: none found (Guarma is inaccessible online; only a flag).
- Marketing: no pre-release material, trailer or Rockstar description naming Fussar was found (THR descriptions of
  6 Sep 2018 cover the gang only).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The Red Dead Wiki lists three missions of Red Dead Redemption 2 in which Fussar appears: one in chapter 4 and two in chapter 5. He speaks only in the two Guarma missions. Three other Guarma missions are driven by his regime without showing him; they are listed in the second table.",
              "Le Red Dead Wiki recense trois missions de Red Dead Redemption 2 où apparaît Fussar : une au chapitre 4 et deux au chapitre 5. Il ne parle que dans les deux missions de Guarma. Trois autres missions de Guarma tournent autour de son régime sans le montrer ; elles figurent dans le second tableau.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Fussar's role", "Rôle de Fussar")], "rows": [
        M("The Gilded Cage", C4,
          "A guest at Mayor Lemieux's party in Saint Denis. [[angelo-bronte|Bronte]] points him out to [[dutch-van-der-linde|Dutch]] and [[arthur-morgan|Arthur]] from a balcony.",
          "Invité à la réception du maire Lemieux à Saint-Denis. Depuis un balcon, [[angelo-bronte|Bronte]] le désigne à [[dutch-van-der-linde|Dutch]] et à [[arthur-morgan|Arthur]]."),
        M("A Kind and Benevolent Despot", C5,
          "Mocks the captured [[javier-escuella|Javier]] in Aguasdulces, then harangues his soldiers while Dutch and Arthur slip into his refinery, which they blow up to free Javier.",
          "Se moque de [[javier-escuella|Javier]], prisonnier, à Aguasdulces, puis harangue ses soldats pendant que Dutch et Arthur s'introduisent dans sa raffinerie, qu'ils font sauter pour libérer Javier."),
        M("Paradise Mercifully Departed", C5,
          "Joins the standoff in the cabin where the ship's captain is held, escapes after Levi Simon is shot, then fires on the gang from a tower; Arthur kills him.",
          "Se joint au face-à-face dans la cabane où est retenu le capitaine du navire, s'enfuit après la mort de Levi Simon, puis tire sur la bande depuis une tour ; Arthur le tue."),
    ]}},
    {"h4": two("Missions shaped by his regime", "Missions marquées par son régime")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Fussar", "Lien avec Fussar")], "rows": [
        M("Welcome to the New World", C5,
          "His overseer, Levi Simon, has the castaways chained; [[hercule-fontaine|Hercule Fontaine]] and Leon Fuentes describe his rule over Guarma.",
          "Son contremaître, Levi Simon, fait enchaîner les naufragés ; [[hercule-fontaine|Hercule Fontaine]] et Leon Fuentes décrivent son emprise sur Guarma."),
        M("Savagery Unleashed", C5,
          "Arthur and Leon Fuentes save plantation workers whom the island's soldiers are hanging.",
          "Arthur et Leon Fuentes sauvent des ouvriers de la plantation que les soldats de l'île sont en train de pendre."),
        M("Hell Hath No Fury", C5,
          "The warship he called in from Cuba attacks Cinco Torres; Arthur sinks it with the fort's cannon.",
          "Le navire de guerre qu'il a fait venir de Cuba attaque Cinco Torres ; Arthur le coule avec le canon du fort."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are spoken about Fussar by other characters. They are given in the original English and checked against a fan transcript of the game. Fussar's own lines are under Personality.",
              "Les répliques ci-dessous sont prononcées au sujet de Fussar par d'autres personnages. Elles sont citées dans leur version originale anglaise et vérifiées sur une transcription du jeu réalisée par des fans. Les paroles de Fussar lui-même figurent dans la rubrique Personnalité.")},
    {"quotes": [
        {"q": two("Okay. Well, Fussar will be desperate to find you. We must be very careful.",
                  "Okay. Well, Fussar will be desperate to find you. We must be very careful."),
         "src": two("Hercule Fontaine to Dutch, after the ambush, Welcome to the New World (RDR2, chapter 5)",
                    "Hercule Fontaine à Dutch, après l'embuscade, Welcome to the New World (RDR2, chapitre 5). Traduction : « Bon. Fussar va vous chercher partout. Il faut être très prudents. »")},
        {"q": two("I am not from here. I bring things in and off the islands... behind Colonel Fussar's back.",
                  "I am not from here. I bring things in and off the islands... behind Colonel Fussar's back."),
         "src": two("Hercule Fontaine, when Dutch asks about him, Welcome to the New World (RDR2, chapter 5)",
                    "Hercule Fontaine, quand Dutch l'interroge sur lui-même, Welcome to the New World (RDR2, chapitre 5). Traduction : « Je ne suis pas d'ici. Je fais entrer et sortir des marchandises des îles... dans le dos du colonel Fussar. »")},
        {"q": two("You know, wasn't Fussar one of the fellers Bronte pointed out to us at the party in Saint Denis?",
                  "You know, wasn't Fussar one of the fellers Bronte pointed out to us at the party in Saint Denis?"),
         "src": two("Arthur to Dutch in the caves, A Kind and Benevolent Despot (RDR2, chapter 5)",
                    "Arthur à Dutch dans les grottes, A Kind and Benevolent Despot (RDR2, chapitre 5). Traduction : « Dis donc, Fussar, ce ne serait pas un des types que Bronte nous a montrés à la réception de Saint-Denis ? »")},
        {"q": two("Very kind of you, Mr. Fussar!", "Very kind of you, Mr. Fussar!"),
         "src": two("Dutch, as the warship's fire hits its own soldiers, Hell Hath No Fury (RDR2, chapter 5)",
                    "Dutch, quand les tirs du navire de guerre frappent ses propres soldats, Hell Hath No Fury (RDR2, chapitre 5). Traduction : « Bien aimable à vous, monsieur Fussar ! »")},
        {"q": two("This feller is really beginning to try my patience. / And he ain't even had you tortured yet.",
                  "This feller is really beginning to try my patience. / And he ain't even had you tortured yet."),
         "src": two("Dutch, then Arthur, after Micah's report on the captain and the gun positions, Paradise Mercifully Departed (RDR2, chapter 5)",
                    "Dutch, puis Arthur, après le rapport de Micah sur le capitaine et les pièces d'artillerie, Paradise Mercifully Departed (RDR2, chapitre 5). Traduction : « Ce type commence vraiment à mettre ma patience à l'épreuve. / Et il ne t'a même pas encore fait torturer. »")},
        {"q": two("Oh, I'll fight Alberto Fussar every day I can.", "Oh, I'll fight Alberto Fussar every day I can."),
         "src": two("Hercule Fontaine, when Dutch asks if he is in, Paradise Mercifully Departed (RDR2, chapter 5)",
                    "Hercule Fontaine, quand Dutch lui demande s'il en est, Paradise Mercifully Departed (RDR2, chapitre 5). Traduction : « Oh, je combattrai Alberto Fussar chaque jour que je pourrai. »")},
        {"q": two("Fussar is up there I think. / In the tower? / Yes. Yes, that's him.",
                  "Fussar is up there I think. / In the tower? / Yes. Yes, that's him."),
         "src": two("Hercule Fontaine, then Arthur, then Hercule, near the harbor, Paradise Mercifully Departed (RDR2, chapter 5)",
                    "Hercule Fontaine, puis Arthur, puis Hercule, près du port, Paradise Mercifully Departed (RDR2, chapitre 5). Traduction : « Fussar est là-haut, je crois. / Dans la tour ? / Oui. Oui, c'est lui. »")},
        {"q": two("I got him for you, Javier.", "I got him for you, Javier."),
         "src": two("Arthur, after destroying Fussar's tower, Paradise Mercifully Departed (RDR2, chapter 5)",
                    "Arthur, après avoir détruit la tour de Fussar, Paradise Mercifully Departed (RDR2, chapitre 5). Traduction : « Je l'ai eu pour toi, Javier. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("According to the French edition of the Red Dead Wiki, the player cannot talk to Fussar during the party in \"The Gilded Cage\", and he is only present while Dutch and Arthur are with Bronte on the balcony.",
            "Selon l'édition française du Red Dead Wiki, le joueur ne peut pas parler à Fussar pendant la réception de \"The Gilded Cage\", et celui-ci n'est présent que tant que Dutch et Arthur se trouvent avec Bronte sur le balcon."),
        two("The newspaper article on the mayor's party, \"Mayor's Gala Was Grand\" (Blackwater Ledger No. 67), lists Archibald Jameson, Major Hobart Crawley, Gilbert Knightly, Hector Fellowes and Angelo Bronte among the guests, but does not name Fussar. The same issue carries \"Guarma Island Sugar Boom\".",
            "L'article consacré à la réception du maire, \"Mayor's Gala Was Grand\" (Blackwater Ledger n° 67), cite parmi les invités Archibald Jameson, le major Hobart Crawley, Gilbert Knightly, Hector Fellowes et Angelo Bronte, mais pas Fussar. Le même numéro publie \"Guarma Island Sugar Boom\"."),
        two("In \"A Kind and Benevolent Despot\", opening fire on Fussar or his soldiers once Javier has been seen fails the mission, and a cutscene shows the guards killing Javier.",
            "Dans \"A Kind and Benevolent Despot\", ouvrir le feu sur Fussar ou sur ses soldats une fois que Javier est en vue fait échouer la mission, et une cinématique montre les gardes en train de tuer Javier."),
        two("Firing the cannon at Fussar's tower stops the clock on one of the Gold Medal objectives of \"Paradise Mercifully Departed\": escorting the captain to the boat within 1 minute and 45 seconds.",
            "Le tir de canon sur la tour de Fussar arrête le chronomètre de l'un des objectifs de la médaille d'or de \"Paradise Mercifully Departed\" : escorter le capitaine jusqu'au bateau en moins d'une minute et 45 secondes."),
        two("According to the Red Dead Wiki, the double-revolver standoff in the cabin happens again in \"American Venom\", the last mission of the 1907 epilogue.",
            "Selon le Red Dead Wiki, le face-à-face de la cabane, où Dutch tient un revolver dans chaque main, se reproduit dans \"American Venom\", la dernière mission de l'épilogue de 1907."),
        two("The Red Dead Wiki's list of the people Arthur kills counts three named deaths that the story imposes on him: Sheriff Leigh Gray, Alberto Fussar and Colonel Henry Favours.",
            "La liste des personnes tuées par Arthur sur le Red Dead Wiki compte trois morts nommées que l'histoire lui impose : le shérif Leigh Gray, Alberto Fussar et le colonel Henry Favours."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("Fussar appears only in Red Dead Redemption 2. He has no role in Red Dead Online, where Guarma cannot be visited. According to the Red Dead Wiki, a flag bearing the island's coat of arms can be unlocked there as a camp flag at rank 59 of the third Outlaw Pass.",
              "Fussar n'apparaît que dans Red Dead Redemption 2. Il ne joue aucun rôle dans Red Dead Online, où Guarma n'est pas accessible. D'après le Red Dead Wiki, un drapeau aux armes de l'île peut y être débloqué comme drapeau de camp au rang 59 du troisième Outlaw Pass.")},
]
