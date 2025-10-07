import sqlite3
# import argon2

conn = sqlite3.connect('db/account.db')
c = conn.cursor()

# FINISHED
# c.execute(""" CREATE TABLE account(
#             id int,
#             username text,
#             password text
#                 )
#             """)

# password = "thispassworldwillbehashed"

# ph = argon2.PasswordHasher()
# hashed_password = ph.hash(password)

# print(hashed_password)

# c.execute("INSERT INTO account VALUES (:id, :username, :password)",
# {'id': 2, 'username': "tkinteraccount", 'password': hashed_password})
#
# conn.commit()

c.execute("SELECT * FROM account")
print(c.fetchall())

conn.close()