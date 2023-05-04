import requests
import os

# Set access token. This decides which user the flag gets submitted from.
# Currently a access token for the test user Pelle 
admin_token = "23cf13f61cf70b667ec38d0040b7f1450ab809930817d9379018e42b3525e3ad"

# Function to submit the flag on behalf of a user
def submit_flag(user_id, challenge_id, flag, ctfd_base_url, admin_token):
    # Construct the URL
    url = f"{ctfd_base_url}/api/v1/challenges/attempt"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {admin_token}",
    }

    # JSON data
    data = {
        "user_id": user_id,
        "challenge_id": challenge_id,
        "submission": flag,
    }

    # Send the request
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Flag submitted on behalf of the user.")
    else:
        print("Error: Unable to submit the flag.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")

#User id doesn't matter for now...
user_id = 6
challenge_id = 11
flag = "jfifsdse3hfdffkj"

# Set CTFd instance URL
ctfd_base_url = "http://ctfortress.ddns.net:8081"

submit_flag(user_id, challenge_id, flag, ctfd_base_url, admin_token)
