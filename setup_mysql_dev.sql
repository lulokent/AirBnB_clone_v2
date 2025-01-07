-- Creates a MySQL server with:
-- Creates the database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if it doesn't exit
CREATE USER IF NOT EXITS 'hbnb_Dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant Privileges on hbnb_dev_db
GRANT ALL PRIVILGES ON hbnb_dev_db.* To 'hbnb_dev'@'localhost';
-- Flush Privilege
FLUSH PRIVILEGES;

-- Grant Select Privilege on performance schema
GRANT SELECT ON performanc_schema.* TO 'hbnb_dev'@'localhost';
-- Flush Privilege
FLUSH PRIVILEGES;
