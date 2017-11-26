from flask import Flask, jsonify, request, render_template


app = Flask(__name__)
app.debug = False

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'Bread',
                'price': 0.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# API thinking
# POST - used to receive data
# GET - used to send data back

# ENDPOINTS
# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')  # /store/coles
def get_store(name):
    # Iterate over stores, if store name matches, return store
    # If none, return an error
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')  # /store
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')  # /store/coles/bread
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

app.run()
