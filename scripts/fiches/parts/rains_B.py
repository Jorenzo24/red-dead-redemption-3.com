"""Rains Fall, part B: Personality (descriptions, In his own words, Names, Appearance), "Chief, remedies and
horses" (section title proposed to the lead in place of "Skills, weapons and horses": he carries no weapon on screen
and his know-how is diplomacy and herbs), Relationships (22 Oct 2026, medium tier).

Coverage: the wiki's "Personality" and "Appearance" sections, the aliases of the infobox ("Chief Rains", by Colonel
Favours), the mounts of the infobox, the trivia on his name in English, the Owl Feather Trinket page and the herb
trivia of "Archeology for Beginners", plus every relationship the transcript shows. Narrative events are told in A
(Biography): entries below point to it.

SOURCE REGISTER (fetched 22 Oct 2026):
- Full fan transcript of RDR2, Game Scripts Wiki (scripts/v3/work/rains/fc/gsw.txt, gitignored): "Eastward Bound"
  (riders on the hill, Hosea and Charles), "The Gilded Cage" (Bronte on the balcony: "the redskins", "hand a letter to
  the mayor"; Dutch on Evelyn Miller), "American Fathers I" (courthouse scene), "Archeology for Beginners" (tent, Monroe,
  ride, herbs, Chanupa, journal), "The Fine Art of Conversation" (Beaver Hollow, ride, talks; the line to his men is
  labeled "Rains Fall In Lakota"), "The King's Son" (tent; Charles's ride report), "My Last Boy" (plea at Beaver Hollow,
  Paytah on the ride back, Charles's last line). Charles's "Butcher Creek" line (chapter 6 return from Guarma).
- Red Dead Wiki EN: "Rains Fall" (infobox: aka Chief Rains by Colonel Favours; mounts Blue Roan Nokota, Grullo Dun
  Mustang, Tobiano American Paint; Personality; Appearance; Trivia), "Archeology for Beginners" (mission page: rewards
  3 English Mace and the Owl Feather Trinket if nobody is killed; herb trivia), "Owl Feather Trinket" (15 percent slower
  core drain), "Lyndon Monroe" (first name said once by Rains Fall), "Henry Favours", "Paytah", "Evelyn Miller",
  "Wapiti Indians".
- Red Dead Wiki FR: "Pluie-Battante" (scripts/v3/work/rains/fr.txt): his French wiki name; son "Aigle-Qui-Vole".
- Rockstar's character descriptions of 6 Sep 2018 (scripts/v3/sources/thr_descriptions.txt): none for him (gang only).
- Dan Houser on him (Vulture, Harold Goldberg, 14 Oct 2018): quoted in part D (Development), only pointed to here.
- Authoritative parts aligned: charles_A/B/C (promise, Taima, Monroe, Favours, Paytah wording), arthur_A/C/D/F (Isaac
  told to Rains Fall, Owl Feather Trinket, journal page), HOUSE_FACTS (Eagle Flies dies on the reservation).

Lines quoted HERE (part C must not repeat them): "Brutality and beauty...", "Even sacred things... matter more.",
"People have lied to my people for a hundred years or more... that's treason.", "The army aren't all bad men, just as
my people aren't all good.", "In English they call me Rains Fall.", "Chief Rains", "a great chief", "the impetuous
Prince", "easily led", "matters are more complex than he understands", "he walks an old line, he's obstinate and he
hates Monroe", "He's a good man, he wants to help.", "Mix these together. They taste awful...", Charles "I'm sorry, but
we... we must pack and move.", Paytah "Better to die fighting than sick and weak.", Arthur's journal "wise and
thoughtful and sensible", Arthur "I like Rains Fall". Wiki quote-list lines (correct path, glory in death, three
treaties, My Last Boy speech, "bunch of families") are left to part C and only paraphrased here.

FIXES AFTER FACT-CHECK (22 Oct 2026): relationships trimmed to what the Biography lacks, with pointers (OWNERSHIP);
Personality cut to the official-description note and his stance (the Favours, wolves, Chanupa and "disappointment"
sentences duplicated A); Charles's promise is about the horses (gsw l. 12227: "I will not fight over some horses");
Dutch praises Eagle Flies's courage BEFORE the chief enters (gsw l. 13109-13110); "brokering peace" (gsw l. 12511), not
"arranges the meeting himself"; Paytah and Hosea entries no longer retell the riders; the 1907 meeting attributed to the
wiki (FIX_RULES 9); Appearance rewritten (too close to the wiki); possessive "Eagle Flies's" fiche-wide.

Excluded: "willing to put up with decades of abuse" (wiki wording, beyond what he says); "he seems to admit his
pacifism" (wiki interpretation); the fan transcript's stage note that he "is ill with something" (not shown as a
fact); the Sitting Bull and Red Cloud models (wiki "appear to be based", speculation); the wiki claim that Favours
"was given the information of his name in Lakotan" (inference); "Fallender Regen" (German wiki, irrelevant here);
an outfit catalogue (gallery captions instead); "Tobiano American Paint" is listed as a mount by the wiki but is also
the dead horse the wolves eat in "Archeology for Beginners": kept attributed to the infobox only.
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 6, 2018 cover the Van der Linde gang and do not include Rains Fall; the words of Dan Houser, co-writer of the game and co-founder of Rockstar Games, on the character are quoted under Development and performance. In the game he argues for peace at every turn. He tells Arthur that he keeps trying to settle the tribe's conflict with the Army through negotiation, that war would be futile, and that he has never seen victory in killing. Arthur's journal and Arthur's words to Charles about him are given under Relationships.",
        "Les descriptions de personnages publiées par Rockstar le 6 septembre 2018 portent sur le gang Van der Linde et ne comprennent pas Rains Fall ; ce qu'en dit Dan Houser, coscénariste du jeu et cofondateur de Rockstar Games, est cité dans la partie Conception et interprétation. Dans le jeu, il plaide pour la paix en toute occasion. Il explique à Arthur qu'il cherche toujours à régler par la négociation le conflit qui oppose la tribu à l'armée, qu'une guerre ne mènerait à rien et qu'il n'a jamais vu de victoire dans le fait de tuer. Le journal d'Arthur et ce qu'il dit de lui à Charles figurent dans la partie Relations.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "On the way to the sacred site in \"Archeology for Beginners\": \"Brutality and beauty are both all around us, yet so often we're unable to see past our own grievances. This is what I try to teach my son.\" When Arthur brings back the pipe: \"Even sacred things... are only things. People... the heart... matter more.\" On Captain Monroe: \"The army aren't all bad men, just as my people aren't all good.\" In his tent in \"The King's Son\", after his son's capture: \"People have lied to my people for a hundred years or more... that's treason.\"",
        "En route vers le site sacré, dans \"Archeology for Beginners\" : \"Brutality and beauty are both all around us, yet so often we're unable to see past our own grievances. This is what I try to teach my son.\" (la brutalité et la beauté nous entourent, et pourtant nous sommes si souvent incapables de voir au-delà de nos propres griefs ; c'est ce que j'essaie d'apprendre à mon fils). Quand Arthur lui rapporte la pipe : \"Even sacred things... are only things. People... the heart... matter more.\" (même les choses sacrées ne sont que des choses ; les gens, le cœur, comptent davantage). À propos du capitaine Monroe : \"The army aren't all bad men, just as my people aren't all good.\" (dans l'armée, tous ne sont pas mauvais, comme tous les miens ne sont pas bons). Sous sa tente, dans \"The King's Son\", après la capture de son fils : \"People have lied to my people for a hundred years or more... that's treason.\" (on ment à mon peuple depuis cent ans ou plus ; voilà la trahison).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Rains Fall is the English form of his name. At the peace talks, Colonel Favours says he cannot pronounce \"that silly name\"; the chief answers: \"In English they call me Rains Fall.\" Favours then calls him \"Chief Rains\", the alias listed by the Red Dead Wiki. His name in his own language is never given. Evelyn Miller introduces him to Arthur as \"a great chief\". Captain Monroe addresses him as \"sir\", and Eagle Flies calls him \"Father\". The French-language Red Dead Wiki names him Pluie-Battante. An earlier name, found on concept art, is given under Development and performance.",
        "Rains Fall est la forme anglaise de son nom. Lors des pourparlers, le colonel Favours avoue ne pas pouvoir prononcer \"that silly name\" (ce nom ridicule) ; le chef répond : \"In English they call me Rains Fall.\" (en anglais, on m'appelle Rains Fall). Favours l'appelle alors \"Chief Rains\" (chef Rains), surnom que retient le Red Dead Wiki. Son nom dans sa propre langue n'est jamais donné. Evelyn Miller le présente à Arthur comme \"a great chief\" (un grand chef). Le capitaine Monroe lui dit \"sir\" (monsieur), et Eagle Flies l'appelle \"Father\" (père). Le Red Dead Wiki francophone le nomme Pluie-Battante. Un nom antérieur, relevé sur des dessins préparatoires, figure dans la partie Conception et interprétation.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is an elderly man who wears his black hair long, with a red ribbon tied around one lock. According to the Red Dead Wiki, he looks visibly older in the 1907 ending credits than at the Annesburg station in the epilogue, where his appearance is unchanged from 1899.",
        "C'est un homme âgé aux cheveux noirs portés longs, avec un ruban rouge noué autour d'une mèche. D'après le Red Dead Wiki, il paraît nettement plus âgé dans le générique de fin de 1907 qu'à la gare d'Annesburg pendant l'épilogue, où il a la même apparence qu'en 1899.")},
]

# ---------------------------------------------------------------- SKILLS (section title: "Chief, remedies and horses")
BLOCKS_SKILLS = [
    {"h4": two("Chief and negotiator", "Chef et négociateur")},
    {"p": two(
        "As chief of the Wapiti, Rains Fall deals with the authorities on the tribe's behalf; his treaties, his appointments in Saint Denis and the peace talks are told under Biography. He offers to pay Arthur \"very handsomely\" for proof about the oil on the reservation. He says he is brokering peace and that Colonel Favours has agreed to a meeting, and he wants people from outside the tribe at the table, believing it will make lying harder for the Army.",
        "En tant que chef des Wapiti, Rains Fall traite avec les autorités au nom de la tribu ; ses traités, ses rendez-vous à Saint-Denis et les pourparlers sont racontés dans la biographie. Il propose de payer Arthur \"very handsomely\" (très généreusement) pour obtenir des preuves au sujet du pétrole de la réserve. Il dit œuvrer à la paix et annonce que le colonel Favours a accepté une rencontre ; il tient à ce que des personnes étrangères à la tribu soient présentes, convaincu que l'armée aura alors plus de mal à mentir.")},
    {"h4": two("Herbs and remedies", "Plantes et remèdes")},
    {"p": two(
        "During the ride of \"Archeology for Beginners\", he stops twice to pick plants for Arthur's cough: English Mace, then ginseng. He puts them in Arthur's saddlebag with this advice: \"Mix these together. They taste awful... but it'll help to keep your strength up.\" The mission page lists three English Mace among the rewards, and notes that English Mace and ginseng are two of the three ingredients of a Special Health Cure, the third being Yarrow. If no soldier is killed, he gives Arthur the Owl Feather Trinket, which can be obtained no other way. According to the Red Dead Wiki, the trinket slows the drain of the Health, Stamina and Dead Eye cores by 15 percent.",
        "Pendant la chevauchée de \"Archeology for Beginners\", il s'arrête deux fois pour cueillir des plantes contre la toux d'Arthur : de l'English Mace, puis du ginseng. Il les glisse dans la sacoche d'Arthur avec ce conseil : \"Mix these together. They taste awful... but it'll help to keep your strength up.\" (mélangez-les ; c'est infect, mais ça vous aidera à garder des forces). La page de la mission compte trois English Mace parmi les récompenses, et précise que l'English Mace et le ginseng sont deux des trois ingrédients d'un Special Health Cure, le troisième étant l'achillée (Yarrow). Si aucun soldat n'est tué, il offre à Arthur l'Owl Feather Trinket, qu'on ne peut obtenir d'aucune autre façon. D'après le Red Dead Wiki, ce talisman ralentit de 15 % l'épuisement des noyaux de santé, d'endurance et de Dead Eye.")},
    {"h4": two("Horses", "Chevaux")},
    {"p": two(
        "Rains Fall rides his own horse to the sacred site, to the gang's camp at Beaver Hollow and to the peace talks. The Red Dead Wiki lists three mounts for him: a Blue Roan Nokota, a Grullo Dun Mustang and a Tobiano American Paint.",
        "Rains Fall se rend à cheval au site sacré, au camp du gang à Beaver Hollow et aux pourparlers. Le Red Dead Wiki lui attribue trois montures : un Nokota rouan bleu, un Mustang grullo dun et un American Paint tobiano.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": None, "slug": None, "name": "Eagle Flies", "text": [two(
        "Eagle Flies is his younger son and his only surviving child (see Biography). In Saint Denis, Eagle Flies calls Arthur a mercenary. In front of Arthur, Rains Fall calls him \"the impetuous Prince\" and says that his son is \"easily led\". In \"A Rage Unleashed\", Eagle Flies says his father need not know about the raid and would rather live in ignorance.",
        "Eagle Flies est son fils cadet et le seul enfant qui lui reste (voir la biographie). À Saint-Denis, Eagle Flies traite Arthur de mercenaire. Devant Arthur, Rains Fall le surnomme \"the impetuous Prince\" (le prince impétueux) et dit de lui qu'il se laisse \"easily led\" (facilement entraîner). Dans \"A Rage Unleashed\", Eagle Flies affirme que son père n'a pas besoin d'être au courant du raid et qu'il préfère ne rien savoir."),
        two("Their split over war and peace, his capture, his father's plea at Beaver Hollow and his death in his father's tent are told under Biography.",
            "Leur désaccord entre guerre et paix, sa capture, la supplique de son père à Beaver Hollow et sa mort sous la tente paternelle sont racontés dans la biographie.")]},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [two(
        "Rains Fall first sees [[arthur-morgan|Arthur]] with the gang's wagon train and meets him in Saint Denis. Their talks in his tent and on the ride of \"Archeology for Beginners\" (Arthur's illness, his son Isaac, his warning about Dutch) and in \"The King's Son\" are told under Biography.",
            "Rains Fall aperçoit d'abord [[arthur-morgan|Arthur]] avec le convoi de chariots du gang, puis le rencontre à Saint-Denis. Leurs échanges sous la tente et pendant la chevauchée de \"Archeology for Beginners\" (la maladie d'Arthur, son fils Isaac, sa mise en garde contre Dutch), puis dans \"The King's Son\", sont racontés dans la biographie."),
        two("After \"Archeology for Beginners\", Arthur writes in his journal that not long ago he would have found such a man weak and pathetic, and that he now sees him as \"wise and thoughtful and sensible\"; he would like to help him, or at least stop Dutch from pushing his son into something stupid. On the way to Fort Wallace he tells Charles: \"I like Rains Fall.\" In \"My Last Boy\", the chief's plea to Arthur in front of the gang reveals their dealings to Dutch. In 1907, according to the Red Dead Wiki, Rains Fall speaks of Arthur to John (see Biography).",
            "Après \"Archeology for Beginners\", Arthur écrit dans son journal qu'il n'y a pas si longtemps il aurait trouvé un tel homme faible et pitoyable, et qu'il le voit désormais \"wise and thoughtful and sensible\" (sage, réfléchi et sensé) ; il aimerait l'aider, ou au moins empêcher Dutch de pousser son fils à une bêtise. En route vers Fort Wallace, il confie à Charles : \"I like Rains Fall.\" (je l'aime bien, Rains Fall). Dans \"My Last Boy\", le chef appelle Arthur à l'aide devant le gang, ce qui révèle à Dutch leurs relations. En 1907, d'après le Red Dead Wiki, Rains Fall parle d'Arthur à John (voir la biographie).")]},
    {"img": "charles-smith.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
        "[[charles-smith|Charles]] helps the Wapiti on their reservation from chapter 5 onward (see Biography), and he has told Rains Fall that he will not fight over the tribe's horses. Rains Fall tells Arthur that most of what he knows about Dutch comes from Charles. Charles persuades Arthur to come to the peace talks (\"Do it for me\"). After Eagle Flies's death, he tells the chief: \"I'm sorry, but we... we must pack and move.\" He stays behind to help the tribe.",
        "[[charles-smith|Charles]] aide les Wapiti sur leur réserve à partir du chapitre 5 (voir la biographie), et il a dit à Rains Fall qu'il ne se battrait pas pour les chevaux de la tribu. Rains Fall confie à Arthur que l'essentiel de ce qu'il sait de Dutch lui vient de Charles. Charles convainc Arthur de venir aux pourparlers (\"Do it for me\", fais-le pour moi). Après la mort d'Eagle Flies, il dit au chef : \"I'm sorry, but we... we must pack and move.\" (je suis désolé, mais il faut faire vos bagages et partir). Il reste sur place pour aider la tribu.")},
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Rains Fall knows [[dutch-van-der-linde|Dutch]] only by reputation. He tells Arthur that Dutch \"talks a lot\". After Eagle Flies's capture, he says he is sure Dutch means well but that \"matters are more complex than he understands\" (his view of the damage done to relations with the Army is told under Biography). At Beaver Hollow, Dutch praises Eagle Flies's courage just before the chief arrives to beg his son to stay; when Rains Fall turns to Arthur, Dutch asks: \"You helped this feller, Arthur?\"",
        "Rains Fall ne connaît [[dutch-van-der-linde|Dutch]] que de réputation. Il confie à Arthur que Dutch \"talks a lot\" (parle beaucoup). Après la capture d'Eagle Flies, il le croit de bonne foi, mais estime que \"matters are more complex than he understands\" (les choses sont plus compliquées qu'il ne le croit) ; le tort que Dutch a fait aux relations avec l'armée est raconté dans la biographie. À Beaver Hollow, Dutch salue le courage d'Eagle Flies juste avant que le chef n'arrive pour supplier son fils de rester ; quand Rains Fall se tourne vers Arthur, Dutch demande : \"You helped this feller, Arthur?\" (tu as aidé ce type, Arthur ?).")},
    {"img": None, "slug": None, "name": "Henry Favours", "text": two(
        "The colonel commands the regiment at Fort Wallace. Rains Fall describes him to Arthur: \"he walks an old line, he's obstinate and he hates Monroe\". His revenge for the raid, the failed talks and the shot that kills Eagle Flies at the oil fields are told under Biography. According to the Red Dead Wiki, Favours had agreed with Leviticus Cornwall to drive the tribe off its land.",
        "Le colonel commande le régiment de Fort Wallace. Rains Fall le décrit ainsi à Arthur : \"he walks an old line, he's obstinate and he hates Monroe\" (il s'en tient à la vieille ligne, il est obstiné et il déteste Monroe). Sa vengeance après le raid, l'échec des pourparlers et le coup de feu qui tue Eagle Flies aux champs de pétrole sont racontés dans la biographie. D'après le Red Dead Wiki, Favours s'était entendu avec Leviticus Cornwall pour chasser la tribu de ses terres.")},
    {"img": None, "slug": None, "name": "Lyndon Monroe", "text": two(
        "\"He's a good man, he wants to help,\" Rains Fall tells Arthur about Captain Monroe, whose news from Saint Denis, help with the vaccines and arrest at the talks are told under Biography. According to the Red Dead Wiki, Rains Fall is the only character to say Monroe's first name, once, in \"The Fine Art of Conversation\", and only if Arthur has not met Monroe before.",
        "\"He's a good man, he wants to help\" (c'est un homme bien, il veut aider), dit le chef à Arthur à propos du capitaine Monroe, dont les nouvelles de Saint-Denis, l'aide pour les vaccins et l'arrestation lors des pourparlers sont racontées dans la biographie. D'après le Red Dead Wiki, Rains Fall est le seul à prononcer le prénom de Monroe, une fois, dans \"The Fine Art of Conversation\", et seulement si Arthur ne l'a pas rencontré auparavant.")},
    {"img": None, "slug": None, "name": "Evelyn Miller", "text": two(
        "The writer introduces Rains Fall and Eagle Flies to Arthur outside the Saint Denis courthouse and explains the oil claim and the treaty at stake (see Biography). In \"The Gilded Cage\", Dutch tells Arthur that Miller is lobbying officials in Saint Denis on the chief's behalf.",
        "C'est l'écrivain qui présente Rains Fall et Eagle Flies à Arthur devant le palais de justice de Saint-Denis, et qui lui expose l'affaire du pétrole et le traité en jeu (voir la biographie). Dans \"The Gilded Cage\", Dutch apprend à Arthur que Miller fait pression sur les responsables de Saint-Denis pour le compte du chef.")},
    {"img": "leviticus-cornwall.jpeg", "slug": "leviticus-cornwall", "name": "Leviticus Cornwall", "text": two(
        "The oil on the reservation ties [[leviticus-cornwall|Cornwall]] to the tribe's troubles (see Biography). The Leland Oil Development Company file on the oil near Wapiti, which Arthur takes in \"American Fathers II\", is kept in the foreman's office of the Cornwall Kerosene & Tar refinery. Rains Fall never meets him on screen.",
        "Le pétrole de la réserve lie [[leviticus-cornwall|Cornwall]] aux malheurs de la tribu (voir la biographie). Le dossier de la Leland Oil Development Company sur le pétrole de Wapiti, qu'Arthur emporte dans \"American Fathers II\", se trouve dans le bureau du contremaître de la raffinerie Cornwall Kerosene & Tar. Rains Fall ne le rencontre jamais à l'écran.")},
    {"img": None, "slug": None, "name": "Paytah", "text": two(
        "Paytah is Eagle Flies's companion. In \"My Last Boy\" he rides off with Eagle Flies despite the chief's plea. On the way back to the reservation with the dying Eagle Flies, he tells Arthur: \"Better to die fighting than sick and weak.\"",
        "Paytah est le compagnon d'Eagle Flies. Dans \"My Last Boy\", il part avec Eagle Flies malgré la supplique du chef. Sur le chemin de la réserve, avec Eagle Flies mourant, il dit à Arthur : \"Better to die fighting than sick and weak.\" (mieux vaut mourir en se battant que malade et affaibli).")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "In \"Eastward Bound\", [[hosea-matthews|Hosea]] tells Arthur how the Native Americans of the Heartlands lost their land (see Biography), adding that he heard the Army there was particularly harsh about it.",
        "Dans \"Eastward Bound\", [[hosea-matthews|Hosea]] raconte à Arthur comment les Amérindiens des Heartlands ont perdu leurs terres (voir la biographie), et ajoute qu'il a entendu dire que l'armée s'y était montrée particulièrement dure.")},
    {"img": "angelo-bronte.jpeg", "slug": "angelo-bronte", "name": "Angelo Bronte", "text": two(
        "From a balcony at the mayor's party in \"The Gilded Cage\", [[angelo-bronte|Bronte]] points out Rains Fall and Eagle Flies to Dutch and Arthur (see Biography). He says he has no sympathy for them, since anyone stupid enough to be tricked by the Americans gets what they deserve.",
        "Depuis un balcon, lors de la réception du maire dans \"The Gilded Cage\", [[angelo-bronte|Bronte]] désigne Rains Fall et Eagle Flies à Dutch et à Arthur (voir la biographie). Il dit n'avoir aucune sympathie pour eux : quiconque est assez bête pour se laisser duper par les Américains n'a que ce qu'il mérite.")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "[[john-marston|John]] is one of the gang members who volunteer to ride with the Wapiti in \"My Last Boy\". In 1907 he can meet Rains Fall at the Annesburg train station; according to the Red Dead Wiki, the chief knows him as one of Arthur's companions (see Biography).",
        "[[john-marston|John]] fait partie des membres du gang qui se portent volontaires pour suivre les Wapiti dans \"My Last Boy\". En 1907, il peut croiser Rains Fall à la gare d'Annesburg ; d'après le Red Dead Wiki, le chef sait qu'il a été l'un des compagnons d'Arthur (voir la biographie).")},
]
