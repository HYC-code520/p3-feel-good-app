from colorama import init, Fore, Style
import sqlite3
import os

def get_random_animal_story_by_type(animal_type):
    """Retrieve a random animal story for the specified type."""
    # Dynamically calculate the absolute path to the database
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "mood_journal.db")
    # print("Attempting to connect to:", db_path)  # Debug the database path

    try:
        with sqlite3.connect(db_path) as con:
            sql = "SELECT story FROM animal_inspirations WHERE LOWER(animal_type) = ? ORDER BY RANDOM() LIMIT 1"
            cursor = con.cursor()
            cursor.execute(sql, (animal_type.lower(),))  # Match animal type in lowercase
            story = cursor.fetchone()
            return story[0] if story else None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
