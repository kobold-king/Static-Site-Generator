import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitDelim(unittest.TestCase):
    def test_split1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_unbalanced_delimiters(self):
        node = TextNode("Unbalanced delimiter here `code block unfinished", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("Unbalanced delimiter: ` in 'Unbalanced delimiter here `code block unfinished'", str(context.exception))

    def test_consecutive_delimiters(self):
        node = TextNode("This is a **boldphrase****word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("boldphrase", TextType.BOLD),
            TextNode("", TextType.TEXT),  # Handles splitting properly
            TextNode("word", TextType.BOLD)
        ])

    def test_empty_node_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("", TextType.TEXT)])

    def test_mixed_types_in_old_nodes(self):
           mixed_nodes = [
               TextNode("This is text", TextType.TEXT),
               TextNode("Not to process", TextType.BOLD),  # Should pass through untouched
               TextNode("Here we have `code` inside", TextType.TEXT),
           ]
           new_nodes = split_nodes_delimiter(mixed_nodes, "`", TextType.CODE)
           self.assertEqual(new_nodes, [
               TextNode("This is text", TextType.TEXT),
               TextNode("Not to process", TextType.BOLD),
               TextNode("Here we have ", TextType.TEXT),
               TextNode("code", TextType.CODE),
               TextNode(" inside", TextType.TEXT),
           ])

if __name__ == "__main__":
    unittest.main()
