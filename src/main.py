import os
import shutil
from static_to_public import static_to_public

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    static_to_public(dir_path_static, dir_path_public)


main()
