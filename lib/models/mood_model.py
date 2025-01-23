from colorama import init, Fore, Style
import sqlite3
import os

def log_mood_to_db(general_feeling, mood_description, notes):
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database", "mood_journal.db")
    # print("Attempting to connect to:", db_path)  # Debug the path

    with sqlite3.connect(db_path) as con:
        sql = """
        INSERT INTO mood_logs (timestamp, general_feeling, mood, notes)
        VALUES (DATETIME('now'), ?, ?, ?)
        """
        cursor = con.cursor()
        cursor.execute(sql, (general_feeling, mood_description, notes))
        con.commit()
    # print("Mood logged!")




def view_mood_history():
    import sqlite3
    import os

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "mood_journal.db")

    try:
        with sqlite3.connect(db_path) as con:
            # Convert UTC timestamps to local time when retrieving
            sql = """
            SELECT 
                DATETIME(timestamp, 'localtime') AS local_timestamp, 
                mood, 
                notes 
            FROM mood_logs 
            ORDER BY timestamp ASC
            """
            cursor = con.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
