# Basic turtle usage
import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
# tim.hideturtle()
turtle.colormode(255)
tim.pensize(3)
tim.speed(500)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    tim.color(r, g, b)

#
# for i in range(8):
#     angle = int(360 / (3 + i))
#     for k in range(3+i):
#         tim.forward(100)
#         tim.right(angle)
#     tim.home()
#     change_color()
colour = ["CornFlowerBlue", "DarkOrchid", "Indian Red", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.back(250)
for i in range(360):
    for x in range(3):
        tim.forward(400)
        tim.right(120)
        tim.right(1)
    # tim.setheading(i)
    tim.color(random.choice(colour))
c = ["red", "IndianRed", "FireBrick"]
directions = [0, 90, 180, 270]
#
# for i in range(150):
#     tim.color(random.choice(colour))
#     tim.forward(50)
#     tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
