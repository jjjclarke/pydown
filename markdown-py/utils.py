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