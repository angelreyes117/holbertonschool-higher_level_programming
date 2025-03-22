-- Lists all genres by their rating sum
SELECT tv_genres.name, SUM(tv_shows_rate.rating) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows_rate ON tv_show_genres.show_id = tv_shows_rate.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
