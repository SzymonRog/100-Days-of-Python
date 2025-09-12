import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.start_cars()


    def generate_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.goto(x=random.randint(310,1200), y=random.randrange(-230, 230,40))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() < -300:
                car.goto(x=random.randint(310, 1200), y=random.choice(range(-230, 230, 40)))

    def start_cars(self):
        for i in range(15):
            self.generate_car()

    def detect_collision(self,player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        for i in range(MOVE_INCREMENT):
            self.generate_car()
