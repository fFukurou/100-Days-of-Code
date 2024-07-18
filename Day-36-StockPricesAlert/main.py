#Stock Prices Alert Project
#CAUTION !!! the Alpha Vantage (Stocks) API rate limit is 25 requests per day...
#CAUTION !!! Running this file will subtract dollars from the Twilio free trial account...

import requests
from personal_info import *
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stocks_api_key,
}

news_params = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "pageSize": 3,
    "excludeDomains": "https://consent.yahoo.com/",
    "apiKey": news_api_key,
}

# ----------------------------- If there is a problem with the API (rate limit...)
try:
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    data = response.json()

    stocks_data = data["Time Series (Daily)"]

    stocks_list = [value for (day, value) in stocks_data.items()]
    last_day_closing_price = stocks_list[0]["4. close"]
    day_before_last_closing_price = stocks_list[1]["4. close"]

    absolute_price_difference = abs(float(last_day_closing_price) - float(day_before_last_closing_price))

    percent_difference = ((float(last_day_closing_price) - float(day_before_last_closing_price)) / float(day_before_last_closing_price)) * 100
    print(percent_difference)

# ----------------------- then it will default to example values
except:
    last_day_closing_price = 255
    day_before_last_closing_price = 220
    absolute_price_difference = abs(last_day_closing_price - day_before_last_closing_price)

    percent_difference = ((last_day_closing_price - day_before_last_closing_price) / day_before_last_closing_price) * 100

# ----------------------

def get_news():
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    data = response.json()
    first_three_articles = data["articles"][:3]
    return first_three_articles
    



if percent_difference > 5 or percent_difference < -5:
    news = get_news()
    formatted_news = [f"{STOCK_NAME}: {"🔺" if percent_difference > 0 else "🔻"} {percent_difference:.2f}%\n HEADLINE:{article["title"]}\n BRIEF: {article["description"] if article["description"] != None else article["content"]}" for article in news]
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=f"whatsapp:{twilio_whatsapp_number}",
                                      body=f"{formatted_news[0]}",
                                      to=f"whatsapp:{my_number}") # WhatsApp

    print(message.sid)

