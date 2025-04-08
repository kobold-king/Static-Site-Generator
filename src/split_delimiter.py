from textnode import TextNode, TextType

allowed_delimiters = ["**", "_", "`"]

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Validate the delimiter BEFORE processing nodes
    if delimiter not in allowed_delimiters:
        raise Exception("Invalid Markdown syntax")

    textnode_list = []

    #split nodes in sepperate nodes
    for node in old_nodes:
        #check to see if node is not TextType.TEXT
        if node.text_type != TextType.TEXT:
            textnode_list.append(node)
            continue

        extra_list = recursive_delimiter_finder(node.text, delimiter, text_type)
        textnode_list.extend(extra_list)

    return textnode_list

def recursive_delimiter_finder(text, delimiter, text_type, wip_list=None):
    result = wip_list or []
    #check if text is now empty
    if not text:
        return result  # No more work to do, just return the list

        #check to see if anymore delimiters exist in text
    if delimiter not in text:
        result.append(TextNode(text, TextType.TEXT))
        return result  # All done for this branch of recursion


    split_text = text.split(delimiter, maxsplit=2)

    # Check for balanced delimiters
    if len(split_text) < 3:
        raise Exception(f"Unbalanced delimiter: {delimiter} in '{text}'")

    # If the first part is not empty, append it as plain text
    if split_text[0]:
        result.append(TextNode(split_text[0], TextType.TEXT))

    # Append the part inside the delimiters with its special type
    result.append(TextNode(split_text[1], text_type))

    # Recurse on the remaining part of the string
    return recursive_delimiter_finder(split_text[2], delimiter, text_type, result)
