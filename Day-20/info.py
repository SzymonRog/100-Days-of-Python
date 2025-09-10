import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280, 260)
        self.write_score()

    def add_score(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 16, "normal"))



class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(0, 0)

    def write_game_over(self, score):
        self.clear()
        self.write(f"GAME OVER\nYour score: {score}", align="center", font=("Arial", 36, "bold"))
