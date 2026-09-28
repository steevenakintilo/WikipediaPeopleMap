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

import "./global.css";
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import {LIST_OF_THEME} from './global_variable'
import {list_of_countries , list_of_country_flag,VAR_TO_DESCRIPTION,STAT_TO_DESCRIPTION,SUB_THEME_TO_THEME,LIST_OF_VARIABLE_THAT_NEED_COMPUTING} from "./global_variable.tsx"
import { generate_list_of_dict , make_a_graphic ,generate_list_of_dict2, generate_list_of_dict_for_scatter, make_a_graphic_scatter} from "./utility_function.tsx";

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

const OtherStatistics = () => {

    const [list_of_ranking_data,set_list_of_ranking_data] : any = useState({});
    const [list_of_user_data,set_list_of_user_data] : any = useState({});
    


    const [list_of_graph, set_list_of_graph] = useState<any[]>([]);
    const [list_of_dict, set_list_of_dict] = useState<any[]>([]);
    const [list_of_keys_name, set_list_of_keys_name] = useState<string[]>([]);
    const [result_found,set_result_found] : any = useState(false)
    const [loading,set_loading] : any = useState(false)
    const [server_error_found,set_server_error_found] : any = useState(false)
    
    const [dict_info,set_dict_info] : any = useState({});
    const [keys_info,set_keys_info] : any = useState({});
    const [text_input, settext_input] = useState("");
    

    function handle_list_of_user_data(data_recieved:any) {
        set_list_of_ranking_data(data_recieved.ranking_list_of_dict)
    }



    useEffect(() => {
    if (!result_found) {
        return;
    }
      
      const keys = Object.keys(list_of_ranking_data);

      const new_list_of_graph: any[] = [];
      const new_list_of_dict: any[] = [];
      const new_list_of_keys_name: string[] = [];

      for (let i = 0; i < keys.length - 1; i++) {

          const key = keys[i];

          if (list_of_ranking_data[key].length >= 1) {
              

            const generic_dict = generate_list_of_dict_for_scatter(
                list_of_ranking_data[key],
                10
            );

            const generic_chart = make_a_graphic_scatter(
                generic_dict,
                key
            );
            
              new_list_of_keys_name.push(key);

                  new_list_of_graph.push(generic_chart);

                  new_list_of_dict.push(
                      generate_list_of_dict(
                          list_of_ranking_data[key],
                          50000000
                      )
                  );
              }
          }
      
      set_list_of_graph(new_list_of_graph);
      set_list_of_dict(new_list_of_dict);
      set_list_of_keys_name(new_list_of_keys_name);
    }, [list_of_ranking_data, result_found]);


    function handle_dict_and_keys_info(dict_info:any,keys_info:string) {
      set_dict_info(dict_info)
      set_keys_info(keys_info)
    }


    // const generic_dict = generate_list_of_dict(
    //     list_of_ranking_data["boy_name_score_of_size500"],
    //     10
    // );
    
    // const generic_chart = make_a_graphic(
    //     "bar-horizontal",
    //     generic_dict,
    //     "toto"
    // );

    console.log(list_of_graph)

    

    async function get_list_of_user_other_advanced_statistics() {      
      set_loading(true)
      set_server_error_found(false)

      const response = await fetch(`http://127.0.0.1:8000/get_other_statistics`, {
          method: 'GET',
          headers: {"Content-Type" : "application/json"},

      })
      
      if (response.status == 500) {
          set_server_error_found(true)
          set_loading(false)
          set_result_found(false)
          return {}
      }
      const data_fetch = await response.json()
      //console.log(data_fetch)
      set_result_found(true)
      set_loading(false)
      return data_fetch

    }


    function handle_text_input (event:any) {
      settext_input(event.target.value)
    }

  function navbar() {
    
    return (
          <nav className="navbar navbar-expand-lg  navbarBGcolor fixed-top navbar_color">
            <div className="container-fluid">
                
                <div className="d-grid gap-2">
                    <a type="button" className="btn btn-dark" href="/Home" style={{margin :"auto"}}>Retourner au menu</a>
                </div>
            </div>
          </nav>
    )  
  }

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
                    Consultez d'autre statistiques lié au page Wikipedia.
                </h1>
                <br></br>


                <div className="d-grid gap-2">
                    <button type="button" className="btn btn-dark" onClick={() => get_list_of_user_other_advanced_statistics().then((result) => handle_list_of_user_data(result))}>Rechercher les statistiques🔎</button>
                    
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
                    <br></br>

                    <h1 className="wikifont">
                        Autres statistiques intéressantes !
                    </h1>


                    

                    <br></br>
                    

                    {list_of_graph.map((graph: any, index2: number) => (
                        <div key={index2}>
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
                        </div>                            
                    ))}

                    {/* <AgCharts
                        options={generic_chart}
                        style={{
                            width: '1500px',
                            height: '700px'
                        }}
                    />
                     */}

                    
                    {/* <div>
                        <AgCharts options={test_chart} />  
                    </div>
                                        */}

                    {/* <div>
                        <AgCharts options={generic_chart} />  
                    </div>
                    */}


                    

                    
                    {/* {list_of_keys_name.map((_: any, index: number) => (
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
                  ))} */}
                </div>
                )}
            </div>

        )}

        {/* {detailed_stat_modal(dict_info)} */}

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

export default OtherStatistics;