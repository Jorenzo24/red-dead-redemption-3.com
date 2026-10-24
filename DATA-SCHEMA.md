# DATA-SCHEMA.md

> Spec des structures de données du site. Sert deux objectifs :
> 1. Garantir la **cohérence** entre toutes les fiches/articles écrits à la main.
> 2. Servir de **spec future** pour les content collections d'Astro lors de la
>    migration (§4 du CLAUDE.md : « Astro-ready »).
>
> **Règle d'or** : chaque page de contenu (article ou fiche) commence par un bloc
> de métadonnées extractible (front-matter YAML en commentaire HTML), et son HTML
> est découpé en sections sémantiques nettes et **identiques d'une page à l'autre**.
> C'est ce qui permettra le copier-coller vers Astro sans perte.

---

## 1. Conventions communes

- **Encodage** : UTF-8.
- **Langue** : `<html lang="en">` à la racine, `<html lang="fr">` sous `/fr/`, etc.
- **Slug** : minuscules, mots séparés par `-`, ASCII uniquement (transliterer les
  accents). Ex : `arthur-morgan`, `dutch-van-der-linde`.
- **Date** : format ISO `YYYY-MM-DD`.
- **Front-matter** : YAML, placé en commentaire HTML juste après `<!DOCTYPE html>`,
  AVANT toute balise. Format :
  ```html
  <!DOCTYPE html>
  <!--
  ---
  type: article
  slug: protagonist-fans-want-to-see
  lang: en
  title: "The protagonist players actually want to see in RDR3"
  description: "..."
  publishedAt: 2026-05-18
  updatedAt: 2026-05-18
  author: joseph
  tags: [rdr3, editorial, characters]
  hero:
    image: assets/articles/protagonist-fans/hero.webp
    alt: "..."
  hreflang:
    - { lang: en, href: "/articles/protagonist-fans-want-to-see/" }
    # - { lang: fr, href: "/fr/articles/le-protagoniste-attendu/" }  # quand traduit
  ---
  -->
  <html lang="en">
  ```

---

## 2. Article

### URL pattern
- EN : `/articles/<slug>/` (le fichier physique est `articles/<slug>/index.html`)
- FR : `/fr/articles/<slug-fr>/` (slug localisé)

### Front-matter (obligatoire)

| Champ          | Type          | Requis | Notes                                                      |
|----------------|---------------|--------|------------------------------------------------------------|
| `type`         | `"article"`   | oui    | Discriminant pour Astro                                    |
| `slug`         | string        | oui    | Identique au nom du dossier                                |
| `lang`         | enum          | oui    | `en` / `fr` / `es` / `de` / `pt-BR`                        |
| `title`        | string        | oui    | < 60 chars, identique au `<title>` et `<h1>`               |
| `description`  | string        | oui    | < 160 chars, identique à `<meta name="description">`       |
| `publishedAt`  | date ISO      | oui    | Date de première publication                               |
| `updatedAt`    | date ISO      | oui    | Date de dernière modif (alimente `<lastmod>` du sitemap)   |
| `author`       | string        | oui    | Slug auteur (pour l'instant : `joseph`)                    |
| `tags`         | string[]      | oui    | Tags libres (3-6 idéalement)                               |
| `hero.image`   | path          | oui    | Chemin relatif vers l'image hero (WebP de préférence)      |
| `hero.alt`     | string        | oui    | Alt descriptif, jamais vide                                |
| `hreflang`     | array         | oui    | Liste de toutes les versions linguistiques EXISTANTES + soi |

### Structure HTML (sections sémantiques, ordre fixe)

```html
<body>
  <header>...</header>          <!-- partial: site header -->

  <article class="article">
    <header class="article-header">
      <p class="article-eyebrow">[Editorial · RDR3]</p>
      <h1>{{ title }}</h1>
      <p class="article-lede">{{ accroche en 1-2 phrases }}</p>
      <div class="article-meta">
        <time datetime="{{ publishedAt }}">{{ date formatée }}</time>
        <span>·</span>
        <span>{{ author }}</span>
      </div>
    </header>

    <figure class="article-hero">
      <img src="{{ hero.image }}" alt="{{ hero.alt }}" loading="eager">
    </figure>

    <div class="article-body">
      <!-- prose: h2/h3, p, ul/ol, blockquote, figure -->
    </div>

    <aside class="related">              <!-- bas de page : PAS de tags ni Home -->
      <h2 class="related__title">More articles</h2>
      <div class="card-grid">…3 autres articles (.acard)…</div>
    </aside>
  </article>

  <footer>...</footer>          <!-- partial: site footer -->
</body>
```

### Schema.org (JSON-LD obligatoire)
- Type : `Article` (ou `NewsArticle` si actualité chaude — éviter en phase 1).
- Champs : `headline`, `description`, `image`, `datePublished`, `dateModified`,
  `author`, `publisher`, `mainEntityOfPage`, `inLanguage`.

---

## 3. Fiche personnage

> ✅ **Gabarit stabilisé en Phase 2.** Fiche de référence : `characters/arthur-morgan/`
> (+ miroir FR `fr/personnages/arthur-morgan/`). Toute nouvelle fiche DOIT reprendre
> cette structure pour garantir l'harmonie (sections identiques d'une fiche à l'autre).

### URL pattern (figée)
- EN : `/characters/<slug>/`
- FR : `/fr/personnages/<slug>/`

### Front-matter

| Champ           | Type          | Requis | Notes                                                       |
|-----------------|---------------|--------|-------------------------------------------------------------|
| `type`          | `"character"` | oui    |                                                             |
| `slug`          | string        | oui    | Identique au nom du dossier, même slug EN et FR             |
| `lang`          | enum          | oui    | `en` / `fr` / …                                             |
| `title`         | string        | oui    | Nom canonique (« Arthur Morgan »), = `<title>` et `<h1>`    |
| `description`   | string        | oui    | < 160 chars                                                 |
| `games`         | string[]      | oui    | Ex. `["Red Dead Redemption 2", "Red Dead Online"]`          |
| `status`        | enum          | oui    | `alive` / `deceased` / `unknown`                            |
| `born` / `died` | string?       | non    | Canon si connu (ex. `"c. 1863"`, `"1899"`), sinon omis      |
| `affiliation`   | string        | non    | Ex. `Van der Linde gang`                                    |
| `voicedBy`      | string?       | non    | Doubleur / acteur de performance capture                    |
| `author`        | string        | oui    | Slug auteur (`joseph`) — affiché en byline (EEAT)           |
| `updatedAt`     | date ISO      | oui    | Date de mise à jour — affichée « Updated … » (EEAT)         |
| `hero.image`    | path          | oui    | Portrait (infobox)                                          |
| `hero.alt`      | string        | oui    | Alt descriptif                                              |
| `hreflang`      | array         | oui    | Toutes les versions linguistiques existantes + soi          |
| `sections`      | string[]      | oui    | Liste des sections présentes (voir taxonomie ci-dessous)    |

### Taxonomie des sections (fil conducteur, ordre fixe)

Chaque fiche = une **infobox** (toujours visible) + une **intro** (1-2 `<p class="character-intro">`)
+ des **accordéons** `<details class="accordion">` dans cet ordre. On masque simplement
les sections non pertinentes ; on peut en ajouter une au cas par cas si besoin.

1. **Biographie** *(`open` par défaut)* — chronologique : origines → vie → rôle dans les jeux. Sous-titres `<h3>`.
2. **Personnalité**
3. **Relations** — sous-titres `<h3>` par personnage lié
4. **Mort / Destin** *(si applicable)*
5. **Coulisses** — doubleur, performance capture, développement
6. **Accueil & héritage** — réception critique, récompenses, impact culturel
7. **Anecdotes**
8. **Galerie** — `.accordion__gallery` (figures)

> Pas de section « Sources » : on ne cite pas Wikipedia/Fandom (on ne veut pas
> paraître dérivé des sites qu'on cherche à dépasser, cf. §5 « contenu original »).
> L'EEAT passe plutôt par un **auteur** + une **date de mise à jour** visibles
> (ligne `.profile__byline` sous les chips) et l'originalité du texte.

**Comportement accordéons** : le 1er (`Biographie`) est `open`, les autres repliés.
Mécanisme = `<details>`/`<summary>` natif (zéro JS, contenu indexable).

### Structure HTML — layout « profil réseau social » (ordre fixe)

```html
<body class="theme-light">
  <header>…</header>                          <!-- partial: site header + lang-switch -->
  <article class="profile">
    <div class="profile__cover"><img …></div>  <!-- bannière large (défaut: fond-site.jpeg) -->
    <div class="profile__inner">
      <div class="profile__head">
        <img class="profile__avatar" …>         <!-- portrait (chevauche la cover) -->
        <div class="profile__id">
          <p class="profile__eyebrow">Character · …</p>
          <h1 class="profile__name">{{ title }}</h1>
        </div>
      </div>
      <div class="profile__chips"><span class="chip">…</span>…</div>   <!-- faits clés -->
      <p class="profile__byline">By <span>Joseph Lambert</span> · Updated <time>…</time></p>
      <div class="profile__intro"><p>…</p><p>…</p></div>
      <dl class="profile__facts"><div><dt>…</dt><dd>…</dd></div>…</dl>  <!-- grille pleine largeur -->
      <div class="accordions">
        <details class="accordion" open><summary>…</summary><div class="accordion__body">…</div></details>
        …
      </div>
      <aside class="related">…"More characters" : autres fiches (.ccard), omis si aucune…</aside>
    </div>
  </article>
  <footer>…</footer>                          <!-- partial: site footer -->
</body>
```

> ⚠️ Plus de float : le layout profil (cover + avatar + chips + grille de faits)
> remplace l'ancienne `.infobox` flottante (qui laissait des vides quand l'intro
> était courte).

### Carte sur la home (section Characters)
Composant **`.ccard`** (poster vertical 3:4, nom en superposition), **distinct**
des cartes d'articles `.acard` (les personnages sont une partie différente du site) :

```html
<a class="ccard" href="/characters/{{slug}}/">
  <img src="assets/characters/{{slug}}/portrait.jpeg" alt="{{name}}">
  <span class="ccard__overlay">
    <span class="ccard__tag">Character</span>
    <span class="ccard__name">{{name}}</span>
    <span class="ccard__role">{{affiliation}} · {{game}}</span>
    <span class="ccard__cta">View profile →</span>
  </span>
</a>
```

### Schema.org (JSON-LD obligatoire)
- Type : `Person` (personnage fictif), rattaché via `subjectOf` à `VideoGame`
  (`Red Dead Redemption 2`, etc.).
- Champs : `name`, `description`, `image`, `gender`, `nationality`, `birthDate`,
  `deathDate`, `subjectOf`, `mainEntityOfPage`, `inLanguage`.

### Thème
- Fiches en **thème clair « média »** (`<body class="theme-light">`), comme les articles.

---

## 4. Mission

> Pilote : `missions/outlaws-from-the-west/` (+ FR `fr/missions/outlaws-from-the-west/`),
> 24 oct. 2026. Une page par mission principale, générée depuis des données comme les fiches.

### URL pattern (figée)
- EN : `/missions/<slug>/` · FR : `/fr/missions/<slug>/` (segment `missions` identique en FR).
- `slug` = nom EN de la mission « slugifié » (`gen_mission.slugify` : ASCII, minuscules,
  apostrophes supprimées, tout le reste → `-`). Ex. `Who the Hell is Leviticus Cornwall?`
  → `who-the-hell-is-leviticus-cornwall`. Même slug dans toutes les langues (le nom de la
  mission reste en anglais, tel que Rockstar le publie). `build()` refuse un slug ≠ slugify(name).

### Fichiers
- Données : `scripts/missions/<jeu>_<slug_avec_underscores>.py`, qui expose `MISSION` (dict).
  Docstring = registre des sources (ce qui est repris, d'où, et ce qui est écarté).
- Générateur : `scripts/gen_mission.py` (`build(m)` écrit les 2 pages + entrées sitemap EN/FR,
  idempotent). Réutilise `gen_fiche` (header/menu, footer, byline, rendu des blocs, tokens).
- Build : `python3 scripts/build_missions.py [slug ...]` (2 passes pour que les missions d'un
  même lot se lient entre elles ; avec des slugs, reconstruit aussi leurs voisines prev/next).
- Chaque page commence par un front-matter YAML en commentaire (`type: mission`, slug, lang,
  title, game, chapter, number, dates, hreflang, `data:` = module source).

### Dict `MISSION`

Convention : `two(en, fr)` = `{"en": ..., "fr": ...}`. Toute prose accepte les tokens
`[[<slug-perso>|Texte]]` (lien fiche, **seulement si la fiche est en ligne**, sinon texte simple)
et `[[m:<slug-mission>|Texte]]` (lien page mission, **seulement si la page existe**). Le token `m:`
marche aussi dans les fiches (`gen_fiche._links`).

| Champ           | Type              | Requis | Notes |
|-----------------|-------------------|--------|-------|
| `slug`          | string            | oui    | = slugify(`name`) |
| `name`          | string            | oui    | Nom EN officiel = `<h1>` dans toutes les langues (jamais de `« »`) |
| `game`          | `rdr2` / `rdr1`   | oui    | Pilote le libellé du jeu, le `<title>` et `about` (VideoGame) |
| `also_games`    | string[]          | non    | Autres jeux à ajouter à `about` |
| `chapter`       | int / `"E1"` `"E2"` `"A1"`…`"A3"` | oui | Clé de `gen_mission.CHAPTERS` (guide lié, libellés EN/FR) |
| `number`        | int               | oui    | Rang dans le chapitre |
| `chapter_total` | int               | non    | Nb de missions du chapitre (« Mission 1 of 6 ») |
| `story_order`   | int               | non    | Rang dans toute l'histoire du jeu (1 = « première mission du jeu ») |
| `publishDate` / `updated` | date ISO | oui / non | Byline « Updated » = `updated` sinon `publishDate` ; JSON-LD + sitemap |
| `prev` / `next` | `{slug, name}` ou `None` | oui | Fait « Mission précédente/suivante » + nav du bas ; lien seulement si la page existe |
| `meta_desc`     | two               | oui    | Meta description, unique, factuelle |
| `og_desc`       | two               | non    | OG/Twitter (défaut : `meta_desc`) |
| `hero`          | `{src, alt: two, cap: two}` | non | `src` relatif à la racine (`assets/...`), aussi `og:image` |
| `chips`         | two[]             | non    | Chips en plus de Jeu · Chapitre · Mission n sur N |
| `facts`         | dict              | oui    | Clés optionnelles, chacune two : `giver`, `location`, `characters`, `unlocks`, `rewards`. Jeu, Chapitre, Mission (rang), Précédente/Suivante sont générés |
| `intro`         | two[]             | oui    | 2-3 phrases factuelles |
| `sections`      | dict              | oui    | Voir ci-dessous ; une section absente ou vide n'est JAMAIS rendue |
| `reading_dark`  | bool              | non    | Blocs « tabac » (défaut `True`, comme les fiches) |

`sections` (ordre de rendu fixe, accordéons `<details>`, le 1er présent est ouvert) :

| Clé       | EN / FR                                   | Contenu |
|-----------|-------------------------------------------|---------|
| `story`   | Story / Déroulé                           | Liste de blocs fiche (`p`, `h3`, `h4`, `ul`, `quotes`, `table`) ; h3 = étapes de la mission |
| `choices` | Choices and variants / Choix et variantes | Idem (dialogues à choix, issues, variantes, conditions d'échec) |
| `gold`    | Gold Medal objectives / Objectifs de la médaille d'or | `{"objectives": [two..], "caption": two?, "after": [blocs]?}` → table `# / Objectif` avec légende attribuée au Red Dead Wiki |
| `quotes`  | Quotes / Citations                        | `[{"q": "réplique VO", "src": two, "fr": "traduction"}]` → VO dans les deux langues, FR : « src. Traduction : "..." » |
| `trivia`  | Trivia / Anecdotes                        | Liste de two (puces) ou liste de blocs |

Règle des citations (comme sur les fiches, 24 oct. 2026) : **aucune réplique n'est citée deux fois
sur une page**. Une réplique citée dans `story` ou `choices` (et, autant que possible, dans `trivia`)
ne revient PAS dans `quotes` ; on la garde là où elle se lit le mieux (en général le déroulé).
`quotes` ne contient que des répliques verbatim absentes du reste de la page, vérifiées dans la
transcription du wiki (`scripts/v3/work/_m/<Mission>_dialogues.txt`) ou celle du jeu
(`scripts/v3/work/story-ch1/fc/gsw.txt`) ; en cas de divergence entre les deux (mot, locuteur),
on écarte la réplique. Éviter aussi une réplique déjà paraphrasée de près dans le déroulé. Peu de
répliques disponibles = bloc plus court ; liste vide = section non rendue.

Bloc `table` (missions) : `{"table": {"caption": two?, "head": [two..], "rows": [[two|str..]..]}}`
(seul bloc rendu par `gen_mission` lui-même, pour la légende ; le reste passe par `gen_fiche`).

### Structure HTML (ordre fixe)
`body.theme-light.read-dark` → header (menu « Story/Histoire » actif) → fil d'Ariane
Accueil › Histoire › Chapitre N : nom (guide) › Mission → `article.article.mission` :
`header.article-header` (eyebrow « Mission · Red Dead Redemption 2 · Chapter 1 », `h1`,
`.story-meta` chips, byline) → `figure.article-hero` → `.profile__intro` → `dl.profile__facts`
→ `.accordions` → `nav.story-nav` (précédente · toutes les missions du chapitre · suivante ;
`<span>` sans lien tant que la page voisine n'existe pas). Aucune CSS propre aux missions.

### SEO
- `<title>` : « <Mission>: RDR2 Mission Walkthrough and Story » / « <Mission> : mission de RDR2,
  déroulé et histoire » (RDR1 pour `game: rdr1`). og/twitter = même titre.
- JSON-LD `Article` (auteur Joseph Lambert, `datePublished`, `dateModified`, `about` VideoGame)
  + `BreadcrumbList` (4 niveaux). hreflang en/fr/x-default réciproques, canonical = self.
- Sitemaps : `build()` ajoute l'URL EN à `sitemap-en.xml` et l'URL FR à `sitemap-fr.xml`
  (sinon met à jour `lastmod`).

---

## 5. Sitemap

- `sitemap.xml` = **sitemap index** (liste les sitemaps par langue).
- `sitemap-en.xml` = URLs EN (homepage + futurs articles + futures fiches).
- `sitemap-fr.xml` (futur) = URLs FR, créé quand le FR est de qualité indexable.
- Chaque entrée `<url>` inclut les `<xhtml:link rel="alternate" hreflang="...">`
  pour TOUTES les langues existantes + `x-default`.

---

## 6. Évolution de ce document

À chaque fois qu'on stabilise un champ ou qu'on en ajoute un sur une fiche/article
réelle, **mettre ce fichier à jour AVANT** de continuer à écrire d'autres pages.
Sinon les pages divergent et la migration Astro devient un cauchemar.
