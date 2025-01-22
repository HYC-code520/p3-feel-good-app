import sqlite3

def get_random_animal_story():
    sql = "SELECT story FROM animal_inspirations ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect("../database/mood_journal.db") as con:
        cursor = con.cursor()
        cursor.execute(sql)
        story = cursor.fetchone()
    return story[0] if story else "No inspiring animal stories found."
