from flask import Blueprint

import app.controllers.auth as controller

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    return controller.login()