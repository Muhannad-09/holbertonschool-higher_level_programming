-- Script to list records with score >= 10 from second_table ordered by score

-- Select score and name where score is greater than or equal to 10
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
