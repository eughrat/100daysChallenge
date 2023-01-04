import requests
from datetime import datetime

MY_LAT = 54.405122
MY_LNG = 18.581872

#
# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response.status_code)
#
# data = response.json()
# print(data)

parametrs = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parametrs, )
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.now()
