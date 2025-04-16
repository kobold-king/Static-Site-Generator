from enum import Enum
import re

class BlockType(Enum):
        PARAGRAPH = "paragraph"
        HEADING = "heading"
        QUOTE = "quote"
        CODE = "code"
        UNLIST = "unordered_list"
        OLIST = "ordered_list"


def block_to_block_type(block):
    pattern = r"^>(\w*)"
    matches = re.findall(pattern, block)

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if "```" in block:
        split_block = block.split("```")
        if len(split_block) < 3:
            return BlockType.PARAGRAPH
        else:
            return BlockType.CODE

    if len(matches) != 0:
        return BlockType.QUOTE

    if "- " in block:
        split_block = block.split("\n")
        for line in split_block:
            if "- " not in line:
                return BlockType.PARAGRAPH
                break
        return BlockType.UNLIST

    if ". " in block:
        split_block = block.split("\n")
        for line in split_block:
            if ". " not in line:
                return BlockType.PARAGRAPH
                break
        return BlockType.OLIST

    return BlockType.PARAGRAPH
