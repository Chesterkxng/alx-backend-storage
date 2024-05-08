-- create a table usrs if it doesn't exist
-- if exist no fail
CREATE TABLE IF NOT EXISTS users (
       id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN') DEFAULT 'US'
);
