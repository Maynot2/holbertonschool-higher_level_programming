-- List row with a name value
SELECT `name`, `score` FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
