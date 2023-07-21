-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS bookings cascade;
DROP SEQUENCE IF EXISTS bookings_id_seq;

-- DROP TABLE IF EXISTS availability_of_spaces;
-- DROP SEQUENCE IF EXISTS availability_of_spaces_id_seq;

DROP TABLE IF EXISTS availability cascade;
DROP SEQUENCE IF EXISTS availability_id_seq;

DROP TABLE IF EXISTS spaces cascade;
DROP SEQUENCE IF EXISTS spaces_id_seq;

DROP TABLE IF EXISTS landlords cascade;
DROP SEQUENCE IF EXISTS landlords_id_seq;

DROP TABLE IF EXISTS tenants cascade;
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
    title VARCHAR(255),
    description VARCHAR(255),
    price_per_night INT,
    landlord_id INT,
    CONSTRAINT fk_landlord_id foreign key(landlord_id) 
    REFERENCES landlords(id)
    ON DELETE cascade
);

CREATE SEQUENCE IF NOT EXISTS availability_id_seq;
CREATE TABLE availability (
    id SERIAL PRIMARY KEY,
    space_id INT,
    date date,
    CONSTRAINT fk_space_id foreign key(space_id) 
    REFERENCES spaces(id)
    ON DELETE cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    space_id INT,
    space_title TEXT,
    tenant_id INT,
    landlord_id INT,
    date DATE,
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

INSERT INTO spaces 
(title, description, price_per_night, landlord_id)
VALUES
('Space 1', 'Space 1 is very nice', 50, 1),
('Space 2', 'Space 2 is cool', 60, 1),
('Space 3', 'Space 3 rubbish', 20, 2)
;

INSERT INTO availability
(space_id, date)
VALUES
(1, '2023-07-18'),
(1, '2023-07-19'),
(1, '2023-07-20'),
(2, '2023-07-21'),
(2, '2023-07-22'),
(2, '2023-07-23'),
(3, '2023-07-24')
;

INSERT INTO bookings 
(space_id, space_title, tenant_id, landlord_id, date, status)
VALUES
(1, 'Space 1', 1, 1, '2023-07-18', 'pending'),
(1, 'Space 1', 1, 1, '2023-07-20', 'pending'),
(1, 'Space 1', 1, 1, '2023-07-17', 'approved'),
(2, 'Space 2', 2, 1, '2023-07-18', 'pending'),
(3, 'Space 3', 2, 2, '2023-07-17', 'pending')
;