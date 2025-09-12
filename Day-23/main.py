import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

keys = {
    "w": False,
    "s": False,
}
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

for i in range(100):
    car_manager.move_cars()

def key_down(key):
    keys[key] = True

def key_up(key):
    keys[key] = False

screen.listen()
screen.onkeypress(lambda: key_down("w"), "w")
screen.onkeyrelease(lambda: key_up("w"), "w")
screen.onkeypress(lambda: key_down("s"), "s")
screen.onkeyrelease(lambda: key_up("s"), "s")

# główna funkcja update
game_is_on = True
def game_update():
    global game_is_on
    if not game_is_on:
        return


    if keys["w"]:
        player.move_up()
    if keys["s"]:
        player.move_down()


    car_manager.move_cars()


    if car_manager.detect_collision(player):
        scoreboard.write_game_over()
        game_is_on = False
        print("Game Over")
        return


    if player.check_finish_line():
        scoreboard.increase_level()
        car_manager.increase_speed()


    screen.update()

    screen.ontimer(game_update, 20)


game_update()
screen.mainloop()
