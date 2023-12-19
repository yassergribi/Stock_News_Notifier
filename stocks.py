import requests
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_api = os.environ['ALPHA_API']

print(alpha_api)

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'

stocks_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey": alpha_api,
}

def get_stocks_percentage():
    response = requests.get(url=STOCK_ENDPOINT, params=stocks_params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]


    data_list = [value for (key, value) in data.items()]

    yesterday_data = data_list[0]
    yesterday_closing_price = float(yesterday_data["4. close"])

    day_before_data = data_list[1]
    day_before_closing_price = float(day_before_data["4. close"])

    percentage = ((yesterday_closing_price - day_before_closing_price)/yesterday_closing_price )*100

    return round(percentage)

