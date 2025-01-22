import sqlite3

def get_random_quote():
    sql = "SELECT text FROM motivational_quotes ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect("../database/mood_journal.db") as con:
        cursor = con.cursor()
        cursor.execute(sql)
        quote = cursor.fetchone()
    return quote[0] if quote else "No motivational quotes found."
