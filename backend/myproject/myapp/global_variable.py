import os
import datetime

x = datetime.datetime.now()

CURRENT_YEAR = int(x.year)
USER_DICT_FILE_PATH = rf"{os.getcwd().split(r"\backend\myproject")[0]}\src\user_info_dict.txt"
NUMBER_OF_USER = 706208
NUMBER_OF_USER = 712430

MAXIMUM_AGE_TO_DISPLAY = 122

HISTORICAL_PERIODS = [
    "Prehistory",
    "Antiquity",
    "Middle Ages",
    "Renaissance",
    "Contemporary Period",
    "Today Time"
]

VARIABLE_NAME_TO_DICT_FRENCH = {

    "age_": "âges",
    "birthday_": "dates de naissance",
    "deathday_": "dates de décès",
    "birth_year_": "années de naissance",

    "boy_name_": "prénoms masculins",
    "girl_name_": "prénoms féminins",
    "french_boy_name_": "prénoms masculins français",
    "french_girl_name_": "prénoms féminins français",

    "name_": "prénoms",
    "last_name_": "noms de famille",
    "french_last_name_": "noms de famille français",

    "job_": "métiers",

    "town_": "villes",
    "town_birth_": "villes de naissance",
    "town_death_": "villes de décès",
    "french_town_": "villes françaises",
    "french_town_birth_": "villes françaises de naissance",
    "french_town_death_": "villes françaises de décès",

    "country_": "pays",
    "country_birth_": "pays de naissance",
    "country_death_": "pays de décès",


    "continent_": "continents",
    "continent_birth_": "continents de naissance",
    "continent_death_": "continents de décès",
        
    "region_of_birth_": "régions de naissance",
    "region_of_death_": "régions de décès",

    "region_birth_": "régions de naissance",
    "region_death_": "régions de décès",
    
    "region_": "régions",

    "first_char_of_the_page_": "premières lettres des pages",
    "time_period_of_birth_": "périodes historiques",
    "time_period_": "périodes historiques",
        

    "death_month_day_": "dates de décès",
    "birth_and_death_month_day_": "dates de naissance et de décès",

    "page_name_lenght_": "longueurs des noms de pages",
}

HISTORICAL_PERIODS_DICT_TO_FRENCH = {
    "Prehistory": "Préhistoire",
    "Antiquity": "Antiquité",
    "Middle Ages": "Moyen Âge",
    "Renaissance": "Renaissance",
    "Contemporary Period": "Époque contemporaine",
    "Today Time": "Époque actuelle",
    "Undefined":"Indéfinie",
    "Préhistoire": "Préhistoire",
    "Antiquité": "Antiquité",
    "Moyen Âge": "Moyen Âge",
    "Époque contemporaine": "Époque contemporaine",
    "Époque actuelle": "Époque actuelle",
    "Indéfinie": "Indéfinie"
}

HISTORICAL_PERIODS_DICT_TO_FRENCH_WITH_DATE = {
    "Prehistory": "Préhistoire (-99999999-3301)",
    "Antiquity": "Antiquité (-3300-475)",
    "Middle Ages": "Moyen Âge (476-1491)",
    "Renaissance": "Renaissance (1492-1788)",
    "Contemporary Period": "Époque contemporaine (1789-1999)",
    "Today Time": "Époque actuelle (2000-????)",
    "Undefined":"Indéfinie"
}

HISTORICAL_PERIODS_DICT = {
    "Préhistoire -99999999-3301":"Prehistory",
    "Antiquité -3300-475":"Antiquity",
    "Moyen Âge 476-1491":"Middle Ages",
    "Renaissance 1492-1788":"Renaissance",
    "Époque contemporaine 1789-1999":"Contemporary Period",
    "Époque actuelle 2000-?????":"Today Time"
    
}

HISTORICAL_PERIODS_WITH_DATE = [
    "Préhistoire -99999999-3301",
    "Antiquité -3300-475",
    "Moyen Âge 476-1491",
    "Renaissance 1492-1788",
    "Époque contemporaine 1789-1999",
    "Époque actuelle 2000-?????"
    
]

GENDER_TO_FRENCH_DICT = {
    "Man":"Homme",
    "Woman":"Femme",
    "Unclear":"Indéfinie",
}


VARIABLE_TO_LETTER_FOR_RANKING = {
    "name": "aa",
    "boy_name": "ab",
    "girl_name": "ac",
    "french_boy_name": "ad",
    "french_girl_name": "ae",
    "last_name": "af",
    "french_last_name": "ag",
    "age": "ah",
    "birth_year": "ai",
    "job": "aj",
    "town_birth": "ak",
    "town_death": "al",
    "town": "am",
    "french_town_birth": "an",
    "french_town_death" : "ao",
    "french_town": "ap",
    "country_birth": "aq",
    "country_death": "ar",
    "country": "as",
    "continent": "at",
    "region_of_birth": "au",
    "region_of_death":"av",
    "region":"aw",
    "time_period_of_birth": "ax",
    "birthday": "ay",
    "deathday" : "az",
    "birth_and_death_month_day" : "ba",
    "page_name_lenght": "bb",
    "first_char_of_the_page": "bc",
}

VARIABLE_TO_LETTER_FOR_GENDER_RATIO = {
    "last_name": "af",
    "french_last_name": "ag",
    "age": "ah",
    "town_birth": "ak",
    "town_death": "al",
    "town": "am",
    "french_town_birth": "an",
    "french_town_death" : "ao",
    "french_town": "ap",
    "country_birth": "aq",
    "country_death": "ar",
    "country": "as",
    "continent_birth": "at",
    "continent_death": "au",
    "continent": "av",
    "region_birth": "aw",
    "region_death":"ax",
    "region":"ay",
    "time_period_of_birth": "az",
}

LIST_OF_CONTINENT_NAME = ["Afrique","Amerique","Asie","Europe","Océanie"]

NUMBER_OF_USERS_TO_SEARCH = 500


UNPRECISENESS_DATA_FR = {
    "town_birth_place is unknown": "La ville de naissance est inconnue",
    "birth town localisation is unknown": "La localisation de la ville de naissance est inconnue",
    "country_birth_place is unknown": "Le pays de naissance est inconnu",
    "birthdate is between two date": "La date de naissance est comprise entre deux dates",
    "birth year is real but month and day are not": "L'année de naissance est connue, mais pas le mois ni le jour",
    "death year is real but month and day are not": "L'année de décès est connue, mais pas le mois ni le jour",
    "town_death_place is unknown": "La ville de décès est inconnue",
    "country_death_place is unknown": "Le pays de décès est inconnu",
    "death town localisation is unknown": "La localisation de la ville de décès est inconnue",
    "birth_date and death_date may be the same": "La date de naissance et la date de décès pourraient être identiques",
    "birth_date and death_date are wrong": "Les dates de naissance et de décès semblent incorrectes",
    "birth_date is bad": "La date de naissance semble incorrecte",
    "gender is unclear": "Le genre est incertain",
    "death_date is bad": "La date de décès semble incorrecte",
    "continent of birth is unknown": "Le continent de naissance est inconnu",
    "continent of death is unknown": "Le continent de décès est inconnu",
    "birth_date is before the year 1900": "La date de naissance est antérieure à 1900",
    "age is unknown": "L'âge est inconnu",
    "age is unknown/younger than 16 and birth_date/death_date may be unknown too": "L'âge est inconnu ou inférieur à 16 ans, et les dates de naissance et de décès peuvent également être inconnues",
    "birth_date is after death_date": "La date de naissance est postérieure à la date de décès",
    "birth_date year is the same as death_date year so one of the date is wrong": "L'année de naissance est identique à l'année de décès : l'une des deux dates est probablement incorrecte",
    "User is born before christ": "La personne est née avant Jésus-Christ",
    "age is unknown and birth_date/death_date may be unknown too": "L'âge est inconnu, et les dates de naissance et de décès peuvent également être inconnues",
    "job is unknown":"La profession est inconnu",
    "User may have a bigger role than homme politique":"Le metier de l'utilisateur est probablement plus précis que l'homme politique.",
    "User may have a bigger role than femme politique":"Le metier de l'utilisateur est probablement plus précis que femme politique.",
    "death_day is undefined":"Le jour de décès est inconnu"
}

AGE_GROUP_DICT: dict[str, str] = {
    "-99": "-999 ans",
    "0": "0 à 9 ans",
    "1": "10 à 19 ans",
    "2": "20 à 29 ans",
    "3": "30 à 39 ans",
    "4": "40 à 49 ans",
    "5": "50 à 59 ans",
    "6": "60 à 69 ans",
    "7": "70 à 79 ans",
    "8": "80 à 89 ans",
    "9": "90 à 99 ans",
    "10": "100 à 109 ans",
    "11": "110 à 119 ans",
    "12": "120 à 129 ans",
}

LIST_OF_REGIONS_NAME = [
    "Europe du Nord",
    "Europe de l'Ouest",
    "Europe du Sud",
    "Europe de l'Est",
    "Afrique du Nord",
    "Afrique de l'Ouest",
    "Afrique centrale",
    "Afrique de l'Est",
    "Afrique australe",
    "Moyen-Orient",
    "Asie centrale",
    "Asie de l'Est",
    "Asie du Sud",
    "Asie du Sud-Est",
    "Caucase",
    "Amérique anglo-saxonne",
    "Amérique centrale",
    "Caraïbes",
    "Amérique du Sud",
    "Australasie",
    "Mélanésie",
    "Micronésie",
    "Polynésie",
]


USERS_TO_SKIP = [
    "Het Gulden Cabinet"
]