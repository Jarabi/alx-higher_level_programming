-- List number of shows in each genre
-- Genres without linked shows are not listed
SELECT g.name AS genre, COUNT(id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres sg
ON g.id = sg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
