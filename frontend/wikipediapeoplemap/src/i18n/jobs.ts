import { JOBS_MORE } from "./jobs_data_more.ts"
import { JOBS_EXTRA, PORTFOLIOS } from "./jobs_data_extra.ts"
import { ADJECTIVES, ORG_NOUNS, PORTFOLIO_WORDS } from "./jobs_data_org.ts"
import { JOBS as JOBS_BASE, NATIONALITIES, PLACES, ROLES, SPORTS, THE_PLACES, type Entry } from "./jobs_data.ts"

// Traduction des métiers (qui viennent du backend, en français sans accents) : un dictionnaire de métiers complets,
// plus des règles pour les titres composés ("Président de la République de Pologne", "Écrivain russe"…).
// Un métier inconnu reste tel quel (en français).

export function normalize_job(text: string) {
  return text
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/œ/g, "oe")
    .replace(/&nbsp;/g, " ")
    .replace(/[’`]/g, "'")
    .toLowerCase()
    .replace(/\s+/g, " ")
    .trim()
}

function build_map(entries: Entry[]) {
  const map = new Map<string, string>()
  for (const [forms, english] of entries) {
    for (const form of forms.split("|")) {
      const key = normalize_job(form)
      if (!map.has(key)) {
        map.set(key, english)
      }
    }
  }
  return map
}

const JOBS = [...JOBS_BASE, ...JOBS_MORE, ...JOBS_EXTRA]
const JOB_MAP = build_map(JOBS)
const NATIONALITY_MAP = build_map(NATIONALITIES)
const ROLE_MAP = build_map(ROLES)
const PLACE_MAP = build_map(PLACES)
const PORTFOLIO_MAP = build_map([...PORTFOLIO_WORDS, ...PORTFOLIOS])
const ORG_NOUN_MAP = build_map(ORG_NOUNS)
const SPORT_MAP = new Map(Object.entries(SPORTS).map(([key, value]) => [normalize_job(key), value]))
function masculine_forms(token: string) {
  return [token, token.replace(/ienne$/, "ien"), token.replace(/aise$/, "ais"), token.replace(/oise$/, "ois"), token.replace(/enne$/, "en"), token.replace(/e$/, "")]
}

function lookup_in<T>(map: Map<string, T>, token: string): T | undefined {
  for (const form of masculine_forms(token)) {
    const found = map.get(form)
    if (found !== undefined) {
      return found
    }
  }
  return undefined
}

const ROLE_PREFIXES = [...ROLE_MAP.keys()].sort((a, b) => b.length - a.length)

// Mots du dictionnaire qui ne sont pas des métiers : on ne les accole pas ("grand roi" ne donne pas "great and king")
const NOT_AN_OCCUPATION = new Set(["great", "first", "high", "important", "young person", "member", "parent", "child", "man", "woman", "boy", "adult", "teenager", "daughter", "son", "brother", "sister", "wife", "spouse", "mistress", "heir", "descendant", "victim", "survivor", "student", "pupil", "master", "guardian", "practitioner", "fighter", "religious", "athlete", "player", "agent"])

export type PlaceTranslator = (name: string) => string

const PREPOSITION = /^(de la |de l'|du |des |de |d')(.+)$/

// "Parti communiste italien" -> "the Italian Communist Party" ; "Assemblée nationale de Slovénie" -> "the National Assembly of Slovenia"
// Strict : tous les mots doivent être connus, sinon null (on garde alors le français).
function translate_org(rest: string, original: string, place_translator?: PlaceTranslator, depth = 0): string | null {
  const parts = rest.split(/ (?:de la |de l'|du |des |de |d')/)
  if (parts.length > 2) {
    return null
  }
  const head_tokens = parts[0].split(" ")
  const noun = ORG_NOUN_MAP.get(head_tokens[0])
  if (noun === undefined) {
    return null
  }
  const adjectives: [string, number][] = []
  for (const token of head_tokens.slice(1)) {
    const adjective = lookup_in(ADJECTIVES, token)
    const nationality = lookup_in(NATIONALITY_MAP, token)
    if (adjective !== undefined) {
      adjectives.push([adjective[0], adjective[1]])
    } else if (nationality !== undefined) {
      adjectives.push([nationality, 0])
    } else {
      return null
    }
  }
  adjectives.sort((a, b) => a[1] - b[1])
  const head = [...adjectives.map(([word]) => word), noun].join(" ")
  if (parts.length === 1) {
    return `the ${head}`
  }
  const place_original = tail_of(original, parts[1])
  const place = translate_place_part(parts[1], place_original, place_translator, depth + 1)
  if (place === null) {
    return is_proper_noun(place_original) ? `the ${head} of ${place_original}` : null
  }
  return `the ${head} of ${with_article(place)}`
}

// Un lieu ou une organisation : liste des pays (via place_translator), noms connus, ou "organisation de lieu"
function translate_place_part(rest: string, original: string, place_translator?: PlaceTranslator, depth = 0): string | null {
  const known = PLACE_MAP.get(rest)
  if (known !== undefined) {
    return known
  }
  if (place_translator !== undefined) {
    const translated = place_translator(original)
    if (translated !== original) {
      return translated
    }
  }
  // "Parti social-démocrate d'Allemagne" -> "Social Democratic Party of Germany"
  const composite = rest.match(/^(.+?) (?:de la |de l'|du |des |de |d')(.+)$/)
  if (composite && depth < 2) {
    const head = PLACE_MAP.get(composite[1])
    if (head !== undefined) {
      const tail_original = tail_of(original, composite[2])
      const tail = translate_place_part(composite[2], tail_original, place_translator, depth + 1)
      if (tail !== null) {
        return `${head} of ${with_article(tail)}`
      }
      if (is_proper_noun(tail_original)) {
        return `${head} of ${tail_original}`
      }
    }
  }
  if (depth < 2) {
    return translate_org(rest, original, place_translator, depth)
  }
  return null
}

const THE_PREFIXES = ["Legislative Assembly", "National Assembly", "Grand Council", "National Council", "House of", "Senate", "Supreme Court", "Court of", "Council of", "Chamber of"]

function with_article(place: string) {
  if (place.startsWith("the ")) {
    return place
  }
  return THE_PLACES.has(place.toLowerCase()) || THE_PREFIXES.some((prefix) => place.startsWith(prefix)) ? `the ${place}` : place
}

// "Pau", "New York" : un nom propre court qu'on peut garder tel quel. Un morceau de français ("Conseil exécutif suprême de …") non.
function is_proper_noun(text: string) {
  const tokens = text.trim().split(/\s+/)
  return tokens.length >= 1 && tokens.length <= 3 && tokens.every((token) => token.charAt(0) !== token.charAt(0).toLowerCase())
}

function capitalize(text: string) {
  return text.charAt(0).toUpperCase() + text.slice(1)
}

// Retrouve le texte d'origine d'un morceau normalisé : on réutilise la fin du texte reçu (mêmes caractères, accents compris)
function tail_of(original: string, normalized_rest: string) {
  const trimmed = original.trim()
  return trimmed.length >= normalized_rest.length ? trimmed.slice(trimmed.length - normalized_rest.length) : trimmed
}

function translate_normalized(normalized: string, original: string, place_translator?: PlaceTranslator, depth = 0): string | null {
  const direct = JOB_MAP.get(normalized)
  if (direct !== undefined) {
    return direct
  }
  if (depth > 2) {
    return null
  }

  // "Roi des Francs puis roi de France" -> "King of the Franks, then King of France"
  if (normalized.includes(" puis ") && depth === 0) {
    const halves = normalized.split(" puis ")
    const translated = halves.map((half) => translate_normalized(half, tail_of(original, half), place_translator, depth + 1))
    if (halves.length === 2 && translated.every((half) => half !== null)) {
      const [first, second] = translated as string[]
      return `${first}, then ${capitalize(second)}`
    }
  }

  // "Premier ministre du cabinet fantôme", "Chancelier de l'Échiquier de l'ombre" -> "Shadow …"
  const shadow = normalized.match(/^(.+?) (?:du cabinet fantome|de l'ombre)$/)
  if (shadow) {
    const translated = translate_normalized(shadow[1], original, place_translator, depth + 1)
    if (translated !== null) {
      return `Shadow ${translated.charAt(0).toLowerCase()}${translated.slice(1)}`
    }
  }

  // "Roi de Castille et de Galice" / "Duc d'Apulie, de Calabre et de Sicile" -> "King of Castile and Galicia"
  const listed = normalized.match(/^(.+?) (?:de la |de l'|du |des |de |d')(.+?)(?:,| et) (?:de la |de l'|du |des |de |d')(.+)$/)
  if (listed && ROLE_MAP.has(listed[1])) {
    const names = [listed[2], ...listed[3].split(/,\s*|\s+et\s+/)].map((name) => name.replace(/^(?:de la |de l'|du |des |de |d')/, "").trim())
    const places = names.map((name) => translate_place_part(name, tail_of(original, name), place_translator))
    if (places.every((place) => place !== null)) {
      const list = places as string[]
      const joined = list.length === 2 ? `${list[0]} and ${list[1]}` : `${list.slice(0, -1).join(", ")} and ${list[list.length - 1]}`
      return `${ROLE_MAP.get(listed[1])} of ${joined}`
    }
  }

  // "Président du Conseil des ministres espagnol" -> "President of the Spanish Council of Ministers"
  const council = normalized.match(/^(president|presidente) du conseil des ministres (\S+)$/)
  if (council) {
    const nationality = lookup_in(NATIONALITY_MAP, council[2])
    if (nationality !== undefined) {
      return `President of the ${nationality} Council of Ministers`
    }
  }

  // "Avocat (métier)" -> "Avocat"
  const parenthetical = normalized.match(/^(.*?) \([^)]*\)$/)
  if (parenthetical) {
    return translate_normalized(parenthetical[1], original, place_translator, depth + 1)
  }

  // "Un ancien joueur de rugby" -> "former rugby player"
  const sport_player = normalized.match(/^(?:un |une )?(ancien |ancienne )?(joueur|joueuse) (?:de |d')(.+)$/)
  if (sport_player) {
    const sport = SPORT_MAP.get(sport_player[3])
    if (sport !== undefined) {
      const former = sport_player[1] ? "former " : ""
      const female = sport_player[2] === "joueuse" ? "female " : ""
      return `${former}${female}${sport} player`
    }
  }

  // "Ministre des Affaires étrangères" : titre complet connu
  const role_exact = ROLE_MAP.get(normalized)
  if (role_exact !== undefined) {
    return role_exact
  }

  // "Ministre danois des Affaires étrangères" -> "Danish Minister of Foreign Affairs" ;
  // "Secrétaire d'État britannique à la Culture, aux Médias et aux Sports" -> "British Secretary of State for Culture, Media and Sport"
  const portfolio_role = normalized.match(
    /^(ministre delegue|ministre deleguee|ministre d'etat|ministre federal|ministre federale|ministre|secretaire d'etat|secretaire)(?: (?!charge|chargee)(\S+))?(?: charge| chargee)? (?:de la |de l'|du |des |de |d'|a la |a l'|au |aux |a )(.+)$/,
  )
  if (portfolio_role) {
    const nationality = portfolio_role[2] === undefined ? undefined : lookup_in(NATIONALITY_MAP, portfolio_role[2])
    const items = portfolio_role[3]
      .split(/,\s*|\s+et\s+/)
      .map((item) => item.replace(/^(?:de la |de l'|du |des |de |d'|a la |a l'|au |aux |a |la |le |l'|les )/, "").trim())
      .map((item) => PORTFOLIO_MAP.get(item))
    if (items.every((item) => item !== undefined) && (portfolio_role[2] === undefined || nationality !== undefined)) {
      const list = items as string[]
      const joined = list.length === 1 ? list[0] : `${list.slice(0, -1).join(", ")} and ${list[list.length - 1]}`
      const role = portfolio_role[1]
      const base = role === "ministre d'etat" ? "Minister of State" : role.startsWith("ministre delegue") ? "Minister Delegate" : role.startsWith("secretaire d'etat") ? "Secretary of State" : role === "secretaire" ? "Secretary" : role.startsWith("ministre federal") ? "Federal Minister" : "Minister"
      const connector = base === "Minister" || base === "Federal Minister" || base === "Secretary" ? "of" : "for"
      return `${nationality === undefined ? "" : nationality + " "}${base} ${connector} ${joined}`
    }
  }

  // "Député à l'Assemblée législative de l'Ontario" -> "Member of the Legislative Assembly of Ontario"
  const member = normalized.match(/^(?:depute|deputee|senateur|senatrice) (?:a la |a l'|au |aux |a )(.+)$/)
  if (member) {
    const body = translate_place_part(member[1], tail_of(original, member[1]), place_translator)
    if (body !== null) {
      return `Member of ${with_article(body)}`
    }
  }

  // "Président de la République de Pologne" -> "President of the Republic of Poland"
  for (const role of ROLE_PREFIXES) {
    if (!normalized.startsWith(role + " ")) {
      continue
    }
    const rest = normalized.slice(role.length + 1)
    const with_preposition = rest.match(PREPOSITION)
    if (with_preposition) {
      const place_original = tail_of(original, with_preposition[2])
      const place = translate_place_part(with_preposition[2], place_original, place_translator)
      if (place !== null) {
        return `${ROLE_MAP.get(role)} of ${with_article(place)}`
      }
      if (is_proper_noun(place_original)) {
        return `${ROLE_MAP.get(role)} of ${place_original}`
      }
      return null
    }
  }

  // "Écrivain russe" -> "Russian writer"
  const last_space = normalized.lastIndexOf(" ")
  if (last_space > 0) {
    const nationality = NATIONALITY_MAP.get(normalized.slice(last_space + 1))
    const head = translate_normalized(normalized.slice(0, last_space), original, place_translator, depth + 1)
    if (nationality !== undefined && head !== null) {
      return `${nationality} ${head.charAt(0).toLowerCase()}${head.slice(1)}`
    }
  }

  // "Un homme d'affaires" -> "homme d'affaires"
  const article = normalized.match(/^(?:un|une) (.+)$/)
  if (article) {
    return translate_normalized(article[1], original, place_translator, depth + 1)
  }

  // "Médecin écrivain" -> "physician and writer" : chaque mot est un métier connu
  const words = normalized.split(" ")
  if (words.length >= 2 && words.length <= 3) {
    const parts = words.map((word) => JOB_MAP.get(word))
    if (parts.every((part) => part !== undefined && !NOT_AN_OCCUPATION.has(part)) && new Set(parts).size === parts.length) {
      const list = parts as string[]
      return list.length === 2 ? `${list[0]} and ${list[1]}` : `${list[0]}, ${list[1]} and ${list[2]}`
    }
  }

  return null
}

// Traduit un métier ; renvoie null si on ne sait pas
export function translate_job_to_english(job: string, place_translator?: PlaceTranslator): string | null {
  const normalized = normalize_job(job)
  if (normalized === "") {
    return null
  }
  const english = translate_normalized(normalized, job, place_translator)
  if (english === null) {
    return null
  }
  const starts_with_capital = job.trim().charAt(0) !== job.trim().charAt(0).toLowerCase()
  return starts_with_capital ? capitalize(english) : english
}

// --- Recherche : anglais -> français (le backend cherche en français)

let reverse_map: Map<string, string[]> | null = null

function reverse() {
  if (reverse_map === null) {
    const grouped = new Map<string, string[]>()
    for (const [forms, english] of JOBS) {
      const key = english.toLowerCase()
      const list = grouped.get(key) ?? []
      for (const form of forms.split("|")) {
        const normalized = normalize_job(form)
        if (!list.includes(normalized)) {
          list.push(normalized)
        }
      }
      grouped.set(key, list)
    }
    // Le backend cherche par "contient" : une forme qui en contient une autre est inutile
    reverse_map = new Map()
    for (const [english, list] of grouped) {
      const sorted = [...list].sort((a, b) => a.length - b.length)
      const kept: string[] = []
      for (const form of sorted) {
        if (!kept.some((shorter) => form.includes(shorter))) {
          kept.push(form)
        }
      }
      reverse_map.set(english, kept)
    }
  }
  return reverse_map
}

// Morceaux d'une recherche de métier que le dictionnaire ne connaît ni en anglais ni en français
let known_french: Set<string> | null = null

export function unknown_job_parts(filter: string): string[] {
  if (known_french === null) {
    known_french = new Set(JOBS.flatMap(([forms]) => forms.split("|").map(normalize_job)))
  }
  return filter
    .split("#")
    .map((part) => part.trim())
    .filter((part) => part !== "" && !reverse().has(part.toLowerCase()) && !known_french!.has(normalize_job(part)))
}

// "actor#painter" -> "acteur#actrice#peintre". Un morceau inconnu est envoyé tel quel.
export function job_filter_to_french(filter: string): string {
  const parts = filter.split("#").map((part) => part.trim()).filter((part) => part !== "")
  let changed = false
  const result: string[] = []
  for (const part of parts) {
    const french = reverse().get(part.toLowerCase())
    if (french !== undefined) {
      result.push(...french)
      changed = true
    } else {
      result.push(part)
    }
  }
  return changed ? result.join("#") : filter
}
