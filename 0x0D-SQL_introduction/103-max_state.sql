-- Displays the average temperature (F) by city ordered by temperature (desc).
SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures` GROUP BY `state`;
