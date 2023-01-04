##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }


# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import random
import pandas as pd
import datetime
import smtplib

from os import listdir
from os.path import isfile, join



#DATA PREPARATION
data = pd.read_csv("birthdays.csv")
data_dict = {(list(i[-1])[-2], list(i[-1])[-1]): list(i[-1]) for i in data.iterrows()}
print(data_dict)

#SET TODAY DATE
today_day = datetime.datetime.today().day
today_month = datetime.datetime.today().month
today = (today_month, today_day)

#RANDOM LETTER
path = "./letter_templates"
files = [file for file in listdir(path) if isfile(join(path, file))]
random_letter_path = path + "/" + random.choice(files)

with open(random_letter_path, "r") as file:
    letter = file.read()

#SENDING MAIL
my_email = "eughrat@gmail.com"
password = "lliqwsxbzqrwznog"

for k in data_dict.keys():
    if k == today:
        letter = letter.replace("[NAME]",data_dict[k][0])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="eughrat@yahoo.com",
                msg=f"Subject:Birthday Wishes\n\nT{letter}")


