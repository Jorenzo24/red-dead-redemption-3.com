"""Agustin Allende, part B: Personality (official description, observable traits, In his own words, Names, Appearance),
Weapons, stagecoach and villa (the fiche-specific skills section), Relationships (21 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN sections Personality (kept only where a transcript supports a trait), Appearance, the GOTY
quote box, the infobox (aka, weapons, family, affiliations), the trivia on the sabre and the armored stagecoach, the
portrait left in the villa, the corpse on the road, the rebel posters ("General Sanchez's dog"), Irish's card game, the
"only major character who gives no mission" note; plus the four transcripts of his missions and the lines others speak
about him in eleven more transcripts. Narrative events are told in part A; the entries below point to them.

SOURCE REGISTER (read 21 Oct 2026; wiki cache scripts/v3/work/_m/):
- Official description: Red Dead Redemption: Game of the Year Edition guide (BradyGames), quoted in the quote box of the
  Red Dead Wiki EN page "Agustin Allende" ("This gentleman is a 53-year-old, sadistic, military leader..."). The guide
  itself was not read: quoted through the wiki, attributed. Rockstar's 6 Sep 2018 descriptions cover the RDR2 gang only.
- Transcripts, his own lines (every quoted line checked): "The Demon Drink/dialogues", "Mexican Caesar/dialogues",
  "Cowards Die Many Times/dialogues", "An Appointed Time/dialogues".
- Transcripts, what others say of him: "Civilization, at Any Price/dialogues" and "Empty Promises/dialogues" (De Santa),
  "Mexican Caesar/dialogues" (Espinoza), "The Great Mexican Train Robbery/dialogues" and "The Gates of El Presidio/
  dialogues" (Reyes, Javier), "Father Abraham/dialogues" and "The Mexican Wagon Train/dialogues" (Luisa, Ricketts),
  "The Gunslinger's Tragedy/dialogues" (Ricketts), "Captain De Santa's Downfall/dialogues" (Victor, De Santa), "Must a
  Savior Die?/dialogues" (executioner), "We Shall Be Together in Paradise/dialogues" (Irish).
- Mission pages: "Mexican Caesar" (villa gates locked until "An Appointed Time"), "An Appointed Time" (stagecoach escort,
  corpse on the road, lasso and flight variants, gates still down in 1914), infobox givers of the four missions.
- Other wiki pages: "Ignacio Sanchez" (poster captions), "Raul Zubieta" (medals trivia), "Herbert Moon" (quote box),
  "Espinoza", FR wiki "Agustin Allende" (infobox: armored stagecoach; "épée en or").
- Visual check: live portrait.jpeg and gallery-1.jpeg for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only (parts A and C must not repeat them): the GOTY description; "Ah, perhaps you come to hunt me, eh? Your
  country loves to make trouble in mine.", "My people have lived and worked here for a hundred years...", "You are in no
  position to negotiate.", "You know, you are a rare find. A gringo who is also a friend of our country." (In his own
  words); De Santa's "His Excellency, El Coronel", Reyes's "perrito" and "marioneta" lines, Irish's "Colonel something or
  other" line, the two poster captions (Names); De Santa's "Colonel Allende controls any situation..." line, Espinoza's
  "I am Allende's brazo derecho" line, Luisa's "Allende es pura maldad", Ricketts's "feudal king" and "For once, I agree
  with Allende" lines, Victor's "Allende is scared, and making mistakes", Herbert Moon's "all the same" line
  (relationship entries).
- Left to part C Quotes (paraphrased here, never in quotation marks): every line of the wiki's Quotes list ("We'll make a
  patriot of you yet!", "Force must be used...", "Sorry? Why be sorry?...", "Qué será, será...", "Don't shoot! Here, take
  Williamson..."), the top quote box ("We brought them God!..."), the Demon Drink quote box ("I see in their faces..."),
  "Buying my freedom, pendejo!", the multiplayer lines.
- Told once elsewhere, pointer here: every mission event (A); his uncle and Javier's father (A Origins: one clause in the
  relationship entries); the 1911 newspaper (A); the multiplayer model and the GOTY box art (C Other media); the actor
  and the pre-release artwork (D).
- Gameplay HERE only (part C Trivia must not repeat): no mission given; the villa gates; the stagecoach and its escort;
  the corpse on the road; the portrait left in the villa; the gates still down in 1914; the flight variants; weapons.

WIKI-ONLY (kept, attributed): the GOTY description; sabre and Cattleman Revolver (infobox); the golden sword (FR wiki
infobox); the armored stagecoach's only appearance; the portrait in the villa; the poster captions; Zubieta and Allende
as the only soldiers with medals; the "no mission given" note; Herbert Moon's line (wiki quote box, no transcript).

Excluded: "doesn't care who he kills", "intelligent", "manipulates people for his own gain" as the wiki's own judgments
(only the GOTY guide's wording is quoted, attributed); "hinting that the Rebels did not decide to occupy it" (wiki
inference); "his family is of Spanish origin" (wiki says "implied"); the Communist Manifesto allusion and "possible
that Allende was once a communist" (speculation); the vomiting at the start of "Mexican Caesar" read as a hangover and
"an extremely heavy drinker" (wiki inference; the scene itself is left to part A); the FR wiki's "too old to find a
wife" and "favourite activity" paragraph (opinion); Javier as Allende's "hitman for hire" (no transcript: Reyes and
Javier say only that Javier and Bill paid for his protection); "screams when the corpse is set on fire" (mission page,
unverifiable, tasteless detail of no value); the Espinoza page's claim that he "holds Allende in very high esteem" beyond
Espinoza's own line; Fussar comparisons of the FR wiki (fan analysis).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "The Red Dead Wiki quotes the Game of the Year Edition guide of Red Dead Redemption: \"This gentleman is a 53-year-old, sadistic, military leader of a local Mexican province. The province is in the midst of a rebellion. Many years ago, Allende was an idealist, but he's become a vicious cynic with a love of torture and sexual abuse. Takes pleasure in all manner of vices. He is intelligent, corrupt, and brutal.\"",
        "Le Red Dead Wiki cite le guide de l'édition Game of the Year de Red Dead Redemption : \"This gentleman is a 53-year-old, sadistic, military leader of a local Mexican province. The province is in the midst of a rebellion. Many years ago, Allende was an idealist, but he's become a vicious cynic with a love of torture and sexual abuse. Takes pleasure in all manner of vices. He is intelligent, corrupt, and brutal.\" (Ce monsieur de 53 ans est le chef militaire sadique d'une province mexicaine, en pleine rébellion. Idéaliste il y a bien des années, il est devenu un cynique impitoyable, qui aime la torture et les violences sexuelles. Il se complaît dans tous les vices. Il est intelligent, corrompu et brutal.)")},
    {"p": two(
        "On screen, he insults his officers in Spanish, in front of John. At their first meeting, he threatens to have John dragged around town by a horse or set upon by dogs, then gives him orders. He receives him on the terrace of his mansion in Escalera, with young women brought to him by his soldiers. He speaks of the people of the province with contempt. He is never seen near a fight: John remarks on it to De Santa, who answers that the governor must be protected and kept out of harm's way.",
        "À l'écran, il insulte ses officiers en espagnol devant John. À leur première rencontre, il menace de faire traîner John dans les rues par un cheval ou de lui lâcher les chiens dessus, puis lui donne des ordres. Il le reçoit sur la terrasse de sa demeure d'Escalera, entouré de jeunes femmes que ses soldats lui amènent. Il parle avec mépris des habitants de la province. On ne le voit jamais près d'un combat : John le fait remarquer à De Santa, qui répond que le gouverneur doit être protégé et tenu à l'abri du danger.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "To John, at their first meeting in \"The Demon Drink\": \"Ah, perhaps you come to hunt me, eh? Your country loves to make trouble in mine.\" On his family and the province, in the same scene: \"My people have lived and worked here for a hundred years. We brought civilization, and these people, these fucking monkeys, despise us.\" When John asks to be given the two outlaws first: \"You are in no position to negotiate.\" Welcoming John back in \"Cowards Die Many Times\": \"You know, you are a rare find. A gringo who is also a friend of our country.\"",
        "À John, lors de leur première rencontre dans \"The Demon Drink\" : \"Ah, perhaps you come to hunt me, eh? Your country loves to make trouble in mine.\" (ah, vous êtes peut-être venu me chasser, hein ? Votre pays adore semer le trouble dans le mien). Sur sa famille et la province, dans la même scène : \"My people have lived and worked here for a hundred years. We brought civilization, and these people, these fucking monkeys, despise us.\" (les miens vivent et travaillent ici depuis cent ans ; nous avons apporté la civilisation, et ces gens, ces putains de singes, nous méprisent). Quand John demande à recevoir d'abord les deux hors-la-loi : \"You are in no position to negotiate.\" (vous n'êtes pas en position de négocier). En accueillant John dans \"Cowards Die Many Times\" : \"You know, you are a rare find. A gringo who is also a friend of our country.\" (vous savez, vous êtes une perle rare : un gringo qui est aussi un ami de notre pays).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "John, Reyes and the newspapers call him Colonel Allende or Allende; his soldiers say el Coronel. De Santa calls him \"His Excellency, El Coronel\" in \"Mexican Caesar\". Reyes calls him \"una marioneta\", a puppet, and \"a perrito for General Sánchez\", which he explains as a little dog that licks the general's feet. According to the captions of the Red Dead Wiki, two rebel posters call him the lapdog and the puppet of Sanchez. Irish, who claims to have played Three Card Stud with him, remembers only \"Colonel something or other...some Spanish name\". Wikipedia spells his first name Agustín.",
        "John, Reyes et les journaux l'appellent le colonel Allende ou Allende ; ses soldats disent el Coronel. De Santa le désigne comme \"His Excellency, El Coronel\" (Son Excellence le Colonel) dans \"Mexican Caesar\". Reyes le traite de \"marioneta\" (marionnette) et de \"perrito\" (petit chien) du général Sánchez, un chien qui lui lèche les pieds. D'après les légendes du Red Dead Wiki, deux affiches rebelles font de lui le toutou et la marionnette de Sanchez. Irish, qui affirme avoir joué au Three Card Stud avec lui, ne se souvient que d'un \"Colonel something or other...some Spanish name\" (colonel quelque chose, un nom espagnol). Wikipédia écrit son prénom Agustín.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is a man of about fifty with slicked-back black hair, a receding hairline, a curled handlebar mustache and a tuft of beard under the lip. He wears a black army uniform with a gold-embroidered collar, gold fringed epaulettes and three medals on the chest. According to the Red Dead Wiki, he and Major Raul Zubieta are the only soldiers in the game with medals on their uniforms.",
        "C'est un homme d'une cinquantaine d'années, aux cheveux noirs plaqués en arrière et au front dégarni, avec une moustache en guidon recourbée et une mouche sous la lèvre. Il porte un uniforme militaire noir au col brodé d'or, des épaulettes à franges dorées et trois médailles sur la poitrine. Selon le Red Dead Wiki, le major Raul Zubieta et lui sont les seuls soldats du jeu à porter des médailles.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Suggested section title for the module: "Weapons, stagecoach and villa" / "Armes, diligence et villa".
BLOCKS_SKILLS = [
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "Allende appears in four story missions of the second act of Red Dead Redemption but gives none of them: Captain de Santa gives \"The Demon Drink\", \"Mexican Caesar\" and \"Cowards Die Many Times\", and Abraham Reyes gives \"An Appointed Time\" (the Missions table lists his role in each). The Red Dead Wiki notes that he is the only major character of the game who never gives John a mission directly. According to the mission page of \"Mexican Caesar\", the gates of his villa are locked after that mission and stay shut until \"An Appointed Time\".",
        "Allende apparaît dans quatre missions principales du deuxième acte de Red Dead Redemption, mais n'en confie aucune : le capitaine De Santa donne \"The Demon Drink\", \"Mexican Caesar\" et \"Cowards Die Many Times\", et Abraham Reyes \"An Appointed Time\" (le tableau des missions résume son rôle dans chacune). Le Red Dead Wiki relève qu'il est le seul personnage majeur du jeu à ne jamais confier directement de mission à John. D'après la page de \"Mexican Caesar\", les grilles de sa villa sont fermées après cette mission et le restent jusqu'à \"An Appointed Time\".")},
    {"p": two(
        "In \"An Appointed Time\", the mission page describes several variants. John can kill both men, one of them or neither, and Reyes shoots whoever John spares. If John tries to lasso Bill while Allende pins him down, Reyes shoots both, which can block the mission. On rare occasions Allende runs into the brush and Reyes shoots him in the back; sometimes nobody shoots him and the mission stalls. After the mission, his body can stay on the road east of Escalera and cannot be looted. The gates of the villa still lie in pieces in 1914, and, according to the Red Dead Wiki, his portrait still hangs inside.",
        "Dans \"An Appointed Time\", la page de la mission décrit plusieurs variantes. John peut tuer les deux hommes, l'un des deux ou aucun, et Reyes abat celui que John épargne. Si John tente de prendre Bill au lasso pendant qu'Allende le maintient au sol, Reyes les abat tous les deux, ce qui peut bloquer la mission. Plus rarement, Allende s'enfuit dans les broussailles et Reyes l'abat dans le dos ; il arrive aussi que personne ne tire et que la mission se fige. Après la mission, son corps peut rester sur la route à l'est d'Escalera, sans pouvoir être fouillé. Les grilles de la villa gisent toujours en morceaux en 1914 et, selon le Red Dead Wiki, son portrait est toujours accroché à l'intérieur.")},
    {"h4": two("Weapons and stagecoach", "Armes et diligence")},
    {"p": two(
        "The Red Dead Wiki lists a sabre and a Cattleman Revolver as his weapons; the French-language wiki calls the blade a golden sword. He owns an armored stagecoach with a Gatling gun mounted on the back, which appears only in \"An Appointed Time\". On his flight, the mission page counts a driver, a guard riding shotgun, a gunner on the Gatling and two riders behind the coach. John stops it by killing the driver or the horses.",
        "Le Red Dead Wiki lui attribue un sabre et un Cattleman Revolver ; le wiki francophone parle d'une épée en or. Il possède une diligence blindée, armée d'une mitrailleuse Gatling à l'arrière, que l'on ne voit que dans \"An Appointed Time\". Lors de sa fuite, la page de la mission compte un cocher, un garde armé à ses côtés, un tireur à la Gatling et deux cavaliers derrière la voiture. John l'arrête en abattant le cocher ou les chevaux.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "Allende promises to find Bill Williamson and Javier Escuella for John in exchange for his help against the rebels, then sends him to Chuparosa, where De Santa has him arrested and set before a firing squad (see Biography). The promised 20,000 pesos are never paid. John tells Luisa later that Allende betrayed him and that he saw him do things that disgust even him. John stops the colonel's stagecoach on the road out of Escalera (see Biography).",
        "Allende promet à John de lui trouver Bill Williamson et Javier Escuella en échange de son aide contre les rebelles, puis l'envoie à Chuparosa, où De Santa le fait arrêter et mettre face à un peloton (voir la biographie). Les 20 000 pesos promis ne sont jamais versés. John confie plus tard à Luisa qu'Allende l'a trahi, et qu'il l'a vu commettre des actes qui le dégoûtent, lui-même. John arrête la diligence du colonel sur la route à la sortie d'Escalera (voir la biographie).")},
    {"img": "abraham-reyes.jpeg", "slug": "abraham-reyes", "name": "Abraham Reyes", "text": two(
        "The leader of the revolt against him. Allende tells John that men like Javier's father are natural allies for Reyes. Reyes holds President Sanchez responsible for everything Allende does, and says it is worse that Allende enjoys beating the people he swore to protect. Reyes looks forward to sleeping in his silk sheets. His rebels take Escalera, and Allende dies on the road, shot by John or by Reyes (see Biography).",
        "Le chef de la révolte dirigée contre lui. Allende explique à John que les hommes comme le père de Javier sont des alliés naturels de Reyes. Reyes tient le président Sanchez pour responsable de tout ce que fait Allende, et juge pire encore qu'Allende prenne plaisir à battre le peuple qu'il a juré de protéger. Reyes se voit déjà dormir dans ses draps de soie. Ses rebelles prennent Escalera, et Allende meurt sur la route, abattu par John ou par Reyes (voir la biographie).")},
    {"img": "vincente-de-santa.jpeg", "slug": "vincente-de-santa", "name": "Vincente de Santa", "text": [
        two("His captain and go-between with John. Allende insults him in Spanish in front of John, calls him a crybaby and tells him not to stand behind him, since he is not his shadow. De Santa brings him young women from the villages, which he presents as patriots. He defends his colonel to John: \"Colonel Allende controls any situation he is in because he knows the situation can never be allowed to control him.\"",
            "Son capitaine, et son intermédiaire auprès de John. Allende l'insulte en espagnol devant John, le traite de pleurnichard et lui interdit de se tenir derrière lui, puisqu'il n'est pas son ombre. De Santa lui amène des jeunes femmes des villages, qu'il présente comme des patriotes. Il défend son colonel face à John : \"Colonel Allende controls any situation he is in because he knows the situation can never be allowed to control him.\" (le colonel Allende maîtrise toute situation, parce qu'il sait qu'aucune situation ne doit jamais le maîtriser)."),
        two("De Santa carries out the betrayal of John in Chuparosa, then dies at Sepulcro, shot by John or by the rebels; at the execution he oversees there, he condemns the prisoners in the name of Colonel Allende's government (see Biography).",
            "C'est De Santa qui exécute la trahison de John à Chuparosa ; il meurt ensuite à Sepulcro, abattu par John ou par les rebelles, après avoir condamné des prisonniers au nom du gouvernement du colonel Allende (voir la biographie)."),
    ]},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Bill lives under the colonel's protection in Escalera; according to Reyes, he and Javier paid Allende to hide them. When the rebels break down the door of the mansion, Bill covers Allende's run to the stagecoach. Once the coach is stopped, Allende pushes him out and offers him to John in exchange for his own life. Both men die on the road (see Biography).",
        "Bill vit sous la protection du colonel à Escalera ; selon Reyes, Javier et lui ont payé Allende pour qu'il les cache. Quand les rebelles enfoncent la porte de la demeure, Bill couvre la course d'Allende vers la diligence. Une fois la voiture arrêtée, Allende le pousse dehors et le livre à John en échange de sa propre vie. Les deux hommes meurent sur la route (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Allende tells John that Javier comes from the province and that his father, a drunk, worked land farmed by Allende's uncle (see Biography). Javier is under his protection at El Presidio; when John corners him there, Javier says that Bill is with Allende (see Biography).",
        "Allende raconte à John que Javier est originaire de la province et que son père, un ivrogne, travaillait une terre cultivée par l'oncle d'Allende (voir la biographie). Javier est sous sa protection à El Presidio ; quand John l'y accule, Javier lui apprend que Bill est avec Allende (voir la biographie).")},
    {"img": "luisa-fortuna.jpeg", "slug": "luisa-fortuna", "name": "Luisa Fortuna", "text": two(
        "Luisa blames Allende for the death of her father, killed by the army, and for the girls taken that day (see Biography). She tells John she cannot forgive him for having helped Allende, and says of the colonel: \"Allende es pura maldad.\" She is killed in Escalera on the day the town falls (see Biography).",
        "Luisa tient Allende pour responsable de la mort de son père, tué par l'armée, et des jeunes filles enlevées le même jour (voir la biographie). Elle dit à John qu'elle ne lui pardonne pas d'avoir aidé Allende, et lâche à propos du colonel : \"Allende es pura maldad.\" (Allende, c'est le mal à l'état pur). Elle est tuée à Escalera le jour où la ville tombe (voir la biographie).")},
    {"img": "landon-ricketts.jpeg", "slug": "landon-ricketts", "name": "Landon Ricketts", "text": two(
        "The gunslinger never meets him. He describes him to John in \"The Gunslinger's Tragedy\": \"Colonel Allende, he runs this place like a feudal king. He's an awful individual.\" When Luisa reports that Allende is sending a writer and a local official to their deaths, Ricketts answers: \"For once, I agree with Allende. Some men need to be killed.\" He then fights the colonel's soldiers alongside John (see Biography).",
        "Le pistolero ne le rencontre jamais. Il le décrit à John dans \"The Gunslinger's Tragedy\" : \"Colonel Allende, he runs this place like a feudal king. He's an awful individual.\" (le colonel Allende gouverne cet endroit comme un roi féodal ; c'est un individu épouvantable). Quand Luisa rapporte qu'Allende envoie à la mort un écrivain et un fonctionnaire local, Ricketts répond : \"For once, I agree with Allende. Some men need to be killed.\" (pour une fois, je suis d'accord avec Allende : il y a des hommes qu'il faut tuer). Il affronte ensuite les soldats du colonel aux côtés de John (voir la biographie).")},
    {"img": "irish.jpeg", "slug": "irish", "name": "Irish", "text": two(
        "In \"We Shall Be Together in Paradise\", Irish suggests to John that he try the provincial governor based in Escalera, whose name he cannot remember (see Names). He says he played Three Card Stud with him.",
        "Dans \"We Shall Be Together in Paradise\", Irish suggère à John de s'adresser au gouverneur de la province, installé à Escalera, dont il a oublié le nom (voir Noms). Il affirme avoir joué au Three Card Stud avec lui.")},
    {"img": None, "slug": None, "name": "Espinoza", "text": two(
        "The army captain, De Santa's rival. He tells John: \"I am Allende's brazo derecho. His right arm. I am one of the few men he respects.\" He tells John that the colonel himself told him De Santa had praised him and asked that he be given the munitions escort of \"Mexican Caesar\". John kills him in Chuparosa (see Biography).",
        "Capitaine de l'armée et rival de De Santa. Il déclare à John : \"I am Allende's brazo derecho. His right arm. I am one of the few men he respects.\" (je suis le bras droit d'Allende, l'un des rares hommes qu'il respecte). Il lui confie que le colonel lui a rapporté les éloges de De Santa à son sujet, et que De Santa a demandé qu'on lui confie l'escorte des munitions de \"Mexican Caesar\". John le tue à Chuparosa (voir la biographie).")},
    {"img": None, "slug": None, "name": "Ignacio Sanchez", "text": two(
        "The president of Mexico, never seen in the game, in whose name Allende governs Nuevo Paraíso. Reyes calls Allende his puppet (see Names). The Blackwater Ledger reports the fall of Sanchez's government a few issues after Allende's death (see Biography).",
        "Le président du Mexique, jamais montré dans le jeu, au nom duquel Allende gouverne le Nuevo Paraíso. Reyes fait d'Allende sa marionnette (voir Noms). Le Blackwater Ledger annonce la chute du gouvernement de Sanchez quelques numéros après la mort d'Allende (voir la biographie).")},
    {"img": None, "slug": None, "name": "Reyes's rebels", "text": two(
        "The rebels fight his army across the province and free the prisoners of his jail in Escalera before storming the mansion (see Biography). After the death of De Santa, Victor, one of them, tells John: \"Allende is scared, and making mistakes.\" The executioner at El Presidio asks Reyes whether he really thought he could overthrow Allende.",
        "Les rebelles combattent son armée dans toute la province et libèrent les détenus de sa prison d'Escalera avant de prendre la demeure d'assaut (voir la biographie). Après la mort de De Santa, Victor, l'un d'eux, confie à John : \"Allende is scared, and making mistakes.\" (Allende a peur, et il commet des erreurs). À El Presidio, le bourreau demande à Reyes s'il croyait vraiment pouvoir renverser Allende.")},
    {"img": None, "slug": None, "name": "Raul Zubieta", "text": two(
        "The army major who holds Reyes prisoner in Escalera on the day of the assault; John kills him in a duel (see Biography). The Red Dead Wiki lists Allende among his affiliations.",
        "Le major de l'armée qui tient Reyes prisonnier à Escalera le jour de l'assaut ; John le tue en duel (voir la biographie). Le Red Dead Wiki range Allende parmi ses affiliations.")},
    {"img": None, "slug": None, "name": "His uncle", "text": two(
        "Not named in the game. Allende mentions him once, as the man whose land Javier's father worked (see Biography). The Red Dead Wiki lists him as his only known relative.",
        "Son nom n'est pas donné. Allende ne l'évoque qu'une fois, comme celui dont le père de Javier travaillait la terre (voir la biographie). Le Red Dead Wiki en fait son seul parent connu.")},
    {"img": None, "slug": None, "name": "Herbert Moon", "text": two(
        "The Armadillo shopkeeper lumps him with the other Mexican leaders in a free-roam line quoted by the Red Dead Wiki: \"Sanchez, Allende, De Santa, Reyes; all the same! They just want Armadillo rail rides.\"",
        "Le commerçant d'Armadillo le met dans le même sac que les autres dirigeants mexicains, dans une réplique d'exploration libre citée par le Red Dead Wiki : \"Sanchez, Allende, De Santa, Reyes; all the same! They just want Armadillo rail rides.\" (Sanchez, Allende, De Santa, Reyes : tous pareils ! Ils ne veulent que le train pour Armadillo).")},
]
