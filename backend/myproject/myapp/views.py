from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import WikipediaUser

from .global_variable import *
from .utility_function  import *


import ast
import os

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
            wiki_user = WikipediaUser(
                page_name=line["page_name"],
                page_url=line["page_url"],
                picture_url=line.get("picture_url"),

                first_name=line.get("first_name"),
                first_name_standard=line.get("first_name_standard"),

                last_name=line.get("last_name"),
                last_name_standard=line.get("last_name_standard"),

                job=line.get("job"),

                # Birth information
                town_birth_place=line.get("town_birth_place"),
                town_birth_place_href=line.get("town_birth_place_href"),
                birth_town_localisation=line.get("birth_town_localisation"),
                country_birth_place=line.get("country_birth_place"),
                time_period_of_birth=line.get("time_period_of_birth"),
                continent_of_birth=line.get("continent_of_birth"),
                region_of_birth=line.get("region_of_birth"),

                birth_date=str(line.get("birth_date")),
                birth_year=str(line.get("birth_year")),
                birth_month=str(line.get("birth_month")),
                birth_day=str(line.get("birth_day")),
                birth_month_day=str(line.get("birth_month_day")),

                # Death information
                town_death_place=line.get("town_death_place"),
                town_death_place_href=line.get("town_death_place_href"),
                town_death_localisation=line.get("town_death_localisation"),
                country_death_place=line.get("country_death_place"),
                continent_of_death=line.get("continent_of_death"),
                region_of_death=line.get("region_of_death"),

                death_date=str(line.get("death_date")),
                death_year=str(line.get("death_year")),
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
                    "wikipedia_page_lenght", 0
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

    try:
        user_obj = WikipediaUser.objects.filter(page_name=username).first()
        page_name = user_obj.page_name
    except:
        return HttpResponse(f"{username} doesn't exist", status=404)
    
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
        "list_of_unpreciseness_data": user_obj.list_of_unpreciseness_data,
        "country_birth_place_emoji": user_obj.country_birth_place_emoji,
        "country_death_place_emoji": user_obj.country_death_place_emoji,
    }

    return JsonResponse(user_info_dict,status=200)



def display_chunck_of_user_info(request,chunk_nb=0):
    """Display chunck (10000 users) of user info"""
    if request.method != "GET":
        return HttpResponse(f"Error!", status=404)

    all_user_obj = WikipediaUser.objects.all()
    list_of_all_user_data =  []

    index_start = chunk_nb * 10000
    index_end = (chunk_nb + 1) * 10000
    try:
        for user_obj in all_user_obj[index_start:index_end]:
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
                "birth_town_localisation": user_obj.birth_town_localisation,
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
                "list_of_unpreciseness_data": user_obj.list_of_unpreciseness_data,
                "country_birth_place_emoji": user_obj.country_birth_place_emoji,
                "country_death_place_emoji": user_obj.country_death_place_emoji,
            }
            list_of_all_user_data.append(user_info_dict)
    except:
        print("error blabla")
    return JsonResponse({"all_user_data":list_of_all_user_data},status=200)
