-- Displays the average temperature (F) by city ordered by temperature (desc).
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`  WHERE month = 7 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`
WHERE `month`=7 OR `month=8`
GROUP BY `city` 
ORDER BY `avg_temp` DESC
LIMIT 3;
