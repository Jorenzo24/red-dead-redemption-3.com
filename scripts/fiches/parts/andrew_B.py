"""Andrew Milton, part B: Personality (official descriptions, traits, In his own words, Names,
Appearance), Skills (Pinkerton agent: mandate and means, weapons and horse), Relationships (20 Oct 2026,
medium tier).

Sources (register): Rockstar published no 6 Sep 2018 character description of Milton (the descriptions in
../uncle/fc/thr_descriptions.txt cover the Van der Linde gang only; no match for Milton or Pinkerton) and no
official guide biography page is known. Transcripts: "A Fisher of Men/dialogues" (river scene),
"The Battle of Shady Belle/dialogues" (Clemens Point, ride to Shady Belle), "Red Dead Redemption (mission)/
dialogues" (Tilly's report, Van Horn, Arthur to Dutch, John and Micah). No transcript exists on the wiki for
"Banking, The Old American Art", "Fleeting Joy" or "Just a Social Call" (pages missing, checked 20 Oct 2026):
those scenes follow the fact-checked parts (hosea_A, arthur_B/C, dutch_B, sadie_A/B, micah_B, edgar_A/B) and
the wiki's quote list, attributed. Newspaper "Bureau of Investigation Founded" (Blackwater Ledger No. 74, New
Hanover Gazette No. 39, Saint Denis Times No. 55; wiki transcription). Red Dead Wiki EN "Andrew Milton"
(infobox: aliases, weapons, Andalusian; quote list; Appearance; Trivia), FR "Andrew Milton" (aliases, incl.
"Agent Ducon" for Agent Moron), "Agent Johns" (quote box and quotes), "Red Dead Redemption 2 Cut Content"
("Milton Andrews" in the files). Fact-checked parts reused: arthur_A/B/C, dutch_A/B, hosea_A/B, edgar_A/B,
micah_A/B, molly_A, sadie_A/B, abigail_A/B, jack_A/B, tilly_B, susan_A/B, lenny_A.

Ownership: names (Agent Milton, Mr. Milton, the late first name, Agent Moron, your new friend, Milton Andrews),
appearance, mandate and means, weapons and horse live HERE. Narrative events (river meeting, Clemens Point
offer, bank and Hosea's execution, Lakay, Annesburg, Abigail's seizure, Van Horn and his death) live in part A;
relationship entries refer to them in one clause.
Lines quoted in this part (parts A and C must NOT repeat them verbatim): "I enjoy society... flaws and all. You
people venerate savagery... and you will die... savagely. All of you." (quote box form; the transcript is
garbled); "Some of us sooner than others. Good day, Mr. Morgan."; "I don't know if you're aware but this...
this is a civilized land now. We didn't kill all them savages..." (full line); "And as a consequence that lets
you take what you please... Who made you the messiah to these lost souls you've led so horribly astray?";
"You ain't much of anything more than a killer, Mr. van der Linde."; "I don't wanna kill all these folk,
Dutch... just you."; "You'll be dead, sure... but I'm gonna be just fine. We offered you a deal, Mr. Morgan...
you should have taken it."; "Pinkerton Detective Agency... seconded to the United States
Government."; "This is Agent Milton with the Pinkerton Detective Agency. On behalf of Cornwall Kerosene &
Tar..." (wiki quote list); "the late Andrew Milton"; "And to what do we owe the pleasure, Agent Moron?"; "I
think your new friend should leave now, Dutch"; "This place, ain't no such thing as civilized..."; "You came
for me? Risked life and limb..."; "In that case... It'd be my honor... to join you."; "You enjoy being a rich
man's toy do you?"; "Oh, we're all gonna die, Agent."; "Ah, Mr. Morgan, nice to see you again"; "that bastard
Milton comes back with an army"; "You're still a yapping dog, Mr. Milton..."; "What a fine young man... and in
such complex circumstances."; "disagreeable men"; "He was pretty shot up by the time I got to him... so really
it was more of a mercy killing. Slow... but merciful."; "Spare me the philosophy lesson... I've already heard
it... from Mac Callander."; "Get your damn hands off of me, boy."; "Agent Milton and his men... took her to Van
Horn... to be put on a boat and tried for murder."; "Seems old Micah was pretty close with Milton."; "Micah was
the rat, John. Milton told me."; "Rip Van Winkle."; "Mr. Matthews, I presume."; "Mr. Milton... I'd like to find
a poisonous snake for him." and "Milton said a lot. Come on. I won't be out here all night." (wiki quote box,
attributed).
Left to A or C (not quoted here): "You're losing your strength, Mr. Morgan." (last words); "Calm down, Mr.
Morgan."; "That's quite a cough."; the Molly/Micah revelation lines ("sweated her", "never talked a word",
"he's been a good boy ever since"; here only paraphrased in the Molly and Micah entries); "Horrible man."
(Abigail); "orphaned street kid..." and the 5,000 dollar bounty (arthur_A owns them); "Dutch, get out here!"; the Lakay threat "You fools weren't listening to me..." (wiki quote list, left to C);
"when I return I'll be with fifty men..." (paraphrased here in Skills); Arthur's low-honor memory of the
messiah line in "A Fork in the Road" (C trivia may say it, pointing to Personality for the line).

WIKI-ONLY (kept, attributed): the Lakay announcement (quote list, no transcript); Cornwall's "for
people who need it" retort (mission summary, no transcript); Agent Johns's lines; "Milton Andrews" in the files;
the first name in the ending credits; weapons and horse (infobox); the Cattleman used on Hosea instead of his
Schofield; Arthur telling him of his tuberculosis as one of the few characters he tells outright.

Excluded: the wiki's "sadistic, obsessive, sociopathic, irascible, self-righteous, ambitious", "hypocritical",
"explicitly racist", "morbid sense of humor", "his subordinate agents dislike him" (interpretation; the facts
behind them are given as facts); "Agent Miller" alias ({{Citation needed}} on the wiki); the etymology of
Andrew and Milton (the wiki ties it to his worldview: interpretation, and no game source); "his modern haircut
likely reflects his affinity for progress" (speculation); outfit catalogue beyond three sentences (SPEC);
"likely a developer oversight" for the Cattleman (speculation); the Steve Haines comparison (wiki analysis);
"likely learned the ropes from him" (wiki inference; only the newspaper's "mentorship" is used); Milton
"rose through the ranks" (unsourced); the wiki's "amnesty" for the Clemens Point offer (the transcript says
three days to run off, conditional on Dutch giving himself up); U.S. Marshals and Blackwater Police
Department affiliations (infobox only, no game line found; left to the facts grid in part D as wiki-only);
Bill, Javier, Charles, Uncle, Pearson, Strauss, Swanson, Karen, Mary-Beth, Kieran (present at Clemens Point
or Lakay, no Milton-specific exchange).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include Milton, and no character page from an official guide is known for him. What the game shows of him comes from a few face-to-face scenes, in which he does the talking for the agency. In his first meetings with the gang, he introduces himself by his title and his agency. He addresses the outlaws formally, as Mr. Morgan, Mr. Matthews or Mr. van der Linde. He speaks in the name of law and civilization, and describes the gang's way of life as savagery (see In his own words).",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang Van der Linde et ne comprennent pas Milton ; on ne lui connaît pas non plus de fiche dans un guide officiel. Ce que le jeu montre de lui tient en quelques face-à-face, où c'est lui qui parle au nom de l'agence. Lors de ses premières rencontres avec la bande, il se présente par son titre et son agence. Il s'adresse aux hors-la-loi avec une politesse formelle : monsieur Morgan, monsieur Matthews, monsieur van der Linde. Il parle au nom de la loi et de la civilisation, et voit dans le mode de vie de la bande une forme de sauvagerie (voir Dans ses propres mots).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "By the river in \"A Fisher of Men\", Arthur asks whether he enjoys being a rich man's toy. Milton answers: \"I enjoy society... flaws and all. You people venerate savagery... and you will die... savagely. All of you.\" When Arthur replies that everyone dies, he says: \"Some of us sooner than others. Good day, Mr. Morgan.\"",
        "Au bord de la rivière, dans \"A Fisher of Men\", Arthur lui demande s'il aime servir de jouet à un homme riche. Milton répond : \"I enjoy society... flaws and all. You people venerate savagery... and you will die... savagely. All of you.\" (j'aime la société, avec tous ses défauts ; vous autres, vous vénérez la sauvagerie, et vous mourrez comme des sauvages, tous autant que vous êtes). Quand Arthur réplique que tout le monde meurt, il lâche : \"Some of us sooner than others. Good day, Mr. Morgan.\" (certains plus tôt que d'autres ; bonne journée, monsieur Morgan).")},
    {"p": two(
        "At Clemens Point, in \"The Battle of Shady Belle\", he lays out his view to the whole gang: \"I don't know if you're aware but this... this is a civilized land now. We didn't kill all them savages only to allow the likes of you to act like human dignity and basic decency was outmoded or not yet invented. This thing, it's done.\" To Dutch he says: \"And as a consequence that lets you take what you please, kill whom you please and hang the rest of us? Who made you the messiah to these lost souls you've led so horribly astray?\" When Dutch calls himself a seeker, Milton answers: \"You ain't much of anything more than a killer, Mr. van der Linde.\" He adds: \"I don't wanna kill all these folk, Dutch... just you.\"",
        "À Clemens Point, dans \"The Battle of Shady Belle\", il expose sa vision devant toute la bande : \"I don't know if you're aware but this... this is a civilized land now. We didn't kill all them savages only to allow the likes of you to act like human dignity and basic decency was outmoded or not yet invented. This thing, it's done.\" (je ne sais pas si vous êtes au courant, mais c'est une terre civilisée, maintenant ; on n'a pas tué tous ces sauvages pour laisser des gens comme vous faire comme si la dignité humaine et la décence la plus élémentaire étaient passées de mode ou restaient à inventer ; tout ça, c'est fini). À Dutch, il lance : \"And as a consequence that lets you take what you please, kill whom you please and hang the rest of us? Who made you the messiah to these lost souls you've led so horribly astray?\" (et ça vous autorise à prendre ce qui vous plaît, à tuer qui vous plaît et à vous moquer du reste ? Qui a fait de vous le messie de ces âmes perdues que vous avez si terriblement égarées ?). Quand Dutch se dit simple chercheur, Milton rétorque : \"You ain't much of anything more than a killer, Mr. van der Linde.\" (vous n'êtes guère plus qu'un tueur, monsieur van der Linde). Il ajoute : \"I don't wanna kill all these folk, Dutch... just you.\" (je ne veux pas tuer tous ces gens, Dutch ; seulement vous).")},
    {"p": two(
        "At Van Horn, when Arthur tells him he has tuberculosis and will take him along, Milton replies: \"You'll be dead, sure... but I'm gonna be just fine. We offered you a deal, Mr. Morgan... you should have taken it.\"",
        "À Van Horn, quand Arthur lui annonce qu'il a la tuberculose et qu'il l'emmènera avec lui, Milton répond : \"You'll be dead, sure... but I'm gonna be just fine. We offered you a deal, Mr. Morgan... you should have taken it.\" (vous, vous serez mort, c'est sûr ; mais moi, je m'en sortirai très bien ; on vous a proposé un marché, monsieur Morgan, vous auriez dû l'accepter).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "He introduces himself as Agent Milton, and Arthur and Dutch call him Mr. Milton. His first name is never spoken. It appears in the 1907 newspaper article \"Bureau of Investigation Founded\" (see Biography, After his death). According to the Red Dead Wiki, it also appears in the ending credits. At Clemens Point, Dutch greets him with: \"And to what do we owe the pleasure, Agent Moron?\" Susan Grimshaw calls him Dutch's new friend: \"I think your new friend should leave now, Dutch.\" According to the Red Dead Wiki's page on cut content, the game files name him Milton Andrews.",
        "Il se présente comme l'agent Milton, et Arthur comme Dutch l'appellent monsieur Milton. Son prénom n'est jamais prononcé. On le trouve dans l'article de journal de 1907 \"Bureau of Investigation Founded\" (voir Biographie, Après sa mort). D'après le Red Dead Wiki, il figure aussi au générique de fin. À Clemens Point, Dutch l'accueille d'un \"And to what do we owe the pleasure, Agent Moron?\" (et à quoi devons-nous ce plaisir, agent Crétin ?). Susan Grimshaw le désigne comme le nouvel ami de Dutch : \"I think your new friend should leave now, Dutch.\" (je crois que ton nouvel ami devrait s'en aller, Dutch). Selon la page du Red Dead Wiki consacrée au contenu coupé, les fichiers du jeu le nomment Milton Andrews.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He has a thin build, a pitted, beardless face and dark hair cropped close on the sides and combed back. He wears the same kind of outfit as the other Pinkerton agents: a dark gray suit with his badge on the lapel, a red waistcoat and a black bowler hat.",
        "Il est de constitution maigre, imberbe, le visage marqué de cicatrices de petite vérole, les cheveux sombres coupés ras sur les côtés et peignés vers l'arrière. Il s'habille comme les autres agents de la Pinkerton : costume gris foncé avec l'insigne au revers, gilet rouge et chapeau melon noir.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Pinkerton agent", "Agent de la Pinkerton")},
    {"h4": two("Mandate and means", "Mandat et moyens")},
    {"p": two(
        "Milton works for the Pinkerton Detective Agency. At the river he describes his position to Arthur: \"Pinkerton Detective Agency... seconded to the United States Government.\" At Lakay he speaks in the name of three backers: Cornwall's company, the United States government and the Commonwealth of West Elizabeth (see Quotes). The hunt is paid for by Leviticus Cornwall (see Relationships).",
        "Milton travaille pour l'agence de détectives Pinkerton. Au bord de la rivière, il présente ainsi sa fonction à Arthur : \"Pinkerton Detective Agency... seconded to the United States Government.\" (agence de détectives Pinkerton, détachée auprès du gouvernement des États-Unis). À Lakay, il parle au nom de trois commanditaires : la compagnie de Cornwall, le gouvernement des États-Unis et le Commonwealth de West Elizabeth (voir Citations). C'est Leviticus Cornwall qui finance la traque (voir Relations).")},
    {"h4": two("Weapons and horse", "Armes et cheval")},
    {"p": two(
        "The Red Dead Wiki lists a Schofield Revolver as his usual sidearm, along with a Cattleman Revolver; according to the same wiki, the Cattleman is the gun he uses to kill Hosea. He rides an Andalusian, according to the English-language wiki.",
        "Le Red Dead Wiki lui attribue un Schofield Revolver comme arme habituelle, ainsi qu'un Cattleman Revolver ; selon le même wiki, c'est avec le Cattleman qu'il abat Hosea. Il monte un andalou, d'après le wiki anglophone.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": [
        two(
            "Dutch is the man Milton wants. At the river he tells Arthur: \"We want Van der Linde.\" Their one face-to-face conversation takes place at Clemens Point. Dutch answers his speech on civilization: \"This place, ain't no such thing as civilized. It's man so in love with greed, he has forgotten himself and found only appetites.\" He mocks the offer made to him: \"You came for me? Risked life and limb in this den of lowlifes and murderers so that they might live and love? Ain't that fine.\" Then he raises his hands as if to surrender: \"In that case... It'd be my honor... to join you.\" The gang takes up its weapons.",
            "Dutch est l'homme que Milton veut. Au bord de la rivière, il le dit à Arthur : \"We want Van der Linde.\" (c'est Van der Linde que nous voulons). Leur seule conversation en tête-à-tête a lieu à Clemens Point. Dutch répond à son discours sur la civilisation : \"This place, ain't no such thing as civilized. It's man so in love with greed, he has forgotten himself and found only appetites.\" (cet endroit n'a rien de civilisé ; c'est l'homme, si amoureux de sa cupidité qu'il s'est oublié lui-même et n'a plus trouvé que des appétits). Il se moque de l'offre qui le vise : \"You came for me? Risked life and limb in this den of lowlifes and murderers so that they might live and love? Ain't that fine.\" (vous êtes venu pour moi ? Vous avez risqué votre peau dans ce repaire de vauriens et d'assassins pour qu'ils puissent vivre et aimer ? Comme c'est beau). Puis il lève les mains comme pour se rendre : \"In that case... It'd be my honor... to join you.\" (dans ce cas, ce serait un honneur de vous suivre). La bande prend aussitôt les armes."),
        two(
            "At the bank in Saint Denis, Dutch pleads with him from inside the building for Hosea's life (see Biography). In \"Just a Social Call\", Dutch watches him from the Annesburg harbor as he comes off Cornwall's yacht, and kills Cornwall after the agents have left (see Biography).",
            "À la banque de Saint-Denis, Dutch le supplie depuis l'intérieur du bâtiment d'épargner Hosea (voir la biographie). Dans \"Just a Social Call\", Dutch l'observe depuis le port d'Annesburg descendre du yacht de Cornwall, et abat Cornwall une fois les agents partis (voir la biographie)."),
    ]},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "Milton knows Arthur from the agency's files before they meet at the river in \"A Fisher of Men\" (see Biography). Arthur tells him he is guilty of nothing except not playing by his rules, and asks: \"You enjoy being a rich man's toy do you?\" To Milton's threat he answers: \"Oh, we're all gonna die, Agent.\" At Clemens Point, Milton greets him as an acquaintance: \"Ah, Mr. Morgan, nice to see you again\". On the ride to Shady Belle, Arthur tells John that they must move everyone \"before that bastard Milton comes back with an army\".",
            "Milton connaît Arthur par les dossiers de l'agence avant leur rencontre au bord de la rivière, dans \"A Fisher of Men\" (voir la biographie). Arthur lui répond qu'il n'est coupable de rien, sinon de ne pas jouer selon ses règles, et lui demande : \"You enjoy being a rich man's toy do you?\" (ça vous plaît d'être le jouet d'un homme riche ?). À sa menace, il réplique : \"Oh, we're all gonna die, Agent.\" (oh, on va tous mourir, agent). À Clemens Point, Milton le salue comme une vieille connaissance : \"Ah, Mr. Morgan, nice to see you again\" (ah, monsieur Morgan, ravi de vous revoir). En route pour Shady Belle, Arthur explique à John qu'il faut mettre tout le monde à l'abri \"before that bastard Milton comes back with an army\" (avant que ce salaud de Milton revienne avec une armée)."),
        two(
            "At Van Horn, Arthur tells him plainly that he has tuberculosis; according to the Red Dead Wiki, Milton is one of the few characters Arthur tells outright. When Milton tells him he should have taken the deal, Arthur answers: \"I'm a fool, Mr. Milton.\" His last words to him are: \"You're still a yapping dog, Mr. Milton...\" Their final confrontation and Milton's death are told in the Biography.",
            "À Van Horn, Arthur lui avoue sans détour qu'il a la tuberculose ; selon le Red Dead Wiki, Milton fait partie des rares personnages à qui Arthur le dit ouvertement. Quand Milton lui reproche de ne pas avoir accepté le marché, Arthur répond : \"I'm a fool, Mr. Milton.\" (je suis un imbécile, monsieur Milton). Ses derniers mots à son adresse sont : \"You're still a yapping dog, Mr. Milton...\" (vous n'êtes toujours qu'un roquet qui aboie, monsieur Milton). Leur dernier affrontement et la mort de Milton sont racontés dans la biographie."),
    ]},
    {"img": "edgar-ross.jpeg", "slug": "edgar-ross", "name": "Edgar Ross", "text": two(
        "Ross is Milton's partner in 1899 and mostly leaves the talking to him. Ross is with him at the river and at Clemens Point, where Milton introduces him as Agent Ross, at the bank in Saint Denis according to the Red Dead Wiki, and in Annesburg, where the two come off Cornwall's yacht together. After Milton's death, Ross takes over the hunt (see Biography).",
        "Ross est le coéquipier de Milton en 1899 et lui laisse presque toujours la parole. Il l'accompagne au bord de la rivière et à Clemens Point, où Milton le présente comme l'agent Ross, devant la banque de Saint-Denis selon le Red Dead Wiki, et à Annesburg, où les deux hommes descendent ensemble du yacht de Cornwall. Après la mort de Milton, Ross reprend la traque (voir la biographie).")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "Milton recognizes Hosea at Clemens Point: \"Mr. Matthews, I presume.\" During the Saint Denis bank robbery he catches Hosea in the diversion and kills him in front of the bank (see Biography).",
        "À Clemens Point, Milton reconnaît Hosea : \"Mr. Matthews, I presume.\" (monsieur Matthews, je présume). Pendant le braquage de la banque de Saint-Denis, il capture Hosea au cours de la diversion et l'abat devant la banque (voir la biographie).")},
    {"img": "leviticus-cornwall.jpeg", "slug": "leviticus-cornwall", "name": "Leviticus Cornwall", "text": two(
        "Cornwall pays the Pinkertons who hunt the gang. The gang robbed his train in the Grizzlies, and Milton brings the robbery up at the river. In \"Just a Social Call\", Cornwall berates Milton and Ross in Annesburg for their lack of progress and threatens to stop funding them (see Biography).",
        "Cornwall finance les Pinkerton qui traquent la bande. Celle-ci a attaqué son train dans les Grizzlies, et Milton évoque ce braquage au bord de la rivière. Dans \"Just a Social Call\", Cornwall reproche à Milton et à Ross, à Annesburg, leur manque de résultats et menace de leur couper les vivres (voir la biographie).")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "Milton's men seize Abigail outside Beaver Hollow during \"Our Best Selves\". At Van Horn she kills him with Sadie's revolver (see Biography).",
        "Les hommes de Milton s'emparent d'Abigail devant Beaver Hollow pendant \"Our Best Selves\". À Van Horn, elle l'abat avec le revolver de Sadie (voir la biographie).")},
    {"img": "tilly-jackson.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
        "Tilly escapes Milton's men with Jack and brings the news to the gang at the start of \"Red Dead Redemption\": \"Agent Milton and his men... took her to Van Horn... to be put on a boat and tried for murder.\"",
        "Tilly échappe aux hommes de Milton avec Jack et apporte la nouvelle à la bande au début de \"Red Dead Redemption\" : \"Agent Milton and his men... took her to Van Horn... to be put on a boat and tried for murder.\" (l'agent Milton et ses hommes l'ont emmenée à Van Horn, pour la mettre sur un bateau et la faire juger pour meurtre).")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "Milton names Micah as the Pinkertons' informant at Van Horn (see Biography and Quotes). Back at Beaver Hollow, Arthur tells Dutch: \"Seems old Micah was pretty close with Milton.\" He tells John: \"Micah was the rat, John. Milton told me.\" Earlier, Micah had watched Milton come off Cornwall's yacht in Annesburg with Arthur and Dutch.",
        "À Van Horn, Milton désigne Micah comme l'informateur des Pinkerton (voir la biographie et les citations). De retour à Beaver Hollow, Arthur dit à Dutch : \"Seems old Micah was pretty close with Milton.\" (on dirait que ce bon vieux Micah était très proche de Milton). Il le dit aussi à John : \"Micah was the rat, John. Milton told me.\" (c'était Micah, le rat, John ; Milton me l'a dit). Auparavant, Micah avait vu Milton descendre du yacht de Cornwall à Annesburg, aux côtés d'Arthur et de Dutch.")},
    {"img": "molly-oshea.jpeg", "slug": "molly-oshea", "name": "Molly O'Shea", "text": two(
        "Molly had claimed in front of the gang that she told the Pinkertons about the Saint Denis bank job, and Susan Grimshaw shot her (see Molly O'Shea). What Milton later says about her questioning is told in the Biography.",
        "Molly avait affirmé devant la bande qu'elle avait parlé aux Pinkerton du braquage de la banque de Saint-Denis, et Susan Grimshaw l'avait abattue (voir Molly O'Shea). Ce que Milton dira ensuite de ses interrogatoires est raconté dans la biographie.")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "Jack is fishing with Arthur when Milton and Ross ride up to the river. Milton's first words are about him: \"What a fine young man... and in such complex circumstances.\" On the way back, Jack asks Arthur why he lied about where Dutch is, and Arthur calls the two agents \"disagreeable men\". Jack is with Tilly when Milton's men take his mother (see Biography).",
        "Jack pêche avec Arthur quand Milton et Ross arrivent au bord de la rivière. Les premiers mots de Milton sont pour lui : \"What a fine young man... and in such complex circumstances.\" (quel beau jeune homme, et dans des circonstances si compliquées). Sur le chemin du retour, Jack demande à Arthur pourquoi il a menti sur l'endroit où se trouve Dutch, et Arthur qualifie les deux agents de \"disagreeable men\" (hommes désagréables). Jack est avec Tilly quand les hommes de Milton enlèvent sa mère (voir la biographie).")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "At Clemens Point, Milton names Dutch and Hosea, then turns to John and asks who he is. John answers: \"Rip Van Winkle.\" John is in prison at Sisika when Milton attacks Lakay.",
        "À Clemens Point, Milton nomme Dutch et Hosea, puis se tourne vers John et lui demande qui il est. John répond : \"Rip Van Winkle.\" John est en prison à Sisika quand Milton attaque Lakay.")},
    {"img": "lenny-summers.jpeg", "slug": "lenny-summers", "name": "Lenny Summers", "text": two(
        "Lenny warns Dutch as Milton and Ross walk into Clemens Point (see Biography). As the agents leave, Lenny tells Milton \"Come on.\" and, according to the Red Dead Wiki, takes hold of him. Milton shoves him away: \"Get your damn hands off of me, boy.\"",
        "Lenny prévient Dutch quand Milton et Ross entrent dans le camp de Clemens Point (voir la biographie). Au départ des agents, Lenny lance à Milton \"Come on.\" (allez, on y va) et, d'après le Red Dead Wiki, l'empoigne. Milton le repousse : \"Get your damn hands off of me, boy.\" (bas les pattes, garçon).")},
    {"img": "sadie-adler.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
        "At Lakay she and Arthur take Milton's agents from the flank. At Van Horn Milton's men capture her, and Abigail kills Milton with Sadie's revolver (see Biography).",
        "À Lakay, Arthur et elle prennent les agents de Milton de flanc. À Van Horn, les hommes de Milton la capturent, et Abigail abat Milton avec le revolver de Sadie (voir la biographie).")},
    {"img": None, "slug": None, "name": "Mac Callander", "text": two(
        "Mac is a member of the Van der Linde gang who never returns after Blackwater. At the river, Milton brings him up to cut Arthur short: \"Spare me the philosophy lesson... I've already heard it... from Mac Callander.\" When Arthur repeats the name, Milton says: \"He was pretty shot up by the time I got to him... so really it was more of a mercy killing. Slow... but merciful.\" On the way back, Jack asks whether Mac is in jail, and Arthur says he hopes Mac is fine where he is.",
        "Mac est un membre du gang Van der Linde qui n'est jamais revenu de Blackwater. Au bord de la rivière, Milton parle de lui pour couper court au discours d'Arthur : \"Spare me the philosophy lesson... I've already heard it... from Mac Callander.\" (épargnez-moi la leçon de philosophie, je l'ai déjà entendue, de la bouche de Mac Callander). Quand Arthur répète son nom, Milton ajoute : \"He was pretty shot up by the time I got to him... so really it was more of a mercy killing. Slow... but merciful.\" (il était bien criblé de balles quand je suis arrivé ; alors au fond, c'était plutôt un geste de pitié ; lent, mais miséricordieux). Sur le chemin du retour, Jack demande si Mac est en prison, et Arthur répond qu'il espère que Mac va bien, là où il est.")},
    {"img": None, "slug": None, "name": "Agent Johns", "text": two(
        "Johns is one of the Pinkerton agents under Milton. According to the Red Dead Wiki, he searches the train cars in the Saint Denis rail yard after the bank robbery, grumbling: \"Milton said a lot. Come on. I won't be out here all night.\" The same wiki has him complaining, during a later search of Shady Belle in \"Dear Uncle Tacitus\", that Milton makes them go through the place again: \"Mr. Milton... I'd like to find a poisonous snake for him.\"",
        "Johns est l'un des agents de la Pinkerton placés sous les ordres de Milton. Selon le Red Dead Wiki, il fouille les wagons de la gare de triage de Saint-Denis après le braquage de la banque, en maugréant : \"Milton said a lot. Come on. I won't be out here all night.\" (Milton a dit plein de choses ; allez, je ne vais pas passer la nuit ici). Toujours d'après ce wiki, lors d'une nouvelle fouille de Shady Belle dans \"Dear Uncle Tacitus\", il se plaint que Milton leur fasse retourner les lieux une fois de plus : \"Mr. Milton... I'd like to find a poisonous snake for him.\" (M. Milton, je lui trouverais bien un serpent venimeux).")},
]
