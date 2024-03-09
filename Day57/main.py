from flask import Flask, render_template
import random
from datetime import datetime
import requests
app = Flask(__name__)


@app.route('/')
def index():
    random_number = random.randint(0, 10)
    date = datetime.now().strftime("%Y")
    return render_template('index.html', rand=random_number, date=date)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    print(type(response))
    all_posts = response.json()
    print(num)
    return render_template("blog.html", posts=all_posts)


@app.route('/guess/<name>')
def guess(name):
    parameters = {
        "name": f"{name}",
    }
    response = requests.get(url="https://api.genderize.io", params=parameters)
    gender = response.json()["gender"]
    response1 = requests.get(url="https://api.agify.io/", params=parameters)
    age = response1.json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)

