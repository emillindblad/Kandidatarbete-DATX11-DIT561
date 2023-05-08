from flask import Flask, render_template, g, request, url_for, redirect
import container_manager


app = Flask(__name__)

temp_name="sqli-challenge"

status = {
    "msg" : "",
    "on" : False,
}

@app.route("/<int:challenge_id>")
def index(challenge_id):
    container_info = container_manager.get_info(challenge_id)

    data = {}
    status = container_manager.check_status(temp_name)
    if status["on"]:
        data["on"] = status["on"]
    return render_template('index.html', challenge_id=container_info["name"], status=data)

@app.route("/<int:challenge_id>/container_start", methods=['POST'])
def start(challenge_id):
    res = container_manager.start(challenge_id)
    print("@@@start@@@")
    print(res)

    return redirect(url_for('index', challenge_id=challenge_id))

@app.route("/<int:challenge_id>/container_stop", methods=['POST'])
def container_stop(challenge_id):
    res = container_manager.stop()
    print("@@@stop@@@")
    print(res)

    return redirect(url_for('index', challenge_id=challenge_id))
