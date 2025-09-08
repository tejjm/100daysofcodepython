COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random as re

class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        if re.randint(1,6) == 6:

            new_car = Turtle()
            new_car.shape("square")
            new_car.color(re.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.goto(x=280,y=re.randint(-250,250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT




