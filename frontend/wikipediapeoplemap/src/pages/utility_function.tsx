
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
    console.error(list_ , error);
    // Expected output: ReferenceError: nonExistentFunction is not defined
    // (Note: the exact output may be browser-dependent)
    }
   
    return list_of_dict
}


export function generate_list_of_dict2(list_:any,big_index:number) {
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
            console.error(list_ , error);
            // Expected output: ReferenceError: nonExistentFunction is not defined
            // (Note: the exact output may be browser-dependent)
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
        console.error(list_ , error);
        // Expected output: ReferenceError: nonExistentFunction is not defined
        // (Note: the exact output may be browser-dependent)
        }

    }
   
    return list_of_dict
}



export function generate_list_of_dict3(list_:any,big_index:number) {
    let list_of_dict:any = [];

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {
            list_of_dict.push({ data_name: data[0], data_number: data[1] , data_occurence: data[2]});
        }
        
    });

    } catch (error) {
    console.error(list_ , error);
    // Expected output: ReferenceError: nonExistentFunction is not defined
    // (Note: the exact output may be browser-dependent)
    }
   
    return list_of_dict
}

export function generate_list_of_dict4(list_:any,big_index:number) {
    let list_of_dict:any = [];

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {
            list_of_dict.push({ data_name: data[0], ratio_girl: data[1] , ratio_boy: data[2],data_occurence : data[3]});
        }
        
    });

    } catch (error) {
    console.error(list_ , error);
    // Expected output: ReferenceError: nonExistentFunction is not defined
    // (Note: the exact output may be browser-dependent)
    }
   
    return list_of_dict
}

export function generate_list_of_dict_with_date(list_:any,big_index:number) {
    let list_of_dict:any = [];

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {
            
            list_of_dict.push({ data_name:  new Date(data[0].toString()), data_number: data[1] });            
        }
        
    });

    } catch (error) {
    //console.error(list_ , error);
    // Expected output: ReferenceError: nonExistentFunction is not defined
    // (Note: the exact output may be browser-dependent)
    }
   
    return list_of_dict
}

// export function generate_list_of_dict2(list_:any,list2_:any,big_index:number) {
//     let list_of_dict:any = [];

//     list_.forEach((data, index) => {
//         if (index < big_index && list2_[index] > 0) {
//         list_of_dict.push({ data_name:  new Date(data), data_number: list2_[index] });
//         }
//     });

//     return list_of_dict
// }

export function generate_list(list_:any) {
    let generated_list:any = [];
    list_.forEach((data, index:number) => {
    generated_list.push(<li key={index}>{data}</li>);
    });

    return generated_list
}

    
export function make_a_graphic(type:string,dict_data:string,graph_title:string) {
    
    let series_data: any = []
    if (graph_title == "birth_and_death_year" || graph_title == "death_year" || graph_title == "birth_year") {
        series_data = [{ type: 'bar', xKey: 'data_name', yKey: 'data_number' , fill:generate_random_colour()}]
        
        let graph_data = {
            data: dict_data,
            series: series_data,
            title: { text: graph_title },
            axes: [
            {
                    type: "time",
                    position: "bottom"
                },
                {
                    type: "number",
                    position: "left"
                }
            ],
            // navigator: {
            //     enabled: true,

            //     miniChart: {
            //         enabled: true
            //     }
            // },

            // zoom: {
            //     enabled: true
            // }            
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

        axes: [
            {
                type: "category",
                position: "bottom",
                title: {
                    text: "Variable"
                }
            },
            {
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
        ],

        // // navigator: {
        //     enabled: true,
        //     miniChart: {
        //         enabled: true
        //     }
        // },

        // zoom: {
        //     enabled: true
        // }
    }

    return graph_data
}



export function generate_list_of_dict_for_scatter(list_:any,big_index:number) {
    let list_of_dict:any = [];

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {        
            list_of_dict.push({ x_value: data[1],y_value: data[2],other_data:data[0]})
        }
        
    });

    } catch (error) {
    console.error(list_ , error);
    // Expected output: ReferenceError: nonExistentFunction is not defined
    // (Note: the exact output may be browser-dependent)
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

export function make_a_graphic2(type:string,value1:string,var_name1:string,value2:string,var_name2:string,graph_title:string) {
    
    let series_data: any = []
    if (type === "bar") {
        series_data = [{ type: 'bar', xKey: 'data_name', yKey: 'data_number' , fill:generate_random_colour()}]
    } else if (type === "pie") {
        series_data = [{ type: 'pie', legendItemKey: 'data_name', angleKey: 'data_number', fill:generate_random_colour()}]
    } else if (type === "line") {
        series_data = [{ type: 'line', xKey: 'data_name', yKey: 'data_number', fill:generate_random_colour()}]
    } else if (type === "donut") {
        series_data = [{ type: 'donut', legendItemKey: 'data_name', angleKey: 'data_number', fill:generate_random_colour()}]
    }
    
    let graph_data = {
        data: [
            { data_name: var_name1, data_number: value1},
            { data_name: var_name2, data_number: value2},
        ],
        
        series: series_data,
        title: { text: graph_title },
        
    }
    
    return graph_data
    }

export function make_a_graphic3(type:string,dict_data:string,graph_title:string) {
    
    let series_data: any = []
    
    series_data = [{ type: 'line', xKey: 'data_name', yKey: 'data_number', fill:generate_random_colour()}]

    let graph_data = {
        data: dict_data,
        series: series_data,
        title: { text: graph_title },
        
    }
    
    return graph_data
}
    
