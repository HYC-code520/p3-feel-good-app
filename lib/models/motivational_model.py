def get_random_quote_by_category(category):
    """Retrieve a random quote from a specific category."""
    import sqlite3
    import os

    # Calculate the database path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "mood_journal.db")
    print("Attempting to connect to:", db_path)  # Debug path

    try:
        with sqlite3.connect(db_path) as con:
            sql = "SELECT text FROM motivational_quotes WHERE LOWER(category) = ? ORDER BY RANDOM() LIMIT 1"
            cursor = con.cursor()
            cursor.execute(sql, (category.lower(),))  # Use lowercase for category matching
            quote = cursor.fetchone()
            return quote[0] if quote else f"Sorry, we couldn't find any {category} quotes right now. Try another!"
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return "An error occurred while retrieving a quote."
