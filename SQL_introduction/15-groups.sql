-- Script to count number of records for each score in second_table

-- Group by score and count how many times each appears
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
