CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    subscription TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
