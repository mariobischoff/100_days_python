import os
import requests
from datetime import timedelta, datetime
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
APLHA_API_KEY = os.environ.get("APLHA_API_KEY")

def get_prices(dates: list[str]):
    """Recive a list of dates (2020-09-21) and return a dict with prices"""
    alpha_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": APLHA_API_KEY,
    }
    alpha_url = "https://www.alphavantage.co/query"
    response = requests.get(alpha_url, alpha_params)
    prices = response.json()
    prices = prices["Time Series (Daily)"]

    prices_dict = {}
    for date in dates:
        prices_dict[date] = float(prices[date]["4. close"])

    return prices_dict

def get_news(date: str):
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "function": "NEWS_SENTIMENT",
        "from": date
    }
    news_api = "https://newsapi.org/v2/everything"
    r = requests.get(news_api, news_params)
    news = r.json()
    news = news["articles"][:3]
    news_dict = {new["title"]: new["description"] for new in news}
    return news_dict

def percent_change(x, y):
    return (x * 100 / y) - 100

# Datetime calculations
a_day_ago = timedelta(days=1)
yesterday = datetime.today() - a_day_ago
a_day_before_yesterday = yesterday - a_day_ago

# Date as String
a_day_before_yesterday = str(a_day_before_yesterday.date())
yesterday = str(yesterday.date())

# Get prices
prices = get_prices([a_day_before_yesterday, yesterday])

percent_change = percent_change(prices[a_day_before_yesterday], prices[yesterday])

if percent_change > 2 or percent_change < -2:
    up_down = ""
    if percent_change > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    print(f"{STOCK}: {up_down} {percent_change:.2f}")
    news = get_news(a_day_before_yesterday)
    for title, description in news.items():
        print(f"Headline: {title}")
        print(f"Brief: {description}")
        print("")

        account_sid = os.environ.get("ACCOUNT_SID")
        auth_token = os.environ.get("AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        client.messages.create(
            body=f"{STOCK}: {up_down} {percent_change:.2f}\nHeadline: {title}\nBrief: {description}",
            from_="+14195065772",
            to="+5519999630766"
        )