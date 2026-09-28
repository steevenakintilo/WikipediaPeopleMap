from collections import Counter
from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.db.models import Q
from django_ratelimit.decorators import ratelimit
from django.views.decorators.csrf import csrf_exempt

from random import randint
from random import sample
from random import uniform

from ..global_variable import *
from ..utility_function  import *

import os


@csrf_exempt
def get_other_statistics(request):
    """Display chunck (10000 users) of user info"""
    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)

    print("hello")
    file_path_for_ranking = rf"{os.getcwd()}\ranking_folder"

    list_of_file_data = []
    list_of_file_name = []
    dict_of_data = {}
    for file in os.listdir(file_path_for_ranking):
        if len(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n")) > 2501:
            list_of_file_data.append(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n")[0:2501])
        elif len(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n")) != 0:
            list_of_file_data.append(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n"))
                

        # try:
        #     list_of_file_data.append(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n")[0:5])
        # except:
        #     list_of_file_data.append(print_file_content(rf"{file_path_for_ranking}\{file}").split("\n"))
        
        list_of_file_name.append(file)


    list_of_list = []

    graph_name_list = []
    index = 0
    for data , name in zip(list_of_file_data,list_of_file_name):
        #if name == "$aa_name_#d_score_of_size250.txt":
        #    return
        #graph_name = f"{VARIABLE_NAME_TO_DICT_FRENCH[name.split("#")[0]]}{name.split("#")[1]}"
        # print(name.split("#")[0][4:])
        # print(VARIABLE_NAME_TO_DICT_FRENCH[name.split("#")[0][4:]])
        graph_name = f"Liste des {VARIABLE_NAME_TO_DICT_FRENCH[name.split("#")[0][4:]]} classé(e)s par score présent au moins {name.split("#")[1].split("size")[1]} fois dans la liste"
        if "ville" in graph_name:
            print(graph_name)
        # if "continent" in graph_name.lower():
        #     graph_name = f"Liste des {VARIABLE_NAME_TO_DICT_FRENCH[name.split("#")[0][4:]]} classé(e)s par score présent au moins {name.split("#")[1].split("size")[1]} fois dans la liste"


        #if name == "$aa_name_#c_score_of_size100.txt":  
        #    print(name)

        for index , line in enumerate(data):
            if index == len(data) - 1:
                dict_of_data[graph_name.replace(".txt","")] = list_of_list
                list_of_list = []
                
            elif len(line) != 0:
                line_with_good_type = [line.split("#####")[0],float(line.split("#####")[1]) ,float(line.split("#####")[2])]
                list_of_list.append(line_with_good_type)
                #print(line.split("#####"))
                    
    #print(list_of_file_data[0])
    #print(list_of_file_name[0])

    # print(file_path_for_ranking)
    # print(os.listdir(file_path_for_ranking))
    #return HttpResponse(f"YAAAY", status=200)
    return JsonResponse({"ranking_list_of_dict":dict_of_data},status=200)