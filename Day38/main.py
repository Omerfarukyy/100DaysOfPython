import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

today = datetime.now()
GENDER = "male"
WEIGHT_KG = "55"
HEIGHT_CM = "178"
AGE = "19"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
print(APP_ID)
print(APP_KEY)
sheety_endpoint = os.environ.get("sheety_endpoint")
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

headers_for_sheet = {
    "authorization": os.environ.get("authorization")

}
parameters_for_sheet = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": result["exercises"][0]["user_input"],
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
    }
}
print(headers_for_sheet["authorization"])
response_sheety = requests.post(sheety_endpoint, json=parameters_for_sheet, headers=headers_for_sheet)
response_sheety.raise_for_status()
print(response_sheety.json())
