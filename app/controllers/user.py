from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity

import app.services.user as service


def get_all_users():
    try:
        return jsonify(service.get_all_users(request.args)), HTTPStatus.OK
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

def get_user_by_id(user_id):
    try:
        if user_id != int(get_jwt_identity()):
            return jsonify({
                "message": "Accès interdit"
            }), HTTPStatus.FORBIDDEN

        user = service.get_user_by_id(user_id)

        if user is None:
            return jsonify({
                "message": "Utilisateur introuvable"
            }), HTTPStatus.NOT_FOUND

        return jsonify(user), HTTPStatus.OK
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

def create_user():
    data = request.get_json()

    try:
        return jsonify(service.create_user(data["username"], data["password"])), HTTPStatus.OK
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR