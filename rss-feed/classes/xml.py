import datetime
from email.utils import formatdate, parsedate_tz


class XML:
    def __init__(self, title, link, description, articles):
        self.title = title
        self.link = link
        self.description = description
        self.articles = articles

    def generate_header(self):
        return '<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>' + self.title + '</title><link>' + self.link + '</link>' + '<description>' + self.description + '</description>'

    def generate_footer(self):
        return '</channel></rss>'

    def generate_items(self):
        output = ''
        for article in self.articles:
            pubDate = article["publishedAt"]
            # pubDate = str(parsedate_tz(pubDate))
            output += '<item><title>' + article["title"] + '</title><link>' + article["url"] + '</link><description>' + article["description"] + '</description><pubDate>' + pubDate + '</pubDate></item>'
        return output
