import unittest

from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_text_to_textnodes(self):
            new_nodes = text_to_textnodes(
                "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            )

            self.assertEqual(
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ],
                new_nodes,
            )

    def test_text_to_textnodes_mixed(self):
            new_nodes = text_to_textnodes(
                "This is _italic text_ with a **BOLD** word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            )

            self.assertEqual(
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("italic text", TextType.ITALIC),
                    TextNode(" with a ", TextType.TEXT),
                    TextNode("BOLD", TextType.BOLD),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ],
                new_nodes,
            )


if __name__ == "__main__":
    unittest.main()
