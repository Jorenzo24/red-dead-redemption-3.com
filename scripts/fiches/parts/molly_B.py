"""Molly O'Shea, part B: Personality (official descriptions, traits, In her own words, Names, Appearance),
Camp life, Relationships (20 Oct 2026, medium tier).

Sources (register):
- Rockstar character description of 6 Sep 2018 (English text as reprinted by The Hollywood Reporter / Heat
  Vision, Sep 2018, saved in ../uncle/fc/thr_descriptions.txt, line 131; also in Rockstar's tweet of 6 Sep 2018).
  French text from rockstargames.com/reddeadredemption2/fr/features/vanderlindegang, as quoted by the French Red
  Dead Wiki page "Molly O'Shea" (molly/fr.txt): "Fille de Dublin dont Dutch s'est entiché, du moins pour
  l'instant. De nature angoissée, Molly peine à se faire à la vie de cavale."
- A character page from an official guide (wiki file MollyOSheaBio.jpg, captioned "Biography in RDR 2",
  uploaded 12 Nov 2018), downloaded through the wiki API on 20 Oct 2026 to molly/fcB/MollyBio.png and read; text
  copied verbatim in molly/fcB/guide_bio.txt. Wikipedia's "List of Red Dead Redemption 2 characters" cites the same
  facts to the official guide (Price 2018, p. 373); the edition is not named on the page, so the text says "an
  official guide".
- Red Dead Wiki EN "Molly O'Shea" (infobox, quote box, Personality, Appearance, Trivia) and FR "Molly O'Shea";
  "Molly's Poem" (document text, title gloss, villanelle form; molly/fcB/wiki_Molly_s_Poem.txt); "Camp Events"
  (../hosea/m/Camp_Events.txt: Horseshoe Overlook lines 34, 46, 47, 56, 106, 108; Sean's Return Party 176, 188;
  Clemens Point 227, 232, 236, 238, 240, 241, 248; Shady Belle 339, 340, 348; Jack's Return Party 369, 373; Lakay
  407; Beaver Hollow 416); Dutch van der Linde infobox ("Your Majesty", by Molly O'Shea, ../bill/fc2).
- Transcripts: "Outlaws from the West" (Susan: "Miss O'Shea will show you the way."); "Polite Society, Valentine
  Style" (Karen: "Miss O'Shea is far too high and mighty now"); "Who is Not Without Sin" (Molly: "I was wondering
  when he'd show up."); "The Battle of Shady Belle" (Molly asks Dutch for a word, "Not now").
- Fact-checked fiches reused as is: arthur_D (mirror, cigars, "Not Molly, Dutch"), dutch_B/D, susan_A/B, karen_A/B,
  tilly_B, mary_B, abigail_B, sean_B, kieran_A/B, micah_B, orville_A/B, simon_A/B, uncle_A/B, bill_B.

Ownership (FIX_RULES): official descriptions (Rockstar 6 Sep 2018 and the guide page) live HERE only; parts A
and C must not quote them (C may say that Rockstar published descriptions on 6 Sep 2018). Names, appearance,
camp life (no chores, no crimes, lodging in Dutch's tent) and ALL camp scenes live here, each in ONE relationship
entry. Molly's Poem (its text, title and form) is quoted HERE only ("In her own words"); A and C may mention that
the poem lies in Dutch's tent, without quoting it. Mission events (Colter arrival, An Honest Mistake opening, The
Battle of Shady Belle refusal, the Lakay absence, the Beaver Hollow claim and death, the burning of the body,
Milton's revelation, the "Not Molly" endings) live in part A; entries here refer to them in one clause.
Lines quoted here (parts A and C must NOT repeat them): the Rockstar and guide descriptions; the poem refrains;
"Dutch is all the company I need" (as quoted by the Red Dead Wiki); "Miss O'Shea" (Names); "Your Majesty" (Names).
"I'm nobody's servant girl" is paraphrased (the wiki gives two wordings, nobody's / no one's, and no transcript).
"I was wondering when he'd show up." now lives in part C Quotes only; the Swanson entry points to it.
Part C keeps the wiki quote-box line ("I won't be ignored, Dutch van der Linde...") and the An Honest Mistake
lines, which are not used here. Trivia (C) keeps the companion-icon fact, the horse-riding fact, the Constance
Skirt resemblance; it must not repeat the chores refusal, the poem, or the mirror scene.
Fact-check fixes (20 Oct 2026): mirror scene without Arthur's unsourced "seven years" reply, reward = one Cigar,
chapter 3 only (Missable Content table, Martha's Swain); Tilly's reaction = "got what she deserved" (Tilly wiki page),
the "fool in love" line moved to Mary-Beth (it is hers); Karen fight: Clemens Point per Camp Events, Shady Belle per
Molly's page, attributed; "two Irish members" removed; crime claim attributed to the Swanson wiki page; "no weapon, no
horse" removed (inferred from empty infobox fields); copied sentences reworded (Tilly chores, Sean, Dutch compare);
duplicates cut (Valentine wagon, Micah informer, Milton, Uncle, Swanson quote, Arthur money ending, Susan at Lakay,
dock and chores in Camp life; Pearson entry removed, pure repeat of the Biography). Added from the coverage report,
attributed: envy of the other women, "turned Dutch against her", hair, eye-shadow, Clemens Point drift from Dutch's
tent, the party exit, Karen vs Susan after the death, Karen's drinking, Abigail's "sweet but not stupid".

WIKI-ONLY (kept, attributed or paraphrased without quotation marks): all camp events material (no transcripts);
the two camp lines quoted with attribution; the "West Briton" insult (wiki, YouTube reference); Karen threatening
her "Dutch or no Dutch" (paraphrased); Abigail's advice wording; Molly's line after Kieran's death; Mary-Beth and
Tilly after the death; the outfit; Uncle saying he found her in Saint Denis; Susan's remarks at Lakay.
Excluded: the wiki's readings ("vanity and narcissism", "seemingly due to", "may also be superstitious",
"insinuating that she believes Dutch is only interested in sex", "possibly Arthur" as shaken, "first to notice
Dutch's mental decline", "foreshadow her death"); the accent versus wealthy background trivia and "she must have
some education" (interpretation; C may treat it attributed if it wishes); "stuck-up and entitled" as a verdict
(kept only as the scenes it rests on); eye color (the wiki says green, the guide portrait shows blue: left out);
the Karen fight's exact blows are given in both wiki versions; the FR wiki's "disappears for weeks at Shady Belle"
(contradicted by the camp events of that chapter); the outfit catalogue (reduced to two sentences).
"""

def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar Games' official description of Molly, published in September 2018, reads: \"A Dublin girl and the object of Dutch's affection, for now at least, Molly is too high-strung for a life on the run and it's all starting to take a toll on her.\"",
        "La description officielle de Molly publiée par Rockstar Games en septembre 2018 dit, dans sa version française : \"Fille de Dublin dont Dutch s'est entiché, du moins pour l'instant. De nature angoissée, Molly peine à se faire à la vie de cavale.\"")},
    {"p": two(
        "A character page from an official guide, reproduced on the Red Dead Wiki, opens with the same sentence and goes further. It says that \"She claims to be from a well-to-do Irish family who came over to America on a romantic whim in search of adventure and excitement.\" It adds that Molly found that excitement in Dutch van der Linde \"but wants more than he can, or is prepared to, give her.\" It ends: \"She considers herself a few cuts above the other gang members, which hasn't won her many supporters in camp.\"",
        "Une page de personnage tirée d'un guide officiel, reproduite sur le Red Dead Wiki, reprend cette phrase et va plus loin. Elle précise que Molly \"claims to be from a well-to-do Irish family\" (dit venir d'une famille irlandaise aisée), partie pour l'Amérique sur un coup de tête romantique, en quête d'aventure et de sensations. Elle les a trouvées auprès de Dutch van der Linde, mais elle attend de lui plus qu'il ne peut ou ne veut lui donner. Le guide conclut : \"She considers herself a few cuts above the other gang members, which hasn't won her many supporters in camp.\" (elle se croit bien au-dessus des autres membres de la bande, ce qui ne lui a pas valu beaucoup d'alliés au camp).")},
    {"p": two(
        "She is the only woman of the camp who does no chores. According to the Red Dead Wiki, the other women envy her that exemption. When Arthur suggests she help them clean the camp, she replies that she is nobody's servant girl. She spends much of her time in Dutch's tent, putting on make-up, looking at herself in a small mirror or writing. As the story goes on she keeps more and more to herself, and when Arthur tries to talk to her she tells him she wants to be left alone or that she is poor company. At Shady Belle she walks up and down the dock, muttering that she has been lied to and that the camp laughs at her, and she tells Arthur to go away if he comes near. According to the Red Dead Wiki's character page, she sometimes shouts at him that he and the others turned Dutch against her.",
        "C'est la seule femme du camp à ne faire aucune corvée. D'après le Red Dead Wiki, les autres femmes lui envient ce privilège. Quand Arthur lui suggère de les aider à nettoyer le camp, elle rétorque qu'elle n'est la servante de personne. Elle passe une bonne partie de son temps sous la tente de Dutch, à se maquiller, à se regarder dans un petit miroir ou à écrire. Au fil de l'histoire, elle s'isole de plus en plus, et quand Arthur cherche à lui parler, elle lui répond qu'elle veut être tranquille ou qu'elle n'est pas de bonne compagnie. À Shady Belle, elle arpente le ponton en marmonnant qu'on lui a menti et que tout le camp se moque d'elle, et elle chasse Arthur s'il approche. D'après la page du personnage sur le Red Dead Wiki, il lui arrive de lui crier que lui et les autres ont monté Dutch contre elle.")},
    {"h4": two("In her own words", "Dans ses propres mots")},
    {"p": two(
        "At Colter, when Arthur asks whether she would like to stay with the others for company, she refuses; the Red Dead Wiki gives her answer as \"Dutch is all the company I need.\" In Dutch's tent the player can read a poem in her hand, titled \"Uaibhreach\", Irish for proud or haughty. It is written as a villanelle, a fixed form of nineteen lines built on two refrains: \"I was a girl until your call\" and \"I've nothing left. I gave you all.\" The poem recalls the Liffey, the river of Dublin, and speaks of Dutch's \"parasites and lackeys\" mocking a love they dare not see. Its last stanza has her sitting alone, writing and waiting for him.",
        "À Colter, quand Arthur lui demande si elle ne veut pas rester avec les autres pour avoir de la compagnie, elle refuse ; le Red Dead Wiki rapporte sa réponse : \"Dutch is all the company I need.\" (Dutch est la seule compagnie dont j'ai besoin). Dans la tente de Dutch, le joueur peut lire un poème de sa main, intitulé \"Uaibhreach\", un adjectif irlandais qui veut dire fière, hautaine. C'est une villanelle, une forme fixe de dix-neuf vers construite sur deux refrains : \"I was a girl until your call\" (j'étais une jeune fille, jusqu'à ton appel) et \"I've nothing left. I gave you all.\" (il ne me reste rien, je t'ai tout donné). Le poème évoque la Liffey, le fleuve de Dublin, et les \"parasites and lackeys\" (parasites et laquais) de Dutch, qui raillent un amour qu'ils n'osent pas voir. Dans la dernière strophe, elle est seule, à écrire en l'attendant.")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Susan Grimshaw and Karen Jones call her \"Miss O'Shea\". According to the Red Dead Wiki, she calls Dutch \"Your Majesty\".",
        "Susan Grimshaw et Karen Jones l'appellent \"Miss O'Shea\". D'après le Red Dead Wiki, elle appelle Dutch \"Your Majesty\" (Votre Majesté).")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "The guide's portrait shows a young woman with long, curly red hair, freckles and red lipstick, in a pale high-collared blouse, a fringed shawl with a red floral print and a dark skirt. In camp she wears more make-up than the other women, with eye-shadow and red lipstick. According to the Red Dead Wiki, her hair is half tied up, with the rest of her red curls falling down her back, and her usual outfit is a low-cut green corseted top with gold trim, a red skirt and white boots.",
        "Le portrait du guide montre une jeune femme aux longs cheveux roux bouclés, aux taches de rousseur et au rouge à lèvres vif, vêtue d'un chemisier clair à col montant, d'un châle à franges imprimé de fleurs rouges et d'une jupe sombre. Au camp, elle se maquille plus que les autres femmes : fard à paupières et rouge à lèvres. D'après le Red Dead Wiki, ses cheveux sont à moitié relevés, le reste de ses boucles rousses tombant dans son dos, et sa tenue habituelle se compose d'un corsage vert décolleté à liseré doré, d'une jupe rouge et de bottines blanches.")},
]

# ---------------------------------------------------------------- SKILLS (camp life)
BLOCKS_SKILLS = [
    {"h3": two("Camp life", "La vie au camp")},
    {"p": two(
        "At Colter Molly lodges with Dutch in his cabin, and at Horseshoe Overlook and Clemens Point she lives in his tent. According to the Red Dead Wiki's page on Reverend Swanson, she, Swanson and Simon Pearson are the only gang members never shown committing, planning or taking part in a crime.",
        "À Colter, Molly loge avec Dutch dans sa cabane ; à Horseshoe Overlook et à Clemens Point, elle vit sous sa tente. D'après la page du Red Dead Wiki consacrée au révérend Swanson, elle est, avec lui et Simon Pearson, l'un des seuls membres de la bande qu'on ne voit jamais commettre, préparer ou faciliter un crime.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": [
        two(
            "Molly is Dutch's companion when the story begins. At Horseshoe Overlook he flirts with her in his tent; if Arthur makes fun of them, Dutch defends his feelings and suggests he join Bill, Javier and Charles at Smithfield's Saloon in Valentine. Another day Dutch asks Molly what he should compare her to. If Arthur is nearby, Dutch puts the question to him. Arthur replies that she is an idiot if she believes Dutch, and tells her to compare Dutch to that. Dutch tells Molly that Arthur has no poetry in him. At the party for Sean's return the two dance to Dutch's gramophone. Molly also asks him to go for a walk, and he hesitates.",
            "Au début de l'histoire, Molly est la compagne de Dutch. À Horseshoe Overlook, il la courtise sous sa tente ; si Arthur se moque d'eux, Dutch défend ses sentiments et l'envoie rejoindre Bill, Javier et Charles au Smithfield's Saloon de Valentine. Un autre jour, Dutch demande à Molly à quoi il pourrait la comparer. Si Arthur est dans les parages, Dutch lui pose la question. Arthur répond qu'elle est idiote si elle croit Dutch, et lui conseille de comparer Dutch à ça. Dutch soupire devant Molly qu'Arthur n'a pas une once de poésie. À la fête du retour de Sean, ils dansent tous deux au son du gramophone de Dutch. Molly lui propose aussi une promenade, et il se fait prier."),
        two(
            "At Clemens Point the tone changes: from the moment \"An Honest Mistake\" becomes available, her camp scenes with Dutch show neglect instead of affection, and according to the Red Dead Wiki she spends more and more time away from his tent. The camp hears them argue there. She accuses him of looking at another woman, and he calls her delusional. She reproaches him for not showing her any affection in weeks. Another time she asks why he has been so cold, and he says nothing is wrong and he is trying to rest. He calls her needy and selfish, while she says she only wants to help and that he will not talk to her. She also accuses him of flirting with Mary-Beth and says she fears she is getting too old for him. At Shady Belle he refuses her a word (see Biography). At the party for Jack's return she rants at him, drunk, that he has ruined her life. Dutch answers that he sees things differently, and she walks off, telling him to leave her alone. Arthur can then remark to Dutch on her bitter mood.",
            "À Clemens Point, le ton change : dès que \"An Honest Mistake\" est disponible, ses scènes de camp avec Dutch ne montrent plus de tendresse mais de l'indifférence, et d'après le Red Dead Wiki elle passe de moins en moins de temps sous sa tente. Le camp les y entend se disputer. Elle l'accuse de regarder une autre femme, et il la traite d'affabulatrice. Elle lui reproche de ne lui avoir témoigné aucune tendresse depuis des semaines. Une autre fois, elle lui demande pourquoi il est si froid avec elle, et il assure que tout va bien et qu'il essaie simplement de se reposer. Il la trouve envahissante et égoïste, quand elle dit seulement vouloir l'aider et se heurter à son silence. Elle l'accuse aussi de faire du charme à Mary-Beth et dit craindre d'être devenue trop vieille pour lui. À Shady Belle, il refuse de l'écouter (voir la biographie). À la fête du retour de Jack, ivre, elle lui lance qu'il a gâché sa vie. Dutch répond qu'il voit les choses autrement, et elle s'en va en lui disant de la laisser tranquille. Arthur peut ensuite glisser à Dutch un mot sur son amertume."),
    ]},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "Molly and Arthur speak little. When her pocket mirror breaks, she asks him whether her grandmother was right that it brings seven years of bad luck, and asks him for a new one. He can find one in a cabin at Martha's Swain; this request is available in chapter 3 only, and in return she gives him a cigar. At the party for Jack's return he can ask her to join in, and she says she is not in the mood.",
            "Molly et Arthur se parlent peu. Quand son miroir de poche se brise, elle lui demande si sa grand-mère avait raison de dire que cela porte malheur pendant sept ans, puis le prie de lui en trouver un autre. Il peut en dénicher un dans une cabane de Martha's Swain ; cette requête n'est proposée qu'au chapitre 3, et Molly le remercie d'un cigare. À la fête du retour de Jack, il peut l'inviter à se joindre à la fête, et elle répond qu'elle n'a pas le cœur à ça."),
        two(
            "She tries to talk to him about Dutch at the start of \"An Honest Mistake\", and at Beaver Hollow he tries to stop Dutch from shooting her (see Biography).",
            "Elle tente de lui parler de Dutch au début de \"An Honest Mistake\", et à Beaver Hollow il essaie d'empêcher Dutch de l'abattre (voir la biographie)."),
    ]},
    {"img": "karen-jones.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": [
        two(
            "Karen is the woman Molly clashes with most. She mocks Molly's airs on the road to Valentine (see Biography). At Horseshoe Overlook Molly takes her to task over a remark Karen made earlier: she shouts that Karen is not as clever as she thinks and that Dutch loves her, Molly, very much. Karen stays noncommittal, Molly swears, and she leaves complaining about how unkind the other girls are.",
            "Karen est la femme avec qui Molly se heurte le plus. Elle raille les grands airs de Molly sur la route de Valentine (voir la biographie). À Horseshoe Overlook, Molly lui demande des comptes sur une remarque qu'elle a faite : elle lui crie qu'elle n'est pas aussi maligne qu'elle le croit et que Dutch l'aime, elle, profondément. Karen se garde de répondre franchement, Molly jure, puis s'en va en pestant contre la méchanceté des autres filles."),
        two(
            "At Clemens Point Molly demands to know what Karen has against her, and the quarrel turns physical. The Red Dead Wiki gives two versions of the blows. Its camp events page has Molly slap Karen and Karen punch her in the face. Karen's page has Karen slap Molly when Molly grabs her arm. Molly's own page places the fight at Shady Belle and adds that Karen threatens to kill her, Dutch or no Dutch, if she raises a hand again.",
            "À Clemens Point, Molly exige de savoir ce que Karen a contre elle, et la dispute en vient aux mains. Le Red Dead Wiki donne deux versions des coups. Sa page des événements de camp fait gifler Karen par Molly, puis Karen répliquer d'un coup de poing au visage. La page de Karen inverse : c'est Karen qui gifle Molly quand celle-ci lui saisit le bras. La page de Molly situe la bagarre à Shady Belle et ajoute que Karen menace de la tuer, Dutch ou pas, si elle lève encore la main sur elle."),
        two(
            "At Shady Belle Karen joins her on the dock. Molly tells her to stop laughing at her, and Karen replies that no one is. Molly then admits she has always believed herself better than everyone, and says the whole camp now either laughs at her or pities her, before walking off. When Arthur says Molly is losing it, Karen answers that she lost it months ago. Right after Molly's death, Karen turns on Susan. Susan says Molly broke the rules; Karen rejects that and calls her a murderer. According to the Red Dead Wiki, Karen's drinking gets worse after the death.",
            "À Shady Belle, Karen la rejoint sur le ponton. Molly lui ordonne d'arrêter de se moquer d'elle ; Karen répond que personne ne se moque d'elle. Molly reconnaît alors s'être toujours crue au-dessus de tout le monde, et dit que tout le camp, désormais, rit d'elle ou la prend en pitié, puis elle s'éloigne. Quand Arthur dit que Molly perd la tête, Karen répond qu'elle l'a perdue il y a des mois. Juste après la mort de Molly, Karen s'en prend à Susan. Susan invoque les règles que Molly a enfreintes ; Karen le conteste et la traite de meurtrière. D'après le Red Dead Wiki, Karen boit encore davantage après cette mort."),
    ]},
    {"img": "susan-grimshaw.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
        "Susan runs the camp's work, which Molly refuses to share. At Clemens Point Susan warns Dutch that Molly is unhappy and that her temper could cause trouble; Dutch brushes the warning aside with a joke about arguing with young women. At Beaver Hollow Susan shoots her (see Biography).",
        "Susan dirige les tâches du camp, que Molly refuse de partager. À Clemens Point, Susan prévient Dutch que Molly est malheureuse et que son caractère pourrait causer des ennuis ; Dutch balaie l'avertissement d'une boutade sur l'inutilité de discuter avec les jeunes femmes. À Beaver Hollow, c'est Susan qui l'abat (voir la biographie).")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "At Clemens Point Molly comes to Abigail to complain about Dutch. Abigail says she understands how Molly feels, then tells her plainly that Dutch does not love her the way she wants to be loved, and that she does not want to see her make a fool of herself. According to the Red Dead Wiki, she calls Molly sweet but not stupid and tells her to take care of herself. Molly denies it and leaves upset. Arthur then remarks to Abigail that Molly is losing her grip.",
        "À Clemens Point, Molly vient se plaindre de Dutch auprès d'Abigail. Abigail dit comprendre ce qu'elle ressent, puis lui explique sans détour que Dutch ne l'aime pas comme elle voudrait être aimée, et qu'elle ne veut pas la voir se ridiculiser. D'après le Red Dead Wiki, elle la trouve gentille mais pas sotte et l'invite à prendre soin d'elle. Molly le conteste et s'en va, bouleversée. Arthur fait ensuite remarquer à Abigail que Molly perd pied.")},
    {"img": "tilly-jackson.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
        "At Horseshoe Overlook Molly stops by while Tilly is working. When Tilly asks for help, Molly excuses herself on the grounds that she is in love, and Tilly tells her to pitch in or move along. If Arthur comes too close, Molly tells him the conversation is private. After Molly's death, according to the Red Dead Wiki, Tilly shows little sympathy and believes Molly got what she deserved.",
        "À Horseshoe Overlook, Molly passe voir Tilly pendant qu'elle travaille. Quand Tilly lui demande un coup de main, Molly se dérobe en expliquant qu'elle est amoureuse, et Tilly lui dit de s'y mettre ou de passer son chemin. Si Arthur s'approche trop, Molly lui fait savoir que la conversation est privée. Après la mort de Molly, d'après le Red Dead Wiki, Tilly se montre peu compatissante et estime que Molly n'a eu que ce qu'elle méritait.")},
    {"img": "mary-beth-gaskill.jpeg", "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill", "text": two(
        "At the party for Sean's return, while Uncle, Karen and Sean sing at the poker table, Dutch and Mary-Beth try to persuade Molly to join in. At Clemens Point Molly accuses Dutch of flirting with Mary-Beth (see Dutch van der Linde). After Molly's death, Mary-Beth tells Tilly she cannot get over it; according to the Red Dead Wiki, she adds that Molly was simply a fool in love who would say anything. The wiki names Mary-Beth and Karen as the members most shaken by the death.",
        "À la fête du retour de Sean, pendant qu'Uncle, Karen et Sean chantent à la table de poker, Dutch et Mary-Beth essaient de convaincre Molly de se joindre à eux. À Clemens Point, Molly accuse Dutch de faire du charme à Mary-Beth (voir Dutch van der Linde). Après la mort de Molly, Mary-Beth confie à Tilly qu'elle ne s'en remet pas ; d'après le Red Dead Wiki, elle ajoute que Molly n'était qu'une amoureuse aveugle, prête à dire n'importe quoi. Le wiki cite Mary-Beth et Karen comme les membres les plus ébranlés par cette mort.")},
    {"img": "sean-macguire.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
        "Sean, like Molly, is Irish. At Horseshoe Overlook he sits by her and says they are both far from home; she agrees. He asks what she thinks of him. She claims to have no real opinion, and he leaves laughing, saying her stuck-up looks tell him otherwise. According to the Red Dead Wiki, he once calls her a West Briton, a term for an Irish person seen as too fond of England. After his death and Kieran's, she speaks to Arthur about both (see Kieran Duffy).",
        "Sean est irlandais, comme Molly. À Horseshoe Overlook, il s'assoit près d'elle et lui fait remarquer qu'ils sont tous deux loin de chez eux ; elle en convient. Il lui demande ce qu'elle pense de lui. Elle prétend ne pas avoir d'avis, et il s'éloigne en riant, assurant que ses airs pincés disent le contraire. D'après le Red Dead Wiki, il la traite un jour de \"West Briton\", terme qui désigne un Irlandais jugé trop anglophile. Après sa mort et celle de Kieran, elle parle des deux à Arthur (voir Kieran Duffy).")},
    {"img": "kieran-duffy.jpeg", "slug": "kieran-duffy", "name": "Kieran Duffy", "text": two(
        "After Kieran's death in \"Horsemen, Apocalypses\", Molly talks to Arthur about it, about Sean's death and about the fact that Dutch is not speaking to her. According to the Red Dead Wiki, she is visibly distraught and asks him how any of this can be all right.",
        "Après la mort de Kieran, dans \"Horsemen, Apocalypses\", Molly en parle à Arthur, ainsi que de la mort de Sean et du silence de Dutch à son égard. D'après le Red Dead Wiki, elle est visiblement bouleversée et lui demande comment tout cela pourrait aller bien.")},
    {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
        "Uncle interrupts her talk with Arthur in \"An Honest Mistake\" and brings her back drunk to Beaver Hollow (see Biography).",
        "Uncle interrompt sa conversation avec Arthur dans \"An Honest Mistake\" et la ramène ivre à Beaver Hollow (voir la biographie).")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "Micah names Molly, with Reverend Swanson, among the members who contribute nothing and should be cut loose. He is the real informer (see Biography).",
        "Micah range Molly, avec le révérend Swanson, parmi les membres qui n'apportent rien et dont il faudrait se débarrasser. C'est lui le véritable informateur (voir la biographie).")},
    {"img": "andrew-milton.jpeg", "slug": "andrew-milton", "name": "Andrew Milton", "text": two(
        "Milton clears her at Van Horn (see Biography). According to the Red Dead Wiki, she left the Pinkertons with more questions than answers.",
        "Milton la disculpe à Van Horn (voir la biographie). D'après le Red Dead Wiki, elle a laissé les Pinkerton avec plus de questions que de réponses.")},
    {"img": "orville-swanson.jpeg", "slug": "orville-swanson", "name": "Orville Swanson", "text": two(
        "She remarks on his drunken return in \"Who is Not Without Sin\" (see Biography). Micah lumps the two of them together among the members he wants cut loose (see Micah Bell).",
        "Elle commente son retour en état d'ivresse dans \"Who is Not Without Sin\" (voir la biographie). Micah les met tous deux dans le même sac, parmi les membres dont il veut se débarrasser (voir Micah Bell).")},
]
