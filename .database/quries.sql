--CREATE TABLE User(fristname TEXT NOT NULL,
                  username TEXT NOT NULL UNIQUE,
                  lastname TEXT NOT NULL,
                  email TEXT NOT NULL,
                  password TEXT NOT NULL);

CREATE TABLE Media (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    releasedate TEXT,
                    summary BLOB,
                    genre TEXT,
                    game INTEGER NOT NULL CHECK (game >= 0 AND game <= 1));

CREATE TABLE Review (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    rating INTEGER NOT NULL CHECK (rating >= 0 AND rating <= 10),
                    username TEXT NOT NULL,
                    media_id INTEGER NOT NULL,
                    comment BLOB,
                    FOREIGN KEY (username) REFERENCES User(username),
                    FOREIGN KEY (media_id) REFERENCES Media(id));

