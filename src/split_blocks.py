def markdown_to_blocks(markdown):
    lines =  markdown.split("\n\n")
    blocks = []

    for line in lines:
        striptext = line.strip()

        if striptext =="":
            continue

        elif "\n" in striptext:
            result = "\n".join(item.strip() for item in striptext.split("\n"))
            blocks.append(result)

        else:
            blocks.append(striptext)


    return blocks
