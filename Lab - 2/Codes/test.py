import difflib

def read_go_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def compare_go_files(file_path_old, file_path_new):
    lines_old = read_go_file(file_path_old)
    lines_new = read_go_file(file_path_new)
    
    output_file = "changes.txt"
    

    diff = difflib.unified_diff(lines_old, lines_new, fromfile=file_path_old, tofile=file_path_new)
    print(diff)

    # differ = difflib.Differ()
    # diff2 = list(differ.compare(lines_old, lines_new))
    # print(diff2)

    # with open("output_file.txt", "w") as f:
    #     f.write("File\t\tAdditions\tDeletions\n")
    #     f.write("--------------------------------\n")
    #     for line in diff:
    #         additions, deletions, filename = line.split("\t")
    #         f.write(f"{filename}\t{additions}\t\t{deletions}\n")


    # Print the differences
    for line in diff:
        print(line, end='')

if __name__ == "__main__":
    
    file_path_old = f"./../files/fileA.go"
    file_path_new = f"./../files/fileB.go"
    
    try:
        compare_go_files(file_path_old, file_path_new)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)
