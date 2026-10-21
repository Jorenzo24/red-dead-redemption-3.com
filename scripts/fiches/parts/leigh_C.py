"""Leigh Johnson, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN, fetched Oct 2026; shared cache scripts/v3/work/_m/, copies in
scripts/v3/work/leigh/fc/):
- Character page "Leigh Johnson" (Mission appearances, Quotes, Trivia, Gallery captions) and FR page (Apparitions
  dans les missions, Anecdotes).
- Mission pages (infobox rewards, order numbers, prerequisites, unlocks, new game elements, failure conditions,
  trivia): "Political Realities in Armadillo" (8th mission), "Justice in Pike's Basin" (9th), "Spare the Rod, Spoil the
  Bandit" (11th), "Hanging Bonnie MacFarlane" (23rd), "The Assault on Fort Mercer" (24th, last mission of New Austin),
  "Dinner for Two" (Undead Nightmare side mission, no transcript on the wiki), "We Shall Be Together in Paradise"
  (follows Fort Mercer), "Obstacles in Our Path", "Women and Cattle", "The Burning", "Old Swindler Blues", "The Sport of
  Kings, and Liars", "Let the Dead Bury Their Dead" (prerequisite links).
- Transcripts used word for word for every mission quote: "Political Realities in Armadillo/dialogues", "Justice in
  Pike's Basin/dialogues", "Spare the Rod, Spoil the Bandit/dialogues", "Hanging Bonnie MacFarlane/dialogues", "The
  Assault on Fort Mercer/dialogues", "Exodus in America/dialogues", "Wild Horses, Tamed Passions/dialogues", "Obstacles in
  Our Path/dialogues". Undead Nightmare lines come from the character page's quote list and the "Dinner for Two" quote box
  (no transcript exists). Walton Lowe's line comes from the quote list of his wiki page.
- Other pages: "Baxter Deaton" (quote list; admits most of his rumors are made up), "Mel Thaxton" (quote list; heard in
  1911 and 1914), "Norman Deek" (two holsters), "Grand Prix" (Carreras Perdido Cup, third race "L. Johnson's Run"),
  "Liars and Cheats" (released September 21, 2010; Leigh Johnson in the Redemption list), "Red Dead Redemption: The Man
  from Blackwater" (aired on Fox on May 29, 2010; 5USA on June 5, 2010; scenes used), "Palmer" (RDR2 sheriff of
  Armadillo, 1907), "Coot's Chapel", "Priscilla Johnson".
- In-game newspapers: Blackwater Ledger No. 56 ("Shoot Out at Fort Mercer": "Marshall Leigh Johnson"), Blackwater
  Ledger & Sentinel No. 213 ("Marshall Johnson of Armadillo Retires"), tombstone inscription (Coot's Chapel page).
- Real world: Liars and Cheats Pack details published by Rockstar on August 27, 2010 and released September 21, 2010;
  The Man from Blackwater, directed by John Hillcoat; RDR1 ports PS4/Switch August 17, 2023 and PC October 29, 2024
  without multiplayer (all as in seth_C, nigel_C, bonnie_C).

VERIFIED POINTS: mission numbers 8, 9, 11, 23, 24 (mission pages); the Undead Nightmare quote lines are given as the
wiki lists them; the line to Eli is quoted from the transcript ("That sarcasm's most unbecoming, Eli. It's going to hold
you back in life..."), not from the wiki quote list's variant; "You ride with us again, Marston?" (transcript) replaces
the quote list's "Will you ride with us again Marston?".

EXCLUDED: the jurisdiction analysis and the "critical lack of local law enforcement" explanation (wiki's reading; only
the facts are listed in Trivia); "Coincidentally or not, Rio Del Lobo is where the second treasure is" (wiki's reading);
the yellow tinge of the beard "possibly from alcohol or tobacco" (speculation; appearance belongs to part B); the FR
wiki's "he does not seem to understand modernity" and "he seems to hate the town" (interpretation; the facts are in
part A); the Tersk / Kentucky Saddler / Standardbred Pinto horses, the dual revolvers used only in cutscenes, the
shotgun versus Repeater Carbine in Pike's Basin, the one revolver in Dinner for Two (weapons and horses: part B); the
badge texture and dual wielding as cut content (part D); the different voices in early trailers (part D); the woman of
Ridgewood returning in Undead Nightmare as Millicent Waterbury's mother (about her, not Johnson); "Jonah appears
friendlier if the player follows the deputies" (about Jonah); the Red Dead Online claim that Bonnie "hopes he can come
back" is kept only as an attributed wiki statement.

OWNERSHIP: narrative events live in part A (one line per mission here). Quotes here are mostly exchanges and lines by
other characters, to leave single signature lines to part B "In his own words"; the fixer resolves any overlap. The
newspapers are told in part A (Trivia only notes the spelling "Marshall"). RDR2 and Red Dead Online mentions live here
(Other media), not in the biography.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A1 = two("Act I: New Austin", "Acte I : New Austin")
UNM = two("Undead Nightmare", "Undead Nightmare")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Leigh Johnson has a strand of five story missions in the first act of Red Dead Redemption, all in New Austin, numbered 8, 9, 11, 23 and 24 in the story order. The first, \"Political Realities in Armadillo\", becomes available after Bonnie MacFarlane's \"Obstacles in Our Path\". It introduces cover, bounty hunting and fast travel from a campsite, and unlocks the bounty hunting jobs and the stranger missions \"American Appetites\" (part 1) and \"Water and Honesty\". \"Justice in Pike's Basin\" introduces basic ranged combat, opens the Pike's Basin gang hideout and unlocks Nigel West Dickens's strand. \"Spare the Rod, Spoil the Bandit\" requires \"Women and Cattle\" and \"Old Swindler Blues\"; \"Hanging Bonnie MacFarlane\" requires \"The Burning\". \"The Assault on Fort Mercer\", the last mission of New Austin, requires the strands of Johnson, Dickens, Seth Briars and Irish, introduces mounted weapons and the Gatling gun, and leads to \"We Shall Be Together in Paradise\", the first mission in Mexico. In Undead Nightmare, Johnson gives one side mission.",
              "Leigh Johnson propose une série de cinq missions principales dans le premier acte de Red Dead Redemption, toutes dans le New Austin, numérotées 8, 9, 11, 23 et 24 dans l'ordre de l'histoire. La première, \"Political Realities in Armadillo\", se débloque après \"Obstacles in Our Path\", une mission de Bonnie MacFarlane. Elle introduit les mises à couvert, la chasse aux primes et le voyage rapide depuis un campement, et débloque les contrats de chasseur de primes ainsi que les missions d'inconnu \"American Appetites\" (première partie) et \"Water and Honesty\". \"Justice in Pike's Basin\" introduit le combat à distance, ouvre le repaire de Pike's Basin et débloque la série de Nigel West Dickens. \"Spare the Rod, Spoil the Bandit\" exige d'avoir terminé \"Women and Cattle\" et \"Old Swindler Blues\" ; \"Hanging Bonnie MacFarlane\" exige \"The Burning\". \"The Assault on Fort Mercer\", dernière mission du New Austin, suppose d'avoir bouclé les séries de Johnson, de Dickens, de Seth Briars et d'Irish ; elle introduit les armes fixes et la mitrailleuse Gatling, et mène à \"We Shall Be Together in Paradise\", la première mission au Mexique. Dans Undead Nightmare, Johnson confie une mission secondaire.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Johnson's role", "Rôle de Johnson")], "rows": [
        M("Political Realities in Armadillo", A1,
          "Mission giver. Meets John, then tracks Walton Lowe with him to Pleasance House. Rewards: 20 dollars, 75 fame (125 with the gold medal) and 200 honor.",
          "Donneur de mission. Rencontre John, puis traque Walton Lowe avec lui jusqu'à Pleasance House. Récompenses : 20 dollars, 75 points de célébrité (125 avec la médaille d'or) et 200 points d'honneur."),
        M("Justice in Pike's Basin", A1,
          "Mission giver. Leads John and his deputies against the Bollard Twins gang to recover Mr. Gulch's cattle. Rewards: 25 dollars, 150 fame (200 with the gold medal) and 100 honor.",
          "Donneur de mission. Mène John et ses adjoints contre la bande des jumeaux Bollard pour récupérer le bétail de M. Gulch. Récompenses : 25 dollars, 150 points de célébrité (200 avec la médaille d'or) et 100 points d'honneur."),
        M("Spare the Rod, Spoil the Bandit", A1,
          "Mission giver. Leads the posse to Ridgewood Farm, then after Williamson's men; captures Norman Deek. Rewards: 50 dollars, a Winchester Repeater if John has none, 250 fame (300 with the gold medal) and 200 honor.",
          "Donneur de mission. Conduit le groupe à Ridgewood Farm, puis aux trousses des hommes de Williamson ; capture Norman Deek. Récompenses : 50 dollars, une Winchester Repeater si John n'en a pas, 250 points de célébrité (300 avec la médaille d'or) et 200 points d'honneur."),
        M("Hanging Bonnie MacFarlane", A1,
          "Mission giver. Receives the gang's demand at his office and leads the exchange of Norman Deek at Tumbleweed, which turns into an ambush. Reward: 150 fame (200 with the gold medal).",
          "Donneur de mission. Reçoit l'ultimatum de la bande à son bureau et dirige l'échange de Norman Deek à Tumbleweed, qui tourne au guet-apens. Récompense : 150 points de célébrité (200 avec la médaille d'or)."),
        M("The Assault on Fort Mercer", A1,
          "Mission giver. Leads his deputies inside the fort once John has opened fire; Williamson has already left. His last appearance in the story. Rewards: 50 dollars and 150 fame (200 with the gold medal).",
          "Donneur de mission. Mène ses adjoints dans le fort une fois que John a ouvert le feu ; Williamson est déjà parti. Sa dernière apparition dans l'histoire. Récompenses : 50 dollars et 150 points de célébrité (200 avec la médaille d'or)."),
        M("Dinner for Two", UNM,
          "Mission giver. Asks John to find his missing deputies, Jonah and Eli. Reward: a Sawed-off Shotgun.",
          "Donneur de mission. Demande à John de retrouver ses adjoints disparus, Jonah et Eli. Récompense : un fusil à canon scié."),
    ]}},
    {"h4": two("Missions in which he is mentioned", "Missions où il est évoqué")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Link with Johnson", "Lien avec Johnson")], "rows": [
        M("Exodus in America", A1,
          "John's guide, Jake, says the marshal hired him after a telegram from Blackwater.",
          "Jake, le guide de John, explique que le marshal l'a engagé à la suite d'un télégramme de Blackwater."),
        M("Wild Horses, Tamed Passions", A1,
          "Drew MacFarlane says he has seen the telegram the marshal received from Blackwater.",
          "Drew MacFarlane affirme avoir vu le télégramme reçu par le marshal."),
        M("Obstacles in Our Path", A1,
          "Bonnie advises John to see the marshal about Williamson.",
          "Bonnie conseille à John d'aller voir le marshal au sujet de Williamson."),
        M("Women and Cattle", A1,
          "Bonnie has heard from Johnson that John plans to settle in the area.",
          "Bonnie a appris par Johnson que John compte s'installer dans la région."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the mission transcripts of the Red Dead Wiki. The Undead Nightmare lines come from the wiki's quote list and mission page, as no transcript exists for the expansion's missions.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. Celles d'Undead Nightmare proviennent de la liste de citations et de la page de mission du wiki, faute de transcription pour les missions de l'extension.")},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("Jake: Ain't we all? Yeah, so it was the Marshal who hired me. Leigh Johnson, do you know him? / Marston: I think I heard his name. / Jake: Says he got a telegram from some Blackwater big bugs askin' for a guide.", "Jake: Ain't we all? Yeah, so it was the Marshal who hired me. Leigh Johnson, do you know him? / Marston: I think I heard his name. / Jake: Says he got a telegram from some Blackwater big bugs askin' for a guide."),
         "src": two("Exodus in America (RDR1, Act I), on the road to Fort Mercer",
                    "Exodus in America (RDR1, acte I), sur la route de Fort Mercer. Traduction : « Jake : Comme nous tous ! Bref, c'est le marshal qui m'a engagé. Leigh Johnson, vous le connaissez ? / Marston : Il me semble avoir entendu son nom. / Jake : Il dit qu'il a reçu un télégramme de gros bonnets de Blackwater qui demandaient un guide. »")},
        {"q": two("They ain't theories, Mr. Marston. I saw the telegram the Marshal got from Blackwater. It ain't exactly a state secret who sent you.", "They ain't theories, Mr. Marston. I saw the telegram the Marshal got from Blackwater. It ain't exactly a state secret who sent you."),
         "src": two("Drew MacFarlane, Wild Horses, Tamed Passions (RDR1, Act I)",
                    "Drew MacFarlane, Wild Horses, Tamed Passions (RDR1, acte I). Traduction : « Ce ne sont pas des théories, monsieur Marston. J'ai vu le télégramme que le marshal a reçu de Blackwater. Ce n'est pas vraiment un secret d'État, qui vous envoie. »")},
        {"q": two("You know, you should go pay the Marshal a visit in Armadillo sometime. I'm sure he could help you deal with that nice Mr. Williamson.", "You know, you should go pay the Marshal a visit in Armadillo sometime. I'm sure he could help you deal with that nice Mr. Williamson."),
         "src": two("Bonnie MacFarlane, Obstacles in Our Path (RDR1, Act I)",
                    "Bonnie MacFarlane, Obstacles in Our Path (RDR1, acte I). Traduction : « Vous savez, vous devriez rendre visite au marshal à Armadillo. Je suis sûre qu'il pourrait vous aider à régler son compte à ce charmant M. Williamson. »")},
        {"q": two("Woman: I thought you were supposed to protect us, Marshal? You folk ain't men. You ain't nothing. You're just some man on a government payroll, taking money that the rest of us have to pay for with our lives! What is wrong with this country? / Leigh: Mount up, men. The man that kills the boss of that bunch gets fifty dollars. / Woman: It ain't about the money, Marshal. These are people's lives. People's homes!", "Woman: I thought you were supposed to protect us, Marshal? You folk ain't men. You ain't nothing. You're just some man on a government payroll, taking money that the rest of us have to pay for with our lives! What is wrong with this country? / Leigh: Mount up, men. The man that kills the boss of that bunch gets fifty dollars. / Woman: It ain't about the money, Marshal. These are people's lives. People's homes!"),
         "src": two("A survivor of Ridgewood Farm, Spare the Rod, Spoil the Bandit (RDR1, Act I)",
                    "Une survivante de Ridgewood Farm, Spare the Rod, Spoil the Bandit (RDR1, acte I). Traduction : « La femme : Vous n'étiez pas censé nous protéger, marshal ? Vous n'êtes pas des hommes, vous autres. Vous n'êtes rien. Vous n'êtes qu'un type payé par le gouvernement, qui touche un argent que nous, on paie de nos vies ! Qu'est-ce qui ne va pas dans ce pays ? / Leigh : En selle, les gars. Cinquante dollars pour celui qui abat le chef de cette bande. / La femme : Ce n'est pas une question d'argent, marshal. Ce sont des vies. Des foyers ! »")},
        {"q": two("Marshal: Get down from that horse, boy, or I'll shoot. / Outlaw on Horse: I wouldn't recommend that, mister. Not if Drew MacFarlane wants to see his Bonnie back in one piece.", "Marshal: Get down from that horse, boy, or I'll shoot. / Outlaw on Horse: I wouldn't recommend that, mister. Not if Drew MacFarlane wants to see his Bonnie back in one piece."),
         "src": two("Hanging Bonnie MacFarlane (RDR1, Act I), outside the marshal's office",
                    "Hanging Bonnie MacFarlane (RDR1, acte I), devant le bureau du marshal. Traduction : « Le marshal : Descends de ce cheval, mon garçon, ou je tire. / Le cavalier : Je vous le déconseille, monsieur. Pas si Drew MacFarlane veut revoir sa Bonnie en un seul morceau. »")},
        {"q": two("You wait, Marshal. I'll be back for you.", "You wait, Marshal. I'll be back for you."),
         "src": two("Norman Deek, Hanging Bonnie MacFarlane (RDR1, Act I), tied onto a horse on the way to Tumbleweed",
                    "Norman Deek, Hanging Bonnie MacFarlane (RDR1, acte I), attaché sur un cheval en route vers Tumbleweed. Traduction : « Attends un peu, marshal. Je reviendrai m'occuper de toi. »")},
        {"q": two("Whoever kills the Marshal gets to keep the badge!", "Whoever kills the Marshal gets to keep the badge!"),
         "src": two("Walton Lowe, Red Dead Redemption (RDR1, Act I), according to the quote list of his page on the Red Dead Wiki",
                    "Walton Lowe, Red Dead Redemption (RDR1, acte I), d'après la liste de citations de sa page sur le Red Dead Wiki. Traduction : « Celui qui tue le marshal garde l'insigne ! »")},
    ]},
    {"h4": two("Red Dead Redemption, Act I", "Red Dead Redemption, acte I")},
    {"quotes": [
        {"q": two("Johnson: What's going on here? / Jonah: I got me one of them Williamson boys. / Marston: And I got me one of them idiots who give marshals a bad name.", "Johnson: What's going on here? / Jonah: I got me one of them Williamson boys. / Marston: And I got me one of them idiots who give marshals a bad name."),
         "src": two("Political Realities in Armadillo (RDR1, Act I), on entering his office",
                    "Political Realities in Armadillo (RDR1, acte I), en entrant dans son bureau. Traduction : « Johnson : Qu'est-ce qui se passe ici ? / Jonah : J'ai attrapé un des gars de Williamson. / Marston : Et moi, un de ces abrutis qui donnent mauvaise réputation aux marshals. »")},
        {"q": two("Johnson: What are you doing here Mr. Marston, apart from frightening my deputies? / Marston: I'm here to capture or kill Bill Williamson. / Johnson: Okay.", "Johnson: What are you doing here Mr. Marston, apart from frightening my deputies? / Marston: I'm here to capture or kill Bill Williamson. / Johnson: Okay."),
         "src": two("Political Realities in Armadillo (RDR1, Act I), Johnson laughing at the answer",
                    "Political Realities in Armadillo (RDR1, acte I), Johnson riant de la réponse. Traduction : « Johnson : Qu'est-ce que vous faites ici, monsieur Marston, à part effrayer mes adjoints ? / Marston : Je suis venu capturer ou tuer Bill Williamson. / Johnson : D'accord. »")},
        {"q": two("Marston: And you're happy to let them drink in your saloon? / Johnson: Happy? No. But the way I figure it, better they're carousin' in there than out robbin' decent folk. / Marston: That's an interesting approach to law enforcement.", "Marston: And you're happy to let them drink in your saloon? / Johnson: Happy? No. But the way I figure it, better they're carousin' in there than out robbin' decent folk. / Marston: That's an interesting approach to law enforcement."),
         "src": two("Political Realities in Armadillo (RDR1, Act I), about Walton's gang",
                    "Political Realities in Armadillo (RDR1, acte I), à propos de la bande de Walton. Traduction : « Marston : Et ça vous va de les laisser boire dans votre saloon ? / Johnson : Ça me va ? Non. Mais à mon avis, mieux vaut qu'ils fassent la noce là-dedans plutôt que de détrousser les honnêtes gens. / Marston : Drôle de façon de faire respecter la loi. »")},
        {"q": two("Marston: I don't want to be no policeman, Marshal. / Johnson: Nor did I, my friend. I can promise you that. I'll see you soon, Mr. Marston.", "Marston: I don't want to be no policeman, Marshal. / Johnson: Nor did I, my friend. I can promise you that. I'll see you soon, Mr. Marston."),
         "src": two("Political Realities in Armadillo (RDR1, Act I), at Pleasance House",
                    "Political Realities in Armadillo (RDR1, acte I), à Pleasance House. Traduction : « Marston : Je n'ai pas envie de devenir policier, marshal. / Johnson : Moi non plus, mon ami. Je vous le garantis. À bientôt, monsieur Marston. »")},
        {"q": two("Leigh: I have no idea. If it's important, they'll send someone down like they did with you. / John: Suddenly, the world is full of \"Theys\".", "Leigh: I have no idea. If it's important, they'll send someone down like they did with you. / John: Suddenly, the world is full of \"Theys\"."),
         "src": two("Justice in Pike's Basin (RDR1, Act I), at the telephone",
                    "Justice in Pike's Basin (RDR1, acte I), au téléphone. Traduction : « Leigh : Aucune idée. Si c'est important, ils enverront quelqu'un, comme ils l'ont fait avec vous. / John : D'un coup, le monde est plein de \"ils\". »")},
        {"q": two("Eli: Well, it was a group of four men rounding up Mr. Gulch's livestock and none of them looked like Mr. Gulch's hands, so yes, sir. Right now. / Leigh: That sarcasm's most unbecoming, Eli. It's going to hold you back in life, even worse than your lazy eye.", "Eli: Well, it was a group of four men rounding up Mr. Gulch's livestock and none of them looked like Mr. Gulch's hands, so yes, sir. Right now. / Leigh: That sarcasm's most unbecoming, Eli. It's going to hold you back in life, even worse than your lazy eye."),
         "src": two("Justice in Pike's Basin (RDR1, Act I), when Eli reports the rustlers",
                    "Justice in Pike's Basin (RDR1, acte I), quand Eli signale les voleurs de bétail. Traduction : « Eli : Eh bien, c'étaient quatre hommes qui rassemblaient le bétail de M. Gulch, et aucun ne ressemblait à ses employés, alors oui, monsieur. En ce moment même. / Leigh : Ce sarcasme ne te sied guère, Eli. Il te nuira dans la vie, plus encore que ton œil qui louche. »")},
        {"q": two("Leigh: How long you been workin' for the government, Marston? / John: I don't work for the government. / Leigh: Well, I got a telegram from some federal clowns in Blackwater that says otherwise.", "Leigh: How long you been workin' for the government, Marston? / John: I don't work for the government. / Leigh: Well, I got a telegram from some federal clowns in Blackwater that says otherwise."),
         "src": two("Justice in Pike's Basin (RDR1, Act I), on the ride to the canyon",
                    "Justice in Pike's Basin (RDR1, acte I), en route vers le canyon. Traduction : « Leigh : Depuis combien de temps vous travaillez pour le gouvernement, Marston ? / John : Je ne travaille pas pour le gouvernement. / Leigh : Eh bien, j'ai reçu un télégramme de quelques guignols fédéraux de Blackwater qui dit le contraire. »")},
        {"q": two("Eli: Mr. West Dickens, the tonics merchant. He was due in town last week. / Leigh: Oh, the narcotic and bat piss salesman who cons housewives out of their money with promises of eternal youth.", "Eli: Mr. West Dickens, the tonics merchant. He was due in town last week. / Leigh: Oh, the narcotic and bat piss salesman who cons housewives out of their money with promises of eternal youth."),
         "src": two("Justice in Pike's Basin (RDR1, Act I), after the fight",
                    "Justice in Pike's Basin (RDR1, acte I), après le combat. Traduction : « Eli : M. West Dickens, le marchand de toniques. Il était attendu en ville la semaine dernière. / Leigh : Ah, le vendeur de stupéfiants et de pisse de chauve-souris qui soutire leur argent aux ménagères en leur promettant la jeunesse éternelle. »")},
        {"q": two("Leigh: Thank you, John Marston. It's gonna be a bloody job. / Marston: I don't think I know any other kind, sir.", "Leigh: Thank you, John Marston. It's gonna be a bloody job. / Marston: I don't think I know any other kind, sir."),
         "src": two("Spare the Rod, Spoil the Bandit (RDR1, Act I), when John agrees to ride to Ridgewood",
                    "Spare the Rod, Spoil the Bandit (RDR1, acte I), quand John accepte de partir pour Ridgewood. Traduction : « Leigh : Merci, John Marston. Ça va être sanglant. / Marston : Je crois que je n'ai jamais connu autre chose, monsieur. »")},
        {"q": two("Leigh: Killing and thieving's never right, boy, no matter how you dress it up. / Marston: Unless it's ordered by a court of law, you mean?", "Leigh: Killing and thieving's never right, boy, no matter how you dress it up. / Marston: Unless it's ordered by a court of law, you mean?"),
         "src": two("Spare the Rod, Spoil the Bandit (RDR1, Act I), after Jonah asks John about his gang",
                    "Spare the Rod, Spoil the Bandit (RDR1, acte I), après que Jonah a interrogé John sur son gang. Traduction : « Leigh : Tuer et voler, ce n'est jamais juste, mon garçon, quel que soit l'habit qu'on lui donne. / Marston : Sauf quand c'est ordonné par un tribunal, vous voulez dire ? »")},
        {"q": two("Nice to see you again, buddy. Thanks for your help, John. Norman here's gonna help us get to Bill. Ain't you, Norman?", "Nice to see you again, buddy. Thanks for your help, John. Norman here's gonna help us get to Bill. Ain't you, Norman?"),
         "src": two("Spare the Rod, Spoil the Bandit (RDR1, Act I), on finding Norman Deek alive",
                    "Spare the Rod, Spoil the Bandit (RDR1, acte I), en découvrant Norman Deek vivant. Traduction : « Content de te revoir, mon vieux. Merci pour ton aide, John. Norman ici présent va nous aider à atteindre Bill. Pas vrai, Norman ? »")},
        {"q": two("Marshal: They come down here, dressed as cocky as the king of diamonds, talkin' a lot of flannel about helpin' us, about spreadin' peace and civilization to the West, but they've brought nothin' but trouble and taxes. / Marston: I agree with you. Wolves in sheep's clothing, all of 'em.", "Marshal: They come down here, dressed as cocky as the king of diamonds, talkin' a lot of flannel about helpin' us, about spreadin' peace and civilization to the West, but they've brought nothin' but trouble and taxes. / Marston: I agree with you. Wolves in sheep's clothing, all of 'em."),
         "src": two("Hanging Bonnie MacFarlane (RDR1, Act I), about the federal agents",
                    "Hanging Bonnie MacFarlane (RDR1, acte I), à propos des agents fédéraux. Traduction : « Le marshal : Ils débarquent ici, fiers comme le roi de carreau, en nous servant de belles paroles sur l'aide qu'ils nous apportent, sur la paix et la civilisation qu'ils répandent dans l'Ouest, mais ils n'ont apporté que des ennuis et des impôts. / Marston : Je suis d'accord. Des loups déguisés en agneaux, tous autant qu'ils sont. »")},
        {"q": two("Marshal: Deek's the kind of man who's mean enough to be second-in-command but too cowardly and stupid to ever be a leader. / Marston: Don't ever use that line near your deputies.", "Marshal: Deek's the kind of man who's mean enough to be second-in-command but too cowardly and stupid to ever be a leader. / Marston: Don't ever use that line near your deputies."),
         "src": two("Hanging Bonnie MacFarlane (RDR1, Act I), on the way to Tumbleweed",
                    "Hanging Bonnie MacFarlane (RDR1, acte I), en route vers Tumbleweed. Traduction : « Le marshal : Deek est le genre d'homme assez méchant pour faire un second, mais trop lâche et trop bête pour devenir un jour un chef. / Marston : Ne sortez jamais cette phrase devant vos adjoints. »")},
        {"q": two("Tumbleweed? A lonely, godforsaken place. Some people say it's haunted. It was quite a town, back in its day. Then they build the railroad in Armadillo and went clean past Tumbleweed. And that was that.", "Tumbleweed? A lonely, godforsaken place. Some people say it's haunted. It was quite a town, back in its day. Then they build the railroad in Armadillo and went clean past Tumbleweed. And that was that."),
         "src": two("Hanging Bonnie MacFarlane (RDR1, Act I), when John asks where they are headed",
                    "Hanging Bonnie MacFarlane (RDR1, acte I), quand John demande où ils vont. Traduction : « Tumbleweed ? Un endroit perdu, abandonné de Dieu. Certains disent qu'il est hanté. C'était une sacrée ville, à son époque. Puis ils ont construit le chemin de fer à Armadillo, en passant bien à l'écart de Tumbleweed. Et voilà. »")},
        {"q": two("Marshal: How was this mess supposed to turn out? Sendin' an outlaw to do the work of a lawman? That's madness. / Marston: Ain't much difference between the two, as far as I can tell. / Marshal: There have to be rules, Marston. Even you must understand that.", "Marshal: How was this mess supposed to turn out? Sendin' an outlaw to do the work of a lawman? That's madness. / Marston: Ain't much difference between the two, as far as I can tell. / Marshal: There have to be rules, Marston. Even you must understand that."),
         "src": two("Hanging Bonnie MacFarlane (RDR1, Act I), on the way to Tumbleweed",
                    "Hanging Bonnie MacFarlane (RDR1, acte I), en route vers Tumbleweed. Traduction : « Le marshal : Comment cette pagaille était-elle censée finir ? Envoyer un hors-la-loi faire le travail d'un homme de loi ? C'est de la folie. / Marston : Il n'y a pas grande différence entre les deux, si vous voulez mon avis. / Le marshal : Il faut des règles, Marston. Même vous, vous devez le comprendre. »")},
        {"q": two("Marston: The problem with laws is, everybody ain't the same. And why should a bunch of rich university boys in the East get to decide how a man in Armadillo should live his life? / Marshal: Ughh, well maybe you're right about that.", "Marston: The problem with laws is, everybody ain't the same. And why should a bunch of rich university boys in the East get to decide how a man in Armadillo should live his life? / Marshal: Ughh, well maybe you're right about that."),
         "src": two("Hanging Bonnie MacFarlane (RDR1, Act I), end of the argument about the law",
                    "Hanging Bonnie MacFarlane (RDR1, acte I), à la fin du débat sur la loi. Traduction : « Marston : Le problème avec les lois, c'est que les gens ne sont pas tous pareils. Et pourquoi une bande de riches universitaires de l'Est déciderait de la façon dont un homme d'Armadillo doit vivre sa vie ? / Le marshal : Hum, bon, là-dessus, vous avez peut-être raison. »")},
        {"q": two("Marston: All I care about is Williamson. It is vital we stop him. / Marshal: Agreed. That man is a stone-cold killer.", "Marston: All I care about is Williamson. It is vital we stop him. / Marshal: Agreed. That man is a stone-cold killer."),
         "src": two("The Assault on Fort Mercer (RDR1, Act I), on the hilltop before the assault",
                    "The Assault on Fort Mercer (RDR1, acte I), sur la colline avant l'assaut. Traduction : « Marston : Seul Williamson m'intéresse. Il faut absolument l'arrêter. / Le marshal : D'accord. Cet homme est un tueur de sang-froid. »")},
        {"q": two("Marshal: I'm sorry about this, John. I guess you'll be heading to Mexico. / Marston: So it would seem. How is it down there?", "Marshal: I'm sorry about this, John. I guess you'll be heading to Mexico. / Marston: So it would seem. How is it down there?"),
         "src": two("The Assault on Fort Mercer (RDR1, Act I), his last exchange with John",
                    "The Assault on Fort Mercer (RDR1, acte I), son dernier échange avec John. Traduction : « Le marshal : Je suis désolé, John. Je suppose que vous allez partir pour le Mexique. / Marston : On dirait bien. C'est comment, là-bas ? »")},
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"quotes": [
        {"q": two("Cattle rustlin' and bank robbery are at an all time low. While murder, blood drinking, and psychotic episodes seem to be somewhat prevalent. Either that, or I'm dreaming.", "Cattle rustlin' and bank robbery are at an all time low. While murder, blood drinking, and psychotic episodes seem to be somewhat prevalent. Either that, or I'm dreaming."),
         "src": two("Undead Nightmare, on the state of Armadillo (quote list of the wiki)",
                    "Undead Nightmare, sur l'état d'Armadillo (liste de citations du wiki). Traduction : « Le vol de bétail et les braquages de banque n'ont jamais été aussi rares. En revanche, les meurtres, le sang qu'on boit et les crises de démence semblent assez répandus. Soit ça, soit je rêve. »")},
        {"q": two("It was fast and they died with their bellies full. Well, one of 'em did.", "It was fast and they died with their bellies full. Well, one of 'em did."),
         "src": two("John Marston to Johnson, Dinner for Two (Undead Nightmare), about Jonah and Eli (quote box of the mission page)",
                    "John Marston à Johnson, Dinner for Two (Undead Nightmare), à propos de Jonah et Eli (encadré de la page de la mission). Traduction : « Ça a été rapide, et ils sont morts le ventre plein. Enfin, l'un des deux. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"h4": two("Red Dead Redemption", "Red Dead Redemption")},
    {"ul": [
        two("The in-game texts spell his title \"Marshall\" with a double l: his wife's tombstone at Coot's Chapel, the 1911 article \"Shoot Out at Fort Mercer\" and the 1914 headline \"Marshall Johnson of Armadillo Retires\".",
            "Les textes du jeu écrivent son titre \"Marshall\", avec deux l : la pierre tombale de sa femme à Coot's Chapel, l'article de 1911 \"Shoot Out at Fort Mercer\" et le titre de 1914, \"Marshall Johnson of Armadillo Retires\"."),
        two("His exact office is not consistent. According to the Red Dead Wiki, he wears a United States Marshal badge. In \"Political Realities in Armadillo\", he says Williamson is outside his jurisdiction because Fort Mercer lies in the next county. The 1914 article calls him a town marshal. His missions nonetheless take him to Pike's Basin, to Tumbleweed in Gaptooth Ridge and to Fort Mercer in Rio Bravo.",
            "Sa fonction exacte varie. D'après le Red Dead Wiki, il porte l'insigne de United States Marshal. Dans \"Political Realities in Armadillo\", il explique que Williamson est hors de sa juridiction parce que Fort Mercer se trouve dans le comté voisin. L'article de 1914 le présente comme le marshal de la ville. Ses missions le mènent pourtant à Pike's Basin, à Tumbleweed, dans le Gaptooth Ridge, et à Fort Mercer, dans le Rio Bravo."),
        two("Many people in Armadillo speak badly of him. According to the quote list of his own page on the Red Dead Wiki, the Armadillo bank teller Baxter Deaton says \"They say that Marshal Johnson's buried stolen goods out at Río del Lobo\" and \"I heard the gang at Twin Rocks is in cahoots with Marshal Johnson\"; he also accuses an unnamed marshal of beating women. The same page notes that Deaton admits most of his rumors are made up. The quote list of Mel Thaxton includes \"The Marshal's an idiot, that's this place's problem\", a complaint heard in the saloon in 1911 and in 1914. According to the Red Dead Wiki, Jeb Murphy, Eldin Grubb and Herbert Moon also run him down, a man named Jake says he is not the man he used to be, and workers at MacFarlane's Ranch say he carries the whole world on his shoulders.",
            "Nombre d'habitants d'Armadillo disent du mal de lui. D'après la liste de citations de sa propre page sur le Red Dead Wiki, le guichetier de la banque d'Armadillo, Baxter Deaton, raconte \"They say that Marshal Johnson's buried stolen goods out at Río del Lobo\" (il paraît que le marshal Johnson a enterré des biens volés à Río del Lobo) et \"I heard the gang at Twin Rocks is in cahoots with Marshal Johnson\" (j'ai entendu dire que la bande de Twin Rocks est de mèche avec le marshal Johnson) ; il accuse aussi un marshal, sans le nommer, de battre les femmes. La même page précise que Deaton avoue inventer la plupart de ses rumeurs. La liste de citations de Mel Thaxton comprend \"The Marshal's an idiot, that's this place's problem\" (le marshal est un imbécile, voilà le problème de cette ville), une plainte qu'on entend au saloon en 1911 comme en 1914. D'après le Red Dead Wiki, Jeb Murphy, Eldin Grubb et Herbert Moon le dénigrent aussi, un certain Jake estime qu'il n'est plus l'homme qu'il était, et les employés du MacFarlane's Ranch disent qu'il porte le monde entier sur ses épaules."),
        two("According to the mission page of \"Hanging Bonnie MacFarlane\", the player can follow Johnson and Bonnie when they ride off at the end: the marshal stops with her at a small camp near Del Lobo Rock, and neither can be spoken to. According to the character page, killing their horses in Dead Eye mode right after the mission makes them both fall, and both can then be killed.",
            "D'après la page de la mission \"Hanging Bonnie MacFarlane\", le joueur peut suivre Johnson et Bonnie quand ils s'éloignent à cheval à la fin : le marshal s'arrête avec elle dans un petit campement près de Del Lobo Rock, et on ne peut parler à aucun des deux. D'après la page du personnage, abattre leurs chevaux en mode Dead Eye juste après la mission les fait tomber tous les deux, et on peut alors les tuer."),
        two("According to the mission page of \"The Assault on Fort Mercer\", on rare occasions a cougar kills one of the lawmen during the ride to the fort, which fails the mission; it happens mostly at night.",
            "D'après la page de la mission \"The Assault on Fort Mercer\", il arrive, rarement, qu'un puma tue l'un des hommes de loi pendant la chevauchée vers le fort, ce qui fait échouer la mission ; cela se produit surtout la nuit."),
        two("According to the Red Dead Wiki, his gun belt carries two holsters, a feature shared in the game only with Norman Deek, Enepay and Benton Manning, and his outfit resembles the one worn by Sheriff O'Grady in Red Dead Revolver.",
            "D'après le Red Dead Wiki, son ceinturon porte deux étuis, une particularité qu'il ne partage dans le jeu qu'avec Norman Deek, Enepay et Benton Manning, et sa tenue rappelle celle du shérif O'Grady dans Red Dead Revolver."),
    ]},
    {"h4": two("Undead Nightmare (non-canon)", "Undead Nightmare (hors canon)")},
    {"ul": [
        two("After \"Dinner for Two\", Johnson stays in his office, where he can be seen making calls and doing paperwork. According to the mission page, he can be killed, for example with the shotgun he gave John, fired through the window close to his head.",
            "Après \"Dinner for Two\", Johnson reste dans son bureau, où on le voit téléphoner et remplir des papiers. D'après la page de la mission, on peut le tuer, par exemple avec le fusil qu'il a remis à John, en tirant à travers la fenêtre au plus près de sa tête."),
        two("According to the mission page, Ayauhtéotl can be seen outside the window nearest the marshal's desk at the start of the opening cutscene of \"Dinner for Two\".",
            "D'après la page de la mission, on aperçoit Ayauhtéotl derrière la fenêtre la plus proche du bureau du marshal au début de la cinématique d'ouverture de \"Dinner for Two\"."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("The Man from Blackwater (2010)", "The Man from Blackwater (2010)")},
    {"p": two("Johnson appears in Red Dead Redemption: The Man from Blackwater, a short film made with the game's engine, directed by John Hillcoat and broadcast by Fox on May 29, 2010, then by 5USA in the United Kingdom on June 5, 2010. The film follows the first act, in which John teams up with the marshal and his deputies, Nigel West Dickens and Seth Briars to take Fort Mercer. It reuses his first meeting with John and Jonah from \"Political Realities in Armadillo\", and the Ridgewood Farm massacre and the confrontation with Williamson from \"Spare the Rod, Spoil the Bandit\". When John explains his situation to Johnson, the film adds scenes that are not in the game, showing John's years in Dutch van der Linde's gang, among them a robbery of the Blackwater bank with Bill and Javier Escuella.",
              "Johnson apparaît dans Red Dead Redemption: The Man from Blackwater, un court métrage réalisé avec le moteur du jeu par John Hillcoat, diffusé par Fox le 29 mai 2010, puis par 5USA au Royaume-Uni le 5 juin 2010. Le film reprend le premier acte, où John s'allie au marshal et à ses adjoints, à Nigel West Dickens et à Seth Briars pour prendre Fort Mercer. Il réutilise sa première rencontre avec John et Jonah, tirée de \"Political Realities in Armadillo\", ainsi que le massacre de Ridgewood Farm et la confrontation avec Williamson, tirés de \"Spare the Rod, Spoil the Bandit\". Quand John expose sa situation à Johnson, le film ajoute des scènes absentes du jeu, qui montrent John du temps du gang de Dutch van der Linde, dont un braquage de la banque de Blackwater avec Bill et Javier Escuella.")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Johnson became a playable character model in the multiplayer mode of Red Dead Redemption with the Liars and Cheats Pack, detailed by Rockstar on August 27, 2010 and released on September 21, 2010. Players select him in the Redemption section of the Outfitter, alongside [[john-marston|John]], [[abigail-marston|Abigail]], [[jack-marston|Jack]], [[bonnie-macfarlane|Bonnie MacFarlane]], [[luisa-fortuna|Luisa Fortuna]], [[nigel-west-dickens|Nigel West Dickens]] and [[seth-briars|Seth Briars]]. The same pack added Grand Prix horse races; the third race of the Carreras Perdido Cup is named L. Johnson's Run, and according to the Red Dead Wiki it starts and ends in Armadillo. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, do not include the multiplayer mode.",
              "Johnson devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Liars and Cheats Pack, présenté en détail par Rockstar le 27 août 2010 et sorti le 21 septembre 2010. On le choisit dans la section Redemption de l'Outfitter, aux côtés de [[john-marston|John]], d'[[abigail-marston|Abigail]], de [[jack-marston|Jack]], de [[bonnie-macfarlane|Bonnie MacFarlane]], de [[luisa-fortuna|Luisa Fortuna]], de [[nigel-west-dickens|Nigel West Dickens]] et de [[seth-briars|Seth Briars]]. Le même pack ajoute les courses hippiques Grand Prix ; la troisième course de la Carreras Perdido Cup s'appelle L. Johnson's Run, et, d'après le Red Dead Wiki, elle part d'Armadillo et y revient. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, ne comprennent pas le multijoueur.")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("Rockstar released official artwork of Johnson for Red Dead Redemption. According to the Red Dead Wiki, a promotional image shows him crumpling a bounty notice in his hand, on which the hideout of the target, Campo Mirada, can be made out.",
              "Rockstar a diffusé une illustration officielle de Johnson pour Red Dead Redemption. D'après le Red Dead Wiki, une image promotionnelle le montre en train de froisser un avis de recherche dans sa main, sur lequel on distingue le repaire de la cible, Campo Mirada.")},
    {"h4": two("Red Dead Redemption 2 and Red Dead Online", "Red Dead Redemption 2 et Red Dead Online")},
    {"p": two("Johnson does not appear in Red Dead Redemption 2. In its 1907 epilogue, Armadillo, emptied by a cholera outbreak, has a sheriff named Palmer, who resigns or is shot by the Del Lobo Gang depending on the player's intervention. According to the Red Dead Wiki, the game mentions briefly that Johnson is away because of the cholera outbreak, like most of the town's residents; the 1914 article mentions no break in his 17 years of service. Also according to the wiki, in Red Dead Online, set in 1898, Bonnie MacFarlane mentions him when she starts a recovery mission, saying she hopes he can come back as he is away because of the cholera outbreak.",
              "Johnson n'apparaît pas dans Red Dead Redemption 2. Dans l'épilogue de 1907, Armadillo, vidée par une épidémie de choléra, a pour shérif un certain Palmer, qui démissionne ou tombe sous les balles du gang Del Lobo selon que le joueur intervient ou non. D'après le Red Dead Wiki, le jeu indique brièvement que Johnson est absent à cause du choléra, comme la plupart des habitants ; l'article de 1914 ne signale aucune interruption de ses 17 années de service. Toujours d'après le wiki, dans Red Dead Online, qui se déroule en 1898, Bonnie MacFarlane l'évoque au début d'une mission de récupération : elle espère qu'il pourra revenir, puisqu'il est parti à cause de l'épidémie de choléra.")},
]
