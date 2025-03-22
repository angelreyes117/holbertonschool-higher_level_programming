-- Display the maximum temperature of each state from temperatures table, ordered by state name
SELECT state, MAX(temperature) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
