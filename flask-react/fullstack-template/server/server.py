from flask import Flask, render_template


app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
app.debug = False


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/hello")
def hello():
    return "Hello Route"


if __name__ == "__main__":
    app.run()