# WikipediaPeopleMap

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
| UI | `@steevenakintilo/ui` (design system classique, package vendoré dans `vendor/*.tgz`) + Tailwind CSS 4 || Cartes | Leaflet / `react-leaflet`, MapLibre GL / `react-map-gl` |
| Graphiques | AG Charts |
| SEO / analytics | `react-helmet-async`, `@vercel/analytics` |
| Lint | oxlint |

**Organisation** ([src/](frontend/wikipediapeoplemap/src/)) :

- `api/` : [client.ts](frontend/wikipediapeoplemap/src/api/client.ts) (`api_fetch`, unique point d'appel HTTP, lève `ApiError` si réponse non 2xx), [queries.ts](frontend/wikipediapeoplemap/src/api/queries.ts) (hooks TanStack Query, un par endpoint), `query_client.ts` (configuration du cache).
- `pages/` : une page par route.
- `components/` : recherche avancée (filtres décrits dans `advanced_search_config.ts`), fiche personne (`user_profile_dialog`), tableaux, graphiques, signalement d'erreur (`report_dialog`), layout.
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
