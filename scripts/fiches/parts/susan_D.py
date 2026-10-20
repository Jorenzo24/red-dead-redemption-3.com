"""Susan Grimshaw, reference fiche, PART D: base data, Development and performance, Reception.

Her live page (characters/susan-grimshaw/) was generated from the v2 entry in scripts/_enrich.py
(ENRICHED, "slug": "susan-grimshaw"); the base below is rebuilt from that entry, with corrections.
Changes from the v2 page: the Rockstar description is removed from the intro (it belongs to part B,
Personality); the "Deceased" chip duplicated "Died 1899" and is dropped, as is the "Camp matriarch" chip
(wiki wording); nationality is no longer asserted (no in-game source: the facts grid gives the wiki's
reading, schema nationality None); the v2 Development paragraphs are kept, re-verified against the
Forbes and GameFragger interviews themselves (fetched 20 Oct 2026) and expanded (career, the performance
capture process, re-recordings, the bath scene, the Tilly rescue, the death scene, cut content); the
Reception section keeps Polygon (now quoted from the article itself) and adds Game Informer. Eyebrow and
reg_role match characters_registry.py ("Van der Linde gang &middot; RDR2"). publishDate 2026-07-04 kept
(git: 6b91468, drip publish of susan-grimshaw, 4 Jul 2026).

Sources (internal register, checked 20 Oct 2026, saved in scratchpad cov/susan/fc/ unless noted):
- Forbes, Heather Newman, "Susan Grimshaw's Actress Describes Four Years Of 'Red Dead Redemption 2'",
  12 Feb 2019 (archived copy of 12 Feb 2019 fetched, forbes.txt): first video game worked on and played;
  "comfortable undergarments"; did not know about the MoCap suit; months before learning it was a new Red
  Dead game; performance capture on scale sets; "middle-aged badass women"; "isn't necessarily likable off
  the bat"; the code ("Everyone must earn their keep; she cannot abide hangers on or laziness; and she
  values loyalty above all."); "coquettish around Dutch, and flustered around Micah"; fans hated then loved
  her; "about four and a half years, off and on"; Rod Edge; the washing scene with Roger Clark, "quite a few
  takes"; Miranda Cowan in GTA V, voice only, did not know it was GTA V; closest with Meeya Davis (Tilly),
  Sam Strelitz (Mary-Beth), Jo Armeniox (Karen); The Path, Grey's Anatomy, House of Cards, The Enemy Within.
- GameFragger, Josh Wilding, 21 Feb 2019 (fetched, gamefragger.txt): did not know about the suit; a couple
  of days then months away; "the gang is her family"; "This is my camp"; vulnerability; first time with a
  gun on the Tilly mission; booth sessions to adjust early scenes; still at Clemens Point as a player; the
  death scene, "how betrayed I felt", Rod Edge asking for "one more moan, one more cry"; "Susan dies
  defending her family and she wouldn't have it any other way."; the farewell to Tilly, Meeya Davis-Glover
  pregnant at the time (her belief: "I believe that she was actually pregnant"); Peter Blomquist (Micah);
  GTA V recorded in the middle of the Red Dead shoot.
- GamesRadar+, Rachel Weber, "Sisterhood, shotguns and slapping", 7 Mar 2019 (../abigail/fc/gr_sisterhood.txt):
  rescue mission quote; "middle-aged badass video game characters who will take a guard down with a knife
  in the throat"; Micah hauling Susan onto his lap in one of her first scenes; Samantha Strelitz on the
  scene shot with Vernoff about vanity and aging (a similar moment, not named as the mirror scene).
- Wikipedia, "List of Red Dead Redemption 2 characters" (susan/m/wp_List...): Susan section (Vernoff; four
  and a half years; vulnerability; re-recording; "will go to any lengths"; Campbell); "Kaili Vernoff"
  (fetched): Boston University BFA, six Woody Allen projects (Sweet and Lowdown 1999, The Curse of the Jade
  Scorpion 2001, Crisis in Six Scenes 2016), Miranda Cowan in GTA V (2013).
- Polygon, Colin Campbell, "Red Dead Redemption 2 is a confection of cowboy clichés", 22 Nov 2018 (fetched,
  polygon_campbell.txt).
- Game Informer staff ranking of the gang, 27 Dec 2018 (../abigail/fc/gi_ranking.txt): Susan 11th.
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (../uncle/fc/): unused earrings and corset; Eliza
  mission strand line (relz2.awc); unused encounter after Karen's departure (csn15.awc); concept art of
  Swanson, Grimshaw and Hosea (hosea_D also mentions it, from Hosea's side).
- Official guide character page (SusanGrimshawBio.jpg, guide_bio.txt) and Rockstar's 6 Sep 2018 description:
  quoted in part B only; used here for the facts grid wording.
Excluded: Vernoff's birth year (not needed); the Hellblazer Biz video (not checked; Wikipedia's
re-recording point is sourced here to GameFragger); Vernoff's "I believe" about Davis-Glover's pregnancy
(personal, not about the game); Jim Santangeli naming Susan his favorite character (trivia, part C); the
wiki's "retired painted lady" credit (part C, attributed, if kept); Game Informer's "poetic quality" phrase
(evaluative aside); Campbell's "busty" (kept out; the quoted phrases suffice).
DUPLICATE ownership: actress, interviews and cut content live HERE; parts B and C must not retell them.
Rockstar's description and the guide page belong to part B; the fiancé and early years belong to part A.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Susan is played by Kaili Vernoff, who provides her voice and her performance capture. Vernoff is a stage and screen actress trained at Boston University; according to Wikipedia, she has appeared in six Woody Allen projects, among them Sweet and Lowdown (1999), The Curse of the Jade Scorpion (2001) and the series Crisis in Six Scenes (2016). Around the game's release she had recurring roles in The Path and Grey's Anatomy and appeared in the series finale of House of Cards, as she told Forbes in February 2019.",
              "Susan est interprétée par Kaili Vernoff, qui lui prête sa voix et assure sa capture de jeu. Actrice de théâtre et d'écran formée à l'université de Boston, elle a tourné dans six projets de Woody Allen selon Wikipédia, dont Accords et Désaccords (1999), Le Sortilège du scorpion de jade (2001) et la série Crisis in Six Scenes (2016). Au moment de la sortie du jeu, elle sortait de rôles récurrents dans The Path et Grey's Anatomy et venait d'apparaître dans le dernier épisode de House of Cards, comme elle le rappelait à Forbes en février 2019.")},
    {"p": two("Red Dead Redemption 2 was both the first video game she worked on and the first she ever played, she told Heather Newman of Forbes in an interview published on 12 February 2019. For her first booking she was sent a few scenes to learn and told to wear \"comfortable undergarments\", and she did not realize she would be wearing a motion capture suit until she arrived at the studio. She told GameFragger (Josh Wilding, 21 February 2019) that she worked a couple of days, then did not return for months and assumed her part was over, and only later understood that she was playing Susan. According to Forbes, it took her a few months to learn that the project was a new Red Dead game. She worked on it \"for about four and a half years, off and on\", sometimes a week straight, then nothing for months.",
              "Red Dead Redemption 2 est à la fois le premier jeu vidéo sur lequel elle a travaillé et le premier auquel elle a joué, confie-t-elle à Heather Newman, de Forbes, dans un entretien publié le 12 février 2019. Pour sa première séance, on lui envoie quelques scènes à apprendre en lui conseillant de porter des \"comfortable undergarments\" (des sous-vêtements confortables), et elle ne découvre qu'en arrivant au studio qu'elle va enfiler une combinaison de capture de mouvement. Auprès de GameFragger (Josh Wilding, 21 février 2019), elle raconte avoir tourné deux ou trois jours, puis n'être pas revenue pendant des mois, persuadée que son rôle était terminé, avant de comprendre qu'elle jouait Susan. D'après Forbes, il lui a fallu quelques mois pour apprendre qu'il s'agissait d'un nouveau Red Dead. Elle a travaillé sur le jeu environ quatre ans et demi, par intermittence, parfois une semaine d'affilée, puis plus rien pendant des mois.")},
    {"p": two("Vernoff also worked for Rockstar on Grand Theft Auto V (2013), as the voice of Miranda Cowan, an aging party girl. She told Forbes and GameFragger that this was a voice-only booth job recorded in the middle of the Red Dead shoot, that she did not know which game it was until she arrived, and that she had to make sure Miranda sounded nothing like Susan.",
              "Vernoff a aussi travaillé pour Rockstar sur Grand Theft Auto V (2013), en prêtant sa voix à Miranda Cowan, une fêtarde vieillissante. Elle explique à Forbes et à GameFragger qu'il s'agissait d'un simple doublage en cabine, enregistré en plein tournage de Red Dead, qu'elle ignorait de quel jeu il s'agissait avant d'arriver, et qu'elle devait veiller à ce que Miranda ne ressemble en rien à Susan.")},
    {"h3": two("Playing Susan", "Jouer Susan")},
    {"p": two("Vernoff described Susan's rules to Forbes: \"Everyone must earn their keep; she cannot abide hangers on or laziness; and she values loyalty above all.\" She said the character \"isn't necessarily likable off the bat\", which made her fun to play, and that Susan can be almost coquettish around Dutch and flustered around Micah. To GameFragger she said that the gang is Susan's family. Susan believes, she added, that the gang could not survive without her. As she came to understand the character over the years, she wanted Susan's vulnerability to come through, in the moments when the men tease her or make advances. She also cited a camp scene in which Susan tells Mary-Beth, caught looking at herself in a mirror, that vanity will get her nowhere. Samantha Strelitz, who plays Mary-Beth, told GamesRadar+ in March 2019 that a scene she shot with Vernoff was about vanity, aging and two women struggling to connect.",
              "Auprès de Forbes, Vernoff résume les règles de Susan : \"Everyone must earn their keep; she cannot abide hangers on or laziness; and she values loyalty above all.\" (chacun doit mériter sa place ; elle ne supporte ni les parasites ni la paresse ; et elle place la loyauté au-dessus de tout). Le personnage \"isn't necessarily likable off the bat\" (n'est pas forcément sympathique au premier abord), dit-elle, et c'est ce qui le rendait si amusant à jouer ; Susan se montre presque coquette avec Dutch et troublée face à Micah. À GameFragger, elle explique que la bande est la famille de Susan. Celle-ci, ajoute-t-elle, la croit incapable de survivre sans elle. À mesure qu'elle comprenait le personnage, elle a voulu faire ressortir sa vulnérabilité, dans les moments où les hommes la taquinent ou lui font des avances. Elle cite aussi une scène de camp où Susan, surprenant Mary-Beth devant un miroir, lui fait comprendre que la vanité ne la mènera nulle part. Samantha Strelitz, l'interprète de Mary-Beth, racontait en mars 2019 à GamesRadar+ qu'une scène tournée avec Vernoff parlait de vanité, de vieillissement et de deux femmes qui peinent à se comprendre.")},
    {"p": two("Some early scenes were later adjusted. Vernoff told GameFragger that she was called back to the voiceover booth to rework a few moments shot before she really knew who Susan was, so that they matched the character she had become. She told Forbes that the motion capture director Rod Edge shot as many takes as a scene needed. The scene in which Susan makes Arthur wash took her and Roger Clark \"quite a few takes\", she told the same outlet, and fans often mention it to her.",
              "Certaines scènes anciennes ont été retouchées par la suite. Vernoff raconte à GameFragger avoir été rappelée en cabine pour reprendre quelques moments tournés avant qu'elle ne sache vraiment qui était Susan, afin qu'ils collent au personnage qu'elle était devenue. Auprès de Forbes, elle salue le directeur de la capture Rod Edge, qui tournait autant de prises qu'il le fallait. La scène où Susan oblige Arthur à se laver lui a demandé, ainsi qu'à Roger Clark, \"quite a few takes\" (un bon nombre de prises), confie-t-elle au même magazine, et les fans lui en parlent souvent.")},
    {"p": two("The rescue of Tilly was the first time she worked with a gun in the game, she told GameFragger. In the GamesRadar+ feature by Rachel Weber, published on 7 March 2019, she said she knew few \"middle-aged badass video game characters who will take a guard down with a knife in the throat\", and that the mission balanced the scenes in which Susan is vicious with the girls in camp. She recalled one of her first scenes, in which Peter Blomquist, as Micah, hauls Susan onto his lap and teases her about her age, and said she burst out laughing on most takes.",
              "Le sauvetage de Tilly est la première fois qu'elle manie une arme dans le jeu, raconte-t-elle à GameFragger. Dans l'article de Rachel Weber publié par GamesRadar+ le 7 mars 2019, elle dit connaître peu de \"middle-aged badass video game characters who will take a guard down with a knife in the throat\" (de dures à cuire d'âge mûr capables d'abattre un garde d'un coup de couteau dans la gorge), et voit dans cette mission un contrepoids aux scènes où Susan se montre féroce avec les filles du camp. Elle se souvient de l'une de ses premières scènes, où Peter Blomquist, dans le rôle de Micah, attire Susan sur ses genoux et la taquine sur son âge, et dit avoir éclaté de rire à presque chaque prise.")},
    {"p": two("On Susan's death, she told GameFragger that she was surprised at how betrayed she felt when the character was shot, with the standoff carrying on and nobody running to her. Rod Edge, standing next to her, kept asking for \"one more moan, one more cry\" so that her pain would color the scene. Asked whether Susan deserved a happier ending, she answered: \"I think Susan dies defending her family and she wouldn't have it any other way.\" The moment that moved her most on set, she said, was Susan's farewell to Tilly, played by Meeya Davis-Glover, with whom she had grown close.",
              "À propos de la mort de Susan, elle confie à GameFragger avoir été surprise de se sentir à ce point trahie au moment où le personnage est abattu, alors que l'affrontement se poursuit et que personne ne se précipite vers elle. Rod Edge, à ses côtés, lui demandait \"one more moan, one more cry\" (encore un gémissement, encore un cri) pour que sa douleur imprègne la scène. Quand on lui demande si Susan méritait une fin plus heureuse, elle répond : \"I think Susan dies defending her family and she wouldn't have it any other way.\" (je pense que Susan meurt en défendant sa famille, et qu'elle n'aurait pas voulu qu'il en soit autrement). Le moment qui l'a le plus émue sur le plateau, dit-elle, reste les adieux de Susan à Tilly, jouée par Meeya Davis-Glover, dont elle était devenue proche.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("According to the Red Dead Wiki, the files of Red Dead Redemption 2 contain unused earrings and an unused corset for Susan. Audio from a cut mission strand about a character named Eliza has Susan asking Arthur at Clemens Point whether he has seen her. An unused camp encounter, set after Karen leaves the gang, has Susan nervously telling the camp's girls that Karen stormed off the night before after telling her to go to hell. A piece of concept art shows her with Reverend Swanson and Hosea.",
              "D'après le Red Dead Wiki, les fichiers de Red Dead Redemption 2 contiennent pour Susan des boucles d'oreilles et un corset inutilisés. Des fichiers audio d'une série de missions coupée, consacrée à un personnage nommé Eliza, font demander par Susan à Arthur, à Clemens Point, s'il l'a vue. Une rencontre de camp inutilisée, située après le départ de Karen, montre Susan annonçant nerveusement aux filles du camp que Karen est partie en claquant la porte la veille au soir, après l'avoir envoyée au diable. Une illustration conceptuelle la montre aux côtés du révérend Swanson et d'Hosea.")},
]

BLOCKS_RECEPTION = [
    {"h3": two("Critics", "La critique")},
    {"p": two("In a Polygon column of 22 November 2018 titled \"Red Dead Redemption 2 is a confection of cowboy clichés\", Colin Campbell took Susan as his first example. He described her as a frontierswoman who mothers her charges and turns into an \"angry she-bear\" to protect them, a figure that exists \"to offer support and wisdom to the male hero\", and compared her to Ma Ingalls in Little House on the Prairie, Mrs. Jorgensen in The Searchers and Mrs. Claggett in Destry Rides Again. He concluded: \"She's literally a walking cliché.\"",
              "Dans une chronique publiée par Polygon le 22 novembre 2018 sous le titre \"Red Dead Redemption 2 is a confection of cowboy clichés\" (Red Dead Redemption 2, une confiserie de clichés de cow-boys), Colin Campbell prend Susan comme premier exemple. Il la décrit comme une femme de la Frontière qui materne ses protégés et se change en \"angry she-bear\" (ourse en colère) pour les défendre, une figure qui n'existe que pour apporter soutien et sagesse au héros masculin, et la rapproche de Ma Ingalls dans La Petite Maison dans la prairie, de Mrs. Jorgensen dans La Prisonnière du désert et de Mrs. Claggett dans Femme ou démon. Sa conclusion : \"She's literally a walking cliché.\" (c'est littéralement un cliché ambulant).")},
    {"p": two("In Game Informer's staff ranking of the 24 gang members, published on 27 December 2018, Susan comes 11th. The staff called her \"the hawk of the camp\", cited her amusing scenes and described her killing of Molly O'Shea as \"cold-blooded\" and \"vengeful\"; in the same list, the entry on Molly calls her \"vengeful mama bear Susan Grimshaw\". Vernoff told Forbes in February 2019 that the reaction she heard most often from fans was that they hated Susan at the start of the game and had come to love and admire her by the end.",
              "Dans le classement des 24 membres du gang établi par la rédaction de Game Informer et publié le 27 décembre 2018, Susan arrive 11e. La rédaction la qualifie de \"hawk of the camp\" (le faucon du camp), cite ses scènes amusantes et juge le meurtre de Molly O'Shea \"cold-blooded\" (de sang-froid) et vengeur ; dans la même liste, la notice consacrée à Molly parle de \"vengeful mama bear Susan Grimshaw\" (Susan Grimshaw, mère ourse vengeresse). Vernoff confiait à Forbes en février 2019 que la réaction qu'elle entendait le plus souvent chez les fans était qu'ils détestaient Susan au début du jeu et avaient fini par l'aimer et l'admirer.")},
]


BASE = {
    "slug": "susan-grimshaw", "name": "Susan Grimshaw",
    "publishDate": "2026-07-04", "updated": "2026-10-19", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
    "gender": "Female", "death": "1899", "nationality": None,
    "portrait_alt": two("Susan Grimshaw in Red Dead Redemption 2", "Susan Grimshaw dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
    "meta_desc": two("Susan Grimshaw, who runs the Van der Linde gang's camp in RDR2: her past with Dutch, Tilly's rescue, Molly's death, her stand against Micah in 1899, and Kaili Vernoff's performance.",
                     "Susan Grimshaw, qui dirige le camp du gang Van der Linde dans RDR2 : son passé avec Dutch, le sauvetage de Tilly, la mort de Molly, son face-à-face avec Micah en 1899 et l'interprétation de Kaili Vernoff."),
    "og_desc": two("The complete reference on Susan Grimshaw: life, camp scenes, missions, quotes, development and reception.",
                   "La référence complète sur Susan Grimshaw : vie, scènes de camp, missions, citations, conception et accueil."),
    "schema_desc": two("Long-standing member of the Van der Linde gang who runs its camp, a former partner of Dutch van der Linde, shot dead by Micah Bell at Beaver Hollow in 1899, in Red Dead Redemption 2.",
                       "Membre de longue date du gang Van der Linde qui en dirige le camp, ancienne compagne de Dutch van der Linde, abattue par Micah Bell à Beaver Hollow en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Morte en <strong>1899</strong>"), two("Van der Linde gang", "Gang Van der Linde"),
              two("Voiced by <strong>Kaili Vernoff</strong>", "Voix de <strong>Kaili Vernoff</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Susan Grimshaw, usually called Miss Grimshaw", "Susan Grimshaw, le plus souvent appelée Miss Grimshaw")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, Beaver Hollow, shot by Micah Bell in \"Red Dead Redemption\"", "1899, à Beaver Hollow, abattue par Micah Bell dans \"Red Dead Redemption\"")},
        {"label": two("Status", "Statut"), "value": two("Deceased; buried by Charles Smith in Roanoke Ridge", "Décédée ; enterrée par Charles Smith à Roanoke Ridge")},
        {"label": two("Nationality", "Nationalité"), "value": two("Not stated in the game (American according to the Red Dead Wiki)", "Non précisée dans le jeu (américaine selon le Red Dead Wiki)")},
        {"label": two("Relationships", "Relations"), "value": two("Former partner of Dutch van der Linde (official guide)", "Ancienne compagne de Dutch van der Linde (guide officiel)")},
        {"label": two("Affiliation", "Affiliation"), "value": two("Van der Linde gang", "Gang Van der Linde")},
        {"label": two("Role", "Rôle"), "value": two("Runs the camp; sets up each new camp, with Simon Pearson", "Dirige le camp ; installe chaque nouveau camp, avec Simon Pearson")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Kaili Vernoff (voice and performance capture)", "Kaili Vernoff (voix et capture de jeu)")},
    ],
    "intro": [
        two("Susan Grimshaw is a long-standing member of the Van der Linde gang and the woman who runs its camp, a supporting character of Red Dead Redemption 2 (2018), set in 1899. A former partner of [[dutch-van-der-linde|Dutch van der Linde]], she sets up each new camp with [[simon-pearson|Simon Pearson]] and keeps the others at their chores. In the fourth chapter she rescues [[tilly-jackson|Tilly Jackson]] from the Foreman brothers with [[arthur-morgan|Arthur Morgan]]. At the end of the fifth chapter she shoots [[molly-oshea|Molly O'Shea]], newly arrived at Beaver Hollow, after Molly claims to have informed on the gang. In the sixth she sides with Arthur and [[john-marston|John Marston]] against [[micah-bell|Micah Bell]], who shoots her dead.",
            "Susan Grimshaw est un membre de longue date du gang Van der Linde, la femme qui en dirige le camp, et un personnage secondaire de Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Ancienne compagne de [[dutch-van-der-linde|Dutch van der Linde]], elle installe chaque nouveau camp avec [[simon-pearson|Simon Pearson]] et tient les autres à leurs corvées. Au quatrième chapitre, elle délivre [[tilly-jackson|Tilly Jackson]] des frères Foreman avec [[arthur-morgan|Arthur Morgan]]. À la fin du cinquième, elle abat [[molly-oshea|Molly O'Shea]], tout juste arrivée à Beaver Hollow, qui prétend avoir dénoncé la bande. Au sixième, elle se range du côté d'Arthur et de [[john-marston|John Marston]] contre [[micah-bell|Micah Bell]], qui la tue."),
        two("She is played by Kaili Vernoff, an actress who worked on the game for about four and a half years.",
            "Elle est interprétée par Kaili Vernoff, une actrice qui a travaillé sur le jeu pendant environ quatre ans et demi."),
    ],
    "essentials": [
        two("Dutch's companion in the early years, according to the official guide; the two stayed partners after their relationship ended.",
            "Compagne de Dutch dans les premières années, selon le guide officiel ; tous deux sont restés associés après leur rupture."),
        two("Sets up each new camp, with Simon Pearson, and makes the younger women, Karen, Mary-Beth and Tilly, do their share.",
            "Installe chaque nouveau camp, avec Simon Pearson, et oblige les plus jeunes, Karen, Mary-Beth et Tilly, à faire leur part."),
        two("Rides with Arthur to Radley's House in \"No, No and Thrice, No\" to free Tilly from the Foreman brothers.",
            "Part avec Arthur jusqu'à Radley's House dans \"No, No and Thrice, No\" pour arracher Tilly aux frères Foreman."),
        two("Shoots Molly O'Shea at Beaver Hollow, at the end of chapter 5, after Molly's false claim that she told the Pinkertons about the Saint Denis bank job.",
            "Abat Molly O'Shea à Beaver Hollow, à la fin du chapitre 5, après que celle-ci a faussement prétendu avoir renseigné les Pinkerton sur le braquage de la banque de Saint-Denis."),
        two("Holds Micah at gunpoint when Arthur names him as the informant, and is shot by Micah when Javier's warning that Pinkertons are coming makes her turn.",
            "Tient Micah en joue quand Arthur le désigne comme l'informateur, et se fait abattre par Micah au moment où Javier, qui annonce l'arrivée des Pinkerton, lui fait tourner la tête."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["tilly-jackson", "molly-oshea", "micah-bell", "dutch-van-der-linde"],
}
