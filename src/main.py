from textnode import TextNode, TextType

def main():
    if __name__ == "__main__":
        instance = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        print(repr(instance))

main()
