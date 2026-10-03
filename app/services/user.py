import db
from werkzeug.security import generate_password_hash


def get_all_users(args):
    users_query = db.cur.execute("SELECT id, username FROM user").fetchall()
    users = [dict(user) for user in users_query]

    for param in args:
        if param in ['id', 'username']:
            users = [dict(user) for user in users if str(user[param]) == args.get(param)]
    return users


def get_user_by_id(user_id: int):
    user = db.cur.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
    return dict(user)

def create_user(username: str, password: str):
    password_hash = generate_password_hash(password)
    user = db.cur.execute("INSERT INTO user(username, password) VALUES (?, ?)", (username, password_hash))
    db.con.commit()
    return {"username": username}
