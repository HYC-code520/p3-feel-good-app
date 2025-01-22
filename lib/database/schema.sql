CREATE TABLE IF NOT EXISTS mood_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, -- Automatically adds the current date and time
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
