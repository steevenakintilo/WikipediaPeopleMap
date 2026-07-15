"""A file that handle all the information"""
import traceback

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
            entry = self.zim.get_entry_by_title(self.clean_title(town))

            html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
            portion_of_wikipedia_page_text = html[:100000]
            for i in range (1,100):
                text_normal = portion_of_wikipedia_page_text.replace("\n"*i,"\n")


            reset_file("loto.txt")
            write_into_file("loto.txt",portion_of_wikipedia_page_text)
            
            return text_normal.split('title="Liste des pays du monde">Pays</a>')[1].split("data-sort-value=")[1].split(">")[0].replace('"',"")
        except:
            if potential_birth_country in portion_of_wikipedia_page_text:
                return potential_birth_country
            return "Undifined"

    def get_localisation_of_a_town(self,town:str) -> str:
        """A function that get the localisation of a town"""
        try:
            entry = self.zim.get_entry_by_title(self.clean_title(town))

            html = entry.get_item().content.tobytes().decode("utf-8", errors="replace")
            portion_of_wikipedia_page_text = html[:100000]
            text_normal = portion_of_wikipedia_page_text
            for i in range (1,100):
                text_normal = text_normal.replace("\n"*i,"\n")


            reset_file("loto.txt")
            write_into_file("loto.txt",text_normal)

            return text_normal.split('title="Liste des pays du monde">Pays</a>')[1].split("data-sort-value=")[1].split(">")[0].replace('"',"")
        except:
            return "Undifined"

    def get_user_information(self, page_name:str):
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
            # reset_file("toto.txt")
            # write_into_file("toto.txt",portion_of_wikipedia_page_text)

            if '<table class="infobox_v2 infobox infobox--frwiki noarchive">' in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split('<table class="infobox_v2 infobox infobox--frwiki noarchive">')[1].split("</tbody></table>")[0]
            elif "Biographie" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("Biographie")[1]
            elif len(text_normal) < 20 and "Informations générales" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("Informations générales")[1]            
            elif len(text_normal) < 20 and "infobox--frwiki noarchive" in portion_of_wikipedia_page_text:
                text_normal = portion_of_wikipedia_page_text.split("infobox--frwiki noarchive")[1]
            elif len(text_normal) < 20:
                text_normal = portion_of_wikipedia_page_text
            
            for i in range (1,100):
                text_normal = text_normal.replace("\n"*i,"\n")




            reset_file("toto.txt")
            write_into_file("toto.txt",text_normal)

            today_date_str = str(self.today_date)
            # elif "Activité principale</th>" not in text_normal:
            #     job = text_normal.split("</a></th></tr>")[0].split(">")[-1]
            
            # if "Activités</th>" not in text_normal and "Activité principale</th>" not in text_normal:
            #     print(text_normal.split("</a></th></tr>")[0].split(">"))
            #     job = text_normal.split("</a></th></tr>")[0].split(">")[20]
            # elif "Activité principale</th>" in text_normal:
                
            #     job = text_normal.split("Activité principale</th>")[1].split("<th")[0].split("</a>")[0].split(">")[-1]
            # else:
                
            #     job = text_normal.split("Activités</th>")[1].split("<a href=")[1].split(" title=")[0].replace('"',"")
            
            # if "Activités</th>" not in text_normal and "Activité principale</th>" not in text_normal:
            #     print(text_normal.split("</a></th></tr>")[0].split(">"))
            #     job = text_normal.split("</a></th></tr>")[0].split(">")[20]
            # elif "Activité principale</th>" in text_normal:
                
            #     job = text_normal.split("Activité principale</th>")[1].split("<th")[0].split("</a>")[0].split(">")[-1]
            # else:
                
            #     job = text_normal.split("Activités</th>")[1].split("<a href=")[1].split(" title=")[0].replace('"',"")
            
            if "Activités</th>" not in text_normal:
                if "Activité</th>" in text_normal:
                    job = text_normal.split("Activité</th>")[1].split(" title=")[1].split(">")[0].replace('"',"")
                else:
                    job = text_normal.split("</a></th></tr>")[0].split(">")[-1]
            else:
                job = text_normal.split("Activités</th>")[1].split("<a href=")[1].split(" title=")[0].replace('"',"")
            
            
            job = job.replace("_"," ")
            town_birth_place = ""
            country_birth_place = ""
            birth_date = ""
            death_date = "alive"
            age = "dead"
            is_alive = True
            born_before_chirst = False
            died_before_christ = False
            birth_date_abs = ""
            death_date_abs = ""

            if "Lieu de naissance" in text_normal:
                town_birth_place = text_normal.split("Lieu de naissance")[1].split("</a>")[0].split("title=")[1].split(">")[1]
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
                birth_date = text_normal.split("Date de naissance")[1].split("datetime=")[1].split(" ")[0].replace('"',"")
                if "décès" in text_normal.lower():
                    death_date = text_normal.split("Date de décès")[1].split("datetime=")[1].split(" ")[0].replace('"',"")
                    is_alive = False

                if "U-" in birth_date:
                    whole_birth_date = text_normal.split("Date de naissance")[1].split("<td>")[1].split("<")[0].split(" ")
                    birth_date = f"{self.convert_before_christ_to_date(birth_date)}-{MONTH_TO_NUMBER_DICT[whole_birth_date[1]]}-{whole_birth_date[0]}"
                    born_before_chirst = True
                if "U-" in death_date:
                    whole_death_date = text_normal.split("Date de décès")[1].split("<td>")[1].split("<")[0].split(" ")
                    if "décès" in text_normal.lower():
                        death_date = f"{self.convert_before_christ_to_date(death_date)}-{MONTH_TO_NUMBER_DICT[whole_death_date[1]]}-{whole_death_date[0]}"
                        died_before_christ = True
                elif birth_date.replace("-","").isdigit() is False:
                    pass

                #print(birth_date)
            else:
                try:
                    # town_index = 0
                    # for i , line in enumerate(text_normal.split("<a href=")):
                    #     if "Naissance" in line:
                    #         print(line)
                    #         print(i)
                    #     if i == 8:
                    #         print(line)
                    # return
                    town_birth_place = text_normal.split("<a href=")[4].split(" title=")[0].replace('"',"")
                except:
                    town_birth_place = ""
                
                try:
                    town_birth_place = text_normal.split("<a href=")[3].split(" title=")[1].split(">")[0].replace('"',"")
                except:
                    town_birth_place = text_normal.split("<a href=")[4].split(" title=")[0].replace('"',"")
                

                #
                #print(text_normal.split("<a href=")[11])
                if "%C3%" in town_birth_place or "class=" in town_birth_place:
                    town_birth_place = "Undifined"
                country_birth_place = self.get_country_of_a_town(town_birth_place)
                birth_index = 1
                for i , line in enumerate(text_normal.split("datetime=")):
                    if "Date de naissance" in line or "Naissance" in line:
                        
                        birth_index = i
                
                if birth_index == 0:
                    birth_index = 2


                birth_date = text_normal.split("datetime=")[birth_index - 1].split(" ")[0].replace('"',"")
                if "décès" in text_normal.lower():
                    death_date = text_normal.split("datetime=")[birth_index].split(" ")[0].replace('"',"")
                    is_alive = False

                if "U-" in birth_date:
                    whole_birth_date = text_normal.split("Date de naissance")[1].split("<td>")[1].split("<")[0].split(" ")
                    print(birth_date)
                    try:
                        birth_date = f"{self.convert_before_christ_to_date(birth_date)}-{MONTH_TO_NUMBER_DICT[whole_birth_date[1]]}-{whole_birth_date[0]}"
                    except:
                        birth_date = (int(birth_date.replace("U-0","")) + 1) * -1
                    born_before_chirst = True
                if "U-" in death_date:
                    whole_death_date = text_normal.split("Date de décès")[1].split("<td>")[1].split("<")[0].split(" ")
                    if "décès" in text_normal.lower():
                        try:
                            death_date = f"{self.convert_before_christ_to_date(death_date)}-{MONTH_TO_NUMBER_DICT[whole_death_date[1]]}-{whole_death_date[0]}"
                        except:
                            death_date = (int(death_date.replace("U-0","")) + 1) * -1
                    
                        died_before_christ = True
                
                #print(text_normal.split("<a href=")[4])

            if "décès" not in text_normal.lower():
                #print(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}")
                
                start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                end_date = datetime.strptime(f"{today_date_str.split("-")[0]}-{str(int(today_date_str.split("-")[1]))}-{str(int(today_date_str.split("-")[2]))}", "%Y-%m-%d")

                # Get the relativedelta between two dates
                delta = relativedelta.relativedelta(end_date, start_date)
                age = delta.years
                is_alive = False


            else:
                #print(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}")
                if born_before_chirst:
                    #print(birth_date.split("-"))
                    
                    try:
                        year_start = int(birth_date.split("-")[1]) * -1 + ABSOLUTE_DATE_VALUE
                        year_end = int(death_date.split("-")[1]) * -1 + ABSOLUTE_DATE_VALUE

                        month_start = int(birth_date.split("-")[2])
                        month_end = int(death_date.split("-")[2])

                        day_start = int(birth_date.split("-")[3])
                        day_end = int(death_date.split("-")[3]) 

                        age = self.get_age_between_two_date(year_start,month_start,day_start,year_end,month_end,day_end)
                    except:
                        if birth_date + ABSOLUTE_DATE_VALUE <= death_date + ABSOLUTE_DATE_VALUE:
                            age = (death_date + ABSOLUTE_DATE_VALUE) - (birth_date + ABSOLUTE_DATE_VALUE)
                        else:
                            age = (birth_date + ABSOLUTE_DATE_VALUE) - (death_date + ABSOLUTE_DATE_VALUE)
                    # start_date = datetime.strptime(f"{year_start}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                    # end_date = datetime.strptime(f"{year_end}-{str(int(death_date.split("-")[1]))}-{str(int(death_date.split("-")[2]))}", "%Y-%m-%d")

                    # # Get the relativedelta between two dates
                    # delta = relativedelta.relativedelta(end_date, start_date)
                    # age = delta.years

                else:

                    try:
                        start_date = datetime.strptime(f"{birth_date.split("-")[0]}-{str(int(birth_date.split("-")[1]))}-{str(int(birth_date.split("-")[2]))}", "%Y-%m-%d")
                        end_date = datetime.strptime(f"{death_date.split("-")[0]}-{str(int(death_date.split("-")[1]))}-{str(int(death_date.split("-")[2]))}", "%Y-%m-%d")

                        # Get the relativedelta between two dates
                        delta = relativedelta.relativedelta(end_date, start_date)
                        age = delta.years
                    except:
                        print(birth_date)
                        print(death_date)
                        if birth_date + ABSOLUTE_DATE_VALUE <= death_date + ABSOLUTE_DATE_VALUE:
                            age = (death_date + ABSOLUTE_DATE_VALUE) - (birth_date + ABSOLUTE_DATE_VALUE)
                        else:
                            age = (birth_date + ABSOLUTE_DATE_VALUE) - (death_date + ABSOLUTE_DATE_VALUE)

            town_birth_place = town_birth_place.replace("_"," ")
            if "(" in town_birth_place and ")" in town_birth_place:
                town_birth_place = town_birth_place.split("(")[0]
            print(f"Page name: {page_name}")
            print(f"Page url: https://fr.wikipedia.org/wiki/{page_name}")
            print(f"Job: {job}")
            print(f"Town birth place: {town_birth_place}")
            print(f"Country birth place: {country_birth_place}")
            print(f"Birth date: {birth_date}")
            print(f"Death date: {death_date}")
            print(f"Age: {age}")
            print(f"Is Alive: {is_alive}")
            print(f"Today date: {today_date_str}")
            print("\n"*5)
            #print('Years, Months, Days between two dates is')
            #print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')

        except:
            traceback.print_exc()

    def start(self):
        """blabla"""


toto = WikiPeopleData()
# OK USER
toto.get_user_information("Emmanuel_Macron")
toto.get_user_information("Alexandre_le_Grand")
toto.get_user_information("Brandon_Johnson_(homme_politique)")
toto.get_user_information("Jean_de_La_Fontaine")
# MEH USER

# BAD USER
# toto.get_user_information("Emmanuel_Macron")
# print("\n"*4)
#toto.get_user_information("Alexandre_le_Grand")

#toto.get_user_information("Brandon_Johnson_(homme_politique)")
# Selena_Gomez
