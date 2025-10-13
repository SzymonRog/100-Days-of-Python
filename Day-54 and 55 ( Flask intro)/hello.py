from random import randint

from flask import Flask

app = Flask(__name__)

gen_number = randint(1, 10)

@app.route("/")
def home():
    return "<h1>Welcome in number guessing game!</h1>"\
            "<p>Try to guess the number between 1 and 10</p>"\
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif />"

@app.route("/<int:number>")
def guess(number):
    if number == gen_number:
        return "<h1>You guessed it right!</h1>"\
                f"<p>The number was: {number}</p>"\

    elif number > gen_number:
        return "<h1>Too high!</h1>"\

    else:
        return "<h1>Too low!</h1>"

if __name__ == "__main__":
    app.run(debug=True)