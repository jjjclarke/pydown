import sys
from converter import markdown_to_html
from file_io import read_md_file, write_html_file

def main(input_file_name, output_file_name):
    markdown_text = read_md_file(input_file_name)
    html_text = markdown_to_html(markdown_text)
    write_html_file(output_file_name, html_text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("")
    else:
        main(sys.argv[1], sys.argv[2])