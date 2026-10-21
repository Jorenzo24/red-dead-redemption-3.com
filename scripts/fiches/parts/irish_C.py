"""Irish, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/, copies in
scripts/v3/work/irish/fc/):
- Character page "Irish" (Mission appearances, Quotes, Trivia, Gallery captions) and FR page "L'Irlandais"
  (Anecdotes), irish/en.txt and irish/fr.txt.
- Mission pages (infobox rewards, order numbers, prerequisites, unlocks, trivia): "A Frenchman, a Welshman and an
  Irishman" (19th mission), "Man is Born Unto Trouble" (20th), "On Shaky's Ground" (21st), "The Assault on Fort
  Mercer" (24th), "We Shall Be Together in Paradise" (25th); "Liars, Cheats and Other Proud Americans" (opens the
  Irish strand).
- Transcripts used word for word for every mission quote: "A Frenchman, a Welshman and an Irishman/dialogues", "Man
  is Born Unto Trouble/dialogues", "On Shaky's Ground/dialogues", "The Assault on Fort Mercer/dialogues", "We Shall
  Be Together in Paradise/dialogues"; mentions: "Liars, Cheats and Other Proud Americans/dialogues", "The Sport of
  Kings, and Liars/dialogues", "A Gentle Drive with Friends/dialogue". "Irish/Quotes" (optional ride conversations
  and the multiplayer taunts, no transcript).
- Other pages: "Liars and Cheats" (released September 21, 2010; Irish in the Damnation list), "Shaky" (Red Dead
  Online stranger, 1898), "Kent Gallaway" line (trivia of the "A Frenchman..." dialogue page).
- Real world: Liars and Cheats Pack detailed by Rockstar on August 27, 2010 and released on September 21, 2010 (as in
  allende_C, bonnie_C, nigel_C); RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024 without multiplayer
  (as in allende_C, leigh_C, seth_C). Lily of the West: traditional ballad (mission page trivia, Wikipedia link
  given by the wiki).

VERIFIED POINTS: the song line is "I love me faithless Flora, the Lily of the West" in the transcript (the
character page's trivia writes "precious Flora"); "Christ, the church has more money than anyboy!" is a typo of
the transcript, quoted as "anybody"; the "Hold on! Hold on...I missed it." line is the only line of Irish in the
Fort Mercer transcript before the fight is over; the Fort Mercer mission page lists Irish in the posse in its
summary and notes in its trivia that he is seen in the opening cutscene (both given as the page's statements;
HOUSE_FACTS: he misses the fight); "Think you're a real hard-case, don't you?" is in the wiki's multiplayer list
for Irish and, per the dialogue page's trivia, also said by Kent Gallaway at the lake cabin.

EXCLUDED: the Dublin origin (inference from "west of Dublin"); the Cork origin from "shitehawk" (not in any
transcript); the Damnation section "due to his crimes" (wiki speculation); the Uncle comparison (interpretation);
the "born fighting" line as a prophecy of his death (interpretation); "Irish cowers" (mission page caption,
contradicted by its own trivia); the Myths and Mavericks gallery caption (no other source); the raft-fire,
falling-off-the-cliff and floating-raft glitches (minor bugs); the El Rato translation note (part B, Names); the
Spanish word Irish asks for (no value beyond the transcript line); the "Far Away" song after the crossing (not
about Irish); the Herald.ie criticism (part D, Reception).

OWNERSHIP: narrative events live in part A (one line per mission here). The two newspapers (Ledger No. 56 notices
and article, Ledger & Sentinel No. 213 notice) are told in part A only. Lines left to part B "In his own words"
and Names, and therefore NOT quoted here: "It's the whiskey, sir...", "They said God invented whiskey...", "Down
here, they call me El Rato...", "You're an angry and a feck ugly man; but not a bad one.", "I'm a good Catholic
boy.", "I woke up with me head in a pair of tits...". If part B uses a line quoted below, the fixer removes it from
one place.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A1 = two("Act I: New Austin", "Acte I : New Austin")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Irish has a strand of three story missions in the first act of Red Dead Redemption, numbered 19 to 21 in the story order. The first, \"A Frenchman, a Welshman and an Irishman\", becomes available after Nigel West Dickens's \"Liars, Cheats and Other Proud Americans\". His strand is one of the four that must be completed before Leigh Johnson's \"The Assault on Fort Mercer\", with those of Johnson, Dickens and Seth Briars. He also gives \"We Shall Be Together in Paradise\", the 25th mission, which opens Nuevo Paraíso and the second act. He has no mission in Undead Nightmare.",
              "Irish propose une série de trois missions principales dans le premier acte de Red Dead Redemption, numérotées de 19 à 21 dans l'ordre de l'histoire. La première, \"A Frenchman, a Welshman and an Irishman\", se débloque après \"Liars, Cheats and Other Proud Americans\", une mission de Nigel West Dickens. Sa série fait partie des quatre à boucler avant \"The Assault on Fort Mercer\", la mission de Leigh Johnson, avec celles de Johnson, de Dickens et de Seth Briars. Il confie aussi \"We Shall Be Together in Paradise\", la 25e mission, qui ouvre le Nuevo Paraíso et le deuxième acte. Il n'a aucune mission dans Undead Nightmare.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Irish's role", "Rôle d'Irish")], "rows": [
        M("A Frenchman, a Welshman and an Irishman", A1,
          "Mission giver. Saved by John from French and Welsh in Armadillo, then leads him to an empty cabin on Lake Don Julio. Rewards: 50 fame and 100 honor; the Double-barreled Shotgun is dropped at the cabin.",
          "Donneur de mission. Sauvé par John des mains de French et de Welsh à Armadillo, il le conduit à une cabane vide au bord du lac Don Julio. Récompenses : 50 points de célébrité et 100 d'honneur ; le fusil de chasse à deux coups est récupéré à la cabane."),
        M("Man is Born Unto Trouble", A1,
          "Mission giver. Takes John from Benedict Point to the Gaptooth Breach mine and works the lift that brings up the Gatling gun. Rewards: 250 fame; unlocks the Gaptooth Breach hideout and parts 2 and 3 of the stranger mission \"Funny Man\".",
          "Donneur de mission. Emmène John de Benedict Point à la mine de Gaptooth Breach et actionne le monte-charge qui remonte la Gatling. Récompenses : 250 points de célébrité ; débloque la planque de Gaptooth Breach et les parties 2 et 3 de la mission d'inconnu \"Funny Man\"."),
        M("On Shaky's Ground", A1,
          "Mission giver. Leads John to Shaky's warehouse in Thieves' Landing, then drives the ammunition wagon to MacFarlane's Ranch. Reward: 150 fame.",
          "Donneur de mission. Conduit John jusqu'à l'entrepôt de Shaky à Thieves' Landing, puis mène le chariot de munitions jusqu'au MacFarlane's Ranch. Récompense : 150 points de célébrité."),
        M("The Assault on Fort Mercer", A1,
          "Supplied the Gatling gun but arrives after the fight; offers to take John to Mexico.",
          "A fourni la Gatling mais arrive après le combat ; propose à John de l'emmener au Mexique."),
        M("We Shall Be Together in Paradise", A1,
          "Mission giver. Takes John down the San Luis River by raft under fire and leaves him in Nuevo Paraíso. Rewards: 150 fame and access to Nuevo Paraíso; unlocks the strands of Landon Ricketts and Vincente de Santa.",
          "Donneur de mission. Fait descendre le San Luis à John sur son radeau, sous les balles, et le laisse au Nuevo Paraíso. Récompenses : 150 points de célébrité et accès au Nuevo Paraíso ; débloque les séries de Landon Ricketts et de Vincente de Santa."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Link with Irish", "Lien avec Irish")], "rows": [
        M("Liars, Cheats and Other Proud Americans", A1,
          "[[nigel-west-dickens|Dickens]] sends John to Irish for heavy firepower.",
          "[[nigel-west-dickens|Dickens]] envoie John voir Irish pour obtenir une grosse puissance de feu."),
        M("A Gentle Drive with Friends", A1,
          "[[seth-briars|Seth]] relays Dickens's message that the machine gun has no ammunition, if John already has it.",
          "[[seth-briars|Seth]] transmet le message de Dickens : la mitrailleuse n'a pas de munitions, si John l'a déjà."),
        M("The Sport of Kings, and Liars", A1,
          "Dickens waits for Seth and Irish to deliver their part; John calls Irish the drunk of the team.",
          "Dickens attend que Seth et Irish remplissent leur part ; John voit en Irish l'ivrogne de l'équipe."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the transcripts of the Red Dead Wiki. Lines from optional conversations and multiplayer come from the wiki's list of his lines, as no transcript exists for them.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Celles des conversations facultatives et du multijoueur proviennent de la liste de ses répliques publiée par le wiki, faute de transcription.")},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("Irish, I've met enough men like you to last me a lifetime.", "Irish, I've met enough men like you to last me a lifetime."),
         "src": two("John Marston, A Frenchman, a Welshman and an Irishman (RDR1, Act I), on the ride to the lake",
                    "John Marston, A Frenchman, a Welshman and an Irishman (RDR1, acte I), sur la route du lac. Traduction : « Irish, des types comme toi, j'en ai assez croisé pour toute une vie. »")},
        {"q": two("You and West Dickens are so crooked, you could swallow nails and spit out corkscrews.", "You and West Dickens are so crooked, you could swallow nails and spit out corkscrews."),
         "src": two("John Marston, Man is Born Unto Trouble (RDR1, Act I), when Irish tells him about the miners' machine gun",
                    "John Marston, Man is Born Unto Trouble (RDR1, acte I), quand Irish lui parle de la mitrailleuse des mineurs. Traduction : « Toi et West Dickens, vous êtes si tordus que vous pourriez avaler des clous et recracher des tire-bouchons. »")},
        {"q": two("Ladies, I'm sorry about this man. He's unfortunately lost his mind to the demon drink. At least I hope he has and he wasn't this stupid all along.", "Ladies, I'm sorry about this man. He's unfortunately lost his mind to the demon drink. At least I hope he has and he wasn't this stupid all along."),
         "src": two("John Marston, On Shaky's Ground (RDR1, Act I), to the two nuns",
                    "John Marston, On Shaky's Ground (RDR1, acte I), aux deux religieuses. Traduction : « Mesdames, je suis désolé pour cet homme. Le démon de la boisson lui a hélas fait perdre la tête. Du moins je l'espère, et j'espère qu'il n'a pas toujours été aussi bête. »")},
        {"q": two("You always miss all the drama. There must be cobwebs growin' on that holster of yours.", "You always miss all the drama. There must be cobwebs growin' on that holster of yours."),
         "src": two("John Marston, On Shaky's Ground (RDR1, Act I), on the wagon, after Irish says he is sorry he missed the fight",
                    "John Marston, On Shaky's Ground (RDR1, acte I), sur le chariot, quand Irish regrette d'avoir manqué la fusillade. Traduction : « Tu rates toujours le spectacle. Ton étui doit être couvert de toiles d'araignée. »")},
        {"q": two("This is the fourth time your so-called friends have nearly got me killed. I thought you said they loved you over here?", "This is the fourth time your so-called friends have nearly got me killed. I thought you said they loved you over here?"),
         "src": two("John Marston, We Shall Be Together in Paradise (RDR1, Act I), during a lull in the attack on the raft",
                    "John Marston, We Shall Be Together in Paradise (RDR1, acte I), pendant une accalmie de l'attaque du radeau. Traduction : « C'est la quatrième fois que tes soi-disant amis manquent de me faire tuer. Tu ne disais pas qu'ils t'adoraient, par ici ? »")},
    ]},
    {"h4": two("Red Dead Redemption, Act I", "Red Dead Redemption, acte I")},
    {"quotes": [
        {"q": two("You got it all wrong, Welsh! All wrong. It was French! I promise. He said he was gonna rip you off, and now he's rippin' me off!", "You got it all wrong, Welsh! All wrong. It was French! I promise. He said he was gonna rip you off, and now he's rippin' me off!"),
         "src": two("A Frenchman, a Welshman and an Irishman (RDR1, Act I), with his head held over the trough",
                    "A Frenchman, a Welshman and an Irishman (RDR1, acte I), la tête au-dessus de l'abreuvoir. Traduction : « Tu te trompes, Welsh ! Tu te trompes du tout au tout. C'était French ! Je te le jure. Il disait qu'il allait te rouler, et maintenant c'est moi qu'il roule ! »")},
        {"q": two("I can't thank you enough for taking care of those two degenerates. Untrustworthy, poor in personal hygiene, and lackin' in the finer qualities of a gentleman.", "I can't thank you enough for taking care of those two degenerates. Untrustworthy, poor in personal hygiene, and lackin' in the finer qualities of a gentleman."),
         "src": two("A Frenchman, a Welshman and an Irishman (RDR1, Act I), after John has killed French and Welsh",
                    "A Frenchman, a Welshman and an Irishman (RDR1, acte I), après la mort de French et de Welsh. Traduction : « Je ne vous remercierai jamais assez de m'avoir débarrassé de ces deux dégénérés. Pas fiables, pas très portés sur l'hygiène, et dépourvus des qualités qui font un gentleman. »")},
        {"q": two("Aaah... I'll cover you from the ridge... I'm better from long range. It'll be a piece of cake, fella. Trust me.", "Aaah... I'll cover you from the ridge... I'm better from long range. It'll be a piece of cake, fella. Trust me."),
         "src": two("A Frenchman, a Welshman and an Irishman (RDR1, Act I), above the cabin, when John asks for his help",
                    "A Frenchman, a Welshman and an Irishman (RDR1, acte I), au-dessus de la cabane, quand John lui demande son aide. Traduction : « Aaah... je vais te couvrir depuis la crête... Je suis meilleur de loin. Ce sera du gâteau, mon gars. Fais-moi confiance. »")},
        {"q": two("The entrance is plain to see and there's a shaft them bastards use to haul out heavy ore. We, I mean you, can use that lift to get you and the gun to the surface. I'd do it all meself, but the mines play havoc with me sinuses.", "The entrance is plain to see and there's a shaft them bastards use to haul out heavy ore. We, I mean you, can use that lift to get you and the gun to the surface. I'd do it all meself, but the mines play havoc with me sinuses."),
         "src": two("Man is Born Unto Trouble (RDR1, Act I), outside the Gaptooth Breach mine",
                    "Man is Born Unto Trouble (RDR1, acte I), devant la mine de Gaptooth Breach. Traduction : « L'entrée se voit de loin, et il y a un puits que ces salauds utilisent pour remonter le minerai. On peut, je veux dire tu peux, prendre ce monte-charge pour te remonter avec la mitrailleuse. J'irais bien moi-même, mais les mines me détraquent les sinus. »")},
        {"q": two("Ah, there she is, what a beautiful weapon... God's own gun, ain't that the truth...", "Ah, there she is, what a beautiful weapon... God's own gun, ain't that the truth..."),
         "src": two("Man is Born Unto Trouble (RDR1, Act I), when the lift brings up the Gatling gun",
                    "Man is Born Unto Trouble (RDR1, acte I), quand le monte-charge remonte la Gatling. Traduction : « Ah, la voilà, quelle arme magnifique... Le fusil du bon Dieu, et c'est bien la vérité... »")},
        {"q": two("Irish: And you're a hypocrite, Marston. You've robbed just as many innocent folks as me. / John: I tried to only rob those who had more than they deserved. / Irish: Christ, the church has more money than anybody!", "Irish: And you're a hypocrite, Marston. You've robbed just as many innocent folks as me. / John: I tried to only rob those who had more than they deserved. / Irish: Christ, the church has more money than anybody!"),
         "src": two("On Shaky's Ground (RDR1, Act I), walking through Thieves' Landing after the nuns",
                    "On Shaky's Ground (RDR1, acte I), dans les rues de Thieves' Landing, après l'épisode des religieuses. Traduction : « Irish : Et toi, t'es un hypocrite, Marston. T'as volé autant d'innocents que moi. / John : J'essayais de ne voler que ceux qui avaient plus qu'ils ne méritaient. / Irish : Bon Dieu, l'Église a plus d'argent que n'importe qui ! »")},
        {"q": two("Labour relations don't sound like they're exactly... at an all-time high. You sneak in and get poor Shaky loose. I'll go get the wagon... Good luck, Marston. He's a good man, that Shaky.", "Labour relations don't sound like they're exactly... at an all-time high. You sneak in and get poor Shaky loose. I'll go get the wagon... Good luck, Marston. He's a good man, that Shaky."),
         "src": two("On Shaky's Ground (RDR1, Act I), outside the warehouse door, as Shaky is being beaten",
                    "On Shaky's Ground (RDR1, acte I), devant la porte de l'entrepôt, pendant que Shaky se fait tabasser. Traduction : « On dirait que les relations sociales ne sont pas exactement... au beau fixe. Tu te glisses à l'intérieur et tu libères ce pauvre Shaky. Moi, je vais chercher le chariot... Bonne chance, Marston. C'est un brave type, ce Shaky. »")},
        {"q": two("Someone's gotta drive the wagon, don't they? Team work, Johnny boy. That's my game. Not just the glory, like you.", "Someone's gotta drive the wagon, don't they? Team work, Johnny boy. That's my game. Not just the glory, like you."),
         "src": two("On Shaky's Ground (RDR1, Act I), when John says he always misses the action",
                    "On Shaky's Ground (RDR1, acte I), quand John lui reproche de toujours manquer l'action. Traduction : « Faut bien que quelqu'un conduise le chariot, non ? L'esprit d'équipe, Johnny. Moi, c'est mon truc. Pas comme toi, qui ne penses qu'à la gloire. »")},
        {"q": two("Er, yes. Of course. What am I thinkin'? Don't worry, you can count on me. I just hope I don't steal all your glory. Wouldn't be right or proper.", "Er, yes. Of course. What am I thinkin'? Don't worry, you can count on me. I just hope I don't steal all your glory. Wouldn't be right or proper."),
         "src": two("On Shaky's Ground (RDR1, Act I), when John tells him he will fight at Fort Mercer",
                    "On Shaky's Ground (RDR1, acte I), quand John lui annonce qu'il combattra à Fort Mercer. Traduction : « Euh, oui. Bien sûr. Où avais-je la tête ? T'inquiète, tu peux compter sur moi. J'espère juste ne pas te voler toute la gloire. Ce ne serait pas correct. »")},
        {"q": two("Chupa-feckin-rosa? Oh, I'll take you there, John. I'm real popular down there. You just meet me at the ferry. I've got lots of friends down South.", "Chupa-feckin-rosa? Oh, I'll take you there, John. I'm real popular down there. You just meet me at the ferry. I've got lots of friends down South."),
         "src": two("The Assault on Fort Mercer (RDR1, Act I), after the prisoner names Chuparosa",
                    "The Assault on Fort Mercer (RDR1, acte I), quand le prisonnier cite Chuparosa. Traduction : « Chupa-foutue-rosa ? Oh, je vais t'y emmener, John. Là-bas, tout le monde m'adore. Retrouve-moi au bac. J'ai plein d'amis dans le Sud. »")},
        {"q": two("Irish: I know we ain't exactly old pals, but, y'know...have I ever done you wrong? / Marston: No, but not through lack of trying.", "Irish: I know we ain't exactly old pals, but, y'know...have I ever done you wrong? / Marston: No, but not through lack of trying."),
         "src": two("We Shall Be Together in Paradise (RDR1, Act I), at Brittlebrush Trawl",
                    "We Shall Be Together in Paradise (RDR1, acte I), à Brittlebrush Trawl. Traduction : « Irish : Je sais qu'on n'est pas vraiment de vieux copains, mais bon... je t'ai déjà fait du tort ? / Marston : Non, mais ce n'est pas faute d'avoir essayé. »")},
        {"q": two("Irish: I came into this world fightin'. And I'll go out of it fightin'! / Marston: I expect you'll go out of it pissin' your pants.", "Irish: I came into this world fightin'. And I'll go out of it fightin'! / Marston: I expect you'll go out of it pissin' your pants."),
         "src": two("We Shall Be Together in Paradise (RDR1, Act I), under fire on the raft",
                    "We Shall Be Together in Paradise (RDR1, acte I), sous le feu, sur le radeau. Traduction : « Irish : Je suis venu au monde en me battant, et je le quitterai en me battant ! / Marston : Je te vois plutôt le quitter en pissant dans ton froc. »")},
    ]},
    {"h4": two("Optional conversation (ride to the lake)", "Conversation facultative (route du lac)")},
    {"quotes": [
        {"q": two("Better watch your mouth, me friend. I've cut out a man's tongue for less. ... It was just a joke, fella.", "Better watch your mouth, me friend. I've cut out a man's tongue for less. ... It was just a joke, fella."),
         "src": two("A Frenchman, a Welshman and an Irishman (RDR1, Act I), according to the Red Dead Wiki's list of his lines",
                    "A Frenchman, a Welshman and an Irishman (RDR1, acte I), d'après la liste de ses répliques du Red Dead Wiki. Traduction : « Fais gaffe à ce que tu dis, mon ami. J'ai coupé la langue d'un homme pour moins que ça. ... C'était pour rire, mon gars. »")},
    ]},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"quotes": [
        {"q": two("Nobody shoots at Irish and lives!", "Nobody shoots at Irish and lives!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Personne ne tire sur Irish et ne vit pour le raconter ! »")},
        {"q": two("Me ma could shoot better than you!", "Me ma could shoot better than you!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Ma mère tire mieux que toi ! »")},
        {"q": two("Ain't you got some peckers to be suckin'?", "Ain't you got some peckers to be suckin'?"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « T'as pas mieux à faire, genre sucer des queues ? »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("The title \"A Frenchman, a Welshman and an Irishman\" plays on the European jokes that start with an Englishman, an Irishman and a Scotsman, whose nationalities change with the country telling them. The title \"Man is Born Unto Trouble\" comes from the Book of Job (5:7): \"Yet man is born unto trouble, as the sparks fly upward.\" According to its mission page, \"We Shall Be Together in Paradise\" refers both to the promise of paradise made to one of the two criminals crucified with Jesus and to Nuevo Paraíso, where the mission leads.",
            "Le titre \"A Frenchman, a Welshman and an Irishman\" reprend les histoires drôles européennes qui commencent par un Anglais, un Irlandais et un Écossais, et dont les nationalités changent selon le pays où on les raconte. Le titre \"Man is Born Unto Trouble\" vient du livre de Job (5:7) : \"Yet man is born unto trouble, as the sparks fly upward\" (l'homme naît pour souffrir, comme l'étincelle pour voler). D'après sa page de mission, \"We Shall Be Together in Paradise\" renvoie à la fois au paradis promis à l'un des deux malfaiteurs crucifiés avec Jésus et au Nuevo Paraíso, où mène la mission."),
        two("On the way to the Gaptooth Breach mine, Irish sings \"I love me faithless Flora, the Lily of the West\" (transcript wording; the character page gives \"precious Flora\"). \"Lily of the West\" is a traditional ballad. According to the mission page, it comes from the west of Ireland, where the woman is called Flora, while the version popular in the United States names her Mary.",
            "Sur la route de la mine de Gaptooth Breach, Irish chante \"I love me faithless Flora, the Lily of the West\" (texte de la transcription ; la page du personnage écrit \"precious Flora\"). \"Lily of the West\" est une ballade traditionnelle. D'après la page de la mission, elle vient de l'ouest de l'Irlande, où la femme s'appelle Flora, alors que la version répandue aux États-Unis la nomme Mary."),
        two("The page of \"The Assault on Fort Mercer\" lists Irish among the posse in its summary, and its trivia notes that he can be seen next to John in the opening cutscene, although he takes no part in the fight.",
            "La page de \"The Assault on Fort Mercer\" compte Irish parmi les membres de l'expédition dans son résumé, et ses anecdotes signalent qu'on l'aperçoit à côté de John dans la cinématique d'ouverture, alors qu'il ne prend aucune part au combat."),
        two("According to the page of \"On Shaky's Ground\", the order of the missions allows a mismatch: Seth can still pass on the message that the gun has no ammunition after John has already fetched it with Irish.",
            "D'après la page de \"On Shaky's Ground\", l'ordre des missions permet une incohérence : Seth peut encore transmettre le message selon lequel la mitrailleuse n'a pas de munitions alors que John est déjà allé les chercher avec Irish."),
        two("According to the Red Dead Wiki, if the player shoots at Irish before one of his missions, he either fires back or runs away, and he cannot be killed. After \"We Shall Be Together in Paradise\", he can be killed, but only by a very quick player, often with Dead Eye; otherwise he disappears for good. After \"On Shaky's Ground\", a player who catches up with his wagon and climbs back on makes him flee, and he can then be killed or hogtied.",
            "D'après le Red Dead Wiki, si le joueur tire sur Irish avant l'une de ses missions, il riposte ou s'enfuit, et il est impossible de le tuer. Après \"We Shall Be Together in Paradise\", on peut l'abattre, mais seulement en étant très rapide, souvent avec le Dead Eye ; sinon, il disparaît pour de bon. Après \"On Shaky's Ground\", un joueur qui rattrape son chariot et remonte dessus le fait fuir, et peut alors le tuer ou le ligoter."),
        two("According to the Red Dead Wiki, when Irish puts his revolver away in \"We Shall Be Together in Paradise\", the game plays a holstering animation, and the gun then reappears tucked in the front of his trousers.",
            "D'après le Red Dead Wiki, quand Irish range son revolver dans \"We Shall Be Together in Paradise\", le jeu joue l'animation d'un rangement dans un étui, puis l'arme réapparaît glissée à l'avant de son pantalon."),
        two("\"Think you're a real hard-case, don't you?\", one of Irish's multiplayer taunts, is also shouted by Kent Gallaway, one of the gunmen at the Lake Don Julio cabin, if he survives a few seconds.",
            "\"Think you're a real hard-case, don't you?\" (tu te crois coriace, hein ?), l'une des provocations d'Irish en multijoueur, est aussi lancée par Kent Gallaway, l'un des hommes armés de la cabane du lac Don Julio, s'il survit quelques secondes."),
        two("According to its mission page, \"We Shall Be Together in Paradise\" belongs to the New Austin missions but is counted as a Nuevo Paraíso mission in the game's statistics.",
            "D'après sa page de mission, \"We Shall Be Together in Paradise\" fait partie des missions du New Austin, mais les statistiques du jeu la comptent parmi celles du Nuevo Paraíso."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Irish became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. Players select him in the Damnation section of the Outfitter, with [[abraham-reyes|Abraham Reyes]], [[agustin-allende|Agustin Allende]], [[bill-williamson|Bill Williamson]], [[dutch-van-der-linde|Dutch van der Linde]], [[edgar-ross|Edgar Ross]] and [[harold-macdougal|Harold MacDougal]]. According to the Red Dead Wiki, his multiplayer model carries its revolver in a holster on the hip, and the wiki lists 29 taunts for him, a few of which are quoted above. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, do not include the multiplayer mode.",
              "Irish devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. On le choisit dans la section Damnation de l'Outfitter, aux côtés d'[[abraham-reyes|Abraham Reyes]], d'[[agustin-allende|Agustin Allende]], de [[bill-williamson|Bill Williamson]], de [[dutch-van-der-linde|Dutch van der Linde]], d'[[edgar-ross|Edgar Ross]] et d'[[harold-macdougal|Harold MacDougal]]. D'après le Red Dead Wiki, son modèle multijoueur porte son revolver dans un étui à la hanche, et le wiki lui recense 29 provocations, dont quelques-unes sont citées plus haut. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, ne comprennent pas le multijoueur.")},
    {"h4": two("Red Dead Redemption 2 and Red Dead Online", "Red Dead Redemption 2 et Red Dead Online")},
    {"p": two("Irish does not appear in Red Dead Redemption 2 or Red Dead Online. His contact Shaky does: according to the Red Dead Wiki, Shaky is a stranger in Red Dead Online, set in 1898, where he gives the player paid jobs in Thieves' Landing.",
              "Irish n'apparaît ni dans Red Dead Redemption 2 ni dans Red Dead Online. Son contact Shaky, si : d'après le Red Dead Wiki, il fait partie des inconnus de Red Dead Online, dont l'action se situe en 1898, et confie au joueur des contrats rémunérés à Thieves' Landing.")},
]
