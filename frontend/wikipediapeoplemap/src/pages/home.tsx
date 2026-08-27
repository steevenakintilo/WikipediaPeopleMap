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

import {gender_to_color ,list_of_countries , list_of_country_flag} from "./global_variable.tsx"
import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";

import { useEffect, useState } from 'react';
import { data, useNavigate } from 'react-router';

import "leaflet/dist/leaflet.css";
import "./home.css";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

polyfillCountryFlagEmojis();

const HomePage = () => {
    const [list_of_user_data,set_list_of_user_data] : any = useState({});

    useEffect(() => {
        get_list_of_user(0).then((result) => {
            set_list_of_user_data(result.all_user_data)
        })

    }, []);
 


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

    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    const navigate = useNavigate();
    async function get_list_of_user(chunk:number) {
      let blob = {"test":"tljikoest"}
      const response = await fetch(`http://127.0.0.1:8000/display_chunck_of_user_info/${chunk}`, {
          method: 'GET',
          //headers: {"Content-Type" : "application/json",Authorization: `Bearer ${token}`,},
          headers: {"Content-Type" : "application/json"},

      })
      
      const data_fetch = await response.json()
      ////console.log("blbabla " , data_fetch[0])
      return data_fetch

    }


    async function get_list_of_user_advanced_search(chunk:number) {
      change_latitude_and_longitude(5,20)
      const response = await fetch(`http://127.0.0.1:8000/display_chunck_of_user_info_advanced_search/${chunk}/`, {
          method: 'POST',
          //headers: {"Content-Type" : "application/json",Authorization: `Bearer ${token}`,},
          headers: {"Content-Type" : "application/json"},
          body:JSON.stringify(dict_of_advance_search)

      })
      
      const data_fetch = await response.json()
      ////console.log("blbabla " , data_fetch[0])
      return data_fetch

    }

    function handle_chunck() {
      setchunck(current_chunck_index + 1)
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
  function change_latitude_and_longitude(pos_x:number,pos_y:number) {
    if (pos_x != 999999999999999 && pos_y != 999999999999999) {
      setlatitude(pos_x)
      setlongitude(pos_y)
      if (pos_x === 5 && pos_y === 20) {
        setzoom(2)
      } else {
        setzoom(30)
      
      }
      
    }
    
  }

  function handle_dict_of_advance_search(event:any,key:any) {
    set_dict_of_advance_search((prev: any) => ({
      ...prev,
      [key]: event.target.value,
    }));
  }
  
  
  function handle_searched_name(event:any) {
    setsearched_name(event.target.value)
  }

  const dict_localisation_pin_picture : any= {
    999999999999999: "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1787351654/image_mobyht.png",
    default: "https://uxwing.com/wp-content/themes/uxwing/download/location-travel-map/map-pin-icon.png",
  };
  function display_user_profile() {
    var toto: any = []
    {Object.values(list_of_user_data).map((user,index) =>
      user.page_name.toLowerCase().includes(searched_name.toLowerCase()) != "" && (
      toto.push(
          <li className="list-group-item">
            {user.page_name} {index + 1}/{Object.keys(list_of_user_data).length}
            <br></br>
            <h1 className="body_flag">
              <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} alt="" width="50" height="50" className="me-2"/>
                <img src={dict_localisation_pin_picture[user.birth_town_localisation[0]]  ?? dict_localisation_pin_picture.default} style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1])} alt="" width="35" height="35" className="me-2"/>
              <img src={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxw6xy-R6L-ethznPligpikS1nTohfbsiKoVEX6WlL3Q&s=10"} style={{ cursor: "pointer" }} onClick={() => window.open(user.page_url, "_blank")} alt="" width="35" height="35" className="me-2"/>
              {user.country_birth_place_emoji}
              👤
              
            </h1>
            
          </li>
        )
      )
    )}
    return (
      toto
    )
  }


  function advanced_search_modal() {
    var status_death_string_list : any = ["Mort","Vivant","Les 2"]
    var gender_string_list : any = ["Homme","Femme","Les 2"]
    
    return(

      <div>
        <div className="modal fade" id="exampleModal" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h1 className="modal-title fs-5" id="exampleModalLabel">Recherches avancées 🔎</h1>
                <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div className="modal-body">
                {/* <input
                    className="form-control w-50"
                    type="text"
                    placeholder="Pays de naissance"
                />
                 */}
                  <input className="form-control w-75" type="text" placeholder={"Métier"} onChange={(event) => handle_dict_of_advance_search(event,"job")}></input>
                  <br></br>
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"country_of_birth")}
>
                    <option selected>Pays de naissance</option>
                    
                    {list_of_countries
                        .map((country, i) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {country} {list_of_country_flag[i]}
                        </option>
                      ))}
                    
                    
                  </select>

                  <br></br>
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"alive_status")}
>
                    <option selected>Mort ou Vivant?</option>
                    
                    {status_death_string_list
                        .map((death_status:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {death_status}
                        </option>
                      ))}
                    
                    
                  </select>
                  <br></br>
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"gender")}
>
                    <option selected>Genre?</option>
                    
                    {gender_string_list
                        .map((gender:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {gender}
                        </option>
                      ))}
                    
                    
                  </select>
                  <br></br>
                  
                  <input className="form-control w-75" 
                    placeholder={"Niveau de précision de la page (0-100%)"} 
                    type="number"
                    min={0}
                    max={100}
                    step={1}
                    onChange={(event) => handle_dict_of_advance_search(event,"preciseness_level")}>
                  </input>

              </div>
              
              <div className="modal-footer">
                
                <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                <button type="button" className="btn btn-danger" data-bs-dismiss="modal" onClick={() => window.location.reload()}>Reset</button>
                <button type="button" className="btn btn-primary" data-bs-dismiss="modal" onClick={() => get_list_of_user_advanced_search(0).then((result) => {set_list_of_user_data(result.all_user_data)})}>Rechercher 🔎</button>
              </div>
            </div>
          </div>
        </div>
      </div> 
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
          {Object.values(list_of_user_data).map((user) =>
              
              user.birth_town_localisation?.[0] !== 999999999999999 &&
              user.birth_town_localisation?.[1] !== 999999999999999 && (

              <CircleMarker 
              center={((user.birth_town_localisation))}
              radius={10}
              fillColor={gender_to_color[user.gender+user.is_alive]}
              color={gender_to_color[user.gender+user.is_alive]}

              >                
                  <Popup>
                      {user.page_name}
                      <img src={"https://uxwing.com/wp-content/themes/uxwing/download/location-travel-map/map-pin-icon.png"} style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1])} alt="" width="15" height="15" className="me-2"/>

                      <br></br>
                      <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} onClick={() => window.open(user.page_url, "_blank")} alt="" width="250" height="250" className="me-2"/>
                  </Popup>
                  
              </CircleMarker>
              )
              
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
                  <br></br>
                  <button type="button" className="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" style={{margin :"auto"}}>Recherches avancées 🔎</button>

                  
                </li>

                
                {/* <button type="button" className="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                  Launch demo modal
                </button>
                 */}
                {advanced_search_modal()}
                
                

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