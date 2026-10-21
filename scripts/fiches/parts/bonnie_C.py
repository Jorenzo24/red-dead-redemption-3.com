"""Bonnie MacFarlane, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026 via the MediaWiki API, cache scripts/v3/work/_m/ and
scripts/v3/work/bonnie/):
- Character page "Bonnie MacFarlane" (Mission appearances, Quotes incl. Multiplayer and Red Dead Online lists, Trivia,
  Gallery captions) and FR page (fr.txt: Apparitions dans les missions, Anecdotes).
- Mission pages (infobox position, rewards, trivia): Exodus in America (first mission; Bonnie on the train); New Friends,
  Old Problems (second; rewards; barn line; subtitle discrepancies); Obstacles in Our Path (third; 20 Fame win or lose);
  This is Armadillo, USA (fourth); Women and Cattle (fifth); Wild Horses, Tamed Passions (sixth; lasso, Kentucky Saddler);
  A Tempest Looms (seventh); The Burning (22nd; its "only mission without a Stranger unlock" trivia is dropped: Hanging Bonnie MacFarlane unlocks none either); Hanging
  Bonnie MacFarlane (23rd); The Outlaw's Return (49th, first of the Homestead chapter); Old Friends, New Problems (53rd;
  Amos subtitle fixed in the GOTY edition); Paternal Pride (Undead Nightmare; quote box; Winchester Repeater reward);
  Red Dead Online free roam pages Recovery, Delivery, Caravan Escort, On The Hunt (Bonnie's start and end points).
- Transcripts ("/dialogues") of the eleven RDR1 missions: every mission quote below is checked word for word against
  them. Paternal Pride has no transcript: its line comes from the mission page's quote box. "Daddy, stop teasing me!",
  the multiplayer taunts and the Red Dead Online lines come from the character page's quote lists.
- Other pages: "Letter to Bonnie MacFarlane" (Arthur's and John's reactions to the survivor), "Kidnapped Woman Found
  Alive" (Blackwater Ledger No. 55), "MacFarlane's Ranch" (RDR2 barn note), "Outfitter" wording as in abigail_C/jack_C.
- Real world: Liars and Cheats Pack detailed by Rockstar on August 27, 2010 and released on September 21, 2010 (as in
  jack_C, abigail_C); RDR1 ports on PlayStation 4 and Nintendo Switch (August 17, 2023) and PC (October 29, 2024)
  without multiplayer (as in uncle_C, bill_C, jack_C).

Ownership: narrative events are in part A (one line per mission here). Quotes: "Call me Bonnie, you dolt!" and "call me
Bonnie, you fool" are left to part B (Names); the GOTY guide description and "I wouldn't change my life for all the
money in the world" (wiki only, no transcript) to part B. If part B quotes any line below, the fixer keeps it in one
place. Real-world material (Kimberly Irion, Rob Hanson naming, Steve J. Palmer motion capture on the train, Game
Informer's list) goes to part D. Appearance details (two belts, necklace) and "John calls her Bonnie only twice" go to B.
Fix pass (20 Oct 2026): Quotes no longer repeat part B's "In her own words" lines (Burning quote trimmed to its first sentences);
"Stupid is the word..." added (New Friends transcript); trivia items on rewards, 20 Fame, the Winchester artwork and the
Stranger unlock cut (told in part B or wrong); the Red Dead Online paragraph of Other media cut (told in A, B and the table).
Excluded: the Annie Stoakes comparison (interpretation); "Bonnie is the only character John willingly opens up to"
(interpretation, left to B if sourced); "plausibly an in-story misreporting" for the age conflict (speculation); the
"Paternal Pride" Walking Dead references (wiki speculation, "appears to be"); the "$15 never taken from John's account"
reading that the debt was "considered absolved" (implication: only the account fact is kept); the players' theory on
why she was on the train; the "John's bandage on his right foot" trivia (not about Bonnie); "Gentleman's Attire"
Nightwatch glitch (no value); the PlayStation Home outfit for the Xbox avatar (FR only, unverified: only PlayStation
Home, from the EN page, is kept).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A1 = two("Act I: New Austin", "Acte I : New Austin")
A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
UN = two("Undead Nightmare", "Undead Nightmare")
RO = two("Red Dead Online (1898)", "Red Dead Online (1898)")
R2 = two("Red Dead Redemption 2", "Red Dead Redemption 2")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Bonnie gives John the first missions of Red Dead Redemption after \"Exodus in America\": her strand runs from \"New Friends, Old Problems\" to \"Hanging Bonnie MacFarlane\" and teaches the basics of the game (shooting, riding, driving a wagon, herding, the lasso, climbing). She returns in two missions of Act III and in one side mission of Undead Nightmare. In Red Dead Online she gives free roam missions. The events are told in the Biography.",
              "Bonnie confie à John les premières missions de Red Dead Redemption après \"Exodus in America\" : sa série va de \"New Friends, Old Problems\" à \"Hanging Bonnie MacFarlane\" et sert à apprendre les bases du jeu (tir, équitation, conduite d'un chariot, conduite de troupeau, lasso, escalade). Elle revient dans deux missions de l'acte III et dans une mission secondaire d'Undead Nightmare. Dans Red Dead Online, elle propose des missions en monde libre. Le déroulé des événements se trouve dans la Biographie.")},
    {"h4": two("Red Dead Redemption and Undead Nightmare", "Red Dead Redemption et Undead Nightmare")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Bonnie's role", "Rôle de Bonnie")], "rows": [
        M("Exodus in America", A1,
          "Travels on the same train as John, then finds him shot near Fort Mercer with Amos.",
          "Voyage dans le même train que John, puis le trouve blessé près de Fort Mercer avec Amos."),
        M("New Friends, Old Problems", A1,
          "Mission giver. Tells John what his treatment cost, shows him the ranch and patrols the property with him at night.",
          "Donneuse de mission. Annonce à John le prix de ses soins, lui fait visiter le ranch et surveille la propriété avec lui la nuit."),
        M("Obstacles in Our Path", A1,
          "Mission giver. Questions John about Bill, races him on horseback and sends him to the marshal.",
          "Donneuse de mission. Interroge John sur Bill, le défie à la course à cheval et l'envoie voir le marshal."),
        M("This is Armadillo, USA", A1,
          "Mission giver. Rides with John to Armadillo in her wagon and pays for his first medicine.",
          "Donneuse de mission. Se rend avec John à Armadillo dans son chariot et lui offre ses premiers médicaments."),
        M("Women and Cattle", A1,
          "Mission giver. Hears John's account of his past, then has him drive the herd to pasture.",
          "Donneuse de mission. Écoute John raconter son passé, puis lui fait mener le troupeau au pâturage."),
        M("Wild Horses, Tamed Passions", A1,
          "Mission giver. Introduces her father, gives John a lasso, breaks horses with him and gives him the stallion.",
          "Donneuse de mission. Présente son père, remet un lasso à John, dresse des chevaux avec lui et lui offre l'étalon."),
        M("A Tempest Looms", A1,
          "Mission giver. Argues with Amos, then brings the herd home through the storm with John.",
          "Donneuse de mission. Se dispute avec Amos, puis ramène le troupeau à travers l'orage avec John."),
        M("The Burning", A1,
          "Mission giver. Searches for her father with John, then watches him save the horses from the burning barn.",
          "Donneuse de mission. Cherche son père avec John, puis le voit sauver les chevaux de la grange en feu."),
        M("Hanging Bonnie MacFarlane", A1,
          "Kidnapped by Williamson's gang and nearly hanged at Tumbleweed; cut down by John.",
          "Enlevée par la bande de Williamson et presque pendue à Tumbleweed ; décrochée par John."),
        M("The Outlaw's Return", A3,
          "Meets Jack and helps John drive the cattle he buys off the ranch.",
          "Fait la connaissance de Jack et aide John à sortir du ranch le bétail qu'il achète."),
        M("Old Friends, New Problems", A3,
          "Sends the telegram asking for corn, then meets [[abigail-marston|Abigail]] at the ranch. Her last appearance in the story.",
          "Envoie le télégramme réclamant du maïs, puis fait la connaissance d'[[abigail-marston|Abigail]] au ranch. Sa dernière apparition dans l'histoire."),
        M("Paternal Pride", UN,
          "Mission giver. Asks John to find her father in the barn.",
          "Donneuse de mission. Demande à John de retrouver son père dans la grange."),
    ]}},
    {"h4": two("Red Dead Online and Red Dead Redemption 2", "Red Dead Online et Red Dead Redemption 2")},
    {"table": {"head": [two("Mission", "Mission"), two("Game", "Jeu"), two("Bonnie's role", "Rôle de Bonnie")], "rows": [
        M("Recovery", RO,
          "Mission giver. The introductory job sends the player after a ranch wagon held by six bandits at Brittlebrush Trawl; another ends at Pike's Basin.",
          "Donneuse de mission. La mission d'introduction envoie le joueur récupérer un chariot du ranch retenu par six bandits à Brittlebrush Trawl ; une autre se termine à Pike's Basin."),
        M("Delivery", RO,
          "Mission giver. Deliveries from MacFarlane's Ranch to Brittlebrush Trawl or Quaker's Cove.",
          "Donneuse de mission. Livraisons du MacFarlane's Ranch vers Brittlebrush Trawl ou Quaker's Cove."),
        M("Caravan Escort", RO,
          "Mission giver. Escort of two wagons from MacFarlane's Ranch to Thieves' Landing.",
          "Donneuse de mission. Escorte de deux chariots du MacFarlane's Ranch à Thieves' Landing."),
        M("On The Hunt", RO,
          "Mission giver. Hunt for a grizzly bear on the Lower Montana River.",
          "Donneuse de mission. Chasse d'un grizzly sur la Lower Montana River."),
        M("Random encounter (shipwreck survivor)", R2,
          "Mentioned. A dying man carries a love letter addressed to her.",
          "Évoquée. Un mourant porte une lettre d'amour qui lui est adressée."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise.")},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"quotes": [
        {"q": two("I do. \"Stupid\" is the word we use around here.", "I do. \"Stupid\" is the word we use around here."),
         "src": two("When John cannot find a polite word for how he feels, New Friends, Old Problems (RDR1, Act I)",
                    "Quand John ne trouve pas de mot poli pour dire comment il se sent, New Friends, Old Problems (RDR1, acte I). Traduction : « Moi, si. Ici, on dit \"stupide\". »")},
        {"q": two("Next time, Mr. Marston, I strongly recommend you don't try to lose it quite so earnestly.", "Next time, Mr. Marston, I strongly recommend you don't try to lose it quite so earnestly."),
         "src": two("To John, about his life, New Friends, Old Problems (RDR1, Act I)",
                    "À John, à propos de sa vie, New Friends, Old Problems (RDR1, acte I). Traduction : « La prochaine fois, Mr. Marston, je vous recommande vivement de ne pas chercher à la perdre avec autant d'application. »")},
        {"q": two("Change is only good when it makes things better.", "Change is only good when it makes things better."),
         "src": two("On the railroad reaching the ranch, New Friends, Old Problems (RDR1, Act I)",
                    "Sur l'arrivée du chemin de fer au ranch, New Friends, Old Problems (RDR1, acte I). Traduction : « Le changement n'a de bon que lorsqu'il améliore les choses. »")},
        {"q": two("Well, with your trigger itch and my feminine intuition, we should make quite a team.", "Well, with your trigger itch and my feminine intuition, we should make quite a team."),
         "src": two("On the night patrol, New Friends, Old Problems (RDR1, Act I)",
                    "Pendant la ronde de nuit, New Friends, Old Problems (RDR1, acte I). Traduction : « Avec votre gâchette qui vous démange et mon intuition féminine, on devrait faire une sacrée équipe. »")},
        {"q": two("You are being deliberately obscure as a substitute for having a personality.", "You are being deliberately obscure as a substitute for having a personality."),
         "src": two("To John, This is Armadillo, USA (RDR1, Act I)",
                    "À John, This is Armadillo, USA (RDR1, acte I). Traduction : « Vous jouez les mystérieux exprès, faute d'avoir une personnalité. »")},
        {"q": two("We'll be lucky if our ranch survives another 5 years. Businessmen are the new cowboys.", "We'll be lucky if our ranch survives another 5 years. Businessmen are the new cowboys."),
         "src": two("This is Armadillo, USA (RDR1, Act I)",
                    "This is Armadillo, USA (RDR1, acte I). Traduction : « On aura de la chance si notre ranch tient encore cinq ans. Les hommes d'affaires sont les nouveaux cow-boys. »")},
        {"q": two("You do so love to talk in riddles, Mr. Marston.", "You do so love to talk in riddles, Mr. Marston."),
         "src": two("Women and Cattle (RDR1, Act I)",
                    "Women and Cattle (RDR1, acte I). Traduction : « Vous adorez parler par énigmes, Mr. Marston. »")},
        {"q": two("Civilization is a truly beautiful thing, Mr. Marston.", "Civilization is a truly beautiful thing, Mr. Marston."),
         "src": two("After John describes his mission, Women and Cattle (RDR1, Act I)",
                    "Après que John a décrit sa mission, Women and Cattle (RDR1, acte I). Traduction : « La civilisation est vraiment une belle chose, Mr. Marston. »")},
        {"q": two("You're not bad with the herd. Ranching might be your true calling, Mr. Marston. Either that or you were a cow in a past life.", "You're not bad with the herd. Ranching might be your true calling, Mr. Marston. Either that or you were a cow in a past life."),
         "src": two("Women and Cattle (RDR1, Act I)",
                    "Women and Cattle (RDR1, acte I). Traduction : « Vous vous débrouillez avec le troupeau. L'élevage est peut-être votre vraie vocation, Mr. Marston. Ou alors vous étiez une vache dans une vie antérieure. »")},
        {"q": two("I think you could be a fine rancher someday. If you can bear to stop killing people for a living.", "I think you could be a fine rancher someday. If you can bear to stop killing people for a living."),
         "src": two("Wild Horses, Tamed Passions (RDR1, Act I)",
                    "Wild Horses, Tamed Passions (RDR1, acte I). Traduction : « Je crois que vous pourriez faire un bon éleveur un jour. Si vous arrivez à renoncer à tuer des gens pour gagner votre vie. »")},
        {"q": two("And if we lose the herd, we'll all die, you stupid man.", "And if we lose the herd, we'll all die, you stupid man."),
         "src": two("To Amos, A Tempest Looms (RDR1, Act I)",
                    "À Amos, A Tempest Looms (RDR1, acte I). Traduction : « Et si on perd le troupeau, on mourra tous, espèce d'idiot. »")},
        {"q": two("We all need to look for answers somewhere. Some in big ol' books. Others in big ol' bottles of whiskey.", "We all need to look for answers somewhere. Some in big ol' books. Others in big ol' bottles of whiskey."),
         "src": two("On faith, A Tempest Looms (RDR1, Act I)",
                    "Sur la foi, A Tempest Looms (RDR1, acte I). Traduction : « On a tous besoin de chercher des réponses quelque part. Certains dans de gros livres. D'autres dans de grosses bouteilles de whisky. »")},
        {"q": two("He switched his saddle for a tie, and that's fine. I just never met a man in a tie I could trust.", "He switched his saddle for a tie, and that's fine. I just never met a man in a tie I could trust."),
         "src": two("About her surviving brother, The Burning (RDR1, Act I)",
                    "À propos de son seul frère encore en vie, The Burning (RDR1, acte I). Traduction : « Il a troqué sa selle contre une cravate, c'est son affaire. Simplement, je n'ai jamais rencontré d'homme en cravate à qui je puisse faire confiance. »")},
        {"q": two("The outlaw with a code? How wonderfully romantic! The reluctant murderer, the noble criminal.", "The outlaw with a code? How wonderfully romantic! The reluctant murderer, the noble criminal."),
         "src": two("To John, The Burning (RDR1, Act I)",
                    "À John, The Burning (RDR1, acte I). Traduction : « Le hors-la-loi qui a un code ? Comme c'est romantique ! L'assassin malgré lui, le noble criminel. »")},
        {"q": two("If you think I'm going to lower myself by making a joke about being \"all tied up,\" you've got another thing coming.", "If you think I'm going to lower myself by making a joke about being \"all tied up,\" you've got another thing coming."),
         "src": two("To John, after he cuts her down, Hanging Bonnie MacFarlane (RDR1, Act I)",
                    "À John, qui vient de la décrocher, Hanging Bonnie MacFarlane (RDR1, acte I). Traduction : « Si vous croyez que je vais m'abaisser à plaisanter sur le fait d'être \"ficelée\", vous vous trompez lourdement. »")},
        {"q": two("Good Lord, do my eyes deceive me? A devil walks among us.", "Good Lord, do my eyes deceive me? A devil walks among us."),
         "src": two("Greeting John at the corral, The Outlaw's Return (RDR1, Act III)",
                    "En accueillant John à l'enclos, The Outlaw's Return (RDR1, acte III). Traduction : « Seigneur, mes yeux me jouent-ils des tours ? Un démon marche parmi nous. »")},
    ]},
    {"h4": two("Undead Nightmare", "Undead Nightmare")},
    {"quotes": [
        {"q": two("First hell walks the earth, then you turn up... can my week get any worse?", "First hell walks the earth, then you turn up... can my week get any worse?"),
         "src": two("Greeting John, Paternal Pride (Undead Nightmare)",
                    "En accueillant John, Paternal Pride (Undead Nightmare). Traduction : « D'abord l'enfer se répand sur terre, puis c'est vous qui débarquez... ma semaine peut-elle encore empirer ? »")},
        {"q": two("Daddy, stop teasing me!", "Daddy, stop teasing me!"),
         "src": two("Calling to her father, Undead Nightmare",
                    "En appelant son père, Undead Nightmare. Traduction : « Papa, arrête de me taquiner ! »")},
    ]},
    {"h4": two("Multiplayer and Red Dead Online", "Multijoueur et Red Dead Online")},
    {"quotes": [
        {"q": two("Are you afraid of losing to a woman?", "Are you afraid of losing to a woman?"),
         "src": two("Multiplayer taunt, Red Dead Redemption",
                    "Provocation du multijoueur, Red Dead Redemption. Traduction : « Tu as peur de perdre contre une femme ? »")},
        {"q": two("This sure beats milking cows!", "This sure beats milking cows!"),
         "src": two("Multiplayer taunt, Red Dead Redemption",
                    "Provocation du multijoueur, Red Dead Redemption. Traduction : « Ça vaut mieux que de traire les vaches ! »")},
        {"q": two("Look at that male pride go!", "Look at that male pride go!"),
         "src": two("Multiplayer taunt, Red Dead Redemption",
                    "Provocation du multijoueur, Red Dead Redemption. Traduction : « Regardez-moi cette fierté masculine ! »")},
        {"q": two("Leave now, or never leave at all!", "Leave now, or never leave at all!"),
         "src": two("Multiplayer taunt, Red Dead Redemption",
                    "Provocation du multijoueur, Red Dead Redemption. Traduction : « Pars maintenant, ou tu ne repartiras jamais ! »")},
        {"q": two("You really helped me out last time, thank you.", "You really helped me out last time, thank you."),
         "src": two("To the player, Red Dead Online",
                    "Au joueur, Red Dead Online. Traduction : « Vous m'avez vraiment rendu service la dernière fois, merci. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("The Blackwater Ledger article \"Kidnapped Woman Found Alive\", published after her rescue, calls her \"a spinster of 29 years\" and judges a crime of passion implausible for that reason. The age contradicts the 27 years given elsewhere, including by the Game of the Year Edition guide.",
            "L'article du Blackwater Ledger \"Kidnapped Woman Found Alive\", paru après son sauvetage, la qualifie de \"spinster of 29 years\" (vieille fille de 29 ans) et juge pour cette raison peu plausible la piste du crime passionnel. Cet âge contredit les 27 ans donnés ailleurs, notamment par le guide de l'édition Game of the Year."),
        two("During the tour of the ranch in \"New Friends, Old Problems\", Bonnie says her father built the barn himself when she was a little girl. In Red Dead Online (1898) and Red Dead Redemption 2 (1899 and 1907), the ranch has no barn.",
            "Pendant la visite du ranch, dans \"New Friends, Old Problems\", Bonnie raconte que son père a construit la grange de ses mains quand elle était petite. Dans Red Dead Online (1898) et Red Dead Redemption 2 (1899 et 1907), le ranch n'a pas de grange."),
        two("By the Red Dead Wiki's dates, Bonnie would be about 14 in Red Dead Online, set in 1898; her model there looks like a woman in her early twenties.",
            "D'après les dates du Red Dead Wiki, Bonnie aurait environ 14 ans dans Red Dead Online, qui se déroule en 1898 ; son modèle y a l'allure d'une femme d'une vingtaine d'années."),
        two("When the shipwreck survivor of Red Dead Redemption 2 wakes up to hand over his letter, Arthur exclaims \"Whoa, I thought you was already gone!\" and John \"Jesus! I thought you were dead...\".",
            "Quand le rescapé du naufrage de Red Dead Redemption 2 se réveille pour tendre sa lettre, Arthur s'exclame \"Whoa, I thought you was already gone!\" (je te croyais déjà parti) et John \"Jesus! I thought you were dead...\" (je te croyais mort)."),
        two("The $15 Bonnie paid the doctor is never deducted from John's money during the game.",
            "Les 15 $ que Bonnie a payés au médecin ne sont jamais prélevés sur l'argent de John au cours du jeu."),
        two("In the original release, when Amos passes Bonnie at the end of \"Old Friends, New Problems\", he says \"Ma'am\" while the subtitles read \"Howdy, miss\". The Game of the Year Edition fixed it.",
            "Dans la version d'origine, quand Amos croise Bonnie à la fin de \"Old Friends, New Problems\", il dit \"Ma'am\" alors que les sous-titres affichent \"Howdy, miss\". L'édition Game of the Year a corrigé l'erreur."),
        two("In Undead Nightmare, two of her lines are written as graffiti on walls in Blackwater: \"You do so love to talk in riddles\" and \"Civilization is truly a beautiful thing\".",
            "Dans Undead Nightmare, deux de ses répliques sont peintes en graffiti sur des murs de Blackwater : \"You do so love to talk in riddles\" et \"Civilization is truly a beautiful thing\"."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Bonnie became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. Players select her in the Redemption section of the Outfitter, alongside [[john-marston|John]], [[abigail-marston|Abigail]], [[jack-marston|Jack]], [[leigh-johnson|Leigh Johnson]], [[luisa-fortuna|Luisa Fortuna]], [[nigel-west-dickens|Nigel West Dickens]] and [[seth-briars|Seth Briars]]. The Red Dead Wiki lists 28 taunts for her model, a few of which are quoted above. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, do not include the multiplayer mode.",
              "Bonnie devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. On la choisit dans la section Redemption de l'Outfitter, aux côtés de [[john-marston|John]], d'[[abigail-marston|Abigail]], de [[jack-marston|Jack]], de [[leigh-johnson|Leigh Johnson]], de [[luisa-fortuna|Luisa Fortuna]], de [[nigel-west-dickens|Nigel West Dickens]] et de [[seth-briars|Seth Briars]]. Le Red Dead Wiki recense 28 provocations pour son modèle, dont quelques-unes sont citées plus haut. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, ne comprennent pas le multijoueur.")},
    {"h4": two("Marketing and merchandise", "Promotion et produits dérivés")},
    {"p": two("Rockstar released promotional images and artwork of Bonnie for Red Dead Redemption, and she appears on the back of the fold-out map packaged with the game. According to the Red Dead Wiki, her outfit could be bought for avatars in PlayStation Home, Sony's former online space on PlayStation 3. According to a Red Dead Wiki gallery caption, the Undead Nightmare trailer includes a shot of John and Bonnie embracing.",
              "Rockstar a diffusé des images promotionnelles et des illustrations de Bonnie pour Red Dead Redemption, et elle figure au dos de la carte dépliante fournie avec le jeu. D'après le Red Dead Wiki, sa tenue pouvait être achetée pour les avatars de PlayStation Home, l'ancien espace en ligne de Sony sur PlayStation 3. D'après une légende de la galerie du Red Dead Wiki, la bande-annonce d'Undead Nightmare contient un plan où John et Bonnie s'étreignent.")},
    {"h4": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
    {"p": two("In Red Dead Redemption 2 she is only mentioned: in the shipwreck survivor's letter and, in the 1907 epilogue, as away from her ranch (see Biography).",
              "Red Dead Redemption 2 ne fait que l'évoquer : dans la lettre du rescapé du naufrage et, pendant l'épilogue de 1907, par son absence du ranch (voir la biographie).")},
]
