"""Irish, part B: Personality (official description, observable traits, In his own words, Names, Appearance),
Contraband, weapons and horses (the fiche-specific skills section), Relationships (21 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN sections Personality and Appearance, the Rockstar quote box, the infobox (aka, weapon,
family, affiliations, occupation, location), the trivia items on his revolver carry, his invulnerability before
missions, killing him after his last mission, his travels, his parents, the nuns, swimming, El Rato, Ricketts and the
colonel, plus the pages "Alwyn Lloyd", "Leander Holland", "Shaky", "Irish/Quotes" and the mission pages listed in
irish/missions.txt. Narrative events are told in part A; entries below point to them.

SOURCE REGISTER (read 21 Oct 2026; wiki cache scripts/v3/work/_m/):
- Official description: the quote box of the Red Dead Wiki EN page "Irish" ("A teller of tall tales, who'll try to talk
  his way out of anything.", labelled "Rockstar's description of Irish"). The original Rockstar page was not found
  (Wayback search timed out): quoted through the wiki, attributed. Rockstar's 6 Sep 2018 descriptions
  (sources/thr_descriptions.txt) cover the RDR2 gang only: none for Irish. No Game of the Year guide description of
  Irish is quoted by the wiki.
- Transcripts (wiki "/dialogues" pages, every quoted line checked): "A Frenchman, a Welshman and an Irishman",
  "Man is Born Unto Trouble", "On Shaky's Ground", "The Assault on Fort Mercer", "We Shall Be Together in Paradise",
  "Liars, Cheats and Other Proud Americans" (Dickens introduces Irish).
- Quote page "Irish/Quotes" (_m/Irish_Quotes.txt): ride conversations 2 to 4 and 8 of "A Frenchman, a Welshman and an
  Irishman" that are not in the transcript ("Life's too short for regrets...", the tonic and the "back-door trots",
  the invitation to Armadillo); used paraphrased except where stated.
- Mission pages: failure conditions (assaulting, killing or abandoning Irish; killing his horse) on the four New Austin
  missions; "We Shall Be Together in Paradise" (only mission he fights in, with a Cattleman Revolver; failure if the
  rope of the raft is shot; killing him right after the mission; the revolver tucked into his trousers);
  "On Shaky's Ground" (he drives the wagon, failure if Shaky is assaulted or killed).
- Other wiki pages: "Alwyn Lloyd" (Welsh; his real name printed in Blackwater Ledger No. 56, checked in
  _m/Blackwater_Ledger_No_56.txt: "Alwyn Lloyd, believed to be of Welsh origin, died by gunshot in Armadillo"),
  "Leander Holland" (French; real name not found in a newspaper: wiki-only), "Shaky".
- FR Red Dead Wiki "L'Irlandais" (fc/web_notes_BD.txt): the name the French wiki gives him.
- Visual check: the live portrait.jpeg for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only: the Rockstar description; "It's the whiskey, sir...", "Life's too short for regrets...",
  "Team work, Johnny boy...", "I came into this world fightin'...", "You know me, Johnny boy. I'll be late to me own
  funeral..." (In his own words); "Down here, they call me El Rato...", "I'm pretty sure Rato means..." (Names).
  Part C Quotes must not repeat these.
- Relationship entries paraphrase lines without quotation marks; part C Quotes keeps the verbatim versions (the
  hypocrite exchange, the parting words to John, the morphine pills, the Dickens tonic, "pissin' your pants").
- Gameplay (failure conditions, invulnerability before missions, killing him after his last mission, the raft rope,
  the revolver carry) lives HERE; part C Trivia must not repeat it.
- Told once elsewhere, pointer here: every mission event (A), his father, mother, brother's wife and the boat crossing
  (A Origins), the Fort Mercer absence and his excuse (A and C Quotes).

WIKI-ONLY (kept, attributed): the Rockstar description (quote box); the Cattleman Revolver and Repeater Carbine
(infobox); that he cannot swim (trivia; no transcript line); that he shoots back or flees and cannot be killed if
attacked before a mission (trivia); that he can be killed right after "We Shall Be Together in Paradise" with Dead Eye
(trivia); the revolver carried in the front of his trousers (trivia and mission page; visible on the portrait); Leander
Holland as French's real name; the identification of the American in Chuparosa as Landon Ricketts and of the colonel
as Agustin Allende (the game names neither); the brother's wife (no transcript; pointer only).

Excluded: "dysfunctional alcoholic", "lazy drunk and a coward" and "regular problem for the people he was around"
as our own words (wiki interpretation; facts given instead, John's insults paraphrased as his); "possibly" slit by a
Welshman (the transcript only says his father warned him and had his throat slit); Dublin or Cork as his birthplace
(wiki "may be" from "west of Dublin" and "shitehawk": speculation); "well-travelled" to Mexico and Canada as fact (his
claims, told as claims); "just barely more well-dressed than Seth" (comparison); the Uncle comparison (wiki trivia:
interpretation); the "attempts to get John Marston killed" reason for the Damnation category (wiki "most likely");
"Twinkle-Toe Dave" (wiki background, no transcript: left to A, not repeated here).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "The Red Dead Wiki quotes a description of the character by Rockstar: \"A teller of tall tales, who'll try to talk his way out of anything.\" Wikipedia's summary of Red Dead Redemption calls him an alcoholic arms smuggler. In his missions, John finds him drunk or passed out more often than sober, and he blames his poor memory on whiskey. He forgets John's name, or pretends to, between two missions.",
        "Le Red Dead Wiki cite une description du personnage signée Rockstar : \"A teller of tall tales, who'll try to talk his way out of anything.\" (un raconteur d'histoires à dormir debout, qui tentera de se tirer de n'importe quelle situation à force de baratin). Le résumé de Red Dead Redemption sur Wikipédia le présente comme un trafiquant d'armes alcoolique. Dans ses missions, John le trouve plus souvent ivre ou assommé par l'alcool qu'à jeun, et Irish met ses trous de mémoire sur le compte du whisky. D'une mission à l'autre, il oublie le nom de John, ou fait semblant.")},
    {"p": two(
        "He avoids danger whenever he can. He offers to cover John from a ridge, says the mines play havoc with his sinuses, and volunteers to fetch the wagon while John goes in. In the only fight he takes part in, on the river, he shoots back and calls out where the attackers are. He boasts of contacts and friends who turn out to be hostile, and admits his memories of Mexico are blurred by drink. His speech is full of Irish turns of phrase (me for my, feck, shite) and of colorful comparisons. He calls John Johnny, Johnny boy, fella, dovey or smiler.",
        "Il fuit le danger dès qu'il le peut. Il propose de couvrir John depuis une crête, prétend que les mines lui ravagent les sinus, et se porte volontaire pour aller chercher le chariot pendant que John entre. Dans le seul combat auquel il prend part, sur le fleuve, il riposte et signale à John la position des assaillants. Il se vante de relations et d'amis qui se révèlent hostiles, et reconnaît que ses souvenirs du Mexique sont noyés dans l'alcool. Il parle avec des tournures irlandaises (me pour my, feck, shite) et des comparaisons imagées. Il appelle John Johnny, Johnny boy, fella, dovey ou smiler.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "Woken up in Benedict Point, in \"Man is Born Unto Trouble\", he explains his lapses: \"It's the whiskey, sir... It gives me the memory of a new born babe. As innocent as can be.\" On the two men who were drowning him, in \"A Frenchman, a Welshman and an Irishman\": \"Life's too short for regrets... and I'd outgrown them fools.\" On the wagon out of Thieves' Landing, in \"On Shaky's Ground\", when John points out that he missed the shooting: \"Someone's gotta drive the wagon, don't they? Team work, Johnny boy. That's my game. Not just the glory, like you.\"",
        "Réveillé à Benedict Point, dans \"Man is Born Unto Trouble\", il explique ses absences : \"It's the whiskey, sir... It gives me the memory of a new born babe. As innocent as can be.\" (c'est le whisky, monsieur, il me donne la mémoire d'un nouveau-né, innocent comme l'agneau). Sur les deux hommes qui le noyaient, dans \"A Frenchman, a Welshman and an Irishman\" : \"Life's too short for regrets... and I'd outgrown them fools.\" (la vie est trop courte pour les regrets, et ces imbéciles, je les avais dépassés). Sur le chariot qui quitte Thieves' Landing, dans \"On Shaky's Ground\", quand John lui fait remarquer qu'il a raté la fusillade : \"Someone's gotta drive the wagon, don't they? Team work, Johnny boy. That's my game. Not just the glory, like you.\" (il faut bien que quelqu'un conduise le chariot, non ? L'esprit d'équipe, Johnny, c'est ça mon truc. Pas seulement la gloire, comme toi).")},
    {"p": two(
        "On the raft, in \"We Shall Be Together in Paradise\": \"You know me, Johnny boy. I'll be late to me own funeral. They said God invented whiskey to stop the Irish from rulin' the world.\" Under fire a few minutes later: \"I came into this world fightin'. And I'll go out of it fightin'!\"",
        "Sur le radeau, dans \"We Shall Be Together in Paradise\" : \"You know me, Johnny boy. I'll be late to me own funeral. They said God invented whiskey to stop the Irish from rulin' the world.\" (tu me connais, Johnny, je serai en retard à mon propre enterrement. On dit que Dieu a inventé le whisky pour empêcher les Irlandais de gouverner le monde). Sous les balles, quelques minutes plus tard : \"I came into this world fightin'. And I'll go out of it fightin'!\" (je suis venu au monde en me battant, et je le quitterai en me battant !).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Irish is a nickname, and the game never gives him another name. Wikipedia lists him as Irish, and Nigel West Dickens calls him Mr. Irish. When he sings to himself in Benedict Point, he calls himself Uncle Irish. Welsh and French insult him as a paddy and a mick. On the raft he claims that in Mexico he is known as El Rato: \"Down here, they call me El Rato. The cat. On account of me stealth and cunning.\" John corrects him: \"I'm pretty sure Rato means \"rat,\" my friend.\" John adds that he likes it, as it is a little more inventive than Irish. The 1914 newspaper notice that the Red Dead Wiki attributes to him describes an Irish man of unknown name (see Biography). According to the French-language Red Dead Wiki, the French version of the game calls him l'Irlandais.",
        "Irish est un surnom, et le jeu ne lui en donne jamais d'autre. Wikipédia le désigne sous ce nom, et Nigel West Dickens l'appelle Mr. Irish. Quand il chantonne tout seul à Benedict Point, il se surnomme lui-même Uncle Irish (tonton Irish). Welsh et French l'insultent en le traitant de paddy et de mick, deux sobriquets méprisants pour les Irlandais. Sur le radeau, il affirme qu'au Mexique on l'appelle El Rato : \"Down here, they call me El Rato. The cat. On account of me stealth and cunning.\" (par ici, on m'appelle El Rato, le chat, à cause de ma discrétion et de ma ruse). John le reprend : \"I'm pretty sure Rato means \"rat,\" my friend.\" (je suis à peu près sûr que Rato veut dire rat, mon ami). Il ajoute que le surnom lui plaît, un peu plus inventif qu'Irish. L'avis de décès de 1914 que le Red Dead Wiki lui attribue parle d'un Irlandais dont le nom est inconnu (voir la biographie). D'après le Red Dead Wiki francophone, la version française du jeu le nomme l'Irlandais.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He has long, shaggy dark hair and a thick dark beard. He wears a worn, pale shirt with rolled-up sleeves over his trousers. He carries his revolver tucked into the front of his trousers rather than in a holster, as the Red Dead Wiki and the mission page of \"We Shall Be Together in Paradise\" note.",
        "Il a de longs cheveux bruns en bataille et une épaisse barbe sombre. Il porte une chemise pâle et usée, manches retroussées, sur son pantalon. Il glisse son revolver à l'avant de son pantalon plutôt que dans un étui, comme le relèvent le Red Dead Wiki et la page de la mission \"We Shall Be Together in Paradise\".")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Suggested section title for the module: "Contraband, weapons and horses" / "Contrebande, armes et chevaux".
BLOCKS_SKILLS = [
    {"h4": two("Contraband and contacts", "Contrebande et contacts")},
    {"p": two(
        "Nigel West Dickens presents him as the man who can supply the firepower for Fort Mercer. Irish says he knows guns front, back and sideways, and the Red Dead Wiki lists his occupation as contraband dealer. His Thieves' Landing contact, Shaky, provides the ammunition for the Gatling gun (see Relationships). He claims to have friends across the border, and says he has been to Mexico and to Canada (see Biography).",
        "Nigel West Dickens le présente comme l'homme qui peut fournir la puissance de feu nécessaire contre Fort Mercer. Irish affirme connaître les armes sous toutes leurs coutures, et le Red Dead Wiki le classe comme trafiquant de contrebande. Son contact à Thieves' Landing, Shaky, fournit les munitions de la mitrailleuse Gatling (voir Relations). Il prétend avoir des amis de l'autre côté de la frontière, et dit être allé au Mexique et au Canada (voir la biographie).")},
    {"h4": two("Weapons", "Armes")},
    {"p": two(
        "The Red Dead Wiki lists a Cattleman Revolver and a Repeater Carbine. According to the mission page, \"We Shall Be Together in Paradise\" is the only mission in which he fights, with his Cattleman Revolver. In \"On Shaky's Ground\" he draws a revolver on two nuns and then on John, who takes it from him (see Biography). John mocks him for never using it, saying cobwebs must be growing on his holster.",
        "Le Red Dead Wiki lui attribue un Cattleman Revolver et une Repeater Carbine. Selon la page de la mission, \"We Shall Be Together in Paradise\" est la seule mission où il se bat, avec son Cattleman Revolver. Dans \"On Shaky's Ground\", il braque un revolver sur deux religieuses, puis sur John, qui le lui prend (voir la biographie). John se moque de lui parce qu'il ne s'en sert jamais : à l'entendre, des toiles d'araignée doivent pousser sur son étui.")},
    {"h4": two("Horses, wagons and the raft", "Chevaux, chariots et radeau")},
    {"p": two(
        "He rides his own horse with John in New Austin. At Gaptooth Breach he works the lift that brings John and the Gatling gun up from the mine, then waits below with a borrowed flatbed wagon. In \"On Shaky's Ground\" he drives the wagon loaded with ammunition while John rides shotgun. He crosses the San Luis River with John on his own raft. According to the Red Dead Wiki, he admits during the crossing that he cannot swim. On the Mexican bank, he looks over the horses waiting there before he and John ride off.",
        "Au New Austin, il accompagne John sur son propre cheval. À Gaptooth Breach, il actionne le monte-charge qui remonte John et la mitrailleuse du fond de la mine, puis attend en contrebas avec un chariot plat emprunté. Dans \"On Shaky's Ground\", il conduit le chariot chargé de munitions pendant que John assure la protection, fusil en main. Il traverse le San Luis avec John sur son propre radeau. D'après le Red Dead Wiki, il avoue pendant la traversée qu'il ne sait pas nager. Sur la rive mexicaine, il examine les chevaux qui les attendent avant qu'ils ne repartent chacun de leur côté.")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "Irish appears in five missions: the three of his own strand in New Austin, \"The Assault on Fort Mercer\" and the first mission in Mexico; the Missions table lists them. Each of them fails if John assaults or kills Irish. The four New Austin missions also fail if John abandons him or kills the horse he rides, and the river crossing fails if John abandons him or shoots the rope of the raft. According to the Red Dead Wiki, if John attacks him before one of his missions, Irish shoots back or runs away and cannot be killed. Right after \"We Shall Be Together in Paradise\", he can be killed only if the player acts very quickly, usually with Dead Eye; otherwise he rides off and is not seen again.",
        "Irish apparaît dans cinq missions : les trois de sa propre série au New Austin, \"The Assault on Fort Mercer\" et la première mission au Mexique ; le tableau des missions les recense. Toutes échouent si John agresse ou tue Irish. Les quatre missions du New Austin échouent aussi si John l'abandonne ou tue le cheval qu'il monte, et la traversée du fleuve échoue si John l'abandonne ou tire dans la corde du radeau. D'après le Red Dead Wiki, si John l'attaque avant l'une de ses missions, Irish riposte ou s'enfuit, et il est impossible de le tuer. Juste après \"We Shall Be Together in Paradise\", on ne peut l'abattre qu'en réagissant très vite, en général avec le Dead Eye ; sinon, il s'éloigne et on ne le revoit plus.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [two(
        "John meets him by saving his life in an Armadillo barn and holds that debt over him in every mission that follows (see Biography). John's patience runs out quickly: he threatens Irish several times, calls him a liar, a coward and a lazy drunk, and refuses his offer of a permanent partnership because he has had enough of liars. Irish answers that John would get more help if he were more cordial with people.",
        "John fait sa connaissance en lui sauvant la vie dans une grange d'Armadillo, et lui rappelle cette dette à chaque mission (voir la biographie). La patience de John s'épuise vite : il menace Irish à plusieurs reprises, le traite de menteur, de lâche et d'ivrogne paresseux, et refuse son offre d'association durable, parce qu'il en a assez des menteurs. Irish lui répond qu'il obtiendrait plus d'aide s'il se montrait plus aimable avec les gens."),
        two(
        "After the nuns at Thieves' Landing, Irish calls John a hypocrite who has robbed as many innocent people as he has; John answers that he tried to rob only those who had more than they deserved (see Quotes). John makes Irish promise to fight at Fort Mercer, and Irish does not turn up until the fight is over (see Biography). When they part on the Mexican bank, Irish tells John that he is an angry and ugly man, but not a bad one (see Quotes).",
        "Après l'épisode des religieuses de Thieves' Landing, Irish traite John d'hypocrite, qui a volé autant d'innocents que lui ; John répond qu'il s'efforçait de ne voler que ceux qui avaient plus qu'ils ne méritaient (voir Citations). John fait promettre à Irish de se battre à Fort Mercer, et Irish n'arrive qu'une fois le combat terminé (voir la biographie). Quand ils se séparent sur la rive mexicaine, Irish dit à John qu'il est un homme colérique et laid, mais pas un mauvais homme (voir Citations).")]},
    {"img": "nigel-west-dickens.jpeg", "slug": "nigel-west-dickens", "name": "Nigel West Dickens", "text": two(
        "Dickens calls Irish an old friend and sends John to find him, usually in Armadillo or a nearby town on a drinking spree; John sums him up as an alcoholic arms dealer. On their first ride, Irish calls Dickens a swindling charlatan who talks endlessly, and says one dose of his tonic once upset his stomach for weeks (see Quotes). The Gatling gun Irish finds is delivered to Dickens and mounted in his wagon (see Biography). At Brittlebrush Trawl, Dickens chats with him before the crossing, calls him an interesting fellow and says he is well connected south of the border; Irish laughs when Dickens claims that men like him are revered abroad.",
        "Dickens présente Irish comme un vieil ami et envoie John le chercher, d'ordinaire à Armadillo ou dans une ville voisine, en pleine beuverie ; John le résume d'une formule : un trafiquant d'armes alcoolique. Pendant leur première chevauchée, Irish traite Dickens de charlatan escroc intarissable, et raconte qu'une dose de son tonique lui a un jour dérangé l'estomac pendant des semaines (voir Citations). La mitrailleuse Gatling dénichée par Irish est livrée à Dickens et montée dans son chariot (voir la biographie). À Brittlebrush Trawl, Dickens bavarde avec lui avant la traversée, le qualifie d'homme intéressant et assure qu'il a de bonnes relations de l'autre côté de la frontière ; Irish éclate de rire quand Dickens prétend qu'à l'étranger, les hommes de sa trempe sont vénérés.")},
    {"img": None, "slug": None, "name": "Shaky", "text": two(
        "A stuttering smuggler who works out of the Thieves' Landing warehouse, and Irish's source for the Gatling gun ammunition. Irish leaves John to free him from the men beating him while he goes for the wagon, calling Shaky a good man (see Biography). When Shaky says they are even, Irish mocks his stutter and claims Shaky still owes him for morphine pills taken to calm his nerves; Shaky swears at him (see Quotes). The mission fails if Shaky is assaulted or killed.",
        "Un contrebandier bègue qui opère depuis l'entrepôt de Thieves' Landing, et la source d'Irish pour les munitions de la mitrailleuse Gatling. Irish laisse à John le soin de le libérer des hommes qui le passent à tabac et part chercher le chariot, non sans assurer que Shaky est un brave type (voir la biographie). Quand Shaky estime qu'ils sont quittes, Irish se moque de son bégaiement et affirme que Shaky lui doit encore des cachets de morphine destinés à calmer ses nerfs ; Shaky l'injurie (voir Citations). La mission échoue si Shaky est agressé ou tué.")},
    {"img": None, "slug": None, "name": "Welsh (Alwyn Lloyd) and French", "text": two(
        "Irish says he met these two men on the boat to America and that the three of them have been as thick as thieves ever since (see Origins). In 1911 they are drowning him in a horse trough in Armadillo, accusing him of stealing their gun and trying to steal their horses; Irish blames French, and John kills both (see Biography). Irish then says they were his only friends in the world and that he is glad to see them dead. According to the Red Dead Wiki, a notice in the Blackwater Ledger names Welsh as Alwyn Lloyd, believed to be of Welsh origin and killed by gunshot in Armadillo; the wiki gives French's name as Leander Holland. After the fight, John remarks that French did not sound very French.",
        "Irish raconte avoir rencontré ces deux hommes sur le bateau qui les amenait en Amérique, et qu'ils sont depuis comme les doigts de la main (voir Origines). En 1911, ils sont en train de le noyer dans un abreuvoir d'Armadillo, l'accusant de leur avoir volé leur arme et d'avoir tenté de voler leurs chevaux ; Irish rejette la faute sur French, et John les abat tous les deux (voir la biographie). Irish déclare ensuite que c'étaient ses seuls amis au monde, et qu'il est ravi de voir ces salauds morts. D'après le Red Dead Wiki, un avis du Blackwater Ledger identifie Welsh comme Alwyn Lloyd, présumé d'origine galloise et tué par balle à Armadillo ; le wiki donne à French le nom de Leander Holland. Après l'affrontement, John fait remarquer que French n'avait pas vraiment l'accent français.")},
    {"img": "seth-briars.jpeg", "slug": "seth-briars", "name": "Seth Briars", "text": two(
        "Both are recruited through Dickens for the Fort Mercer plan, but they share no scene. When Seth passes on Dickens's message that the machine gun needs ammunition, John says he will have to pay Irish another visit, which leads to \"On Shaky's Ground\" (see Biography).",
        "Tous deux sont recrutés par l'intermédiaire de Dickens pour le plan contre Fort Mercer, mais ils ne partagent aucune scène. Quand Seth transmet le message de Dickens selon lequel la mitrailleuse manque de munitions, John répond qu'il va devoir rendre une nouvelle visite à Irish, ce qui mène à \"On Shaky's Ground\" (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Irish never meets him. He helps arm the assault on Bill's hideout, then offers to guide John to Mexico when the prisoner at Fort Mercer says Bill has gone near Chuparosa, promising they will find him without trouble (see Biography).",
        "Irish ne le rencontre jamais. Il contribue à armer l'assaut contre le repaire de Bill, puis propose de guider John jusqu'au Mexique quand le prisonnier de Fort Mercer révèle que Bill est parti du côté de Chuparosa, en promettant qu'ils le retrouveront sans peine (voir la biographie).")},
    {"img": "landon-ricketts.jpeg", "slug": "landon-ricketts", "name": "Landon Ricketts", "text": two(
        "On the Mexican bank, Irish tells John about an American he once saw shoot a man and drank with in Chuparosa, before wondering whether that was in Canada (see Biography). The game does not name this man; the Red Dead Wiki identifies him as Landon Ricketts, whom John meets on arriving in Chuparosa.",
        "Sur la rive mexicaine, Irish parle à John d'un Américain qu'il aurait vu abattre un homme et avec qui il aurait bu à Chuparosa, avant de se demander si ce n'était pas plutôt au Canada (voir la biographie). Le jeu ne nomme pas cet homme ; le Red Dead Wiki l'identifie comme Landon Ricketts, que John rencontre en arrivant à Chuparosa.")},
    {"img": "agustin-allende.jpeg", "slug": "agustin-allende", "name": "Agustin Allende", "text": two(
        "Irish suggests the provincial governor as another lead: a colonel based in Escalera, whose Spanish name he cannot recall and with whom he says he played cards (see Biography). He cannot remember whether the man was pleasant or a bastard. The Red Dead Wiki identifies this colonel as Agustin Allende.",
        "Irish propose le gouverneur de la province comme autre piste : un colonel installé à Escalera, dont il a oublié le nom espagnol et avec qui il dit avoir joué aux cartes (voir la biographie). Il ne sait plus si l'homme était charmant ou un salaud. Le Red Dead Wiki identifie ce colonel comme Agustin Allende.")},
    {"img": None, "slug": None, "name": "The Mexican gunmen", "text": two(
        "Armed men on the Mexican bank attack the raft, one of them calling Irish a traitor (see Biography). Irish admits there is a bounty or two on his head in Mexico, linked, as far as he remembers, to money and to a misunderstanding about a man's daughter. He concludes that it is the women of Mexico, not the men, who love him.",
        "Des hommes armés postés sur la rive mexicaine attaquent le radeau, et l'un d'eux traite Irish de traître (voir la biographie). Irish reconnaît que sa tête est mise à prix une ou deux fois au Mexique, pour une histoire d'argent et, si sa mémoire est bonne, un malentendu au sujet de la fille d'un homme. Il en conclut que ce sont les femmes du Mexique, pas les hommes, qui l'adorent.")},
    {"img": None, "slug": None, "name": "His family", "text": two(
        "The game shows none of his relatives. Irish says his father warned him never to trust a Welshman and had his throat slit, and he swears on his mother's life that his intentions were pure. For his brother and the reasons he left home, see Origins.",
        "Le jeu ne montre aucun membre de sa famille. Irish raconte que son père l'avait mis en garde contre les Gallois et qu'il a fini égorgé, et il jure sur la vie de sa mère que ses intentions étaient pures. Sur son frère et les raisons de son départ, voir Origines.")},
]
