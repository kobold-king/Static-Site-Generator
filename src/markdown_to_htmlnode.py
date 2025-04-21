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
            header, text = block.split(maxsplit=1)
            count = header.count("#")
            return ParentNode(f"h{count}", text_to_htmlnode(block))
        case BlockType.QUOTE:
            block.strip(">")
            return ParentNode("blockquote", text_to_htmlnode(block))
        case BlockType.UNLIST:
            return ParentNode("ul", text_to_htmlnode(block))
        case BlockType.OLIST:
            return ParentNode("ol", text_to_htmlnode(block))
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

def text_to_list_nodes(list, type):
    list_lines = list.splitlines()
    nodes = []
    for lines in list_lines:
        nodes.append(ParentNode("li", text_to_htmlnode(lines)))
    return nodes


#take text in block and create textnodes  -  text_to_textnodes
#take the text nodes and convert them to leafnodes  -  text_node_to_html_node
#leafnodes are placed in a parent node for that block
#all blocks are placed into 1 last parent block with div

    #return ParentNode("div", blocknodes)
