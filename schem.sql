CREATE TABLE IF NOT EXISTS items (
    id integer PRIMARY KEY,
    name char(150) NOT NULL,
    folder_id integer,
    is_weighted boolean,
    description text
);