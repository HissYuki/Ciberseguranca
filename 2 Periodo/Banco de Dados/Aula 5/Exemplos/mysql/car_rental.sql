-- Cria o banco de dados
DROP DATABASE IF EXISTS car_rental
CREATE DATABASE car_rental;
USE car_rental;

CREATE TABLE IF NOT EXISTS car_rental.person (
	id INT NOT NULL AUTO_INCREMENT,
    cpf CHAR(11) NOT NULL,
    person_name VARCHAR(256) NOT NULL,
    birth_date DATE NOT NULL,
    UNIQUE(cpf),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS car_rental.email (
	email VARCHAR(100) NOT NULL,
    id_person INT NOT NULL,
    UNIQUE(email),
    FOREIGN KEY(id_person) REFERENCES car_rental.person (id)
);

CREATE TABLE IF NOT EXISTS car_rental.phone (
	country_code SMALLINT UNSIGNED NOT NULL,
    ddd SMALLINT UNSIGNED NOT NULL,
    phone_number BIGINT UNSIGNED NOT NULL,
    id_person INT NOT NULL,
    UNIQUE(phone_number),
    FOREIGN KEY(id_person) REFERENCES car_rental.person (id)
);

CREATE TABLE IF NOT EXISTS car_rental.car (
	id INT NOT NULL AUTO_INCREMENT,
    current_value DECIMAL(6,2) UNSIGNED NOT NULL,
    capacity TINYINT UNSIGNED NOT NULL,
    category VARCHAR(45) NOT NULL,
    chassi CHAR(17) NOT NULL,
    color VARCHAR(20) NOT NULL,
    model_year YEAR NOT NULL,
    model VARCHAR(30) NOT NULL,
    brand VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
);

