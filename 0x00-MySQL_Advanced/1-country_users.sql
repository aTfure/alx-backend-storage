-- Script that create  a table users following these requirements:
-- id, email, name, country(enumeration of US, CO and TN)

CREATE TABLE IF NOT EXISTS users(
	id int NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	PRIMARY KEY(id),
	country ENUM('US','CO','TN') DEFAULT 'US' NOT NULL
);
