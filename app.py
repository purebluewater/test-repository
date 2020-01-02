from flask import Flask              #when postmake make reqeuest through API, that request is in this variable
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     # turn off flasky sqlalchemy sql tracker
app.secret_key = 'jose'
api = Api(app)  # allow you easily to add resources

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  #create new endpoint: /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register') #when we execute post request to /register, it will call UserRegister

if __name__=='__main__':    #this will prevent import to run the statement
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
