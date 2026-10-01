
import { useState} from 'react';

export function generate_random_colour() {
    return '#'+(Math.random() * 0xFFFFFF << 0).toString(16).padStart(6, '0');
}


export function is_screen_for_mobile() {
    if (window.screen.width <= 768) {
        return true
    }
    return false
    
}
export function generate_list_of_dict(list_:any,big_index:number) {
    let list_of_dict:any = [];

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {
            
            if (data[0].toString().toLowerCase() == "true") {
                list_of_dict.push({ data_name: data[1] + " Vrai", data_number: data[1] });
            } else if (data[0].toString().toLowerCase() == "false") {
                list_of_dict.push({ data_name: data[1] + " Faux", data_number: data[1] });
            } else {
                list_of_dict.push({ data_name: data[0], data_number: data[1] });
            }
            
            
        }
        
    });

    } catch (error) {
    }
   
    return list_of_dict
}


export function generate_list_of_dict_with_a_lenght_limit(list_:any,big_index:number) {
    let list_of_dict:any = [];
    if (list_ == undefined) {
        return
    }
    if (list_.length <= 500) {
        try {
            list_.forEach((data:any, index:number) => {
                if (index < big_index) {
                    list_of_dict.push({ data_name: data[0], data_number: data[1] });
                }
                
            });

            } catch (error) {
            }

    } else {
            try {
                list_.forEach((data:any, index:number) => {
                    if (index < big_index) {
                        
                        if (data[1]  >= 25) {
                            list_of_dict.push({ data_name: data[0], data_number: data[1] });
                        }
            }
        });

        } catch (error) {
        }

    }
   
    return list_of_dict
}



export function generate_list_of_dict_with_three_params_as_data(list_:any,big_index:number) {
    let list_of_dict:any = [];

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {
            list_of_dict.push({ data_name: data[0], data_number: data[1] , data_occurence: data[2]});
        }
        
    });

    } catch (error) {
    //console.error(list_ , error);
    // Expected output: ReferenceError: nonExistentFunction is not defined
    // (Note: the exact output may be browser-dependent)
    }
   
    return list_of_dict
}

export function generate_list_of_dict_with_four_params_as_data(list_:any,big_index:number) {
    let list_of_dict:any = [];

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {
            list_of_dict.push({ data_name: data[0], ratio_girl: data[1] , ratio_boy: data[2],data_occurence : data[3]});
        }
        
    });

    } catch (error) {
    }
   
    return list_of_dict
}
    
export function make_a_graphic(type:string,dict_data:string,graph_title:string) {
    
    let series_data: any = []
    if (graph_title == "birth_and_death_year" || graph_title == "death_year" || graph_title == "birth_year") {
        series_data = [{ type: 'bar', xKey: 'data_name', yKey: 'data_number' , fill:generate_random_colour()}]
        
        let graph_data = {
            data: dict_data,
            series: series_data,
            title: { text: graph_title },
            axes: {
                x: {
                    type: "time",
                    position: "bottom"
                },
                y: {
                    type: "number",
                    position: "left"
                }
            },
        }
        
        return graph_data
    } else {
        if (type === "bar") {
        series_data = [{ type: 'bar', xKey: 'data_name', yKey: 'data_number' , fill:generate_random_colour()}]
        } else if(type === "bar-horizontal") {
        series_data = [{ type: 'bar', direction: "horizontal",xKey: 'data_name', yKey: 'data_number' , fill:generate_random_colour()}]
        } else if (type === "pie") {
            series_data = [{ type: 'pie', legendItemKey: 'data_name', angleKey: 'data_number', fill:generate_random_colour()}]
        } else if (type === "line") {
            series_data = [{ type: 'line', xKey: 'data_name', yKey: 'data_number', fill:generate_random_colour()}]
        } else if (type === "donut") {
            series_data = [{ type: 'donut', legendItemKey: 'data_name', angleKey: 'data_number', fill:generate_random_colour()}]
        } else if (type === "area") {
            series_data = [{ type: 'area', xKey: 'data_name', yKey: 'data_number', fill:generate_random_colour()}]
        }
        
        let graph_data = {
            data: dict_data,
            series: series_data,
            title: { text: graph_title },        
        }
        
        return graph_data
    }
    
}

export function make_a_stacked_bar_graphic(
    dict_data: any,
    graph_title: string
) {

    let series_data: any = []

    series_data = [
        {
            type: 'bar',
            xKey: 'data_name',
            yKey: 'ratio_boy',
            yName: 'Homme',
            stacked: true,
            normalizedTo: 100,
            fill: generate_random_colour()
        },
        {
            type: 'bar',
            xKey: 'data_name',
            yKey: 'ratio_girl',
            yName: 'Femme',
            stacked: true,
            normalizedTo: 100,
            fill: generate_random_colour()
        }
    ]

    let graph_data = {
        data: dict_data,

        series: series_data,

        title: {
            text: graph_title
        },

        axes: {
            x: {
                type: "category",
                position: "bottom",
                title: {
                    text: "Variable"
                }
            },
            y: {
                type: "number",
                position: "left",
                min: 0,
                max: 100,
                label: {
                    formatter: (params: any) => {
                        return `${params.value}%`
                    }
                },
                title: {
                    text: "Pourcentage"
                }
            }
        },
    }

    return graph_data
}

  export function navbar() {
    
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

// A GARDER SI JE VEUX RETESTER LES SCATTER
export function generate_list_of_dict_for_scatter(list_:any,big_index:number) {
    let list_of_dict:any = [];

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {        
            list_of_dict.push({ x_value: data[1],y_value: data[2],other_data:data[0]})
        }
        
    });

    } catch (error) {
    }
   
    return list_of_dict
}



export function make_a_graphic_scatter(dict_data:string,graph_title:string) {
    
    let series_data: any = []
    series_data = [
    {
        type: 'bar',
        xKey: 'other_data',
        yKey: 'x_value',
        yName: 'Score',

        tooltip: {
                renderer: (params: any) => ({
                    title: params.datum.other_data,
                    data: [
                        {
                            label: 'Score',
                            value: params.datum.x_value
                        },
                        {
                            label: "Nombre d'occurrences",
                            value: params.datum.y_value
                        }
                    ]
                })
            }
        }
    ]
    let graph_data = {
        data: dict_data,
        series: series_data,
        title: { text: graph_title },
        axes: {
            x: {
                type: 'number',
                title: {
                    text: 'Score'
                }
            },
            y: {
                type: 'number',
                title: {
                    text: "Nombre d'occurrences"
                }
            }
        }
    }

    return graph_data
}
