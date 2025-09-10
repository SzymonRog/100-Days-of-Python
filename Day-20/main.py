import random
import time
import turtle
from snake import Snake
from food import Food
import info

# Konfiguracja ekranu
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()

screen.listen()


screen.listen()
screen.onkey(snake.turn_up, "w")
screen.onkey(snake.turn_down, "s")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

# Pętla gry
def generate_food():
    x = random.randrange(-280, 280,20)
    y = random.randrange(-280, 280,20)


hit_wall = False
hit_body = False

food_gen = Food()

score = info.Score()
game_over = info.GameOver()

while not hit_wall and not hit_body:

    screen.update()
    time.sleep(0.07)

    snake.move()
    hit_wall = snake.hit_wall()
    hit_body = snake.hit_body()
    has_collected = snake.has_collected(food_gen)
    if has_collected:
        score.add_score()
        score.write_score()
        food_gen.refresh()



game_over.write_game_over(score.score)


screen.exitonclick()
