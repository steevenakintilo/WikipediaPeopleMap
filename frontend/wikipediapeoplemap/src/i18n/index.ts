import i18n from "i18next"
import { initReactI18next, useTranslation } from "react-i18next"

import en from "./en.json"

// Le texte français du code sert de clé : le français n'a donc aucune traduction à déclarer,
// et une clé absente de en.json s'affiche telle quelle (en français) au lieu de planter.
export const LANGUAGES = [
  { code: "fr", label: "Français" },
  { code: "en", label: "English" },
] as const

export type LanguageCode = (typeof LANGUAGES)[number]["code"]

const STORAGE_KEY = "lang"

function initial_language(): LanguageCode {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)
    if (saved === "fr" || saved === "en") {
      return saved
    }
  } catch {
    // stockage indisponible (navigation privée…) : on retombe sur la langue du navigateur
  }
  return navigator.language?.toLowerCase().startsWith("fr") ? "fr" : "en"
}

i18n.use(initReactI18next).init({
  resources: {
    fr: { translation: {} },
    en: { translation: en },
  },
  lng: initial_language(),
  fallbackLng: "fr",
  keySeparator: false,
  nsSeparator: false,
  interpolation: { escapeValue: false },
})

function apply_language(language: string) {
  document.documentElement.lang = language
  try {
    localStorage.setItem(STORAGE_KEY, language)
  } catch {
    // le choix ne sera simplement pas mémorisé
  }
}

apply_language(i18n.language)
i18n.on("languageChanged", apply_language)

// Format des nombres selon la langue affichée (se met à jour au changement de langue)
export function useNumberFormat() {
  const { i18n: instance } = useTranslation()
  const locale = instance.language === "en" ? "en-US" : "fr-FR"
  return (value: any) => (typeof value === "number" ? value.toLocaleString(locale) : value)
}

export default i18n
