from flask import Flask, render_template
from flask_restful import Resource, Api

from items import ItemList

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app.debug = False
api = Api(app)


@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

# Resource declaration
api.add_resource(ItemList, '/items')

if __name__ == "__main__":
    app.run()