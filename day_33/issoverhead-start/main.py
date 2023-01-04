import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 54.405122
MY_LONG = 18.581872

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

my_email = "eughrat@gmail.com"
password = "lliqwsxbzqrwznog"

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(1000)
    if (MY_LONG < iss_longitude + 5 and MY_LONG > iss_longitude - 5) and (MY_LAT < iss_latitude + 5 and MY_LAT > iss_latitude - 5) and (time_now > sunset or time_now < sunrise):

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="eughrat@yahoo.com",
                msg="Subject:ISS \n\nLook up! ISS is over you!")
