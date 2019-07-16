import datetime
from . import db
from datetime import date
from marshmallow import fields, Schema


class VehicleModel(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    own_vehicle = db.Column(db.Boolean, default=False, nullable=False)
    is_loaded = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.driver_id = data.get('driver_id')
        self.name = data.get('name')
        self.type = data.get('type')
        self.own_vehicle = data.get('own_vehicle')
        self.is_loaded = data.get('is_loaded')
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
    def get_all_vehicles():
        return VehicleModel.query.all()

    @staticmethod
    def get_one_vehicle(id):
        return VehicleModel.query.get(id)

    @staticmethod
    def get_driver_id(driver_id):
        return VehicleModel.query.get(driver_id)

    @staticmethod
    def get_trucks_today():
        return db.session.query(VehicleModel). \
            filter(db.cast(VehicleModel.created_at, db.Date) == date.today()).all()

    # TODO: create a method to count how many loaded trucks pass by the terminal by week and month.

    def __repr(self):
        return '<id {}>'.format(self.id)


class VehicleSchema(Schema):
    id = fields.Int(dump_only=True)
    driver_id = fields.Int(required=True)
    name = fields.Str(required=True)
    type = fields.Int(required=True)
    own_vehicle = fields.Boolean(required=True)
    is_loaded = fields.Boolean(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
