import unittest

from blocktype_block_to_block import block_to_block_type, BlockType

class TestBlockTypes(unittest.TestCase):
    def test_basic_paragraph(self):
        blocktype = [block_to_block_type("Basic Ass Text.")]
        self.assertListEqual([BlockType.PARAGRAPH], blocktype)

    def test_basic_header(self):
        blocktype = [block_to_block_type("# Header 1")]
        self.assertListEqual([BlockType.HEADING], blocktype)

    def test_basic_code(self):
        blocktype = [block_to_block_type("```code```")]
        self.assertListEqual([BlockType.CODE], blocktype)

    def test_basic_quote(self):
        blocktype = [block_to_block_type(">quote\n>quote2")]
        self.assertListEqual([BlockType.QUOTE], blocktype)

    def test_basic_ordered_list(self):
        blocktype = [block_to_block_type("1. This is a list\n2. with items")]
        self.assertListEqual([BlockType.OLIST], blocktype)

if __name__ == "__main__":
    unittest.main()
