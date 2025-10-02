import os
import shutil
import logging

def list_all_files(directory):
    logging.info("inside listing file")
    return os.listdir(directory)

def move_file(source,destination):
    shutil.move(source,destination)
    logging.info("inside moving file")
    return f"File moved successfully to {destination} "

def rename_file(old_name,new_name):
    os.rename(old_name,new_name)
    logging.info("inside rename file")
    return f"File has been successfully remaned from {old_name} to {new_name}"

def delete_file(file_name):
    try:
        if os.path.exists(file_name):
            logging.info("deleting the file")
            os.remove(file_name)
            return "File has been deleted successfully"
        else:
            logging.warn("no such files")
            return "No such files to delete"    
    except Exception as e:
        logging.error(e)
        print(e)

def  file_organizer():
    directory="C:\IntelliTest\AGILE"   
    files=list_all_files(directory)
    logging.info("The list of files are",files)  

    action=input("What actions do u want to perform ? press 1 (renaming), press 2 (moving), press 3 (deleting)")

    if action=='1':
        old_name=input("Enter old name")
        new_name=input("enter new name")
        print(rename_file(old_name,new_name))

    elif action=='2':
        source=input("Enter the correct path or name of old file")
        destination=input("Enter the correct path or name of new file")
        print(move_file(source,destination))
    elif action=='3':    
        file=input("Enter the file to be deleted")
        print(delete_file(file))
    else:
        print("Please enter a valid number")


file_organizer()


