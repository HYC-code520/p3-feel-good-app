import sqlite3
import os

def log_mood_to_db(mood, notes):
    # Calculate and print the database path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "mood_journal.db")
    print("Attempting to connect to:", db_path)  # Debug the path

    # Use the absolute path to connect
    with sqlite3.connect(db_path) as con:
        sql = "INSERT INTO mood_logs (timestamp, mood, notes) VALUES (DATETIME('now'), ?, ?)"
        cursor = con.cursor()
        cursor.execute(sql, (mood, notes))
        con.commit()
    print("Mood logged!")

def view_mood_history():
    db_path = "../database/mood_journal.db"
    with sqlite3.connect(db_path) as con:
        sql = "SELECT timestamp, mood, notes FROM mood_logs ORDER BY timestamp DESC"
        cursor = con.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

