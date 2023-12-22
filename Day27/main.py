from tkinter import *

window = Tk()
window.title("gui")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="New text")
my_label.config(padx=5, pady=5)


def button_clicked():
    print("ı got clicked")
    my_label.config(text=f"{inpt.get()}")


button = Button(text="Click it bro", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=3, row=0)
inpt = Entry(width=10)
inpt.grid(column=4, row=3)
inpt.get()

window.mainloop()
