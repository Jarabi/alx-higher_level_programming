-- List number of shows in each genre
SELECT name AS genre, COUNT(id) AS number_of_shows
FROM tv_genres g
LEFT JOIN tv_show_genres sg
ON g.id = sg.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
