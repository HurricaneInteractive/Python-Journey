import web
import requests
from bs4 import BeautifulSoup
import json

web.config.debug = False

urls = (
    '/', 'Home',
    '/retrievePosts', 'RetrievePost',
    '/autoComplete', 'AutoComplete'
)

app = web.application(urls, globals())
render = web.template.render("Views/Templates", base="MainLayout")


class Home:
    def GET(self):
        return render.Home()


class RetrievePost:
    def POST(self):
        data = web.input()
        url = 'https://www.meetup.com/en-AU/find/' + data.topic.lower() + '/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        # ul = soup.find("div", {"id": "simple-view"})
        # ul = ul.find("ul", {"class": "j-groupCard-list"})
        data = []
        list_items = soup.findAll('li', {'class': 'groupCard'})

        for item in list_items:
            link = item.find('a', {'class': 'groupCard--photo'}).attrs['href']
            title = item.find('h3').text
            image_url = item.find('a', {'class': 'groupCard--photo'}).get('style')
            title = ' '.join(title.split())
            obj = {'link': link, 'title': title, 'imageUrl': image_url}
            data.append(obj)

        # data = json.dumps(data)
        return json.dumps(data)


class AutoComplete:
    def GET(self):
        f = open('./data/topics.json', 'r+')
        topics = json.loads(f.read())
        return json.dumps(topics['topics'])



if __name__ == "__main__":
    app.run()