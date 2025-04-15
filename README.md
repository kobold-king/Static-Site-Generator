# Static-Site-Generator
Boot.dev guided project #3

Project Notes
================================
python3 -m http.server 8888 -> starts local server
ctrl - C   to end

http://localhost:8888 to open index page

markdown cheat sheet
https://www.markdownguide.org/cheat-sheet/

HTML ref list
https://developer.mozilla.org/en-US/docs/Web/HTML/Element

The Plan:

The flow of data through the full system is:

    1. Markdown files are in the /content directory. A template.html file is in the root of the project.
    2. The static site generator (the Python code in src/) reads the Markdown files and the template file.
    3. The generator converts the Markdown files to a final HTML file for each page and writes them to the /public directory.
    4. We start the built-in Python HTTP server (a separate program, unrelated to the generator) to serve the contents of the /public directory on http://localhost:8888 (our local machine).
    5. We open a browser and navigate to http://localhost:8888 to view the rendered site.

How the SSG Works

The vast majority of our coding will happen in the src/ directory because almost all of the work is done in steps 2 and 3 above. Here's a rough outline of what the final program will do when it runs:

    1. Delete everything in the /public directory.
    2. Copy any static assets (HTML template, images, CSS, etc.) to the /public directory.
    3. Generate an HTML file for each Markdown file in the /content directory. For each Markdown file:
        1. Open the file and read its contents.
        2. Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
        3. Convert each block into a tree of HTMLNode objects. For inline elements (like bold text, links, etc.) we will convert:
            Raw markdown -> TextNode -> HTMLNode
        4. Join all the HTMLNode blocks under one large parent HTMLNode for the pages.
        5. Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant HTML string and inject it in the HTML template.
        6. Write the full HTML string to a file for that page in the /public directory.eee

HOW THE  TEXT to TEXTHTML works:

key notes: Lists preserve the order of the elements that are inserted into them, elements can reassigned sequentially as we pass the methods through them

The key insight is that split_nodes_delimiter takes a list of nodes as input and returns a new list of nodes. Each time you call it, you're transforming the entire list.

Here's what happens:

    You start with nodes = [TextNode(text, TextType.TEXT)] - a single node containing the entire text.

    When you call split_nodes_delimiter(nodes, "**", TextType.BOLD), it:
        Looks through each existing node
        If the node is of type TEXT, it splits it by the "**" delimiter
        It returns a new list where the TEXT nodes containing "**" have been replaced by multiple nodes: TEXT, BOLD, TEXT
        The order is preserved because it's splitting sequentially

    Then you take that new list and apply split_nodes_delimiter(nodes, "_", TextType.ITALIC):
        Again, it only processes TEXT nodes (not BOLD ones from the previous step)
        It splits those TEXT nodes that contain "_" into TEXT, ITALIC, TEXT
        The previously created BOLD nodes remain unchanged

    The same happens with the CODE markers.

    Your check_node functions (which I assume handle links and images) work on the same principle.

Each step builds on the results of the previous one, preserving order while adding more granular node separation. The nodes don't become "different things" - the list gets progressively more detailed with each special markdown feature being processed.

I notice you're calling check_node twice at the end. Are these meant to be separate functions for handling images and links? If so, you might want to rename them to be more descriptive of their purpose.
