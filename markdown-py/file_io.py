def read_md_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_md_file(file_path, contents):
    with open(file_path, "w") as file:
        file.write(contents)