from htmlnode import ParentNode, LeafNode
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

    return ParentNode("div", [html_node_list])

def block_to_html_node(block, blocktype):
    #strip the markdown text so it doesn't show in the html
    match(blocktype):
        case BlockType.HEADING:
            header, text = block.split(maxsplit=1)
            count = header.count("#")
            return ParentNode(f"h{count}", text_to_htmlnode(block))
        case BlockType.QUOTE:
                pass
        case BlockType.UNLIST:
            pass
        case BlockType.OLIST:
            pass
        case BlockType.CODE:
            pass
        case BlockType.PARAGRAPH:
            return ParentNode('p', text_to_htmlnode(block))

def text_to_htmlnode(text):
    text_nodes = text_to_textnodes(text)
    children_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return children_nodes


#take text in block and create textnodes  -  text_to_textnodes
#take the text nodes and convert them to leafnodes  -  text_node_to_html_node
#leafnodes are placed in a parent node for that block
#all blocks are placed into 1 last parent block with div

    #return ParentNode("div", blocknodes)
