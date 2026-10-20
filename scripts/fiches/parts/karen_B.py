"""Karen Jones, part B: Personality (official descriptions, traits, In her own words, Names, Appearance),
Skills/weapons/horse, Relationships (20 Oct 2026, medium tier).

Sources (register):
- Rockstar character description of 6 Sep 2018 (English text as reprinted by The Hollywood Reporter / Heat
  Vision, Sep 2018, saved in ../uncle/fc/thr_descriptions.txt, line 116; French text from
  rockstargames.com/reddeadredemption2/fr/features/vanderlindegang, as quoted by the French Red Dead Wiki page
  "Karen Jones", karen/fr.txt).
- A character page from an official guide (wiki file KarenJonesBio.jpg, captioned "Biography in RDR 2",
  uploaded 12 Nov 2018, downloaded to karen/fcB/KarenBio.png and read; text quoted verbatim in
  karen/fcB/guide_bio.txt). Wikipedia's "List of Red Dead Redemption 2 characters" cites the same facts to the
  official guide (Price 2018, p. 381); the edition is not named on the page, so the text says "an official guide".
- Red Dead Wiki EN "Karen Jones" (infobox, quote box, Personality, Appearance, Relationships, Trivia) and FR
  "Karen Jones"; wiki page "Old Belle" (horse); "Camp Events" (Colter, Horseshoe Overlook, Sean's Return Party,
  Clemens Point, Shady Belle, Jack's Return Party, Beaver Hollow); "Davey Callander", "Jenny Kirk" (Karen's
  remarks, wiki-only); "A Rage Unleashed" (shotgun, trivia).
- Transcripts: "Polite Society, Valentine Style" ("Trying to play him. Not very well."; "Thank you, Arthur. I
  don't much like being saved, but... when I have to be."; "Or is that Uncle?"); "Sodom? Back to Gomorrah" ("You've
  always been a bad drunk... and, before you say it, I know... takes one to know one."); "Outlaws from the West"
  ("Miss Jones", Susan; "Miss Karen", Dutch); "Letter from Tilly" ("Karen who was a sister to me").
- Fact-checked fiches reused as is: kieran_B (Karen entries), susan_A/B, sean_B, hosea_A/B, abigail_B, john_A/D,
  bill_A/B, lenny_A/B, sadie_A/B, uncle_A/B, micah_B, javier_A/B, arthur_A/D.

Ownership (FIX_RULES): official descriptions (Rockstar 6 Sep 2018 and the guide page) live HERE only; part A
Origins and part C Marketing must not quote them (C may say Rockstar published descriptions on 6 Sep 2018).
Names, appearance (guide portrait, unkempt hair late in the game, face covered at Colter), skills (guard duty,
songs, weapons, Old Belle; the absence of an item request is in part C Trivia only) and ALL camp scenes live HERE, each in ONE relationship entry:
Valentine joke at the Saints Hotel aftermath, confession seat, Blackwater memory -> Arthur / Dutch (see entries);
behind-the-tent slap, party night in John's tent, mourning and "A Prisoner for Life" -> Sean; chores, "our lot",
"gotten soft", Malcolm Foreman story, swamp sewing, manor talk, worry about the drink, "a sister to me" -> Tilly;
suffrage, Valentine curse, Saint Denis talks, vomiting at Jack's party, romance teasing -> Mary-Beth;
eating Susan, "having a baby", alchemy, berating after Molly's death -> Susan; crow trick and "devil" ->
Trelawny; whistle and kiss, "Mr. Bell" -> Micah; drunk flirt -> John; comforting Abigail -> Abigail; Hosea's
case of drinks, trust in Dutch and Hosea -> Hosea; Isaiah reading -> Swanson; baby taunt, cigarette, poker table,
party drinks -> Kieran; Molly confrontation and blows -> Molly; Callander boys and Jenny -> Davey Callander /
Jenny Kirk entries. Narrative mission events (Tucson, Valentine outing and hotel, bank planning, "Sodom? Back to
Gomorrah", Blessed are the Peacemakers return, Eagle Flies escort, departure, Tilly's 1907 letter as a whole)
live in part A; relationship entries refer to them in one clause.

Lines quoted in this part (parts A and C must NOT repeat them; A paraphrases): the Rockstar and guide
descriptions; the wiki quote box "Listen, it's a hard life, this world, for anyone born without means. Any as
judges those who find it hard, is a fool. I'm a lot of things, I'm not quite a fool."; "Thank you, Arthur. I don't
much like being saved, but... when I have to be." (Polite Society); "You've always been a bad drunk... and, before
you say it, I know... takes one to know one." (Sodom ride); "Miss Jones", "Miss Karen" (Names); "Or is that
Uncle?" (Uncle entry); "a sister to me" (Tilly entry). Part C may still use "Trying to play him. Not very well.",
"It's a bank, Arthur." (already quoted in arthur_B), "Gentlemen... let's go rob ourselves a bank." and the
lost-girl/drunken-harlot lines of "Sodom? Back to Gomorrah".

WIKI-ONLY (kept, attributed or paraphrased without quotation marks): the whole camp events material (no
transcripts), the party night with Sean ("see her"), Karen's remarks on the Callander boys and Jenny, Karen
sticking up for Kieran, Bill thinking she is sweet on him, the trust in Dutch and Hosea, Old Belle's breed, the
weapons of the infobox, the shotgun in "A Rage Unleashed", the unkempt hair, the covered face at Colter, the
absence of an item request, the Molly slap (two wiki versions, both given).

Arthur's "Mid twenties, blonde" (Polite Society transcript, optional question to the hotel owner) is quoted in
Appearance; the wiki's "busty" is not used. Excluded: the wiki's readings "implied that deep down... a more vulnerable side",
"possibly from embarrassment or perhaps disappointment", "Sean's death likely contributed to Karen's growing
alcoholism", "her years of debauchery may be taking their toll" as the wiki's own claim (the guide's wording is
quoted instead); the wiki claim that Karen "deeply respects Dutch and Hosea" (kept only as the scene it rests
on); the wiki's "Karen and Sean seem to be lovers" (FR trivia, wording); Arthur "respects that she takes on roles
traditionally held by men" (wiki judgment, no scene given); Karen's hostility toward Micah at Beaver Hollow (no
scene described); Tilly's worry placed in chapter 6 by the wiki's trivia (the camp events page lists it at Shady
Belle, chapter 4; the camp events placement is used); "foreshadowed" (interpretation); the outfit catalogue
(reduced to the guide portrait); the camp-events gloss that Karen "hints at his story's endings and the honor
system" (interpretation); Karen helping the injured Arthur after his escape from the O'Driscolls (event, part A;
transcript only shows her calling his name).
"""

def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar Games' official description of Karen, published in September 2018 (see Marketing), reads: \"A consummate scam artist and trigger woman who can drink pretty much anybody under the table. Bold and full of fun, she loves the outlaw life and wouldn't have it any other way.\"",
        "La description officielle de Karen publiée par Rockstar Games en septembre 2018 (voir Promotion) dit, dans sa version française : \"Escroc accomplie sachant manier les armes, elle a également une très bonne descente. Téméraire et toujours prête à s'amuser, elle chérit sa vie de hors-la-loi et ne la troquerait pour rien au monde.\"")},
    {"p": two(
        "A character page from an official guide, reproduced on the Red Dead Wiki, follows that description closely, adding of her drinking that she \"does so most nights\", and that \"If a bank needs robbing, just say the word and she'll be the first on her horse.\" It also notes that \"the debauchery is starting to take a toll on her after all these years\". It ends: \"She speaks her mind and takes no nonsense but is big-hearted and looks out for everyone, especially the other girls.\"",
        "Une page de personnage tirée d'un guide officiel, reproduite sur le Red Dead Wiki, reprend cette description presque mot pour mot, en précisant qu'elle boit ainsi \"most nights\" (presque tous les soirs), et ajoute que \"If a bank needs robbing, just say the word and she'll be the first on her horse\" (s'il y a une banque à braquer, il suffit de le dire, elle sera la première en selle). Le guide relève aussi que ses années de débauche commencent à peser sur elle. Il conclut : \"She speaks her mind and takes no nonsense but is big-hearted and looks out for everyone, especially the other girls.\" (elle dit ce qu'elle pense et ne s'en laisse pas conter, mais elle a bon cœur et veille sur tout le monde, surtout sur les autres filles).")},
    {"p": two(
        "Sitting with Tilly and Mary-Beth at Horseshoe Overlook, she tells them that poor women have no choice but to get by as best they can in a world run by men. On guard duty she jokes that the girl men once had to rescue now keeps watch over them, rifle in hand. According to the Red Dead Wiki's camp events page, she starts to be seen drunk in camp during the Clemens Point chapter.",
        "Assise avec Tilly et Mary-Beth à Horseshoe Overlook, elle leur explique que les femmes pauvres n'ont pas d'autre choix que de se débrouiller dans un monde mené par les hommes. De garde, elle plaisante : la fille que les hommes devaient autrefois tirer d'affaire veille maintenant sur eux, carabine en main. D'après la page du Red Dead Wiki consacrée aux événements de camp, c'est au chapitre de Clemens Point qu'on commence à la voir ivre au camp.")},
    {"h4": two("In her own words", "Dans ses propres mots")},
    {"p": two(
        "Leaving the Saints Hotel in \"Polite Society, Valentine Style\", she tells Arthur: \"Thank you, Arthur. I don't much like being saved, but... when I have to be.\" On the ride to Valentine in \"Sodom? Back to Gomorrah\", she teases Arthur about his drinking, and admits to her own: \"You've always been a bad drunk... and, before you say it, I know... takes one to know one.\" The Red Dead Wiki opens its page on her with a line she says to Molly O'Shea on the dock at Shady Belle: \"Listen, it's a hard life, this world, for anyone born without means. Any as judges those who find it hard, is a fool. I'm a lot of things, I'm not quite a fool.\"",
        "En sortant du Saints Hotel, dans \"Polite Society, Valentine Style\", elle dit à Arthur : \"Thank you, Arthur. I don't much like being saved, but... when I have to be.\" (merci, Arthur ; je n'aime pas trop qu'on me sauve, mais... quand il le faut). En route vers Valentine, dans \"Sodom? Back to Gomorrah\", elle se moque de la façon de boire d'Arthur, en reconnaissant la sienne : \"You've always been a bad drunk... and, before you say it, I know... takes one to know one.\" (tu as toujours eu l'alcool mauvais... et avant que tu le dises, je sais : c'est l'hôpital qui se moque de la charité). Le Red Dead Wiki ouvre sa page sur une phrase qu'elle adresse à Molly O'Shea, sur le ponton de Shady Belle : \"Listen, it's a hard life, this world, for anyone born without means. Any as judges those who find it hard, is a fool. I'm a lot of things, I'm not quite a fool.\" (écoute, la vie est dure en ce bas monde pour qui naît sans le sou ; celui qui juge ceux qui la trouvent dure est un idiot ; je suis bien des choses, mais pas tout à fait une idiote).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "She is only ever called Karen Jones. In \"Outlaws from the West\", Susan Grimshaw addresses her as \"Miss Jones\" when she hands out the jobs at Colter, and Dutch calls her \"Miss Karen\" when he asks her and Tilly to look after Sadie Adler. Neither the games nor the guide give her a nickname or another name.",
        "On ne l'appelle jamais autrement que Karen Jones. Dans \"Outlaws from the West\", Susan Grimshaw l'appelle \"Miss Jones\" en distribuant les tâches à Colter, et Dutch dit \"Miss Karen\" quand il lui demande, ainsi qu'à Tilly, de s'occuper de Sadie Adler. Ni le jeu ni le guide ne lui donnent de surnom ou d'autre nom.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "The guide's portrait shows a woman with curly blonde hair, light eyes and freckles, in the outfit she wears for the Valentine bank robbery: a dark red dress with puffed sleeves, and a black top hat with a buckled band and feathers. In \"Polite Society, Valentine Style\", Arthur describes her to the owner of the Saints Hotel as \"Mid twenties, blonde\". At Colter her face is covered except for her eyes and nose, according to the Red Dead Wiki, which adds that her hair becomes more unkempt as her drinking gets worse and often lacks its ringlets late in the story.",
        "Le portrait du guide montre une femme aux cheveux blonds bouclés, aux yeux clairs et aux taches de rousseur, dans la tenue qu'elle porte pour le braquage de la banque de Valentine : une robe rouge sombre à manches bouffantes et un haut-de-forme noir orné d'une boucle et de plumes. Dans \"Polite Society, Valentine Style\", Arthur la décrit au patron du Saints Hotel en ces termes : \"Mid twenties, blonde\" (la vingtaine bien entamée, blonde). D'après le Red Dead Wiki, à Colter, on ne voit de son visage que les yeux et le nez ; le wiki ajoute que sa coiffure se défait à mesure qu'elle boit davantage et que, vers la fin de l'histoire, elle a souvent perdu ses anglaises.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Skills, weapons and horse", "Compétences, armes et cheval")},
    {"h4": two("Guard duty and camp work", "Tours de garde et travail au camp")},
    {"p": two(
        "Karen and Sadie Adler are the only women of the gang who take turns on guard duty, according to the Red Dead Wiki. In camp she does chores with Tilly and Mary-Beth, sews with Tilly, and reads romance novels by the wagons at Clemens Point.",
        "D'après le Red Dead Wiki, Karen et Sadie Adler sont les deux seules femmes du gang à prendre des tours de garde. Au camp, elle fait les corvées avec Tilly et Mary-Beth, coud avec Tilly et lit des romans sentimentaux près des chariots à Clemens Point.")},
    {"h4": two("Songs", "Chansons")},
    {"p": two(
        "She is one of the camp's regular singers, and Javier plays the guitar on several of her songs. The Red Dead Wiki's camp events page lists two songs she sings alone: \"Lorena\", by the fire at Horseshoe Overlook, and \"Dance by the Light of the Moon\", at Hosea's request at Clemens Point. With Susan, Uncle, Pearson or Sean, she sings \"Come, Bustle, Bustle\", \"One Eyed Riley\", \"I Wouldn't Marry\", \"Poor Lonesome Cowboy\" and \"Otis Miller\" at Horseshoe Overlook, and \"The Louisville Maid\" and \"Wild Free Rover\" at the party for Sean's return. At Shady Belle she sings \"A Prisoner for Life\", \"The Sailor Boy\" and \"The Heartland Stage Company\".",
        "Elle fait partie des chanteurs attitrés du camp, et Javier l'accompagne à la guitare sur plusieurs chansons. La page du Red Dead Wiki consacrée aux événements de camp en cite deux qu'elle chante seule : \"Lorena\", au coin du feu à Horseshoe Overlook, et \"Dance by the Light of the Moon\", à la demande de Hosea, à Clemens Point. Avec Susan, Uncle, Pearson ou Sean, elle entonne \"Come, Bustle, Bustle\", \"One Eyed Riley\", \"I Wouldn't Marry\", \"Poor Lonesome Cowboy\" et \"Otis Miller\" à Horseshoe Overlook, puis \"The Louisville Maid\" et \"Wild Free Rover\" à la fête du retour de Sean. À Shady Belle, elle chante \"A Prisoner for Life\", \"The Sailor Boy\" et \"The Heartland Stage Company\".")},
    {"h4": two("Weapons and horse", "Armes et cheval")},
    {"p": two(
        "The Red Dead Wiki gives her a Cattleman revolver and a Carbine Repeater. In \"A Rage Unleashed\" she holds a double-barreled shotgun, without firing it, when Eagle Flies first comes to Beaver Hollow. Her horse is Old Belle, a smoky black Nokota mare according to the wiki's page on the horse. Karen rides her only once in the story, for the Valentine bank robbery; the rest of the time the mare is kept at camp, for as long as Karen is with the gang.",
        "Le Red Dead Wiki lui attribue un revolver Cattleman et une carabine Carbine Repeater. Dans \"A Rage Unleashed\", elle tient un fusil à double canon, sans s'en servir, lors de la première venue d'Eagle Flies à Beaver Hollow. Sa monture s'appelle Old Belle, une jument Nokota noir fumé selon la page du wiki consacrée au cheval. Karen ne la monte qu'une fois dans l'histoire, pour le braquage de la banque de Valentine ; la jument reste au camp jusqu'au départ de Karen.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "tilly-jackson.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": [
        two(
            "Tilly is her closest friend in camp. Doing chores at Horseshoe Overlook, Tilly says that one day men will help with the work, and Karen laughs and tells her not to count on it. At Clemens Point, Tilly says she robbed a man but let a woman go because the woman needed the money for her son, who had fought in the Civil War. Karen calls her soft, since the son fought for the wrong side; if Arthur is nearby, he will not agree that Tilly has gone soft, and Karen calls him soft too. Tilly also tells Karen and Mary-Beth how Malcolm Foreman took her from her mother.",
            "Tilly est sa plus proche amie au camp. Pendant les corvées, à Horseshoe Overlook, Tilly assure qu'un jour les hommes aideront aux tâches ; Karen rit et lui conseille de ne pas trop y compter. À Clemens Point, Tilly raconte avoir dépouillé un homme, mais épargné une femme qui avait besoin de l'argent pour son fils, ancien combattant de la guerre de Sécession. Karen la trouve devenue bien tendre, le fils s'étant battu dans le mauvais camp ; si Arthur est là, il refuse d'admettre que Tilly s'est ramollie, et Karen le trouve bien tendre, lui aussi. Tilly raconte aussi à Karen et à Mary-Beth comment Malcolm Foreman l'a arrachée à sa mère."),
        two(
            "At Shady Belle, sewing in the gazebo, Karen complains about the swamp and Tilly answers that it beats freezing to death. Inside the manor, Tilly sees that something is wrong; Karen says the good times may not have been as good as she remembers, and Tilly tells her it will be all right. Tilly also tells Arthur she is worried about Karen's drinking and that talking to her will not work. In her 1907 letter (see Biography), Tilly calls Karen a woman \"who was a sister to me\".",
            "À Shady Belle, en cousant sous le kiosque, Karen se plaint du marais, et Tilly lui répond que c'est toujours mieux que de mourir de froid. Dans le manoir, Tilly voit bien que quelque chose ne va pas ; Karen confie que le bon vieux temps n'était peut-être pas aussi bon que dans son souvenir, et Tilly lui assure que tout ira bien. Tilly confie aussi à Arthur qu'elle s'inquiète de la voir boire autant et que lui parler n'y changera rien. Dans sa lettre de 1907 (voir la biographie), Tilly dit de Karen qu'elle était \"a sister to me\" (une sœur pour moi)."),
    ]},
    {"img": "mary-beth-gaskill.jpeg", "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill", "text": [
        two(
            "Mary-Beth shares the young women's chores and outings with Karen and Tilly. At Horseshoe Overlook the two agree that Valentine is not a romantic town, and Karen passes on a rumor of a curse laid on it by Native Americans after a massacre. Mary-Beth tells Tilly she knows that she and Karen make fun of her romance novels. At Clemens Point, Mary-Beth hopes women will one day vote; Karen says men will not allow it and asks Arthur his opinion, and he answers that voting was never his thing.",
            "Mary-Beth partage avec Karen et Tilly les corvées et les sorties des jeunes femmes. À Horseshoe Overlook, toutes deux conviennent que Valentine n'a rien de romantique, et Karen rapporte la rumeur d'une malédiction jetée sur la ville par des Amérindiens après un massacre. Mary-Beth confie à Tilly qu'elle sait que Karen et elle se moquent de ses romans à l'eau de rose. À Clemens Point, Mary-Beth espère que les femmes voteront un jour ; Karen répond que les hommes ne le permettront pas et demande son avis à Arthur, qui répond que le vote ne l'a jamais intéressé."),
        two(
            "At Shady Belle they argue about Saint Denis: Karen says the city is built on dirt, Mary-Beth on memories, and Karen walks off. Karen later tells her she heard of someone in Saint Denis who drank blood, which Mary-Beth finds romantic. In another scene, after Mary-Beth says she stole a necklace from a mansion, Karen admits that the city scares her; Mary-Beth finds it all romantic, and Karen calls her mad. At the party for Jack's return, when Karen vomits by Pearson's wagon, Mary-Beth tries to get her to bed and Karen tells her to leave her alone.",
            "À Shady Belle, elles se disputent au sujet de Saint-Denis : pour Karen, la ville est bâtie sur la crasse, pour Mary-Beth, sur des souvenirs, et Karen finit par tourner les talons. Plus tard, Karen lui raconte avoir entendu parler de quelqu'un qui buvait du sang à Saint-Denis, ce que Mary-Beth trouve romantique. Dans une autre scène, Mary-Beth raconte avoir volé un collier dans une belle demeure ; Karen avoue que la ville lui fait peur, Mary-Beth n'y voit que du romantisme, et Karen la traite de folle. À la fête du retour de Jack, quand Karen vomit près du chariot de Pearson, Mary-Beth essaie de la mettre au lit, et Karen lui dit de la laisser tranquille."),
    ]},
    {"img": "sean-macguire.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": [
        two(
            "At Horseshoe Overlook, behind John's tent, Sean asks Karen whether she missed him. She first claims she cried every night, then says angrily that she missed Davey, Mac and Jenny more. When he tries to hold her she slaps him and threatens to stab him if he touches her again; he answers that he loves it when she talks nasty to him.",
            "À Horseshoe Overlook, derrière la tente de John, Sean demande à Karen si elle s'est languie de lui. Elle prétend d'abord avoir pleuré toutes les nuits, puis lâche avec colère que Davey, Mac et Jenny lui ont bien plus manqué. Quand il tente de l'enlacer, elle le gifle et menace de le poignarder s'il la touche encore ; il répond qu'il adore quand elle lui parle méchamment."),
        two(
            "At the party for his return, according to the Red Dead Wiki, Sean tells her he loves her; she answers that he only loves her when he is drunk, and says she hates him. They go into John's tent and have sex. During the act she cries and says she wants someone to see her, and Sean answers that he does; she leaves the tent as soon as it is over. After his death in Rhodes, Karen tells Arthur at Shady Belle that camp is not the same without Sean, who was full of himself but whom she liked; Arthur tells her Sean had a soft spot for her. She and Susan sing \"A Prisoner for Life\" and dedicate it to him.",
            "À la fête de son retour, d'après le Red Dead Wiki, Sean lui déclare qu'il l'aime ; elle répond qu'il ne l'aime que lorsqu'il a bu, et lui dit qu'elle le déteste. Ils entrent dans la tente de John et couchent ensemble. Pendant l'acte, elle pleure et dit qu'elle veut que quelqu'un la voie, et Sean répond que lui la voit ; elle quitte la tente sitôt l'affaire terminée. Après la mort de Sean à Rhodes, Karen confie à Arthur, à Shady Belle, que le camp n'est plus le même sans lui : il était imbu de lui-même, mais elle l'aimait bien ; Arthur lui répond que Sean avait un faible pour elle. Avec Susan, elle chante \"A Prisoner for Life\" et la lui dédie."),
    ]},
    {"img": "susan-grimshaw.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": [
        two(
            "Karen is the young woman who answers Susan back the most. At Horseshoe Overlook she sits down beside Susan at a meal and recalls that, back in Colter, she had thought about eating her, going as far as describing the dishes she and Pearson had in mind, until Susan leaves the table. At Clemens Point, when Susan finds her drunk at the poker table, Karen replies that she is having a baby, says she will not be bullied, and tells Susan to keep quiet unless she is the one feeding her. While sewing with Tilly, she complains of Susan's nagging, then tells Susan she is learning alchemy.",
            "Karen est la jeune femme qui tient le plus tête à Susan. À Horseshoe Overlook, elle s'assoit près de Susan pendant un repas et lui raconte qu'à Colter elle a songé à la manger, en allant jusqu'à décrire les plats qu'elle et Pearson avaient imaginés, jusqu'à ce que Susan quitte la table. À Clemens Point, quand Susan la trouve ivre à la table de poker, Karen répond qu'elle est en train d'accoucher, déclare qu'elle ne se laissera pas malmener et lui lance qu'à moins de la nourrir, elle n'a qu'à se taire. En cousant avec Tilly, elle se plaint des remontrances de Susan, puis lui annonce qu'elle étudie l'alchimie."),
        two(
            "The two still sing together at the poker table and the campfire (see Skills). Right after Susan shoots Molly O'Shea at the end of \"That's Murfree Country\", Karen lashes out at her. Susan points to the camp's rules, which Molly had broken; Karen rejects that and calls her a murderer.",
            "Les deux femmes chantent pourtant ensemble à la table de poker et au coin du feu (voir Compétences). Juste après que Susan a abattu Molly O'Shea, à la fin de \"That's Murfree Country\", Karen s'en prend à elle ; Susan invoque les règles que Molly a enfreintes, Karen le conteste et la traite de meurtrière."),
    ]},
    {"img": "molly-oshea.jpeg", "slug": "molly-oshea", "name": "Molly O'Shea", "text": two(
        "Karen mocks Molly on the way to Valentine (see Biography). Back at Horseshoe Overlook, Molly confronts her, says Karen is not as clever as she thinks and that Dutch loves her very much; Karen keeps her answers vague, and Molly ends up swearing and leaving in a rage. At Clemens Point Molly demands to know what Karen's problem with her is. The Red Dead Wiki's pages describe the blows differently: on the camp events page Molly slaps Karen, who punches her in the face; on Karen's page Karen slaps Molly when Molly grabs her arm. At Shady Belle, on the dock, Karen tells Molly that nobody is laughing at her (see In her own words); after Molly walks off, Arthur says she is losing it, and Karen answers that she lost it months ago.",
        "Karen se moque de Molly sur la route de Valentine (voir la biographie). De retour à Horseshoe Overlook, Molly vient lui faire face, lui assène qu'elle n'est pas aussi maligne qu'elle le croit et que Dutch l'aime, elle, profondément ; Karen répond par des banalités, jusqu'à ce que Molly jure et s'en aille furieuse. À Clemens Point, Molly exige de savoir ce que Karen a contre elle. Les pages du Red Dead Wiki décrivent les coups différemment : selon la page des événements de camp, Molly gifle Karen, qui lui répond d'un coup de poing au visage ; selon la page de Karen, c'est Karen qui gifle Molly quand celle-ci lui saisit le bras. À Shady Belle, sur le ponton, Karen assure à Molly que personne ne se moque d'elle (voir Dans ses propres mots) ; quand Molly s'éloigne et qu'Arthur la dit en train de perdre la tête, Karen répond qu'elle l'a perdue il y a des mois.")},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "Arthur deals with the man who hits her at the Saints Hotel in \"Polite Society, Valentine Style\", and rides with her on the Valentine bank job (see Biography). At Horseshoe Overlook Karen can invite him to sit down and talk. Depending on the player's choices, he owns up to crimes that weigh on him and says he thinks he is letting his anger out; she warns him that it can only end well if he keeps his head. At Clemens Point, when Dutch dances with Susan at night, Arthur can dance with Karen.",
            "Arthur règle son compte à l'homme qui la frappe au Saints Hotel, dans \"Polite Society, Valentine Style\", et participe avec elle au braquage de la banque de Valentine (voir la biographie). À Horseshoe Overlook, Karen peut l'inviter à s'asseoir et à se confier ; selon les choix du joueur, il avoue des crimes qui le travaillent et dit croire qu'il passe ainsi sa colère, et elle lui répond que tout cela ne finit bien que s'il garde la raison. À Clemens Point, quand Dutch danse le soir avec Susan, Arthur peut inviter Karen à danser."),
        two(
            "At Shady Belle, and again at the party for Jack's return, Karen, who has been drinking, comes over to praise how manly Arthur is; when he tells her she has had too much, she says she has not.",
            "À Shady Belle, puis de nouveau à la fête du retour de Jack, Karen, ivre, s'approche d'Arthur pour vanter sa virilité ; quand il lui fait remarquer qu'elle a trop bu, elle le nie."),
    ]},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "At Clemens Point Bill asks Karen about her plan to rob the Valentine bank. She is willing to bring him in, as long as the job stays hers and he does not cut her out. Lenny and Arthur join them later (see Biography). According to the Red Dead Wiki, Bill asks Arthur whether Karen is sweet on him, and Arthur doubts it.",
        "À Clemens Point, Bill interroge Karen sur son projet de braquer la banque de Valentine. Elle veut bien l'associer au coup, à condition que l'affaire reste la sienne et qu'il ne l'écarte pas. Lenny et Arthur les rejoignent ensuite (voir la biographie). D'après le Red Dead Wiki, Bill demande à Arthur s'il pense que Karen a un faible pour lui, ce dont Arthur doute.")},
    {"img": "lenny-summers.jpeg", "slug": "lenny-summers", "name": "Lenny Summers", "text": two(
        "Lenny is the fourth member of the Valentine bank job (see Biography). On the ride there, when Arthur says he is glad she and Lenny came along, Karen answers that someone has to keep the boys out of trouble, and that she is not sure Lenny can keep his head after the night he and Arthur spent in Valentine.",
        "Lenny est le quatrième homme du braquage de Valentine (voir la biographie). En chemin, quand Arthur se dit content qu'elle et Lenny soient de la partie, Karen répond qu'il faut bien quelqu'un pour garder ces messieurs hors des ennuis, et doute que Lenny garde la tête froide après la nuit qu'Arthur et lui ont passée à Valentine.")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "When Hosea comes back to camp at Clemens Point with a case of drinks after a big win at cards, Karen asks how he did it; he answers that he cheated, like a proper gentleman, and asks her to sing (see Skills). According to the Red Dead Wiki, in another camp scene Karen tells Mary-Beth, who fears the law, that she trusts Dutch and Hosea to protect the gang.",
        "Quand Hosea revient au camp de Clemens Point avec une caisse de bouteilles après un gros gain aux cartes, Karen lui demande comment il s'y est pris ; il répond qu'il a triché, en vrai gentleman, puis lui demande de chanter (voir Compétences). D'après le Red Dead Wiki, dans une autre scène de camp, Karen assure à Mary-Beth, qui craint la loi, qu'elle fait confiance à Dutch et à Hosea pour protéger la bande.")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "At Horseshoe Overlook Karen tells Arthur that the Blackwater ferry job shook her. What stays with her is the sight of the men coming back to camp soaked in blood, Dutch most of all, wearing an expression she had never seen on him.",
        "À Horseshoe Overlook, Karen confie à Arthur que le coup raté du ferry de Blackwater l'a marquée : elle n'oubliera jamais les hommes rentrant au camp couverts de sang, et surtout Dutch, avec dans le regard quelque chose qu'elle ne lui avait jamais vu.")},
    {"img": "kieran-duffy.jpeg", "slug": "kieran-duffy", "name": "Kieran Duffy", "text": two(
        "At Horseshoe Overlook Karen tells the bound Kieran she thought O'Driscolls ate babies but that he looks like one; when he asks her for water, she refuses and throws her cigarette at him. Once he is free, he stops by the poker table to tell her he is still alive; Karen asks Arthur to reassure him, Arthur warns him to watch himself instead, and Karen tells Kieran that the men only act tough. At the party for Jack's return she urges him to drink; he says he might have a little, then insists he will just watch.",
        "À Horseshoe Overlook, Karen lance à Kieran, ligoté, qu'elle croyait que les O'Driscoll mangeaient les bébés, mais qu'il a lui-même l'air d'un bébé ; quand il lui demande de l'eau, elle refuse et lui jette sa cigarette. Une fois libre, il passe à la table de poker lui dire qu'il est toujours en vie ; Karen demande à Arthur de le rassurer, Arthur lui conseille plutôt de faire attention à lui, et Karen explique à Kieran que les hommes ne font que jouer les durs. À la fête du retour de Jack, elle l'encourage à boire ; il dit qu'il prendra peut-être un petit verre, puis affirme qu'il se contentera de regarder.")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "At Horseshoe Overlook Micah whistles at Karen as she works and asks her for a kiss; she leaves without answering. At Shady Belle she calls him Mr. Bell and will not use his first name, so that nobody thinks she likes him. Micah replies that whiskey is all she cares for, that he is the only one in camp who does not worry about her, and that she will get what she deserves.",
        "À Horseshoe Overlook, Micah siffle Karen pendant qu'elle travaille et lui réclame un baiser ; elle s'éloigne sans un mot. À Shady Belle, elle le salue d'un Mr. Bell et refuse de l'appeler par son prénom, pour que personne ne s'imagine qu'elle l'apprécie. Micah réplique que la seule chose qu'elle aime, c'est une bouteille de whiskey, que tout le monde s'inquiète pour elle sauf lui, et qu'elle aura ce qu'elle mérite.")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "At Horseshoe Overlook John, after a few drinks, makes a pass at Karen; she points out that he has Abigail and leaves. If Arthur is close by, John asks him whether he is making a fool of himself, and Arthur says he is.",
        "À Horseshoe Overlook, John, ivre, tente de séduire Karen, qui lui rappelle l'existence d'Abigail et s'en va. Si Arthur est là, John lui demande s'il se conduit comme un idiot, et Arthur ne peut que confirmer.")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "At Shady Belle, while Jack is missing, Abigail cries on John's bed and Karen sits with her, telling her that nobody is going to hurt the boy.",
        "À Shady Belle, pendant la disparition de Jack, Abigail pleure sur le lit de John ; Karen reste auprès d'elle et lui assure que personne ne fera de mal à l'enfant.")},
    {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
        "Uncle rides with Karen, Tilly and Mary-Beth to Valentine in \"Polite Society, Valentine Style\". When Tilly says she can smell the sheep on the way into town, Karen asks: \"Or is that Uncle?\" On the road, after Arthur declines to help a stranded driver catch his horse, she asks Uncle why he did not help, and Uncle pleads lumbago. Uncle, Karen and Susan sing together at the poker table and the campfire (see Skills).",
        "Uncle accompagne Karen, Tilly et Mary-Beth à Valentine dans \"Polite Society, Valentine Style\". Quand Tilly dit sentir l'odeur des moutons à l'entrée de la ville, Karen demande : \"Or is that Uncle?\" (ou alors c'est Uncle ?). Sur la route, après qu'Arthur a refusé d'aider un cocher à rattraper son cheval, elle demande à Uncle pourquoi il n'a pas aidé, et Uncle invoque son lumbago. Uncle, Karen et Susan chantent ensemble à la table de poker et au coin du feu (voir Compétences).")},
    {"img": "simon-pearson.jpeg", "slug": "simon-pearson", "name": "Simon Pearson", "text": two(
        "Pearson sings with Karen at the poker table, \"Poor Lonesome Cowboy\" and, with Uncle, \"Otis Miller\" (see Skills). According to Karen herself, at Colter the two of them could not agree on which dish to make of Susan (see Susan Grimshaw).",
        "Pearson chante avec Karen à la table de poker, \"Poor Lonesome Cowboy\" puis, avec Uncle, \"Otis Miller\" (voir Compétences). À en croire Karen, à Colter, tous deux n'arrivaient pas à se mettre d'accord sur la recette à appliquer à Susan (voir Susan Grimshaw).")},
    {"img": "josiah-trelawny.jpeg", "slug": "josiah-trelawny", "name": "Josiah Trelawny", "text": two(
        "At Clemens Point Trelawny asks Karen about the book she is reading by the wagons, which she calls a silly romance. Susan cuts in to ask whether Karen means to do any work. Trelawny answers with a trick, producing a crow from his hand; Susan walks off, disgusted, while Karen laughs. After he plays a similar trick on Mary-Beth, Karen calls him a devil; Mary-Beth calls him a kind devil.",
        "À Clemens Point, Trelawny interroge Karen sur le livre qu'elle lit près des chariots, une romance idiote, selon elle. Susan les interrompt pour demander si Karen compte travailler un jour ; Trelawny fait surgir un corbeau de sa main, Susan s'en va écœurée et Karen éclate de rire. Après un tour du même genre joué à Mary-Beth, Karen le traite de diable ; Mary-Beth, elle, le trouve gentil, pour un diable.")},
    {"img": "orville-swanson.jpeg", "slug": "orville-swanson", "name": "Orville Swanson", "text": two(
        "At Colter Swanson reads a passage of Isaiah aloud from his Bible. When he finishes, Karen asks him what it means; he says he does not know, but that the words comfort him.",
        "À Colter, Swanson lit à voix haute un passage d'Isaïe dans sa Bible. Quand il a fini, Karen lui demande ce que cela veut dire ; il avoue n'en avoir aucune idée, mais dit que ça le réconforte.")},
    {"img": "sadie-adler.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
        "Dutch puts Sadie in the care of Karen and Tilly when he brings her to Colter (see Biography). Later the two are the only women of the gang who stand guard (see Skills).",
        "Dutch confie Sadie à Karen et à Tilly quand il l'amène à Colter (voir la biographie). Par la suite, ce sont les deux seules femmes du gang à monter la garde (voir Compétences).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Javier plays the guitar on several of Karen's songs in camp (see Skills), and in chapter 6 the two escort Eagle Flies into Beaver Hollow (see Biography). According to the Red Dead Wiki, Karen says Javier was a close friend of Jenny Kirk, and the two talk about her in camp.",
        "Javier accompagne à la guitare plusieurs chansons de Karen au camp (voir Compétences), et au chapitre 6, tous deux escortent Eagle Flies jusqu'à Beaver Hollow (voir la biographie). D'après le Red Dead Wiki, Karen affirme que Javier était un ami proche de Jenny Kirk, et tous deux parlent d'elle au camp.")},
    {"img": None, "slug": None, "name": "Davey and Mac Callander", "text": two(
        "The brothers are lost after the Blackwater robbery: Davey reaches Colter already dead of his wounds, and Mac is missing. Karen tells Sean she missed them more than him (see Sean MacGuire). According to the Red Dead Wiki, she also says that she used to yell at the noisy brothers to shut up all the time, and that she misses doing it now that they are gone.",
        "Les deux frères sont perdus après le braquage de Blackwater : Davey arrive à Colter déjà mort de ses blessures, et Mac manque à l'appel. Karen dit à Sean qu'ils lui ont manqué davantage que lui (voir Sean MacGuire). D'après le Red Dead Wiki, elle raconte aussi qu'elle passait son temps à crier aux deux frères, toujours bruyants, de se taire, et que ça lui manque maintenant qu'ils ne sont plus là.")},
    {"img": None, "slug": None, "name": "Jenny Kirk", "text": two(
        "Jenny, a young member of the gang, is wounded in the Blackwater robbery and dies during the flight to Colter, according to the Red Dead Wiki. The wiki adds that Karen says in a camp conversation that she misses her and that Jenny died too young.",
        "Jenny, une jeune membre de la bande, est blessée lors du braquage de Blackwater et meurt pendant la fuite vers Colter, selon le Red Dead Wiki. Le wiki rapporte aussi que Karen confie dans une conversation de camp qu'elle lui manque et qu'elle est morte trop jeune.")},
]
