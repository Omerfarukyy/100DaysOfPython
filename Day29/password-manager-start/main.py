import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# automatically call this email for password manager
EMAIL_CONSTANT = "xx@hotmail.com"
global exist
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

    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    global exist
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        pass
    exist = website in data
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please fill the empty fields")
    elif exist:
        messagebox.showwarning(message="This site is already in password manager")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword:{password} \n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# ------------------------- SEARCH WEBSITE -----------------------------#


def search():
    try:
        website_name = website_input.get()
        with open("data.json") as file:
            data = json.load(file)
        website = data[website_name]
        website_email = website["email"]
        website_password = website["password"]
    except FileNotFoundError:
        messagebox.showwarning(message="Password Manager is empty")
    except KeyError:
        messagebox.showwarning(message=f"There is no site name like {website_name} in password manager ")
    else:
        messagebox.showinfo(title=f"{website_name}", message=f"Email: {website_email}\n Password:{website_password}")
        pyperclip.copy(f"{website_password}")

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

website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

website_button = Button(text="Search", width=14, command=search)
website_button.grid(column=2, row=1)

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
