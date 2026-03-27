import requests
import requests
from dotenv import load_dotenv
import os
load_dotenv()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    API_KEY = os.environ.get("NEWS_API_KEY")
    COMPANY_NAME = "Tesla Inc"
    parameters = {
        "q" : COMPANY_NAME,
        "apikey" : API_KEY,
        "language": "es",
        "pageSize" : 3,
        "sortBy" : "publishedAt"
    }
    response = requests.get("https://newsapi.org/v2/everything", params= parameters)
    response.raise_for_status()
    data = response.json()

    news = data["articles"]

    list_news = []

    for new in news:
         dict= {
             "title" : new["title"],
             "description" : new["description"],
             "url" : new["url"]
         }
         list_news.append(dict)

    return list_news



