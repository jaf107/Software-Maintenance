import os
from git import Repo

def is_go_file(filename):
    return filename.lower().endswith('.go')

def compare_git_versions(repo_path, commit1, commit2, output_file):
    try:
        repo = Repo(repo_path)
    except Exception as e:
        print("Error: Invalid repository path or Git repository not found.")
        return

    try:
        diff = repo.git.diff("--numstat", commit1, commit2).splitlines()
    except Exception as e:
        print("Error: Invalid commit hashes or unable to compare commits.")
        return

    with open(output_file, "w") as f:
        f.write("File\t\t\t\t\tAdditions\tDeletions\tTotal Changes made\n")
        f.write("------------------------------------------------------------------\n")
        for line in diff:
            additions, deletions, filename = line.split("\t")
            if is_go_file(filename):
                total_changes = int(additions) + int(deletions)
                f.write(f"{filename}\t\t{additions}\t\t\t{deletions}\t\t\t\t{total_changes}\n")
                print(f"{filename}\t\t{additions}\t\t\t{deletions}\t\t\t\t{total_changes}")

if __name__ == "__main__":
    # repo_path = r"E:\Lab - Software Maintenance\Test-Repo\example"
    repo_path = f"./../test-repo"
    commit1 = "19299f6048bb8ab82de0cf9266ae46356c3b12b7"
    commit2 = "3dc24130247597153c0c54156448d48a260b4a07"
    output_file = "changes_output.txt"

    # Check if the repository path is valid
    if not os.path.exists(repo_path):
        print("Invalid repository path.")
    else:
        compare_git_versions(repo_path, commit1, commit2, output_file)
