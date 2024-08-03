import sys, os, shutil
from converter import markdown_to_html, template_dir
from file_io import read_md_file, write_html_file

def main(input_file_name, output_file_name):
    markdown_text = read_md_file(input_file_name)
    html_text = markdown_to_html(markdown_text)
    write_html_file(output_file_name, html_text)
    
    # here, must copy the CSS file from templates dir
    # to make sure that it can actually read it
    shutil.copy(os.path.join(template_dir, 'style.css'), os.path.join(os.path.dirname(output_file_name), 'style.css'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("")
    else:
        main(sys.argv[1], "output/index.html")