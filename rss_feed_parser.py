import requests
from bs4 import BeautifulSoup
import pandas as pd

class RSSFeedParser:
    def __init__(self) -> None:
        pass

    def getResponse(self, url: str) -> requests.Response:
        """
        Get the response from the url
        """
        try:
            resp = requests.get(url)
            return resp
        except Exception as e:
            print('Exception: {}'.format(e))
            print('Status code: {}'.format(resp.status_code))
            return None

    def getNewsItems(self, resp: requests.Response) -> list:
        """
        Get the news items from the response
        """
        try:
            soup = BeautifulSoup(resp.content, features='xml')
            # Find all the <item> tags
            items = soup.find_all('item')
            # Create a list of dictionaries to store the news items
            news_items = list()
            # Scrape the HTML tags for each news item
            for item in items:
                news_item = dict()
                news_item['title'] = item.title.text
                news_item['link'] = item.link.text
                news_item['pubDate'] = item.pubDate.text
                news_items.append(news_item)
            return news_items
        except Exception as e:
            print('Exception: {}'.format(e))
            return None
    
    def getDataFrame(self, news_items: list) -> pd.DataFrame:
        """
        Create a dataframe from the news items
        """
        try:
            df = pd.DataFrame(news_items, columns=['title', 'link', 'pubDate'])
            return df
        except Exception as e:
            print('Exception: {}'.format(e))
            return None

    def saveDataFrame(self, df: pd.DataFrame, filename: str) -> None:
        """
        Save the dataframe to a csv file
        """
        try:
            df.to_csv(filename, index=False, encoding='utf-8')
        except Exception as e:
            print('Exception: {}'.format(e))
            return None

    