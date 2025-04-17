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
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if "- " in block:
        split_block = block.split("\n")
        for line in split_block:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
                break
        return BlockType.UNLIST

    if block.startswith("1. "):
        i = 1
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST

    return BlockType.PARAGRAPH
