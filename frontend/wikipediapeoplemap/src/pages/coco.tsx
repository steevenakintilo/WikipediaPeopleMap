// import { ComposableMap, Geographies, Geography } from "react-simple-maps";

// import geoUrl from "../custom.geo.json";

import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  ZoomControl,
  CircleMarker,
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
          "Man":"blue",
          "Woman":"red",
          "Unknown":"grey"
    }

    
  return (
    <div>
      {/* <div className="card" style={{width: "5rem;"}}>
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Ammons_and_Johnson.jpg?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail_unscaled" className="card-img-top" alt="..."/>
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
          <a href="#" className="btn btn-primary">Go somewhere</a>
        </div>
      </div>
   */}
      <div className="map-wrapper">
        <MapContainer
          center={[20, 0]}
          zoom={2}
          minZoom={2}
          maxZoom={18}
          zoomControl={true}
          scrollWheelZoom={true}
          className="world-map"
        >

          
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
              fillColor={gender_to_color[user.gender]}
              color={gender_to_color[user.gender]}

              >                
                  <Popup>
                      {user.page_name}
                      <br></br>
                      <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} onClick={() => window.open(user.page_url, "_blank")} alt="" width="250" height="250" className="me-2"/>
                  </Popup>
                  
              </CircleMarker>
          )}
        </MapContainer>
      </div>
    </div>
  );
};

export default HomePage;