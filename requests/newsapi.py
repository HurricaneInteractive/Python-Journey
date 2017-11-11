'''
    Opens a random article in the response from the news api: https://newsapi.org/
    This will require a apikey.
    Either set a variable below and change 'api.read()' in the params to the variable
    or
    Create a txt file in the current directory called 'apikey.txt' and paste key in there
'''

import requests
import simplejson as json
# using selenium to create and open a web browser
# Follow setup instructions before running script: http://selenium-python.readthedocs.io/installation.html
# Currently using Firefox driver
from selenium import webdriver
import random


# REQUEST SETUP
api = open("./apikey.txt", "r+")
newsAPIEndPoint = 'https://newsapi.org/v1/articles';
params = {"source": "abc-news-au", "apiKey": api.read()}
headers = {"Content-Type": "application/json"}

# WEBDRIVER
driver = webdriver.Firefox()

r = requests.get(newsAPIEndPoint, params=params, headers=headers);
print("URL", r.url)
print("Status Code:", r.status_code)
# parses response text into json
data = json.loads(r.text)
# get all the articles
articles = data["articles"]
# append all the urls into a list
urls = []
for item in articles:
    urls.append(item["url"])

# Pick a random url
random_index = random.randrange(0, len(urls) + 1)
random_url = urls[random_index];
# open in web browser
driver.get(random_url)