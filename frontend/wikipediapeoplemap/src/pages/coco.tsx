// import { ComposableMap, Geographies, Geography } from "react-simple-maps";

// import geoUrl from "../custom.geo.json";

import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  ZoomControl,
  CircleMarker,
  useMap
} from "react-leaflet";

import {gender_to_color , gender_to_color2 , list_of_countries , list_of_country_flag, NUMBER_OF_USER} from "./global_variable.tsx"
import { Tooltip } from "bootstrap";
import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";

import { useEffect, useState } from 'react';
import { data, useNavigate } from 'react-router';

import "leaflet/dist/leaflet.css";

import 'bootstrap/dist/css/bootstrap.min.css';

import "./home.css";
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import Legend from "./map_legend.tsx"
import Custom_navbar from "./navbar.tsx";

polyfillCountryFlagEmojis();

const Home = () => {
    const [list_of_user_data,set_list_of_user_data] : any = useState({});

    let dict_of_advance_search_empty = {
      "job":"",
      "is_alive":false
    }
    const longitude_position_of_france = 6.6034
    const latitude_position_of_france = 48.8883
    const [longitude,setlongitude] = useState(longitude_position_of_france)
    const [latitude,setlatitude] = useState(latitude_position_of_france)
    const [zoom,setzoom] = useState(6)
    const [searched_name,setsearched_name] : any = useState("")
    const [current_chunck_index,setchunck] = useState(0)
    const [complete_profile_user,setcomplete_profile_user] = useState("")
    const [launch_profil_root,setlaunch_profile_root] = useState(false)
    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    const [user_data_info,set_user_data_info] : any = useState({});
    
    const tooltipTriggerList = document.querySelectorAll(
        '[data-bs-toggle="tooltip"]'
      );

      tooltipTriggerList.forEach((tooltipTriggerEl) => {
        new Tooltip(tooltipTriggerEl);
      });
    
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
  // // {user.page_name} {index + 1}/{Object.keys(list_of_user_data).length}

  function display_user_profile() {
    var user_info_data: any = []
    var start_index = current_chunck_index * Object.keys(list_of_user_data).length
    if (Object.keys(list_of_user_data).length != 500) {
      start_index = (((current_chunck_index)) * 500 + Object.keys(list_of_user_data).length) - Object.keys(list_of_user_data).length
      if ("number_of_people_to_display" in dict_of_advance_search) {
        start_index = (((current_chunck_index)) * dict_of_advance_search["number_of_people_to_display"] + Object.keys(list_of_user_data).length) - Object.keys(list_of_user_data).length
        
      }
    }

    console.log(dict_of_advance_search)
    if (current_chunck_index == 999999) {
      start_index = 0
    }
    {Object.values(list_of_user_data).map((user:any,index) =>
      <h1>
        blabla
      </h1>
    )}
    return (
      user_info_data
    )
  }

  function user_info_modal() {
    <div>
        toto
    </div>
    
  }

  return (

    <div>   
    {/* <div>
      {Custom_navbar(0)}
      
      <br></br>
      <br></br>
      <br></br>
      
    </div> */}
    <div className="d-flex align-items-stretch min-vh-100">
      
      {/* <div className="card" style={{width: "5rem;"}}>
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Ammons_and_Johnson.jpg?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail_unscaled" className="card-img-top" alt="..."/>
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
          <a href="#" className="btn btn-primary">Go somewhere</a>
        </div>
      </div>
   */}

      <div className="map-wrapper border-end border-end border-2 border-secondary"
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

          {/* Fond OpenStreetMap */}
          {/* <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          /> */}

          <TileLayer
            attribution="&copy; Google Maps"
            url="https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
            subdomains={["mt0", "mt1", "mt2", "mt3"]}
          />
          {/* Boutons + / - */}
         
          {Object.values(list_of_user_data).map((user:any) =>
              
              user.town_death_localisation?.[0] !== 999999999999999 &&
              user.town_death_localisation?.[1] !== 999999999999999 && user.display_death_localisation == true && (

              <CircleMarker 
              center={((user.town_death_localisation))}
              radius={10}
              pathOptions={{
                fillColor: "black",
                color: "black",
                fillOpacity: 0.3
              }}
              >                
                  <Popup>
                      {user.page_name}
                      <img src={"https://uxwing.com/wp-content/themes/uxwing/download/location-travel-map/map-pin-icon.png"} data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Localiser l'utilisateur" style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1])} alt="" width="15" height="15" className="me-2"/>

                      <br></br>
                      <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="Voir la page Wikipedia" onClick={() => window.open(user.page_url, "_blank")} alt="" width="250" height="250" className="me-2"/>
                  </Popup>
                  
              </CircleMarker>
              )
              
          )}
          
        </MapContainer>
        
      </div>
      <div className="" style={{flexShrink:0 }}>
          <div className="card">
            <ul className="list-group list-group-flush">
              <div>
                
                <img src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1789683297/how-to-draw-an-earth-step-6_1_go2k7j.jpg" style={{ cursor: "pointer" }} alt="" width="500" height="500" className="me-2"/>
                
                
                

                {/* <li className="list-group-item">
                  <h1>fefefe</h1>
                </li>
                 */}
                
              </div>
              
            </ul>
          </div>
      </div>            
      

    </div>
    </div>
    
  );
};

export default Home;