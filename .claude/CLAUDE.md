# red-dead-redemption-3.com — Contexte projet

## Hébergement & déploiement

- **VPS** : Hetzner avec cPanel/WHM
- **Username cPanel** : `reddeadredemptio`
- **Deploy path** : `/home/reddeadredemptio/public_html/`
- **Méthode de déploiement** : Git Version Control de cPanel — `.cpanel.yml` à la racine pilote la copie des fichiers
- **Déclencheur de déploiement** : push sur la branche `main` du repo distant connecté dans cPanel, puis "Update from Remote" + "Deploy HEAD Commit"

## Stack technique

- HTML5 / CSS3 / JavaScript vanilla — **pas de framework**, pas de build step
- Pas de Node, pas de npm, pas de bundler — les fichiers servis sont ceux du repo
- Tout doit fonctionner en ouverture directe `file://` localement

## Conventions de développement

### Chemins
- **Chemins relatifs uniquement** : `css/style.css`, jamais `/css/style.css`
- Raison : permet l'ouverture directe en `file://` et la portabilité si déployé en sous-dossier

### Images
- Format **WebP** pour les photos (avec fallback JPEG si besoin)
- **SVG inline** pour les icônes et logos (zéro requête HTTP supplémentaire)
- **Jamais de hotlink** vers des images externes — tout doit être hébergé sur le domaine
- **Alt text obligatoire** sur toutes les balises `<img>` (accessibilité + SEO)
- Toutes les images dans `assets/`

### CSS & JS
- Mobile-first : breakpoints en `min-width`
- Pas de dépendances externes hors fonts Google (à éviter quand possible)
- CSS et JS minifiés à la main si pertinent — pas de build automatique

## Cache-busting

Le `.htaccess` met **CSS et JS en cache navigateur 1 mois**. Sans cache-busting, un visiteur récurrent verra l'ancien CSS/JS pendant 30 jours.

**Règle absolue** : à chaque modification de `css/style.css` ou `js/main.js`, **bumper le query string `?v=AAAAMMJJx`** dans `index.html`, `404.html` et toutes les pages qui les référencent.

- Format : `?v=20260518a` (date du jour + lettre `a`)
- Si plusieurs modifs dans la journée : passer à `b`, `c`, etc.
- Exemple :
  ```html
  <link rel="stylesheet" href="css/style.css?v=20260518a">
  <script src="js/main.js?v=20260518a"></script>
  ```

Oublier de bumper = servir du code périmé pendant 1 mois.

## SEO — règles obligatoires

- **Title** unique et descriptif sur chaque page (< 60 caractères idéalement)
- **Meta description** unique et incitative (< 160 caractères)
- **Open Graph complet** : `og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `og:locale`
- **Schema.org** en JSON-LD quand pertinent (Article, Product, FAQPage, BreadcrumbList…)
- **sitemap.xml** à jour à chaque nouvelle page (lastmod, changefreq, priority)
- **robots.txt** : Allow all + lien vers sitemap
- Un seul `<h1>` par page
- Hiérarchie des titres respectée (`h1` → `h2` → `h3`, sans saut)
- URLs propres (sans `.html` visible si possible — gérer via `.htaccess`)

## Git — règles

- **`main` = production** : tout commit sur `main` est déployable
- **Branches feature** pour les développements : `feat/nom-feature`, `fix/nom-bug`
- **Jamais de push direct sur `main`** sans validation locale (le site est en prod)
- Commits descriptifs en français ou en anglais, mais cohérent dans le projet
- `.gitignore` exclut `.DS_Store`, `node_modules/`, `*.env`, `*.log`, `*.bak`, `*.old`

## Sécurité

- Headers HTTP de sécurité configurés dans `.htaccess` (X-Frame-Options, X-Content-Type-Options, etc.)
- HTTPS forcé, redirection `www` → non-`www`
- Accès bloqué aux fichiers sensibles (`.env`, `.yml`, `.log`, `.git/`, etc.)
- **Jamais de secrets en clair** dans le repo (clés API, mots de passe, tokens)
