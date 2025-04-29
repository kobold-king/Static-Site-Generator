from htmlnode import ParentNode
from blocktype_block_to_block import block_to_block_type, BlockType
from textnode import TextType, TextNode, text_node_to_html_node
from split_blocks import markdown_to_blocks
from text_to_textnode import text_to_textnodes



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_node_list = []
    #grandchild_node = LeafNode("b", "grandchild") #text in the block
    #child_node = ParentNode("span", [grandchild_node]) #each of the blocks
    for block in blocks:
        blocktype = block_to_block_type(block)
        html_node_list.append(block_to_html_node(block, blocktype))

    return ParentNode("div", html_node_list)

def block_to_html_node(block, blocktype):
    #strip the markdown text so it doesn't show in the html
    match(blocktype):
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNLIST:
            items = block.split("\n")
            html_items = []
            for item in items:
                text = item[2:]
                children = text_to_htmlnode(text)
                html_items.append(ParentNode("li", children))
            return ParentNode("ul", html_items)
        case BlockType.OLIST:
            items = block.split("\n")
            html_items = []
            for item in items:
                text = item[3:]
                children = text_to_htmlnode(text)
                html_items.append(ParentNode("li", children))
            return ParentNode("ol", html_items)
        case BlockType.CODE:
            # Extract text for code block
            # Assuming the format is "```\ncode content\n```"
            lines = block.split("\n")
            # Remove the first and last lines (the ones with ```)
            code_content = "\n".join(lines[1:-1])

            # Make sure there's a trailing newline
            if not code_content.endswith("\n"):
                code_content += "\n"

            # Create nodes
            text_node = TextNode(code_content, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [html_node])
            pre_node = ParentNode("pre", [code_node])
            return pre_node
        case BlockType.PARAGRAPH:
            # Replace newlines with spaces for paragraph text
            text = block.replace("\n", " ")
            # Create children nodes with inline markdown parsing
            #children = text_to_children(text)
            return ParentNode("p", text_to_htmlnode(text))


def text_to_htmlnode(text):
    text_nodes = text_to_textnodes(text)
    children_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return children_nodes

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_htmlnode(text)
    return ParentNode(f"h{level}", children)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_htmlnode(content)
    return ParentNode("blockquote", children)
#take text in block and create textnodes  -  text_to_textnodes
#take the text nodes and convert them to leafnodes  -  text_node_to_html_node
#leafnodes are placed in a parent node for that block
#all blocks are placed into 1 last parent block with div

    #return ParentNode("div", blocknodes)
