import json
import sqlite3
import argon2

# conn = sqlite3.connect('account.db')
conn = sqlite3.connect('content.db')


c = conn.cursor()

# Create table
c.execute(""" CREATE TABLE IF NOT EXISTS movie (
            id INTEGER PRIMARY KEY,
            title TEXT,
            date INT,
            rating int,
            duration int,
            description text,
            director text,
            writer text,
            actor text,
            genre text,
            poster text,
            video text
                )
            """)

# Reset
# c.execute("DROP TABLE IF EXISTS movie")

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
# add movie
movie_details = {
     "title": "The SpongeBob SquarePants Movie",
    "year": 2004,
    "rating": 7.1,
    "duration_mins": 87,
    "description": "SpongeBob and Patrick embark on an adventure to retrieve King Neptune's stolen crown and save Mr. Krabs from execution.",
    "directors": ["Stephen Hillenburg", "Mark Osborne"],
    "writers": ["Stephen Hillenburg", "Derek Drymon", "Tim Hill", "Kent Osborne", "Aaron Springer", "Paul Tibbitt"],
    "actors": [
        "Tom Kenny", "Bill Fagerbakke", "Clancy Brown",
        "Rodger Bumpass", "Scarlett Johansson", "Jeffrey Tambor"
    ],
    "genre": ["Animation", "Adventure", "Comedy", "Family"],
    "poster": "spongebob.jpg",
    "video": "Spongebob.mp4"
}

c.execute("INSERT INTO movie (title, date, rating, duration, description, director, writer, actor, genre,poster,video) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
          (
        movie_details["title"],
        movie_details["year"],
        movie_details["rating"],
        movie_details["duration_mins"],
        movie_details["description"],
        json.dumps(movie_details["directors"]),
        json.dumps(movie_details["writers"]),
        json.dumps(movie_details["actors"]),
        json.dumps(movie_details["genre"]),
        movie_details["poster"],
        movie_details["video"]))

# c.execute("DELETE FROM movie WHERE id = ?", (2,))
conn.commit() # for add and delete to actually take persistent effect

# c.execute("SELECT * FROM account")
# print(c.fetchall())
try:
    c.execute("SELECT * FROM movie")
except:
    print("no table found")
for row in c.fetchall():
    print(row)

conn.close()