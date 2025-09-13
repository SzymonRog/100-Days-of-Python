import turtle


class Score:
    def __init__(self, score_1, score_2):
        self.score_1 = score_1
        self.score_2 = score_2
        self.scoreboard = turtle.Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.color("white")

    def write_score(self):
        self.scoreboard.clear()
        self.scoreboard.penup()
        self.scoreboard.goto(-100, 180)
        self.scoreboard.write(self.score_1, align="center", font=("Arial", 50, "bold"))
        self.scoreboard.goto(100, 180)
        self.scoreboard.write(self.score_2, align="center", font=("Arial", 50, "bold"))
    def update_score(self, score_1, score_2):
        self.score_1 = score_1
        self.score_2 = score_2
        self.write_score()

