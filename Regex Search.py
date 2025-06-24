print("Aditya M \n1AY24AI004 \nAIML 'M' ")
import os
import re

def regex_search_in_files(folder_path
                         ):
    pattern = input("Enter the regular expression to search for: ")
    try:
        regex = re.compile(pattern)
    except re.error:
        print("Invalid regular expression.")
        return
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line_num, line in enumerate(lines, start=1):
                    if regex.search(line):
                        print(f"{filename} [Line {line_num}]: {line.strip()}")
folder = input("Enter folder path: ").strip()
if os.path.isdir(folder):
    regex_search_in_files(folder)
else:
    print("Invalid folder path.")