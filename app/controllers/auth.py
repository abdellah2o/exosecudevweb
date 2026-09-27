from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token

from flask import request, jsonify
import app.services.auth as service


def login():
    data = request.get_json()

    try:
        user = service.login(
            data.get("username"),
            data.get("password")
        )

        if user is None:
            return jsonify({
                "message": "Username ou mot de passe incorrect"
            }), HTTPStatus.UNAUTHORIZED

        access = create_access_token(
            identity=str(user['id']),
            additional_claims={
                'username': user['username']
            }
        )
        refresh = create_refresh_token(identity=str(user['id']))

        return jsonify({
            "user": user,
            "access": access,
            "refresh": refresh
        }), HTTPStatus.OK

    except Exception as e:
        return jsonify({
            "message": str(e)
        }), HTTPStatus.INTERNAL_SERVER_ERROR