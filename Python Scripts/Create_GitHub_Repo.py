#Works on Android
import requests
#my password credentials file is called pw.py
import pw

#Set the user agent
HEADERS = {
    "Authorization": f"Token {pw.git}",
    "User-Agent": "MyPythonScript",
}

#Prompt the user to enter the name of the repository
repository_name = input("Enter the name of the repository: ")

#Prompt the user to choose between public and private
visibility = input("Make Repo visible '1' for Public or '2' for Private: ")

#Set the visibility of the repository based on user input
if visibility.lower() == "1":
    visibility = False
else:
    visibility = True

#Set the description of the repository
description = input("Enter the description here: ")
#Set the name and description of the repository
data = {
    "name": repository_name,
    "description": description,
    "private": visibility,
}

#Send the POST request to the GitHub API to create the repository
response = requests.post(
    "https://api.github.com/user/repos", json=data, headers=HEADERS
)

# heck the status code of the response
if response.status_code == 201:
    print("Repository created successfully")
else:
    print("Error creating repository")
    print(response.json())
