# SQL Introduction Project

This project contains SQL scripts that demonstrate basic database operations in MySQL 8.0 on Ubuntu.

## Requirements

- Environment: Ubuntu 20.04 LTS (or Ubuntu 22.04 for the sandbox)
- MySQL version: 8.0 (8.0.25 on Ubuntu 20.04; 8.0.39 on Ubuntu 22.04)
- Allowed editors: vi, vim, emacs
- All SQL scripts begin with a comment describing the task.
- All SQL keywords are in uppercase.
- Every file ends with a new line.
- The length of your files will be checked using `wc`.

## Files

- **0-list_databases.sql**: Lists all databases.
- **1-create_database_if_missing.sql**: Creates the database `hbtn_0c_0` if it does not already exist.
- **2-remove_database.sql**: Deletes the database `hbtn_0c_0` if it exists.
- **3-list_tables.sql**: Lists all tables of the current database.
- **4-first_table.sql**: Creates a table named `first_table` with columns `id` and `name`.
- **5-full_table.sql**: Shows the full creation statement for `first_table`.
- **6-list_values.sql**: Lists all rows in the table `first_table`.
- **7-insert_value.sql**: Inserts a row (id = 89, name = "Best School") into `first_table`.
- **8-count_89.sql**: Counts the number of records with id = 89 in `first_table`.
- **9-full_creation.sql**: Creates the table `second_table` and inserts multiple rows.
- **10-top_score.sql**: Lists all records from `second_table` (displaying score and name) ordered by score descending.
- **11-best_score.sql**: Lists records from `second_table` with a score >= 10 (displaying score and name) ordered by score descending.
- **12-no_cheating.sql**: Updates Bob’s score to 10 in `second_table` (using only the name field).
- **13-change_class.sql**: Deletes records from `second_table` with a score <= 5.
- **14-average.sql**: Computes the average score from `second_table` (result column named `average`).
- **15-groups.sql**: Lists the number of records grouped by score from `second_table` (sorted by number descending).
- **16-no_link.sql**: Lists all records from `second_table` where the name column is not null (displaying score and name, ordered by descending score).
- **100-move_to_utf8.sql**: Converts the database `hbtn_0c_0`, the table `first_table`, and its `name` column to UTF8 (utf8mb4 with collation utf8mb4_unicode_ci).
- **101-avg_temperatures.sql**: Displays the average temperature (Fahrenheit) by city from the imported temperatures table, ordered by average temperature descending.
- **102-top_city.sql**: Displays the top 3 cities (by average temperature) during July and August from the temperatures table.
- **103-max_state.sql**: Displays the maximum temperature of each state from the temperatures table, ordered by state name.

## How to Run

To execute any script, use a command similar to the following (adjusting the database name as needed):

```bash
cat <script_name.sql> | mysql -hlocalhost -uroot -p <database_name>

