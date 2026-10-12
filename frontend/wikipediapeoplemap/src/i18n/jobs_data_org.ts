import type { Entry } from "./jobs_data.ts"

// Vocabulaire pour traduire les noms d'organisations ("Parti communiste italien" -> "Italian Communist Party")
// et les listes de portefeuilles ("Culture, Médias et Sports"). Français sans accents, en minuscules.

// Noms d'institutions (tête du groupe nominal)
export const ORG_NOUNS: Entry[] = [
  ["parti", "Party"], ["conseil", "Council"], ["assemblee", "Assembly"], ["commission", "Commission"], ["comite", "Committee"],
  ["chambre", "Chamber"], ["senat", "Senate"], ["parlement", "Parliament"], ["congres", "Congress"], ["union", "Union"],
  ["ligue", "League"], ["front", "Front"], ["mouvement", "Movement"], ["bureau", "Bureau"], ["cour", "Court"], ["tribunal", "Court"],
  ["banque", "Bank"], ["ministere", "Ministry"], ["organisation", "Organization"], ["forum", "Forum"], ["fondation", "Foundation"],
  ["institut", "Institute"], ["academie", "Academy"], ["universite", "University"], ["association", "Association"],
  ["federation", "Federation"], ["confederation", "Confederation"], ["alliance", "Alliance"], ["coalition", "Coalition"],
  ["gouvernement", "Government"], ["republique", "Republic"], ["royaume", "Kingdom"], ["empire", "Empire"], ["etat", "State"],
  ["junte", "Junta"], ["cabinet", "Cabinet"], ["armee", "Army"], ["marine", "Navy"], ["service", "Service"], ["agence", "Agency"],
  ["office", "Office"], ["direction", "Directorate"], ["secretariat", "Secretariat"], ["centre", "Centre"], ["societe", "Society"],
  ["compagnie", "Company"], ["groupe", "Group"], ["club", "Club"], ["diete", "Diet"], ["douma", "Duma"], ["cortes", "Cortes"],
  ["presidium", "Presidium"], ["politburo", "Politburo"], ["directoire", "Directorate"], ["gouvernorat", "Governorate"],
  ["syndicat", "Union"], ["internationale", "International"], ["eglise", "Church"], ["ordre", "Order"], ["province", "Province"],
]

// Adjectifs : [anglais, classe]. Ordre anglais : origine, portée, type.
export type OrgAdjective = [english: string, rank: 0 | 1 | 2]

const ADJ_ENTRIES: [string, string, 0 | 1 | 2][] = [
  // portée (rang 1)
  ["national|nationale", "National", 1], ["central|centrale", "Central", 1], ["federal|federale", "Federal", 1],
  ["general|generale", "General", 1], ["supreme", "Supreme", 1], ["regional|regionale", "Regional", 1], ["local|locale", "Local", 1],
  ["international|internationale", "International", 1], ["europeen|europeenne", "European", 1], ["provincial|provinciale", "Provincial", 1],
  ["permanent|permanente", "Standing", 1], ["mondial|mondiale", "World", 1], ["municipal|municipale", "Municipal", 1],
  ["territorial|territoriale", "Territorial", 1], ["departemental|departementale", "Departmental", 1], ["populaire", "People's", 1],
  ["provisoire", "Provisional", 1], ["transitoire", "Transitional", 1], ["executif|executive", "Executive", 1],
  ["legislatif|legislative", "Legislative", 1], ["constituant|constituante", "Constituent", 1], ["presidentiel|presidentielle", "Presidential", 1],
  ["royal|royale", "Royal", 1], ["imperial|imperiale", "Imperial", 1], ["pontifical|pontificale", "Pontifical", 1],
  // type (rang 2)
  ["communiste", "Communist", 2], ["socialiste", "Socialist", 2], ["social-democrate", "Social Democratic", 2],
  ["democrate", "Democratic", 2], ["democratique", "Democratic", 2], ["republicain|republicaine", "Republican", 2],
  ["conservateur|conservatrice", "Conservative", 2], ["liberal|liberale", "Liberal", 2], ["travailliste", "Labour", 2],
  ["ecologiste", "Green", 2], ["nationaliste", "Nationalist", 2], ["monarchiste", "Monarchist", 2], ["fasciste", "Fascist", 2],
  ["militaire", "Military", 2], ["politique", "Political", 2], ["economique", "Economic", 2], ["social|sociale", "Social", 2],
  ["constitutionnel|constitutionnelle", "Constitutional", 2], ["revolutionnaire", "Revolutionary", 2], ["islamique", "Islamic", 2],
  ["chretien|chretienne", "Christian", 2], ["ouvrier|ouvriere", "Workers'", 2], ["paysan|paysanne", "Peasants'", 2],
  ["unifie", "United", 1], ["uni|unie", "United", 1], ["plurinational|plurinationale", "Plurinational", 1], ["orientale|oriental", "Eastern", 1], ["cooperatif|cooperative", "Cooperative", 2], ["parlementaire", "Parliamentary", 2], ["unitaire", "Unitary", 2], ["unioniste", "Unionist", 2], ["loyaliste", "Loyalist", 2], ["patriotique", "Patriotic", 2], ["patriote", "Patriotic", 2], ["salut", "Salvation", 2], ["populiste", "Populist", 2], ["progressiste", "Progressive", 2],
  ["radical|radicale", "Radical", 2], ["autonomiste", "Autonomist", 2], ["independantiste", "Independence", 2],
  ["judiciaire", "Judicial", 2], ["financier|financiere", "Financial", 2], ["commercial|commerciale", "Commercial", 2],
  ["scientifique", "Scientific", 2], ["culturel|culturelle", "Cultural", 2], ["sportif|sportive", "Sports", 2],
  ["olympique", "Olympic", 2], ["catholique", "Catholic", 2], ["orthodoxe", "Orthodox", 2], ["protestant|protestante", "Protestant", 2],
  ["musulman|musulmane", "Muslim", 2], ["juif|juive", "Jewish", 2], ["laique", "Secular", 2], ["agraire", "Agrarian", 2],
  ["syndical|syndicale", "Trade Union", 2], ["maritime", "Maritime", 2], ["aerien|aerienne", "Air", 2], ["secret|secrete", "Secret", 2],
  ["moderne", "Modern", 2], ["nouveau|nouvelle", "New", 2], ["grand|grande", "Great", 1],
]

// Portefeuilles supplémentaires (un mot ou un groupe : "Culture", "Médias", "Condition féminine"...)
export const PORTFOLIO_WORDS: Entry[] = [
  ["culture", "Culture"], ["medias", "Media"], ["sports", "Sport"], ["sport", "Sport"], ["alimentation", "Food"], ["agriculture", "Agriculture"],
  ["peche", "Fisheries"], ["tourisme", "Tourism"], ["commerce", "Trade"], ["commerce exterieur", "Foreign Trade"], ["industrie", "Industry"],
  ["education", "Education"], ["education de base", "Basic Education"], ["energie", "Energy"], ["electricite", "Electricity"],
  ["recherche", "Research"], ["famille", "Family"], ["condition feminine", "Women's Affairs"], ["femmes", "Women"], ["outre-mer", "Overseas Territories"],
  ["cooperation internationale", "International Cooperation"], ["cooperation", "Cooperation"], ["cooperation nordique", "Nordic Cooperation"],
  ["developpement", "Development"], ["developpement communautaire", "Community Development"], ["developpement constitutionnel", "Constitutional Development"], ["investissement", "Investment"],
  ["partenariat public-prive", "Public-Private Partnership"], ["economie numerique", "Digital Economy"], ["telecommunications", "Telecommunications"],
  ["postes", "Posts"], ["postes et des telecommunications", "Posts and Telecommunications"], ["information", "Information"], ["communication", "Communications"],
  ["sante", "Health"], ["bien-etre social", "Social Welfare"], ["affaires sociales", "Social Affairs"], ["affaires etrangeres", "Foreign Affairs"],
  ["affaires economiques", "Economic Affairs"], ["affaires autochtones", "Indigenous Affairs"], ["plan", "Planning"], ["finances", "Finance"],
  ["economie", "Economy"], ["budget", "Budget"], ["justice", "Justice"], ["droits de l'homme", "Human Rights"], ["citoyennete", "Citizenship"],
  ["interieur", "the Interior"], ["collectivites locales", "Local Government"], ["collectivites territoriales", "Territorial Authorities"], ["environnement", "the Environment"],
  ["defense", "Defence"], ["transports", "Transport"], ["transport", "Transport"], ["eaux", "Water"], ["travaux publics", "Public Works"],
  ["logement", "Housing"], ["urbanisme", "Urban Planning"], ["amenagement du territoire", "Regional Planning"], ["infrastructures", "Infrastructure"],
  ["territoire", "Territory"], ["mobilite durable", "Sustainable Mobility"], ["tourisme", "Tourism"], ["jeunesse", "Youth"], ["travail", "Labour"],
  ["emploi", "Employment"], ["population", "Population"], ["bien-etre", "Welfare"], ["securite sociale", "Social Security"], ["retraites", "Pensions"],
  ["fonction publique", "Public Service"], ["reforme agraire", "Agrarian Reform"], ["relations exterieures", "External Relations"],
  ["egalite des chances", "Equal Opportunities"], ["integration", "Integration"], ["immigration", "Immigration"], ["numerique", "Digital Affairs"],
  ["science", "Science"], ["sciences", "Science"], ["technologie", "Technology"], ["innovation", "Innovation"], ["enseignement superieur", "Higher Education"],
  ["education nationale", "National Education"], ["reconstruction", "Reconstruction"], ["guerre", "War"], ["marine", "the Navy"], ["armees", "the Armed Forces"],
  ["colonies", "the Colonies"], ["aviation", "Aviation"], ["cultes", "Religious Affairs"], ["affaires religieuses", "Religious Affairs"],
  ["petites et moyennes entreprises", "Small and Medium Enterprises"], ["pme", "SMEs"], ["artisanat", "Crafts"], ["consommation", "Consumer Affairs"],
  ["ville", "Urban Affairs"], ["affaires municipales", "Municipal Affairs"], ["affaires culturelles", "Cultural Affairs"], ["propagande", "Propaganda"],
  ["transition ecologique", "Ecological Transition"], ["solidarite", "Solidarity"], ["handicap", "Disability"], ["personnes agees", "Elderly Affairs"],
  ["formation professionnelle", "Vocational Training"], ["alphabetisation", "Literacy"], ["enfance", "Children"], ["securite", "Security"],
]

// Rôles qui prennent "Secretary of State for", "Minister of State for", etc.
export const ADJECTIVES: Map<string, OrgAdjective> = new Map()
for (const [forms, english, rank] of ADJ_ENTRIES) {
  for (const form of forms.split("|")) {
    ADJECTIVES.set(form, [english, rank])
  }
}
