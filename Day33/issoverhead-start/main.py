import requests
from datetime import datetime
import smtplib

MY_LAT = 41.008240
MY_LONG = 28.978359

my_email = "pythontestomer@gmail.com"
password = "rqvnudtdaqdafgok"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_in_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT+5 > iss_latitude > MY_LAT-5 or MY_LONG+5 > iss_longitude > MY_LONG-5:
        is_in = True
    else:
        is_in = False
    return is_in


def is_in_time_range():
    time_now = datetime.now()
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 3

    if sunset > time_now.hour > sunrise:
        is_time = True
    else:
        is_time = False
    return is_time


if is_in_range() and is_in_time_range():
    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"omerfarukyy@hotmail.com",
                            msg=f"Subject:Look Up!\n\nISS is currently passing over you look up!")

