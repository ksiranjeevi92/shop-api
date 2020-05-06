from flask_restful import Resource, reqparse
from flask_cors import cross_origin

from models.shop import ShopModel

_data_parser = reqparse.RequestParser()

_data_parser.add_argument('name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_data_parser.add_argument('shopname',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_data_parser.add_argument('status',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )

class ShopCreate(Resource):
    def post(self):
        data = _data_parser.parse_args()
        if ShopModel.find_by_name(data['name']):
            return {"message": "A name already exists"}, 400

        shop = ShopModel(data['name'], data['shopname'], data['status'])
        shop.save_to_db()
        return {'message': 'created'}, 201

class Shop(Resource):
    @classmethod
    def get(cls, id: int):
        shop = ShopModel.find_by_id(id)
        if not shop:
            return {'message': 'Not Found'}, 404
        return shop.json(), 200
    @classmethod
    def put(self, id):
        data = _data_parser.parse_args()
        item = ShopModel.find_by_id(id)

        if item:
            item.name = data['name']
            item.shopname = data['shopname']
            item.status = data['status']
        else:
            item = ShopModel(id, **data)

        item.save_to_db()

        return item.json()

    @classmethod
    def delete(cls, id: int):
        shop = ShopModel.find_by_id(id)
        if not shop:
            return {'message': 'Not Found'}, 404
        shop.delete_from_db()
        return {'message': 'deleted.'}, 200


class ShopList(Resource):
    def get(self):
        items = [item.json() for item in ShopModel.get_all()]
        return {
                   'items': items
               }, 200