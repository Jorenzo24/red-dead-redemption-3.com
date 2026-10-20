"""Landon Ricketts, part B: Personality (official description, observable traits, In his own words, Names,
Appearance), Gunfighting and weapons, Relationships (20 Oct 2026, medium tier).

Sources (register, read 20 Oct 2026; wiki pages fetched via the Red Dead Wiki API into scripts/v3/work/_m/ and
scripts/v3/work/landon/fc/):
- Rockstar's character descriptions of 6 Sep 2018 (THR) cover the RDR2 Van der Linde gang only; none exists for
  Ricketts.
- Official description: the Red Dead Redemption Game of the Year Edition guide, as quoted in the quote box of the
  Red Dead Wiki EN page "Landon Ricketts" ("Landon is a 50-year-old former star gunslinger..."). The guide itself was
  not read: quoted through the wiki, attributed.
- Transcripts (scripts/v3/work/_m/): "The Gunslinger's Tragedy/dialogues", "Landon Ricketts Rides Again/dialogues",
  "Lucky in Love/dialogues", "The Mexican Wagon Train/dialogues", "We Shall Be Together in Paradise/dialogues" (Irish's
  American in Chuparosa), "Good, Honest, Snake Oil/dialogues" (RDR2 lawman's line).
- Mission pages: "The Gunslinger's Tragedy" (rewards: Schofield Revolver gifted, Dead Eye level 3; fail conditions incl.
  Landon's horse; trivia: Semi-automatic Pistol), "Landon Ricketts Rides Again" (train or horse; "nearly invincible";
  cutscene weapon swaps High Power / Volcanic), "Lucky in Love" (poker and dueling introduced; card on his thigh),
  "The Mexican Wagon Train" (last mission of his strand), "Biographies and Lies" (giver, Boom Bait, UN), "Further
  Questions of Female Suffrage" (Arthur's line, fc/).
- Red Dead Wiki EN "Landon Ricketts": infobox (weapons Cattleman, Schofield, Volcanic, Semi-automatic, High Power;
  family: unnamed wife, dead), Trivia (Schofield preferred but Cattleman seen most; John's camp poker mention in RDR2);
  FR "Landon Ricketts" (speaks Spanish in most of his missions; nickname "Ricketts infecté" for the undead version).
- Fact-checked parts reused as is: jack_B (Ricketts entry and "Landon Ricketts, eat your heart out."), jack_C (Dead
  Eye mention; "My pa knew Landon Ricketts, friend!" stays in jack_C, not quoted here), javier_B (the Emilio exchange),
  sadie_C (Arthur's "A new pair of pants..." line), john_B/john_D.

Ownership (OWNERSHIP.md): the guide description, names, appearance, gameplay (Dead Eye lesson as a mechanic, the gifted
Schofield, his weapons, mission strand, train option, Spanish) and the relationship entries live HERE. Narrative
events (the four missions as stories, the 1896/1899/1902 newspaper past, the 1914 obituary, Undead Nightmare) live
in part A; entries refer to them in one clause.
Lines quoted in this part (parts A and C must NOT repeat them): the GOTY guide description; "Not a name that means
much anymore."; "Living quietly, waiting." / "For what?" / "I don't know, and you?"; "I didn't say I'd become a
coward. I'm not going to stand by and watch good people suffer. They've been beaten down for too long. I give them
some hope."; "Damn right they don't, my sarcastic little apprentice."; "Only a buzzard feeds on his friends.";
"I always thought I'd lived a charmed life. I've known wealth, respect, love, even fame."; "You know, you remind me a
lot of myself. How I used to be. Stubborn and angry."; "My name means something."; "Thank God my wife died. Unlucky in
love, lucky in cards."; "you are the savior of this town" (Ramon); "an old goat like me"; "See if this Schofield makes
a difference. Now that's a real gun."; "A duel is all about timing..." (Lucky in Love); "Landon Ricketts, eat your
heart out." (Jack); "A new pair of pants and you think you're Landon Ricketts" (Arthur); "Killed more than Landon
Ricketts without even pulling a trigger" (RDR2 lawman). Left to part C Quotes: every line of the wiki's Quotes list
(twenty-five years, impasse, strange kind of fame, fighter, fastest, getting older, feed them their balls, self-pity,
peasants, fence, Mexico as home, Chuparosa is my town, executed, Manolo, second chance) and the multiplayer and
Undead Nightmare lines.

WIKI-ONLY (kept, attributed): GOTY description (quote box); weapon list (infobox); Cattleman more often than the
Schofield (trivia); the card on his thigh in "Lucky in Love" (mission trivia, as a description, no "cheat" claim);
John's camp poker mention in RDR2 (trivia, no transcript); "nearly invincible" (mission trivia); weapon swaps in the
dynamite cutscene (mission trivia); Irish's American = Ricketts (link in the wiki's transcript only, presented as such).

Excluded: "calm, principled and world-weary", "kills only when he must" (v2 interpretation, not in any source);
the watery eye "afraid of death" reading (mission trivia speculation); "Ricketts claims he has never been married in
The Gunslinger's Tragedy" (wiki trivia; the line is not in the transcript); the Wyatt Earp, Wild Bill Hickok, Michael
Landon and Lee Van Cleef comparisons (wiki speculation, no source); "a cheat card" (wiki reading); "heavily implied"
(Irish, wiki wording); Ramon's line already said "again" (kept only as "the savior of this town"); the rare glitch
where he shoots horses and the double-Ricketts glitch (bugs, no value); the Calloway dime novel and the RDR2 cigarette
card (part C, Other media); "Landon's Patience" ability card, Myths and Mavericks, Zombie Ricketts as a playable model
(part C); Undead Nightmare in relationship entries (non-canon, part A); horse breed or name (not given anywhere).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the gang of Red Dead Redemption 2 and do not include Ricketts. The Red Dead Wiki quotes the Game of the Year Edition guide of Red Dead Redemption: \"Landon is a 50-year-old former star gunslinger, but now he is past his prime. Holed up in Mexico and awaiting death, he is tough and powerful. But he is also vain and somewhat pretentious.\"",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang de Red Dead Redemption 2 et ne comprennent pas Ricketts. Le Red Dead Wiki cite le guide de l'édition Game of the Year de Red Dead Redemption : \"Landon is a 50-year-old former star gunslinger, but now he is past his prime. Holed up in Mexico and awaiting death, he is tough and powerful. But he is also vain and somewhat pretentious.\" (Landon est un ancien pistolero vedette de 50 ans, aujourd'hui sur le déclin. Retiré au Mexique dans l'attente de la mort, il reste dur et puissant, mais il est aussi vaniteux et un peu prétentieux.)")},
    {"p": two(
        "In Chuparosa he answers the townspeople's calls for help, and the bank employee Ramon tells him: \"you are the savior of this town\". He mocks John's shooting at their first meeting and keeps teasing him on the missions that follow. He bets that he is still the fastest gun. He drinks with John in Chuparosa and plays poker at the cantina. He speaks Spanish with the locals, notably with Emilio Fortuna, and translates for John. In \"The Mexican Wagon Train\" he jokes that some writers and officials need to be killed, then tells Luisa that he was joking. On the same ride he turns hard on John, calls him a rat and reminds him that his own name means something (see Biography).",
        "À Chuparosa, il répond aux appels à l'aide des habitants, et l'employé de banque Ramon lui lance : \"you are the savior of this town\" (vous êtes le sauveur de cette ville). Il se moque du tir de John à leur première rencontre et continue de le taquiner dans les missions suivantes. Il parie qu'il reste la gâchette la plus rapide. Il boit avec John à Chuparosa et joue au poker à la cantina. Il parle espagnol avec les habitants, notamment avec Emilio Fortuna, et sert d'interprète à John. Dans \"The Mexican Wagon Train\", il plaisante en disant que certains écrivains et fonctionnaires méritent la mort, puis assure à Luisa qu'il plaisantait. Pendant la même chevauchée, il se montre dur avec John, le traite de rat et lui rappelle que son nom à lui veut dire quelque chose (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "Asked in \"The Gunslinger's Tragedy\" what he is doing in Mexico, he says: \"Living quietly, waiting.\" John asks: \"For what?\" He answers: \"I don't know, and you?\" When John remarks that the bank wagon fight does not fit a quiet life, he replies: \"I didn't say I'd become a coward. I'm not going to stand by and watch good people suffer. They've been beaten down for too long. I give them some hope.\" John says the townspeople do not know how lucky they are, and Ricketts closes: \"Damn right they don't, my sarcastic little apprentice.\" On the same ride, when John says he is hunting old friends, he comments: \"Only a buzzard feeds on his friends.\"",
        "Quand John lui demande, dans \"The Gunslinger's Tragedy\", ce qu'il fait au Mexique, il répond : \"Living quietly, waiting.\" (je vis tranquillement, j'attends). John : \"For what?\" (quoi donc ?). Lui : \"I don't know, and you?\" (je n'en sais rien, et vous ?). Quand John fait remarquer que l'attaque du chariot de la banque cadre mal avec une vie tranquille, il réplique : \"I didn't say I'd become a coward. I'm not going to stand by and watch good people suffer. They've been beaten down for too long. I give them some hope.\" (je n'ai pas dit que j'étais devenu lâche ; je ne vais pas rester les bras croisés à regarder souffrir des braves gens ; on les écrase depuis trop longtemps ; je leur donne un peu d'espoir). John observe que les habitants ne mesurent pas leur chance, et Ricketts conclut : \"Damn right they don't, my sarcastic little apprentice.\" (ça, c'est sûr, mon petit apprenti sarcastique). Sur la même route, quand John explique qu'il traque d'anciens amis, il glisse : \"Only a buzzard feeds on his friends.\" (il n'y a qu'un vautour pour se nourrir de ses amis).")},
    {"p": two(
        "On the road to the convoy in \"The Mexican Wagon Train\", he tells John: \"You know, you remind me a lot of myself. How I used to be. Stubborn and angry.\" A little later: \"I always thought I'd lived a charmed life. I've known wealth, respect, love, even fame.\"",
        "En route vers le convoi, dans \"The Mexican Wagon Train\", il confie à John : \"You know, you remind me a lot of myself. How I used to be. Stubborn and angry.\" (vous savez, vous me rappelez beaucoup celui que j'étais : têtu et en colère). Un peu plus loin : \"I always thought I'd lived a charmed life. I've known wealth, respect, love, even fame.\" (j'ai toujours pensé avoir eu une vie bénie ; j'ai connu la fortune, le respect, l'amour, et même la gloire).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "He does not give his name at first and tells John that it no longer matters; John calls him old man, before and after learning his name. After the bottle practice he introduces himself: \"Landon Ricketts. Not a name that means much anymore.\" On the way back to town he calls himself \"an old goat like me\" whom he expected to be forgotten. In \"The Mexican Wagon Train\" he tells John: \"My name means something.\" The people of Chuparosa call him Señor Ricketts, and Luisa and John say Mr. Ricketts. In the transcripts John uses his first name once, during the bank wagon fight. The Red Dead Wiki calls the undead version of him Zombie Ricketts; the French wiki gives Ricketts infecté.",
        "Il ne donne pas son nom tout de suite et dit à John que cela n'a plus d'importance ; John l'appelle le vieux, avant comme après avoir appris son nom. Après l'exercice des bouteilles, il se présente : \"Landon Ricketts. Not a name that means much anymore.\" (Landon Ricketts, un nom qui ne dit plus grand-chose à personne). Sur le chemin du retour, il se décrit comme \"an old goat like me\" (un vieux bouc comme moi) qu'il croyait oublié depuis longtemps. Dans \"The Mexican Wagon Train\", il lance à John : \"My name means something.\" (mon nom veut dire quelque chose). Les habitants de Chuparosa l'appellent Señor Ricketts, Luisa et John disent Mr. Ricketts. Dans les transcriptions, John n'emploie son prénom qu'une fois, pendant la fusillade autour du chariot de la banque. Le Red Dead Wiki nomme sa version mort-vivante Zombie Ricketts ; le wiki francophone, Ricketts infecté.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is an old man with a lined face, gray hair falling to his shoulders and a thick gray mustache, with a tuft of beard under the lower lip. In Red Dead Redemption he wears a worn jacket over an open-collared shirt and a hat. The Red Dead Wiki notes a red sash among his clothes.",
        "C'est un vieil homme au visage ridé, aux cheveux gris qui tombent sur les épaules, avec une épaisse moustache grise et une mouche sous la lèvre inférieure. Dans Red Dead Redemption, il porte une veste usée sur une chemise au col ouvert, et un chapeau. Le Red Dead Wiki relève une ceinture d'étoffe rouge dans sa tenue.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Gunfighting and weapons", "Tir et armes")},
    {"h4": two("What he teaches John", "Ce qu'il apprend à John")},
    {"p": two(
        "Ricketts gives the four missions of his strand in Red Dead Redemption, all starting in Chuparosa (see Missions). In the first, \"The Gunslinger's Tragedy\", he hands John a Schofield Revolver with the words \"See if this Schofield makes a difference. Now that's a real gun.\" He tells him to keep his back straight, because a bent back makes the gun jump. The mission unlocks the third level of Dead Eye: the player marks three bottles, then at least two of the vultures Ricketts scares off the rooftops. The Schofield is the mission's reward, with the new Dead Eye level.",
        "Ricketts confie les quatre missions de sa série dans Red Dead Redemption, qui partent toutes de Chuparosa (voir Missions). Dans la première, \"The Gunslinger's Tragedy\", il remet à John un Schofield Revolver en lui disant : \"See if this Schofield makes a difference. Now that's a real gun.\" (voyons si ce Schofield change quelque chose ; ça, c'est une vraie arme). Il lui conseille de garder le dos droit, faute de quoi l'arme saute. La mission débloque le troisième niveau du Dead Eye : le joueur marque trois bouteilles, puis au moins deux des vautours que Ricketts fait s'envoler des toits. Le Schofield est la récompense de la mission, avec ce nouveau niveau de Dead Eye.")},
    {"p": two(
        "\"Lucky in Love\" introduces poker and dueling to the player. On the way to John's duel with Andreas Müller, Ricketts explains: \"A duel is all about timing. If you pull your gun too soon, you'll be less accurate. After you draw, pick your shots carefully, like I showed you.\" In \"Landon Ricketts Rides Again\" the player chooses between taking the train with him to Casa Madrugada and riding there; in the caves he sets the dynamite charge on Luisa's cell door while John covers him. The mission page notes that he is nearly invincible in that mission. Every mission of his strand fails if the player attacks or kills him; three of them also fail if the player abandons him or kills his horse.",
        "\"Lucky in Love\" initie le joueur au poker et au duel. En accompagnant John vers son duel contre Andreas Müller, Ricketts explique : \"A duel is all about timing. If you pull your gun too soon, you'll be less accurate. After you draw, pick your shots carefully, like I showed you.\" (un duel, c'est une affaire de timing ; si vous dégainez trop tôt, vous serez moins précis ; une fois l'arme sortie, choisissez bien vos cibles, comme je vous l'ai montré). Dans \"Landon Ricketts Rides Again\", le joueur choisit entre prendre le train avec lui jusqu'à Casa Madrugada et s'y rendre à cheval ; dans les grottes, il pose la charge de dynamite sur la porte de la cellule de Luisa pendant que John le couvre. La page de la mission précise qu'il y est quasiment invincible. Chaque mission de sa série échoue si le joueur l'attaque ou le tue ; trois d'entre elles échouent aussi si le joueur l'abandonne ou tue son cheval.")},
    {"h4": two("Weapons", "Armes")},
    {"p": two(
        "The Red Dead Wiki lists the Cattleman Revolver, the Schofield Revolver, the Volcanic Pistol, the Semi-automatic Pistol and the High Power Pistol among his weapons. Despite his praise for the Schofield, he is seen with a Cattleman Revolver in most scenes, the wiki notes. According to the mission pages, he sometimes uses a Semi-automatic Pistol in \"The Gunslinger's Tragedy\", and in the dynamite cutscene of \"Landon Ricketts Rides Again\" his Cattleman is sometimes replaced by a High Power Pistol or a Volcanic Pistol. The Red Dead Wiki also points out playing cards on his right thigh when the camera widens as John sits down at the poker table in \"Lucky in Love\".",
        "Le Red Dead Wiki lui attribue le Cattleman Revolver, le Schofield Revolver, le Volcanic Pistol, le Semi-automatic Pistol et le High Power Pistol. Malgré ses éloges du Schofield, il porte un Cattleman Revolver dans la plupart des scènes, relève le wiki. D'après les pages des missions, il utilise parfois un Semi-automatic Pistol dans \"The Gunslinger's Tragedy\", et dans la cinématique de la dynamite de \"Landon Ricketts Rides Again\" son Cattleman est parfois remplacé par un High Power Pistol ou un Volcanic Pistol. Le Red Dead Wiki signale aussi des cartes à jouer posées sur sa cuisse droite quand le plan s'élargit au moment où John s'assoit à la table de poker, dans \"Lucky in Love\".")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": [two(
        "Ricketts watches John kill three bandits on his arrival in Chuparosa in 1911, trains him and rides with him through the four missions of his strand (see Biography). John tells him that stories about him were told when he was a boy, and Ricketts later tells him that all those stories were true. Ricketts calls him partner, Mr. Marston and, once, his sarcastic little apprentice. In \"The Mexican Wagon Train\", John tells him how he left the gang and why he is hunting its former members.",
        "Ricketts voit John abattre trois bandits à son arrivée à Chuparosa en 1911, l'entraîne et chevauche avec lui pendant les quatre missions de sa série (voir la biographie). John lui raconte qu'on parlait de lui quand il était enfant, et Ricketts lui assure plus tard que toutes ces histoires étaient vraies. Ricketts l'appelle partner, Mr. Marston et, une fois, son petit apprenti sarcastique. Dans \"The Mexican Wagon Train\", John lui raconte comment il a quitté le gang et pourquoi il en traque les anciens membres."),
        two("Their last ride ends with a handshake at the border. According to the Red Dead Wiki, John also mentions Ricketts during a poker game at camp in Red Dead Redemption 2.",
            "Leur dernière chevauchée se termine par une poignée de main à la frontière. D'après le Red Dead Wiki, John évoque aussi Ricketts lors d'une partie de poker au camp, dans Red Dead Redemption 2.")]},
    {"img": "luisa-fortuna.jpeg", "slug": "luisa-fortuna", "name": "Luisa Fortuna", "text": two(
        "Ricketts describes Emilio's sister to John as a teacher and a fine young woman, and says the army holds her because she is a rebel close to Reyes. He frees her from her cell in \"Landon Ricketts Rides Again\" and carries her out of the caves. In \"The Mexican Wagon Train\" she finds him drinking with John and asks for help with Allende's prisoners (see Biography). Before leaving, he tells John to talk to her.",
        "Ricketts présente à John la sœur d'Emilio comme une institutrice et une jeune femme de valeur, et explique que l'armée la détient parce qu'elle est une rebelle proche de Reyes. Il la libère de sa cellule dans \"Landon Ricketts Rides Again\" et la porte hors des grottes. Dans \"The Mexican Wagon Train\", elle le trouve en train de boire avec John et lui demande de l'aide au sujet des prisonniers d'Allende (voir la biographie). Avant de partir, il conseille à John d'aller lui parler.")},
    {"img": "agustin-allende.jpeg", "slug": "agustin-allende", "name": "Agustin Allende", "text": two(
        "At their first meeting Ricketts describes the colonel to John as the head of a foul local government who runs the region like a feudal king. Ricketts fights his soldiers to free Luisa and the prisoners of the convoy (see Biography).",
        "Dès leur première rencontre, Ricketts présente le colonel à John comme le chef d'un gouvernement local infâme, qui dirige la région comme un roi féodal. Ricketts affronte ses soldats pour libérer Luisa, puis les prisonniers du convoi (voir la biographie).")},
    {"img": "abraham-reyes.jpeg", "slug": "abraham-reyes", "name": "Abraham Reyes", "text": two(
        "Ricketts never meets the rebel leader on screen. At his first meeting with John he speaks of another local man promising the peasants their freedom, like the two or three before him, without giving a name. In \"Landon Ricketts Rides Again\" he names Reyes as the rebel leader Luisa is close to.",
        "Ricketts ne croise jamais le chef rebelle à l'écran. Lors de sa première rencontre avec John, il parle d'un énième homme du pays qui promet la liberté aux paysans, comme les deux ou trois précédents, sans donner de nom. Dans \"Landon Ricketts Rides Again\", il nomme Reyes comme le chef rebelle dont Luisa est proche.")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Ricketts helps John look for him in Chuparosa. In \"Landon Ricketts Rides Again\" he relays John's questions about him to Emilio Fortuna, then asks Luisa whether a Javier Escuella was among her jailers, and concludes that Javier is still in Mexico. In \"The Mexican Wagon Train\" he has no news of him.",
        "Ricketts aide John à le rechercher à Chuparosa. Dans \"Landon Ricketts Rides Again\", il transmet à Emilio Fortuna les questions de John à son sujet, puis demande à Luisa si un certain Javier Escuella faisait partie de ses geôliers, et en conclut que Javier est toujours au Mexique. Dans \"The Mexican Wagon Train\", il n'a aucune nouvelle de lui.")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "John names Bill to Ricketts as one of the two men he is after. In \"Landon Ricketts Rides Again\", Ricketts says he has heard that John's recent encounters with Bill did not go his way.",
        "John cite Bill à Ricketts comme l'un des deux hommes qu'il recherche. Dans \"Landon Ricketts Rides Again\", Ricketts dit avoir entendu que les récentes rencontres de John avec Bill n'avaient pas tourné à son avantage.")},
    {"img": "irish.jpeg", "slug": "irish", "name": "Irish", "text": two(
        "In \"We Shall Be Together in Paradise\", before leaving John in Mexico, Irish says he once met an American in Chuparosa, saw him shoot a man and drank with him. The game does not name this American; the Red Dead Wiki's transcript links him to Ricketts.",
        "Dans \"We Shall Be Together in Paradise\", avant de laisser John au Mexique, Irish raconte avoir rencontré un Américain à Chuparosa, l'avoir vu abattre un homme et avoir bu avec lui. Le jeu ne nomme pas cet Américain ; la transcription du Red Dead Wiki le relie à Ricketts.")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "Jack never meets Ricketts on screen, but his 1914 voice lines name him, among them, after a kill in Dead Eye: \"Landon Ricketts, eat your heart out.\"",
        "Jack ne croise jamais Ricketts à l'écran, mais ses répliques de 1914 le citent, notamment après un tir en Dead Eye : \"Landon Ricketts, eat your heart out\" (Landon Ricketts peut aller se rhabiller).")},
    {"img": "sadie-adler.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
        "In \"Further Questions of Female Suffrage\" (Red Dead Redemption 2), after Sadie starts the gunfight with the Lemoyne Raiders, Arthur tells her: \"A new pair of pants and you think you're Landon Ricketts\".",
        "Dans \"Further Questions of Female Suffrage\" (Red Dead Redemption 2), après que Sadie a déclenché la fusillade contre les Lemoyne Raiders, Arthur lui lance : \"A new pair of pants and you think you're Landon Ricketts\" (un pantalon neuf, et tu te prends pour Landon Ricketts).")},
    {"img": None, "slug": None, "name": "His wife", "text": two(
        "The games do not name her. In \"Lucky in Love\", winning at the poker table, Ricketts says: \"Thank God my wife died. Unlucky in love, lucky in cards.\" The Red Dead Wiki dates her death to before 1911, cause unknown.",
        "Les jeux ne lui donnent pas de nom. Dans \"Lucky in Love\", en pleine série de gains au poker, Ricketts lance : \"Thank God my wife died. Unlucky in love, lucky in cards.\" (Dieu merci, ma femme est morte : malheureux en amour, heureux au jeu). Le Red Dead Wiki situe sa mort avant 1911, sans cause connue.")},
    {"img": None, "slug": None, "name": "Emilio Fortuna", "text": two(
        "Luisa's brother is talking with Ricketts at the hotel when John arrives in \"Landon Ricketts Rides Again\". He cannot say whether the Escuella he heard of is Javier (see Javier Escuella).",
        "Le frère de Luisa discute avec Ricketts à l'hôtel quand John arrive, dans \"Landon Ricketts Rides Again\". Il ne sait pas dire si l'Escuella dont il a entendu parler est Javier (voir Javier Escuella).")},
    {"img": None, "slug": None, "name": "Carlos", "text": two(
        "Ricketts has been told that this butcher of El Matadero can help them reach Luisa. Carlos distracts the guards at the caves, leaves horses for the escape and takes Luisa away at the end (see Biography).",
        "On a indiqué à Ricketts que ce boucher d'El Matadero pourrait les aider à rejoindre Luisa. Carlos détourne l'attention des gardes devant les grottes, laisse des chevaux pour la fuite et emmène Luisa à la fin (voir la biographie).")},
    {"img": None, "slug": None, "name": "Andreas Müller", "text": two(
        "Ricketts plays poker with this German silver prospector at the Chuparosa cantina and teases him at the table. When Müller accuses John of cheating and draws, Ricketts tries to calm him down; John then kills him in a duel, and Ricketts says Müller always played his cards too early (see Biography).",
        "Ricketts joue au poker avec ce prospecteur d'argent allemand à la cantina de Chuparosa et le raille à table. Quand Müller accuse John de tricher et dégaine, Ricketts tente de le calmer ; John le tue ensuite en duel, et Ricketts remarque que Müller a toujours abattu ses cartes trop tôt (voir la biographie).")},
    {"img": None, "slug": None, "name": "Ramon", "text": two(
        "This man of Chuparosa runs to Ricketts when bandits attack the bank wagon in \"The Gunslinger's Tragedy\" and asks for his help \"again\". Ricketts calls him by name and promises to take care of it.",
        "Cet habitant de Chuparosa accourt auprès de Ricketts quand des bandits attaquent le chariot de la banque, dans \"The Gunslinger's Tragedy\", et lui demande son aide \"again\" (une fois de plus). Ricketts l'appelle par son prénom et promet de s'en occuper.")},
]
