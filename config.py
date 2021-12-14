from os import environ, path


basedir = path.abspath(path.dirname(__file__))


class BaseConfig:
    """Base configuration class"""

    # Flask-realted config
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = f'sqlite:///' + path.join(basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    """Test configuration class"""
    # Flask-realted config
    FLASK_ENV = 'development'

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = f'sqlite////in_memory' # TODO


class DevelopmentConfig(BaseConfig):
    """Development config class"""
    # Flask-realted config
    FLASK_ENV = 'development'


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    
    'default': DevelopmentConfig,
}
