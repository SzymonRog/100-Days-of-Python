import requests
from flask import Flask, render_template


app = Flask(__name__)


def get_blogs():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    response.raise_for_status()
    return response.json()

@app.route('/')
def home():
    blogs = get_blogs()
    return render_template("index.html", blogs=blogs)

@app.route("/blog/<int:index>")
def get_blog_post(index):
    blog = get_blogs()[index - 1]
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
