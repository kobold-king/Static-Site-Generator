from extract_links import extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType

def check_node(nodes):
    new_node_list = []

    for node in nodes:
        #Check to see if node is coorect text type
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
            continue
        #Checkk to see if the node is a image or just a link
        if "![" in node.text:
            new_image_nodes = split_nodes_image(node)
            new_node_list.extend(new_image_nodes)

        else:
            new_link_nodes = split_nodes_link(node)
            new_node_list.extend(new_link_nodes)

    return new_node_list

def split_nodes_image(old_node):
    new_nodes = []

    image_extraction = extract_markdown_images(old_node.text)
    updated_node_text = old_node.text

    if len(image_extraction) == 0:
        new_nodes.append(old_node)

    for image_alt, image_url in image_extraction:
        if updated_node_text == "":
            break

        split_text = updated_node_text.split(f"![{image_alt}]({image_url})", 1)

        #if len(split_text) != 2:
                #raise ValueError("Invalid markdown, image section not closed")
        if split_text[0] == "":
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            updated_node_text = split_text[1]

        else:
            new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            updated_node_text = split_text[1]

        if updated_node_text != "" and "![" not in updated_node_text:
            new_nodes.append(TextNode(updated_node_text, TextType.TEXT))
            updated_node_text = ""


    return new_nodes


def split_nodes_link(old_node):
    new_nodes = []

    link_extraction = extract_markdown_links(old_node.text)
    updated_node_text = old_node.text

    if len(link_extraction) == 0:
        new_nodes.append(old_node)

    for link_alt, link_url in link_extraction:
        if updated_node_text == "":
            break

        split_text = updated_node_text.split(f"[{link_alt}]({link_url})", 1)

        #if len(split_text) != 2:
                #raise ValueError("Invalid markdown, image section not closed")
        if split_text[0] == "":
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            updated_node_text = split_text[1]

        else:
            new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            updated_node_text = split_text[1]

        if updated_node_text != "" and " [" not in updated_node_text:
            new_nodes.append(TextNode(updated_node_text, TextType.TEXT))
            updated_node_text = ""


    return new_nodes
