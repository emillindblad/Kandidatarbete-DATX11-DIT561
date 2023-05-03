import docker, docker.errors
import random


client = docker.from_env()
temp_name="sqli-challenge"

# def start(image, container_name): no arguments for now
def start():
    #TODO: probably refactor the container mangement to a different file when using more containers

    dockerfile_path = "../../Challenges/sql-injection"
    image, log_generator = client.images.build(path=dockerfile_path, tag=f"{temp_name}:latest", rm=True)
    print(image.id)
    port = random.randint(8001,8030)

    try:
        container = client.containers.run(image.id, ports={5000:port}, name=temp_name, detach=True)

        return {
            "msg" : f"Container started with id {container.short_id}",
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


# def stop(container_name):
def stop():
    try:
        container = client.containers.get(temp_name)
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

