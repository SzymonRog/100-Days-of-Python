from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 7
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def check_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y < -280:
            new_y = -280
        self.goto(self.xcor(), new_y)



