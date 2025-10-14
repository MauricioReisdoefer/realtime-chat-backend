from app import db
from models.user_model import User
from flask import request

def create_user():
    data = request.get_json()
    user = User(username=data.get('username'))
    user.set_password(data.get('password'))  # usa o método certo

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