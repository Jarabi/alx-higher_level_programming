-- List all shows without the genre "Comedy"
SELECT s.title
FROM tv_shows s
WHERE s.title NOT IN (
	SELECT s.title
	FROM tv_shows s
	LEFT JOIN tv_show_genres sg
	ON sg.show_id = s.id
	LEFT JOIN tv_genres g
	ON sg.genre_id = g.id
	WHERE g.name = "Comedy"
)
ORDER BY s.title;
