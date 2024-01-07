import smtplib
import random
import datetime as dt

my_email = "DogumGunuKutlayanOmer@hotmail.com"
password = "qoeihnosqqizcpka"

with open("quotes.txt") as quotes:
    data = quotes.read().splitlines()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="omerfarukyy@hotmail.com",
                            msg=f"Subject:Motivational Monday!\n\n{random.choice(data)}")
