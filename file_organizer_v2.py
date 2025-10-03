import os
import shutil

#Function to list the files in directory
def list_directories(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]

def create_dir(path, dir_name):
    full_path=os.path.join(path,dir_name)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    return full_path

def move_files(file,source_dir,dest_dir):
    shutil.move(os.path.join(source_dir,file),os.path.join(dest_dir,file))    

def organize_file(directory):
    image_exts=(".jpg",".jpeg",".png",".gif")
    video_exts = ('.mp4', '.mkv', '.mov', '.avi')   
    doc_files=(".csv",".txt",".pdf",".docx")

    files=list_directories(directory)

    for file in files:
        file_lower=file.lower()

        if file_lower.endswith(image_exts):
            target_dir=create_dir(directory,'Images')
            move_files(file,directory,target_dir)
        elif file_lower.endswith(video_exts):
            target_dir=create_dir(directory,"Vedios")
            move_files(file,directory,target_dir)
        elif file_lower.endswith(doc_files):
            target_dir=create_dir(directory,"Docs")
            move_files(file,directory,target_dir)
        else:
            target_dir=create_dir(directory,"Others")
            move_files(file,directory,target_dir)             

organize_file("C:\\Users\\lenovo\\Downloads")



 





    

