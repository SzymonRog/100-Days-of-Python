from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.write_level_turtle = Turtle()
        self.init_scoreboard()

    def init_scoreboard(self):
        self.write_level_turtle.hideturtle()
        self.write_level_turtle.penup()
        self.write_level_turtle.goto(-280, 260)
        self.write_score()

    def write_score(self):
        self.write_level_turtle.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_level_turtle.clear()
        self.write_score()

    def write_game_over(self):
        self.write_level_turtle.goto(0, 0)
        self.write_level_turtle.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
