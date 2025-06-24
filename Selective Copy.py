print("Aditya M, USN:1AY24AI004, SEC:M")
import os
import shutil
def copy_files_with_extension(source_folder, destination_folder, file_extension):
    os.makedirs(destination_folder, exist_ok=True)
    file_extension = file_extension.lower()
    count = 0
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(file_extension):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(destination_folder, filename)
                if os.path.exists(destination_path):
                    base, ext = os.path.splitext(filename)
                    i = 1
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(destination_folder, f"{base}_{i}{ext}")
                        i += 1
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} → {destination_path}")
                count += 1
    print(f"\nTotal files copied: {count}")
source = input("Enter the path to the source folder: ").strip()
destination = input("Enter the path to the destination folder: ").strip()
extension = input("Enter the file extension to search for (e.g., .pdf, .jpg): ").strip()
copy_files_with_extension(source, destination, extension)

# Deleting Unneeded Files
print("Aditya M, USN:1AY24AI004, SEC:M")
import os
def find_large_files(folder_path, size_threshold_mb=100):
    size_threshold_bytes = size_threshold_mb * 1024 * 1024
    large_files_found = 0
    print(f"\nScanning for files larger than {size_threshold_mb}MB in:\n{os.path.abspath(folder_path)}\n")
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            try:
                file_path = os.path.join(foldername, filename)
                file_size = os.path.getsize(file_path)
                if file_size > size_threshold_bytes:
                    size_mb = file_size / (1024 * 1024)
                    print(f"{os.path.abspath(file_path)} - {size_mb:.2f} MB")
                    large_files_found += 1
            except (PermissionError, FileNotFoundError):
                continue
    if large_files_found == 0:
        print("No files larger than the specified size were found.")
    else:
        print(f"\nTotal large files found: {large_files_found}")
folder = input("Enter the path to the folder to scan: ").strip()
find_large_files(folder)
