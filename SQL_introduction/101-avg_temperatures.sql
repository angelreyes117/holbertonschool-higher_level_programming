-- Display the average temperature (Fahrenheit) by city from temperatures table, ordered by average temperature descending
SELECT city, AVG(temperature) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
