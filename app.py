from flask import Flask
from flask_restful import Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT
from user import UserRegister
from item import Item, ItemList


app = Flask(__name__)
app.secret_key = 'testing'
api = Api(app)
jwt = JWT(app, authenticate, identity)


# Resources and route below.
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
