import web
import csv
import json
import os
from hashlib import blake2b

urls = (
    '/', 'Home',
    '/processCSV', 'ProcessCSV'
)

app = web.application(urls, globals())
render = web.template.render('Views/Templates', base="MainLayout")


class Home:
    def GET(self):
        return render.Home()


class ProcessCSV:
    def POST(self):
        file = web.input(csv_upload={})
        data_lines = []
        file_hash = blake2b(b'Hacked').hexdigest()
        with open('files/' + file_hash + '.csv', 'wb') as f:
            f.write(file['csv_upload'].value)
        
        with open('files/' + file_hash + '.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_lines.append(dict(row))
        
        os.remove('files/' + file_hash + '.csv')
        return json.dumps(data_lines)


if __name__ == '__main__':
    app.run()