from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restx import Api, Resource, fields
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required

from exts import db
from config import DevConfig
from models import Blog, User

app = Flask(__name__)

app.config.from_object(DevConfig())

db.init_app(app)

migrate = Migrate(app, db)
JWTManager(app)

api = Api(app, doc='/docs')


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Blog": Blog, "User": User}

if __name__ == '__main__':
    app.run()