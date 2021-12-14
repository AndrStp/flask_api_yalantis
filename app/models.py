from app import db
from datetime import datetime


class Driver(db.Model):
    """Driver model"""
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(64))
    second_name = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, index=True, 
                           default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=None)


class Vehicle(db.Model):
    """Vehicle model"""
    __tablename__ = 'vehichles'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'))
    make = db.Column(db.String(32))
    model = db.Column(db.String(64))
    plate_number = db.Column(db.String(8), index=True)
    created_at = db.Column(db.DateTime, index=True, 
                           default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=None)

