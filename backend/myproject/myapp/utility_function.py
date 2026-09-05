"""File that handle utility functions"""

# Too general exception
# pylint: disable=W0718

# No exception type specified
# pylint: disable=W0702

from random import randint

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

def dms_to_decimal(dms,name=""):
    try:
        if name == "blablobla":
            return 999999999999999 ,999999999999999
                       
        parts = dms.split(",")
        def convert(coordinate):
            coordinate = coordinate.strip()
            parts = coordinate.split()

            degrees = float(
                parts[0]
                .replace("°", "")
                .replace("′", "")
                .replace("″", "")
                .replace('"', "")
                .replace("'", "")
            )

            minutes = float(
                parts[1]
                .replace("′", "")
                .replace("'", "")
                .replace("′′", "")
                .replace("°", "")
                .replace('"', "")
                .replace("″", "")
            )

            if len(parts) >= 4:
                seconds = float(
                    parts[2]
                    .replace("″", "")
                    .replace('"', "")
                    .replace("′′", "")
                    .replace("°", "")
                    .replace("′", "")
                    .replace("'", "")
                )
                direction = parts[3].upper()
            else:
                seconds = 0
                direction = parts[2].upper()

            decimal = degrees + minutes / 60 + seconds / 3600

            if direction in ("S", "W"):
                decimal = -decimal

            return decimal
        latitude = convert(parts[0]) + randint(1000000000000000000,90000000000000000000) / 10000000000000000000000
        longitude = convert(parts[1]) + randint(1000000000000000000,90000000000000000000) / 10000000000000000000000
        return latitude, longitude
    except:
        return 999999999999999 ,999999999999999
        return -32.8471,-47.3926
                