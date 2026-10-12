import { list_of_countries } from "../utils/global_variable.tsx"
import { translate_job_to_english } from "./jobs.ts"

// Traduction des valeurs qui viennent du backend (pays, causes de décès, erreurs…).
// Le backend les écrit en français, souvent en minuscules et sans accents ("etats-unis", "royaume uni").
type Translate = (text: string) => string

function normalize(text: string) {
  return text
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[-’']/g, " ")
    .replace(/\s+/g, " ")
    .trim()
}

const PLACE_BY_NORMALIZED_NAME = new Map(list_of_countries.map((name) => [normalize(name), name]))

// Pays, continent ou région : retrouve le nom d'origine ("États-Unis") quelle que soit l'écriture reçue
export function translate_place(name: any, t: Translate) {
  if (typeof name !== "string") {
    return name
  }
  return t(PLACE_BY_NORMALIZED_NAME.get(normalize(name)) ?? name)
}

// Texte libre en minuscules dans en.json (causes de décès, erreurs) : on cherche la version minuscule
// puis on remet la majuscule du début si le texte reçu en avait une
export function translate_text(text: any, t: Translate) {
  if (typeof text !== "string") {
    return text
  }
  const key = text.toLowerCase().replace(/’/g, "'")
  const translated = t(key)
  if (translated === key) {
    return text
  }
  return text[0] === text[0].toUpperCase() ? translated[0].toUpperCase() + translated.slice(1) : translated
}

// Les métiers n'ont qu'une traduction anglaise : en français on garde le texte d'origine.
// (t("Oui") ne change que si la langue affichée n'est pas le français)
export function translate_job(job: any, t: Translate) {
  if (typeof job !== "string" || t("Oui") === "Oui") {
    return job
  }
  return translate_job_to_english(job, (name) => translate_place(name, t)) ?? job
}

// Traducteur des libellés d'un graphique selon la statistique (sa clé côté backend) : seules les
// statistiques de pays / continents / régions, causes de décès et erreurs sont traduites
// (traduire un prénom comme "Maurice" en "Mauritius" serait une erreur).
export function data_name_translator(key: string, t: Translate): (name: any) => any {
  if (/^(country|continent|region)_/.test(key)) {
    return (name) => translate_place(name, t)
  }
  if (key === "job") {
    return (name) => translate_job(name, t)
  }
  if (key === "cause_of_death" || key === "dict_of_error") {
    return (name) => translate_text(name, t)
  }
  return (name) => name
}

// Même chose pour les classements, dont la clé est le titre français ("Liste des pays classé(e)s…")
export function ranking_name_translator(title: string, t: Translate): (name: any) => any {
  if (/^Liste des (pays|continents|régions)/.test(title)) {
    return (name) => translate_place(name, t)
  }
  if (/^Liste des métiers/.test(title)) {
    return (name) => translate_job(name, t)
  }
  return (name) => name
}
