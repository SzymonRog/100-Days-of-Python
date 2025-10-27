from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Regexp, Length

app = Flask(__name__)


app.config["SECRET_KEY"] = "supersekretnyklucz"

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Pole jest wymagane!"), Regexp(r".+@.+\..+",message="Podaj poprawny adres email z @ i .!")])
    password = PasswordField("Password", validators=[DataRequired(message="Pole jest wymagane!"), Length(min=8, message="Hasło musi mieć co najmniej 8 znaków.")])
    submit = SubmitField("Login")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        return f"<h2>Zalogowano jako: {email} z hasłem {password}</h2>"

    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)