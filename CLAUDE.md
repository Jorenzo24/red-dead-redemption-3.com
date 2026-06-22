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
- [ ] Phase 3 : ~20 fiches + quelques articles, toujours en dur
- [ ] Phase 4 (futur) : évaluation migration Astro
- [ ] Phase 5 (futur) : déploiement langues par vagues

> Quand une phase avance, cocher ici et noter les décisions structurantes prises.

### Décisions structurantes actées
- **Articles : EN primaire + miroir FR** reliés par hreflang réciproque (x-default → EN).
  16 articles publiés (2022 → mi-2026), index `/articles/` + `/fr/articles/`, fil
  « Latest news » sur la home. Slugs localisés par langue.
- **Anciennes URLs FR `/fr/blog/` et `/fr/blog-fr/`** → **301** vers `/fr/articles/`
  (antériorité préservée, voir `.htaccess`).
- **Images d'articles/fiches** : sourcing web autorisé par Joseph (il vérifie les
  droits avant publication) — override du §6 « pas de scraping ». Optimisées (≈1600px),
  ratio **4:3** pour vignettes et heros.
- **Thème « média » clair** (`<body class="theme-light">`) sur articles + index + fiches ;
  la home garde le thème western sombre.
- **Fiches personnages (Phase 2)** : gabarit stabilisé = infobox + intro + accordéons
  `<details>` (1er ouvert), taxonomie de sections figée dans `DATA-SCHEMA.md §3`.
  Fiche de référence : `characters/arthur-morgan/`.
- **Cache-buster CSS** actuellement à `?v=20260622f` (cf. §8 : bumper à chaque modif CSS).
