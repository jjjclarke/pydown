import re

def convert_heading(line):
    match = re.match(r"(#+)\s*(.*)", line)
    if match:
        hashes, text = match.groups()
        level = len(hashes)
        return f"<h{level}>{text}</h{level}>"
    return None

def convert_formatting(line):
    line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
    line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
    line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)
    return line

def convert_links(line):
    line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)
    return line

def convert_code_blocks(lines):
    in_code_block = False
    html_lines = []

    for line in lines:
        if line.strip().startswith('```'):
            if in_code_block:
                html_lines.append('</pre></code>')
                in_code_block = False
            else:
                html_lines.append('<pre><code>')
                in_code_block = True
        else:
            if in_code_block:
                html_lines.append(line)
            else:
                html_lines.append(convert_formatting(convert_links(line)))

    return html_lines