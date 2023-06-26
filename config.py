from decouple import config
import os

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///dev.db")
    DEBUG=True
    SQLALCHEMY_ECHO=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///dev.db"
    DEBUG = config("DEBUG", cast=bool)
    SQLALCHEMY_ECHO = config("ECHO", cast=bool)
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool)

class TestConfig(Config):
    # ALSO NEED TO SET AUTH CREDENTIALS SETTINGS PROBABLY
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_ECHO=False
    TESTING=True