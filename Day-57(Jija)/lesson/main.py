from datetime import datetime
from flask import Flask
from flask import render_template
import random
import requests
from twilio.rest.api.v2010.account.recording.add_on_result.payload import data

app = Flask(__name__)

def get_gender(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    return data["gender"]

def get_age(name):
    response = requests.get(url=f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    return data["age"]

@app.route("/guess/<name>")
def guess(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("guess.html", gender=gender, name=name,age=age)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    response.raise_for_status()
    data = response.json()
    return render_template("blog.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)