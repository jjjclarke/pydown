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

def convert_lists(lines):
    in_list = False
    in_ordered_list = False
    list_type = ""
    html_lines = []

    for line in lines:
        if re.match(r'^\s*[\*\-\+]\s+', line):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
                list_type = "ul"
            html_lines.append(f"<li>{line.strip()[2:]}</li>")
        elif re.match(r'^\s*\d+\.\s+', line):
            if not in_ordered_list:
                html_lines.append("<ol>")
                in_ordered_list = True
                list_type = "ol"
            html_lines.append(f"<li>{line.strip()[3:]}</li>")
        else:
            if in_list or in_ordered_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
                in_ordered_list = False
            html_lines.append(line)
    
    if in_list or in_ordered_list:
        html_lines.append(f"</{list_type}>")

    return html_lines

def convert_images(line):
    # the blind leading the blind ( i don't know if this will work )
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img alt="\1" src="\2" />', line)

def convert_blockquotes(lines):
    in_blockquotes = False
    html_lines = []

    for line in lines:
        if line.startswith('>'):
            if not in_blockquotes:
                html_lines.append('<blockquote>')
                in_blockquotes = True
            html_lines.append(line[1:].strip())
        else:
            if in_blockquotes:
                html_lines.append('</blockquote>')
                in_blockquotes = False
            html_lines.append(line)

    if in_blockquotes:
        html_lines.append('</blockquote>')

    return html_lines

def convert_horizontal_rules(line):
    if re.match(r'^\s*([-*_]){3,}\s*$', line):
        return '<hr />'
    return line