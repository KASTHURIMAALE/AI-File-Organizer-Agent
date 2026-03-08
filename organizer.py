import os
import shutil
from classifier import classify_file

def organize_files(folder_path, files):

    summary = {}

    for file in files:

        category = classify_file(file)

        category_folder = os.path.join(folder_path, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        source = os.path.join(folder_path, file)
        destination = os.path.join(category_folder, file)

        shutil.move(source, destination)

        summary[category] = summary.get(category, 0) + 1

    return summary