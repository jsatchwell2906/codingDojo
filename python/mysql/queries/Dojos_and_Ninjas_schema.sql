-- INSERT INTO dojos (name)
-- VALUES ("Coding Dojo"), ("Karate Dojo"), ("Cooking Dojo");

-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM dojos;

-- INSERT INTO ninjas (first_name, last_name, dojo_id)
-- VALUES ("Justin", "Satchwell", 70), ("Analisa", "Arnold", 70), ("Malcolm", "Satchwell", 70),
-- 		("Fred", "Satchwell", 71), ("Wilma", "Satchwell", 71), ("Karen", "Satchwell", 71),
-- 		("Cammie", "Dodson", 72), ("Jacob", "Greenberg", 72), ("Arthur", "Ericksen", 72);

-- SELECT * FROM dojos
-- LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
-- WHERE dojos.id  = 70;

-- SELECT * FROM dojos
-- LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
-- 	WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);

SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);