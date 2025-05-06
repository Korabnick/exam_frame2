from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.models import db, User, Role
from app.schemas import UserSchema, UserCreateSchema, UserLoginSchema
from app.utils.decorators import admin_required

api_bp = Blueprint('api', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_create_schema = UserCreateSchema()
user_login_schema = UserLoginSchema()

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    errors = user_login_schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
        
    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
        
    access_token = create_access_token(
        identity=user.username,
        additional_claims={'is_admin': user.is_admin}
    )
    return jsonify({'access_token': access_token}), 200

@api_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200

@api_bp.route('/users', methods=['POST'])
@admin_required
def create_user():
    data = request.get_json()
    errors = user_create_schema.validate(data)
    if errors:
        return jsonify({'errors': errors}), 400
        
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
        
    user_role = Role.query.filter_by(name='user').first()
    new_user = User(
        username=data['username'],
        email=data['email'],
        role_id=user_role.id
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(user_schema.dump(new_user)), 201