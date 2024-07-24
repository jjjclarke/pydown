from utils import convert_formatting, convert_heading, convert_links

def markdown_to_html(markdown_text):
    html_lines = []
    lines = markdown_text.split("\n")
    for line in lines:
        html_line = convert_heading(line)
        if html_line is None:
            line = convert_formatting(line)
            line = convert_links(line)
            html_line = f"<p>{line}</p>" if line.strip() else ""
        html_lines.append(html_line)
    return "\n".join(html_lines)