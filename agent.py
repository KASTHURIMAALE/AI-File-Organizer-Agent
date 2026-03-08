from scanner import scan_folder
from organizer import organize_files

def run_file_organizer_agent(folder_path):

    files = scan_folder(folder_path)

    if not files:
        return "No files found in the folder"

    result = organize_files(folder_path, files)

    return result