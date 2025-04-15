from split_delimiter import split_nodes_delimiter
from split_images_links import check_node
from textnode import TextType,TextNode

def text_to_textnodes(text):
    #beginner node is made 1st
    nodes = [TextNode(text, TextType.TEXT)]
    #Node is passed in and returns new nodes
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    #new nodes are passed into step 2 and then new nodes are retrned again while preserving
    #the originally made nodes are let in the same place
    #example: after bold we have [text(with italics), BOLD, Text]
    #after italics pplit it becomes [text, italics, text, BOLD, Text]
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = check_node(nodes)
    nodes = check_node(nodes)
    return nodes
