from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/data')
def render_path():
    foo = str(request.query_string)
    return foo

