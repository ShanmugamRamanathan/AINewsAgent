
import feedparser
from newspaper import Article

RSS_FEEDS = [
    "https://marktechpost.com/feed",
    "https://research.google/blog/rss",
    "https://aihub.org/feed?cat=-473",
    "https://bair.berkeley.edu/blog/feed.xml",
    "https://analyticsindiamag.com/feed/",
    "https://arxiv.org/rss/cs.LG"
]

def fetch_news():
    articles = []
    for feed in RSS_FEEDS:
        parsed_feed = feedparser.parse(feed)
        for entry in parsed_feed.entries:
            article = Article(entry.link)
            article.download()
            article.parse()
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "content": article.text
            })

    # print("Articles - ",articles)
    return articles
