// import { ComposableMap, Geographies, Geography } from "react-simple-maps";

// import geoUrl from "../custom.geo.json";

import { Tooltip } from "bootstrap";
import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";

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

import "./home.css";
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import {NUMBER_OF_USER} from './global_variable'
import {list_of_countries , list_of_country_flag,VAR_TO_DESCRIPTION,STAT_TO_DESCRIPTION} from "./global_variable.tsx"
import { generate_list_of_dict , make_a_graphic , generate_list_of_dict_with_date , YearsChart} from "./utility_function.tsx";

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

const Statistics = () => {
    //const [list_of_user_data,set_list_of_user_data] : any = useState({});
    const [list_of_user_data,set_list_of_user_data] : any = useState({});

    const [result_found,set_result_found] : any = useState(false)
    const [loading,set_loading] : any = useState(false)
    useEffect(() => {
        // get_list_of_user_advanced_search().then((result) => {
        //     set_list_of_user_data(result.all_user_data)
        //     console.log("typeof: ", typeof(result.all_user_data))
        // })

    }, []);
 

    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    const [dict_info,set_dict_info] : any = useState({});
    const [keys_info,set_keys_info] : any = useState({});
    const [text_input, settext_input] = useState("");





    function handle_dict_and_keys_info(dict_info:any,keys_info:string) {
      set_dict_info(dict_info)
      set_keys_info(keys_info)
    }
    async function get_list_of_user_advanced_search() {
      
      
      //setchunck(0)
      set_loading(true)
      const response = await fetch(`http://127.0.0.1:8000/get_advanced_statistics`, {
          method: 'POST',
          //headers: {"Content-Type" : "application/json",Authorization: `Bearer ${token}`,},
          headers: {"Content-Type" : "application/json"},
          body:JSON.stringify(dict_of_advance_search)

      })
      
      const data_fetch = await response.json()

      set_result_found(true)
      set_loading(false)
      ////console.log("blbabla " , data_fetch[0])
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
        
        const keys = Object.keys(list_of_user_data);
        
        //console.log(list_of_user_data["age"] , " meade lux lewis")
        for (var i = 0; i < keys.length - 1; i++) {    
            
            if (list_of_user_data[keys[i]].length > 1) {
                //console.log("caq ", keys[i])
                list_of_keys_name.push(keys[i])
                if (keys[i] != "age" && keys[i] != "grade_over_20" && keys[i] != "wikipedia_page_lenght" && keys[i] != "preciseness_level" && keys[i] != "dict_of_error" && keys[i] != "number_of_error_per_page" && keys[i] != "age_group"
                  && keys[i] != "birth_year" && keys[i] != "death_year" && keys[i] != "birth_and_death_year"
                ) {
                    generic_dict = generate_list_of_dict(list_of_user_data[keys[i]],10)
                    generic_chart = make_a_graphic("bar" , generic_dict,VAR_TO_DESCRIPTION[keys[i]])
                    list_of_graph.push(generic_chart)
                    if (keys[i] != "town_birth_and_death_place" && keys[i] != "town_birth_place" && keys[i] != "town_death_place" && keys[i] != "dict_of_error_counter") {
                      list_of_dict.push(generate_list_of_dict(list_of_user_data[keys[i]],2000))
                    } 
                      else {
                      list_of_dict.push(generate_list_of_dict(list_of_user_data[keys[i]],500))
                    
                    }
                    
                } else if (keys[i] == "dict_of_error") {
                    generic_dict = generate_list_of_dict(list_of_user_data[keys[i]],3)
                    generic_chart = make_a_graphic("bar" , generic_dict,VAR_TO_DESCRIPTION[keys[i]])
                    list_of_graph.push(generic_chart)
                    list_of_dict.push(generate_list_of_dict(list_of_user_data[keys[i]],500))
                } else if (
                    keys[i] == "birth_year" ||
                    keys[i] == "death_year" ||
                    keys[i] == "birth_and_death_year"
                ) {
                    generic_dict = generate_list_of_dict_with_date(
                        list_of_user_data[keys[i]],
                        100000
                    );

                    list_of_graph.push({
                        type: "echarts",
                        data: generic_dict,
                    });

                    list_of_dict.push(
                        generate_list_of_dict(
                            list_of_user_data[keys[i]],
                            500
                        )
                    );
                }  else {
                    generic_dict = generate_list_of_dict(list_of_user_data[keys[i]],10000000)
                    generic_chart = make_a_graphic("bar" , generic_dict,VAR_TO_DESCRIPTION[keys[i]])
                    list_of_graph.push(generic_chart)
                    list_of_dict.push(generate_list_of_dict(list_of_user_data[keys[i]],500))
                    
                }
                
            }

            //console.log("fpoekfgezkpo " , )
        }
        //console.log("coca cola " , generic_chart)
        
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
                     <input className="form-control w-100" type="text" placeholder={"Métier ex: acteur ou chanteuse-peintre-médecin ou foot"} onChange={(event) => handle_dict_of_advance_search(event,"job")}></input>
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
                   <button type="button" className="btn btn-primary" data-bs-dismiss="modal" onClick={() => get_list_of_user_advanced_search().then((result) => set_list_of_user_data(result.all_wikipedia_info))}>Rechercher 🔎</button>
                   
                 </div>
               </div>
             </div>
           </div>
         </div> 
       )
    }


    function detailed_stat_modal(data_dict:any) {
      
      if (result_found == false) {
        data_dict = {}
      }

      var total_number : any = 0
      var text_to_display = "Son%"
      {Object.values(data_dict).map((data:any,index:number) => (
        total_number+=data.data_number
      ))}
      if (keys_info == "dict_of_error") {
        total_number = list_of_user_data.number_of_user_found
        text_to_display = "% de personnes avec cette erreur"
      }
      console.log(list_of_user_data.number_of_user_found)
      return(
         <div>
           <div className="modal fade" id="exampleModal2" aria-labelledby="exampleModalLabel2" aria-hidden="true">
             <div className="modal-dialog modal-lg">
               <div className="modal-content">
                 <div className="modal-header">
                   <h1 className="modal-title fs-5" id="exampleModalLabel2">Statistiques détaillées: {VAR_TO_DESCRIPTION[keys_info]}</h1>
                   <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                 </div>
                  
                 <div className="modal-body">
                    {/* <input name="myInput" placeholder={"Cherche ton élement"} onChange={handle_text_input}/> */}
                    
                    <input name="myInput" placeholder={"Cherche ton élement"} onChange={handle_text_input}/>
                    <TableContainer component={Paper}>
                    <Table>
                      <TableHead>
                        <TableRow>
                          <TableCell>{"."}</TableCell>
                          <TableCell>{"Element"}</TableCell>
                          <TableCell>{"Nombre de fois qu'il est présent"}</TableCell>
                          <TableCell>{text_to_display}</TableCell>
                          <TableCell>{"Nombre total d'élements"}</TableCell>
                          
                        </TableRow>
                      </TableHead>

                      <TableBody>
                        {Object.values(data_dict).map((data:any,index:number) => (

                          data.data_name.toString().toLowerCase().includes(text_input.toLowerCase()) != "" && (
                            <TableRow key={index}>
                              <TableCell>{index + 1}</TableCell>
                              <TableCell>{data.data_name}</TableCell>
                              <TableCell>{data.data_number}</TableCell>
                              <TableCell>{Math.round((data.data_number/total_number * 100) * 100)/100}</TableCell>
                              <TableCell>{total_number}</TableCell>
                              
                              
                              
                            </TableRow>
                          )
                        ))}
                      </TableBody>
                    
                    </Table>
                  </TableContainer>
                    <br></br>
                    
                 </div>
                 
                 <div className="modal-footer">
                   <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                 </div>
               </div>
             </div>
           </div>
         </div> 
       )
    }
   return (

    <div className="container">
        <div
            className=""
        >

        

        {result_found == false &&(
            <div>
                
                
                <br></br>
                
                <br></br>
                <h1 className="wikifont">
                    Consultez les statistiques détaillées des pages Wikipédia et affinez vos recherches grâce aux filtres avancés.
                </h1>
                <br></br>


                <div className="d-grid gap-2">
                    <button type="button" className="btn btn-dark" onClick={() => get_list_of_user_advanced_search().then((result) => set_list_of_user_data(result.all_wikipedia_info))}>Rechercher 🔎</button>
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
              
                {loading == true &&(
                <div>
                    <h2 className="wikifont">
                        ça charge (maximum 5 minutes)...:
                    </h2>
                    
                    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original" alt="2 min Countdown"></img>
                </div>
                )}
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
                        <h2>
                            ça charge...
                        </h2>
                        
                        <div className="tenor-gif-embed" data-postid="17234189" data-share-method="host" data-aspect-ratio="1.19403" data-width="100%"><a href="https://tenor.com/view/homer-simpson-the-simpsons-spinning-walking-floor-gif-17234189">Homer Simpson The Simpsons GIF</a>from <a href="https://tenor.com/search/homer+simpson-gifs">Homer Simpson GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
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
                        Statistiques détaillées des {list_of_user_data.number_of_user_found} pages Wikipédia:
                    </h1>

                    <br></br>
                    
                    {/* <div>
                        <AgCharts options={test_chart} />  
                    </div>
                                        */}

                    {/* <div>
                        <AgCharts options={generic_chart} />  
                    </div>
                    */}

                    
                    {list_of_graph
                        .map((graph:any, index:number) => (
                        <div>
                            {["first_name","gender","town_birth_place","country_birth_place","continent_of_birth","region_of_birth","birth_date","born_and_died_in_the_same_town","born_before_christ","first_char_of_the_page","no_country_counter"].includes(list_of_keys_name[index]) &&(
                              <div>
                              <br></br>
                              <br></br>
                              <br></br>
                              <br></br>
                              
                                <h1 className="wikifont"><mark>- {STAT_TO_DESCRIPTION[list_of_keys_name[index]]}</mark></h1>
                              </div>

                            )}
                            
                            {graph.type === "echarts" ? (
                                <YearsChart data={graph.data} />
                            ) : (
                                <AgCharts options={graph} />
                            )}
                            <br></br>
                            <br></br>
                            
                            <div className="d-grid gap-2">
                                <button className="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal2" onClick={() => (handle_dict_and_keys_info(list_of_dict[index],list_of_keys_name[index]))}>
                                    {"Toutes les statistiques 📊"}
                                </button>
                            </div>
                        
                        </div>

                    ))}

                </div>
                )}
            </div>

        )}
        {advanced_search_modal()}
        {detailed_stat_modal(dict_info)}

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

export default Statistics;