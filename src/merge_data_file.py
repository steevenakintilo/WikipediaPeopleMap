from utility_function import *

def merge_files():
    """A function that will merge all user_info_dict.txt files into one"""
    list_of_lines = []
    for i in range(21):
        if len(list_of_lines) % 10000 != 0:
            print(len(list_of_lines))
        current_user_info_file = print_file_content(f"user_info_dict{i + 1}.txt").split("\n")
        for line in current_user_info_file:
            if line not in list_of_lines and len(str(line)) > 1:
                list_of_lines.append(line)
                write_into_file("user_info_dict.txt",line+"\n")

def merge_filess():
    """A function that will merge all user_info_dict.txt files into one"""
    seen = set()
    with open("user_info_dict.txt", "w", encoding="utf-8") as out:
        for i in range(101):
            with open(f"user_info_dict{i + 1}.txt", encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip("\n")
                    if len(line) > 1 and line not in seen:
                        seen.add(line)
                        out.write(line + "\n")
merge_filess()
