import requests
from datetime import datetime
import os


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

SHEETY_KEY = os.environ["SHEETY_KEY"]

######################################################################################################

todays_date = datetime.now().strftime("%m/%d/%Y")
current_time = datetime.now().strftime("%H:%M:%S")


######################################################################################################

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

user_params = {
    "query":"ran 1 miles, cycle for 15 min",
    "gender":"male",
    "weight_kg":78.5,
    "height_cm":190,
    "age":29
    }

response = requests.post(url=nutritionix_endpoint, json=user_params, headers=nutri_headers)
nutri_result = response.json()
print(nutri_result)


######################################################################################################

sheety_enpoint = os.environ["sheety_enpoint"]

sheety_headers = {
    "Authorization": SHEETY_KEY,
}

sheet_params = {}

for i in nutri_result["exercises"]:
    sheet_params = {
        "arkusz1": {
            "date": todays_date,
            "time": current_time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"],
        }
    }

    response = requests.post(url=sheety_enpoint, json=sheet_params, headers=sheety_headers)
    sheety_result = response
