import requests
import json

new_post = {
    "title": "My First API Post",
    "body": "Learning HTTP with Python!",
    "userId": 1
}

try:
    response = requests.get("https://api.github.com/users/anthropics/repos")
    print(f"Status Code: {response.status_code}")
    repos = response.json()
    with open("test.json", "w") as f:
        json.dump(repos, f, indent=2)
    

except requests.exceptions.ConnectionError:
    print("Could not connect to server")


