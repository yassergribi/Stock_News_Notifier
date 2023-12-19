from re import A
import requests
from stocks import get_stocks_percentage
from news import get_news
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone = os.environ["TWILIO_PHONE"]
my_phone = os.environ["MY_PHONE"]

percentage = get_stocks_percentage()

if percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


percentage = abs(percentage)
if percentage >= 0.1:
    articles = get_news()

    formated_articles = [f"{STOCK}: {up_down}{percentage}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in articles]

    client = Client(account_sid, auth_token)
    for article in formated_articles:
        message = client.messages \
                    .create(
                        body=article,
                        from_= twilio_phone,
                        to= my_phone
                    )

    print(message.status)

