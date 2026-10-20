"""Angelo Bronte, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/angelo/, m/, fcb/ and w/):
- Red Dead Wiki EN "Angelo Bronte" (Mission appearances, Quotes, Trivia) and FR "Angelo Bronte" (fr.txt: listed as a
  character mentioned in Red Dead Online).
- Mission pages: Blood Feuds, Ancient and Modern; The Joys of Civilization; Angelo Bronte, A Man of Honor (gold medal
  objectives, trivia: Jack's pronunciation, firearms in the cemetery); The Gilded Cage (quote box); Horsemen,
  Apocalypses; Urban Pleasures; Country Pursuits (trivia: Hosea's line recalled in "Red Dead Redemption"); Revenge is
  a Dish Best Eaten (quote box, gold medal objectives, trivia: El Presidio echo, "repulsive little maggot", 150 dollars,
  Mauser, alligator); No, No and Thrice, No (trivia: Susan's dialogue); Simple Pleasures; Bare Knuckle Friendships.
- Other pages: "Henri Lemieux" (quote box of Bronte's line on the mayor), "Angelo Bronte's Mansion" and "Saint Denis
  Mob" (free roam trivia, Red Dead Online), "Guido Martelli" and "Blood Money" (Rockstar Newswire, Capitale), Camp
  Events (activities and events unlocked after "Angelo Bronte, A Man of Honor"). Leitmotif: fact-checked sadie_C,
  colm_C, john_E. Blood Money release date July 13, 2021, as in sean_C.
- No transcript exists on the wiki for Bronte's three missions (API missingtitle, Oct 2026). Quoted lines come only
  from quote boxes, quote lists and story text of the wiki pages named above, with the speaker and mission they give
  (this sourcing note is kept out of the public text).
Fix pass (20 Oct 2026): the Wapiti line and Dutch's "worst crook in town" removed from Quotes (quoted in part B);
Trivia items on the mansion doors/guards (part B + part D cut content) and "a lizard in a suit" (part B) removed;
the Javier echo reworded (John's own line, as in dutch_D); Martelli in Online = underboss (Blood Money is set in 1898);
the second Missions table retitled "Other missions linked to Bronte" (Bare Knuckle Friendships never names him).
Ownership: narrative events are in part A (one line per mission here). Bronte's lines from the character page's quote
list ("You are nothing...", "So, you walk into my city...", "You ask me to show compassion?", "You twist words...",
"The law will find you!") are left to part B "In his own words" and not repeated here; the Quotes block keeps lines
by others about him and his two remarks on guests at the gala (to be deduped by the fixer if part B uses them).
Real-world material (Jim Pirri, casting) goes to part D.
Excluded: the name's supposed references to Angelo Bruno and Charles Matranga, and the Sicilian town of Bronte as
"foreshadowing" (wiki speculation, "may be", "seems"); the Italian taunt at the party (sources disagree on its
target and meaning); the Newswire text itself (not retrievable, Oct 2026: attributed through the wiki).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
EP1 = two("Epilogue 1: Pronghorn Ranch", "Épilogue 1 : Pronghorn Ranch")
EP2 = two("Epilogue 2: Beecher's Hope", "Épilogue 2 : Beecher's Hope")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Bronte appears in person in three missions of Red Dead Redemption 2, all in chapter 4. Other missions bring up his name, his tip, his mansion or his former organization, from the raid on Braithwaite Manor to the 1907 epilogue; they are listed in the second table. The events themselves are told in the Biography.",
              "Bronte apparaît en personne dans trois missions de Red Dead Redemption 2, toutes au chapitre 4. D'autres missions évoquent son nom, son tuyau, sa demeure ou son ancienne organisation, de l'assaut contre Braithwaite Manor à l'épilogue de 1907 ; elles figurent dans le second tableau. Le déroulé des événements se trouve dans la Biographie.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Bronte's role", "Rôle de Bronte")], "rows": [
        M("Angelo Bronte, A Man of Honor", C4,
          "Receives [[dutch-van-der-linde|Dutch]], [[arthur-morgan|Arthur]] and [[john-marston|John]] at his mansion and returns [[jack-marston|Jack]] once the cemetery is cleared of grave robbers.",
          "Reçoit [[dutch-van-der-linde|Dutch]], [[arthur-morgan|Arthur]] et [[john-marston|John]] dans sa demeure et rend [[jack-marston|Jack]] une fois le cimetière débarrassé des pilleurs de tombes."),
        M("The Gilded Cage", C4,
          "Guest of honor at Mayor Lemieux's garden party; points out the guests to Dutch and Arthur and gives them the trolley station tip.",
          "Invité d'honneur de la garden-party du maire Lemieux ; présente les invités à Dutch et Arthur et leur souffle le tuyau de la station de tramways."),
        M("Revenge is a Dish Best Eaten", C4,
          "Captured in his mansion, knocked out by John and drowned by Dutch from the skiff.",
          "Capturé dans sa demeure, assommé par John et noyé par Dutch depuis la barque."),
    ]}},
    {"h4": two("Other missions linked to Bronte", "Autres missions liées à Bronte")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Bronte", "Lien avec Bronte")], "rows": [
        M("Blood Feuds, Ancient and Modern", C3,
          "[[catherine-braithwaite|Catherine Braithwaite]] reveals that her sons gave Jack to Bronte; her letter to him lies in the manor.",
          "[[catherine-braithwaite|Catherine Braithwaite]] révèle que ses fils ont livré Jack à Bronte ; sa lettre à Bronte se trouve dans le manoir."),
        M("The Joys of Civilization", C4,
          "Dutch and Arthur look for Bronte's address in Saint Denis.",
          "Dutch et Arthur cherchent l'adresse de Bronte à Saint-Denis."),
        M("Horsemen, Apocalypses", C4,
          "Dutch and Arthur plan the trolley station robbery Bronte suggested.",
          "Dutch et Arthur préparent l'attaque de la station de tramways suggérée par Bronte."),
        M("Urban Pleasures", C4,
          "Bronte's tip proves to be a set-up; Dutch, Arthur and [[lenny-summers|Lenny]] escape the police with fifteen dollars and a quarter each.",
          "Le tuyau de Bronte se révèle un piège ; Dutch, Arthur et [[lenny-summers|Lenny]] échappent à la police avec quinze dollars et vingt-cinq cents chacun."),
        M("Country Pursuits", C4,
          "Dutch argues with [[hosea-matthews|Hosea]] over killing Bronte, then finds a boat to reach his mansion.",
          "Dutch se dispute avec [[hosea-matthews|Hosea]] au sujet du meurtre de Bronte, puis trouve une barque pour atteindre sa demeure."),
        M("Simple Pleasures", EP1,
          "John reminds Jack how far he now is from Bronte's mansion.",
          "John rappelle à Jack combien il est loin, désormais, de la demeure de Bronte."),
        M("Bare Knuckle Friendships", EP2,
          "[[charles-smith|Charles]] and John fight off the men of Guido Martelli, once Bronte's underboss, who now runs things in Saint Denis.",
          "[[charles-smith|Charles]] et John repoussent les hommes de Guido Martelli, jadis bras droit de Bronte, qui fait désormais la loi à Saint-Denis."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Bronte's own exchanges with Dutch, and his remark on Rains Fall and Eagle Flies, are quoted under Personality.",
              "Les répliques ci-dessous sont citées en version originale. Les échanges de Bronte avec Dutch, ainsi que sa remarque sur Rains Fall et Eagle Flies, figurent dans la rubrique Personnalité.")},
    {"h4": two("At the mayor's party", "À la réception du maire")},
    {"quotes": [
        {"q": two("See that wretch? He's the mayor! He'll do anything for a dollar, and I mean anything.",
                  "See that wretch? He's the mayor! He'll do anything for a dollar, and I mean anything."),
         "src": two("Bronte to Dutch and Arthur, describing Henri Lemieux, The Gilded Cage (RDR2, chapter 4)",
                    "Bronte à Dutch et Arthur, à propos d'Henri Lemieux, The Gilded Cage (RDR2, chapitre 4). Traduction : « Vous voyez ce misérable ? C'est le maire ! Il ferait n'importe quoi pour un dollar, et je dis bien n'importe quoi. »")},
    ]},
    {"h4": two("About Bronte", "Au sujet de Bronte")},
    {"quotes": [
        {"q": two("You'll damn us all...", "You'll damn us all..."),
         "src": two("Hosea to Dutch, after Arthur backs the plan to kill Bronte, Country Pursuits (RDR2, chapter 4)",
                    "Hosea à Dutch, après qu'Arthur a soutenu le projet de tuer Bronte, Country Pursuits (RDR2, chapitre 4). Traduction : « Tu vas tous nous perdre... »")},
        {"q": two("It ain't nice, I know it... but it is us, or him. I figure it might as well be him.",
                  "It ain't nice, I know it... but it is us, or him. I figure it might as well be him."),
         "src": two("Dutch, after drowning Bronte, Revenge is a Dish Best Eaten (RDR2, chapter 4)",
                    "Dutch, après avoir noyé Bronte, Revenge is a Dish Best Eaten (RDR2, chapitre 4). Traduction : « Ce n'est pas joli, je sais... mais c'était nous ou lui. Autant que ce soit lui. »")},
        {"q": two("You're a long way from Angelo Bronte's mansion now.", "You're a long way from Angelo Bronte's mansion now."),
         "src": two("John to Jack, in the stables, Simple Pleasures (RDR2, epilogue, 1907)",
                    "John à Jack, dans les écuries, Simple Pleasures (RDR2, épilogue, 1907). Traduction : « Tu es bien loin de la demeure d'Angelo Bronte, maintenant. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("On the ride back from the mansion, Jack gets both of his Italian words slightly wrong, according to the mission page: he says \"pantafòla\" for \"pantòfola\" (slipper), and pronounces \"cavallo\" (horse) the Spanish way.",
            "Sur le chemin du retour, Jack écorche ses deux mots d'italien, selon la page de la mission : il dit \"pantafòla\" pour \"pantòfola\" (pantoufle) et prononce \"cavallo\" (cheval) à l'espagnole."),
        two("Firing a weapon in the cemetery while looking for the grave robbers fails \"Angelo Bronte, A Man of Honor\". John then shouts: \"Goddamn it, Arthur! How are we gonna get Jack back now?\"",
            "Faire feu dans le cimetière pendant la recherche des pilleurs de tombes fait échouer \"Angelo Bronte, A Man of Honor\". John s'écrie alors : \"Goddamn it, Arthur! How are we gonna get Jack back now?\" (bon sang, Arthur ! Comment on va récupérer Jack, maintenant ?)."),
        two("Bronte carries cash that Arthur can loot once he is knocked out: 150 dollars according to the mission page, 155 according to the character page. The money can pay off the bounty earned during the raid.",
            "Bronte porte sur lui de l'argent qu'Arthur peut récupérer une fois qu'il est assommé : 150 dollars selon la page de la mission, 155 selon la page du personnage. La somme peut servir à payer la prime gagnée pendant l'assaut."),
        two("The Mauser pistol Bronte throws at John can be picked up before Arthur carries him off, although the weapon is not otherwise available until \"That's Murfree Country\", in chapter 5.",
            "Le pistolet Mauser que Bronte lance sur John peut être ramassé avant qu'Arthur n'emporte son propriétaire, alors que cette arme n'est normalement accessible qu'à partir de \"That's Murfree Country\", au chapitre 5."),
        two("The alligator that takes Bronte's body can already be seen when the gang reaches the back of the mansion, at the start of \"Revenge is a Dish Best Eaten\".",
            "L'alligator qui emporte le corps de Bronte est déjà visible quand la bande arrive à l'arrière de la demeure, au début de \"Revenge is a Dish Best Eaten\"."),
        two("Dutch calls Bronte a \"repulsive little maggot\" as he drowns him. [[simon-pearson|Pearson]] uses the same insult against [[uncle|Uncle]] in a camp scene, after Uncle criticizes his cooking.",
            "Dutch traite Bronte de \"repulsive little maggot\" (répugnant petit asticot) en le noyant. [[simon-pearson|Pearson]] lance la même insulte à [[uncle|Uncle]] dans une scène de camp, quand celui-ci critique sa cuisine."),
        two("In Red Dead Redemption, John himself uses nearly the same words as Dutch when he confronts [[javier-escuella|Javier Escuella]] in 1911: \"It's you or me, the way I see it, it might as well be you.\"",
            "Dans Red Dead Redemption, c'est John qui reprend presque mot pour mot la phrase de Dutch quand il affronte [[javier-escuella|Javier Escuella]] en 1911 : \"It's you or me, the way I see it, it might as well be you.\" (c'est toi ou moi, et à mon avis, autant que ce soit toi)."),
        two("Hosea's warning in \"Country Pursuits\" comes back to Arthur during his last ride to camp in the mission \"Red Dead Redemption\", if his honor is low.",
            "L'avertissement d'Hosea dans \"Country Pursuits\" revient à l'esprit d'Arthur lors de sa dernière chevauchée vers le camp, dans la mission \"Red Dead Redemption\", si son honneur est bas."),
        two("Among the gold medal objectives of \"Revenge is a Dish Best Eaten\" are searching every room of the mansion and carrying Bronte to the skiff within 1 minute and 30 seconds.",
            "Parmi les objectifs de la médaille d'or de \"Revenge is a Dish Best Eaten\" figurent la fouille de toutes les pièces de la demeure et le transport de Bronte jusqu'à la barque en moins d'une minute et trente secondes."),
        two("Susan's conversation with Arthur on the ride in \"No, No and Thrice, No\" depends on whether Jack has been brought back from Bronte's: before, she lists the gang's recent kidnappings; after, she remarks that Kieran has not been seen for a while.",
            "La conversation entre Susan et Arthur pendant le trajet de \"No, No and Thrice, No\" dépend du retour de Jack : avant, elle fait le compte des enlèvements récents qui ont frappé la bande ; après, elle note que Kieran n'a pas été vu depuis un moment."),
        two("Several companion activities at Shady Belle, among them \"Go Rustling\" with Uncle and a coach robbery with Lenny, only become available once \"Angelo Bronte, A Man of Honor\" is complete.",
            "Plusieurs activités de compagnon à Shady Belle, dont \"Go Rustling\" avec Uncle et une attaque de diligence avec Lenny, ne se débloquent qu'une fois \"Angelo Bronte, A Man of Honor\" terminée."),
        two("Bronte is one of only four characters in Red Dead Redemption 2 with a recurring musical theme of his own, with [[john-marston|John Marston]], [[sadie-adler|Sadie Adler]] and [[colm-odriscoll|Colm O'Driscoll]].",
            "Bronte fait partie des quatre seuls personnages de Red Dead Redemption 2 dotés d'un thème musical récurrent, avec [[john-marston|John Marston]], [[sadie-adler|Sadie Adler]] et [[colm-odriscoll|Colm O'Driscoll]]."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Red Dead Online", "Red Dead Online")},
    {"p": two("Bronte does not appear in Red Dead Online, but the French edition of the Red Dead Wiki lists him among the characters mentioned there. The Blood Money update, released on 13 July 2021, centers on Guido Martelli, Bronte's underboss (Red Dead Online is set in 1898, while Bronte is alive), who sends the player after Capitale. Rockstar's Newswire, as quoted by the Red Dead Wiki, describes Capitale as a system of exchange designed for the Bronte family's more sensitive business, whose value depends on its scarcity. The Red Dead Wiki adds that getting back into his Flavian Street mansion, which normally takes a glitch, is easier in Online. Members of the Saint Denis mob can also attack the player during deliveries of goods to Saint Denis for Cripps's trading company, in the Frontier Pursuits update.",
              "Bronte n'apparaît pas dans Red Dead Online, mais l'édition française du Red Dead Wiki le compte parmi les personnages qui y sont mentionnés. La mise à jour Blood Money, sortie le 13 juillet 2021, tourne autour de Guido Martelli, le bras droit de Bronte (Red Dead Online se déroule en 1898, du vivant de Bronte), qui lance le joueur à la recherche du Capitale. Le Newswire de Rockstar, cité par le Red Dead Wiki, présente le Capitale comme un moyen d'échange conçu pour les affaires les plus délicates de la famille Bronte, et dont la valeur tient à sa rareté. Le Red Dead Wiki ajoute qu'on ne peut retourner dans sa demeure de Flavian Street qu'à la faveur d'un bug, et que c'est bien plus simple dans Online. Des membres de la pègre de Saint-Denis peuvent aussi attaquer le joueur lors des livraisons de marchandises à Saint-Denis pour le comptoir de Cripps, dans la mise à jour Frontier Pursuits.")},
]
