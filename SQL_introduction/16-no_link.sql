-- Script to list records with a non-empty name from second_table

-- Select only rows where name is not NULL and not empty, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
