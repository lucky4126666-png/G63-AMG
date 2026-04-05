import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)

def init():
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY,
        user TEXT,
        text TEXT
    )
    """)
    conn.commit()

def save(user, text):
    c = conn.cursor()
    c.execute("INSERT INTO logs (user, text) VALUES (?, ?)", (user, text))
    conn.commit()
