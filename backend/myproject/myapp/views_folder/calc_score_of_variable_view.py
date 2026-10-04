from collections import Counter
from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django_ratelimit.decorators import ratelimit

from myapp.models import WikipediaUser

from random import randint
from random import sample

from ..global_variable import *
from ..utility_function  import *

import os
import traceback

# pylint : disable=C0200
# pylint: disable=consider-using-enumerate


def calc_score_of_all_variable(request):
    """Compute the score of almost all varible"""
    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)


    print("ko")
    name_dict_grade = {}
    name_dict_occurence = {}

    town_dict_grade = {}
    town_dict_occurence = {}


    town_birth_dict_grade = {}
    town_birth_dict_occurence = {}


    town_death_dict_grade = {}
    town_death_dict_occurence = {}
    
    job_dict_grade = {}
    job_dict_occurence = {}

    country_dict_grade = {}
    country_dict_occurence = {}

    birthday_dict_grade = {}
    birthday_dict_occurence = {}

    town_dict_french_grade = {}
    town_dict_french_occurence = {}

    last_name_dict_grade = {}
    last_name_dict_occurence = {}

    age_dict_grade = {}
    age_dict_occurence = {}

    birth_year_dict_grade = {}
    birth_year_dict_occurence = {}

    region_of_birth_dict_grade = {}
    region_of_birth_dict_occurence = {}

    page_lenght_dict_grade = {}
    page_lenght_dict_occurence = {}

    first_char_of_the_page_dict_grade = {}
    first_char_of_the_page_dict_occurence = {}


    boy_name_dict_grade = {}
    boy_name_dict_occurence = {}

    girl_name_dict_grade = {}
    girl_name_dict_occurence = {}

    french_boy_name_dict_grade = {}
    french_boy_name_dict_occurence = {}
    
    french_girl_name_dict_occurence = {}
    french_girl_name_dict_grade = {}

    french_last_name_dict_grade = {}
    french_last_name_dict_occurence = {}

    
    time_period_of_birth_dict_grade = {}
    time_period_of_birth_dict_occurence = {}


    continent_of_birth_dict_grade = {}
    continent_of_birth_dict_occurence = {}

    town_birth_french_dict_grade = {}
    town_birth_french_dict_occurence = {}

    town_death_french_dict_grade = {}
    town_death_french_dict_occurence = {}

    country_birth_dict_grade = {}
    country_birth_dict_occurence = {}

    country_death_dict_grade = {}
    country_death_dict_occurence = {}

    deathday_dict_grade = {}
    deathday_dict_occurence = {}

    birth_and_death_date_dict_grade = {}
    birth_and_death_date_dict_occurence = {}

    region_of_death_dict_grade = {}
    region_of_death_dict_occurence = {}

    birth_and_death_date_dict_grade = {}
    birth_and_death_date_dict_occurence = {}

    region_of_death_dict_grade = {}
    region_of_death_dict_occurence = {}

    region_of_birth_and_death_dict_grade = {}
    region_of_birth_and_death_dict_occurence = {}

    list_of_name  = []
    all_user_obj = WikipediaUser.objects.all().order_by("position").filter(position__gte=0)
    list_of_dict_score = []
    list_of_dict_occurence = []

    error = 0
    #for user_obj in all_user_obj[0:1000]:
    for user_obj in all_user_obj:
                
        try:
            # if user_obj.first_name not in list_of_name:
            #     list_of_name.append(user_obj.first_name)
            
            if user_obj.first_name.lower() != "undefined":
                if user_obj.first_name not in name_dict_grade:
                    name_dict_grade[user_obj.first_name] = 0
                    name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                else:
                    name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                            
                if user_obj.first_name in name_dict_occurence:
                    name_dict_occurence[f"{user_obj.first_name}"] +=1
                else:
                    name_dict_occurence[f"{user_obj.first_name}"] = 0
                    name_dict_occurence[f"{user_obj.first_name}"] +=1



            if user_obj.first_name.lower() != "undefined" and user_obj.gender == "Woman":
                if user_obj.first_name not in girl_name_dict_grade:
                    girl_name_dict_grade[user_obj.first_name] = 0
                    girl_name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                else:
                    girl_name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                            
                if user_obj.first_name in girl_name_dict_occurence:
                    girl_name_dict_occurence[f"{user_obj.first_name}"] +=1
                else:
                    girl_name_dict_occurence[f"{user_obj.first_name}"] = 0
                    girl_name_dict_occurence[f"{user_obj.first_name}"] +=1


            if user_obj.first_name.lower() != "undefined" and user_obj.gender == "Man":
                if user_obj.first_name not in boy_name_dict_grade:
                    boy_name_dict_grade[user_obj.first_name] = 0
                    boy_name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                else:
                    boy_name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                            
                if user_obj.first_name in boy_name_dict_occurence:
                    boy_name_dict_occurence[f"{user_obj.first_name}"] +=1
                else:
                    boy_name_dict_occurence[f"{user_obj.first_name}"] = 0
                    boy_name_dict_occurence[f"{user_obj.first_name}"] +=1
            

            if user_obj.first_name.lower() != "undefined" and user_obj.gender == "Woman" and user_obj.country_birth_place.lower() == "france":
                if user_obj.first_name not in french_girl_name_dict_grade:
                    french_girl_name_dict_grade[user_obj.first_name] = 0
                    french_girl_name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                else:
                    french_girl_name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                            
                if user_obj.first_name in french_girl_name_dict_occurence:
                    french_girl_name_dict_occurence[f"{user_obj.first_name}"] +=1
                else:
                    french_girl_name_dict_occurence[f"{user_obj.first_name}"] = 0
                    french_girl_name_dict_occurence[f"{user_obj.first_name}"] +=1






            if user_obj.last_name.lower() != "undefined" and user_obj.country_birth_place.lower() == "france":
                if user_obj.last_name not in french_last_name_dict_grade:
                    french_last_name_dict_grade[user_obj.last_name] = 0
                    french_last_name_dict_grade[user_obj.last_name] += user_obj.power_ranking
                else:
                    french_last_name_dict_grade[user_obj.last_name] += user_obj.power_ranking
                            
                if user_obj.last_name in french_last_name_dict_occurence:
                    french_last_name_dict_occurence[f"{user_obj.last_name}"] +=1
                else:
                    french_last_name_dict_occurence[f"{user_obj.last_name}"] = 0
                    french_last_name_dict_occurence[f"{user_obj.last_name}"] +=1


            if user_obj.first_name.lower() != "undefined" and user_obj.gender == "Man" and user_obj.country_birth_place.lower() == "france":
                if user_obj.first_name not in french_boy_name_dict_grade:
                    french_boy_name_dict_grade[user_obj.first_name] = 0
                    french_boy_name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                else:
                    french_boy_name_dict_grade[user_obj.first_name] += user_obj.power_ranking
                            
                if user_obj.first_name in french_boy_name_dict_occurence:
                    french_boy_name_dict_occurence[f"{user_obj.first_name}"] +=1
                else:
                    french_boy_name_dict_occurence[f"{user_obj.first_name}"] = 0
                    french_boy_name_dict_occurence[f"{user_obj.first_name}"] +=1
            
            if user_obj.town_birth_place.lower() != "undefined" and user_obj.town_birth_place != "":

                if user_obj.town_birth_place not in town_birth_dict_grade:
                    town_birth_dict_grade[user_obj.town_birth_place] = 0
                    town_birth_dict_grade[user_obj.town_birth_place] += user_obj.power_ranking
                else:
                    town_birth_dict_grade[user_obj.town_birth_place] += user_obj.power_ranking
                            
                if user_obj.town_birth_place in town_birth_dict_occurence:
                    town_birth_dict_occurence[f"{user_obj.town_birth_place}"] +=1
                else:
                    town_birth_dict_occurence[f"{user_obj.town_birth_place}"] = 0
                    town_birth_dict_occurence[f"{user_obj.town_birth_place}"] +=1

                if user_obj.town_birth_place not in town_dict_grade:
                    town_dict_grade[user_obj.town_birth_place] = 0
                    town_dict_grade[user_obj.town_birth_place] += user_obj.power_ranking
                else:
                    town_dict_grade[user_obj.town_birth_place] += user_obj.power_ranking
                            
                if user_obj.town_birth_place in town_dict_occurence:
                    town_dict_occurence[f"{user_obj.town_birth_place}"] +=1
                else:
                    town_dict_occurence[f"{user_obj.town_birth_place}"] = 0
                    town_dict_occurence[f"{user_obj.town_birth_place}"] +=1

            if user_obj.town_death_place.lower() != "undefined" and user_obj.town_death_place != "" and user_obj.town_death_place != "alive":
                if user_obj.town_death_place not in town_death_dict_grade:
                    town_death_dict_grade[user_obj.town_death_place] = 0
                    town_death_dict_grade[user_obj.town_death_place] += user_obj.power_ranking
                else:
                    town_death_dict_grade[user_obj.town_death_place] += user_obj.power_ranking
                            
                if user_obj.town_death_place in town_death_dict_occurence:
                    town_death_dict_occurence[f"{user_obj.town_death_place}"] +=1
                else:
                    town_death_dict_occurence[f"{user_obj.town_death_place}"] = 0
                    town_death_dict_occurence[f"{user_obj.town_death_place}"] +=1

                if user_obj.town_death_place not in town_dict_grade:
                    town_dict_grade[user_obj.town_death_place] = 0
                    town_dict_grade[user_obj.town_death_place] += user_obj.power_ranking
                else:
                    town_dict_grade[user_obj.town_death_place] += user_obj.power_ranking
                            
                if user_obj.town_death_place in town_dict_occurence:
                    town_dict_occurence[f"{user_obj.town_death_place}"] +=1
                else:
                    town_dict_occurence[f"{user_obj.town_death_place}"] = 0
                    town_dict_occurence[f"{user_obj.town_death_place}"] +=1
            

            if user_obj.job.lower() != "undefined" and user_obj.job != "":
                if user_obj.job not in job_dict_grade:
                    job_dict_grade[user_obj.job] = 0
                    job_dict_grade[user_obj.job] += user_obj.power_ranking
                else:
                    job_dict_grade[user_obj.job] += user_obj.power_ranking

                if user_obj.job in job_dict_occurence:
                    job_dict_occurence[f"{user_obj.job}"] += 1
                else:
                    job_dict_occurence[f"{user_obj.job}"] = 0
                    job_dict_occurence[f"{user_obj.job}"] += 1

            if user_obj.country_birth_place.lower() != "undefined" and user_obj.country_birth_place != "":
                if user_obj.country_birth_place not in country_dict_grade:
                    country_dict_grade[user_obj.country_birth_place] = 0
                    country_dict_grade[user_obj.country_birth_place] += user_obj.power_ranking
                else:
                    country_dict_grade[user_obj.country_birth_place] += user_obj.power_ranking

                if user_obj.country_birth_place in country_dict_occurence:
                    country_dict_occurence[f"{user_obj.country_birth_place}"] += 1
                else:
                    country_dict_occurence[f"{user_obj.country_birth_place}"] = 0
                    country_dict_occurence[f"{user_obj.country_birth_place}"] += 1


            if user_obj.country_death_place.lower() != "undefined" and user_obj.country_death_place != "" and user_obj.continent_of_death != "alive":
                if user_obj.country_death_place not in country_dict_grade:
                    country_dict_grade[user_obj.country_death_place] = 0
                    country_dict_grade[user_obj.country_death_place] += user_obj.power_ranking
                else:
                    country_dict_grade[user_obj.country_death_place] += user_obj.power_ranking

                if user_obj.country_death_place in country_dict_occurence:
                    country_dict_occurence[f"{user_obj.country_death_place}"] += 1
                else:
                    country_dict_occurence[f"{user_obj.country_death_place}"] = 0
                    country_dict_occurence[f"{user_obj.country_death_place}"] += 1

            if user_obj.birth_month_day.lower()  != "undefined" and user_obj.birth_month_day  != "" and "fluriel" not in user_obj.birth_month_day.lower():
                if user_obj.birth_month_day not in birthday_dict_grade:
                    birthday_dict_grade[user_obj.birth_month_day] = 0
                    birthday_dict_grade[user_obj.birth_month_day] += user_obj.power_ranking
                else:
                    birthday_dict_grade[user_obj.birth_month_day] += user_obj.power_ranking

                if user_obj.birth_month_day in birthday_dict_occurence:
                    birthday_dict_occurence[f"{user_obj.birth_month_day}"] += 1
                else:
                    birthday_dict_occurence[f"{user_obj.birth_month_day}"] = 0
                    birthday_dict_occurence[f"{user_obj.birth_month_day}"] += 1

                
                if user_obj.birth_month_day not in birth_and_death_date_dict_grade:
                    birth_and_death_date_dict_grade[user_obj.birth_month_day] = 0
                    birth_and_death_date_dict_grade[user_obj.birth_month_day] += user_obj.power_ranking
                else:
                    birth_and_death_date_dict_grade[user_obj.birth_month_day] += user_obj.power_ranking

                if user_obj.birth_month_day in birth_and_death_date_dict_occurence:
                    birth_and_death_date_dict_occurence[user_obj.birth_month_day] += 1
                else:
                    birth_and_death_date_dict_occurence[user_obj.birth_month_day] = 0
                
            if (
                user_obj.country_birth_place.lower() == "france"
                and user_obj.town_birth_place.lower() != "undefined"
                and user_obj.town_birth_place != ""
            ):
                if user_obj.town_birth_place not in town_dict_french_grade:
                    town_dict_french_grade[user_obj.town_birth_place] = 0
                    town_dict_french_grade[user_obj.town_birth_place] += user_obj.power_ranking
                else:
                    town_dict_french_grade[user_obj.town_birth_place] += user_obj.power_ranking

                if user_obj.town_birth_place in town_dict_french_occurence:
                    town_dict_french_occurence[f"{user_obj.town_birth_place}"] += 1
                else:
                    town_dict_french_occurence[f"{user_obj.town_birth_place}"] = 0
                    town_dict_french_occurence[f"{user_obj.town_birth_place}"] += 1

                if user_obj.town_birth_place not in town_birth_french_dict_grade:
                    town_birth_french_dict_grade[user_obj.town_birth_place] = 0
                    town_birth_french_dict_grade[user_obj.town_birth_place] += user_obj.power_ranking
                else:
                    town_birth_french_dict_grade[user_obj.town_birth_place] += user_obj.power_ranking

                if user_obj.town_birth_place in town_birth_french_dict_occurence:
                    town_birth_french_dict_occurence[user_obj.town_birth_place] += 1
                else:
                    town_birth_french_dict_occurence[user_obj.town_birth_place] = 0


            if (
                user_obj.country_death_place.lower() == "france"
                and user_obj.town_death_place.lower() != "undefined"
                and user_obj.town_death_place != ""
                and user_obj.town_death_place != "alive"
            ):
                if user_obj.town_death_place not in town_dict_french_grade:
                    town_dict_french_grade[user_obj.town_death_place] = 0
                    town_dict_french_grade[user_obj.town_death_place] += user_obj.power_ranking
                else:
                    town_dict_french_grade[user_obj.town_death_place] += user_obj.power_ranking

                if user_obj.town_death_place in town_dict_french_occurence:
                    town_dict_french_occurence[f"{user_obj.town_death_place}"] += 1
                else:
                    town_dict_french_occurence[f"{user_obj.town_death_place}"] = 0
                    town_dict_french_occurence[f"{user_obj.town_death_place}"] += 1

                if user_obj.town_death_place not in town_death_french_dict_grade:
                    town_death_french_dict_grade[user_obj.town_death_place] = 0
                    town_death_french_dict_grade[user_obj.town_death_place] += user_obj.power_ranking
                else:
                    town_death_french_dict_grade[user_obj.town_death_place] += user_obj.power_ranking

                if user_obj.town_death_place in town_death_french_dict_occurence:
                    town_death_french_dict_occurence[user_obj.town_death_place] += 1
                else:
                    town_death_french_dict_occurence[user_obj.town_death_place] = 0


            if user_obj.last_name.lower() != "undefined" and user_obj.last_name != "":
                if user_obj.last_name not in last_name_dict_grade:
                    last_name_dict_grade[user_obj.last_name] = 0
                    last_name_dict_grade[user_obj.last_name] += user_obj.power_ranking
                else:
                    last_name_dict_grade[user_obj.last_name] += user_obj.power_ranking

                if user_obj.last_name in last_name_dict_occurence:
                    last_name_dict_occurence[f"{user_obj.last_name}"] += 1
                else:
                    last_name_dict_occurence[f"{user_obj.last_name}"] = 0
                    last_name_dict_occurence[f"{user_obj.last_name}"] += 1

            if 1 <= user_obj.age <= 122:
                if user_obj.age not in age_dict_grade:
                    age_dict_grade[user_obj.age] = 0
                    age_dict_grade[user_obj.age] += user_obj.power_ranking
                else:
                    age_dict_grade[user_obj.age] += user_obj.power_ranking

                if user_obj.age in age_dict_occurence:
                    age_dict_occurence[user_obj.age] += 1
                else:
                    age_dict_occurence[user_obj.age] = 0
                    age_dict_occurence[user_obj.age] += 1

            if 1 <= user_obj.birth_year <= 2026:
                if user_obj.birth_year not in birth_year_dict_grade:
                    birth_year_dict_grade[user_obj.birth_year] = 0
                    birth_year_dict_grade[user_obj.birth_year] += user_obj.power_ranking
                else:
                    birth_year_dict_grade[user_obj.birth_year] += user_obj.power_ranking

                if user_obj.birth_year in birth_year_dict_occurence:
                    birth_year_dict_occurence[user_obj.birth_year] += 1
                else:
                    birth_year_dict_occurence[user_obj.birth_year] = 0
                    birth_year_dict_occurence[user_obj.birth_year] += 1





            if user_obj.region_of_death != "Undefined" and user_obj.region_of_death != "" and user_obj.is_alive is False:
                if user_obj.region_of_death not in region_of_death_dict_grade:
                    region_of_death_dict_grade[user_obj.region_of_death] = 0
                    region_of_death_dict_grade[user_obj.region_of_death] += user_obj.power_ranking
                else:
                    region_of_death_dict_grade[user_obj.region_of_death] += user_obj.power_ranking

                if user_obj.region_of_death in region_of_death_dict_occurence:
                    region_of_death_dict_occurence[user_obj.region_of_death] += 1
                else:
                    region_of_death_dict_occurence[user_obj.region_of_death] = 1

                if user_obj.region_of_death not in region_of_birth_and_death_dict_grade:
                    region_of_birth_and_death_dict_grade[user_obj.region_of_death] = 0
                    region_of_birth_and_death_dict_grade[user_obj.region_of_death] += user_obj.power_ranking
                else:
                    region_of_birth_and_death_dict_grade[user_obj.region_of_death] += user_obj.power_ranking

                if user_obj.region_of_death in region_of_birth_and_death_dict_occurence:
                    region_of_birth_and_death_dict_occurence[user_obj.region_of_death] += 1
                else:
                    region_of_birth_and_death_dict_occurence[user_obj.region_of_death] = 1


            if user_obj.region_of_birth != "Undefined" and user_obj.region_of_birth != "":
                if user_obj.region_of_birth not in region_of_birth_dict_grade:
                    region_of_birth_dict_grade[user_obj.region_of_birth] = 0
                    region_of_birth_dict_grade[user_obj.region_of_birth] += user_obj.power_ranking
                else:
                    region_of_birth_dict_grade[user_obj.region_of_birth] += user_obj.power_ranking

                if user_obj.region_of_birth in region_of_birth_dict_occurence:
                    region_of_birth_dict_occurence[user_obj.region_of_birth] += 1
                else:
                    region_of_birth_dict_occurence[user_obj.region_of_birth] = 0
                    region_of_birth_dict_occurence[user_obj.region_of_birth] += 1

                if user_obj.region_of_birth not in region_of_birth_and_death_dict_grade:
                    region_of_birth_and_death_dict_grade[user_obj.region_of_birth] = 0
                    region_of_birth_and_death_dict_grade[user_obj.region_of_birth] += user_obj.power_ranking
                else:
                    region_of_birth_and_death_dict_grade[user_obj.region_of_birth] += user_obj.power_ranking

                if user_obj.region_of_birth in region_of_birth_and_death_dict_occurence:
                    region_of_birth_and_death_dict_occurence[user_obj.region_of_birth] += 1
                else:
                    region_of_birth_and_death_dict_occurence[user_obj.region_of_birth] = 1
                


            if user_obj.time_period_of_birth.lower() != "undefined" and user_obj.time_period_of_birth != "":
                if user_obj.time_period_of_birth not in time_period_of_birth_dict_grade:
                    time_period_of_birth_dict_grade[user_obj.time_period_of_birth] = 0
                    time_period_of_birth_dict_grade[user_obj.time_period_of_birth] += user_obj.power_ranking
                else:
                    time_period_of_birth_dict_grade[user_obj.time_period_of_birth] += user_obj.power_ranking

                if user_obj.time_period_of_birth in time_period_of_birth_dict_occurence:
                    time_period_of_birth_dict_occurence[f"{user_obj.time_period_of_birth}"] += 1
                else:
                    time_period_of_birth_dict_occurence[f"{user_obj.time_period_of_birth}"] = 0
                    time_period_of_birth_dict_occurence[f"{user_obj.time_period_of_birth}"] += 1


            if user_obj.continent_of_birth != "Undefined" and user_obj.continent_of_birth != "":
                if user_obj.continent_of_birth not in continent_of_birth_dict_grade:
                    continent_of_birth_dict_grade[user_obj.continent_of_birth] = 0
                    continent_of_birth_dict_grade[user_obj.continent_of_birth] += user_obj.power_ranking
                else:
                    continent_of_birth_dict_grade[user_obj.continent_of_birth] += user_obj.power_ranking

                if user_obj.continent_of_birth in continent_of_birth_dict_occurence:
                    continent_of_birth_dict_occurence[f"{user_obj.continent_of_birth}"] += 1
                else:
                    continent_of_birth_dict_occurence[f"{user_obj.continent_of_birth}"] = 0
                    continent_of_birth_dict_occurence[f"{user_obj.continent_of_birth}"] += 1

            if user_obj.page_lenght >= 0:
                if user_obj.page_lenght not in page_lenght_dict_grade:
                    page_lenght_dict_grade[user_obj.page_lenght] = 0
                    page_lenght_dict_grade[user_obj.page_lenght] += user_obj.power_ranking
                else:
                    page_lenght_dict_grade[user_obj.page_lenght] += user_obj.power_ranking

                if user_obj.page_lenght in page_lenght_dict_occurence:
                    page_lenght_dict_occurence[user_obj.page_lenght] += 1
                else:
                    page_lenght_dict_occurence[user_obj.page_lenght] = 0
                    page_lenght_dict_occurence[user_obj.page_lenght] += 1
            if user_obj.first_char_of_the_page != "Undefined" and user_obj.first_char_of_the_page != "":
                if user_obj.first_char_of_the_page not in first_char_of_the_page_dict_grade:
                    first_char_of_the_page_dict_grade[user_obj.first_char_of_the_page] = 0
                    first_char_of_the_page_dict_grade[user_obj.first_char_of_the_page] += user_obj.power_ranking
                else:
                    first_char_of_the_page_dict_grade[user_obj.first_char_of_the_page] += user_obj.power_ranking

                if user_obj.first_char_of_the_page in first_char_of_the_page_dict_occurence:
                    first_char_of_the_page_dict_occurence[f"{user_obj.first_char_of_the_page}"] += 1
                else:
                    first_char_of_the_page_dict_occurence[f"{user_obj.first_char_of_the_page}"] = 0
                    first_char_of_the_page_dict_occurence[f"{user_obj.first_char_of_the_page}"] += 1

            if user_obj.country_birth_place.lower() != "undefined" and user_obj.country_birth_place != "":
                if user_obj.country_birth_place not in country_birth_dict_grade:
                    country_birth_dict_grade[user_obj.country_birth_place] = 0
                    country_birth_dict_grade[user_obj.country_birth_place] += user_obj.power_ranking
                else:
                    country_birth_dict_grade[user_obj.country_birth_place] += user_obj.power_ranking

                if user_obj.country_birth_place in country_birth_dict_occurence:
                    country_birth_dict_occurence[user_obj.country_birth_place] += 1
                else:
                    country_birth_dict_occurence[user_obj.country_birth_place] = 0


            if (
                user_obj.country_death_place.lower() != "undefined"
                and user_obj.country_death_place != ""
                and user_obj.country_death_place.lower() != "alive"
            ):
                if user_obj.country_death_place not in country_death_dict_grade:
                    country_death_dict_grade[user_obj.country_death_place] = 0
                    country_death_dict_grade[user_obj.country_death_place] += user_obj.power_ranking
                else:
                    country_death_dict_grade[user_obj.country_death_place] += user_obj.power_ranking

                if user_obj.country_death_place in country_death_dict_occurence:
                    country_death_dict_occurence[user_obj.country_death_place] += 1
                else:
                    country_death_dict_occurence[user_obj.country_death_place] = 0


            #if  user_obj.death_month_day.lower() != "undefined" and user_obj.death_month_day != "" and "fluriel" not in user_obj.death_month_day.lower() and user_obj.is_alive is False:
            #if user_obj.is_alive is False:
            
            # if user_obj.death_month_day != "alive" and user_obj.death_month_day.lower() != "undefined":
            #     print("deathday_dict_occurence " , user_obj.death_month_day)
            if (
                user_obj.death_month_day
                and user_obj.birth_month_day
                and user_obj.death_month_day.lower() not in ("undefined", "alive")
                and user_obj.birth_month_day.lower() != "undefined"
                and "fluriel" not in user_obj.birth_month_day.lower()
                and "fluriel" not in user_obj.death_month_day.lower()
            ):
                if user_obj.death_month_day not in deathday_dict_occurence:
                    deathday_dict_grade[user_obj.death_month_day] = 0
                    deathday_dict_grade[user_obj.death_month_day] += user_obj.power_ranking
                else:
                    deathday_dict_grade[user_obj.death_month_day] += user_obj.power_ranking

                if user_obj.death_month_day in deathday_dict_occurence:
                    deathday_dict_occurence[f"{user_obj.death_month_day}"] += 1
                else:
                    deathday_dict_occurence[f"{user_obj.death_month_day}"] = 0
                    deathday_dict_occurence[f"{user_obj.death_month_day}"] += 1


                
                if user_obj.death_month_day not in birth_and_death_date_dict_grade:
                    birth_and_death_date_dict_grade[user_obj.death_month_day] = 0
                    birth_and_death_date_dict_grade[user_obj.death_month_day] += user_obj.power_ranking
                else:
                    birth_and_death_date_dict_grade[user_obj.birth_month_day] += user_obj.power_ranking

                if user_obj.death_month_day in birth_and_death_date_dict_occurence:
                    birth_and_death_date_dict_occurence[user_obj.death_month_day] += 1
                else:
                    birth_and_death_date_dict_occurence[user_obj.death_month_day] = 0
            

            # if user_obj.birth_date is not None and str(user_obj.birth_date) != "":
            #     birth_date = str(user_obj.birth_date)

            #     if birth_date not in birth_date_dict_grade:
            #         birth_date_dict_grade[birth_date] = 0
            #         birth_date_dict_grade[birth_date] += user_obj.power_ranking
            #     else:
            #         birth_date_dict_grade[birth_date] += user_obj.power_ranking

            #     if birth_date in birth_date_dict_occurence:
            #         birth_date_dict_occurence[birth_date] += 1
            #     else:
            #         birth_date_dict_occurence[birth_date] = 0


            # if user_obj.death_date is not None and str(user_obj.death_date) != "":
            #     death_date = str(user_obj.death_date)

            #     if death_date not in death_date_dict_grade:
            #         death_date_dict_grade[death_date] = 0
            #         death_date_dict_grade[death_date] += user_obj.power_ranking
            #     else:
            #         death_date_dict_grade[death_date] += user_obj.power_ranking

            #     if death_date in death_date_dict_occurence:
            #         death_date_dict_occurence[death_date] += 1
            #     else:
            #         death_date_dict_occurence[death_date] = 0
        except:
            traceback.print_exc()
            error+=1
            if error > 20:
                return




    # print(town_birth_french_dict_grade)
    # print(town_death_french_dict_grade)
    # print(country_birth_dict_grade)
    # print(country_death_dict_grade)

    list_of_dict_occurence = [
        name_dict_occurence,
        town_dict_occurence,
        job_dict_occurence,
        country_dict_occurence,
        birthday_dict_occurence,
        town_dict_french_occurence,
        last_name_dict_occurence,
        age_dict_occurence,
        birth_year_dict_occurence,
        region_of_birth_dict_occurence,
        page_lenght_dict_occurence,
        first_char_of_the_page_dict_occurence,
        boy_name_dict_occurence,
        girl_name_dict_occurence,
        french_boy_name_dict_occurence,
        french_girl_name_dict_occurence,
        french_last_name_dict_occurence,
        time_period_of_birth_dict_occurence,
        continent_of_birth_dict_occurence,
        town_death_dict_occurence,
        town_birth_dict_occurence,
        town_birth_french_dict_occurence,
        town_death_french_dict_occurence,
        country_birth_dict_occurence,
        country_death_dict_occurence,
        deathday_dict_occurence,
        region_of_death_dict_occurence,
        region_of_birth_and_death_dict_occurence,
        birth_and_death_date_dict_occurence
    ]

    list_of_dict_score = [
        name_dict_grade,
        town_dict_grade,
        job_dict_grade,
        country_dict_grade,
        birthday_dict_grade,
        town_dict_french_grade,
        last_name_dict_grade,
        age_dict_grade,
        birth_year_dict_grade,
        region_of_birth_dict_grade,
        page_lenght_dict_grade,
        first_char_of_the_page_dict_grade,
        boy_name_dict_grade,
        girl_name_dict_grade,
        french_boy_name_dict_grade,
        french_girl_name_dict_grade,
        french_last_name_dict_grade,
        time_period_of_birth_dict_grade,
        continent_of_birth_dict_grade,
        town_death_dict_grade,
        town_birth_dict_grade,
        town_birth_french_dict_grade,
        town_death_french_dict_grade,
        country_birth_dict_grade,
        country_death_dict_grade,
        deathday_dict_grade,
        region_of_death_dict_grade,
        region_of_birth_and_death_dict_grade,
        birth_and_death_date_dict_grade
    ]

    list_of_variable_to_search = ["name","town","job","country","birthday","french_town","last_name","age","birth_year","region_of_birth","page_name_lenght","first_char_of_the_page","boy_name","girl_name","french_boy_name","french_girl_name","french_last_name","time_period_of_birth",
    "continent","town_death","town_birth","french_town_birth","french_town_death","country_birth","country_death","deathday","region_of_death","region","birth_and_death_month_day"]

    # print(name_dict_grade)
    # print(name_dict_occurence)
    size_list = [5,25,100,250,500,1000,2500,5000,10000,25000,50000,100000]
    alphabet = "abcdefghijklmnopqrstuvwxyz"


    for index in range(len(list_of_dict_score)):
        print(f"Currently working on {list_of_variable_to_search[index]} dict")
        print(VARIABLE_TO_LETTER_FOR_RANKING[list_of_variable_to_search[index]])
        
        if list_of_variable_to_search[index] in ["birthday","time_period_of_birth","continent"]:
            size_list = [5]
        elif list_of_variable_to_search[index] in ["town"]:
            size_list = [5,25,100,250,500,1000,2500,5000,10000]    
        elif list_of_variable_to_search[index] in ["birthday"]:
            size_list = [25,100,250,500,1000,2500,5000,10000,25000,50000,100000]
        elif list_of_variable_to_search[index] in ["french_town","french_town_birth","french_town_death"]:
            size_list = [5,25,100,250,500,1000,2500]
        elif list_of_variable_to_search[index] in ["region_of_death","region"]:
            size_list = [25,100,250,500,1000,2500,5000,10000,25000,50000,100000]
        elif list_of_variable_to_search[index] in ["first_char_of_the_page"]:
            size_list = [5,25,100,250,500,1000,2500,5000,10000,25000,50000,100000]    
        else:
            size_list = [5,25,100,250,500,1000,2500,5000,10000,25000,50000,100000]

        try:                    
            for key , value  in list_of_dict_score[index].items():
                if list_of_dict_occurence[index][key] == 0:
                    continue
                list_of_dict_score[index][key] = round(value / list_of_dict_occurence[index][key],5)
            list_of_dict_score[index] = dict(sorted(list_of_dict_score[index].items(), key=lambda item: item[1],reverse=True))
            try:
                for nb , size in enumerate(size_list):
                    isFile = os.path.isfile(f"ranking_folder/${VARIABLE_TO_LETTER_FOR_RANKING[list_of_variable_to_search[index]]}_{list_of_variable_to_search[index]}_#{alphabet[nb]}_score_of_size{size}.txt")
                    if isFile:
                        reset_file(f"ranking_folder/${VARIABLE_TO_LETTER_FOR_RANKING[list_of_variable_to_search[index]]}_{list_of_variable_to_search[index]}_#{alphabet[nb]}_score_of_size{size}.txt")
            except:
                print(f"{list_of_variable_to_search[index]} dict small mistakes")
                traceback.print_exc()
                pass
        except:
            print(f"{list_of_variable_to_search[index]} dict big mistakes")
            traceback.print_exc()
            pass

        for key , value  in list_of_dict_score[index].items():
            for nb , size in enumerate(size_list):
                if list_of_dict_occurence[index][key] >= size:
                    #print(key,value,name_dict_occurence[key])
                    #write_into_file("name_score.txt",f"Prénom: {key} Score: {value} Nombre d'occurences du prénom: {name_dict_occurence[key]}\n")
                    write_into_file(f"ranking_folder/${VARIABLE_TO_LETTER_FOR_RANKING[list_of_variable_to_search[index]]}_{list_of_variable_to_search[index]}_#{alphabet[nb]}_score_of_size{size}.txt",f"{key}#####{value}#####{list_of_dict_occurence[index][key]}\n")
                    
                
    return HttpResponse("DONE!",status=200)


def calc_gender_ratio_of_some_variable(request):
    """Compute gender ratio of different variables"""

    if request.method != "GET":
        return HttpResponse("Error!", status=404)

    last_name_occurence = {}
    last_name_gender_nb = {}
    last_name_ratio = {}

    french_last_name_occurence = {}
    french_last_name_gender_nb = {}
    french_last_name_ratio = {}

    age_occurence = {}
    age_gender_nb = {}
    age_gender_ratio = {}

    town_birth_occurence = {}
    town_birth_gender_nb = {}
    town_birth_gender_ratio = {}

    town_death_occurence = {}
    town_death_gender_nb = {}
    town_death_gender_ratio = {}

    town_occurence = {}
    town_gender_nb = {}
    town_gender_ratio = {}

    french_town_birth_occurence = {}
    french_town_birth_gender_nb = {}
    french_town_birth_gender_ratio = {}

    french_town_death_occurence = {}
    french_town_death_gender_nb = {}
    french_town_death_gender_ratio = {}

    french_town_occurence = {}
    french_town_gender_nb = {}
    french_town_gender_ratio = {}

    country_birth_occurence = {}
    country_birth_gender_nb = {}
    country_birth_gender_ratio = {}

    country_death_occurence = {}
    country_death_gender_nb = {}
    country_death_gender_ratio = {}

    country_occurence = {}
    country_gender_nb = {}
    country_gender_ratio = {}

    continent_of_birth_occurence = {}
    continent_of_birth_gender_nb = {}
    continent_of_birth_gender_ratio = {}

    continent_of_death_occurence = {}
    continent_of_death_gender_nb = {}
    continent_of_death_gender_ratio = {}

    continent_occurence = {}
    continent_gender_nb = {}
    continent_gender_ratio = {}

    region_of_birth_occurence = {}
    region_of_birth_gender_nb = {}
    region_of_birth_gender_ratio = {}

    region_of_death_occurence = {}
    region_of_death_gender_nb = {}
    region_of_death_gender_ratio = {}

    region_occurence = {}
    region_gender_nb = {}
    region_gender_ratio = {}

    time_period_of_birth_occurence = {}
    time_period_of_birth_gender_nb = {}
    time_period_of_birth_gender_ratio = {}

    all_user_obj = WikipediaUser.objects.all().order_by("position").filter(position__gte=0)


    for user_obj in all_user_obj:

        if user_obj.gender in ["Man", "Woman"]:

            # =====================================================
            # LAST NAME
            # =====================================================

            if user_obj.last_name.lower() != "undefined" and user_obj.last_name != "":
                if user_obj.last_name not in last_name_occurence:
                    last_name_occurence[user_obj.last_name] = 1
                else:
                    last_name_occurence[user_obj.last_name] += 1

                if f"{user_obj.last_name}_nb_of_{user_obj.gender.lower()}" not in last_name_gender_nb:
                    last_name_gender_nb[f"{user_obj.last_name}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    last_name_gender_nb[f"{user_obj.last_name}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # FRENCH LAST NAME
            # =====================================================

            if user_obj.last_name.lower() != "undefined" and user_obj.last_name != "" and user_obj.country_birth_place.lower() == "france":
                if user_obj.last_name not in french_last_name_occurence:
                    french_last_name_occurence[user_obj.last_name] = 1
                else:
                    french_last_name_occurence[user_obj.last_name] += 1

                if f"{user_obj.last_name}_nb_of_{user_obj.gender.lower()}" not in french_last_name_gender_nb:
                    french_last_name_gender_nb[f"{user_obj.last_name}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    french_last_name_gender_nb[f"{user_obj.last_name}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # AGE
            # =====================================================

            if user_obj.age > 0 and user_obj.age < 123:
                if user_obj.age not in age_occurence:
                    age_occurence[user_obj.age] = 1
                else:
                    age_occurence[user_obj.age] += 1

                if f"{user_obj.age}_nb_of_{user_obj.gender.lower()}" not in age_gender_nb:
                    age_gender_nb[f"{user_obj.age}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    age_gender_nb[f"{user_obj.age}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # TOWN BIRTH
            # =====================================================

            if user_obj.town_birth_place.lower() != "undefined" and user_obj.town_birth_place != "":
                if user_obj.town_birth_place not in town_birth_occurence:
                    town_birth_occurence[user_obj.town_birth_place] = 1
                else:
                    town_birth_occurence[user_obj.town_birth_place] += 1

                if f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}" not in town_birth_gender_nb:
                    town_birth_gender_nb[f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    town_birth_gender_nb[f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # TOWN DEATH
            # =====================================================

            if user_obj.town_death_place.lower() != "undefined" and user_obj.town_death_place != "" and user_obj.is_alive is False:
                if user_obj.town_death_place not in town_death_occurence:
                    town_death_occurence[user_obj.town_death_place] = 1
                else:
                    town_death_occurence[user_obj.town_death_place] += 1

                if f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}" not in town_death_gender_nb:
                    town_death_gender_nb[f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    town_death_gender_nb[f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # TOWN = BIRTH + DEATH
            # =====================================================

            if user_obj.town_birth_place.lower() != "undefined" and user_obj.town_birth_place != "":
                if user_obj.town_birth_place not in town_occurence:
                    town_occurence[user_obj.town_birth_place] = 1
                else:
                    town_occurence[user_obj.town_birth_place] += 1

                if f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}" not in town_gender_nb:
                    town_gender_nb[f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    town_gender_nb[f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}"] += 1

            if user_obj.town_death_place.lower() != "undefined" and user_obj.town_death_place != "" and user_obj.is_alive is False:
                if user_obj.town_death_place not in town_occurence:
                    town_occurence[user_obj.town_death_place] = 1
                else:
                    town_occurence[user_obj.town_death_place] += 1

                if f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}" not in town_gender_nb:
                    town_gender_nb[f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    town_gender_nb[f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # FRENCH TOWN BIRTH
            # =====================================================

            if (
                user_obj.town_birth_place.lower() != "undefined"
                and user_obj.town_birth_place != ""
                and user_obj.country_birth_place.lower() == "france"
            ):
                if user_obj.town_birth_place not in french_town_birth_occurence:
                    french_town_birth_occurence[user_obj.town_birth_place] = 1
                else:
                    french_town_birth_occurence[user_obj.town_birth_place] += 1

                if f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}" not in french_town_birth_gender_nb:
                    french_town_birth_gender_nb[f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    french_town_birth_gender_nb[f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # FRENCH TOWN DEATH
            # =====================================================

            if (
                user_obj.town_death_place.lower() != "undefined"
                and user_obj.town_death_place != ""
                and user_obj.country_death_place.lower() == "france" and user_obj.is_alive is False
            ):
                if user_obj.town_death_place not in french_town_death_occurence:
                    french_town_death_occurence[user_obj.town_death_place] = 1
                else:
                    french_town_death_occurence[user_obj.town_death_place] += 1

                if f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}" not in french_town_death_gender_nb:
                    french_town_death_gender_nb[f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    french_town_death_gender_nb[f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # FRENCH TOWN = BIRTH + DEATH
            # =====================================================

            if (
                user_obj.town_birth_place.lower() != "undefined"
                and user_obj.town_birth_place != ""
                and user_obj.country_birth_place.lower() == "france"
            ):
                if user_obj.town_birth_place not in french_town_occurence:
                    french_town_occurence[user_obj.town_birth_place] = 1
                else:
                    french_town_occurence[user_obj.town_birth_place] += 1

                if f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}" not in french_town_gender_nb:
                    french_town_gender_nb[f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    french_town_gender_nb[f"{user_obj.town_birth_place}_nb_of_{user_obj.gender.lower()}"] += 1

            if (
                user_obj.town_death_place.lower() != "undefined"
                and user_obj.town_death_place != ""
                and user_obj.country_death_place.lower() == "france" and user_obj.is_alive is False
            ):
                if user_obj.town_death_place not in french_town_occurence:
                    french_town_occurence[user_obj.town_death_place] = 1
                else:
                    french_town_occurence[user_obj.town_death_place] += 1

                if f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}" not in french_town_gender_nb:
                    french_town_gender_nb[f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    french_town_gender_nb[f"{user_obj.town_death_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # COUNTRY BIRTH
            # =====================================================

            if user_obj.country_birth_place.lower() != "undefined" and user_obj.country_birth_place != "":
                if user_obj.country_birth_place not in country_birth_occurence:
                    country_birth_occurence[user_obj.country_birth_place] = 1
                else:
                    country_birth_occurence[user_obj.country_birth_place] += 1

                if f"{user_obj.country_birth_place}_nb_of_{user_obj.gender.lower()}" not in country_birth_gender_nb:
                    country_birth_gender_nb[f"{user_obj.country_birth_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    country_birth_gender_nb[f"{user_obj.country_birth_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # COUNTRY DEATH
            # =====================================================

            if user_obj.country_death_place.lower() != "undefined" and user_obj.country_death_place != "" and user_obj.is_alive is False:
                if user_obj.country_death_place not in country_death_occurence:
                    country_death_occurence[user_obj.country_death_place] = 1
                else:
                    country_death_occurence[user_obj.country_death_place] += 1

                if f"{user_obj.country_death_place}_nb_of_{user_obj.gender.lower()}" not in country_death_gender_nb:
                    country_death_gender_nb[f"{user_obj.country_death_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    country_death_gender_nb[f"{user_obj.country_death_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # COUNTRY = BIRTH + DEATH
            # =====================================================

            if user_obj.country_birth_place.lower() != "undefined" and user_obj.country_birth_place != "":
                if user_obj.country_birth_place not in country_occurence:
                    country_occurence[user_obj.country_birth_place] = 1
                else:
                    country_occurence[user_obj.country_birth_place] += 1

                if f"{user_obj.country_birth_place}_nb_of_{user_obj.gender.lower()}" not in country_gender_nb:
                    country_gender_nb[f"{user_obj.country_birth_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    country_gender_nb[f"{user_obj.country_birth_place}_nb_of_{user_obj.gender.lower()}"] += 1

            if user_obj.country_death_place.lower() != "undefined" and user_obj.country_death_place != "" and user_obj.is_alive is False:
                if user_obj.country_death_place not in country_occurence:
                    country_occurence[user_obj.country_death_place] = 1
                else:
                    country_occurence[user_obj.country_death_place] += 1

                if f"{user_obj.country_death_place}_nb_of_{user_obj.gender.lower()}" not in country_gender_nb:
                    country_gender_nb[f"{user_obj.country_death_place}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    country_gender_nb[f"{user_obj.country_death_place}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # CONTINENT BIRTH
            # =====================================================

            if user_obj.continent_of_birth.lower() != "undefined" and user_obj.continent_of_birth != "":
                if user_obj.continent_of_birth not in continent_of_birth_occurence:
                    continent_of_birth_occurence[user_obj.continent_of_birth] = 1
                else:
                    continent_of_birth_occurence[user_obj.continent_of_birth] += 1

                if f"{user_obj.continent_of_birth}_nb_of_{user_obj.gender.lower()}" not in continent_of_birth_gender_nb:
                    continent_of_birth_gender_nb[f"{user_obj.continent_of_birth}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    continent_of_birth_gender_nb[f"{user_obj.continent_of_birth}_nb_of_{user_obj.gender.lower()}"] += 1


            # =====================================================
            # CONTINENT DEATH
            # =====================================================

            if user_obj.continent_of_death.lower() != "undefined" and user_obj.continent_of_death != "" and user_obj.is_alive is False:
                if user_obj.continent_of_death not in continent_of_death_occurence:
                    continent_of_death_occurence[user_obj.continent_of_death] = 1
                else:
                    continent_of_death_occurence[user_obj.continent_of_death] += 1

                if f"{user_obj.continent_of_death}_nb_of_{user_obj.gender.lower()}" not in continent_of_death_gender_nb:
                    continent_of_death_gender_nb[f"{user_obj.continent_of_death}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    continent_of_death_gender_nb[f"{user_obj.continent_of_death}_nb_of_{user_obj.gender.lower()}"] += 1


            # =====================================================
            # CONTINENT = BIRTH + DEATH
            # =====================================================

            if user_obj.continent_of_birth.lower() != "undefined" and user_obj.continent_of_birth != "":
                if user_obj.continent_of_birth not in continent_occurence:
                    continent_occurence[user_obj.continent_of_birth] = 1
                else:
                    continent_occurence[user_obj.continent_of_birth] += 1

                if f"{user_obj.continent_of_birth}_nb_of_{user_obj.gender.lower()}" not in continent_gender_nb:
                    continent_gender_nb[f"{user_obj.continent_of_birth}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    continent_gender_nb[f"{user_obj.continent_of_birth}_nb_of_{user_obj.gender.lower()}"] += 1


            if user_obj.continent_of_death.lower() != "undefined" and user_obj.continent_of_death != "" and user_obj.is_alive is False:
                if user_obj.continent_of_death not in continent_occurence:
                    continent_occurence[user_obj.continent_of_death] = 1
                else:
                    continent_occurence[user_obj.continent_of_death] += 1

                if f"{user_obj.continent_of_death}_nb_of_{user_obj.gender.lower()}" not in continent_gender_nb:
                    continent_gender_nb[f"{user_obj.continent_of_death}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    continent_gender_nb[f"{user_obj.continent_of_death}_nb_of_{user_obj.gender.lower()}"] += 1
            # =====================================================
            # REGION BIRTH
            # =====================================================

            if user_obj.region_of_birth.lower() != "undefined" and user_obj.region_of_birth != "":
                if user_obj.region_of_birth not in region_of_birth_occurence:
                    region_of_birth_occurence[user_obj.region_of_birth] = 1
                else:
                    region_of_birth_occurence[user_obj.region_of_birth] += 1

                if f"{user_obj.region_of_birth}_nb_of_{user_obj.gender.lower()}" not in region_of_birth_gender_nb:
                    region_of_birth_gender_nb[f"{user_obj.region_of_birth}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    region_of_birth_gender_nb[f"{user_obj.region_of_birth}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # REGION DEATH
            # =====================================================

            if user_obj.region_of_death.lower() != "undefined" and user_obj.region_of_death != "" and user_obj.is_alive is False:
                if user_obj.region_of_death not in region_of_death_occurence:
                    region_of_death_occurence[user_obj.region_of_death] = 1
                else:
                    region_of_death_occurence[user_obj.region_of_death] += 1

                if f"{user_obj.region_of_death}_nb_of_{user_obj.gender.lower()}" not in region_of_death_gender_nb:
                    region_of_death_gender_nb[f"{user_obj.region_of_death}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    region_of_death_gender_nb[f"{user_obj.region_of_death}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # REGION = BIRTH + DEATH
            # =====================================================

            if user_obj.region_of_birth.lower() != "undefined" and user_obj.region_of_birth != "":
                if user_obj.region_of_birth not in region_occurence:
                    region_occurence[user_obj.region_of_birth] = 1
                else:
                    region_occurence[user_obj.region_of_birth] += 1

                if f"{user_obj.region_of_birth}_nb_of_{user_obj.gender.lower()}" not in region_gender_nb:
                    region_gender_nb[f"{user_obj.region_of_birth}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    region_gender_nb[f"{user_obj.region_of_birth}_nb_of_{user_obj.gender.lower()}"] += 1

            if user_obj.region_of_death.lower() != "undefined" and user_obj.region_of_death != "" and user_obj.is_alive is False:
                if user_obj.region_of_death not in region_occurence:
                    region_occurence[user_obj.region_of_death] = 1
                else:
                    region_occurence[user_obj.region_of_death] += 1

                if f"{user_obj.region_of_death}_nb_of_{user_obj.gender.lower()}" not in region_gender_nb:
                    region_gender_nb[f"{user_obj.region_of_death}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    region_gender_nb[f"{user_obj.region_of_death}_nb_of_{user_obj.gender.lower()}"] += 1

            # =====================================================
            # TIME PERIOD OF BIRTH
            # =====================================================

            if user_obj.time_period_of_birth.lower() != "undefined" and user_obj.time_period_of_birth != "":
                if user_obj.time_period_of_birth not in time_period_of_birth_occurence:
                    time_period_of_birth_occurence[HISTORICAL_PERIODS_DICT_TO_FRENCH[user_obj.time_period_of_birth]] = 1
                else:
                    time_period_of_birth_occurence[HISTORICAL_PERIODS_DICT_TO_FRENCH[user_obj.time_period_of_birth]] += 1

                if f"{user_obj.time_period_of_birth}_nb_of_{user_obj.gender.lower()}" not in time_period_of_birth_gender_nb:
                    time_period_of_birth_gender_nb[f"{user_obj.time_period_of_birth}_nb_of_{user_obj.gender.lower()}"] = 1
                else:
                    time_period_of_birth_gender_nb[f"{user_obj.time_period_of_birth}_nb_of_{user_obj.gender.lower()}"] += 1
            

    size_list = [
        5, 25, 100, 250, 500, 1000,
        2500, 5000, 10000, 25000,
        50000, 100000
    ]

    list_of_dict_occurence = [
        last_name_occurence,
        french_last_name_occurence,
        age_occurence,
        town_birth_occurence,
        town_death_occurence,
        town_occurence,
        french_town_birth_occurence,
        french_town_death_occurence,
        french_town_occurence,
        country_birth_occurence,
        country_death_occurence,
        country_occurence,
        continent_of_birth_occurence,
        continent_of_death_occurence,
        continent_occurence,
        region_of_birth_occurence,
        region_of_death_occurence,
        region_occurence,
        time_period_of_birth_occurence
    ]


    list_of_dict_gender_nb = [
        last_name_gender_nb,
        french_last_name_gender_nb,
        age_gender_nb,
        town_birth_gender_nb,
        town_death_gender_nb,
        town_gender_nb,
        french_town_birth_gender_nb,
        french_town_death_gender_nb,
        french_town_gender_nb,
        country_birth_gender_nb,
        country_death_gender_nb,
        country_gender_nb,
        continent_of_birth_gender_nb,
        continent_of_death_gender_nb,
        continent_gender_nb,
        region_of_birth_gender_nb,
        region_of_death_gender_nb,
        region_gender_nb,
        time_period_of_birth_gender_nb
    ]


    list_of_dict_gender_ratio = [
        last_name_ratio,
        french_last_name_ratio,
        age_gender_ratio,
        town_birth_gender_ratio,
        town_death_gender_ratio,
        town_gender_ratio,
        french_town_birth_gender_ratio,
        french_town_death_gender_ratio,
        french_town_gender_ratio,
        country_birth_gender_ratio,
        country_death_gender_ratio,
        country_gender_ratio,
        continent_of_birth_gender_ratio,
        continent_of_death_gender_ratio,
        continent_gender_ratio,
        region_of_birth_gender_ratio,
        region_of_death_gender_ratio,
        region_gender_ratio,
        time_period_of_birth_gender_ratio
    ]

    list_of_variable_to_search = [
        "last_name",
        "french_last_name",
        "age",
        "town_birth",
        "town_death",
        "town",
        "french_town_birth",
        "french_town_death",
        "french_town",
        "country_birth",
        "country_death",
        "country",
        "continent_birth",
        "continent_death",
        "continent",
        "region_birth",
        "region_death",
        "region",
        "time_period_of_birth"
    ]

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for index in range(len(list_of_dict_occurence)):

        print(f"Currently working on {list_of_variable_to_search[index]}")

        if list_of_variable_to_search[index] in ["birthday","time_period_of_birth","continent","continent_birth","continent_death"]:
            size_list = [5]
        elif list_of_variable_to_search[index] in ["town","country_birth"]:
            size_list = [5,25,100,250,500,1000,2500,5000,10000,25000]    
        elif list_of_variable_to_search[index] in ["french_town","country"]:
            size_list = [5,25,100,250,500,1000,2500,5000,10000,25000,50000]    
        elif list_of_variable_to_search[index] in ["country_death"]:
            size_list = [5,25,100,250,500,1000,2500,5000,10000,25000,50000]    
        elif list_of_variable_to_search[index] in ["french_town_birth"]:
            size_list = [5,25,100,250,500,1000,2500,5000]
        elif list_of_variable_to_search[index] in ["french_town_death"]:
            size_list = [5,25,100,250,500,1000,2500,5000]
        elif list_of_variable_to_search[index] in ["region","region_of_birth","region_of_death"]:
            size_list = [25,100,250,500,1000,2500,5000,10000,25000,50000,100000]             
        else:
            size_list = [5,25,100,250,500,1000,2500,5000,10000,25000,50000,100000]

        for key in list_of_dict_occurence[index].keys():

            try:
                list_of_dict_gender_ratio[index][key] = (
                    list_of_dict_gender_nb[index][f"{key}_nb_of_woman"]
                    /
                    (
                        list_of_dict_gender_nb[index][f"{key}_nb_of_woman"]
                        +
                        list_of_dict_gender_nb[index][f"{key}_nb_of_man"]
                    )
                ) * 100

            except:
                list_of_dict_gender_ratio[index][key] = 0

        list_of_dict_gender_ratio[index] = dict(
            sorted(
                list_of_dict_gender_ratio[index].items(),
                key=lambda item: item[1],
                reverse=True
            )
        )

        # reset_file(f"ranking_folder/${VARIABLE_TO_LETTER_FOR_RANKING[list_of_variable_to_search[index]]}_{list_of_variable_to_search[index]}_#{alphabet[nb]}_score_of_size{size}.txt")

        for nb , size in enumerate(size_list):

            file_path = (
                f"ratio_of_man_and_woman/"
                f"{VARIABLE_TO_LETTER_FOR_GENDER_RATIO[list_of_variable_to_search[index]]}_"
                f"ratio_of_man_and_woman_per_"
                f"{list_of_variable_to_search[index]}_#{alphabet[nb]}"
                f"of_size{size}.txt"
            )

            if os.path.isfile(file_path):
                reset_file(file_path)

        for key, value in list_of_dict_gender_ratio[index].items():

            for nb , size in enumerate(size_list):

                if list_of_dict_occurence[index][key] >= size:

                    try:
                        ratio_of_woman = round(value, 3)
                        ratio_of_man = round(100 - value, 3)

                        write_into_file(
                            (
                                f"ratio_of_man_and_woman/"
                                f"{VARIABLE_TO_LETTER_FOR_GENDER_RATIO[list_of_variable_to_search[index]]}_"
                                f"ratio_of_man_and_woman_per_"
                                f"{list_of_variable_to_search[index]}_#{alphabet[nb]}"
                                f"of_size{size}.txt"
                            ),
                            f"{key}#####"
                            f"{ratio_of_woman}#####"
                            f"{ratio_of_man}#####"
                            f"{list_of_dict_occurence[index][key]}\n"
                        )

                    except:
                        pass

    return HttpResponse("DONE!", status=200)