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

    <footer class="article-footer">
      <ul class="article-tags">...</ul>
    </footer>
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

> ⚠️ **Phase 2** — pas encore stabilisée. Voir CLAUDE.md §5.
> Les champs ci-dessous sont indicatifs, à affiner sur les premières fiches réelles.

### URL pattern (figée)
- EN : `/characters/<slug>/`
- FR : `/fr/personnages/<slug>/`

### Front-matter pressenti (à valider en construisant la première fiche)

| Champ           | Type          | Notes                                          |
|-----------------|---------------|------------------------------------------------|
| `type`          | `"character"` |                                                |
| `slug`          | string        |                                                |
| `lang`          | enum          |                                                |
| `name`          | string        | Nom canonique (« Arthur Morgan »)              |
| `aliases`       | string[]      | Surnoms, pseudonymes                           |
| `appearances`   | enum[]        | `RDR1`, `RDR2`, `RDR_undead_nightmare`, …      |
| `birthYear`     | int?          | Canon si connu, sinon `null`                   |
| `deathYear`     | int?          | Idem                                           |
| `affiliations`  | string[]      | Slugs : `van-der-linde-gang`, `pinkertons`, …  |
| `role`          | string        | `protagonist` / `antagonist` / `supporting`…   |
| `relatedTo`     | string[]      | Slugs d'autres personnages liés                |
| `image`         | path          |                                                |

### Schema.org
- Type : `Person` rattaché via `subjectOf` à `VideoGame` (RDR1/RDR2/RDR3).

---

## 4. Sitemap

- `sitemap.xml` = **sitemap index** (liste les sitemaps par langue).
- `sitemap-en.xml` = URLs EN (homepage + futurs articles + futures fiches).
- `sitemap-fr.xml` (futur) = URLs FR, créé quand le FR est de qualité indexable.
- Chaque entrée `<url>` inclut les `<xhtml:link rel="alternate" hreflang="...">`
  pour TOUTES les langues existantes + `x-default`.

---

## 5. Évolution de ce document

À chaque fois qu'on stabilise un champ ou qu'on en ajoute un sur une fiche/article
réelle, **mettre ce fichier à jour AVANT** de continuer à écrire d'autres pages.
Sinon les pages divergent et la migration Astro devient un cauchemar.
