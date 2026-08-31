"""A file that handle all the information"""
import ast
import json
import re
import sys
import traceback
import time
import unicodedata

from collections import Counter
from datetime import datetime
from urllib.parse import unquote,quote
from dateutil import relativedelta
from unidecode import unidecode

from bs4 import BeautifulSoup
from libzim.reader import Archive


from global_variable import *
from utility_function import *


# Undefined Variable
# pylint: disable=E0602

# Too general exception
# pylint: disable=W0718

# No exception type specified
# pylint: disable=W0702

# Line is too long
# pylint: disable=C0301

class WikiPeopleData():
    """A class that define all the birth/death place/date of all real people on wikipedia"""
    def __init__(self):
        self.zim = Archive(r"../wikipedia_fr_all_maxi_2026-02.zim")
        self.today_date : datetime = datetime.now().date()
        self.list_of_country : list[str] = print_file_content("list_of_country.txt").split("\n")
        self.list_of_country_lower : list[str] = print_file_content("list_of_country.txt").lower().replace("-"," ").split("\n")
        self.list_of_wikipedia_page_of_real_people : list[str] = print_file_content("list_of_wikipedia_page_of_real_people.txt").split("\n")
        self.list_of_wikipedia_page_of_non_real_people : list[str] = print_file_content("list_of_wikipedia_page_of_non_real_people.txt").split("\n")
        #self.all_user_data_file : list[str] = print_file_content("user_info_dict.txt").split("\n")
        self.all_real_people_set = set(self.list_of_wikipedia_page_of_real_people)

        with open("data_files/people_dict_power_ranking.json", "r", encoding="utf-8") as file:
            self.power_ranking_json = json.load(file)
        with open("data_files/list_of_link_of_all_users_sorted.json", "r", encoding="utf-8") as file:
            self.list_of_link_of_user = json.load(file)
                
    def clean_title(self,title:str) -> str:
        """A function that clean a wikipedia title"""
        title = title.strip()

        # enlève seulement les guillemets extérieurs si présents
        if len(title) >= 2 and title[0] == '"' and title[-1] == '"':
            title = title[1:-1]

        title = unquote(title)
        title = title.replace("_", " ")

        return title.strip()

    def convert_before_christ_to_date(self,date:str) -> int:
        """A function that convert wikipedia before christ date to date"""
        date = date.replace("U-","")
        if date[0] == "0":
            date = int(date[1:]) + 1
        return date * -1

    def get_age_between_two_date(self,date1_year:int,date1_month:int,date1_day:int,date2_year:int,date2_month:int,date2_day:int) -> int:
        """A function that get an age between two date"""
        age = date2_year - date1_year
        if (date2_month <= date1_month and date2_day < date1_day) or date2_day < date1_day:
            age-=1
        return age

    def clean_localisation(self,s):
        """A function that clean localisation and remove useless char"""
        s = unicodedata.normalize("NFKC", s)
        s = s.lower()
        s = s.replace("″", "′′")
        s = " ".join(s.split())
        return s


    def get_all_links_of_a_page(self,page_name):
        """A function that get link of a page"""
        # Example: get article by title
        #try:
        entry = self.zim.get_entry_by_title(self.clean_title(page_name))
        list_of_link = []
        # Read raw HTML
        html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
        #soup = BeautifulSoup(html, "html.parser")
        #intro_text =  str(html[:10000])
        intro_text = str(html)
        #split_link = intro_text.split("<a href=")
        titles = re.findall(r'<a\s[^>]*title="([^"]+)"', html)
        
        #print(titles)
        
        for title in titles:
            if title in self.all_real_people_set and title not in list_of_link:
                list_of_link.append(title)
        # for link in split_link:
        #     if "title=" in link:
        #         split_link_ = link.split("title=")[1].split(">")
        #         link_name = split_link_[0].replace('"',"")
        #         if link_name in self.all_real_people_set and link_name not in list_of_link:
        #             list_of_link.append(link_name)
                
        #print(soup.get_text()[:1000])
        
        #print(list_of_link)
        return list_of_link
    def get_country_of_a_town(self,town:str,potential_birth_country:str="") -> str:
        """A function that get the country of a town"""
        try:
            if potential_birth_country.lower().replace("-"," ") not in self.list_of_country_lower:
                potential_birth_country = ""
            

            if town.isdigit():
                return "Undefined"
            if len(town) == 0:
                return "Undefined"
            if town == "Undefined":
                return "Undefined"
            if len(potential_birth_country) != 0:
                if potential_birth_country[0] == "":
                    potential_birth_country = potential_birth_country[1:]

            entry = self.zim.get_entry_by_title(self.clean_title(town))

            html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
            portion_of_wikipedia_page_text = html[:100000]
            for i in range (1,100):
                text_normal = portion_of_wikipedia_page_text.replace("\n"*i,"\n")


            if str(town) == "1861":
                reset_file("get_country_of_a_town.txt")
                write_into_file("get_country_of_a_town.txt",text_normal)
            return text_normal.split('title="Liste des pays du monde">Pays</a>')[1].split("data-sort-value=")[1].split(">")[0].replace('"',"")
        except:
            try:
                if potential_birth_country in portion_of_wikipedia_page_text and len(potential_birth_country) > 1:
                    return potential_birth_country
                list_of_found_country = []
                list_of_found_index = []
                for country in self.list_of_country:
                    country_html_checker = f'title="{country}">{country}'
                    for index , line in enumerate(text_normal.split("\n")):
                        if country_html_checker.lower().replace("_"," ") in line.lower().replace("_"," "):
                            list_of_found_country.append(country)
                            list_of_found_index.append(index)
                            #return country
                
                


                         
                if len(list_of_found_country) != 0:
                    return list_of_found_country[list_of_found_index.index(min(list_of_found_index))]
                return "Undefined"
            except:
                return "Undefined"

    def birth_year_to_time_period(self,birth_year:int):
        """A function that convert a birh date to a time period"""
        time_period = "Prehistory"
        if birth_year >= -3300:
            time_period = "Antiquity"
        if birth_year >= 476:
            time_period = "Middle Ages"
        if birth_year >= 1492:
            time_period = "Renaissance"
        if birth_year >= 1789:
            time_period = "Contemporary Period"
        if birth_year >= 2000:
            time_period = "Today Time"
        if birth_year == 123456789:
            time_period = "Undefined"
        return time_period

    def get_localisation_of_a_town(self,town:str) -> str:
        """A function that get the localisation of a town"""
        try:
            if len(town) == 0:
                return "Undefined"
            if town == "Undefined":
                return "Undefined"

            entry = self.zim.get_entry_by_title(self.clean_title(town))

            html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
            portion_of_wikipedia_page_text = html[:100000]
            text_normal = portion_of_wikipedia_page_text

            for i in range (1,100):
                text_normal = text_normal.replace("\n"*i,"\n")

            soup = BeautifulSoup(text_normal, "html.parser")

            page_text = soup.get_text(" ", strip=True)

            # reset_file("town_text.txt")
            # write_into_file("town_text.txt",html+"\n")
            #localisation_direction = ""
            localisation_sud = f'{page_text.split("Coordonnées")[1].split('sud')[0]}'
            localisation_est = f'{page_text.split("Coordonnées")[1].split('est')[0]}'
            localisation_ouest = f'{page_text.split("Coordonnées")[1].split('ouest')[0]}'
            localisation_nord = f'{page_text.split("Coordonnées")[1].split('nord')[0]}'
            # if len(localisation_est) - 2 == len(localisation_ouest):
            #     localisation_direction = "ouest"
            # elif len(localisation_nord) < len(localisation_sud) and len(localisation_nord) < len(localisation_ouest) and len(localisation_nord) < len(localisation_est):
            #     localisation_direction = "nord"
            # elif len(localisation_sud) < len(localisation_nord) and len(localisation_sud) < len(localisation_ouest) and len(localisation_sud) < len(localisation_est):
            #     localisation_direction = "sud"
            # elif len(localisation_est) < len(localisation_nord) and len(localisation_est) < len(localisation_est):
            #     localisation_direction = "est"

            localisation_possible_name = ["ouest","nord","sud","est"]
            localisation_possible_lenght = [len(localisation_ouest),len(localisation_nord),len(localisation_sud),len(localisation_est)]

            paired = list(zip(localisation_possible_name, localisation_possible_lenght))

            paired.sort(key=lambda x: x[1], reverse=False)


            list_of_element, occurence_of_element_list = zip(*paired)
            list_of_element = list(list_of_element)
            occurence_of_element_list = list(occurence_of_element_list)
            # print(list_of_element)
            # print(occurence_of_element_list)
            # # print("sud ",len(localisation_sud))
            # print("est ",len(localisation_est))
            # print("ouest" ,len(localisation_ouest))
            # print("nord " , len(localisation_nord))
            localisation = f'{page_text.split("Coordonnées")[1].split(list_of_element[1])[0]}{list_of_element[1][0].upper()}'.replace("nord","N").replace("ouest","O").replace("sud","S").replace("est","E")
            localisation = localisation.replace("O","W")

            # print(localisation_direction,list_of_element[1])
            # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


            if len(localisation.strip()) > 50:
                return localisation.strip()[0:28]

            return localisation.strip()
        except:
            try:
                return TOWN_TO_LOCALISATION_DICT[town.lower().strip().replace("_"," ")]
            except:
                return "Undefined"

    def get_gender_of_a_person(self,page_text:str,is_alive:bool) ->  str:
        """A function that get the gender of a person"""

        boy_score = 0
        girl_score = 0
        page_text = page_text.lower()
        soup = BeautifulSoup(page_text, "html.parser")

        page_text = soup.get_text(" ", strip=True)

        page_chars_checker = 50000
        page_split = page_text[:page_chars_checker].split(" ")
        #print(page_split[0:100])
        # CHECK FOR BOY
        # if "est né" in page_text[:page_chars_checker] and "est née" not in page_text[:page_chars_checker]:
        #     boy_score+=1
        if "né" in page_split and "née" in page_split:
            if page_split.index("né") < page_split.index("née"):
                boy_score+=5
        elif "né" in page_split:
            #print(page_split.index("né"),page_split.index("né"),page_split.index("né"))
            boy_score+=1

        if "est un" in page_text[:page_chars_checker] and "est une" not in page_text[:page_chars_checker]:
            boy_score+=2

        if "est un" in page_text[:page_chars_checker] and "est une" in page_text[:page_chars_checker]:
            if len(page_text.split("est un")[1]) > len(page_text.split("est une")[1]):
                boy_score+=5
                        

        if "était un" in page_text[:page_chars_checker] and "était une" not in page_text[:page_chars_checker] and is_alive is False:
            boy_score+=1

        if "était un" in page_text[:page_chars_checker] and "était une" in page_text[:page_chars_checker] and is_alive is False:
            if len(page_text.split("était un")[1]) > len(page_text.split("était une")[1]):
                boy_score+=5
            
                        
        if "est mort" in page_text[:page_chars_checker] and "est morte" in page_text[:page_chars_checker] and is_alive is False:
            if len(page_text.split("est morte")[1]) > len(page_text.split("est mort")[1]):
                boy_score+=5
        

        if "et mort" in page_text[:page_chars_checker] and "et morte" in page_text[:page_chars_checker] and is_alive is False:
            if len(page_text.split("et morte")[1]) > len(page_text.split("et mort")[1]):
                boy_score+=5
        
        if "baptisé" in page_text[:page_chars_checker]:
            boy_score+=1
        if "est mort" in page_text and "est morte" not in page_text:
            boy_score+=1
        if "et mort" in page_text and "et morte" not in page_text:
            boy_score+=1
        
        # CHECK FOR GIRL

        if "né" in page_split and "née" in page_split:
            if page_split.index("née") < page_split.index("né"):
                girl_score+=5
        elif "née" in page_split:
            girl_score+=1

        if "est une" in page_text[:page_chars_checker] and "est un" not in page_text[:page_chars_checker]:
            girl_score+=2

        if "est un" in page_text[:page_chars_checker] and "est une" in page_text[:page_chars_checker]:
            if len(page_text.split("est une")[1]) < len(page_text.split("est un")[1]):
                girl_score+=5
                        
        if "était une" in page_text[:page_chars_checker] and "était un" not in page_text[:page_chars_checker] and is_alive is False:
            girl_score+=1

        if "était un" in page_text[:page_chars_checker] and "était une" in page_text[:page_chars_checker] and is_alive is False:
            if len(page_text.split("était une")[1]) < len(page_text.split("était un")[1]):
                girl_score+=5
            
                        
        if "baptisée" in page_text[:page_chars_checker]:
            girl_score+=1


        if "est mort" in page_text[:page_chars_checker] and "est morte" in page_text[:page_chars_checker] and is_alive is False:
            if len(page_text.split("est morte")[1]) < len(page_text.split("est mort")[1]):
                girl_score+=5
            

        if "et mort" in page_text[:page_chars_checker] and "et morte" in page_text[:page_chars_checker] and is_alive is False:
            if len(page_text.split("et morte")[1]) < len(page_text.split("et mort")[1]):
                girl_score+=5
                        
    
        if "est morte" in page_text:
            girl_score+=1
        if "et morte" in page_text:
            girl_score+=1

        if page_text.lower().split(" ").count("elle") > page_text.lower().split(" ").count("il"):
            girl_score+=5
        elif page_text.lower().split(" ").count("elle") < page_text.lower().split(" ").count("il"):
            boy_score+=5
                
        if boy_score == girl_score:
            return "Unclear"
        elif boy_score > girl_score:
            return "Man"
        return "Woman"

    def country_to_continent(self,country:str) -> str:
        """A function that return the continent of a given country"""
        country = country.lower().replace("-"," ")
        list_of_continents_name = ["Africa","America","Asia","Europe","Oceania"]
        list_of_continents_name = ["Afrique","Amerique","Asie","Europe","Océanie"]

        for continent_list , continent_name in zip(LIST_OF_CONTINENTS,list_of_continents_name):
            for country_name in continent_list:
                country_name = country_name.replace("-"," ")
                if country == country_name:
                    return continent_name
        return "Undefined"


    def country_to_region_of_the_world(self,country:str) -> str:
        """A function that return the region of the world of a given country"""
        country = country.lower().replace("-"," ")

        for region_list , region_name in zip(LIST_OF_REGIONS,LIST_OF_REGIONS_NAME):
            for country_name in region_list:
                country_name = country_name.replace("-"," ")
                country = country.replace("-"," ")
                if country.lower() == country_name.lower():
                    return region_name
        return "Undefined"

    def is_element_in_line(self,line:str):
        """A function that check if an element is in a line"""
        for job in JOBS:
            if f'"{job.lower()}' in line.lower() and line.lower().count(f'"{job.lower()}') > 1:
                return job
        return None

    def remove_bad_link_of_an_user(self,list_of_link:list[str]):
        """A function that remove all the bad link of an user"""
        new_list_of_link = []
        for link in list_of_link:
            if link not in BAD_WIKI_PAGE:
                new_list_of_link.append(link)

        return new_list_of_link
    def get_user_information(self, page_name:str,force_print_data:bool=False,page_nb:int=-999) -> bool:
        """A function that get user information (age,date of birth,death,place of birth,death...)"""
        try:

            # Faire if date de naissance / lieu de naissance in text blabla
            # Date de naissance
            # Lieu de naissance
            # Else Checker Naissance
            # Naissance
            # Décès
            # Date de décès
            # Lieu de décès
            # Activité principale
            # Activité

            try:
                entry = self.zim.get_entry_by_title(self.clean_title(page_name))
            except:
                write_into_file("list_of_wikipedia_page_of_non_real_people.txt",page_name+"\n")
                return False

            
            html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
            portion_of_wikipedia_page_text = html[:100000]



            try:
            # Find the first image
                soup = BeautifulSoup(html, "html.parser")
                img = soup.find("img")
                img_path = img["src"].lstrip("./")
                filename = img_path.split("/")[-1]
                
                picture_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(filename)}"
                
                if picture_url == "https://commons.wikimedia.org/wiki/Special:FilePath/langfr-250px-Defaut_2.svg.png" or ".svg." in picture_url:
                    picture_url = "https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg"
            except:
                picture_url = "https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg"
                                
            sub_job = []
            if page_nb == -999:
                reset_file("user_text_info.txt")
                write_into_file("user_text_info.txt",portion_of_wikipedia_page_text)
            text_normal = ""
            if '<table class="infobox_v2 infobox infobox--frwiki noarchive">' in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split('<table class="infobox_v2 infobox infobox--frwiki noarchive">')[1].split("</tbody></table>")[0]
            elif "Biographie" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("Biographie")[1]
            elif len(text_normal) < 20 and "Informations générales" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("Informations générales")[1]
            elif len(text_normal) < 20 and "infobox--frwiki noarchive" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("infobox--frwiki noarchive")[1]
            if len(text_normal) < 7500:
                soup = BeautifulSoup(html, "html.parser")
                whole_page_text_plain_text = soup.get_text(" ", strip=True)
                if len(whole_page_text_plain_text) > 75000:                           
                    text_normal = portion_of_wikipedia_page_text
                else:
                    text_normal = html
                                    
            for i in range (1,100):
                text_normal = text_normal.replace("\n"*i,"\n")


            if page_nb == -999:
                reset_file("user_text_info2.txt")
                write_into_file("user_text_info2.txt",text_normal)
                
            
            today_date_str = str(self.today_date)

            try:
                if "Activités</th>" not in text_normal:

                    if "Activité</th>" in text_normal:
                        job = text_normal.split("Activité</th>")[1].split(" title=")[1].split(">")[0].replace('"',"")       
                        
                        # try:
                        #     job = text_normal.split("Activité</th>")[1].split(" title=")[1].split(">")[0].replace('"',"")       
                        #     if job.lower() in text_normal.split("Activité</th>")[1].split(" title=")[1].split(">")[1]:
                        #         job = text_normal.split("Activité</th>")[1].split(" title=")[1].split(">")[1].replace('"',"").split("<")[0]
                        # except:
                        #     job = text_normal.split("Activité</th>")[1].split(" title=")[1].split(">")[0].replace('"',"")       
                                                
                    elif "Profession</th>" in text_normal:
                        job = text_normal.split("Profession</th>")[1].split(" title=")[1].split(">")[0].replace('"',"")

                    else:
                        if "Activité principale</th>" not in text_normal:
                            job = text_normal.split("</a></th></tr>")[0].split(">")[-1]
                            job_index = 0
                            
                            if len(text_normal.split("</a></th></tr>")[0].split(">")[job_index -1].split("<")[0]) != 0:
                                
                                for index , line in enumerate(text_normal.split("</a></th></tr>")[0].split(">")):
                                    is_job_in_line = self.is_element_in_line(line)
                                    if is_job_in_line != None:
                                        job = is_job_in_line
                                        job_index = 9999
                                        break
                                    if "et <a href=" in line:
                                        job_index = index
                                        break
                                if job_index != 0 and job_index != 9999:
                                    job = text_normal.split("</a></th></tr>")[0].split(">")[job_index -1].split("<")[0]
                            if job == "":
                                job = text_normal.split("Activité principale")[1].split("</a>")[0].split(">")[-1]
                                    
                        else:
                            job = text_normal.split("Activité principale</th>")[1].split(" title=")[1].split(">")[0].replace('"',"")
                            if text_normal.split("Activité principale</th>")[1].split("</div></td>")[0].split("<div>")[1].strip() in JOBS:
                                job = text_normal.split("Activité principale</th>")[1].split("</div></td>")[0].split("<div>")[1].strip()
                        # if '<' in job or '=' in job:
                        #     job = "jobo"
                        
                else:
                    try:
                        job = text_normal.split("Activités</th>")[1].split("<a href=")[1].split(" title=")[1].split("<")[0].split(">")[1].strip()
                    except:
                        job = text_normal.split("Activités</th>")[1].split("<a href=")[1].split(" title=")[0].replace('"',"")
                    #print("job ", text_normal.split("Activités</th>")[1].split("<a href=")[8])

            except:
                pass

            
            try:
                job = job.replace("_"," ")
            except:
                pass
            town_birth_place = ""
            country_birth_place = ""
            town_death_place = ""
            country_death_place = ""
            birth_date = ""
            death_date = ""
            age = "dead"
            is_alive = True
            born_before_chirst = False
            died_before_christ = False
            preciseness_level = 200
            continent_of_birth = ""
            continent_of_death = ""
            birth_town_localisation = ""
            death_town_localisation = ""
            list_of_unpreciseness_data = []
            town_birth_place_href = ""
            town_death_place_href = ""
            birth_year_is_real_but_month_and_day_are_not = False
            death_year_is_real_but_month_and_day_are_not = False
            soup = BeautifulSoup(html[:100000], "html.parser")
            page_text_plain_text = soup.get_text(" ", strip=True)

            if page_nb == -999:
                reset_file("blabla.txt")
                write_into_file("blabla.txt",page_text_plain_text.replace(",","\n"))
            soup = BeautifulSoup(text_normal, "html.parser")
            page_text_small_text = soup.get_text(" ", strip=True)

            soup = BeautifulSoup(html, "html.parser")
            whole_page_text_plain_text = soup.get_text(" ", strip=True)


            is_alive_check = False
            try:
                if "décès" in text_normal.lower():
                    naissance_pos = 0
                    deces_pos =  0
                    if "naissance" in text_normal:
                        for i , word in enumerate(text_normal.replace("\n"," ").split(" ")):
                            if "naissance" in word and naissance_pos == 0:
                                naissance_pos = i
                            if "décès" in word.lower() and deces_pos == 0:
                                deces_pos = i
                                                        
                        if deces_pos <= naissance_pos and naissance_pos - deces_pos > 200:
                            is_alive_check = True
                        if deces_pos >= naissance_pos and deces_pos - naissance_pos > 200:
                            is_alive_check = True


                                                
            except:
                pass


            if "Lieu de naissance" in text_normal and "<td>Inconnu" not in text_normal:
                try:
                    if "<td>Inconnu" in text_normal:
                        town_birth_place = "Undefined"
                    else:
                        town_birth_place = text_normal.split("Lieu de naissance")[1].split("</a>")[0].split("title=")[1].split(">")[1]
                        try:
                            town_birth_place_href = text_normal.split("Lieu de naissance")[1].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                        except:
                            town_birth_place_href = ""

                        if " " in town_birth_place:
                            if town_birth_place.split(" ")[1] in LIST_OF_MONTH:
                                town_birth_place = text_normal.split("Lieu de naissance")[1].split("</a>")[2].split("title=")[1].split(">")[1]
                            try:
                                town_birth_place_href = text_normal.split("Lieu de naissance")[1].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                            except:
                                town_birth_place_href = ""
                except:
                    pass
                # print(text_normal.split("Lieu de naissance")[1].split("</a>")[0])
                # if town_birth_place.isdigit() and " " not in town_birth_place:
                #     town_birth_place = text_normal.split("<a href=")[4].split(" title=")[1].split(">")[0].replace('"',"")
                # elif town_birth_place.split(" ")[0].isdigit() and " " in town_birth_place:
                #     town_birth_place = text_normal.split("<a href=")[4].split(" title=")[1].split(">")[0].replace('"',"")
                # elif town_birth_place.split(" ")[1] in LIST_OF_MONTH:
                #     town_birth_place = text_normal.split("<a href=")[4].split(" title=")[1].split(">")[0].replace('"',"")

                if town_birth_place != "Undefined":
                    try:
                        potential_birth_country = text_normal.split("Lieu de naissance")[1].split("</a>")[2].split("title=")[1].split(">")[0].replace('"',"")

                        if "av. J.-C." in potential_birth_country:
                            try:
                                potential_birth_country = text_normal.split("Lieu de naissance")[1].split("Date de décès")[0].split('title=')[-1].split(">")[1].split("<")[0]
                            except:
                                potential_birth_country = "x"
                    #print(potential_birth_country)
                        #print(text_normal.split("Lieu de naissance")[1].split("Date de décès")[0].split('title=')[-1].split(">")[1]).split("<")[0]
                    except:
                        potential_birth_country = "x"
                    country_birth_place = self.get_country_of_a_town(town_birth_place.replace(" ","_"),potential_birth_country.replace(" ","_"))

                #return
                try:
                    birth_date = text_normal.split("Date de naissance")[1].split("datetime=")[1].split(" ")[0].replace('"',"")

                except:
                    pass

                try:
                    if len(birth_date) == 0:
                        for i , line in enumerate(text_normal.split("datetime=")):
                            if "Date de naissance" in line or "Naissance" in line:
                                birth_index = i

                        if birth_index == 0:
                            birth_index = 2

                        try:
                            birth_date = text_normal.split("datetime=")[birth_index - 1].split(" ")[0].replace('"',"")
                        except:
                            pass
                except:
                    pass
                # print("kokpopo " , page_name)
                # print("kpogkroepkgperkgporekgopkgporkgporkgoperrkgpkgpoekgrpo")
                # print(text_normal.split("Date de naissance")[1].split("datetime=")[1].split(" "))
                # print(birth_date)
                # return


                if "décès" in text_normal.lower() and is_alive_check == False:
                    is_alive = False
                    try:
                        death_date = text_normal.split("Date de décès")[1].split("datetime=")[1].split(" ")[0].replace('"',"")
                    except:
                        pass
                    try:
                        if death_date == "":
                            birth_index = 1
                            for i , line in enumerate(text_normal.split("datetime=")):
                                if "Décès" in line:
                                    death_index = i

                            if death_index == 0:
                                death_index = 2
                            try:
                                death_date = text_normal.split("datetime=")[death_index + 1].split(" ")[0].replace('"',"")
                            except:
                                pass
                    except:
                        pass

                try:
                    if "U-" in birth_date:
                        whole_birth_date = text_normal.split("Date de naissance")[1].split("<td>")[1].split("<")[0].split(" ")
                        birth_date = f"{self.convert_before_christ_to_date(birth_date)}-{MONTH_TO_NUMBER_DICT[whole_birth_date[1]]}-{whole_birth_date[0]}"
                        born_before_chirst = True
                except:
                    pass
                try:
                    if "U-" in death_date:
                        whole_death_date = text_normal.split("Date de décès")[1].split("<td>")[1].split("<")[0].split(" ")
                        if "décès" in text_normal.lower() and is_alive_check == False:
                            death_date = f"{self.convert_before_christ_to_date(death_date)}-{MONTH_TO_NUMBER_DICT[whole_death_date[1]]}-{whole_death_date[0]}"
                            died_before_christ = True
                except:
                    pass
                # elif birth_date.replace("-","").isdigit() is False:
                #     pass

                #print(birth_date)
            else:

                try:
                    if town_birth_place == "" or "%C" in town_birth_place:
                        town_birth_place = text_normal.split("<a href=")[3].split(" title=")[1].split(">")[0].replace('"',"")
                        try:
                            town_birth_place_href = text_normal.split("<a href=")[3].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                        except:
                            town_birth_place_href = ""


                    skip_the_rest = False

                                        
                    try:
                        town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split("-")[0].replace('"',"").strip()
                        town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    
                        if "(" in text_normal.split(town_birth_place)[1] and ")" in text_normal.split(town_birth_place)[1]:
                            town_birth_place_href = town_birth_place+text_normal.split(town_birth_place)[1].split('"')[0]


                        if town_birth_place == "(":
                            potential_place = page_text_small_text.split(town_birth_place_year)[1].split(")")[1].strip().split(",")
                            town_birth_place = potential_place[0].strip()

                            if page_text_small_text.split(town_birth_place_year)[1].split(")")[1].strip().count(",") >= 2:
                                town_birth_place = potential_place[1].strip()
                        for i in range(3):
                            if town_birth_place != "" and town_birth_place != "Undefined" and town_birth_place in text_normal.split("<a href=")[3 + i]:
                                try:
                                    town_birth_place_href = text_normal.split("<a href=")[3 + i].split("title=")[0].strip()
                                    town_birth_place_href = unquote(town_birth_place_href.replace('"',""))

                                except:
                                    town_birth_place_href = ""
                                break
                        skip_the_rest = True
                    except:
                        town_birth_place_year = ""
                        town_birth_place = ""


                    
                                     
                    try:
                        if (town_birth_place.isdigit() and " " not in town_birth_place) or (town_birth_place.split(" ")[0].isdigit() and " " in town_birth_place) or (town_birth_place.split(" ")[1].lower() in LIST_OF_MONTH) or (town_birth_place.split(" ")[0].lower() in LIST_OF_MONTH):
                            try:
                                town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split("-")[0].replace('"',"").strip()
                                town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                                if town_birth_place == "(":
                                    potential_place = page_text_small_text.split(town_birth_place_year)[1].split(")")[1].strip().split(",")
                                    town_birth_place = potential_place[0].strip()
                                    if page_text_small_text.split(town_birth_place_year)[1].split(")")[1].strip().count(",") >= 2:
                                        town_birth_place = potential_place[1].strip()

                            except:
                                town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split("-")[0].replace('"',"").strip()
                            skip_the_rest = True
                    except:
                        pass
                    try:
                        if town_birth_place == "" or "%C" in town_birth_place:
                            town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split("-")[0].replace('"',"").strip()
                            town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    except:
                        pass


                    try:
                        if town_birth_place == "" or "%C" in town_birth_place:
                            town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split('" ')[0].replace('"',"").strip()
                            town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    except:
                        pass

                    # for i in range(3):
                    #     #     if town_birth_place != "" and town_birth_place != "Undefined" and town_birth_place in text_normal.split("<a href=")[3 + i]:
                    #     #         print("popo " , town_birth_place,text_normal.split("<a href=")[3 + i])
                    #     #         try:
                    #     #             town_birth_place_href = text_normal.split("<a href=")[3 + i].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                    #     #         except:
                    #     #             town_birth_place_href = ""
                    #     #         break


                    if skip_the_rest:
                        pass
                    elif town_birth_place.isdigit() and " " not in town_birth_place:

                        town_birth_place = text_normal.split("<a href=")[4].split(" title=")[1].split(">")[0].replace('"',"")
                        try:
                            town_birth_place_href = text_normal.split("<a href=")[4].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                        except:
                            town_birth_place_href = ""

                    elif town_birth_place.split(" ")[0].isdigit() and " " in town_birth_place:
                        town_birth_place = text_normal.split("<a href=")[4].split(" title=")[1].split(">")[0].replace('"',"")
                        try:
                            town_birth_place_href = text_normal.split("<a href=")[4].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                        except:
                            town_birth_place_href = ""

                    elif town_birth_place.split(" ")[1].lower() in LIST_OF_MONTH:

                        town_birth_place = text_normal.split("<a href=")[4].split(" title=")[1].split(">")[0].replace('"',"")
                        try:
                            town_birth_place_href = text_normal.split("<a href=")[4].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                        except:
                            town_birth_place_href = ""

                    elif town_birth_place.split(" ")[0].lower() in LIST_OF_MONTH:

                        town_birth_place = text_normal.split("<a href=")[4].split(" title=")[1].split(">")[0].replace('"',"")
                        try:
                            town_birth_place_href = text_normal.split("<a href=")[4].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                        except:
                            town_birth_place_href = ""


                    if town_birth_place[0:4].isdigit() and " " in town_birth_place and town_birth_place.count(" ") > 1:
                        town_birth_place = text_normal.split("<a href=")[3].split(" title=")[1].split(">")[0].replace('"',"")
                        for i in range(5,len(text_normal.split("<a href="))):
                            if "%C" not in text_normal.split("<a href=")[i] and "class=" not in text_normal.split("<a href=")[i]:
                                town_birth_place = text_normal.split("<a href=")[i]
                                break

                        town_birth_place = town_birth_place.split("title=")[1].split(">")[0].replace('"',"")

                    if town_birth_place[0:4].isdigit() and " " in town_birth_place and town_birth_place.count(" ") > 1:
                        town_birth_place = text_normal.split("<a href=")[3].split(" title=")[1].split(">")[0].replace('"',"")

                        for i in range(3,len(text_normal.split("<a href="))):
                            #print(i)
                            if "%C" not in text_normal.split("<a href=")[i] and "class=" not in text_normal.split("<a href=")[i]:
                                town_birth_place = text_normal.split("<a href=")[i]
                                break
                        town_birth_place = town_birth_place.split("title=")[1].split(">")[0].replace('"',"")

                    if town_birth_place.split(" ")[0].lower() in LIST_OF_MONTH:
                        town_birth_place = ""


                    try:
                        if town_birth_place == "" or "%C" in town_birth_place:
                            town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split("-")[0].replace('"',"").strip()
                            town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    except:
                        pass

                    try:
                        if town_birth_place == "" or "%C" in town_birth_place:
                            town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split('" ')[0].replace('"',"").strip()
                            town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    except:
                        pass


                except:

                    try:
                        if town_birth_place[0:4].isdigit() and " " in town_birth_place and town_birth_place.count(" ") > 1:
                            town_birth_place = text_normal.split("<a href=")[3].split(" title=")[1].split(">")[0].replace('"',"")

                            for i in range(3,len(text_normal.split("<a href="))):
                                #print(i)
                                if "%C" not in text_normal.split("<a href=")[i] and "class=" not in text_normal.split("<a href=")[i]:
                                    town_birth_place = text_normal.split("<a href=")[i]
                                    break
                            town_birth_place = town_birth_place.split("title=")[1].split(">")[0].replace('"',"")

                        else:
                            town_birth_place = text_normal.split("<a href=")[4].split(" title=")[0].replace('"',"")
                            if "%C" in town_birth_place or "class=" in town_birth_place:
                                town_birth_place = text_normal.split("<a href=")[6].split(" title=")[0].replace('"',"")
                            else:

                                try:
                                    town_birth_place_href = text_normal.split("<a href=")[4].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                                except:
                                    town_birth_place_href = ""

                    except:

                        pass

                    try:
                        if "%C" in town_birth_place or "class=" in town_birth_place:
                            if "Naissance" in text_normal:
                                town_birth_place = text_normal.split("Naissance")[1].split("<a href=")[1].split(">")[0].split('"')[1].strip()
                    except:
                        town_birth_place = ""

                #


                #print(text_normal.split("<a href=")[11])
                if "%C" in town_birth_place or "class=" in town_birth_place:
                    town_birth_place = "Undefined"

                if town_birth_place != "town_birth_place":
                    if town_birth_place_href != "" and town_birth_place_href != "Undefined":
                        country_birth_place = self.get_country_of_a_town(town_birth_place_href.replace(" ","_"))
                    else:
                        country_birth_place = self.get_country_of_a_town(town_birth_place.replace(" ","_"))
                    
                                        


                try:
                    if town_birth_place.isdigit():
                        if "Naissance" in text_normal:
                            town_birth_place = text_normal.split("Naissance")[1].split("title=")[2].split("<")[0].split(">")[1].strip()
                except:
                    town_birth_place = ""
                birth_index = 1
                for i , line in enumerate(text_normal.split("datetime=")):
                    if "Date de naissance" in line or "Naissance" in line:
                        birth_index = i

                if birth_index == 0:
                    birth_index = 2


                try:
                    birth_date = text_normal.split("datetime=")[birth_index - 1].split(" ")[0].replace('"',"")
                    if "<" in birth_date or ">" in birth_date:
                        birth_date = text_normal.split("datetime=")[birth_index].split(" ")[0].replace('"',"")
                except:
                    pass

                if len(birth_date) <= 4 and birth_date.isdigit():
                    birth_date+="-01-01"
                    birth_year_is_real_but_month_and_day_are_not =  True




                if "décès" in text_normal.lower() and is_alive_check is False:        
                    is_alive = False
                    if "Date Naissance" in text_normal:
                        pass          
                    try:
                        death_date = text_normal.split("datetime=")[birth_index].split(" ")[0].replace('"',"")
                    except:
                        pass
                if "U-" in birth_date:
                    try:
                        whole_birth_date = text_normal.split("Date de naissance")[1].split("<td>")[1].split("<")[0].split(" ")
                    except:
                        whole_birth_date = ""
                    #print(birth_date)
                    try:
                        birth_date = f"{self.convert_before_christ_to_date(birth_date)}-{MONTH_TO_NUMBER_DICT[whole_birth_date[1]]}-{whole_birth_date[0]}"
                    except:
                        try:
                            birth_date = (int(birth_date.replace("U-0","")) + 1) * -1
                        except:
                            pass
                    born_before_chirst = True
                if "U-" in death_date:
                    try:
                        whole_death_date = text_normal.split("Date de décès")[1].split("<td>")[1].split("<")[0].split(" ")
                    except:
                        pass
                    if "décès" in text_normal.lower() and is_alive_check == False:
                        try:
                            death_date = f"{self.convert_before_christ_to_date(death_date)}-{MONTH_TO_NUMBER_DICT[whole_death_date[1]]}-{whole_death_date[0]}"
                        except:
                            try:
                                death_date = (int(death_date.replace("U-0","")) + 1) * -1
                            except:
                                pass
                        died_before_christ = True

                #print(text_normal.split("<a href=")[4])


            birth_date_is_between_two_date = False
            death_date_is_between_two_date = False

            try:
                if len(str(death_date)) <= 4 and death_date.isdigit():
                    death_date+="-01-01"
                    death_year_is_real_but_month_and_day_are_not =  True
            except:
                pass

            if death_date != "" and death_date != "Undefined" and death_date == birth_date:
                if "né en" in page_text_plain_text:
                    if page_text_plain_text.split("né en")[1].strip().split(" ")[0].replace(",","").replace("-","").isdigit():
                        birth_date = ""
                        birth_date = f"{page_text_plain_text.split("né en")[1].strip().split(" ")[0].replace(",","").replace("-","")}-01-01"
                if "née en" in page_text_plain_text:
                    if page_text_plain_text.split("née en")[1].strip().split(" ")[0].replace(",","").replace("-","").isdigit():
                        birth_date = ""
                        birth_date = f"{page_text_plain_text.split("née en")[1].strip().split(" ")[0].replace(",","").replace("-","")}-01-01"

                if is_alive is False:

                    if "mort en" in page_text_plain_text:
                        if page_text_plain_text.split("mort en")[1].strip().split(" ")[0].replace("-","").replace(",","").isdigit():
                            death_date = ""
                            death_date = f"{page_text_plain_text.split("mort en")[1].strip().split(" ")[0].replace(",","").replace("-","")}-01-01"
                    if "morte en" in page_text_plain_text:
                        if page_text_plain_text.split("morte en")[1].strip().split(" ")[0].replace("-","").replace(",","").isdigit():
                            death_date = ""
                            death_date = f"{page_text_plain_text.split("morte en")[1].strip().split(" ")[0].replace(",","").replace("-","")}-01-01"


            try:
                birth_year = int(birth_date.split("-")[0])
                death_year = int(death_date.split("-")[0])

                if birth_year > death_year:
                    text_split = text_normal.split("Date de naissance")[1].split("\n")
                    if "entre" in text_split[2]:
                        birth_date_one = int(text_split[2].split("entre")[1].strip().split("et")[0].strip())
                        birth_date_two = int(text_split[2].split("entre")[1].strip().split("et")[1].strip())
                        birth_date = int((birth_date_one+birth_date_two)/2)
                        birth_date_is_between_two_date = True

                    death_date = text_normal.split("Date de décès")[1].split("datetime=")[1].split(" ")[0].replace('"',"")
                    if death_date[0] == "0":
                        death_date = death_date[1:]
            except:
                pass
            
            # print(birth_date)
            if "décès" not in text_normal.lower() or is_alive_check:
                #print(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}")
                try:
                    start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                    end_date = datetime.strptime(f"{today_date_str.split("-")[0]}-{str(int(today_date_str.split("-")[1]))}-{str(int(today_date_str.split("-")[2]))}", "%Y-%m-%d")

                    # Get the relativedelta between two dates
                    delta = relativedelta.relativedelta(end_date, start_date)
                    age = delta.years
                except:
                    age = -999

            else:
                #print(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}")
                if born_before_chirst:
                    #print(birth_date.split("-"))
                    try:
                        if len(birth_date) <= 4 and birth_date.isdigit():
                            birth_date+="-01-01"
                            birth_year_is_real_but_month_and_day_are_not =  True
                        if birth_date[0] == "0":
                            birth_date = birth_date[1:]
                        if death_date[0] == "0":
                            death_date = death_date[1:]
                    except:
                        pass
                    try:
                        year_start = int(birth_date.split("-")[1]) * -1 + ABSOLUTE_DATE_VALUE
                        year_end = int(death_date.split("-")[1]) * -1 + ABSOLUTE_DATE_VALUE

                        month_start = int(birth_date.split("-")[2])
                        month_end = int(death_date.split("-")[2])

                        day_start = int(birth_date.split("-")[3])
                        day_end = int(death_date.split("-")[3])

                        age = self.get_age_between_two_date(year_start,month_start,day_start,year_end,month_end,day_end)
                    except:
                        try:
                            
                            year_birth_date_ = birth_date[0:len(birth_date.split("-")[0])]
                            year_death_date_ = death_date[0:len(death_date.split("-")[0])]

                            # print(year_birth_date_)
                            # print(death_date)

                            if int(year_birth_date_) + ABSOLUTE_DATE_VALUE <= int(year_death_date_) + ABSOLUTE_DATE_VALUE:
                                age = (int(year_death_date_) + ABSOLUTE_DATE_VALUE) - (int(year_birth_date_) + ABSOLUTE_DATE_VALUE)
                            else:
                                age = (int(year_birth_date_) + ABSOLUTE_DATE_VALUE) - (int(year_death_date_) + ABSOLUTE_DATE_VALUE)
                        except:
                            age = -999
                    # start_date = datetime.strptime(f"{year_start}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                    # end_date = datetime.strptime(f"{year_end}-{str(int(death_date.split("-")[1]))}-{str(int(death_date.split("-")[2]))}", "%Y-%m-%d")

                    # # Get the relativedelta between two dates
                    # delta = relativedelta.relativedelta(end_date, start_date)
                    # age = delta.years

                else:
                    try:
                        if len(birth_date) <= 4 and birth_date.isdigit():
                            birth_date+="-01-01"
                            birth_year_is_real_but_month_and_day_are_not = True
                        if birth_date[0] == "0":
                            birth_date = birth_date[1:]
                        if death_date[0] == "0":
                            death_date = death_date[1:]
                    except:
                        pass
                    try:
                        start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                        end_date = datetime.strptime(f"{death_date.split("-")[0]}-{str(int(death_date.split("-")[1]))}-{str(int(death_date.split("-")[2]))}", "%Y-%m-%d")

                        # Get the relativedelta between two dates
                        delta = relativedelta.relativedelta(end_date, start_date)
                        age = delta.years
                                                    
                    except:
                        try:
                            year_birth_date_ = birth_date[0:len(birth_date.split("-")[0])]
                            year_death_date_ = death_date[0:len(death_date.split("-")[0])]

                            # print(year_birth_date_)
                            # print(death_date)

                            if int(year_birth_date_) + ABSOLUTE_DATE_VALUE <= int(year_death_date_) + ABSOLUTE_DATE_VALUE:
                                age = (int(year_death_date_) + ABSOLUTE_DATE_VALUE) - (int(year_birth_date_) + ABSOLUTE_DATE_VALUE)
                            else:
                                age = (int(year_birth_date_) + ABSOLUTE_DATE_VALUE) - (int(year_death_date_) + ABSOLUTE_DATE_VALUE)
                        except:
                            age = -999
            try:
                if birth_date_is_between_two_date and is_alive is False and len(str(birth_date)) <= 4:
                    if int(birth_date) + ABSOLUTE_DATE_VALUE <= int(death_date[0:len(str(birth_date))]) + ABSOLUTE_DATE_VALUE:
                        age = (int(int(death_date[0:len(str(birth_date))])) + ABSOLUTE_DATE_VALUE) - (int(birth_date) + ABSOLUTE_DATE_VALUE)
                    else:
                        age = (int(birth_date) + ABSOLUTE_DATE_VALUE) - (int(death_date[0:len(str(birth_date))]) + ABSOLUTE_DATE_VALUE)
            except:
                age = -999
            if "Lieu de décès" in text_normal:
                try:
                    town_death_place = text_normal.split("Lieu de décès")[1].split(' title=')[1].split(">")[0].replace('"',"")
                    try:
                        town_death_place_href = text_normal.split("Lieu de décès")[1].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                    except:
                        town_death_place_href = ""

                    country_death_place = self.get_country_of_a_town(town_death_place.replace(" ","_"),"")
                except:
                    pass
            elif "décès" in text_normal.lower() and is_alive_check == False:
                try:
                    town_death_place = text_normal.split("Décès")[1].split(')')[1].split(' title=')[1].split(">")[0].replace('"',"")
                    country_death_place = self.get_country_of_a_town(town_death_place.replace(" ","_"),"")
                    town_death_place_ =  town_death_place
                    country_death_place_ = country_death_place

                    if page_name == "Molière":
                        try:
                            if page_text_small_text.split(death_date.split("-")[0])[1].split(")")[1].strip().count(",") <= 2:
                                potential_place = page_text_small_text.split(death_date.split("-")[0])[1].split(")")[1].strip().split(",")[1].strip()
                                town_death_place = potential_place
                                country_death_place = self.get_country_of_a_town(town_death_place.replace(" ","_"),"")

                        except:
                            town_death_place =  ""
                            country_death_place = ""

                    try:
                        town_death_place_href = text_normal.split("Décès")[1].split(')')[1].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                    except:
                        town_death_place_href = ""


                    if town_death_place == "" or "<" in town_death_place or ">" in town_death_place or "%C" in town_death_place:

                        try:
                            if page_text_small_text.split(death_date.split("-")[0])[1].split(")")[1].strip().count(",") <= 2:
                                potential_place = page_text_small_text.split(death_date.split("-")[0])[1].split(")")[1].strip().split(",")[1].strip()
                                town_death_place = potential_place
                                country_death_place = self.get_country_of_a_town(town_death_place.replace(" ","_"),"")

                        except:
                            town_death_place =  town_death_place_
                            country_death_place = country_death_place_


                    # town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    # if town_birth_place == "(":
                    #     potential_place = page_text_small_text.split(town_birth_place_year)[1].split(")")[1].strip().split(",")
                    #     town_birth_place = potential_place[0].strip()
                    #     if page_text_small_text.split(town_birth_place_year)[1].split(")")[1].strip().count(",") >= 2:
                    #         town_birth_place = potential_place[1].strip()

                    #print(page_text_small_text.split(death_year))
                except:
                    try:
                        if town_death_place == "" or "<" in town_death_place or ">" in town_death_place or "%C" in town_death_place:
                            town_death_place = text_normal.split("Décès")[1].split('(')[2].split("title=")[1].replace('"',"").strip()
                            for line in text_normal.split("Décès")[1].split("href="):
                                if town_death_place.lower() in line.lower() and "title=" in line.lower():
                                    town_death_place_href = unquote(line.split(" title=")[0].replace('"',""))
                                    break
                            if len(town_death_place_href) != 0:
                                country_death_place = self.get_country_of_a_town(town_death_place_href.replace(" ","_"),"")
                            else:
                                country_death_place = self.get_country_of_a_town(town_death_place.replace(" ","_"),"")

                    except:
                        pass


            try:
                if len(str(birth_date)) > 4 and "-" not in str(birth_date[0]):
                    if death_date == birth_date and int(birth_date.split("-")[0]) >= 1900 and is_alive_check:
                        is_alive = True
            except:
                pass
            try:
                if is_alive and len(str(birth_date)) == 4:
                    age = 2026 - int(birth_date)
            except:
                age = -999
            gender = self.get_gender_of_a_person(html[:1000000],is_alive)

            
            job_player_list = ["joueuse","groupe","ancienne","femme d'","femme de"]

            determiner = "une"
            job_player_ = "joueuse"
            if gender == "Man":
                determiner = "un"
                job_player_list = ["joueur","groupe","ancien","homme d'","homme de"]
                job_player_ = "joueur"
                      
            try:
                if "id=" in job:
                    job = ""
            except:
                job = ""

            try:
                if "<" in job or ">" in job:
                    job = ""
            except:
                job = ""
            
            if job.isdigit():
                job = ""          
            
            try:
                if is_alive and len(job.strip()) <= 1 or job in LIST_OF_INCOMPLETE_JOB:
                    if "est un" in page_text_plain_text:
                        list_of_element_after_sentence = page_text_plain_text.split(f"est {determiner}")[1].split(" ")[0:10]
                        
                        for index,element in enumerate(list_of_element_after_sentence):
                            if len(element) > 1:
                                job = element
                                job_index = index
                                break
                        
                        if job in job_player_list or list_of_element_after_sentence[job_index+1].startswith("d'") or list_of_element_after_sentence[job_index+1].starthwith("de"):
                            job_index = 0
                            particle = "de"
                            for index , element in enumerate(list_of_element_after_sentence):
                                if job in ["ancien","ancienne"] and len(element) != 0 and element not in ["ancien","ancienne"]:
                                    job_index = index
                                    break
                                if element.startswith("d'"):
                                    job_index = index
                                    particle = "d'"
                                    break

                                if element == "de":
                                    job_index = index + 1
                                    break


                            if job in ["ancien","ancienne"]:
                                job_name = "ancien"
                                if gender == "Woman":
                                    job_name = "ancienne"
                                job = f"{determiner} {job_name} {list_of_element_after_sentence[job_index]}"
                            elif job not in ["ancien","ancienne"]:
                                job = f"{determiner} {job_player_} de {list_of_element_after_sentence[job_index]}"
                            if particle != "de" and job not in ["ancien","ancienne"]:
                                job = f"{job_} {job_player_} {list_of_element_after_sentence[job_index]}"
                            job_ = job
                            
                elif is_alive is False and job.strip() == "":
                    if "était un" in page_text_plain_text:
                        list_of_element_after_sentence = page_text_plain_text.split(f"est {determiner}")[1].split(" ")[0:10]
                        job_index = 0
                        for index,element in enumerate(list_of_element_after_sentence):
                            if len(element) > 1:
                                job = element
                                job_index = index
                                break

                        
                        if job in job_player_list or list_of_element_after_sentence[job_index+1].startswith("d'") or list_of_element_after_sentence[job_index+1].starthwith("de"):
                            job_index = 0
                            particle = "de"
                            for index , element in enumerate(list_of_element_after_sentence):
                                if job in ["ancien","ancienne"] and len(element) != 0 and element not in ["ancien","ancienne"]:
                                    job_index = index
                                    break
                                if element.startswith("d'"):
                                    job_index = index
                                    particle = "d'"
                                    break

                                if element == "de":
                                    job_index = index + 1
                                    break


                            if job in ["ancien","ancienne"]:
                                job_name = "ancien"
                                if gender == "Woman":
                                    job_name = "ancienne"
                                job = f"{determiner} {job_name} {list_of_element_after_sentence[job_index]}"
                            elif job not in ["ancien","ancienne"]:
                                job = f"{determiner} {job_player_} de {list_of_element_after_sentence[job_index]}"
                            if particle != "de" and job not in ["ancien","ancienne"]:
                                job = f"{job_} {job_player_} {list_of_element_after_sentence[job_index]}"
                            job_ = job
                            
                    elif "est un" in page_text_plain_text:
                        list_of_element_after_sentence = page_text_plain_text.split(f"est {determiner}")[1].split(" ")[0:10]
                        job_index = 0

                        for index,element in enumerate(list_of_element_after_sentence):
                            if len(element) > 1:
                                job = element
                                job_index = index
                                break

                        if job in job_player_list or list_of_element_after_sentence[job_index+1].startswith("d'") or list_of_element_after_sentence[job_index+1].starthwith("de"):
                            job_index = 0
                            particle = "de"
                            for index , element in enumerate(list_of_element_after_sentence):
                                if job in ["ancien","ancienne"] and len(element) != 0 and element not in ["ancien","ancienne"]:
                                    job_index = index
                                    break
                                if element.startswith("d'"):
                                    job_index = index
                                    particle = "d'"
                                    break

                                if element == "de":
                                    job_index = index + 1
                                    break


                            if job in ["ancien","ancienne"]:
                                job_name = "ancien"
                                if gender == "Woman":
                                    job_name = "ancienne"
                                job = f"{determiner} {job_name} {list_of_element_after_sentence[job_index]}"
                            elif job not in ["ancien","ancienne"]:
                                job = f"{determiner} {job_player_} de {list_of_element_after_sentence[job_index]}"
                            if particle != "de" and job not in ["ancien","ancienne"]:
                                job = f"{job_} {job_player_} {list_of_element_after_sentence[job_index]}"
                            job_ = job
                        


            except:
                pass


            try:
                if job.lower() == "un ancien joueur" or job.lower() == "une ancienne joueuse":
                    for i , line in enumerate(page_text_plain_text.lower().split(job)[1].strip().split(" ")):
                        if line == line == "d'":
                            job = f"{job} d'{page_text_plain_text.lower().split(job)[1].strip().split(" ")[i + 1]}"
                            break
                        if line == "de":
                            job = f"{job} de {page_text_plain_text.lower().split(job)[1].strip().split(" ")[i + 1]}"
                            break
                        if i > 10:
                            break
            except:
                pass                
            if job.lower() == "homme" and "homme politique" in page_text_plain_text.lower():
                preciseness_level -= 4
                job = "Homme politique"
                list_of_unpreciseness_data.append("User may have a bigger role than homme politique")

            if job.lower() == "femme" and "femme politique" in page_text_plain_text.lower():
                preciseness_level -= 4
                list_of_unpreciseness_data.append("User may have a bigger role than femme politique")
                job = "Femme politique"

            if job.lower() == "homme" and "homme d'état" in page_text_plain_text.lower():
                preciseness_level -= 4
                job = "Homme d'état"
                list_of_unpreciseness_data.append("User may have a bigger role than homme d'état")

            if job.lower() == "femme" and "femme d'état" in page_text_plain_text.lower():
                preciseness_level -= 4
                list_of_unpreciseness_data.append("User may have a bigger role than femme d'état")
                job = "Femme d'état"
            

            # if job in LIST_OF_INCOMPLETE_JOB:
            #     for little_job in JOBS:
            #         print(little_job)
            #         if little_job.lower() in page_text_plain_text.lower():
            #             print("yeaaah " , little_job)  
            #             job = little_job
            #             break
            
            list_of_little_job = []
            if job in LIST_OF_INCOMPLETE_JOB:
                for little_job in JOBS:
                    for word in page_text_plain_text.lower().split(" "):
                        if little_job.lower().strip() == word.lower().strip():
                            job = little_job
                            list_of_little_job.append(job)
                            break

                job = "Undefined"
                if len(list_of_little_job) != 0:
                    job = list_of_little_job[0]
                
            try:
                potential_new_job = print_file_content("potential_new_job.txt").split("\n")
                if job == town_birth_place and len(job) != 0 and job not in potential_new_job and job not in JOBS and job not in self.list_of_country and job not in CITIES:
                    print("JOB: " , job)
                    write_into_file("potential_new_job.txt",job+"\n")
                    write_into_file("potential_new_job_page.txt",page_name+"\n")

            except:
                pass
            
            if job == town_birth_place:

                if town_birth_place in CITIES:
                    town_birth_place = job
                    country_birth_place = self.get_country_of_a_town(town_birth_place.replace(" ","_"),"")
                    continent_of_birth = self.country_to_continent(country_birth_place.replace(" ","_"))
                else:
                    try:
                        town_birth_place = text_normal.split("<a href=")[2].split(" title=")[0].replace('"',"")
                        if town_birth_place != job and town_birth_place != "":
                            country_birth_place = self.get_country_of_a_town(town_birth_place,"")
                            continent_of_birth = self.country_to_continent(country_birth_place)
                    except:
                        town_birth_place = ""

                if job not in JOBS:
                    job = ""
                if (town_birth_place == job or town_birth_place == "") and town_birth_place not in CITIES:
                    town_birth_place = ""
            if len(job) <= 1:
                job = ""

            town_birth_place = town_birth_place.replace("en:","").replace("fr:","")
            town_death_place = town_death_place.replace("en:","").replace("fr:","")

            town_birth_place = town_birth_place.replace("_"," ")
            town_death_place = town_death_place.replace("_"," ")
            job = unquote(job)
            
            ### CHECK JOB
            if ":" in job or "//" in job:
                job = "Undefined"
            if job.isdigit():
                job = "Undefined"
            ###
            for prefix in JOBS_PREFIX:
                if f"{prefix.lower().replace("armées","armée").strip()} {job.lower().replace("armées","armée").strip()}" in page_text_plain_text.lower().replace("armées","armée").strip():
                    job = f"{prefix.strip()} {job.strip()}"

            job_ = job
            try:
                job = job[0].upper() + job[1:]
            except:
                job = job_
            
            if job.lower() in LIST_OF_WEIRD_JOB:
                job = WEIRD_JOB_REPLACEMENTS[job.lower()]



            # CAS AVEC DES IMAGES A DATES EX ERIC CLAPTON OU LE PAPE FRANCOIS
            
            try:
                if "Date de naissance" in text_normal:
                    if birth_date in text_normal:
                        split_birth_text = text_normal.split(birth_date)
                        if "Date de naissance" not in split_birth_text[0]:
                            birth_date  = split_birth_text[2].split("Date de naissance")[1].split("datetime=")[1].split(" d")[0].replace('"',"").strip()
                            if is_alive:
                                try:
                                    start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                                    end_date = datetime.strptime(f"{today_date_str.split("-")[0]}-{str(int(today_date_str.split("-")[1]))}-{str(int(today_date_str.split("-")[2]))}", "%Y-%m-%d")
                
                                    # Get the relativedelta between two dates
                                    delta = relativedelta.relativedelta(end_date, start_date)
                                    age = delta.years
                                except:
                                    age = -999
                            else:
                                try:
                                    start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                                    end_date = datetime.strptime(f"{death_date.split("-")[0]}-{str(int(death_date.split("-")[1]))}-{str(int(death_date.split("-")[2]))}", "%Y-%m-%d")
            
                                    # Get the relativedelta between two dates
                                    delta = relativedelta.relativedelta(end_date, start_date)
                                    age = delta.years
                                                                
                                except:
                                    try:
                                        year_birth_date_ = birth_date[0:len(birth_date.split("-")[0])]
                                        year_death_date_ = death_date[0:len(death_date.split("-")[0])]
            
                                        # print(year_birth_date_)
                                        # print(death_date)
            
                                        if int(year_birth_date_) + ABSOLUTE_DATE_VALUE <= int(year_death_date_) + ABSOLUTE_DATE_VALUE:
                                            age = (int(year_death_date_) + ABSOLUTE_DATE_VALUE) - (int(year_birth_date_) + ABSOLUTE_DATE_VALUE)
                                        else:
                                            age = (int(year_birth_date_) + ABSOLUTE_DATE_VALUE) - (int(year_death_date_) + ABSOLUTE_DATE_VALUE)
                                    except:
                                        age = -999    


                elif "Naissance" in text_normal:
                    if birth_date in text_normal:
                        split_birth_text = text_normal.split(birth_date)
                        if "Naissance" not in split_birth_text[0]:
                            birth_date = split_birth_text[2].split("Naissance")[1].split("datetime=")[1].split(" d")[0].replace('"',"").strip()
                            if birth_date[0] == "0" and birth_date[1] != "-":
                                birth_date = birth_date[1:]
                            
                            if is_alive:
                                try:
                                    start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                                    end_date = datetime.strptime(f"{today_date_str.split("-")[0]}-{str(int(today_date_str.split("-")[1]))}-{str(int(today_date_str.split("-")[2]))}", "%Y-%m-%d")
                
                                    # Get the relativedelta between two dates
                                    delta = relativedelta.relativedelta(end_date, start_date)
                                    age = delta.years
                                except:
                                    age = -999
                            else:
                                try:
                                    start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                                    end_date = datetime.strptime(f"{death_date.split("-")[0]}-{str(int(death_date.split("-")[1]))}-{str(int(death_date.split("-")[2]))}", "%Y-%m-%d")
            
                                    # Get the relativedelta between two dates
                                    delta = relativedelta.relativedelta(end_date, start_date)
                                    age = delta.years
                                                        
                                except:
                                    try:
                                        year_birth_date_ = birth_date[0:len(birth_date.split("-")[0])]
                                        year_death_date_ = death_date[0:len(death_date.split("-")[0])]
                                                            
                                        
                                        # print(death_date)
            
                                        if int(year_birth_date_) + ABSOLUTE_DATE_VALUE <= int(year_death_date_) + ABSOLUTE_DATE_VALUE:
                                            age = (int(year_death_date_) + ABSOLUTE_DATE_VALUE) - (int(year_birth_date_) + ABSOLUTE_DATE_VALUE)
                                        else:
                                            age = (int(year_birth_date_) + ABSOLUTE_DATE_VALUE) - (int(year_death_date_) + ABSOLUTE_DATE_VALUE)
                                    except:
                                        age = -999    
            except:
                pass                            

            #return

            
            #birth_date  = split_birth_text[2].split("Naissance")[1].split("datetime=")[1].split(" d")[0].replace('"',"").strip()
            #birth_date  = split_birth_text[2].split("Date de naissance")[1].split("datetime=")[1].split(" d")[0].replace('"',"").strip()
            #birth_date = text_normal.split("Date de naissance")[1].split("datetime=")[1].split(" ")[0].replace('"',"")

            # CAS OU LA DATE DE NAISSANCE/MORT ETAIT FAUSSE EX LOUIS AMSTRONG

            if page_name == "Mouammar Kadhafi":
                birth_date = "1942-01-01"
                birth_year_is_real_but_month_and_day_are_not = True
                age = 69


            try:
                if birth_date == death_date and is_alive == False:
                    if "Naissance" in text_normal:
                        birth_date = text_normal.split("Naissance")[1].split("datetime=")[1].split(" ")[0].replace('"',"")
                    if "Date de naissance" in text_normal:
                        birth_date = text_normal.split("Date de naissance")[1].split("datetime=")[1].split(" ")[0].replace('"',"")

                    try:
                        death_date = text_normal.split("Date de décès")[1].split("datetime=")[1].split(" ")[0].replace('"',"")
                    except:
                        death_date = text_normal.split("Décès")[1].split("datetime=")[1].split(" ")[0].replace('"',"")

                    if birth_date != death_date:
                        try:
                            start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                            end_date = datetime.strptime(f"{death_date.split("-")[0]}-{str(int(death_date.split("-")[1]))}-{str(int(death_date.split("-")[2]))}", "%Y-%m-%d")

                            # Get the relativedelta between two dates
                            delta = relativedelta.relativedelta(end_date, start_date)
                            age = delta.years
                                                
                        except:
                            try:
                                year_birth_date_ = birth_date[0:len(birth_date.split("-")[0])]
                                year_death_date_ = death_date[0:len(death_date.split("-")[0])]
                                                    
                                
                                # print(death_date)

                                if int(year_birth_date_) + ABSOLUTE_DATE_VALUE <= int(year_death_date_) + ABSOLUTE_DATE_VALUE:
                                    age = (int(year_death_date_) + ABSOLUTE_DATE_VALUE) - (int(year_birth_date_) + ABSOLUTE_DATE_VALUE)
                                else:
                                    age = (int(year_birth_date_) + ABSOLUTE_DATE_VALUE) - (int(year_death_date_) + ABSOLUTE_DATE_VALUE)
                            except:
                                age = -999
            except:
                pass              
            if age <= 15:
                try:
                    if born_before_chirst is False:
                        if birth_year != "Undefined" and len(str(birth_year)) != 0 and str(birth_year).isdigit() and is_alive:
                            age = int(str(self.today_date).split("-")[0]) - birth_year
                        if birth_year != "Undefined" and len(str(birth_year)) != 0 and str(birth_year).isdigit() and death_year != "Undefined" and len(str(death_year)) != 0 and str(death_year).isdigit() and is_alive is False:
                            age = death_year - birth_year
                    else:
                        if birth_year != "Undefined" and len(str(birth_year)) != 0 and str(birth_year).isdigit() and death_year != "Undefined" and len(str(death_year)) != 0 and str(death_year).isdigit() and is_alive is False:
                            age = (death_year + ABSOLUTE_DATE_VALUE) - (birth_year + ABSOLUTE_DATE_VALUE)
                except:
                    age = -999    
                    
                
                if "Notes_et_références" in text_normal:
                    if "datetime" not in text_normal.split("Notes_et_références")[0]:
                        birth_date = "Undefined"
                        birth_year = 123456789
                        birth_month = "Undefined"
                        birth_day = "Undefined"

                        if is_alive is False:
                            death_date = "Undefined"
                            death_year = 123456789
                            death_month = "Undefined"
                            death_day = "Undefined"
                if '<h2 id="Références">' in text_normal:
                    if "datetime" not in text_normal.split('<h2 id="Références">')[0]:
                        birth_date = "Undefined"
                        birth_year = 123456789
                        birth_month = "Undefined"
                        birth_day = "Undefined"

                        if is_alive is False:
                            death_date = "Undefined"
                            death_year = 123456789
                            death_month = "Undefined"
                            death_day = "Undefined"   

            if age >= 125:
                birth_date = "Undefined"
                birth_year = 123456789
                birth_month = "Undefined"
                birth_day = "Undefined"

                if is_alive is False:
                    death_date = "Undefined"
                    death_year = 123456789
                    death_month = "Undefined"
                    death_day = "Undefined"
                age = -999



            try:
                if type(birth_year) != int:
                    birth_year = 123456789
            except:
                birth_year = 123456789

            if is_alive is False:
                try:
                    if type(death_year) != int:
                        death_year = 123456789
                except:
                    death_year = 123456789

            town_birth_place = unquote(town_birth_place)
            country_birth_place = unquote(country_birth_place)
            town_death_place = unquote(town_death_place)
            country_death_place = unquote(country_death_place)


            try:
                if is_alive is False:
                    if "Naissance Date inconnu" in page_text_plain_text:
                        if len(birth_date) != 0 and "-" in birth_date:
                            death_date = birth_date
                            town_death_place = town_birth_place
                            country_death_place = country_birth_place
                            continent_of_death = continent_of_birth
                            death_year_is_real_but_month_and_day_are_not = birth_year_is_real_but_month_and_day_are_not
                            birth_year_is_real_but_month_and_day_are_not = False
                            birth_date = ""
                            town_birth_place = ""
                            country_birth_place = ""
                            continent_of_birth = ""
                    if "Décès Date inconnu" in page_text_plain_text:
                        death_date = ""
                        town_death_place = ""
                        country_death_place = ""
                        continent_of_death = ""
            except:
                pass

            if town_birth_place in JOBS:
                town_birth_place = "Undefined"

            if town_death_place in JOBS and is_alive is False:
                town_death_place = "Undefined"
        
            try:
                if "(" in town_birth_place and ")" in town_birth_place:
                    town_birth_place = town_birth_place.split("(")[0]
            except:
                town_birth_place = "Undefined"
            if "<" in str(birth_date) or ">" in str(birth_date) or "_" in str(birth_date):
                birth_date = ""
                age = -999

            if "<" in str(death_date) or ">" in str(death_date) or "_" in str(death_date):
                death_date = ""
                age = -999

            try:
                if (town_birth_place.isdigit() and " " not in town_birth_place) or (town_birth_place.split(" ")[0].isdigit() and " " in town_birth_place) or (town_birth_place.lower().split(" ")[1].lower() in LIST_OF_MONTH) or (town_birth_place.lower().split(" ")[0].lower() in LIST_OF_MONTH) or (len(town_birth_place.strip()) == 1 and town_birth_place.strip().isalpha() is False):
                    town_birth_place = "Undefined"
                    if town_birth_place.lower() in NON_TOWN_ELEMENT_LIST or "</" in town_birth_place.lower() or "www." in town_birth_place.lower() or "http" in town_birth_place.lower() or ".jp" in town_birth_place.lower() or ".png" in town_birth_place.lower() or ".wb" in town_birth_place.lower():
                        town_birth_place = "Undefined"
                    for html in HTML_ELEMENT_LIST:
                        if html.lower() in  town_birth_place:
                            town_birth_place = "Undefined"
                            break
                    
                        
            except:
                pass

            try:
                if (town_death_place.isdigit() and " " not in town_death_place) or (town_death_place.split(" ")[0].isdigit() and " " in town_death_place) or (town_death_place.split(" ")[1].lower() in LIST_OF_MONTH) or (town_death_place.split(" ")[0].lower() in LIST_OF_MONTH) and is_alive is False or (len(town_death_place.strip()) == 1 and town_death_place.strip().isalpha() is False):        
                    town_death_place = "Undefined"
                    if town_death_place.lower() in NON_TOWN_ELEMENT_LIST or "</" in town_death_place or "www." in town_death_place or "http" in town_death_place or ".jp" in town_death_place or ".png" in town_death_place or ".wb" in town_death_place:
                        town_death_place = "Undefined"
                    for html in HTML_ELEMENT_LIST:
                        if html.lower() in  town_death_place:
                            town_death_place = "Undefined"
                            break
                    
                                        
            except:
                pass

            job = unquote(job)
            if town_birth_place in self.list_of_country:
                country_birth_place = town_birth_place
                town_birth_place = "Undefined"
                town_birth_place_href = "Undefined"

            if town_death_place in self.list_of_country and is_alive is False:
                country_birth_place = town_death_place
                town_death_place = "Undefined"
                town_death_place_href = "Undefined"


            if len(town_birth_place) > 1:
                if town_birth_place[-1] == ",":
                    town_birth_place = town_birth_place[0:-1]

            if len(town_death_place) > 1:
                if town_death_place[-1] == ",":
                    town_death_place = town_death_place[0:-1]
            
            if town_birth_place != "Undefined" and len(town_birth_place) != 0:
                town_birth_place = unquote(town_birth_place)
                town_birth_place_href = unquote(town_birth_place_href)

                if "(" in town_birth_place and ")" not in town_birth_place:
                    town_birth_place = town_birth_place + ")"

                if "(" in town_birth_place_href and ")" not in town_birth_place_href:
                    town_birth_place_href = town_birth_place_href + ")"
                
                birth_town_localisation = self.get_localisation_of_a_town(town_birth_place)
                if birth_town_localisation == "Undefined" or len(birth_town_localisation) == "" and town_birth_place_href != "":
                    birth_town_localisation = self.get_localisation_of_a_town(town_birth_place_href)
                if "à" in birth_town_localisation and town_birth_place_href != "Undefined" and len(town_birth_place_href) != 0:
                    birth_town_localisation = self.get_localisation_of_a_town(town_birth_place_href)
                if "à" in birth_town_localisation:
                    birth_town_localisation = "Undefined"                


            try:
                if self.clean_localisation(birth_town_localisation.lower()) in LIST_OF_GOOD_LOCALISATION:
                    country_birth_place = DICT_OF_LOCALISATION_TO_COUNTRY[self.clean_localisation(birth_town_localisation.lower())]
            except:
                pass
            try:
                if self.clean_localisation(death_town_localisation.lower()) in LIST_OF_GOOD_LOCALISATION and is_alive is False:
                    country_death_place = DICT_OF_LOCALISATION_TO_COUNTRY[self.clean_localisation(death_town_localisation.lower())]
            except:
                pass                
            job_ = job
            try:
                job = WIKIJOB_TO_JOB_DICT_MAN[job.lower()]
                if gender == "Woman":
                    job = WIKIJOB_TO_JOB_DICT_WOMAN[job.lower()]

            except:
                job = job_

            
            try:
                if job[-1] == "." or job[-1] == ",":
                    job = job[0:-1]
            except:
                job = "Undefined"
            

            if birth_date == "Undefined":
                age = -999       
            if is_alive is False:
                if town_death_place != "Undefined" and len(town_death_place) != 0:
                    town_death_place = unquote(town_death_place)
                    town_death_place_href = unquote(town_death_place_href)
                    if "(" in town_death_place and ")" not in town_death_place:
                        town_death_place = town_death_place + ")"

                    if "(" in town_death_place_href and ")" not in town_death_place_href:
                        town_death_place_href = town_death_place_href + ")"
                    
                    death_town_localisation = self.get_localisation_of_a_town(town_death_place)
                    if death_town_localisation == "Undefined" or len(death_town_localisation) == "" and town_death_place_href != "":
                        death_town_localisation = self.get_localisation_of_a_town(town_death_place_href)
                    if "à" in death_town_localisation and town_death_place_href != "Undefined" and len(town_death_place_href) != 0:
                        death_town_localisation = self.get_localisation_of_a_town(town_death_place_href)
                    if "à" in death_town_localisation:
                        death_town_localisation = "Undefined"      
                    


            for html in HTML_ELEMENT_LIST:
                if html.lower() in town_birth_place.lower().replace("\n"," ").strip():
                    town_birth_place = "Undefined"
                    break
            for html in HTML_ELEMENT_LIST:
                if html.lower() in town_death_place.lower().replace("\n"," ").strip() and is_alive is False:
                    town_death_place = "Undefined"
                    break

            for html in HTML_ELEMENT_LIST:
                if html.lower() in town_birth_place_href.lower().replace("\n"," ").strip():
                    town_birth_place_href = "Undefined"
                    break
            for html in HTML_ELEMENT_LIST:
                if html.lower() in town_death_place_href.lower().replace("\n"," ").strip() and is_alive is False:
                    town_death_place_href = "Undefined"
                    break

            if town_birth_place == town_death_place and len(birth_town_localisation) != 0 and len(town_birth_place) != 0:
                death_town_localisation = birth_town_localisation

            if town_birth_place == town_death_place and len(death_town_localisation) != 0 and len(town_birth_place) != 0:
                death_town_localisation = birth_town_localisation

            if birth_town_localisation == death_town_localisation:
                if len(country_birth_place) != 0 and len(country_death_place) == 0:
                    country_death_place = country_birth_place

                if len(country_death_place) != 0 and len(country_birth_place) == 0:
                    country_death_place = country_birth_place

            if birth_town_localisation == "Undefined":
                country_birth_place = "Undefined"

            if death_town_localisation == "Undefined" and is_alive is False:
                death_town_localisation = "Undefined"

            if "_" in country_birth_place:
                country_birth_place = country_birth_place.replace("_","  ")
            if "_" in country_death_place:
                country_death_place = country_death_place.replace("_","  ")
            
            if "-" in country_birth_place:
                country_birth_place = country_birth_place.replace("-","  ")
            if "-" in country_death_place:
                country_death_place = country_death_place.replace("-","  ")


            country_birth_place_emoji = "🏳️"
            country_death_place_emoji = "🏳️"
                        
            special_name_country_list = []
            for country in COUNTRY_NORMALIZATION_DICT:
                special_name_country_list.append(country)

            if country_birth_place.lower() in special_name_country_list:
                country_birth_place = COUNTRY_NORMALIZATION_DICT[country_birth_place.lower()]
            
            if country_birth_place.lower() not in self.list_of_country_lower:
                country_birth_place = "Undefined"

            if country_birth_place.lower() not in self.list_of_country_lower:
                country_birth_place = "Undefined"


            try:
                if country_birth_place.lower() in self.list_of_country_lower:
                    country_birth_place_emoji = country_to_flag_dict[country_birth_place.lower().replace("-"," ").strip()]
            except:
                pass    
                        
            if country_death_place.lower() in special_name_country_list and is_alive is False:
                country_death_place = COUNTRY_NORMALIZATION_DICT[country_death_place.lower()]
            
            if country_death_place.lower() not in self.list_of_country_lower and is_alive is False:
                country_death_place = "Undefined"

            try:
                if country_death_place.lower() in self.list_of_country_lower and is_alive is False:
                    country_death_place_emoji = country_to_flag_dict[country_death_place.lower().replace("-"," ").strip()]
            except:
                pass
            if country_birth_place != "Undefined" and len(country_birth_place) != 0:
                continent_of_birth = self.country_to_continent(country_birth_place)

            if country_death_place != "Undefined" and len(country_death_place) != 0:
                continent_of_death = self.country_to_continent(country_death_place)
            
            if job == "" or job == "Undefined":
                job = "Undefined"
                preciseness_level -= 20
                list_of_unpreciseness_data.append("job is unknown")


            
            if birth_date == "<!DOCTYPE":
                return


            try:
                if birth_year_is_real_but_month_and_day_are_not and "-01-01" in birth_date:
                    birth_date = birth_date.replace("-01-01","-13-99")
            except:
                pass
            try:

                if death_year_is_real_but_month_and_day_are_not and "-01-01" in death_date:
                    death_date = death_date.replace("-01-01","-13-99")
            except:
                pass



            try:
                    if "u" in birth_date:
                        birth_date = "unedefined"
                        birth_day = "unedefined"
                        birth_month = "unedefined"
                        birth_year = 123456789
            except:
                pass
            try:
            
                if "u" in death_date:
                    death_date = "unedefined"
                    death_day = "unedefined"
                    death_month = "unedefined"
                    death_year = 123456789
            except:
                pass
            if town_birth_place == "" or town_birth_place == "Undefined":
                preciseness_level -= 20
                #print("town_birth_place is bad")
                list_of_unpreciseness_data.append("town_birth_place is unknown")

            if birth_town_localisation == "" or birth_town_localisation == "Undefined":
                preciseness_level -= 10
                list_of_unpreciseness_data.append("birth town localisation is unknown")

            if country_birth_place == "" or country_birth_place == "Undefined":
                preciseness_level -= 20
                #print("country_birth_place is bad")
                list_of_unpreciseness_data.append("country_birth_place is unknown")
            if birth_date_is_between_two_date:
                preciseness_level -= 20
                list_of_unpreciseness_data.append("birthdate is between two date")
            if birth_year_is_real_but_month_and_day_are_not:
                preciseness_level -= 10
                list_of_unpreciseness_data.append("birth year is real but month and day are not")
            if death_year_is_real_but_month_and_day_are_not:
                preciseness_level -= 10
                list_of_unpreciseness_data.append("death year is real but month and day are not")

            if is_alive is False:
                if town_death_place == "" or town_death_place == "Undefined":
                    preciseness_level -= 20
                    #print("town_death_place is bad")
                    list_of_unpreciseness_data.append("town_death_place is unknown")

                if country_death_place == "" or country_death_place == "Undefined":
                    preciseness_level -= 20
                    list_of_unpreciseness_data.append("country_death_place is unknown")
                if death_town_localisation == "" or death_town_localisation == "Undefined":
                    preciseness_level -= 10
                    list_of_unpreciseness_data.append("death town localisation is unknown")

                if birth_date == death_date and birth_year != 123456789:
                    preciseness_level -= 40
                    list_of_unpreciseness_data.append("birth_date and death_date may be the same")
                    #print("birth_date == death_date")
                
                if birth_date == death_date and birth_year == 123456789:
                    preciseness_level -= 50
                    list_of_unpreciseness_data.append("birth_date and death_date are wrong")
                    #print("birth_date == death_date")
                

            try:
                if len(birth_date) < 2:
                    preciseness_level -= 30
                    list_of_unpreciseness_data.append("birth_date is bad")
                    #print("birth_date is bad")
            except:
                preciseness_level -= 30
                list_of_unpreciseness_data.append("birth_date is bad")

            if gender == "Unclear":
                preciseness_level -= 20
                list_of_unpreciseness_data.append("gender is unclear")
            if is_alive is False:
                try:
                    if len(death_date) < 2:
                        preciseness_level -= 30
                        list_of_unpreciseness_data.append("death_date is bad")
                        #print("death_date is bad")
                except:
                    preciseness_level -= 30
                    list_of_unpreciseness_data.append("death_date is bad")

            if continent_of_birth == "" or continent_of_birth == "Undefined":
                preciseness_level -= 10
                list_of_unpreciseness_data.append("continent of birth is unknown")
            if (continent_of_death == "" or continent_of_death == "Undefined") and is_alive is False:
                preciseness_level -= 10
                list_of_unpreciseness_data.append("continent of death is unknown")

            try:
                birth_year = int(birth_date.split("-")[0])

                if birth_year < 1900 or "-" in str(birth_year):
                    preciseness_level -= 10
                    list_of_unpreciseness_data.append("birth_date is before the year 1900")
                    #print("birth_date is imprecise")
            except Exception:
                pass

            if age == -999:
                preciseness_level -= 10
                list_of_unpreciseness_data.append("age is unknown")

            
            if age <= 15 and is_alive is False:
                preciseness_level -= 10
                list_of_unpreciseness_data.append("age is unknown/younger than 16 and birth_date/death_date may be unknown too")
            
            try:
                birth_year = int(birth_date.split("-")[0])
                death_year = int(death_date.split("-")[0])

                if birth_year > death_year and is_alive is False:
                    preciseness_level -= 40
                    list_of_unpreciseness_data.append("birth_date is after death_date")
                    #print("birth_date and death_date are imprecise")
            except Exception:
                pass

            try:
                birth_year = int(birth_date.split("-")[0])
                death_year = int(death_date.split("-")[0])

                if birth_year == death_year and is_alive is False:
                    preciseness_level -= 20
                    list_of_unpreciseness_data.append("birth_date year is the same as death_date year so one of the date is wrong")
                    #print("birth_date and death_date are imprecise")
            except Exception:
                pass

            if born_before_chirst:
                #print("user is born before christ")
                list_of_unpreciseness_data.append("User is born before christ")
                preciseness_level-= 30

            # try:
            #     death_year = int(death_date.split("-")[0])
            #     if death_year < 1900 or "-" not in death_date:
            #         preciseness_level -= 10
            #         print("death_date is imprecise")
            # except Exception:
            #     pass





            print_data = False

            if int(preciseness_level/2) < MINIMAL_PRECISSENES_SCORE:
                print_data = True



            if birth_date == "":
                birth_date = "Undefined"

            if is_alive:
                death_date = "alive"
                country_death_place = "alive"
                continent_of_death = "alive"
                region_of_death = "alive"
            else:
                if death_date == "":
                    death_date = "Undefined"
                if town_birth_place == "":
                    town_birth_place = "Undefined"
                if country_death_place == "":
                    country_death_place = "Undefined"
                if continent_of_death == "":
                    continent_of_death = "Undefined"

            
            if force_print_data:
                print_data = True
            else:
                print_data = False
            if town_birth_place == "" or town_birth_place == "Undefined":
                if country_birth_place.lower().strip().replace("  "," ").replace("   "," ").replace("    "," ").replace("-"," ") not in self.list_of_country_lower:
                    country_birth_place = "Undefined"
                birth_town_localisation = "Undefined"
                continent_of_birth = "Undefined"

            if (town_death_place == "" or town_birth_place == "Undefined") and is_alive is False:
                if country_death_place.lower().strip().replace("  "," ").replace("   "," ").replace("    "," ").replace("-"," ") not in self.list_of_country_lower:
                    country_death_place = "Undefined"
                
                death_town_localisation = "Undefined"
                continent_of_death = "Undefined"



            # do_after = True
            # if do_after:
            try:
                power_ranking = int(self.power_ranking_json[page_name.replace("_","")])
                position = list(self.power_ranking_json.keys()).index(page_name.replace("_","")) + 1
                last_position = len(list(self.power_ranking_json.keys()))
                if position == 1:
                    position = 0
                position_pourcentage = round((position * 100) / last_position,2)

                if str(round((position * 100) / last_position,4))[0] == "0":
                    position_pourcentage = round((position * 100) / last_position,5)
                position_pourcentage_20 = round(20 - round(((position * 100) / last_position) / 5 , 2),2)
            except:
                power_ranking = 0
                position = -999
                last_position = len(list(self.power_ranking_json.keys()))
                position_pourcentage = -999
                position_pourcentage_20 = -999

        
            # power_ranking = 0
            # position = -999
            # last_position = len(list(self.power_ranking_json.keys()))
            # position_pourcentage = -999
            # position_pourcentage_20 = -999

            # power_ranking = 0
            # position = 0
            # position_pourcentage = 0

            time_period_of_birth = "Undefined"
            birth_month = "Undefined"
            birth_day = "Undefined"
            death_month = "Undefined"
            death_day = "Undefined"
            death_year = 123456789
                        
            if is_alive:
                death_month = "alive"
                death_day = "alive"
                death_year = 123456789


            #print(birth_date)
            #NUMBER_TO_MONTH_DICT
            try:
                if born_before_chirst:
                    birth_year = int(birth_date.split("-")[1]) * -1
                    birth_month = NUMBER_TO_MONTH_DICT[birth_date.split("-")[2]]
                    birth_day = birth_date.split("-")[3]

                else:
                    birth_year = int(birth_date.split("-")[0])
                    birth_month = NUMBER_TO_MONTH_DICT[birth_date.split("-")[1]]
                    birth_day = birth_date.split("-")[2]

                if birth_year_is_real_but_month_and_day_are_not:
                    birth_month = "Fluriel"
                    birth_day = "99"
            except:
                birth_year = 123456789

            try:
                if died_before_christ:
                    death_year = int(death_date.split("-")[1]) * -1
                    death_month = NUMBER_TO_MONTH_DICT[death_date.split("-")[2]]
                    death_day = death_date.split("-")[3]

                else:
                    death_year = int(death_date.split("-")[0])
                    death_month = NUMBER_TO_MONTH_DICT[death_date.split("-")[1]]
                    death_day = death_date.split("-")[2]

                if death_year_is_real_but_month_and_day_are_not:
                    death_month = "Fluriel"
                    death_month = NUMBER_TO_MONTH_DICT[death_date.split("-")[1]]
                    death_day = death_date.split("-")[2]
                    death_day = "99"
            except:
                if is_alive:
                    death_year = "alive"
                else:
                    death_year = 123456789
                                
            if birth_year != "Undefined" and len(str(birth_year)) != 0:
                time_period_of_birth = self.birth_year_to_time_period(birth_year)

            # try:
            #     power_ranking = self.power_ranking_json[page_name.replace("_","")]
            # except:
            #     power_ranking = 0

            if country_birth_place == "":
                country_birth_place = "Undefined"
            if birth_date == "":
                birth_date = "Undefined"
            if continent_of_birth == "":
                continent_of_birth = "Undefined"
            if continent_of_death == "":
                continent_of_death = "Undefined"
            if job == "":
                job = "Undefined"

            if town_birth_place == "":
                town_birth_place = "Undefined"

            if birth_town_localisation == "":
                birth_town_localisation = "Undefined"

            

            if death_town_localisation == "":
                death_town_localisation = "Undefined"

            if country_death_place == "":
                country_death_place = "Undefined"

            if death_date == "":
                death_date = "Undefined"

            if gender == "":
                gender = "Undefined"

            if "<" in town_death_place or ">" in town_death_place:
                town_death_place = "Undefined"
            if "<" in town_birth_place or ">" in town_birth_place:
                town_death_place = "Undefined"

            birth_month_day = "Undefined"
            death_month_day = "Undefined"

            try:
                if birth_day != "Undefined" and birth_month != "Undefined":
                    birth_month_day = f"{birth_day}-{birth_month}"
            except:
                pass

            try:
                if death_day != "Undefined" and death_month != "Undefined" and is_alive is False:
                    death_month_day = f"{death_day}-{death_month}"
            except:
                pass                
            if is_alive:
                death_month_day = "alive"
            

            first_name = "Undefined"
            last_name = "Undefined"
            first_name_standard = "Undefined"
            last_name_standard = "Undefined"

            page_name_copy = page_name
            if " " in page_name_copy:
                first_name = page_name_copy.split(" ")[0].strip()
                last_name = page_name_copy.split(" ", 1)[1].strip()
                if "(" in last_name:
                    last_name = last_name.split("(")[0].strip()

            
            first_name = unquote(first_name)
            last_name = unquote(last_name)
            region_of_birth = self.country_to_region_of_the_world(country_birth_place)
            region_of_death = "alive"
            if is_alive == False:
                region_of_death = self.country_to_region_of_the_world(country_death_place)

            born_and_died_in_the_same_town = "alive"
            born_and_died_in_the_same_country = "alive"
            born_and_died_in_the_same_continent = "alive"
            born_and_died_in_the_same_region = "alive"
            if town_birth_place_href == "" or town_birth_place_href == "Undefined":
                town_birth_place_href = town_birth_place

            if is_alive is False:
                if town_death_place_href == "" or town_death_place_href == "Undefined":
                    town_death_place_href = town_death_place
                            
            if is_alive:
                town_death_place_href = "alive"

            if is_alive is False:
                born_and_died_in_the_same_town = False
                born_and_died_in_the_same_country = False
                born_and_died_in_the_same_continent = False
                born_and_died_in_the_same_region = False
                if town_birth_place == town_death_place and town_birth_place != "Undefined" and len(town_birth_place) != 0:
                    born_and_died_in_the_same_town = True
                if country_birth_place == country_death_place and country_birth_place != "Undefined" and len(country_birth_place) != 0:
                    born_and_died_in_the_same_continent = True
                if continent_of_birth == continent_of_death and continent_of_birth != "Undefined" and len(continent_of_birth) != 0:
                    born_and_died_in_the_same_continent = True
                if region_of_birth == region_of_death and region_of_birth != "Undefined" and len(region_of_birth) != 0:
                    born_and_died_in_the_same_region = True


            #all_links_of_a_page = self.get_all_links_of_a_page(page_name)
            all_links_of_a_page = self.list_of_link_of_user[page_name]
            all_links_of_a_page = self.remove_bad_link_of_an_user(all_links_of_a_page)
            number_of_links = len(all_links_of_a_page)
            if " " in page_name:
                first_name = page_name.split(" ")[0]

            #print(print_data,print_data,print_data)  
            #print_data = False
            if town_birth_place_href != "Undefined" and len(town_birth_place_href) != 0 and len(town_birth_place) < len(town_birth_place_href) and town_birth_place in town_birth_place_href:
                town_birth_place = town_birth_place_href.replace("_"," ")

            if town_death_place_href != "Undefined" and len(town_death_place_href) != 0 and len(town_death_place) < len(town_death_place_href) and town_death_place in town_death_place_href:
                town_death_place = town_death_place_href.replace("_"," ")

            if country_birth_place.lower() in NON_COUNTRY_ELEMENTS:
                country_birth_place = "Undefined"
            if country_death_place.lower() in NON_COUNTRY_ELEMENTS:
                country_death_place = "Undefined"

            if town_birth_place.lower() in NON_TOWN_ELEMENT_LIST or "↑" in town_birth_place or "</" in town_birth_place.lower() or "www." in town_birth_place.lower() or "http" in town_birth_place.lower() or ".jp" in town_birth_place.lower() or ".png" in town_birth_place.lower() or ".wb" in town_birth_place.lower():
                town_birth_place = "Undefined"
                town_birth_place_href = "Undefined"
            if town_death_place.lower() in NON_TOWN_ELEMENT_LIST or "↑" in town_death_place or "</" in town_death_place.lower() or "www." in town_death_place.lower() or "http" in town_death_place.lower() or ".jp" in town_death_place.lower() or ".png" in town_death_place.lower() or ".wb" in town_death_place.lower() and is_alive is False:
                town_death_place = "Undefined"
                town_death_place_href = "Undefined"

            NON_TOWN_ELEMENT_LIST_LOWER = []
            for elem in NON_TOWN_ELEMENT_LIST:
                NON_TOWN_ELEMENT_LIST_LOWER.append(elem.lower())

            if town_birth_place.lower().strip() in NON_TOWN_ELEMENT_LIST_LOWER:
                town_birth_place = "Undefined"
                town_birth_place_href = "Undefined"
            if town_death_place.lower().strip() in NON_TOWN_ELEMENT_LIST_LOWER:
                town_death_place = "Undefined"
                town_death_place_href = "Undefined"

            if is_alive is False:
                if town_death_place == "" or town_death_place == "Undefined" and "town_death_place is unknown" not in list_of_unpreciseness_data:
                    preciseness_level -= 20
                    #print("town_death_place is bad")
                    list_of_unpreciseness_data.append("town_death_place is unknown")

            if town_birth_place == "" or town_birth_place == "Undefined" and "town_birth_place is unknown" not in list_of_unpreciseness_data:
                preciseness_level -= 20
                #print("town_birth_place is bad")
                list_of_unpreciseness_data.append("town_birth_place is unknown")


            born_and_died_on_the_same_day = False
            try:
                if is_alive is False:
                    if "fluriel" not in f"{birth_month_day.lower()}{death_month_day.lower()}" and birth_month_day == death_month_day:
                        born_and_died_on_the_same_day = True
            except:
                pass

            try:
                if len(town_birth_place) != 0:
                    if "(" in town_birth_place and ")" in town_birth_place:
                        for country in self.list_of_country:
                            if f"({country.lower()})" in town_birth_place.lower():
                                country_birth_place = country

            except:
                pass

            try:
                if len(town_death_place) != 0 and is_alive is False:
                    if "(" in town_death_place and ")" in town_death_place:
                        for country in self.list_of_country:
                            if f"({country.lower()})" in town_death_place.lower():
                                country_death_place = country

            except:
                pass
            
            if print_data:
                print(f"Page name: {page_name}")
                print(f"Page url: https://fr.wikipedia.org/wiki/{page_name.replace(" ","_")}")
                print(f"Picture url: {picture_url}")
                print(f"First name: {first_name}")
                print(f"Last name: {last_name}")
                print(f"Job: {job}")
                print(f"Town birth place: {town_birth_place}")
                print(f"Town birth place href: {town_birth_place_href}")
                print(f"Birth Town localisation: {birth_town_localisation}")
                print(f"Country birth place: {country_birth_place}")
                print(f"Country birth place emojie: {country_birth_place_emoji}")
                print(f"Birth year time period: {time_period_of_birth}")
                if continent_of_birth != "Undefined" and len(continent_of_birth) != 0:
                    print(f"Continent of birth: {continent_of_birth}")

                print(f"Region of birth: {region_of_birth}")
                if is_alive is False:
                    print(f"Town death place: {town_death_place}")
                    print(f"Town death place href: {town_death_place_href}")
                    print(f"Death Town localisation: {death_town_localisation}")
                    print(f"Country death place: {country_death_place}")
                    print(f"Country death place emojie: {country_death_place_emoji}")
                                    

                if continent_of_death != "Undefined" and len(continent_of_death) != 0 and is_alive is False:
                    print(f"Continent of death: {continent_of_death}")

                print(f"Region of death {region_of_death}")
                if is_alive is False:
                    print(f"born_and_died_in_the_same_town: {born_and_died_in_the_same_town}")
                    print(f"born_and_died_in_the_same_country: {born_and_died_in_the_same_continent}")
                    print(f"born_and_died_in_the_same_continent: {born_and_died_in_the_same_continent}")
                    print(f"born_and_died_in_the_same_region: {born_and_died_in_the_same_region}")
                    print(f"born_and_died_on_the_same_day: {born_and_died_on_the_same_day}")

                print(f"Birth date: {birth_date}")
                print(f"Birth year: {birth_year}")
                print(f"Birth month: {birth_month}")
                print(f"Birth day: {birth_day}")
                print(f"Birth day withouth year: {birth_month_day}")

                if is_alive is False:
                    print(f"Death date: {death_date}")
                    print(f"Death year: {death_year}")
                    print(f"Death month: {death_month}")
                    print(f"Death day: {death_day}")
                    print(f"Death day withouth year: {death_month_day}")
                
                print(f"Born before Christ: {born_before_chirst}")

                if is_alive is False:
                    print(f"Dead before Christ: {died_before_christ}")
                print(f"Age: {age}")
                print(f"Is Alive: {is_alive}")
                print(f"Gender: {gender}")
                print(f"Power ranking: {power_ranking}")
                print(f"Positition: {position}/{last_position}")
                print(f"Position %: {position_pourcentage}")
                print(f"Grade: {position_pourcentage_20}/20")
                print(f"Number of wikipedia page: {last_position}")
                print(f"First char of the page {page_name[0].lower()}")
                print(f"Wikipedia page lenght: {len(whole_page_text_plain_text)}")
                print(f"All links of the page: {all_links_of_a_page}")
                print(f"Number of links: {number_of_links}")
                print(f"Preciseness Level {int(preciseness_level/2)}")
                print(f"List of unpreciseness data {list_of_unpreciseness_data}")
                print(f"Today date: {today_date_str}")
                print("\n"*5)

            born_and_died_before_christ = False
            born_and_died_after_christ = False
            born_before_christ_and_died_after_christ = False

            birth_town_localisation = unicodedata.normalize("NFKC", birth_town_localisation)
            birth_town_localisation = " ".join(birth_town_localisation.split())

            death_town_localisation = unicodedata.normalize("NFKC", death_town_localisation)
            death_town_localisation = " ".join(death_town_localisation.split())


            if born_before_chirst and died_before_christ:
                born_and_died_before_christ = True
                born_and_died_after_christ = False
            if born_before_chirst and died_before_christ is False:
                born_before_christ_and_died_after_christ = True

            # if page_name not in self.list_of_wikipedia_page_of_real_people:
            #     write_into_file("list_of_wikipedia_page_of_real_people.txt",page_name+"\n")

            if page_name[0] == "'":
                page_name = page_name[1:]
                page_name = "%27"+page_name

            # print(f"Positition: {position}/{last_position}")
            # print(f"Position %: {position_pourcentage}")
            # print(f"Number of wikipedia page: {last_position}")
            list_of_page_linked_to = []
            number_of_page_linked_to = 0
            user_info_dict = {
                "page_name":page_name,
                "page_url":f"https://fr.wikipedia.org/wiki/{page_name.replace(" ","_")}",
                "picture_url":picture_url,
                "first_name":first_name.lower(),
                "first_name_standard":unidecode(first_name.lower()),
                "last_name":last_name.lower(),
                "last_name_standard":unidecode(last_name.lower()),                
                "job":job,
                "town_birth_place":town_birth_place.strip().replace("  "," ").replace("   "," ").replace("    "," "),
                "town_birth_place_href":town_birth_place_href,
                "birth_town_localisation":birth_town_localisation,
                "country_birth_place":country_birth_place.strip().replace("  "," ").replace("   "," ").replace("    "," "),
                "time_period_of_birth":time_period_of_birth,
                "continent_of_birth":continent_of_birth,
                "region_of_birth":region_of_birth,
                "birth_date":birth_date,
                "birth_year":birth_year,
                "birth_month":birth_month,
                "birth_day":birth_day,
                "birth_month_day":birth_month_day,
                "town_death_place":town_death_place.strip().replace("  "," ").replace("   "," ").replace("    "," "),
                "town_death_place_href":town_death_place_href,       
                "town_death_localisation":death_town_localisation,
                "country_death_place":country_death_place.strip().replace("  "," ").replace("   "," ").replace("    "," "),
                "continent_of_death":continent_of_death,
                "region_of_death":region_of_death,
                "born_and_died_in_the_same_town":born_and_died_in_the_same_town,
                "born_and_died_in_the_same_country":born_and_died_in_the_same_country,
                "born_and_died_in_the_same_continent":born_and_died_in_the_same_continent,
                "born_and_died_in_the_same_region":born_and_died_in_the_same_region,
                "born_and_died_on_the_same_day":born_and_died_on_the_same_day,
                "death_date":death_date,
                "death_year":death_year,
                "death_month":death_month,
                "death_day":death_day,
                "death_month_day":death_month_day,
                "born_before_christ":born_before_chirst,
                "died_before_christ":died_before_christ,
                "born_and_died_before_christ":born_and_died_before_christ,
                "born_and_died_after_christ":born_and_died_after_christ,
                "born_before_christ_and_died_after_christ":born_before_christ_and_died_after_christ,
                "age":age,
                "is_alive":is_alive,
                "gender":gender,
                "power_ranking":power_ranking,
                "position":position,
                "position_percentage":position_pourcentage,
                "grade_over_20":position_pourcentage_20,
                "first_char_of_the_page":unquote(page_name[0].lower()),
                "wikipedia_page_length":len(whole_page_text_plain_text),
                "all_links_of_a_page":all_links_of_a_page,
                "number_of_links":number_of_links,
                "preciseness_level":int(preciseness_level/2),
                "list_of_unpreciseness_data":list_of_unpreciseness_data,
                "country_birth_place_emoji":country_birth_place_emoji,
                "country_death_place_emoji":country_death_place_emoji
            }

            # # A faire apres
            # "list_of_page_linked_to":list_of_page_linked_to,
            # "number_of_page_linked_to":number_of_page_linked_to,
            # #

            print_data = False
            if print_data:
                if int(preciseness_level/2) < MINIMAL_PRECISSENES_SCORE and force_print_data:
                    print(user_info_dict)
                    print("-------"*120)
            #print('Years, Months, Days between two dates is')
            #print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
            if page_nb != -999:
                write_into_file(f"user_info_dict{page_nb}.txt",str(user_info_dict)+"\n")
            return True
        except:
            traceback.print_exc()
            print("PAGE NAME:" , page_name)
            if page_nb != -999:
                write_into_file(f"flop_info_dict{page_nb}.txt",f"{page_name}"+"\n")
            # if page_name not in self.list_of_wikipedia_page_of_real_people:
            #     write_into_file("list_of_wikipedia_page_of_real_people.txt",page_name+"\n")

            # if page_name[0] == "'":
            #     page_name = page_name[1:]
            #     page_name = "%27"+page_name


            # print(f"https://fr.wikipedia.org/wiki/{page_name.replace(" ","_")}")
            #return False

    def remove_page_name_from_link(self,page_name,list_of_link):
        """A function that remove page name from link"""
        new_list_of_link = []

        if page_name not in list_of_link:
            return list_of_link

        for link in list_of_link:
            if page_name != link and page_name in self.all_real_people_set:
                new_list_of_link.append(link)

        return new_list_of_link

    def calc_stat(self):
        """A function that calc stats of all wikipedia page"""
        list_of_dict_link = print_file_content("user_info_dict.txt").split("\n")
        nb_total = 0
        nb_total_with_link = 0
        nb_of_people_withouth_link = 0
        nb_of_people_with_link = 0
        list_of_link_nb = []
        list_of_link_name = []

        list_of_link_name2 = []
        list_of_link_name_ = []

        dict_of_number_of_link_per_page_sorted = {}
        dict_of_people_who_are_the_most_linked_sorted = {}
        dict_of_wikipedia_page_length_sorted = {}
        list_of_link_name_occurence = []
        for i , link in enumerate(list_of_dict_link):
            if i % 93000 == 0:
                #print(link , int(i/93000) * 10)
                print(int(i/93000) * 10)

            try:
                current_dict = ast.literal_eval(link)
                name = current_dict["page_name"]

                # print(type(current_dict["list_of_name"]))
                # print(current_dict["list_of_name"])

                list_of_link = self.remove_page_name_from_link(current_dict["page_name"],current_dict["all_links_of_a_page"])
                nb_total+=len(list_of_link)
                list_of_link_nb.append(len(list_of_link))
                list_of_link_name.append(name)
                list_of_link_name_.append(name)
                for elem in list_of_link:
                    list_of_link_name2.append(elem.strip())

                if len(list_of_link) == 0:
                    nb_of_people_withouth_link+=1
                else:
                    nb_of_people_with_link+=1
                    nb_total_with_link+=len(list_of_link)


            except:
                list_of_link_nb.append(0)
                list_of_link_name.append(name)

        # for name in list_of_link_name:
        #     list_of_link_name_occurence.append(list_of_link_name2.count(name))

        print("Occurrences in list_of_link_name2:",
          sum(x == "Ray Charles" for x in list_of_link_name2))
        counts = Counter(list_of_link_name2)

        print(counts["Ray Charles"])

        idx = list_of_link_name.index("Ray Charles")
        print(list_of_link_name.index("Ray Charles"))
        
        list_of_link_name_occurence = [
            counts.get(name.strip(), 0)
            for name in list_of_link_name
        ]
        len_all_wikipedia_fr_page =  4583129
        print(f"Number of people on the whole wikipedia fr {len(list_of_dict_link)}")
        print(f"Number of total link of the whole wikipedia fr {nb_total}")
        print(f"Average number of link per person on the whole wikipedia fr {round(len(list_of_dict_link)/nb_total,2)}")
        print(f"Number of people withouth a link on the whole wikipedia fr {nb_of_people_withouth_link}")
        print(f"% of people withouth a link on the whole wikipedia fr {int((nb_of_people_withouth_link/len(list_of_dict_link)) * 100)}")
        print(f"Number of people with a link on the whole wikipedia fr {len(list_of_dict_link) - nb_of_people_withouth_link}")
        print(f"% of people with a link on the whole wikipedia fr {100 - int((nb_of_people_withouth_link/len(list_of_dict_link)) * 100)}")
        print(f"Average number of link per person who have atleast 1 link on the whole wikipedia fr {round((nb_of_people_with_link - nb_of_people_withouth_link)/nb_total_with_link,2)}")
        print(f"Average wikipedia page per user 5306")
        paired = list(zip(list_of_link_name, list_of_link_nb))
        paired.sort(key=lambda x: x[1], reverse=True)

        nb_link_by_user = 0
        nb_link_by_page = 0
        try:
            list_of_element, occurence_of_element_list = zip(*paired)
        except:
            return [] , []
        list_of_element = list(list_of_element)
        occurence_of_element_list = list(occurence_of_element_list)

        for i in range(10):
            print("Most Link on this page: " ,list_of_element[i],occurence_of_element_list[i])

        for i in range(len(list_of_element)):
            dict_of_number_of_link_per_page_sorted[list_of_element[i]] = occurence_of_element_list[i]
        nbz = 500
        nb_link_by_page = sum(occurence_of_element_list[0:nbz])
        paired = list(zip(list_of_link_name_, list_of_link_name_occurence))
        paired.sort(key=lambda x: x[1], reverse=True)
        try:
            list_of_element, occurence_of_element_list = zip(*paired)
        except:
            return [] , []
        list_of_element = list(list_of_element)
        occurence_of_element_list = list(occurence_of_element_list)
        print("\n\n\n\n")

        for i in range(len(list_of_element)):
            dict_of_people_who_are_the_most_linked_sorted[list_of_element[i]] = occurence_of_element_list[i]

        for i in range(10):
            print("Most Linked user: " , list_of_element[i],occurence_of_element_list[i])

        nb_link_by_user = sum(occurence_of_element_list[0:nbz])
        page_size_of_the_top_500_user = 76198514
        nb_link_by_page_size = int(page_size_of_the_top_500_user / nb_link_by_page)
        print(nb_link_by_page_size)
        nb_link_by_page_size = 310
        merged_data_name = []
        merged_data_value = []
        merged_data_dict = {}

        print(nb_link_by_page)
        print(nb_link_by_user)
        print(nb_link_by_user/nb_link_by_page)

        #  100 5.49
        #  250 4.30
        #  500 3.67
        #  1000 3.13
        #  10000 1.86

        # 152397

        with open("list_of_wikipedia_page_length.json", "r", encoding="utf-8") as file:
            pages_lenght = json.load(file)


        list_of_page_name = []
        list_of_page_size = []
        for name , lenght in pages_lenght.items():
            list_of_page_name.append(name)
            list_of_page_size.append(lenght)

        paired = list(zip(list_of_page_name, list_of_page_size))

        paired.sort(key=lambda x: x[1], reverse=True)
        try:
            list_of_element, list_of_size_of_element = zip(*paired)
        except:
            return [] , []
        list_of_element = list(list_of_element)
        list_of_size_of_element = list(list_of_size_of_element)
        print("\n\n\n\n")

        for i in range(len(list_of_element)):
            dict_of_wikipedia_page_length_sorted[list_of_element[i]] = list_of_size_of_element[i]

        for i in range(10):
            print("Biggest Wikipedia Page by user: " , list_of_element[i],list_of_size_of_element[i])

        index = 0
        for user , data  in dict_of_number_of_link_per_page_sorted.items():
            #print(user,self.all_user_data_file.index(user))
            #print(user,self.list_of_wikipedia_page_of_real_people.index(user))
            page_len = pages_lenght[user]
            merged_data_name.append(user)
            merged_data_value.append((data * 3.67) + counts[user] + (page_len / nb_link_by_page_size))
            if index % 80000 == 0 or user == "Ray Charles" or user == "François Hollande":
                print(
                    f"User={user} | "
                    f"Data={data * 3.67:.2f} | "
                    f"Links={counts[user]} | "
                    f"Page={page_len / nb_link_by_page_size:.2f} | "
                    f"Total={(data * 3.67) + dict_of_people_who_are_the_most_linked_sorted[user] + (page_len / nb_link_by_page_size):.2f}"
                )

            index+=1

        paired = list(zip(merged_data_name, merged_data_value))

        paired.sort(key=lambda x: x[1], reverse=True)

        try:
            list_of_element, occurence_of_element_list = zip(*paired)
        except:
            return [] , []
        list_of_element = list(list_of_element)
        occurence_of_element_list = list(occurence_of_element_list)

        for i in range(len(list_of_element)):
            merged_data_dict[list_of_element[i]] = occurence_of_element_list[i]


        with open("data_files/list_of_the_longest_page.json", "w",encoding="utf-8") as f:
            json.dump(dict_of_wikipedia_page_length_sorted, f,ensure_ascii=False,indent=4)
  
        with open("data_files/list_of_page_with_the_most_link.json", "w",encoding="utf-8") as f:
            json.dump(dict_of_number_of_link_per_page_sorted, f,ensure_ascii=False,indent=4)

        with open("data_files/list_of_most_linked_user.json", "w",encoding="utf-8") as f:
            json.dump(dict_of_people_who_are_the_most_linked_sorted, f,ensure_ascii=False,indent=4)

        with open("data_files/people_dict_power_ranking.json", "w",encoding="utf-8") as f:
            json.dump(merged_data_dict, f,ensure_ascii=False,indent=4)

    def get_all_users_data(self):
        """A function that get all users data"""
        start = time.time()
        nbz = 20
        list_of_all_people = print_file_content(LIST_OF_REAL_PEOPLE_FILEPATH).split("\n")
        small_list_of_people = split_list(list_of_all_people,int(len(list_of_all_people)/nbz))
        list_of_all_people = small_list_of_people[int(sys.argv[1])]
        #list_of_all_people = list(set(list_of_all_people))
        # erreurs = [
        #     "Art and Language",
        #     "Saïan Supa Crew",
        #     "G-Unit",
        #     "D-Block Europe",
        #     "Vitor Hublot",
        #     "5.5 designers",
        #     "Le Klub des 7",
        #     "Chocolate Genius Inc.",
        #     "83 (collectif)",
        #     "Spoke Orkestra",
        #     "Maison d'édition"
        #      ""
        # ]

        skip_those_user = [
            "Ḥassān ibn T̠ābit",
            "Ṣafī al-Dīn al-Urmawī",
            "Ọranyan",
            "‘Abd al-Karīm b. Ibrāhīm al-Jīlī",
            "‘Abd al-Wahhab ibn Ahmad al-Sha‘rānī",
            "‘Alī b. Muhammad al-Jurjāni",
            "‘Etuate Lavulavu",
            "‘Ubada ibn al-Samit",
            "‘Âbd al-‘Âziz Ibn Mussâ Ibn Nussâyr",
            "’Anbasa ibn Suhaym al-Kalbi",
            "₩uNo",
            "Anne Frank",
            "Jésus de Nazareth"
        ]
        reset_file(f"user_info_dict{sys.argv[1]}.txt")
        for idx , people in enumerate(list_of_all_people):
            if int(sys.argv[1]) + 1 == 21 and people in skip_those_user:
                continue
            if people.isdigit():
                write_into_file("list_of_wikipedia_page_of_non_real_people.txt",people+"\n")
                continue
            if people in BAD_WIKI_PAGE:
                continue
            if idx % int(10000/nbz) == 0 and int(sys.argv[1]) == 1:
                print(idx , people)
                reset_file("counting.txt")
                write_into_file("counting.txt",idx)
            if len(people) >= 4:
                if people[0:4].isdigit() and " " in people and ("aux" in people or "dans" in people):
                    write_into_file("list_of_wikipedia_page_of_non_real_people.txt",people+"\n")
                    continue
            toto.get_user_information(people.replace('"',""),False,int(sys.argv[1])+1)
            # if user_info is False:
            #     ok+=1
            #     print(idx,ok)
            #     quit()

        if int(sys.argv[1]) == 1:
            end = time.time()
            print(f"Execution time: {end - start:.6f} seconds")
    def sorted_list_of_linked_of_user(self):
        """A function that generate a sorted list of link of all user"""
        with open("data_files/list_of_link_of_all_user.json", "r", encoding="utf-8") as file:
            people_links = json.load(file)
        with open("data_files/list_of_merged_data.json", "r", encoding="utf-8") as file:
            people_top = json.load(file)

        #reset_file("user_info_dict.txt")
        index = 0
        list_of_occurence = []
        list_of_user = []
        dict_link_sorted = {}
        skip = False
        for user,user_links in people_links.items():
            skip = False
            list_of_occurence = []
            list_of_user = []
            for u in user_links:
                try:
                    list_of_user.append(u)
                    list_of_occurence.append(people_top[u.replace("_"," ")])
                    # else:
                    #     print("not in set " , u)
                except:
                    skip = True
            if skip:
                dict_link_sorted[user] = user_links
                continue
            if len(list_of_user) != 0:
                #print(list_of_user, list_of_occurence)
                paired = list(zip(list_of_user, list_of_occurence))

                paired.sort(key=lambda x: x[1], reverse=True)

                list_of_element, occurence_of_element_list = zip(*paired)
                list_of_element = list(list_of_element)
                occurence_of_element_list = list(occurence_of_element_list)
                dict_link_sorted[user] = list_of_element
                if index % 90000 == 0:
                    print(user,user_links)
                    print(list_of_element,occurence_of_element_list)
                    print("\n\n\n\n")
            else:
                dict_link_sorted[user] = user_links
            if index % 90000 == 0:
                pass
            index+=1

        with open("data_files/list_of_link_of_all_users_sorted.json", "w",encoding="utf-8") as f:
            json.dump(dict_link_sorted, f,ensure_ascii=False,indent=4)
    def start(self):
        """blabla"""


toto = WikiPeopleData()
# OK USER
# toto.get_user_information("Emmanuel_Macron")
# toto.get_user_information("Alexandre_le_Grand")
# toto.get_user_information("Brandon_Johnson_(homme_politique)")
# toto.get_user_information("Jean_de_La_Fontaine")
# toto.get_user_information("William_Shakespeare")
# toto.get_user_information("Selena_Gomez")
# toto.get_user_information("Charlemagne")
# toto.get_user_information("Louis_XV")
# toto.get_user_information("Moliere")


do_user_data =  False
do_stat = False
do_sorted_file = False

if do_user_data:
    try:
        toto.get_all_users_data()
    except:
        print("You must put args number (int)")
    quit()
elif do_stat:
    print("Doing something else")
    toto.calc_stat()
    toto.sorted_list_of_linked_of_user()
elif do_sorted_file:
    # reset_file("user_info_dict_sorted_by_power.txt")
    # all_user_sorted = print_file_content(r"data_files/list_of_user_sorted_by_power.txt").split("\n")
    # all_user_dict_file = print_file_content(r"user_info_dict.txt").split("\n")
    # print(len(all_user_dict_file))
    # print(len(all_user_sorted))
    # print(len(toto.list_of_wikipedia_page_of_real_people))
    # for i , user in enumerate(all_user_sorted):

    #     if i % 25000 == 0:
    #         print(i,user)
    #     try:
    #         # ANNE FRANK
    #         if i == 1780:
    #             write_into_file("user_info_dict_sorted_by_power.txt",all_user_dict_file[-3]+"\n")          
    #         # JESUS DE NAZARETH
    #         if i == 337:
    #             write_into_file("user_info_dict_sorted_by_power.txt",all_user_dict_file[-2]+"\n")       
                        
    #         write_into_file("user_info_dict_sorted_by_power.txt",all_user_dict_file[toto.list_of_wikipedia_page_of_real_people.index(user)]+"\n")
    #     except:
    #         print("ERREUR!!! " , user)
    
    
    
    
    reset_file("user_info_dict_sorted_by_power.txt")
    all_user_sorted = print_file_content(r"data_files/list_of_user_sorted_by_power.txt").split("\n")
    all_user_dict_file = print_file_content(r"user_info_dict.txt").split("\n")
    
    print("user_info_dict.txt " , len(all_user_dict_file))
    print("data_files/list_of_user_sorted_by_power.txt " , len(all_user_sorted))
    print("list_of_wikipedia_page_of_real_people.txt " , len(toto.list_of_wikipedia_page_of_real_people))

    # O(1) lookup instead of O(n) list.index() in a loop
    # (if there are duplicate names, this keeps the LAST index for each,
    #  matching list.index() behavior would need the FIRST occurrence instead —
    #  see note below)
    user_to_index = {name: idx for idx, name in enumerate(toto.list_of_wikipedia_page_of_real_people)}

    output_lines = []

    for i, user in enumerate(all_user_sorted):
        if i % 25000 == 0 or i < 25:
            print(i, user)

        try:
            # # ANNE FRANK
            # if i == 1780:
            #     output_lines.append(all_user_dict_file[-3] + "\n")
            # # JESUS DE NAZARETH
            # if i == 337:
            #     output_lines.append(all_user_dict_file[-2] + "\n")

            idx = user_to_index[user]  # KeyError instead of ValueError if missing
            # try:            
            #     output_lines.append(all_user_dict_file[idx - 1] + "\n")
            # except:
            
            try:
                if user != ast.literal_eval(all_user_dict_file[idx])["page_name"]:
                    output_lines.append(all_user_dict_file[idx - 1] + "\n")
                                
                else:
                    output_lines.append(all_user_dict_file[idx] + "\n")
                                
            except:
                pass
                        
        except:
            print("ERREUR!!! ", user)
        
    # Single write instead of one write() call per line
    for line in output_lines:
        write_into_file("user_info_dict_sorted_by_power.txt",line)    
    #write_into_file("user_info_dict_sorted_by_power.txt", "".join(output_lines))
#         good_line = ast.literal_eval(line)
# list_of_user_sorted_by_power.txt
# # MEH USER

# BAD USER
# toto.get_user_information("Emmanuel_Macron")
# print("\n"*4)
#toto.get_user_information("Alexandre_le_Grand")

#toto.get_user_information("Brandon_Johnson_(homme_politique)")
# Selena_Gomez

# DATE DE CONNARD
# 27Abdu_Llâh_Ibn_Kullâb
# CHARLEMAGNE

# A TEST


# 'Ray Clough'

try:
    toto.get_user_information(sys.argv[1],True)
except:
    toto.get_user_information("Ray Brown")
