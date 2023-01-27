import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


url = "https://www.amazon.com/dp/B091S7XQK9/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0?th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price_whole = soup.find("span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay",)

for i in price_whole:
    price = i.get_text()

price = float(price.strip("$"))
print(price)

my_email = "eughrat@gmail.com"
password = "lliqwsxbzqrwznog"

if price < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="michal.piernicki@gmail.com",
            msg=f"Subject:Price tracker \n\nThe product you're hunting for is on offer for sale below $200! Currently its price is {price}\n\n link: {url}")


