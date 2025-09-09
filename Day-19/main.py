import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make the bet", prompt="Which turtle will win the race?").lower()

if user_bet:
    is_race_on = True


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start = -100

turtles = []

for i in range(6):
    turtle_race = Turtle(shape="turtle")
    turtle_race.color(colors[i])
    turtle_race.penup()
    turtle_race.goto(x=-220, y=y_start + (30 * i) + 30)
    turtles.append(turtle_race)

def random_step(turtle_object):
    turtle_object.forward(random.randint(0, 10))


while is_race_on:
    for turtle in turtles:
        random_step(turtle)
        if turtle.xcor() >= 220:
            is_race_on = False
            if(user_bet == turtle.pencolor()):
                print(f"You Win!{turtle.pencolor()} won the race!")
            else:
                print(f"You Lose!{turtle.pencolor()} won the race!")






screen.exitonclick()
