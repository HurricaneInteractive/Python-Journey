import web
import requests
from bs4 import BeautifulSoup
import json

web.config.debug = False

urls = (
    '/', 'Home',
    '/retrievePosts', 'RetrievePost'
)

app = web.application(urls, globals())
render = web.template.render("Views/Templates", base="MainLayout")


class Home:
    def GET(self):
        return render.Home()


class RetrievePost:
    def POST(self):
        data = web.input()
        url = 'https://www.meetup.com/en-AU/find/' + data.topic + '/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        ul = soup.find("div", {"id": "simple-view"})
        ul = ul.find("ul", {"class": "j-groupCard-list"})
        print(ul)
        return "success"


if __name__ == "__main__":
    app.run()