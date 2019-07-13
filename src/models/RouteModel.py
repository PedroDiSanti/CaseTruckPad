import datetime
from . import db
from marshmallow import fields, Schema


class RouteModel(db.Model):
    __tablename__ = 'route'

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    origin_latitude = db.Column(db.Float, nullable=False)
    origin_longitude = db.Column(db.Float, nullable=False)
    destination_latitude = db.Column(db.Float, nullable=False)
    destination_longitude = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.driver_id = data.get('driver_id')
        self.origin_latitude = data.get('origin_latitude')
        self.origin_longitude = data.get('origin_longitude')
        self.destination_latitude = data.get('destination_latitude')
        self.destination_longitude = data.get('destination_longitude')
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_routes():
        return RouteModel.query.all()

    @staticmethod
    def get_one_route(id):
        return RouteModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class RouteSchema(Schema):
    id = fields.Int(dump_only=True)
    driver_id = fields.Int(required=True)
    origin_latitude = fields.Float(required=True)
    origin_longitude = fields.Float(required=True)
    destination_latitude = fields.Float(required=True)
    destination_longitude = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
