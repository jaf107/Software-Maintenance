import difflib

def read_go_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def compare_go_files(file_path_old, file_path_new):
    lines_old = read_go_file(file_path_old)
    lines_new = read_go_file(file_path_new)
    
    additions = 0
    deletions = 0
    
    diff = difflib.unified_diff(lines_old, lines_new, fromfile=file_path_old, tofile=file_path_new)

    for line in diff:
        if line.startswith('+'):
            additions += 1
        elif line.startswith('-'):
            deletions += 1
        # print(line, end='')
        
    total_changes = int(additions) + int(deletions)

    output_file = "t2_changes_count.txt"
    
    with open(output_file, "w") as f:
        f.write(f"\tAdditions\tDeletions\tTotal Changes made\n")
        f.write("--------------------------------------------\n")
        f.write(f"\t\t{additions}\t\t\t{deletions}\t\t\t{total_changes}")

    print(f"\tAdditions\tDeletions\tTotal Changes made")
    print(f"\t{additions}\t\t{deletions}\t\t{total_changes}")


if __name__ == "__main__":
    file_path_old = f"./../files/fileA.go"
    file_path_new = f"./../files/fileB.go"
    
    try:
        compare_go_files(file_path_old, file_path_new)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)
