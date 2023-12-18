import turtle
import pandas
from guess import Guess

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()

guess = Guess()
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while len(guess.correct_guesses) < 50:
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guess.correct_guess(answer_state)
        answer_state = screen.textinput(f"{guess.count} / 50 States Correct", "What's another state's name?").title()
        if answer_state == "Exit":
            break
    else:
        answer_state = screen.textinput(f"{guess.count} / 50 States Correct", "What's another state's name?").title()
        if answer_state == "Exit":
            break

missing_states = set(all_states) ^ set(guess.correct_guesses)
print(f"Those you didn't find ({len(missing_states)}): {missing_states}")
missing_states = list(missing_states)
data = {
    "missing_states": []
}
for s in missing_states:
    data["missing_states"].append(s)
new_data = pandas.DataFrame(data)
new_data.to_csv("missing_states.csv")
