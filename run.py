from os import getenv
from dotenv import load_dotenv
from app import create_app


if __name__ == '__main__':
    load_dotenv()
    app = create_app(getenv('FLASK_CONFIG', 'default'))
    app.run()