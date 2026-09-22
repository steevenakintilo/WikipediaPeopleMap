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

import {random_localisation_in_france} from "./global_variable.tsx"
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
    //const [list_of_user_data,set_list_of_user_data] : any = useState({});
    var list_of_random_position : any = []
    useEffect(() => {
        // for (var i = 0; i <= 100;i++) {
        //     list_of_random_position.push([getRandomArbitrary(-89,89),getRandomArbitrary(-179,179)])
        // }


    }, []);
 

    

//   for (var i = 0; i <= 100;i++) {
//     list_of_random_position.push([getRandomArbitrary(-89,89),getRandomArbitrary(-179,179)])
//   }

    
    
    let dict_of_advance_search_empty = {
      "job":"",
      "is_alive":false
    }



    var list_of_random_position : any = random_localisation_in_france.sort(() => Math.random() - 0.5);

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

  function getRandomArbitrary(min:number, max:number) {
    return Math.random() * (max - min) + min;
  }

  function user_info_modal() {
    <div>
        toto
    </div>
    
  }

 





// Coordonnées aproximatives de la france
//   MIN_LAT = 42.3
//   MAX_LAT = 51.1
//   MIN_LON = -5.1
//   MAX_LON = 9.6

  // if (list_of_random_position.length <= 100) {
  //       for (var i = 0; i <= 100;i++) {
  //           list_of_random_position.push([getRandomArbitrary(42,51.5),getRandomArbitrary(-5.5,10)])
  //       }

  // }
  console.log("blabla " , list_of_random_position)
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
         
          {list_of_random_position.slice(0, 100).map((position:any) =>
              
            (

              <CircleMarker 
              center={((position))}
              radius={10}
              pathOptions={{
                fillColor: "black",
                color: "black",
                fillOpacity: 0.3
              }}
              >                
                  {/* <Popup>
                      {user.page_name}
                      
                      <br></br>
                  </Popup>
                   */}
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
            <br></br>
            <br></br>
            
            <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/WorldMap">Explorer la Map</a>
            <br></br>
            
            <a type="button" className="btn btn-dark btn-xl" style={{margin :"auto"}} href="/statistics">Statistique</a>
            <br></br>
            
            {/* <button type="button" className="btn btn-dark btn-lg" style={{margin :"auto"}}>Informations</button>
            <br></br>
             */}
            
            </ul>
          </div>
      </div>            
      

    </div>
    </div>
    
  );
};

export default Home;