# Flash card project, if you press right button the pair of the word is deleted from the words_to_learn.csv file
# else the words don't removed from the pool
import random
from tkinter import *
import pandas
from pathlib import Path
BACKGROUND_COLOR = "#B1DDC6"
global random_index

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    data = data.to_dict(orient="records")
    french_words_list = [pair["French"] for pair in data]
    english_words_list = [pair["English"] for pair in data]

except FileNotFoundError:

    with open("./data/words_to_learn.csv", "w") as file:
        pass
    data = pandas.read_csv("./data/french_words.csv")
    data = data.to_dict(orient="records")
    french_words_list = [pair["French"] for pair in data]
    english_words_list = [pair["English"] for pair in data]

# FUNCTIONS


def remove():
    global random_index
    french_words_list.remove(french_words_list[random_index])
    english_words_list.remove(english_words_list[random_index])


def random_word_right():
    global words
    global random_index
    remove()
    canvas.itemconfig(background, image=card_front)
    canvas.itemconfig(word_lang, text="French", fill="Black")
    random_index = random.randint(0, len(data)-1)

    canvas.itemconfig(words, text=f"{french_words_list[random_index]}", fill="Black")

    window.after(3000, flipping_the_card)


def random_word_wrong():
    global words
    global random_index

    canvas.itemconfig(background, image=card_front)
    canvas.itemconfig(word_lang, text="French", fill="Black")
    random_index = random.randint(0, len(data)-1)

    canvas.itemconfig(words, text=f"{french_words_list[random_index]}", fill="Black")
    window.after(3000, flipping_the_card)


def flipping_the_card():
    global random_index
    canvas.itemconfig(background, image=card_back)
    canvas.itemconfig(words, text=f"{english_words_list[random_index]}", fill="White")
    canvas.itemconfig(word_lang, text="English", fill="White")


# GUI

window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
background = canvas.create_image(400, 263, image=card_front)
word_lang = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
words = canvas.create_text(400, 300, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_button = Button(image=right, highlightthickness=0, command=random_word_right)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=random_word_wrong)
wrong_button.grid(column=0, row=1)

random_word_wrong()
window.mainloop()

words_to_learn = pandas.DataFrame({'French': french_words_list, 'English': english_words_list})
filepath = Path("./data/words_to_learn.csv")
words_to_learn.to_csv(filepath, index=False)
