from flask import Flask,  jsonify
from flask_restful import Api

from db import db
from resource.shop import ShopCreate
from resource.shop import Shop
from resource.shop import ShopList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fbdehezqfnhjqd:79bcc943f58c12f74d8ae2892bc784afa6460bf24fa25ca5252e3debf88c8a54@ec2-54-217-204-34.eu-west-1.compute.amazonaws.com:5432/d6mal2jruh45nd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


# @app.before_first_request
# def create_tables():
    # db.create_all()

api.add_resource(ShopCreate, '/api/create')
api.add_resource(ShopList, '/api/list')
api.add_resource(Shop, '/api/shop/<int:id>')

if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run()


