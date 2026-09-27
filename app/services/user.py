import db


def get_all_users():
    users = db.cur.execute("SELECT * FROM user").fetchall()
    return [dict(user) for user in users]

def get_user_by_id(user_id: int):
    user = db.cur.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
    return dict(user)