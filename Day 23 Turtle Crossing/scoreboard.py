FONT = ("Courier", 12, "normal")
FINISH_LINE_Y = 280

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level()
    def level(self):
        self.goto(x=-280, y=270)
        self.write(f"Level {self.score}", move=False, align="left", font=FONT)

    def increase_level(self):
            self.score+=1
            self.clear()
            self.level()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"center",("Courier",30,"normal"))