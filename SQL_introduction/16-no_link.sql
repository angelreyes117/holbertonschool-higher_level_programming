-- List records from second_table where name is not null, displaying score and name, ordered by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
