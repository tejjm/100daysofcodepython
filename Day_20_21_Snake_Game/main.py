from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
scoreboard = Scoreboard()

#Creating a snake body
s = Snake()
food = Food()
s.create_snake()
screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.left,"Left")
screen.onkey(s.right,"Right")
screen.tracer(0)
written = scoreboard.write
is_game_on = True
#Snake movement and score updating
while is_game_on:
    screen.update()
    s.move()
    time.sleep(0.1)
    scoreboard.display_score()
    if s.snake_body[0].distance(food) < 15:
        print("nom nom nom")
        scoreboard.update_score()
        s.extend_segment()
        food.refresh()

    if s.snake_body[0].xcor() > 298 or s.snake_body[0].xcor() < -298 or s.snake_body[0].ycor() > 298 or s.snake_body[0].ycor() < -298:
        is_game_on = False
        scoreboard.game_over()


    for body in s.snake_body[1:]:
        if s.snake_body[0].distance(body) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()