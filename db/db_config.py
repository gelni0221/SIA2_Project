import sqlite3
import argon2

conn = sqlite3.connect('account.db')
c = conn.cursor()

# FINISHED
# c.execute(""" CREATE TABLE account(
#             id int,
#             username text,
#             password text
#                 )
#             """)

# Reset
# c.execute("DROP TABLE account")

# password = "pass"
#
# ph = argon2.PasswordHasher()
# hashed_password = ph.hash(password)
#
# # print(hashed_password)
#
# c.execute("INSERT INTO account VALUES (:id, :username, :password)",
# {'id': 1, 'username': "admin", 'password': hashed_password})
#
# conn.commit()

c.execute("SELECT * FROM account")
print(c.fetchall())

conn.close()