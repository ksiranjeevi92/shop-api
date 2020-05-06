from flask import Flask,  jsonify
from flask_restful import Api
from flask_cors import CORS, cross_origin
from db import db

from resource.shop import ShopCreate
from resource.shop import Shop
from resource.shop import ShopList

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fbdehezqfnhjqd:79bcc943f58c12f74d8ae2892bc784afa6460bf24fa25ca5252e3debf88c8a54@ec2-54-217-204-34.eu-west-1.compute.amazonaws.com:5432/d6mal2jruh45nd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.before_first_request
def create_tables():
    db.create_all()
db.init_app(app)
api.add_resource(ShopCreate, '/api/create')
api.add_resource(ShopList, '/api/list')
api.add_resource(Shop, '/api/shop/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)


