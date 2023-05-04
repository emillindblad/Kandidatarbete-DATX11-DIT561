import requests
import json

host = "localhost"
admim_token = "adb29e71643d34f2a72715bd5f93214baade20566124beb8467e083df23e80ca"

def get_challenge_flag(challenge_id):
    url = f"http://{host}/api/v1/challenges/{challenge_id}/flags"
# params = {"id": "13"}
    params = {}
    headers = {
        "Authorization": f"Token {admim_token} ",
        "Content-Type": "application/json",
    }

    r = requests.get(url, params=params, headers=headers)

# print(r.headers)

    data = r.json()

    print(json.dumps(data,indent=4))

def add_challenge_flag(challenge_id,flag):
    url = f"http://{host}/api/v1/flags"

    headers = {
        "Authorization": f"Token {admim_token} ",
        "Content-Type": "application/json",
    }

    data = {
        "content" : flag,
        "data" : "",
        "type" : "static",
        "challenge" : challenge_id
    }

    r = requests.post(url, headers=headers, json=data)

    print(r.content)

    # data = r.json()

    # print(json.dumps(data,indent=4))

def delete_challenge_flag(flag_id):
    url = f"http://{host}/api/v1/flags/{flag_id}"

    headers = {
        "Authorization": f"Token {admim_token} ",
        "Content-Type": "application/json",
    }

    r = requests.delete(url, headers=headers)

    print(r.json())


# Also possible to post submissions using the api key of a user, in this case emil
def challenge_attempt(challenge_id, attempt):
    url = f"http://{host}/api/v1/challenges/attempt"

    headers = {
        "Authorization": "Token 5d5f3e9c1c04f8816e8b599f1a7e9a9204c97f56b2360769872495292028ec73",
        "Content-Type": "application/json",
    }

    data = {
        "challenge_id": challenge_id,
        "submission": f"{attempt}",
    }

    r = requests.post(url, headers=headers, json=data)

    print(r.content)

# get_challenge_flag(13)
# delete_challenge_flag(37)
# add_challenge_flag(13,"flag_from_api")
# challenge_attempt(28, "Just_a_test_submission")

