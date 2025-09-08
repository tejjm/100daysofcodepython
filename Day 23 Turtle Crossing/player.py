from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
sb = Scoreboard()
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.left(90)
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def reset(self):
        self.goto(x=0,y=-280)
    def level_finish(self):
        sb.increase_level()
        self.reset()
