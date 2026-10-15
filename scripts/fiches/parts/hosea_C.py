"""Hosea Matthews, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched 15 Oct 2026 via the MediaWiki API, saved in
scratchpad cov/hosea/, cov/hosea/m/, cov/arthur/m/, cov/dutch/dlg/, cov/micah/m/):
- Red Dead Wiki EN "Hosea Matthews" (infobox aliases, Mission appearances, Notable
  Murders Committed, Quotes, Trivia, Gallery captions) and FR "Hosea Matthews"
  (Apparitions dans les missions, Anecdotes).
- Mission pages: Outlaws from the West, Enter, Pursued by a Memory, Old Friends, Who
  the Hell is Leviticus Cornwall?, Eastward Bound, Exit Pursued by a Bruised Ego, The
  Spines of America, A Strange Kindness, The New South, Advertising, The New American
  Art, The Fine Joys of Tobacco, Blessed are the Peacemakers, Blood Feuds, Ancient and
  Modern, The Battle of Shady Belle, Angelo Bronte, A Man of Honor, The Gilded Cage,
  Horsemen, Apocalypses, Country Pursuits, Banking, The Old American Art, A Fork in the
  Road, Who is Not Without Sin.
- Transcripts "/dialogues": Outlaws from the West, Enter, Pursued by a Memory, Old
  Friends, Who the Hell is Leviticus Cornwall?, Eastward Bound, Exit Pursued by a
  Bruised Ego (page "/Dialogues"), The New South, Blessed are the Peacemakers, The
  Battle of Shady Belle, A Fisher of Men, Red Dead Redemption (mission). No transcript
  exists for Advertising, The Gilded Cage, Country Pursuits, Banking or A Fork in the
  Road: quotes from them come from the quote boxes of the mission or character pages.
- Other wiki pages: Camp Events, Errand Boy, The Case of the Deceitful German,
  Dominoes, Silver Dollar, Bessie Matthews, Saint Denis Robbers Still on the Run,
  Red Dead Redemption 2 Cut Content, Arthur's Journal (gang savings table).
- Real world: Wikipedia "List of Red Dead Redemption 2 characters" (Hosea section:
  Piggyback Complete Official Guide, 26 Oct 2018, pp. 28 and 370; CBR, Anastasia
  Owens, 8 Aug 2021; Game Informer, 27 Dec 2018); trailer dates and the 6 Sep 2018
  gang portraits as established in micah_C / arthur parts.
Excluded: the emphysema diagnosis (speculation), the Richard Sharpe / Obadiah
Hakeswill source (\"possibly based\"), the reading of his priest anecdote as a sign of
Jewish faith, the Hosea/Lenny vs Arthur/John parallel (fan analysis), the FR
\"Clint Eastwood traits\" comparison (unsourced), the claim that he killed the owner of
the Shire (the transcript only says \"you know how it is\"), the burial lines as
\"foreshadowing\", Micah's Guarma line in quotation marks (no transcript, paraphrased),
the Turkoman breed of Silver Dollar (file name only).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]
K = lambda name, mission, en, fr: [name, mission, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 21 story missions of Red Dead Redemption 2 for Hosea: 19 in which he appears, from the opening of chapter 1 to the Saint Denis bank robbery at the end of chapter 4, and two in chapter 6 in which only his voice is heard, as a memory. The French edition lists 18: it leaves out \"The Spines of America\" and the two voice-only appearances. The table follows the English list in story order. Hosea is never playable. He is the sole mission giver of three missions, \"Exit Pursued by a Bruised Ego\", \"The Spines of America\" and \"The Fine Joys of Tobacco\", and shares two: \"The Gilded Cage\" with Dutch and \"Advertising, The New American Art\" with Abigail.",
              "Le Red Dead Wiki anglais recense 21 missions principales de Red Dead Redemption 2 pour Hosea : 19 où il apparaît, du début du chapitre 1 au braquage de la banque de Saint-Denis à la fin du chapitre 4, et deux au chapitre 6 où l'on n'entend que sa voix, sous forme de souvenir. L'édition française en compte 18 : elle omet \"The Spines of America\" et les deux apparitions vocales. Le tableau suit la liste anglaise, dans l'ordre du récit. Hosea n'est jamais jouable. Il est le seul donneur de trois missions, \"Exit Pursued by a Bruised Ego\", \"The Spines of America\" et \"The Fine Joys of Tobacco\", et en partage deux : \"The Gilded Cage\" avec Dutch et \"Advertising, The New American Art\" avec Abigail.")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Hosea's role", "Rôle de Hosea")], "rows": [
        M("Outlaws from the West", C1,
          "Rides at the head of the wagons with [[dutch-van-der-linde|Dutch]] through the snowstorm and spots [[arthur-morgan|Arthur]] coming back from scouting. At Colter he checks an empty cabin, lantern and revolver in hand, and Davey Callander is carried inside, already dead. When Dutch returns from Adler Ranch, he helps [[sadie-adler|Sadie Adler]] down from Dutch's horse and sends [[micah-bell|Micah]] to bed.",
          "Mène les chariots avec [[dutch-van-der-linde|Dutch]] dans la tempête de neige et repère [[arthur-morgan|Arthur]] qui revient d'éclaireur. À Colter, il inspecte une cabane vide, lanterne et revolver à la main, puis Davey Callander y est porté, déjà mort. Au retour de Dutch depuis Adler Ranch, il aide [[sadie-adler|Sadie Adler]] à descendre du cheval de Dutch et envoie [[micah-bell|Micah]] se coucher."),
        M("Enter, Pursued by a Memory", C1,
          "When [[abigail-marston|Abigail]] begs Arthur to look for [[john-marston|John]], he tells Arthur to at least go and look, and asks [[javier-escuella|Javier]] to ride with him. He thanks both men on their return and, with [[leopold-strauss|Strauss]], explains that the gang will keep heading east once the weather breaks.",
          "Quand [[abigail-marston|Abigail]] supplie Arthur de partir à la recherche de [[john-marston|John]], il lui demande d'aller au moins jeter un œil et propose à [[javier-escuella|Javier]] de l'accompagner. Il remercie les deux hommes à leur retour et, avec [[leopold-strauss|Strauss]], annonce que le gang continuera vers l'est dès que le temps se calmera."),
        M("Old Friends", C1,
          "Stays at Colter with [[simon-pearson|Pearson]] and [[charles-smith|Charles]] while the others raid the O'Driscoll camp. He only appears in the opening and closing scenes, although the map shows an ally marker for him at the hideout.",
          "Reste à Colter avec [[simon-pearson|Pearson]] et [[charles-smith|Charles]] pendant que les autres attaquent le camp O'Driscoll. Il n'apparaît que dans les scènes d'ouverture et de fin, même si la carte affiche pour lui un marqueur allié au repaire."),
        M("Who the Hell is Leviticus Cornwall?", C1,
          "Objects to robbing the train: the weather is breaking, the plan was to lie low and go back west, and [[leviticus-cornwall|Leviticus Cornwall]] is a railway, sugar and oil magnate. Dutch goes ahead anyway and Hosea takes no part in the robbery.",
          "S'oppose à l'attaque du train : le temps se lève, le plan était de se faire oublier puis de repartir vers l'ouest, et [[leviticus-cornwall|Leviticus Cornwall]] est un magnat du rail, du sucre et du pétrole. Dutch passe outre et Hosea ne participe pas au braquage."),
        M("Eastward Bound", C1,
          "Proposes Horseshoe Overlook, near Valentine, as the new camp and rides there in Arthur's wagon. He helps Charles hold the wagon up while Arthur refits a wheel, tells them how the Wapiti lost the Heartlands, and gives Arthur yarrow and ginseng. On arrival he tells the gang to pose as itinerant workers and to start in Valentine.",
          "Propose Horseshoe Overlook, près de Valentine, comme nouveau camp et s'y rend dans le chariot d'Arthur. Il soulève le chariot avec Charles pendant qu'Arthur remonte une roue, raconte comment les Wapiti ont perdu les Heartlands et donne à Arthur de l'achillée et du ginseng. À l'arrivée, il demande au gang de se faire passer pour des ouvriers itinérants et de commencer par Valentine."),
        M("Exit Pursued by a Bruised Ego", C2,
          "Mission giver. Takes Arthur after a bear of about a thousand pounds near O'Creagh's Run, after a stop in Valentine to sell or stable a Shire. The bear charges; Arthur drives it off. Hosea then gives Arthur a map of legendary animals and returns to camp, with or without him.",
          "Donneur de mission. Emmène Arthur traquer un ours d'environ 450 kilos près d'O'Creagh's Run, après un détour par Valentine pour vendre ou mettre à l'écurie un Shire. L'ours charge et Arthur le fait fuir. Hosea lui offre ensuite une carte des animaux légendaires et rentre au camp, avec ou sans lui."),
        M("The Spines of America", C2,
          "Mission giver. Has to prove himself to Seamus, the fence at Emerald Ranch, by stealing a stagecoach, itself stolen, that Bob Crawford has bought and keeps at Carmody Dell. By day he distracts the Crawfords with a fake spinal treatment while Arthur loots the house; by night he drives the coach away. Seamus pays 300 dollars.",
          "Donneur de mission. Doit faire ses preuves auprès de Seamus, le receleur d'Emerald Ranch, en volant une diligence, elle-même volée, que Bob Crawford a achetée et garde chez lui, à Carmody Dell. De jour, il occupe les Crawford avec un faux traitement de la colonne vertébrale pendant qu'Arthur pille la maison ; de nuit, c'est lui qui emmène la diligence. Seamus paie 300 dollars."),
        M("A Strange Kindness", C2,
          "Can be heard arguing with Dutch about the gang's violence just before the mission begins; he has no part in the mission itself, given by Dutch.",
          "On l'entend reprocher à Dutch la violence du gang juste avant le début de la mission ; il ne joue aucun rôle dans la mission elle-même, confiée par Dutch."),
        M("The New South", C3,
          "Leads Dutch and Arthur from Clemens Point toward a fishing spot. When [[josiah-trelawny|Trelawny]] is freed in Rhodes, Dutch tells Hosea to find out about the Braithwaites. If Arthur agrees, the three fish together on Flat Iron Lake.",
          "Conduit Dutch et Arthur de Clemens Point vers un coin de pêche. Une fois [[josiah-trelawny|Trelawny]] libéré à Rhodes, Dutch charge Hosea de se renseigner sur les Braithwaite. Si Arthur accepte, les trois hommes pêchent ensemble sur le lac Flat Iron."),
        M("Advertising, The New American Art", C3,
          "Mission giver with Abigail. Sells the stolen moonshine back to [[catherine-braithwaite|Catherine Braithwaite]] as lost goods, then agrees to hand it out free in the Grays' saloon for 10 dollars more. In Rhodes he and Arthur play two brothers, Melvin and Fenton. Lemoyne Raiders break up the evening; the two shoot their way out and escape by wagon.",
          "Donneur de mission avec Abigail. Revend à [[catherine-braithwaite|Catherine Braithwaite]] le moonshine volé en le présentant comme une marchandise retrouvée, puis accepte de le distribuer gratuitement dans le saloon des Gray contre 10 dollars de plus. À Rhodes, Arthur et lui jouent deux frères, Melvin et Fenton. Des Lemoyne Raiders interrompent la soirée ; les deux hommes se frayent un chemin à coups de feu et fuient en chariot."),
        M("The Fine Joys of Tobacco", C3,
          "Mission giver. Plays cribbage with Catherine Braithwaite at her manor and vouches for Arthur, then stays to negotiate while Arthur and [[sean-macguire|Sean]] burn the Grays' tobacco fields.",
          "Donneur de mission. Joue au cribbage avec Catherine Braithwaite dans son manoir et se porte garant d'Arthur, puis reste négocier pendant qu'Arthur et [[sean-macguire|Sean]] incendient les champs de tabac des Gray."),
        M("Blessed are the Peacemakers", C3,
          "Calls Colm O'Driscoll's offer of a parley a trap. Micah, who gives the mission, persuades Dutch to go.",
          "Qualifie de piège la rencontre proposée par Colm O'Driscoll. Micah, qui donne la mission, convainc Dutch d'y aller."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Joins the assault on Braithwaite Manor to get Jack back. He enters the house with Dutch, takes part in setting it on fire and questions Catherine, who says Jack is with Angelo Bronte in Saint Denis or on a boat to Italy.",
          "Participe à l'assaut de Braithwaite Manor pour récupérer Jack. Il entre dans la maison avec Dutch, prend part à l'incendie et interroge Catherine, qui affirme que Jack est chez Angelo Bronte à Saint-Denis ou sur un bateau pour l'Italie."),
        M("The Battle of Shady Belle", C3,
          "Tries with Dutch to reassure John about Jack, and is at Clemens Point when [[andrew-milton|Agent Milton]] and [[edgar-ross|Edgar Ross]] arrive to offer the gang amnesty in exchange for Dutch.",
          "Tente avec Dutch de rassurer John au sujet de Jack, et se trouve à Clemens Point quand [[andrew-milton|l'agent Milton]] et [[edgar-ross|Edgar Ross]] viennent proposer l'amnistie au gang en échange de Dutch."),
        M("Angelo Bronte, A Man of Honor", C4,
          "Present at the party at Shady Belle for [[jack-marston|Jack]]'s return. Beside the fountain he jokes with Jack about the boy's stay at [[angelo-bronte|Bronte]]'s mansion.",
          "Présent à la fête donnée à Shady Belle pour le retour de [[jack-marston|Jack]]. Près de la fontaine, il plaisante avec l'enfant sur son séjour chez [[angelo-bronte|Bronte]]."),
        M("The Gilded Cage", C4,
          "Mission giver with Dutch. Tells Arthur they need proper clothes for the occasion, rides to Mayor Lemieux's garden party with Dutch, Arthur and [[bill-williamson|Bill]] in a coach driven by [[lenny-summers|Lenny]], and works the guests for a new target. He comes back with a lead on the Saint Denis bank.",
          "Donneur de mission avec Dutch. Annonce à Arthur qu'il leur faut une tenue convenable pour l'occasion, se rend à la garden-party du maire Lemieux avec Dutch, Arthur et [[bill-williamson|Bill]] dans une voiture conduite par [[lenny-summers|Lenny]], et sonde les invités à la recherche d'une nouvelle cible. Il en revient avec une piste sur la banque de Saint-Denis."),
        M("Horsemen, Apocalypses", C4,
          "Defends Shady Belle when the O'Driscolls attack the camp.",
          "Défend Shady Belle quand les O'Driscoll attaquent le camp."),
        M("Country Pursuits", C4,
          "Argues against Dutch's plan to go after Bronte, calling it unnecessary and risky. Arthur sides with Dutch, and Hosea warns Dutch that he will damn them all.",
          "S'oppose au projet de Dutch de s'en prendre à Bronte, qu'il juge inutile et risqué. Arthur se range du côté de Dutch, et Hosea prévient ce dernier qu'il va tous les perdre."),
        M("Banking, The Old American Art", C4,
          "Convinces a hesitant Dutch that the job is well planned, then sets off the diversion with Abigail. Captured by Agent Milton, he is held in the street outside the bank and shot in the chest.",
          "Convainc Dutch, qui hésite, que le coup est bien préparé, puis déclenche la diversion avec Abigail. Capturé par l'agent Milton, il est retenu dans la rue devant la banque et abattu d'une balle dans la poitrine."),
        M("A Fork in the Road (voice only)", C6,
          "Heard in Arthur's memories after the doctor's diagnosis. With high Honor, Arthur hears the snowstorm line from \"Outlaws from the West\", although Hosea said it to Dutch while Arthur was away scouting; with low Honor, he hears the line about the gang turning into killers.",
          "Entendu dans les souvenirs d'Arthur après le diagnostic du médecin. Avec un honneur élevé, Arthur entend la réplique sur la tempête de neige de \"Outlaws from the West\", que Hosea avait pourtant dite à Dutch pendant qu'Arthur était parti en éclaireur ; avec un honneur bas, il entend celle sur le gang devenu une bande de tueurs."),
        M("Red Dead Redemption (voice only)", C6,
          "Heard again in Arthur's memories during his last ride. With high Honor, the line is his plea against more deaths; with low Honor, Arthur hears the remark about staring into the fire, a line about thinking themselves above the law and morality, and the warning from \"Country Pursuits\".",
          "De nouveau entendu dans les souvenirs d'Arthur lors de sa dernière chevauchée. Avec un honneur élevé, c'est sa supplique contre de nouvelles morts ; avec un honneur bas, Arthur entend la phrase sur le feu, une remarque sur le fait de s'être crus au-dessus de la loi et de la morale, et l'avertissement de \"Country Pursuits\"."),
    ]}},
    # ---------------------------------------------------------- notable kills
    {"h3": two("Notable people Hosea kills", "Personnages notables tués par Hosea")},
    {"p": two("Hosea avoids violence when he can, and the Red Dead Wiki credits him with only two notable killings, both in chapter 3. The table adds the Crawfords, whom he can kill in \"The Spines of America\" if the robbery goes wrong. Unnamed enemies killed in gunfights, such as the Lemoyne Raiders who chase the wagon out of Rhodes, are not listed one by one.",
              "Hosea évite la violence autant que possible, et le Red Dead Wiki ne lui attribue que deux meurtres notables, tous deux au chapitre 3. Le tableau y ajoute les Crawford, qu'il peut tuer dans \"The Spines of America\" si le vol tourne mal. Les ennemis anonymes abattus pendant les fusillades, comme les Lemoyne Raiders qui poursuivent le chariot à la sortie de Rhodes, ne sont pas détaillés.")},
    {"table": {"head": [two("Name", "Nom"), two("Mission", "Mission"), two("Circumstances", "Circonstances")], "rows": [
        K(two("Lemoyne Raider", "Lemoyne Raider"), "Advertising, The New American Art",
          "Storyline. During the saloon fight in Rhodes, a Raider throws Hosea off the balcony. Hosea draws as he lands and shoots him in self-defence.",
          "Histoire. Pendant la bagarre du saloon de Rhodes, un Raider jette Hosea du haut de la galerie. Hosea dégaine en touchant le sol et l'abat en état de légitime défense."),
        K(two("A Braithwaite", "Un Braithwaite"), "Blood Feuds, Ancient and Modern",
          "Storyline. Burned alive while the gang sets Braithwaite Manor on fire.",
          "Histoire. Brûlé vif pendant que le gang incendie Braithwaite Manor."),
        K(two("Bob Crawford Sr. and Bob Crawford Jr.", "Bob Crawford père et fils"), "The Spines of America",
          "Determinant. Either Crawford can be killed by Arthur or by Hosea; if they catch Arthur and he does not fight back, they kill Hosea and the mission fails.",
          "Selon le joueur. Chacun des deux Crawford peut être tué par Arthur ou par Hosea ; s'ils surprennent Arthur et qu'il ne riposte pas, ce sont eux qui tuent Hosea, et la mission échoue."),
    ]}},
]

BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent.")},
    {"h4": two("Red Dead Redemption 2, chapters 1 and 2", "Red Dead Redemption 2, chapitres 1 et 2")},
    {"quotes": [
        {"q": two("If we don't stop soon, we'll all be dying. This weather, it's May... I'm just hoping the law got as lost as we did.",
                  "If we don't stop soon, we'll all be dying. This weather, it's May... I'm just hoping the law got as lost as we did."),
         "src": two("Outlaws from the West (RDR2, chapter 1), to Dutch, in the snowstorm; his first line in the game",
                    "Outlaws from the West (RDR2, chapitre 1), à Dutch, dans la tempête de neige ; sa première réplique du jeu. Traduction : « Si on ne s'arrête pas bientôt, on va tous y passer. Ce temps, en mai... J'espère juste que la loi s'est perdue autant que nous. »")},
        {"q": two("I know...the west is where our problems are worse.",
                  "I know...the west is where our problems are worse."),
         "src": two("Enter, Pursued by a Memory (RDR2, chapter 1), to Arthur, who is worried about heading east toward civilization",
                    "Enter, Pursued by a Memory (RDR2, chapitre 1), à Arthur, inquiet de partir vers l'est et la civilisation. Traduction : « Je sais... c'est à l'ouest que nos ennuis sont les pires. »")},
        {"q": two("Poor bastards... we really screwed them over down here. Come on, let's not push our luck.",
                  "Poor bastards... we really screwed them over down here. Come on, let's not push our luck."),
         "src": two("Eastward Bound (RDR2, chapter 1), to Arthur and Charles, about the Native riders watching them from a cliff",
                    "Eastward Bound (RDR2, chapitre 1), à Arthur et Charles, à propos des cavaliers amérindiens qui les observent depuis une falaise. Traduction : « Les pauvres... on les a vraiment roulés, par ici. Allez, ne tentons pas le sort. »")},
        {"q": two("There is a town a little way down the track... name of Valentine... live stock town. All mud and morons if I remember right.",
                  "There is a town a little way down the track... name of Valentine... live stock town. All mud and morons if I remember right."),
         "src": two("Eastward Bound (RDR2, chapter 1), to the whole gang, gathered by Dutch at the new camp",
                    "Eastward Bound (RDR2, chapitre 1), à tout le gang, rassemblé par Dutch au nouveau camp. Traduction : « Il y a une ville un peu plus bas sur la piste... elle s'appelle Valentine... une ville de bétail. Rien que de la boue et des crétins, si j'ai bonne mémoire. »")},
        {"q": two("Truth is, there's never really any getting out, and staying in… it's hard, you know that, but Bessie and I made it work.",
                  "Truth is, there's never really any getting out, and staying in… it's hard, you know that, but Bessie and I made it work."),
         "src": two("Exit Pursued by a Bruised Ego (RDR2, chapter 2), to Arthur, who asks whether he and Bessie ever thought of leaving the outlaw life",
                    "Exit Pursued by a Bruised Ego (RDR2, chapitre 2), à Arthur, qui lui demande si Bessie et lui ont songé à quitter la vie de hors-la-loi. Traduction : « La vérité, c'est qu'on n'en sort jamais vraiment, et rester dedans... c'est dur, tu le sais, mais Bessie et moi, on s'en est accommodés. »")},
    ]},
    {"h4": two("Red Dead Redemption 2, chapters 3 and 4", "Red Dead Redemption 2, chapitres 3 et 4")},
    {"quotes": [
        {"q": two("My days of looking good are long over, Dutch.",
                  "My days of looking good are long over, Dutch."),
         "src": two("The New South (RDR2, chapter 3), to Dutch, who tells him he does not look well",
                    "The New South (RDR2, chapitre 3), à Dutch, qui lui trouve mauvaise mine. Traduction : « Ça fait longtemps que je n'ai plus bonne mine, Dutch. »")},
        {"q": two("We're in the new trade of advertising, which is an American art form about ensuring people buy the correct things. One more dollar says give us half an hour, what harm can we do in half an hour?",
                  "We're in the new trade of advertising, which is an American art form about ensuring people buy the correct things. One more dollar says give us half an hour, what harm can we do in half an hour?"),
         "src": two("Advertising, The New American Art (RDR2, chapter 3), to the staff of the Rhodes Parlour House",
                    "Advertising, The New American Art (RDR2, chapitre 3), au personnel du Rhodes Parlour House. Traduction : « Nous travaillons dans un métier nouveau, la publicité, un art américain qui consiste à s'assurer que les gens achètent les bonnes choses. Un dollar de plus pour une demi-heure : quel mal pourrait-on faire en une demi-heure ? »")},
        {"q": two("They want a parley? It's a trap.",
                  "They want a parley? It's a trap."),
         "src": two("Blessed are the Peacemakers (RDR2, chapter 3), to Dutch and Micah, about Colm O'Driscoll's offer",
                    "Blessed are the Peacemakers (RDR2, chapitre 3), à Dutch et Micah, à propos de l'offre de Colm O'Driscoll. Traduction : « Ils veulent parlementer ? C'est un piège. »")},
    ]},
    {"h4": two("Camp lines", "Répliques de camp")},
    {"quotes": [
        {"q": two("Anyway, I got caught by some hill country sheriff, stealing a chicken I think it was... And he decided I was going to be hanged for it.",
                  "Anyway, I got caught by some hill country sheriff, stealing a chicken I think it was... And he decided I was going to be hanged for it."),
         "src": two("Camp (RDR2), to the gang around the campfire",
                    "Au camp (RDR2), au gang réuni autour du feu. Traduction : « Bref, un shérif de l'arrière-pays m'a pris en train de voler, une poule je crois... Et il a décidé que j'allais être pendu pour ça. »")},
        {"q": two("My Pa used to say if you stare into the fire long enough, you can see the whole world pass by.",
                  "My Pa used to say if you stare into the fire long enough, you can see the whole world pass by."),
         "src": two("Camp (RDR2), during a campfire conversation",
                    "Au camp (RDR2), lors d'une conversation au coin du feu. Traduction : « Mon père disait que si on fixe le feu assez longtemps, on voit le monde entier défiler. »")},
    ]},
]

BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Story and characters", "Histoire et personnages")},
    {"ul": [
        two("His first lines in \"Outlaws from the West\", spoken in a snowstorm, include the words \"it's May\".",
            "Ses premières répliques dans \"Outlaws from the West\", en pleine tempête de neige, contiennent les mots \"it's May\" (on est en mai)."),
        two("The subtitles of the opening scene of \"The Battle of Shady Belle\" misspell his surname as \"Mathews\" when Milton addresses him.",
            "Dans la scène d'ouverture de \"The Battle of Shady Belle\", les sous-titres orthographient son nom \"Mathews\" quand Milton s'adresse à lui."),
    ]},
    {"h4": two("Gameplay", "Jeu")},
    {"ul": [
        two("Hosea almost never takes a turn on watch at camp; he is most likely to be found on guard in chapter 2, before any mission of the chapter has been started. From \"Eastward Bound\" onward, if Arthur keeps talking to him, Hosea can send him off to pester Uncle instead.",
            "Hosea ne prend presque jamais son tour de garde au camp ; c'est au chapitre 2, avant d'avoir lancé la moindre mission du chapitre, qu'on a le plus de chances de l'y trouver. À partir de \"Eastward Bound\", si Arthur insiste pour lui parler, Hosea peut l'envoyer importuner Uncle à sa place."),
        two("Hosea leaves camp while some of the missions he appears in are available: during \"Exit Pursued by a Bruised Ego\", \"The Spines of America\" and \"A Strange Kindness\" in chapter 2, \"Advertising, The New American Art\" and \"The Fine Joys of Tobacco\" in chapter 3, and \"The Gilded Cage\", \"Country Pursuits\" and the bank robbery in chapter 4. His camp interactions end for good once \"Banking, The Old American Art\" is unlocked.",
            "Hosea quitte le camp tant que certaines des missions où il apparaît sont disponibles : \"Exit Pursued by a Bruised Ego\", \"The Spines of America\" et \"A Strange Kindness\" au chapitre 2, \"Advertising, The New American Art\" et \"The Fine Joys of Tobacco\" au chapitre 3, puis \"The Gilded Cage\", \"Country Pursuits\" et le braquage de la banque au chapitre 4. Ses interactions de camp cessent définitivement une fois \"Banking, The Old American Art\" débloquée."),
        two("In \"Exit Pursued by a Bruised Ego\", Hosea's opening lines change depending on whether \"Americans at Rest\" or \"A Quiet Time\" has been completed, and he comments differently on each horse Arthur can buy. He recalls a saddle stolen outside a saloon in Deer Creek, and smokes a cigar while Arthur tracks the bear.",
            "Dans \"Exit Pursued by a Bruised Ego\", les premières répliques de Hosea varient selon que \"Americans at Rest\" ou \"A Quiet Time\" a été terminée, et il commente différemment chaque cheval qu'Arthur peut acheter. Il évoque une selle volée devant un saloon de Deer Creek et fume un cigare pendant qu'Arthur suit la piste de l'ours."),
        two("In \"The Spines of America\", Hosea complains if Arthur skips the house and goes straight for the coach, and he is disappointed if Arthur watches the spinal treatment instead of looting. Staying in the house afterwards lets the player hear the Crawfords talk about the massage.",
            "Dans \"The Spines of America\", Hosea râle si Arthur délaisse la maison pour filer droit vers la diligence, et il se montre déçu si Arthur assiste au massage au lieu de piller. En restant dans la maison ensuite, le joueur entend les Crawford parler de la séance."),
        two("Hosea's body can be looted in front of the bank in \"Banking, The Old American Art\" by climbing over a gate. It carries only ordinary items, and looting it costs a significant amount of Honor.",
            "Le corps de Hosea peut être fouillé devant la banque dans \"Banking, The Old American Art\", en escaladant une grille. Il ne porte que des objets ordinaires, et le fouiller coûte beaucoup d'honneur."),
    ]},
    {"h4": two("References", "Références")},
    {"ul": [
        two("The Aldous Filson novels he reads parody Arthur Conan Doyle's Sherlock Holmes stories. According to the Red Dead Wiki, The Case of the Deceitful German may mirror A Scandal in Bohemia (1891), the first story in which Holmes is outwitted by a woman; in the novel, the German baron turns out to be a woman in disguise.",
            "Les romans d'Aldous Filson qu'il lit parodient les aventures de Sherlock Holmes d'Arthur Conan Doyle. Selon le Red Dead Wiki, The Case of the Deceitful German pourrait faire écho à Un scandale en Bohême (1891), première nouvelle où Holmes se fait déjouer par une femme ; dans le roman, le baron allemand se révèle être une femme déguisée."),
    ]},
]

BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("The second trailer, released on September 28, 2017, includes a shot of Bill, Hosea and Arthur outside the burning Braithwaite Manor. The third trailer, released on May 2, 2018, shows him bareheaded beside Dutch. Promotional artwork shows him holding a lantern, between Dutch and Arthur. On September 6, 2018, Hosea was among the 23 gang members whose portraits Rockstar posted on Twitter; the composite of the series places him in the back row, between John and Charles. His description on the gang page of the official website is quoted under Personality.",
              "La deuxième bande-annonce, publiée le 28 septembre 2017, montre Bill, Hosea et Arthur devant Braithwaite Manor en flammes. La troisième, publiée le 2 mai 2018, le montre tête nue aux côtés de Dutch. Une illustration promotionnelle le représente une lanterne à la main, entre Dutch et Arthur. Le 6 septembre 2018, Hosea figure parmi les 23 membres du gang dont Rockstar publie le portrait sur Twitter ; la composition réunissant la série le place au dernier rang, entre John et Charles. Sa description sur la page du gang du site officiel est citée dans la partie Personnalité.")},
    {"p": two("Red Dead Redemption 2: The Complete Official Guide, published by Piggyback on October 26, 2018, describes him on page 28 and gives him a profile on page 370.",
              "Le guide officiel de Piggyback, Red Dead Redemption 2: The Complete Official Guide, paru le 26 octobre 2018, le décrit en page 28 et lui consacre une fiche en page 370.")},
    {"h4": two("In the game world", "Dans l'univers du jeu")},
    {"p": two("After the bank robbery, the newspaper article \"Saint Denis Robbers Still on the Run\" reports that two gang members were killed, Lenny Summers, nineteen, and Hosea Matthews, believed to be about 55. It adds that their bodies were never found during the cleanup and that Hosea was wanted in at least six states. In \"Red Dead Redemption\", the last mission of chapter 6, as he and Sadie ride to rescue Abigail, Arthur lists the people they have lost and says they have to put an end to this. With high Honor the list begins \"John, Hosea, Mac\"; with low Honor it begins with Hosea and ends \"now John\". In both versions he then adds Eagle Flies. John is in fact alive: Arthur believes him dead because Dutch and Micah told him so. Arthur's journal also contains a drawing of Hosea.",
              "Après le braquage, l'article \"Saint Denis Robbers Still on the Run\" annonce la mort de deux membres du gang, Lenny Summers, 19 ans, et Hosea Matthews, qui aurait environ 55 ans. Il précise que leurs corps n'ont jamais été retrouvés lors du déblaiement et que Hosea était recherché dans au moins six États. Dans \"Red Dead Redemption\", dernière mission du chapitre 6, alors qu'il chevauche avec Sadie pour libérer Abigail, Arthur énumère ceux qu'ils ont perdus et dit qu'il faut mettre un terme à tout cela. Avec un honneur élevé, la liste commence par \"John, Hosea, Mac\" ; avec un honneur bas, elle s'ouvre sur Hosea et se termine par \"now John\" (et maintenant John). Dans les deux cas, il ajoute ensuite Eagle Flies. John est pourtant vivant : Arthur le croit mort parce que Dutch et Micah le lui ont dit. Le journal d'Arthur contient aussi un dessin de Hosea.")},
    {"h4": two("Press and appearances", "Presse et apparitions")},
    {"p": two("On August 8, 2021, CBR published a feature by Anastasia Owens titled \"Red Dead Redemption 2: Hosea Matthews, Explained\", covering among other things his marriage to Bessie and his death. Press rankings that mention him are given under Reception. Curzon Dobell, his performer, was among the guests of SacAnime Summer 2019 in Sacramento (June 7 to 9, 2019), as were Roger Clark, Rob Wiethoff, Alex McKenna, Peter Blomquist and Steve J. Palmer.",
              "Le 8 août 2021, CBR publie un article d'Anastasia Owens intitulé \"Red Dead Redemption 2: Hosea Matthews, Explained\", qui revient notamment sur son mariage avec Bessie et sur sa mort. Les classements de presse qui le citent figurent dans la partie Accueil. Curzon Dobell, son interprète, figure parmi les invités de la SacAnime de l'été 2019, à Sacramento (du 7 au 9 juin 2019), tout comme Roger Clark, Rob Wiethoff, Alex McKenna, Peter Blomquist et Steve J. Palmer.")},
]
