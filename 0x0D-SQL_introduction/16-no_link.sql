-- List row with a name value
SELECT `score`, `name` FROM `second_table` 
WHERE `name` NOT NULL
GROUP BY `score` 
ORDER BY `score` DESC;
