# WikipediaPeopleMap

[🇬🇧 English](#english)

Carte et statistiques des personnes ayant un article sur Wikipédia (FR) : lieux et dates de naissance et de décès, genre, âge, métier, pays, continent, etc. Le site est en ligne sur <https://www.wikipediapeoplemap.com>.

Le projet est découpé en trois blocs indépendants :

```
WikipediaPeopleMap/
├── src/        Récupération et traitement de la donnée (dump Wikipédia → fichiers)
├── backend/    API Django (PostgreSQL + Redis)
├── frontend/   Sites React (site public + page d'administration)
├── pytest/     Essais de scrapping
```

```
 Dump Wikipédia (.zim)
        │  src/wikidata.py (20 process en parallèle)
        ▼
 user_info_dict*.txt ──merge──► user_info_dict.txt ──import──► PostgreSQL
                                                                   │
                                                  Django (API JSON + cache Redis)
                                                                   │
                                                      React (cartes, stats, jeux)
```

---

## 1. `src/` — Récupération de la donnée

### Fichiers à télécharger (obligatoire)

Les données nécessaires à `src/` ne sont pas versionnées dans le dépôt (trop volumineuses). Avant de lancer quoi que ce soit, il faut récupérer :

1. **Le dump Wikipédia `.zim`** : à télécharger sur <https://dumps.wikimedia.org/kiwix/zim/wikipedia/>. Prendre la version française complète (`wikipedia_fr_all_maxi_*.zim`) et la placer à la racine du projet. Le code attend par défaut `wikipedia_fr_all_maxi_2026-02.zim` : si tu télécharges une autre version, renomme le fichier ou adapte le chemin dans les scripts.
2. **Les fichiers JSON et texte** nécessaires au fonctionnement du code de récupération de données (listes de pages, dictionnaires, classements, etc.) : à télécharger depuis ce dossier Google Drive : <https://drive.google.com/drive/folders/1aG3o0gjXv1Wp0kFa_r2nIE374SkiSDiN?usp=sharing>. Les replacer aux emplacements attendus par les scripts (`src/`, `src/data_files/`).

> Une version de la base de données datant du **08/10/2026** est également présente dans ce dossier Google Drive. Elle permet de lancer le backend avec des données complètes sans refaire toute l'extraction.

### Source

Aucun appel à l'API Wikipédia : tout est lu **hors ligne** depuis un dump Kiwix `wikipedia_fr_all_maxi_2026-02.zim` (non versionné, à la racine), ouvert avec [`libzim`](https://pypi.org/project/libzim/) (`Archive.get_entry_by_title`). Le HTML de chaque article est ensuite parsé avec BeautifulSoup et des regex. Cela évite le rate-limiting et rend le traitement reproductible.

### Pipeline

1. **Liste des pages** : `all_wikipedia_page_fr.txt` liste tous les titres du dump.
2. **Filtre vraie personne** : [check_if_user_is_real.py](src/check_if_user_is_real.py) (classe `WikiSrapping`) trie les pages en `list_of_wikipedia_page_of_real_people.txt` et `list_of_wikipedia_page_of_non_real_people.txt` (personnages fictifs, groupes, etc.).
3. **Extraction par page** : [wikidata.py](src/wikidata.py), classe `WikiPeopleData`. `get_user_information(page_name)` extrait de l'infobox / du texte :
   - nom, prénom (et versions normalisées sans accent via `unidecode`), métier, photo ;
   - date et lieu de naissance / décès, avec gestion des dates avant J.-C. (`convert_before_christ_to_date`) ;
   - âge (`get_age_between_two_date`), vivant ou non ;
   - genre (`get_gender_of_a_person`, déduit du texte de l'article) ;
   - coordonnées de la ville (`get_localisation_of_a_town`), pays (`get_country_of_a_town`), continent, région du monde, période historique ;
   - liens sortants de la page (`get_all_links_of_a_page`), utilisés pour le calcul de popularité.
4. **Parallélisation** : [launch_script.py](src/launch_script.py) lance 20 process `wikidata.py <n>`. Chaque process traite 1/20ᵉ de la liste (`get_all_users_data`) et écrit une ligne par personne (un `dict` Python sérialisé) dans `user_info_dict<n>.txt`.
5. **Fusion et dédoublonnage** : [merge_data_file.py](src/merge_data_file.py) concatène les fichiers en `user_info_dict.txt`.
6. **Statistiques et classement** :
   - `WikiPeopleData.calc_stat()` calcule les statistiques sur les liens entre les pages (pages les plus liées, ayant le plus de liens, le plus d’amis, le plus de traductions, ainsi que la taille des pages) et les enregistre dans `data_files/*.json` ;
   - `data_files/people_dict_power_ranking.json` et `list_of_user_sorted_by_power.txt` : classement par « puissance » (liens entrants, nombre de traductions, taille de page) ;

[global_variable.py](src/global_variable.py) contient les dictionnaires de référence (mois, groupes d'âge, pays → continent, métiers, etc.) et [utility_function.py](src/utility_function.py) les helpers de fichiers (`write_into_file`, `reset_file`, `print_file_content`, `split_list`).

### Lancer

Prérequis : avoir téléchargé le `.zim` et les fichiers du Google Drive (voir [Fichiers à télécharger](#fichiers-à-télécharger-obligatoire)).

```bash
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt

cd src
python launch_script.py        # extraction parallèle (long : plusieurs heures)
python merge_data_file.py      # produit user_info_dict.txt
```

> Les chemins vers le `.zim` sont relatifs à `src/` (`../wikipedia_fr_all_maxi_2026-02.zim`). Certains scripts annexes contiennent encore des chemins absolus Windows à adapter.

---

## 2. `backend/` — API Django

Dossier : `backend/myproject/`. Django 5.2, des vues fonctionnelles qui renvoient du `JsonResponse`, une vue par fichier dans [myapp/views_folder/](backend/myproject/myapp/views_folder/).

> Pour éviter de relancer toute l'extraction, une version de la base de données datant du **08/10/2026** est disponible dans le [dossier Google Drive](https://drive.google.com/drive/folders/1aG3o0gjXv1Wp0kFa_r2nIE374SkiSDiN?usp=sharing).

### Stack

| Rôle | Techno |
|---|---|
| Framework | Django 5.2, gunicorn |
| Base de données | PostgreSQL (`psycopg 3`, SSL requis) en prod, SQLite en local |
| Cache | Redis (`django.core.cache.backends.redis`, TTL 7 jours) |
| Statique | WhiteNoise |
| CORS | `django-cors-headers` (origines whitelistées dans `settings.py`) |
| Anti-abus | `django-ratelimit` par IP |
| Alertes | `discord-webhook` |

### Modèles ([models.py](backend/myproject/myapp/models.py))

- **`WikipediaUser`** : une personne. Champs Wikipédia (`page_name` unique, `page_url`, `picture_url`, nom/prénom + versions standardisées, `job`), naissance (ville, lien, localisation, pays, continent, région, période, date et année/mois/jour), décès (mêmes champs), genre, âge, vivant ou non, score de puissance, nombre de traductions, jeux auxquels la personne peut participer.
- **`WikipediaUserUniqueTown`** : une personne par ville, pour afficher des cartes lisibles sans empiler des milliers de points au même endroit (voir `_select_unique_town_pks` dans `rb.py`).
- **`WikiopediaUserToUpdate`** : file de corrections proposées par les visiteurs (`data_to_update` JSON, `update_level`, compteurs `nb_of_good_report` / `nb_of_bad_report`).

### Endpoints ([myapp/urls.py](backend/myproject/myapp/urls.py))

| Route | Vue | Rôle |
|---|---|---|
| `display_user_info/<username>` | `display_user_info_view` | Fiche d'une personne |
| `display_chunck_of_user_info/<n>/` | `basic_user_view` | Pagination par blocs pour la carte du monde |
| `display_chunck_of_user_info_advanced_search/<n>/` | `advanced_searched_for_user_view` | Idem avec filtres (pays, métier, genre, âge, période…) |
| `display_chunck_of_user_info_advanced_search_qjis` | `qjis_map_view` | Données de la carte « Qjis » |
| `get_advanced_statistics` | `advanced_search_for_statistics_view` | Statistiques agrégées filtrées (rate-limit 15 / 15 min, cache Redis) |
| `get_other_statistics` | `get_other_statistics_view` | Statistiques complémentaires |
| `calc_score_of_all_variable` | `calc_score_of_variable_view` | Classements par variable (pays, métier, ville…) |
| `calc_gender_ratio_of_some_variable` | idem | Ratio homme / femme par variable |
| `create_who_was_born_first_game` | `create_game_view` | Génère une manche du jeu « Qui est le plus âgé ? » |
| `update_user_info_status` (POST) | `update_user` | Signalement d'une erreur par un visiteur (4 / h / IP) |
| `update_user_info` (POST) | `update_user` | Correction d'une fiche, **protégée par l'en-tête `X-Admin-API-Key`** |
| `validate_an_user/<user>` | `update_user` | Valide ou rejette une correction |

### Configuration

Variables d'environnement (fichier `.env`, chargé par `python-dotenv`) :

```
DEBUG=False
PGENGINE=django.db.backends.postgresql
PGNAME=… PGUSER=… PGPASSWORD=… PGHOST=… PGPORT=5432
REDIS_URL=redis://…
ADMIN_API_KEY=…
```

`RUN_BACKEND_PROD` dans [settings.py](backend/myproject/myproject/settings.py) bascule entre PostgreSQL (prod) et SQLite (`db.sqlite3`, local). Attention : `CACHES` exige toujours `REDIS_URL`.

### Lancer

```bash
cd backend/myproject
pip install -r requirements.txt
python manage.py migrate        # ou update_db.bat (makemigrations + migrate)
python manage.py runserver      # http://127.0.0.1:8000
# prod
gunicorn myproject.wsgi
```

---

## 3. `frontend/` — Interface React

Monorepo npm avec deux applications Vite.

### Site public : `frontend/wikipediapeoplemap/`

| Domaine | Techno |
|---|---|
| Framework | React 19 + TypeScript 6, Vite 8 |
| Compilation | **React Compiler** (`babel-plugin-react-compiler` via `@rolldown/plugin-babel`) |
| Données serveur | **TanStack Query** (cache, états de chargement / erreur, devtools) |
| Routing | `react-router-dom` 7 |
| UI | `@steevenakintilo/ui` (design system classique, package vendoré dans `vendor/*.tgz`) + Tailwind CSS 4 |
| Cartes | Leaflet / `react-leaflet`, MapLibre GL / `react-map-gl` |
| Graphiques | AG Charts |
| Traduction | `i18next` / `react-i18next` (français et anglais) |
| SEO / analytics | `react-helmet-async`, `@vercel/analytics` |
| Lint | oxlint |

**Organisation** ([src/](frontend/wikipediapeoplemap/src/)) :

- `api/` : [client.ts](frontend/wikipediapeoplemap/src/api/client.ts) (`api_fetch`, unique point d'appel HTTP, lève `ApiError` si réponse non 2xx), [queries.ts](frontend/wikipediapeoplemap/src/api/queries.ts) (hooks TanStack Query, un par endpoint), `query_client.ts` (configuration du cache).
- `pages/` : une page par route.
- `components/` : recherche avancée (filtres décrits dans `advanced_search_config.ts`), fiche personne (`user_profile_dialog`), tableaux, graphiques, signalement d'erreur (`report_dialog`), layout.
- `i18n/` : traductions. Le texte français du code sert de clé et [en.json](frontend/wikipediapeoplemap/src/i18n/en.json) donne la version anglaise ; `data_names.ts` et `jobs.ts` traduisent les valeurs venant du backend (pays, causes de décès, métiers…), et une recherche de métier tapée en anglais est reconvertie en français avant l'envoi.
- `utils/` : constantes (couleurs par genre, listes de pays), thème sombre / clair, helpers.

**Routes** :

| URL | Page |
|---|---|
| `/`, `/Home` | Accueil |
| `/WorldMap` | Carte mondiale des naissances / décès avec recherche avancée |
| `/Statistics` | Statistiques filtrables |
| `/OtherStatistics` | Statistiques complémentaires |
| `/Qjis` | Carte pour Qjis |
| `/WikiGames`, `/WhoIsOlder` | Mini-jeux |
| `/About` | À propos |

Les données de la carte sont chargées **par blocs** (`chunk_nb`) pour afficher rapidement les premiers résultats.

L'URL du backend est définie dans [global_variable.tsx](frontend/wikipediapeoplemap/src/utils/global_variable.tsx) (`backend_url_prod`).

```bash
cd frontend
npm install
cd wikipediapeoplemap
npm run dev          # http://localhost:5173
npm run build        # tsc -b && vite build
npm run lint
```

### Page d'administration : `frontend/admin/`

Page permettant de modifier les informations d'un `WikipediaUser`. L'accès est protégé par une clé API (`X-Admin-API-Key`).
```
VITE_BACKEND_URL=http://127.0.0.1:8000
VITE_ADMIN_API_KEY=…
```

---

## Licence

Voir [LICENSE](LICENSE).


---

<a id="english"></a>

# WikipediaPeopleMap (English)

[🇫🇷 Français](#wikipediapeoplemap)

Map and statistics of people who have an article on (French) Wikipedia: places and dates of birth and death, gender, age, job, country, continent, etc. The site is online at <https://www.wikipediapeoplemap.com>.

The project is split into three independent blocks:

```
WikipediaPeopleMap/
├── src/        Data retrieval and processing (Wikipedia dump → files)
├── backend/    Django API (PostgreSQL + Redis)
├── frontend/   React sites (public site + admin page)
├── pytest/     Scraping experiments
```

```
 Wikipedia dump (.zim)
        │  src/wikidata.py (20 parallel processes)
        ▼
 user_info_dict*.txt ──merge──► user_info_dict.txt ──import──► PostgreSQL
                                                                   │
                                                  Django (JSON API + Redis cache)
                                                                   │
                                                      React (maps, stats, games)
```

---

## 1. `src/` — Data retrieval

### Files to download (required)

The data needed by `src/` is not versioned in the repository (too large). Before running anything, you need to get:

1. **The Wikipedia `.zim` dump**: download it from <https://dumps.wikimedia.org/kiwix/zim/wikipedia/>. Take the full French version (`wikipedia_fr_all_maxi_*.zim`) and put it at the root of the project. By default the code expects `wikipedia_fr_all_maxi_2026-02.zim`: if you download another version, rename the file or adapt the path in the scripts.
2. **The JSON and text files** needed by the data retrieval code (page lists, dictionaries, rankings, etc.): download them from this Google Drive folder: <https://drive.google.com/drive/folders/1aG3o0gjXv1Wp0kFa_r2nIE374SkiSDiN?usp=sharing>. Put them back where the scripts expect them (`src/`, `src/data_files/`).

> A version of the database dated **08/10/2026** is also available in this Google Drive folder. It lets you run the backend with complete data without redoing the whole extraction.

### Source

No call to the Wikipedia API: everything is read **offline** from a Kiwix dump `wikipedia_fr_all_maxi_2026-02.zim` (not versioned, at the root), opened with [`libzim`](https://pypi.org/project/libzim/) (`Archive.get_entry_by_title`). The HTML of each article is then parsed with BeautifulSoup and regexes. This avoids rate limiting and makes the processing reproducible.

### Pipeline

1. **Page list**: `all_wikipedia_page_fr.txt` lists all the titles of the dump.
2. **Real person filter**: [check_if_user_is_real.py](src/check_if_user_is_real.py) (class `WikiSrapping`) sorts the pages into `list_of_wikipedia_page_of_real_people.txt` and `list_of_wikipedia_page_of_non_real_people.txt` (fictional characters, groups, etc.).
3. **Per-page extraction**: [wikidata.py](src/wikidata.py), class `WikiPeopleData`. `get_user_information(page_name)` extracts from the infobox / the text:
   - first name, last name (and normalized versions without accents via `unidecode`), job, photo;
   - date and place of birth / death, with handling of dates before Christ (`convert_before_christ_to_date`);
   - age (`get_age_between_two_date`), alive or not;
   - gender (`get_gender_of_a_person`, deduced from the text of the article);
   - coordinates of the town (`get_localisation_of_a_town`), country (`get_country_of_a_town`), continent, world region, historical period;
   - outgoing links of the page (`get_all_links_of_a_page`), used to compute popularity.
4. **Parallelization**: [launch_script.py](src/launch_script.py) launches 20 `wikidata.py <n>` processes. Each process handles 1/20th of the list (`get_all_users_data`) and writes one line per person (a serialized Python `dict`) into `user_info_dict<n>.txt`.
5. **Merge and deduplication**: [merge_data_file.py](src/merge_data_file.py) concatenates the files into `user_info_dict.txt`.
6. **Statistics and ranking**:
   - `WikiPeopleData.calc_stat()` computes statistics on the links between pages (most linked pages, pages with the most links, the most friends, the most translations, as well as page size) and saves them in `data_files/*.json`;
   - `data_files/people_dict_power_ranking.json` and `list_of_user_sorted_by_power.txt`: ranking by “power” (incoming links, number of translations, page size);

[global_variable.py](src/global_variable.py) contains the reference dictionaries (months, age groups, country → continent, jobs, etc.) and [utility_function.py](src/utility_function.py) the file helpers (`write_into_file`, `reset_file`, `print_file_content`, `split_list`).

### Run

Prerequisites: have downloaded the `.zim` and the Google Drive files (see [Files to download](#files-to-download-required)).

```bash
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt

cd src
python launch_script.py        # parallel extraction (long: several hours)
python merge_data_file.py      # produces user_info_dict.txt
```

> The paths to the `.zim` are relative to `src/` (`../wikipedia_fr_all_maxi_2026-02.zim`). Some side scripts still contain absolute Windows paths to adapt.

---

## 2. `backend/` — Django API

Folder: `backend/myproject/`. Django 5.2, function-based views returning `JsonResponse`, one view per file in [myapp/views_folder/](backend/myproject/myapp/views_folder/).

> To avoid rerunning the whole extraction, a version of the database dated **08/10/2026** is available in the [Google Drive folder](https://drive.google.com/drive/folders/1aG3o0gjXv1Wp0kFa_r2nIE374SkiSDiN?usp=sharing).

### Stack

| Role | Tech |
|---|---|
| Framework | Django 5.2, gunicorn |
| Database | PostgreSQL (`psycopg 3`, SSL required) in prod, SQLite locally |
| Cache | Redis (`django.core.cache.backends.redis`, 7-day TTL) |
| Static files | WhiteNoise |
| CORS | `django-cors-headers` (origins whitelisted in `settings.py`) |
| Anti-abuse | `django-ratelimit` per IP |
| Alerts | `discord-webhook` |

### Models ([models.py](backend/myproject/myapp/models.py))

- **`WikipediaUser`**: one person. Wikipedia fields (unique `page_name`, `page_url`, `picture_url`, first/last name + standardized versions, `job`), birth (town, link, location, country, continent, region, period, date and year/month/day), death (same fields), gender, age, alive or not, power score, number of translations, games the person can take part in.
- **`WikipediaUserUniqueTown`**: one person per town, to display readable maps without stacking thousands of points in the same place (see `_select_unique_town_pks` in `rb.py`).
- **`WikiopediaUserToUpdate`**: queue of corrections suggested by visitors (`data_to_update` JSON, `update_level`, counters `nb_of_good_report` / `nb_of_bad_report`).

### Endpoints ([myapp/urls.py](backend/myproject/myapp/urls.py))

| Route | View | Role |
|---|---|---|
| `display_user_info/<username>` | `display_user_info_view` | A person's profile |
| `display_chunck_of_user_info/<n>/` | `basic_user_view` | Paginated blocks for the world map |
| `display_chunck_of_user_info_advanced_search/<n>/` | `advanced_searched_for_user_view` | Same with filters (country, job, gender, age, period…) |
| `display_chunck_of_user_info_advanced_search_qjis` | `qjis_map_view` | Data for the “Qjis” map |
| `get_advanced_statistics` | `advanced_search_for_statistics_view` | Filtered aggregated statistics (rate limit 15 / 15 min, Redis cache) |
| `get_other_statistics` | `get_other_statistics_view` | Additional statistics |
| `calc_score_of_all_variable` | `calc_score_of_variable_view` | Rankings by variable (country, job, town…) |
| `calc_gender_ratio_of_some_variable` | same | Male / female ratio by variable |
| `create_who_was_born_first_game` | `create_game_view` | Generates a round of the “Who is the oldest?” game |
| `update_user_info_status` (POST) | `update_user` | A visitor reports an error (4 / h / IP) |
| `update_user_info` (POST) | `update_user` | Correction of a profile, **protected by the `X-Admin-API-Key` header** |
| `validate_an_user/<user>` | `update_user` | Validates or rejects a correction |

### Configuration

Environment variables (`.env` file, loaded by `python-dotenv`):

```
DEBUG=False
PGENGINE=django.db.backends.postgresql
PGNAME=… PGUSER=… PGPASSWORD=… PGHOST=… PGPORT=5432
REDIS_URL=redis://…
ADMIN_API_KEY=…
```

`RUN_BACKEND_PROD` in [settings.py](backend/myproject/myproject/settings.py) switches between PostgreSQL (prod) and SQLite (`db.sqlite3`, local). Note: `CACHES` always requires `REDIS_URL`.

### Run

```bash
cd backend/myproject
pip install -r requirements.txt
python manage.py migrate        # or update_db.bat (makemigrations + migrate)
python manage.py runserver      # http://127.0.0.1:8000
# prod
gunicorn myproject.wsgi
```

---

## 3. `frontend/` — React interface

npm monorepo with two Vite applications.

### Public site: `frontend/wikipediapeoplemap/`

| Area | Tech |
|---|---|
| Framework | React 19 + TypeScript 6, Vite 8 |
| Compilation | **React Compiler** (`babel-plugin-react-compiler` via `@rolldown/plugin-babel`) |
| Server data | **TanStack Query** (cache, loading / error states, devtools) |
| Routing | `react-router-dom` 7 |
| UI | `@steevenakintilo/ui` (classic design system, package vendored in `vendor/*.tgz`) + Tailwind CSS 4 |
| Maps | Leaflet / `react-leaflet`, MapLibre GL / `react-map-gl` |
| Charts | AG Charts |
| Translation | `i18next` / `react-i18next` (French and English) |
| SEO / analytics | `react-helmet-async`, `@vercel/analytics` |
| Lint | oxlint |

**Organization** ([src/](frontend/wikipediapeoplemap/src/)):

- `api/`: [client.ts](frontend/wikipediapeoplemap/src/api/client.ts) (`api_fetch`, the single HTTP call point, throws `ApiError` on a non-2xx response), [queries.ts](frontend/wikipediapeoplemap/src/api/queries.ts) (TanStack Query hooks, one per endpoint), `query_client.ts` (cache configuration).
- `pages/`: one page per route.
- `components/`: advanced search (filters described in `advanced_search_config.ts`), person profile (`user_profile_dialog`), tables, charts, error report (`report_dialog`), layout.
- `i18n/`: translations. The French text of the code is the key and [en.json](frontend/wikipediapeoplemap/src/i18n/en.json) gives the English version; `data_names.ts` and `jobs.ts` translate the values coming from the backend (countries, causes of death, jobs…), and a job search typed in English is converted back to French before being sent.
- `utils/`: constants (colors by gender, country lists), dark / light theme, helpers.

**Routes**:

| URL | Page |
|---|---|
| `/`, `/Home` | Home |
| `/WorldMap` | World map of births / deaths with advanced search |
| `/Statistics` | Filterable statistics |
| `/OtherStatistics` | Additional statistics |
| `/Qjis` | Map for Qjis |
| `/WikiGames`, `/WhoIsOlder` | Mini-games |
| `/About` | About |

The map data is loaded **in blocks** (`chunk_nb`) to display the first results quickly.

The backend URL is defined in [global_variable.tsx](frontend/wikipediapeoplemap/src/utils/global_variable.tsx) (`backend_url_prod`).

```bash
cd frontend
npm install
cd wikipediapeoplemap
npm run dev          # http://localhost:5173
npm run build        # tsc -b && vite build
npm run lint
```

### Admin page: `frontend/admin/`

Page used to edit the information of a `WikipediaUser`. Access is protected by an API key (`X-Admin-API-Key`).
```
VITE_BACKEND_URL=http://127.0.0.1:8000
VITE_ADMIN_API_KEY=…
```

---

## License

See [LICENSE](LICENSE).
