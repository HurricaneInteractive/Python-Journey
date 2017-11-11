# imports libraries
from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image
import os


# define a search function
def StartSearch():
    # gets user input and define params
    search = input("Search for: ")
    params = {"q": search}
    # sets a directory name based on search
    dir_name = search.replace(" ", "_").lower()

    # if the directory does not exist, then create it
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    # creates search url
    r = requests.get("https://www.bing.com/images/search", params=params)

    # uses beautiful soup to parse and find all <a> elements with class of thumb
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class", "thumb"})

    # sets download limit
    stop_length = 5
    i = 0

    # for each <a>
    for item in links:
        if i < stop_length:
            # try to send request
            try:
                # get the image using the <a> href
                img_object = requests.get(item.attrs["href"])
                print("Getting:", item.attrs["href"])
                # create a title from href attribute
                title = item.attrs["href"].split("/")[-1]
                # try to save image
                try:
                    # saves image info directory using the image format and title
                    img = Image.open(BytesIO(img_object.content))
                    img.save("./" + dir_name + "/" + title, img.format)
                # skip over image if it can't be saved and continue to next iteration
                except:
                    print('Skipped')
                    continue
            # if it can't send the request, continue to next iteration
            except:
                print("Could not request image")
                continue
            i += 1
    
    StartSearch()

StartSearch()
