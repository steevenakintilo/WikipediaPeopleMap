// Imports react
import {
  MapContainer,
  TileLayer,
  CircleMarker,
  useMap
} from "react-leaflet";

import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Helmet } from 'react-helmet-async';
import { Button, cn } from "@steevenakintilo/ui";

// Mes imports
import { random_localisation_in_france } from "../utils/global_variable.tsx"
import { LOGO_URL } from "../components/nav_links.ts";

const SITE_URL = "https://wikipediapeoplemap.com"
const SITE_TITLE = "Wikipedia People Map - La carte des personnes de Wikipédia"
const SITE_DESCRIPTION = "Explorez sur une carte interactive les lieux de naissance et de décès des personnes ayant une page Wikipédia en français, avec des statistiques et des filtres avancés."
const PREVIEW_IMAGE = `${SITE_URL}/logo-preview.png`


const longitude_position_of_france = 6.6034
const latitude_position_of_france = 48.8883

// Menu de l'accueil : un bouton par page, avec une courte explication
const HOME_MENU = [
  {
    id: "WorldMapPageButton",
    to: "/WorldMap",
    label: "Explorer la Map",
    description: "",
  },
  {
    id: "StatisticsPageButton",
    to: "/Statistics",
    label: "Statistiques détaillées",
    description: "",
  },
  {
    id: "OtherStatisticsPageButton",
    to: "/OtherStatistics",
    label: "Autres statistiques",
    description: "",
  },
  {
    id: "QjisMapPageButton",
    to: "/Qjis",
    label: "Carte pour QGIS",
    description: "",
    desktop_only: true,
  },
  {
    id: "AboutPageButton",
    to: "/About",
    label: "À propos",
    description: "",
  },
]

const MapController = ({
  latitude,
  longitude,
  zoom,
}: {
  latitude: number;
  longitude: number;
  zoom: number;
}) => {
  const map = useMap();


  useEffect(() => {
    map.setView([latitude, longitude], zoom);
  }, [latitude, longitude, zoom, map]);

  return null;
};

const Home = () => {
  // Mélangé une seule fois par affichage de la page (copie : le tableau global n'est plus modifié)
  const [list_of_random_position] : any = useState(() => [...random_localisation_in_france].sort(() => Math.random() - 0.5));

  return (
    <main className="flex min-h-dvh">
       <Helmet>
        <html lang="fr" />
        <title>{SITE_TITLE}</title>
        <meta name="description" content={SITE_DESCRIPTION} />
        <link rel="canonical" href={`${SITE_URL}/`} />

        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="Wikipedia People Map" />
        <meta property="og:title" content={SITE_TITLE} />
        <meta property="og:description" content={SITE_DESCRIPTION} />
        <meta property="og:url" content={`${SITE_URL}/`} />
        <meta property="og:image" content={PREVIEW_IMAGE} />
        <meta property="og:locale" content="fr_FR" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={SITE_TITLE} />
        <meta name="twitter:description" content={SITE_DESCRIPTION} />
        <meta name="twitter:image" content={PREVIEW_IMAGE} />
      </Helmet>
      <h1 className="sr-only">Wikipedia People Map</h1>

      {/* Ordinateur : la carte prend toute la hauteur, à gauche du menu */}
      <div className="sticky top-0 isolate hidden h-dvh min-w-0 flex-1 border-r-2 border-neutral-500 md:block">
        <MapContainer
          minZoom={2}
          maxZoom={18}
          zoomControl={true}
          scrollWheelZoom={true}
          className="size-full"
        >

        <MapController
          latitude={latitude_position_of_france}
          longitude={longitude_position_of_france}
          zoom={6}
        />


          <TileLayer
            attribution="&copy; Google Maps"
            url="https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
            subdomains={["mt0", "mt1", "mt2", "mt3"]}
          />

          {list_of_random_position.slice(0, 100).map((position:any,index:number) =>

            (
              <CircleMarker
                key={index}
                center={((position))}
                radius={10}
                pathOptions={{
                  fillColor: "black",
                  color: "black",
                  fillOpacity: 0.3
                }}
              >
              </CircleMarker>
            )

          )}

        </MapContainer>
      </div>

      <div className="flex w-full flex-col items-center justify-center gap-5 px-4 py-5 md:h-dvh md:w-[520px] md:shrink-0">
        <img
          src={LOGO_URL}
          alt=""
          className="size-[270px] max-w-full object-contain md:h-auto md:max-h-[50dvh] md:w-full"
        />

        <nav aria-label="Pages du site" className="flex flex-col items-center gap-3.5">
          {HOME_MENU.map((item) => (
            <div key={item.id} className={cn("flex-col items-center gap-1 text-center", item.desktop_only ? "hidden md:flex" : "flex")}>
              <Button
                asChild
                className="h-auto w-72 rounded-[5px] bg-[#212529] px-5 py-2.5 text-xl font-normal text-white hover:bg-[#424649] dark:ring-1 dark:ring-white/20"
              >
                <Link id={item.id} to={item.to}>{item.label}</Link>
              </Button>
              <p className="max-w-sm text-xs text-pretty text-muted-foreground">{item.description}</p>
            </div>
          ))}
        </nav>
      </div>
    </main>
  );
};

export default Home;
