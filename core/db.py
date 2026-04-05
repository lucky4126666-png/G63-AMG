import psycopg2
from core.config import DATABASE_URL

conn = psycopg2.connect(DATABASE_URL)

def init_db():
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id BIGINT PRIMARY KEY,
        usage INT DEFAULT 0
    )
    """)
    conn.commit()

def add_user(uid):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (id) VALUES (%s) ON CONFLICT DO NOTHING", (uid,))
    conn.commit()
