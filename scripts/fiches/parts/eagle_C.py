"""Eagle Flies, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (fetched Oct 2026; local copies in scripts/v3/work/eagle/ and scripts/v3/work/_m/):
- Red Dead Wiki EN "Eagle Flies" (Mission appearances, Trivia, Gallery) = work/eagle/en.txt; FR "Aigle-Qui-Vole"
  (Apparitions dans les missions, Anecdotes) = work/eagle/fr.txt.
- Mission pages (infobox chapter, giver, reward, Gold Medal objectives, Mission Failure, Deaths, Trivia): "Eastward Bound",
  "The Gilded Cage", "American Fathers I", "American Fathers II", "A Rage Unleashed", "Archeology for Beginners",
  "The Fine Art of Conversation", "Favored Sons", "The King's Son", "My Last Boy", "Red Dead Redemption (mission)";
  wiki pages "Henry Favours" (trivia: looting his body), "Paytah", "Wapiti Indians", "Wapiti Indian Reservation".
- TRANSCRIPT: Game Scripts Wiki full transcript, work/eagle/fc/gsw.txt (gitignored): every quote below is checked word for
  word against it (American Fathers I+II l. 9536-9656; A Rage Unleashed l. 12212-12295; Favored Sons l. 12850-12931;
  The King's Son l. 12985-13095; My Last Boy l. 13109-13293; Red Dead Redemption l. 13489). Curly apostrophes normalised.
  The American Fathers II exchange also appears as the mission page's quote box (wording without the transcript's ellipses
  inside the first sentence; the transcript wording is used).
- Real world: Rockstar's character descriptions of 6 Sep 2018 (THR, scripts/v3/sources/thr_descriptions.txt) cover the
  gang only, none for Eagle Flies (HOUSE_FACTS 119). The "American Fathers II" refinery escape in pre-release footage:
  mission page trivia only (no trailer could be dated with a source), attributed.

QUOTES: lines quoted here are NOT to be repeated in part B. Left to part B on purpose: the wiki's headline line "Father has
confused wisdom with weakness..." (A Rage Unleashed), which B may quote under "In his own words"; if B does not, the fixer
can move it here. If B quotes any line below, cut it here (FIX_RULES: one place).

TRIVIA kept only for facts told nowhere else in A or C. Excluded:
- The wiki trivia comparing him with Nastas (interpretation) and its claim about "medicine for smallpox" (unsourced).
- The unique American Paint (part B, Skills); the grave west/east of Donner Falls (part A, Epilogue).
- The wiki trivia "sixteen braves" headcount reasoning ("points to an error caused by the developers": speculation); only
  the count of sixteen riders is kept.
- Little Bighorn comparison on "My Last Boy" (wiki: "similarities", interpretation).
- Red Dead Online: the wiki lists no appearance, outfit or item for him; nothing claimed beyond that.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists eight missions of Red Dead Redemption 2 for Eagle Flies, from the gang's ride to Horseshoe Overlook in chapter 1 to the battle at the oil fields in chapter 6. The French edition also counts eight, but groups the two parts of \"American Fathers\" under one title and adds \"Archeology for Beginners\", in which he does not appear: his father only talks about him. He appears in no other game of the series. The second table lists the missions in which he is only mentioned.",
              "Le Red Dead Wiki anglais recense huit missions de Red Dead Redemption 2 pour Eagle Flies, de la chevauchée du gang vers Horseshoe Overlook au chapitre 1 jusqu'à la bataille des champs pétrolifères au chapitre 6. L'édition française en compte huit elle aussi, mais réunit les deux parties d'\"American Fathers\" sous un seul titre et ajoute \"Archeology for Beginners\", où il n'apparaît pas : seul son père parle de lui. Il ne figure dans aucun autre jeu de la série. Le second tableau rassemble les missions où il est seulement mentionné.")},
    {"h4": two("Red Dead Redemption 2: missions with Eagle Flies", "Red Dead Redemption 2 : missions avec Eagle Flies")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Eagle Flies's role", "Rôle d'Eagle Flies")], "rows": [
        M("Eastward Bound", C1,
          "One of three riders watching the gang from a cliff while the wagon wheel is repaired; the wiki names him, [[rains-fall|Rains Fall]] and Paytah.",
          "L'un des trois cavaliers qui observent le gang du haut d'une falaise pendant la réparation de la roue ; le wiki les identifie comme lui, [[rains-fall|Rains Fall]] et Paytah."),
        M("The Gilded Cage", C4,
          "Guest at the mayor's garden party in Saint Denis with his father; [[angelo-bronte|Angelo Bronte]] mocks them from the balcony.",
          "Invité à la garden-party du maire de Saint-Denis avec son père ; [[angelo-bronte|Angelo Bronte]] se moque d'eux depuis le balcon."),
        M("American Fathers I", C4,
          "Met by [[arthur-morgan|Arthur]] outside the courthouse with Rains Fall and Evelyn Miller. A cutscene-only mission.",
          "Rencontre [[arthur-morgan|Arthur]] devant le palais de justice avec Rains Fall et Evelyn Miller. Mission constituée d'une seule cinématique."),
        M("American Fathers II", C4,
          "Mission giver. Briefs Arthur on the refinery, sets off the oil well explosion that covers his escape, fights his way out with him and pays the 125-dollar reward.",
          "Donneur de mission. Renseigne Arthur sur la raffinerie, provoque l'explosion du puits qui couvre sa fuite, s'échappe avec lui sous les balles et lui verse la récompense de 125 dollars."),
        M("A Rage Unleashed", C6,
          "Comes to Beaver Hollow for help recovering the tribe's horses; takes part in the night raid on the Army boat with [[dutch-van-der-linde|Dutch]], Arthur, [[charles-smith|Charles]] and Paytah.",
          "Vient à Beaver Hollow chercher de l'aide pour récupérer les chevaux de la tribu ; participe au raid nocturne sur le bateau de l'armée avec [[dutch-van-der-linde|Dutch]], Arthur, [[charles-smith|Charles]] et Paytah."),
        M("Favored Sons", C6,
          "Leads the Wapiti warriors in the ambush on an Army patrol in Cumberland Forest; left behind when the cavalry arrives.",
          "Mène les guerriers wapiti dans l'embuscade tendue à une patrouille de l'armée dans Cumberland Forest ; laissé sur place à l'arrivée de la cavalerie."),
        M("The King's Son", C6,
          "Prisoner at Fort Wallace, freed by Arthur and Charles; escapes behind Charles on Taima, then by canoe.",
          "Prisonnier à Fort Wallace, libéré par Arthur et Charles ; s'enfuit derrière Charles sur Taima, puis en canoë."),
        M("My Last Boy", C6,
          "Leads the attack on the Cornwall refinery, saves Arthur in the warehouse and is shot by Colonel Favours; dies on the reservation.",
          "Mène l'attaque contre la raffinerie de Cornwall, sauve Arthur dans l'entrepôt et reçoit une balle du colonel Favours ; meurt sur la réserve."),
    ]}},
    {"h4": two("Red Dead Redemption 2: missions where he is mentioned", "Red Dead Redemption 2 : missions où il est mentionné")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Mention", "Mention")], "rows": [
        M("That's Murfree Country", C5,
          "Charles tells Arthur he has met Rains Fall and Eagle Flies and has been helping at the reservation.",
          "Charles raconte à Arthur qu'il a croisé Rains Fall et Eagle Flies et qu'il aide à la réserve."),
        M("Archeology for Beginners", C6,
          "Rains Fall reproaches Arthur for the horse raid with his son. Listed by the French wiki only.",
          "Rains Fall reproche à Arthur le raid des chevaux mené avec son fils. Citée par le wiki français uniquement."),
        M("The Fine Art of Conversation", C6,
          "Rains Fall says his son has too much of a mind of his own; Charles may voice his anger at the arrest.",
          "Rains Fall dit que son fils n'en fait qu'à sa tête ; Charles peut s'emporter contre son arrestation."),
        M("Red Dead Redemption", C6,
          "Arthur names him to [[sadie-adler|Sadie]] among the people Dutch used.",
          "Arthur le cite devant [[sadie-adler|Sadie]] parmi ceux dont Dutch s'est servi."),
    ]}},
]

BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Each is checked against a full transcript of Red Dead Redemption 2. Lines already quoted under Personality and Relationships do not appear again here.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Chacune est vérifiée sur une transcription complète de Red Dead Redemption 2. Les répliques déjà citées dans les rubriques Personnalité et Relations ne sont pas reprises ici.")},
    {"h4": two("Chapter 4", "Chapitre 4")},
    {"quotes": [
        {"q": two("Told you, they're all mercenaries.", "Told you, they're all mercenaries."),
         "src": two("American Fathers I (RDR2, chapter 4), to his father, when Arthur asks how much the job pays",
                    "American Fathers I (RDR2, chapitre 4), à son père, quand Arthur demande combien rapporte le travail. Traduction : « Je te l'avais dit, ce sont tous des mercenaires. »")},
        {"q": two("It's a waste of our time and his.", "It's a waste of our time and his."),
         "src": two("American Fathers I (RDR2, chapter 4), about the appointment with the senator",
                    "American Fathers I (RDR2, chapitre 4), à propos du rendez-vous avec le sénateur. Traduction : « C'est une perte de temps, pour nous comme pour lui. »")},
        {"q": two("If the... files are as incriminating as we believe... Mr. Cornwall's men will destroy them... if they know you're coming.", "If the... files are as incriminating as we believe... Mr. Cornwall's men will destroy them... if they know you're coming."),
         "src": two("American Fathers II (RDR2, chapter 4), to Arthur, above the refinery",
                    "American Fathers II (RDR2, chapitre 4), à Arthur, au-dessus de la raffinerie. Traduction : « Si ces dossiers sont aussi compromettants qu'on le pense, les hommes de M. Cornwall les détruiront s'ils savent que vous arrivez. »")},
        {"q": two("I thought you were gonna enter and leave silently?", "I thought you were gonna enter and leave silently?"),
         "src": two("American Fathers II (RDR2, chapter 4), to Arthur, who reminds him he was not supposed to get involved",
                    "American Fathers II (RDR2, chapitre 4), à Arthur, qui lui rappelle qu'il ne devait pas s'en mêler. Traduction : « Je croyais que vous deviez entrer et ressortir sans bruit ? »")},
        {"q": two("Thank you. I hope... well, I don't know what I hope... but who knows... maybe these will be of some use. Here's your money.", "Thank you. I hope... well, I don't know what I hope... but who knows... maybe these will be of some use. Here's your money."),
         "src": two("American Fathers II (RDR2, chapter 4), to Arthur, taking the papers",
                    "American Fathers II (RDR2, chapitre 4), à Arthur, en prenant les papiers. Traduction : « Merci. J'espère... enfin, je ne sais pas ce que j'espère... mais qui sait, ils serviront peut-être à quelque chose. Voici votre argent. »")},
    ]},
    {"h4": two("Chapter 6", "Chapitre 6")},
    {"quotes": [
        {"q": two("Colonel Favours is a liar and a murderer... his people won't stop until we're all dead. Without horses, we cannot hunt... without hunting... we will starve. This is another act of war.", "Colonel Favours is a liar and a murderer... his people won't stop until we're all dead. Without horses, we cannot hunt... without hunting... we will starve. This is another act of war."),
         "src": two("A Rage Unleashed (RDR2, chapter 6), to Dutch, at Beaver Hollow",
                    "A Rage Unleashed (RDR2, chapitre 6), à Dutch, à Beaver Hollow. Traduction : « Le colonel Favours est un menteur et un assassin, ses hommes ne s'arrêteront pas avant qu'on soit tous morts. Sans chevaux, on ne peut pas chasser, et sans chasse, on mourra de faim. C'est un nouvel acte de guerre. »")},
        {"q": two("Father need not know anything... he'd rather live in ignorance.", "Father need not know anything... he'd rather live in ignorance."),
         "src": two("A Rage Unleashed (RDR2, chapter 6), to Charles, before riding off with Dutch",
                    "A Rage Unleashed (RDR2, chapitre 6), à Charles, avant de partir avec Dutch. Traduction : « Père n'a pas besoin de savoir quoi que ce soit, il préfère vivre dans l'ignorance. »")},
        {"q": two("Put your hands up. You're surrounded. Nobody need get hurt. Your humiliation of us has gone on quite enough.", "Put your hands up. You're surrounded. Nobody need get hurt. Your humiliation of us has gone on quite enough."),
         "src": two("Favored Sons (RDR2, chapter 6), to the trapped Army patrol",
                    "Favored Sons (RDR2, chapitre 6), à la patrouille prise au piège. Traduction : « Les mains en l'air. Vous êtes encerclés. Personne n'a besoin d'être blessé. Vous nous avez assez humiliés. »")},
        {"q": two("My father won't be happy about this.", "My father won't be happy about this."),
         "src": two("Favored Sons (RDR2, chapter 6), as the shooting starts",
                    "Favored Sons (RDR2, chapitre 6), au début de la fusillade. Traduction : « Mon père ne va pas être content. »")},
        {"q": two("Sure... I enjoy being tortured... clears the mind.", "Sure... I enjoy being tortured... clears the mind."),
         "src": two("The King's Son (RDR2, chapter 6), to Arthur, who asks if he is all right after cutting him loose",
                    "The King's Son (RDR2, chapitre 6), à Arthur, qui lui demande s'il va bien après l'avoir détaché. Traduction : « Bien sûr, j'adore qu'on me torture, ça éclaircit les idées. »")},
        {"q": two("They'll pay for this. They'll wish they killed me when they had a chance.", "They'll pay for this. They'll wish they killed me when they had a chance."),
         "src": two("The King's Son (RDR2, chapter 6), in the canoe, to Charles",
                    "The King's Son (RDR2, chapitre 6), dans le canoë, à Charles. Traduction : « Ils vont le payer. Ils regretteront de ne pas m'avoir tué quand ils le pouvaient. »")},
        {"q": two("Where would we go?", "Where would we go?"),
         "src": two("The King's Son (RDR2, chapter 6), to Arthur, who suggests the tribe should run away",
                    "The King's Son (RDR2, chapitre 6), à Arthur, qui suggère que la tribu prenne la fuite. Traduction : « Et où irions-nous ? »")},
        {"q": two("Mr. Van der Linde! Mr. Morgan! They tried to kill my people for oil. For oil! Today we ride once more. Ride with me, ride with us. Ride with us against the factory.", "Mr. Van der Linde! Mr. Morgan! They tried to kill my people for oil. For oil! Today we ride once more. Ride with me, ride with us. Ride with us against the factory."),
         "src": two("My Last Boy (RDR2, chapter 6), riding into Beaver Hollow with his warriors",
                    "My Last Boy (RDR2, chapitre 6), en arrivant à Beaver Hollow avec ses guerriers. Traduction : « Monsieur Van der Linde ! Monsieur Morgan ! Ils ont voulu tuer mon peuple pour du pétrole. Pour du pétrole ! Aujourd'hui, nous reprenons les armes. Venez avec moi, venez avec nous. Venez avec nous contre l'usine. »")},
        {"q": two("Your words mean nothing to me, Father.", "Your words mean nothing to me, Father."),
         "src": two("My Last Boy (RDR2, chapter 6), to Rains Fall, who begs him not to go",
                    "My Last Boy (RDR2, chapitre 6), à Rains Fall, qui le supplie de renoncer. Traduction : « Tes paroles ne signifient rien pour moi, père. »")},
        {"q": two("Any men we see... we must save them.", "Any men we see... we must save them."),
         "src": two("My Last Boy (RDR2, chapter 6), to Arthur and Charles at the oil fields",
                    "My Last Boy (RDR2, chapitre 6), à Arthur et à Charles, aux champs pétrolifères. Traduction : « Tous les hommes qu'on croise, il faut les sauver. »")},
        {"q": two("You saved my life more than once... to give mine for yours... it's as it should be.", "You saved my life more than once... to give mine for yours... it's as it should be."),
         "src": two("My Last Boy (RDR2, chapter 6), to Arthur, after being shot by Favours",
                    "My Last Boy (RDR2, chapitre 6), à Arthur, après avoir été touché par Favours. Traduction : « Vous m'avez sauvé la vie plus d'une fois. Donner la mienne pour la vôtre, c'est dans l'ordre des choses. »")},
        {"q": two("Our men... we must go back for the bodies...", "Our men... we must go back for the bodies..."),
         "src": two("My Last Boy (RDR2, chapter 6), on the ride to the reservation",
                    "My Last Boy (RDR2, chapitre 6), sur la route de la réserve. Traduction : « Nos hommes... il faut retourner chercher les corps... »")},
    ]},
    {"h4": two("About Eagle Flies", "À propos d'Eagle Flies")},
    {"quotes": [
        {"q": two("I know your son, a little. He's very brave... very angry.", "I know your son, a little. He's very brave... very angry."),
         "src": two("Arthur to Rains Fall, The King's Son (RDR2, chapter 6)",
                    "Arthur à Rains Fall, The King's Son (RDR2, chapitre 6). Traduction : « Je connais un peu votre fils. Il est très courageux... et très en colère. »")},
        {"q": two("He saw Eagle Flies burned hot, and he fanned the flames. He's not helping that tribe. He's helping himself.", "He saw Eagle Flies burned hot, and he fanned the flames. He's not helping that tribe. He's helping himself."),
         "src": two("Charles to Arthur, about Dutch, on the ride to Fort Wallace, The King's Son (RDR2, chapter 6)",
                    "Charles à Arthur, à propos de Dutch, en route vers Fort Wallace, The King's Son (RDR2, chapitre 6). Traduction : « Il a vu qu'Eagle Flies brûlait de colère, et il a attisé le feu. Il n'aide pas cette tribu. Il s'aide lui-même. »")},
        {"q": two("Fearless, always has been.", "Fearless, always has been."),
         "src": two("Paytah, when Arthur calls Eagle Flies a brave man, My Last Boy (RDR2, chapter 6)",
                    "Paytah, quand Arthur dit d'Eagle Flies que c'est un homme courageux, My Last Boy (RDR2, chapitre 6). Traduction : « Il n'a jamais eu peur de rien. »")},
        {"q": two("And Eagle Flies. Another angry fool he used, just like he did with the rest of us.", "And Eagle Flies. Another angry fool he used, just like he did with the rest of us."),
         "src": two("Arthur to Sadie, about Dutch, Red Dead Redemption (RDR2, chapter 6)",
                    "Arthur à Sadie, à propos de Dutch, Red Dead Redemption (RDR2, chapitre 6). Traduction : « Et Eagle Flies. Un autre jeune exalté dont il s'est servi, comme il l'a fait avec nous tous. »")},
    ]},
]

BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("In \"American Fathers II\" and \"A Rage Unleashed\", attacking, killing or abandoning Eagle Flies fails the mission, according to the mission pages; in \"American Fathers II\", letting him be killed by the guards also fails it.",
            "Dans \"American Fathers II\" et \"A Rage Unleashed\", attaquer, tuer ou abandonner Eagle Flies fait échouer la mission, selon les pages des missions ; dans \"American Fathers II\", le laisser se faire tuer par les gardes la fait échouer aussi."),
        two("According to the mission page of \"My Last Boy\", sixteen braves ride into Beaver Hollow with Eagle Flies and Paytah.",
            "D'après la page de la mission \"My Last Boy\", seize guerriers arrivent à Beaver Hollow avec Eagle Flies et Paytah."),
        two("In \"My Last Boy\", if Arthur does not pull the soldier off Eagle Flies on the walkway, Sadie does it instead (mission page).",
            "Dans \"My Last Boy\", si Arthur ne débarrasse pas Eagle Flies du soldat qui l'attaque sur la passerelle, Sadie s'en charge (page de la mission)."),
        two("If the player does not shoot Colonel Favours in time, Favours kills Arthur and the mission fails, with the message \"Failed: You have died\" (mission page). According to the wiki's page on Favours, looting the colonel's body after the cutscene makes Eagle Flies die on the spot and fails the mission.",
            "Si le joueur ne tire pas sur le colonel Favours à temps, celui-ci tue Arthur et la mission échoue, avec le message \"Failed: You have died\" (page de la mission). D'après la page du wiki consacrée à Favours, fouiller le corps du colonel après la cinématique fait mourir Eagle Flies sur place et fait échouer la mission."),
        two("The Gold Medal objectives of \"My Last Boy\" include saving Paytah, who struggles with a soldier near a train car after the Gatling gun train arrives.",
            "Parmi les objectifs de médaille d'or de \"My Last Boy\" figure le sauvetage de Paytah, aux prises avec un soldat près d'un wagon après l'arrivée du train à la mitrailleuse Gatling."),
        two("According to the wiki's page on the reservation, Wapiti inhabitants are hostile to Arthur at first, then greet him once he has done a few missions for Rains Fall and Eagle Flies.",
            "D'après la page du wiki consacrée à la réserve, les Wapiti se montrent d'abord hostiles envers Arthur, puis le saluent une fois qu'il a accompli quelques missions pour Rains Fall et Eagle Flies."),
    ]},
]

BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("Eagle Flies appears only in Red Dead Redemption 2. The Red Dead Wiki lists no Red Dead Online appearance for him. Rockstar's character descriptions published on September 6, 2018 cover the members of the Van der Linde gang and include none for him. According to the mission page of \"American Fathers II\", the escape from the refinery, with Arthur climbing out of a window, being held up by guards and saved by an exploding oil well, featured in several pre-release promotional videos and trailers of the game.",
              "Eagle Flies n'apparaît que dans Red Dead Redemption 2. Le Red Dead Wiki ne lui attribue aucune apparition dans Red Dead Online. Les descriptions de personnages publiées par Rockstar le 6 septembre 2018 portent sur les membres de la bande de Van der Linde et ne le concernent pas. D'après la page de la mission \"American Fathers II\", la fuite de la raffinerie, où Arthur sort par une fenêtre, se fait braquer par des gardes puis est sauvé par l'explosion d'un puits de pétrole, figurait dans plusieurs vidéos promotionnelles et bandes-annonces diffusées avant la sortie du jeu.")},
]
