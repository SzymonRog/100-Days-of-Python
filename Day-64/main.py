from pydoc import describe

from dominate.tags import header
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'

class UpdateForm(FlaskForm):
    rating = StringField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Update")

class AddFrom(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Search")

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(500))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(500))
    img_url: Mapped[str] = mapped_column(String(500))




# CREATE TABLE


@app.route("/")
def home():
    movies = Movie.query.all()
    movies.sort(key=lambda x: x.rating, reverse=True)
    return render_template("index.html", movies=movies)

@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    form = UpdateForm()
    movie = Movie.query.filter_by(id=id).first()
    if request.method == "POST":
        form.validate_on_submit()
        rating = form.rating.data
        review = form.review.data

        if not rating == "":
            movie.rating = rating
        if not review == "":
            movie.review = review
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete(id):
    movie = Movie.query.filter_by(id=id).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET","POST"])
def add():
    form = AddFrom()
    if request.method == "POST":
        title = request.form.get("title")
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYTQyODQzMzhjYjQ1YzNlZTFiYzA1MTdlYjNiZWU5YSIsIm5iZiI6MTc2MTg0Njk4OC43OTYsInN1YiI6IjY5MDNhNmNjMThlYzRlMzI4M2U5OTc2OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.r8dc2ncEh6L_ZP3so3q2GgsZ61nM_QL_81EqNWgldWc"
        }
        params = {
            "query": title
        }

        response = requests.get(f"https://api.themoviedb.org/3/search/movie",headers=headers,params=params)
        response.raise_for_status()
        movies = response.json()["results"]
        return render_template("select.html", movies=movies)


    return render_template("add.html", form=form)

@app.route("/select", methods=["GET","POST"])
def select():
    if request.method == "POST":
        title = request.form.get("title")
        year = request.form.get("year")
        description = request.form.get("description")
        img_url = request.form.get("img_url")

        new_movie = Movie(
            title=title,
            year=year,
            description=description,
            img_url=img_url,
            rating=0.0,
            ranking=0,
            review=""
        )

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("update", id=new_movie.id))
    return redirect(url_for("add"))

if __name__ == '__main__':
    app.run(debug=True)


