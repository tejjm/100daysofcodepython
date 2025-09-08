import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
#Creating screen for the game to run
screen = Screen()
screen.bgcolor("white")
screen.title("The Turtle Crossing Game!")
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(key="w",fun=player.move_up)
game_is_on = True
car_manager = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Creating cars and making them move
    car_manager.create_car()
    car_manager.move()
    #Checking collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
    #Checking if finish line reached
    if player.ycor() == 290:
        player.level_finish()
        car_manager.level_up()

screen.exitonclick()
