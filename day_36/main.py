import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "VELO2WIP9B86LL16"
NEWS_KEY = "acaa5932f52f49438c934c27c8cd8046"

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

todays_date = datetime.today().date()
yesterday_date = datetime.today() - timedelta(days=1)
yesterday_date = yesterday_date.date()

stock_dates = list(data["Time Series (Daily)"].keys())

stock_first_date_close_price = float(data["Time Series (Daily)"][stock_dates[0]]['4. close'])

# TODO 2. - Get the day before yesterday's closing stock price

stock_second_date_close_price = float(data["Time Series (Daily)"][stock_dates[1]]['4. close'])

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

price_diff = abs(stock_first_date_close_price - stock_second_date_close_price)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_diff = (price_diff / stock_second_date_close_price) * 100

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_parameters = {
    "q": "ibm",
    "from": "todays_date",
    "sortBy": "publishedAt",
    "apiKey": NEWS_KEY,
    "language": 'en',
}

news_url = NEWS_ENDPOINT
news_r = requests.get(news_url, params=news_parameters)
news_data = news_r.json()

articles = news_data["articles"]

news = {}

for i in range(3):
    title = articles[i]["title"]
    description = articles[i]["description"]
    news[title] = description

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
# TODO 9. - Send each article as a separate message via Twilio.

account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)

if stock_first_date_close_price >= stock_second_date_close_price:
    for k, v in news.items():
        message = client.messages \
                        .create(
                             body=f"IBM: 🔺{round(percentage_diff)}%\nHeadline: {k}\nBrief: {v}",
                            from_="+17853775297",
                            to="+48695391444"
                         )
else:
    for k, v in news.items():
        message = client.messages \
                        .create(
                             body=f"IBM: 🔻{round(percentage_diff)}%\nHeadline: {k}\nBrief: {v}",
                            from_="+17853775297",
                            to="+48695391444"
                         )

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.




# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
