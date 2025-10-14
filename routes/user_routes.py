from flask import Blueprint, jsonify
from controller.user_controller import create_user as create_user_func, get_all, filter_by_id, login

user_bp = Blueprint("user", import_name="user", url_prefix="/user")

@user_bp.route('/create', methods=['POST'])
def create_user():
    return create_user_func()

@user_bp.route('/all', methods=['GET'])
def get_users():
    users = get_all()
    data = [{"id": u.id, "username": u.username} for u in users]
    return jsonify(data), 200

@user_bp.route('/filter/<string:username>', methods=['GET'])
def get_by_name(username):
    users = filter_by_id(username)
    data = [{"id": u.id, "username": u.username} for u in users]
    return jsonify(data), 200

@user_bp.route('/login', methods=['POST'])
def login_user():
    return login()