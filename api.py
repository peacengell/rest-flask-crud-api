from flask import Flask, jsonify, request


app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ],

    }
]

# Home page route


@app.route('/')
def home():
    return "Hello, World!"

# Post app route

# user to received data


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# Get /store/<string:name>
# use to get information only
# for specificque store.


@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    # if match return it
    # if none return store not found
    for store in stores:
        if name == store['name']:
            return jsonify(store)
        else:
            return jsonify({'message': "Store " + (str(name)).title() + " not found!."})

# Get /store
# List all the store available


@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})

# Post to store/<string>/item {name:, price:}
# to create item in store.


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        request_data = request.get_json()
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': "Store " + (str(name)).title() + " and " + str(items) + " not found!."})
# Get /store/<string:name>/item


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        else:
            return jsonify({'message': "Store " + (str(name)).title() + " and " + str(items) + " not found!."})


app.run(debug=True, port=5000)
