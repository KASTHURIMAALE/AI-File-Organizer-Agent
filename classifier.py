
import os
from config import FILE_CATEGORIES

def classify_file(file_name):

    extension = os.path.splitext(file_name)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"