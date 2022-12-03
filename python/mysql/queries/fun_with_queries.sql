-- CONCAT()
SELECT CONCAT('Mr.', ' ', first_name, ' ', last_name) AS full_name FROM users;
-- CONCAT_WS()
SELECT CONCAT_WS(' ', first_name, last_name, 'cool') AS full_name FROM users;
-- LENGTH()
SELECT LENGTH(last_name) AS last_len FROM users;
-- LOWER()
SELECT LOWER(first_name) AS first_lowercase FROM users;
SELECT first_name from users;

-- HOUR()
SELECT HOUR(updated_at) AS date_hour, updated_at FROM users;
-- DAYNAME()
SELECT DAYNAME(updated_at) AS day_name, updated_at FROM users;
-- MONTH()
SELECT MONTH(updated_at) AS month_number, updated_at FROM users;
-- NOW()
SELECT NOW() AS right_now;
-- DATE_FORMAT()
SELECT DATE_FORMAT(updated_at, '%W %M %e %Y') FROM users;