from http import HTTPStatus

from flask import jsonify, request
import app.services.user as service


def get_all_users():
    try:
        return jsonify(service.get_all_users()), HTTPStatus.OK
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

def get_user_by_id(user_id):
    try:
        return jsonify(service.get_user_by_id(user_id)), HTTPStatus.OK
    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR