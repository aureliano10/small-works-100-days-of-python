import requests
from dotenv import load_dotenv
import os
load_dotenv()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_actions_data():
    API_KEY = os.environ.get("ACTIONS_API_KEY")
    STOCK = "TSLA"

    parameters = {
        "function" : "TIME_SERIES_DAILY",
        "symbol" : STOCK,
        "outputsize" : "compact",
        "apikey" : API_KEY,

    }
    response = requests.get("https://www.alphavantage.co/query", params= parameters)
    response.raise_for_status()
    data = response.json()
    data_formated = list(data["Time Series (Daily)"])
    days = [
            data["Time Series (Daily)"][data_formated[0]],
            data["Time Series (Daily)"][data_formated[1]]
            ]
    today = float(days[0]['4. close'])
    yesterday = float(days[1]['4. close'])
    variacion = ((today - yesterday) / yesterday) * 100
    # if variacion > 5 or variacion < -5:
    #     return True, variacion
    # else:
    #     return False, variacion
    return True, variacion