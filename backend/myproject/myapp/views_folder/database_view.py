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

from ..global_variable import *
from ..utility_function  import *


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
                death_year = 123456789
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
                town_birth_place=unidecode(line.get("town_birth_place").replace("-"," ")),
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
                town_death_place=unidecode(line.get("town_death_place").replace("-"," ")),
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
                death_year = 123456789
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
                town_birth_place=unidecode(user.town_birth_place).replace("-"," "),
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
                town_death_place=unidecode(user.town_death_place).replace("-"," "),
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


@csrf_exempt
def update_all_wikipedia_user(request):
    """Update all Wikipedia users in batches."""

    if request.method != "POST":
        return HttpResponse("Error!", status=404)

    BATCH_SIZE = 1500

    user_data_dict = print_file_content(
        USER_DICT_FILE_PATH
    ).split("\n")

    fields_to_update = [
        # General information
        "page_url",
        "age_group_nb",
        "century_of_birth",
        "century_of_death",
        "number_of_word_in_page_name",
        "picture_url",
        "page_lenght",
        "first_name",
        "first_name_standard",
        "last_name",
        "last_name_standard",
        "job",

        # Birth information
        "town_birth_place",
        "town_birth_place_href",
        "birth_town_localisation",
        "country_birth_place",
        "time_period_of_birth",
        "continent_of_birth",
        "region_of_birth",
        "birth_date",
        "birth_year",
        "birth_month",
        "birth_day",
        "birth_month_day",

        # Death information
        "town_death_place",
        "town_death_place_href",
        "town_death_localisation",
        "country_death_place",
        "continent_of_death",
        "region_of_death",
        "death_date",
        "death_year",
        "death_month",
        "death_day",
        "death_month_day",
        "cause_of_death",
        "is_cause_of_death_known",

        # Birth / death comparisons
        "born_outside_france",
        "died_outside_france",
        "born_and_died_in_the_same_town",
        "born_and_died_in_the_same_country",
        "born_and_died_in_the_same_continent",
        "born_and_died_in_the_same_region",
        "born_before_christ",
        "died_before_christ",
        "born_and_died_before_christ",
        "born_and_died_after_christ",
        "born_and_died_in_the_same_day",
        "born_before_christ_and_died_after_christ",

        # Age
        "age",
        "age_group",
        "is_alive",
        "week_day_of_birth",
        "week_day_of_death",

        # Personal information
        "gender",

        # Ranking
        "power_ranking",
        "position",
        "position_percentage",
        "grade_over_20",

        # Wikipedia page analysis
        "first_char_of_the_page",
        "wikipedia_page_lenght",
        "all_links_of_a_page",
        "number_of_links",
        "number_of_user_who_have_linked_this_user",
        "list_of_friend_of_user",
        "number_of_friends",
        "list_of_page_name_linked_sorted",
        "preciseness_level",
        "list_of_unpreciseness_data",

        # Country emojis
        "country_birth_place_emoji",
        "country_death_place_emoji",

        # Metadata
        "number_of_views",
    ]

    total_users = len(user_data_dict)
    total_updated = 0
    total_skipped = 0
    total_errors = 0

    # ---------------------------------------------------------
    # Process the file in batches
    # ---------------------------------------------------------

    for batch_start in range(0, total_users, BATCH_SIZE):

        batch_lines = user_data_dict[
            batch_start:batch_start + BATCH_SIZE
        ]

        parsed_lines = []
        page_names = []

        # -----------------------------------------------------
        # Parse current batch
        # -----------------------------------------------------

        for offset, user in enumerate(batch_lines):

            i = batch_start + offset

            try:
                line = ast.literal_eval(user)

                if i % 10000 == 0:
                    print(
                        f"{i}/{total_users} - "
                        f"{line.get('page_name')}"
                    )

                page_name = line.get("page_name")

                if not page_name:
                    total_skipped += 1
                    continue

                if page_name in USERS_TO_SKIP:
                    total_skipped += 1
                    continue

                if line.get("position") == -999:
                    total_skipped += 1
                    continue

                parsed_lines.append(line)
                page_names.append(page_name)

            except Exception as error:
                total_errors += 1

                print(
                    f"Error parsing user {i}: {error}"
                )
                print(user)
                print("----")

        if not page_names:
            continue

        # -----------------------------------------------------
        # ONE SELECT for the entire batch
        # -----------------------------------------------------

        users_by_page_name = {
            user.page_name: user
            for user in WikipediaUser.objects.filter(
                page_name__in=page_names
            )
        }

        users_to_update = []

        # -----------------------------------------------------
        # Update objects in memory
        # -----------------------------------------------------

        for line in parsed_lines:

            try:
                page_name = line["page_name"]

                user_obj = users_by_page_name.get(page_name)

                if user_obj is None:
                    total_skipped += 1
                    continue

                # -------------------------------------------------
                # Birth / death years
                # -------------------------------------------------

                birth_year = line.get("birth_year")
                death_year = line.get("death_year")

                if type(birth_year) != int:
                    birth_year = 123456789

                if type(death_year) != int:
                    death_year = 123456789

                # -------------------------------------------------
                # Cause of death
                # -------------------------------------------------

                is_cause_of_death_known_ = False

                if (
                    line.get("cause_of_death") != "Unspecified"
                    and line.get("cause_of_death") != "alive"
                ):
                    is_cause_of_death_known_ = True

                # -------------------------------------------------
                # Age group
                # -------------------------------------------------

                try:
                    age_group = line.get("age_group")

                    if age_group:
                        age_group_nb = int(age_group[0])
                    else:
                        age_group_nb = -99

                except (ValueError, TypeError, IndexError):
                    age_group_nb = -99

                # =================================================
                # General information
                # =================================================

                user_obj.page_name = line["page_name"]
                user_obj.page_url = line["page_url"]

                user_obj.age_group_nb = age_group_nb

                user_obj.century_of_birth = line.get(
                    "century_of_birth"
                )

                user_obj.century_of_death = line.get(
                    "century_of_death"
                )

                user_obj.number_of_word_in_page_name = len(
                    line["page_name"].split(" ")
                )

                user_obj.picture_url = line.get(
                    "picture_url"
                )

                user_obj.page_lenght = len(
                    line["page_name"]
                )

                user_obj.first_name = line.get(
                    "first_name"
                )

                user_obj.first_name_standard = line.get(
                    "first_name_standard"
                )

                user_obj.last_name = line.get(
                    "last_name"
                )

                user_obj.last_name_standard = line.get(
                    "last_name_standard"
                )

                job = line.get("job")

                if job is not None:
                    user_obj.job = unidecode(job)
                else:
                    user_obj.job = None

                # =================================================
                # Birth information
                # =================================================

                town_birth_place = line.get(
                    "town_birth_place"
                )

                if town_birth_place is not None:
                    user_obj.town_birth_place = (
                        unidecode(town_birth_place)
                        .replace("-", " ")
                    )
                else:
                    user_obj.town_birth_place = None

                user_obj.town_birth_place_href = line.get(
                    "town_birth_place_href"
                )

                if (
                    user_obj.birth_town_localisation
                    and len(user_obj.birth_town_localisation) < 50
                ):
                    new_localisation = line.get(
                        "birth_town_localisation"
                    )

                    if new_localisation is not None:
                        user_obj.birth_town_localisation = (
                            new_localisation
                        )

                elif not user_obj.birth_town_localisation:
                    user_obj.birth_town_localisation = line.get(
                        "birth_town_localisation"
                    )

                country_birth_place = line.get(
                    "country_birth_place"
                )

                if country_birth_place is not None:
                    user_obj.country_birth_place = (
                        country_birth_place.lower()
                    )
                else:
                    user_obj.country_birth_place = None

                user_obj.time_period_of_birth = line.get(
                    "time_period_of_birth"
                )

                user_obj.continent_of_birth = line.get(
                    "continent_of_birth"
                )

                user_obj.region_of_birth = line.get(
                    "region_of_birth"
                )

                user_obj.birth_date = str(
                    line.get("birth_date")
                )

                user_obj.birth_year = birth_year

                user_obj.birth_month = str(
                    line.get("birth_month")
                )

                user_obj.birth_day = str(
                    line.get("birth_day")
                )

                user_obj.birth_month_day = str(
                    line.get("birth_month_day")
                )

                # =================================================
                # Death information
                # =================================================

                town_death_place = line.get(
                    "town_death_place"
                )

                if town_death_place is not None:
                    user_obj.town_death_place = (
                        unidecode(town_death_place)
                        .replace("-", " ")
                    )
                else:
                    user_obj.town_death_place = None

                user_obj.town_death_place_href = line.get(
                    "town_death_place_href"
                )

                if (
                    user_obj.town_death_localisation
                    and len(user_obj.town_death_localisation) < 50
                ):
                    new_localisation = line.get(
                        "town_death_localisation"
                    )

                    if new_localisation is not None:
                        user_obj.town_death_localisation = (
                            new_localisation
                        )

                elif not user_obj.town_death_localisation:
                    user_obj.town_death_localisation = line.get(
                        "town_death_localisation"
                    )

                country_death_place = line.get(
                    "country_death_place"
                )

                if country_death_place is not None:
                    user_obj.country_death_place = (
                        country_death_place.lower()
                    )
                else:
                    user_obj.country_death_place = None

                user_obj.continent_of_death = line.get(
                    "continent_of_death"
                )

                user_obj.region_of_death = line.get(
                    "region_of_death"
                )

                user_obj.death_date = str(
                    line.get("death_date")
                )

                user_obj.death_year = death_year

                user_obj.death_month = str(
                    line.get("death_month")
                )

                user_obj.death_day = str(
                    line.get("death_day")
                )

                user_obj.death_month_day = str(
                    line.get("death_month_day")
                )

                user_obj.cause_of_death = line.get(
                    "cause_of_death"
                )

                user_obj.is_cause_of_death_known = (
                    is_cause_of_death_known_
                )

                # =================================================
                # Birth / death comparisons
                # =================================================

                user_obj.born_outside_france = line.get(
                    "user_birth_outside_france",
                    False
                )

                user_obj.died_outside_france = line.get(
                    "user_death_outside_france",
                    False
                )

                user_obj.born_and_died_in_the_same_town = str(
                    line.get(
                        "born_and_died_in_the_same_town",
                        "False"
                    )
                )

                user_obj.born_and_died_in_the_same_country = str(
                    line.get(
                        "born_and_died_in_the_same_country",
                        "False"
                    )
                )

                user_obj.born_and_died_in_the_same_continent = str(
                    line.get(
                        "born_and_died_in_the_same_continent",
                        "False"
                    )
                )

                user_obj.born_and_died_in_the_same_region = str(
                    line.get(
                        "born_and_died_in_the_same_region",
                        "False"
                    )
                )

                user_obj.born_before_christ = str(
                    line.get(
                        "born_before_christ",
                        False
                    )
                )

                user_obj.died_before_christ = str(
                    line.get(
                        "died_before_christ",
                        "False"
                    )
                )

                user_obj.born_and_died_before_christ = str(
                    line.get(
                        "born_and_died_before_christ",
                        "False"
                    )
                )

                user_obj.born_and_died_after_christ = str(
                    line.get(
                        "born_and_died_after_christ",
                        "False"
                    )
                )

                user_obj.born_and_died_in_the_same_day = str(
                    line.get(
                        "born_and_died_on_the_same_day",
                        "False"
                    )
                )

                user_obj.born_before_christ_and_died_after_christ = str(
                    line.get(
                        "born_before_christ_and_died_after_christ",
                        "False"
                    )
                )

                # =================================================
                # Age
                # =================================================

                user_obj.age = line.get("age")

                user_obj.age_group = line.get(
                    "age_group"
                )

                user_obj.is_alive = line.get(
                    "is_alive",
                    True
                )

                user_obj.week_day_of_birth = line.get(
                    "week_day_of_birth"
                )

                user_obj.week_day_of_death = line.get(
                    "week_day_of_death"
                )

                # =================================================
                # Personal information
                # =================================================

                user_obj.gender = line.get(
                    "gender"
                )

                # =================================================
                # Ranking
                # =================================================

                user_obj.power_ranking = line.get(
                    "power_ranking"
                )

                user_obj.position = line.get(
                    "position"
                )

                user_obj.position_percentage = line.get(
                    "position_percentage"
                )

                user_obj.grade_over_20 = line.get(
                    "grade_over_20"
                )

                # =================================================
                # Wikipedia page analysis
                # =================================================

                user_obj.first_char_of_the_page = line.get(
                    "first_char_of_the_page"
                )

                user_obj.wikipedia_page_lenght = line.get(
                    "wikipedia_page_length",
                    0
                )

                user_obj.all_links_of_a_page = line.get(
                    "all_links_of_a_page",
                    []
                )

                user_obj.number_of_links = line.get(
                    "number_of_links",
                    0
                )

                user_obj.number_of_user_who_have_linked_this_user = (
                    line.get(
                        "number_of_user_who_have_linked_this_user",
                        0
                    )
                )

                user_obj.list_of_friend_of_user = line.get(
                    "list_of_friend_of_user",
                    []
                )

                user_obj.number_of_friends = line.get(
                    "number_of_friends",
                    0
                )

                user_obj.list_of_page_name_linked_sorted = line.get(
                    "list_of_page_name_linked_sorted",
                    []
                )

                user_obj.preciseness_level = line.get(
                    "preciseness_level"
                )

                user_obj.list_of_unpreciseness_data = line.get(
                    "list_of_unpreciseness_data",
                    []
                )

                # =================================================
                # Country emojis
                # =================================================

                user_obj.country_birth_place_emoji = line.get(
                    "country_birth_place_emoji"
                )

                user_obj.country_death_place_emoji = line.get(
                    "country_death_place_emoji"
                )

                # =================================================
                # Metadata
                # =================================================

                user_obj.number_of_views = 0

                users_to_update.append(user_obj)

            except Exception as error:

                total_errors += 1

                print(
                    f"Error while preparing user "
                    f"{error}"
                )

                print(line)
                print("----")

        # ---------------------------------------------------------
        # ONE BULK UPDATE for the entire batch
        # ---------------------------------------------------------

        if users_to_update:

            try:

                WikipediaUser.objects.bulk_update(
                    users_to_update,
                    fields=fields_to_update,
                    batch_size=BATCH_SIZE,
                )

                total_updated += len(users_to_update)

                print(
                    f"Updated {total_updated} users"
                )

            except Exception as error:

                total_errors += 1

                print(
                    f"Error during bulk update: {error}"
                )

        # ---------------------------------------------------------
        # Free references from the previous batch
        # ---------------------------------------------------------

        del parsed_lines
        del page_names
        del users_by_page_name
        del users_to_update

    # -------------------------------------------------------------
    # Finished
    # -------------------------------------------------------------

    print(
        f"Finished: "
        f"{total_updated} updated, "
        f"{total_skipped} skipped, "
        f"{total_errors} errors"
    )

    return HttpResponse(
        f"Users updated in the database. "
        f"Updated: {total_updated}, "
        f"Skipped: {total_skipped}, "
        f"Errors: {total_errors}",
        status=200
    )

@csrf_exempt
def rupdate_all_wikipedia_user(request):
    """Update all Wikipedia users"""

    if request.method != "POST":
        return HttpResponse("Error!", status=404)

    user_data_dict = print_file_content(USER_DICT_FILE_PATH).split("\n")

    for i, user in enumerate(user_data_dict[0:5]):
        try:
            line = ast.literal_eval(user)

            #if i % 10000 == 0:
            print(i, line["page_name"])

            if line["page_name"] in USERS_TO_SKIP:
                continue

            user_obj = WikipediaUser.objects.filter(
                page_name=line["page_name"]
            ).first()

            if user_obj is None:
                continue

            birth_year = line.get("birth_year")
            death_year = line.get("death_year")

            if type(birth_year) != int:
                birth_year = 123456789

            if type(death_year) != int:
                death_year = 123456789

            if line.get("age") == -999:
                is_alive = False
            else:
                is_alive = line.get("is_alive", True)

            if line.get("position") == -999:
                continue

            is_cause_of_death_known_ = False

            if (
                line.get("cause_of_death") != "Unspecified"
                and line.get("cause_of_death") != "alive"
            ):
                is_cause_of_death_known_ = True

            try:
                age_group_nb = int(line.get("age_group")[0])
            except:
                age_group_nb = -99

            # General information
            user_obj.page_name = line["page_name"]
            user_obj.page_url = line["page_url"]
            user_obj.age_group_nb = age_group_nb
            user_obj.century_of_birth = line.get("century_of_birth")
            user_obj.century_of_death = line.get("century_of_death")
            user_obj.number_of_word_in_page_name = len(
                line["page_name"].split(" ")
            )
            user_obj.picture_url = line.get("picture_url")
            user_obj.page_lenght = len(line["page_name"])

            user_obj.first_name = line.get("first_name")
            user_obj.first_name_standard = line.get(
                "first_name_standard"
            )

            user_obj.last_name = line.get("last_name")
            user_obj.last_name_standard = line.get(
                "last_name_standard"
            )

            user_obj.job = unidecode(line.get("job"))

            # Birth information
            user_obj.town_birth_place = unidecode(
                line.get("town_birth_place")
            ).replace("-"," ")
            user_obj.town_birth_place_href = line.get(
                "town_birth_place_href"
            )
            if (len(user_obj.birth_town_localisation)) < 50:
                user_obj.birth_town_localisation = line.get(
                    "birth_town_localisation"
                )
            user_obj.country_birth_place = line.get(
                "country_birth_place"
            ).lower()
            user_obj.time_period_of_birth = line.get(
                "time_period_of_birth"
            )
            user_obj.continent_of_birth = line.get(
                "continent_of_birth"
            )
            user_obj.region_of_birth = line.get(
                "region_of_birth"
            )

            user_obj.birth_date = str(
                line.get("birth_date")
            )
            user_obj.birth_year = birth_year
            user_obj.birth_month = str(
                line.get("birth_month")
            )
            user_obj.birth_day = str(
                line.get("birth_day")
            )
            user_obj.birth_month_day = str(
                line.get("birth_month_day")
            )

            # Death information
            user_obj.town_death_place = unidecode(
                line.get("town_death_place")
            ).replace("-"," ")
            user_obj.town_death_place_href = line.get(
                "town_death_place_href"
            )
            if (len(user_obj.town_death_localisation)) < 50:
                        
                user_obj.town_death_localisation = line.get(
                    "town_death_localisation"
                )
            user_obj.country_death_place = line.get(
                "country_death_place"
            ).lower()
            user_obj.continent_of_death = line.get(
                "continent_of_death"
            )
            user_obj.region_of_death = line.get(
                "region_of_death"
            )

            user_obj.death_date = str(
                line.get("death_date")
            )
            user_obj.death_year = death_year
            user_obj.death_month = str(
                line.get("death_month")
            )
            user_obj.death_day = str(
                line.get("death_day")
            )
            user_obj.death_month_day = str(
                line.get("death_month_day")
            )

            user_obj.cause_of_death = line.get(
                "cause_of_death"
            )
            user_obj.is_cause_of_death_known = (
                is_cause_of_death_known_
            )

            # Birth / death comparisons
            user_obj.born_outside_france = line.get(
                "user_birth_outside_france",
                "False"
            )

            user_obj.died_outside_france = line.get(
                "user_death_outside_france",
                "False"
            )

            user_obj.born_and_died_in_the_same_town = str(
                line.get(
                    "born_and_died_in_the_same_town",
                    "False"
                )
            )

            user_obj.born_and_died_in_the_same_country = str(
                line.get(
                    "born_and_died_in_the_same_country",
                    "False"
                )
            )

            user_obj.born_and_died_in_the_same_continent = str(
                line.get(
                    "born_and_died_in_the_same_continent",
                    "False"
                )
            )

            user_obj.born_and_died_in_the_same_region = str(
                line.get(
                    "born_and_died_in_the_same_region",
                    "False"
                )
            )

            user_obj.born_before_christ = line.get(
                "born_before_christ",
                False
            )

            user_obj.died_before_christ = str(
                line.get(
                    "died_before_christ",
                    "False"
                )
            )

            user_obj.born_and_died_before_christ = str(
                line.get(
                    "born_and_died_before_christ",
                    "False"
                )
            )

            user_obj.born_and_died_after_christ = str(
                line.get(
                    "born_and_died_after_christ",
                    "False"
                )
            )

            user_obj.born_and_died_in_the_same_day = str(
                line.get(
                    "born_and_died_on_the_same_day",
                    "False"
                )
            )

            user_obj.born_before_christ_and_died_after_christ = str(
                line.get(
                    "born_before_christ_and_died_after_christ",
                    "False"
                )
            )

            # Age
            user_obj.age = line.get("age")
            user_obj.age_group = line.get("age_group")
            user_obj.is_alive = line.get(
                "is_alive",
                True
            )

            user_obj.week_day_of_birth = line.get(
                "week_day_of_birth"
            )

            user_obj.week_day_of_death = line.get(
                "week_day_of_death"
            )

            # Personal information
            user_obj.gender = line.get("gender")

            # Ranking
            user_obj.power_ranking = line.get(
                "power_ranking"
            )
            user_obj.position = line.get("position")
            user_obj.position_percentage = line.get(
                "position_percentage"
            )
            user_obj.grade_over_20 = line.get(
                "grade_over_20"
            )

            # Wikipedia page analysis
            user_obj.first_char_of_the_page = line.get(
                "first_char_of_the_page"
            )

            user_obj.wikipedia_page_lenght = line.get(
                "wikipedia_page_length",
                0
            )

            user_obj.all_links_of_a_page = line.get(
                "all_links_of_a_page",
                []
            )

            user_obj.number_of_links = line.get(
                "number_of_links",
                0
            )

            user_obj.number_of_user_who_have_linked_this_user = (
                line.get(
                    "number_of_user_who_have_linked_this_user",
                    0
                )
            )

            user_obj.list_of_friend_of_user = line.get(
                "list_of_friend_of_user",
                []
            )

            user_obj.number_of_friends = line.get(
                "number_of_friends",
                0
            )

            user_obj.list_of_page_name_linked_sorted = line.get(
                "list_of_page_name_linked_sorted",
                []
            )

            user_obj.preciseness_level = line.get(
                "preciseness_level"
            )

            user_obj.list_of_unpreciseness_data = line.get(
                "list_of_unpreciseness_data",
                []
            )

            # Country emojis
            user_obj.country_birth_place_emoji = line.get(
                "country_birth_place_emoji"
            )

            user_obj.country_death_place_emoji = line.get(
                "country_death_place_emoji"
            )

            user_obj.number_of_views = 0
            # Save existing object
            user_obj.save()

        except Exception as error:
            print(f"Error while adding user: {error}")
            print("user")
            print(user)
            print("----")
            
            # import traceback
            # traceback.print_exc()
            

    return HttpResponse(
        "Users updated in the database",
        status=200
    )