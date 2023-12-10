
import random
import turtle

import colorgram
from turtle import Turtle, Screen

colors = colorgram.extract('painting.jpeg', 30)
turt = Turtle()
turt.speed(10)
turtle.colormode(255)
rgb_colors = []
a = -250
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

for i in range(10):
    a += 50
    turt.penup()
    turt.setposition(-250, a)
    for x in range(10):
        turt.dot(20, random.choice(rgb_colors))
        turt.penup()
        turt.forward(50)
        turt.pendown()
turt.hideturtle()

screen = Screen()
screen.exitonclick()
