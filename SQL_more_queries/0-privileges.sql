-- Task: List all privileges of user_0d_1 and user_0d_2 on localhost
-- This script displays the privileges granted to user_0d_1 and user_0d_2

-- List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
