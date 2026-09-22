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

const Statistics = () => {
    //const [list_of_user_data,set_list_of_user_data] : any = useState({});
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



    
    
    const tooltipTriggerList = document.querySelectorAll(
        '[data-bs-toggle="tooltip"]'
      );

      tooltipTriggerList.forEach((tooltipTriggerEl) => {
        new Tooltip(tooltipTriggerEl);
      });
    



    function add_space(number: number) {
        const br_list:any = []
        for (let i = 0 ; i < number ; i++) {
            br_list.push(<br></br>)  
        }

        return br_list
    }
   return (

    <div className="d-flex min-vh-100">
    


    <div
        className="position-absolute top-50 start-50 translate-middle"
        style={{
        width: "100%",
        height: "100vh",
        position: "sticky",
        top: 0,
        }}
    >
    <br></br>
    <input className="form-control w-75 " type="text" style={{ alignItems: "center" , justifyContent: "center", display: "flex"}} placeholder={"Nom de la page"} onChange={(event) => ""}></input>

    </div>

    {/* <div
        className="border-end border-2 border-secondary position-absolute top-50 start-50 translate-middle"
        style={{
        width: "70%",
        height: "100vh",
        position: "sticky",
        top: 0,
        }}
    >

    <br></br>
    <input className="form-control w-75 " type="text" style={{ alignItems: "center" , justifyContent: "center", display: "flex"}} placeholder={"Nom de la page"} onChange={(event) => ""}></input>

    </div>

    <div
        style={{
        width: "30%",
        height: "100vh",
        overflowY: "auto",
        }}
    >
        ...
        
    </div> */}

    </div>
    
  );
};

export default Statistics;