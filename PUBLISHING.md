# Drip-publishing (publication automatique au goutte-à-goutte)

Objectif : écrire des fiches à l'avance, les garder **invisibles**, et en publier
**une par jour** automatiquement, pour envoyer à Google un signal de fraîcheur
régulier sans rien faire à la main.

## Comment ça marche

1. Les fiches prêtes attendent dans **`_queue/NN-<slug>/`** (jamais déployé : `_queue/`
   n'est pas dans `.cpanel.yml`). Les images, elles, sont déjà dans
   `assets/characters/<slug>/` (une image orpheline non liée ne pose aucun souci SEO).
2. Chaque jour à **09:00 UTC**, la GitHub Action `daily-publish.yml` lance
   `scripts/publish_next.py`, qui :
   - prend la prochaine fiche **due** (`publishDate <= aujourd'hui`) ;
   - copie les pages EN + FR dans `characters/<slug>/` et `fr/personnages/<slug>/` ;
   - ajoute la carte aux 2 listings + 2 accueils (au marqueur `<!-- @ccards -->`) ;
   - ajoute les URLs aux sitemaps avec un `lastmod` du jour ;
   - retire la fiche de la file.
3. L'Action **commit + push** le résultat, puis **déclenche le déploiement cPanel**.

S'il n'y a rien de dû ce jour-là, l'Action ne fait rien (aucun commit).

> **Fenêtre de relecture** : comme la file est versionnée, tu peux relire `_queue/`
> à tout moment et corriger une fiche avant son jour de publication.

## Setup unique (≈ 5 min) — à faire une seule fois

### 1. Créer un token API cPanel
cPanel → **Manage API Tokens** → *Create* → nomme-le `github-drip` → copie le token.

### 2. Ajouter 4 secrets GitHub
Repo GitHub → **Settings → Secrets and variables → Actions → New repository secret** :

| Secret | Valeur |
|---|---|
| `CPANEL_HOST` | l'hôte cPanel, ex. `serverXXX.web-hosting.com` (sans `https://`) |
| `CPANEL_USER` | `reddeadredemptio` |
| `CPANEL_TOKEN` | le token créé à l'étape 1 |
| `CPANEL_REPO_ROOT` | le **Repository Path** affiché dans cPanel → *Git Version Control → Manage* (ex. `/home/reddeadredemptio/repositories/red-dead-redemption-3`) |

C'est tout. Dès que les secrets existent, le cycle est 100 % mains libres.

### Vérifier que ça marche
GitHub → onglet **Actions → Daily drip-publish → Run workflow** (déclenchement manuel).
S'il y a une fiche due, elle part en ligne et le déploiement se lance. Sinon : « Nothing to publish today. »

### Si le déploiement auto échoue (mauvais chemin, endpoint cPanel différent…)
Le **commit du jour est quand même poussé** (l'étape deploy est `continue-on-error`).
Filet de sécurité : cPanel → *Git Version Control* → **Update from Remote** → **Deploy HEAD Commit**, comme avant. On ajuste l'endpoint et tout redevient automatique.

## Régler la cadence
Dans `.github/workflows/daily-publish.yml`, la ligne `cron: "0 9 * * *"` = 1×/jour.
- 1 tous les 2 jours : `0 9 */2 * *`
- 3×/semaine (lun/mer/ven) : `0 9 * * 1,3,5`

Comme le script ne publie qu'**une** fiche par exécution et seulement si elle est **due**,
tu pilotes aussi le rythme via les `publishDate` dans `_queue/*/meta.json`.

## Ajouter une fiche à la file (format)
```
_queue/NN-<slug>/
├── meta.json   {"slug","name","role_en","role_fr","publishDate":"YYYY-MM-DD"}
├── en.html     page EN finale (chemins ../../ comme à /characters/<slug>/)
└── fr.html     page FR finale (chemins ../../../ comme à /fr/personnages/<slug>/)
```
+ les images dans `assets/characters/<slug>/` (`portrait.jpeg`, `cover.jpeg`, `gallery-*.jpeg`, `rel/*.jpeg`).
