from app import db
from datetime import datetime


class Driver(db.Model):
    """Driver model"""
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(64), nullable=False)
    second_name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    vehicle = db.relationship('Vehicle', backref='driver')

    def to_json(self) -> dict:
        """Return Driver info in the json format"""
        json_data = {
            'id': self.id,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        return json_data
    
    def from_json(json_data) -> tuple:
        id = json_data.get('id')
        first_name = json_data.get('first_name')
        second_name = json_data.get('second_name')
        created_at = json_data.get('created_at')
        updated_at = json_data.get('updated_at')
        return id, first_name, second_name, created_at, updated_at


class Vehicle(db.Model):
    """Vehicle model"""
    __tablename__ = 'vehichles'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'))
    make = db.Column(db.String(32), nullable=False)
    model = db.Column(db.String(64), nullable=False)
    plate_number = db.Column(db.String(8), index=True, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())


    @classmethod
    def has_driver_id(cls) -> bool:
        """Helper function"""
        return Vehicle.driver_id != None

    
    def has_driver(self) -> bool:
        """Return True if has a reference to a Driver"""
        return self.driver_id != None
    
    def to_json(self) -> dict:
        json_data = {
            'id': self.id,
            'driver_id': self.driver_id,
            'make': self.make,
            'model': self.model,
            'plate_number': self.plate_number,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        return json_data
    
    def from_json(json_data) -> tuple:
        id = json_data.get('id')
        driver_id = json_data.get('driver_id')
        make = json_data.get('make')
        model = json_data.get('model')
        plate_number = json_data.get('plate_number')
        created_at = json_data.get('created_at')
        updated_at = json_data.get('updated_at')
        return id, driver_id, make, model, plate_number, created_at, updated_at