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

            wiki_user = WikipediaUser(
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
            # import traceback
            # traceback.print_exc()
            # # continue
            
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
 
    

@ratelimit(key='ip', rate='10/m')
def display_chunck_of_user_info(request,chunk_nb=0):
    
    """Display chunck (10000 users) of user info"""
    
    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)

    all_user_obj = WikipediaUser.objects.all().order_by("position").filter(position__gte=0)

    #all_user_obj = WikipediaUser.objects.filter(number_of_user_who_have_linked_this_user=0,position__gte=0,position__lte=35000).order_by("position")
    
    
    length = all_user_obj.count()
    
    random_number_list = []
    if chunk_nb == 999999999:
        random_number = randint(0,NUMBER_OF_USER-501)
        all_user_obj = WikipediaUser.objects.filter(position__gte=random_number-500,position__lte=random_number)
        chunk_nb = 0
    #print(random_number)
    list_of_all_user_data =  []
    nb = NUMBER_OF_USERS_TO_SEARCH
    index_start = (chunk_nb * nb)
    
    index_end = (chunk_nb + 1) * nb

    
    list_of_localisation = []
    for user_obj in all_user_obj[index_start:index_end]:
        try:
            # if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
            #     continue

            # if dms_to_decimal(user_obj.birth_town_localisation) in list_of_localisation:
            #     continue
            
            list_of_localisation.append(dms_to_decimal(user_obj.birth_town_localisation,user_obj.page_name))
            if len(user_obj.page_name) > 35:
                page_name_shorter = user_obj.page_name[0:35]+"..."
            else:
                page_name_shorter = user_obj.page_name

            user_info_dict = {
                "page_name": user_obj.page_name,
                "page_name_shorter":page_name_shorter,
                "page_url": user_obj.page_url,
                "gender":user_obj.gender,
                "is_alive":str(user_obj.is_alive),
                "picture_url": user_obj.picture_url,
                #"birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),
                "birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),   
                "birth_country_name":user_obj.country_birth_place,           
                "town_death_localisation": dms_to_decimal(user_obj.town_death_localisation),
                "country_birth_place_emoji":user_obj.country_birth_place_emoji,
                "page_nb":chunk_nb,
                "number_of_element":length
            }
            list_of_all_user_data.append(user_info_dict)
        except:

            pass

    return JsonResponse({"all_user_data":list_of_all_user_data},status=200)


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
                    "country_birth_place": recieved_data["country_of_birth"][0:-3].replace("-"," ").lower()
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
        filters["age__lte"] = MAXIMUM_AGE_TO_DISPLAY
                
        
    
    if "birth_year" in recieved_data:
        if "time_period_of_birth" in recieved_data:
            if len(recieved_data["time_period_of_birth"]) != 0 and recieved_data["time_period_of_birth"] in HISTORICAL_PERIODS_WITH_DATE:
               pass 
            else:
                try:
                    if "+" in recieved_data["birth_year"]:
                        filters["birth_year__gte"] = int(recieved_data["birth_year"].replace("+",""))
                        filters["birth_year__lte"] = 2022
                        filters["age__gte"] = 0
                                                                        
                                                
                    else:
                        filters["birth_year"] = int(recieved_data["birth_year"])
                except:
                    pass
        else:
            if "+" in recieved_data["birth_year"]:
                filters["birth_year__gte"] = int(recieved_data["birth_year"].replace("+",""))
                filters["birth_year__lte"] = 2022
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
            if recieved_data["time_period_of_birth"] != "Antiquité -3300-475":
                filters["age__gte"] = -998
                                        
        if recieved_data["time_period_of_birth"] == "Indéfinie":
            filters["time_period_of_birth"] = "Undefined"
            if recieved_data["time_period_of_birth"] != "Antiquité -3300-475":
                filters["age__gte"] = -998
                                
    if "first_name" in recieved_data:
        if len(recieved_data["first_name"]) != 0:
            if "+" in recieved_data["first_name"]:
                filters["first_name__icontains"] = recieved_data["first_name"].replace("+","").lower()
            else:
                filters["first_name"] = recieved_data["first_name"].lower()

    if "last_name" in recieved_data:
        if len(recieved_data["last_name"]) != 0:
            if "+" in recieved_data["last_name"]:
                filters["last_name__icontains"] = recieved_data["last_name"].replace("+","").lower()
            else:
                filters["last_name"] = recieved_data["last_name"].lower()

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
        if len(recieved_data["birth_month_day"]) != "0":
            filters["birth_month_day"] = recieved_data["birth_month_day"]

    if "death_month_day" in recieved_data:
        if len(recieved_data["death_month_day"]) != "0":
            filters["death_month_day"] = recieved_data["death_month_day"]
            display_only_death_localisation = True
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
            filters["position__lte"] = int(recieved_data["latest_position_of_user_to_display"])
        filters["position__gte"] = -1

            #sort_user_by = recieved_data["sort_user_by"]
        
                
    filters["birth_town_localisation__icontains"] = " "
    filters["position__gte"] = 0
    if "born_before_christ" in recieved_data:
        if recieved_data["born_before_christ"] == "oui":
            filters["born_before_christ"] = True
        if recieved_data["born_before_christ"] == "non":
            filters["born_before_christ"] = False
    


     
    #filters["age__lte"] = 123
            
    print(recieved_data)
    print(filters)

        
    if accept_multiple_element:
        all_user_obj = WikipediaUser.objects.filter(query,**filters)
    else:
        all_user_obj = WikipediaUser.objects.filter(**filters)

    # if accept_multiple_element:
    #     all_user_obj = WikipediaUser.objects.filter(query,**filters).order_by("-wikipedia_page_lenght")
    # else:
    #     all_user_obj = WikipediaUser.objects.filter(**filters).order_by("-wikipedia_page_lenght")

    list_of_all_user_data =  []
    
    list_of_localisation = []
    user_info_dict = {}
    number_of_people_to_display = 5000000000
    for user_obj in all_user_obj[0:NUMBER_OF_USER + 1]:
        try:
            
            # if (user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined") and display_people_with_no_localisation  is False:
            #     #nb_of_bad_user+=1
            #     continue
            
            if len(list_of_all_user_data) >= number_of_people_to_display:
                break
            
            list_of_localisation.append(dms_to_decimal(user_obj.birth_town_localisation,user_obj.page_name))

            
            # print(display_death_localisation)
            if display_only_death_localisation is False:
                list_of_all_user_data.append(dms_to_decimal(user_obj.birth_town_localisation,"__qjis__"))
            else:
                list_of_all_user_data.append(dms_to_decimal("blablobla"))
                         
            if display_death_localisation or display_only_death_localisation:
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
    return HttpResponse("OK!",status=200)


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
