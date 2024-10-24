import os
from utils import (
    convert_formatting,
    convert_heading,
    convert_links,
    convert_code_blocks,
    convert_lists,
    convert_images,
    convert_blockquotes,
    convert_horizontal_rules
)

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

def markdown_to_html(markdown_text):
    html_lines = []

    lines = markdown_text.split("\n")
    lines = convert_code_blocks(lines)
    lines = convert_lists(lines)
    lines = convert_blockquotes(lines)

    for line in lines:
        html_line = convert_heading(line)
        if html_line is None:
            if not line.startswith("<code><pre>") and not line.startswith("</pre></code>"):
                line = convert_formatting(line)
                line = convert_links(line)
                line = convert_images(line)
                line = convert_horizontal_rules(line)
                html_line = f'<p>{line}</p>' if line.strip() else ''
            else:
                html_line = line
        html_lines.append(html_line)
        
    return wrap_around_template("\n".join(html_lines))

def load_template(file_path):
    with open(os.path.join(template_dir, file_path), 'r') as file:
        return file.read()

def wrap_around_template(content):
    html_template = load_template("index.html")
    return html_template.replace("{content}", content)