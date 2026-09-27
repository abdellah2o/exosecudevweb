from flask import Blueprint
from flask_jwt_extended import jwt_required

import app.controllers.user as controller

user_bp = Blueprint("user", __name__)

@user_bp.route("/api/users", methods=["GET"])
@jwt_required()
def get_all_users():
    return controller.get_all_users()

@user_bp.route("/api/users/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user_by_id(user_id: int):
    return controller.get_user_by_id(user_id)