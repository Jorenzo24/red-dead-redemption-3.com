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
- Real world: Rockstar's character descriptions of 6 Sep 2018: told in part B (Personality) only. The "American Fathers II" refinery escape in pre-release footage:
  mission page trivia only (no trailer could be dated with a source), attributed.

QUOTES (after the fact-check, FIX_RULES 6): every line quoted in part B (In his own words, Personality, Relationships) was
cut from here; "This will lead to war." and Arthur's "Ah, you, you silly fool." (gsw l. 13249) added. Lines quoted here are
NOT to be repeated in part B. Left to part B on purpose: the wiki's headline line "Father has
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
    {"p": two("The English Red Dead Wiki lists eight missions of Red Dead Redemption 2 for Eagle Flies, from the gang's ride to Horseshoe Overlook in chapter 1 to the battle at the oil fields in chapter 6. The French edition also counts eight, but groups the two parts of \"American Fathers\" under one title and adds \"Archeology for Beginners\", in which he does not appear: his father only talks about him. The second table lists the missions in which he is only mentioned.",
              "Le Red Dead Wiki anglais recense huit missions de Red Dead Redemption 2 pour Eagle Flies, de la chevauchée du gang vers Horseshoe Overlook au chapitre 1 jusqu'à la bataille des champs pétrolifères au chapitre 6. L'édition française en compte huit elle aussi, mais réunit les deux parties d'\"American Fathers\" sous un seul titre et ajoute \"Archeology for Beginners\", où il n'apparaît pas : seul son père parle de lui. Le second tableau rassemble les missions où il est seulement mentionné.")},
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
          "Mission giver. Briefs Arthur on the refinery; an oil well explosion (set off by him, according to the Red Dead Wiki) covers Arthur's escape. Fights his way out with him and pays the 125-dollar reward.",
          "Donneur de mission. Renseigne Arthur sur la raffinerie ; l'explosion d'un puits, qu'il a provoquée selon le Red Dead Wiki, couvre la fuite d'Arthur. S'échappe avec lui sous les balles et lui verse la récompense de 125 dollars."),
        M("A Rage Unleashed", C6,
          "Comes to Beaver Hollow for help recovering the tribe's horses; takes part in the night raid on the Army boat with [[dutch-van-der-linde|Dutch]], Arthur and [[charles-smith|Charles]]; Paytah brings the canoes.",
          "Vient à Beaver Hollow chercher de l'aide pour récupérer les chevaux de la tribu ; participe au raid nocturne sur le bateau de l'armée avec [[dutch-van-der-linde|Dutch]], Arthur et [[charles-smith|Charles]] ; Paytah fournit les canoës."),
        M("Favored Sons", C6,
          "Mission giver. Leads the Wapiti warriors in the ambush on an Army patrol in Cumberland Forest; left behind when the cavalry arrives.",
          "Donneur de mission. Mène les guerriers wapiti dans l'embuscade tendue à une patrouille de l'armée dans Cumberland Forest ; laissé sur place à l'arrivée de la cavalerie."),
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
        {"q": two("This will lead to war.", "This will lead to war."),
         "src": two("American Fathers I (RDR2, chapter 4), when his father says the tribe is to be moved again",
                    "American Fathers I (RDR2, chapitre 4), quand son père annonce que la tribu doit être déplacée une nouvelle fois. Traduction : « Ça mènera à la guerre. »")},
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
        {"q": two("Put your hands up. You're surrounded. Nobody need get hurt. Your humiliation of us has gone on quite enough.", "Put your hands up. You're surrounded. Nobody need get hurt. Your humiliation of us has gone on quite enough."),
         "src": two("Favored Sons (RDR2, chapter 6), to the trapped Army patrol",
                    "Favored Sons (RDR2, chapitre 6), à la patrouille prise au piège. Traduction : « Les mains en l'air. Vous êtes encerclés. Personne n'a besoin d'être blessé. Vous nous avez assez humiliés. »")},
        {"q": two("My father won't be happy about this.", "My father won't be happy about this."),
         "src": two("Favored Sons (RDR2, chapter 6), as the shooting starts",
                    "Favored Sons (RDR2, chapitre 6), au début de la fusillade. Traduction : « Mon père ne va pas être content. »")},
        {"q": two("Mr. Van der Linde! Mr. Morgan! They tried to kill my people for oil. For oil! Today we ride once more. Ride with me, ride with us. Ride with us against the factory.", "Mr. Van der Linde! Mr. Morgan! They tried to kill my people for oil. For oil! Today we ride once more. Ride with me, ride with us. Ride with us against the factory."),
         "src": two("My Last Boy (RDR2, chapter 6), riding into Beaver Hollow with his warriors",
                    "My Last Boy (RDR2, chapitre 6), en arrivant à Beaver Hollow avec ses guerriers. Traduction : « Monsieur Van der Linde ! Monsieur Morgan ! Ils ont voulu tuer mon peuple pour du pétrole. Pour du pétrole ! Aujourd'hui, nous reprenons les armes. Venez avec moi, venez avec nous. Venez avec nous contre l'usine. »")},
        {"q": two("Your words mean nothing to me, Father.", "Your words mean nothing to me, Father."),
         "src": two("My Last Boy (RDR2, chapter 6), to Rains Fall, who begs him not to go",
                    "My Last Boy (RDR2, chapitre 6), à Rains Fall, qui le supplie de renoncer. Traduction : « Tes paroles ne signifient rien pour moi, père. »")},
        {"q": two("You saved my life more than once... to give mine for yours... it's as it should be.", "You saved my life more than once... to give mine for yours... it's as it should be."),
         "src": two("My Last Boy (RDR2, chapter 6), to Arthur, after being shot by Favours",
                    "My Last Boy (RDR2, chapitre 6), à Arthur, après avoir été touché par Favours. Traduction : « Vous m'avez sauvé la vie plus d'une fois. Donner la mienne pour la vôtre, c'est dans l'ordre des choses. »")},
    ]},
    {"h4": two("About Eagle Flies", "À propos d'Eagle Flies")},
    {"quotes": [
        {"q": two("Ah, you, you silly fool.", "Ah, you, you silly fool."),
         "src": two("Arthur to Eagle Flies, after Colonel Favours shoots him, My Last Boy (RDR2, chapter 6)",
                    "Arthur à Eagle Flies, après le tir du colonel Favours, My Last Boy (RDR2, chapitre 6). Traduction : « Ah, espèce d'idiot. »")},
    ]},
]

BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("According to the mission page of \"My Last Boy\", sixteen braves ride into Beaver Hollow with Eagle Flies and Paytah.",
            "D'après la page de la mission \"My Last Boy\", seize guerriers arrivent à Beaver Hollow avec Eagle Flies et Paytah."),
        two("If the player does not shoot Colonel Favours in time, Favours kills Arthur and the mission fails, with the message \"Failed: You have died\" (mission page). According to the wiki's page on Favours, looting the colonel's body after the cutscene makes Eagle Flies die on the spot and fails the mission.",
            "Si le joueur ne tire pas sur le colonel Favours à temps, celui-ci tue Arthur et la mission échoue, avec le message \"Failed: You have died\" (page de la mission). D'après la page du wiki consacrée à Favours, fouiller le corps du colonel après la cinématique fait mourir Eagle Flies sur place et fait échouer la mission."),
        two("The Gold Medal objectives of \"My Last Boy\" include saving Paytah, who struggles with a soldier near a train car after the Gatling gun train arrives.",
            "Parmi les objectifs de médaille d'or de \"My Last Boy\" figure le sauvetage de Paytah, aux prises avec un soldat près d'un wagon après l'arrivée du train à la mitrailleuse Gatling."),
        two("According to the wiki's page on the reservation, Wapiti inhabitants remark on Arthur's presence at first and some tell him to leave, although they never attack him; they greet him once he has done a few missions for Rains Fall and Eagle Flies.",
            "D'après la page du wiki consacrée à la réserve, les Wapiti commencent par s'étonner de la présence d'Arthur, et certains lui disent de partir, sans jamais l'attaquer ; ils le saluent une fois qu'il a accompli quelques missions pour Rains Fall et Eagle Flies."),
    ]},
]

BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("Eagle Flies appears only in Red Dead Redemption 2. The Red Dead Wiki lists no Red Dead Online appearance for him. According to the mission page of \"American Fathers II\", the game's pre-release trailers and promotional videos used the end of that mission: Arthur leaves the office by the window, guards stop him, and an oil well explodes.",
              "Eagle Flies n'apparaît que dans Red Dead Redemption 2. Le Red Dead Wiki ne lui attribue aucune apparition dans Red Dead Online. D'après la page de la mission \"American Fathers II\", les bandes-annonces et vidéos promotionnelles diffusées avant la sortie du jeu reprenaient la fin de cette mission : Arthur quitte le bureau par la fenêtre, des gardes l'arrêtent, puis un puits de pétrole explose.")},
]
