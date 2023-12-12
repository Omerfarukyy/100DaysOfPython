from turtle import Turtle

stretch_wid = 5
stretch_len = 1
outline = 5


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len, outline=outline)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor()+30)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor()-30)
