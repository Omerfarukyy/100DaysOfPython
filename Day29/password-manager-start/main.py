from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# automatically call this email for password manager
EMAIL_CONSTANT = "xx@hotmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]

    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please fill the empty fields")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword:{password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} / {email} / {password} \n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=400)
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)

website_input = Entry(width=50)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()


email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(column=0, row=2)

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(index=0, string=EMAIL_CONSTANT)

password_label = Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(column=0, row=3)

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=password_generate)
generate_password_button.grid(column=2, row=3)


add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
