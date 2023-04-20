# https://academy.masterschool.com/ns/books/published/swe/WritingFiles/6-ReproducingFilesOnYourComputer.html
def main():
    pass


def create_identical_file(file_path: str, file_path_to_copy: str):
    """receive existing file path and creates copy in file_path_to_copy"""
    with open(file_path, "r") as file:
        file_copy = file.read()
    with open(file_path_to_copy, "w") as file:
        file.write(file_copy)


if __name__ == '__main__':
    main()