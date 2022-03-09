from rss_feed_parser import RSSFeedParser

def scrapeURL(url: str, filename: str) -> None:
    """
    Call url and store the returned rss file
    in a folder called news in current directory.
    """
    rss_parser = RSSFeedParser()
    resp = rss_parser.getResponse(url)
    news_items = rss_parser.getNewsItems(resp)
    df = rss_parser.getDataFrame(news_items)
    rss_parser.saveDataFrame(df, 'news/' + filename)
    