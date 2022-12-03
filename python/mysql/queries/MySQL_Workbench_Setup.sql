INSERT INTO users (first_name, last_name, email)
VALUES ("Justin", "Satchwell", "jsatch@uw.edu"), ("Analisa", "Arnold", "arnola2@uw.edu"), ("Malcolm", "Satchwell", "notbornyet@gmail.com");

SELECT * FROM users;

SELECT email
FROM users
WHERE id = 1;

SELECT first_name, last_name, email
FROM users
WHERE id = 3;

UPDATE users
SET last_name = "Pancakes"
WHERE id = 3;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM users WHERE id = 2;

SELECT first_name
FROM users
ORDER BY first_name;

SELECT first_name
FROM users
ORDER BY first_name DESC;