from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(x=0,y=270)
        self.display_score()
    def display_score(self):
        self.write(f"Score : {self.score}", False, "center", ("normal", 18))
    def update_score(self):
        self.score+=1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", ("normal", 18))




