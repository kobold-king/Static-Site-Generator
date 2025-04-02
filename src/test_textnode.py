import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        #should pass

    def test_eq2(self):
        node = TextNode("This is not a text", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
        #should pass

    def test_eq3(self):
        node = TextNode("This is SPARTA!", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


    def test_eq4(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)



    def test_eq5(self):
        node = TextNode("This is a text node", TextType.BOLD, "Eggman.html")
        node2 = TextNode("This is a text node", TextType.BOLD, "Eggman.html")
        self.assertEqual(node, node2)
        #should pass

    def test_eq6(self):
        node = TextNode("This is a text node", TextType.BOLD, "Eggman.html")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)
        #should pass

    def test_eq7(self):
        node = TextNode("This is a text node", TextType.BOLD, "Eggman.html")
        node2 = TextNode("oogabooga", TextType.CODE, "Egg.html")
        self.assertNotEqual(node, node2)
        #should pass

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
if __name__ == "__main__":
    unittest.main()
