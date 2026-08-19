CREATE DATABASE wanderly_india;

CREATE TABLE users (
 id SERIAL PRIMARY KEY,
 name VARCHAR(120) NOT NULL,
 email VARCHAR(180) UNIQUE NOT NULL,
 password_hash TEXT NOT NULL,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE destinations (
 id SERIAL PRIMARY KEY,
 name VARCHAR(120) NOT NULL,
 country VARCHAR(120) NOT NULL,
 description TEXT,
 image_url TEXT
);

CREATE TABLE packages (
 id SERIAL PRIMARY KEY,
 title VARCHAR(180) NOT NULL,
 destination VARCHAR(120) NOT NULL,
 duration_days INTEGER NOT NULL,
 price_inr NUMERIC(12,2) NOT NULL,
 image_url TEXT
);

CREATE TABLE bookings (
 id SERIAL PRIMARY KEY,
 user_id INTEGER REFERENCES users(id),
 package_id INTEGER REFERENCES packages(id),
 travel_date DATE NOT NULL,
 guests INTEGER NOT NULL,
 status VARCHAR(30) DEFAULT 'confirmed',
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
