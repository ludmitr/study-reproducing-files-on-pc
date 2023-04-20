# https://academy.masterschool.com/ns/books/published/swe/WritingFiles/6-ReproducingFilesOnYourComputer.html
def main():
    create_identical_file("olympic-medals.csv", "olympic-medals-copy.csv")
    create_file_with_n_lines("olympic-medals.csv", "olympic-medals-copy.csv", 5)

def create_identical_file(original_file_path: str, file_path_to_copy: str):
    """creates copy in file_path_to_copy from original_file_path"""
    with open(original_file_path, "r") as file:
        original_data = file.read()
    with open(file_path_to_copy, "w") as file:
        file.write(original_data)


def create_file_with_n_lines(original_file_path: str, file_path_to_copy: str, num_lines: int):
    """
    creates copy from original_file_path
    with num_lines in file_path_to_copy
    """
    with open(original_file_path, "r") as file:
        original_data = file.read()

    lines = original_data.split("\n")

    # checking if num_lines in range of lines in data and adding lines file_path_to_copy
    if num_lines <= len(lines):
        with open(file_path_to_copy, "w") as file:
            for line in lines[:num_lines]:
                file.write(line + "\n")


if __name__ == '__main__':
    main()
