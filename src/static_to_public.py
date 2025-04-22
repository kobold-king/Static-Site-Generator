import os, shutil

def static_to_public(folder_path):
    folder_path = "/home/deck/boot.dev/github.com/kobold-king/Static-Site-Generator/public/"
    #deletes content in public folder
    for file_object in os.listdir(folder_path):
        #joins the file name to the pre-existing file path
        file_object_path = os.path.join(folder_path, file_object)
        if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
            os.unlink(file_object_path)
        else:
            shutil.rmtree(file_object_path)

    source_folder = "/home/deck/boot.dev/github.com/kobold-king/Static-Site-Generator/static/"
    destination = folder_path

    shutil.copytree(source_folder, destination, dirs_exist_ok=True)
