from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=2, height=100)
window.config(padx=10, pady=10)

is_equal_to = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=1, pady=1)

result = Label(text="0")
result.grid(column=1, row=1)
result.config(padx=1, pady=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=1, pady=1)

Km = Label(text="Km")
Km.grid(column=2, row=1)
Km.config(padx=1, pady=1)

def converter():
    mile = int(inpt.get())
    km = mile * 1.6
    result.config(text=f"{km}")


button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)
button.config(padx=1, pady=1)

inpt = Entry(width=10)
inpt.grid(column=1, row=0)
inpt.get()

window.mainloop()
