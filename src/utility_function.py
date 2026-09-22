"""File that handle utility functions"""

# Too general exception
# pylint: disable=W0718

# No exception type specified
# pylint: disable=W0702

import calendar

def write_into_file(path:str, data:str) -> None:
    """A function that write data into a file"""
    with open(path, "ab") as f:
        f.write(str(data).encode("utf-8"))

def reset_file(path:str) -> None:
    """A function that reset a file"""
    f = open(path, "w",encoding="utf8")
    f.write("")
    f.close()

def print_file_content(path:str) -> str:
    """A function that print the content of a file"""
    f = open(path, 'r',encoding="utf-8")
    content = f.read()
    f.close()
    return content


def split_list(lst:list[str], chunk_size:int):
    """A function that split a list"""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def list_to_lower(lst:list[str]):
    """A function that return a list of string to lower"""
    return [x.lower() for x in lst]

def get_weekday_from_a_date(date:str):
    """A function that get the weekday of a given date"""
    try:

        if "-13-99" in date:
            return "Charbre"
        given_date = f"{date.split("-")[2]} {date.split("-")[1]} {date.split("-")[0]}"
        if date[0] == "-":
            given_date = f"{date.split("-")[3]} {date.split("-")[2]} {date.split("-")[1]}"
        day, month, year = map(int, given_date.split())  # day, month, year

        week_day = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        return week_day[calendar.weekday(year, month, day)]
    except:
        return "Undefined"