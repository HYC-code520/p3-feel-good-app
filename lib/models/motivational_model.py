import sqlite3
import os

def get_random_quote():
    # Dynamically calculate the absolute path to the database
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "mood_journal.db")
    print("Attempting to connect to:", db_path)  # Debug the database path

    try:
        # Connect to the database using the absolute path
        with sqlite3.connect(db_path) as con:
            sql = "SELECT text FROM motivational_quotes ORDER BY RANDOM() LIMIT 1"
            cursor = con.cursor()
            cursor.execute(sql)
            quote = cursor.fetchone()
            return quote[0] if quote else "No motivational quotes found."
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return "An error occurred while retrieving a quote."
