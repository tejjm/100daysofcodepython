from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
ball = Ball()
screen = Screen()
screen.setup(width=800,height=600)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()
p1 = Paddle()
p1.goto(x=-380,y=0)
p2 = Paddle()
p2.goto(x=375,y=0)

screen.listen()
screen.onkeypress(key='w', fun=p1.w)
screen.onkeypress(key='s', fun=p1.s)
screen.onkeypress(key='Up', fun=p2.w)
screen.onkeypress(key='Down', fun=p2.s)
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detecting collision with top and bottom walls
    if ball.ycor() > 260 or ball.ycor() < -270:
        ball.bounce_y()
    #Detecting collision with paddles
    if ball.distance(p2) < 50 and ball.xcor() > 350 or ball.distance(p1) < 50 and ball.xcor() < -350 :
        ball.bounce_x()
    #Detecting collision with side walls and resetting the ball
    elif ball.xcor()>370:
        screen.tracer()
        ball.goto(0,0)
        screen.update()
        scoreboard.p2_point()
        ball.reset_ball()
    elif ball.xcor()<-370:
        screen.tracer()
        ball.goto(0,0)
        screen.update()
        scoreboard.p1_point()
        ball.reset_ball()
screen.exitonclick()
