from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restx import Api, Resource, fields, Namespace
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required

from exts import db
from models import User

# ESTABLISH AUTHENTICATION NAMESPACE
auth = Namespace('auth', description='Namespace for authentication')

user_model = auth.model(
    "User",
    {
        "id": fields.Integer(),
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
    }
)

login_model = auth.model(
    "Login",
    {
        "username": fields.String(),
        "email": fields.String(),
    }
)

auth_response = auth.model(
    "Auth Response",
    {
        "message": fields.String(),
        "access_token": fields.String(default=None),
        "refresh_token": fields.String(default=None),
    }
)

@auth.route('/signup')
class SignUp(Resource):
    @api.expect(user_model)
    @api.marshal_with(auth_response)
    def post(self):
        '''ADD NEW USER'''
        data = request.get_json()
        username = data.get('username'),
        email = data.get('email'),
        password = generate_password_hash((data.get('password')))

        # CHECK USER
        email = data.get('email')
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"message": f"User {email} already exists"}, 409

        new_user = User(
            username = username,
            email = email,
            password = password
        )
        new_user.add()
        return {"message": f"User {email} created successfully"}, 201

@auth.route('/login')
class Login(Resource):
    @api.expect(login_model)
    @api.marshal_with(auth_response, skip_none=True)
    def post(self):
        '''LOGIN USER'''
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user == None:
            return {"message": f"User {email} has not been created"}, 404

        if (check_password_hash(existing_user.password, password)):
            acccess_token = create_access_token(identity=existing_user.email)
            refresh_token = create_access_token(identity=existing_user.email)
            return {
                "message": f"User {email} has been logged in successfully",
                "access_token": acccess_token,
                "refresh_token": refresh_token
                }, 200
        else:
            return {"message": f"Incorrect password for user {email}"}, 403

        return {"message": "Error occured during login"}, 500

