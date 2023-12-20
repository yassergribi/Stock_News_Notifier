from stocks import get_stocks_percentage
from news import get_news
from twilio_service import send_sms

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


percentage = get_stocks_percentage()
if percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
    percentage = abs(percentage)


if percentage >= 5:
    articles = get_news()

    formated_articles = [f"{STOCK}: {up_down}{percentage}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in articles]

    for article in formated_articles:
        send_sms(article)

