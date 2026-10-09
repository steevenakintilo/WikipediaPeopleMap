import { useState, type CSSProperties, type FormEvent } from "react"

import { derive_fields } from "./derived.ts"
import { country_to_flag } from "./flags.ts"
import { MANUAL_ONLY, UNPRECISENESS, detect_unpreciseness, preciseness_level, to_unpreciseness_keys } from "./unpreciseness.ts"

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL ?? "http://127.0.0.1:8000"
const BACKEND_PROD = import.meta.env.VITE_BACKEND_PROD ?? "http://127.0.0.1:8000"

const ADMIN_API_KEY = import.meta.env.VITE_ADMIN_API_KEY ?? ""

// Champs envoyés à /update_user_info (mêmes noms que le modèle Django WikipediaUser)
const FIELDS = [
  "picture_url", "birth_date", "is_alive", "death_date", "gender", "age", "job",
  "town_birth_place", "town_birth_localisation", "country_birth_place", "country_birth_place_emoji",
  "continent_of_birth",
  "town_death_place", "town_death_localisation", "country_death_place", "country_death_place_emoji",
  "continent_of_death", "time_period_of_birth",
] as const

type Field = typeof FIELDS[number]
type Form = Record<Field, string>

const COUNTRIES = [
  "Afghanistan",
  "Afrique du Sud",
  "Albanie",
  "Algérie",
  "Allemagne",
  "Andorre",
  "Angola",
  "Antigua et Barbuda",
  "Arabie saoudite",
  "Argentine",
  "Arménie",
  "Australie",
  "Autriche",
  "Azerbaïdjan",
  "Bahamas",
  "Bahreïn",
  "Bangladesh",
  "Barbade",
  "Belgique",
  "Belize",
  "Bénin",
  "Bhoutan",
  "Biélorussie",
  "Birmanie",
  "Bolivie",
  "Bosnie Herzégovine",
  "Botswana",
  "Brésil",
  "Brunei",
  "Bulgarie",
  "Burkina Faso",
  "Burundi",
  "Cambodge",
  "Cameroun",
  "Canada",
  "Cap Vert",
  "République centrafricaine",
  "Chili",
  "Chine",
  "Chypre",
  "Chypre du Nord",
  "Colombie",
  "Comores",
  "République du Congo",
  "République démocratique du Congo",
  "Îles Cook",
  "Corée du Nord",
  "Corée du Sud",
  "Costa Rica",
  "Côte d'Ivoire",
  "Croatie",
  "Cuba",
  "Danemark",
  "Djibouti",
  "République dominicaine",
  "Dominique",
  "Égypte",
  "Émirats arabes unis",
  "Équateur",
  "Érythrée",
  "Espagne",
  "Estonie",
  "Eswatini",
  "États Unis",
  "Éthiopie",
  "Fidji",
  "Finlande",
  "France",
  "Gabon",
  "Gambie",
  "Géorgie",
  "Ghana",
  "Grèce",
  "Grenade",
  "Guatemala",
  "Guinée",
  "Guinée Bissau",
  "Guinée équatoriale",
  "Guyana",
  "Haïti",
  "Honduras",
  "Hongrie",
  "Inde",
  "Indonésie",
  "Irak",
  "Iran",
  "Irlande",
  "Islande",
  "Israël",
  "Italie",
  "Jamaïque",
  "Japon",
  "Jordanie",
  "Kazakhstan",
  "Kenya",
  "Kirghizistan",
  "Kiribati",
  "Kosovo",
  "Koweït",
  "Laos",
  "Lesotho",
  "Lettonie",
  "Liban",
  "Liberia",
  "Libye",
  "Liechtenstein",
  "Lituanie",
  "Luxembourg",
  "Macédoine du Nord",
  "Madagascar",
  "Malaisie",
  "Malawi",
  "Maldives",
  "Mali",
  "Malte",
  "Maroc",
  "Îles Marshall",
  "Maurice",
  "Mauritanie",
  "Mexique",
  "Micronésie",
  "Moldavie",
  "Monaco",
  "Mongolie",
  "Monténégro",
  "Mozambique",
  "Namibie",
  "Nauru",
  "Népal",
  "Nicaragua",
  "Niger",
  "Nigeria",
  "Niue",
  "Norvège",
  "Nouvelle Zélande",
  "Oman",
  "Ossétie du Sud Alanie",
  "Ouganda",
  "Ouzbékistan",
  "Pakistan",
  "Palaos",
  "Palestine",
  "Panama",
  "Papouasie Nouvelle Guinée",
  "Paraguay",
  "Pays Bas",
  "Pérou",
  "Philippines",
  "Pologne",
  "Portugal",
  "Qatar",
  "Roumanie",
  "Royaume Uni",
  "Russie",
  "Rwanda",
  "Saint Christophe et Niévès",
  "Saint Marin",
  "Saint Vincent et les Grenadines",
  "Sainte Lucie",
  "Îles Salomon",
  "Salvador",
  "Samoa",
  "São Tomé et Principe",
  "Sénégal",
  "Serbie",
  "Seychelles",
  "Sierra Leone",
  "Singapour",
  "Slovaquie",
  "Slovénie",
  "Somalie",
  "Soudan",
  "Soudan du Sud",
  "Sri Lanka",
  "Suède",
  "Suisse",
  "Suriname",
  "Syrie",
  "Tadjikistan",
  "Taïwan",
  "Tanzanie",
  "Tchad",
  "République tchèque",
  "Thaïlande",
  "Timor oriental",
  "Togo",
  "Tonga",
  "Trinité et Tobago",
  "Tunisie",
  "Turkménistan",
  "Turquie",
  "Tuvalu",
  "Ukraine",
  "Uruguay",
  "Vanuatu",
  "Vatican",
  "Venezuela",
  "Viêt Nam",
  "Yémen",
  "Zambie",
  "Zimbabwe",
]

// Valeurs exactes de la base ("Amerique" sans accent)
const CONTINENTS = ["Afrique", "Amerique", "Asie", "Europe", "Océanie"]

const HISTORICAL_PERIODS = ["Prehistory", "Antiquity", "Middle Ages", "Renaissance", "Contemporary Period", "Today Time"]

// Champs à choix : liste déroulante au lieu d'un champ texte libre
const CHOICES: Partial<Record<Field, string[]>> = {
  is_alive: ["true", "false"],
  gender: ["Man", "Woman", "Unclear"],
  // En base les pays sont en minuscules ("états unis")
  country_birth_place: COUNTRIES.map((country) => country.toLowerCase()),
  country_death_place: COUNTRIES.map((country) => country.toLowerCase()),
  continent_of_birth: CONTINENTS,
  continent_of_death: CONTINENTS,
  time_period_of_birth: HISTORICAL_PERIODS,
}

const CHOICE_LABELS: Record<string, string> = { Man: "Homme", Woman: "Femme", Unclear: "Non précisé" }

// Nom de la clé dans la réponse de display_user_info quand il diffère du champ envoyé
const RESPONSE_KEY: Partial<Record<Field, string>> = { town_birth_localisation: "birth_town_localisation" }

// Changer un pays met à jour son drapeau automatiquement
const FLAG_FIELD: Partial<Record<Field, Field>> = {
  country_birth_place: "country_birth_place_emoji",
  country_death_place: "country_death_place_emoji",
}

const EMPTY_FORM = Object.fromEntries(FIELDS.map((field) => [field, ""])) as Form

function to_text(value: unknown): string {
  if (value === null || value === undefined) return ""
  if (typeof value === "object") return JSON.stringify(value)
  return String(value)
}

export function Admin() {
  const [username, set_username] = useState("")
  const [form, set_form] = useState<Form>(EMPTY_FORM)
  const [status, set_status] = useState("")
  const [loading, set_loading] = useState(false)
  const [loaded_username, set_loaded_username] = useState("")
  // Clés de list_of_unpreciseness_data cochées
  const [unpreciseness, set_unpreciseness] = useState<string[]>([])

  function set_field(field: Field, value: string) {
    const flag_field = FLAG_FIELD[field]
    set_form((prev) => ({ ...prev, [field]: value, ...(flag_field ? { [flag_field]: country_to_flag(value) } : {}) }))
  }

  // Pré-remplit le formulaire avec les infos actuelles de la personne
  async function load() {
    if (!username) return
    set_loading(true)
    set_status("")
    try {
      const response = await fetch(`${BACKEND_PROD}/display_user_info/${encodeURIComponent(username)}`)
      if (!response.ok) throw new Error(`HTTP ${response.status}`)
      const data = await response.json()
      const user = Array.isArray(data) ? data[0] : (data.user ?? data)
      set_form(Object.fromEntries(FIELDS.map((field) => [field, to_text(user?.[RESPONSE_KEY[field] ?? field])])) as Form)
      set_unpreciseness(to_unpreciseness_keys(user?.list_of_unpreciseness_data))
      set_loaded_username(username)
      set_status("Infos chargées.")
    } catch (error) {
      set_status(`Chargement impossible : ${error}`)
    } finally {
      set_loading(false)
    }
  }

  async function submit(event: FormEvent) {
    event.preventDefault()
    if (!ADMIN_API_KEY) {
      set_status("VITE_ADMIN_API_KEY manquante dans .env")
      return
    }
    set_loading(true)
    set_status("")
    try {
      const response = await fetch(`${BACKEND_URL}/update_user_info`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json", "X-Admin-API-Key": ADMIN_API_KEY },
        body: JSON.stringify({
          username, ...form, ...derived,
          // Types du modèle Django : is_alive BooleanField, age / birth_year IntegerField, death_year CharField
          is_alive: form.is_alive === "true",
          age: form.age.trim() === "" ? null : Number(form.age),
          birth_year: Number(derived.birth_year),
          death_year: String(derived.death_year),
          list_of_unpreciseness_data: unpreciseness,
          preciseness_level: preciseness_level(unpreciseness),
        }),
      })
      const text = await response.text()
      set_status(response.ok ? `Mis à jour. ${text}` : `Erreur HTTP ${response.status} : ${text}`)
    } catch (error) {
      set_status(`Envoi impossible : ${error}`)
    } finally {
      set_loading(false)
    }
  }

  const derived = derive_fields(form)

  // Imprécisions inconnues de la liste (anciennes clés) : affichées pour pouvoir les retirer
  const extra_unpreciseness = unpreciseness.filter((key) => !UNPRECISENESS.some((item) => item.key === key))

  function toggle_unpreciseness(key: string, checked: boolean) {
    set_unpreciseness((prev) => (checked ? [...prev, key] : prev.filter((item) => item !== key)))
  }

  // Recalcule depuis le formulaire, en gardant les cases que seul le texte de la page peut décider
  function recompute_unpreciseness() {
    const detected = detect_unpreciseness(form, derived.born_before_christ === "True", String(derived.death_day))
    set_unpreciseness((prev) => [...prev.filter((key) => MANUAL_ONLY.has(key)), ...detected])
  }

  const wikipedia_url = `https://fr.wikipedia.org/wiki/${encodeURIComponent(username.replaceAll(" ", "_"))}`

  return (
    <main style={styles.main}>
      <h1>Admin : modifier une fiche</h1>

      <form onSubmit={submit} style={styles.form}>
        <label style={styles.label}>
          username (nom de la page)
          <div style={styles.row}>
            <input style={{ ...styles.input, flex: 1 }} value={username} onChange={(e) => set_username(e.target.value)}
              // Entrée ou sortie du champ : charge directement les infos actuelles
              onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); load() } }}
              onBlur={() => { if (username !== loaded_username) load() }}
              required
            />
            <button type="button" onClick={load} disabled={!username || loading}>Charger</button>
          </div>
        </label>

        {username && (
          <a href={wikipedia_url} target="_blank" rel="noopener noreferrer">Voir la page Wikipédia de {username}</a>
        )}

        {FIELDS.map((field) => (
          <label key={field} style={styles.label}>
            {field}
            {CHOICES[field] ? (
              <select
                style={styles.input}
                value={form[field]}
                onChange={(e) => set_field(field, e.target.value)}
              >
                <option value="">-- Choisir --</option>
                {/* Valeur actuelle hors liste : on la garde visible pour ne pas la perdre */}
                {form[field] && !CHOICES[field].includes(form[field]) && <option value={form[field]}>{form[field]}</option>}
                {CHOICES[field].map((choice) => <option key={choice} value={choice}>{CHOICE_LABELS[choice] ?? choice}</option>)}
              </select>
            ) : (
              <input
                style={styles.input}
                value={form[field]}
                onChange={(e) => set_form((prev) => ({ ...prev, [field]: e.target.value }))}
              />
            )}
          </label>
        ))}

        <fieldset style={styles.derived}>
          <legend>Imprécisions (list_of_unpreciseness_data) : score {preciseness_level(unpreciseness)}</legend>
          <button type="button" onClick={recompute_unpreciseness} style={{ alignSelf: "flex-start" }}>Recalculer depuis le formulaire</button>
          {UNPRECISENESS.map((item) => (
            <label key={item.key} style={styles.check}>
              <input type="checkbox" checked={unpreciseness.includes(item.key)} onChange={(e) => toggle_unpreciseness(item.key, e.target.checked)} />
              {item.fr} <span style={{ color: "#888" }}>(-{item.penalty})</span>
            </label>
          ))}
          {extra_unpreciseness.map((key) => (
            <label key={key} style={styles.check}>
              <input type="checkbox" checked onChange={() => toggle_unpreciseness(key, false)} /> {key} <span style={{ color: "#888" }}>(inconnue)</span>
            </label>
          ))}
        </fieldset>

        <fieldset style={styles.derived}>
          <legend>Calculé automatiquement (envoyé aussi)</legend>
          {Object.entries(derived).map(([key, value]) => (
            <div key={key}><code>{key}</code> : {String(value)}</div>
          ))}
        </fieldset>

        <button type="submit" disabled={!username || loading} style={styles.submit}>
          {loading ? "..." : "Envoyer /update_user_info"}
        </button>
        {status && <p>{status}</p>}
      </form>
    </main>
  )
}

const styles: Record<string, CSSProperties> = {
  main: { maxWidth: 640, margin: "0 auto", padding: 16, fontFamily: "system-ui, sans-serif" },
  form: { display: "flex", flexDirection: "column", gap: 12 },
  label: { display: "flex", flexDirection: "column", gap: 4, fontSize: 14, fontWeight: 600 },
  row: { display: "flex", gap: 8 },
  input: { padding: 8, fontSize: 14, fontWeight: 400, border: "1px solid #ccc", borderRadius: 6 },
  derived: { fontSize: 13, display: "flex", flexDirection: "column", gap: 2, border: "1px solid #ccc", borderRadius: 6 },
  check: { display: "flex", gap: 6, alignItems: "flex-start" },
  submit: { padding: 10, background: "#212529", color: "white", border: 0, borderRadius: 6, cursor: "pointer" },
}
