from database import db
from models.user_model import User
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta

def create_user():
    data = request.get_json()
    user = User(username=data.get('username'), email=data.get('email'))
    user.set_password(data.get('password'))

    db.session.add(user)
    db.session.commit()

    return {
        'message': 'User criado',
        'data': {
            'id': user.id,
            'username': user.username
        }
    }, 201

def get_all():
    return User.query.all()

def filter_by_id(name):
    filtered = User.query.filter(User.name == name).all()
    return filtered

def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user : User = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Credenciais inválidas'}), 401

    access_token = create_access_token(
        identity=user.id,
        expires_delta=timedelta(hours=1)
    )

    return jsonify({
        'access_token': access_token,
        'user': {
            'id': user.id,
            'username': user.username
        }
    }), 200