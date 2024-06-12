-- script that creates a new table in a database

CREATE TABLE IF NOT EXISTS users(
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(256) NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id),
	UNIQUE (email)
);
