from os import close
import pprint
import docker, docker.errors
import random
import json
from flag_generator import generate_flag
from api_testing import add_challenge_flag 
import uuid

client = docker.from_env()
temp_name="sqli-challenge"

def start(challenge_id):
    data = get_info(challenge_id)
    # dockerfile_path = f"../../{data['path']}"
    # image, log_generator = client.images.build(path=dockerfile_path, rm=True)
    # print(image.id)
    existing_image_id = data['image-id']
    port = random.randint(8001,8030)
#    unique_id = str(uuid.uuid4())[:8]
#    container_name = f"{data['container_name']}-{unique_id}"

    try:
        container = client.containers.run(existing_image_id, ports={22:port}, name=data["container_name"], detach=True, environment={'FLAG': generate_flag("1","1","ourPassword")})
        add_challenge_flag(challenge_id, generate_flag("1","1","ourPassword"))
        return {
            "msg" : f"Container {container.name} started with id {container.short_id}",
            "port" : port,
            "on" : True
        }

    except (docker.errors.ContainerError, docker.errors.ImageNotFound,  docker.errors.APIError ) as e:
    #TODO: catch error if port is busy
        print(e)
        return {
            "succuess" : False,
            "error" : e
        }


def stop(challenge_id):
    data = get_info(challenge_id)
    try:
        container = client.containers.get(data["container_name"])
        container.stop()
        container.remove()
        return {
            "succuess" : True
        }
    except (docker.errors.APIError) as e:
        print(e)

        return {
            "succuess" : False,
            "error" : e
        }

def check_status(container_name):
    print(container_name)
    out = {}
    try:
        c = client.containers.get(container_name)

        print(c.status)
        out["on"] = False
        if c.status == "running":
            print("Container running")
            out["on"] = True
            data = client.api.containers(filters={"id" : c.short_id})
            out["port"] = data[0]["Ports"][0]["PublicPort"]

    except (docker.errors.NotFound, docker.errors.APIError) as e:
        print(f"Error: {e}")
        out["on"] = False
        out["error"] = e
    return out

def get_info(challenge_id):
    key = str(challenge_id)
    with open('challenge_mappings.json', 'r') as f:
        data=json.load(f)
    return data[key]

