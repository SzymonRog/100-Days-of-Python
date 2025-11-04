from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'




class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)



login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        password_hash = generate_password_hash(password, salt_length=8)
        new_user = User(name=name, email=email, password=password_hash)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    if current_user.is_authenticated:
        return redirect(url_for("secrets", id=current_user.id))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("secrets", id=user.id))
            else:
                flash("Incorrect password, try again.")
                error = "Incorrect password, try again."
        else:
            flash("Email does not exist.")
            error = "Email does not exist."

    if current_user.is_authenticated:
        return redirect(url_for("secrets", id=current_user.id))

    return render_template("login.html", error=error)


@app.route('/secrets')
def secrets():
    id = request.args.get("id")
    user_name = User.query.filter_by(id=id).first().name
    return render_template("secrets.html", name=user_name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))



@app.route('/download')
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf")



if __name__ == "__main__":
    app.run(debug=True)
