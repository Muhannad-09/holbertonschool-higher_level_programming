-- Task: Create MySQL user user_0d_1 with full privileges
-- This script creates the user 'user_0d_1'@'localhost' with password 'user_0d_1_pwd'
-- and grants them all privileges on the server.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
