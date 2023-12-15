from turtle import Turtle
alignment = "center"
font = ("Courier", 25, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = -1
        self.high_score = 0
        self.file_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=250)
        self.increase_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.point} High Score: {self.high_score}", move=False, align=alignment, font=font)

    def increase_score(self):
        self.clear()
        self.point += 1
        self.update_scoreboard()


    def reset(self):
        self.clear()
        if self.point > self.high_score:
            self.high_score = self.point

        self.point = 0
        self.update_scoreboard()