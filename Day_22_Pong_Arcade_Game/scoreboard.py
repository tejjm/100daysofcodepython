from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1score = 0
        self.p2score = 0
        self.update_score()
    def update_score(self):
        self.goto(x=100,y=210)
        self.write(self.p1score,False,"center",("Courier",70,"normal"))
        self.goto(x=-100,y=210)
        self.write(self.p2score, False, "center", ("Courier", 70, "normal"))
    def p1_point(self):
        self.p1score+=1
        self.clear()
        self.update_score()
    def p2_point(self):
        self.p2score+=1
        self.clear()
        self.update_score()