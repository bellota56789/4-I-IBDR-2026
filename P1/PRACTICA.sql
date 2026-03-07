CREATE TABLE defaultdb.a (
	id INT auto_increment NOT NULL,
	pilotos varchar(100) NOT NULL,
	CONSTRAINT a_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE defaultdb.b (
	id INT auto_increment NOT NULL,
	pilotos varchar(100) NOT NULL,
	CONSTRAINT b_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO defaultdb.a
(id, pilotos)
VALUES(1, 's.perez'),
(2, 'm.botas'),
(3, 'm.verstappen'),
(4, 'i.hadjar'),
(5, 'c.leclerick'),
(6, 'l.hamilton'),
(7, 'l.norris');

INSERT INTO defaultdb.b
(id, pilotos)
VALUES(1, 'g.rosell'),
(2, 'k.antonelli'),
(3, 's.perez'),
(4, 'f.alonso'),
(5, 'm.vealtappey'),
(6, 'l.lawson'),
(7, 'l.hamilton');

SELECT *
FROM defaultdb.a
INNER JOIN defaultdb.b
ON defaultdb.a.pilotos  = defaultdb.b.pilotos ;

SELECT *
FROM defaultdb.a
FULL OUTER JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos;

SELECT *
FROM defaultdb.a
LEFT OUTER JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos;

SELECT *
FROM defaultdb.a
RIGHT OUTER JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos;

SELECT *
FROM defaultdb.a
LEFT OUTER JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos
UNION ALL
SELECT *
FROM defaultdb.a
RIGHT OUTER JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos;

SELECT *
FROM defaultdb.a
LEFT JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos
WHERE defaultdb.b.pilotos IS NULL;

SELECT *
FROM defaultdb.a
RIGHT JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos
WHERE defaultdb.a.pilotos IS NULL;

SELECT *
FROM defaultdb.a
LEFT JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos
WHERE defaultdb.b.pilotos IS NULL
UNION ALL
SELECT *
FROM defaultdb.a
RIGHT JOIN defaultdb.b
ON defaultdb.a.pilotos = defaultdb.b.pilotos
WHERE defaultdb.a.pilotos IS NULL;
