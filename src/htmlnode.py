class HTMLNode:
    # tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    # value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    # children - A list of HTMLNode objects representing the children of this node
    # props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag =  tag
        self.value =  value
        self.children = children
        self.props =  props

    def to_html(self):
        raise NotImplementedError("Subclasses must implement the to_html method")
        #should raise ths error if a subcass does not contain the to_html method and soething tries to use it

    def props_to_html(self):
        if self.props is None:
            return ""

        props_html = ""

        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return(f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class LeafNode(HTMLNode):
