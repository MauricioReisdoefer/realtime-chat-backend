from models.message_model import Message
from flask import request
from database import db

def create_message():
    data = request.get_json()
    message = Message(
        content=data.get('content')
    )
    db.session.add(message)
    db.session.commit()
    return {
        'message': 'Message criado com sucesso',
        'data': message.toMap()
    }, 200
    
def get_all():
    return Message.query.all()