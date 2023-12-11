from turtle import Turtle
alignment = "center"
font = ("Courier", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = -1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=250)
        self.increase_score()

    def update_scoreboard(self):
        self.write(f"Score: {self.point}", move=False, align=alignment, font=font)

    def increase_score(self):
        self.clear()
        self.point += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=alignment, font=font)
