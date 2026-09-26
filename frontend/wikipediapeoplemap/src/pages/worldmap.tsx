// Imports react
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  ZoomControl,
  CircleMarker,
  useMap
} from "react-leaflet";

import { Tooltip } from "bootstrap";
import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";

import { useEffect, useState } from 'react';
//import { data, useNavigate } from 'react-router';

import "leaflet/dist/leaflet.css";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import Legend from "./map_legend.tsx"
polyfillCountryFlagEmojis();

// Mes imports
import {gender_to_color , gender_to_color2 , list_of_countries , list_of_country_flag, NUMBER_OF_USER} from "./global_variable.tsx"
import "./global.css";


const WorldMap = () => {
    const [list_of_user_data,set_list_of_user_data] : any = useState({});

    useEffect(() => {
        get_list_of_user(0).then((result) => {
            set_list_of_user_data(result.all_user_data)
        })

    }, []);
    

    const width  = window.innerWidth || document.documentElement.clientWidth || 
    document.body.clientWidth;
    const height = window.innerHeight|| document.documentElement.clientHeight|| 
    document.body.clientHeight;
    var display_mobile_version : boolean = true
    if (width > 768) {
      display_mobile_version = false
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
    const [hide_searchbar,set_hide_searchbar] : any = useState(display_mobile_version)
    const [no_move,set_no_move] : any = useState(false)

  
    const tooltipTriggerList = document.querySelectorAll(
        '[data-bs-toggle="tooltip"]'
      );

      tooltipTriggerList.forEach((tooltipTriggerEl) => {
        new Tooltip(tooltipTriggerEl);
      });
    //const navigate = useNavigate();

    function handle_search_bar(){
      set_hide_searchbar(!hide_searchbar)
      set_no_move(false)
    }
    async function get_list_of_user(chunk:number) {
      //setchunck(0)

      const response = await fetch(`http://127.0.0.1:8000/display_chunck_of_user_info/${chunk}`, {
          method: 'GET',
          //headers: {"Content-Type" : "application/json",Authorization: `Bearer ${token}`,},
          headers: {"Content-Type" : "application/json"},

      })
      
      const data_fetch = await response.json()
      //////console.log("blbabla " , data_fetch[0])
      return data_fetch

    }


    async function get_list_of_user_advanced_search(chunk:number,reset_chunck:boolean=false) {
      change_latitude_and_longitude(5,20)

      
      dict_of_advance_search["page_nb"] = current_chunck_index
      if (reset_chunck == true) {
        setchunck(0)
      }
      //setchunck(0)
      const response = await fetch(`http://127.0.0.1:8000/display_chunck_of_user_info_advanced_search/${chunk}/`, {
          method: 'POST',
          //headers: {"Content-Type" : "application/json",Authorization: `Bearer ${token}`,},
          headers: {"Content-Type" : "application/json"},
          body:JSON.stringify(dict_of_advance_search)

      })
      
      const data_fetch = await response.json()
      //////console.log("blbabla " , data_fetch[0])
      return data_fetch

    }

    async function get_user_info(user:string) {
      const response = await fetch(`http://127.0.0.1:8000/display_user_info/${user}`, {
          method: 'GET',
          headers: {"Content-Type" : "application/json"},
      
      })
      
      const data_fetch = await response.json()
      return data_fetch

    }
    
    
    function handle_complete_profile_user(user:string) {
      setcomplete_profile_user(user)
      setlaunch_profile_root(true)
    }
    

    function handle_chunck(event:any,value:number) {
      
      if (value == 1) {
        setchunck(current_chunck_index + 1)

      } else if (current_chunck_index > 0) {
        setchunck(current_chunck_index - 1)
      }
      
      var index : number = current_chunck_index
      if (value == 1) {
        index = current_chunck_index + 1
      } else if (current_chunck_index > 0) {
        index = current_chunck_index - 1
      
      }

      if (value != 0 ) {
          if (Object.keys(dict_of_advance_search).length === 0) {
            get_list_of_user(index).then((result) => {
                set_list_of_user_data(result.all_user_data)
            })
            
          } else {
            //console.log("papa est remplie " , current_chunck_index, value , index)
            
            get_list_of_user_advanced_search(index).then((result) => {set_list_of_user_data(result.all_user_data)})        
          }
          
      } else  {
        get_list_of_user(999999999).then((result) => {
            set_list_of_user_data(result.all_user_data)
            setchunck(999999)
        })
        
      }      
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
  function change_latitude_and_longitude(pos_x:number,pos_y:number,move:boolean=false) {
    console.log("move de connard " , move)
    set_no_move(move)
    if (pos_x != 999999999999999 && pos_y != 999999999999999 && no_move == false) {
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

  const dict_localisation_pin_picture2 : any= {
    999999999999999: "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1787351654/image_mobyht.png",
    default: "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1788295917/pin_death_khphfd.png",
  };
  
  function display_user_profile(mobile_display=false) {
    var user_info_data: any = []
    var start_index = current_chunck_index * Object.keys(list_of_user_data).length
    if (Object.keys(list_of_user_data).length != 500) {
      start_index = (((current_chunck_index)) * 500 + Object.keys(list_of_user_data).length) - Object.keys(list_of_user_data).length
      if ("number_of_people_to_display" in dict_of_advance_search) {
        start_index = (((current_chunck_index)) * dict_of_advance_search["number_of_people_to_display"] + Object.keys(list_of_user_data).length) - Object.keys(list_of_user_data).length
        
      }
    }

    //console.log(dict_of_advance_search)
    if (current_chunck_index == 999999) {
      start_index = 0
    }

    if (mobile_display == true) {
      {Object.values(list_of_user_data).map((user:any,index) =>
      user.page_name.toLowerCase().includes(searched_name.toLowerCase()) != "" && (
        user_info_data.push(
            <li className="list-group-item">
              {user.page_name_even_shorter_for_mobile} {(start_index) + index + 1}/{list_of_user_data[Object.keys(list_of_user_data).length - 1].number_of_element}
              
              <br></br>
              <h1 className="body_flag">
                <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} alt="" width="70" height="70" className="me-2"/>
                  <img src={dict_localisation_pin_picture[user.birth_town_localisation[0]]  ?? dict_localisation_pin_picture.default} style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1],true)} alt="" width="25" height="25" className="me-2"/>
                
                {user.display_death_localisation == true &&(
                    <img src={dict_localisation_pin_picture2[user.town_death_localisation[0]]  ?? dict_localisation_pin_picture2.default} style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.town_death_localisation[0],user.town_death_localisation[1],true)} alt="" width="25" height="25" className="me-2"/>
                )}


                
                {/* user.display_death_localisation == true
                */}
                <span
                  data-bs-toggle="tooltip"
                  data-bs-placement="top"
                  data-bs-title={user.birth_country_name}
                >
                  {user.country_birth_place_emoji}
                </span>
                
                <button type="button" className="btn btn-outline-secondary ms-2" data-bs-toggle="modal" data-bs-target="#exampleModal2" onClick={() => handle_complete_profile_user(user.page_name)}>+ d'info</button>

                
                
              </h1>
              
            </li>
          )
        )
      )}
    
    } else {
      {Object.values(list_of_user_data).map((user:any,index) =>
        user.page_name.toLowerCase().includes(searched_name.toLowerCase()) != "" && (
        user_info_data.push(
            <li className="list-group-item">
              
              
          
              {user.page_name_shorter} {(start_index) + index + 1}/{list_of_user_data[Object.keys(list_of_user_data).length - 1].number_of_element}
              
              <br></br>
              <h1 className="body_flag">
                <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} alt="" width="50" height="50" className="me-2"/>
                  <img src={dict_localisation_pin_picture[user.birth_town_localisation[0]]  ?? dict_localisation_pin_picture.default} style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1],true)} alt="" width="35" height="35" className="me-2"/>
                
                {user.display_death_localisation == true &&(
                    <img src={dict_localisation_pin_picture2[user.town_death_localisation[0]]  ?? dict_localisation_pin_picture2.default} style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.town_death_localisation[0],user.town_death_localisation[1],true)} alt="" width="35" height="35" className="me-2"/>
                )}

                <img src={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxw6xy-R6L-ethznPligpikS1nTohfbsiKoVEX6WlL3Q&s=10"} style={{ cursor: "pointer" }} onClick={() => window.open(user.page_url, "_blank")} alt="" width="35" height="35" className="me-2"/>

                
                {/* user.display_death_localisation == true
                */}
                <span
                  data-bs-toggle="tooltip"
                  data-bs-placement="top"
                  data-bs-title={user.birth_country_name}
                >
                  {user.country_birth_place_emoji}
                </span>
                <button type="button" className="btn btn-outline-secondary ms-2" data-bs-toggle="modal" data-bs-target="#exampleModal2" onClick={() => handle_complete_profile_user(user.page_name)}>+ d'info</button>

                
                
              </h1>
              
            </li>
          )
        )
      )}
    
    }
    return (
      user_info_data
    )
  }

  function user_info_modal() {
    if (complete_profile_user != "" && launch_profil_root === true) {
      get_user_info(complete_profile_user).then((result) => {set_user_data_info(result)})
      setlaunch_profile_root(false)
    }
    
    const gender_to_french_dict : any = {
      "Man":"Homme",
      "Woman":"Femme",
      "Unclear":"Ne sais pas"
    }
    
    var number_of_user_to_show : number = 5
    var number_of_linked_user_to_show : number = 5
    var number_of_friend_to_show : number = 5
    
    
    if (user_data_info.all_links_of_a_page != undefined) {
        if (user_data_info.all_links_of_a_page.length < 5) {
        number_of_user_to_show = user_data_info.all_links_of_a_page.length
      }
      
    }

    if (user_data_info.list_of_page_name_linked_sorted != undefined) {
        if (user_data_info.list_of_page_name_linked_sorted.length < 5) {
        number_of_linked_user_to_show = user_data_info.list_of_page_name_linked_sorted.length
      }
      
    }
    
    if (user_data_info.list_of_friend_of_user != undefined) {
        if (user_data_info.list_of_friend_of_user.length < 5) {
        number_of_friend_to_show = user_data_info.list_of_friend_of_user.length
      }
      
    }
    
    //console.log("user_data_info " , user_data_info)
    return (
    <div>
      <div
        className="modal fade"
        id="exampleModal2"
        aria-labelledby="exampleModalLabel2"
        aria-hidden="true"
      >
        <div className="modal-dialog modal-lg">
          <div className="modal-content">

            <div className="modal-header">
              <h1 className="modal-title fs-5" id="exampleModalLabel2">
                Profil complet de {complete_profile_user} ⚠️MON SITE PEUT SE TROMPER!⚠️
              </h1>

              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>

            <div className="modal-body">
              
              {/* Identité */}
              <div className="text-center">
                <h1 className="wikifont">
                  <strong>{user_data_info.page_name}</strong>
                </h1>

                <img
                  src={decodeURIComponent(
                    decodeURIComponent(user_data_info.picture_url)
                  )}
                  style={{ cursor: "pointer" }}
                  data-bs-toggle="tooltip"
                  data-bs-placement="top"
                  data-bs-title="Voir la page Wikipedia"
                  onClick={() =>
                    window.open(user_data_info.page_url, "_blank")
                  }
                  alt=""
                  width="250"
                  height="250"
                  className="me-2"
                />
              </div>

              <hr />

              {/* Informations générales */}
              <h2 className="wikifont">
                <strong>Informations générales</strong>
              </h2>

              <p className="wikifont">
                <strong>Nombre de vue(s) :</strong>{" "}
                {user_data_info.number_of_views + 1}
              </p>

              <p className="wikifont">
                <strong>Profession :</strong>{" "}
                {user_data_info.job}
              </p>

              <p className="wikifont">
                <strong>Genre :</strong>{" "}
                {gender_to_french_dict[user_data_info.gender]}
              </p>

              <p className="wikifont">
                <strong>Statut :</strong>{" "}
                {user_data_info.is_alive ? "Vivant(e)" : "Décédé(e)"}
              </p>

              {user_data_info.age && user_data_info.age > 0 &&(
                <p className="wikifont">
                  <strong>Âge :</strong>{" "}
                  {user_data_info.age} ans
                </p>
              )}
              
              {user_data_info.age && user_data_info.age >= 110 && user_data_info.is_alive == true &&(
                <p className="wikifont">
                  <strong>Attention :</strong>{" "}
                  L'utilisateur est probalement mort le site est mauvais pour les âges vraiment élevés ⚠️ 
                </p>
              )}
              
              <hr />

              {/* Naissance */}
              <h2 className="wikifont">
                <strong>Naissance</strong>
              </h2>

              <p className="wikifont">
                <strong>Date :</strong>{" "}
                {user_data_info.birth_date} 
              </p>

              <p className="wikifont">
                <strong>Date complete:</strong>{" "}
                {user_data_info.week_day_of_birth} {user_data_info.birth_day} {user_data_info.birth_month} {user_data_info.birth_year} 
              </p>
                            
              <p className="body_flag">
                <strong>Lieu :</strong>{" "}
                {user_data_info.country_birth_place_emoji}{" "}
                {user_data_info.town_birth_place},{" "}
                {user_data_info.country_birth_place}
              </p>

              <p className="wikifont">
                <strong>Région du monde:</strong>{" "}
                {user_data_info.region_of_birth}
              </p>

              <p className="wikifont">
                <strong>Continent :</strong>{" "}
                {user_data_info.continent_of_birth}
              </p>

              <p className="wikifont">
                <strong>Période historique :</strong>{" "}
                {user_data_info.time_period_of_birth}
              </p>

              <hr />

              {/* Décès */}
              {!user_data_info.is_alive && (
                <>
                  <h2 className="wikifont">
                    <strong>Décès</strong>
                  </h2>

                  {user_data_info.is_cause_of_death_known == true &&(
                    <p className="wikifont">
                      <strong>Cause de la mort :</strong>{" "}
                      {user_data_info.cause_of_death}
                    </p>
                  )}

                  <p className="wikifont">
                    <strong>Date :</strong>{" "}
                    {user_data_info.death_date}
                  </p>

                  <p className="wikifont">
                    <strong>Date complete:</strong>{" "}
                    {user_data_info.week_day_of_death} {user_data_info.death_day} {user_data_info.death_month} {user_data_info.death_year} 
                  </p>

                  <p className="body_flag">
                    <strong>Lieu :</strong>{" "}
                    {user_data_info.country_death_place_emoji}{" "}
                    {user_data_info.town_death_place},{" "}
                    {user_data_info.country_death_place}
                  </p>

                  <p className="wikifont">
                    <strong>Région du monde:</strong>{" "}
                    {user_data_info.region_of_death}
                  </p>

                  <p className="wikifont">
                    <strong>Continent :</strong>{" "}
                    {user_data_info.continent_of_death}
                  </p>

                  <hr />
                </>
              )}


              {/* Wikipedia */}
              <h2 className="wikifont">
                <strong>Wikipedia</strong>
              </h2>

              <p className="wikifont">
                <strong>Longueur de la page :</strong>{" "}
                {user_data_info.wikipedia_page_length} {" caractères"}
              </p>
              

              <p className="wikifont">
                <strong>Nombre de liens :</strong>{" "}
                {user_data_info.number_of_links}
                <br></br>
                <br></br>
                

                {number_of_user_to_show > 0 && (
                  <text>
                    <strong>Le top {number_of_user_to_show}:</strong>{" "}
                    <br></br>
                  </text>
                  
                )}
                
                
                {user_data_info.all_links_of_a_page != undefined && (
                  user_data_info.all_links_of_a_page.map((link: any, i: number) => (
                    <div key={i}>- {link}</div>
                  ))
                )}
                
                <br></br>
                <strong>Nombre de personnes qui le mentionnent sur leur page Wikipédia :</strong>{" "}
                {user_data_info.number_of_user_who_have_linked_this_user}
                <br></br>
                <br></br>
                

                {number_of_linked_user_to_show > 0 && (
                  <text>
                    <strong>Le top {number_of_linked_user_to_show}:</strong>{" "}
                    <br></br>
                  </text>
                  
                )}
                
                
                {user_data_info.list_of_page_name_linked_sorted != undefined && (
                  user_data_info.list_of_page_name_linked_sorted.map((link: any, i: number) => (
                    <div key={i}>- {link}</div>
                  ))
                )}
                
                <br></br>
                <strong>Nombre d’ami(s) qu’il a (personne(s) qu’il mentionne sur sa page Wikipédia et qui le mentionne(nt) sur leur propre page) :</strong>{" "}
                {user_data_info.number_of_friends}
                <br></br>
                <br></br>
                

                {number_of_friend_to_show > 0 && (
                  <text>
                    <strong>Le top {number_of_friend_to_show}:</strong>{" "}
                    <br></br>
                  </text>
                  
                )}
                
                
                {user_data_info.list_of_friend_of_user != undefined && (
                  user_data_info.list_of_friend_of_user.map((link: any, i: number) => (
                    <div key={i}>- {link}</div>
                  ))
                )}
                
              </p>
              
              <hr />

              {/* Wikipedia */}
              <h2 className="wikifont">
                <strong>Statistiques</strong>
              </h2>

              <p className="wikifont">
                <strong>Classement :</strong>{" "}
                {user_data_info.position + 1}/{NUMBER_OF_USER}
              </p>
              
              <p className="wikifont">
                <strong>Score :</strong>{" "}
                {user_data_info.power_ranking}
              </p>
              
              <p className="wikifont">
                <strong>Note sur 20 :</strong>{" "}
                {user_data_info.grade_over_20}/{20}
              </p>
              
              <p className="wikifont">
                <strong>Position en % :</strong>{" "}
                top {user_data_info.position_percentage}% des meilleur pages
              </p>
              
              <hr />
              
              <h2 className="wikifont">
                <strong>Précisions/Erreurs</strong>
              </h2>

              <p className="wikifont">
                <strong>Niveau de précision :</strong>{" "}
                {user_data_info.preciseness_level}/100
              </p>

              <p className="wikifont">
                <strong>Nombre d'éléments non trouvés par mon code sur la page :</strong>{" "}
                {user_data_info.number_of_unpreciseness_date}
              </p>
              
              <p className="wikifont">
                <strong>Nombre d'erreurs sur la page :</strong>{" "}

                {user_data_info.list_of_unpreciseness_data != undefined && (
                  user_data_info.list_of_unpreciseness_data.map((error: any, i: number) => (
                    <div key={i}>- {error}</div>
                  ))
                )}
                
              </p>

            </div>
          </div>
        </div>
      </div>
    </div>
    )
      
    
  }

  function advanced_search_modal() {
    const status_death_string_list : any = ["Mort","Vivant","Les 2"]
    const gender_string_list : any = ["Homme","Femme","Les 2"]
    const historical_period: any = [
    "Préhistoire -99999999-3301",
    "Antiquité -3300-475",
    "Moyen Âge 476-1491",
    "Renaissance 1492-1788",
    "Époque contemporaine 1789-1999",
    "Époque actuelle 2000-?????",
    "Toutes"
    ]

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
                  <input className="form-control w-100" type="text" placeholder={"Métier ex: acteur ou chanteuse#peintre#médecin ou foot"} onChange={(event) => handle_dict_of_advance_search(event,"job")}></input>
                  <br></br>
                  <input className="form-control w-75" type="text" placeholder={"Nom (+ pour inclure les noms contenant)"} onChange={(event) => handle_dict_of_advance_search(event,"last_name")}></input>
                  <br></br>
                  <input className="form-control w-75" type="text" placeholder={"Prénom (+ pour inclure les noms contenant)"} onChange={(event) => handle_dict_of_advance_search(event,"first_name")}></input>
                  
                  <br></br>
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"country_of_birth")}
>
                    <option selected>Continent/Région/Pays de naissance</option>
                    
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
                    onChange={(event) => handle_dict_of_advance_search(event,"country_death_place")}
                  >
                    <option selected>Continent/Région/Pays de mort</option>
                    
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
                  <br></br>

                  <input className="form-control w-100" 
                    placeholder={"Année de naissance (+ pour inclure les années suivantes)"} 
                    type="text"
                    onChange={(event) => handle_dict_of_advance_search(event,"birth_year")}>
                  </input>
                  <br></br>
                  <input className="form-control w-100" 
                    placeholder={"Année de mort (- pour inclure les années précédentes)"} 
                    type="text"
                    onChange={(event) => handle_dict_of_advance_search(event,"death_year")}>
                  </input>
                  <br></br>
                  <input className="form-control w-75" 
                    placeholder={"Age minimum"} 
                    type="number"
                    min={1}
                    max={125}
                    step={1}
                    onChange={(event) => handle_dict_of_advance_search(event,"age")}>
                  </input>
                    
                  <br></br>   
                  <input className="form-control w-75" 
                    placeholder={"Age maximum"} 
                    type="number"
                    min={1}
                    max={125}
                    step={1}
                    onChange={(event) => handle_dict_of_advance_search(event,"age_max")}>
                  </input>


                  <br></br>
                  
                  <input className="form-control w-75" type="text" placeholder={"Ville de naisannce"} onChange={(event) => handle_dict_of_advance_search(event,"town_birth_place")}></input>

                  <br></br>

                  <input className="form-control w-75" type="text" placeholder={"Ville de mort"} onChange={(event) => handle_dict_of_advance_search(event,"town_death_place")}></input>

                  <br></br>
                    
                  <input className="form-control w-75" type="text" placeholder={"Ville de naisannce ou mort"} onChange={(event) => handle_dict_of_advance_search(event,"town_birth_or_death_place")}></input>

                  <br></br>

                  <input className="form-control w-75" type="text" placeholder={"Date de naissance (JJ-MOIS ex: 01-janvier)"} onChange={(event) => handle_dict_of_advance_search(event,"birth_month_day")}></input>
                  <br></br>
                  <input className="form-control w-75" type="text" placeholder={"Date de mort (JJ-MOIS ex: 13-mars)"} onChange={(event) => handle_dict_of_advance_search(event,"death_month_day")}></input>
                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"time_period_of_birth")}
                  >
                    <option selected>Période historique?</option>
                    
                    {historical_period
                        .map((history:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {history}
                        </option>
                      ))}
                    
                    
                  </select>
                  <br></br>
                  
                  <input className="form-control w-75" 
                    placeholder={"Siécle de naissance"} 
                    type="number"
                    min={1}
                    max={125}
                    step={1}
                    onChange={(event) => handle_dict_of_advance_search(event,"century_of_birth")}>
                  </input>
                  <br></br>
                  
                  <input className="form-control w-75" 
                    placeholder={"Siécle de mort"} 
                    type="number"
                    min={1}
                    max={125}
                    step={1}
                    onChange={(event) => handle_dict_of_advance_search(event,"century_of_death")}>
                  </input>
                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"display_people_with_no_localisation")}
                  >
                    <option selected>Afficher les gens qui n'ont pas de localisation de naissance?</option>
                    
                    {["oui","non"]
                        .map((choice:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {choice}
                        </option>
                      ))}
                    
                    
                  </select>
                  
                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"display_only_one_person_per_town")}
                  >
                    <option selected>Afficher seulement un utilisateur par ville de naissance?</option>
                    
                    {["oui","non"]
                        .map((choice:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {choice}
                        </option>
                      ))}
                    
                    
                  </select>
                  

                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"is_cause_of_death_known")}
                  >
                    <option selected>Afficher seulement les utilisateurs avec une cause de mort connue?</option>
                    
                    {["oui","non"]
                        .map((choice:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {choice}
                        </option>
                      ))}
                    
                    
                  </select>
                  
                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"sort_user_by")}
                  >
                    <option selected>Trier les utilisateurs par?</option>
                    
                    {["Nombre de lien","Taille de la page wipedia","Nombre de personnes qui les lient","Âge","Nombre d'ami(e)","Taille du nom de la page","Nombre de vue(s)","Par défaut"]
                        .map((choice:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {choice}
                        </option>
                      ))}
                    
                    
                  </select>
                  
                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                  onChange={(event) => handle_dict_of_advance_search(event,"born_before_christ")}
                  >
                  <option selected>Né avant Jésus-Christ?</option>
                  
                  {["oui","non","Les 2"]
                      .map((choice:any, i:number) => (
                        
                      
                      <option
                        key={i}
                        className="list-group-item list-group-item-action body_flag"
                        data-bs-dismiss="modal"
                      >

                        {choice}
                      </option>
                    ))}
                  
                  
                </select>
                
                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"display_only_death_localisation")}
                  >
                    <option selected>Afficher seulement les lieux de mort?</option>
                    
                    {["oui","non"]
                        .map((choice:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {choice}
                        </option>
                      ))}
                    
                    
                  </select>
                  
                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"display_only_people_born_and_dead_the_same_day")}
                  >
                    <option selected>Afficher seulement les gens nés et morts le même jour ?</option>
                    
                    {["oui","non"]
                        .map((choice:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {choice}
                        </option>
                      ))}
                    
                    
                  </select>

                  <br></br>
                  
                  <select className="form-select body_flag" aria-label="Default select example"                       
                    onChange={(event) => handle_dict_of_advance_search(event,"display_only_people_born_and_dead_in_the_same_town")}
                  >
                    <option selected>Afficher seulement les gens nés/morts dans la même ville</option>
                    
                    {["oui","non"]
                        .map((choice:any, i:number) => (
                          
                        
                        <option
                          key={i}
                          className="list-group-item list-group-item-action body_flag"
                          data-bs-dismiss="modal"
                        >

                          {choice}
                        </option>
                      ))}
                    
                    
                  </select>

                  <br></br>
                  
                  <input className="form-control w-75" type="number" min="1" max="706280" placeholder={"Position maximale de la personne à afficher"} onChange={(event) => handle_dict_of_advance_search(event,"latest_position_of_user_to_display")}></input>
                  
                  <br></br>
                  <input className="form-control w-75" 
                    placeholder={"Nombre de personnes affichées (1-500)"} 
                    type="number"
                    min={0}
                    max={500}
                    step={1}
                    onChange={(event) => handle_dict_of_advance_search(event,"number_of_people_to_display")}>
                  </input>
                                    

              </div>
              
              <div className="modal-footer">
                
                <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                <button type="button" className="btn btn-danger" data-bs-dismiss="modal" onClick={() => window.location.reload()}>Reset</button>
                <button type="button" className="btn btn-primary" data-bs-dismiss="modal" onClick={() => get_list_of_user_advanced_search(current_chunck_index,true).then((result) => {set_list_of_user_data(result.all_user_data)})}>Rechercher 🔎</button>
              </div>
            </div>
          </div>
        </div>
      </div> 
    )
    
    
  }

  var user_profile = display_user_profile()
  var user_profile_mobile = display_user_profile(true)
  
  return (

    <div>   

    <div className="d-flex align-items-stretch">  
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
              
              user.birth_town_localisation?.[0] !== 999999999999999 &&
              user.birth_town_localisation?.[1] !== 999999999999999 && (

              <CircleMarker 
              center={((user.birth_town_localisation))}
              radius={10}
              pathOptions={{
                fillColor: gender_to_color[`${user.gender}${user.is_alive}`],
                color: gender_to_color[`${user.gender}${user.is_alive}`],
                fillOpacity: 0.3
              }}
              >                
                  <Popup>
                      {user.page_name}
                      <img src={"https://uxwing.com/wp-content/themes/uxwing/download/location-travel-map/map-pin-icon.png"} data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Localiser l'utilisateur" style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1],true)} alt="" width="15" height="15" className="me-2"/>

                      <br></br>
                      {/* <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="Voir la page Wikipedia" onClick={() => window.open(user.page_url, "_blank")} alt="" width="250" height="250" className="me-2"/> */}
                      <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} data-bs-placement="bottom" data-bs-toggle="modal" data-bs-target="#exampleModal2" data-bs-title="Voir le profil" onClick={() => handle_complete_profile_user(user.page_name)} alt="" width="250" height="250" className="me-2"/>
                  
                      
                  </Popup>
                  
              </CircleMarker>
              )
              
          )}
          
         
          {Object.values(list_of_user_data).map((user:any) =>
              
              user.town_death_localisation?.[0] !== 999999999999999 &&
              user.town_death_localisation?.[1] !== 999999999999999 && user.display_death_localisation == true && (

              <CircleMarker 
              center={((user.town_death_localisation))}
              radius={10}
              pathOptions={{
                fillColor: gender_to_color2[`${user.gender}${user.is_alive}`],
                color: gender_to_color2[`${user.gender}${user.is_alive}`],
                fillOpacity: 0.3
              }}
              >                
                  <Popup>
                      {user.page_name}
                      <img src={"https://uxwing.com/wp-content/themes/uxwing/download/location-travel-map/map-pin-icon.png"} data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Localiser l'utilisateur" style={{ cursor: "pointer" }} onClick={() => change_latitude_and_longitude(user.birth_town_localisation[0],user.birth_town_localisation[1],true)} alt="" width="15" height="15" className="me-2"/>

                      <br></br>
                      <img src={decodeURIComponent(decodeURIComponent(user.picture_url))} style={{ cursor: "pointer" }} data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="Voir la page Wikipedia" onClick={() => window.open(user.page_url, "_blank")} alt="" width="250" height="250" className="me-2"/>
                  </Popup>
                  
              </CircleMarker>
              )
              
          )}

          
          <Legend />
  
        </MapContainer>
      </div>

      {/* <div>
          <button type="button" className="btn btn-danger  btn-sm">.</button>
      </div>
       */}

      {hide_searchbar == false && (
        <div className="" style={{flexShrink:0 }}>
            <div className="card">
              <ul className="list-group list-group-flush">
                <div>


                  <li className="list-group-item desktop-only">
                    <a type="button" className="btn btn-dark" href="/Home" style={{margin :"auto"}}>Menu</a>
                                        
                    <br></br>
                    <br></br>
                    
                    <input className="form-control w-75" type="text" placeholder={"Nom de la page"} onChange={(event) => handle_searched_name(event)}></input>
                    <br></br>
                    <button type="button" className="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" style={{margin :"auto"}}>Recherches avancées 🔎</button>
                    <br></br>
                    <br></br>
                    
                    <button type="button" className="btn btn-warning" data-bs-dismiss="modal" onClick={(event) => handle_chunck(event,0)}>Page Aléatoire</button>
                    
                    <br></br>
                    <br></br>
                    
                    <button type="button" className="btn btn-secondary" data-bs-dismiss="modal" onClick={(event) => handle_chunck(event,-1)}>Page Précédente</button>
                    <button type="button" className="btn btn-secondary ms-4" data-bs-dismiss="modal" onClick={(event) => handle_chunck(event,+1)}>Page Suivante</button>
                    <br></br>
                    <br></br>
                    <button type="button" className="btn btn-light">Page {current_chunck_index + 1}</button>
                    
                  </li>

                  <li className="list-group-item mobile-only">
                    <a type="button" className="btn btn-dark" href="/Home" style={{margin :"auto"}}>Menu</a>
                    
                    <br></br>
                    <br></br>
                    
                    <a type="button" className="btn btn-warning btn-sm mobile-only" onClick={() => handle_search_bar()}>Masquer la recherche 🙈</a>

                    <br></br>
                    
                    <input className="form-control w-75" type="text" placeholder={"Nom de la page"} onChange={(event) => handle_searched_name(event)}></input>
                    <br></br>
                    <button type="button" className="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" style={{margin :"auto"}}>Recherches avancées 🔎</button>
                    <br></br>
                    <br></br>

                    <button type="button" className="btn btn-secondary" data-bs-dismiss="modal" onClick={(event) => handle_chunck(event,-1)}>{"Page -"}</button>
                    <button type="button" className="btn btn-secondary ms-4" data-bs-dismiss="modal" onClick={(event) => handle_chunck(event,+1)}>{"Page +"}</button>
                    <br></br>
                    <br></br>
                    <button type="button" className="btn btn-light">Page {current_chunck_index + 1}</button>
                    
                  </li>

                  
                  
                  {advanced_search_modal()}
                  {user_info_modal()}
                  
                  
                  
                  <div className="desktop-only">
                    {user_profile}
                  </div>
                  
                  <div className="mobile-only">
                    {user_profile_mobile}
                  </div>
                  
                  {/* <li className="list-group-item">
                    <h1>fefefe</h1>
                  </li>
                  */}
                  
                </div>
              </ul>
            </div>
        </div>            
        

      )}

      {hide_searchbar == true && (
        <div className="mobile-only">
          <button type="button" className="btn btn-light btn-sm" style={{margin :"auto"}} onClick={() => handle_search_bar()}>🙈</button>
        </div>
                
      )}

      </div>
    </div>
    
  );
};

export default WorldMap;