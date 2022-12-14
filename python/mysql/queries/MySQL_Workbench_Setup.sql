INSERT INTO users (first_name, last_name)
VALUES ("Jane", "Amsden"), ("Emily", "Dixon"), ("Theodore", "Dostoevsky"), ("William", "Shapiro"), ("Lao", "Xiu");

SELECT * FROM users;

INSERT INTO books (title, num_of_pages)
VALUES ("C Sharp", 200), ("Java", 150), ("Python", 300), ("PHP", 250), ("Ruby", 175);

SELECT * FROM books;

UPDATE books
SET title = "C#"
WHERE id = 1;

UPDATE users
SET first_name = "Bill"
WHERE id = 4;

SELECT * FROM favorites;

INSERT INTO favorites (user_id, book_id)
VALUES (1, 1);

INSERT INTO favorites (user_id, book_id)
VALUES (1, 2), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4),
		(4, 1), (4, 2), (4, 3), (4, 4), (4, 5);

SELECT id, first_name, last_name FROM users
JOIN favorites ON users.id = favorites.user_id
WHERE favorites.book_id = 3;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM favorites WHERE user_id = 2 AND book_id = 3;

INSERT INTO favorites (user_id, book_id)
VALUES (5, 2);

SELECT title, num_of_pages from books
JOIN favorites ON books.id = favorites.book_id
WHERE favorites.user_id = 3;

SELECT * from users
JOIN favorites ON favorites.user_id = users.id
WHERE favorites.book_id = 5;