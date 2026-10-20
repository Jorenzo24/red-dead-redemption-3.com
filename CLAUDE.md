# red-dead-redemption-3.com

> Fichier de mémoire persistante du projet. Claude Code le lit à chaque session.
> Il prime sur les suppositions. En cas de doute, demander — ne pas inventer.

---

## 1. NATURE & STRATÉGIE DU PROJET

Site de contenu autour de l'univers **Red Dead Redemption**, sur le nom de
domaine exact `red-dead-redemption-3.com` (déposé il y a plusieurs années,
antériorité à préserver).

**Contexte clé** : RDR3 n'est PAS annoncé officiellement par Rockstar.
Sortie estimée par les analystes entre ~2030 et 2034 (après GTA VI).
L'horizon de ce projet est donc **long (4 à 8 ans)**. La stratégie n'est
PAS de faire de l'actualité chaude — c'est de **construire de l'autorité de
domaine durable AVANT que le hype démarre**, pour être en position dominante
le jour J.

**Les 3 piliers de contenu :**
1. **Wiki personnages** (moteur SEO principal) — fiches type encyclopédie pour
   les personnages de l'univers RDR (RDR1 + RDR2, sans distinction : ils font
   partie de l'univers que RDR3 prolongera). Contenu evergreen, trafic stable.
2. **Éditorial RDR3** (capte le hype futur) — articles à ANGLE, honnêtes,
   pas de la soupe spéculative recyclée. Positionnement : « ce qu'on sait
   *vraiment* », à l'opposé du contenu vide des gros médias.
3. **Hub lore/chronologie** (liant SEO interne) — relie les fiches entre elles.

**Règle éditoriale anti-soupe** : ne jamais publier de contenu spéculatif vide
(« RDR3 release date » recyclé). Si on parle de RDR3, c'est avec un angle
original et une honnêteté sur ce qui est connu vs supposé. Toujours distinguer
fait confirmé / rumeur / spéculation dans le texte.

---

## 2. STACK TECHNIQUE — « EN DUR » (NON NÉGOCIABLE EN PHASE 1)

- **HTML5 sémantique, CSS vanilla, JS vanilla. ZÉRO framework, ZÉRO build.**
- Pas d'Astro, pas de Next, pas de Strapi, pas de WordPress, pas de npm en prod.
- Le site livré sur cPanel = fichiers statiques purs.
- Hébergement : VPS Hetzner / cPanel. Déploiement Git → cPanel via `.cpanel.yml`.

**Décision actée — migration Astro FUTURE (pas maintenant) :**
Astro sera envisagé PLUS TARD, une fois le gabarit éprouvé sur du contenu réel.
Conséquence impérative : tout ce qu'on écrit en dur doit être **Astro-ready**
(voir §4). C'est la seule contrainte qui ne se rattrape pas après coup.

---

## 3. ARCHITECTURE D'URL & MULTILINGUE (À FIGER DÈS MAINTENANT)

L'architecture multilingue doit être **structurellement en place dès la phase 1**,
même si le contenu démarre en anglais seul. Ne JAMAIS changer les URLs après
indexation (perte d'antériorité = échec de tout le projet).

**Structure d'URL (définitive, ne jamais modifier) :**
- Anglais = racine (marché prioritaire US) : `https://red-dead-redemption-3.com/`
- Autres langues = sous-répertoires : `/fr/`, `/es/`, `/de/`, `/pt-br/` …
- Fiches : `/characters/<slug>/` (ex : `/characters/arthur-morgan/`)
  - Version FR : `/fr/personnages/<slug>/` (slug et segment localisés)
- Articles : `/articles/<slug>/`
- **URLs en répertoire avec slash final, JAMAIS de `.html` dans l'URL publique.**
  (Le fichier physique peut être `index.html` dans le dossier, ou rewrite
  `.htaccess` — l'URL exposée reste propre et stable.)

**Règles hreflang (cause n°1 d'échec des sites multilingues — appliquer à la lettre) :**
- Chaque page liste TOUTES ses variantes linguistiques + se référence elle-même.
- Annotations **réciproques** : si EN pointe vers FR, FR doit pointer vers EN.
- Une balise `x-default` pointant vers la version EN (racine).
- Codes ISO **stricts et valides** : `en`, `fr`, `es`, `de`, `pt-BR`.
  JAMAIS `en-uk` (faux) — c'est `en-gb`. Vérifier chaque code.
- Les variantes de langue **ne se canonicalisent JAMAIS entre elles**.
  Chaque langue = URL canonique distincte (canonical = self).
- Choisir UNE méthode hreflang (balises `<link>` dans le `<head>`) et s'y tenir.
- Sitemaps **séparés par langue** + index de sitemaps.

**Déploiement des langues (par vagues de qualité, pas big-bang) :**
- Phase 1 : EN seul (contenu), infra multilingue en place mais non peuplée.
- Vagues suivantes : FR (qualité garantie par Joseph, natif), puis ES, DE,
  PT-BR — traduction SOIGNÉE avec relecture, jamais de machine brute non revue.
- Tant qu'une langue n'est pas réellement de qualité : pas indexée.
- La traduction n'est pas que linguistique : adapter le vocabulaire de
  recherche réel de chaque marché (pas une trad littérale des mots-clés EN).

---

## 4. CONTRAINTES « ASTRO-READY » (impératif pour la migration future)

Pour que le passage à Astro plus tard soit du quasi copier-coller sans perte SEO :

- **Séparation données / présentation, même en manuel** : chaque fiche et
  chaque article commence par un bloc de métadonnées structuré (front-matter
  YAML en commentaire HTML, ou un `.json` jumeau à côté du `.html`).
  Le contenu ne doit jamais être « collé » au HTML de façon non extractible.
- **HTML découpé en sections sémantiques nettes et répétables** (mêmes classes,
  même ordre, mêmes blocs sur toutes les fiches → futur composant Astro).
- **Aucune logique de présentation en dur non factorisable** : si un élément
  se répète sur toutes les fiches, il doit être identifiable comme « partial ».
- URLs définitives dès maintenant (voir §3) — Astro devra produire EXACTEMENT
  les mêmes URLs.
- Garder un fichier `DATA-SCHEMA.md` documentant la structure de données d'une
  fiche et d'un article (ce sera la spec des content collections Astro).

---

## 5. GABARIT FICHE PERSONNAGE (à stabiliser en phase 2, pas phase 1)

Champs prévus (à affiner en construisant les premières fiches RÉELLES, pas dans
l'abstrait) : nom, slug, alias, jeux d'apparition (RDR1/RDR2), date de
naissance/mort si canon, affiliations (gang Van der Linde, etc.), rôle/statut,
biographie réécrite EN PROPRE (jamais du Fandom/Wikipédia reformulé), liens
internes vers personnages liés, visuel.

- **Schema.org** : type `Person` (+ rattachement à l'univers via `VideoGame`
  / `CreativeWork` selon pertinence). À implémenter sur chaque fiche.
- Bios : contenu **original obligatoire**. Le contenu dérivé plafonne
  l'autorité qu'on cherche justement à construire.

---

## 6. VISUELS — DÉCISION ACTÉE

La gestion des images des personnages est **assurée par Joseph lui-même**
(il fournit / sélectionne / capture). Risque copyright Rockstar/Take-Two
identifié et porté en conscience par Joseph — **ne pas relancer le débat**,
ne pas scraper d'images, ne pas hotlinker. Si une image manque : placeholder
SVG propre avec dimensions + description, en attendant que Joseph la fournisse.

Design fourni par Joseph dans `assets/` : logo, fond de page d'accueil,
typo des titres = **« Chinese Rock »** (prévoir `@font-face`, fallback propre,
et chargement performant — pas de FOIT).

> **PIÈGE Chinese Rock** : les glyphes `«` et `»` sont **mappés mais VIDES** (aucun
> contour). Dans un titre `h1`-`h6` (police `--serif` = Chinese Rock), les guillemets
> français disparaissent en laissant un trou. Invisible dans le HTML, visible seulement
> au rendu. **Ne jamais mettre `« »` dans un titre** : reformuler. Le corps de texte
> (`--sans` système) n'est pas concerné, les `« »` s'y affichent. `"` droits et `“ ” ‘ ’`
> ont de vrais contours et passent en titre.

---

## 7. CONVENTIONS

- Mobile-first responsive.
- Images : WebP prioritaire, fallback JPEG/PNG, `alt` descriptif obligatoire.
- SVG inline pour icônes/illustrations.
- Jamais de hotlink d'images externes.
- Performance = priorité SEO réelle (Core Web Vitals). Pas de JS superflu.
- Title + meta description uniques sur chaque page. Open Graph complet.
- Compression Gzip + cache via `.htaccess` (gérés par skill init-projet).
- Langue du site = **anglais par défaut** (`<html lang="en">` à la racine —
  override le `lang="fr"` du squelette de la skill init-projet).

## 8. DÉPLOIEMENT (cPanel / Hetzner)

- **Username cPanel** : `reddeadredemptio`
- **Deploy path** : `/home/reddeadredemptio/public_html/`
- **Méthode** : `.cpanel.yml` à la racine pilote la copie des fichiers via Git Version Control de cPanel.
- **Déclencheur** : push sur `main` → cPanel > Git Version Control > Update from Remote + Deploy HEAD Commit.

### Cache-busting (NE PAS OUBLIER)

Le `.htaccess` met **CSS et JS en cache navigateur 1 mois**. À chaque modif de
`css/style.css` ou `js/main.js`, **bumper le query string `?v=AAAAMMJJx`** dans
toutes les pages qui les référencent (`index.html`, `404.html`, …).
- Format : `?v=20260518a` (date + lettre `a`, puis `b`, `c` si plusieurs modifs/jour).
- Oublier = servir du code périmé pendant 30 jours aux visiteurs récurrents.

## 9. GIT

- Branche `main` = production. Jamais de push direct sur `main`.
- Branches de feature (`feature/...`) pour toute modif.
- Commits clairs et atomiques.

## 10. ÉTAT D'AVANCEMENT (à tenir à jour par Claude Code)

- [x] Phase 1 : init projet (skill) + design de base + 1-2 articles tests
- [x] Phase 2 : 1 fiche personnage soignée (stabilise le gabarit) — Arthur Morgan (EN+FR)
- [x] Phase 3 : objectif dépassé — **43 fiches en ligne (RDR2 + RDR1) + 7 en file (vague 7)** (EN+FR), **story guides RDR2 ET RDR1 COMPLETS** (RDR2 ch. 1-6 + 2 épilogues ; RDR1 actes I-III), **20 articles**, toujours en dur
- [ ] Phase 4 (futur) : évaluation migration Astro
- [ ] Phase 5 (futur) : déploiement langues par vagues

> Quand une phase avance, cocher ici et noter les décisions structurantes prises.

### Point de reprise (au 5 oct. 2026)

- **Vague 6 entièrement en ligne (43 fiches). La file `_queue/` est VIDE : le site ne publie
  plus rien tant qu'une nouvelle vague n'est pas préparée.**
- Fait le 5 oct. 2026 : les 7 personnages de la vague 6 sont désormais liés depuis les 6 pages
  `/story/rdr1-act-*/` + `/fr/histoire/rdr1-acte-*/` (1re mention + paragraphe récap des
  personnages, pas dans les puces « Key events ») ; « Vicente » corrigé en « Vincente de Santa ».
- **File (au 5 oct. 2026) : 1 article + 7 fiches.** Article « RDR2 Next-Gen Update: What Has
  Actually Been Said in 2026 » le 8 oct. (si Rockstar annonce la version next-gen d'ici là, le
  retirer de la file). Puis vague 7, une fiche tous les 3 jours du 11 au 29 oct. 2026.
- **RENDEZ-VOUS DATÉ, après le 29 oct. 2026** : repasser sur les guides `/story/` (+ FR) des
  chapitres 3, 5 et 6 pour transformer en liens les mentions en texte simple de Catherine
  Braithwaite, Alberto Fussar, Hercule Fontaine, Rains Fall et Eagle Flies (fiches de la vague 7),
  PUIS relancer `python scripts/gen_storystrip.py` pour que leurs réglettes apparaissent.
- **File vide = rien ne publie.** Un drip à vide
  affiche `NOTHING_DUE` sans bruit : c'est passé inaperçu du 27 août au 9 sept. 2026.
  Vérifier `ls _queue/` avant de conclure que tout va bien.
- Pistes de contenu suivantes : arc Wapiti/Guarma (Eagle Flies, Rains Fall, Fussar),
  second rôles RDR2 restants, ou guide Undead Nightmare.

### Décisions structurantes actées
- **Articles : EN primaire + miroir FR** reliés par hreflang réciproque (x-default → EN).
  20 articles publiés (2022 → oct. 2026), index `/articles/` + `/fr/articles/`, fil
  « Latest news » sur la home (max 3 cartes). Slugs localisés par langue. Derniers en date :
  « RDR2 Mexico Mod Nuevo Paraíso » (5 oct. 2026 ; mod fan gratuit, Mexique de RDR1 dans RDR2,
  sorti une semaine après les Mod Guidelines Rockstar du 10 sept. 2026 qui interdisent ce type
  de mod ; images `assets/articles/rdr2-mexico-mod-nuevo-paraiso/`, captures de la page Nexus) ;
  « RDR2 passes 87 million » (résultats Take-Two T1 2027 : 87M unités ; extrapole le budget
  probable de RDR3 en étiquetant fait/estimation/spéculation ; 3e volet de la série ventes
  63M→70M→87M) ; « RDR2 Free DLC for July » (débunk de l'event Red Dead Online présenté à
  tort comme un DLC). Registre factuel + sourcé.
- **Anciennes URLs FR `/fr/blog/` et `/fr/blog-fr/`** → **301** vers `/fr/articles/`
  (antériorité préservée, voir `.htaccess`).
- **Images d'articles/fiches** : sourcing web autorisé par Joseph (il vérifie les
  droits avant publication) — override du §6 « pas de scraping ». Optimisées (≈1600px),
  ratio **4:3** pour vignettes et heros.
- **Thème « média » clair** (`<body class="theme-light">`) sur articles + index + fiches ;
  la home garde le thème western sombre.
- **Fiches personnages (Phase 2)** : gabarit stabilisé = layout « profil » (cover +
  avatar + chips + grille de faits) puis accordéons `<details>` (1er ouvert) ;
  taxonomie figée dans `DATA-SCHEMA.md §3`. Carte d'accueil dédiée `.ccard` (poster,
  distincte des cartes d'articles). Fiche de référence : `characters/arthur-morgan/`.
- **EEAT** : PAS de section « Sources » (liens Wikipedia/Fandom = paraît dérivé des
  concurrents qu'on veut dépasser). À la place : byline **auteur + date « Updated »**
  sur articles ET fiches. Vérifier chaque fait précis (récompense gagnée vs nommée,
  dates, noms) avant publication.
- **Menu header (global)** : `.site-header__menu` avec liens « Characters/Personnages »
  (→ `/characters/` · `/fr/personnages/`) + « Articles » (→ `/articles/` · `/fr/articles/`),
  à côté du sélecteur de langue. État actif `.is-active` + `aria-current="page"` selon
  la section. Présent sur TOUTES les pages indexables (pas sur le 404, minimal volontaire).
  Templates `_templates/` à jour aussi.
- **Pages de listing** : `/characters/` + `/fr/personnages/` (grille `.ccard`),
  `/articles/` + `/fr/articles/`. Reliées par hreflang réciproque, dans les sitemaps.
- **Bas de page** : pas de tags ni bouton Home ; à la place une section de suggestions
  « More articles » (articles) / « More characters » (fiches). Les fiches affichent
  **4 autres personnages + bouton « All characters »** (`.related__head` + `.related__all`)
  vers le listing complet. Grilles de cartes personnages = `.card-grid--portraits`
  (2 par ligne mobile, 4 par ligne desktop) ; les grilles d'articles gardent `.card-grid` (3 max).
- **Relations (fiches)** : liste « cast » illustrée (`.rel` + portrait). Le **nom**
  d'un personnage qui A déjà une fiche est un **lien rouge SANS soulignement**
  (`.rel__body h3 a`, `text-decoration:none`) vers cette fiche ; sinon nom en clair.
  Les liens contextuels dans l'intro/bio restent des liens inline normaux.
  Portraits : artwork officiel ou capture in-game (rendu wiki, API Red Dead Wiki) ;
  à défaut, `assets/characters/placeholder-avatar.svg` (avatar western).
- **Fiches personnages : 43 en ligne (EN + FR) + vague 7 en file (7)**, publiées par vagues via le drip.
  Cadence libre (une `publishDate` par fiche) : vagues 1-3 à 1/jour, vagues 4-5 à ~1 tous les 3 jours.
  - Phase 2 (8) : Arthur, John, Dutch, Micah, Sadie, Hosea, Bill, Charles.
  - Vague 1 (5) : Abigail/Jack Marston, Sean MacGuire, Lenny Summers, Javier Escuella.
  - Vague 2 (6) : Kieran Duffy, Mary Linton, Leopold Strauss, Susan Grimshaw, Colm O'Driscoll, Edgar Ross.
  - Vague 3 (6, drip 9→14 juil. 2026) : Angelo Bronte, Leviticus Cornwall, Andrew Milton, Josiah Trelawny, Molly O'Shea, Uncle.
  - **Vague 4 (6, casting RDR1, 27 juil.→11 août 2026, FAIT)** : Bonnie MacFarlane, Landon Ricketts,
    Nigel West Dickens, Seth Briars, Marshal Leigh Johnson, Abraham Reyes. **Premières fiches RDR1-natives**
    (New Austin / Mexique), groupe « Autres figures ». Faits sourcés (guide GOTY, journaux in-game) :
    5 des 6 survivent à RDR1, seul Landon meurt (vieillesse, rapporté 1914) ; Reyes gagne puis trahit
    sa révolution.
  - **Vague 5 (5, complète le gang, publiée 14→26 août 2026, FAIT)** : Karen Jones, Tilly Jackson,
    Mary-Beth Gaskill, Simon Pearson (cuisinier), Orville Swanson (aumônier). Comble le trou du gang.
    Les 5 survivent à RDR2 (mort de Karen = spéculation de Tilly, jamais un fait) ; fins d'épilogue
    incluses (Mary-Beth romancière « Leslie Dupont », Pearson épicerie de Rhodes, Swanson pasteur à NY).
  - **Vague 6 (7, second rôles RDR1, publiée 15 sept.→3 oct. 2026, FAIT)** : Agustin Allende, Vincente de Santa,
    Luisa Fortuna, Nastas, Harold MacDougal, Irish, Archer Fordham. Exactement les 7 personnages que le
    guide RDR1 cite en texte simple faute de fiche. Prudence factuelle assumée : pas de nom sur le coup
    fatal d'Allende, rien sur le sort de MacDougal après Yale, aucune cause de mort inventée pour Irish.
    Fordham apparaît aussi dans l'épilogue RDR2 (il observe Micah avec Ross). Orthographe wiki =
    « Vincente de Santa » (et non Vicente).
  - Les 7 mentions des guides RDR1 sont devenues des liens internes le 5 oct. 2026 (FAIT).
  - **Vague 7 (7, casting des chapitres RDR2, en file 11→29 oct. 2026)** : Catherine Braithwaite,
    Tavish Gray (ch. 3), Alberto Fussar, Hercule Fontaine (ch. 5), Rains Fall, Eagle Flies (ch. 6),
    Sister Calderón (RDR2 + mère supérieure de Las Hermanas dans RDR1). Ordre de l'histoire pour que
    chaque fiche lie les précédentes. Faits vérifiés par fiche (agents) ; écartés : tireur de Sean,
    meurtrier de Gareth/Gerald, cause de la mort de Tavish (non montrée), prénom/origine de Calderón,
    sort d'Hercule. Fussar EST tué par Arthur au canon ; Eagle Flies meurt dans la réserve (erreur
    corrigée au passage dans le guide ch. 6). `nationality` du schema Person désormais optionnelle
    (`None` = non canon). Driver : `scripts/_wave7.py`.
  - Prochaine cible : arc Wapiti/Guarma (Eagle Flies, Rains Fall, Fussar), ou guide histoire RDR1 Undead
    Nightmare, ou second rôles RDR2 restants.
  Au-delà de 5 persos, « More characters » affiche 4 fiches pertinentes (pas toutes).
- **Titres des fiches (oct. 2026), ton encyclopédique** : `<title>` + og/twitter =
  « Nom: Biography, Story and Relationships » / « Nom : biographie, histoire et relations ».
  **Plus d'étiquette de jeu (RDR1/RDR2) dans le titre** (Joseph, 16 oct. 2026 : abréviations inutiles).
  Pas de suffixe « | Red Dead Redemption 3 ». H1 = nom seul, ligne au-dessus du nom inchangée
  (personnalisée par fiche, choix de Joseph). Généré par `gen_fiche.py`.
- **Réglette « Dans l'histoire » sur les fiches (oct. 2026)** : sous la grille de faits, pastilles
  cliquables vers les chapitres (1-6, É1, É2 pour RDR2 ; I-III pour RDR1). Règle : un chapitre
  apparaît si SON guide lie la fiche. Zone `<!-- @storystrip:start/end -->`, générée par
  `scripts/gen_storystrip.py` (idempotent, à relancer après toute modif des liens des guides).
- **Fiches enrichies (chantier oct. 2026, pilote Molly O'Shea, format v2)** : modèle des articles
  « Good Article » de Wikipédia (Arthur Morgan, John Marston) + règles WP:WAF. Biographie = récit
  CONCIS des seuls événements qui comptent (Origines / rôle / mort ou devenir), PAS de sous-titres
  par chapitre (ça forçait du remplissage) ; le chapitre est cité dans la phrase avec lien vers
  son guide. Section « Conception et interprétation » (monde réel : interprète, audition,
  interviews datées et attribuées, contenu coupé). « Accueil » seulement s'il existe des sources.
  Longueur = importance du perso. Sources : Wikipédia + sources primaires qu'elle cite (interviews,
  guide officiel), JAMAIS paraphrasées ni copiées. Données : `scripts/_enrich.py`, `build_live()`.
  Molly : 266 → 470 mots, erreur corrigée (morte à Beaver Hollow, pas Shady Belle).
  Série 1 (6 oct. 2026) : Karen, Tilly, Mary-Beth, Pearson (≈ 350-450 mots chacune, sections
  Conception sourcées GamesRadar/Fuzzable mars 2019 ; Accueil pour Mary-Beth via Game Informer).
  Série 2 (6 oct.) : Sean, Lenny, Kieran, Swanson. Corrections : Sean tué par une embuscade des Gray
  (pas un chasseur de primes) ; interprète de Lenny = Harron ATKINS (pas « Alexander », erreur
  introduite dans Tilly et corrigée) ; Kieran = Pico Alexander ; Swanson = Sean Haberle ; Bill =
  Steve J. Palmer.
  Série 3 (6 oct.) : Strauss, Trelawny, Susan, Uncle → GANG SECONDAIRE TERMINÉ. Correction : c'est
  Charles (épilogue 1907), pas Dutch, qui annonce la mort de Strauss en détention. Uncle : 3 interprètes
  (Spider Madison RDR1 ; John O'Creagh, mort en production, puis James McBride RDR2).
  Principaux 1 (6 oct.) : Arthur, John, Dutch. Ces fiches de phase 2 étaient écrites À LA MAIN :
  désormais générées via `_enrich.py` (bloc "video" ajouté à gen_fiche pour l'embed Game Awards).
  Correction : les cicatrices de John viennent des loups au ch. 1 (l'ancienne fiche disait l'inverse).
  Reste : principaux (Hosea, Micah, Sadie, Charles, Bill, Javier, Abigail, Jack)
  puis hors-gang (RDR2 et RDR1).
  ATTENTION : ne pas re-publier une fiche enrichie depuis son ancien driver `_waveN.py`.
- **GABARIT COMPLET « référence » (pilote John Marston, 7 oct. 2026, validé dans le principe)** : objectif
  = être la source la plus exhaustive ET la plus fiable (agrégation façon Red Dead Wiki + monde réel façon
  Wikipédia). Ordre : intro, encadré « L'essentiel » (clé `essentials`), faits, puis UN SEUL accordéon « Biographie »
  (h3 = périodes : Origines, RDR2 1899, épilogue 1907, RDR1, Undead Nightmare hors canon ; h4 = chapitres liés
  au guide via la clé `chapter`), puis rubriques indépendantes : Relations, Missions (blocs `table`), Apparence et compétences, Citations (bloc `quotes`, VO +
  « Traduction » en FR), Conception et interprétation, Accueil, Autres médias, Anecdotes.
  Variantes : COMPLÈTE (majeurs), MOYENNE (secondaires à vrai rôle), COURTE (rôles brefs) ; jamais de
  section vide. Données longues dans `scripts/fiches/<slug>.py` (fonction `build(cl, CH)`).
  **v3 (8 oct. 2026, validé par Joseph) : le Red Dead Wiki (Fandom) est la BASE de structure.** On couvre
  TOUT ce qu'il dit de non spéculatif, puis on AJOUTE (Wikipédia, interviews, accueil, sources). Longueur
  ≥ page du wiki. Le contenu de jeu décrit par le wiki (missions, dialogues, tenues, objets) est admis s'il
  n'est pas contredit ; on écarte interprétations, théories, spéculation. Outil : `python scripts/coverage.py
  <slug> <Page_Wiki> [--save DIR]` (compare section par section). Rédaction des fiches majeures répartie
  entre agents selon une spec commune (style, format des blocs, liens), puis assemblage, contre-vérification
  ET contrôle de couverture. À appliquer à TOUTES les fiches, existantes et nouvelles.
  **Protocole de vérification obligatoire** : (1) collecte sourcée par agents (wiki EN+FR + transcriptions
  de missions, Wikipédia + sources primaires, walkthroughs), tags CONFIRMÉ (2 sources indépendantes ou
  texte primaire) / WIKI-ONLY ; (2) seuls les CONFIRMÉS sont affirmés ; (3) CONTRE-VÉRIFICATION par un agent
  indépendant qui relit le brouillon phrase par phrase pour le prendre en défaut ; on corrige TOUT avant
  publication (pilote John : 11 problèmes trouvés, dont 3 erreurs) ; (4) cohérence avec guides et autres
  fiches ; (5) registre des sources en docstring du module.
- **Liens inter-fiches : JAMAIS de lien « vers l'avant ».** Une fiche ne lie (relations + tokens
  inline + cartes « More characters ») que des personnages DÉJÀ en ligne à SA `publishDate` ; le
  sens arrière d'une paire lie (ex. Seth→Nigel, Leigh→Bonnie), le sens avant reste en texte simple.
  Évite tout lien interne en 404 pendant le déroulé d'une vague. Vérif datée avant merge.
- **RÈGLE ÉDITORIALE IMPÉRATIVE — ton média neutre, factuel.**
  1. **PAS de prose « poétique »/d'ambiance qui sonne IA** ni d'analyse à deux sous
     (« c'est comme appeler la météo une annonce »). Bannir conclusions évocatrices
     sans info et tics défensifs (« pas du Fandom reformulé »).
  2. **Une phrase = un fait.** Ne pas être tranché : donner les faits, laisser conclure.
     Événements, missions, noms, dates, recaps scannables.
  3. **Citer sources et chiffres** quand c'est pertinent (média + date d'un titre, post
     Newswire, ventes, dates de sortie) — bon pour le SEO/GEO. Attribution dans le texte,
     PAS de liens sortants vers les sources (cf. règle EEAT anti-Fandom).
  4. **Traductions FR rédigées, jamais littérales.** Le FR est réécrit pour l'usage réel
     de la langue, relu sans l'EN sous les yeux ; bannir les calques (« papier »/« bulletin »
     pour un article/post). Noms de missions/objets du jeu laissés en anglais tels que Rockstar
     les publie. Idem futures langues ES/DE/PT-BR.
  (cf. mémoires feedback.)
- **Story guides RDR2 ET RDR1 — COMPLETS** (`/story/` + `/fr/histoire/`), EN+FR, gabarit article
  `theme-light`. **RDR2 : ch. 1-6 + 2 épilogues** (Colter, Horseshoe Overlook, Clemens Point,
  Saint-Denis, Guarma, Beaver Hollow ; épilogue I Pronghorn Ranch + II Beecher's Hope).
  **RDR1 : actes I-III** (New Austin, Nuevo Paraíso, West Elizabeth), publiés d'un bloc le 9 sept. 2026 ;
  l'acte III couvre la mort de John (1911) ET l'épilogue Jack/Ross (1914), la frise n'ayant que 3 blocs RDR1.
  Format factuel : sections + recap « Key events » à puces + nav prev/next, reliés aux fiches ;
  index `/story/` = frise, **plus aucun placeholder « Soon »** (la nav enchaîne épilogue RDR2 → acte I RDR1).
  **Pages écrites à la main → NE PAS utiliser les tokens `[[slug|Texte]]`** (seul `gen_fiche` les
  convertit) ; mettre des `<a href>` directs. Décisions de contenu notables : RDR2 ch.6 = 4 fins
  (choix × honneur) ; détails wiki non vérifiés écartés ; épilogue RDR2 = mort de Micah en tir partagé
  (Dutch tire, John achève), pas « Dutch tue Micah » ; RDR1 = Dutch se laisse tomber de la falaise
  (pas abattu par John), Javier tué OU capturé à El Presidio (choix du joueur), Allende et Bill tués à Escalera, où Luisa meurt aussi (« An Appointed Time », pas El Presidio).
  Tous les personnages RDR1 cités ont désormais une fiche et sont liés (depuis le 5 oct. 2026).
- **Drip publishing** : `_queue/NN-<slug>/` (meta.json + en.html + fr.html), publié par
  `.github/workflows/daily-publish.yml` → `scripts/publish_next.py` (cron 09:00 UTC ; la plus
  ancienne échéance due). Gère **TROIS types** via `meta.json` "type" : `character` (défaut),
  `article` (carte en tête des index + fil d'accueil, cf. PUBLISHING.md) ET `story` (chapitre : bascule le placeholder « Soon » de la frise en entrée liée, repointe la nav
  du chapitre précédent). **Publication atomique** : tout est calculé/validé AVANT d'écrire ; en
  cas de dérive du markup, échec bruyant sans rien écrire, file rejouable. Images requises AVANT
  publication dans `assets/characters/<slug>/` (fiches) ou `assets/story/<slug>/` (chapitres).
  Générateurs : `scripts/gen_fiche.py` (fiche data→HTML, tokens `[[slug|Texte]]` + relations rouges ;
  byline = `publishDate` de la fiche), drivers `_wave2.py`…`_wave4.py`.
  **Specs images fiche** : portrait **1000×562**, cover **1600×900**, gallery **1400×787**,
  `rel/` **600×337** (JPEG + WebP). Portraits de relation = réutiliser le `portrait.jpeg` déjà en
  ligne du personnage lié (cohérence, zéro sourcing).
  **Portraits depuis les rendus « character bio » RDR2** : ces rendus sont des **diptyques**
  (corps entier + gros plan visage, sur un côté variable selon le perso). NE PAS crop tel quel
  (coupe le visage). Technique : isoler le gros plan visage, puis **visage net centré sur fond flou**
  du même plan pour remplir le 16:9 (cf. vague 5). Sinon, capture in-game 16:9 avec visage net.
- **Page « Personnages » regroupée par faction** (Le gang Van der Linde · La famille Marston ·
  Rivaux et forces de l'ordre · Autres figures), alpha dans chaque groupe. Source unique
  `scripts/characters_registry.py` + `scripts/gen_listing.py` (régénère la zone `@charlist:start/end`,
  **fiches publiées uniquement**). Le drip régénère les 2 pages listing. PAS de lede/blurb sur la page (retiré : sonnait IA).
  Chaque groupe porte une ancre (`#van-der-linde-gang`… / `#gang-van-der-linde`…).
- **Accueil = sections courtes qui renvoient vers les pages dédiées (oct. 2026)** : plus de grille
  de tous les personnages. Section **Personnages** = intro + **4 cartes choisies à la main**
  (Arthur, John, Dutch, Micah, jamais touchées par le drip) + liens par faction avec compteurs
  + bouton « Browse all characters » (sans nombre, choix de Joseph), ces deux derniers générés par `gen_listing` dans la zone
  `<!-- @homechars:start/end -->` (le marqueur `@ccards` n'existe plus). Section **Story/Histoire**
  (fond noir ; c'est Personnages qui porte la bande chaude `.section--alt`, pour trancher avec les actus) = intro + 2 cartes `.arc` (RDR2 1899-1907, RDR1 1911-1914) listant
  chapitres/actes en liens. Nouveau chapitre ou acte = à ajouter à la main dans `.arc__steps`.
- **Sourcing images (pipeline)** : via l'**API MediaWiki du Red Dead Wiki**
  (`reddead.fandom.com/api.php?action=query&generator=images&…`). L'API passe avec un simple UA
  navigateur, mais **depuis sept. 2026 le CDN `static.wikia.nocookie.net` renvoie 403 (Cloudflare)
  sur un UA seul** : il faut AUSSI `-e https://reddead.fandom.com/` (Referer), un en-tête `Accept:
  image/...` et les `Sec-Fetch-Dest/Mode/Site`. Le CDN répond alors en **WebP** quel que soit le nom
  de fichier (Pillow lit, `identify` confirme). Récupérer l'URL exacte via `prop=imageinfo` plutôt que
  de deviner le hash du chemin. Recadrage aux specs ci-dessus ; pour les rendus « bio » verticaux,
  montage **visage net + fond flou** plutôt qu'un crop qui coupe le visage.
  **Vérifier l'image AVANT de l'utiliser** (contact sheet + lecture) : la vague 6 a écarté une carte,
  deux visuels promo à texte incrusté, un intérieur illisible, et a corrigé un cadrage qui prenait Ross
  pour Fordham. `prop=fileusage` dit sur quelle page du wiki une image est utilisée : c'est ce qui a
  confirmé que `Riley_rdr1.png` est bien le portrait de MacDougal.
- **DÉPLOIEMENT = AUTOMATIQUE** : un **cron cPanel** fait `git reset --hard origin/main` dans
  `public_html` **toutes les ~15 min** (voir `PUBLISHING.md`). **Plus besoin de « Deploy HEAD
  Commit »** : un merge sur `main` part en ligne dans le quart d'heure. (Le workflow ne déploie
  PAS lui-même : port cPanel 2083 firewallé depuis GitHub.)
- **Renforcement SEO/perf/EEAT (chantiers faits)** : fil d'Ariane (visuel + `BreadcrumbList`)
  + `Organization`/`WebSite` sur l'accueil ; images **WebP** servies par négociation `.htaccess`
  (fallback JPEG) + `width`/`height` partout (anti-CLS) ; pages **EEAT** `/about/`,
  `/about/joseph-lambert/` (entité auteur, byline reliée), `/contact/` (+ FR) ; **menu =
  Characters/Personnages · Articles · Timeline/Chronologie** + footer nav ; hub
  `/timeline/` + `/fr/chronologie/`. Email contact `contact@red-dead-redemption-3.com`
  (forwarder cPanel à créer).
- **Gabarit complet, ajustements validés par Joseph le 8 oct. 2026 (après lecture de John v3)** :
  (1) **PAS de section « Apparence »** : décrire des tenues en texte sans image n'apporte rien
  (liberté assumée sur l'exhaustivité du wiki) ; les tenues deviennent les **légendes de la galerie**
  (John : 20 images sourcées via l'API du wiki, planche contact vérifiée, visuels à texte/logo écartés).
  (2) **« Personnalité » = court (~450 mots)** : descriptions officielles (Rockstar, guides), traits
  observables, sous-titre « Dans ses propres mots » (répliques VO + trad entre parenthèses en FR),
  surnoms, ce qu'en disent les créateurs. **Jamais une seconde biographie triée par année.**
  (3) **UNE SEULE section « Relations »** (plus de « Relations en détail ») : même composant `.rel`
  (portrait + texte) sur toutes les fiches, texte long sur les fiches complètes (clé `relationships`
  = liste `{img, slug, name, text}` ; `text` peut être une liste de paragraphes). Portraits de relation
  = `portrait.jpeg` du perso redimensionné en 600 px de large. John : 30 entrées, `rel_after = 1`.
  (4) **Bandeau d'année (« year chip »)** sur les longues biographies : clé `"year"` sur un bloc
  h3 → `data-year` (`""` = masquer, ex. Origines et Undead Nightmare) ; les h4 héritent de l'année.
  `js/main.js` `initYearChip()` + CSS `.year-chip` : bandeau FIXE sous le header, **aligné sur la
  colonne de texte** (left/width recalculés en JS), dégradé blanc → transparent, « année · titre du
  chapitre ». Retour Joseph 9 oct. : dans le header ça ressemblait à un menu, dans la marge c'était
  illisible ; il doit être au niveau du contenu. À généraliser si Joseph valide.
- **Blocs de lecture « tabac » sur TOUTES les fiches (14 oct. 2026, validé par Joseph)** : la page garde son fond
  crème ; accordéons, « L'essentiel » et grille de faits passent en brun tabac (#1d1712), texte parchemin, liens
  rouge brique #ee6b55 (contraste 5,8:1 ; l'ambre faisait trop Fandom). Classe `read-dark` sur `<body>`, mise
  par défaut par `gen_fiche` (désactivable par fiche : `"reading_dark": False`). Fil d'Ariane aligné sur la
  colonne qui le suit (`:has(+ .profile)` / `:has(+ .article)`).
- **Arthur Morgan v3 (13 oct. 2026)** : 2e fiche au standard complet, même pipeline que John (6 rédacteurs
  `parts/arthur_A..F.py`, 4 relectures contradictoires ≈ 1 150 affirmations, contrôle de couverture, 4 correcteurs).
  33 350 mots EN (195 % du wiki). 38 relations (avatar de remplacement pour les persos sans fiche, `img: None`),
  galerie 22 images. Le wiki se trompe sur sa page Arthur (Bronte assommé par John, Sadie annonce Sisika, barque
  vers le bateau de l'armée, arme prise au garde à Guarma) : les pages de mission font foi.
  Schema `Person.image` = portrait + toute la galerie (gen_fiche, oct. 2026).
- **Dutch van der Linde v3 (14 oct. 2026)** : 3e fiche complète (4 rédacteurs `parts/dutch_A..D.py`, 3 relectures
  ≈ 900 affirmations, couverture, correcteurs). 21 060 mots EN (181 % du wiki). Module `fiches/dutch_van_der_linde.py`
  avec `build(cl, CH, base)` : la base (méta, Conception, Accueil) reste l'entrée v2 de `_enrich.py`, passée en
  argument. Dutch n'est PAS dans Red Dead Online (fait « Jeux » corrigé). Réplique de Ross, transcription :
  « Oh trust me, it looks better in the report that way » (le wiki dit « on », à tort ; corrigé chez John).
  Coffre de la gare de tramways : 15 dollars et un quart chacun ; le « 90 dollars » de la page Arthur du wiki
  est écarté (retiré d'Arthur). **La spec de rédaction vit désormais dans `scripts/fiches/SPEC.md`** (le scratchpad
  a été purgé une fois). À reprendre : passe de reformulation sur arthur_B/C (tournures encore proches du wiki,
  signalé par la relecture Dutch) ; fiches Nastas/Fordham à revérifier (affirmations sans source).
- **Sadie Adler v3 (15 oct. 2026)** : 4e fiche complète. Sa page de phase 2 était du HTML écrit à la main sans
  données : la base (méta, faits, intro, Conception, Accueil) est reconstruite dans `parts/sadie_D.py` (`BASE`),
  module `fiches/sadie_adler.py` avec `build(cl, CH)`. 13 350 mots EN (315 % du wiki), 26 relations, galerie 15.
  Corrections reportées chez John : UN SEUL télégramme de Sadie, adressé « JIM MILTON », « IF YOURE THE JM I KNOW »
  (pas « ses télégrammes signent JM ») ; Sadie ne « se moque » PAS de l'alias (la page de mission dit qu'ils
  évoquent le passé). Le wiki se trompe sur la page Sadie (« lettre » au lieu de télégramme dans Motherhood).
- **Micah Bell v3 (16 oct. 2026)** : 5e fiche complète (base reconstruite dans `parts/micah_D.py`, même schéma
  que Sadie). 15 100 mots EN (195 % du wiki), 36 relations, galerie 13. Nouveaux faits sourcés : coupure de 1877
  (Micah Bell, 38 ans, et son fils, 17 ans, soupçonnés du meurtre des Briggs, comté de Crawford, Ohio), lettre
  d'Amos, articles de 1907 (Blackwater Ledger n° 75, etc.). Navire de Saint-Denis : nommé (Antenor) sans
  destination (sources divergentes). Leçon : les fiches complètes génèrent beaucoup de DOUBLONS entre Conception,
  Anecdotes, Citations et Relations ; la relecture doit les chercher explicitement (catégorie DUPLICATE).
- **Hosea Matthews v3 (16 oct. 2026)** : 6e fiche complète (base reconstruite, `parts/hosea_D.py`). ~12 000 mots
  EN (≈ 300 % du wiki). Peu de sources réelles (pas d'article Wikipédia sur Curzon Dobell) : Conception courte
  mais sourcée (Bristol Old Vic, mai 2025). Rappels : Milton n'offre PAS de grâce à Clemens Point mais trois jours
  pour fuir ; Davey arrive mort à Colter ; « Horsemen, Apocalypses » précède « Urban Pleasures ».
- **Charles Smith v3 (15 oct. 2026)** : 7e fiche complète (base reconstruite, `parts/charles_D.py`). 12 760 mots
  EN (330 % du wiki), 29 relations, galerie 8. Corrections : au mont Hagen, Charles reste à couvert puis abat
  l'agresseur de Sadie (aussi corrigé dans `john_D.py`) ; c'est Taima, Eagle Flies assis derrière Charles, qui
  sert à la fuite ; Karen et Javier amènent Eagle Flies à Beaver Hollow ; la mort au machete d'un O'Driscoll
  est dans « Horsemen, Apocalypses ». Faits wiki-only attribués dans le texte : nom de ring « Lone Wolf »,
  surnom « Sulky », race Nokota de Falmouth.
- **Bill Williamson v3 (16 oct. 2026)** : 8e fiche complète (base reconstruite, `parts/bill_D.py`). 14 280 mots EN
  (250 % du wiki), 32 relations, galerie 14. Corrections : mort « près d'Escalera » (sur la route, pas dans la
  ville) ; aucune date de naissance canon (1866 écarté, estimation du wiki 1869-1872 attribuée) ; c'est Uncle qui
  évoque le braquage près du Canada ; à « My Last Boy », Bill est avec le groupe de Dutch, pas à l'entrepôt ; à
  Fort Mercer, c'est Jonah qui rapporte la fuite au Mexique. Bill n'est PAS dans Red Dead Online (seule la tenue
  « The Dedham » s'en inspire). Erreur corrigée au passage dans le guide ch. 4 (EN+FR) : John est arrêté à
  Saint-Denis, c'est Micah qui fait naufrage avec Arthur, Dutch, Bill et Javier.
- **Javier Escuella v3 (18 oct. 2026)** : 9e fiche complète (base reconstruite, `parts/javier_D.py` ; l'ancienne
  venait de `_wave1.py`). 13 900 mots EN (245 % du wiki), 33 relations, galerie 13. Sources primaires lues sur image :
  avis de recherche de Shady Belle (« asesinato y traición », Punta Orgullo, 1 000 $) et biographie du guide
  Collector's (il a tué « a high-ranking army officer over a woman »). Sort en 1911 = choix du joueur partout
  (tué ou capturé et livré au Bureau). Erreurs corrigées au passage : guide RDR1 acte 2 (Reyes n'est pas libéré
  à El Presidio lors de la capture de Javier ; Luisa meurt à Escalera dans « An Appointed Time ») ; fiche Luisa
  (même erreur, HTML + `_wave6.py`) ; fiche Arthur (c'est Uncle qui évoque le braquage près du Canada ; Arthur
  évoque seul celui de Tucson).
- **Abigail Marston v3 (19 oct. 2026)** : 10e fiche complète (base reconstruite, `parts/abigail_D.py`). 15 180 mots
  EN (420 % du wiki), 29 relations, galerie 16. Tombe : « Abigail Marston, 1877-1914, Always in our hearts », aucune
  cause de mort. Une fille morte avant 1911 est attestée par John (« Women and Cattle », « Father Abraham »), sans
  plus. Undead Nightmare : guérie par le masque remis en place (« A Civilized Man »), pas par une fontaine.
  Enlèvement 1899 : saisie DEVANT le camp par les hommes de Milton. Erreurs corrigées au passage : fiche Milton
  (tué à Van Horn, pas Beaver Hollow ; HTML + `_wave3.py`), fiche Bonnie (rencontre Abigail chez elle dans « Old
  Friends, New Problems », livraison de maïs ; HTML + `_wave4.py`), Hosea (Abigail a caché l'explosif seule), Micah
  (lieu des avances à Abigail disputé entre wikis, plus de « Clemens Point »).
- **Jack Marston v3 (19 oct. 2026)** : 11e fiche complète, FIN DES PRINCIPAUX DU GANG (base reconstruite,
  `parts/jack_D.py`). 15 300 mots EN (336 % du wiki), 28 relations, galerie 18. Nom crédité (manuel RDR1) : John
  « Jack » Marston Jr. Interprètes : Josh Blaylock (RDR1), Marissa Buccianti (1899) et Ted Sutherland (1907) ;
  Rob Wiethoff fait la capture du duel contre Ross. Jack n'apparaît à l'écran dans RDR1 qu'au retour à Beecher's
  Hope (acte III). Arme de Ross : fusil (rifle) en 1899, fusil de chasse en 1914. Erreur corrigée au passage :
  guide RDR1 acte 3 (1914 : un homme à la gare de Blackwater, Emily à la cabane du lac Don Julio, Phillip à son
  camp au Mexique ; pas « la femme à Blackwater, le frère à Thieves' Landing »).
- **Uncle v3 (19 oct. 2026)** : 12e fiche complète (base reconstruite, `parts/uncle_D.py`, l'entrée v2 d'`_enrich.py`
  est remplacée). 12 500 mots EN (245 % du wiki), 21 relations, galerie 18. Aucun vrai nom (le jeu n'en donne pas).
  Trois interprètes : Spider Madison (RDR1), John O'Creagh (mort le 30 oct. 2016, ses chants restent), James McBride.
  « An Honest Mistake » : Lowe et Cooperforth meurent dans la grange (corrigé aussi chez Charles). Erreurs corrigées
  au passage : guide RDR2 ch. 2 (« Polite Society » = Arthur, Uncle, Karen, Mary-Beth, Tilly ; pas Hosea), guide RDR1
  acte 3 (Uncle repousse la première vague avec John avant d'être touché ; Abigail et Jack sur UN cheval).
  NB : la réglette « Dans l'histoire » est DÉSACTIVÉE (`ENABLED = False` dans `gen_storystrip.py`).
- **Format MOYEN v3 (19 oct. 2026) pour les secondaires du gang** (wiki de 1 300 à 2 900 mots) : mêmes sections et
  règles, 2 rédacteurs (A+C, B+D), 2 relecteurs + couverture, 1 correcteur ; outils dans le scratchpad `cov/`
  (`setup_medium.py`, `galfetch.py`, `galbuild.py`, `mkmodule.py`, `mkrel.py`, `split2.py`). Le navire de Saint-Denis
  n'a JAMAIS de destination (retirée d'Arthur, Charles, Micah).
  - **Sean MacGuire v3** : 7 900 mots EN, 17 relations, galerie 16. Sauvetage = « The First Shall Be Last » (pas « Who
    is Not Without Sin »). Père Darragh : nom sur la coupure de presse en jeu, lien de parenté = wiki. Présent dans Red
    Dead Online (missions Blood Money, 13 juil. 2021).
  - **Lenny Summers v3** : 7 900 mots EN, 17 relations, galerie 14. Arthur l'appelle « Leonard » une fois (« Preaching
    Forgiveness as He Went »). « Fils d'anciens esclaves » = wiki, attribué. Lenny n'a pas rejoint le gang adolescent
    (phrase retirée d'Arthur).
  - **Kieran Duffy v3** : 6 100 mots EN, 20 relations, galerie 11. Capturé au ch. 1 (« Old Friends », corrigé dans le
    guide ch. 3). Pico Alexander : seule la voix est sourcée (pas de « motion capture » affirmée). Aucune description
    Rockstar 2018 pour lui.
  - **Susan Grimshaw v3** : 7 300 mots EN, 23 relations, galerie 8. Molly tuée à la FIN du ch. 5 ; Susan tuée par Micah
    au ch. 6, enterrée par Charles à Roanoke Ridge. Shady Belle nettoyée de Lemoyne Raiders (pas d'O'Driscoll). Selon
    le guide officiel, elle est dans le gang depuis aussi longtemps qu'Arthur (corrigé chez Arthur).
  - **Karen Jones v3** : 6 650 mots EN, 22 relations, galerie 8. Son alcoolisme commence au chapitre de Clemens Point
    (Camp Events), PAS après la mort de Sean. Seul indice d'âge en jeu : « Mid twenties, blonde » (Arthur, Polite Society).
  - **Tilly Jackson v3** : 7 000 mots EN, 21 relations, galerie 7. Elle cache Jack quand les hommes de Milton saisissent
    Abigail DEVANT le camp (pas pendant le raid sur Beaver Hollow). Lettre de 1907 signée « Yours, Tilly » ; elle s'y
    présente comme Tilly Pierre (corrigé chez Hosea et Abigail). Arthur conduit Susan chez les Radley.
  - **Mary-Beth Gaskill v3** : 6 300 mots EN, 17 relations, galerie 8. Rencontre de 1907 à la gare de Valentine (non
    rattachée à une partie précise de l'épilogue). C'est à Karen, pas à Mary-Beth, que Trelawny parle de son livre.
  - **Simon Pearson v3** : 6 700 mots EN, 23 relations, galerie 14. A servi « brièvement » dans la marine (jamais
    « cuisinier de la marine », corrigé chez Dutch). Interprète : Jim Santangeli.
  - **Orville Swanson v3** : 5 850 mots EN, 24 relations, galerie 2 (peu d'images exploitables). Scène de la gare
    d'Emerald SANS transcription : seuls deux répliques attestées et le départ en train ; le reste est retiré.
  - **Leopold Strauss v3** : 6 000 mots EN, 19 relations, galerie 10. Il quitte le gang à Beaver Hollow, chassé par
    Arthur OU de lui-même selon le joueur. Mort en détention Pinkerton entre 1899 et 1907 (rapportée par Charles).
  - **Josiah Trelawny v3** : 6 600 mots EN, 16 relations, galerie 16. Libéré à « The New South » une fois qu'Arthur a
    ramené Anders Anderson (aucune promesse du shérif à l'écran). « He ain't Trelawny » se dit à l'ALLER vers la chasse à
    l'ours (« Exit, Pursued by a Bruised Ego ») ; la réplique sur Sean est optionnelle, comme celles de la pêche. Origine :
    Cornouailles selon ses propres dires à Uncle. Après le ch. 6, on l'entend seulement à son appartement de Saint-Denis.
  - **Molly O'Shea v3** : 5 200 mots EN, 13 relations, galerie 8. Elle PRÉTEND venir d'une famille aisée de Dublin
    (le guide le dit, à attribuer). Gifle de Karen à Clemens Point (camp events ; sa page wiki dit Shady Belle). Dans la
    fin argent honneur bas, « Not Molly… not Miss Grimshaw… not even Colm » vient APRÈS que Dutch arrive et arrête Micah
    (corrigé chez Dutch, Arthur, Susan). Miroir : récompense = un cigare, ch. 3 seulement ; la réplique « aucun ne vivra
    sept ans » n'existe pas (retirée d'Arthur).
- **Hors gang, format MOYEN v3 (20 oct. 2026)** :
  - **Colm O'Driscoll v3** : 5 600 mots EN, 14 relations, galerie 7. Parlementage, capture et évasion d'Arthur = tous
    dans « Blessed are the Peacemakers » (Lone Mule Stead) ; pendaison = « Goodbye, Dear Friend » (ch. 6). Mort du
    frère de Colm : deux versions attribuées (Dutch, transcription : il tue le frère puis Colm tue Annabelle ; page wiki
    « Old Friends » : ordre inverse), racontée UNE fois (relation Dutch). Aucune source ne lie Milton à Colm (« the law »).
    Scène de prononciation Sean/Kieran = Clemens Point. Andrew Berg (capture de mouvement attribuée au wiki).
  - **Edgar Ross v3** : 8 600 mots EN, 19 relations, galerie 11. Prénom et chef du Bureau : journal de 1907 ; Emily :
    journal de 1914 (Blackwater Ledger n° 213) ; Phillip : transcription (« Philip »). « This is your fault, Marston! »
    est de Hopkins, pas de Ross. À Beecher's Hope (1911), Ross apparaît au peloton de la grange, pas en tête de colonne.
    Jack tire le premier. Générique 1907 : Ross et Fordham examinent le corps de Micah. Erreurs corrigées au passage :
    fiche Fordham (présence à Beecher's Hope attribuée au wiki ; légende galerie-1 = 1907, pas 1911 ; HTML + `_wave6.py`).
- **Cache-buster CSS** actuellement à `?v=20261014d` (cf. §8 : bumper à chaque modif CSS ;
  `CSS_V` dans `scripts/gen_fiche.py` doit suivre). JS à `?v=20261009a` (`JS_V` dans `gen_fiche.py`).
