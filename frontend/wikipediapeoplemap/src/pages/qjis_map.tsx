// import { ComposableMap, Geographies, Geography } from "react-simple-maps";

// import geoUrl from "../custom.geo.json";

import { Tooltip } from "bootstrap";
import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";
import { Accordion } from 'react-bootstrap';
import { useEffect, useState } from 'react';
import { data, useNavigate } from 'react-router';

//import Custom_navbar from "./navbar.tsx";

import { AgCharts } from "ag-charts-react";
import {
    ModuleRegistry,
    AllCommunityModule
} from "ag-charts-community";

ModuleRegistry.registerModules([AllCommunityModule]);

import "leaflet/dist/leaflet.css";

import 'bootstrap/dist/css/bootstrap.min.css';

import "./global.css";
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import {NUMBER_OF_USER} from './global_variable'
import {list_of_countries , list_of_country_flag,VAR_TO_DESCRIPTION,STAT_TO_DESCRIPTION,SUB_THEME_TO_THEME} from "./global_variable.tsx"
import { generate_list_of_dict , make_a_graphic ,generate_list_of_dict2} from "./utility_function.tsx";

import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper
} from "@mui/material";
import { grey } from "@mui/material/colors";

polyfillCountryFlagEmojis();

const QjisMap = () => {
    //const [total_number_of_user_found,set_total_number_of_user_found] : any = useState({});
    const [total_number_of_user_found,set_total_number_of_user_found] : any = useState(0);
    
    const [result_found,set_result_found] : any = useState(false)
    const [loading,set_loading] : any = useState(false)
    const [server_error_found,set_server_error_found] : any = useState(false)
    const [no_result_found_text,set_no_result_found_text] : any = useState(false)
    useEffect(() => {
        // get_list_of_user_advanced_search().then((result) => {
        //     set_total_number_of_user_found(result.all_user_data)
        //     console.log("typeof: ", typeof(result.all_user_data))
        // })

    }, []);
 

    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    



    
    function handle_dict_and_keys_info(dict_info:any,keys_info:string) {
      set_dict_info(dict_info)
      set_keys_info(keys_info)
    }
    async function get_list_of_user_advanced_search() {
      
      
    //setchunck(0)
    set_loading(true)
    set_server_error_found(false)

    const response = await fetch(`http://127.0.0.1:8000/display_chunck_of_user_info_advanced_search_qjis`, {
        method: 'POST',
        //headers: {"Content-Type" : "application/json",Authorization: `Bearer ${token}`,},
        headers: {"Content-Type" : "application/json"},
        body:JSON.stringify(dict_of_advance_search)

    })
    

    if (response.status == 500) {
        set_server_error_found(true)
        set_loading(false)
        set_result_found(false)
        return {}
    }

    if (response.status == 404) {
        set_server_error_found(false)
        set_loading(false)
        set_result_found(false)
        set_no_result_found_text(true)
        return {}
        
    }
    const data_fetch = await response

    console.log("ddddd " , data_fetch )
    
    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "qjis_localisation.csv";
    document.body.appendChild(a);
    console.log(a,url,document.body)
    a.click();

    a.remove();
    window.URL.revokeObjectURL(url);
    set_result_found(true)
    set_loading(false)
    return data_fetch

    }


    function handle_text_input (event:any) {
      // console.log("tototo");
      settext_input(event.target.value)
    }


    

//   for (var i = 0; i <= 100;i++) {
//     list_of_random_position.push([getRandomArbitrary(-89,89),getRandomArbitrary(-179,179)])
//   }

    
    
    let dict_of_advance_search_empty = {
      "job":"",
      "is_alive":false
    }

    var generic_chart : any = ""
    var generic_dict = ""

    var list_of_graph : any = []
    var list_of_dict : any = []
    var list_of_keys_name : any = []
    if (result_found == true) {
        
    }




    
    
    const tooltipTriggerList = document.querySelectorAll(
        '[data-bs-toggle="tooltip"]'
      );

      tooltipTriggerList.forEach((tooltipTriggerEl) => {
        new Tooltip(tooltipTriggerEl);
      });
    



    // function add_space(number: number) {
    //     const br_list:any = []
    //     for (let i = 0 ; i < number ; i++) {
    //         br_list.push(<br></br>)  
    //     }

    //     return br_list
    // }

    

  function Custom_navbar(variable:any = "") {
    
    return (
          <nav className="navbar navbar-expand-lg  navbarBGcolor fixed-top navbar_color">
          <div className="container-fluid">
              
              <div className="d-grid gap-2">
                  <a type="button" className="btn btn-dark" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
              </div>
              
              {/* <a type="button" className="btn btn-secondary" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
              <a type="button" className="btn btn-secondary" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
              <a type="button" className="btn btn-secondary" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
              <a type="button" className="btn btn-secondary" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
              <a type="button" className="btn btn-secondary" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
               */}
          </div>


          
          {/* <select className="form-select w-25 mx-auto" style={{backgroundColor:"#cad3db"}} aria-label="Multiple select example">
              <option>Somaire</option>
              <option>TEST1</option>
              <option>TEST2</option>
              <option>TEST3</option>
          </select>
           */}
          </nav>
      )  
}

    function handle_dict_of_advance_search(event:any,key:any) {
        set_dict_of_advance_search((prev: any) => ({
        ...prev,
        [key]: event.target.value,
        }));
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
                       <option selected>Periode historique?</option>
                       
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
                       onChange={(event) => handle_dict_of_advance_search(event,"display_only_one_person_per_first_name")}
   >
                       <option selected>Afficher seulement un utilisateur par prénom?</option>
                       
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
                       onChange={(event) => handle_dict_of_advance_search(event,"display_only_one_person_per_last_name")}
   >
                       <option selected>Afficher seulement un utilisateur par nom de famille?</option>
                       
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
   
                                       
   
                 </div>
                 
                 <div className="modal-footer">
                   
                   <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                   <button type="button" className="btn btn-danger" data-bs-dismiss="modal" onClick={() => window.location.reload()}>Reset</button>
                   <button type="button" className="btn btn-primary" data-bs-dismiss="modal" onClick={() => get_list_of_user_advanced_search().then((result) => set_total_number_of_user_found(result.nb_of_user_found))}>Rechercher 🔎</button>
                   
                 </div>
               </div>
             </div>
           </div>
         </div> 
       )
    }

   console.log("opkoprekgoper " , total_number_of_user_found)
   return (

    <div className="container">
        <div
            className=""
        >

        

        {result_found == false &&(
            <div>

              <div className="mobile-only">
                
                <br></br>
                
                
                <h1 className="wikifont">
                  Cette fonctionnalité nécessite le logiciel QGIS et n’est donc disponible que sur PC.
                </h1>
                
                <br></br>
                <br></br>
                
                <div className="d-grid gap-2">
                  <a type="button" className="btn btn-secondary btn-xl" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
                </div>
                <br></br>
                <br></br>
                
                <img src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790349009/earth_qha8vm.gif" style={{ cursor: "pointer" }} alt="" width="390" height="390" className="me-2"/>
              
                
              </div>
              <div className="desktop-only">
                  <br></br>
                  
                  <br></br>
                  <h1 className="wikifont">
                      Generez un fichier csv de position utilisable sur qjis avec la recherche et les filtres avancés.
                  </h1>
                  <br></br>


                  <div className="d-grid gap-2">
                      <button type="button" className="btn btn-dark" onClick={() => get_list_of_user_advanced_search().then((result) => set_total_number_of_user_found(result.all_wikipedia_info))}>Generez le fichier 📁</button>
                  </div>

                  <br></br>
                  <br></br>

                  <div className="d-grid gap-2">
                      <button type="button" className="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" onClick={() => ""}>Filtres avancées 🔎</button>
                  </div>

                  <br></br>
                  <br></br>

                  <div className="d-grid gap-2">
                    <a type="button" className="btn btn-secondary" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
                  </div>
                  <br></br>
                  <br></br>

                  {server_error_found === true &&(
                    <h2 className="wikifont">
                      Erreur serveur, veuillez patienter quelques minutes.
                    </h2>
                    

                  )}
                  {server_error_found === false && result_found == false && no_result_found_text == true &&(
                    <h2 className="wikifont">
                      Aucun résultat n'a été trouvé utilise d'autres filtres
                    </h2>
                    

                  )}
                  
                  {loading == true &&(
                  <div>
                      <h2 className="wikifont">
                          Ça charge veuillez patienter quelques minutes
                      </h2>
                      
                      <img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original" width="450" height="450"></img>
                  </div>
                  )}
              </div>
            </div>
            

        )}
        
        
        {result_found == true &&(
            <div>

                {loading == true &&(
                    <div>

                        <div className="d-grid gap-2">
                            <a type="button" className="btn btn-dark" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
                        </div>
                        <br></br>    
                        <h2 className="wikifont">
                          Ça charge veuillez patienter quelques minutes
                        </h2>
                        
                        <img src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790270925/homer-simpson-the-simpsons_ovduma.gif" width="700" height="700"></img>
                        {/* <div className="tenor-gif-embed" data-postid="17234189" data-share-method="host" data-aspect-ratio="1.19403" data-width="100%"><a href="https://tenor.com/view/homer-simpson-the-simpsons-spinning-walking-floor-gif-17234189">Homer Simpson The Simpsons GIF</a>from <a href="https://tenor.com/search/homer+simpson-gifs">Homer Simpson GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
                     */}
                    
                    </div>
                    )}

                    {loading != true &&(
                    <div>
                        {Custom_navbar("")}

                        <br></br>

                        
                        {/* <div className="d-grid gap-2">
                            <a type="button" className="btn btn-dark" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
                        </div>
                        */}
                        <br></br>
                        <br></br>

                        <div className="d-grid gap-2">
                            <button type="button" className="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" onClick={() => ""}>Filtres avancées 🔎</button>
                        </div>
                        
                        <br></br>

                        <h1 className="wikifont">
                            Les pages wikipédia ont éte trouvé ton fichier va être télécharger automatiquement!:
                        </h1>

                        <br></br>
                    </div>
                    )}
            </div>

        )}

        {advanced_search_modal()}

        {/* <br></br>
        <br></br>
        
        <h2>
            ça charge...:
        </h2>
        
        <img src="https://i.makeagif.com/media/8-30-2014/64qNV9.gif" alt="2 min Countdown"></img>
         */}
        </div>
    </div>
    
  );
};

export default QjisMap;