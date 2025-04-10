from extract_links import extract_markdown_links, extract_markdown_images

def test_extract_markdown_images1(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extract_markdown_images2(self):
    matches = extract_markdown_images(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    )
    self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    )
    self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

def test_extract_markdown_links_no_anchor(self):
    matches = extract_markdown_links(
        "This is text with a link [](https://www.boot.dev)"
    )
    self.assertListEqual([("", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
