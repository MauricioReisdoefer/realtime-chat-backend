from app import db
from models.user_model import User
from flask import request

def create_user():
    data = request.get_json()
    user = User(
        name=data.get('name'),
        password=data.get('password')
    )
    db.session.add(user)
    db.session.commit()
    return {
        'message': 'User criado com sucesso',
        'data': user.toMap()
    }, 201
    