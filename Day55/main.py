from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world'


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"hello dammn {name}"


app.run(debug=True)