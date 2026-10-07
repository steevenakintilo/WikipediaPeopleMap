import { Suspense } from "react"
import { Link, NavLink, Outlet, useLocation } from "react-router-dom"
import { MenuIcon, MonitorIcon, MoonIcon, SunIcon } from "lucide-react"
import {
  Button,
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
  Spinner,
  useTheme,
} from "@steevenakintilo/ui"

import { LOGO_URL, LOGO_URL2 ,NAV_LINKS , NAV_LINKS2 } from "./nav_links.ts"

// Classe fixe (pas de fonction) : NavLink met aria-current="page" sur le lien actif,
// et SheetClose asChild ne sait fusionner que des className en chaîne
const nav_link_class = "flex items-center gap-2 rounded-md px-3 py-1.5 text-sm font-medium text-muted-foreground transition-colors hover:bg-muted hover:text-foreground aria-[current=page]:bg-muted aria-[current=page]:text-foreground"

function ThemeToggle() {
  const { setTheme } = useTheme()

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon" aria-label="Changer le thème">
          <SunIcon className="dark:hidden" />
          <MoonIcon className="hidden dark:block" />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={() => setTheme("light")}>
          <SunIcon /> Clair
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("dark")}>
          <MoonIcon /> Sombre
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("system")}>
          <MonitorIcon /> Système
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}

function MobileNav() {
  return (
    <Sheet>
      <SheetTrigger asChild>
        <Button variant="ghost" size="icon" className="md:hidden" aria-label="Ouvrir le menu">
          <MenuIcon />
        </Button>
      </SheetTrigger>
      <SheetContent side="right" className="w-72">
        <SheetHeader>
          <SheetTitle>Wikipedia People Map</SheetTitle>
          <SheetDescription>Naviguer dans le site</SheetDescription>
        </SheetHeader>
        <nav className="flex flex-col gap-1 px-4">
          {NAV_LINKS.map((link) => (
            <SheetClose asChild key={link.to}>
              <NavLink to={link.to} className={nav_link_class}>
                <link.icon className="size-4" />
                {link.label}
              </NavLink>
            </SheetClose>
          ))}
        </nav>
      </SheetContent>
    </Sheet>
  )
}

function SiteHeader() {
  return (
    <header className="sticky top-0 z-50 h-14 border-b bg-background/90 backdrop-blur">
      <div className="mx-auto flex h-full max-w-7xl items-center gap-2 px-4">
        <Link to="/Home" className="mr-auto flex items-center gap-2.5 font-semibold tracking-tight">
          <img src={LOGO_URL} alt="" className="size-8" />
          <span>WikipediaPeopleMap</span>
        </Link>
        <nav className="hidden items-center gap-1 md:flex">
          {NAV_LINKS.map((link) => (
            <NavLink key={link.to} to={link.to} className={nav_link_class}>
              {link.label}
            </NavLink>
          ))}
        </nav>
        <ThemeToggle />
        <MobileNav />
      </div>
    </header>
  )
}

function SiteHeader2() {
  return (
    <header className="sticky top-0 z-50 h-14 border-b bg-background/90 backdrop-blur">
      <div className="mx-auto flex h-full max-w-7xl items-center gap-2 px-4">
        <Link to="/Home" className="mr-auto flex items-center gap-2.5 font-semibold tracking-tight">
          <img src={LOGO_URL2} alt="" className="size-8" />
          <span>WikipediaPeopleMap</span>
        </Link>
        <nav className="hidden items-center gap-1 md:flex">
          {NAV_LINKS2.map((link) => (
            <NavLink key={link.to} to={link.to} className={nav_link_class}>
              {link.label}
            </NavLink>
          ))}
        </nav>
        <ThemeToggle />
        <MobileNav />
      </div>
    </header>
  )
}


function PageFallback() {
  return (
    <div role="status" className="flex flex-1 items-center justify-center gap-2 text-sm text-muted-foreground">
      <Spinner /> Chargement de la page…
    </div>
  )
}

const SiteLayout = () => {
  // L'accueil est lui-même le menu (gros boutons) : pas d'en-tête de navigation dessus
  const { pathname } = useLocation()
  const is_home = pathname === "/" || pathname === "/Home"  
  const is_game_menu = pathname === "/WikiGames" 
  const is_game = pathname === "/WhoIsOlder" 
  
  
  return (
    <div className="flex min-h-dvh flex-col">
      {!is_home && !is_game_menu && !is_game && <SiteHeader />}
      {is_game && <SiteHeader2 />}
      
      <Suspense fallback={<PageFallback />}>
        <Outlet />
      </Suspense>
    </div>
  )
}

export default SiteLayout
