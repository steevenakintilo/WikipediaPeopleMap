// Imports react
import {
  MapContainer,
  TileLayer,
  Popup,
  CircleMarker,
  useMap
} from "react-leaflet";

import { useEffect, useRef, useState } from 'react';
import { keepPreviousData, useQuery } from '@tanstack/react-query';
import {
  ChevronLeftIcon,
  ChevronRightIcon,

  ListIcon,
  MapPinIcon,

  SearchIcon,
  SearchXIcon,
  ShuffleIcon,
  SlidersHorizontalIcon,
} from "lucide-react";
import {
  Badge,
  Button,
  cn,
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  Skeleton,
  Spinner,
  toast,
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@steevenakintilo/ui";

import Legend from "./map_legend.tsx"

// Mes imports
import {gender_to_color , gender_to_color2} from "../utils/global_variable.tsx"
import { RANDOM_CHUNK, retry_if_failed, user_list_query } from "../api/queries.ts"
import { ActiveFilters, AdvancedSearchDialog } from "../components/advanced_search.tsx";
import { count_active_filters, MAP_FILTERS } from "../components/advanced_search_config.ts";
import { EmptyState, ErrorState , TooMuchRequestError} from "../components/page.tsx";
import { PersonPicture } from "../components/person_picture.tsx";
import { ProfileHost, type ProfileHostHandle } from "../components/user_profile_dialog.tsx";

const NO_DATA = {}
// Coordonnée renvoyée par le backend quand le lieu est inconnu
const UNKNOWN_LOCATION = 999999999999999
// Index de page affiché après un clic sur "Page aléatoire"
const RANDOM_PAGE_INDEX = 999999

const longitude_position_of_france = 6.6034
const latitude_position_of_france = 48.8883

// Recentre la carte à chaque nouvelle position demandée (map_view est un nouvel objet à chaque demande)
const MapController = ({ map_view }: { map_view: any }) => {
  const map = useMap();

  useEffect(() => {
    map.setView([map_view.latitude, map_view.longitude], map_view.zoom);
  }, [map_view, map]);

  return null;
};

// Mini logo Wikipédia d'origine (lien vers la page de la personne)
const WIKIPEDIA_LOGO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxw6xy-R6L-ethznPligpikS1nTohfbsiKoVEX6WlL3Q&s=10"
const PIN_BIRTH = "https://uxwing.com/wp-content/themes/uxwing/download/location-travel-map/map-pin-icon.png"
const PIN_DEATH = "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1788295917/pin_death_khphfd.png"
const PIN_UNKNOWN = "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1787351654/image_mobyht.png"

function is_known_location(localisation: any) {
  return localisation?.[0] !== UNKNOWN_LOCATION && localisation?.[1] !== UNKNOWN_LOCATION
}

function picture_of(user: any) {
  return decodeURIComponent(decodeURIComponent(user.picture_url))
}

type PersonRowProps = {
  user: any
  rank: number
  total: any
  on_locate: (localisation: any) => void
  on_open_profile: () => void
}

function PersonRow({ user, rank, total, on_locate, on_open_profile }: PersonRowProps) {
  const birth_known = is_known_location(user.birth_town_localisation)

  return (
    <li className="flex gap-3 px-4 py-3 transition-colors hover:bg-muted/40">
      <button type="button" className="shrink-0" onClick={on_open_profile} aria-label={`Profil de ${user.page_name}`}>
        <PersonPicture src={picture_of(user)} name={user.page_name} stretch className="size-[70px] cursor-pointer" />
      </button>
      <div className="min-w-0 flex-1 space-y-1">
        <div className="flex items-start justify-between gap-2">
          <button type="button" className="min-w-0 truncate text-left font-medium hover:underline" title={user.page_name} onClick={on_open_profile}>
            {user.page_name_shorter}
          </button>
          <span className="shrink-0 pt-0.5 text-xs text-muted-foreground tabular-nums">
            {rank}/{total}
          </span>
        </div>
        <div className="flex flex-wrap items-center gap-1">
          <Tooltip>
            <TooltipTrigger asChild>
              <span className="cursor-default text-lg leading-none" aria-label={user.birth_country_name}>{user.country_birth_place_emoji}</span>
            </TooltipTrigger>
            <TooltipContent>{user.birth_country_name}</TooltipContent>
          </Tooltip>
          {/* Mes pins d'origine : naissance, lieu non trouvé, mort */}
          <button
            type="button"
            className="shrink-0"
            disabled={!birth_known}
            title={birth_known ? "Lieu de naissance" : "Lieu de naissance non trouvé"}
            aria-label={birth_known ? "Voir le lieu de naissance" : "Lieu de naissance non trouvé"}
            onClick={() => on_locate(user.birth_town_localisation)}
          >
            <img src={birth_known ? PIN_BIRTH : PIN_UNKNOWN} alt="" className="size-[1.125rem] object-contain" />
          </button>
          {user.display_death_localisation == true && (
            <button
              type="button"
              className="shrink-0"
              disabled={!is_known_location(user.town_death_localisation)}
              title={is_known_location(user.town_death_localisation) ? "Lieu de mort" : "Lieu de mort non trouvé"}
              aria-label={is_known_location(user.town_death_localisation) ? "Voir le lieu de mort" : "Lieu de mort non trouvé"}
              onClick={() => on_locate(user.town_death_localisation)}
            >
              <img src={is_known_location(user.town_death_localisation) ? PIN_DEATH : PIN_UNKNOWN} alt="" className="size-[1.125rem] object-contain" />
            </button>
          )}
          <div className="ml-auto flex items-center gap-1">
            <Tooltip>
              <TooltipTrigger asChild>
                <Button variant="ghost" size="icon-xs" asChild>
                  <a href={user.page_url} target="_blank" rel="noopener noreferrer" aria-label="Page Wikipédia">
                    <img src={WIKIPEDIA_LOGO} alt="" className="size-[1.125rem] object-contain" />
                  </a>
                </Button>
              </TooltipTrigger>
              <TooltipContent>Page Wikipédia</TooltipContent>
            </Tooltip>
            <Button variant="outline" size="xs" onClick={on_open_profile}>
              + d'info
            </Button>
          </div>
        </div>
      </div>
    </li>
  )
}

const WorldMap = () => {
    const [my_geolocation,set_my_geolocalisation] : any = useState([])

    useEffect(() => {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const { latitude, longitude } = position.coords;

                set_my_geolocalisation([latitude,longitude])
            },
            (error) => {
                console.error(error);
            }
        );


    }, []);

    const [map_view,set_map_view] : any = useState({latitude: latitude_position_of_france, longitude: longitude_position_of_france, zoom: 6})
    const [searched_name,setsearched_name] : any = useState("")
    const [current_chunck_index,setchunck] = useState(0)
    // Ouvre la fiche (gérée par <ProfileHost>, hors de cette page pour ne pas re-rendre la carte)
    const profile_host = useRef<ProfileHostHandle>(null)
    const [filters_open,set_filters_open] = useState(false)
    // Panneau de la liste sur mobile
    const [panel_open,set_panel_open] = useState(false)
    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    // Une recherche avancée a été lancée : la pagination continue sur ses résultats
    const [advanced_search_launched,set_advanced_search_launched] = useState(false)

    // Liste demandée au backend : TanStack Query fait l'appel et garde chaque page en cache
    const [user_list_request,set_user_list_request] : any = useState({chunk: 0, search: null})
    const user_list = useQuery({
      ...user_list_query(user_list_request),
      // Garde la liste actuelle affichée pendant le chargement de la suivante
      placeholderData: keepPreviousData,
    })
    const list_of_user_data : any = user_list.data?.all_user_data ?? NO_DATA


    const active_filters_count = count_active_filters(MAP_FILTERS, dict_of_advance_search)

    // Déclarée avant ses usages : React Compiler ne gère pas les fonctions appelées avant leur déclaration
    function change_latitude_and_longitude(pos_x:number,pos_y:number) {
      if (pos_x != UNKNOWN_LOCATION && pos_y != UNKNOWN_LOCATION) {
        if (pos_x === 5 && pos_y === 20) {
          set_map_view({latitude: pos_x, longitude: pos_y, zoom: 2})
        } else {
          set_map_view({latitude: pos_x, longitude: pos_y, zoom: 30})

        }

      }

    }

    function get_list_of_user(chunk:number) {
      set_user_list_request({chunk: chunk, search: null})
    }


    function get_list_of_user_advanced_search(chunk:number,reset_chunck:boolean=false) {
      change_latitude_and_longitude(5,20)
      set_advanced_search_launched(true)
      set_filters_open(false)

      if (reset_chunck == true) {
        setchunck(0)
      }
      const request = {chunk: chunk, search: dict_of_advance_search}
      set_user_list_request(request)
      retry_if_failed(user_list_query(request).queryKey)
    }

    // Comme l'ancien bouton Reset (rechargement de la page) : filtres vidés et liste initiale
    function reset_search() {
      set_dict_of_advance_search({})
      set_advanced_search_launched(false)
      setchunck(0)
      get_list_of_user(0)
    }

    function handle_complete_profile_user(user:string) {
      // Le panneau mobile (modal) bloquerait le défilement de la fiche : on le ferme
      set_panel_open(false)
      profile_host.current?.open(user)
    }


    function handle_chunck(value:number) {

      if (value == 1) {
        setchunck(current_chunck_index + 1)

      } else if (current_chunck_index > 0) {
        setchunck(current_chunck_index - 1)
      }

      let index : number = current_chunck_index
      if (value == 1) {
        index = current_chunck_index + 1
      } else if (current_chunck_index > 0) {
        index = current_chunck_index - 1

      }

      if (value != 0 ) {
          if (Object.keys(dict_of_advance_search).length === 0 && advanced_search_launched == false) {
            get_list_of_user(index)

          } else {

            get_list_of_user_advanced_search(index)
          }

      } else  {
        // Page aléatoire : nouvel identifiant à chaque clic pour ne pas resservir le cache
        set_user_list_request({chunk: RANDOM_CHUNK, search: null, random_id: Date.now()})
        setchunck(RANDOM_PAGE_INDEX)

      }
    }

  function locate(localisation: any) {
    change_latitude_and_longitude(localisation[0], localisation[1])
    // Sur mobile, on referme la liste pour voir la carte
    set_panel_open(false)
  }

  function geolocate() {
    if (my_geolocation.length !== 2) {
      toast.error("Position indisponible", { description: "Autorisez l'accès à votre position dans le navigateur." })
      return
    }
    locate(my_geolocation)
  }

  function handle_searched_name(event:any) {
    setsearched_name(event.target.value)
  }

  // Rang affiché à côté de chaque personne (même calcul qu'avant)
  const number_of_people = Object.keys(list_of_user_data).length
  let start_index = current_chunck_index * number_of_people
  if (number_of_people != 500) {
    start_index = current_chunck_index * 500
    if ("number_of_people_to_display" in dict_of_advance_search) {
      start_index = current_chunck_index * dict_of_advance_search["number_of_people_to_display"]
    }
  }
  if (current_chunck_index == RANDOM_PAGE_INDEX) {
    start_index = 0
  }
  const total_number_of_people = list_of_user_data[number_of_people - 1]?.number_of_element

  const people = Object.values(list_of_user_data)
    .map((user: any, index: number) => ({ user, rank: start_index + index + 1 }))
    .filter(({ user }) => user.page_name.toLowerCase().includes(searched_name.toLowerCase()))

  const page_label = current_chunck_index == RANDOM_PAGE_INDEX ? "Page aléatoire" : `Page ${current_chunck_index + 1}`

  function render_people_list() {
    var too_much_request_status = ''
    if (user_list.error != null) {
      too_much_request_status = user_list.error.toString()
    }
    if (user_list.isPending) {
      return (
        <ul className="divide-y" aria-busy="true">
          {Array.from({ length: 6 }, (_, i) => (
            <li key={i} className="flex gap-3 px-4 py-3">
              <Skeleton className="size-14 rounded-lg" />
              <div className="flex-1 space-y-2 pt-1">
                <Skeleton className="h-4 w-40" />
                <Skeleton className="h-6 w-full" />
              </div>
            </li>
          ))}
        </ul>
      )
    }

    if (too_much_request_status == "ApiError: Erreur HTTP 429") {
      return( 
        <div className="p-4">
          <TooMuchRequestError description="Tu as fait trop de requêtes, patiente 15 minutes." on_retry={() => user_list.refetch()} />
        </div>
      )
      
    }
    else if (user_list.isError) {
      return (
        <div className="p-4">
          <ErrorState description="Impossible de charger la liste des personnes." on_retry={() => user_list.refetch()} />
        </div>
      )
    }

    else if (people.length === 0) {
      return (
        <div className="p-4">
          <EmptyState
            icon={<SearchXIcon />}
            title="Aucune personne trouvée"
            description={searched_name != "" ? `Personne sur cette page ne correspond à « ${searched_name} ».` : "Essayez d'autres filtres."}
          />
        </div>
      )
    }

    return (
      <ul className={cn("divide-y transition-opacity", user_list.isPlaceholderData && "opacity-60")}>
        {people.map(({ user, rank }) => (
          <PersonRow
            key={rank}
            user={user}
            rank={rank}
            total={total_number_of_people}
            on_locate={locate}
            on_open_profile={() => handle_complete_profile_user(user.page_name)}
          />
        ))}
      </ul>
    )
  }

  function render_panel() {
    return (
      <div className="flex min-h-0 flex-1 flex-col">
        <div className="space-y-3 border-b p-4">
          <InputGroup>
            <InputGroupAddon>
              <SearchIcon />
            </InputGroupAddon>
            <InputGroupInput
              placeholder="Filtrer cette page par nom"
              aria-label="Filtrer cette page par nom"
              value={searched_name}
              onChange={(event) => handle_searched_name(event)}
            />
          </InputGroup>
          <div className="flex flex-wrap gap-2">
            <Button variant="outline" className="flex-1" onClick={() => set_filters_open(true)}>
              <SlidersHorizontalIcon /> Filtres avancés
              {active_filters_count > 0 && <Badge className="ml-1">{active_filters_count}</Badge>}
            </Button>
            <Tooltip>
              <TooltipTrigger asChild>
                <Button variant="outline" size="icon" onClick={() => geolocate()} aria-label="Me géolocaliser">
                  <MapPinIcon />
                </Button>
              </TooltipTrigger>
              <TooltipContent>Me géolocaliser</TooltipContent>
            </Tooltip>
            <Tooltip>
              <TooltipTrigger asChild>
                <Button variant="outline" size="icon" onClick={() => handle_chunck(0)} aria-label="Page aléatoire">
                  <ShuffleIcon />
                </Button>
              </TooltipTrigger>
              <TooltipContent>Page aléatoire</TooltipContent>
            </Tooltip>
          </div>
          <ActiveFilters sections={MAP_FILTERS} filters={dict_of_advance_search} set_filters={set_dict_of_advance_search} />
        </div>

        <div className="flex items-center justify-between border-b px-2 py-1.5">
          <Button variant="ghost" size="sm" onClick={() => handle_chunck(-1)} disabled={current_chunck_index == 0}>
            <ChevronLeftIcon /> Précédente
          </Button>
          <span className="flex items-center gap-2 text-sm font-medium">
            {user_list.isFetching && <Spinner className="size-3.5" />}
            {page_label}
          </span>
          <Button variant="ghost" size="sm" onClick={() => handle_chunck(+1)}>
            Suivante <ChevronRightIcon />
          </Button>
        </div>

        <div className="min-h-0 flex-1 overflow-y-auto">
          {render_people_list()}
        </div>
      </div>
    )
  }

  return (
    <main className="flex h-[calc(100dvh-3.5rem)] min-h-0">
      {/* isolate : les calques Leaflet restent sous les fenêtres (Dialog, Sheet…) */}
      <div className="relative isolate min-w-0 flex-1">
        <MapContainer
          minZoom={2}
          maxZoom={18}
          zoomControl={true}
          scrollWheelZoom={true}
          className="size-full"
        >

        <MapController map_view={map_view} />
          <TileLayer
            attribution="&copy; Google Maps"
            url="https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
            subdomains={["mt0", "mt1", "mt2", "mt3"]}
          />
          {Object.values(list_of_user_data).map((user:any,index:number) =>

              is_known_location(user.birth_town_localisation) && (

              <CircleMarker
              key={index}
              center={((user.birth_town_localisation))}
              radius={10}
              pathOptions={{
                fillColor: gender_to_color[`${user.gender}${user.is_alive}`],
                color: gender_to_color[`${user.gender}${user.is_alive}`],
                fillOpacity: 0.3
              }}
              >
                  <Popup>
                    <div className="flex w-[250px] flex-col gap-2">
                      <button type="button" onClick={() => handle_complete_profile_user(user.page_name)} aria-label={`Profil de ${user.page_name}`}>
                        <PersonPicture src={picture_of(user)} name={user.page_name} stretch className="size-[250px] cursor-pointer [&_[data-slot=avatar-fallback]]:text-4xl" />
                      </button>
                      <p className="text-sm leading-snug font-medium">{user.page_name}</p>
                      <div className="flex flex-wrap gap-1.5">
                        <Button size="xs" onClick={() => handle_complete_profile_user(user.page_name)}>+ d'info</Button>
                        <Button size="xs" variant="outline" onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1])}>
                          <MapPinIcon /> Centrer
                        </Button>
                      </div>
                    </div>
                  </Popup>

              </CircleMarker>
              )

          )}


          {Object.values(list_of_user_data).map((user:any , index:number) =>

              is_known_location(user.town_death_localisation) && user.display_death_localisation == true && (

              <CircleMarker
              key={index}
              center={((user.town_death_localisation))}
              radius={10}
              pathOptions={{
                fillColor: gender_to_color2[`${user.gender}${user.is_alive}`],
                color: gender_to_color2[`${user.gender}${user.is_alive}`],
                fillOpacity: 0.3
              }}
              >
                  <Popup>
                    <div className="flex w-[250px] flex-col gap-2">
                      <a href={user.page_url} target="_blank" rel="noopener noreferrer" aria-label="Page Wikipédia">
                        <PersonPicture src={picture_of(user)} name={user.page_name} stretch className="size-[250px] cursor-pointer [&_[data-slot=avatar-fallback]]:text-4xl" />
                      </a>
                      <p className="text-sm leading-snug font-medium">{user.page_name} <span className="font-normal text-muted-foreground">(lieu de décès)</span></p>
                      <div className="flex flex-wrap gap-1.5">
                        <Button size="xs" onClick={() => handle_complete_profile_user(user.page_name)}>+ d'info</Button>
                        <Button size="xs" variant="outline" onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1])}>
                          <MapPinIcon /> Lieu de naissance
                        </Button>
                      </div>
                    </div>
                  </Popup>

              </CircleMarker>
              )

          )}

        </MapContainer>

        <Legend className="absolute bottom-3 left-3 z-[1000]" />

        {user_list.isFetching && (
          <div className="absolute top-3 left-1/2 z-[1000] flex -translate-x-1/2 items-center gap-2 rounded-full border bg-background/95 px-3 py-1.5 text-xs font-medium shadow-md">
            <Spinner className="size-3.5" /> Chargement…
          </div>
        )}

        <Button className="absolute top-3 right-3 z-[1000] shadow-md md:hidden" onClick={() => set_panel_open(true)}>
          <ListIcon /> Liste
          {active_filters_count > 0 && <Badge variant="secondary" className="ml-1">{active_filters_count}</Badge>}
        </Button>
      </div>

      {/* Ordinateur : liste toujours visible à droite */}
      <aside className="hidden w-[400px] shrink-0 flex-col border-l md:flex">
        {render_panel()}
      </aside>

      {/* Mobile : liste dans un panneau qui monte du bas */}
      <Sheet open={panel_open} onOpenChange={set_panel_open}>
        <SheetContent side="bottom" className="gap-0 p-0 data-[side=bottom]:h-[85dvh]" onOpenAutoFocus={(event) => event.preventDefault()}>
          <SheetHeader className="border-b">
            <SheetTitle>Personnes · {page_label}</SheetTitle>
            <SheetDescription>Touchez un pin pour voir le lieu sur la carte.</SheetDescription>
          </SheetHeader>
          {render_panel()}
        </SheetContent>
      </Sheet>

      <AdvancedSearchDialog
        open={filters_open}
        on_open_change={set_filters_open}
        sections={MAP_FILTERS}
        filters={dict_of_advance_search}
        set_filters={set_dict_of_advance_search}
        on_search={() => get_list_of_user_advanced_search(current_chunck_index,true)}
        on_reset={() => reset_search()}
      />

      <ProfileHost ref={profile_host} />
    </main>

  );
};

export default WorldMap;
