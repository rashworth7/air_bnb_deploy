-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

DROP TABLE IF EXISTS landlords;
DROP SEQUENCE IF EXISTS landlords_id_seq;

DROP TABLE IF EXISTS tenants;
DROP SEQUENCE IF EXISTS tenants_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS landlords_id_seq;
CREATE TABLE landlords (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS tenants_id_seq;
CREATE TABLE tenants (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    title INT,
    description VARCHAR(255),
    price_per_night INT,
    availability_dates DATE,
    landlord_id INT,
    CONSTRAINT fk_landlord_id foreign key(landlord_id) 
    REFERENCES landlords(id)
    ON DELETE cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    space_id INT,
    date DATE,
    tenant_id INT,
    landlord_id INT,
    status VARCHAR(255),
    CONSTRAINT fk_space_id foreign key(space_id) 
    REFERENCES spaces(id)
    ON DELETE cascade,
    CONSTRAINT fk_tenant_id foreign key(tenant_id) 
    REFERENCES tenants(id)
    ON DELETE cascade,
    CONSTRAINT fk_landlord_id foreign key(landlord_id) 
    REFERENCES landlords(id)
    ON DELETE cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO landlords (username) VALUES ('Charlotte');
INSERT INTO landlords (username) VALUES ('Oli');
INSERT INTO landlords (username) VALUES ('Nebiat');
INSERT INTO landlords (username) VALUES ('Rich');
INSERT INTO tenants (username) VALUES ('Charlotte');
INSERT INTO tenants (username) VALUES ('Oli');
INSERT INTO tenants (username) VALUES ('Nebiat');
INSERT INTO tenants (username) VALUES ('Rich');
