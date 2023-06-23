from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restx import Resource, fields, Namespace, marshal
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, jwt_required

from models import User

# ESTABLISH AUTHENTICATION NAMESPACE
auth_ns = Namespace('auth', description='Namespace for authentication')

# MODEL SERIALIZER (INTERFACE FOR REQUEST / RESPONSE - NOT STRICTLY ENFORCED)
user_model = auth_ns.model(
    "User",
    {
        "id": fields.Integer(),
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
    }
)

login_model = auth_ns.model(
    "Login",
    {
        "username": fields.String(),
        "email": fields.String(),
    }
)

auth_response = auth_ns.model(
    "Auth Response",
    {
        "message": fields.String(),
        "access_token": fields.String(default=None),
        "refresh_token": fields.String(default=None),
    }
)

@auth_ns.route('/signup')
class SignUp(Resource):
    @auth_ns.expect(user_model)
    @auth_ns.marshal_with(auth_response)
    def post(self):
        '''ADD NEW USER'''
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = generate_password_hash((data.get('password')))

        # CHECK USER
        email = data.get('email')
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"message": f"User {email} already exists"}, 409

        new_user = User(
            username=username,
            email=email,
            password=password
        )
        new_user.add()
        return marshal({"message": f"User {email} created successfully"}, auth_response), 201

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    @auth_ns.marshal_with(auth_response, skip_none=True)
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
            refresh_token = create_refresh_token(identity=existing_user.email)
            return marshal({
                "message": f"User {email} has been logged in successfully",
                "access_token": acccess_token,
                "refresh_token": refresh_token
                }, auth_response), 200
        else:
            return {"message": f"Incorrect password for user {email}"}, 403

        return {"message": "Error occured during login"}, 500

@auth_ns.route('/refresh')
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        '''REFRESH JWT'''
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return make_response(jsonify({'access_token': new_access_token}), 200)