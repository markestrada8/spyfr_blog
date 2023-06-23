from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from extensions import db
from config import DevConfig, TestConfig
from models import Blog, User
from auth import auth_ns
from blog import blog_ns

def create_app(config):

    app = Flask(__name__)

    app.config.from_object(config)
    if config != TestConfig:
        db.init_app(app)

    CORS(app)

    migrate = Migrate(app, db)
    JWTManager(app)

    api = Api(app, doc='/docs')

    # INCORPORATE ROUTE/CONTROLLERS
    api.add_namespace(blog_ns)
    api.add_namespace(auth_ns)

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "Blog": Blog, "User": User}

    return app