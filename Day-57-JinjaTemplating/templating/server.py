import random
import datetime
import requests
from flask import Flask, render_template
app = Flask(__name__)

AGIFY_ENDPOINT = "https://api.agify.io?name="
GENDERIZE_ENDPOINT = "https://api.genderize.io/?name="
BLOG_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    random_number = random.randint(1, 100)
    name = "Fukurou"
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, name=name, current_year=year)

@app.route('/guess/<name>')
def guess(name):
    agify_data = requests.get(f"{AGIFY_ENDPOINT}{name}").json()
    predicted_age = agify_data['age']
    genderize_data = requests.get(f"{GENDERIZE_ENDPOINT}{name}").json()
    predicted_gender = genderize_data['gender']
    return render_template("guess.html", name=name, age=predicted_age, gender=predicted_gender)


@app.route('/blog/<num>')
def get_blog(num):
    all_posts = requests.get(BLOG_ENDPOINT).json()
    return render_template("blog.html", posts=all_posts)





if __name__ == "__main__":
    app.run(debug=True)