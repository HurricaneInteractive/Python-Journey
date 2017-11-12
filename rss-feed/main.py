import requests
import simplejson as json
from classes.xml import XML


api = open("./apikey.txt", "r+")
newsAPIEndPoint = 'https://newsapi.org/v1/articles';
params = {"source": "abc-news-au", "apiKey": api.read()}
headers = {"Content-Type": "application/json"}

r = requests.get(newsAPIEndPoint, params=params, headers=headers)

data = json.loads(r.text)
# f = open("./example.json", "w+")
# f.write(json.dumps(data))

rss_title = "News API"
rss_link = "https://newsapi.org/"
rss_description = "RSS feed based on news api response"
rss_articles = data["articles"]

xml = XML(rss_title, rss_link, rss_description, rss_articles)
output = xml.generate_header()
output += xml.generate_items()
output += xml.generate_footer()

rss = open("./newsfeed.rss", "w+")
rss.write(output)
print("Done")