from collections import Counter
from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django_ratelimit.decorators import ratelimit

from myapp.models import WikipediaUser , WikipediaUserUniqueTown , WikiopediaUserToUpdate

from random import randint
from random import sample
from django.db.models import OuterRef, Subquery

from ..global_variable import *
from ..utility_function  import *


import ast
import os
import json
import csv
import traceback

def hi():
    return HttpResponse("Hi!")


@ratelimit(key='ip', rate='30/m')
def display_user_info(request, username):
    if request.method != "GET":
        return HttpResponse(f"Error! with this {username} info", status=404)

    try:
        user_obj = WikipediaUser.objects.filter(page_name=username.strip()).first()

        print("USER OBJ :", user_obj)
        if user_obj is None and username  != "Personne":
            print("USER NOT FOUND")
            return HttpResponse(f"{username} doesn't exist", status=404)

        #print("PAGE NAME :", user_obj.page_name)

        if username != "Personne":
            try:
                user_obj = WikipediaUser.objects.filter(page_name=username.strip()).first()

                
                page_name = user_obj.page_name
            except:
                return HttpResponse(f"{username} doesn't exist", status=404)

            list_of_unpreciseness_data = []
            if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
                birth_place_emoji = "🏳️"
            else:
                birth_place_emoji = user_obj.country_birth_place_emoji

            if user_obj.town_death_localisation == "" or user_obj.town_death_localisation.lower() == "undefined":
                death_place_emoji = "🏳️"
            else:
                death_place_emoji = user_obj.country_death_place_emoji

            for page_error in user_obj.list_of_unpreciseness_data:
                try:
                    list_of_unpreciseness_data.append(UNPRECISENESS_DATA_FR[page_error]+",")
                except:
                    list_of_unpreciseness_data.append(page_error+",")

            ranking_adjust = 0
            if username != "Gaston Cougny":
                ranking_adjust = 1
            # if username == "Jésus de Nazareth":
            #     user_obj.power_ranking = 1197
            #     user_obj.position = 338
            #     user_obj.position_percentage = 0.05043
            #     user_obj.grade_over_20 = 19.99

            # if username == "Anne Frank":
            #     user_obj.power_ranking = 636
            #     user_obj.position = 1780
            #     user_obj.position_percentage = 0.26559
            #     user_obj.grade_over_20 = 19.95

            # if username == "’Anbasa ibn Suhaym al-Kalbi": 
            #     user_obj.power_ranking = 34 
            #     user_obj.position = 241885 
            #     user_obj.position_percentage = 36.09 
            #     user_obj.grade_over_20 = 12.78 
            
            # if username == "₩uNo": 
            #     user_obj.power_ranking = 60 
            #     user_obj.position = 127250 
            #     user_obj.position_percentage = 18.99 
            #     user_obj.grade_over_20 = 16.2


            user_obj_update_obj = WikiopediaUserToUpdate.objects.filter(page_name=username.strip()).first()
            print("cvacacgkoprkgokpoger")
            print(user_obj_update_obj)
            print(user_obj_update_obj)
            print(user_obj_update_obj)
            print(user_obj_update_obj)
            if user_obj_update_obj is None:
                update_level = 3
            else:
                update_level = user_obj_update_obj.update_level

            print(update_level,update_level,update_level)   
            print("toto") 
            print("korgpoerkgpoerkgpoer00")
            print(page_name)
            user_info_dict = {
                "page_name": page_name,
                "page_url": user_obj.page_url,
                "picture_url": user_obj.picture_url,
                "first_name": user_obj.first_name,
                "first_name_standard": user_obj.first_name_standard,
                "last_name": user_obj.last_name,
                "last_name_standard": user_obj.last_name_standard,
                "job": user_obj.job,
                "town_birth_place": user_obj.town_birth_place,
                "town_birth_place_href": user_obj.town_birth_place_href,
                "birth_town_localisation": user_obj.birth_town_localisation,
                "country_birth_place": user_obj.country_birth_place,
                "time_period_of_birth": HISTORICAL_PERIODS_DICT_TO_FRENCH[user_obj.time_period_of_birth],
                "continent_of_birth": user_obj.continent_of_birth,
                "region_of_birth": user_obj.region_of_birth,
                "birth_date": user_obj.birth_date,
                "birth_year": user_obj.birth_year,
                "birth_month": user_obj.birth_month,
                "birth_day": user_obj.birth_day,
                "birth_month_day": user_obj.birth_month_day,
                "town_death_place": user_obj.town_death_place,
                "town_death_place_href": user_obj.town_death_place_href,
                "town_death_localisation": user_obj.town_death_localisation,
                "country_death_place": user_obj.country_death_place,
                "continent_of_death": user_obj.continent_of_death,
                "region_of_death": user_obj.region_of_death,
                "born_and_died_in_the_same_town": user_obj.born_and_died_in_the_same_town,
                "born_and_died_in_the_same_country": user_obj.born_and_died_in_the_same_country,
                "born_and_died_in_the_same_continent": user_obj.born_and_died_in_the_same_continent,
                "born_and_died_in_the_same_region": user_obj.born_and_died_in_the_same_region,
                "death_date": user_obj.death_date,
                "death_year": user_obj.death_year,
                "death_month": user_obj.death_month,
                "death_day": user_obj.death_day,
                "death_month_day": user_obj.death_month_day,
                "cause_of_death":user_obj.cause_of_death,
                "is_cause_of_death_known":user_obj.is_cause_of_death_known,
                "born_before_christ": user_obj.born_before_christ,
                "died_before_christ": user_obj.died_before_christ,
                "born_and_died_before_christ": user_obj.born_and_died_before_christ,
                "born_and_died_after_christ": user_obj.born_and_died_after_christ,
                "born_before_christ_and_died_after_christ": user_obj.born_before_christ_and_died_after_christ,
                "age": user_obj.age,
                "week_day_of_birth":user_obj.week_day_of_birth,
                "week_day_of_death":user_obj.week_day_of_death,
                "is_alive": user_obj.is_alive,
                "gender": user_obj.gender,
                "power_ranking": user_obj.power_ranking,
                "position": user_obj.position - ranking_adjust,
                "position_percentage": user_obj.position_percentage,
                "grade_over_20": user_obj.grade_over_20,
                "first_char_of_the_page": user_obj.first_char_of_the_page,
                "wikipedia_page_length": user_obj.wikipedia_page_lenght,
                "all_links_of_a_page": user_obj.all_links_of_a_page[0:5],
                "number_of_links": user_obj.number_of_links,
                "preciseness_level": user_obj.preciseness_level,
                "number_of_user_who_have_linked_this_user":user_obj.number_of_user_who_have_linked_this_user,
                "list_of_page_name_linked_sorted":user_obj.list_of_page_name_linked_sorted[0:5],
                "list_of_friend_of_user":user_obj.list_of_friend_of_user[0:5],
                "number_of_friends":user_obj.number_of_friends,
                "list_of_unpreciseness_data": list_of_unpreciseness_data,
                "number_of_unpreciseness_date":len(list_of_unpreciseness_data),
                "number_of_views":user_obj.number_of_views,
                "country_birth_place_emoji": birth_place_emoji,
                "country_death_place_emoji": death_place_emoji,
                "century_of_birth":user_obj.century_of_birth,
                "century_of_death":user_obj.century_of_death,
                "update_level":update_level,
                            
            }
            #user_obj.number_of_views += 1
            
            user_obj.save()
            for key , value in user_info_dict.items():
                if type(value) != list and type(value) != int and type(value) != bool and type(value) != float:
                    if value.lower() == "undefined":
                        user_info_dict[key] = "Indéfini(e)"    
            return JsonResponse(user_info_dict,status=200)

        
        user_info_dict = {
            "page_name": "personne",
            "page_url": "https://fr.wikipedia.org/wiki/Personne",
            "picture_url": "https://res.cloudinary.com/dtwkfeqz3/image/upload/v1790973930/1955-futurama-bender_pxvpaj.jpg",
            "first_name": "personne",
            "first_name_standard": "personne",
            "last_name": "personne",
            "last_name_standard": "personne",
            "job": "personne",
            "town_birth_place": "personne",
            "town_birth_place_href": "personne",
            "birth_town_localisation": dms_to_decimal("blabla"),
            "country_birth_place": "personne",
            "time_period_of_birth": "personne",
            "continent_of_birth": "personne",
            "region_of_birth": "personne",
            "birth_date": "personne",
            "birth_year": "personne",
            "birth_month": "personne",
            "birth_day": "personne",
            "birth_month_day": "personne",
            "town_death_place": "personne",
            "town_death_place_href": "personne",
            "town_death_localisation": "personne",
            "country_death_place": "personne",
            "continent_of_death": "personne",
            "region_of_death": "personne",
            "born_and_died_in_the_same_town": "personne",
            "born_and_died_in_the_same_country": "personne",
            "born_and_died_in_the_same_continent": "personne",
            "born_and_died_in_the_same_region": "personne",
            "death_date": "personne",
            "death_year": "personne",
            "death_month": "personne",
            "death_day": "personne",
            "death_month_day": "personne",
            "born_before_christ": "personne",
            "died_before_christ": "personne",
            "born_and_died_before_christ": "personne",
            "born_and_died_after_christ": "personne",
            "born_before_christ_and_died_after_christ": "personne",
            "age": "personne",
            "is_alive": True,
            "gender": "personne",
            "power_ranking": "personne",
            "position": "personne",
            "position_percentage": "personne",
            "number_of_views":"personne",
            "grade_over_20": "personne",
            "number_of_user_who_have_linked_this_user":1,
            "first_char_of_the_page": "personne",
            "wikipedia_page_length": "personne",
            "all_links_of_a_page": ["personne"],
            "number_of_links": 1,
            "preciseness_level": "personne",
            "list_of_unpreciseness_data": ["personne"],
            "number_of_unpreciseness_date": "personne",
            "country_birth_place_emoji": "🏴‍☠️",
            "country_death_place_emoji": "🏴‍☠️",
        }
    
        return JsonResponse(user_info_dict,status=200)
 

    except Exception as e:
        print("========== ERROR ==========")
        print(type(e).__name__)
        print(repr(e))
        traceback.print_exc()
        print("============================")
        raise

    
# @ratelimit(key='ip', rate='30/m')
# def rdisplay_user_info(request,username):
#     """Display user info"""
    
#     print("USERNAME RECU :", repr(username))
#     print("USER TROUVE :", user_obj)

#     if request.method != "GET":
#         return HttpResponse(f"Error! with this {username} info", status=404)


#     if username != "Personne":
#         try:
#             user_obj = WikipediaUser.objects.filter(page_name=username.strip()).first()

            
#             page_name = user_obj.page_name
#         except:
#             return HttpResponse(f"{username} doesn't exist", status=404)

#         list_of_unpreciseness_data = []
#         if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
#             birth_place_emoji = "🏳️"
#         else:
#             birth_place_emoji = user_obj.country_birth_place_emoji

#         if user_obj.town_death_localisation == "" or user_obj.town_death_localisation.lower() == "undefined":
#             death_place_emoji = "🏳️"
#         else:
#             death_place_emoji = user_obj.country_death_place_emoji

#         for page_error in user_obj.list_of_unpreciseness_data:
#             try:
#                 list_of_unpreciseness_data.append(UNPRECISENESS_DATA_FR[page_error]+",")
#             except:
#                 list_of_unpreciseness_data.append(page_error+",")

#         ranking_adjust = 0
#         if username != "Gaston Cougny":
#             ranking_adjust = 1
#         # if username == "Jésus de Nazareth":
#         #     user_obj.power_ranking = 1197
#         #     user_obj.position = 338
#         #     user_obj.position_percentage = 0.05043
#         #     user_obj.grade_over_20 = 19.99

#         # if username == "Anne Frank":
#         #     user_obj.power_ranking = 636
#         #     user_obj.position = 1780
#         #     user_obj.position_percentage = 0.26559
#         #     user_obj.grade_over_20 = 19.95

#         # if username == "’Anbasa ibn Suhaym al-Kalbi": 
#         #     user_obj.power_ranking = 34 
#         #     user_obj.position = 241885 
#         #     user_obj.position_percentage = 36.09 
#         #     user_obj.grade_over_20 = 12.78 
        
#         # if username == "₩uNo": 
#         #     user_obj.power_ranking = 60 
#         #     user_obj.position = 127250 
#         #     user_obj.position_percentage = 18.99 
#         #     user_obj.grade_over_20 = 16.2


        
#         user_info_dict = {
#             "page_name": page_name,
#             "page_url": user_obj.page_url,
#             "picture_url": user_obj.picture_url,
#             "first_name": user_obj.first_name,
#             "first_name_standard": user_obj.first_name_standard,
#             "last_name": user_obj.last_name,
#             "last_name_standard": user_obj.last_name_standard,
#             "job": user_obj.job,
#             "town_birth_place": user_obj.town_birth_place,
#             "town_birth_place_href": user_obj.town_birth_place_href,
#             "birth_town_localisation": user_obj.birth_town_localisation,
#             "country_birth_place": user_obj.country_birth_place,
#             "time_period_of_birth": HISTORICAL_PERIODS_DICT_TO_FRENCH[user_obj.time_period_of_birth],
#             "continent_of_birth": user_obj.continent_of_birth,
#             "region_of_birth": user_obj.region_of_birth,
#             "birth_date": user_obj.birth_date,
#             "birth_year": user_obj.birth_year,
#             "birth_month": user_obj.birth_month,
#             "birth_day": user_obj.birth_day,
#             "birth_month_day": user_obj.birth_month_day,
#             "town_death_place": user_obj.town_death_place,
#             "town_death_place_href": user_obj.town_death_place_href,
#             "town_death_localisation": user_obj.town_death_localisation,
#             "country_death_place": user_obj.country_death_place,
#             "continent_of_death": user_obj.continent_of_death,
#             "region_of_death": user_obj.region_of_death,
#             "born_and_died_in_the_same_town": user_obj.born_and_died_in_the_same_town,
#             "born_and_died_in_the_same_country": user_obj.born_and_died_in_the_same_country,
#             "born_and_died_in_the_same_continent": user_obj.born_and_died_in_the_same_continent,
#             "born_and_died_in_the_same_region": user_obj.born_and_died_in_the_same_region,
#             "death_date": user_obj.death_date,
#             "death_year": user_obj.death_year,
#             "death_month": user_obj.death_month,
#             "death_day": user_obj.death_day,
#             "death_month_day": user_obj.death_month_day,
#             "cause_of_death":user_obj.cause_of_death,
#             "is_cause_of_death_known":user_obj.is_cause_of_death_known,
#             "born_before_christ": user_obj.born_before_christ,
#             "died_before_christ": user_obj.died_before_christ,
#             "born_and_died_before_christ": user_obj.born_and_died_before_christ,
#             "born_and_died_after_christ": user_obj.born_and_died_after_christ,
#             "born_before_christ_and_died_after_christ": user_obj.born_before_christ_and_died_after_christ,
#             "age": user_obj.age,
#             "week_day_of_birth":user_obj.week_day_of_birth,
#             "week_day_of_death":user_obj.week_day_of_death,
#             "is_alive": user_obj.is_alive,
#             "gender": user_obj.gender,
#             "power_ranking": user_obj.power_ranking,
#             "position": user_obj.position - ranking_adjust,
#             "position_percentage": user_obj.position_percentage,
#             "grade_over_20": user_obj.grade_over_20,
#             "first_char_of_the_page": user_obj.first_char_of_the_page,
#             "wikipedia_page_length": user_obj.wikipedia_page_lenght,
#             "all_links_of_a_page": user_obj.all_links_of_a_page[0:5],
#             "number_of_links": user_obj.number_of_links,
#             "preciseness_level": user_obj.preciseness_level,
#             "number_of_user_who_have_linked_this_user":user_obj.number_of_user_who_have_linked_this_user,
#             "list_of_page_name_linked_sorted":user_obj.list_of_page_name_linked_sorted[0:5],
#             "list_of_friend_of_user":user_obj.list_of_friend_of_user[0:5],
#             "number_of_friends":user_obj.number_of_friends,
#             "list_of_unpreciseness_data": list_of_unpreciseness_data,
#             "number_of_unpreciseness_date":len(list_of_unpreciseness_data),
#             "number_of_views":user_obj.number_of_views,
#             "country_birth_place_emoji": birth_place_emoji,
#             "country_death_place_emoji": death_place_emoji,
#             "century_of_birth":user_obj.century_of_birth,
#             "century_of_death":user_obj.century_of_death,
                        
#         }
#         user_obj.number_of_views += 1
#         user_obj.save()
#         for key , value in user_info_dict.items():
#             if type(value) != list and type(value) != int and type(value) != bool and type(value) != float:
#                 if value.lower() == "undefined":
#                     user_info_dict[key] = "Indéfini(e)"

#         return JsonResponse(user_info_dict,status=200)
    
        

#     if username == "Personne":
        
#         user_info_dict = {
#             "page_name": "personne",
#             "page_url": "https://fr.wikipedia.org/wiki/Personne",
#             "picture_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/960px-Question_mark_%28black%29.svg.png?utm_source=fr.wikipedia.org&utm_campaign=index&utm_content=thumbnail",
#             "first_name": "personne",
#             "first_name_standard": "personne",
#             "last_name": "personne",
#             "last_name_standard": "personne",
#             "job": "personne",
#             "town_birth_place": "personne",
#             "town_birth_place_href": "personne",
#             "birth_town_localisation": dms_to_decimal("blabla"),
#             "country_birth_place": "personne",
#             "time_period_of_birth": "personne",
#             "continent_of_birth": "personne",
#             "region_of_birth": "personne",
#             "birth_date": "personne",
#             "birth_year": "personne",
#             "birth_month": "personne",
#             "birth_day": "personne",
#             "birth_month_day": "personne",
#             "town_death_place": "personne",
#             "town_death_place_href": "personne",
#             "town_death_localisation": "personne",
#             "country_death_place": "personne",
#             "continent_of_death": "personne",
#             "region_of_death": "personne",
#             "born_and_died_in_the_same_town": "personne",
#             "born_and_died_in_the_same_country": "personne",
#             "born_and_died_in_the_same_continent": "personne",
#             "born_and_died_in_the_same_region": "personne",
#             "death_date": "personne",
#             "death_year": "personne",
#             "death_month": "personne",
#             "death_day": "personne",
#             "death_month_day": "personne",
#             "born_before_christ": "personne",
#             "died_before_christ": "personne",
#             "born_and_died_before_christ": "personne",
#             "born_and_died_after_christ": "personne",
#             "born_before_christ_and_died_after_christ": "personne",
#             "age": "personne",
#             "is_alive": True,
#             "gender": "personne",
#             "power_ranking": "personne",
#             "position": "personne",
#             "position_percentage": "personne",
#             "number_of_views":"personne",
#             "grade_over_20": "personne",
#             "number_of_user_who_have_linked_this_user":1,
#             "first_char_of_the_page": "personne",
#             "wikipedia_page_length": "personne",
#             "all_links_of_a_page": ["personne"],
#             "number_of_links": 1,
#             "preciseness_level": "personne",
#             "list_of_unpreciseness_data": ["personne"],
#             "number_of_unpreciseness_date": "personne",
#             "country_birth_place_emoji": "🏴‍☠️",
#             "country_death_place_emoji": "🏴‍☠️",
#         }
#         return JsonResponse(user_info_dict,status=200)

 

