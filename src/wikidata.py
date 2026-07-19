"""A file that handle all the information"""
import traceback
import time
import unicodedata

from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import relativedelta
from global_variable import *
from libzim.reader import Archive
from urllib.parse import unquote
from utility_function import *


# Undifined Variable
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


    def get_country_of_a_town(self,town:str,potential_birth_country:str="") -> str:
        """A function that get the country of a town"""
        try:
            if len(town) == 0:
                return "Undifined"
            if town == "Undifined":
                return "Undifined"
            entry = self.zim.get_entry_by_title(self.clean_title(town))

            html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
            portion_of_wikipedia_page_text = html[:100000]
            for i in range (1,100):
                text_normal = portion_of_wikipedia_page_text.replace("\n"*i,"\n")


            reset_file("loto.txt")
            write_into_file("loto.txt",portion_of_wikipedia_page_text)
            return text_normal.split('title="Liste des pays du monde">Pays</a>')[1].split("data-sort-value=")[1].split(">")[0].replace('"',"")
        except:
            
            try:
                if potential_birth_country in portion_of_wikipedia_page_text and len(potential_birth_country) > 1:            
                    return potential_birth_country
                blabla = 'title="États-Unis">États-Unis'
                for country in self.list_of_country:
                    country_html_checker = f'title="{country}">{country}'
                    if country_html_checker in text_normal:
                        return country

                return "Undifined"
            except:

                return "Undifined"

    def get_localisation_of_a_town(self,town:str) -> str:
        """A function that get the localisation of a town"""
        try:
            if len(town) == 0:
                return "Undifined"
            if town == "Undifined":
                return "Undifined"
            
            entry = self.zim.get_entry_by_title(self.clean_title(town))

            html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
            portion_of_wikipedia_page_text = html[:100000]
            text_normal = portion_of_wikipedia_page_text

            for i in range (1,100):
                text_normal = text_normal.replace("\n"*i,"\n")

            soup = BeautifulSoup(text_normal, "html.parser")

            page_text = soup.get_text(" ", strip=True)

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
            return "Undifined"

    def get_gender_of_a_person(self,page_text:str,is_alive:bool) ->  str:
        """A function that get the gender of a person"""
        
        boy_score = 0
        girl_score = 0
        page_text = page_text.lower()
        soup = BeautifulSoup(page_text, "html.parser")

        page_text = soup.get_text(" ", strip=True)

        PAGE_CHARS_CHECKER = 50000
        page_split = page_text[:PAGE_CHARS_CHECKER].split(" ")
        #print(page_split[0:100])
        # CHECK FOR BOY
        # if "est né" in page_text[:PAGE_CHARS_CHECKER] and "est née" not in page_text[:PAGE_CHARS_CHECKER]:
        #     boy_score+=1
        if "né" in page_split and "née" in page_split:
            if page_split.index("né") < page_split.index("née"):
                boy_score+=1
        elif "né" in page_split:
            #print(page_split.index("né"),page_split.index("né"),page_split.index("né"))
            boy_score+=1
        
        if "est un" in page_text[:PAGE_CHARS_CHECKER] and "est une" not in page_text[:PAGE_CHARS_CHECKER]:
            boy_score+=1
        
        if "est un" in page_text[:PAGE_CHARS_CHECKER] and "est une" in page_text[:PAGE_CHARS_CHECKER]:
            split_text = page_text.split("est un")
            if "est une" not in split_text[0]:
                boy_score+=1
        
        
        if "était un" in page_text[:PAGE_CHARS_CHECKER] and "était une" not in page_text[:PAGE_CHARS_CHECKER] and is_alive is False:
            boy_score+=1
        
        if "était un" in page_text[:PAGE_CHARS_CHECKER] and "était une" in page_text[:PAGE_CHARS_CHECKER] and is_alive is False:
            split_text = page_text.split("était un")
            if "était une" not in split_text[0]:
                boy_score+=1
        
        if "baptisé" in page_text[:PAGE_CHARS_CHECKER]:
            boy_score+=1
        if "est mort" in page_text and "est morte" not in page_text:
            boy_score+=1
        
        # CHECK FOR GIRL

        if "né" in page_split and "née" in page_split:
            if page_split.index("née") < page_split.index("né"):
                girl_score+=1
        elif "née" in page_split:
            girl_score+=1
        
        if "est une" in page_text[:PAGE_CHARS_CHECKER] and "est un" not in page_text[:PAGE_CHARS_CHECKER]:
            girl_score+=1
        
        if "est un" in page_text[:PAGE_CHARS_CHECKER] and "est une" in page_text[:PAGE_CHARS_CHECKER]:
            split_text = page_text.split("est une")
            if "est un" not in split_text[0]:
                girl_score+=1

        if "était une" in page_text[:PAGE_CHARS_CHECKER] and "était un" not in page_text[:PAGE_CHARS_CHECKER] and is_alive is False:
            girl_score+=1
        
        if "était un" in page_text[:PAGE_CHARS_CHECKER] and "était une" in page_text[:PAGE_CHARS_CHECKER] and is_alive is False:
            split_text = page_text.split("est une")
            if "était un" not in split_text[0]:
                girl_score+=1

        if "baptisée" in page_text[:PAGE_CHARS_CHECKER]:
            girl_score+=1

        if "est morte" in page_text:
            girl_score+=1

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
        return "Undifined"

    def get_user_information(self, page_name:str,force_print_data:bool=False) -> None:
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
            entry = self.zim.get_entry_by_title(self.clean_title(page_name))

            html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
            portion_of_wikipedia_page_text = html[:100000]
            sub_job = []
            # reset_file("toto.txt")
            # write_into_file("toto.txt",portion_of_wikipedia_page_text)
            text_normal = ""
            if '<table class="infobox_v2 infobox infobox--frwiki noarchive">' in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split('<table class="infobox_v2 infobox infobox--frwiki noarchive">')[1].split("</tbody></table>")[0]
            elif "Biographie" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("Biographie")[1]
            elif len(text_normal) < 20 and "Informations générales" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("Informations générales")[1]            
            elif len(text_normal) < 20 and "infobox--frwiki noarchive" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("infobox--frwiki noarchive")[1]
            if len(text_normal) < 20:
                text_normal = portion_of_wikipedia_page_text
            
            for i in range (1,100):
                text_normal = text_normal.replace("\n"*i,"\n")




            reset_file("toto.txt")
            write_into_file("toto.txt",text_normal)

            today_date_str = str(self.today_date)
            
            try:
                if "Activités</th>" not in text_normal:
                        
                    if "Activité</th>" in text_normal:    
                        job = text_normal.split("Activité</th>")[1].split(" title=")[1].split(">")[0].replace('"',"")
                    elif "Profession</th>" in text_normal:
                        job = text_normal.split("Profession</th>")[1].split(" title=")[1].split(">")[0].replace('"',"")
                    
                    else:
                        if "Activité principale</th>" not in text_normal:
                            job = text_normal.split("</a></th></tr>")[0].split(">")[-1]
                            job_index = 0
                            if len(text_normal.split("</a></th></tr>")[0].split(">")[job_index -1].split("<")[0]) != 0:
                                
                                for index , line in enumerate(text_normal.split("</a></th></tr>")[0].split(">")):
                                    if  "et <a href=" in line:
                                        job_index = index
                                        break
                                if job_index != 0:
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
                    job = text_normal.split("Activités</th>")[1].split("<a href=")[1].split(" title=")[0].replace('"',"")
                    #print("job ", text_normal.split("Activités</th>")[1].split("<a href=")[8])
                    
            except:
                pass  

                      
            job = job.replace("_"," ")
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
            soup = BeautifulSoup(html[:100000], "html.parser")
            page_text_plain_text = soup.get_text(" ", strip=True)

            soup = BeautifulSoup(text_normal, "html.parser")
            page_text_small_text = soup.get_text(" ", strip=True)
            

            if "Lieu de naissance" in text_normal and "<td>Inconnu" not in text_normal:
                


                try:
                    if "<td>Inconnu" in text_normal:
                        town_birth_place = "Undifined"
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

                if town_birth_place != "Undifined":
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
                    
                    country_birth_place = self.get_country_of_a_town(town_birth_place,potential_birth_country)
                    
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

                if "décès" in text_normal.lower():
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
                        if "décès" in text_normal.lower():
                            death_date = f"{self.convert_before_christ_to_date(death_date)}-{MONTH_TO_NUMBER_DICT[whole_death_date[1]]}-{whole_death_date[0]}"
                            died_before_christ = True
                except:
                    pass
                # elif birth_date.replace("-","").isdigit() is False:
                #     pass

                #print(birth_date)
            else:


                try:
                    town_birth_place = text_normal.split("<a href=")[4].split(" title=")[0].replace('"',"")  
                except:
                    town_birth_place = ""
                
                try:

                    if town_birth_place == "" or "%C3%" in town_birth_place:
                        town_birth_place = text_normal.split("<a href=")[3].split(" title=")[1].split(">")[0].replace('"',"")
                        try:
                            town_birth_place_href = text_normal.text_normal.split("<a href=")[3].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                        except:
                            town_birth_place_href = ""


                    skip_the_rest = False
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
                        if town_birth_place == "" or "%C3%" in town_birth_place:
                            print("ici")
                            town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split("-")[0].replace('"',"").strip()
                            town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    except:
                        pass
                    
                    
                    try:
                        if town_birth_place == "" or "%C3%" in town_birth_place:
                            town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split('" ')[0].replace('"',"").strip()
                            town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    except:
                        pass
                    

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
                            if "%C3%" not in text_normal.split("<a href=")[i] and "class=" not in text_normal.split("<a href=")[i]:
                                town_birth_place = text_normal.split("<a href=")[i]
                                break
                        
                        town_birth_place = town_birth_place.split("title=")[1].split(">")[0].replace('"',"")
                    
                    if town_birth_place[0:4].isdigit() and " " in town_birth_place and town_birth_place.count(" ") > 1:
                            town_birth_place = text_normal.split("<a href=")[3].split(" title=")[1].split(">")[0].replace('"',"")
                            
                            for i in range(3,len(text_normal.split("<a href="))):
                                #print(i)
                                if "%C3%" not in text_normal.split("<a href=")[i] and "class=" not in text_normal.split("<a href=")[i]:
                                    town_birth_place = text_normal.split("<a href=")[i]
                                    break
                            town_birth_place = town_birth_place.split("title=")[1].split(">")[0].replace('"',"")
                        
                    if town_birth_place.split(" ")[0].lower() in LIST_OF_MONTH:
                        town_birth_place = ""

                    
                    try:
                        if town_birth_place == "" or "%C3%" in town_birth_place:
                            print("ici")
                            town_birth_place_year = text_normal.split("Naissance")[1].split("datetime=")[1].split("-")[0].replace('"',"").strip()
                            town_birth_place = page_text_small_text.split(town_birth_place_year)[1].split(" ")[1]
                    except:
                        pass
                    
                    try:
                        if town_birth_place == "" or "%C3%" in town_birth_place:
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
                                if "%C3%" not in text_normal.split("<a href=")[i] and "class=" not in text_normal.split("<a href=")[i]:
                                    town_birth_place = text_normal.split("<a href=")[i]
                                    break
                            town_birth_place = town_birth_place.split("title=")[1].split(">")[0].replace('"',"")
                        
                        else:
                            town_birth_place = text_normal.split("<a href=")[4].split(" title=")[0].replace('"',"")
                            if "%C3%" in town_birth_place or "class=" in town_birth_place:
                                town_birth_place = text_normal.split("<a href=")[6].split(" title=")[0].replace('"',"")
                            else:
                    
                                try:
                                    town_birth_place_href = text_normal.split("<a href=")[4].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                                except:
                                    town_birth_place_href = ""

                    except:
                        
                        pass
                
                
                #
                
                #print(text_normal.split("<a href=")[11])
                if "%C3%" in town_birth_place or "class=" in town_birth_place:
                    town_birth_place = "Undifined"
                if town_birth_place != "town_birth_place":
                    country_birth_place = self.get_country_of_a_town(town_birth_place)
                
                
                birth_index = 1
                for i , line in enumerate(text_normal.split("datetime=")):
                    if "Date de naissance" in line or "Naissance" in line:
                        
                        birth_index = i
                
                if birth_index == 0:
                    birth_index = 2

                try:
                    birth_date = text_normal.split("datetime=")[birth_index - 1].split(" ")[0].replace('"',"")
                except:
                    pass
                if "décès" in text_normal.lower():
                    try:
                        death_date = text_normal.split("datetime=")[birth_index].split(" ")[0].replace('"',"")
                    except:
                        pass
                    is_alive = False
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
                    if "décès" in text_normal.lower():
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
            if "décès" not in text_normal.lower():
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
                        if len(birth_date) == 4:
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
                            year_death_date_ = birth_date[0:len(death_date.split("-")[0])]
                            
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
                        if len(birth_date) == 4:
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
                            year_death_date_ = birth_date[0:len(death_date.split("-")[0])]
                            
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

                    country_death_place = self.get_country_of_a_town(town_death_place,"")
                except:
                    pass
            elif "décès" in text_normal.lower():
                try:
                    town_death_place = text_normal.split("Décès")[1].split(')')[1].split(' title=')[1].split(">")[0].replace('"',"")
                    country_death_place = self.get_country_of_a_town(town_death_place,"")
                    town_death_place_ =  town_death_place
                    country_death_place_ = country_death_place
                    try:
                        town_death_place_href = text_normal.split("Décès")[1].split(')')[1].split("<td><a ")[1].split("href=")[1].split(" ")[0].replace('"',"")
                    except:
                        town_death_place_href = ""
                    

                    try:
                        if page_text_small_text.split(death_date.split("-")[0])[1].split(")")[1].strip().count(",") <= 2:
                            potential_place = page_text_small_text.split(death_date.split("-")[0])[1].split(")")[1].strip().split(",")[1].strip()
                            town_death_place = potential_place
                            country_death_place = self.get_country_of_a_town(town_death_place,"")

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
                        town_death_place = text_normal.split("Décès")[1].split('(')[2].split("title=")[1].replace('"',"").strip()
                        for line in text_normal.split("Décès")[1].split("href="): 
                            if town_death_place.lower() in line.lower() and "title=" in line.lower():
                                town_death_place_href = unquote(line.split(" title=")[0].replace('"',""))
                                break
                    except:
                        pass
            
            
            try:
                if len(str(birth_date)) > 4 and "-" not in str(birth_date[0]):
                    if death_date == birth_date and int(birth_date.split("-")[0]) >= 1900:
                        is_alive = True
            except:
                pass
            try:
                if is_alive and len(str(birth_date)) == 4:
                    age = 2026 - int(birth_date)
            except:
                age = -999    
            gender = self.get_gender_of_a_person(html[:1000000],is_alive)

            job_player = "joueuse"
            determiner = "une"
            if gender == "Man":
                determiner = "un"
                job_player = "joueur"
            if "id=" in job:
                job = ""
            
            
            if "<" in job or ">" in job:
                job = ""
            
            try:
                if is_alive and len(job.strip()) <= 1:
                    if "est un" in page_text_plain_text:
                        list_of_element_after_sentence = page_text_plain_text.split(f"est {determiner}")[1].split(" ")[0:10]
                        for index,element in enumerate(list_of_element_after_sentence):
                            if len(element) > 1:
                                job = element
                                job_index = index
                                break 
                        
                        job_ = job
                        if job == job_player or list_of_element_after_sentence[job_index+1].startswith("d'") or list_of_element_after_sentence[job_index+1].starthwith("de"):
                            job_index = 0
                            particle = "de"
                            for index , element in enumerate(list_of_element_after_sentence):
                                if element.startswith("d'"):
                                    job_index = index
                                    particle = "d'"
                                    break

                                if element == "de":
                                    job_index = index + 1
                                    break
                            job = f"{determiner} de {list_of_element_after_sentence[job_index]}"  
                            if particle != "de":
                                job = f"{job_} {list_of_element_after_sentence[job_index]}"  
                  
                elif is_alive is False and job.strip() == "":
                    if "était un" in page_text_plain_text:
                        list_of_element_after_sentence = page_text_plain_text.split(f"est {determiner}")[1].split(" ")[0:10]
                        job_index = 0
                        for index,element in enumerate(list_of_element_after_sentence):
                            if len(element) > 1:
                                job = element
                                job_index = index
                                break 
                        
                        job_ = job
                        if job == job_player or list_of_element_after_sentence[job_index+1].startswith("d'") or list_of_element_after_sentence[job_index+1].starthwith("de"):
                            job_index = 0
                            particle = "de"
                            for index , element in enumerate(list_of_element_after_sentence):
                                if element.startswith("d'"):
                                    job_index = index
                                    particle = "d'"
                                    break

                                if element == "de":
                                    job_index = index + 1
                                    break
                            job = f"{determiner} de {list_of_element_after_sentence[job_index]}"  
                            if particle != "de":
                                job = f"{job_} {list_of_element_after_sentence[job_index]}"  
                
                    elif "est un" in page_text_plain_text:
                        list_of_element_after_sentence = page_text_plain_text.split(f"est {determiner}")[1].split(" ")[0:10]
                        job_index = 0

                        for index,element in enumerate(list_of_element_after_sentence):
                            if len(element) > 1:
                                job = element
                                job_index = index
                                break 
                        
                        job_ = job
                        if job == job_player or list_of_element_after_sentence[job_index+1].startswith("d'") or list_of_element_after_sentence[job_index+1].starthwith("de"):
                            job_index = 0
                            particle = "de"
                            for index , element in enumerate(list_of_element_after_sentence):
                                if element.startswith("d'"):
                                    job_index = index
                                    particle = "d'"
                                    break

                                if element == "de":
                                    job_index = index + 1
                                    break
                            job = f"{determiner} de {list_of_element_after_sentence[job_index]}"  
                            if particle != "de":
                                job = f"{job_} {list_of_element_after_sentence[job_index]}"  
                
                                
                            
            except:
                pass    
            
            
            #print(town_birth_place,job)
            
            if job == town_birth_place:
                if job not in JOBS:
                    job = ""
                town_birth_place = ""
            if len(job) <= 1:
                job = ""
            town_birth_place = town_birth_place.replace("en:","").replace("fr:","")
            town_death_place = town_death_place.replace("en:","").replace("fr:","")
                
            town_birth_place = town_birth_place.replace("_"," ")
            town_death_place = town_death_place.replace("_"," ")
            job = unquote(job)
            town_birth_place = unquote(town_birth_place)
            country_birth_place = unquote(country_birth_place)
            town_death_place = unquote(town_death_place)
            country_death_place = unquote(country_death_place)
            
            if "<" in str(birth_date) or ">" in str(birth_date) or "_" in str(birth_date):
                birth_date = ""
                age = -999
            
            if "<" in str(death_date) or ">" in str(death_date) or "_" in str(death_date):
                death_date = ""
                age = -999
            
            if town_birth_place != "Undifined" and len(town_birth_place) != 0:
                birth_town_localisation = self.get_localisation_of_a_town(town_birth_place)
                if birth_town_localisation == "Undifined" or len(birth_town_localisation) == "" and town_birth_place_href != "":
                    birth_town_localisation = self.get_localisation_of_a_town(town_birth_place_href)
            if is_alive is False:
                if town_death_place != "Undifined" and len(town_death_place) != 0:
                    death_town_localisation = self.get_localisation_of_a_town(town_death_place)
                    if death_town_localisation == "Undifined" or len(death_town_localisation) == "" and town_death_place_href != "":
                        death_town_localisation = self.get_localisation_of_a_town(town_death_place_href)
            
            if town_birth_place == town_death_place and len(birth_town_localisation) != 0 and len(town_birth_place) != 0:
                death_town_localisation = birth_town_localisation
            
            if town_birth_place == town_death_place and len(death_town_localisation) != 0 and len(town_birth_place) != 0:
                death_town_localisation = birth_town_localisation
                                    
            if birth_town_localisation == death_town_localisation:
                if len(country_birth_place) != 0 and len(country_death_place) == 0:
                    country_death_place = country_birth_place
                
                if len(country_death_place) != 0 and len(country_birth_place) == 0:
                    country_death_place = country_birth_place

            if country_birth_place != "Undifined" and len(country_birth_place) != 0:
                continent_of_birth = self.country_to_continent(country_birth_place)
            
            if country_death_place != "Undifined" and len(country_death_place) != 0:
                continent_of_death = self.country_to_continent(country_death_place)
                
            
            if job == "":
                preciseness_level -= 20
                list_of_unpreciseness_data.append("job is unknown")
            

            if birth_date == "<!DOCTYPE":
                return
            if town_birth_place == "" or town_birth_place == "Undifined":
                preciseness_level -= 20
                #print("town_birth_place is bad")
                list_of_unpreciseness_data.append("town_birth_place is unknown")

            if birth_town_localisation == "":
                preciseness_level -= 10
                list_of_unpreciseness_data.append("birth town localisation is unknown")
            
            if country_birth_place == "" or country_birth_place == "Undifined":
                preciseness_level -= 20
                #print("country_birth_place is bad")
                list_of_unpreciseness_data.append("country_birth_place is unknown")
            if birth_date_is_between_two_date:
                preciseness_level -= 20
                list_of_unpreciseness_data.append("birthdate is between two date")
            if birth_year_is_real_but_month_and_day_are_not:
                preciseness_level -= 10
                list_of_unpreciseness_data.append("birth year is real but month and day are not")
            if is_alive is False:
                if town_death_place == "":
                    preciseness_level -= 20
                    #print("town_death_place is bad")
                    list_of_unpreciseness_data.append("town_death_place is unknown")

                if country_death_place == "":
                    preciseness_level -= 20
                    list_of_unpreciseness_data.append("country_death_place is unknown")
                if death_town_localisation == "":
                    preciseness_level -= 10
                    list_of_unpreciseness_data.append("death town localisation is unknown")

                if birth_date == death_date:
                    preciseness_level -= 40
                    list_of_unpreciseness_data.append("birth_date and death_date may be the same")   
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
                
            try:
                birth_year = int(birth_date.split("-")[0])
                
                if birth_year < 1900 or "-" in birth_year:
                    preciseness_level -= 10
                    list_of_unpreciseness_data.append("birth_date is before the year 1900")
                    #print("birth_date is imprecise")
            except Exception:
                pass
            
            if age == -999:
                preciseness_level -= 10
                list_of_unpreciseness_data.append("age is unknown")
                    
            try:
                birth_year = int(birth_date.split("-")[0])
                death_year = int(death_date.split("-")[0])
                
                if birth_year > death_year:
                    preciseness_level -= 40
                    list_of_unpreciseness_data.append("birth_date is after death_date")
                    #print("birth_date and death_date are imprecise")
            except Exception:
                pass
            
            try:
                birth_year = int(birth_date.split("-")[0])
                death_year = int(death_date.split("-")[0])
                
                if birth_year == death_year:
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




            if "(" in town_birth_place and ")" in town_birth_place:
                town_birth_place = town_birth_place.split("(")[0]
            
            print_data = False

            if int(preciseness_level/2) < MINIMAL_PRECISSENES_SCORE:
                print_data = True



            if force_print_data:
                print_data = True
            else:
                print_data = False
            if town_birth_place == "":
                country_birth_place = ""
                birth_town_localisation = ""
                continent_of_birth = ""
            
            if town_death_place == "":
                country_death_place = ""
                death_town_localisation = ""
                continent_of_death = ""
            
            if print_data:
                print(f"Page name: {page_name}")
                print(f"Page url: https://fr.wikipedia.org/wiki/{page_name}")
                print(f"Job: {job}")
                print(f"Town birth place: {town_birth_place}")
                print(f"Birth Town localisation: {birth_town_localisation}")
                print(f"Country birth place: {country_birth_place}")
                if continent_of_birth != "Undifined" and len(continent_of_birth) != 0:
                    print(f"Continent of birth: {continent_of_birth}")
                
                
                if is_alive is False:
                    print(f"Town death place: {town_death_place}")
                    print(f"Death Town localisation: {death_town_localisation}")
                    print(f"Country death place: {country_death_place}")
                if continent_of_death != "Undifined" and len(continent_of_death) != 0:
                    print(f"Continent of death: {continent_of_death}")
                
                print(f"Birth date: {birth_date}")
                print(f"Death date: {death_date}")
                print(f"Born before Christ: {born_before_chirst}")
                
                if is_alive is False:
                    print(f"Dead before Christ: {died_before_christ}")
                print(f"Age: {age}")
                print(f"Is Alive: {is_alive}")
                print(f"Gender: {gender}")

                
                
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
                born_before_christ_and_died_after_christ

            if page_name[0] == "'":
                page_name = page_name[1:]
                page_name = "%27"+page_name
            
            user_info_dict = {
                "page_name":page_name,
                "page_url":f"https://fr.wikipedia.org/wiki/{page_name.replace(" ","_")}",
                "job":job,
                "town_birth_place":town_birth_place,
                "birth_town_localisation":birth_town_localisation,
                "country_birth_place":country_birth_place,
                "continent_of_birth":continent_of_birth,
                "birth_date":birth_date,
                "birth_death_localisation":death_town_localisation,
                "country_death_place":country_death_place,
                "continent_of_death":continent_of_death,
                "death_date":death_date,
                "born_before_christ":born_before_chirst,
                "died_before_christ":died_before_christ,
                "born_and_died_before_christ":born_and_died_before_christ,
                "born_and_died_after_christ":born_and_died_after_christ,
                "born_before_christ_and_died_after_christ":born_before_christ_and_died_after_christ,
                "age":age,
                "is_alive":is_alive,
                "gender":gender,
                "preciseness_level":int(preciseness_level/2),
                "list_of_unpreciseness_data":list_of_unpreciseness_data

            }

            if int(preciseness_level/2) < MINIMAL_PRECISSENES_SCORE and force_print_data:
                print(user_info_dict)
                print("-------"*120)
            #print('Years, Months, Days between two dates is')
            #print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
            return True
        except:
            traceback.print_exc()
            if page_name[0] == "'":
                page_name = page_name[1:]
                page_name = "%27"+page_name

            print(f"https://fr.wikipedia.org/wiki/{page_name.replace(" ","_")}")
            return False
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


do_time_test = False
if do_time_test:
    start = time.time()
            
    list_of_all_people = print_file_content(r"C:\Users\sakin\Desktop\code\six-degrees-of-separation-wikipedia\src\real_people_dir\real_people_diff_withouth_doublon.txt").split("\n")[0:10000]
    ok = 0
    for idx , people in enumerate(list_of_all_people):
        if people.isdigit():
            continue
        
        if idx % 1000 == 0:
            print(idx)
            reset_file("counting.txt")
            write_into_file("counting.txt",idx)
        if len(people) >= 4:
            if people[0:4].isdigit() and " " in people and ("aux" in people or "dans" in people):
                continue
            
        user_info = toto.get_user_information(people.replace('"',""),False)
        if user_info is False:
            ok+=1
            print(idx,ok)
            quit()

    end = time.time()
    print(f"Execution time: {end - start:.6f} seconds")

# MEH USER

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
# -Z-
# Abas_(Arménie)
# Abba_Jifar_II
# Abbas_Fahdel
# Abby_Jane_Morrell
# Abdelhalim_Abdelouahab
# Abdel_Gadir_Salim


toto.get_user_information("Inoxtag",True)