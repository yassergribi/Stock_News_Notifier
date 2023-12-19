import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API = "38dd80ea2cdc4d3981e89d8b06e4c8cd"
news_url = "https://newsapi.org/v2/everything"

news_params = {
    # "q":STOCK,
    "qInTitle":COMPANY_NAME,
    # "sortBy":"popularity",
    "apiKey":NEWS_API
    }

news_descriptions = []

def get_news():
    response = requests.get(url=news_url, params=news_params)
    articles = response.json()["articles"][:3]

    return articles
