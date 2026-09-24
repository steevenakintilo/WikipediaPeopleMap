from collections import Counter
from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django_ratelimit.decorators import ratelimit

from myapp.models import WikipediaUser , WikipediaUserUniqueTown

from random import randint
from random import sample
from django.db.models import OuterRef, Subquery

from .global_variable import *
from .utility_function  import *


import ast
import os
import json
import csv
import string
import secrets

@csrf_exempt
@ratelimit(key='ip', rate='10/m')
def display_chunck_user_birth_town_localisation_qjis(request,chunk_nb=0):
    """Display chunck (10000 users) of user birth town localisation"""
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
        if recieved_data["country_of_birth"] != "" and "/" not in recieved_data["country_of_birth"] and "Tous les pays" not in recieved_data["country_of_birth"]:

            searched_region = ""
            for region in LIST_OF_REGIONS_NAME:
                if region in recieved_data["country_of_birth"][0:-2]:
                    searched_region = region
                    break

            print(searched_region)
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
                    "country_birth_place": recieved_data["country_of_birth"][0:-3].replace("-"," ").lower().strip()
                }
        else:
            filters = {}
    except KeyError:
        filters = {}

    display_death_localisation = False

    if "country_death_place" in recieved_data:
        if recieved_data["country_death_place"] != "" and "/" not in recieved_data["country_death_place"] and "Tous les pays" not in recieved_data["country_death_place"]:
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
                filters["country_death_place"] = recieved_data["country_death_place"][0:-3].replace("-"," ").lower().strip()
            
        
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
                age = 1
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
            age = recieved_data["age"]
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
        if "-" in recieved_data["job"]:
            accept_multiple_element = True
            for job in recieved_data["job"].split("-"):
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
                filters["first_name__icontains"] = recieved_data["first_name"].replace("+","").lower().strip()
            else:
                filters["first_name"] = recieved_data["first_name"].lower().strip()

    if "last_name" in recieved_data:
        if len(recieved_data["last_name"]) != 0:
            if "+" in recieved_data["last_name"]:
                filters["last_name__icontains"] = recieved_data["last_name"].replace("+","").lower().strip()
            else:
                filters["last_name"] = recieved_data["last_name"].lower().strip()

    print(recieved_data)
    if "town_birth_place" in recieved_data:
        if ";" in recieved_data["town_birth_place"]:
            accept_multiple_element = True
            for town in recieved_data["town_birth_place"].split(";"):
                query |= Q(town_birth_place__icontains=town)
        else:
            filters["town_birth_place__icontains"] = unidecode(recieved_data["town_birth_place"])

    if "town_death_place" in recieved_data:
        if ";" in recieved_data["town_death_place"]:
            accept_multiple_element = True
            for town in recieved_data["town_death_place"].split(";"):
                query |= Q(town_death_place__icontains=town)
        else:
            filters["town_death_place__icontains"] = unidecode(recieved_data["town_death_place"])
            filters["is_alive"] = False

    
    if "birth_month_day" in recieved_data:
        if len(recieved_data["birth_month_day"]) != "0":
            filters["birth_month_day"] = recieved_data["birth_month_day"]

    if "death_month_day" in recieved_data:
        if len(recieved_data["death_month_day"]) != "0":
            filters["death_month_day"] = recieved_data["death_month_day"]
            display_death_localisation = True
        

    display_only_death_localisation = False
    if "display_only_death_localisation" in recieved_data:
        if recieved_data["display_only_death_localisation"] == "oui":
            display_only_death_localisation = True
            #recieved_data["alive_status"] = "Mort"
            filters["is_alive"] = False
            display_death_localisation = True

    if "display_only_people_born_and_dead_the_same_day" in recieved_data:
        if recieved_data["display_only_people_born_and_dead_the_same_day"] == "oui":
            filters["age__gte"] = 3
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
            filters["position__lte"] = int(recieved_data["latest_position_of_user_to_display"]) + 1
        filters["position__gte"] = -1

    sort_user_by = "None"
    if "sort_user_by" in recieved_data:
        if recieved_data["sort_user_by"] != "Par défaut":
            if recieved_data["sort_user_by"] == "Nombre de lien":
                sort_user_by = "number_of_links"
            if recieved_data["sort_user_by"] == "Nombre d'ami(e)":
                sort_user_by = "number_of_friends"
                        
            if recieved_data["sort_user_by"] == "Taille de la page wipedia":
                sort_user_by = "wikipedia_page_lenght"
            if recieved_data["sort_user_by"] == "Âge":
                sort_user_by = "age"
                filters["age__lte"] = MAXIMUM_AGE_TO_DISPLAY
            if recieved_data["sort_user_by"] == "Nombre de personnes qui les lient":
                sort_user_by = "number_of_user_who_have_linked_this_user"
            if recieved_data["sort_user_by"] == "Taille du nom de la page":
                sort_user_by = "number_of_word_in_page_name"
                                    
            #sort_user_by = recieved_data["sort_user_by"]
    #filters["town_death_localisation__icontains"] = "Undefined"
    
    if "born_before_christ" in recieved_data:
        if recieved_data["born_before_christ"] == "oui":
            filters["born_before_christ"] = True
        if recieved_data["born_before_christ"] == "non":
            filters["born_before_christ"] = False

    display_town_birth_or_death_place = False
    if "town_birth_or_death_place" in recieved_data:
        accept_multiple_element = True
        display_town_birth_or_death_place = True
        query |= Q(town_birth_place__icontains=recieved_data["town_birth_or_death_place"]) | Q(town_death_place__icontains=["town_birth_or_death_place"])
        display_death_localisation = True

    
    filters["position__gte"] = 0
    #filters["position__lte"] = 101

    #filters["age__lte"] = 123
    #filters["town_birth_place"] = "Paris"
            
    #print(recieved_data)
    print(filters)


    
    if 'birth_town_localisation__icontains' in filters:
        if filters["birth_town_localisation__icontains"] == ' ':
            filters.pop("birth_town_localisation__icontains")


    if "is_cause_of_death_known" in recieved_data:
        filters["is_cause_of_death_known"] = True
    
    if sort_user_by != "None":
        if accept_multiple_element:
            all_user_obj = WikipediaUser.objects.filter(query,**filters).order_by(f"-{sort_user_by}")
        else:
            all_user_obj = WikipediaUser.objects.filter(**filters).order_by(f"-{sort_user_by}")
    else:
        sort_user_by = "position"
        if accept_multiple_element:
            all_user_obj = WikipediaUser.objects.filter(query,**filters).order_by(f"{sort_user_by}")
        else:
            all_user_obj = WikipediaUser.objects.filter(**filters).order_by(f"{sort_user_by}")





    list_of_first_name = []
    display_only_one_person_per_first_name = False
    if "display_only_one_person_per_first_name" in recieved_data:
        if recieved_data["display_only_one_person_per_first_name"] == "oui":
            display_only_one_person_per_first_name = True

    list_of_last_name = []
    display_only_one_person_per_last_name = False
    if "display_only_one_person_per_last_name" in recieved_data:
        print("caca coco popo lili")
        if recieved_data["display_only_one_person_per_last_name"] == "oui":
            display_only_one_person_per_last_name = True
    
    list_of_all_user_data =  []
    
    list_of_localisation = []
    user_info_dict = {}
    number_of_people_to_display = 5000000000
    
    length = all_user_obj.count()
    nb_of_bad_user = 0
    for user_obj in all_user_obj:
        try:
            
            # if (user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined"):
            #     nb_of_bad_user+=1
            #     continue
            # if (user_obj.town_death_localisation == "" or user_obj.town_death_localisation.lower() == "undefined") and display_death_localisation:
            #     nb_of_bad_user+=1
            #     continue
            
            if display_only_one_person_per_first_name and user_obj.first_name_standard in list_of_first_name:
                nb_of_bad_user+=1
                continue
            elif display_only_one_person_per_first_name:
                list_of_first_name.append(user_obj.first_name_standard)
            

            if display_only_one_person_per_last_name and user_obj.last_name_standard in list_of_last_name:
                nb_of_bad_user+=1
                continue
            elif display_only_one_person_per_last_name:
                list_of_last_name.append(user_obj.last_name_standard)
            
            # elif display_only_one_person_per_first_name:
            #     continue

            # if display_only_one_person_per_last_name and user_obj.last_name_standard not in list_of_last_name:
            #     list_of_last_name.append(user_obj.last_name_standard)
            # elif display_only_one_person_per_last_name:
            #     continue

            if len(list_of_all_user_data) >= number_of_people_to_display:
                break


            if display_town_birth_or_death_place is False:
                list_of_localisation.append(dms_to_decimal(user_obj.birth_town_localisation,user_obj.page_name))

                
                # print(display_death_localisation)
                if display_only_death_localisation is False:
                    list_of_all_user_data.append(dms_to_decimal(user_obj.birth_town_localisation,"__qjis__"))
                else:
                    list_of_all_user_data.append(dms_to_decimal("blablobla"))
                            
                if display_death_localisation or display_only_death_localisation:
                    list_of_all_user_data.append(dms_to_decimal(user_obj.town_death_localisation,"__qjis__"))
            else:
                #print(user_obj.town_birth_place.lower().strip(),user_obj.town_death_place.lower().strip(),recieved_data["town_birth_or_death_place"].lower().strip())
                if user_obj.town_birth_place.lower().strip() == recieved_data["town_birth_or_death_place"].lower().strip():
                    list_of_localisation.append(dms_to_decimal(user_obj.birth_town_localisation,user_obj.page_name))                                            
                if user_obj.is_alive is False and user_obj.town_death_place.lower().strip() == recieved_data["town_birth_or_death_place"].lower().strip():
                    list_of_all_user_data.append(dms_to_decimal(user_obj.town_death_localisation,"__qjis__"))
            #print(user_info_dict)
            list_of_all_user_data.append(user_info_dict)
        except:
            pass

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump({"all_user_data":list_of_all_user_data}, file, indent=4, ensure_ascii=False)

    with open("data.json", "r", encoding="utf-8") as file:
        list_of_loc = json.load(file)
        list_of_loc = list_of_loc["all_user_data"]


    data = [
        ['latitude', 'longitude']
    ]
    for x in list_of_loc:
        data.append(x)


    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)



    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(32))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f"attachment; filename=qjis_list_of_localisation_{password}"

    writer = csv.writer(response)
    #writer.writerow(['latitude', 'longitude'])
    writer.writerows(data)

    print("total")
    print(response)

    #return HttpResponse("OK!",status=200)
    return response
    return JsonResponse({"nb_of_user_found":length - nb_of_bad_user,"response_file":response},status=200)


