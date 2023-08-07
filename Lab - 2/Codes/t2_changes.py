import difflib


def compare_go_files(file_path_old, file_path_new):
    try:
        lines_old = read_go_file(file_path_old)
        lines_new = read_go_file(file_path_new)
    except FileNotFoundError:
        print("Error: One or both files not found.")
        return

    diff = difflib.unified_diff(
        lines_old, lines_new, fromfile=file_path_old, tofile=file_path_new)

    additions = deletions = 0
    filename = ""
    for line in diff:
        if line.startswith('---') or line.startswith('+++'):
            continue
        elif line.startswith('+'):
            additions += 1
        elif line.startswith('-'):
            deletions += 1
        else:
            if filename:
                print(f"File: {filename}")
                print(f"Additions: {additions}")
                print(f"Deletions: {deletions}")
                print("---------------------")
                additions = deletions = 0
            filename = line[1:].strip()

    if filename:
        print(f"File: {filename}")
        print(f"Additions: {additions}")
        print(f"Deletions: {deletions}")


def read_go_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


if __name__ == "__main__":

    file_path_old = f"./../files/fileA.go"  # Use forward slash for path
    file_path_new = f"./../files/fileB.go"  # Use forward slash for path

    compare_go_files(file_path_old, file_path_new)


# import difflib


# def is_go_file(filename):
#     return filename.endswith(".go")


# def compare_files(file1_path, file2_path):
#     with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
#         lines1 = file1.readlines()
#         lines2 = file2.readlines()

#     differ = difflib.Differ()
#     diff = list(differ.compare(lines1, lines2))

#     additions = sum(1 for line in diff if line.startswith('+ '))
#     subtractions = sum(1 for line in diff if line.startswith('- '))

#     return additions, subtractions


# def main():
#     # file1_path = input("Enter the path of the first file: ")
#     # file2_path = input("Enter the path of the second file: ")
#     file1_path = f"./../files/fileA.go"  # Use forward slash for path
#     file2_path = f"./../files/fileB.go"  # Use forward slash for path

#     additions, subtractions = compare_files(file1_path, file2_path)

#     output_filename = "file_changes.txt"
#     with open(output_filename, "w") as f:
#         f.write("File\t\tAdditions\tDeletions\tTotal Changes made\n")
#         f.write("--------------------------------------------\n")

#         diff = difflib.ndiff(open(file1_path).readlines(),
#                              open(file2_path).readlines())
#         for line in diff:
#             if line.startswith('+ ') or line.startswith('- '):
#                 _, change, filename = line.split()
#                 if is_go_file(filename):
#                     total_changes = 1 if change == '?' else int(change)
#                     f.write(
#                         f"{filename}\t{1 if change == '+' else 0}\t\t{1 if change == '-' else 0}\t\t{total_changes}\n")
#                     print(
#                         f"{filename}\t\t{1 if change == '+' else 0}\t\t{1 if change == '-' else 0}\t\t{total_changes}")

#     print(f"Results written to {output_filename}")


# if __name__ == "__main__":
#     main()
