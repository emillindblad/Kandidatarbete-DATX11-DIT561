from flask import Flask, render_template, session, url_for, redirect
import container_manager, os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route("/<int:challenge_id>")
def index(challenge_id):
    session['foo']='bar'
    print(session)
    info = container_manager.get_info(challenge_id)

    data = container_manager.check_status(info["container_name"])
    print(data)
    return render_template('index.html', challenge_name=info["name"], challenge_id=challenge_id, data=data)

@app.route("/<int:challenge_id>/container_start", methods=['POST'])
def start(challenge_id):
    res = container_manager.start(challenge_id)
    print("@@@start@@@")
    print(res)

    return redirect(url_for('index', challenge_id=challenge_id))

@app.route("/<int:challenge_id>/container_stop", methods=['POST'])
def container_stop(challenge_id):
    res = container_manager.stop(challenge_id)
    print("@@@stop@@@")
    print(res)

    return redirect(url_for('index', challenge_id=challenge_id))
