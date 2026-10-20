"""Molly O'Shea, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/molly/ and cov/molly/m/):
- Red Dead Wiki EN "Molly O'Shea" (Mission Appearances, infobox quote box, Trivia) and FR "Molly O'Shea" (fr.txt:
  Apparitions dans les missions, same nine missions as the EN list minus "Who is Not Without Sin").
- Mission pages: Outlaws from the West; Eastward Bound; Polite Society, Valentine Style; A Quiet Time; Who is Not
  Without Sin; An Honest Mistake (infobox: giver Molly O'Shea/Uncle); Blessed are the Peacemakers; Blood Feuds, Ancient
  and Modern; The Battle of Shady Belle; Horsemen, Apocalypses (failure conditions); Banking, The Old American Art
  (trivia); That's Murfree Country (chapter 5, Deaths, trophy No Traitors); Red Dead Redemption (mission).
- Transcripts "/dialogues": Outlaws from the West (l. 558), Polite Society, Valentine Style (l. 221-223), Who is Not
  Without Sin (l. 303), Blessed are the Peacemakers (l. 5), The Battle of Shady Belle (l. 264-278), Red Dead Redemption
  (l. 173-175, 710, 764). Every quote below is checked word for word against them, except Molly's Beaver Hollow line,
  which comes from the quote box of her character page, which does not name its scene (no transcript of "That's Murfree Country" exists on the wiki,
  checked 20 Oct 2026; nor of "An Honest Mistake", whose lines are therefore not quoted).
- Real world: Rockstar's character portraits posted on Twitter on September 6, 2018 and reproduced by The Hollywood
  Reporter on September 7, 2018 (../uncle/fc/thr_descriptions.txt: entry "Molly O'Shea"; the description itself is NOT
  quoted here, part B owns it); Wikipedia "List of Red Dead Redemption 2 characters" (m/wp_list.txt: caption of the
  composite of the 23 gang members, front row, between Sadie and Mary-Beth).
Ownership (FIX_RULES), left to other parts: the scenes themselves (A); camp lines ("Dutch is all the company I need",
"I'm nobody's servant girl", "I need to be alone", "How is any of this okay?", dock rants, Abigail's advice, Sean's
"West Briton", Karen's "Dutch or no Dutch"), personality, names, appearance, the Constance Skirt, the poem and its
villanelle form, the mirror (B); Penny O'Brien, audition, interviews, concept art, and all cut content (the Gilded Cage
outfit, the unused grave, the unused riding lines) (D).
Kills: none; no kills table.
Excluded: the dominoes and mirror "foreshadowing" trivia (interpretation); the trivia reading her An Honest Mistake
questions as a sign that she noticed Dutch's decline or as a reference to her interrogation (speculation); her
"Lord God almighty" line as a quotation (no transcript); "Molly is the only female in the gang who never does chores"
(personality, part B).
Fact-check fixes (20 Oct 2026): "Dutch? Could I have a word with ya?" was spliced across Dutch's "Yes?" (Shady Belle
transcript l.264-268): only "Could I have a word with ya?" is quoted, the exchange given in the context; the low-honor
line is quoted in full and placed after Micah's stab and Dutch's arrival (transcript l.686-710); the quote-box line is
linked to the Beaver Hollow confrontation, which the character page paraphrases in the same words (attributed, no
transcript); "never rides out with Arthur" kept in Trivia only (reworded, it was copied from the wiki) and the
"Horsemen, Apocalypses" failure clause left to the Biography; Constance Skirt added (wiki trivia, attributed).
"I was wondering when he'd show up." is quoted here only (part B points to it).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists ten story missions of Red Dead Redemption 2 for Molly, from the arrival at Colter to her death at Beaver Hollow. The table below also includes the missions in which she is only talked about.",
              "Le Red Dead Wiki anglais recense pour Molly dix missions principales de Red Dead Redemption 2, de l'arrivée à Colter à sa mort à Beaver Hollow. Le tableau ci-dessous intègre aussi les missions où il n'est question que d'elle.")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Molly's role", "Rôle de Molly")], "rows": [
        M("Outlaws from the West", C1,
          "At camp. [[susan-grimshaw|Susan Grimshaw]] says that Molly will show [[dutch-van-der-linde|Dutch]] the way to his cabin.",
          "Au camp. [[susan-grimshaw|Susan Grimshaw]] annonce que Molly va conduire [[dutch-van-der-linde|Dutch]] jusqu'à sa cabane."),
        M("Eastward Bound", C1,
          "Listed by the Red Dead Wiki; the mission page, the move to Horseshoe Overlook, does not name her.",
          "Citée par le Red Dead Wiki ; la page de la mission, le départ pour Horseshoe Overlook, ne la nomme pas."),
        M("Polite Society, Valentine Style", C2,
          "Mentioned. On the road to Valentine, [[tilly-jackson|Tilly]] asks whether they should have brought her, and [[karen-jones|Karen]] mocks her.",
          "Mentionnée. Sur la route de Valentine, [[tilly-jackson|Tilly]] se demande s'il aurait fallu l'emmener, et [[karen-jones|Karen]] se moque d'elle."),
        M("A Quiet Time", C2,
          "At camp, according to the character page, when [[lenny-summers|Lenny]] reports [[micah-bell|Micah]]'s arrest in Strawberry.",
          "Au camp, d'après la page du personnage, quand [[lenny-summers|Lenny]] annonce l'arrestation de [[micah-bell|Micah]] à Strawberry."),
        M("Who is Not Without Sin", C2,
          "At camp. She comments as [[arthur-morgan|Arthur]] carries a drunk [[orville-swanson|Reverend Swanson]] to his tent.",
          "Au camp. Elle fait un commentaire quand [[arthur-morgan|Arthur]] ramène sous sa tente le [[orville-swanson|révérend Swanson]], ivre."),
        M("An Honest Mistake", C3,
          "Co-giver with [[uncle|Uncle]], according to the mission page. She calls Arthur over to talk about Dutch and is interrupted by Uncle's tip.",
          "Donneuse de la mission avec [[uncle|Uncle]], d'après la page de la mission. Elle appelle Arthur pour lui parler de Dutch et se fait couper par le tuyau d'Uncle."),
        M("Blessed are the Peacemakers", C3,
          "At camp. Asked by Arthur where Dutch is, she waves him off and walks away.",
          "Au camp. Quand Arthur lui demande où est Dutch, elle l'écarte d'un geste et s'éloigne."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Listed by the Red Dead Wiki; she is not among the riders to Braithwaite Manor, and the mission page does not name her.",
          "Citée par le Red Dead Wiki ; elle ne fait pas partie des cavaliers partis au manoir Braithwaite, et la page de la mission ne la nomme pas."),
        M("The Battle of Shady Belle", C3,
          "On arrival at Shady Belle, she asks Dutch for a word, and he turns her down.",
          "À l'arrivée à Shady Belle, elle demande à parler à Dutch, qui l'éconduit."),
        M("Horsemen, Apocalypses", C4,
          "At Shady Belle during the O'Driscoll attack. She does not fight; the mission fails if she is killed.",
          "À Shady Belle pendant l'attaque des O'Driscoll. Elle ne combat pas ; la mission échoue si elle est tuée."),
        M("Banking, The Old American Art", C4,
          "Absent. She is one of the gang members who take no part in the Saint Denis bank robbery.",
          "Absente. Elle fait partie des membres de la bande qui ne participent pas au braquage de la banque de Saint-Denis."),
        M("That's Murfree Country", C5,
          "Killed. Brought drunk to Beaver Hollow by Uncle, she claims she informed the Pinkertons, and Susan shoots her.",
          "Tuée. Ramenée ivre à Beaver Hollow par Uncle, elle affirme avoir renseigné les Pinkerton, et Susan l'abat."),
        M("Red Dead Redemption", C6,
          "Mentioned. [[andrew-milton|Milton]] tells Arthur that she never talked; Arthur later tells Dutch that the traitor is Micah, not Molly.",
          "Mentionnée. [[andrew-milton|Milton]] apprend à Arthur qu'elle n'a jamais parlé ; Arthur affirme ensuite à Dutch que le traître est Micah, pas Molly."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Molly's camp lines are quoted under Personality.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Les répliques de Molly au camp figurent dans la section Personnalité.")},
    {"h4": two("Molly", "Molly")},
    {"quotes": [
        {"q": two("I was wondering when he'd show up.", "I was wondering when he'd show up."),
         "src": two("Who is Not Without Sin (RDR2, chapter 2), as Arthur carries a drunk Reverend Swanson into camp",
                    "Who is Not Without Sin (RDR2, chapitre 2), quand Arthur ramène au camp le révérend Swanson, ivre. Traduction : « Je me demandais quand il allait se montrer. »")},
        {"q": two("Could I have a word with ya?", "Could I have a word with ya?"),
         "src": two("To Dutch, The Battle of Shady Belle (RDR2, chapter 3), on the gang's arrival at Shady Belle, after she calls out \"Dutch?\" and he answers \"Yes?\". Dutch then says: \"Not now. Come on Arthur.\"",
                    "À Dutch, The Battle of Shady Belle (RDR2, chapitre 3), à l'arrivée de la bande à Shady Belle, après l'avoir interpellé (\"Dutch?\") et qu'il a répondu \"Yes?\". Dutch enchaîne : \"Not now. Come on Arthur.\" Traduction : « Je pourrais te dire un mot ? » (« Pas maintenant. Viens, Arthur. »)")},
        {"q": two("I won't be ignored, Dutch van der Linde. I aren't him... I ain't her, or any of your stooges! You don't owe me nothing. I don't owe you nothing. Nothing!", "I won't be ignored, Dutch van der Linde. I aren't him... I ain't her, or any of your stooges! You don't owe me nothing. I don't owe you nothing. Nothing!"),
         "src": two("To Dutch (RDR2; quote box of her page on the Red Dead Wiki, which does not name the scene; the same page's account of the Beaver Hollow confrontation in \"That's Murfree Country\" paraphrases these words)",
                    "À Dutch (RDR2 ; citation en exergue de sa page sur le Red Dead Wiki, qui ne précise pas la scène ; le récit que fait la même page de l'esclandre de Beaver Hollow, dans \"That's Murfree Country\", reprend ces mots). Traduction : « Je ne me laisserai pas ignorer, Dutch van der Linde. Je suis pas lui... je suis pas elle, ni un de tes larbins ! Tu me dois rien. Je te dois rien. Rien ! »")},
    ]},
    {"h4": two("Said to her and about her", "Ce qu'on lui dit, ce qu'on dit d'elle")},
    {"quotes": [
        {"q": two("You're over here...Miss O'Shea will show you the way.", "You're over here...Miss O'Shea will show you the way."),
         "src": two("Susan Grimshaw to Dutch, Outlaws from the West (RDR2, chapter 1), pointing to his cabin at Colter",
                    "Susan Grimshaw à Dutch, Outlaws from the West (RDR2, chapitre 1), en lui désignant sa cabane à Colter. Traduction : « C'est par ici... Mademoiselle O'Shea va vous montrer le chemin. »")},
        {"q": two("You think we should've asked Molly to come with us?", "You think we should've asked Molly to come with us?"),
         "src": two("Tilly Jackson to Karen and Mary-Beth, Polite Society, Valentine Style (RDR2, chapter 2), on the wagon to Valentine",
                    "Tilly Jackson à Karen et Mary-Beth, Polite Society, Valentine Style (RDR2, chapitre 2), dans le chariot qui les mène à Valentine. Traduction : « Tu crois qu'on aurait dû proposer à Molly de venir ? »")},
        {"q": two("Oh no, Miss O'Shea is far too high and mighty now for the likes of us... or to do any real work. She's a society lady now.", "Oh no, Miss O'Shea is far too high and mighty now for the likes of us... or to do any real work. She's a society lady now."),
         "src": two("Karen Jones, in reply to Tilly, Polite Society, Valentine Style (RDR2, chapter 2)",
                    "Karen Jones, en réponse à Tilly, Polite Society, Valentine Style (RDR2, chapitre 2). Traduction : « Oh non, Mademoiselle O'Shea est bien trop grande dame maintenant pour des filles comme nous... ou pour faire un vrai travail. C'est une femme du monde, désormais. »")},
        {"q": two("Hey Molly, where's Dutch?", "Hey Molly, where's Dutch?"),
         "src": two("Arthur Morgan, Blessed are the Peacemakers (RDR2, chapter 3), at the opening of the mission; Molly waves him off and walks away",
                    "Arthur Morgan, Blessed are the Peacemakers (RDR2, chapitre 3), au début de la mission ; Molly l'écarte d'un geste et s'éloigne. Traduction : « Hé, Molly, où est Dutch ? »")},
        {"q": two("Can you believe that girl? All I've got going on and she wants to talk.", "Can you believe that girl? All I've got going on and she wants to talk."),
         "src": two("Dutch van der Linde to Arthur, The Battle of Shady Belle (RDR2, chapter 3), riding out of Shady Belle after turning her away",
                    "Dutch van der Linde à Arthur, The Battle of Shady Belle (RDR2, chapitre 3), en quittant Shady Belle après l'avoir éconduite. Traduction : « Tu te rends compte, cette fille ? Avec tout ce que j'ai sur le dos, elle veut discuter. »")},
        {"q": two("I've got far more important things to worry about right now than Molly O'Shea.", "I've got far more important things to worry about right now than Molly O'Shea."),
         "src": two("Dutch van der Linde, The Battle of Shady Belle (RDR2, chapter 3), when Arthur asks whether everything is okay between them",
                    "Dutch van der Linde, The Battle of Shady Belle (RDR2, chapitre 3), quand Arthur lui demande si tout va bien entre eux. Traduction : « J'ai des soucis bien plus importants en ce moment que Molly O'Shea. »")},
        {"q": two("Micah? You mean Molly?", "Micah? You mean Molly?"),
         "src": two("Arthur Morgan to Andrew Milton, Red Dead Redemption (RDR2, chapter 6), at Van Horn",
                    "Arthur Morgan à Andrew Milton, Red Dead Redemption (RDR2, chapitre 6), à Van Horn. Traduction : « Micah ? Vous voulez dire Molly ? »")},
        {"q": two("Molly O'Shea? We sweated her a couple of times... never talked a word, had to let her go.", "Molly O'Shea? We sweated her a couple of times... never talked a word, had to let her go."),
         "src": two("Andrew Milton to Arthur, Red Dead Redemption (RDR2, chapter 6), at Van Horn",
                    "Andrew Milton à Arthur, Red Dead Redemption (RDR2, chapitre 6), à Van Horn. Traduction : « Molly O'Shea ? On l'a cuisinée une ou deux fois... jamais dit un mot, on a dû la relâcher. »")},
        {"q": two("You're the rat, Micah. Not Molly, Dutch. Him. HIM!", "You're the rat, Micah. Not Molly, Dutch. Him. HIM!"),
         "src": two("Arthur Morgan, Red Dead Redemption (RDR2, chapter 6), ending in which Arthur goes back for the money with high honor",
                    "Arthur Morgan, Red Dead Redemption (RDR2, chapitre 6), fin où Arthur retourne chercher l'argent avec un honneur élevé. Traduction : « C'est toi, le rat, Micah. Pas Molly, Dutch. Lui. LUI ! »")},
        {"q": two("You lie, Micah. You're the rat. Not Molly, Dutch. It's him. Him! Kill him! Not Molly... not Miss Grimshaw... not even Colm. It's him.", "You lie, Micah. You're the rat. Not Molly, Dutch. It's him. Him! Kill him! Not Molly... not Miss Grimshaw... not even Colm. It's him."),
         "src": two("Arthur Morgan to Dutch, Red Dead Redemption (RDR2, chapter 6), ending in which Arthur goes back for the money with low honor, after Micah has stabbed him in the chest and Dutch has arrived and stopped Micah",
                    "Arthur Morgan à Dutch, Red Dead Redemption (RDR2, chapitre 6), fin où Arthur retourne chercher l'argent avec un honneur bas, après que Micah l'a poignardé à la poitrine et que Dutch, arrivé sur les lieux, l'a retenu. Traduction : « Tu mens, Micah. C'est toi, le rat. Pas Molly, Dutch. C'est lui. Lui ! Tue-le ! Pas Molly... pas Mademoiselle Grimshaw... même pas Colm. C'est lui. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("Arthur never takes Molly along on a mission or a companion activity, the only gang member in that case, so she never shows up as a companion icon on the map, not even in \"Horsemen, Apocalypses\".",
            "Arthur n'emmène jamais Molly en mission ni en activité de compagnon, cas unique dans la bande : elle n'apparaît donc jamais sur la carte comme icône de compagnon, pas même dans \"Horsemen, Apocalypses\"."),
        two("According to the Red Dead Wiki, she is the only gang member who dies in 1899 and is not buried.",
            "D'après le Red Dead Wiki, elle est le seul membre de la bande mort en 1899 à ne pas être enterré."),
        two("According to the Red Dead Wiki, she is the only member of the gang who is never seen riding a horse.",
            "D'après le Red Dead Wiki, elle est le seul membre de la bande qu'on ne voit jamais à cheval."),
        two("According to the Red Dead Wiki, her red skirt closely resembles the Constance Skirt that female characters can wear in Red Dead Online.",
            "D'après le Red Dead Wiki, sa jupe rouge ressemble beaucoup à la Constance Skirt que peuvent porter les personnages féminins de Red Dead Online."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Molly is one of the gang members whose portrait and short description Rockstar posted on Twitter on September 6, 2018, a series that The Hollywood Reporter reproduced the next day (see Personality). She also figures in the composite of 23 gang members' official art designs that illustrates Wikipedia's list of the game's characters, in the front row between Sadie Adler and Mary-Beth Gaskill.",
              "Molly fait partie des membres de la bande dont Rockstar publie le portrait et une courte description sur Twitter le 6 septembre 2018, une série que The Hollywood Reporter reprend le lendemain (voir Personnalité). Elle figure aussi dans le montage des illustrations officielles de 23 membres de la bande qui ouvre la liste des personnages du jeu sur Wikipédia, au premier rang, entre Sadie Adler et Mary-Beth Gaskill.")},
]
