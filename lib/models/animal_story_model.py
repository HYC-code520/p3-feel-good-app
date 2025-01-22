import sqlite3
import os

def get_random_animal_story():
    # Dynamically calculate the absolute path to the database
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "mood_journal.db")
    print("Attempting to connect to:", db_path)  # Debug the database path

    try:
        # Connect to the database using the absolute path
        with sqlite3.connect(db_path) as con:
            sql = "SELECT story FROM animal_inspirations ORDER BY RANDOM() LIMIT 1"
            cursor = con.cursor()
            cursor.execute(sql)
            story = cursor.fetchone()
            return story[0] if story else "No inspiring animal stories found."
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return "An error occurred while retrieving an animal story."
