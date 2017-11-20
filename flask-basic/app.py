from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'ok'
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
