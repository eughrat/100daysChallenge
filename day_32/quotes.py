import random
import datetime as dt
import smtplib

current_day_of_the_week = dt.datetime.now().weekday()

with open("quotes.txt", "r") as file:
    lines = file.readlines()
    random_quote = random.choice(lines)
    print(random_quote)

my_email = "eughrat@gmail.com"
password = "lliqwsxbzqrwznog"


if current_day_of_the_week == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="eughrat@yahoo.com",
            msg=f"Subject:Motivation Quote\n\nT{random_quote}")
