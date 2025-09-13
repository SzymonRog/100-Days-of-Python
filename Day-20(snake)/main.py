import random
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
food_gen = Food()
score = info.Score()
game_over = info.GameOver()

# sterowanie
screen.listen()
screen.onkey(snake.turn_up, "w")
screen.onkey(snake.turn_down, "s")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

# parametry gry
delay = 150   # ms – co ile wywoływać update_game
speedup = 5   # ile ms skracać delay po zjedzeniu

def update_game():
    global delay

    snake.move()

    # kolizja ze ścianą
    if snake.hit_wall() or snake.hit_body():
        snake.reset()
        score.reset()
        # game_over.write_game_over(score.score)


    # jedzenie
    if snake.has_collected(food_gen):
        delay = max(50, delay - speedup)  # nie schodzimy poniżej ~20 FPS
        score.add_score()
        score.write_score()
        food_gen.refresh()


    screen.update()
    screen.ontimer(update_game, delay)


# start gry
update_game()
screen.mainloop()
