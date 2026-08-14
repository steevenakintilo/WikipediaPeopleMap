from utility_function import *
import ast
import json
from global_variable import *
from urllib.parse import unquote
from collections import Counter

def get_all_job_name():
    all_data = print_file_content("user_info_dict_sorted_by_power.txt").split("\n")

    reset_file(r"stat_files/all_job.txt")
    reset_file(r"stat_files/all_job_page.txt")
    reset_file(r"stat_files/all_job2.txt")
    reset_file(r"stat_files/all_job_page2.txt")
        
    toto = []
    dict_of_page_size = {}
    for i , hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i " , i)
        try:
            line = ast.literal_eval(hg)
            if line["job"] not in toto:
                if len(str(line["job"])) > 20 or str(line["job"]).count(" ") > 3:
                    write_into_file(r"stat_files/all_job2.txt",line["job"]+"\n")
                    write_into_file(r"stat_files/all_job_page2.txt", line["job"] + "   -----------   " + line["page_name"] + "\n")
                else:                    
                    write_into_file(r"stat_files/all_job.txt",line["job"]+"\n")
                    write_into_file(r"stat_files/all_job_page.txt", line["job"] + "   -----------   " + line["page_name"] + "\n")
                toto.append(line["job"])

        except:
            pass


def get_all_small_age():
    all_data = print_file_content("user_info_dict_sorted_by_power.txt").split("\n")

    reset_file(r"stat_files/all_age.txt")
    reset_file(r"stat_files/all_age2.txt")
        
    toto = []
    dict_of_page_size = {}
    for i , hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i " , i)
        try:
            line = ast.literal_eval(hg)
            if line["age"] not in toto:
                if str(line["age"]).isdigit() is False:
                    continue
                if int(line["age"]) <= 5 or int(line["age"]) == -999:
                    write_into_file(r"stat_files/all_age.txt",str(line["age"])+"\n")
                    write_into_file(r"stat_files/all_age2.txt", str(line["age"]) + "   -----------   " + line["page_name"] + "\n")
                                        
                #toto.append(line["age"])

        except:
            pass

def get_all_unclear_people_age():
    all_data = print_file_content("user_info_dict_sorted_by_power.txt").split("\n")

    reset_file(r"stat_files/all_gender.txt")
    reset_file(r"stat_files/all_gender2.txt")
        
    toto = []
    dict_of_page_size = {}
    for i , hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i " , i)
        try:
            line = ast.literal_eval(hg)
            if line["gender"] not in toto:
                if line["gender"] == "Unclear":
                    write_into_file(r"stat_files/all_gender.txt",str(line["gender"])+"\n")
                    write_into_file(r"stat_files/all_gender2.txt", str(line["gender"]) + "   -----------   " + line["page_name"] + "\n")
                                        
                #toto.append(line["age"])

        except:
            pass

def get_all_undefined_town():
    all_data = print_file_content("user_info_dict_sorted_by_power.txt").split("\n")
    print(len(all_data))
    reset_file(r"stat_files/all_town.txt")
    reset_file(r"stat_files/all_town2.txt")
    

    skip = False
    toto = []
    dict_of_page_size = {}
    for i , hg in enumerate(all_data):
        skip = False
        if i % 100000 == 0:
            print("i " , i)
        try:
            line = ast.literal_eval(hg)
            if line["town_birth_place"] not in toto and line["town_death_place"] not in toto:
                # for html in HTML_ELEMENT_LIST:
                #     if html.lower() in line["town_birth_place"].lower() or html.lower() in line["town_death_place"].lower():
                #         skip = True
                if skip is False:
                    if line["town_birth_place"] != "Undefined" and len(line["town_birth_place"]) != 0 and (line["birth_town_localisation"] == "Undefined"  or len(line["birth_town_localisation"]) ==0):
                        write_into_file(r"stat_files/all_town.txt",str(line["town_birth_place"])+"\n")
                        write_into_file(r"stat_files/all_town2.txt", str(line["town_birth_place"]) + "   -----------   " + line["page_name"] + "\n")
                        toto.append(line["town_birth_place"])    
                    if line["town_death_place"] != "Undefined" and len(line["town_death_place"]) != 0 and (line["death_town_localisation"] == "Undefined"  and len(line["death_town_localisation"]) ==0) and line["is_alive"] is False:
                        write_into_file(r"stat_files/all_town.txt",str(line["town_death_place"])+"\n")
                        write_into_file(r"stat_files/all_town2.txt", str(line["town_death_place"]) + "   -----------   " + line["page_name"] + "\n")
                        toto.append(line["town_death_place"])
            
        except:
            pass
def get_all_undefined_town2():
    all_data = print_file_content("user_info_dict_sorted_by_power.txt").split("\n")
    print(len(all_data))
    reset_file(r"stat_files/all_town3.txt")
    

    skip = False
    toto = []
    dict_of_page_size = {}
    for i , hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i " , i)
        try:
            line = ast.literal_eval(hg)
                # for html in HTML_ELEMENT_LIST:
                #     if html.lower() in line["town_birth_place"].lower() or html.lower() in line["town_death_place"].lower():
                #         skip = True
            if line["town_birth_place"] != "Undefined" and len(line["town_birth_place"]) != 0 and (line["birth_town_localisation"] == "Undefined"  or len(line["birth_town_localisation"]) ==0):
                toto.append(line["town_birth_place"].lower().strip())    
            if line["town_death_place"] != "Undefined" and len(line["town_death_place"]) != 0 and (line["death_town_localisation"] == "Undefined"  and len(line["death_town_localisation"]) ==0) and line["is_alive"] is False:
                toto.append(line["town_death_place"].lower().strip())
                
            
        except:
            pass


    blabla_town = []
    blabla_count = []
    for t in toto:
        if t not in  blabla_town:
            blabla_town.append(t)
            blabla_count.append(toto.count(t))
    paired = list(zip(blabla_town, blabla_count))
    
    paired.sort(key=lambda x: x[1], reverse=False)


    list_of_element, occurence_of_element_list = zip(*paired)
    list_of_element = list(list_of_element)
    occurence_of_element_list = list(occurence_of_element_list)
    list_of_element.reverse()
    occurence_of_element_list.reverse()

    for elem , occurence in zip(list_of_element,occurence_of_element_list):
        write_into_file(r"stat_files/all_town3.txt",f"{elem}     -------     {occurence}\n")

def get_all_job_name2():
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    jobs = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            job = line.get("job")

            if job and job != "Undefined":
                jobs[job.lower().strip()] += 1

        except (ValueError, SyntaxError):
            continue

    # Sort by occurrence descending
    jobs_sorted = sorted(
        jobs.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # One single write
    with open(r"stat_files/all_job3.txt", "w", encoding="utf-8") as f:
        for job, count in jobs_sorted:
            f.write(f"{job}     -------     {count}\n")

def get_all_country_name():
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    countries = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            birth_country = line.get("country_birth_place")
            if birth_country and birth_country != "Undefined":
                countries[birth_country.lower().strip()] += 1

            death_country = line.get("country_death_place")
            if death_country and death_country != "Undefined":
                countries[death_country.lower().strip()] += 1

        except (ValueError, SyntaxError):
            continue

    countries_sorted = sorted(
        countries.items(),
        key=lambda x: x[1],
        reverse=True
    )

    with open(r"stat_files/all_country.txt", "w", encoding="utf-8") as f:
        for country, count in countries_sorted:
            f.write(f"{country}     -------     {count}\n")

def get_all_first_name():
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    first_names = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            first_name = line.get("first_name")

            if first_name and first_name != "Undefined":
                first_names[first_name.lower().strip()] += 1

        except (ValueError, SyntaxError):
            continue

    # Sort by occurrence descending
    first_names_sorted = sorted(
        first_names.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # One single write
    with open(r"stat_files/all_first_name.txt", "w", encoding="utf-8") as f:
        for first_name, count in first_names_sorted:
            f.write(f"{first_name}     -------     {count}\n")


def get_all_last_name():
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    last_names = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            last_name = line.get("last_name")

            if last_name and last_name != "Undefined":
                last_names[last_name.lower().strip()] += 1

        except (ValueError, SyntaxError):
            continue

    # Sort by occurrence descending
    last_names_sorted = sorted(
        last_names.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # One single write
    with open(r"stat_files/all_last_name.txt", "w", encoding="utf-8") as f:
        for last_name, count in last_names_sorted:
            f.write(f"{last_name}     -------     {count}\n")

def get_all_gender():
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    genders = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            gender = line.get("gender")

            if gender and gender != "Undefined":
                genders[gender.lower().strip()] += 1

        except (ValueError, SyntaxError):
            continue

    # Sort by occurrence descending
    genders_sorted = sorted(
        genders.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # One single write
    with open(r"stat_files/all_gender.txt", "w", encoding="utf-8") as f:
        for gender, count in genders_sorted:
            f.write(f"{gender}     -------     {count}\n")


def get_all_birth_month_day():
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    birth_month_days = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            birth_month_day = line.get("birth_month_day")

            if birth_month_day and birth_month_day != "Undefined":
                birth_month_days[str(birth_month_day).strip()] += 1

        except (ValueError, SyntaxError):
            continue

    # Sort by occurrence descending
    birth_month_days_sorted = sorted(
        birth_month_days.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # One single write
    with open(r"stat_files/all_birth_month_day.txt", "w", encoding="utf-8") as f:
        for birth_month_day, count in birth_month_days_sorted:
            f.write(f"{birth_month_day}     -------     {count}\n")

def get_all_continent_of_birth():
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    continents = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            continent = line.get("continent_of_birth")

            if continent and continent != "Undefined":
                continents[continent.lower().strip()] += 1

        except (ValueError, SyntaxError):
            continue

    # Sort by occurrence descending
    continents_sorted = sorted(
        continents.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # One single write
    with open(r"stat_files/all_continent_of_birth.txt", "w", encoding="utf-8") as f:
        for continent, count in continents_sorted:
            f.write(f"{continent}     -------     {count}\n")

def get_all_generic_function(variable_to_search):
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    variavble_name = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            var = line.get(variable_to_search)

            try:
                if var != "Undefined" and len(str(var)) != 0:
                    variavble_name[var.lower().strip()] += 1
            except:
                if var != "Undefined" and len(str(var)) != 0:
                    variavble_name[var] += 1
                        
        except (ValueError, SyntaxError):
            continue

    # Sort by occurrence descending
    variavble_name_sorted = sorted(
        variavble_name.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # One single write
    with open(rf"stat_files/all_{variable_to_search}.txt", "w", encoding="utf-8") as f:
        for var, count in variavble_name_sorted:
            f.write(f"{var}     -------     {count}\n")


def get_all_generic_function2(variable_to_search,variable_to_search2):
    with open("user_info_dict_sorted_by_power.txt", "r", encoding="utf-8") as f:
        all_data = f.readlines()

    print(len(all_data))

    variavble_name = Counter()

    for i, hg in enumerate(all_data):
        if i % 100000 == 0:
            print("i", i)

        try:
            line = ast.literal_eval(hg)

            var = line.get(variable_to_search)
            var2 = line.get(variable_to_search2)
                        

            try:
                if var != "Undefined" and len(str(var)) != 0:
                    variavble_name[var.lower().strip()] += 1
            except:
                if var != "Undefined" and len(str(var)) != 0:
                    variavble_name[var] += 1

            try:
                if var2 != "Undefined" and len(str(var2)) != 0:
                    variavble_name[var2.lower().strip()] += 1
            except:
                if var != "Undefined" and len(str(var2)) != 0:
                    variavble_name[var2] += 1
                        
        except (ValueError, SyntaxError):
            continue

    # Sort by occurrence descending
    variavble_name_sorted = sorted(
        variavble_name.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # One single write
    with open(rf"stat_files/all_{variable_to_search}_and_{variable_to_search2}.txt", "w", encoding="utf-8") as f:
        for var, count in variavble_name_sorted:
            f.write(f"{var}     -------     {count}\n")


def get_top_1000_user():
    all_data = print_file_content("user_info_dict_sorted_by_power.txt").split("\n")[0:1000]
    reset_file(r"stat_files/top_1000_user_info_dict_sorted_by_power.txt")
    for line in all_data:
        write_into_file(r"stat_files/top_1000_user_info_dict_sorted_by_power.txt",line+"\n")
    

# #ranked_user()
# #idk_how_to_name_it()

print("get_all_undefined_town")
get_all_undefined_town()

print("get_all_small_age")
get_all_small_age()

print("get_all_job_name")
get_all_job_name()

print("get_all_unclear_people_age")
get_all_unclear_people_age()

print("get_all_undefined_town2")
get_all_undefined_town2()

print("get_all_job_name2")
get_all_job_name2()

print("get_all_country_name")
get_all_country_name()

print("get_all_first_name")
get_all_first_name()

print("get_all_last_name")
get_all_last_name()

print("get_all_gender")
get_all_gender()

print("get_all_continent_of_birth")
get_all_continent_of_birth()

print("get_all_birth_month_day")
get_all_birth_month_day()

print("get_top_1000_user")
get_top_1000_user()

print("get_birth_year")
get_all_generic_function("birth_year")

print("get_death_year")
get_all_generic_function("death_year")


list_of_stuff_to_check = ["born_before_christ","born_before_christ_and_died_after_christ","born_and_died_in_the_same_town","born_and_died_in_the_same_country",
                          "born_and_died_in_the_same_continent","born_and_died_in_the_same_region","region_of_birth","region_of_death","is_alive","first_char_of_the_page","get_all_continent_of_death",
                           "town_birth_place","town_death_place","death_date","birth_date","birth_month","death_month"]

for stuff in list_of_stuff_to_check:
    print(f"get_{stuff}")
    get_all_generic_function(stuff)

print("get town_birth_place & town_death_place")
get_all_generic_function2("town_birth_place","town_death_place")

print("get birth_year & death_year")
get_all_generic_function2("birth_year","death_year")

print("get birth_date & death_date")
get_all_generic_function2("birth_date","death_date")

print("get birth_month & death_month")
get_all_generic_function2("birth_month","death_month")
