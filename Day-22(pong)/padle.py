from turtle import Turtle

class Padle(Turtle):
    def __init__(self, player: int):
        super().__init__(shape="square")
        self.color("white")
        self.score = 0
        self.penup()
        self.player = player
        self.shapesize(stretch_wid=5, stretch_len=0.5)  # prostokąt
        # Ustaw pozycję zależnie od gracza
        x = -350 if player == 1 else 350
        self.goto(x, 0)

    def move_up(self):
        if self.ycor() < 250:  # ograniczenie, żeby nie wychodziło poza ekran
            self.sety(self.ycor() + 7)

    def move_down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 7)
    def add_score(self):
        self.score += 1

    def reset_pos(self):
        x = -350 if self.player == 1 else 350
        self.goto(x, 0)
