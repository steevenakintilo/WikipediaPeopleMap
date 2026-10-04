import { AgCharts } from "ag-charts-react"
import { AllCommunityModule, ModuleRegistry } from "ag-charts-community"
import { Button } from "@steevenakintilo/ui"

import { useIsDark } from "../utils/use_is_dark.ts"

ModuleRegistry.registerModules([AllCommunityModule])

// Graphique AgCharts avec ses options d'origine (pleine largeur, titre et couleur du graphique),
// puis le bouton vers le tableau détaillé. Seul ajout : le fond sombre d'AG Charts en mode sombre.
export function StatChartCard({ options, on_show_table }: { options: any, on_show_table: () => void }) {
  const is_dark = useIsDark()

  return (
    <div className="space-y-4">
      <AgCharts options={is_dark ? { ...options, theme: "ag-default-dark" } : options} />
      <Button variant="secondary" className="w-full" onClick={on_show_table}>
        Toutes les statistiques 📊
      </Button>
    </div>
  )
}
