def is_single_line_comment(line):
    return line.strip().startswith("//")


def is_start_of_multi_line_comment(line):
    return line.strip().startswith("/*")


def is_end_of_multi_line_comment(line):
    return line.strip().endswith("*/")


def count_sloc(file_path):
    sloc = 0
    inside_multi_line_comment = False

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            # Ignore blank lines
            if not line:
                continue

            # Ignore single-line comments
            if is_single_line_comment(line):
                continue

            # Handle multi-line comments
            if inside_multi_line_comment:
                if is_end_of_multi_line_comment(line):
                    inside_multi_line_comment = False
                continue
            elif is_start_of_multi_line_comment(line):
                if not is_end_of_multi_line_comment(line):
                    inside_multi_line_comment = True
                continue

            sloc += 1

    return sloc


if __name__ == "__main__":
    # file_path = input("Enter the path to the Go file: ")
    file_path = f"./../files/test.go"

    try:
        sloc_count = count_sloc(file_path)
        print("Source Lines of Code (SLOC) in the file:", sloc_count)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)
