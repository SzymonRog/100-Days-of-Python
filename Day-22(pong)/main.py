import turtle
from time import sleep

import padle
import ball
import score as score_module  # unikamy konfliktu nazw

screen = turtle.Screen()
screen.title("pong game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Linia środkowa
line = turtle.Turtle()
line.color("white")
line.pensize(4)
line.penup()
line.goto(0, 300)
line.setheading(270)
for _ in range(20):
    line.pendown()
    line.forward(30)
    line.penup()
    line.forward(30)

# Obiekty gry
padle_1 = padle.Padle(1)
padle_2 = padle.Padle(2)
ball = ball.Ball()
score_display = score_module.Score(padle_1.score, padle_2.score)

# Flagi klawiszy
keys = {"w": False, "s": False, "Up": False, "Down": False}

def press(key):
    keys[key] = True

def release(key):
    keys[key] = False

def game_loop():
    # Ruch paletek
    if keys["w"]: padle_1.move_up()
    if keys["s"]: padle_1.move_down()
    if keys["Up"]: padle_2.move_up()
    if keys["Down"]: padle_2.move_down()

    # Ruch piłki
    ball.move()
    ball.hit_padle(padle_1)
    ball.hit_padle(padle_2)

    # Sprawdzenie ścian i punktów
    result = ball.check_wall()
    if result == 1:
        padle_2.add_score()
        score_display.update_score(padle_1.score, padle_2.score)
        ball.reset()
        padle_2.reset_pos()
        padle_1.reset_pos()
        sleep(0.2)

        # możesz dodać delay używając ontimer
    elif result == 2:
        padle_1.add_score()
        score_display.update_score(padle_1.score, padle_2.score)
        ball.reset()
        padle_2.reset_pos()
        padle_1.reset_pos()
        sleep(0.2)



    screen.update()
    screen.ontimer(game_loop, 15)

# Bindy klawiszy
screen.listen()
for k in keys:
    screen.onkeypress(lambda k=k: press(k), k)
    screen.onkeyrelease(lambda k=k: release(k), k)

game_loop()
score_display.update_score(padle_1.score, padle_2.score)
screen.mainloop()
