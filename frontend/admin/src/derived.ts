// Champs calculés à partir des dates, pays et continents (même logique que le backend)

const NUMBER_TO_MONTH: Record<string, string> = {
  "01": "janvier", "02": "février", "03": "mars", "04": "avril", "05": "mai", "06": "juin",
  "07": "juillet", "08": "août", "09": "septembre", "10": "octobre", "11": "novembre", "12": "décembre",
  "13": "fluriel",
}

const WEEK_DAYS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

const UNDEFINED = "Undefined"
const UNKNOWN_YEAR = 123456789

const REGIONS: Record<string, string[]> = {
  "Europe du Nord": ["Angleterre", "Danemark", "Estonie", "Écosse", "Finlande", "Irlande", "Irlande du Nord", "Islande", "Lettonie", "Lituanie", "Norvège", "Pays de Galles", "Royaume-Uni", "Suède"],
  "Europe de l'Ouest": ["Allemagne", "Andorre", "Autriche", "Belgique", "France", "Liechtenstein", "Luxembourg", "Monaco", "Pays-Bas", "Suisse"],
  "Europe du Sud": ["Albanie", "Bosnie-Herzégovine", "Chypre", "Chypre du Nord", "Croatie", "Espagne", "Grèce", "Italie", "Kosovo", "Macédoine", "Macédoine du Nord", "Malte", "Monténégro", "Portugal", "Saint-Marin", "Serbie", "Slovénie", "Vatican"],
  "Europe de l'Est": ["Biélorussie", "Moldavie", "Pologne", "République tchèque", "Roumanie", "Slovaquie", "Ukraine", "Russie"],
  "Afrique du Nord": ["Algérie", "Égypte", "Libye", "Maroc", "Soudan", "Tunisie"],
  "Afrique de l'Ouest": ["Bénin", "Burkina Faso", "Cap-Vert", "Côte d'Ivoire", "Gambie", "Ghana", "Guinée", "Guinée-Bissau", "Liberia", "Mali", "Mauritanie", "Niger", "Nigeria", "Sénégal", "Sierra Leone", "Togo"],
  "Afrique centrale": ["Angola", "Burundi", "Cameroun", "République centrafricaine", "République du Congo", "République démocratique du Congo", "Gabon", "Guinée équatoriale", "Rwanda", "São Tomé-et-Principe", "Tchad"],
  "Afrique de l'Est": ["Comores", "Djibouti", "Érythrée", "Éthiopie", "Kenya", "Madagascar", "Malawi", "Maurice", "Mozambique", "Ouganda", "Seychelles", "Somalie", "Soudan du Sud", "Tanzanie", "Zambie", "Zimbabwe"],
  "Afrique australe": ["Afrique du Sud", "Botswana", "Eswatini", "Lesotho", "Namibie"],
  "Moyen-Orient": ["Arabie saoudite", "Bahreïn", "Émirats arabes unis", "Irak", "Iran", "Israël", "Jordanie", "Koweït", "Liban", "Oman", "Palestine", "Qatar", "Syrie", "Turquie", "Yémen"],
  "Asie centrale": ["Afghanistan", "Kazakhstan", "Kirghizistan", "Ouzbékistan", "Tadjikistan", "Turkménistan"],
  "Asie de l'Est": ["Chine", "Corée du Nord", "Corée du Sud", "Japon", "Mongolie", "Taïwan", "Taiwan"],
  "Asie du Sud": ["Bangladesh", "Bhoutan", "Inde", "Maldives", "Népal", "Pakistan", "Sri Lanka"],
  "Asie du Sud-Est": ["Birmanie", "Brunei", "Cambodge", "Indonésie", "Laos", "Malaisie", "Philippines", "Singapour", "Thaïlande", "Timor oriental", "Viêt Nam"],
  "Caucase": ["Abkhazie", "Arménie", "Azerbaïdjan", "Géorgie", "Ossétie du Sud-Alanie"],
  "Amérique anglo-saxonne": ["Canada", "États-Unis"],
  "Amérique centrale": ["Belize", "Costa Rica", "Guatemala", "Honduras", "Mexique", "Nicaragua", "Panama", "Salvador"],
  "Caraïbes": ["Antigua-et-Barbuda", "Bahamas", "Barbade", "Cuba", "Dominique", "Grenade", "Haïti", "Jamaïque", "République dominicaine", "Saint-Christophe-et-Niévès", "Sainte-Lucie", "Saint-Vincent-et-les Grenadines", "Trinité-et-Tobago"],
  "Amérique du Sud": ["Argentine", "Bolivie", "Brésil", "Chili", "Colombie", "Équateur", "Guyana", "Paraguay", "Pérou", "Suriname", "Uruguay", "Venezuela"],
  "Australasie": ["Australie", "Nouvelle-Zélande"],
  "Mélanésie": ["Fidji", "Papouasie-Nouvelle-Guinée", "Îles Salomon", "Vanuatu"],
  "Micronésie": ["Kiribati", "Îles Marshall", "Micronésie", "Nauru", "Palaos"],
  "Polynésie": ["Îles Cook", "Niue", "Samoa", "Tonga", "Tuvalu"],
}

// En base les pays sont en minuscules et sans tiret ("états unis")
function normalize(country: string): string {
  return country.trim().toLowerCase().replaceAll("-", " ")
}

const COUNTRY_TO_REGION = new Map(
  Object.entries(REGIONS).flatMap(([region, countries]) => countries.map((country) => [normalize(country), region] as const)),
)

function region_of(country: string): string {
  return COUNTRY_TO_REGION.get(normalize(country)) ?? ""
}

function is_known(value: string): boolean {
  return value.trim() !== "" && value.trim().toLowerCase() !== "undefined"
}

type ParsedDate = { year: number, month: string, day: string }

// Format année-mois-jour, avec un "-" devant pour avant Jésus-Christ ("-480-08-06")
function parse_date(date: string): ParsedDate | null {
  const before_christ = date.startsWith("-")
  const parts = (before_christ ? date.slice(1) : date).split("-")
  if (parts.length !== 3 || !/^\d+$/.test(parts[0])) return null
  const year = Number(parts[0]) * (before_christ ? -1 : 1)
  return { year, month: parts[1], day: parts[2] }
}

function week_day(date: string, parsed: ParsedDate | null): string {
  if (date.includes("-13-99")) return "Charbre"
  if (!parsed) return UNDEFINED
  const month = Number(parsed.month)
  const day = Number(parsed.day)
  if (!(month >= 1 && month <= 12 && day >= 1 && day <= 31)) return UNDEFINED
  const value = new Date(Date.UTC(2000, month - 1, day))
  // Comme le backend : avant J.-C. le jour est calculé sur l'année positive (-480 → 480)
  value.setUTCFullYear(Math.abs(parsed.year))
  if (value.getUTCDate() !== day) return UNDEFINED
  // getUTCDay : 0 = dimanche, la liste commence au lundi
  return WEEK_DAYS[(value.getUTCDay() + 6) % 7]
}

function date_fields(date: string, prefix: "birth" | "death", week_day_field: string) {
  const parsed = parse_date(date)
  const month = parsed ? NUMBER_TO_MONTH[parsed.month] : undefined
  const day = parsed && /^\d{2}$/.test(parsed.day) ? parsed.day : undefined
  return {
    [`${prefix}_year`]: parsed ? parsed.year : UNKNOWN_YEAR,
    [`${prefix}_month`]: month ?? UNDEFINED,
    [`${prefix}_day`]: day ?? UNDEFINED,
    [`${prefix}_month_day`]: month && day ? `${day}-${month}` : UNDEFINED,
    [week_day_field]: week_day(date, parsed),
  }
}

const bool = (value: boolean) => (value ? "True" : "False")

const same = (a: string, b: string) => is_known(a) && is_known(b) && normalize(a) === normalize(b)

export type DerivedSource = {
  birth_date: string, death_date: string,
  town_birth_place: string, town_death_place: string,
  country_birth_place: string, country_death_place: string,
  continent_of_birth: string, continent_of_death: string,
}

export function derive_fields(form: DerivedSource): Record<string, string | number> {
  const birth = parse_date(form.birth_date)
  const death = parse_date(form.death_date)
  const born_bc = !!birth && birth.year < 0
  const died_bc = !!death && death.year < 0
  const birth_region = region_of(form.country_birth_place)

  return {
    ...date_fields(form.birth_date, "birth", "week_day_of_birth"),
    ...date_fields(form.death_date, "death", "week_day_of_death"),
    born_and_died_in_the_same_town: bool(same(form.town_birth_place, form.town_death_place)),
    born_and_died_in_the_same_country: bool(same(form.country_birth_place, form.country_death_place)),
    born_and_died_in_the_same_continent: bool(same(form.continent_of_birth, form.continent_of_death)),
    born_and_died_in_the_same_region: bool(!!birth_region && birth_region === region_of(form.country_death_place)),
    born_before_christ: bool(born_bc),
    died_before_christ: bool(died_bc),
    born_and_died_before_christ: bool(born_bc && died_bc),
    born_and_died_after_christ: bool(!!birth && !!death && !born_bc && !died_bc),
    born_before_christ_and_died_after_christ: bool(born_bc && !!death && !died_bc),
  }
}
