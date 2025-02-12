from flask import Blueprint, jsonify, request
from business.exceptions import InvalidUserException, UserNotFoundException

from business.user_service import UserService
from presentation.user_handler import UserHandler


controller = Blueprint("controller", __name__)

user_service = UserService()
user_handeler = UserHandler(user_service)

@controller.route("/")
def hello_world():
    return "I am OK!"

@controller.route("/user", methods = ['POST'])
def user():
    incoming_data = request.get_json(force=True)
    print(incoming_data)
    try:
        user_data = user_handeler.create_user(incoming_data)
    except InvalidUserException:
        return jsonify({"message": "Invalid user data"}), 400
    return jsonify(user_data)

@controller.route("/user/<user_id>")
def get_user(user_id):
    try:
        user_data = user_handeler.get_user(user_id)
    except UserNotFoundException:
        return jsonify({"message": "User not found", "user_id": user_id}), 404
    return jsonify(user_data)
    