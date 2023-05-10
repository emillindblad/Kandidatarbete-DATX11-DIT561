from os import close
import docker, docker.errors
import random
import json
from flag_generator import generate_flag
from ctfd_api_caller import add_challenge_flag, delete_challenge_flag

client = docker.from_env()
temp_name="sqli-challenge"

def start(challenge_id, user_id):
    info = get_info(challenge_id)
    # dockerfile_path = f"../../{data['path']}"
    # image, log_generator = client.images.build(path=dockerfile_path, rm=True)
    # print(image.id)
    existing_image_id = info['image-id']
    port = random.randint(8200,8400)
#    unique_id = str(uuid.uuid4())[:8]
#    container_name = f"{data['container_name']}-{unique_id}"

    try:
        flag = generate_flag(user_id, challenge_id)
        print(flag)
        container = client.containers.run(existing_image_id, ports={info["port"]:port}, name=f"{user_id}-{info['container_name']}", detach=True, environment={'FLAG': flag})
        flag_id = add_challenge_flag(challenge_id, flag)
        return {
            "msg" : f"Container {container.name} started with id {container.short_id}",
            "port" : port,
            "on" : True,
            "flag_id" : flag_id
        }

    except (docker.errors.ContainerError, docker.errors.ImageNotFound,  docker.errors.APIError ) as e:
    #TODO: catch error if port is busy
        print(e)
        return {
            "succuess" : False,
            "error" : e
        }


def stop(challenge_id, user_id, flag_id):
    info = get_info(challenge_id)
    container_name = f"{user_id}-{info['container_name']}"
    try:
        container = client.containers.get(container_name)
        container.stop()
        container.remove()
        delete_challenge_flag(flag_id)
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

