print("Anish B L \n1AY24AI010 \nAIML 'M' ")
import os

def find_large_files(folder_path, size_limit_mb=100):
    size_limit_bytes = size_limit_mb * 1024 * 1024
    print(f"\nFiles larger than {size_limit_mb} MB in '{folder_path}':\n")

    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            try:
                filepath = os.path.join(foldername, filename)
                filesize = os.path.getsize(filepath)
                if filesize > size_limit_bytes:
                    size_in_mb = round(filesize / (1024 * 1024), 2)
                    print(f"{os.path.abspath(filepath)} - {size_in_mb} MB")
            except (FileNotFoundError, PermissionError):
                continue
folder = input(" enter the folder name")
jnEnter folder path to scan: ").strip()
size_limit = input("Enter size limit in MB (default is 100): ").strip()

try:
    size_limit = int(size_limit) if size_limit else 100
    if os.path.isdir(folder):
        find_large_files(folder, size_limit)
    else:
        print("Invalid folder path.")
except ValueError:
    print("Size limit must be a number.")
