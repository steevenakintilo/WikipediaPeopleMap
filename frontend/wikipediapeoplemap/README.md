# WikipediaPeopleMap : site public

[🇬🇧 English](#english)

Site React de [WikipediaPeopleMap](https://www.wikipediapeoplemap.com) : carte mondiale des lieux de naissance et de décès des personnes ayant une page Wikipédia, statistiques filtrables, mini-jeux, export pour QGIS. Le site est disponible en **français** et en **anglais**.

Il communique avec l'API Django du dossier [`backend/`](../../backend) (voir le [README principal](../../README.md)).

## Stack

| Domaine | Techno |
|---|---|
| Framework | React 19 + TypeScript, Vite |
| Compilation | **React Compiler** (`babel-plugin-react-compiler` via `@rolldown/plugin-babel`) |
| Données serveur | **TanStack Query** (cache, états de chargement / erreur, devtools) |
| Routing | `react-router-dom` |
| UI | `@steevenakintilo/ui` (design system vendoré dans `vendor/*.tgz`) + Tailwind CSS 4 |
| Cartes | Leaflet / `react-leaflet`, MapLibre GL / `react-map-gl` |
| Graphiques | AG Charts |
| Traduction | `i18next` / `react-i18next` |
| SEO / analytics | `react-helmet-async`, `@vercel/analytics` |
| Lint / tests | oxlint, Playwright |

## Lancer

```bash
npm install
npm run dev          # http://localhost:5173
npm run build        # tsc -b && vite build
npm run preview      # sert le build
npm run lint         # oxlint
```

Tests de parcours utilisateur (Playwright : accessibilité, mobile, résilience) :

```bash
npm run test:ux          # desktop + mobile, backend simulé
npm run test:ux:live     # desktop contre le vrai backend Django (127.0.0.1:8000)
npm run test:ux:report   # rapport HTML
```

### URL du backend

Elle est définie dans [`src/utils/global_variable.tsx`](src/utils/global_variable.tsx) (`backend_url_prod`). En local, pointe-la sur `http://127.0.0.1:8000`, mais **remets l'URL de production avant de commiter** : sinon le site déployé appelle un backend inexistant (erreur `ERR_CONNECTION_REFUSED`). Côté Django, `CORS_ALLOWED_ORIGINS` doit contenir l'origine du front (`http://localhost:5173` en local).

### Déploiement

Le site est déployé sur Vercel ([vercel.json](vercel.json) redirige toutes les routes vers `index.html`). Si le *Root Directory* du projet Vercel n'est pas `frontend/wikipediapeoplemap`, le build échoue ou construit autre chose.

## Organisation (`src/`)

- `api/` : [client.ts](src/api/client.ts) (`api_fetch`, unique point d'appel HTTP, lève `ApiError` si réponse non 2xx), [queries.ts](src/api/queries.ts) (un hook TanStack Query par endpoint), `query_client.ts` (cache).
- `pages/` : une page par route (carte, statistiques, autres statistiques, QGIS, jeux, à propos).
- `components/` : recherche avancée (filtres décrits dans `advanced_search_config.ts`), fiche personne, tableaux, graphiques, signalement d'erreur, layout, sélecteur de langue.
- `i18n/` : traductions (voir ci-dessous).
- `utils/` : constantes (couleurs par genre, listes de pays, libellés des statistiques), thème sombre / clair, helpers.

## Traduction (`src/i18n/`)

Le **texte français du code sert de clé** : on écrit `t("Rechercher")` et [`en.json`](src/i18n/en.json) associe la version anglaise. Le français n'a donc aucun fichier de traduction, et une clé absente de `en.json` s'affiche en français au lieu de planter. La langue choisie est mémorisée (`localStorage`), par défaut celle du navigateur.

Ajouter un texte : l'écrire en français dans le code avec `t("…")`, puis ajouter la ligne dans `en.json`. Pour les textes avec variables : `t("Page {{n}}", { n })` (clé et traduction doivent avoir les mêmes `{{variables}}`).

Les valeurs qui viennent du **backend** (toujours en français) sont traduites à l'affichage :

- `data_names.ts` : pays, continents, régions (insensible à la casse et aux accents : `etats-unis` → *United States*), causes de décès, erreurs de données.
- `jobs.ts` (+ `jobs_data*.ts`) : métiers. Un dictionnaire de métiers complets, plus des règles pour les titres composés (« Président de la République de Pologne », « Écrivain russe », « Ministre danois des Affaires étrangères »…). Un titre dont un mot est inconnu reste en français plutôt que d'être traduit à moitié.

**Recherche par métier en anglais** : le backend cherche en français. Une recherche tapée en anglais (`actor#painter`) est donc convertie en français avant l'envoi (`job_filter_to_french`, appelée dans `api_fetch`). Seuls les noms de métiers entiers du dictionnaire sont reconnus ; un métier inconnu affiche « This job does not exist » et bloque la recherche.

## Licence

Voir [LICENSE](../../LICENSE).

---

<a id="english"></a>

# WikipediaPeopleMap: public site

[🇫🇷 Français](#wikipediapeoplemap--site-public)

React site of [WikipediaPeopleMap](https://www.wikipediapeoplemap.com): world map of the birth and death places of people who have a Wikipedia page, filterable statistics, mini-games, QGIS export. The site is available in **French** and **English**.

It talks to the Django API in the [`backend/`](../../backend) folder (see the [main README](../../README.md)).

## Stack

| Area | Tech |
|---|---|
| Framework | React 19 + TypeScript, Vite |
| Compilation | **React Compiler** (`babel-plugin-react-compiler` via `@rolldown/plugin-babel`) |
| Server data | **TanStack Query** (cache, loading / error states, devtools) |
| Routing | `react-router-dom` |
| UI | `@steevenakintilo/ui` (design system vendored in `vendor/*.tgz`) + Tailwind CSS 4 |
| Maps | Leaflet / `react-leaflet`, MapLibre GL / `react-map-gl` |
| Charts | AG Charts |
| Translation | `i18next` / `react-i18next` |
| SEO / analytics | `react-helmet-async`, `@vercel/analytics` |
| Lint / tests | oxlint, Playwright |

## Run

```bash
npm install
npm run dev          # http://localhost:5173
npm run build        # tsc -b && vite build
npm run preview      # serves the build
npm run lint         # oxlint
```

User-journey tests (Playwright: accessibility, mobile, resilience):

```bash
npm run test:ux          # desktop + mobile, mocked backend
npm run test:ux:live     # desktop against the real Django backend (127.0.0.1:8000)
npm run test:ux:report   # HTML report
```

### Backend URL

It is defined in [`src/utils/global_variable.tsx`](src/utils/global_variable.tsx) (`backend_url_prod`). Locally, point it to `http://127.0.0.1:8000`, but **put the production URL back before committing**: otherwise the deployed site calls a backend that does not exist (`ERR_CONNECTION_REFUSED` error). On the Django side, `CORS_ALLOWED_ORIGINS` must contain the origin of the front (`http://localhost:5173` locally).

### Deployment

The site is deployed on Vercel ([vercel.json](vercel.json) redirects every route to `index.html`). If the Vercel project's *Root Directory* is not `frontend/wikipediapeoplemap`, the build fails or builds something else.

## Organization (`src/`)

- `api/`: [client.ts](src/api/client.ts) (`api_fetch`, the single HTTP call point, throws `ApiError` on a non-2xx response), [queries.ts](src/api/queries.ts) (one TanStack Query hook per endpoint), `query_client.ts` (cache).
- `pages/`: one page per route (map, statistics, other statistics, QGIS, games, about).
- `components/`: advanced search (filters described in `advanced_search_config.ts`), person profile, tables, charts, error report, layout, language selector.
- `i18n/`: translations (see below).
- `utils/`: constants (colors by gender, country lists, statistics labels), dark / light theme, helpers.

## Translation (`src/i18n/`)

The **French text of the code is the key**: you write `t("Rechercher")` and [`en.json`](src/i18n/en.json) maps it to the English version. French therefore has no translation file, and a key missing from `en.json` is displayed in French instead of crashing. The chosen language is remembered (`localStorage`), defaulting to the browser's.

To add a text: write it in French in the code with `t("…")`, then add the line to `en.json`. For texts with variables: `t("Page {{n}}", { n })` (the key and the translation must have the same `{{variables}}`).

Values coming from the **backend** (always in French) are translated at display time:

- `data_names.ts`: countries, continents, regions (case- and accent-insensitive: `etats-unis` → *United States*), causes of death, data errors.
- `jobs.ts` (+ `jobs_data*.ts`): jobs. A dictionary of complete jobs, plus rules for compound titles (“Président de la République de Pologne”, “Écrivain russe”, “Ministre danois des Affaires étrangères”…). A title containing an unknown word stays in French rather than being half translated.

**Searching by job in English**: the backend searches in French. A search typed in English (`actor#painter`) is therefore converted to French before being sent (`job_filter_to_french`, called in `api_fetch`). Only whole job names from the dictionary are recognized; an unknown job shows “This job does not exist” and blocks the search.

## License

See [LICENSE](../../LICENSE).
