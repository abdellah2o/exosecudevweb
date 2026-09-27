import db


def login(username, password):
    verif = db.cur.execute("SELECT * FROM user WHERE username=? AND password=?;", (username, password)).fetchone()

    if verif is None:
        return None

    return dict(verif)