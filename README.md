# Flask-RESTful API project template

This project shows one of the possible ways to implement RESTful API server.

There are implemented two models: Driver and Vehicle, one Driver has many Vehicles.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-RESTful - restful API library.
3. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

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
│   ├── test
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
### Users endpoint
POST http://127.0.0.1:5000/api/v1/users


+++++++++++++++++++++++++++++++++++++++++++++++++ !!!


REQUEST
```json
{
	"name": "John John"
}
```
RESPONSE
```json
{
    "id": 1,
    "name": "John John",
    "todos": []
}
```
PUT http://127.0.0.1:5000/api/users/1

REQUEST
```json
{
	"name": "Smith Smith"
}
```
RESPONSE
```json
{
    "id": 1,
    "name": "Smith Smith",
    "todos": []
}
```
DELETE http://127.0.0.1:5000/api/users/1

RESPONSE
```json
{
    "id": 3,
    "name": "Tom Tom",
    "todos": []
}
```
GET http://127.0.0.1:5000/api/users

RESPONSE
```json
{
    "count": 2,
    "users": [
        {
            "id": 1,
            "name": "John John",
            "todos": [
                {
                    "id": 1,
                    "name": "First task",
                    "description": "First task description"
                },
                {
                    "id": 2,
                    "name": "Second task",
                    "description": "Second task description"
                }
            ]
        },
        {
            "id": 2,
            "name": "Smith Smith",
            "todos": []
        }
    ]
}
```
GET http://127.0.0.1:5000/api/users/2
```json
{
    "id": 2,
    "name": "Smith Smith",
    "todos": []
}
```
GET http://127.0.0.1:5000/api/users?name=John John
```json
{
    "count": 1,
    "users": [
        {
            "id": 1,
            "name": "John John",
            "todos": [
                {
                    "id": 1,
                    "name": "First task",
                    "description": "First task description"
                },
                {
                    "id": 2,
                    "name": "Second task",
                    "description": "Second task description"
                }
            ]
        }
    ]
}
```
GET http://127.0.0.1:5000/api/users?limit=1&offset=1
```json
{
    "count": 1,
    "users": [
        {
            "id": 2,
            "name": "Smith Smith",
            "todos": []
        }
    ]
}
```

Todo endpoint is similar to Users endpoint.