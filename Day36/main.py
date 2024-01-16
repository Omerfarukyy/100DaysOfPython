import os
import requests
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.environ.get("twilio_account_id")
auth_token = os.environ.get("twilio_auth_token")
phone_num = os.environ.get("phone_num")

parameters = {
    "apikey": os.environ.get("api_key_for_alphavantage"),
    "function": "TIME_SERIES_DAILY",
    # tsla price of uk
    "symbol": "TSLA.LON",

}
parameters_for_news = {
    "apiKey": os.environ.get("api_key_for_newsapi"),
    "q": "tesla",
    "from": "2023-12-16",
    "sortBy": "publishedAt"
}


def convert_list_to_string(given_list):
    convert = ""
    for variables in given_list:
        convert += variables
    return float(convert)


response = requests.get(url=STOCK_ENDPOINT, params=parameters)
data = response.json()
print(data)
yesterday_closing_stock_price = [value for value in data["Time Series (Daily)"]["2024-01-15"]["4. close"]]
yesterday_closing_stock_price = convert_list_to_string(yesterday_closing_stock_price)

day_before_yesterday_closing_stock_price = [value for value in data["Time Series (Daily)"]["2024-01-12"]["4. close"]]
day_before_yesterday_closing_stock_price = convert_list_to_string(day_before_yesterday_closing_stock_price)

difference = abs(yesterday_closing_stock_price - day_before_yesterday_closing_stock_price)

percentage_difference = (difference / day_before_yesterday_closing_stock_price) * 100.0
print(difference)
print(percentage_difference)
data2 = {}
if percentage_difference > 5:
    r = requests.get(url=NEWS_ENDPOINT, params=parameters_for_news)
    data2 = r.json()
    first3_articles = data2["articles"][:3]

    client = Client(account_sid, auth_token)
    for article in first3_articles:
        message = client.messages.create(
            from_='+13365858295',
            body=f"{parameters['symbol']}"
                 f"Headline: {article['title']}"
                 f"Brief: {article['content']}",
            to=phone_num
        )
