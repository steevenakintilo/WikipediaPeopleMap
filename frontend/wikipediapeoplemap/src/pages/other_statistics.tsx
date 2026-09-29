import { polyfillCountryFlagEmojis } from "country-flag-emoji-polyfill";
import { Accordion } from 'react-bootstrap';
import {useState,useEffect } from 'react';

import { AgCharts } from "ag-charts-react";
import {
    ModuleRegistry,
    AllCommunityModule
} from "ag-charts-community";

// import {
//     ZoomModule,
//     NavigatorModule,
// } from 'ag-charts-enterprise';

// ModuleRegistry.registerModules([
//     ZoomModule,
//     NavigatorModule,
// ]);

ModuleRegistry.registerModules([AllCommunityModule]);

import 'bootstrap/dist/css/bootstrap.min.css';

import "./global.css";
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import {THEME_TO_SUB_THEMES_FOR_RANKING, LIST_OF_THEME_FOR_RANKING , LIST_OF_THEME_FOR_GENDER_RATIO , THEME_TO_SUB_THEMES_FOR_GENDER_RATIO} from './global_variable'

import {make_a_graphic ,generate_list_of_dict3, generate_list_of_dict4 , make_a_stacked_bar_graphic , is_screen_for_mobile} from "./utility_function.tsx";

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
    const [list_of_gender_data,set_list_of_gender_data] : any = useState({});
    


    const [list_of_graph, set_list_of_graph] = useState<any[]>([]);
    const [list_of_dict, set_list_of_dict] = useState<any[]>([]);
    const [list_of_keys_name, set_list_of_keys_name] = useState<string[]>([]);

    const [list_of_graph2, set_list_of_graph2] = useState<any[]>([]);
    const [list_of_dict2, set_list_of_dict2] = useState<any[]>([]);
    const [list_of_keys_name2, set_list_of_keys_name2] = useState<string[]>([]);
    
    const [result_found,set_result_found] : any = useState(false)
    const [loading,set_loading] : any = useState(false)
    const [server_error_found,set_server_error_found] : any = useState(false)
    
    const [dict_info,set_dict_info] : any = useState({});
    const [keys_info,set_keys_info] : any = useState({});
    const [text_input, settext_input] = useState("");
    

    function handle_list_of_user_data(data_recieved:any) {
        set_list_of_ranking_data(data_recieved.ranking_list_of_dict)
        set_list_of_gender_data(data_recieved.gender_ratio_list_of_dict)
        
    }



    useEffect(() => {
    if (!result_found) {
        return;
    }
      
      const keys = Object.keys(list_of_ranking_data);
      const keys2 = Object.keys(list_of_gender_data);
      
      const new_list_of_graph: any[] = [];
      const new_list_of_dict: any[] = [];
      const new_list_of_keys_name: string[] = [];

      const new_list_of_graph2: any[] = [];
      const new_list_of_dict2: any[] = [];
      const new_list_of_keys_name2: string[] = [];
      var number_of_bar_to_display = 10;
      if (is_screen_for_mobile() == true) {
        number_of_bar_to_display = 3
      }

      for (let i = 0; i < keys.length - 1; i++) {

          const key = keys[i];

          if (list_of_ranking_data[key].length >= 1) {
              

            const generic_dict = generate_list_of_dict3(
                list_of_ranking_data[key],
                number_of_bar_to_display
            );

            const generic_chart = make_a_graphic(
                "bar",
                generic_dict,
                key
            );
            
              new_list_of_keys_name.push(key);

                  new_list_of_graph.push(generic_chart);

                  new_list_of_dict.push(
                      generate_list_of_dict3(
                          list_of_ranking_data[key],
                          50000000
                      )
                  );
              }
            }
      
      for (let i = 0; i < keys2.length - 1; i++) {

          const key = keys2[i];
          if (list_of_gender_data[key].length >= 1) {
              

            const generic_dict = generate_list_of_dict4(
                list_of_gender_data[key],
                number_of_bar_to_display
            );

            const generic_chart = make_a_stacked_bar_graphic(
                generic_dict,
                key
            );
            
              new_list_of_keys_name2.push(key);

                  new_list_of_graph2.push(generic_chart);

                  new_list_of_dict2.push(
                      generate_list_of_dict4(
                          list_of_gender_data[key],
                          50000000
                      )
                  );
              }
            }
      
      
      set_list_of_graph(new_list_of_graph);
      set_list_of_dict(new_list_of_dict);
      set_list_of_keys_name(new_list_of_keys_name);

      set_list_of_graph2(new_list_of_graph2);
      set_list_of_dict2(new_list_of_dict2);
      set_list_of_keys_name2(new_list_of_keys_name2);
      
    }, [list_of_ranking_data , list_of_gender_data ,result_found]);


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
      if (result_found == false || keys_info.length == 0) {
        data_dict = {}
      }

      var total_number : any = 0
      var text_to_display = "son score"
      var average : any = 0
      var mediane : any = 0

      var average_step_list : any = 0
      {Object.values(data_dict).map((data:any) => (
        total_number+=data.data_occurence
      ))}
      
      var graph_name = ""
      
      // if (keys_info.length != 0) {
      //   graph_name = keys_info
      // }
      
      return(
         <div>
           <div className="modal fade" id="exampleModal2" aria-labelledby="exampleModalLabel2" aria-hidden="true">
             <div className="modal-dialog modal-xl">
               <div className="modal-content">
                 <div className="modal-header">
                   <h1 className="modal-title fs-5" id="exampleModalLabel2">Statistiques détaillées: {graph_name}</h1>
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
                          <TableCell>{text_to_display}</TableCell>
                          <TableCell>{"Nombre de fois qu'il est présent"}</TableCell>
                          <TableCell>{"Nombre d'élements"}</TableCell>
                          
                          
                        </TableRow>
                      </TableHead>

                      <TableBody>
                        {Object.values(data_dict).map((data:any,index:number) => (

                          data.data_name.toString().toLowerCase().includes(text_input.toLowerCase()) != "" && (
                            <TableRow key={index}>
                              <TableCell>{(index + 1) + "/" + data_dict.length.toString()}</TableCell>
                              <TableCell>{data.data_name}</TableCell>
                              <TableCell>{data.data_number}</TableCell>
                              <TableCell>{data.data_occurence}</TableCell>
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

    function detailed_stat_modal2(data_dict:any) {
      if (result_found == false || keys_info.length == 0) {
        data_dict = {}
      }

      var total_number : any = 0
      {Object.values(data_dict).map((data:any) => (
        total_number+=data.data_occurence
      ))}
      
      var graph_name = ""
      
      
      return(
         <div>
           <div className="modal fade" id="exampleModal3" aria-labelledby="exampleModalLabel3" aria-hidden="true">
             <div className="modal-dialog modal-xl">
               <div className="modal-content">
                 <div className="modal-header">
                   <h1 className="modal-title fs-5" id="exampleModalLabel3">Statistiques détaillées: {graph_name}</h1>
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
                          <TableCell>{"% de femme"}</TableCell>
                          <TableCell>{"% d'homme"}</TableCell>
                          <TableCell>{"Nombre de fois qu'il est présent"}</TableCell>
                          
                          
                          
                        </TableRow>
                      </TableHead>

                      <TableBody>
                        {Object.values(data_dict).map((data:any,index:number) => (

                          data.data_name.toString().toLowerCase().includes(text_input.toLowerCase()) != "" && (
                            <TableRow key={index}>
                              <TableCell>{(index + 1) + "/" + data_dict.length.toString()}</TableCell>
                              <TableCell>{data.data_name}</TableCell>
                              <TableCell>{data.ratio_girl}</TableCell>
                              <TableCell>{data.ratio_boy}</TableCell>
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
                    <h1 className="wikifont">
                      Le score correspond à la moyenne de tous les utilisateurs possédant cette variable.
                    </h1>

                    

                    <br></br>
                    
                    

                    {/* <AgCharts options={list_of_graph2[69]} /> */}
                    

                    <Accordion>
                        <Accordion.Item eventKey={"Ratio Homme Femme"}>
                          <Accordion.Header>
                          {/* <strong style={{fontSize : "30px"}}>- {THEME_TO_SUB_THEMES_FOR_RANKING[list_of_keys_name[index]]}</strong> */}
                          
                          <strong style={{fontSize : "30px"}}>- {"Ratio Homme Femme!"}</strong>
                          
                          </Accordion.Header>
                          <Accordion.Body>
                            {list_of_keys_name2.map((_: any, index: number) => (
                              <div key={list_of_keys_name2[index]}>
                                {LIST_OF_THEME_FOR_GENDER_RATIO.includes(list_of_keys_name2[index]) && (
                                  <div>
                                    <br /><br /><br /><br />

                                    <Accordion>
                                      <Accordion.Item eventKey={list_of_keys_name2[index]}>
                                        <Accordion.Header>
                                        {/* <strong style={{fontSize : "30px"}}>- {THEME_TO_SUB_THEMES_FOR_RANKING[list_of_keys_name[index]]}</strong> */}
                                        
                                        <strong style={{fontSize : "30px"}}>- {THEME_TO_SUB_THEMES_FOR_GENDER_RATIO[list_of_keys_name2[index]].split("classé(e)s")[0]}</strong>
                                        
                                        </Accordion.Header>
                                        <Accordion.Body>
                                          {list_of_graph2.map((graph: any, index2: number) => (
                                            <div key={index2}>
                                              {[list_of_keys_name2[index]].includes(THEME_TO_SUB_THEMES_FOR_GENDER_RATIO[list_of_keys_name2[index2]]) && (
                                                <div>
                                                  <AgCharts options={graph} />
                                                  <br /><br />
                                                  <br /><br />
                                                  <br /><br />
                                                  
                                                  
                                                  <div className="d-grid gap-2">
                                                    <button
                                                      className="btn btn-secondary"
                                                      data-bs-toggle="modal"
                                                      data-bs-target="#exampleModal3"
                                                      onClick={() => handle_dict_and_keys_info(list_of_dict2[index2], list_of_keys_name2[index2])}
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
                            
                          </Accordion.Body>
                      </Accordion.Item>
                    </Accordion>
                            

                    <br></br>
                    <br></br>
                    <br></br>

                    <Accordion>
                        <Accordion.Item eventKey={"Classement"}>
                          <Accordion.Header>
                          {/* <strong style={{fontSize : "30px"}}>- {THEME_TO_SUB_THEMES_FOR_RANKING[list_of_keys_name[index]]}</strong> */}
                          
                          <strong style={{fontSize : "30px"}}>- {"Classement!"}</strong>
                          
                          </Accordion.Header>
                          <Accordion.Body>
                            {list_of_keys_name.map((_: any, index: number) => (
                              <div key={list_of_keys_name[index]}>
                                {LIST_OF_THEME_FOR_RANKING.includes(list_of_keys_name[index]) && (
                                  <div>
                                    <br /><br /><br /><br />

                                    <Accordion>
                                      <Accordion.Item eventKey={list_of_keys_name[index]}>
                                        <Accordion.Header>
                                        {/* <strong style={{fontSize : "30px"}}>- {THEME_TO_SUB_THEMES_FOR_RANKING[list_of_keys_name[index]]}</strong> */}
                                        
                                        <strong style={{fontSize : "30px"}}>- {THEME_TO_SUB_THEMES_FOR_RANKING[list_of_keys_name[index]].split("classé(e)s")[0]}</strong>
                                        
                                        </Accordion.Header>
                                        <Accordion.Body>
                                          {list_of_graph.map((graph: any, index2: number) => (
                                            <div key={index2}>
                                              {[list_of_keys_name[index]].includes(THEME_TO_SUB_THEMES_FOR_RANKING[list_of_keys_name[index2]]) && (
                                                <div>
                                                  <AgCharts options={graph} />
                                                  <br /><br />
                                                  <br /><br />
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
                            
                          </Accordion.Body>
                        </Accordion.Item>
                      </Accordion>
                  
                    
                    {/* {list_of_graph.map((graph: any, index2: number) => (
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
                    ))} */}

                  </div>
                )}
                
            </div>

        )}

        {detailed_stat_modal(dict_info)}
        {detailed_stat_modal2(dict_info)}
        
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