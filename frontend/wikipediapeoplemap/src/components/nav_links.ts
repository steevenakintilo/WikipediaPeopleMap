import { ChartColumnIcon, FileDownIcon, InfoIcon, MapIcon, ChartPieIcon, HouseIcon } from "lucide-react"

export const LOGO_URL = "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1789683297/how-to-draw-an-earth-step-6_1_go2k7j.jpg"
export const LOGO_URL2 = "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1791294374/wikigaming_igxgda.jpg"

// Pages du site : utilisées par l'en-tête et le menu mobile
export const NAV_LINKS = [
  { to: "/WorldMap", label: "Carte", icon: MapIcon },
  { to: "/Statistics", label: "Statistiques", icon: ChartColumnIcon },
  { to: "/OtherStatistics", label: "Autres statistiques", icon: ChartPieIcon },
  { to: "/Qjis", label: "Export QGIS", icon: FileDownIcon },
  { to: "/About", label: "À propos", icon: InfoIcon },  
]

export const NAV_LINKS2 = [
  { to: "/WhoIsOlder", label: "Qui est né avant?", icon: InfoIcon },
  { to: "/WikiGames", label: "Menu", icon: HouseIcon },
  
]
