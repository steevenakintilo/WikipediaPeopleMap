import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";
import { Accordion } from 'react-bootstrap';
import {useState,useEffect } from 'react';

import { AgCharts } from "ag-charts-react";
import {
    ModuleRegistry,
    AllCommunityModule
} from "ag-charts-community";

ModuleRegistry.registerModules([AllCommunityModule]);

import 'bootstrap/dist/css/bootstrap.min.css';

import "../utils/global.css";
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import {LIST_OF_THEME} from '../utils/global_variable'
import {list_of_countries , list_of_country_flag,VAR_TO_DESCRIPTION,STAT_TO_DESCRIPTION,SUB_THEME_TO_THEME,LIST_OF_VARIABLE_THAT_NEED_COMPUTING} from "../utils/global_variable.tsx"
import { generate_list_of_dict , make_a_graphic ,generate_list_of_dict_with_a_lenght_limit,is_screen_for_mobile,navbar} from "../utils/utility_function.tsx";

import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper
} from "@mui/material";

polyfillCountryFlagEmojis();

const Statistics = () => {

    const [list_of_user_data,set_list_of_user_data] : any = useState({});



    const [list_of_graph, set_list_of_graph] = useState<any[]>([]);
    const [list_of_dict, set_list_of_dict] = useState<any[]>([]);
    const [list_of_keys_name, set_list_of_keys_name] = useState<string[]>([]);
    const [result_found,set_result_found] : any = useState(false)
    const [loading,set_loading] : any = useState(false)
    const [server_error_found,set_server_error_found] : any = useState(false)
    
    const [dict_of_advance_search,set_dict_of_advance_search] : any = useState({})
    const [dict_info,set_dict_info] : any = useState({});
    const [keys_info,set_keys_info] : any = useState({});
    const [text_input, settext_input] = useState("");
    



    useEffect(() => {
    if (!result_found) {
        return;
    }

      const keys = Object.keys(list_of_user_data);

      const new_list_of_graph: any[] = [];
      const new_list_of_dict: any[] = [];
      const new_list_of_keys_name: string[] = [];

      var number_of_bar_to_display = 10;
      if (is_screen_for_mobile() == true) {
        number_of_bar_to_display = 3
      }
      
      for (let i = 0; i < keys.length - 1; i++) {

          const key = keys[i];

          if (list_of_user_data[key].length > 0) {

              new_list_of_keys_name.push(key);

              if (
                  key !== "age" &&
                  key !== "grade_over_20" &&
                  key !== "wikipedia_page_lenght" &&
                  key !== "preciseness_level" &&
                  key !== "dict_of_error" &&
                  key !== "number_of_error_per_page" &&
                  key !== "age_group" &&
                  key !== "birth_year" &&
                  key !== "death_year" &&
                  key !== "birth_and_death_year" &&
                  key !== "birth_year_from_1900" &&
                  key !== "death_year_from_1900" &&
                  key !== "birth_and_death_year_from_1900" &&
                  key !== "number_of_view" &&
                  key !== "century_of_birth" &&
                  key !== "century_of_death"
              ) {

                  const generic_dict = generate_list_of_dict(
                      list_of_user_data[key],
                      number_of_bar_to_display
                  );

                  const generic_chart = make_a_graphic(
                      "bar",
                      generic_dict,
                      VAR_TO_DESCRIPTION[key]
                  );

                  new_list_of_graph.push(generic_chart);

                  if (
                      key !== "town_birth_and_death_place" &&
                      key !== "town_birth_place" &&
                      key !== "town_death_place" &&
                      key !== "dict_of_error_counter"
                  ) {
                      new_list_of_dict.push(
                          generate_list_of_dict(
                              list_of_user_data[key],
                              2000
                          )
                      );
                  } else {
                      new_list_of_dict.push(
                          generate_list_of_dict(
                              list_of_user_data[key],
                              500
                          )
                      );
                  }

              } else if (key === "dict_of_error") {

                  const generic_dict = generate_list_of_dict(
                      list_of_user_data[key],
                      3
                  );

                  const generic_chart = make_a_graphic(
                      "bar",
                      generic_dict,
                      VAR_TO_DESCRIPTION[key]
                  );

                  new_list_of_graph.push(generic_chart);

                  new_list_of_dict.push(
                      generate_list_of_dict(
                          list_of_user_data[key],
                          500
                      )
                  );

              } else if (
                  key === "birth_year" ||
                  key === "death_year" ||
                  key === "birth_and_death_year"
              ) {

                  const generic_dict = generate_list_of_dict_with_a_lenght_limit(
                      list_of_user_data[key],
                      50000000
                  );

                  const generic_chart = make_a_graphic(
                      "bar",
                      generic_dict,
                      VAR_TO_DESCRIPTION[key]
                  );

                  new_list_of_graph.push(generic_chart);

                  new_list_of_dict.push(
                      generate_list_of_dict_with_a_lenght_limit(
                          list_of_user_data[key],
                          50000000
                      )
                  );

              } else {

                  const generic_dict = generate_list_of_dict(
                      list_of_user_data[key],
                      10000000
                  );

                  const generic_chart = make_a_graphic(
                      "bar",
                      generic_dict,
                      VAR_TO_DESCRIPTION[key]
                  );

                  new_list_of_graph.push(generic_chart);

                  new_list_of_dict.push(
                      generate_list_of_dict(
                          list_of_user_data[key],
                          50000000
                      )
                  );
              }
          }
      }
      
      set_list_of_graph(new_list_of_graph);
      set_list_of_dict(new_list_of_dict);
      set_list_of_keys_name(new_list_of_keys_name);

  }, [list_of_user_data, result_found]);

    // A function that handle dict/keys name information

    function handle_dict_and_keys_info(dict_info:any,keys_info:string) {
      set_dict_info(dict_info)
      set_keys_info(keys_info)
    }

    // A function that get other advanced statistics about wikipedia user
    
    async function get_list_of_user_advanced_statistics() {      
      set_loading(true)
      set_server_error_found(false)

      const response = await fetch(`http://127.0.0.1:8000/get_advanced_statistics`, {
          method: 'POST',
          headers: {"Content-Type" : "application/json"},
          body:JSON.stringify(dict_of_advance_search)

      })
      
      if (response.status == 500) {
          set_server_error_found(true)
          set_loading(false)
          set_result_found(false)
          return {}
      }
      const data_fetch = await response.json()

      set_result_found(true)
      set_loading(false)
      return data_fetch

    }

    // A function to handle text input

    function handle_text_input (event:any) {
      settext_input(event.target.value)
    }

    // A function that handle the dict linked to user search filter

    function handle_dict_of_advance_search(event:any,key:any) {
        set_dict_of_advance_search((prev: any) => ({
        ...prev,
        [key]: event.target.value,
        }));
    }

    // A function that open a modal and let user search user trhough filter parameter
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
                     
                     <input className="form-control w-100" 
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
                       onChange={(event) => handle_dict_of_advance_search(event,"display_only_one_person_per_town")}>
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
                       onChange={(event) => handle_dict_of_advance_search(event,"display_only_one_person_per_job")}
   >
                       <option selected>Afficher seulement un utilisateur par métier?</option>
                       
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
                     
                     <input className="form-control w-100" type="number" min="1" max="706280" placeholder={"Position maximale de la personne à afficher"} onChange={(event) => handle_dict_of_advance_search(event,"latest_position_of_user_to_display")}></input>                  
   
                 </div>
                 
                 <div className="modal-footer">
                   
                   <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
                   <button type="button" className="btn btn-danger" data-bs-dismiss="modal" onClick={() => window.location.reload()}>Reset</button>
                   <button type="button" className="btn btn-primary" data-bs-dismiss="modal" onClick={() => get_list_of_user_advanced_statistics().then((result) => set_list_of_user_data(result.all_wikipedia_info))}>Rechercher 🔎</button>
                   
                 </div>
               </div>
             </div>
           </div>
         </div> 
       )
    }

    // A function that show detailed stat about choosen statistics
    
    function detailed_stat_modal(data_dict:any) {
      
      if (result_found == false) {
        data_dict = {}
      }

      var total_number : any = 0
      var text_to_display = "Son%"
      var display_average = false
      var avg : any = 0
      var average : any = 0
      var mediane : any = 0

      var average_step_list : any = 0
      {Object.values(data_dict).map((data:any) => (
        total_number+=data.data_number
      ))}
      if (keys_info == "dict_of_error") {
        total_number = list_of_user_data.number_of_user_found
        text_to_display = "% de personnes avec cette erreur"
      }
      if (data_dict.length > 2) {
          mediane = data_dict[Math.round(data_dict.length/2)].data_name
      }
        
      for (var i = 0; i < data_dict.length; i++) {
          if (total_number/2 >= average_step_list) {
            mediane=data_dict[i].data_name
          }
          average_step_list+=data_dict[i].data_number           
      }
      if (LIST_OF_VARIABLE_THAT_NEED_COMPUTING.includes(keys_info)) {
          {Object.values(data_dict).map((data:any) => (
            avg+= (data.data_name * data.data_number)
          ))}

        display_average = true
        average=(Math.round(avg/total_number * 10) * 10)/100
      }
      
      if (average == 0 && display_average == true) {
        mediane=0
      }
      if (display_average == false) {
        average="."
        mediane="."
      }
      return(
         <div>
           <div className="modal fade" id="exampleModal2" aria-labelledby="exampleModalLabel2" aria-hidden="true">
             <div className="modal-dialog modal-xl">
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
                          <TableCell>{"Nombre d'élements"}</TableCell>
                          
                          <TableCell>{"Moyenne"}</TableCell>
                          <TableCell>{"Mediane"}</TableCell>
                            
                        </TableRow>
                      </TableHead>

                      <TableBody>
                        {Object.values(data_dict).map((data:any,index:number) => (

                          data.data_name.toString().toLowerCase().includes(text_input.toLowerCase()) != "" && (
                            <TableRow key={index}>
                              <TableCell>{(index + 1) + "/" + data_dict.length.toString()}</TableCell>
                              <TableCell>{data.data_name}</TableCell>
                              <TableCell>{data.data_number}</TableCell>
                              <TableCell>{Math.round((data.data_number/total_number * 100) * 100)/100}</TableCell>
                              <TableCell>{total_number}</TableCell>
                              <TableCell>{average}</TableCell>
                              <TableCell>{mediane}</TableCell>
                              
                              
                              
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
                    <button type="button" className="btn btn-dark" onClick={() => get_list_of_user_advanced_statistics().then((result) => set_list_of_user_data(result.all_wikipedia_info))}>Rechercher 🔎</button>
                    
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
                {loading == true &&(
                <div>
                    <h2 className="wikifont">
                        Ça charge veuillez patienter quelques minutes
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
                          Ça charge veuillez patienter quelques minutes
                        </h2>
                        <img className="mobile-only" src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790270925/homer-simpson-the-simpsons_ovduma.gif" width="300" height="300"></img>
                        <img className="desktop-only" src="https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790270925/homer-simpson-the-simpsons_ovduma.gif" width="700" height="700"></img>
                        
                        {/* <div className="tenor-gif-embed" data-postid="17234189" data-share-method="host" data-aspect-ratio="1.19403" data-width="100%"><a href="https://tenor.com/view/homer-simpson-the-simpsons-spinning-walking-floor-gif-17234189">Homer Simpson The Simpsons GIF</a>from <a href="https://tenor.com/search/homer+simpson-gifs">Homer Simpson GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
                     */}
                    
                    </div>
                    )}

                    {loading != true &&(
                    <div>
                    {navbar()}

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


                    

                    
                    {list_of_keys_name.map((_: any, index: number) => (
                    <div key={list_of_keys_name[index]}>
                      {LIST_OF_THEME.includes(list_of_keys_name[index]) && (
                        <div>
                          <br /><br /><br /><br />

                          <Accordion>
                            <Accordion.Item eventKey={list_of_keys_name[index]}>
                              <Accordion.Header>
                              <strong style={{fontSize : "30px"}}>{LIST_OF_THEME.indexOf(list_of_keys_name[index]) + 1}- {STAT_TO_DESCRIPTION[list_of_keys_name[index]]}</strong>
                              </Accordion.Header>
                              <Accordion.Body>
                                {list_of_graph.map((graph: any, index2: number) => (
                                  <div key={index2}>
                                    {[list_of_keys_name[index]].includes(SUB_THEME_TO_THEME[list_of_keys_name[index2]]) && (
                                      <div>
                                        <AgCharts options={graph} />
                                        <br /><br />
                                        
                                        <div className="d-grid gap-2">
                                          <button
                                            className="btn btn-secondary"
                                            data-bs-toggle="modal"
                                            data-bs-target="#exampleModal2"
                                            onClick={() => handle_dict_and_keys_info(list_of_dict[index2], list_of_keys_name[index2])}
                                          >
                                            {"Toutes les statistiques 📊"}
                                          </button>
                                        </div>
                                      </div>
                                    )}
                                  </div>
                                ))}
                              </Accordion.Body>
                            </Accordion.Item>
                          </Accordion>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
                )}
            </div>

        )}

        {advanced_search_modal()}
        {detailed_stat_modal(dict_info)}
        </div>
    </div>
    
  );
};

export default Statistics;