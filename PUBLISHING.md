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
3. L'Action **commit + push** le résultat sur `main`.
4. Le **déploiement est fait côté serveur** par un cron cPanel qui fait `git pull`
   dans `public_html` (voir Setup). Le port API de cPanel (2083) étant bloqué par le
   pare-feu pour les serveurs GitHub, on NE déploie PAS depuis l'Action.

S'il n'y a rien de dû ce jour-là, l'Action ne fait rien (aucun commit).

> **Fenêtre de relecture** : comme la file est versionnée, tu peux relire `_queue/`
> à tout moment et corriger une fiche avant son jour de publication.

## Setup unique (≈ 2 min) — le déploiement automatique

Le dépôt cPanel a pour racine `public_html` : un simple `git pull` met donc le site
à jour instantanément. On automatise ça avec un **cron cPanel** (les jetons GitHub
de l'ancienne approche API ne servent plus, le port 2083 étant bloqué côté pare-feu).

cPanel → **Cron Jobs** → ajouter une tâche. Intervalle conseillé : **toutes les 15 min**
(un `git pull` sans changement est quasi gratuit). Commande :

```
cd /home/reddeadredemptio/public_html && git fetch origin main -q && git reset --hard origin/main -q >> /home/reddeadredemptio/deploy.log 2>&1
```

> Si `git` n'est pas trouvé, préfixer par le chemin cPanel :
> `/usr/local/cpanel/3rdparty/bin/git`.

Avantage : ça déploie **tout** automatiquement (les drips quotidiens **et** chaque
merge sur `main`) — plus jamais besoin de cliquer « Deploy HEAD Commit ».

### Déclencher une publication à la demande
GitHub → **Actions → Daily drip-publish → Run workflow** : publie la prochaine fiche
due (commit sur `main`) ; le cron la met en ligne dans les minutes qui suivent.

### Filet de sécurité (déploiement manuel)
À tout moment : cPanel → *Git Version Control* → **Update from Remote** → **Deploy HEAD Commit**.

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
