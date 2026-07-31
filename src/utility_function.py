"""File that handle utility functions"""

# Too general exception
# pylint: disable=W0718

# No exception type specified
# pylint: disable=W0702

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