from turtle import Turtle
alignment = "center"
font = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=250)
        self.color("black")
        self.level = 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align=alignment, font=font)

    def increase_point(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=alignment, font=font)
