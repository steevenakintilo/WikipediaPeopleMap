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
def hi():
    return HttpResponse("Hi!")


@csrf_exempt
def add_a_wikipedia_user_to_the_database(request):
    """Add Wikipedia users to the database."""

    if request.method != "POST":
        return HttpResponse("Error!", status=404)

    user_data_dict = print_file_content(USER_DICT_FILE_PATH).split("\n")

    for i , user in enumerate(user_data_dict):
        try:
            line = ast.literal_eval(user)
            if i % 10000 == 0:
                print(i,line["page_name"])
            birth_year = line.get("birth_year")
            death_year = line.get("death_year")
            if line["page_name"] in USERS_TO_SKIP:
                continue
            if type(birth_year) != int:
                birth_year = 123456789
            if type(death_year) != int:
                death_year_year = 123456789
            if line.get("age") == -999:
                is_alive = False
            else:
                is_alive = line.get("is_alive",True)

            if line.get("position") == -999:
                continue

            is_cause_of_death_known_= False
            if line.get("cause_of_death") != "Unspecified" and line.get("cause_of_death") != "alive":
                is_cause_of_death_known_ = True

            try:
                age_group_nb = int(line.get("age_group")[0])
            except:
                age_group_nb = -99

            wiki_user = WikipediaUser(
                page_name=line["page_name"],
                page_url=line["page_url"],
                age_group_nb=age_group_nb,
                century_of_birth=line.get("century_of_birth"),
                century_of_death=line.get("century_of_death"),
                number_of_word_in_page_name=len(line["page_name"].split(" ")),
                picture_url=line.get("picture_url"),
                page_lenght = len(line["page_name"]),
                first_name=line.get("first_name"),
                first_name_standard=line.get("first_name_standard"),

                last_name=line.get("last_name"),
                last_name_standard=line.get("last_name_standard"),

                job=unidecode(line.get("job")),

                # Birth information
                town_birth_place=unidecode(line.get("town_birth_place")),
                town_birth_place_href=line.get("town_birth_place_href"),
                birth_town_localisation=line.get("birth_town_localisation"),
                country_birth_place=line.get("country_birth_place").lower(),
                time_period_of_birth=line.get("time_period_of_birth"),
                continent_of_birth=line.get("continent_of_birth"),
                region_of_birth=line.get("region_of_birth"),

                birth_date=str(line.get("birth_date")),
                birth_year=birth_year,
                birth_month=str(line.get("birth_month")),
                birth_day=str(line.get("birth_day")),
                birth_month_day=str(line.get("birth_month_day")),

                # Death information
                town_death_place=unidecode(line.get("town_death_place")),
                town_death_place_href=line.get("town_death_place_href"),
                town_death_localisation=line.get("town_death_localisation"),
                country_death_place=line.get("country_death_place").lower(),
                continent_of_death=line.get("continent_of_death"),
                region_of_death=line.get("region_of_death"),

                death_date=str(line.get("death_date")),
                death_year=death_year,
                death_month=str(line.get("death_month")),
                death_day=str(line.get("death_day")),
                death_month_day=str(line.get("death_month_day")),
                cause_of_death = line.get("cause_of_death"),
                is_cause_of_death_known = is_cause_of_death_known_,        
                    # cause_of_death = models.CharField(
                    #     max_length=500,
                    #     blank=True,
                    #     null=True
                    # )

                    # is_cause_of_death_known = models.BooleanField(
                    #     default=True
                    # )
                
                # Birth / death comparisons
                born_outside_france = line.get("user_birth_outside_france", "False"),

                
                died_outside_france = line.get("user_death_outside_france", "False"),
                
                born_and_died_in_the_same_town=str(
                    line.get("born_and_died_in_the_same_town", "False")
                ),

                born_and_died_in_the_same_country=str(
                    line.get("born_and_died_in_the_same_country", "False")
                ),

                born_and_died_in_the_same_continent=str(
                    line.get("born_and_died_in_the_same_continent", "False")
                ),

                born_and_died_in_the_same_region=str(
                    line.get("born_and_died_in_the_same_region", "False")
                ),

                born_before_christ=line.get(
                    "born_before_christ", False
                ),
                died_before_christ=str(
                    line.get("died_before_christ", "False")
                ),

                born_and_died_before_christ=str(
                    line.get("born_and_died_before_christ", "False")
                ),

                born_and_died_after_christ=str(
                    line.get("born_and_died_after_christ", "False")
                ),

                born_and_died_in_the_same_day=str(
                    line.get("born_and_died_on_the_same_day", "False")
                ),
                born_before_christ_and_died_after_christ=str(
                    line.get("born_before_christ_and_died_after_christ", "False")
                ),
                age=line.get("age"),
                age_group = line.get("age_group"),
                is_alive=line.get("is_alive", True),

                week_day_of_birth = line.get("week_day_of_birth"),
            
                week_day_of_death = line.get("week_day_of_death"),
                
                # Personal information
                gender=line.get("gender"),

                # Ranking
                power_ranking=line.get("power_ranking"),
                position=line.get("position"),
                position_percentage=line.get("position_percentage"),
                grade_over_20=line.get("grade_over_20"),

                # Wikipedia page analysis
                first_char_of_the_page=line.get(
                    "first_char_of_the_page"
                ),
                wikipedia_page_lenght=line.get(
                    "wikipedia_page_length", 0
                ),
                all_links_of_a_page=line.get(
                    "all_links_of_a_page", []
                ),
                number_of_links=line.get(
                    "number_of_links", 0
                ),
                number_of_user_who_have_linked_this_user=line.get("number_of_user_who_have_linked_this_user",0),

                list_of_friend_of_user=line.get(
                    "list_of_friend_of_user", []
                ),
                number_of_friends=line.get(
                    "number_of_friends", 0
                ),
                list_of_page_name_linked_sorted=line.get(
                    "list_of_page_name_linked_sorted", []
                ),
                preciseness_level=line.get(
                    "preciseness_level"
                ),
                list_of_unpreciseness_data=line.get(
                    "list_of_unpreciseness_data", []
                ),

                # Country emojis
                country_birth_place_emoji=line.get(
                    "country_birth_place_emoji"
                ),
                country_death_place_emoji=line.get(
                    "country_death_place_emoji"
                ),
                
                # Metadata
                # is_updated=line.get("is_updated", False),
                # number_of_update=line.get("number_of_update", 0),
            )

            wiki_user.save()

        except Exception as error:
            print(f"Error while adding user: {error}")
            # import traceback
            # traceback.print_exc()
            # continue
            
    return HttpResponse(
        "Users added to the database",
        status=200
    )

@csrf_exempt
def add_a_wikipedia_user_to_the_database_unique_town(request):
    """Add Wikipedia users from unique town the database."""

    if request.method != "POST":
        return HttpResponse("Error!", status=404)

    user_data_dict = print_file_content(USER_DICT_FILE_PATH).split("\n")
    list_of_localisation_birth = []
    list_of_localisation_death = []
    WikipediaUserUniqueTown.objects.all().delete()
    all_user_obj = WikipediaUser.objects.all().order_by("position").filter(position__gte=0)

    skip = False
    for i , user in enumerate(all_user_obj):
        try:
            #line = ast.literal_eval(user)
            if i % 10000 == 0:
                print(i,user.page_name)
            birth_year = user.birth_year
            death_year = user.death_year
            if type(birth_year) != int:
                birth_year = 123456789
            if type(death_year) != int:
                death_year_year = 123456789
            if user.age == -999:
                is_alive = False
            else:
                is_alive = user.is_alive


            if user.town_birth_place in list_of_localisation_birth:
                continue
            else:
                list_of_localisation_birth.append(user.town_birth_place)
            
            if user.is_alive is False:
                if user.town_death_place in list_of_localisation_death:
                    continue
                else:
                    list_of_localisation_death.append(user.town_death_place)

            is_cause_of_death_known_= False
            if user.cause_of_death != "Unspecified" and user.cause_of_death != "alive":
                is_cause_of_death_known_ = True


            try:
                age_group_nb = int(user.age_group[0])
            except:
                age_group_nb = -99

            wiki_user = WikipediaUserUniqueTown(
                page_name=user.page_name,
                page_url=user.page_url,
                age_group_nb=age_group_nb,
                century_of_birth=user.century_of_birth,
                century_of_death=user.century_of_death,
                number_of_word_in_page_name=len(user.page_name.split(" ")),
                picture_url=user.picture_url,
                page_lenght=len(user.page_name),
                first_name=user.first_name,
                first_name_standard=user.first_name_standard,

                last_name=user.last_name,
                last_name_standard=user.last_name_standard,

                job=unidecode(user.job),

                # Birth information
                town_birth_place=unidecode(user.town_birth_place),
                town_birth_place_href=user.town_birth_place_href,
                birth_town_localisation=user.birth_town_localisation,
                country_birth_place=user.country_birth_place.lower(),
                time_period_of_birth=user.time_period_of_birth,
                continent_of_birth=user.continent_of_birth,
                region_of_birth=user.region_of_birth,

                birth_date=str(user.birth_date),
                birth_year=birth_year,
                birth_month=str(user.birth_month),
                birth_day=str(user.birth_day),
                birth_month_day=str(user.birth_month_day),

                # Death information
                town_death_place=unidecode(user.town_death_place),
                town_death_place_href=user.town_death_place_href,
                town_death_localisation=user.town_death_localisation,
                country_death_place=user.country_death_place.lower(),
                continent_of_death=user.continent_of_death,
                region_of_death=user.region_of_death,

                death_date=str(user.death_date),
                death_year=death_year,
                death_month=str(user.death_month),
                death_day=str(user.death_day),
                death_month_day=str(user.death_month_day),
                cause_of_death = user.cause_of_death,
                is_cause_of_death_known = is_cause_of_death_known_,        
                born_outside_france = user.born_outside_france,                    
                died_outside_france = user.died_outside_france,
                            

                # Birth / death comparisons
                born_and_died_in_the_same_town=str(
                    user.born_and_died_in_the_same_town
                ),

                born_and_died_in_the_same_country=str(
                    user.born_and_died_in_the_same_country
                ),

                born_and_died_in_the_same_continent=str(
                    user.born_and_died_in_the_same_continent
                ),

                born_and_died_in_the_same_region=str(
                    user.born_and_died_in_the_same_region
                ),

                born_before_christ=user.born_before_christ,

                died_before_christ=str(
                    user.died_before_christ
                ),

                born_and_died_before_christ=str(
                    user.born_and_died_before_christ
                ),

                born_and_died_after_christ=str(
                    user.born_and_died_after_christ
                ),

                born_and_died_in_the_same_day=str(
                    user.born_and_died_in_the_same_day
                ),

                born_before_christ_and_died_after_christ=str(
                    user.born_before_christ_and_died_after_christ
                ),

                age=user.age,
                age_group = user.age,
                is_alive=user.is_alive,
                
                week_day_of_birth = user.week_day_of_birth,
            
                week_day_of_death = user.week_day_of_death,
                
                # Personal information
                gender=user.gender,

                # Ranking
                power_ranking=user.power_ranking,
                position=user.position,
                position_percentage=user.position_percentage,
                grade_over_20=user.grade_over_20,

                # Wikipedia page analysis
                first_char_of_the_page=user.first_char_of_the_page,
                wikipedia_page_lenght=user.wikipedia_page_lenght,
                all_links_of_a_page=user.all_links_of_a_page,
                number_of_links=user.number_of_links,
                number_of_user_who_have_linked_this_user=(
                    user.number_of_user_who_have_linked_this_user
                ),

                list_of_friend_of_user=user.list_of_friend_of_user,
                number_of_friends=user.number_of_friends,

                list_of_page_name_linked_sorted=user.list_of_page_name_linked_sorted,

                preciseness_level=user.preciseness_level,

                list_of_unpreciseness_data=user.list_of_unpreciseness_data,

                # Country emojis
                country_birth_place_emoji=user.country_birth_place_emoji,
                country_death_place_emoji=user.country_death_place_emoji,

                # Metadata
                # is_updated=user.is_updated,
                # number_of_update=user.number_of_update,
            )
            wiki_user.save()

        except Exception as error:
            print(f"Error while adding user: {error}")
        
                
            
    return HttpResponse(
        "Users added to the database",
        status=200
    )

def display_user_info(request,username):
    """Display user info"""
    if request.method != "GET":
        return HttpResponse(f"Error! with this {username} info", status=404)


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
                        
        }
        print(user_obj.number_of_views)
        user_obj.number_of_views += 1
        user_obj.save()
        for key , value in user_info_dict.items():
            if value == "Undefined":
                user_info_dict[key] = "Indéfini"
        
        return JsonResponse(user_info_dict,status=200)
    
        

    if username == "Personne":
        
        user_info_dict = {
            "page_name": "personne",
            "page_url": "https://fr.wikipedia.org/wiki/Personne",
            "picture_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/960px-Question_mark_%28black%29.svg.png?utm_source=fr.wikipedia.org&utm_campaign=index&utm_content=thumbnail",
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
            "grade_over_20": "personne",
            "number_of_user_who_have_linked_this_user":1,
            "first_char_of_the_page": "personne",
            "wikipedia_page_length": "personne",
            "all_links_of_a_page": ["personne"],
            "number_of_links": 1,
            "preciseness_level": "personne",
            "list_of_unpreciseness_data": "personne",
            "number_of_unpreciseness_date": "personne",
            "country_birth_place_emoji": "🏴‍☠️",
            "country_death_place_emoji": "🏴‍☠️",
        }
        return JsonResponse(user_info_dict,status=200)
 
    

# @csrf_exempt
# @ratelimit(key='ip', rate='10/m')
# def edit_a_profile(request,username=0):
#     if request.method == "PUT":
#         user_obj = WikipediaUser.objects.filter(page_name=username).first()
#         page_name = user_obj.page_name
#         user_obj.page_name = "Dicaprio"
#         user_obj.position = 2962
#         user_obj.save()
#         return HttpResponse("Change Done",status=200)
#     else:
#         return HttpResponse("Request error",status=404)
