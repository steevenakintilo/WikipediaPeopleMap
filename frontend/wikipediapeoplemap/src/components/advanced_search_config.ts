// Configuration des filtres de recherche avancée (champs, options, valeurs envoyées au backend)
import { list_of_countries, list_of_country_flag } from "../utils/global_variable.tsx"

export type Option = { value: string, label: string }

// Les valeurs envoyées au backend sont strictement les mêmes qu'avant (seuls les libellés changent)
export type FilterField =
  | { key: string, label: string, type: "text", placeholder?: string, description?: string }
  | { key: string, label: string, type: "number", min: number, max: number, placeholder?: string }
  | { key: string, label: string, type: "country" }
  | { key: string, label: string, type: "choice", options: Option[] }
  | { key: string, label: string, type: "select", placeholder: string, options: Option[] }

export type FilterSection = { title: string, fields: FilterField[] }

export type Filters = Record<string, string>

// Le backend retire le drapeau à la fin de la valeur : "France 🇫🇷"
export const COUNTRY_OPTIONS = list_of_countries.map((country, i) => ({ value: `${country} ${list_of_country_flag[i]}` }))

const YES_NO: Option[] = [
  { value: "oui", label: "Oui" },
  { value: "non", label: "Non" },
]

export const NO_PREFERENCE = "__no_preference__"

const HISTORICAL_PERIODS: Option[] = [
  { value: "Préhistoire -99999999-3301", label: "Préhistoire (avant -3300)" },
  { value: "Antiquité -3300-475", label: "Antiquité (-3300 à 475)" },
  { value: "Moyen Âge 476-1491", label: "Moyen Âge (476 à 1491)" },
  { value: "Renaissance 1492-1788", label: "Renaissance (1492 à 1788)" },
  { value: "Époque contemporaine 1789-1999", label: "Époque contemporaine (1789 à 1999)" },
  { value: "Époque actuelle 2000-?????", label: "Époque actuelle (depuis 2000)" },
  { value: "Indéfinie", label: "Indéfinie" },
  { value: "Toutes", label: "Toutes" },
]

const SORT_OPTIONS: Option[] = [
  { value: "Par défaut", label: "Par défaut" },
  { value: "Nombre de lien", label: "Nombre de liens" },
  { value: "Taille de la page wipedia", label: "Taille de la page Wikipédia" },
  { value: "Nombre de personnes qui les lient", label: "Nombre de personnes qui les citent" },
  { value: "Âge", label: "Âge" },
  { value: "Nombre d'ami(e)", label: "Nombre d'ami(e)s" },
  { value: "Taille du nom de la page", label: "Taille du nom de la page" },
  { value: "Nombre de vue(s)", label: "Nombre de vues" },  
]

const PAGE_NAME: FilterField = { key: "page_name", label: "Nom de la page wikipedia", type: "text", description: "# pour plusieurs pages, + pour les pages contenant le texte" }

const IDENTITY_FIELDS: FilterField[] = [
  { key: "last_name", label: "Nom de famille", type: "text", description: "# pour plusieurs noms, + pour les noms contenant le texte" },
  { key: "first_name", label: "Prénom", type: "text", description: "# pour plusieurs prénoms, + pour les prénoms contenant le texte" },
  { key: "job", label: "Métier", type: "text", placeholder: "acteur ou chanteuse#peintre", description: "Ex : acteur ou chanteuse#peintre#médecin ou foot" },
  { key: "gender", label: "Genre", type: "choice", options: [{ value: "Homme", label: "Hommes" }, { value: "Femme", label: "Femmes" }, { value: "Les 2", label: "Les deux" }] },
  { key: "alive_status", label: "Mort ou vivant", type: "choice", options: [{ value: "Mort", label: "Décédé(e)s" }, { value: "Vivant", label: "Vivant(e)s" }, { value: "Les 2", label: "Les deux" }] },
]

const IDENTITY: FilterSection = { title: "Identité", fields: [...IDENTITY_FIELDS.slice(0, 3), PAGE_NAME, ...IDENTITY_FIELDS.slice(3)] }

// Page Carte : le nom de la page est dans « Affichage »
const IDENTITY_WITHOUT_PAGE_NAME: FilterSection = { title: "Identité", fields: IDENTITY_FIELDS }

const BIRTH: FilterSection = {
  title: "Naissance",
  fields: [
    { key: "country_of_birth", label: "Continent, région ou pays", type: "country" },
    { key: "town_birth_place", label: "Ville(s)", type: "text", description: "# pour plusieurs villes" },
    { key: "birth_year", label: "Année", type: "text", description: "+ pour inclure les années suivantes" },
    { key: "birth_month_day", label: "Jour", type: "text", placeholder: "01-janvier", description: "Format JJ-MOIS" },
    { key: "time_period_of_birth", label: "Période historique", type: "select", placeholder: "Toutes les périodes", options: HISTORICAL_PERIODS },
    { key: "century_of_birth", label: "Siècle", type: "number", min: 1, max: 125 },
    { key: "born_before_christ", label: "Né(e) avant Jésus-Christ", type: "choice", options: [...YES_NO, { value: "Les 2", label: "Les deux" }] },
  ],
}

const DEATH: FilterSection = {
  title: "Décès",
  fields: [
    { key: "country_death_place", label: "Continent, région ou pays", type: "country" },
    { key: "town_death_place", label: "Ville(s)", type: "text", description: "# pour plusieurs villes" },
    { key: "death_year", label: "Année", type: "text", description: "- pour inclure les années précédentes" },
    { key: "death_month_day", label: "Jour", type: "text", placeholder: "13-mars", description: "Format JJ-MOIS" },
    { key: "century_of_death", label: "Siècle", type: "number", min: 1, max: 125 },
    { key: "is_cause_of_death_known", label: "Afficher les gens avec une cause de décès connue uniquement", type: "choice", options: YES_NO },
    { key: "display_only_people_born_and_dead_the_same_day", label: "Afficher les gens nés et morts le même jour uniquement", type: "choice", options: YES_NO },
    { key: "display_only_people_born_and_dead_in_the_same_town", label: "Afficher les gens nés et morts dans la même ville uniquement", type: "choice", options: YES_NO },
  ],
}

const AGE_AND_PLACES: FilterSection = {
  title: "Âge et lieux",
  fields: [
    { key: "age", label: "Âge minimum", type: "number", min: 1, max: 125 },
    { key: "age_max", label: "Âge maximum", type: "number", min: 1, max: 125 },
    { key: "town_birth_or_death_place", label: "Ville de naissance ou de décès", type: "text" },
  ],
}

// const GAME_SETTINGS: FilterSection = {
//   title: "Paramétre de jeu",
//   fields: [
//     { key: "number_of_rounds", label: "Nombre de round (1-25)", type: "number", min:1 , max: 25 }
//   ],
// }

const PRECISENESS: FilterField = { key: "preciseness_level", label: "Précision minimale de la page (%)", type: "number", min: 0, max: 100 }
const LATEST_POSITION: FilterField = { key: "latest_position_of_user_to_display", label: "Position maximale au classement", type: "number", min: 1, max: 712411 }
const ONE_PER_TOWN: FilterField = { key: "display_only_one_person_per_town", label: "Une seule personne par ville de naissance", type: "choice", options: YES_NO }

// Pages Statistiques et Export QGIS
export const STATISTICS_FILTERS: FilterSection[] = [
  IDENTITY,
  BIRTH,
  DEATH,
  AGE_AND_PLACES,
  {
    title: "Sélection",
    fields: [
      PRECISENESS,
      LATEST_POSITION,
      ONE_PER_TOWN,
      { key: "display_only_one_person_per_first_name", label: "Une seule personne par prénom", type: "choice", options: YES_NO },
      { key: "display_only_one_person_per_last_name", label: "Une seule personne par nom de famille", type: "choice", options: YES_NO },
      { key: "display_only_one_person_per_job", label: "Une seule personne par métier", type: "choice", options: YES_NO },
      { key: "display_only_death_localisation", label: "Afficher uniquement les lieux de décès", type: "choice", options: YES_NO }
    ],
  },
]

// Page Qui est né avant ? (seuls les filtres pris en compte par la vue create_game_view)
export const GAME_FILTERS: FilterSection[] = [

  {
    title : "Paramètres de jeu",
    fields: [{ key: "number_of_rounds", label: "Nombre de round (1-25)", type: "number", min:1 , max: 25 },
      LATEST_POSITION]
  },
  IDENTITY,
  BIRTH,
  DEATH,
  AGE_AND_PLACES,
  {
    title: "Sélection",
    fields: [PRECISENESS, ONE_PER_TOWN],
  },
]

// Page Carte
export const MAP_FILTERS: FilterSection[] = [
  IDENTITY_WITHOUT_PAGE_NAME,
  BIRTH,
  DEATH,
  AGE_AND_PLACES,
  {
    title: "Affichage",
    fields: [
      { key: "sort_user_by", label: "Trier les pages par", type: "select", placeholder: "Par défaut", options: SORT_OPTIONS },
      { key: "number_of_people_to_display", label: "Personnes par page (1-500)", type: "number", min: 0, max: 500 },
      PRECISENESS,
      LATEST_POSITION,
      ONE_PER_TOWN,
      { key: "display_people_with_no_localisation", label: "Afficher les gens qui n'ont pas de localisation de naissance ?", type: "choice", options: YES_NO },
      { key: "display_only_death_localisation", label: "Afficher uniquement les lieux de décès", type: "choice", options: YES_NO },
      PAGE_NAME,
    ],
  },
]

export function is_active(value: string | undefined) {
  return value !== undefined && value !== ""
}

export function displayed_value(field: FilterField, value: string) {
  if (field.type === "choice" || field.type === "select") {
    return field.options.find((option) => option.value === value)?.label ?? value
  }
  return value
}

export function count_active_filters(sections: FilterSection[], filters: Filters) {
  return sections.flatMap((section) => section.fields).filter((field) => is_active(filters[field.key])).length
}

export function without_key(filters: Filters, key: string) {
  const next = { ...filters }
  delete next[key]
  return next
}
