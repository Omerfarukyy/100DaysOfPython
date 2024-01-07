import random
import smtplib
import datetime as dt
import pandas

my_email = "DogumGunuKutlayanOmer@hotmail.com"
password = "qoeihnosqqizcpka"

data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")

with open("./letter_templates/letter_1.txt") as file:
    letter1 = file.read()
with open("./letter_templates/letter_2.txt") as file:
    letter2 = file.read()
with open("./letter_templates/letter_3.txt") as file:
    letter3 = file.read()
letter_list = [letter1, letter2, letter3]
now = dt.datetime.now()
current_month = now.month
current_day = now.day
for birthdays in data:
    if birthdays["month"] == current_month and birthdays["day"] == current_day:
        letter = random.choice(letter_list)
        letter = letter.replace("[NAME]", birthdays["name"])
        email = birthdays["email"]
        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{email}",
                                msg=f"Subject:Happy Birthday!\n\n{letter}")
