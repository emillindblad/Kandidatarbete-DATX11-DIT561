from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route("/", methods=('GET','POST'))
def index():
    if request.method == 'POST':
        input = request.form['man']
        command = f"man {input}"
        output = subprocess.run(command, shell=True,capture_output=True)
        return render_template('index.html', data=output)

    return render_template('index.html')
