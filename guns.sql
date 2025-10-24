CREATE DATABASE gans_schema;

USE gans_schema;

CREATE TABLE cities(
	city_id INT AUTO_INCREMENT,
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT,
    PRIMARY KEY (city_id, city)
);

SELECT * FROM cities;

CREATE TABLE populations(
	city_id INT NOT NULL,
    population INT,
    timestamp_population DATETIME,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

SELECT * FROM populations;

CREATE TABLE weathers(
    city_id INT,    
    forecast_time DATETIME,
    temperature FLOAT,
    forecast VARCHAR(255),
    rain_in_last_3h FLOAT,
    wind_speed FLOAT,
    data_retrieved_at DATETIME,
    PRIMARY KEY (city_id, forecast_time),
    FOREIGN KEY(city_id) REFERENCES cities(city_id)
);

SELECT * FROM weathers;

CREATE TABLE airports (
	airport_icao VARCHAR(255),
    airport_name VARCHAR(255),
    city VARCHAR(255),
    PRIMARY KEY (airport_icao)
);

SELECT * FROM airports;

CREATE TABLE cities_airport (
	city_id INT NOT NULL,
    airport_icao VARCHAR(255) NOT NULL,
    FOREIGN KEY(city_id) REFERENCES cities(city_id),
    FOREIGN KEY(airport_icao) REFERENCES airports(airport_icao)
);

SELECT * FROM cities_airport;

CREATE TABLE flights (
	flight_id INT AUTO_INCREMENT,
    flight_number VARCHAR(255),
    departure_icao VARCHAR(255),
    arrival_icao VARCHAR(255),
    arrival_time DATETIME,
    data_retrieved_on DATETIME,
    PRIMARY KEY (flight_id),
    FOREIGN KEY (arrival_icao) REFERENCES airports(airport_icao)
);

SELECT * FROM flights;
