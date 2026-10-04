// Imprécisions d'une page : clé stockée en base, texte FR (UNPRECISENESS_DATA_FR) et points retirés au score
export const UNPRECISENESS: { key: string, fr: string, penalty: number }[] = [
  { key: "town_birth_place is unknown", fr: "La ville de naissance est inconnue", penalty: 20 },
  { key: "birth town localisation is unknown", fr: "La localisation de la ville de naissance est inconnue", penalty: 10 },
  { key: "country_birth_place is unknown", fr: "Le pays de naissance est inconnu", penalty: 20 },
  { key: "birthdate is between two date", fr: "La date de naissance est comprise entre deux dates", penalty: 20 },
  { key: "birth year is real but month and day are not", fr: "L'année de naissance est connue, mais pas le mois ni le jour", penalty: 10 },
  { key: "death year is real but month and day are not", fr: "L'année de décès est connue, mais pas le mois ni le jour", penalty: 10 },
  { key: "town_death_place is unknown", fr: "La ville de décès est inconnue", penalty: 20 },
  { key: "country_death_place is unknown", fr: "Le pays de décès est inconnu", penalty: 20 },
  { key: "death town localisation is unknown", fr: "La localisation de la ville de décès est inconnue", penalty: 10 },
  { key: "birth_date and death_date may be the same", fr: "La date de naissance et la date de décès pourraient être identiques", penalty: 40 },
  { key: "birth_date and death_date are wrong", fr: "Les dates de naissance et de décès semblent incorrectes", penalty: 50 },
  { key: "birth_date is bad", fr: "La date de naissance semble incorrecte", penalty: 30 },
  { key: "gender is unclear", fr: "Le genre est incertain", penalty: 20 },
  { key: "death_date is bad", fr: "La date de décès semble incorrecte", penalty: 30 },
  { key: "continent of birth is unknown", fr: "Le continent de naissance est inconnu", penalty: 10 },
  { key: "continent of death is unknown", fr: "Le continent de décès est inconnu", penalty: 10 },
  { key: "birth_date is before the year 1900", fr: "La date de naissance est antérieure à 1900", penalty: 10 },
  { key: "age is unknown", fr: "L'âge est inconnu", penalty: 10 },
  { key: "age is unknown/younger than 16 and birth_date/death_date may be unknown too", fr: "L'âge est inconnu ou inférieur à 16 ans, et les dates de naissance et de décès peuvent également être inconnues", penalty: 10 },
  { key: "birth_date is after death_date", fr: "La date de naissance est postérieure à la date de décès", penalty: 40 },
  { key: "birth_date year is the same as death_date year so one of the date is wrong", fr: "L'année de naissance est identique à l'année de décès : l'une des deux dates est probablement incorrecte", penalty: 20 },
  { key: "User is born before christ", fr: "La personne est née avant Jésus-Christ", penalty: 30 },
  { key: "age is unknown and birth_date/death_date may be unknown too", fr: "L'âge est inconnu, et les dates de naissance et de décès peuvent également être inconnues", penalty: 0 },
  { key: "job is unknown", fr: "La profession est inconnu", penalty: 20 },
  { key: "User may have a bigger role than homme politique", fr: "Le metier de l'utilisateur est probablement plus précis que l'homme politique.", penalty: 4 },
  { key: "User may have a bigger role than femme politique", fr: "Le metier de l'utilisateur est probablement plus précis que femme politique.", penalty: 4 },
  { key: "User may have a bigger role than homme d'état", fr: "Le metier de l'utilisateur est probablement plus précis que homme d'état.", penalty: 4 },
  { key: "User may have a bigger role than femme d'état", fr: "Le metier de l'utilisateur est probablement plus précis que femme d'état.", penalty: 4 },
  { key: "death_day is undefined", fr: "Le jour de décès est inconnu", penalty: 4 },
]

const BY_KEY = new Map(UNPRECISENESS.map((item) => [item.key, item]))

// display_user_info renvoie les textes FR suivis d'une virgule : on retrouve la clé d'origine
export function to_unpreciseness_keys(values: unknown): string[] {
  if (!Array.isArray(values)) return []
  return values.map((value) => {
    const text = String(value).replace(/,$/, "").trim()
    return UNPRECISENESS.find((item) => item.fr === text || item.key === text)?.key ?? text
  })
}

// Comme le script : on part de 200, on retire les pénalités, puis on divise par 2
export function preciseness_level(keys: string[]): number {
  const total = keys.reduce((sum, key) => sum + (BY_KEY.get(key)?.penalty ?? 0), 0)
  return Math.trunc((200 - total) / 2)
}

const unknown = (value: string) => value.trim() === "" || value.trim().toLowerCase() === "undefined"

// Année signée : "-480-08-06" donne -480 (avant J.-C.)
function first_year(date: string): number | null {
  const before_christ = date.startsWith("-")
  const value = Number.parseInt((before_christ ? date.slice(1) : date).split("-")[0], 10) * (before_christ ? -1 : 1)
  return Number.isNaN(value) ? null : value
}

export type DetectSource = {
  town_birth_place: string, town_birth_localisation: string, country_birth_place: string, continent_of_birth: string,
  town_death_place: string, town_death_localisation: string, country_death_place: string, continent_of_death: string,
  birth_date: string, death_date: string, is_alive: string, gender: string, job: string, age: string,
}

// Imprécisions que le formulaire permet de recalculer (mêmes règles que le script)
export function detect_unpreciseness(form: DetectSource, born_before_christ: boolean, death_day: string): string[] {
  const dead = form.is_alive === "false"
  const birth_year = first_year(form.birth_date)
  const death_year = first_year(form.death_date)
  const age = Number(form.age)
  const found: string[] = []
  const add = (condition: boolean, key: string) => { if (condition) found.push(key) }

  add(unknown(form.town_birth_place), "town_birth_place is unknown")
  add(unknown(form.town_birth_localisation), "birth town localisation is unknown")
  add(unknown(form.country_birth_place), "country_birth_place is unknown")
  if (dead) {
    add(unknown(form.town_death_place), "town_death_place is unknown")
    add(unknown(form.country_death_place), "country_death_place is unknown")
    add(unknown(form.town_death_localisation), "death town localisation is unknown")
    add(form.birth_date === form.death_date && birth_year !== null, "birth_date and death_date may be the same")
    add(form.birth_date === form.death_date && birth_year === null, "birth_date and death_date are wrong")
  }
  add(form.birth_date.length < 2, "birth_date is bad")
  add(form.gender === "Unclear", "gender is unclear")
  add(dead && form.death_date.length < 2, "death_date is bad")
  add(unknown(form.continent_of_birth), "continent of birth is unknown")
  add(dead && unknown(form.continent_of_death), "continent of death is unknown")
  add(birth_year !== null && birth_year < 1900, "birth_date is before the year 1900")
  add(age === -999, "age is unknown")
  add(dead && !Number.isNaN(age) && age <= 15, "age is unknown/younger than 16 and birth_date/death_date may be unknown too")
  add(dead && birth_year !== null && death_year !== null && birth_year > death_year, "birth_date is after death_date")
  add(dead && birth_year !== null && death_year !== null && birth_year === death_year, "birth_date year is the same as death_date year so one of the date is wrong")
  add(born_before_christ, "User is born before christ")
  add(unknown(form.job), "job is unknown")
  add(dead && death_day === "Undefined", "death_day is undefined")
  return found
}

// Imprécisions que le formulaire ne permet pas de recalculer : on garde ce qui est coché
export const MANUAL_ONLY = new Set([
  "birthdate is between two date",
  "birth year is real but month and day are not",
  "death year is real but month and day are not",
  "age is unknown and birth_date/death_date may be unknown too",
  "User may have a bigger role than homme politique",
  "User may have a bigger role than femme politique",
  "User may have a bigger role than homme d'état",
  "User may have a bigger role than femme d'état",
])
