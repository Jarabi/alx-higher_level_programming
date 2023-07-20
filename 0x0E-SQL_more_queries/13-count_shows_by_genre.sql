-- Count number of shows by genre
SELECT name as genre, COUNT(id) as number_of_shows
FROM tv_genres g
LEFT JOIN tv_show_genres sg
ON g.id = sg.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
