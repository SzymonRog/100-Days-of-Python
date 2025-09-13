import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280, 260)
        self.get_high_score()
        self.write_score()


    def add_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def get_high_score(self):
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())



    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))




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
