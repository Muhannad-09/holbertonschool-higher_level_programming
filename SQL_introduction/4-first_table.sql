-- Script to create table first_table in the current database if it does not exist

-- Create first_table with id INT and name VARCHAR(256)
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
