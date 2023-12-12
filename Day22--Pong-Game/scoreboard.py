from turtle import Turtle
alignment = "center"
font = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=200)

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}  {self.r_score}", move=False, align=alignment, font=font)

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=alignment, font=font)
