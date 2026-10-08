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

import time
import traceback

# STATS_CACHE_TTL = 60 * 60 * 24 * 7  # 7 jours

# def stats_cache_key(data: dict) -> str:
#     normalized = json.dumps(data, sort_keys=True, ensure_ascii=False)
#     return "adv_stats:" + hashlib.md5(normalized.encode()).hexdigest()

@csrf_exempt
@ratelimit(key='ip', rate='15/15m',block=False)
def get_advanced_statistics(request):
    """Get advanced statistics"""
    
    #start = time.perf_counter()
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

    try:
        recieved_data = json.loads(request.body)
    except:
        recieved_data = {}
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

    cache_key = stats_cache_key("adv_stats",recieved_data)
    cached = cache.get(cache_key)
    if isinstance(cached, dict):
        return JsonResponse(cached, status=200)
    
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

            ##print(searched_region)
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
    
    ##print(recieved_data)
    if "town_birth_place" in recieved_data:
        if "#" in recieved_data["town_birth_place"]:
            accept_multiple_element = True
            for town in recieved_data["town_birth_place"].split("#"):
                query |= Q(town_birth_place__icontains=town)
        else:
            filters["town_birth_place__icontains"] = unidecode(recieved_data["town_birth_place"])

    if "town_death_place" in recieved_data:
        if "#" in recieved_data["town_death_place"]:
            accept_multiple_element = True
            for town in recieved_data["town_death_place"].split("#"):
                query |= Q(town_death_place__icontains=town)
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
        

    if "display_only_death_localisation" in recieved_data:
        if recieved_data["display_only_death_localisation"] == "oui":
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
            if recieved_data["sort_user_by"] == "Nombre de langues dans lesquelles la page est traduite":
                sort_user_by = "nb_of_translation"   
            #sort_user_by = recieved_data["sort_user_by"]
    #filters["town_death_localisation__icontains"] = "Undefined"
    
    if "century_of_birth" in recieved_data:
        filters["century_of_birth"] = int(recieved_data["century_of_birth"])

    if "century_of_death" in recieved_data:
        filters["century_of_death"] = int(recieved_data["century_of_death"])
    
    if "born_before_christ" in recieved_data:
        if recieved_data["born_before_christ"] == "oui":
            filters["born_before_christ"] = True
        if recieved_data["born_before_christ"] == "non":
            filters["born_before_christ"] = False

    if "town_birth_or_death_place" in recieved_data:
        accept_multiple_element = True
        query |= Q(town_birth_place__icontains=recieved_data["town_birth_or_death_place"]) | Q(town_death_place__icontains=recieved_data["town_birth_or_death_place"])
        display_death_localisation = True

    
    filters["position__gte"] = 0
    #filters["position__lte"] = 101

    #filters["age__lte"] = 123
    #filters["town_birth_place"] = "Paris"
            
    ###print(recieved_data)
    ##print(filters)


    
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





    set_of_first_name = set()
    display_only_one_person_per_first_name = False
    if "display_only_one_person_per_first_name" in recieved_data:
        if recieved_data["display_only_one_person_per_first_name"] == "oui":
            display_only_one_person_per_first_name = True

    set_of_last_name = set()
    display_only_one_person_per_last_name = False
    if "display_only_one_person_per_last_name" in recieved_data:
        if recieved_data["display_only_one_person_per_last_name"] == "oui":
            display_only_one_person_per_last_name = True



    set_of_job = set()
    display_only_one_person_per_job = False
    if "display_only_one_person_per_job" in recieved_data:
        if recieved_data["display_only_one_person_per_job"] == "oui":
            display_only_one_person_per_job = True
    
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
                ##print("att")

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
    nb_of_bad_user = 0
    first_name_counter = Counter()
    first_name_standard_counter = Counter()

    last_name_counter = Counter()
    last_name_standard_counter = Counter()

    job_counter = Counter()

    town_birth_place_counter = Counter()
    country_birth_place_counter = Counter()
    time_period_of_birth_counter = Counter()
    continent_of_birth_counter = Counter()
    region_of_birth_counter = Counter()

    birth_date_counter = Counter()
    birth_year_counter = Counter()
    birth_year_counter_from_1900 = Counter()
        
    birth_month_counter = Counter()
    birth_day_counter = Counter()
    birth_month_day_counter = Counter()

    death_town_counter = Counter()
    country_death_place_counter = Counter()
    continent_of_death_counter = Counter()
    region_of_death_counter = Counter()

    death_date_counter = Counter()
    death_year_counter = Counter()
    death_year_counter_from_1900 = Counter()
        
    death_month_counter = Counter()
    death_day_counter = Counter()
    death_month_day_counter = Counter()

    born_and_died_in_the_same_town_counter = Counter()
    born_and_died_in_the_same_country_counter = Counter()
    born_and_died_in_the_same_continent_counter = Counter()
    born_and_died_in_the_same_day_counter = Counter()
    born_and_died_in_the_same_region_counter = Counter()

    born_before_christ_counter = Counter()
    died_before_christ_counter = Counter()
    born_and_died_before_christ_counter = Counter()
    born_and_died_after_christ_counter = Counter()
    born_before_christ_and_died_after_christ_counter = Counter()

    week_day_of_birth_counter = Counter()
    week_day_of_death_counter = Counter()

    age_counter = Counter()
    is_alive_counter = Counter()
    gender_counter = Counter()

    first_char_of_the_page_counter = Counter()
    wikipedia_page_lenght_counter = Counter()
    number_of_links_counter = Counter()
    number_of_user_who_have_linked_this_user_counter = Counter()
    number_of_friends_counter = Counter()
    preciseness_level_counter = Counter()

    page_lenght_counter = Counter()
    number_of_word_in_page_name_counter = Counter()

    town_birth_and_death_place_counter = Counter()

    country_birth_and_death_place_counter = Counter()

    continent_of_birth_and_death_counter = Counter()

    region_of_birth_and_death_counter = Counter()


    birth_and_death_date_counter = Counter()

    birth_and_death_year_counter = Counter()
    birth_and_death_year_counter_from_1900 = Counter()
        

    birth_and_death_month_counter = Counter()

    birth_and_death_day_counter = Counter()

    birth_and_death_month_day_counter = Counter()

    week_day_of_birth_and_death_counter = Counter()

    #town_with_no_locolisation_counter = Counter()
    cause_of_death_counter = Counter()
    cause_of_death_known_counter = Counter()

    grade_over_20_counter = Counter()

    no_town_counter = Counter()
    no_country_counter = Counter()
    dict_of_error_counter = Counter()
    number_of_error_per_page_counter = Counter()
    age_group_counter = Counter()
    number_of_view_counter = Counter()

    century_of_birth_counter = Counter()
    century_of_death_counter = Counter()
    page_name_counter = Counter()

    dict_of_counter = {}

    length = all_user_obj.count()
    nb_of_bad_user = 0
    ##print("start get_advanced_statistics function")
    try:
        for user_obj in all_user_obj:

            if display_only_one_person_per_first_name and user_obj.first_name_standard not in set_of_first_name:
                set_of_first_name.add(user_obj.first_name_standard)
            elif display_only_one_person_per_first_name:
                nb_of_bad_user+=1
                continue

            if display_only_one_person_per_last_name and user_obj.last_name_standard not in set_of_last_name:
                set_of_last_name.add(user_obj.last_name_standard)
            elif display_only_one_person_per_last_name:
                nb_of_bad_user+=1
                continue

            if display_only_one_person_per_job and user_obj.job not in set_of_job:
                set_of_job.add(user_obj.job)
            elif display_only_one_person_per_job:
                nb_of_bad_user+=1
                continue
            
            # ─────────────────────────────────────────────
            # Names
            # ─────────────────────────────────────────────

            if user_obj.first_name and user_obj.first_name.lower().strip() != "undefined":
                first_name_counter[user_obj.first_name] += 1

            if user_obj.first_name_standard and user_obj.first_name_standard.lower().strip() != "undefined":
                first_name_standard_counter[user_obj.first_name_standard] += 1

            if user_obj.last_name and user_obj.last_name.lower().strip() != "undefined":
                last_name_counter[user_obj.last_name] += 1

            if user_obj.last_name_standard and user_obj.last_name_standard.lower().strip() != "undefined":
                last_name_standard_counter[user_obj.last_name_standard] += 1

            if user_obj.century_of_birth != -999 and user_obj.age <= MAXIMUM_AGE_TO_DISPLAY and int(user_obj.century_of_birth) <= 21:
                century_of_birth_counter[int(user_obj.century_of_birth)] += 1
            
            if user_obj.century_of_death != -999 and user_obj.age <= MAXIMUM_AGE_TO_DISPLAY and int(user_obj.century_of_death) <= 21:
                century_of_death_counter[int(user_obj.century_of_death)] += 1
            
            # ─────────────────────────────────────────────
            # Job
            # ─────────────────────────────────────────────

            if user_obj.job and user_obj.job.lower().strip() != "undefined":
                job_counter[user_obj.job] += 1


            # ─────────────────────────────────────────────
            # Birth
            # ─────────────────────────────────────────────

            if user_obj.town_birth_place and len(user_obj.town_birth_place) > 0 and user_obj.town_birth_place.lower() != "undefined":
                town_birth_place_counter[user_obj.town_birth_place] += 1

            if user_obj.country_birth_place and len(user_obj.country_birth_place) > 0 and user_obj.country_birth_place.lower() != "undefined":
                country_birth_place_counter[user_obj.country_birth_place] += 1

            if user_obj.time_period_of_birth and len(user_obj.time_period_of_birth) > 0 and user_obj.time_period_of_birth.lower() != "undefined":
                time_period_of_birth_counter[HISTORICAL_PERIODS_DICT_TO_FRENCH_WITH_DATE[user_obj.time_period_of_birth]] += 1

            if user_obj.continent_of_birth and len(user_obj.continent_of_birth) > 0 and user_obj.continent_of_birth.lower() != "undefined":
                continent_of_birth_counter[user_obj.continent_of_birth] += 1

            if user_obj.region_of_birth and len(user_obj.region_of_birth) > 0 and user_obj.region_of_birth.lower() != "undefined":
                region_of_birth_counter[user_obj.region_of_birth] += 1

            if user_obj.birth_date and len(user_obj.birth_date) > 0 and user_obj.birth_date.lower() != "undefined":
                birth_date_counter[user_obj.birth_date] += 1

            if user_obj.birth_year is not None and len(str(user_obj.birth_year)) > 0 and str(user_obj.birth_year) != "123456789" and user_obj.birth_year < CURRENT_YEAR + 1:
                birth_year_counter[user_obj.birth_year] += 1

            try:
                if user_obj.birth_year is not None and len(str(user_obj.birth_year)) > 0 and str(user_obj.birth_year) != "123456789" and user_obj.birth_year >= 1900 and user_obj.birth_year < CURRENT_YEAR + 1:
                    birth_year_counter_from_1900[user_obj.birth_year] += 1
            except:
                pass            
            if user_obj.birth_month and len(user_obj.birth_month) > 0 and user_obj.birth_month.lower() != "undefined":
                birth_month_counter[user_obj.birth_month] += 1

            if user_obj.birth_day and len(user_obj.birth_day) > 0 and user_obj.birth_day.lower() != "undefined":
                birth_day_counter[user_obj.birth_day] += 1

            if user_obj.birth_month_day and len(user_obj.birth_month_day) > 0 and user_obj.birth_month_day.lower() != "undefined":
                birth_month_day_counter[user_obj.birth_month_day] += 1


            if user_obj.town_birth_place == "" or user_obj.town_birth_place.lower() == "undefined":
                no_town_counter[False] += 1
            else:
                no_town_counter[True] += 1


            if user_obj.country_birth_place == "" or user_obj.country_birth_place.lower() == "undefined":
                no_country_counter[False] += 1
            else:
                no_country_counter[True] += 1
                    
            grade_over_20_counter[int(user_obj.grade_over_20)]+=1
            # ─────────────────────────────────────────────
            # Death
            # ─────────────────────────────────────────────

            if user_obj.is_alive is False:
                if (
                    user_obj.town_death_place
                    and user_obj.town_death_place.lower().strip() not in ["undefined", "alive"]
                ):
                    death_town_counter[user_obj.town_death_place] += 1

                if (
                    user_obj.country_death_place
                    and user_obj.country_death_place.lower().strip() != "undefined"
                ):
                    country_death_place_counter[user_obj.country_death_place] += 1

                if (
                    user_obj.continent_of_death
                    and user_obj.continent_of_death.lower().strip() != "undefined"
                ):
                    continent_of_death_counter[user_obj.continent_of_death] += 1

                if (
                    user_obj.region_of_death
                    and user_obj.region_of_death.lower().strip() != "undefined"
                ):
                    region_of_death_counter[user_obj.region_of_death] += 1

                if user_obj.death_date and user_obj.death_date.lower().strip() != "undefined":
                    death_date_counter[user_obj.death_date] += 1

                if user_obj.death_year and user_obj.death_year.lower().strip() != "undefined" and str(user_obj.death_year) != "123456789" and int(user_obj.death_year) < CURRENT_YEAR + 1:
                    try:
                        death_year_counter[int(user_obj.death_year)] += 1
                    except:
                        pass

                if user_obj.death_year and user_obj.death_year.lower().strip() != "undefined" and str(user_obj.death_year) != "123456789" and int(user_obj.death_year) >= 1900 and int(user_obj.death_year) < CURRENT_YEAR + 1:
                    try:
                        death_year_counter_from_1900[int(user_obj.death_year)] += 1
                    except:
                        pass
                
                if user_obj.death_month and user_obj.death_month.lower().strip() != "undefined":
                    death_month_counter[user_obj.death_month] += 1

                if user_obj.death_day and user_obj.death_day.lower().strip() != "undefined":
                    death_day_counter[user_obj.death_day] += 1

                if user_obj.death_month_day and user_obj.death_month_day.lower().strip() != "undefined":
                    death_month_day_counter[user_obj.death_month_day] += 1


            # ─────────────────────────────────────────────
            # Birth / Death comparisons
            # ─────────────────────────────────────────────
            #if user_obj.is_alive is False:

            if user_obj.born_and_died_in_the_same_town != "alive":
                born_and_died_in_the_same_town_counter[
                    user_obj.born_and_died_in_the_same_town
                ] += 1


            if user_obj.born_and_died_in_the_same_country != "alive":                
                born_and_died_in_the_same_country_counter[
                    user_obj.born_and_died_in_the_same_country
                ] += 1


            if user_obj.born_and_died_in_the_same_continent != "alive":                
                born_and_died_in_the_same_continent_counter[
                    user_obj.born_and_died_in_the_same_continent
                ] += 1

            if user_obj.born_and_died_in_the_same_day!= "alive":                
                born_and_died_in_the_same_day_counter[
                    user_obj.born_and_died_in_the_same_day
                ] += 1

            if user_obj.born_and_died_in_the_same_region != "alive":                
                born_and_died_in_the_same_region_counter[
                    user_obj.born_and_died_in_the_same_region
                ] += 1
            
            born_before_christ_counter[
                user_obj.born_before_christ
            ] += 1

            died_before_christ_counter[
                user_obj.died_before_christ
            ] += 1

            born_and_died_before_christ_counter[
                user_obj.born_and_died_before_christ
            ] += 1

            born_and_died_after_christ_counter[
                user_obj.born_and_died_after_christ
            ] += 1

            born_before_christ_and_died_after_christ_counter[
                user_obj.born_before_christ_and_died_after_christ
            ] += 1


            if user_obj.is_cause_of_death_known:
                cause_of_death_counter[user_obj.cause_of_death.lower()] +=1

            if user_obj.is_cause_of_death_known or user_obj.cause_of_death == "Unspecified":
                cause_of_death_known_counter[user_obj.is_cause_of_death_known] +=1
            
            # ─────────────────────────────────────────────
            # Days
            # ─────────────────────────────────────────────

            if user_obj.week_day_of_birth and user_obj.week_day_of_birth.lower().strip() != "undefined":
                week_day_of_birth_counter[user_obj.week_day_of_birth] += 1

            if user_obj.week_day_of_death and user_obj.week_day_of_death.lower().strip() != "undefined" and user_obj.is_alive is False:
                week_day_of_death_counter[user_obj.week_day_of_death] += 1


            # ─────────────────────────────────────────────
            # Personal information
            # ─────────────────────────────────────────────

            if user_obj.age is not None and 1 <= user_obj.age <= MAXIMUM_AGE_TO_DISPLAY:
                age_counter[user_obj.age] += 1

            is_alive_counter[user_obj.is_alive] += 1

            if user_obj.gender and user_obj.gender.lower().strip() != "undefined" and user_obj.gender.lower().strip() != "unclear":
                gender_counter[GENDER_TO_FRENCH_DICT[user_obj.gender]] += 1


            # ─────────────────────────────────────────────
            # Ranking
            # ─────────────────────────────────────────────

            
            # ─────────────────────────────────────────────
            # Wikipedia page analysis
            # ─────────────────────────────────────────────

            if user_obj.first_char_of_the_page:
                first_char_of_the_page_counter[
                    user_obj.first_char_of_the_page
                ] += 1

            if user_obj.wikipedia_page_lenght is not None:

                # if len(str(user_obj.wikipedia_page_lenght)) >= 3:
                #     nb_of_zero_to_remove = len(str(user_obj.wikipedia_page_lenght)) - 2
                #     rounded_number = int(user_obj.wikipedia_page_lenght/10**nb_of_zero_to_remove) * 10**nb_of_zero_to_remove

                # else:   
                #     nb_of_zero_to_remove = len(str(user_obj.wikipedia_page_lenght)) - 1
                #     rounded_number = int(user_obj.wikipedia_page_lenght/10**nb_of_zero_to_remove) * 10**nb_of_zero_to_remove
                nb_of_zero_to_remove = len(str(user_obj.wikipedia_page_lenght)) - 1
                rounded_number = int(user_obj.wikipedia_page_lenght/10**nb_of_zero_to_remove) * 10**nb_of_zero_to_remove


                wikipedia_page_lenght_counter[
                    rounded_number
                    #int(user_obj.wikipedia_page_lenght/10 ** len(str(user_obj.wikipedia_page_lenght)) - 2)
                ] += 1

            if user_obj.number_of_links is not None:
                number_of_links_counter[
                    user_obj.number_of_links
                ] += 1

            if user_obj.number_of_user_who_have_linked_this_user is not None:
                number_of_user_who_have_linked_this_user_counter[
                    user_obj.number_of_user_who_have_linked_this_user
                ] += 1

            if user_obj.number_of_friends is not None:
                number_of_friends_counter[
                    user_obj.number_of_friends
                ] += 1



            nb_of_zero_to_remove = len(str(user_obj.preciseness_level)) - 1
            rounded_number = int(user_obj.preciseness_level/10**nb_of_zero_to_remove) * 10**nb_of_zero_to_remove
            if len(str(str(user_obj.preciseness_level))) == 1:
                if user_obj.preciseness_level <= 5:
                    rounded_number = 0
                else:
                    rounded_number = 10
                
            if user_obj.preciseness_level is not None:
                preciseness_level_counter[
                    rounded_number
                ] += 1


            # ─────────────────────────────────────────────
            # Country emojis
            # ─────────────────────────────────────────────

            
            # ─────────────────────────────────────────────
            # Metadata
            # ─────────────────────────────────────────────

            
            if user_obj.page_lenght is not None:
                page_lenght_counter[
                    user_obj.page_lenght
                ] += 1

            if user_obj.number_of_word_in_page_name is not None:
                number_of_word_in_page_name_counter[
                    user_obj.number_of_word_in_page_name
                ] += 1

            # Ville

            if user_obj.town_birth_place.lower().strip() != "undefined" and len(user_obj.town_birth_place) != 0:
                town_birth_and_death_place_counter[user_obj.town_birth_place] += 1
            
            if user_obj.town_death_place.lower().strip() != "undefined" and user_obj.town_death_place.lower().strip() != "alive" and len(user_obj.town_death_place) != 0:
                town_birth_and_death_place_counter[user_obj.town_death_place] += 1
            

            # if (user_obj.town_birth_place.lower().strip() != "undefined" and len(user_obj.town_birth_place.lower().strip()) != 0) and (user_obj.birth_town_localisation.lower().strip() == "undefined" or user_obj.birth_town_localisation.lower().strip() == ""):
            #     town_with_no_locolisation_counter[user_obj.town_birth_place] += 1
            # if (user_obj.town_death_place.lower().strip() != "undefined" and user_obj.town_death_place.lower().strip() != "alive" and len(user_obj.town_death_place.lower().strip()) != 0) and (user_obj.town_death_localisation.lower().strip() == "undefined" or user_obj.town_death_localisation.lower().strip() == ""):
            #     town_with_no_locolisation_counter[user_obj.town_death_place] += 1
            
            # Pays

            if user_obj.country_birth_place.lower().strip() != "undefined" and len(user_obj.country_birth_place.lower()) != 0 and user_obj.country_birth_place.lower() != " ":
                country_birth_and_death_place_counter[user_obj.country_birth_place] += 1

            if user_obj.country_death_place.lower().strip() != "undefined" and user_obj.country_death_place.lower().strip() != "alive" and len(user_obj.country_death_place.lower()) != 0 and user_obj.country_death_place.lower() != " ":
                country_birth_and_death_place_counter[user_obj.country_death_place] += 1

            # Continents
            
            if user_obj.continent_of_birth.lower().strip() != "undefined":
                continent_of_birth_and_death_counter[user_obj.continent_of_birth] += 1

            if user_obj.continent_of_death.lower().strip() != "undefined" and user_obj.continent_of_death.lower().strip() != "alive":
                continent_of_birth_and_death_counter[user_obj.continent_of_death] += 1

            # Régions

            if user_obj.region_of_birth.lower().strip() != "undefined":    
                region_of_birth_and_death_counter[user_obj.region_of_birth] += 1

            if user_obj.region_of_death.lower().strip() != "undefined" and user_obj.region_of_death.lower().strip() != "alive":
                region_of_birth_and_death_counter[user_obj.region_of_death] += 1

            # Dates

            if user_obj.birth_date.lower().strip() != "undefined" and user_obj.birth_date != "alive":
                birth_and_death_date_counter[user_obj.birth_date] += 1
            
            if user_obj.birth_date and user_obj.birth_date.lower().strip() != "undefined":
                birth_and_death_date_counter[user_obj.birth_date] += 1

            if user_obj.death_date and user_obj.death_date.lower().strip() != "undefined" and user_obj.death_date.lower().strip() != "alive":
                birth_and_death_date_counter[user_obj.death_date] += 1


            # Années
            if user_obj.birth_year and str(user_obj.birth_year).lower().strip() != "undefined" and str(user_obj.birth_year) != "123456789" and user_obj.birth_year < CURRENT_YEAR + 1:
                birth_and_death_year_counter[user_obj.birth_year] += 1

            if user_obj.death_year and str(user_obj.death_year).lower().strip() != "undefined" and str(user_obj.death_year).lower().strip() != "alive" and str(user_obj.death_year) != "123456789" and int(user_obj.death_year) < CURRENT_YEAR + 1:
                try:
                    birth_and_death_year_counter[int(user_obj.death_year)] += 1
                except:
                    pass
            

            if user_obj.birth_year and str(user_obj.birth_year).lower().strip() != "undefined" and str(user_obj.birth_year) != "123456789"and user_obj.birth_year >= 1900 and user_obj.birth_year < CURRENT_YEAR + 1:
                birth_and_death_year_counter_from_1900[user_obj.birth_year] += 1

            if user_obj.death_year and str(user_obj.death_year).lower().strip() != "undefined" and str(user_obj.death_year).lower().strip() != "alive" and str(user_obj.death_year) != "123456789" and int(user_obj.death_year) >= 1900 and int(user_obj.death_year) < CURRENT_YEAR + 1:
                try:
                    birth_and_death_year_counter_from_1900[int(user_obj.death_year)] += 1
                except:
                    pass
            
            # Mois
            if user_obj.birth_month and str(user_obj.birth_month).lower().strip() != "undefined":
                birth_and_death_month_counter[user_obj.birth_month] += 1

            if user_obj.death_month and str(user_obj.death_month).lower().strip() != "undefined" and str(user_obj.death_month).lower().strip() != "alive":
                birth_and_death_month_counter[user_obj.death_month] += 1


            # Jours
            if user_obj.birth_day and str(user_obj.birth_day).lower().strip() != "undefined":
                birth_and_death_day_counter[user_obj.birth_day] += 1

            if user_obj.death_day and str(user_obj.death_day).lower().strip() != "undefined" and str(user_obj.death_day).lower().strip() != "alive":
                birth_and_death_day_counter[user_obj.death_day] += 1


            # Mois + jour
            if user_obj.birth_month_day and str(user_obj.birth_month_day).lower().strip() != "undefined":
                birth_and_death_month_day_counter[user_obj.birth_month_day] += 1

            if user_obj.death_month_day and str(user_obj.death_month_day).lower().strip() != "undefined" and str(user_obj.death_month_day).lower().strip() != "alive":
                birth_and_death_month_day_counter[user_obj.death_month_day] += 1


            # Jour de la semaine
            if user_obj.week_day_of_birth and str(user_obj.week_day_of_birth).lower().strip() != "undefined":
                week_day_of_birth_and_death_counter[user_obj.week_day_of_birth] += 1

            if user_obj.week_day_of_death and str(user_obj.week_day_of_death).lower().strip() != "undefined" and str(user_obj.week_day_of_death).lower().strip() != "alive":
                week_day_of_birth_and_death_counter[user_obj.week_day_of_death] += 1

            if "-" not in str(user_obj.age) and user_obj.age > 0 and user_obj.age != 123456789:
                try:
                    if len(str(user_obj.age)) == 1:
                        age_group_counter[int(user_obj.age)] += 1        
                    else:
                        if int(str(user_obj.age)[:-1]) <= 12:
                            age_group_counter[int(str(user_obj.age)[:-1])] += 1
                except:
                    pass
            if len(user_obj.list_of_unpreciseness_data) != 0:
                for error in user_obj.list_of_unpreciseness_data:
                    dict_of_error_counter[UNPRECISENESS_DATA_FR[error]]+=1
                    # try:
                    #     dict_of_error_counter[UNPRECISENESS_DATA_FR[error]]+=1
                    # except:
                    #     dict_of_error_counter[error]+=1

            number_of_error_per_page_counter[len(user_obj.list_of_unpreciseness_data)] +=1

            number_of_view_counter[user_obj.number_of_views] += 1                     

        dict_of_counter = {
            "first_name": first_name_counter,
            "first_name_standard": first_name_standard_counter,

            "last_name": last_name_counter,
            "last_name_standard": last_name_standard_counter,
            
            "gender": gender_counter,
            "age": age_counter,
            "age_group": age_group_counter,
            "is_alive": is_alive_counter,
            "cause_of_death_known_counter":cause_of_death_known_counter,
            "cause_of_death":cause_of_death_counter,
            "time_period_of_birth": time_period_of_birth_counter,
            "job": job_counter,
            
            "town_birth_place": town_birth_place_counter,
            "town_death_place": death_town_counter,
            "town_birth_and_death_place": town_birth_and_death_place_counter,
            #"town_with_no_locolisation_counter":town_with_no_locolisation_counter,
                    
            "country_birth_place": country_birth_place_counter,
            "country_death_place": country_death_place_counter,
            "country_birth_and_death_place": country_birth_and_death_place_counter,

            "continent_of_birth": continent_of_birth_counter,
            "continent_of_death": continent_of_death_counter,
            "continent_of_birth_and_death": continent_of_birth_and_death_counter,
            
            "region_of_birth": region_of_birth_counter,
            "region_of_death": region_of_death_counter,
            "region_of_birth_and_death": region_of_birth_and_death_counter,
            
            "birth_date": birth_date_counter,
            "death_date": death_date_counter,
            "birth_and_death_date": birth_and_death_date_counter,

            "century_of_birth": century_of_birth_counter,
            "century_of_death": century_of_death_counter,
                    
            "birth_year": birth_year_counter,
            "death_year": death_year_counter,
            "birth_year_from_1900": birth_year_counter_from_1900,
            "death_year_from_1900": death_year_counter_from_1900,
                    
            "birth_and_death_year": birth_and_death_year_counter,
            "birth_and_death_year_from_1900": birth_and_death_year_counter_from_1900,    

            "birth_month": birth_month_counter,
            "death_month": death_month_counter,
            "birth_and_death_month": birth_and_death_month_counter,

            "birth_day": birth_day_counter,
            "death_day": death_day_counter,
            "birth_and_death_day": birth_and_death_day_counter,

            "birth_month_day": birth_month_day_counter,
            "death_month_day": death_month_day_counter,
            "birth_and_death_month_day": birth_and_death_month_day_counter,

            "week_day_of_birth": week_day_of_birth_counter,
            "week_day_of_death": week_day_of_death_counter,
            "week_day_of_birth_and_death": week_day_of_birth_and_death_counter,

            "born_and_died_in_the_same_town":
                born_and_died_in_the_same_town_counter,

            "born_and_died_in_the_same_country":
                born_and_died_in_the_same_country_counter,

            "born_and_died_in_the_same_continent":
                born_and_died_in_the_same_continent_counter,

            "born_and_died_in_the_same_day":
                born_and_died_in_the_same_day_counter,

            "born_and_died_in_the_same_region":
                born_and_died_in_the_same_region_counter,

            "born_before_christ":
                born_before_christ_counter,

            "died_before_christ":
                died_before_christ_counter,

            "born_and_died_before_christ":
                born_and_died_before_christ_counter,

            "born_and_died_after_christ":
                born_and_died_after_christ_counter,

            "born_before_christ_and_died_after_christ":
                born_before_christ_and_died_after_christ_counter,
            
            "first_char_of_the_page":
                first_char_of_the_page_counter,

            "grade_over_20":grade_over_20_counter,
            "wikipedia_page_lenght":wikipedia_page_lenght_counter,
            "page_lenght":
                page_lenght_counter,

            "number_of_word_in_page_name":
                number_of_word_in_page_name_counter,

            "number_of_links":
                number_of_links_counter,

            "number_of_user_who_have_linked_this_user":
                number_of_user_who_have_linked_this_user_counter,
            "number_of_view":number_of_view_counter,
            "number_of_friends":
                number_of_friends_counter,
            "preciseness_level":preciseness_level_counter,
            

            
            "no_country_counter":no_country_counter,
            "no_town_counter":no_town_counter,
            "dict_of_error":dict_of_error_counter,
            "number_of_error_per_page":number_of_error_per_page_counter,
            
            }



        dict_of_counter["birth_year"] = sort_a_counter(birth_year_counter,1)
        dict_of_counter["death_year"] = sort_a_counter(death_year_counter,1)
        dict_of_counter["birth_and_death_year"] = sort_a_counter(birth_and_death_year_counter,1)

        dict_of_counter["birth_year_from_1900"] = sort_a_counter(birth_year_counter_from_1900,1)
        dict_of_counter["death_year_from_1900"] = sort_a_counter(death_year_counter_from_1900,1)
        dict_of_counter["birth_and_death_year_from_1900"] = sort_a_counter(birth_and_death_year_counter_from_1900,1)
        
        #print("end get_advanced_statistics function")
        
        dict_of_counter["number_of_error_per_page"] = sort_a_counter(number_of_error_per_page_counter,1)
        dict_of_counter["preciseness_level"] = sort_a_counter(preciseness_level_counter,1)
        dict_of_counter["age"] = sort_a_counter(age_counter,1)
        dict_of_counter["grade_over_20"] = sort_a_counter(grade_over_20_counter,1)
        dict_of_counter["wikipedia_page_lenght"] = sort_a_counter(wikipedia_page_lenght_counter,1)
        dict_of_counter["number_of_user_found"] = length - nb_of_bad_user
        dict_of_counter["age_group"] = sort_a_counter(age_group_counter,1)
        dict_of_counter["number_of_view"] = sort_a_counter(number_of_view_counter,1)

        dict_of_counter["century_of_birth"] = sort_a_counter(century_of_birth_counter,1)
        dict_of_counter["century_of_death"] = sort_a_counter(century_of_death_counter,1)
        
        # block_of_element = ["first_name","gender","town_birth_place","country_birth_place","continent_of_birth","region_of_birth","birth_date","born_and_died_in_the_same_town","born_before_christ","first_char_of_the_page","no_country_counter"]
        # block_of_element_present = []
        # for element in block_of_element:
        #     if len(dict_of_counter[element]):
        #         block_of_element_present.append(element)
        #     ##print(len(dict_of_counter[element]) , element)

        dict_of_counter = {
            key: sort_a_counter(counter,0,key)
            for key, counter in dict_of_counter.items()
        }

        ##print(f"Request processing time: {elapsed:.3f} seconds")
        result = {"all_wikipedia_info": dict_of_counter}
        cache.set(cache_key, result, STATS_CACHE_TTL)
        return JsonResponse(result, status=200)
        
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({"error": type(e).__name__, "detail": str(e)}, status=500)