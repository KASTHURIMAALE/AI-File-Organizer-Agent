
import os

def scan_folder(folder_path):
    files = []
    
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isfile(full_path):
            files.append(item)

    return files