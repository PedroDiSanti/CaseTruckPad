import datetime
from . import db
from marshmallow import fields, Schema
from .VehicleModel import VehicleSchema, VehicleModel
from .RouteModel import RouteSchema


class DriverModel(db.Model):
    __tablename__ = 'driver'

    id = db.Column(db.Integer, primary_key=True)
    vehicle = db.relationship('VehicleModel', backref='driver', lazy=True)
    route = db.relationship('RouteModel', backref='driver', lazy=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(9), nullable=False)
    cnh = db.Column(db.String(3), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.name = data.get('name')
        self.age = data.get('age')
        self.sex = data.get('sex')
        self.cnh = data.get('cnh')
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
    def get_all_drivers():
        return DriverModel.query.all()

    @staticmethod
    def get_one_driver(id):
        return DriverModel.query.get(id)

    @staticmethod
    def get_driver_by_name(name):
        return DriverModel.query.filter(DriverModel.name == name).all()

    @staticmethod
    def list_drivers_truck_is_not_loaded():
        return db.session.query(DriverModel.id, DriverModel.name)\
                               .join(VehicleModel, DriverModel.id == VehicleModel.driver_id)\
                               .filter(VehicleModel.is_loaded == False)\
                               .all()

    def __repr(self):
        return '<id {}>'.format(self.id)


class DriverSchema(Schema):
    id = fields.Int(dump_only=True)
    vehicle = fields.Nested(VehicleSchema, many=True)
    route = fields.Nested(RouteSchema, many=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    sex = fields.Str(required=True)
    cnh = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
