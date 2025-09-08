from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()
screen.colormode(255)

import colorgram
colors = colorgram.extract('image.jpg', 30)

turtle.speed("fastest")
turtle.pensize(2)
index_of_color = 0
def next_color():
    global index_of_color
    tuple_color = (colors[index_of_color]).rgb
    if index_of_color == len(colors) - 1:
        index_of_color = 0

    index_of_color += 1
    return tuple_color



turtle.penup()


x_start = (screen.window_width() / 2)  * -1
y_start = (screen.window_height()  / 2) * -1



y = y_start
for _ in range(10):
    turtle.penup()
    turtle.setposition(x_start + 40, y + 40)
    for _ in range(10):
        turtle.dot(30, next_color())
        turtle.forward(100)

    y += 100

screen.exitonclick()

