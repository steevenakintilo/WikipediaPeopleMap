
import { useState} from 'react';

export function generate_random_colour() {
    return '#'+(Math.random() * 0xFFFFFF << 0).toString(16).padStart(6, '0');
}
    
export function generate_list_of_dict(list_:any,big_index:number) {
    let list_of_dict:any = [];
    //console.log("Print de debug " , list_)

    try {
     list_.forEach((data:any, index:number) => {
        if (index < big_index) {
            
            if (data[0].toString().toLowerCase() == "true") {
                list_of_dict.push({ data_name: "Oui", data_number: data[1] });
            } else if (data[0].toString().toLowerCase() == "false") {
                list_of_dict.push({ data_name: "Non", data_number: data[1] });
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

export function generate_list_of_dict2(list_:any,list2_:any,big_index:number) {
    let list_of_dict:any = [];

    list_.forEach((data, index) => {
        if (index < big_index && list2_[index] > 0) {
        list_of_dict.push({ data_name:  new Date(data), data_number: list2_[index] });
        }
    });

    return list_of_dict
}

export function generate_list(list_:any) {
    let generated_list:any = [];
    list_.forEach((data, index:number) => {
    generated_list.push(<li key={index}>{data}</li>);
    });

    return generated_list
}

// export function go_to_detailed_stat_page(value_list:any,occurence_list:any,ratio_list:any,len_of_list:any,retrieved_data:any,type_nb:number) {
//     //navigate('/detailed_stat',{state: [value_list,occurence_list,ratio_list,retrieved_data,len_of_list]});
//     localStorage.setItem(
//         "detailed_data_stat",
//         JSON.stringify([value_list, occurence_list, ratio_list, retrieved_data, len_of_list,type_nb])
//     );
    
//     window.open('/detailed_stat', '_blank');
//     }
    
//     export function generate_random_colour() {
//     return '#'+(Math.random() * 0xFFFFFF << 0).toString(16).padStart(6, '0');
// }
    
export function make_a_graphic(type:string,dict_data:string,graph_title:string) {
    
    let series_data: any = []
    if (type === "bar") {
        series_data = [{ type: 'bar', xKey: 'data_name', yKey: 'data_number' , fill:generate_random_colour()}]
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
    
