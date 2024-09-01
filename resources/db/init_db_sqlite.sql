DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS statuses;
DROP TABLE IF EXISTS sessions;

DROP INDEX IF EXISTS users_username_idx;
DROP INDEX IF EXISTS statuses_user_id_created_at_idx;

CREATE TABLE users
(
    id         INTEGER                            NOT NULL,
    user_id    INTEGER UNIQUE                     NOT NULL,
    username   TEXT,
    first_name TEXT,
    last_name  TEXT,
    name       TEXT,
    gender     TEXT(1) COLLATE NOCASE CHECK ( gender IN ('м', 'ж') ),
    age        INTEGER CHECK (age >= 5 AND age <= 150),
    created_at DATETIME DEFAULT (DATETIME('now')) NOT NULL,
    updated_at DATETIME DEFAULT (DATETIME('now')) NOT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX users_username_idx ON users (username);

CREATE TABLE statuses
(
    id         INTEGER                                    NOT NULL,
    text       TEXT,
    grade      INTEGER CHECK (grade >= -5 AND grade <= 5) NOT NULL,
    created_at DATETIME DEFAULT (DATETIME('now'))         NOT NULL,
    updated_at DATETIME DEFAULT (DATETIME('now'))         NOT NULL,
    user_id    INTEGER                                    NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE UNIQUE INDEX statuses_user_id_created_at_idx ON statuses (user_id, created_at);

CREATE TABLE sessions

(
    id         INTEGER                            NOT NULL,
    review     TEXT,
    created_at DATETIME DEFAULT (DATETIME('now')) NOT NULL,
    updated_at DATETIME DEFAULT (DATETIME('now')) NOT NULL,
    user_id    INTEGER                            NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE

);

CREATE UNIQUE INDEX sessions_created_at_user_id_idx ON statuses (user_id, created_at);