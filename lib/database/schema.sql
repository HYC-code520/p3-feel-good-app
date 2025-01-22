CREATE TABLE IF NOT EXISTS mood_logs (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    mood TEXT NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS motivational_quotes (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL,
    category TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS animal_inspirations (
    id INTEGER PRIMARY KEY,
    story TEXT NOT NULL,
    animal_type TEXT
);
