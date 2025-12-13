from expense_tracker import db

def test_init_db():
    db.init_db()
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='expenses'")
    assert cur.fetchone() is not None
    conn.close()
