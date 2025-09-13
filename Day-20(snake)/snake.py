import turtle

STEP = 20
class Snake:
    def __init__(self):
        self.snake = []
        self.length = 3
        self.create_snake()

    def create_snake(self):
        head = turtle.Turtle(shape="square")
        head.color("white")
        head.penup()
        self.snake.append(head)

        for i in range(1, self.length):
            segment = turtle.Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setx(segment.xcor() - STEP * i)
            self.snake.append(segment)

    def add_segment(self):
        segment = turtle.Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setposition(self.snake[-1].position())
        self.snake.append(segment)

    def move(self):
        positions = [segment.pos() for segment in self.snake]
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setposition(positions[i - 1])
        self.snake[0].forward(STEP)

    def turn_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def turn_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def turn_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def turn_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def has_collected(self, food):
        if self.snake[0].distance(food) < 15:  # < STEP/2 to dobry próg
            self.length += 1
            self.add_segment()
            return True
        return False

    def hit_wall(self):
        x,y = self.snake[0].pos()
        if abs(x) > 290 or abs(y) > 290:
            return True
        return False

    def hit_body(self):
        head = self.snake[0]
        segments = self.snake[1:]
        for segment in segments:
            if head.distance(segment) < 10:
                return True
        return False

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
            segment.hideturtle()
        self.snake.clear()
        self.length = 3
        self.create_snake()


