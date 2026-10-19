"""Lenny Summers, part B: Personality (official descriptions, traits, In his own words, Names,
Appearance), Skills/gameplay/weapons/horse, Relationships (19 Oct 2026).

Sources (register): Rockstar character description of 6 Sep 2018 (English text as reprinted by
The Hollywood Reporter / Heat Vision, Sep 2018, saved in ../charles/fc/thr_descriptions.txt; French
text from rockstargames.com/reddeadredemption2/fr/features/vanderlindegang, as quoted by the French
Red Dead Wiki page "Lenny Summers", saved in lenny/fr.txt); character biography page from an official
guide (wiki file LennySummersBio.jpg, captioned "Biography in RDR 2", downloaded to lenny/fc/bio.img and
read: text quoted verbatim; Wikipedia's character list cites the same facts to The Complete Official
Guide, Collector's Edition, Piggyback, 2018, p. 378); the in-game document "Letter to Lenny from Father"
(wiki file Letter_from_Lenny's_Father_content.jpg, downloaded to lenny/fc/letter.png and read); Red Dead
Wiki EN "Lenny Summers" (infobox, quote box with audio file, Personality, Appearance, Trivia, Gallery
captions); FR "Lenny Summers"; wiki pages "Camp Events" (Horseshoe Overlook, Sean's return party,
Clemens Point, Shady Belle, Jack's return party, Lakay), "Five Finger Fillet", "Coach Robbery (Lenny
Summers)", "Maggie", "Susan Grimshaw", "Davey Callander", "Bill Williamson", "Hosea Matthews".
Transcripts: Who the Hell is Leviticus Cornwall?; Old Friends; Outlaws from the West; Eastward Bound;
Sodom? Back to Gomorrah; Exit, Pursued by a Bruised Ego (fc/d_Exit_Pursued_by_a_Bruised_Ego_Dialogues.txt);
the Colter cabin scene with Pearson (Arthur: "Lenny's more into book reading than hunting").
Fact-checked fiches reused for consistency: arthur_B, arthur_D, dutch_C, hosea_B, micah_B, bill_B,
charles_B, javier_B, sadie_B, abigail_B, jack_B.

Ownership (FIX_RULES): official descriptions (Rockstar 2018 EN+FR, guide biography page), names
(Leonard, Lenny, the father's letter), appearance, skills, gameplay (camp availability, Five Finger
Fillet, Coach Robbery availability, ejection from camp), weapons, the horse Maggie, and all camp scenes
live HERE. Each camp scene sits in ONE relationship entry (age teasing at cards, "who are we running
from", worry about the South -> Arthur; Evelyn Miller debate, Shady Belle speech -> Dutch; "good head",
"Lenny and Jenny", burial wish -> Hosea; "boy", shove, drink after a coach job, poker gossip -> Bill;
"folk like you", pride before a fall -> Micah; reading lessons, who to hate, the Callanders, "buddy is
back" -> Sean; hunting complaint -> Pearson; cooking mockery -> Susan; poker silence -> Charles; the
South -> Tilly; "Lennyyyy" at Jack's party -> Jack). Narrative events (joining the gang, Colter, the
train, Strawberry, A Quiet Time, Shady Belle raid, Valentine bank, Braithwaite, the gala, trolley
station, Bronte, the bank and his death, the burial) live in part A; entries refer to them in one clause.
Fact-check of 19 Oct 2026 applied: Names (Arthur says "Leonard" once, in "Preaching Forgiveness as He
Went", mission page; the letter itself is told in part A, Origins); duplicates cut from Personality,
Skills and Relationships (each camp scene or event kept once); Micah's "pride before a fall" placed in
the Guarma camp; Urban Pleasures credit left to part A (attributed to the wiki); Mary-Beth entry merged
into Susan's.
Lines quoted in this part (parts A and C must NOT repeat them): Rockstar EN/FR descriptions; the guide
page text; the wiki quote box line "Before me, at least six generations..."; "Just happy we're back
at'em, Dutch." and "'Course I'm ready." (Who the Hell is Leviticus Cornwall?); "At first, I thought, 'bad
idea...'" and "next time I'll know what you mean by 'a couple of drinks.'" (Sodom? Back to Gomorrah);
the letter's "My Dear Leonard" and "more tutor than father"; Hosea's "a good head on his shoulders" and
"Lenny and Jenny could never have worked."; Arthur's "pretty sweet on her" and "Lenny's more into book
reading than hunting."; Karen's "I ain't even sure Lenny can be relied on to keep his head..." (Sodom).
Paraphrased here, free for part C to quote: Dutch's "first man on his horse"; "When you fall... there'll
be a party"; "Shut up. Me and Arthur did all the work."; Micah's "Least we all know you can read".

WIKI-ONLY (kept, attributed): quote box line (with the wiki's audio file); age teasing at poker and Five
Finger Fillet; Sean conversation on whom to hate; Evelyn Miller details (fraud, freedom, "wary" joke);
Jenny burial idea in Colter and Five Finger Fillet mention; Micah's claim about Jenny in a companion
activity; burial-with-friends wish; Susan's scolding of Lenny and Mary-Beth (YouTube refs); "dangerous
fool" on Davey (YouTube ref); weapons, finishes and horse (infobox, trivia, Maggie page); age 19,
build and height (Appearance section); camp routines (newspaper, guard duty).

Excluded: "joined around December 1898" and "six months" (part A, Origins); the letter's supposed
"abandonment of his family" (the wiki misreads it: the letter is written three days after the father
left by train and expects to meet again "on Sunday next"); the letter's "redeemed" sentence as a
reading of the series' theme (interpretation); "intelligent, fun-loving", "very loyal", "most educated
due to his upbringing", "displays no real care of what others think, perhaps because...", "satirically
compares himself to stereotypes" (wiki interpretation); the Hosea/Arthur and John/Arthur "mirror"
(trivia, interpretation); the gang's reactions to his death "paint a clue to their personality"
(interpretation); "appears to be still alive" after being shot and the journal head/abdomen
discrepancy (part C Trivia if kept); outfit catalogue (SPEC); cut content, actor, trailer look (part D);
Curzon Dobell's favorite character (speaker not identified in the panel captions, as in hosea_D);
Javier "looks back" at the body (wiki reading of an animation); Leviticus Cornwall and Angelo Bronte
(no personal exchange with Lenny; their jobs are told in part A).
"""

def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character description, published on September 6, 2018, reads: \"Young Lenny has been on the run since he was 15 years old after killing the men who murdered his father. Smart, educated, competent and ambitious, he is always ready to do his part.\" A character page from an official guide, reproduced on the Red Dead Wiki, calls him \"a fairly recent addition to the gang\" and adds that \"his father and uncle were well-educated and gave Lenny a good schooling when he was growing up.\" The same page ends: \"Smart, competent and ambitious, he is always ready to do his part, and is fairly happy living in a community where he is mostly judged for his ability not his appearance.\" Wikipedia's list of the game's characters cites The Complete Official Guide (Piggyback, 2018) for these points.",
        "La description officielle publiée par Rockstar le 6 septembre 2018 (version française) : « Le jeune Lenny est en cavale depuis l'âge de 15 ans pour avoir assassiné l'homme qui a tué son père. Intelligent, instruit, compétent et ambitieux, il est toujours prêt à mettre la main à la pâte. » Le texte anglais parle, lui, des hommes qui ont tué son père, au pluriel. Une page de personnage tirée d'un guide officiel, reproduite sur le Red Dead Wiki, le présente comme \"a fairly recent addition to the gang\" (une recrue assez récente) et précise que son père et son oncle, des hommes instruits, lui ont donné une bonne éducation. Elle se termine ainsi : \"Smart, competent and ambitious, he is always ready to do his part, and is fairly happy living in a community where he is mostly judged for his ability not his appearance.\" (intelligent, compétent et ambitieux, il est toujours prêt à faire sa part, et plutôt heureux de vivre dans une communauté qui le juge surtout sur ses capacités, et non sur son apparence). La liste des personnages du jeu sur Wikipédia cite The Complete Official Guide (Piggyback, 2018) pour ces éléments.")},
    {"p": two(
        "He reads and writes (see Biography). He argues with Dutch about books and tries to teach Sean to read (see Relationships). He jokes easily, including at Arthur's expense.",
        "Il sait lire et écrire (voir la biographie). Il débat de livres avec Dutch et essaie d'apprendre à lire à Sean (voir les relations). Il plaisante volontiers, y compris aux dépens d'Arthur.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "The Red Dead Wiki opens its page on him with this line, with an audio clip from the game: \"Before me, at least six generations were born in chains and for the last three years, I've been running from every lawman and bounty hunter west of the Lannahechee River... So yeah, I feel lucky!\" On the ride to Cornwall's train, in \"Who the Hell is Leviticus Cornwall?\", he answers Dutch's praise with \"Just happy we're back at'em, Dutch.\" When Javier asks whether he is ready: \"'Course I'm ready.\"",
        "Le Red Dead Wiki ouvre sa page sur cette réplique, accompagnée d'un extrait sonore du jeu : \"Before me, at least six generations were born in chains and for the last three years, I've been running from every lawman and bounty hunter west of the Lannahechee River... So yeah, I feel lucky!\" (avant moi, au moins six générations sont nées dans les chaînes, et depuis trois ans j'ai à mes trousses tous les hommes de loi et chasseurs de primes à l'ouest de la Lannahechee... alors oui, je me sens chanceux !). En route vers le train de Cornwall, dans \"Who the Hell is Leviticus Cornwall?\", il répond aux éloges de Dutch : \"Just happy we're back at'em, Dutch.\" (content qu'on s'y remette, Dutch). Quand Javier lui demande s'il est prêt : \"'Course I'm ready.\" (évidemment que je suis prêt).")},
    {"p": two(
        "On the way to the Valentine bank in \"Sodom? Back to Gomorrah\", Arthur asks him how he feels about the job: \"At first, I thought, 'bad idea...' but then I figure, they all are if you think about 'em long enough.\" On the same ride, he looks back on his night out with Arthur in Valentine: \"Yeah, next time I'll know what you mean by 'a couple of drinks.'\"",
        "En route vers la banque de Valentine, dans \"Sodom? Back to Gomorrah\", Arthur lui demande ce qu'il pense du coup : \"At first, I thought, 'bad idea...' but then I figure, they all are if you think about 'em long enough.\" (au début, je me suis dit : mauvaise idée... et puis j'ai pensé qu'elles le sont toutes, si on y réfléchit assez longtemps). Pendant le même trajet, il repense à sa soirée avec Arthur à Valentine : \"Yeah, next time I'll know what you mean by 'a couple of drinks.'\" (la prochaine fois, je saurai ce que tu entends par \"quelques verres\").")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "The gang calls him Lenny. His given name, Leonard, comes from his father's letter found in camp, \"Letter to Lenny from Father\" (see Origins), which opens \"My Dear Leonard\". Arthur uses the full name only once, in \"Preaching Forgiveness as He Went\", after the two have shot the three Raiders who stop them on the road. Dutch calls him young Lenny, and Bill calls him boy until Dutch tells him to stop (see Bill Williamson). The French Red Dead Wiki uses the same names.",
        "La bande l'appelle Lenny. Son prénom, Leonard, vient de la lettre de son père que l'on trouve au camp, \"Letter to Lenny from Father\" (voir Origines), qui commence par \"My Dear Leonard\" (mon cher Leonard). Arthur ne l'appelle par ce prénom qu'une seule fois, dans \"Preaching Forgiveness as He Went\", après avoir abattu avec lui les trois Raiders qui les arrêtent sur la route. Dutch l'appelle le jeune Lenny, et Bill l'appelle boy (le garçon) jusqu'à ce que Dutch lui demande d'arrêter (voir Bill Williamson). Le Red Dead Wiki français emploie les mêmes noms.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "The guide's portrait shows a slim young man with short black hair and a thin mustache, in a white shirt with a rounded collar and suspenders, holding a pump-action shotgun. According to the Red Dead Wiki, he is slightly shorter than Arthur. On jobs he covers his face with an orange bandana; the wiki notes that most gang members wear black ones, and that only Dutch and Uncle also wear another color.",
        "Le portrait du guide montre un jeune homme mince, cheveux noirs courts et fine moustache, en chemise blanche à col rond et bretelles, un fusil à pompe à la main. D'après le Red Dead Wiki, il est un peu plus petit qu'Arthur. Pendant les coups, il se masque le visage d'un bandana orange ; le wiki relève que la plupart des membres du gang en portent un noir, et que seuls Dutch et Uncle en ont aussi d'une autre couleur.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Skills, weapons and horse", "Compétences, armes et cheval")},
    {"h4": two("With the gang in 1899", "Avec le gang en 1899")},
    {"p": two(
        "Lenny takes part in most of the gang's big jobs of 1899, from Cornwall's train to the Saint Denis bank (see Biography). He also brings in his own leads: the Lemoyne Raiders' weapons at Shady Belle and the banking coach of his companion activity.",
        "Lenny participe à la plupart des grands coups du gang en 1899, du train de Cornwall à la banque de Saint-Denis (voir la biographie). Il rapporte aussi ses propres pistes : les armes des Lemoyne Raiders à Shady Belle et la diligence de banque de son activité de compagnon.")},
    {"p": two(
        "He is the partner of one companion activity, \"Coach Robbery\", which becomes available after \"Angelo Bronte, A Man of Honor\" in chapter 4 and disappears after \"Country Pursuits\". He is the only opponent at Five Finger Fillet in camp during chapter 2. His camp events start after \"A Quiet Time\"; he is away from camp while some of his missions are available, and his events end for good after \"Banking, The Old American Art\". If Arthur provokes too many of his companions, Lenny is one of six gang members, with John, Bill, Javier, Charles and Sean, who can knock him down and expel him from camp.",
        "Il est le partenaire d'une activité de compagnon, \"Coach Robbery\", qui se débloque après \"Angelo Bronte, A Man of Honor\" au chapitre 4 et disparaît après \"Country Pursuits\". Au chapitre 2, c'est le seul adversaire au jeu du couteau (Five Finger Fillet) au camp. Ses événements de camp commencent après \"A Quiet Time\" ; il s'absente du camp tant que certaines de ses missions sont disponibles, et ses événements cessent définitivement après \"Banking, The Old American Art\". Si Arthur se met à dos trop de ses compagnons, Lenny fait partie des six membres de la bande, avec John, Bill, Javier, Charles et Sean, qui peuvent le mettre à terre et le chasser du camp.")},
    {"h4": two("Weapons and horse", "Armes et cheval")},
    {"p": two(
        "At Colter he stands watch with a Carbine Repeater. The Red Dead Wiki lists among his weapons a custom Cattleman Revolver, in worn blackened steel with an ebony grip, a custom Rolling Block Rifle in blued steel with a browned frame and maple varnish, a Pump-Action Shotgun and a Bolt Action Rifle; it also shows his knife. His horse, according to the same wiki, is Maggie, a light palomino Mustang mare, which carries him out of Strawberry and through his jobs of 1899.",
        "À Colter, il monte la garde avec une Carbine Repeater. Le Red Dead Wiki lui attribue un Cattleman Revolver personnalisé, en acier noirci patiné avec une crosse en ébène, un Rolling Block Rifle personnalisé, en acier bleui avec une carcasse brunie et un vernis érable, un Pump-Action Shotgun et un Bolt Action Rifle ; il montre aussi son couteau. Son cheval, selon le même wiki, est Maggie, une jument Mustang palomino clair, qui l'emporte loin de Strawberry et l'accompagne dans ses coups de 1899.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "Arthur is the gang member Lenny rides with most: Cornwall's train, the night in Valentine, the Shady Belle raid, the Valentine bank, the trolley station and the coach job (see Biography). At the poker table and at Five Finger Fillet, according to the Red Dead Wiki, Lenny teases him about being slow at his age. In the Clemens Point camp he asks Arthur who they are really running from, the Pinkertons or Cornwall; Arthur answers that Cornwall is the one paying the Pinkertons.",
            "Arthur est le membre de la bande avec qui Lenny chevauche le plus : le train de Cornwall, la nuit de Valentine, le raid de Shady Belle, la banque de Valentine, la gare de tramways et l'attaque de diligence (voir la biographie). À la table de poker et au jeu du couteau, d'après le Red Dead Wiki, Lenny le taquine sur sa lenteur, à son âge. Au camp de Clemens Point, il lui demande qui ils fuient vraiment, les Pinkerton ou Cornwall ; Arthur répond que c'est Cornwall qui paie les Pinkerton."),
        two(
            "In the same camp Lenny tells Arthur how uneasy he feels in the South, given where he comes from, and Arthur tells him they will be all right. At Jack's return party at Shady Belle, Arthur can shout his name the way he did in Valentine, and Lenny answers, alarmed, that it is all coming back to him. Arthur stops at his body on the rooftops of Saint Denis.",
            "Dans ce même camp, Lenny confie à Arthur son malaise dans le Sud, vu ses origines, et Arthur lui assure que tout ira bien. À la fête donnée pour le retour de Jack à Shady Belle, Arthur peut hurler son prénom comme à Valentine, et Lenny répond, effrayé, que tout lui revient. Sur les toits de Saint-Denis, Arthur s'arrête devant son corps."),
    ]},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "At Horseshoe Overlook the two debate the writings of Evelyn Miller beside Dutch's tent; Lenny keeps answering back until Dutch concedes. According to the Red Dead Wiki, Lenny dismisses Miller as a fraud and holds up the gang as a truer picture of American freedom; Dutch laughs and, if Arthur is nearby, jokingly tells him to watch out for the young man's brains. Dutch stops Bill from calling him boy (see Bill Williamson). During Jack's return party at Shady Belle, Dutch gives Lenny, Bill, Charles and Micah a speech about his new plan as a storm starts. Lenny dies during the bank robbery Dutch leads in Saint Denis.",
        "À Horseshoe Overlook, tous deux débattent des écrits d'Evelyn Miller près de la tente de Dutch ; Lenny lui tient tête jusqu'à ce que Dutch s'avoue vaincu. D'après le Red Dead Wiki, Lenny balaie Miller comme un imposteur et présente la bande comme une image plus fidèle de la liberté américaine ; Dutch en rit et, si Arthur est à proximité, lui conseille en plaisantant de se méfier de l'intelligence du jeune homme. Dutch interdit à Bill de l'appeler boy (voir Bill Williamson). Pendant la fête pour le retour de Jack, à Shady Belle, Dutch expose son nouveau plan à Lenny, Bill, Charles et Micah alors qu'un orage éclate. Lenny meurt pendant le braquage de banque que Dutch mène à Saint-Denis.")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "On the bear hunt of \"Exit, Pursued by a Bruised Ego\", Hosea says that Lenny has \"a good head on his shoulders\" and, if Micah has been rescued, that it was lucky Lenny was with him. When Hosea coughs at the campfire while talking with Abigail, Lenny or Swanson pats him on the back. According to the Red Dead Wiki, both men say in camp conversations that they want to be buried with friends. Both die in the Saint Denis bank job and are buried side by side (see Biography).",
        "Pendant la chasse à l'ours de \"Exit, Pursued by a Bruised Ego\", Hosea dit de Lenny qu'il a \"a good head on his shoulders\" (la tête sur les épaules) et, si Micah a été tiré d'affaire, que c'est une chance que Lenny ait été avec lui. Quand Hosea tousse au coin du feu en parlant avec Abigail, Lenny ou Swanson lui tape dans le dos. D'après le Red Dead Wiki, les deux hommes disent, dans des conversations de camp, vouloir être enterrés auprès d'amis. Tous deux meurent pendant le braquage de la banque de Saint-Denis et sont enterrés côte à côte (voir la biographie).")},
    {"img": None, "slug": None, "name": "Jenny Kirk", "text": two(
        "Jenny Kirk, a recent recruit like Lenny, was wounded in the failed ferry job in Blackwater and died before the gang reached Colter. On the bear hunt, Arthur tells Hosea that Lenny was \"pretty sweet on her\", and Hosea replies: \"Lenny and Jenny could never have worked.\" According to the Red Dead Wiki, Lenny suggests giving her a proper burial while the gang is at Colter and mentions her during Five Finger Fillet. The wiki adds that Micah, on an outing with Arthur, boasts that Jenny had been with him and asks whether Lenny knows; an irritated Arthur orders him to keep it to himself.",
        "Jenny Kirk, recrue récente comme Lenny, a été blessée lors du coup raté du ferry à Blackwater et est morte avant que la bande n'atteigne Colter. Pendant la chasse à l'ours, Arthur confie à Hosea que Lenny avait \"pretty sweet on her\" (un faible pour elle), et Hosea répond : \"Lenny and Jenny could never have worked.\" (Lenny et Jenny, ça n'aurait jamais pu marcher). D'après le Red Dead Wiki, Lenny propose de lui offrir une vraie sépulture pendant le séjour à Colter et parle d'elle au jeu du couteau. Le wiki ajoute que Micah, lors d'une sortie avec Arthur, se vante d'avoir eu Jenny et demande si Lenny le sait ; agacé, Arthur lui ordonne de garder ça pour lui.")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "Micah taunts Lenny from their first scene together in the Colter cabin, and the two are sent scouting together twice, which ends with Micah jailed in Strawberry (see Biography). In the Clemens Point camp Micah calls out that he has shot many folk like Lenny; asked what he means, Micah says cowards, and laughs as Lenny walks away. If Arthur is there, he says Micah would miss at that range. In the Guarma camp, asked by Arthur, Micah dismisses Lenny's death as pride before a fall.",
        "Micah raille Lenny dès leur première scène commune, dans la cabane de Colter, et les deux hommes partent deux fois ensemble en reconnaissance, ce qui se termine par l'arrestation de Micah à Strawberry (voir la biographie). Au camp de Clemens Point, Micah lui lance qu'il a abattu bien des gens comme lui ; quand Lenny demande ce qu'il entend par là, Micah répond des lâches, et rit pendant que Lenny s'éloigne. Si Arthur est présent, il lui fait remarquer qu'à cette distance, il raterait sa cible. Au camp de Guarma, interrogé par Arthur, Micah réduit la mort de Lenny à l'orgueil qui précède la chute.")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "At Horseshoe Overlook Bill pushes Lenny to the ground behind John's tent; Lenny can laugh at him and tell him to get lost. Asked by Arthur, Bill complains that Lenny shows him no respect, and Arthur turns the charge back on him. When Bill calls him boy, Lenny ignores him, and Dutch tells Bill that Lenny does not like the word anymore; Bill apologizes to Dutch. After a successful coach robbery the two sit down for a friendly drink.",
        "À Horseshoe Overlook, Bill pousse Lenny à terre derrière la tente de John ; Lenny peut lui rire au nez et l'envoyer promener. Interrogé par Arthur, Bill se plaint que Lenny lui manque de respect, et Arthur lui retourne le reproche. Quand Bill l'appelle boy, Lenny l'ignore, et Dutch fait savoir à Bill que Lenny n'aime plus ce mot ; Bill s'excuse auprès de Dutch. Après une attaque de diligence réussie, les deux hommes s'assoient pour boire un verre, en bons termes.")},
    {"img": "sean-macguire.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
        "At the Horseshoe Overlook poker table Lenny tries to teach Sean to read. Sean keeps putting it off, then asks him to stop: reading would only put silly ideas in his head, to which Lenny answers that this is the point, and that he will not give up on him. At Sean's return party Lenny tells Arthur how glad he is that his friend is back, and in the Clemens Point camp the two gossip about Bill. According to the Red Dead Wiki, Lenny tells Sean in another conversation that he is not sure whom to hate more, the slavers who held his ancestors or the white people who resent him now, and he calls Davey Callander a dangerous fool whom he suspects of causing the Blackwater job to go wrong.",
        "À la table de poker de Horseshoe Overlook, Lenny essaie d'apprendre à lire à Sean. Sean remet toujours à plus tard, puis lui demande d'arrêter : la lecture ne ferait que lui mettre des idées stupides dans la tête, à quoi Lenny répond que c'est justement le but, et qu'il ne le lâchera pas. Lors de la fête pour le retour de Sean, Lenny dit à Arthur combien il est content que son ami soit revenu, et au camp de Clemens Point, les deux disent du mal de Bill. D'après le Red Dead Wiki, Lenny confie à Sean, dans une autre conversation, qu'il ne sait pas qui détester le plus, des esclavagistes qui ont asservi ses ancêtres ou des Blancs qui lui en veulent aujourd'hui, et il traite Davey Callander d'imbécile dangereux, qu'il soupçonne d'avoir fait capoter le coup de Blackwater.")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Dutch posts Javier and Lenny together on the hill above the O'Driscoll camp in \"Old Friends\". Before Cornwall's train, Javier asks him whether he is ready, then misses the jump onto the train, on which Lenny lands hanging from the side of a car. Both take part in the Saint Denis bank job, in which Lenny is killed.",
        "Dans \"Old Friends\", Dutch poste Javier et Lenny ensemble sur la colline qui domine le camp des O'Driscoll. Avant le train de Cornwall, Javier lui demande s'il est prêt, puis rate le saut sur le convoi, où Lenny atterrit suspendu au flanc d'un wagon. Tous deux participent au braquage de la banque de Saint-Denis, où Lenny est tué.")},
    {"img": "charles-smith.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
        "At the Horseshoe Overlook poker table Lenny tries to start a conversation with Charles, without success. Both are part of the crews of \"Blood Feuds, Ancient and Modern\" and of the Saint Denis bank job. According to the Red Dead Wiki, Charles is among the survivors who take Lenny's and Hosea's bodies from the morgue.",
        "À la table de poker de Horseshoe Overlook, Lenny tente d'engager la conversation avec Charles, sans succès. Tous deux font partie des équipes de \"Blood Feuds, Ancient and Modern\" et du braquage de la banque de Saint-Denis. D'après le Red Dead Wiki, Charles fait partie des survivants qui récupèrent les corps de Lenny et d'Hosea à la morgue.")},
    {"img": "karen-jones.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": two(
        "Karen and Bill, with Lenny already on board, bring Arthur in on the robbery of the Valentine bank. On the way she says: \"I ain't even sure Lenny can be relied on to keep his head... not after that night you two had in Valentine.\"",
        "Karen et Bill, avec qui Lenny est déjà d'accord, associent Arthur au braquage de la banque de Valentine. En chemin, elle lâche : \"I ain't even sure Lenny can be relied on to keep his head... not after that night you two had in Valentine.\" (je ne suis même pas sûre qu'on puisse compter sur Lenny pour garder la tête froide... pas après la nuit que vous avez passée à Valentine).")},
    {"img": "tilly-jackson.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
        "In the Clemens Point camp Tilly, like Lenny, tells Arthur how uncomfortable she feels in the South, and Arthur reassures her (see Arthur Morgan).",
        "Au camp de Clemens Point, Tilly, comme Lenny, confie à Arthur son malaise dans le Sud, et Arthur la rassure (voir Arthur Morgan).")},
    {"img": "simon-pearson.jpeg", "slug": "simon-pearson", "name": "Simon Pearson", "text": two(
        "At Colter Pearson complains to Arthur that he sent Lenny and Bill hunting and they came back with nothing; Arthur answers: \"Lenny's more into book reading than hunting.\"",
        "À Colter, Pearson se plaint auprès d'Arthur d'avoir envoyé Lenny et Bill chasser et de les avoir vus revenir bredouilles ; Arthur répond : \"Lenny's more into book reading than hunting.\" (Lenny, c'est plus les livres que la chasse).")},
    {"img": "susan-grimshaw.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
        "At Colter, Susan puts Lenny in a shared room with Micah, Javier, Charles and Bill. According to the Red Dead Wiki, she scolds Lenny and Mary-Beth when they make fun of Pearson's cooking, telling them to mind their manners because Pearson takes good care of them.",
        "À Colter, Susan installe Lenny dans une chambre partagée avec Micah, Javier, Charles et Bill. D'après le Red Dead Wiki, elle reprend Lenny et Mary-Beth quand ils se moquent de la cuisine de Pearson, en leur demandant de surveiller leurs manières, puisque Pearson prend bien soin d'eux.")},
    {"img": "sadie-adler.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
        "Lenny is on watch at Colter when Dutch rides in with Sadie (see Biography). After the Lemoyne Raiders attack in \"Further Questions of Female Suffrage\", Arthur tells Lenny that Sadie did \"more than fine\". According to the Red Dead Wiki, Sadie is among the survivors who recover his body after the Saint Denis bank job.",
        "Lenny est de garde à Colter quand Dutch arrive avec Sadie (voir la biographie). Après l'attaque des Lemoyne Raiders dans \"Further Questions of Female Suffrage\", Arthur dit à Lenny que Sadie s'en est \"more than fine\" (plus que bien) sortie. D'après le Red Dead Wiki, Sadie fait partie des survivants qui récupèrent son corps après le braquage de Saint-Denis.")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "When Arthur and Javier bring John back to Colter wounded by wolves, Lenny and Bill carry him into a cabin. Both men later take part in the raid on Braithwaite Manor, the assault on Bronte's mansion and the Saint Denis bank job, where John is arrested and Lenny killed.",
        "Quand Arthur et Javier ramènent à Colter John, blessé par les loups, Lenny et Bill le portent jusqu'à une cabane. Les deux hommes participent ensuite au raid sur le manoir Braithwaite, à l'assaut de la demeure de Bronte et au braquage de la banque de Saint-Denis, où John est arrêté et Lenny tué.")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "At Lakay, Abigail tells Dutch, back from Guarma, that the survivors took Lenny's and Hosea's bodies from the morgue and buried them (see Biography).",
        "À Lakay, Abigail apprend à Dutch, de retour de Guarma, que les survivants ont récupéré les corps de Lenny et d'Hosea à la morgue pour les enterrer (voir la biographie).")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "Lenny rides to Braithwaite Manor with the men looking for the kidnapped Jack in \"Blood Feuds, Ancient and Modern\", and is at the campfire when the gang welcomes the boy back to Shady Belle.",
        "Lenny fait partie des hommes qui partent pour le manoir Braithwaite à la recherche de Jack, enlevé, dans \"Blood Feuds, Ancient and Modern\", et il est au coin du feu quand la bande accueille le garçon à Shady Belle.")},
]
