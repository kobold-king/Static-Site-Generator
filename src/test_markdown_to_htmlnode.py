import unittest

from markdown_to_htmlnode import markdown_to_html_node
from generate_page import extract_title

class TestMDtoHTMLnode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title_1(self):
        md = """
    # This is a level 1 header
    """
        text = extract_title(md)
        self.assertEqual(
            text,
            "This is a level 1 header",
        )

    def test_extract_title_2(self):
        md = """
        # This is a level 1 header
        ## This is a level 2 header
        This is a normal line.
        ### This is a level 3 header
        """
        text = extract_title(md)
        self.assertEqual(
            text,
            "This is a level 1 header",
        )
if __name__ == "__main__":
    unittest.main()
