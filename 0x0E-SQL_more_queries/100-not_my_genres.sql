-- List all genres not linked to the show "Dexter"
SELECT g.name
FROM tv_genres g
WHERE g.id NOT IN (
       	SELECT sg.genre_id
    	FROM tv_show_genres sg
    	JOIN tv_shows s
   	ON sg.show_id = s.id
    	WHERE s.title = "Dexter"
)
ORDER BY g.name;
