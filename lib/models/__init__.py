import sqlite3

def initialize_database():
    """Initialize the database using schema.sql."""
    print("Initializing database...")
    with sqlite3.connect("../database/mood_journal.db") as con:
        with open("../database/schema.sql", "r") as f:
            print("Executing schema.sql...")
            con.executescript(f.read())
    print("Database initialized successfully.")
