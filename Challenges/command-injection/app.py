from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route("/", methods=('GET','POST'))
def index():
    if request.method == 'POST':
        input = request.form['man']
        command = f"man {input}"
        result = subprocess.run(command, shell=True,capture_output=True)
        if result.returncode != 0:
            error = f'No manual entry for {input}'
            return render_template('index.html', data=error)
        output = result.stdout

        # Decode the byte string into a string and replace escape codes with HTML tags
        parsed = output.decode('utf-8').replace('\n', '<br>').replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;').replace('\x08', '')


        return render_template('index.html', data=parsed)

    return render_template('index.html')
