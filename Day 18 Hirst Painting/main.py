# import colorgram
# colors = colorgram.extract("image.jpg",30)
# c = []
# for _ in range(30):
#     color = colors[_]
#     (r,g,b) = color.rgb
#     t_rgb = (r,g,b)
#     c.append(t_rgb)
# print(c)

colors = [(207, 160, 81), (56, 88, 130), (144, 91, 41), (139, 27, 48), (221, 207, 108), (134, 177, 201), (157, 47, 85), (43, 54, 105), (170, 159, 41), (130, 189, 144), (83, 20, 43), (39, 43, 64), (185, 95, 108), (189, 140, 166), (86, 122, 180), (59, 40, 31), (89, 157, 93), (80, 153, 165), (194, 80, 73), (45, 75, 77), (160, 201, 219), (54, 129, 127), (80, 75, 44), (218, 176, 186), (46, 74, 73), (170, 206, 167)]
from turtle import Turtle,Screen,colormode
import random
tim = Turtle()
colormode(255)
def paint_forward():
    count = 0
    total = 10
    space = 40
    r, g, b = random.choice(colors)
    tim.color(r, g, b)
    tim.dot(10)
    tim.penup()
    tim.forward(space)
    count += 1
def move_up():
    space = 40
    x, y = tim.pos()
    new_y = y + space
    tim.sety(new_y)
    tim.left(180)
    tim.forward(40)
# def paint_backward():
#     count = 0
#     total = 10
#     space = 40
#     r, g, b = random.choice(colors)
#     tim.color(r, g, b)
#     tim.dot(10)
#     tim.penup()
#     tim.backward(space)
#     count += 1
    # x, y = tim.pos()
    # new_y = y + space
    # tim.sety(new_y)
def hirst_painting():
    tim.penup()
    tim.setpos(-200,-200)
    tim.pendown()
    cycle_count = 0
    cycle_total = 5
    while cycle_total > cycle_count:
        count = 0
        total = 10
        while total > count:
                paint_forward()
                count+=1
        total = 10
        count = 0
        if total > count:
            move_up()
        while total > count:
            paint_forward()
            count+=1
        total = 10
        count = 0
        if total > count:
            move_up()
        cycle_count+=1

hirst_painting()




screen = Screen()
screen.exitonclick()