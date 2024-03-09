from flask import Flask, render_template
import requests
api = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get(api)
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/blog/<int:num>')
def get_blog(num):
    response = requests.get(api)
    posts = response.json()
    return render_template("post.html", posts=posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)
