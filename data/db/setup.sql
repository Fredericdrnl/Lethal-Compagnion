CREATE TABLE Monsters(
    id_monster SERIAL PRIMARY KEY,
    name_monster VARCHAR(50),
    entry_monster VARCHAR(500),
    particularity VARCHAR(500),
    strategy VARCHAR(500)
)

CREATE TABLE Scrap(
    id_scrap SERIAL PRIMARY KEY,
    name_scrap VARCHAR(500),
    entry_scrap VARCHAR(500),
    cost_scrap INTEGER,
    weight INTEGER,
)

CREATE TABLE Moons(
    id_moon SERIAL PRIMARY KEY,
    name_moon VARCHAR(500),
    difficulty VARCHAR(500),
    cost_moon INTEGER,
    weather VARCHAR(500),
    default_layout VARCHAR(500),
    min_scrap INTEGER,
    max_scrap INTEGER
)

CREATE TABLE Store(
    id_store SERIAL PRIMARY KEY,
    name_store VARCHAR(500),
    entry_store VARCHAR(500),
    cost_store INTEGER,
    weight_store INTEGER,
    conductive_store VARCHAR(500),
    battery_store VARCHAR(500),
)