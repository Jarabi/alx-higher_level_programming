-- List all shows without genre
SELECT title, genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres g
ON g.show_id = s.id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id;
