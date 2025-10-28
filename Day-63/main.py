from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'

db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    author: Mapped[str] = mapped_column(String(100))
    rating: Mapped[float] = mapped_column(Float, nullable=False)


@app.route('/')
def home():

    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add" , methods=["GET","POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = float(request.form.get("rating"))
        new_book = Book(title=title, author=author, rating=rating)

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    book = db.session.query(Book).filter_by(id=id).first()
    if request.method == "POST":
        book.rating = float(request.form.get("rating"))
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)

@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete(id):
    book = db.session.query(Book).filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

