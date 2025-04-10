import re

def extract_markdown_images(text):
    images_alts = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return images_alts

def extract_markdown_links(text):
    links_anchors = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return links_anchors
