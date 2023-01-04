import smtplib

# my_email = "eughrat@gmail.com"
# password = "lliqwsxbzqrwznog"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="eughrat@yahoo.com",
#         msg="Subject:Hello\n\nThis is body")

# my_email = "eughrat@yahoo.com"
# password = "SERek10."
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="eughrat@gmail.com",
#         msg="Subject:Hello\n\nThis is body")

import datetime as dt

now = dt.datetime.now()

print(now)
print(now.year)
print(now.weekday())

date_of_birth = dt.datetime(year=1993, month=12, day=1, hour=0)
print(date_of_birth)
