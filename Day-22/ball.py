import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.dx = 10
        self.dy = 10
        self.penup()
        self.spawn()


    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def spawn(self):
        self.goto(0, 0)
        self.dx = random.choice([5, -5])
        self.dy = random.choice([5, -5])

    def bounce_y(self):
        self.dy *= -1
    def bounce_x(self):
        self.dx *= -1

    def check_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

        # odbicie od lewej/prawej krawędzi
        if self.xcor() > 380:
            return 2
        elif self.xcor() < -380:
            return 1
        return 0

    def hit_padle(self,padle):
        if (self.xcor() < -340 or self.xcor() > 340) and padle.ycor() - 50  < self.ycor() < padle.ycor() + 50:
            self.bounce_x()

    def reset(self):
        self.spawn()




