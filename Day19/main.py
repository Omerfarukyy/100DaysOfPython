# Fully randomized turtle race with a bet
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="which turtle will win the race? Enter a color: ")
turtle_list = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
i = 0
for t in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t])
    turtle_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-225, y=-60+i)
    i += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for trt in turtle_list:
        if trt.xcor() >= 220:
            is_race_on = False
            if trt.pencolor() == user_bet:
                print(f"Your bet {user_bet} is won,")
            else:
                print(f"Your bet is lost,{trt.pencolor()} won")
            break
        trt.forward(random.randint(0, 10))


# Basic sketch thing with turtle
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.back(10)
#
#
# def rotate_right():
#     tim.right(10)
#
#
# def rotate_left():
#     tim.left(10)
#
#
# def clean():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="c", fun=clean)
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=rotate_right)
# screen.onkey(key="d", fun=rotate_left)

screen.exitonclick()
