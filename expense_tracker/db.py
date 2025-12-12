
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "expenses.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        amount REAL NOT NULL CHECK (amount > 0),
        category TEXT NOT NULL,
        notes TEXT,
        created_at TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    init_db()
    print("Database Initialized")