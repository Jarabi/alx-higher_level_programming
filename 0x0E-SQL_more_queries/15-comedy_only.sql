-- List all comedy shows in the database
SELECT title
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE name = "Comedy"
ORDER BY title;
