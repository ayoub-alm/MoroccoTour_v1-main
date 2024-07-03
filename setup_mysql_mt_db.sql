-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS mt_dev_db;
CREATE USER IF NOT EXISTS 'mt_dev'@'localhost' IDENTIFIED BY 'Mt@12_34';
GRANT ALL PRIVILEGES ON `mt_dev_db`.* TO 'mt_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'mt_dev'@'localhost';
FLUSH PRIVILEGES;
