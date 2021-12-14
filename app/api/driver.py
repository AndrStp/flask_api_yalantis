from flask import jsonify, request
from datetime import datetime
from . import api
from ..models import Driver
from app import db


@api.app_errorhandler(404)
def page_not_found(e):
    """App 404 error handler"""
    response = jsonify({'error': 'not found'})
    response.status_code = 404
    return response


@api.app_errorhandler(405)
def method_not_allowed(e):
    """App 405 error handler"""
    response = jsonify({'error': 'method not allowed'})
    response.status_code = 405
    return response


@api.route('/drivers/driver/')
def get_all_drivers() -> dict:
    """Return drivers"""
    args = request.args
    if args:
        if args.get('created_at__gte'):
            query_date = args.get('created_at__gte')
            datetime_obj = datetime.strptime(query_date, "%d-%m-%Y")
            drivers = Driver.query.filter(Driver.created_at >= datetime_obj)
            return jsonify({'drivers': [driver.to_json() for driver in drivers]})

        elif args.get('created_at__lte'):
            query_date = args.get('created_at__lte')
            datetime_obj = datetime.strptime(query_date, "%d-%m-%Y")
            drivers = Driver.query.filter(Driver.created_at <= datetime_obj)
            return jsonify({'drivers': [driver.to_json() for driver in drivers]})
    
    drivers = Driver.query.all()
    return jsonify({'drivers': [driver.to_json() for driver in drivers]})
    

@api.route('/drivers/driver/<int:driver_id>/')
def get_driver(driver_id: int) -> dict:
    """Return the driver info by id"""
    driver = Driver.query.get_or_404(driver_id)
    return jsonify(driver.to_json())


@api.route('/drivers/driver/', methods=['POST'])
def create_driver() -> dict:
    """Create and return a new driver"""
    request_data = request.get_json()
    if request_data:
        id, first_name, second_name, *else_ = Driver.from_json(request.json)
        driver = Driver(first_name=first_name, second_name=second_name)
        db.session.add(driver)
        db.session.commit()
        return jsonify(driver.to_json())


@api.route('/drivers/driver/<int:driver_id>/', methods=['PUT'])
def update_driver(driver_id: int) -> dict:
    """Update driver and return it"""
    driver = Driver.query.get_or_404(driver_id)
    request_data = request.get_json()
    if request_data:
        id, first_name, second_name, *else_ = \
            Driver.from_json(request.json)
        driver.first_name = first_name
        driver.second_name = second_name
        driver.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify(driver.to_json())


@api.route('/drivers/driver/<int:driver_id>/', methods=['DELETE'])
def delete_driver(driver_id: int):
    """Delete driver"""
    driver = Driver.query.get_or_404(driver_id)
    db.session.delete(driver)
    db.session.commit()
    return jsonify({'response': 'Success'})
