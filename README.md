# Flask REST API project template

This project shows one of the possible ways to implement RESTful API server.

There are implemented two models: Driver and Vehicle, one Driver has many Vehicles.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
.
├── README.md
├── run.py
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── driver.py
│   │   ├── vehicle.py
├── tests
│   ├── TODO
├── config.py
├── .flaskenv.example
├── requirements.txt
└── SETUP.md
```

* app - application dir.
* app/api - REST API blueprint.
* .flaskenv.example - python-dotenv example file
* config.py - app configuration objects.
* run.py - flask application initialization.
* SETUP.md - setup instruction

## Running 

1. Clone repository.
2. pip install requirements.txt
3. Initialize venv and activate it
4. Run following commands:
    1. python db init
    2. python db migrate
    3. python db upgrade
5. Start server by running python run.py runserver

## Usage
### Drivers endpoint
GET http://127.0.0.1:5000/api/v1/drivers/driver/

Returns all drivers

RESPONSE
```json
{
  "drivers": [
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "first_name": "test_1",
      "id": 1,
      "second_name": "test_1_sname",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "first_name": "test_2",
      "id": 2,
      "second_name": "test_2_sname",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "first_name": "test_3",
      "id": 3,
      "second_name": "test_3_sname",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "first_name": "test_4",
      "id": 4,
      "second_name": "test_4_sname",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Fri, 10 Dec 2021 00:00:00 GMT",
      "first_name": "test_date_2",
      "id": 7,
      "second_name": "test_date_2_sname",
      "updated_at": "Tue, 14 Dec 2021 20:46:18 GMT"
    }
  ]
}
```

GET http://127.0.0.1:5000/api/v1/drivers/driver/?created_at__gte=12-12-2021

Returns all drivers created on or after December 12th 2021

RESPONSE
```json
{
  "drivers": [
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "first_name": "test_1",
      "id": 1,
      "second_name": "test_1_sname",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "first_name": "test_2",
      "id": 2,
      "second_name": "test_2_sname",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "first_name": "test_3",
      "id": 3,
      "second_name": "test_3_sname",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "first_name": "test_4",
      "id": 4,
      "second_name": "test_4_sname",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    }
  ]
}
```

GET http://127.0.0.1:5000/api/v1/drivers/driver/?created_at__lte=12-12-2021

Returns all drivers created on or before December 12th 2021

RESPONSE
```json
{
  "drivers": [
    {
      "created_at": "Fri, 10 Dec 2021 00:00:00 GMT",
      "first_name": "test_date_2",
      "id": 7,
      "second_name": "test_date_2_sname",
      "updated_at": "Tue, 14 Dec 2021 20:46:18 GMT"
    }
  ]
}
```

GET http://127.0.0.1:5000/api/v1/drivers/driver/1/

Returns the driver by id (1)

RESPONSE
```json
{
  "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
  "first_name": "test_1",
  "id": 1,
  "second_name": "test_1_sname",
  "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
}
```

POST http://127.0.0.1:5000/api/v1/drivers/driver/

Creates new driver with provided fileds. Returns newlt created driver

REQUEST
```json
{
    "first_name": "test_4",
    "second_name": "test_4_sname"
}
```

RESPONSE
```json
{
    "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
    "first_name": "test_4",
    "id": 4,
    "second_name": "test_4_sname",
    "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
}
```

PUT http://127.0.0.1:5000/api/v1/drivers/driver/4/

Updates the fields of the driver (id=4) with given fields

REQUEST
```json
{   
    "id": 4,
    "first_name": "test_4_new",
    "second_name": "test_4_new"
}
```

RESPONSE
```json
{
    "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
    "first_name": "test_4_new",
    "id": 4,
    "second_name": "test_4_new",
    "updated_at": "Tue, 14 Dec 2021 21:02:05 GMT"
}
```

DELETE http://127.0.0.1:5000/api/v1/drivers/driver/4/

Removes the driver (id=4) and returns success json

RESPONSE
```json
{
  "response": "Success"
}
```


### Vehicles endpoint

GET http://127.0.0.1:5000/api/v1/vehicles/vehicle/

RESPONSE
```json
{
  "vehicles": [
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "driver_id": null,
      "id": 1,
      "make": "test_1_make",
      "model": "test_1_model",
      "plate_number": "AA 1111 AA",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "driver_id": 2,
      "id": 2,
      "make": "test_1_make",
      "model": "test_2_model",
      "plate_number": "AA 1111 BB",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "driver_id": null,
      "id": 3,
      "make": "test_1_make",
      "model": "test_1_model",
      "plate_number": "AA 1111 CC",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    }
  ]
}
```

GET http://127.0.0.1:5000/api/v1/vehicles/vehicle/?with_drivers=yes

Returns vehicles with a driver

RESPONSE
```json
{
  "vehicles": [
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "driver_id": 2,
      "id": 2,
      "make": "test_1_make",
      "model": "test_2_model",
      "plate_number": "AA 1111 BB",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    }
  ]
}
```

GET http://127.0.0.1:5000/api/v1/vehicles/vehicle/?with_drivers=no

Returns vehicles without a driver

RESPONSE
```json
{
  "vehicles": [
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "driver_id": null,
      "id": 1,
      "make": "test_1_make",
      "model": "test_1_model",
      "plate_number": "AA 1111 AA",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    },
    {
      "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
      "driver_id": null,
      "id": 3,
      "make": "test_1_make",
      "model": "test_1_model",
      "plate_number": "AA 1111 CC",
      "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
    }
  ]
}
```

GET http://127.0.0.1:5000/api/v1/vehicles/vehicle/1/

Returns the vehicle by id (1)

RESPONSE
```json
{
    "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
    "driver_id": null,
    "id": 1,
    "make": "test_1_make",
    "model": "test_1_model",
    "plate_number": "AA 1111 AA",
    "updated_at": "Tue, 14 Dec 2021 18:19:48 GMT"
}
```

POST http://127.0.0.1:5000/api/v1/vehicles/vehicle/

Creates new Vehicle and returns it

REQUEST
```json
{   
    "make": "test_3_make",
    "model": "test_3_model",
    "plate_number": "XX 0000 XX"
}
```

RESPONSE
```json
{
    "created_at": "Tue, 14 Dec 2021 20:19:48 GMT",
    "driver_id": null,
    "id": 4,
    "make": "test_3_make",
    "model": "test_3_model",
    "plate_number": "XX 0000 XX",
    "updated_at": "Tue, 14 Dec 2021 20:19:48 GMT"
}
```

PUT http://127.0.0.1:5000/api/v1/vehicles/vehicle/4/

Updates the Vehicle with id=4

REQUEST
```json
{   
    "make": "test_3_new_make",
    "model": "test_3_new_model",
    "plate_number": "XX 0000 XX"
}
```

RESPONSE
```json
{
    "created_at": "Tue, 14 Dec 2021 20:19:48 GMT",
    "driver_id": null,
    "id": 4,
    "make": "test_3_new_make",
    "model": "test_3_new_model",
    "plate_number": "XX 0000 XX",
    "updated_at": "Tue, 14 Dec 2021 20:29:48 GMT"
}
```

POST http://127.0.0.1:5000/api/v1/vehicles/set_driver/4/

Adds the driver (json request) to the vehichle if empty,
otherwise removes the driver from the vehicle.
Returns the vehicle.
Returns 405 method not allowed json if the driver (json request) 
is not current driver of the vehicle.

REQUEST
```json
{   
    "id": 3,
    "first_name": "test_3_name",
    "second_name": "test_3_sname"
}
```

RESPONSE
```json
{
    "error": "method not allowed"
}
```

REQUEST
```json
{   
    "id": 2,
    "first_name": "test_2",
    "second_name": "test_2_sname"
}
```

RESPONSE
```json
{
    "created_at": "Tue, 14 Dec 2021 18:19:48 GMT",
    "driver_id": null,
    "id": 2,
    "make": "test_1_make",
    "model": "test_2_model",
    "plate_number": "AA 1111 BB",
    "updated_at": "Tue, 14 Dec 2021 20:49:48 GMT"
}
```

DELETE http://127.0.0.1:5000/api/v1/vehicles/vehicle/4/

Removes the vehicle (id=4) and returns success json

RESPONSE
```json
{   
  "response": "Success"
}
```