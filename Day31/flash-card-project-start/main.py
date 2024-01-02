from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas.create_text(400, 300, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()
