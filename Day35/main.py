import os
import requests
from twilio.rest import Client


account_sid = 'AC34250a225d403d0ccba6e056114a4601'
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

phone_num = os.environ["PERSONAL_PHONE_NUMBER"]

message = client.messages.create(
  from_='+15186621005',
  body='Bring an umbrella, its a rainy day',
  to=phone_num
)


api_key = os.environ["OPENWEATHER_API_KEY"]
MY_LAT = 41.008240
MY_LONG = 28.978359
COUNT = 5
UNIT = "metric"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "units": UNIT,
    "cnt": COUNT,
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
weather = [w["weather"][0] for w in data["list"]]
weather_ids = [weather[w]["id"] for w in range(len(weather))]
weather_desc = [weather[w]["description"] for w in range(len(weather))]
for id in weather_ids:
    if id < 600:
        client = Client(account_sid, auth_token)
        break

print(message.status)
