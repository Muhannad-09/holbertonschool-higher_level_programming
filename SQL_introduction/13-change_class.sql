-- Script to delete records with score <= 5 from second_table

-- Remove all low scoring entries
DELETE FROM second_table
WHERE score <= 5;
