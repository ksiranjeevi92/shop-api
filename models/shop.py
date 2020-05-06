from db import db
from sqlalchemy import inspect

class ShopModel(db.Model):
    __tablename__ = "shop"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    shopname = db.Column(db.String(80))
    status = db.Column(db.Boolean(True))

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __init__(self, name, shopname, status):
        self.name = name
        self.shopname = shopname
        self.status = status

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'shopname': self.shopname,
            'status': self.status
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
