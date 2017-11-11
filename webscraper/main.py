# imports BeautifulSoup : pip3 install bs4
from bs4 import BeautifulSoup
import requests

# Asks for user input
search = input("Enter Search Term: ")
# Creates url params and request
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

# uses beautiful soup to parse response text
soup = BeautifulSoup(r.text, "html.parser")
# creates ol with the id of b_results
results = soup.find("ol", {"id": "b_results"})
# gets all li inside of ol with class of b_algo
links = results.findAll("li", {"class": "b_algo"})

# Loops through each li
for item in links:
    # get link (<a>) text and url (href)
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    # if it has both
    if item_text and item_href:
        # print out values
        print(item_text)
        print(item_href)

        # finds <h2> inside of li
        children = item.find("h2")
        # prints out next sibling
        print("Next Sibling:", children.next_sibling)