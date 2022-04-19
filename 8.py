"""
9. Create a Python project to fetch BBC news. Fetch a list of articles in JSON format from newsapi.org.


"""


import requests
_NEWS_API = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="


def fetch_bbc_news(bbc_news_api_key: str) -> None:
    # fetching a list of articles in json format
    bbc_news_page = requests.get(_NEWS_API + bbc_news_api_key).json()
    # each article in the list is a dict
    for i, article in enumerate(bbc_news_page["articles"], 1):
        print(f"{i}.) {article['title']}")


if __name__ == "__main__":
    fetch_bbc_news(bbc_news_api_key="718b1a4a84614ca29a61e2e17ab9a554")
