import db
from werkzeug.security import check_password_hash


def login(username: str, password: str):
    user = db.cur.execute("SELECT * FROM user WHERE username=?;", (username,)).fetchone()

    if user is None:
        return None

    if not check_password_hash(user["password"], password):
        return None

    return dict(user)