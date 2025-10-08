import sqlite3

conn = sqlite3.connect('db/account.db')
c = conn.cursor()

def find_user_by_username(username):
    c.execute("SELECT * FROM account WHERE username = (:username)",{'username': username})
    row = c.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "username": row[1], "password_hash": row[2]}

