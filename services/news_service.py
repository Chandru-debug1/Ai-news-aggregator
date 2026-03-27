import requests
from config import MEDIASTACK_API_KEY

def get_news(category):
    url = "http://api.mediastack.com/v1/news"
    params = {
        "access_key": MEDIASTACK_API_KEY,
        "categories": category,
        "languages": "en"
    }
    response = requests.get(url, params=params)
    return response.json()