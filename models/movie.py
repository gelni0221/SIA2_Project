import sqlite3

def get_next_movie(movie_id):
    conn = sqlite3.connect('db/content.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movie WHERE id > ? ORDER BY id ASC LIMIT 1", (movie_id,))
    row = c.fetchone()
    if row:
        return {
            "id": row[0],
            "title": row[1],
            "date": row[2],
            "rating": row[3],
            "duration": row[4],
            "description": row[5],
            "director": row[6],
            "writer": row[7],
            "actor": row[8],
            "genre": row[9],
            "poster": row[10],
            "video": row[11],
        }
    else:
        return False


def get_prev_movie(movie_id):
    conn = sqlite3.connect('db/content.db')
    c = conn.cursor()
    c.execute("SELECT * FROM movie WHERE id < ? ORDER BY id DESC LIMIT 1", (movie_id,))
    row = c.fetchone()
    if not row:
        c.execute("SELECT * FROM movie ORDER BY id DESC LIMIT 1")
        row = c.fetchone()
        return {
            "id": row[0],
            "title": row[1],
            "date": row[2],
            "rating": row[3],
            "duration": row[4],
            "description": row[5],
            "director": row[6],
            "writer": row[7],
            "actor": row[8],
            "genre": row[9],
            "poster": row[10],
            "video": row[11],
        }
    else:
        return {
            "id": row[0],
            "title": row[1],
            "date": row[2],
            "rating": row[3],
            "duration": row[4],
            "description": row[5],
            "director": row[6],
            "writer": row[7],
            "actor": row[8],
            "genre": row[9],
            "poster": row[10],
            "video": row[11],
        }

