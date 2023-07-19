-- Import database dump
SELECT title, genre_id
FROM tv_shows s
INNER JOIN tv_show_genres g
ON g.show_id = s.id
ORDER BY s.title ASC, g.genre_id ASC;
