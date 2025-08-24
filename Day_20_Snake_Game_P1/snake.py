from turtle import Turtle
DISTANCE = 20
COORDS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
class Snake():
    def __init__(self):
        self.snake_body =[]
    def create_snake(self):

        for i in range(0, len(COORDS)):
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.goto(COORDS[i])
            self.snake_body.append(t)
    def move(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)
        self.snake_body[0].forward(DISTANCE)
    def up(self):
        s = self.snake_body[0]
        facing = s.heading()
        if facing == 0:
            s.left(90)
        elif facing == 90:
            pass
        elif facing == 180:
            s.right(90)
        elif facing == 270:
            pass
    def down(self):
        s = self.snake_body[0]
        facing = s.heading()
        if facing == 0:
            s.right(90)
        elif facing == 90:
            pass
        elif facing == 180:
            s.left(90)
        elif facing == 270:
            pass
    def left(self):
        s = self.snake_body[0]
        facing = s.heading()
        if facing == 0:
            s.left(90)
        elif facing == 90:
            s.left(90)
        elif facing == 180:
            s.left(90)
        elif facing == 270:
            s.right(90)
    def right(self):
        s = self.snake_body[0]
        facing = s.heading()
        if facing == 0:
            s.right(90)
        elif facing == 90:
            s.right(90)
        elif facing == 180:
            s.right(90)
        elif facing == 270:
            s.left(90)