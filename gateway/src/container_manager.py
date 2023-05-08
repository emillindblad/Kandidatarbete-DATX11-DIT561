from os import close
import docker, docker.errors
import random
import json


client = docker.from_env()
temp_name="sqli-challenge"

def start(challenge_id):
# def start():
    #TODO: probably refactor the container mangement to a different file when using more containers


    data = get_info(challenge_id)
    dockerfile_path = f"../../{data['path']}"
    image, log_generator = client.images.build(path=dockerfile_path, rm=True)
    print(image.id)
    port = random.randint(8001,8030)

    try:
        container = client.containers.run(image.id, ports={5000:port}, name=data["container_name"], detach=True)

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


