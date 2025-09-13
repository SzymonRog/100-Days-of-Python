import random
from turtle import Turtle

STEP = 20

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.shapesize(0.7)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def generate_food(self):
        return random.randrange(-280, 280,STEP)

    def refresh(self):
        self.goto(self.generate_food(), self.generate_food())