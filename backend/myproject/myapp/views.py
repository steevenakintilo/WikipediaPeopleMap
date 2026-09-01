from unidecode import unidecode
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from myapp.models import WikipediaUser

from random import randint

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
    """Add Wikipedia users from the file to the database."""

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
            if type(birth_year) != int:
                birth_year = 123456789
            if type(death_year) != int:
                death_year_year = 123456789
            if line.get("age") == -999:
                is_alive = False
            else:
                is_alive = line.get("is_alive",True)     
            wiki_user = WikipediaUser(
                page_name=line["page_name"],
                page_url=line["page_url"],
                picture_url=line.get("picture_url"),

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
                is_alive=line.get("is_alive", True),

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
            continue

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
            user_obj = WikipediaUser.objects.filter(page_name=username).first()
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
            "born_before_christ": user_obj.born_before_christ,
            "died_before_christ": user_obj.died_before_christ,
            "born_and_died_before_christ": user_obj.born_and_died_before_christ,
            "born_and_died_after_christ": user_obj.born_and_died_after_christ,
            "born_before_christ_and_died_after_christ": user_obj.born_before_christ_and_died_after_christ,
            "age": user_obj.age,
            "is_alive": user_obj.is_alive,
            "gender": user_obj.gender,
            "power_ranking": user_obj.power_ranking,
            "position": user_obj.position,
            "position_percentage": user_obj.position_percentage,
            "grade_over_20": user_obj.grade_over_20,
            "first_char_of_the_page": user_obj.first_char_of_the_page,
            "wikipedia_page_length": user_obj.wikipedia_page_lenght,
            "all_links_of_a_page": user_obj.all_links_of_a_page,
            "number_of_links": user_obj.number_of_links,
            "preciseness_level": user_obj.preciseness_level,
            "list_of_unpreciseness_data": list_of_unpreciseness_data,
            "number_of_unpreciseness_date":len(list_of_unpreciseness_data),
            "country_birth_place_emoji": birth_place_emoji,
            "country_death_place_emoji": death_place_emoji,
        }
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
            "first_char_of_the_page": "personne",
            "wikipedia_page_length": "personne",
            "all_links_of_a_page": "personne",
            "number_of_links": "personne",
            "preciseness_level": "personne",
            "list_of_unpreciseness_data": "personne",
            "number_of_unpreciseness_date": "personne",
            "country_birth_place_emoji": "🏴‍☠️",
            "country_death_place_emoji": "🏴‍☠️",
        }
        return JsonResponse(user_info_dict,status=200)
 
    

def display_chunck_of_user_info(request,chunk_nb=0):
    """Display chunck (10000 users) of user info"""
    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)


    all_user_obj = WikipediaUser.objects.all()
    list_of_all_user_data =  []
    nb = NUMBER_OF_USERS_TO_SEARCH
    index_start = chunk_nb * nb
    index_end = (chunk_nb + 1) * nb
    list_of_localisation = []
    for user_obj in all_user_obj[index_start:index_end]:
        try:
            # if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
            #     continue

            # if dms_to_decimal(user_obj.birth_town_localisation) in list_of_localisation:
            #     continue
            
            
            list_of_localisation.append(dms_to_decimal(user_obj.birth_town_localisation,user_obj.page_name))
            user_info_dict = {
                "page_name": user_obj.page_name,
                "page_url": user_obj.page_url,
                "gender":user_obj.gender,
                "is_alive":str(user_obj.is_alive),
                "picture_url": user_obj.picture_url,
                #"birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),
                "birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),   
                "birth_country_name":user_obj.country_birth_place,           
                "town_death_localisation": dms_to_decimal(user_obj.town_death_localisation),
                "country_birth_place_emoji":user_obj.country_birth_place_emoji
            }
            list_of_all_user_data.append(user_info_dict)
        except:

            pass

    return JsonResponse({"all_user_data":list_of_all_user_data},status=200)


@csrf_exempt
def display_chunck_of_user_info_advanced_search(request,chunk_nb=0):
    """Display chunck (10000 users) of user info"""
    if request.method != "POST":
        return HttpResponse(f"Error!", status=404)



    recieved_data = json.loads(request.body)
        

    #all_user_obj = WikipediaUser.objects.all()

    # all_user_obj = WikipediaUser.objects.filter(
    #     gender__icontains="Woman"
    # )

    # all_user_obj = WikipediaUser.objects.filter(
    #     country_birth_place__icontains="palestine",
    #     country_death_place__icontains="palestine"
    # )

    # all_user_obj = WikipediaUser.objects.filter(
    #     Q(country_birth_place__icontains="palestine") |
    #     Q(country_death_place__icontains="palestine")
    # )



    # if recieved_data["country_of_birth"] != "" and recieved_data["country_of_birth"] != "Pays de naissance":
    #     filters = {
    #         "country_birth_place__icontains": recieved_data["country_of_birth"][0:-3]
    #     }

    #     all_user_obj = WikipediaUser.objects.filter(
    #         country_birth_place__icontains=recieved_data["country_of_birth"][0:-3]
    #     )
    # else:
    #     all_user_obj = WikipediaUser.objects.all()[:1000]

    basic_search = True
    try:

        list_of_key_to_remove = []
        for key,value in recieved_data.items():
            if value == '':
                list_of_key_to_remove.append(key)

        for key in list_of_key_to_remove:
            recieved_data.pop(key)
    except:
        pass
    try:
        if recieved_data["country_of_birth"] != "" and recieved_data["country_of_birth"] != "Pays de naissance" and "Tous les pays" not in recieved_data["country_of_birth"]:

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

    if "alive_status" in recieved_data:
        if recieved_data["alive_status"] == "Mort":
            filters["is_alive"] = False
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

    if "job" in recieved_data:
        filters["job__icontains"] = unidecode(recieved_data["job"])

    if "time_period_of_birth" in recieved_data:
        if len(recieved_data["time_period_of_birth"]) != 0 and recieved_data["time_period_of_birth"] in HISTORICAL_PERIODS_WITH_DATE:
            filters["time_period_of_birth"] = HISTORICAL_PERIODS_DICT[recieved_data["time_period_of_birth"]]


    if "first_name" in recieved_data:
        if len(recieved_data["first_name"]) != 0:
            if "+" in recieved_data["first_name"]:
                filters["first_name__icontains"] = recieved_data["first_name"].replace("+","")
            else:
                filters["first_name"] = recieved_data["first_name"]

    if "last_name" in recieved_data:
        if len(recieved_data["last_name"]) != 0:
            if "+" in recieved_data["last_name"]:
                filters["last_name__icontains"] = recieved_data["last_name"].replace("+","")
            else:
                filters["last_name"] = recieved_data["last_name"]

    print(recieved_data)
    if "town_birth_place" in recieved_data:
        print("opop")
        filters["town_birth_place__icontains"] = unidecode(recieved_data["town_birth_place"])

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


    display_people_with_no_localisation = False
    if "display_people_with_no_localisation" in recieved_data:
        if recieved_data["display_people_with_no_localisation"] == "oui":
            display_people_with_no_localisation = True 
    if filters != {}:
        basic_search = False

    print(recieved_data)
    print(filters)
    all_user_obj = WikipediaUser.objects.filter(**filters)
     
    list_of_all_user_data =  []
    nb = NUMBER_OF_USERS_TO_SEARCH * 2
    index_start = chunk_nb * nb
    index_end = (chunk_nb + 1) * nb
    list_of_localisation = []
    for user_obj in all_user_obj[index_start:index_end]:
        try:
            
            if (user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined") and display_people_with_no_localisation  is False:
                continue

            if len(list_of_all_user_data) >= number_of_people_to_display:
                break
            if "time_period_of_birth" in recieved_data and user_obj.age == -999:
                continue
            # if dms_to_decimal(user_obj.birth_town_localisation) in list_of_localisation:
            #     continue
            
            
            list_of_localisation.append(dms_to_decimal(user_obj.birth_town_localisation,user_obj.page_name))

            if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
                birth_place_emoji = "🏳️"
            else:
                birth_place_emoji = user_obj.country_birth_place_emoji
            user_info_dict = {
                "page_name": user_obj.page_name,
                "page_url": user_obj.page_url,
                "gender":user_obj.gender,
                "is_alive":str(user_obj.is_alive),
                "picture_url": user_obj.picture_url,
                #"birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),
                "birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),   
                "birth_country_name":user_obj.country_birth_place,                      
                #"town_death_localisation": dms_to_decimal(user_obj.town_death_localisation),
                "country_birth_place_emoji":birth_place_emoji
            }
            list_of_all_user_data.append(user_info_dict)
        except:
            pass
    if len(list_of_all_user_data) == 0:
        user_info_dict = {
            "page_name": "Personne",
            "page_url": "https://fr.wikipedia.org/wiki/Personne",
            "gender":"Unknown",
            "is_alive":True,
            "picture_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_%28black%29.svg/960px-Question_mark_%28black%29.svg.png?utm_source=fr.wikipedia.org&utm_campaign=index&utm_content=thumbnail",
            #"birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),
            "birth_town_localisation": dms_to_decimal("blabla"),              
            "country_birth_place_emoji":"🏴‍☠️"
        }
        list_of_all_user_data.append(user_info_dict)
    return JsonResponse({"all_user_data":list_of_all_user_data},status=200)


def display_chunck_user_birth_town_localisation_qjis(request,chunk_nb=0):
    """Display chunck (10000 users) of user birth town localisation"""
    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)

    all_user_obj = WikipediaUser.objects.all()

    # all_user_obj = WikipediaUser.objects.filter(
    #     first_name_standard="aurelia"
    # )

    # all_user_obj = WikipediaUser.objects.filter(
    #     continent_of_birth="Afrique"
    # )
      
    list_of_all_user_data =  []
    nb = NUMBER_OF_USER + 1
    index_start = chunk_nb * nb
    index_end = (chunk_nb + 1) * nb
    for user_obj in all_user_obj[0:nb]:
        try:
            if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
                continue
            list_of_all_user_data.append(dms_to_decimal(user_obj.birth_town_localisation))
            if dms_to_decimal(user_obj.town_death_localisation) != (-999, -999):
                list_of_all_user_data.append(dms_to_decimal(user_obj.town_death_localisation))
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

def display_chunck_of_user_info2(request,chunk_nb=0):
    """Display chunck (10000 users) of user info"""
    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)

    all_user_obj = WikipediaUser.objects.all()
    list_of_all_user_data =  []
    nb = 100000
    index_start = chunk_nb * nb
    index_end = (chunk_nb + 1) * nb
    list_of_unpreciseness_data = []
    for user_obj in all_user_obj[index_start:index_end]:
        try:
            if user_obj.birth_town_localisation == "" or user_obj.birth_town_localisation.lower() == "undefined":
                continue


            user_info_dict = {
                "page_name": user_obj.page_name,
                "page_url": user_obj.page_url,
                "picture_url": user_obj.picture_url,
                "first_name": user_obj.first_name,
                "first_name_standard": user_obj.first_name_standard,
                "last_name": user_obj.last_name,
                "last_name_standard": user_obj.last_name_standard,
                "job": user_obj.job,
                "town_birth_place": user_obj.town_birth_place,
                "town_birth_place_href": user_obj.town_birth_place_href,
                "birth_town_localisation": dms_to_decimal(user_obj.birth_town_localisation),
                "country_birth_place": user_obj.country_birth_place,
                "time_period_of_birth": user_obj.time_period_of_birth,
                "continent_of_birth": user_obj.continent_of_birth,
                "region_of_birth": user_obj.region_of_birth,
                "birth_date": user_obj.birth_date,
                "birth_year": user_obj.birth_year,
                "birth_month": user_obj.birth_month,
                "birth_day": user_obj.birth_day,
                "birth_month_day": user_obj.birth_month_day,
                "town_death_place": user_obj.town_death_place,
                "town_death_place_href": user_obj.town_death_place_href,
                "town_death_localisation": dms_to_decimal(user_obj.town_death_localisation),
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
                "born_before_christ": user_obj.born_before_christ,
                "died_before_christ": user_obj.died_before_christ,
                "born_and_died_before_christ": user_obj.born_and_died_before_christ,
                "born_and_died_after_christ": user_obj.born_and_died_after_christ,
                "born_before_christ_and_died_after_christ": user_obj.born_before_christ_and_died_after_christ,
                "age": user_obj.age,
                "is_alive": user_obj.is_alive,
                "gender": user_obj.gender,
                "power_ranking": user_obj.power_ranking,
                "position": user_obj.position,
                "position_percentage": user_obj.position_percentage,
                "grade_over_20": user_obj.grade_over_20,
                "first_char_of_the_page": user_obj.first_char_of_the_page,
                "wikipedia_page_length": user_obj.wikipedia_page_lenght,
                "all_links_of_a_page": user_obj.all_links_of_a_page,
                "number_of_links": user_obj.number_of_links,
                "preciseness_level": user_obj.preciseness_level,
                "list_of_unpreciseness_data": list_of_unpreciseness_data,
                "number_of_unpreciseness_date":len(list_of_unpreciseness_data),
                "country_birth_place_emoji": user_obj.country_birth_place_emoji,
                "country_death_place_emoji": user_obj.country_death_place_emoji,
            }
            list_of_all_user_data.append(user_info_dict)
        except:
            pass
    return JsonResponse({"all_user_data":list_of_all_user_data},status=200)
