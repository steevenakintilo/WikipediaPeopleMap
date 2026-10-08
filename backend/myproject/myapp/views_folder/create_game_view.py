from collections import Counter
from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django_ratelimit.decorators import ratelimit
from django.db.models import Case, When

from myapp.models import WikipediaUser , WikipediaUserUniqueTown

from random import randint
from random import sample
from django.db.models import OuterRef, Subquery

from ..global_variable import *
from ..utility_function  import *


import ast
import os
import json
import csv

import random
import traceback

@csrf_exempt
@ratelimit(key='ip', rate='20/2m', block=False)
def who_was_born_first(request):
    """A function that create a who is older game"""
    try:
        if getattr(request, 'limited', False):
            return JsonResponse(
                {
                    "error": "too_many_requests",
                    "message": "Trop de requêtes. Veuillez patienter quelques instants."
                },
                status=429
            )

        if request.method != "POST":
            return HttpResponse(f"Error!", status=404)
        
        recieved_data = json.loads(request.body)
                
        
        accept_multiple_element = False

        try:

            list_of_key_to_remove = []
            for key,value in recieved_data.items():
                if value == '':
                    list_of_key_to_remove.append(key)

            for key in list_of_key_to_remove:
                recieved_data.pop(key)
        except:
            pass

        if recieved_data == {'birth_town_localisation__icontains': ' '}:
            recieved_data = {}
        try:
            if "Tous les pays sauf la france".lower() in recieved_data["country_of_birth"].lower():
                filters = {
                    "born_outside_france":True
                }
                
            elif recieved_data["country_of_birth"] != "" and "/" not in recieved_data["country_of_birth"] and "Tous les pays" not in recieved_data["country_of_birth"]:

                searched_region = ""
                for region in LIST_OF_REGIONS_NAME:
                    if region in recieved_data["country_of_birth"][0:-2]:
                        searched_region = region
                        break

                #print(searched_region)
                if recieved_data["country_of_birth"][0:-2].replace("-"," ") in LIST_OF_CONTINENT_NAME:
                    filters = {
                        "continent_of_birth": recieved_data["country_of_birth"][0:-2].replace("-"," ").replace("Amérique","Amerique")
                    }
                elif searched_region in LIST_OF_REGIONS_NAME:
                    filters = {
                        "region_of_birth": searched_region
                    }
                    
                else:
                    filters = {
                        "country_birth_place": recieved_data["country_of_birth"][0:-3].replace("-"," ").lower()
                    }
            else:
                filters = {}
        except KeyError:
            filters = {}

        display_death_localisation = False

        if "country_death_place" in recieved_data:
            if "Tous les pays sauf la france" in recieved_data["country_death_place"]:
                filters["died_outside_france"] = True
            
            elif recieved_data["country_death_place"] != "" and "/" not in recieved_data["country_death_place"] and "Tous les pays" not in recieved_data["country_death_place"]:
                searched_region = ""
                recieved_data["alive_status"] = "Mort"
                display_death_localisation = True
                for region in LIST_OF_REGIONS_NAME:
                    if region in recieved_data["country_death_place"][0:-2]:
                        searched_region = region
                        break

                if recieved_data["country_death_place"][0:-2].replace("-"," ") in LIST_OF_CONTINENT_NAME:
                    filters["continent_of_death"] = recieved_data["country_death_place"][0:-2].replace("-"," ").replace("Amérique","Amerique")
                    
                elif searched_region in LIST_OF_REGIONS_NAME:
                    filters["region_of_death"] = searched_region
                    
                    
                else:
                    filters["country_death_place"] = recieved_data["country_death_place"][0:-3].replace("-"," ").lower()
                
            
        if "alive_status" in recieved_data:
            if recieved_data["alive_status"] == "Mort":
                filters["is_alive"] = False
                display_death_localisation = True
            if recieved_data["alive_status"] == "Vivant":
                filters["is_alive"] = True
        if "gender" in recieved_data:
            if recieved_data["gender"] == "Homme":
                filters["gender"] = "Man"
            if recieved_data["gender"] == "Femme":
                filters["gender"] = "Woman"
                    
                            
        if "preciseness_level" in recieved_data:
            if int(recieved_data["preciseness_level"]) >= 100:
                recieved_data["preciseness_level"] = 100
            filters["preciseness_level__gte"] = recieved_data["preciseness_level"]

        if "age" in recieved_data:
            if int(recieved_data["age"]) <= 0:
                age = 0
            else:
                age = recieved_data["age"]
            filters["age__gte"] = age
            if "age_max" not in recieved_data:
                filters["age__lte"] = MAXIMUM_AGE_TO_DISPLAY
                
        if "age_max" in recieved_data:
            if int(recieved_data["age_max"]) <= 0:
                age = 1
            if int(recieved_data["age_max"]) >= MAXIMUM_AGE_TO_DISPLAY:
                age = MAXIMUM_AGE_TO_DISPLAY
            else:
                age = recieved_data["age_max"]
            filters["age__lte"] = age
        
        
        if "birth_year" in recieved_data:
            if "time_period_of_birth" in recieved_data:
                if len(recieved_data["time_period_of_birth"]) != 0 and recieved_data["time_period_of_birth"] in HISTORICAL_PERIODS_WITH_DATE:
                    pass 
                else:
                    try:
                        if "+" in recieved_data["birth_year"]:
                            filters["birth_year__gte"] = int(recieved_data["birth_year"].replace("+",""))
                            filters["birth_year__lte"] = 2022
                            if "age" not in recieved_data:
                                filters["age__gte"] = 0
                                                                            
                                                    
                        else:
                            filters["birth_year"] = int(recieved_data["birth_year"])
                    except:
                        pass
            else:
                if "+" in recieved_data["birth_year"]:
                    filters["birth_year__gte"] = int(recieved_data["birth_year"].replace("+",""))
                    filters["birth_year__lte"] = 2022
                    if "age" not in recieved_data:
                        filters["age__gte"] = 0
                                                            
                else:
                    filters["birth_year"] = int(recieved_data["birth_year"])


        if "death_year" in recieved_data:
            if "time_period_of_birth" in recieved_data:
                if len(recieved_data["time_period_of_birth"]) != 0 and recieved_data["time_period_of_birth"] in HISTORICAL_PERIODS_WITH_DATE:
                    pass 
                else:
                    try:
                        if "-" in recieved_data["death_year"]:
                            filters["death_year__lte"] = int(recieved_data["death_year"].replace("-",""))
                            if "age" not in recieved_data:
                                filters["age__gte"] = 0
                            display_death_localisation = True

                                                    
                        else:
                            filters["death_year"] = int(recieved_data["death_year"])
                            display_death_localisation = True
                                                    
                    except:
                        pass
            else:
                if "-" in recieved_data["death_year"]:
                    filters["death_year__lte"] = int(recieved_data["death_year"].replace("-",""))
                    if "age" not in recieved_data:
                        filters["age__gte"] = 0
                    display_death_localisation = True
                                            
                                                            
                else:
                    filters["death_year"] = int(recieved_data["death_year"])
                    display_death_localisation = True
                                            

        query = Q()
        if "job" in recieved_data:
            if "#" in recieved_data["job"]:
                accept_multiple_element = True
                for job in recieved_data["job"].split("#"):
                    query |= Q(job__icontains=job)
                
            else:
                filters["job__icontains"] = unidecode(recieved_data["job"])

            
        if "time_period_of_birth" in recieved_data:
            if len(recieved_data["time_period_of_birth"]) != 0 and recieved_data["time_period_of_birth"] in HISTORICAL_PERIODS_WITH_DATE:
                filters["time_period_of_birth"] = HISTORICAL_PERIODS_DICT[recieved_data["time_period_of_birth"]]
                if recieved_data["time_period_of_birth"] != "Antiquité -3300-475" and "age" not in recieved_data:
                    filters["age__gte"] = -998
                                            
            if recieved_data["time_period_of_birth"] == "Indéfinie":
                filters["time_period_of_birth"] = "Undefined"
                if recieved_data["time_period_of_birth"] != "Antiquité -3300-475" and "age" not in recieved_data:
                    filters["age__gte"] = -998
                                    
        if "first_name" in recieved_data:
            if len(recieved_data["first_name"]) != 0:
                if "+" in recieved_data["first_name"]:
                    filters["first_name__icontains"] = recieved_data["first_name"].replace("+","").lower()
                elif "#" in recieved_data["first_name"]:
                    accept_multiple_element = True
                    for name in recieved_data["first_name"].split("#"):
                        query |= Q(first_name=name.lower())
                else:
                    filters["first_name"] = recieved_data["first_name"].lower()

        if "page_name" in recieved_data:
            if len(recieved_data["page_name"]) != 0:
                if "+" in recieved_data["page_name"]:
                    filters["page_name__icontains"] = recieved_data["page_name"].replace("+","").lower()
                elif "#" in recieved_data["page_name"]:
                    accept_multiple_element = True
                    for name in recieved_data["page_name"].split("#"):
                        query |= Q(first_name=name.lower())
                else:
                    filters["page_name"] = recieved_data["page_name"].lower()
        
        if "last_name" in recieved_data:
            if len(recieved_data["last_name"]) != 0:
                if "+" in recieved_data["last_name"]:
                    filters["last_name__icontains"] = recieved_data["last_name"].replace("+","").lower()
                elif "#" in recieved_data["last_name"]:
                    accept_multiple_element = True
                    for name in recieved_data["last_name"].split("#"):
                        query |= Q(last_name=name.lower())
                
                else:
                    filters["last_name"] = recieved_data["last_name"].lower()

        #print(recieved_data)
        if "town_birth_place" in recieved_data:
            if "#" in recieved_data["town_birth_place"]:
                accept_multiple_element = True
                for town in recieved_data["town_birth_place"].split("#"):
                    query |= Q(town_birth_place__icontains=unidecode(town))
            else:
                filters["town_birth_place__icontains"] = unidecode(recieved_data["town_birth_place"])

        if "town_death_place" in recieved_data:
            if "#" in recieved_data["town_death_place"]:
                accept_multiple_element = True
                for town in recieved_data["town_death_place"].split("#"):
                    query |= Q(town_death_place__icontains=unidecode(town))
            else:
                filters["town_death_place__icontains"] = unidecode(recieved_data["town_death_place"])
                filters["is_alive"] = False

        if "birth_month_day" in recieved_data:
            if len(recieved_data["birth_month_day"]) != 0:
                filters["birth_month_day"] = recieved_data["birth_month_day"]

        if "death_month_day" in recieved_data:
            if len(recieved_data["death_month_day"]) != 0:
                filters["death_month_day"] = recieved_data["death_month_day"]
                display_death_localisation = True

        if "is_cause_of_death_known" in recieved_data:
            filters["is_cause_of_death_known"] = True
            display_death_localisation = True

        if "display_only_people_born_and_dead_the_same_day" in recieved_data:
            if recieved_data["display_only_people_born_and_dead_the_same_day"] == "oui":
                filters["age__gte"] = 0
                filters["is_alive"] = False
                filters["born_and_died_in_the_same_day"] = True
                display_death_localisation = True
        
        if "display_only_people_born_and_dead_in_the_same_town" in recieved_data:
            if recieved_data["display_only_people_born_and_dead_in_the_same_town"] == "oui":
                filters["is_alive"] = False
                filters["born_and_died_in_the_same_town"] = True
                display_death_localisation = True
                
        if "country_death_place" in recieved_data:
            if "Tous les pays" in recieved_data["country_death_place"]:
                display_death_localisation = True
        if filters != {}:
            basic_search = False

        if display_death_localisation:
            filters["is_alive"] = False

        if "latest_position_of_user_to_display" in recieved_data:
            if int(recieved_data["latest_position_of_user_to_display"]) <= 1:
                filters["position"] = 1
            else:
                filters["position__lte"] = int(recieved_data["latest_position_of_user_to_display"])
            filters["position__gte"] = -1

        # filters["birth_town_localisation__icontains"] = "Undefined"
        # filters["town_birth_place"] = "Undefined"
        # filters["number_of_user_who_have_linked_this_user"] = 0
        
        if "century_of_birth" in recieved_data:
            filters["century_of_birth"] = int(recieved_data["century_of_birth"])

        if "century_of_death" in recieved_data:
            filters["century_of_death"] = int(recieved_data["century_of_death"])
        
        if "born_before_christ" in recieved_data:
            if recieved_data["born_before_christ"] == "oui":
                filters["born_before_christ"] = True
            if recieved_data["born_before_christ"] == "non":
                filters["born_before_christ"] = False

        display_either_birth_or_death_town = False
        if "town_birth_or_death_place" in recieved_data:
            display_either_birth_or_death_town = True
            accept_multiple_element = True
            display_death_localisation = True
            
            query |= Q(town_birth_place__icontains=recieved_data["town_birth_or_death_place"]) | Q(town_death_place__icontains=recieved_data["town_birth_or_death_place"])
            


        #print(display_death_localisation,display_either_birth_or_death_town,accept_multiple_element)
        filters["position__gte"] = 0
        #filters["age__lte"] = 123
                
        #print(recieved_data)
        #print(filters)
        #print(query , " popopo ")


        #list_of_game_user_can_play
        filters["list_of_game_user_can_play__contains"] = ["whoisolder"]
        
        model = WikipediaUser
        if recieved_data.get("display_only_one_person_per_town") == "oui":
            model = WikipediaUserUniqueTown

        if accept_multiple_element:
            ids = list(model.objects.filter(query, **filters).values_list("pk", flat=True))
        else:
            ids = list(model.objects.filter(**filters).values_list("pk", flat=True))

        nb = 21
        if "number_of_rounds" in recieved_data:        
            nb = int(recieved_data["number_of_rounds"])
        if nb > 21:
            nb = 21

        picked = sample(ids, min(nb, len(ids)))
        order = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(picked)])
        all_user_obj = model.objects.filter(pk__in=picked).order_by(order)
        list_of_all_user_data =  []
        nb = 21

        if len(all_user_obj) < 3:
            return JsonResponse({"all_game_data":{}},status=404)
        for i , user_obj in enumerate(all_user_obj):
            try:
                if len(list_of_all_user_data) < nb:
                    if user_obj.birth_year > all_user_obj[i + 1].birth_year:
                        answer = user_obj.page_name
                    elif user_obj.birth_year < all_user_obj[i + 1].birth_year:
                        answer = all_user_obj[i + 1].page_name
                    else:
                        answer = "les 2"
                    random_nb_1 , random_nb_2 = sample(range(1, len(all_user_obj) - 1), 2)
                    user_info_dict = {
                        "page_name":all_user_obj[random_nb_1].page_name,
                        "picture_url":all_user_obj[random_nb_1].picture_url,
                        "birth_year":all_user_obj[random_nb_1].birth_year,
                        "page_name2":all_user_obj[random_nb_2].page_name,
                        "picture_url2":all_user_obj[random_nb_2].picture_url,
                        "birth_year2":all_user_obj[random_nb_2].birth_year,
                        "answer":answer
                    }
                    list_of_all_user_data.append(user_info_dict)
                else:
                    break
            except IndexError:
                pass

        if len(list_of_all_user_data) == 0:
            user_info_dict = {
                "page_name":"personne",
                "picture_url":"personne",
                "birth_year":"personne",
                "page_name2":"personne",
                "picture_url2":"personne",
                "birth_year2":"personne",
            }
            list_of_all_user_data.append(user_info_dict)
        #print(len(list_of_all_user_data))
        return JsonResponse({"all_game_data":list_of_all_user_data},status=200)
    except:
        traceback.print_exc()
        return JsonResponse({"all_game_data":{}},status=200)