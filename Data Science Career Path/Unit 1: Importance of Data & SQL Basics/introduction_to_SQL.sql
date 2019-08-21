create table friends (
	id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Jane Doe', '1990-05-30');

INSERT INTO friends (id, name, birthday) 
VALUES (2, 'Bill Smith', '1989-06-01');
INSERT INTO friends (id, name, birthday) 
VALUES (3, 'Rick Mesa', '1991-07-02');

UPDATE friends SET name = "Jane Smith" WHERE id = 1;

ALTER TABLE friends ADD COLUMN email TEXT;

UPDATE friends SET email = "jane@codecademy.com" WHERE id = 1;
UPDATE friends SET email = "bsmith@gmail.com" WHERE id = 2;
UPDATE friends SET email = "rickmesa@live.com" WHERE id = 3;

DELETE FROM friends WHERE id = 1;

SELECT * FROM friends;