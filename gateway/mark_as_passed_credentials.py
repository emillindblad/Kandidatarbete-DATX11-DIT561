import requests

# Doesn't currently work. Seems like CTFd doesn't allow logins through scripts.  
# Could potentially create script that simulates browser activity using somethinng like selenium
def login_and_submit_flag(username, password, challenge_id, flag, ctfd_base_url):
    # Log in as the user
    login_url = f"{ctfd_base_url}/login"
    login_data = {
        "name": username,
        "password": password,
    }
    session = requests.Session()
    login_response = session.post(login_url, data=login_data)

    if "invalid" in login_response.text.lower():
        print("Error: Invalid username or password.")
        return

    # Submit the flag
    submit_url = f"{ctfd_base_url}/api/v1/challenges/attempt"
    submit_data = {
        "challenge_id": challenge_id,
        "submission": flag,
    }
    submit_response = session.post(submit_url, json=submit_data)

    if submit_response.status_code == 200:
        print("Flag submitted on behalf of the user.")
    else:
        print("Error: Unable to submit the flag.")
        print(f"Status Code: {submit_response.status_code}")
        print(f"Response: {submit_response.json()}")


username = "Pelle"
password = "pelle"
challenge_id = 11
flag = "jfifsdse3hfdffkj"

# Set CTFd instance URL
ctfd_base_url = "http://ctfortress.ddns.net:8081"

login_and_submit_flag(username, password, challenge_id, flag, ctfd_base_url)
