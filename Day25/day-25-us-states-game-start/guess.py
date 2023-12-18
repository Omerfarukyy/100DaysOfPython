import turtle
import pandas
states = pandas.read_csv("50_states.csv")


class Guess(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.correct_guesses = []
        self.hideturtle()
        self.count = 0

    def correct_guess(self, state_name):
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        state_data = states[states.state == state_name]
        new_turtle.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        new_turtle.write(state_name)
        self.correct_guesses.append(state_name)
        self.count += 1
