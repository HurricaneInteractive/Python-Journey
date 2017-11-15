import web
import csv
import io
import json
import os

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
        with open('files/upload.csv', 'wb') as f:
            f.write(file['csv_upload'].value)
        
        with open('files/upload.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            header = next(csv_reader)
            for row in csv_reader:
                data_lines.append(dict(row))
        
        os.remove('files/upload.csv');
        return json.dumps(data_lines)


if __name__ == '__main__':
    app.run()