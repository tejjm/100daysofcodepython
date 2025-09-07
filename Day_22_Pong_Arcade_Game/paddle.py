from turtle import Turtle,Screen
DISTANCE = 20
WIDTH = 1
LENGTH = 5
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.penup()
        self.setheading(90)
        # self.goto(position)
    def w(self):
        self.forward(DISTANCE)
    def s(self):
        self.backward(DISTANCE)


