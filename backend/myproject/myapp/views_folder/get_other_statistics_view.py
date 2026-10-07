# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django_ratelimit.decorators import ratelimit
from django.views.decorators.csrf import csrf_exempt

from ..global_variable import *
from ..utility_function  import *

import os

@ratelimit(key='ip', rate='5/m')
@csrf_exempt
def get_other_statistics(request):
    """Display other statistics"""
    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)

    file_path_for_ranking = rf"{os.getcwd()}\ranking_folder"
    file_path_for_gender_ratio = rf"{os.getcwd()}\ratio_of_man_and_woman"


    # FOR RANKING
        
    list_of_file_data = []
    list_of_file_name = []
    dict_of_data = {}
    list_of_list = []


    # FOR RATIO

    list_of_file_data2 = []
    list_of_file_name2 = []
    dict_of_data2 = {}
    list_of_list2 = []
    
    for file in os.listdir(file_path_for_ranking):
        size = 2501
        if file in ["$aa_name_#a_score_of_size5.txt","$ab_boy_name_#a_score_of_size5.txt","$ab_girl_name_#a_score_of_size5.txt"]:
            size = len(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n"))
        if len(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n")) > size:
            list_of_file_data.append(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n")[0:size])
        elif len(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n")) != 0:
            list_of_file_data.append(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n"))
        list_of_file_name.append(file)

    
    for file in os.listdir(file_path_for_gender_ratio):
        if len(print_file_content(rf"{file_path_for_gender_ratio}\{file}").split("\n")) > 2501:
            list_of_file_data2.append(print_file_content(rf"{file_path_for_gender_ratio}\{file}").split("\n")[0:2501])
        elif len(print_file_content(rf"{file_path_for_gender_ratio}\{file}").split("\n")) > 0:
            list_of_file_data2.append(print_file_content(rf"{file_path_for_gender_ratio}\{file}").split("\n"))
        list_of_file_name2.append(file)
   

        # try:
        #     list_of_file_data.append(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n")[0:5])
        # except:
        #     list_of_file_data.append(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n"))
        


    #index = 0

    # FOR RANKING
    for data , name in zip(list_of_file_data,list_of_file_name):
        graph_name = f"Liste des {VARIABLE_NAME_TO_DICT_FRENCH[name.split("#")[0][4:]]} classé(e)s par score présent au moins {name.split("#")[1].split("size")[1]} fois dans la liste"
        # print(graph_name)
        # print(name)
    
        for index , line in enumerate(data):
            if index == len(data) - 1:
                dict_of_data[graph_name.replace(".txt","")] = list_of_list
                list_of_list = []
                
            elif len(line) != 0:
                line_with_good_type = [line.split("#####")[0],float(line.split("#####")[1]) ,float(line.split("#####")[2])]
                list_of_list.append(line_with_good_type)
                #print(line.split("#####"))

    # FOR RATIO

    for data , name in zip(list_of_file_data2,list_of_file_name2):
        var = f"{name.split("_per_")[1].split("_of_")[0].split("#")[0]}"
        if var[-1] != "_":
            var = var+"_"
        graph_name = f"Liste des {VARIABLE_NAME_TO_DICT_FRENCH[var]} classé(e)s par ratio femmes/hommes présent au moins {name.split("size")[1].replace(".txt","")} fois dans la liste"
        for index , line in enumerate(data):
            if index == len(data) - 1:
                dict_of_data2[graph_name.replace(".txt","")] = list_of_list2
                list_of_list2 = []
                
            elif len(line) != 0:
                line_with_good_type = [line.split("#####")[0],float(line.split("#####")[1]) ,float(line.split("#####")[2]),float(line.split("#####")[3])]
                list_of_list2.append(line_with_good_type)
                #print(line.split("#####"))


    # TEST

    #print(list_of_file_data[0])
    #print(list_of_file_name[0])

    # print(file_path_for_ranking)
    # print(os.listdir(file_path_for_ranking))
    #return HttpResponse(f"YAAAY", status=200)
    #print(dict_of_data2)
    
    return JsonResponse({"ranking_list_of_dict":dict_of_data,"gender_ratio_list_of_dict":dict_of_data2},status=200)