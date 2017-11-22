from flask import Flask, render_template, request, session
from wtforms import Form, FileField, StringField, validators
from wtforms.csrf.session import SessionCSRF
from datetime import timedelta
import os
import time
import csv
import json

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'Hacker'
app.config['CSRF_SECRET_KEY'] = b'EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym'

class CSVForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = app.config['CSRF_SECRET_KEY']
        csrf_time_limit = timedelta(minutes=20)

        @property
        def csrf_context(self):
            return session

    csvfile = FileField(u'CSV File')
    delimiter = StringField(u'Delimiter (Default comma)')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CSVForm(request.form)
    if request.method == 'POST' and form.validate():
        delimiter = form.delimiter.data
        file_data = request.files['csvfile'].read()
        data_lines = []
        
        t = str(int(time.time()))
        path = os.path.dirname(os.path.realpath(__file__))
        file_name = path + '/uploads/' + t + '.csv'
        
        open(file_name, 'wb').write(file_data)
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
            data_lines = [dict(row) for row in csv_reader]

        os.remove(file_name)
        return json.dumps(data_lines)
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run()
