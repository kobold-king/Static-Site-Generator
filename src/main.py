import os
import shutil
import sys
from static_to_public import static_to_public
from generate_page import generate_pages_recursive

dir_path_static = "./static"
#dir_path_public = "./public"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        print(f"Base path set to: {basepath}")
    else:
        basepath = "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    static_to_public(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)
    #generate_pages_recursive(
        #os.path.join(dir_path_content, "index.md"),
        #template_path,
        #os.path.join(dir_path_public, "index.html"),
    #)


main()
