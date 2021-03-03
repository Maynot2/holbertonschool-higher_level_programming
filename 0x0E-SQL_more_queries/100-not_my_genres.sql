-- Lists all genres of the show Dexter
SELECT t.name
FROM tv_genres t
WHERE t.name NOT IN (
	SELECT a.name
	FROM tv_genres a
	JOIN tv_show_genres b
	ON a.id = b.genre_id
	JOIN tv_shows c
	ON b.show_id = c.id
	WHERE c.title = 'Dexter'
)
ORDER BY t.name;
