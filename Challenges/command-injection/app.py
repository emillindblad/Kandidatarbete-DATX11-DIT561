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
            return render_template('index.html', error=error)

        parsed = subprocess.check_output(f"{command} | groff -Thtml -mandoc 2>/dev/null",shell=True,text=True)
        return render_template('index.html', data=parsed)

    return render_template('index.html')
