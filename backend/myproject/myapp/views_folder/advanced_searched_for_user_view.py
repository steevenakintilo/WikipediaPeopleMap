from collections import Counter
from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django_ratelimit.decorators import ratelimit

from myapp.models import WikipediaUser , WikipediaUserUniqueTown

from random import randint
from random import sample

from ..global_variable import *
from ..utility_function  import *


#import hashlib
import os
import json
import traceback

@csrf_exempt
@ratelimit(key='ip', rate='30/15m',block=False)
def display_chunck_of_user_info_advanced_search(request,chunk_nb=0):
    """Display chunck of user info with advanced search"""

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

        recieved_data["chunk_nb"] = chunk_nb
        if recieved_data == {'birth_town_localisation__icontains': ' '}:
            recieved_data = {}

        #print(recieved_data)
        cache_key = stats_cache_key("adv_searchs",recieved_data)
        cached = cache.get(cache_key)
        if cached is not None:
            return JsonResponse({"all_user_data":cached}, status=200)

        
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

        number_of_people_to_display = NUMBER_OF_USERS_TO_SEARCH
        if "number_of_people_to_display" in recieved_data:
            if type(recieved_data["number_of_people_to_display"]) == str:
                if int(recieved_data["number_of_people_to_display"]) <= 0:
                    number_of_people_to_display = 1
                elif int(recieved_data["number_of_people_to_display"]) >= 500:
                    number_of_people_to_display = 500
                else:
                    number_of_people_to_display = int(recieved_data["number_of_people_to_display"])

        if "birth_month_day" in recieved_data:
            if len(recieved_data["birth_month_day"]) != 0:
                filters["birth_month_day"] = recieved_data["birth_month_day"]

        if "death_month_day" in recieved_data:
            if len(recieved_data["death_month_day"]) != 0:
                filters["death_month_day"] = recieved_data["death_month_day"]
                display_only_death_localisation = True
                display_death_localisation = True
        
        display_people_with_no_localisation = False
        if "display_people_with_no_localisation" in recieved_data:
            if recieved_data["display_people_with_no_localisation"] == "oui":
                display_people_with_no_localisation = True
                

        display_only_death_localisation = False

        if "is_cause_of_death_known" in recieved_data:
            filters["is_cause_of_death_known"] = True
            display_death_localisation = True
        
        if "display_only_death_localisation" in recieved_data:
            if recieved_data["display_only_death_localisation"] == "oui":
                display_only_death_localisation = True
                #recieved_data["alive_status"] = "Mort"
                filters["is_alive"] = False
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

        sort_user_by = "None"
        if "sort_user_by" in recieved_data:
            if recieved_data["sort_user_by"] != "Par défaut":
                if recieved_data["sort_user_by"] == "Nombre de lien":
                    sort_user_by = "number_of_links"
                if recieved_data["sort_user_by"] == "Nombre d'ami(e)":
                    sort_user_by = "number_of_friends"
                if recieved_data["sort_user_by"] == "Nombre de vue(s)":
                    sort_user_by = "number_of_views"        
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
            if "display_people_with_no_localisation" not in recieved_data:
                display_people_with_no_localisation = True
            
                    
        if display_people_with_no_localisation is False:
            filters["birth_town_localisation__icontains"] = " "
        

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
            
            # if "#" in recieved_data["town_birth_or_death_place"]:
            #     accept_multiple_element = True
            #     for town in recieved_data["town_birth_or_death_place"].split("#"):
            #         #query |= Q(town_death_place__icontains=town)
            #         query |= Q(town_birth_place__icontains=unidecode(town)) | Q(town_death_place__icontains=unidecode(town))
            # else:
            
            query |= Q(town_birth_place__icontains=recieved_data["town_birth_or_death_place"]) | Q(town_death_place__icontains=recieved_data["town_birth_or_death_place"])
            


        #print(display_death_localisation,display_either_birth_or_death_town,accept_multiple_element)
        filters["position__gte"] = 0
        #filters["age__lte"] = 123
                
        #print(recieved_data)
        #print(filters)
        #print(query , " popopo ")
        
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



        if "display_only_one_person_per_town" in recieved_data:
            if recieved_data["display_only_one_person_per_town"] == "oui":
                if sort_user_by != "None":
                    if sort_user_by == "position":
                        if accept_multiple_element:
                            all_user_obj = WikipediaUserUniqueTown.objects.filter(query,**filters).order_by(f"{sort_user_by}")
                        else:
                            all_user_obj = WikipediaUserUniqueTown.objects.filter(**filters).order_by(f"{sort_user_by}")
                    else:

                        if accept_multiple_element:
                            all_user_obj = WikipediaUserUniqueTown.objects.filter(query,**filters).order_by(f"-{sort_user_by}")
                        else:
                            all_user_obj = WikipediaUserUniqueTown.objects.filter(**filters).order_by(f"-{sort_user_by}")
                else:

                    sort_user_by = "position"
                    if accept_multiple_element:
                        all_user_obj = WikipediaUserUniqueTown.objects.filter(query,**filters).order_by(f"{sort_user_by}")
                    else:
                        all_user_obj = WikipediaUserUniqueTown.objects.filter(**filters).order_by(f"{sort_user_by}")
            
        # if accept_multiple_element:
        #     all_user_obj = WikipediaUser.objects.filter(query,**filters).order_by("-wikipedia_page_lenght")
        # else:
        #     all_user_obj = WikipediaUser.objects.filter(**filters).order_by("-wikipedia_page_lenght")

        length = all_user_obj.count()
        list_of_all_user_data =  []
        nb = NUMBER_OF_USERS_TO_SEARCH * 2

        nb = NUMBER_OF_USERS_TO_SEARCH
        if number_of_people_to_display != 500:
            nb = number_of_people_to_display
        index_start = chunk_nb * nb
        index_end = (chunk_nb + 1) * nb


        #number_of_people_to_display = 0
        list_of_localisation = []
        toto = []
        ##print(nb,display_death_localisation,display_only_death_localisation)
        nb_of_bad_user = 0
        for user_obj in all_user_obj[index_start:index_end]:
            try:
                
                # if (user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined") and display_people_with_no_localisation  is False:
                #     #nb_of_bad_user+=1
                #     continue
                
                # if len(list_of_all_user_data) >= number_of_people_to_display:
                #     break

                # if dms_to_decimal(user_obj.birth_town_localisation,"__qjis__") in list_of_localisation:
                #     continue
                
                
                # list_of_localisation.append(dms_to_decimal(user_obj.birth_town_localisation,"__qjis__"))
                toto.append([dms_to_decimal(user_obj.birth_town_localisation,"__qjis__")[0],dms_to_decimal(user_obj.birth_town_localisation,"__qjis__")[1]])

                # if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
                #     birth_place_emoji = "🏳️"
                # else:
                #     birth_place_emoji = user_obj.country_birth_place_emoji

                birth_place_emoji = user_obj.country_birth_place_emoji
                if len(user_obj.page_name) > 35:
                    page_name_shorter = user_obj.page_name[0:35]+"..."
                else:
                    page_name_shorter = user_obj.page_name

                if len(user_obj.page_name) > 15:
                    page_name_even_shorter_for_mobile = user_obj.page_name[0:15]+"..."
                else:
                    page_name_even_shorter_for_mobile = user_obj.page_name
                
                page_name = user_obj.page_name
                user_info_dict = {
                    "page_name": page_name,
                    "page_name_shorter": page_name_shorter,
                    "page_name_even_shorter_for_mobile":page_name_even_shorter_for_mobile,
                    "page_url": user_obj.page_url,
                    "gender":user_obj.gender,
                    "is_alive":str(user_obj.is_alive),
                    "picture_url": user_obj.picture_url,
                    #"birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),
                    "birth_country_name":user_obj.country_birth_place,                      
                    #"town_death_localisation": dms_to_decimal(user_obj.town_death_localisation),
                    "country_birth_place_emoji":birth_place_emoji,
                    "display_death_localisation":display_death_localisation,
                    "page_nb":chunk_nb,
                    "number_of_element":length
        
                }

                # #print(display_death_localisation)
                if display_either_birth_or_death_town is False:
                
                    if display_only_death_localisation is False:
                        user_info_dict["birth_town_localisation"] = dms_to_decimal(user_obj.birth_town_localisation)  
                    else:
                        user_info_dict["birth_town_localisation"] = dms_to_decimal("blablobla") 
                    if display_death_localisation or display_only_death_localisation:
                        user_info_dict["town_death_localisation"] = dms_to_decimal(user_obj.town_death_localisation)
                                
                else:

                    if recieved_data["town_birth_or_death_place"].lower() in user_obj.town_birth_place.lower():
                        user_info_dict["birth_town_localisation"] = dms_to_decimal(user_obj.birth_town_localisation)
                    else:
                        user_info_dict["birth_town_localisation"] = dms_to_decimal("blablobla")

                    if recieved_data["town_birth_or_death_place"].lower() in user_obj.town_death_place.lower() and user_obj.is_alive is False:
                        user_info_dict["town_death_localisation"] = dms_to_decimal(user_obj.town_death_localisation)
                    else:
                        user_info_dict["town_death_localisation"] = dms_to_decimal("blablobla")                                 

                    # if display_only_death_localisation is False:
                    #     user_info_dict["birth_town_localisation"] = dms_to_decimal(user_obj.birth_town_localisation)  
                    # else:
                    #     user_info_dict["birth_town_localisation"] = dms_to_decimal("blablobla") 
                                
                #if display_death_localisation or display_only_death_localisation:
                #    user_info_dict["town_death_localisation"] = dms_to_decimal(user_obj.town_death_localisation)
                ##print(user_info_dict)
                list_of_all_user_data.append(user_info_dict)
            except:
                pass

        # #print(toto)
        # #print(len(toto))
        # reset_file("bloblo.txt")
        # write_into_file("bloblo.txt",str(toto))
        if len(list_of_all_user_data) == 0:
            user_info_dict = {
                "page_name": "Personne",
                "page_name_shorter": "Aucun résultat trouver",
                "page_url": "https://fr.wikipedia.org/wiki/Personne",
                "gender":"Unknown",
                "is_alive":True,
                "picture_url": "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790973930/1955-futurama-bender_pxvpaj.jpg",
                #"birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),
                "birth_town_localisation": dms_to_decimal("blabla"),              
                "country_birth_place_emoji":"🏴‍☠️",
                "page_nb":1,
                "number_of_element":1

            }
            
            list_of_all_user_data.append(user_info_dict)
        cache.set(cache_key, list_of_all_user_data, STATS_CACHE_TTL)
        return JsonResponse({"all_user_data":list_of_all_user_data}, status=200)
    except:
        traceback.print_exc()