from turtle import Turtle,Screen
import random
#Etch Sketch Code:
# def etch_sketch():
#     tim = Turtle()
#     screen = Screen()
#
#     def w():
#         tim.forward(10)
#     def s():
#         tim.backward(10)
#     def a():
#         tim.left(15)
#     def d():
#         tim.right(15)
#     def clear():
#         tim.penup()
#         tim.clear()
#         tim.setpos(0,0)
#         tim.pendown()
#     screen.listen()
#     screen.onkeypress(key='w',fun=w)
#     screen.onkeypress(key='a',fun=a)
#     screen.onkeypress(key='s',fun=s)
#     screen.onkeypress(key='d',fun=d)
#     screen.onkeypress(key='c',fun=clear)
#     screen.exitonclick()


screen = Screen()
screen.setup(width=500,height=400)
colors = ["red","orange","yellow","green","blue","purple"]
starting_point = [-100,-70,-40,-10,20,50]
all_turtles = []
is_race_on =  False
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-starting_point[i])
    all_turtles.append(new_turtle)
    #Now the turtles are at the postion
    # things to do next 1) know when turtle hits the right side and stop the race 2) notedown the color of the turtle which wins and output as the result
user_bet = screen.textinput(title="Make your input",prompt="Which turtle will win the race? Enter a color: ")
is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have won the bet!, The winner is {winner}!")
            else:
                print(f"You have lost the bet!, The winner is {winner}!")


screen.exitonclick()