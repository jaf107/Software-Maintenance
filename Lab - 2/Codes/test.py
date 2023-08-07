import difflib


def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    differ = difflib.Differ()
    diff = list(differ.compare(lines1, lines2))

    additions = sum(1 for line in diff if line.startswith('+ '))
    subtractions = sum(1 for line in diff if line.startswith('- '))

    return additions, subtractions


def main():
    # file1_path = input("Enter the path of the first file: ")
    # file2_path = input("Enter the path of the second file: ")

    file1_path = "Go/fileA.go"  # Use forward slash for path
    file2_path = "Go/fileB.go"  # Use forward slash for path

    additions, subtractions = compare_files(file1_path, file2_path)

    output = f"Additions: {additions}\nSubtractions: {subtractions}"
    print(output)

    with open("file_changes.txt", "w") as output_file:
        output_file.write(output)


if __name__ == "__main__":
    main()
