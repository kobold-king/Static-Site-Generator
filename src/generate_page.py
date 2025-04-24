from markdown_to_htmlnode import extract_title, markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    fpath = from_path
    tpath = template_path
    dpath = dest_path

    print(f"Generating page from {fpath} to {dpath} using {tpath}.")

    #Read the markdown file at from_path and store the contents in a variable.
    index = open(fpath, 'r').read()
    #Read the template file at template_path and store the contents in a variable.
    template = open(tpath, 'r').read()

    node = markdown_to_html_node(index)
    html = node.to_html()
    title = extract_title(index)

    #Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    updated_template = replace_lines(template, title, html)

    # Construct the full file path
    file_path = os.path.join(dpath, "index.html")

    # Write the variable to the file
    with open(file_path, 'w') as file:
        file.write(updated_template)


def replace_lines(template, title, html):
    change_1 = template.replace("{{ Title }}", title)
    change_2 = change_1.replace("{{ Content }}", html)
    return change_2
