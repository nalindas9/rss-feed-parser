import os
import time
from utils import *

if __name__ == '__main__':
    URL = 'https://www.yahoo.com/news/rss/'
    # Scrape the URL every 1 hour
    while True:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        # If news folder does not exist, create it
        if not os.path.exists('news'):
            os.makedirs('news')
        scrapeURL(url=URL, filename='news_' + current_time + '.csv')
        time.sleep(3600)