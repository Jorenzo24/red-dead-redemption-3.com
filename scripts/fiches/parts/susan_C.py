"""Susan Grimshaw, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/susan/ and cov/susan/m/):
- Red Dead Wiki EN "Susan Grimshaw" (Mission Appearances: 13 missions; Murders Committed; Quotes; Trivia; Gallery
  captions) and FR "Susan Grimshaw" (fr.txt: same 13 missions).
- Transcripts "/dialogues": Outlaws from the West; Enter, Pursued by a Memory (no line for her); Eastward Bound;
  Polite Society, Valentine Style; Exit, Pursued by a Bruised Ego (EPBE_dlg.txt); Who is Not Without Sin; Blessed are
  the Peacemakers; The Battle of Shady Belle; Red Dead Redemption (mission). Every quote from these missions is
  checked word for word against them.
- Missions without a transcript on the wiki: No, No and Thrice, No (mission page: QuoteTalk box, story, gold medal,
  failure conditions, notes, deaths); Horsemen, Apocalypses; Fleeting Joy; A Strange Kindness; Blood Feuds, Ancient and
  Modern; That's Murfree Country; We Loved Once and True I (fetched). The four No, No and Thrice, No lines come from
  the mission page's quote box and the character page's quote list, and are labeled as such.
- Camp Events (availability note: Tilly, Mary-Beth and Grimshaw away once "No, No and Thrice, No" is unlocked).
- Real world: Rockstar tweet "Susan Grimshaw" of September 6, 2018, reproduced by The Hollywood Reporter on
  September 7, 2018 (../uncle/fc/thr_descriptions.txt; description NOT quoted here, part B); composite of the 23 gang
  members (Wikipedia caption, m/wp_list.txt: front row "... Sean, Tilly, Grimshaw, Sadie ..."); SacAnime Summer 2019
  cast panel, June 8, 2019 (Convention Coverage YouTube video ifohZGPVBMQ, auto captions saved as
  ../javier/fc/yt_ifohZGPVBMQ.txt, 25:22 to 25:33, speaker identifies as Pearson: Jim Santangeli).
Ownership (FIX_RULES), left to other parts: mission narrative (A); camp lines "My camp, my rules.", "Of course I
care. About all of you fools...", "I don't care what you feel, girl. Get ready!", "rot in your own filth" and
all camp scenes, names ("Miss Grimshaw", addressed by surname), weapons and her preference for shotguns, appearance,
the Rockstar description and official guide wording (B); Kaili Vernoff, cut content (unused corset and earrings,
the cut Eliza and Karen encounters), reception (D). Burial, grave and the Paying Respects trophy are told in A, so
the wiki's "grave only John can visit" trivia is not repeated here.
Kills: the character page lists two murders (an unnamed Foreman Brother at Radley's House, Molly O'Shea). The
mission page adds that Susan kills the guard with a knife and may shoot one of the fleeing riders.
Excluded: "physically abusive towards the other young women" (the wiki's own "reasonable to assume": speculation);
"Dutch shows no care ... showing how far he had descended into madness" (interpretation); Tilly's dominoes line read
as foreshadowing Molly's death (interpretation; the scene is B's); "Susan knickers after patch 1.20" (gallery caption,
no value); Jim Santangeli's "favorite character" wording of the wiki (the panel transcript has him say he does not
know how anyone could not love her, which is quoted instead); Red Dead Online: no appearance of Susan found on the
wiki, nothing is claimed.
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

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English and French editions of the Red Dead Wiki both list 13 story missions of Red Dead Redemption 2 for Susan, from the flight to Colter to the last mission of chapter 6. She gives one of them, \"No, No and Thrice, No\", jointly with Mary-Beth Gaskill according to its mission page. Four missions on the list do not show her in their mission page or transcript; the table says so case by case. A second table adds three missions in which she is only mentioned or plays a brief part in camp.",
              "Les éditions anglaise et française du Red Dead Wiki recensent toutes deux 13 missions principales de Red Dead Redemption 2 pour Susan, de la fuite vers Colter à la dernière mission du chapitre 6. Elle en confie une, \"No, No and Thrice, No\", conjointement avec Mary-Beth Gaskill d'après la page de la mission. Quatre missions de la liste ne la montrent ni dans leur page ni dans leur transcription : le tableau le signale au cas par cas. Un second tableau ajoute trois missions où elle est seulement citée ou ne fait qu'une brève apparition au camp.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 to 6", "Red Dead Redemption 2, chapitres 1 à 6")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Susan's role", "Rôle de Susan")], "rows": [
        M("Outlaws from the West", C1,
          "Puts Mary-Beth, Karen and [[simon-pearson|Pearson]] to work in the Colter cabin, then assigns the sleeping quarters, which sets off [[micah-bell|Micah]]'s complaint.",
          "Met Mary-Beth, Karen et [[simon-pearson|Pearson]] au travail dans la cabane de Colter, puis répartit les couchages, ce qui déclenche les protestations de [[micah-bell|Micah]]."),
        M("Enter, Pursued by a Memory", C1,
          "Listed by the wiki. The transcript gives her no line.",
          "Citée par le wiki. La transcription ne lui prête aucune réplique."),
        M("Eastward Bound", C1,
          "Hurries the packing at Colter, then shows [[arthur-morgan|Arthur]] his tent at Horseshoe Overlook and scolds [[tilly-jackson|Tilly]].",
          "Presse le chargement à Colter, puis montre sa tente à [[arthur-morgan|Arthur]] à Horseshoe Overlook et rabroue [[tilly-jackson|Tilly]]."),
        M("Who is Not Without Sin", C2,
          "Takes charge of [[orville-swanson|Swanson]] when Arthur brings him back drunk.",
          "Prend en charge [[orville-swanson|Swanson]] quand Arthur le ramène ivre."),
        M("A Strange Kindness", C2,
          "Listed by the wiki. The mission page does not name her, and the wiki has no transcript.",
          "Citée par le wiki. La page de la mission ne la nomme pas, et le wiki n'en a pas la transcription."),
        M("Blessed are the Peacemakers", C3,
          "Called by [[dutch-van-der-linde|Dutch]] when Arthur returns wounded; sits with him.",
          "Appelée par [[dutch-van-der-linde|Dutch]] quand Arthur rentre blessé ; reste à son chevet."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Listed by the wiki. The mission page does not name her, and the wiki has no transcript.",
          "Citée par le wiki. La page de la mission ne la nomme pas, et le wiki n'en a pas la transcription."),
        M("The Battle of Shady Belle", C3,
          "Tells Dutch that [[andrew-milton|Milton]] should leave; at Shady Belle, Dutch asks her and Pearson to set up the camp.",
          "Fait savoir à Dutch que [[andrew-milton|Milton]] doit partir ; à Shady Belle, Dutch lui confie l'installation du camp avec Pearson."),
        M("No, No and Thrice, No", C4,
          "Mission giver with Mary-Beth. Rides with Arthur to Radley's House to free Tilly from the Foreman Brothers and kills the guard.",
          "Donneuse de la mission avec Mary-Beth. Accompagne Arthur à Radley's House pour libérer Tilly des Foreman Brothers et tue le garde."),
        M("Horsemen, Apocalypses", C4,
          "Takes cover in the house during the O'Driscoll attack on Shady Belle.",
          "Se met à l'abri dans la maison pendant l'attaque des O'Driscoll contre Shady Belle."),
        M("Fleeting Joy", C5,
          "Listed by the wiki for the reunion and the Pinkerton attack at Lakay. The mission page does not name her.",
          "Citée par le wiki pour les retrouvailles et l'attaque de la Pinkerton à Lakay. La page de la mission ne la nomme pas."),
        M("That's Murfree Country", C5,
          "Shoots [[molly-oshea|Molly O'Shea]] at Beaver Hollow and has the body burned.",
          "Abat [[molly-oshea|Molly O'Shea]] à Beaver Hollow et fait brûler le corps."),
        M("Red Dead Redemption", C6,
          "Sides with Arthur and John and turns her shotgun on Micah, who shoots her dead.",
          "Se range du côté d'Arthur et de John et braque son fusil sur Micah, qui l'abat."),
    ]}},
    {"h4": two("Other missions", "Autres missions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Susan's role", "Rôle de Susan")], "rows": [
        M("Polite Society, Valentine Style", C2,
          "Mentioned only: Mary-Beth says Karen is ready to murder her, and Arthur asks if she can spare the girls.",
          "Seulement citée : Mary-Beth dit que Karen est prête à l'assassiner, et Arthur demande si elle peut se passer des filles."),
        M("Exit, Pursued by a Bruised Ego", C2,
          "Mentioned only: Arthur tells Hosea that she sent Micah and Lenny scouting.",
          "Seulement citée : Arthur explique à Hosea qu'elle a envoyé Micah et Lenny en reconnaissance."),
        M("We Loved Once and True I", C2,
          "Tells Arthur in camp that a letter from [[mary-linton|Mary Linton]] has arrived.",
          "Annonce à Arthur, au camp, qu'une lettre de [[mary-linton|Mary Linton]] est arrivée."),
    ]}},
    {"h3": two("Notable people Susan kills", "Personnages notables tués par Susan")},
    {"p": two("The Red Dead Wiki lists two killings for Susan: an unnamed member of the Foreman Brothers and Molly O'Shea. The mission page of \"No, No and Thrice, No\" specifies how the first one dies and adds that she can kill one of the riders during the chase.",
              "Le Red Dead Wiki attribue deux meurtres à Susan : un membre anonyme des Foreman Brothers et Molly O'Shea. La page de la mission \"No, No and Thrice, No\" précise les circonstances du premier et ajoute qu'elle peut abattre l'un des cavaliers pendant la poursuite.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K(two("Foreman Brothers guard", "Garde des Foreman Brothers"), "No, No and Thrice, No",
          "Stabbed by Susan outside Radley's House after she engages him in conversation.",
          "Poignardé par Susan devant Radley's House, après qu'elle a engagé la conversation."),
        K(two("Foreman Brothers rider", "Cavalier des Foreman Brothers"), "No, No and Thrice, No",
          "Determinant. One of the two men fleeing with Anthony Foreman is shot by Susan if Arthur is too slow to kill both, which fails a gold medal objective.",
          "Selon le joueur. L'un des deux hommes qui fuient avec Anthony Foreman est abattu par Susan si Arthur tarde à les tuer tous les deux, ce qui fait échouer un objectif de la médaille d'or."),
        K(two("[[molly-oshea|Molly O'Shea]]", "[[molly-oshea|Molly O'Shea]]"), "That's Murfree Country",
          "Shot in the stomach with a shotgun at Beaver Hollow, after claiming she informed the Pinkertons.",
          "Tuée d'un coup de fusil au ventre à Beaver Hollow, après avoir affirmé avoir renseigné la Pinkerton."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Lines from missions with a transcript on the Red Dead Wiki are checked against it; the four lines about the Foreman Brothers in chapter 4, whose mission has no transcript, come from the quote box of the \"No, No and Thrice, No\" page and from the wiki's quote list. Lines spoken in camp outside missions are quoted under Personality and Relationships and are not repeated here.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Celles des missions dont le Red Dead Wiki publie la transcription y sont vérifiées ; les quatre répliques visant les Foreman Brothers au chapitre 4, dont la mission n'a pas de transcription, proviennent de l'encadré de citation de la page \"No, No and Thrice, No\" et de la liste de citations du wiki. Les répliques prononcées au camp hors des missions figurent dans les rubriques Personnalité et Relations et ne sont pas reprises ici.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 to 3", "Red Dead Redemption 2, chapitres 1 à 3")},
    {"quotes": [
        {"q": two("Miss Gaskill... get that fire lit quick. Miss Jones, bring in whatever blankets we have. Mr. Pearson, see what we've got in terms of food.", "Miss Gaskill... get that fire lit quick. Miss Jones, bring in whatever blankets we have. Mr. Pearson, see what we've got in terms of food."),
         "src": two("Outlaws from the West (RDR2, chapter 1), in the Colter cabin, to Mary-Beth, Karen and Pearson",
                    "Outlaws from the West (RDR2, chapitre 1), dans la cabane de Colter, à Mary-Beth, Karen et Pearson. Traduction : « Mademoiselle Gaskill... allumez-moi ce feu, et vite. Mademoiselle Jones, apportez toutes les couvertures qu'on a. Monsieur Pearson, voyez ce qu'il nous reste à manger. »")},
        {"q": two("Mr. Bell, you're with the fellers over there.", "Mr. Bell, you're with the fellers over there."),
         "src": two("Outlaws from the West (RDR2, chapter 1), to Micah, while handing out the cabins",
                    "Outlaws from the West (RDR2, chapitre 1), à Micah, pendant la répartition des cabanes. Traduction : « Monsieur Bell, vous êtes avec les gars, là-bas. »")},
        {"q": two("Oh, for Lord's sake. Put that book away and go help. Oh... Mary-Beth.", "Oh, for Lord's sake. Put that book away and go help. Oh... Mary-Beth."),
         "src": two("Eastward Bound (RDR2, chapter 1), to Mary-Beth, as the wagons are loaded in Colter",
                    "Eastward Bound (RDR2, chapitre 1), à Mary-Beth, pendant le chargement des chariots à Colter. Traduction : « Oh, pour l'amour du ciel. Rangez-moi ce livre et allez aider. Oh... Mary-Beth. »")},
        {"q": two("It should be, most of your stuff from Blackwater got saved.", "It should be, most of your stuff from Blackwater got saved."),
         "src": two("Eastward Bound (RDR2, chapter 1), to Arthur, who says he is sure everything will be fine with his tent",
                    "Eastward Bound (RDR2, chapitre 1), à Arthur, qui se dit sûr que tout ira bien pour sa tente. Traduction : « Ça devrait, la plupart de vos affaires de Blackwater ont été sauvées. »")},
        {"q": two("Miss Jackson... I've seen shit with more common sense than you. Do it properly.", "Miss Jackson... I've seen shit with more common sense than you. Do it properly."),
         "src": two("Eastward Bound (RDR2, chapter 1), to Tilly, about her work at Horseshoe Overlook",
                    "Eastward Bound (RDR2, chapitre 1), à Tilly, à propos de son travail à Horseshoe Overlook. Traduction : « Mademoiselle Jackson... j'ai vu de la merde avec plus de bon sens que vous. Faites-le correctement. »")},
        {"q": two("Well, thank you, Mr. Morgan. I'll keep an eye on him.", "Well, thank you, Mr. Morgan. I'll keep an eye on him."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), to Arthur, after he brings Swanson back to camp",
                    "Who is Not Without Sin (RDR2, chapitre 2), à Arthur, qui vient de ramener Swanson au camp. Traduction : « Eh bien, merci, monsieur Morgan. Je garderai un œil sur lui. »")},
        {"q": two("Of course. You'll be okay, Mr. Morgan... you're home.", "Of course. You'll be okay, Mr. Morgan... you're home."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), when Dutch asks her to sit with the wounded Arthur",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), quand Dutch lui demande de veiller Arthur, blessé. Traduction : « Bien sûr. Ça va aller, monsieur Morgan... vous êtes chez vous. »")},
        {"q": two("I think your new friend should leave now, Dutch.", "I think your new friend should leave now, Dutch."),
         "src": two("The Battle of Shady Belle (RDR2, chapter 3), about Agent Milton, at Clemens Point",
                    "The Battle of Shady Belle (RDR2, chapitre 3), à propos de l'agent Milton, à Clemens Point. Traduction : « Je crois que ton nouvel ami devrait s'en aller, Dutch. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, chapter 4: the Foreman Brothers", "Red Dead Redemption 2, chapitre 4 : les Foreman Brothers")},
    {"quotes": [
        {"q": two("If they've touched a single hair on that girl's head, I will eviscerate the sons of bitches.", "If they've touched a single hair on that girl's head, I will eviscerate the sons of bitches."),
         "src": two("About the Foreman Brothers, who have kidnapped Tilly (Red Dead Wiki quote list)",
                    "À propos des Foreman Brothers, qui ont enlevé Tilly (liste de citations du Red Dead Wiki). Traduction : « S'ils ont touché à un seul cheveu de cette petite, j'étripe ces fils de putes. »")},
        {"q": two("Well, I don't know what they've been doing here... but I can tell you what they're going to be doing here... dying.", "Well, I don't know what they've been doing here... but I can tell you what they're going to be doing here... dying."),
         "src": two("No, No and Thrice, No (RDR2, chapter 4), to Arthur, who asks what the Foreman Brothers are doing in the area (mission page)",
                    "No, No and Thrice, No (RDR2, chapitre 4), à Arthur, qui se demande ce que les Foreman Brothers font dans la région (page de la mission). Traduction : « Je ne sais pas ce qu'ils faisaient ici... mais je peux vous dire ce qu'ils vont y faire... mourir. »")},
        {"q": two("You've said your last words.", "You've said your last words."),
         "src": two("Cutting off a Foreman Brother, whom she then kills (Red Dead Wiki quote list)",
                    "En coupant la parole à un membre des Foreman Brothers, qu'elle tue ensuite (liste de citations du Red Dead Wiki). Traduction : « Vous venez de prononcer vos dernières paroles. »")},
        {"q": two("History is never done.", "History is never done."),
         "src": two("To Anthony Foreman (Red Dead Wiki quote list)",
                    "À Anthony Foreman (liste de citations du Red Dead Wiki). Traduction : « L'histoire n'est jamais finie. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, chapter 6", "Red Dead Redemption 2, chapitre 6")},
    {"quotes": [
        {"q": two("Well, we're doing our best.", "Well, we're doing our best."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), to Micah, who orders her to pack faster",
                    "Red Dead Redemption (RDR2, chapitre 6), à Micah, qui lui ordonne de remballer plus vite. Traduction : « Eh bien, on fait de notre mieux. »")},
        {"q": two("No. You be quiet, Mr. Bell... and put down your gun.", "No. You be quiet, Mr. Bell... and put down your gun."),
         "src": two("Red Dead Redemption (RDR2, chapter 6), her last words, aiming her shotgun at Micah during the standoff",
                    "Red Dead Redemption (RDR2, chapitre 6), ses derniers mots, en braquant son fusil sur Micah pendant l'affrontement. Traduction : « Non. C'est vous qui allez vous taire, monsieur Bell... et baisser votre arme. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("In \"No, No and Thrice, No\", Arthur chases Anthony Foreman on a leopard-coat Appaloosa commandeered at Radley's House, often the only horse nearby once the mission ends.",
            "Dans \"No, No and Thrice, No\", Arthur poursuit Anthony Foreman sur un Appaloosa à robe léopard réquisitionné à Radley's House, souvent le seul cheval à proximité à la fin de la mission."),
        two("The same mission fails if the player assaults, kills or abandons Susan.",
            "La même mission échoue si le joueur agresse, tue ou abandonne Susan."),
        two("After Micah shoots her in \"Red Dead Redemption\", her body can be looted for shotgun shells and a Miracle Tonic, at the cost of some honor. The Pinkerton attack makes her body hard to reach.",
            "Après que Micah l'a abattue dans \"Red Dead Redemption\", on peut fouiller son corps pour récupérer des cartouches de fusil et un Miracle Tonic, au prix d'une perte d'honneur. L'assaut de la Pinkerton rend son corps difficile à atteindre."),
        two("At a cast panel at SacAnime Summer 2019, on June 8, 2019, Jim Santangeli, who plays Pearson, was asked for his favorite character besides his own. He said: \"I don't know how you can't love Miss Grimshaw.\" He added that as Pearson he felt she was his teammate in the camp.",
            "Lors d'une table ronde des acteurs au SacAnime Summer 2019, le 8 juin 2019, Jim Santangeli, l'interprète de Pearson, s'est vu demander son personnage préféré en dehors du sien. Il a répondu : \"I don't know how you can't love Miss Grimshaw.\" (\"Je ne vois pas comment on pourrait ne pas aimer Miss Grimshaw.\") Il a ajouté qu'en tant que Pearson, il la voyait comme sa coéquipière au camp."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("On September 6, 2018, Rockstar posted Susan Grimshaw's portrait and character description on Twitter, in a series covering the members of the gang, and The Hollywood Reporter reproduced the series the next day. Rockstar also released official artwork of her for Red Dead Redemption 2. In the composite image of the 23 gang members, she stands in the front row, between [[tilly-jackson|Tilly Jackson]] and [[sadie-adler|Sadie Adler]].",
              "Le 6 septembre 2018, Rockstar publie sur Twitter le portrait de Susan Grimshaw et sa description, dans une série consacrée aux membres du gang, et The Hollywood Reporter reprend la série le lendemain. Rockstar a aussi diffusé une illustration officielle du personnage pour Red Dead Redemption 2. Sur l'image qui réunit les 23 membres du gang, elle figure au premier rang, entre [[tilly-jackson|Tilly Jackson]] et [[sadie-adler|Sadie Adler]].")},
]
