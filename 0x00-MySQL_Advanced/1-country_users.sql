-- Sql query to create country and users using enum

CREATE TABLE IF NOT EXISTS users(
        id INT NOT NULL AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL,
        name VARCHAR(255),
        country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
        UNIQUE (email),
        PRIMARY KEY (id)
);
