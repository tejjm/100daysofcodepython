from turtle import Turtle,Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

#Creating a snake body
s = Snake()
s.create_snake()
screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.left,"Left")
screen.onkey(s.right,"Right")
screen.tracer(0)

is_game_on = True
while is_game_on:
    screen.update()
    s.move()
    time.sleep(0.3)





screen.exitonclick()