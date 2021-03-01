-- List row with a name value
SELECT name, score FROM second_table
WHERE score IS NOT NULL
ORDER BY score DESC;
