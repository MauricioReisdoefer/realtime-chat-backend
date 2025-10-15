from flask import Blueprint, jsonify
from controller.message_controller import create_message, get_all
from models.message_model import Message
from models.user_model import User

message_bp = Blueprint("message", import_name="message", url_prefix="/msg")

@message_bp.route("/")
def get_all_messages():
    messages = get_all()
    data = []

    for m in messages:
        user = User.query.filter_by(id=m.user_id).first()
        username = user.username if user else "Unknown"
        data.append({
            "username": username,
            "message": m.content
        })

    return jsonify(data), 200

@message_bp.route("/add")
def create_new_message():
    return create_message()
