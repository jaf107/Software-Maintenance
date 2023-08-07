import git

def get_repository_changes(repo_path, commit_sha_old, commit_sha_new):
    try:
        repo = git.Repo(repo_path)
        diff = repo.git.diff(commit_sha_old, commit_sha_new)
        return diff
    except git.InvalidGitRepositoryError:
        raise Exception("Invalid Git repository path")
    except git.BadName:
        raise Exception("Invalid commit SHA")

if __name__ == "__main__":
    # repo_path = input("Enter the path of the Git repository: ")
    # commit_sha_old = input("Enter the commit SHA of the old version: ")
    # commit_sha_new = input("Enter the commit SHA of the new version: ")
    
    repo_path = "Codes\Repo"
    commit_sha_old = "5e5fb2f150630167b3228ab61b9eacb88c0a7e2a"
    commit_sha_new = "c02641ae2d926e1c6f729fb85f50227e9342688f"
    

    try:
        changes = get_repository_changes(repo_path, commit_sha_old, commit_sha_new)
        print(changes)
    except Exception as e:
        print("Error:", e)
