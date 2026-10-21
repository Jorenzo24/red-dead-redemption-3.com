"""Abraham Reyes, part B: Personality (official description, observable traits, In his own words, Names, Appearance),
Propaganda, weapons and horse (the fiche-specific skills section), Relationships (21 Oct 2026, medium tier).

Coverage: the Red Dead Wiki EN sections Personality (traits kept only where a transcript supports them), the GOTY quote
box, the two quote boxes at the top of the page ("I owe it to the future of Mexico to breed..." and "Marry a
peasant?..."), the infobox (weapons, mount, family, affiliations), the trivia on the meaning of "Reyes", the Confederate
belt buckle, the posters, the Winchester Repeater, the corridos, Herbert Moon's remarks, the Bruiser and audio trivia of
Undead Nightmare; plus the five RDR1 transcripts and the pages "Agave Viejo", "Reyes' Rebels", "Reyes' Rebels Outfit",
"Herbert Moon", "Raul Zubieta", "Ayauhtéotl", "A Civilized Man". Narrative events are told in part A; entries below
point to them.

SOURCE REGISTER (read 21 Oct 2026; wiki cache scripts/v3/work/_m/):
- Official description: Red Dead Redemption: Game of the Year Edition Guide (BradyGames), quoted in the quote box of
  the Red Dead Wiki EN page "Abraham Reyes" ("He is the 30-year-old son of a wealthy nobleman..."). The guide itself was
  not read: quoted through the wiki, attributed. Rockstar's 6 Sep 2018 descriptions cover the RDR2 gang only: none for
  Reyes.
- Transcripts (every quoted line checked): "Must a Savior Die?/dialogues", "Cowards Die Many Times/dialogues", "The
  Great Mexican Train Robbery/dialogues", "The Gates of El Presidio/dialogues", "An Appointed Time/dialogues"; for what
  others say of him: "Civilization, at Any Price/dialogues" (De Santa), "Mexican Caesar/dialogues" (Espinoza),
  "Captain De Santa's Downfall/dialogues" (Victor), "Father Abraham/dialogues" and "My Sister's Keeper/dialogues"
  (Luisa), "Landon Ricketts Rides Again/dialogues" (Ricketts), "The Demon Drink/dialogues" (Allende).
- Mission pages: "Must a Savior Die?" and "The Great Mexican Train Robbery" (Reyes does not fight in them; failure if
  John attacks him or kills his horse), "An Appointed Time" (failure conditions; tied-up drivers; lasso trivia), "A
  Civilized Man" (Bruiser, slimmest; the Semi-auto Shotgun and John's remark).
- Other wiki pages: "Herbert Moon" (two quote boxes), "Reyes' Rebels Outfit" (in-game description), "Agave Viejo"
  (guerrilla base), "Raul Zubieta", "Ayauhtéotl".
- Newspapers: "Another Civil War in Mexico?" (Blackwater Ledger No. 56: "Mr. Reyes", a nobleman's son), "President
  Reyes Denies He is a Tyrant, Despite Massacre" (Blackwater Ledger No. 213).
- Visual check: the live portrait.jpeg and gallery-1.jpeg for Appearance.

OWNERSHIP NOTES:
- Quoted HERE only (parts A and C must not repeat them): the GOTY description; "I owe it to the future of Mexico to
  breed...", "Marry a peasant?...", "When I rule these people...", "Like any great leader, my brother, I will
  delegate.", "That is different. They are an inferior race." (In his own words); "you should have trusted your
  brother, Abraham, all along" and Victor's "Viva Abraham Reyes!" (Names); Herbert Moon's "all the same" line
  (relationship entry; his Napoleon line is in part C Quotes); John's "You have all the makings of a great leader" (In his own words); the outfit description "Disguise yourself as one of Reyes' Rebels..." (Skills).
- Left to part C Quotes (paraphrased here, never in quotation marks): every line of the wiki's Quotes list ("Allende is
  dead... Mexico is mine!", "find your weapons", "These peasant girls...", "Two old friends reunited...", "In a country
  where most people cannot read the newspaper...", "A man like me cannot be with just one woman...", "Their energy...",
  "Sarcasm should be beneath..."), the multiplayer lines, De Santa's and Espinoza's lines, the Laura's Day exchange.
- Told once elsewhere, pointer here: every mission event (A); his origins, Madrid, the nursemaid (A Origins); the 1911
  and 1914 newspapers as a story (A); the multiplayer model (C Other media); the actor, pre-release looks and the cut
  bounty poster (D).
- Gameplay HERE only: missions he gives, failure conditions, his part in the train robbery and the fort assault as
  mechanics, the tied-up drivers and lasso behaviour, the rebels as the law after "An Appointed Time", the outfit, the
  posters, the Bruiser and audio trivia, weapons and horse.

WIKI-ONLY (kept, attributed): the GOTY description; the weapon list and the Cleveland Bay of the infobox; the Winchester
Repeater as his main weapon; the Confederate belt buckle; the poster locations; the third person in multiplayer; the
Bruiser and audio trivia; Herbert Moon's lines (wiki quote boxes, no transcript).

Excluded: "sees himself in a romantic light", "the peasants hold him in high regard", "more cynically minded", "similar to
the other revolutionaries-turned-tyrants", "espouse the virtues of eugenics", "accusations have a grain of truth but are
greatly exaggerated", "seems to respect", "addicted to sex", "foreshadowing", Mussolini comparison, Napoleon analysis,
"Damnation because he was a hypocrite" (wiki interpretation or speculation); "mans a cannon during the assault on El
Presidio" (the transcript and mission page give the cannon to John); "admits he would have liked to meet Dutch" (not in
the transcript: he asks where Dutch is); the wiki's version of "Marry a peasant?" with an obscene phrase and "the makings
of a true leader" (the transcripts read otherwise; the transcript wording is used); "Now find your weapons and let's
fight these dogs!" (wiki wording; transcript has "Now find your weapons and fight these dogs!", left to C); the FR wiki's
age 27 said by a rebel (no transcript has the line) and birth year 1884 (unsourced); the FR wiki nickname "Zombie Reyes";
the FR wiki's "Famille Fortuna" as family; Drew MacFarlane sometimes wearing Reyes's outfit (wiki trivia, no source and
no value); the Pancho Villa, Zapata, Carranza, Madero, Bernardo Reyes models (wiki speculation, no Rockstar source).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "The Red Dead Wiki quotes the Game of the Year Edition guide of Red Dead Redemption: \"He is the 30-year-old son of a wealthy nobleman, who has seemingly sided with the peasants and the rebels to drive out the regime that supports Allende and de Santa. He is very vain and he does not seem to really care about the rights of the poor. However, Mr. Reyes does love to give speeches.\"",
        "Le Red Dead Wiki cite le guide de l'édition Game of the Year de Red Dead Redemption : \"He is the 30-year-old son of a wealthy nobleman, who has seemingly sided with the peasants and the rebels to drive out the regime that supports Allende and de Santa. He is very vain and he does not seem to really care about the rights of the poor. However, Mr. Reyes does love to give speeches.\" (Ce fils de riche aristocrate, âgé de 30 ans, semble s'être rangé du côté des paysans et des rebelles pour chasser le régime qui soutient Allende et De Santa. Très vaniteux, il ne paraît guère se soucier des droits des pauvres. M. Reyes adore en revanche faire des discours.)")},
    {"p": two(
        "He addresses crowds of rebels from a stump or a town square and ends his speeches with cries of \"Viva la revolución!\". He calls John my brother, amigo or compadre. He exaggerates his own deeds when he retells them (see Quotes). He talks openly about the women he sleeps with and rarely names them. He forgets Luisa Fortuna's name more than once (see Relationships).",
        "Il harangue les rebelles du haut d'une souche ou sur la place d'une ville, et termine ses discours aux cris de \"Viva la revolución!\" (vive la révolution). Il appelle John mon frère, amigo ou compadre. Il grossit ses exploits quand il les raconte (voir Citations). Il parle sans détour des femmes avec qui il couche, et cite rarement leur nom. Il oublie plus d'une fois le prénom de Luisa Fortuna (voir Relations).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "On his plans, in \"The Great Mexican Train Robbery\": \"When I rule these people, I will be fair and judicious and wise. How so you ask? Very simple... I know these people! I know this land. In short, I can make them better.\" Asked by John what he will do with power once Mexico is his, in \"The Gates of El Presidio\": \"Like any great leader, my brother, I will delegate.\" On the Chinese workers, in the same mission: \"That is different. They are an inferior race.\" John replies: \"You have all the makings of a great leader, Abraham.\"",
        "Sur ses projets, dans \"The Great Mexican Train Robbery\" : \"When I rule these people, I will be fair and judicious and wise. How so you ask? Very simple... I know these people! I know this land. In short, I can make them better.\" (quand je gouvernerai ce peuple, je serai juste, avisé et sage ; comment, me direz-vous ? C'est très simple : je connais ces gens, je connais cette terre ; bref, je peux les rendre meilleurs). Quand John lui demande ce qu'il fera du pouvoir une fois le Mexique à lui, dans \"The Gates of El Presidio\" : \"Like any great leader, my brother, I will delegate.\" (comme tout grand chef, mon frère, je déléguerai). Sur les ouvriers chinois, dans la même mission : \"That is different. They are an inferior race.\" (c'est différent : c'est une race inférieure). Réponse de John : \"You have all the makings of a great leader, Abraham.\" (vous avez tout d'un grand chef, Abraham).")},
    {"p": two(
        "On Luisa, when John asks whether he will marry her: \"Marry a peasant? My dear boy, don't be absurd. I'm going to be the next president of Mexico. My wife will meet ambassadors, kings, other great men. The very thought that I would marry some peasant girl with the hands of a farmer, well I really don't think so. [...]\" On his women, a little later: \"I owe it to the future of Mexico to breed, my brother. If I can get noble blood flowing through the veins of peasants, can you imagine how great this country can be? An army of Reyes! Of Kings!\"",
        "Sur Luisa, quand John lui demande s'il va l'épouser : \"Marry a peasant? My dear boy, don't be absurd. I'm going to be the next president of Mexico. My wife will meet ambassadors, kings, other great men. The very thought that I would marry some peasant girl with the hands of a farmer, well I really don't think so. [...]\" (épouser une paysanne ? Mon cher, ne soyez pas ridicule ; je serai le prochain président du Mexique, et ma femme recevra des ambassadeurs, des rois et d'autres grands hommes ; l'idée même d'épouser une petite paysanne aux mains de fermière, très peu pour moi [...]). Sur ses conquêtes, un peu plus loin : \"I owe it to the future of Mexico to breed, my brother. If I can get noble blood flowing through the veins of peasants, can you imagine how great this country can be? An army of Reyes! Of Kings!\" (je dois à l'avenir du Mexique de me reproduire, mon frère ; si je fais couler du sang noble dans les veines des paysans, imaginez la grandeur de ce pays ! Une armée de Reyes ! De rois !).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Reyes is the Spanish word for kings, and he plays on it himself (see above). John calls him Abraham or Reyes; Luisa calls him Abraham or Abraham Reyes. He presents himself to John as \"your brother, Abraham\" when he tells him where Javier is hiding. Victor, one of his rebels, cheers \"Viva Abraham Reyes!\" when John shoots Captain de Santa himself at Sepulcro. The Blackwater Ledger calls him Mr. Reyes in 1911, and the Blackwater Ledger & Sentinel calls him President Reyes in 1914.",
        "Reyes signifie rois en espagnol, et il joue lui-même sur le mot (voir plus haut). John l'appelle Abraham ou Reyes ; Luisa dit Abraham ou Abraham Reyes. Il se présente à John comme \"your brother, Abraham\" (ton frère Abraham) au moment de lui révéler la cachette de Javier. Victor, l'un de ses rebelles, s'écrie \"Viva Abraham Reyes!\" quand John abat lui-même le capitaine De Santa à Sepulcro. Le Blackwater Ledger l'appelle Mr. Reyes en 1911, et le Blackwater Ledger & Sentinel President Reyes en 1914.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is a man of about thirty with straight black hair falling to his shoulders, dark eyes, a mustache and a short black beard on the chin. He usually wears a ragged green shawl around his shoulders over a brown jacket. According to the Red Dead Wiki, his belt buckle bears the arms of the Confederate States of America.",
        "C'est un homme d'une trentaine d'années aux cheveux noirs et raides tombant sur les épaules, aux yeux sombres, avec une moustache et une courte barbe noire au menton. Il porte d'ordinaire un châle vert effiloché sur les épaules, par-dessus une veste brune. Selon le Red Dead Wiki, sa boucle de ceinture porte les armes des États confédérés d'Amérique.")},
]

# ---------------------------------------------------------------- SKILLS (fiche-specific)
# Suggested section title for the module: "Propaganda, weapons and horse" / "Propagande, armes et cheval".
BLOCKS_SKILLS = [
    {"h4": two("Speeches, songs and posters", "Discours, chansons et affiches")},
    {"p": two(
        "Reyes recruits through words. He gives speeches after each victory (see Biography) and says that songs reach the people better than newspapers in a country where most cannot read (see Quotes). His face is on posters across the map: according to the Red Dead Wiki, one hangs at Casa Madrugada, in the alley leading to the shooting gallery, three in Escalera, one in Tesoro Azul, one at Solomon's Folly, one at Benedict Point and one on the side of the assay office in Tumbleweed. John tells him he has seen them.",
        "Reyes recrute par la parole. Il prononce un discours après chaque victoire (voir la biographie) et explique que, dans un pays où la plupart des gens ne savent pas lire, la chanson porte mieux que le journal (voir Citations). Son portrait s'affiche dans toute la région : selon le Red Dead Wiki, on en trouve une affiche à Casa Madrugada, dans la ruelle qui mène au stand de tir, trois à Escalera, une à Tesoro Azul, une à Solomon's Folly, une à Benedict Point et une sur le mur du bureau d'essai de Tumbleweed. John lui dit les avoir vues.")},
    {"h4": two("In the game", "Côté jeu")},
    {"p": two(
        "Reyes gives three story missions in the second act of Red Dead Redemption, two of them starting at his base at Agave Viejo, and appears in two others; the Missions table lists them. Each fails if John attacks or kills him, and, in \"The Great Mexican Train Robbery\" and \"An Appointed Time\", if John kills his horse. According to the mission pages, he does not fight in \"Must a Savior Die?\" or \"The Great Mexican Train Robbery\": in the second, he draws the guards' attention while John boards the train, after handing him a knife. In \"An Appointed Time\", the mission page notes that he keeps firing at the stagecoach if John ties up its drivers instead of killing them, and that he shoots both Bill and Allende if John lassoes Bill, which can block the mission.",
        "Reyes confie trois missions principales dans le deuxième acte de Red Dead Redemption, dont deux commencent à sa base d'Agave Viejo, et apparaît dans deux autres ; le tableau des missions les recense. Chacune échoue si John l'agresse ou le tue et, dans \"The Great Mexican Train Robbery\" et \"An Appointed Time\", si John abat son cheval. D'après les pages des missions, il ne combat pas dans \"Must a Savior Die?\" ni dans \"The Great Mexican Train Robbery\" : dans la seconde, il détourne l'attention des gardes pendant que John monte dans le train, après lui avoir remis un couteau. Dans \"An Appointed Time\", la page de la mission signale qu'il continue de tirer sur la diligence si John ligote les conducteurs au lieu de les tuer, et qu'il abat Bill et Allende à la fois si John prend Bill au lasso, ce qui peut bloquer la mission.")},
    {"p": two(
        "Once \"An Appointed Time\" is complete, his rebels replace the army as the law in Nuevo Paraíso, according to the Red Dead Wiki, and the last piece of the Reyes' Rebels Outfit goes on sale in Escalera. Its in-game description reads: \"Disguise yourself as one of Reyes' Rebels and you will be treated kindly by the law in Mexico.\"",
        "Une fois \"An Appointed Time\" terminée, ses rebelles remplacent l'armée comme force de l'ordre dans le Nuevo Paraíso, selon le Red Dead Wiki, et la dernière pièce de la tenue Reyes' Rebels Outfit est mise en vente à Escalera. Sa description en jeu indique : \"Disguise yourself as one of Reyes' Rebels and you will be treated kindly by the law in Mexico.\" (déguisez-vous en rebelle de Reyes et la loi vous traitera avec égards au Mexique).")},
    {"h4": two("Weapons and horse", "Armes et cheval")},
    {"p": two(
        "The Red Dead Wiki lists a Hunting Knife, a Schofield Revolver, a Winchester Repeater and a Rolling Block Rifle among his weapons, plus the Semi-auto Shotgun of Undead Nightmare. According to the wiki, the Winchester Repeater is his main weapon: he uses it at El Presidio and in Escalera, and, depending on the player, to kill Bill Williamson or Colonel Allende. The wiki gives him a Cleveland Bay as his mount.",
        "Le Red Dead Wiki lui attribue un couteau de chasse (Hunting Knife), un Schofield Revolver, une Winchester Repeater et un Rolling Block Rifle, ainsi que le Semi-auto Shotgun d'Undead Nightmare. Selon le wiki, la Winchester Repeater est son arme principale : il s'en sert à El Presidio et à Escalera et, selon les choix du joueur, pour abattre Bill Williamson ou le colonel Allende. Le wiki lui donne pour monture un Cleveland Bay.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "John frees him from the firing squad at El Presidio, and Reyes's rebels save John from his own execution in Chuparosa (see Biography). Their alliance is a bargain struck on the first ride: Reyes is to help John find Bill Williamson and Javier Escuella, and John is to help the rebels win (see Biography). Reyes calls him his brother from then on and receives him at his ranch in Agave Viejo. John answers most of his speeches with sarcasm (see Quotes). When John threatens him over Williamson and Escuella, Reyes promises to deliver them and asks for time. The two men part after Escalera, when John declines to ride on the capital (see Biography). In Undead Nightmare, which is not canon, John kills the undead Reyes.",
        "John le soustrait au peloton d'exécution d'El Presidio, et les rebelles de Reyes lui rendent la pareille à Chuparosa (voir la biographie). Leur alliance repose sur un marché conclu dès leur première chevauchée : Reyes aidera John à retrouver Bill Williamson et Javier Escuella, et John aidera les rebelles à l'emporter (voir la biographie). Dès lors, Reyes l'appelle son frère et l'accueille dans son ranch d'Agave Viejo. John accueille la plupart de ses discours par des sarcasmes (voir Citations). Quand John le menace au sujet de Williamson et d'Escuella, Reyes promet de les lui livrer et réclame du temps. Les deux hommes se quittent après Escalera, John refusant de marcher sur la capitale (voir la biographie). Dans Undead Nightmare, qui n'appartient pas au canon, John abat Reyes devenu mort-vivant.")},
    {"img": "luisa-fortuna.jpeg", "slug": "luisa-fortuna", "name": "Luisa Fortuna", "text": two(
        "Luisa believes she is to marry him after the revolution (see Quotes). She sends John to free him at El Presidio and relays his orders in her own missions. Reyes calls her Laura, laughs at the idea of marrying her and recommends her to John. She is shot dead in Escalera trying to save him, and he later cannot remember who she was (see Biography for all three scenes).",
        "Luisa est persuadée qu'il l'épousera après la révolution (voir Citations). Elle envoie John le libérer à El Presidio et transmet ses ordres dans ses propres missions. Reyes l'appelle Laura, se moque de l'idée de l'épouser et la recommande à John. Elle est abattue à Escalera en tentant de le sauver, et il ne se souvient plus ensuite de qui elle était (ces trois scènes sont racontées dans la biographie).")},
    {"img": "agustin-allende.jpeg", "slug": "agustin-allende", "name": "Agustin Allende", "text": two(
        "The governor of Nuevo Paraíso and the target of his revolt. Reyes describes him to John as a puppet of President Sanchez, a lapdog who beats the people he swore to protect and enjoys it. Allende, for his part, tells John that men like Javier's father are natural allies for Reyes. Allende dies on the road out of Escalera, shot by John or by Reyes (see Biography).",
        "Le gouverneur du Nuevo Paraíso et la cible de sa révolte. Reyes le décrit à John comme une marionnette du président Sanchez, un petit chien qui bat le peuple qu'il a juré de protéger et y prend plaisir. Allende, de son côté, explique à John que les hommes comme le père de Javier sont des alliés naturels de Reyes. Allende meurt sur la route à la sortie d'Escalera, abattu par John ou par Reyes (voir la biographie).")},
    {"img": "vincente-de-santa.jpeg", "slug": "vincente-de-santa", "name": "Vincente de Santa", "text": two(
        "The army captain hunts Reyes and insults him at length in front of John (see Quotes). De Santa betrays John in Chuparosa just before Reyes and his rebels arrive. He dies at Sepulcro, shot by John or by the rebels, and Reyes comments on his death in \"The Gates of El Presidio\" (see Biography).",
        "Le capitaine de l'armée traque Reyes et l'insulte copieusement devant John (voir Citations). De Santa trahit John à Chuparosa juste avant l'arrivée de Reyes et de ses rebelles. Il meurt à Sepulcro, abattu par John ou par les rebelles, et Reyes commente sa mort dans \"The Gates of El Presidio\" (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Reyes's spies locate Javier at El Presidio, where, according to Reyes, he and Bill paid Allende for protection. The rebels' assault on the fort lets John reach him (see Biography).",
        "Les espions de Reyes localisent Javier à El Presidio, où, selon Reyes, Bill et lui ont payé Allende pour être protégés. L'assaut des rebelles sur le fort permet à John de l'atteindre (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Reyes cannot tell John whether Bill is at El Presidio with Javier. Bill flees Escalera in Allende's stagecoach and dies on the road, shot by John or by Reyes (see Biography).",
        "Reyes ne peut pas dire à John si Bill se trouve à El Presidio avec Javier. Bill fuit Escalera dans la diligence d'Allende et meurt sur la route, abattu par John ou par Reyes (voir la biographie).")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "The two men never meet. John tells Reyes about his old leader during \"The Great Mexican Train Robbery\" (see Biography).",
        "Les deux hommes ne se rencontrent jamais. John parle de son ancien chef à Reyes pendant \"The Great Mexican Train Robbery\" (voir la biographie).")},
    {"img": "landon-ricketts.jpeg", "slug": "landon-ricketts", "name": "Landon Ricketts", "text": two(
        "The two men share no scene. Ricketts tells John that Luisa is close to the rebel leader. Reyes cites Ricketts as an example when he suggests that John come back to Mexico one day (see Biography).",
        "Les deux hommes ne partagent aucune scène. Ricketts explique à John que Luisa est proche du chef rebelle. Reyes cite Ricketts en exemple quand il suggère à John de revenir un jour au Mexique (voir la biographie).")},
    {"img": None, "slug": None, "name": "Ignacio Sanchez", "text": two(
        "The president of Mexico, never seen in the game. Reyes calls him \"our country's kind and generous dictator\" and holds him responsible for everything Allende does. He plans to march on the capital once Escalera falls; the newspapers report the outcome (see Biography).",
        "Le président du Mexique, jamais montré dans le jeu. Reyes le qualifie de \"kind and generous dictator\", le bon et généreux dictateur du pays, et le tient pour responsable de tout ce que fait Allende. Il prévoit de marcher sur la capitale une fois Escalera tombée ; les journaux rapportent la suite (voir la biographie).")},
    {"img": None, "slug": None, "name": "His family", "text": two(
        "According to the Blackwater Ledger, he is a nobleman's son born on a ranch outside the capital. His mother and his family's view of Luisa are covered in the Biography. The Red Dead Wiki lists an unnamed father and an unnamed mother.",
        "Selon le Blackwater Ledger, il est le fils d'un aristocrate et a vu le jour dans un ranch aux abords de la capitale. Sa mère et le regard de sa famille sur Luisa sont évoqués dans la biographie. Le Red Dead Wiki mentionne un père et une mère dont le nom n'est pas donné.")},
    {"img": None, "slug": None, "name": "His rebels", "text": two(
        "Reyes' Rebels, named after him, are based at Agave Viejo. Victor tells John that women and even children fight in their ranks. In \"Father Abraham\", Luisa passes on Reyes's requests: ambush Allende's reinforcements, destroy the army's supplies and kill everyone, because Abraham wants to send a message. The prisoners John frees in Escalera declare themselves loyal to him (see Biography).",
        "Les rebelles de Reyes (Reyes' Rebels), qui portent son nom, ont leur base à Agave Viejo. Victor explique à John que des femmes, et même des enfants, se battent dans leurs rangs. Dans \"Father Abraham\", Luisa transmet les demandes de Reyes : tendre une embuscade aux renforts d'Allende, détruire le ravitaillement de l'armée et ne laisser personne en vie, car Abraham veut faire passer un message. Les prisonniers que John libère à Escalera se déclarent fidèles à Reyes (voir la biographie).")},
    {"img": None, "slug": None, "name": "Raul Zubieta", "text": two(
        "The army major who holds Reyes in Escalera. Reyes is his prisoner, tied up and beaten, when John arrives; John kills Zubieta in a duel (see Biography).",
        "Le major de l'armée qui tient Reyes prisonnier à Escalera. Reyes est son prisonnier, ligoté et roué de coups, quand John arrive ; John tue Zubieta en duel (voir la biographie).")},
    {"img": None, "slug": None, "name": "Espinoza", "text": two(
        "The army captain tells John that Reyes tries hard to recruit Americans, with propaganda everywhere promising women and gold. John kills him in Chuparosa (see Biography).",
        "Le capitaine de l'armée explique à John que Reyes cherche à tout prix à recruter des Américains, avec une propagande omniprésente qui promet des femmes et de l'or. John le tue à Chuparosa (voir la biographie).")},
    {"img": None, "slug": None, "name": "Herbert Moon", "text": two(
        "The Armadillo shopkeeper mocks him in free roam (see Quotes). In another line quoted by the Red Dead Wiki, he lumps him with the other leaders: \"Sanchez, Allende, De Santa, Reyes; all the same! They just want Armadillo rail rides.\"",
        "Le commerçant d'Armadillo se moque de lui en exploration libre (voir Citations). Dans une autre réplique citée par le Red Dead Wiki, il le met dans le même sac que les autres dirigeants : \"Sanchez, Allende, De Santa, Reyes; all the same! They just want Armadillo rail rides.\" (Sanchez, Allende, De Santa, Reyes : tous pareils ! Ils ne veulent que le train pour Armadillo).")},
    {"img": None, "slug": None, "name": "Ayauhtéotl", "text": two(
        "Undead Nightmare (non-canon): the woman the undead Reyes chases round the table of the Escalera mansion; she tells John that Reyes took a mask from the catacombs (see Biography).",
        "Undead Nightmare (hors canon) : la femme que Reyes, devenu mort-vivant, poursuit autour de la table de la demeure d'Escalera ; elle apprend à John que Reyes a emporté un masque des catacombes (voir la biographie).")},
]
