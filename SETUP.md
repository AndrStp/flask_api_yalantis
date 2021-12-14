# SETUP INSTRUCTIONS

## Prerequisites

1. python version >= 3.9 
2. venv (optional)
3. Linux/Mac OS (Windows not tested)
4. curl / httpie / postman / IDE extension - to send requests to server


## Instructions

1. $ `mkdir app && cd app`
2. $ `git clone <current_repo>`
3. $ `python3 -m venv env`
4. $ `source env/bin/activate`
5. $ `python -m pip install -r requirements.txt`
6. $ `mv flask.env.example .env` (see flask.env.example for additional instructions)
7. $ `flask db init` (make initial migration)
8. $ `flask db migrate`
9. $ `flask db upgrade`
10. $ `python run.py` - runs the server

Server should run on http://127.0.0.1:5000/