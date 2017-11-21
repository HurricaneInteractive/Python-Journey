from flask import Flask, render_template, request
from wtforms import Form, FileField, StringField, validators
import os

app = Flask(__name__)
app.debug = True

class CSVForm(Form):
    csvfile = FileField(u'CSV File')
    delimiter = StringField(u'Delimiter (Default comma)')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CSVForm(request.form)
    UPLOAD_PATH = 'uploads/'
    if request.method == 'POST' and form.validate():
        return 'ok'
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run()
