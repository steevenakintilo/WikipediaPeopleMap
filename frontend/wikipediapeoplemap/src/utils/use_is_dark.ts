import { useSyncExternalStore } from "react"
import { useTheme } from "@steevenakintilo/ui"

const DARK_QUERY = "(prefers-color-scheme: dark)"

function subscribe(on_change: () => void) {
  const query = window.matchMedia(DARK_QUERY)
  query.addEventListener("change", on_change)
  return () => query.removeEventListener("change", on_change)
}

// Thème réellement affiché (le choix "système" suit le réglage de l'OS).
// Nom en camelCase obligatoire : React (et React Compiler) reconnaît les hooks au motif "useXxx".
export function useIsDark() {
  const { theme } = useTheme()
  const system_is_dark = useSyncExternalStore(subscribe, () => window.matchMedia(DARK_QUERY).matches)
  return theme === "dark" || (theme === "system" && system_is_dark)
}
