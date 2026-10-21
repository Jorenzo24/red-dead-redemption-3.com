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
  "Leander Holland" (French; Ledger No. 56 itself prints "Leander Holland, known to friends by the name of French",
  fc/ireddead_Ledger_No56_text.txt), "Shaky".
- FR Red Dead Wiki "L'Irlandais" (fc/web_notes_BD.txt): the name the French wiki gives him.
- Visual check: the live portrait.jpeg for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only: the Rockstar description; "It's the whiskey, sir...", "Life's too short for regrets...",
  "Team work, Johnny boy...", "I came into this world fightin'...", "You know me, Johnny boy. I'll be late to me own
  funeral..." (In his own words); "Down here, they call me El Rato...", "I'm pretty sure Rato means..." (Names).
  Part C Quotes must not repeat these.
- Relationship entries are one-clause pointers; part C Quotes keeps the verbatim versions (the hypocrite exchange,
  the parting words to John, the Shaky exchange, the Dickens tonic). Fixer (21 Oct 2026): cobwebs jibe left to C
  Quotes; cannot swim told here only; hogtie after "On Shaky's Ground" moved here from C Trivia; "Uncle Irish" is
  said in his sleep (transcript stage direction), not sung.
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
        "The Red Dead Wiki quotes a description of the character by Rockstar: \"A teller of tall tales, who'll try to talk his way out of anything.\" Wikipedia's summary of Red Dead Redemption calls him an alcoholic arms smuggler. In his missions, John finds him drunk or passed out more often than sober. He forgets John's name, or pretends to, between two missions.",
        "Le Red Dead Wiki cite une description du personnage signée Rockstar : \"A teller of tall tales, who'll try to talk his way out of anything.\" (un raconteur d'histoires à dormir debout, qui tentera de se tirer de n'importe quelle situation à force de baratin). Le résumé de Red Dead Redemption sur Wikipédia le présente comme un trafiquant d'armes alcoolique. Dans ses missions, John le trouve plus souvent ivre ou assommé par l'alcool qu'à jeun. D'une mission à l'autre, il oublie le nom de John, ou fait semblant.")},
    {"p": two(
        "He avoids danger whenever he can and leaves the fighting to John. He boasts of friends and contacts, some of whom turn out to be hostile. His speech is full of Irish turns of phrase (me for my, feck, shite) and of colorful comparisons. He calls John Johnny, Johnny boy, fella, dovey or smiler.",
        "Il fuit le danger dès qu'il le peut et laisse John se battre à sa place. Il se vante d'amis et de relations, dont certains se révèlent hostiles. Il parle avec des tournures irlandaises (me pour my, feck, shite) et des comparaisons imagées. Il appelle John Johnny, Johnny boy, fella, dovey ou smiler.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "Woken up in Benedict Point, in \"Man is Born Unto Trouble\", he explains his lapses: \"It's the whiskey, sir... It gives me the memory of a new born babe. As innocent as can be.\" On the two men who were drowning him, in \"A Frenchman, a Welshman and an Irishman\": \"Life's too short for regrets... and I'd outgrown them fools.\" On the wagon out of Thieves' Landing, in \"On Shaky's Ground\", when John points out that he missed the shooting: \"Someone's gotta drive the wagon, don't they? Team work, Johnny boy. That's my game. Not just the glory, like you.\"",
        "Réveillé à Benedict Point, dans \"Man is Born Unto Trouble\", il explique ses absences : \"It's the whiskey, sir... It gives me the memory of a new born babe. As innocent as can be.\" (c'est le whisky, monsieur, il me donne la mémoire d'un nouveau-né, innocent comme l'agneau). Sur les deux hommes qui le noyaient, dans \"A Frenchman, a Welshman and an Irishman\" : \"Life's too short for regrets... and I'd outgrown them fools.\" (la vie est trop courte pour les regrets, et ces imbéciles, je les avais dépassés). Sur le chariot qui quitte Thieves' Landing, dans \"On Shaky's Ground\", quand John lui fait remarquer qu'il a raté la fusillade : \"Someone's gotta drive the wagon, don't they? Team work, Johnny boy. That's my game. Not just the glory, like you.\" (il faut bien que quelqu'un conduise le chariot, non ? L'esprit d'équipe, Johnny, c'est ça mon truc. Pas seulement la gloire, comme toi).")},
    {"p": two(
        "On the raft, in \"We Shall Be Together in Paradise\": \"You know me, Johnny boy. I'll be late to me own funeral. They said God invented whiskey to stop the Irish from rulin' the world.\" Under fire a few minutes later: \"I came into this world fightin'. And I'll go out of it fightin'!\"",
        "Sur le radeau, dans \"We Shall Be Together in Paradise\" : \"You know me, Johnny boy. I'll be late to me own funeral. They said God invented whiskey to stop the Irish from rulin' the world.\" (tu me connais, Johnny, je serai en retard à mon propre enterrement. On dit que Dieu a inventé le whisky pour empêcher les Irlandais de gouverner le monde). Sous les balles, quelques minutes plus tard : \"I came into this world fightin'. And I'll go out of it fightin'!\" (je suis venu au monde en me battant, et je le quitterai en me battant !).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Irish is a nickname, and the game never gives him another name. Wikipedia lists him as Irish, and Nigel West Dickens calls him Mr. Irish. Talking in his sleep in Benedict Point, he calls himself Uncle Irish. Welsh and French insult him as a paddy and a mick. On the raft he claims that in Mexico he is known as El Rato: \"Down here, they call me El Rato. The cat. On account of me stealth and cunning.\" John corrects him: \"I'm pretty sure Rato means \"rat,\" my friend.\" John adds that he likes it, as it is a little more inventive than Irish. The French-language Red Dead Wiki calls him L'Irlandais.",
        "Irish est un surnom, et le jeu ne lui en donne jamais d'autre. Wikipédia le désigne sous ce nom, et Nigel West Dickens l'appelle Mr. Irish. Quand il parle en dormant, à Benedict Point, il se surnomme lui-même Uncle Irish (tonton Irish). Welsh et French l'insultent en le traitant de paddy et de mick, deux sobriquets méprisants pour les Irlandais. Sur le radeau, il affirme qu'au Mexique on l'appelle El Rato : \"Down here, they call me El Rato. The cat. On account of me stealth and cunning.\" (par ici, on m'appelle El Rato, le chat, à cause de ma discrétion et de ma ruse). John le reprend : \"I'm pretty sure Rato means \"rat,\" my friend.\" (je suis à peu près sûr que Rato veut dire rat, mon ami). Il ajoute que le surnom lui plaît, un peu plus inventif qu'Irish. Le Red Dead Wiki francophone l'appelle L'Irlandais.")},
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
        "Nigel West Dickens presents him as the man who can supply the firepower for Fort Mercer. Irish says he knows guns front, back and sideways, and the Red Dead Wiki lists his occupation as contraband dealer. His Thieves' Landing contact, Shaky, provides the ammunition for the Gatling gun (see Relationships). He claims to have friends across the border (see Biography).",
        "Nigel West Dickens le présente comme l'homme qui peut fournir la puissance de feu nécessaire contre Fort Mercer. Irish affirme connaître les armes sous toutes leurs coutures, et le Red Dead Wiki le classe comme trafiquant de contrebande. Son contact à Thieves' Landing, Shaky, fournit les munitions de la mitrailleuse Gatling (voir Relations). Il prétend avoir des amis de l'autre côté de la frontière (voir la biographie).")},
    {"h4": two("Weapons", "Armes")},
    {"p": two(
        "The Red Dead Wiki lists a Cattleman Revolver and a Repeater Carbine. According to the mission page, \"We Shall Be Together in Paradise\" is the only mission in which he fights, with his Cattleman Revolver. In \"On Shaky's Ground\" he draws it on two nuns and on John (see Biography).",
        "Le Red Dead Wiki lui attribue un Cattleman Revolver et une Repeater Carbine. Selon la page de la mission, \"We Shall Be Together in Paradise\" est la seule mission où il se bat, avec son Cattleman Revolver. Dans \"On Shaky's Ground\", il le braque sur deux religieuses, puis sur John (voir la biographie).")},
    {"h4": two("Horses, wagons and the raft", "Chevaux, chariots et radeau")},
    {"p": two(
        "He rides his own horse with John in New Austin, and he brings or drives the wagons that carry the Gatling gun and its ammunition (see the Missions table). He takes John across the San Luis River on his own raft. According to the Red Dead Wiki, he admits during the crossing that he cannot swim.",
        "Au New Austin, il suit John sur son propre cheval, et c'est lui qui amène ou conduit les chariots de la Gatling et de ses munitions (voir le tableau des missions). Il fait traverser le San Luis à John sur son propre radeau. D'après le Red Dead Wiki, il avoue pendant la traversée qu'il ne sait pas nager.")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "Every mission in which Irish appears (see the Missions table) fails if John assaults or kills him. The four New Austin missions also fail if John abandons him or kills the horse he rides, and the river crossing fails if John abandons him or shoots the rope of the raft. According to the Red Dead Wiki, if John attacks him before one of his missions, Irish shoots back or runs away and cannot be killed. After \"On Shaky's Ground\", a player who catches up with his wagon and climbs back on makes him flee, and can then kill or hogtie him. Right after \"We Shall Be Together in Paradise\", he can be killed only if the player acts very quickly, usually with Dead Eye; otherwise he rides off and is not seen again.",
        "Toutes les missions où Irish apparaît (voir le tableau des missions) échouent si John l'agresse ou le tue. Les quatre missions du New Austin échouent aussi si John l'abandonne ou tue le cheval qu'il monte, et la traversée du fleuve échoue si John l'abandonne ou tire dans la corde du radeau. D'après le Red Dead Wiki, si John l'attaque avant l'une de ses missions, Irish riposte ou s'enfuit, et il est impossible de le tuer. Après \"On Shaky's Ground\", un joueur qui rattrape son chariot et remonte dessus le fait fuir, et peut alors le tuer ou le ligoter. Juste après \"We Shall Be Together in Paradise\", on ne peut l'abattre qu'en réagissant très vite, en général avec le Dead Eye ; sinon, il s'éloigne et on ne le revoit plus.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [two(
        "John meets him by saving his life in an Armadillo barn and holds that debt over him in every mission that follows (see Biography). John's patience runs out quickly: he threatens Irish several times, calls him a liar, a coward and a lazy drunk, and refuses his offer of a permanent partnership because he has had enough of liars. Irish answers that John would get more help if he were more cordial with people.",
        "John fait sa connaissance en lui sauvant la vie dans une grange d'Armadillo, et lui rappelle cette dette à chaque mission (voir la biographie). La patience de John s'épuise vite : il menace Irish à plusieurs reprises, le traite de menteur, de lâche et d'ivrogne paresseux, et refuse son offre d'association durable, parce qu'il en a assez des menteurs. Irish lui répond qu'il obtiendrait plus d'aide s'il se montrait plus aimable avec les gens."),
        two(
        "After the nuns at Thieves' Landing, Irish calls John a hypocrite (see Quotes). John makes Irish promise to fight at Fort Mercer, and Irish does not turn up until the fight is over (see Biography). When they part on the Mexican bank, Irish gives John his verdict on his character (see Quotes).",
        "Après l'épisode des religieuses de Thieves' Landing, Irish traite John d'hypocrite (voir Citations). John lui fait promettre de se battre à Fort Mercer, et Irish n'arrive qu'une fois le combat terminé (voir la biographie). Au moment de se quitter, sur la rive mexicaine, Irish dit à John ce qu'il pense de lui (voir Citations).")]},
    {"img": "nigel-west-dickens.jpeg", "slug": "nigel-west-dickens", "name": "Nigel West Dickens", "text": two(
        "Dickens calls Irish an old friend and sends John to him (see Biography). According to the Red Dead Wiki's list of his lines, Irish calls Dickens a charlatan in an optional conversation on the ride to the lake, and blames his tonic for weeks of stomach trouble (see Quotes). The Gatling gun Irish finds ends up in Dickens's wagon (see Biography). At Brittlebrush Trawl, Irish laughs when Dickens says he is leaving for the civilized world, where men like himself are revered and given medals.",
        "Dickens présente Irish comme un vieil ami et envoie John le trouver (voir la biographie). D'après la liste de ses répliques publiée par le Red Dead Wiki, Irish traite Dickens de charlatan lors d'une conversation facultative sur la route du lac, et accuse son tonique de lui avoir détraqué l'estomac pendant des semaines (voir Citations). La mitrailleuse Gatling dénichée par Irish finit dans le chariot de Dickens (voir la biographie). À Brittlebrush Trawl, Irish éclate de rire quand Dickens annonce qu'il part pour le monde civilisé, où les hommes comme lui sont vénérés et couverts de médailles.")},
    {"img": None, "slug": None, "name": "Shaky", "text": two(
        "A stuttering smuggler who works out of the Thieves' Landing warehouse, and Irish's source for the Gatling gun ammunition. Irish sends John in to free him and goes for the wagon (see Biography). When they part, Irish mocks his stutter and the two trade insults (see Quotes). The mission fails if Shaky is assaulted or killed.",
        "Un contrebandier bègue qui opère depuis l'entrepôt de Thieves' Landing, et la source d'Irish pour les munitions de la mitrailleuse Gatling. Irish envoie John le délivrer et part chercher le chariot (voir la biographie). Au moment de se séparer, Irish se moque de son bégaiement et les deux hommes échangent des insultes (voir Citations). La mission échoue si Shaky est agressé ou tué.")},
    {"img": None, "slug": None, "name": "Welsh (Alwyn Lloyd) and French (Leander Holland)", "text": two(
        "Irish says he met these two men on the boat to America; in 1911 they are drowning him in Armadillo when John kills them (see Biography). Both are named in Issue No. 56 of the Blackwater Ledger (see Biography). On the ride to the lake, John remarks that French did not sound very French.",
        "Irish dit avoir rencontré ces deux hommes sur le bateau qui les amenait en Amérique ; en 1911, ils sont en train de le noyer à Armadillo quand John les abat (voir la biographie). Le numéro 56 du Blackwater Ledger donne leurs noms (voir la biographie). Sur la route du lac, John fait remarquer que French n'avait pas vraiment l'accent français.")},
    {"img": "seth-briars.jpeg", "slug": "seth-briars", "name": "Seth Briars", "text": two(
        "Both are recruited through Dickens for the Fort Mercer plan, but they share no scene. Seth's message that the machine gun has no ammunition sends John back to Irish (see Biography).",
        "Tous deux sont recrutés par l'intermédiaire de Dickens pour le plan contre Fort Mercer, mais ils ne partagent aucune scène. C'est le message de Seth sur les munitions manquantes qui renvoie John chez Irish (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Irish never meets him. He helps arm the assault on Bill's hideout, then offers to guide John to Mexico when Bill's trail leads near Chuparosa; at Brittlebrush Trawl, in \"We Shall Be Together in Paradise\", he promises they will find Bill without trouble (see Biography).",
        "Irish ne le rencontre jamais. Il contribue à armer l'assaut contre le repaire de Bill, puis propose de guider John jusqu'au Mexique quand la piste de Bill mène du côté de Chuparosa ; à Brittlebrush Trawl, dans \"We Shall Be Together in Paradise\", il lui promet qu'ils le retrouveront sans peine (voir la biographie).")},
    {"img": "landon-ricketts.jpeg", "slug": "landon-ricketts", "name": "Landon Ricketts", "text": two(
        "On the Mexican bank, Irish recalls an American he saw shoot a man and drank with in Chuparosa, then decides that this was in Canada (see Biography). The game does not name the American; the Red Dead Wiki identifies him as Landon Ricketts, whom John meets on arriving in Chuparosa.",
        "Sur la rive mexicaine, Irish évoque un Américain qu'il aurait vu abattre un homme et avec qui il aurait bu à Chuparosa, avant de conclure que c'était au Canada (voir la biographie). Le jeu ne nomme pas cet Américain ; le Red Dead Wiki l'identifie comme Landon Ricketts, que John rencontre en arrivant à Chuparosa.")},
    {"img": "agustin-allende.jpeg", "slug": "agustin-allende", "name": "Agustin Allende", "text": two(
        "Irish suggests the provincial governor, a colonel based in Escalera, as another lead (see Biography). The Red Dead Wiki identifies this colonel as Agustin Allende.",
        "Irish propose comme autre piste le gouverneur de la province, un colonel installé à Escalera (voir la biographie). Le Red Dead Wiki identifie ce colonel comme Agustin Allende.")},
    {"img": None, "slug": None, "name": "The Mexican gunmen", "text": two(
        "Armed men on the Mexican bank attack the raft, one of them calling Irish a traitor, and Irish admits to a bounty or two on his head (see Biography). He concludes that it is the women of Mexico, not the men, who love him.",
        "Des hommes armés postés sur la rive mexicaine attaquent le radeau, l'un d'eux traite Irish de traître, et Irish avoue avoir une prime ou deux sur la tête (voir la biographie). Il en conclut que ce sont les femmes du Mexique, pas les hommes, qui l'adorent.")},
    {"img": None, "slug": None, "name": "His family", "text": two(
        "The game shows none of his relatives. For his father, his mother and his brother, see Origins.",
        "Le jeu ne montre aucun membre de sa famille. Sur son père, sa mère et son frère, voir Origines.")},
]
