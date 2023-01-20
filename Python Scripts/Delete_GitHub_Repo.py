import requests
import json
import pw

# Make a GET request to the GitHub API to get a list of the user's repos
headers = {"Authorization": f"token {pw.git}"}
response = requests.get("https://api.github.com/user/repos", headers=headers)

# Check that the API call was successful
if response.status_code == 200:
    # Load the response data into a Python object
    repos = json.loads(response.content)

    # Print the names and numbers of the user's repos
    for i, repo in enumerate(repos):
        print(f"{i+1}. {repo['name']}")
else:
    print("Failed to retrieve repos")

# Prompt the user to enter a repo number to delete
repo_number = input("Enter the number of the repo you want to delete: ")

# Get the repo name corresponding to the entered number
repo_name = repos[int(repo_number) - 1]['name']

# Make a DELETE request to the GitHub API to delete the repo
response = requests.delete(f"https://api.github.com/repos/{pw.gitu}/{repo_name}", headers=headers)

# Check that the API call was successful
if response.status_code == 204:
    print(f"Successfully deleted repo {repo_name}")
else:
    print("Failed to delete repo")
