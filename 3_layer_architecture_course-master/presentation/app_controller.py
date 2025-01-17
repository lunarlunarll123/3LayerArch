from flask import Flask, jsonify, request
from business.exceptions import InvalidUserException, UserNotFoundException
from business.user_service import UserService
from business.user_servicehandler import UserServiceHandler

def create_app():
    app = Flask(__name__)
    user_service = UserService()
    user_servicehandeler = UserServiceHandler(user_service)

    @app.route("/")
    def hello_world():
        return "I am OK!"

    @app.route("/user", methods=['POST'])
    def user():
        incoming_data = request.get_json(force=True)
        print(incoming_data)
        try:
            user_data = user_servicehandeler.create_user(incoming_data)
        except InvalidUserException:
            return jsonify({"message": "Invalid user data"}), 400
        return jsonify(user_data)

    @app.route("/user/<user_id>")
    def get_user(user_id):
        try:
            user_data = user_servicehandeler.get_user(user_id)
        except UserNotFoundException:
            return jsonify({"message": "User not found", "user_id": user_id}), 404
        return jsonify(user_data)

    return app