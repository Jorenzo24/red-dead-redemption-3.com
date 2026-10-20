"""Mary-Beth Gaskill, part B: Personality (official descriptions, traits, In her own words, Names, Appearance),
Skills, Relationships (20 Oct 2026, medium tier).

Sources (register):
- Rockstar character description of 6 Sep 2018 (English text as reprinted by The Hollywood Reporter / Heat
  Vision, Sep 2018, saved in ../uncle/fc/thr_descriptions.txt, line 113; French text from
  rockstargames.com/reddeadredemption2/fr/features/vanderlindegang, as quoted by the French Red Dead Wiki page
  "Mary-Beth Gaskill", mary/fr.txt).
- A character page from an official guide (wiki file MaryBethBio.jpg, captioned "Biography in RDR 2", uploaded
  12 Nov 2018, used on the page "Mary-Beth Gaskill"; downloaded through the wiki API on 20 Oct 2026 to
  mary/fcB/mb.raw and read; text transcribed in mary/fcB/guide_bio.txt). Wikipedia's "List of Red Dead
  Redemption 2 characters" cites the same facts to the official guide (Price 2018, p. 382); the edition is not
  named on the page, so the text says "an official guide".
- Red Dead Wiki EN "Mary-Beth Gaskill" (infobox, quote box, Personality, Appearance, Trivia) and FR page; wiki
  pages "Mary-Beth's Notebook" (in-game text, read 20 Oct 2026: "The American Wilderness, A Romance by Mary
  Elizabeth Nom De Plume", "A Frenchwoman on the Run, By Lizzie Nom De Plume", "A French Woman in Saint Denis, By
  Marie la Crosette"), "The Lady of the Manor" (in-game description, author Leslie Dupont), "Fountain Pen", "Errand
  Boy" (item request, Osman Grove, chapter 2), "Arthur Morgan/Relationships" (Mary-Beth section: ring in return
  for the pen, writing talk, illness talk, asks about Mary), "Camp Events" (Colter cabin; Kieran's water;
  Susan's lines and slap; Tilly and the romance; Arthur and "how lost" he is; the Moon; Valentine curse; "our
  lot"; Sean's party dance and the song with Molly; Clemens Point: Dutch and the book, Trelawny's crow, Molly's
  accusation, voting; Malcolm Foreman story; Shady Belle: Kieran's absence, Saint Denis talks, the necklace,
  Kieran's mourning; Jack's party).
- Transcripts: "Polite Society, Valentine Style" ("It means you've got a heart. A small one perhaps, hidden deep
  inside, but a real one."; "I don't believe you're quite that cold, Mr. Morgan."; "Very inspiring, Arthur.");
  "Outlaws from the West" ("Miss Gaskill", Susan); "Eastward Bound" (Susan: "Put that book away and go help.").
  Mission-page quote list of "Red Dead Redemption (mission)" (last-ride recollections, high honor): "Maybe it's a
  sign, Arthur... try... try to do the good thing." (Mary-Beth, Beaver Hollow conversation); "Our time... has
  pretty much passed." (Arthur to Mary-Beth, Horseshoe Overlook). Letter from Tilly ("my darling Mary Beth").
- Fact-checked fiches reused as is: kieran_B, karen_B, tilly_B, susan_B, sadie_B, abigail_B, hosea_B, jack_B,
  lenny_B, micah_B, uncle_B, arthur_D, charles_B, dutch_B/C, abigail_C (dominoes).

Ownership (FIX_RULES): official descriptions (Rockstar 6 Sep 2018 and the guide page) live HERE only; part A
Origins and part C must not quote them. Names and pen names (incl. the notebook signatures) live HERE only.
Appearance (guide portrait, 1907 credits look) and skills (pickpocketing, reading and writing, notebook, dominoes,
fountain pen request and ring) live HERE. ALL camp scenes live HERE, each in ONE relationship entry:
Colter comfort -> Sadie; water, flirt, reading, mourning -> Kieran; reading defensiveness, Moon, Malcolm Foreman
story, Molly's death -> Tilly; Valentine curse, "our lot", voting, Saint Denis, necklace, Jack's party vomiting ->
Karen; idleness, slap, "Put that book away", Kieran's whereabouts -> Susan; mocking the cooking -> Lenny; shark
story -> Pearson; book and charm, Molly's jealousy, Sean's party song -> Dutch / Molly; crow trick -> Trelawny;
dance invitation -> Micah; "lost" line, mother from New Hanover, writing talk, illness talk, dance at Sean's
party, question about Mary -> Arthur. Narrative mission events (Valentine trip, the train tip, the coach robbery,
Colm's torture aftermath, Kieran's body, Visiting Hours, Dutch's announcement in "Our Best Selves", the 1907
station encounter, Tilly's letter as a whole) live in part A; relationship entries refer to them in one clause.
Arthur's guess of her age ("21 or 22", wiki trivia) lives in part D's facts grid only.

Lines quoted in this part (parts A and C must NOT repeat them; A paraphrases): the Rockstar and guide
descriptions; "Maybe it's a sign, Arthur... try... try to do the good thing."; "It means you've got a heart. A
small one perhaps, hidden deep inside, but a real one."; "I don't believe you're quite that cold, Mr. Morgan.";
"Miss Gaskill"; the notebook signatures and the phrase "total tripe". Part C
may still quote "Well, she was a fool then, Arthur." (No, No and Thrice, No), "Very inspiring, Arthur." and the
other Valentine lines (tip, Tilly and the Foreman man).

WIKI-ONLY (kept, attributed or paraphrased without quotation marks): the camp events material (no transcripts),
the ring given in return for the pen, the mother from New Hanover, the writing talk with Arthur, the request to
avenge Kieran, the wiki's "soft spot" for Jack, the French wiki's dance invitation from Micah, the mockery of
Pearson's cooking, the 1907 credits look.

Excluded: the wiki's readings "presents herself as kind... while this is certainly true", "genuinely loving and
considers most of them family", "considered the kindest and most gentle member" (judgments, replaced by scenes);
"it is generally believed that Mary-Beth had a crush on Arthur" (the wiki itself calls it unconfirmed); "possibly
threatening figures" (wiki gloss); "Dutch semble être légèrement attiré" (FR wiki reading; the scenes are told);
the claim that her 1907 dress "alludes to her success" and lifted her "into high-society" (interpretation); the
outfit catalogue (reduced to the guide portrait and the 1907 look); the Diane Lane outfit inspiration and the
Leslie A. Dupont nod (wiki says "may have been" and "possibly": speculation); the FR wiki's "blue eyes" and "two
braids" (contradicted by the guide portrait and the EN wiki); Arthur's "Our time... has pretty much passed" as
a quote here (Arthur's line, paraphrased); the wiki trivia quote about "how lost he is" (no transcript:
paraphrased); the mirror scene with Susan (known from Kaili Vernoff's interview: part D); the dominoes with
Tilly (the wiki names Tilly as a dominoes player, not Mary-Beth's partner).
"""

def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar Games introduced Mary-Beth on September 6, 2018 with a two-sentence description: \"A kind, good-natured young woman, which makes her the perfect criminal. By the time people realize they've been duped, Mary-Beth is already on her way home with the money.\"",
        "Rockstar Games présente Mary-Beth le 6 septembre 2018 en deux phrases. La version française publiée par Rockstar dit : \"Sa gentillesse et sa bonne humeur font d'elle la criminelle parfaite : Mary-Beth se retrouve toujours déjà loin lorsque ses victimes réalisent qu'elles ont été dupées.\"")},
    {"p": two(
        "A character page from an official guide, reproduced on the Red Dead Wiki, opens with nearly the same two sentences. It adds that she \"soon became known as the best pickpocket around\" after running away from an orphanage (see Biography). It describes her as \"Smarter and more perspicacious than she often lets on\", and ends: \"Mary-Beth likes to read and write and has dreams of becoming a novelist one day.\"",
        "Une page de personnage tirée d'un guide officiel, reproduite sur le Red Dead Wiki, s'ouvre sur ces deux phrases, à quelques mots près. Elle ajoute qu'après sa fuite de l'orphelinat (voir la biographie), elle s'est vite fait une réputation de meilleure pickpocket des environs. Le guide la décrit comme \"Smarter and more perspicacious than she often lets on\" (plus fine et plus perspicace qu'elle ne le laisse paraître), et conclut qu'elle aime lire et écrire, et rêve de devenir un jour romancière.")},
    {"p": two(
        "In camp she is most often seen reading a romance novel, and she is shy about it (see Relationships).",
        "Au camp, on la voit le plus souvent plongée dans un roman sentimental, et elle n'aime pas trop qu'on le remarque (voir Relations).")},
    {"h4": two("In her own words", "Dans ses propres mots")},
    {"p": two(
        "On the road to Valentine in \"Polite Society, Valentine Style\", if Arthur helps a stranded driver catch his horse and Uncle mocks him for it, she answers: \"It means you've got a heart. A small one perhaps, hidden deep inside, but a real one.\" If he refuses to help and boasts of being cold, she replies: \"I don't believe you're quite that cold, Mr. Morgan.\" At Beaver Hollow, when Arthur tells her he is ill, she says: \"Maybe it's a sign, Arthur... try... try to do the good thing.\" The Red Dead Wiki opens its page on her with this line.",
        "Sur la route de Valentine, dans \"Polite Society, Valentine Style\", si Arthur aide un cocher à rattraper son cheval et qu'Uncle s'en moque, elle répond : \"It means you've got a heart. A small one perhaps, hidden deep inside, but a real one.\" (ça veut dire que tu as un cœur ; un petit, peut-être, caché tout au fond, mais un vrai). S'il refuse d'aider et se vante d'être sans cœur, elle réplique : \"I don't believe you're quite that cold, Mr. Morgan.\" (je ne vous crois pas si froid que ça, monsieur Morgan). À Beaver Hollow, quand Arthur lui apprend qu'il est malade, elle lui dit : \"Maybe it's a sign, Arthur... try... try to do the good thing.\" (c'est peut-être un signe, Arthur... essaie... essaie de faire le bien). Le Red Dead Wiki ouvre sa page sur cette réplique.")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Her name is Mary-Beth Gaskill. Susan Grimshaw calls her \"Miss Gaskill\" when she hands out the jobs in \"Outlaws from the West\", and Tilly's 1907 letter writes her name \"Mary Beth\", without the hyphen. In the notebook kept at camp she signs her stories with invented names: \"Mary Elizabeth Nom De Plume\" for \"The American Wilderness\", \"Lizzie Nom De Plume\" for \"A Frenchwoman on the Run\" and \"Marie la Crosette\" for \"A French Woman in Saint Denis\". Nom de plume is the French term for a pen name. By 1907 she publishes under the pen name Leslie Dupont, the author named on \"The Lady of the Manor\" (see Biography).",
        "Elle s'appelle Mary-Beth Gaskill. Susan Grimshaw l'appelle \"Miss Gaskill\" en distribuant les tâches dans \"Outlaws from the West\", et la lettre de Tilly, en 1907, écrit son prénom \"Mary Beth\", sans trait d'union. Dans le carnet qu'elle tient au camp, elle signe ses histoires de noms inventés : \"Mary Elizabeth Nom De Plume\" pour \"The American Wilderness\", \"Lizzie Nom De Plume\" pour \"A Frenchwoman on the Run\" et \"Marie la Crosette\" pour \"A French Woman in Saint Denis\". En 1907, elle publie sous le pseudonyme de Leslie Dupont, nom d'auteur qui figure sur \"The Lady of the Manor\" (voir la biographie).")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "The guide's portrait shows a young woman with brown hair in ringlets, green eyes and freckles. In the 1907 credits, according to the Red Dead Wiki, she wears her hair in a topknot, with pearl earrings and a dark green floral dress.",
        "Le portrait du guide montre une jeune femme aux cheveux bruns en anglaises, aux yeux verts et au visage semé de taches de rousseur. Dans le générique de 1907, selon le Red Dead Wiki, elle porte un chignon haut, des boucles d'oreilles en perles et une robe à fleurs vert foncé.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("Talents and camp life", "Talents et vie au camp")},
    {"h4": two("Pickpocketing and cons", "Vol à la tire et arnaques")},
    {"p": two(
        "Mary-Beth is a pickpocket and a con artist rather than a gunwoman: the Red Dead Wiki lists no weapon for her, and she never fires a weapon in the story. Her two cons in the story, the servant-girl ruse in Valentine and the act of a woman who has lost her memory on Sean's coach robbery, are told in the Biography.",
        "Mary-Beth est pickpocket et arnaqueuse plutôt que femme de main : le Red Dead Wiki ne lui attribue aucune arme, et elle ne tire jamais un coup de feu de toute l'histoire. Ses deux arnaques du récit, la fausse domestique de Valentine et l'amnésique de l'attaque de diligence avec Sean, sont racontées dans la biographie.")},
    {"h4": two("Reading and writing", "Lire et écrire")},
    {"p": two(
        "Her notebook, kept at camp, holds her writing exercises; according to the Red Dead Wiki, new stories appear in it as the game goes on. The first two, a romance set in the Wild West and a tale of a French royal on the run, both break off into a sentence in which she calls the story \"total tripe\" or nonsense and turns on herself. The third, set in a misty Saint Denis, follows a nameless woman fleeing a French duke whose family is cursed.",
        "Son carnet, qu'on peut consulter au camp, rassemble ses essais d'écriture ; selon le Red Dead Wiki, de nouvelles histoires s'y ajoutent au fil du jeu. Les deux premières, une romance dans l'Ouest sauvage et le récit d'une aristocrate française en fuite, s'interrompent toutes deux sur une phrase où elle juge l'histoire \"total tripe\" (de la foutaise), ou absurde, et s'en prend à elle-même. La troisième, dans un Saint-Denis noyé de brume, suit une femme sans nom qui fuit un duc français à la famille maudite.")},
    {"h4": two("Camp life and item request", "Vie au camp et commande")},
    {"p": two(
        "She does chores with Tilly and Karen under Susan Grimshaw's orders, and is one of the camp members Arthur can play dominoes with, in chapters 2 and 4. In chapter 2 she can ask Arthur for a fountain pen: according to the Red Dead Wiki, she tells him she wishes she had her own room and a pen to write novels. The pen lies in a cabin at Osman Grove, near Emerald Station. The wiki adds that she gives Arthur a ring in return.",
        "Elle fait les corvées avec Tilly et Karen sous les ordres de Susan Grimshaw, et fait partie des membres du camp avec qui Arthur peut jouer aux dominos, aux chapitres 2 et 4. Au chapitre 2, elle peut demander à Arthur un stylo-plume : d'après le Red Dead Wiki, elle lui confie qu'elle rêve d'une chambre à elle et d'un stylo pour écrire des romans. Le stylo se trouve dans une cabane d'Osman Grove, près d'Emerald Station. Le wiki ajoute qu'elle offre une bague à Arthur en échange.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two(
            "Arthur is the gang member she talks to most. She rides with him to Valentine, is the first to call out to him when he collapses at Clemens Point after escaping the O'Driscolls, and smokes with him at Shady Belle before Susan brings news of Tilly's kidnapping (see Biography). At Horseshoe Overlook she asks what is on his mind; he says the time of outlaws has passed and that the gang can only wait to answer for its sins, and she tells him he is the only one in camp who understands how lost he is. According to the Red Dead Wiki, she also tells him in a camp conversation that her mother came from New Hanover, and the two talk about writing: stories for her, his journal for him.",
            "Arthur est le membre du gang avec qui elle parle le plus. Elle part avec lui à Valentine, est la première à l'appeler quand il s'effondre à Clemens Point après avoir échappé aux O'Driscoll, et fume une cigarette avec lui à Shady Belle avant que Susan n'annonce l'enlèvement de Tilly (voir la biographie). À Horseshoe Overlook, elle lui demande ce qui le tracasse ; il répond que le temps des hors-la-loi est passé et que la bande n'a plus qu'à attendre de payer pour ses péchés, et elle lui dit qu'il est le seul au camp à mesurer à quel point il est perdu. D'après le Red Dead Wiki, elle lui raconte aussi, au détour d'une conversation, que sa mère venait de New Hanover, et tous deux parlent d'écriture : des histoires pour elle, son journal pour lui."),
        two(
            "At the party for Sean's return Arthur can dance with her while Dutch dances with Molly; the scene does not trigger if he is drunk. According to the wiki, she also comes to him to ask whether he has seen Mary. At Beaver Hollow he can tell her he has tuberculosis; she offers her sympathy and tells him he still has time to do good (see In her own words). The Red Dead Wiki notes that, apart from [[charles-smith|Charles Smith]], she is the only gang member Arthur tells about his illness. In 1907 she tells John Marston that she often thinks of Arthur (see Biography).",
            "À la fête du retour de Sean, Arthur peut danser avec elle pendant que Dutch danse avec Molly ; la scène ne se déclenche pas s'il est ivre. Selon le wiki, elle vient aussi lui demander s'il a revu Mary. À Beaver Hollow, il peut lui apprendre qu'il a la tuberculose ; elle lui dit sa peine et l'assure qu'il a encore le temps de faire le bien (voir Dans ses propres mots). Le Red Dead Wiki relève qu'en dehors de [[charles-smith|Charles Smith]], elle est le seul membre du gang à qui Arthur parle de sa maladie. En 1907, elle confie à John Marston qu'elle pense souvent à Arthur (voir la biographie)."),
    ]},
    {"img": "tilly-jackson.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": [
        two(
            "Tilly is her closest companion in camp. At Horseshoe Overlook Tilly asks what she is reading; Mary-Beth admits it is a romance and says she knows Tilly and Karen make fun of her for it. Tilly admits it, and admits too that they read the same books, and Mary-Beth promises to lend her this one, out of Karen's sight. Another day Mary-Beth wonders about the Moon and is annoyed that Tilly does not share her dreamy mood. At Clemens Point she and Karen listen to Tilly tell how Malcolm Foreman took her from her mother.",
            "Tilly est sa plus proche compagne au camp. À Horseshoe Overlook, Tilly lui demande ce qu'elle lit ; Mary-Beth avoue que c'est une romance et dit savoir que Tilly et Karen se moquent d'elle à ce sujet. Tilly le reconnaît, et reconnaît aussi qu'elles lisent les mêmes livres, et Mary-Beth promet de lui prêter celui-ci, à l'insu de Karen. Un autre jour, Mary-Beth se perd en rêveries sur la Lune et s'agace que Tilly ne la suive pas. À Clemens Point, Karen et elle écoutent Tilly raconter comment Malcolm Foreman l'a arrachée à sa mère."),
        two(
            "After Molly O'Shea's death, Mary-Beth tells Tilly she cannot get over it; according to the Red Dead Wiki, Tilly shows little sympathy. Tilly's 1907 letter says the two still see each other (see Biography).",
            "Après la mort de Molly O'Shea, Mary-Beth confie à Tilly qu'elle ne s'en remet pas ; d'après le Red Dead Wiki, Tilly se montre peu compatissante. La lettre de Tilly, en 1907, indique qu'elles se voient toujours (voir la biographie)."),
    ]},
    {"img": "karen-jones.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": [
        two(
            "Karen shares the young women's chores and outings with her. At Horseshoe Overlook they agree that Valentine is not a romantic town, and Karen passes on a rumor of a curse laid on it by Native Americans after a massacre, which fascinates Mary-Beth. Sitting with Tilly, they talk about their lot: Karen says women like them were born poor into a world of men. At Clemens Point Mary-Beth hopes women will one day vote; Karen says men will not allow it and asks whom she would vote for, and Mary-Beth says there is no use talking about something that will never happen.",
            "Karen partage avec elle les corvées et les sorties des jeunes femmes. À Horseshoe Overlook, elles conviennent que Valentine n'a rien de romantique, et Karen rapporte la rumeur d'une malédiction jetée sur la ville par des Amérindiens après un massacre, ce qui passionne Mary-Beth. Assises avec Tilly, elles parlent de leur sort : pour Karen, des femmes comme elles sont nées pauvres dans un monde d'hommes. À Clemens Point, Mary-Beth espère que les femmes voteront un jour ; Karen répond que les hommes ne le permettront pas et lui demande pour qui elle voterait, et Mary-Beth répond qu'il est inutile de parler de ce qui n'arrivera jamais."),
        two(
            "At Shady Belle they argue about Saint Denis: Karen says the city is built on dirt, Mary-Beth on memories, and Karen walks off. In another scene Mary-Beth says she stole a necklace in a mansion the week before; Karen admits that the city scares her, Mary-Beth finds it all romantic, and Karen calls her mad. At the party for Jack's return, when Karen vomits by Pearson's wagon, Mary-Beth tries to get her to bed and Karen tells her to leave her alone.",
            "À Shady Belle, elles se disputent au sujet de Saint-Denis : pour Karen, la ville est bâtie sur la crasse, pour Mary-Beth, sur des souvenirs, et Karen finit par tourner les talons. Dans une autre scène, Mary-Beth raconte avoir volé un collier dans une grande demeure la semaine précédente ; Karen avoue que la ville lui fait peur, Mary-Beth trouve tout cela romantique, et Karen la traite de folle. À la fête du retour de Jack, quand Karen vomit près du chariot de Pearson, Mary-Beth essaie de la mettre au lit, et Karen lui dit de la laisser tranquille."),
    ]},
    {"img": "kieran-duffy.jpeg", "slug": "kieran-duffy", "name": "Kieran Duffy", "text": [
        two(
            "At Horseshoe Overlook, right after Karen refuses Kieran a drink, Mary-Beth brings him water; he thanks her, and she tells him Karen is nice really. Once he is free, he twice joins her where she reads east of camp. In one scene he tells her she is very pretty and she finds him sweet; in another she asks whether he can read; he says no, and her remark that someone could teach him leaves him so flustered that he walks off.",
            "À Horseshoe Overlook, juste après que Karen lui a refusé à boire, Mary-Beth apporte de l'eau à Kieran ; il la remercie, et elle lui assure que Karen est gentille, au fond. Une fois libre, il vient deux fois la trouver là où elle lit, à l'est du camp. Dans une scène, il lui dit qu'elle est très jolie, et elle le trouve adorable ; dans une autre, elle lui demande s'il sait lire ; il répond que non, et quand elle glisse que quelqu'un pourrait lui apprendre, il se trouble tant qu'il s'éclipse."),
        two(
            "After Kieran disappears during Jack's party, she asks Pearson and Miss Grimshaw where he is, and neither knows. She is the one who screams on recognizing his body in \"Horsemen, Apocalypses\" (see Biography). Afterward, according to the Red Dead Wiki, she tells Arthur that Kieran was a gentle soul who did not deserve this, calls his killers pigs and asks Arthur to make them pay, which he promises to do if he can; she also admits she had a soft spot for him.",
            "Après la disparition de Kieran pendant la fête pour Jack, elle demande à Pearson et à Miss Grimshaw où il est passé, mais aucun des deux ne le sait. C'est elle qui hurle en reconnaissant son corps dans \"Horsemen, Apocalypses\" (voir la biographie). Ensuite, d'après le Red Dead Wiki, elle dit à Arthur que Kieran était une âme douce qui ne méritait pas ça, traite ses meurtriers de porcs et demande à Arthur de les faire payer, ce qu'il promet de faire s'il le peut ; elle avoue aussi qu'elle avait un faible pour lui."),
    ]},
    {"img": "susan-grimshaw.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
        "Susan keeps after her about her reading. In \"Eastward Bound\" she tells her to put her book away and go help. At Horseshoe Overlook Susan tells Mary-Beth that she has killed people for betraying the gang; Mary-Beth asks whether reading counts as betrayal, and Susan answers that the problem is idleness, not reading. In another scene Mary-Beth says she has been working, and Susan slaps her and orders her to do more. Kaili Vernoff, who plays Susan, has described another scene between them (see Development and performance).",
        "Susan ne cesse de lui reprocher ses lectures. Dans \"Eastward Bound\", elle lui ordonne de ranger son livre et d'aller aider. À Horseshoe Overlook, Susan raconte à Mary-Beth qu'elle a déjà tué des gens pour avoir trahi la bande ; Mary-Beth lui demande si lire compte comme une trahison, et Susan répond que le problème n'est pas la lecture, mais l'oisiveté. Dans une autre scène, Mary-Beth assure qu'elle a travaillé, et Susan la gifle avant de lui ordonner d'en faire davantage. Kaili Vernoff, l'interprète de Susan, a évoqué une autre scène entre elles (voir Conception et interprétation).")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "At Clemens Point, while she reads near the wagons, Dutch wants to know what the book is. She dismisses it as a silly romance; Dutch objects that romance is nothing of the kind and turns on the charm, under John's puzzled gaze. Arthur, if he passes by, can promise her to keep it to himself. Molly later holds this flirting against Dutch (see Molly O'Shea). In \"Our Best Selves\" Dutch counts her among the runaways he calls cowards (see Biography).",
        "À Clemens Point, alors qu'elle lit près des chariots, Dutch veut savoir quel est ce livre. Elle répond que ce n'est qu'une romance idiote ; Dutch proteste qu'une romance n'a rien d'idiot et sort le grand jeu, sous l'œil perplexe de John. Arthur, s'il passe par là, peut lui promettre de garder ça pour lui. Molly reprochera ce manège à Dutch (voir Molly O'Shea). Dans \"Our Best Selves\", Dutch la range parmi les fuyards qu'il traite de lâches (voir la biographie).")},
    {"img": "molly-oshea.jpeg", "slug": "molly-oshea", "name": "Molly O'Shea", "text": two(
        "At the party for Sean's return, while Uncle, Karen and Sean sing at the poker table, Dutch and Mary-Beth try to get Molly to join in. At Clemens Point Molly reproaches Dutch for his attentions to Mary-Beth and says she fears she has grown too old for him.",
        "À la fête du retour de Sean, pendant qu'Uncle, Karen et Sean chantent à la table de poker, Dutch et Mary-Beth essaient de convaincre Molly de se joindre à eux. À Clemens Point, Molly reproche à Dutch ses attentions pour Mary-Beth et dit craindre d'être devenue trop vieille pour lui.")},
    {"img": "sadie-adler.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
        "At Colter, most of the women gather in the cabin around Sadie, who is weeping for her murdered husband, and Mary-Beth is the one consoling her. She tells Arthur, if he comes over, that Sadie will pull through, and he agrees. She continues to console her at Horseshoe Overlook.",
        "À Colter, la plupart des femmes entourent Sadie dans la cabane, en larmes après le meurtre de son mari, et c'est Mary-Beth qui la console. Si Arthur s'approche, elle lui assure que Sadie va s'en sortir, et il en convient. Elle continue de la consoler à Horseshoe Overlook.")},
    {"img": "sean-macguire.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
        "Sean brings Mary-Beth along as the decoy on his coach robbery near Face Rock, against Arthur's wishes (see Biography). The party for his return is also where Arthur can dance with her (see Arthur Morgan).",
        "Sean emmène Mary-Beth comme appât lors de son attaque de diligence près de Face Rock, contre l'avis d'Arthur (voir la biographie). C'est aussi à la fête de son retour qu'Arthur peut danser avec elle (voir Arthur Morgan).")},
    {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
        "Uncle drives the wagon to Valentine with Mary-Beth, Karen and Tilly in \"Polite Society, Valentine Style\". On the way, she and Uncle trade insults over Arthur's help to a stranded driver (see Biography).",
        "Uncle conduit le chariot jusqu'à Valentine avec Mary-Beth, Karen et Tilly dans \"Polite Society, Valentine Style\". En route, Uncle et elle échangent des piques au sujet du cocher en panne qu'Arthur a aidé (voir la biographie).")},
    {"img": "simon-pearson.jpeg", "slug": "simon-pearson", "name": "Simon Pearson", "text": two(
        "Asked where Kieran is, Pearson does not know and changes the subject to a shark he once watched devour several men.",
        "Quand elle lui demande où est Kieran, Pearson n'en sait rien et enchaîne sur un requin qu'il aurait vu dévorer plusieurs hommes.")},
    {"img": "lenny-summers.jpeg", "slug": "lenny-summers", "name": "Lenny Summers", "text": two(
        "According to the Red Dead Wiki, Lenny and Mary-Beth make fun of Pearson's cooking together, until Susan tells them to mind their manners because Pearson takes good care of them.",
        "D'après le Red Dead Wiki, Lenny et Mary-Beth se moquent ensemble de la cuisine de Pearson, jusqu'à ce que Susan leur demande de surveiller leurs manières, puisque Pearson prend bien soin d'eux.")},
    {"img": "josiah-trelawny.jpeg", "slug": "josiah-trelawny", "name": "Josiah Trelawny", "text": two(
        "At Clemens Point Trelawny compliments her looks and makes a crow fly out of the book she is reading. Once he has gone, Karen calls him a devil, and Mary-Beth answers that he is a kind one.",
        "À Clemens Point, Trelawny la complimente sur sa beauté et fait surgir un corbeau du livre qu'elle lit. Une fois qu'il est parti, Karen le traite de diable ; Mary-Beth, elle, le trouve gentil, pour un diable.")},
    {"img": "abigail-marston.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
        "At Colter Abigail sits by the fire with Mary-Beth and Tilly when Arthur comes in. Both women speak of Kieran's death after \"Horsemen, Apocalypses\".",
        "À Colter, Abigail est assise près du feu avec Mary-Beth et Tilly quand Arthur entre. Les deux femmes évoquent la mort de Kieran après \"Horsemen, Apocalypses\".")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "Mary-Beth is at the campfire with Dutch, Hosea, John, Abigail and the others when the gang welcomes Jack back to Shady Belle, after Javier's song. The Red Dead Wiki notes that, like most of the women of the gang, she has a soft spot for the boy.",
        "Mary-Beth est autour du feu avec Dutch, Hosea, John, Abigail et les autres quand le gang accueille Jack à Shady Belle, après la chanson de Javier. Le Red Dead Wiki relève que, comme la plupart des femmes de la bande, elle a un faible pour le garçon.")},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "According to the French Red Dead Wiki's page on Micah Bell, Micah invites Mary-Beth to dance at the Clemens Point camp, and she turns him down. She has no scenes with him in the story missions.",
        "Selon la page consacrée à Micah Bell sur le Red Dead Wiki francophone, Micah invite Mary-Beth à danser au camp de Clemens Point, et elle refuse. Elle ne partage aucune scène avec lui dans les missions principales.")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "In the epilogue John can find her at Valentine station, where they talk about Arthur and she gives him one of her novels (see Biography).",
        "Dans l'épilogue, John peut la retrouver à la gare de Valentine, où ils parlent d'Arthur et où elle lui offre l'un de ses romans (voir la biographie).")},
]
