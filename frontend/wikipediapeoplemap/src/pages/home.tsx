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

import { useEffect, useState } from 'react';
import { data, useNavigate } from 'react-router';

import "leaflet/dist/leaflet.css";
import "./home.css";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

const HomePage = () => {
    const [list_of_user_data,set_list_of_user_data] : any = useState({});

    useEffect(() => {
        get_list_of_user(0).then((result) => {
            set_list_of_user_data(result.all_user_data)
        })

    }, []);
 

    const x = 6.6034
    const y = 48.8883
    const [longitude,setlongitude] = useState(x)
    const [latitude,setlatitude] = useState(y)
    const [zoom,setzoom] = useState(6)
    const [searched_name,setsearched_name] : any = useState("")
    const navigate = useNavigate();
    async function get_list_of_user(maximum_number_of_game:number) {
            const response = await fetch(`http://127.0.0.1:8000/display_chunck_of_user_info/${maximum_number_of_game}`, {
                method: 'GET',
                //headers: {"Content-Type" : "application/json",Authorization: `Bearer ${token}`,},
                headers: {"Content-Type" : "application/json"},
                
            })
            const data_fetch = await response.json()
            ////console.log("blbabla " , data_fetch[0])
            return data_fetch

    }

    const gender_to_color = {
      "ManTrue":"#66B2FF",
      "WomanTrue":"#FF6666",
      "UnknownTrue":"grey",
      "ManFalse":"#000066",
      "WomanFalse":"#660000",
      "UnknownFalse":"202020"
      
    }

  
  
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
  function  test(pos_x,pos_y) {
    setlatitude(pos_x)
    setlongitude(pos_y)
    setzoom(30)
    
  }

  function handle_searched_name(event:any) {
    setsearched_name(event.target.value)
  }

  function display_user_profile() {
    var toto: any = []
    {Object.values(list_of_user_data).map((user,index) =>
      user.page_name.toLowerCase().includes(searched_name.toLowerCase()) != "" && (
      toto.push(
          <li className="list-group-item">
            {user.page_name} {index + 1}/{Object.keys(list_of_user_data).length}
            <br></br>

            <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} alt="" width="50" height="50" className="me-2"/>
            <img src={"https://uxwing.com/wp-content/themes/uxwing/download/location-travel-map/map-pin-icon.png"} style={{ cursor: "pointer" }} onClick={() => test(user.birth_town_localisation[0],user.birth_town_localisation[1])} alt="" width="35" height="35" className="me-2"/>
            <img src={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxw6xy-R6L-ethznPligpikS1nTohfbsiKoVEX6WlL3Q&s=10"} style={{ cursor: "pointer" }} onClick={() => window.open(user.page_url, "_blank")} alt="" width="35" height="35" className="me-2"/>
          </li>
        )
      )
    )}
    return (
      toto
    )
  }

  var user_profile = display_user_profile()
  return (
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


      <div className="map-wrapper p-20 col-10 border-end border-end border-2 border-secondary"
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
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />

          {/* Boutons + / - */}
          {Object.values(list_of_user_data).map((user) =>
              

              <CircleMarker 
              center={((user.birth_town_localisation))}
              radius={10}
              fillColor={gender_to_color[user.gender+user.is_alive]}
              color={gender_to_color[user.gender+user.is_alive]}

              >                
                  <Popup>
                      {user.page_name}
                      <img src={"https://uxwing.com/wp-content/themes/uxwing/download/location-travel-map/map-pin-icon.png"} style={{ cursor: "pointer" }} onClick={() => test(user.birth_town_localisation[0],user.birth_town_localisation[1])} alt="" width="15" height="15" className="me-2"/>

                      <br></br>
                      <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} onClick={() => window.open(user.page_url, "_blank")} alt="" width="250" height="250" className="me-2"/>
                  </Popup>
                  
              </CircleMarker>
          )}
        </MapContainer>
        
      </div>
      <div className="" style={{flexShrink: 0 }}>
          <div className="card">
            <ul className="list-group list-group-flush">
              <div>
                <li className="list-group-item">
                  <br></br>
                  <input className="form-control w-75" type="text" placeholder={"Nom de la page"} onChange={(event) => handle_searched_name(event)}></input>
                </li>

                {user_profile}
                {/* <li className="list-group-item">
                  <h1>fefefe</h1>
                </li>
                 */}
                
              </div>
            </ul>
          </div>
      </div>            
      

    </div>
  );
};

export default HomePage;