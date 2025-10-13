import requests
from datetime import *
NEWS_API = "2cfdfb0793304dcdacdb1ba1ce7326e7"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
today = datetime.today()
yesterday = today - timedelta(days=1)
print(today,yesterday)
paramters = {
    "apiKey" : NEWS_API,
    "q" : COMPANY_NAME,
    "from" : "2025-10-09",
    "to" : "2025-10-10",
    "language" : "en",
    "sortBy" : "popularity",
    "pageSize" : 3
}
def get_news():
    top_3 = []
    try:
        news_response = requests.get(NEWS_ENDPOINT,params=paramters)
        news_response.raise_for_status()
        news = news_response.json()
        for i in range(0,3):
            headline = news["articles"][i]["title"]
            description = news["articles"][i]["description"]
            top_3.append(f"{headline}\n{description}")
        return top_3
    except:
        return "Now articles in the given period"



