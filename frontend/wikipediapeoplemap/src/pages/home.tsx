// Imports react
import {
  MapContainer,
  TileLayer,
  CircleMarker,
  useMap
} from "react-leaflet";

import {random_localisation_in_france} from "./global_variable.tsx"
import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";

import { useEffect, useState } from 'react';

import "leaflet/dist/leaflet.css";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

polyfillCountryFlagEmojis();

// Mes imports
import "./global.css";

const Home = () => {
  var list_of_random_position : any = []
  var list_of_random_position : any = random_localisation_in_france.sort(() => Math.random() - 0.5);

  const longitude_position_of_france = 6.6034
  const latitude_position_of_france = 48.8883
  const [longitude] = useState(longitude_position_of_france)
  const [latitude] = useState(latitude_position_of_france)
  const [zoom] = useState(6)
  
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

  return (

    <div>   

      <div className="d-flex align-items-stretch min-vh-100">
        <div className="map-wrapper border-end border-end border-2 border-secondary desktop-only"
          style={{
            position: "sticky",
            top: 0,
            height: "100vh",
          }}
        >
          <MapContainer
            minZoom={2}
            maxZoom={18}
            zoomControl={true}
            scrollWheelZoom={true}
            className="world-map"
          >

          <MapController
            latitude={latitude}
            longitude={longitude}
            zoom={zoom}
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
        <div className="desktop-only" style={{flexShrink:0 }}>
            <div className="card">
              <ul className="list-group list-group-flush">
              <div>
              
              <img src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1789683297/how-to-draw-an-earth-step-6_1_go2k7j.jpg" style={{ cursor: "pointer" }} alt="" width="500" height="440" className="me-2"/>
              </div>
              <br></br>
              <br></br>
              
              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/WorldMap">Explorer la Map</a>
              <br></br>
              
              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/Statistics">Statistiques détaillées</a>
              <br></br>

              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/OtherStatistics">Autres statistiques</a>
              <br></br>

              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/Qjis">Carte pour qjis</a>
              <br></br>
              
              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/About">À propos</a>
              <br></br>
              
              </ul>
            </div>
        </div>            
          
        <div className="mobile-only" style={{flexShrink:0 }}>
            <div className="card position-absolute top-50 start-50 translate-middle">
              <ul className="list-group list-group-flush">
              <div>
              
              <img src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1789683297/how-to-draw-an-earth-step-6_1_go2k7j.jpg" style={{ cursor: "pointer" }} alt="" width="350" height="350" className="me-2"/>
              </div>
              <br></br>
              <br></br>
              
              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/WorldMap">Explorer la Map</a>
              <br></br>
              
              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/Statistics">Statistiques détaillées</a>
              <br></br>

              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/OtherStatistics">Autres statistiques</a>
              <br></br>
              
              <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/About">À propos</a>
              <br></br>
              
              </ul>
            </div>
        </div>            
        

      </div>
    </div>
    
  );
};

export default Home;