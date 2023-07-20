-- Import database dump
SELECT title, genre_id
FROM tv_shows s
LEFT JOIN tv_show_genres g
ON g.show_id = s.id
ORDER BY s.title, g.genre_id;
