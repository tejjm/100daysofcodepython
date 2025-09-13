from turtle import Turtle
class Writer(Turtle):
    def __init__(self,x,y,answer):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(x=x,y=y)
        self.write(answer,move=False,align="center",font=("Arial",8,"normal"))

