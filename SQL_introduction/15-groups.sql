-- Group records in second_table by score and display score and number of records, ordered by number descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
