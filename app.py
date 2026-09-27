from datetime import timedelta

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
import db

from app.routes.user import user_bp
from app.routes.auth import auth_bp

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "cacapipi"
app.config["JWT_ALGORITHM"] = "HS256"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)

app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api/health')
def testdb():
    users = db.cur.execute("SELECT * FROM user;").fetchall()
    return jsonify([dict(user) for user in users])


if __name__ == '__main__':
    app.run()
