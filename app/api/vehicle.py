from flask import jsonify, request, abort
from datetime import datetime
from . import api
from ..models import Vehicle, Driver
from app import db


@api.route('/vehicles/vehicle/')
def get_all_vehicles() -> dict:
    """Return vehicles"""
    args = request.args
    if args:
        if args.get('with_drivers') == 'yes':
            vehicles = Vehicle.query.filter(Vehicle.has_driver_id())
            return jsonify({'vehicles': [vehicle.to_json() for vehicle in vehicles]})
        if args.get('with_drivers') == 'no':
            vehicles = Vehicle.query.filter(Vehicle.has_driver_id() == False)
            return jsonify({'vehicles': [vehicle.to_json() for vehicle in vehicles]})

    vehicles = Vehicle.query.all()
    return jsonify({'vehicles': [vehicle.to_json() for vehicle in vehicles]})
    

@api.route('/vehicles/vehicle/<int:vehicle_id>/')
def get_vehicle(vehicle_id: int) -> dict:
    """Return the vehicle info by id"""
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    return jsonify(vehicle.to_json())


@api.route('/vehicles/vehicle/', methods=['POST'])
def create_vehicle() -> dict:
    """Create and return a new vehicle"""
    request_data = request.get_json()
    if request_data:
        id, driver_id, make, model, plate_number, *else_ = \
            Vehicle.from_json(request.json)
        vehicle = Vehicle(make=make, model=model, plate_number=plate_number)
        db.session.add(vehicle)
        db.session.commit()
        return jsonify(vehicle.to_json())


@api.route('/vehicles/vehicle/<int:vehicle_id>/', methods=['PUT'])
def update_vehicle(vehicle_id: int) -> dict:
    """Update vehicle and return it"""
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    request_data = request.get_json()
    if request_data:
        id, driver_id, make, model, plate_number, *else_ = \
            Vehicle.from_json(request.json)
        vehicle.make = make
        vehicle.model = model
        vehicle.plate_number = plate_number
        vehicle.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify(vehicle.to_json())


@api.route('/vehicles/set_driver/<int:vehicle_id>/', methods=['POST'])
def set_driver(vehicle_id: int) -> dict:
    """Adds the driver (json POST request) to the vehichle if empty,
    otherwise removes the driver from the vehicle.
    Returns the vehicle"""
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    request_data = request.get_json()
    if request_data:
        id, *else_ = Driver.from_json(request.json)
        driver = Driver.query.get_or_404(id)
        if not vehicle.driver:
            driver.vehicle.append(vehicle)
            db.session.commit()
        else:
            if vehicle.driver == driver:
                driver.vehicle.remove(vehicle)
                db.session.commit()
            else:
                abort(405)
        vehicle = Vehicle.query.get(vehicle_id)
        return jsonify(vehicle.to_json())


@api.route('/vehicles/vehicle/<int:vehicle_id>/', methods=['DELETE'])
def delete_vehicle(vehicle_id: int):
    """Delete vehicle"""
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'response': 'Success'})
