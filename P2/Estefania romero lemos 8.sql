
CREATE TABLE Compras.a (
	id INT auto_increment NOT NULL,
	año varchar(100) NOT NULL,
	cantidad INT NOT NULL,
	PRIMARY KEY(id)
);
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Compras.a
(id, año, cantidad)
VALUES(1, '2025', 352645),
(2, '2024', 165565),
(3, '2024', 254654),
(4, '2023', 159521),
(5, '2023', 251696),
(6, '2023', 111894);

SELECT 
    SUM(CASE WHEN año = 2025 THEN cantidad ELSE 0 END) AS "2025",
    SUM(CASE WHEN año = 2024 THEN cantidad ELSE 0 END) AS "2024",
    SUM(CASE WHEN año = 2023 THEN cantidad ELSE 0 END) AS "2023"
FROM Compras.a;

CREATE TABLE duplicados.a (
	id INT auto_increment NOT NULL,
	valor INTEGER NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO duplicados.a
(id, valor)
VALUES(1001, 1),
(1002, 1),
(2002, 2),
(3003, 3),
(3004, 3),
(4004, 4);

SELECT 1 AS valor
UNION ALL SELECT 2
UNION ALL SELECT 3
UNION ALL SELECT 4;

CREATE TABLE huecos.a (
	id INT auto_increment NOT NULL,
	fila INT NOT NULL,
	aplicacion varchar(100) NOT NULL,
	estado varchar(100) NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO huecos.a
(id, fila, aplicacion, estado)
VALUES(1001, 1, 'web', 'Aprobado'),
(2002, 2, '', 'Fallo'),
(3003, 3, '', 'Fallo'),
(4004, 4, '', 'Fallo'),
(5005, 5, 'App', 'Aprobado'),
(6006, 6, '', 'Fallo'),
(7007, 7, '', 'Fallo'),
(8008, 8, '', 'Aprobado'),
(9009, 9, '', 'Aprobado'),
(1010, 10, 'RESTAPI', 'Fallo'),
(2020, 11, '', 'Fallo'),
(3030, 12, '', 'Fallo');

SELECT 'Web' AS Aplicacion, Estado FROM huecos.a
UNION ALL
SELECT 'App' AS Aplicacion, Estado FROM huecos.a
UNION ALL
SELECT 'RESTAPI' AS Aplicacion, Estado FROM huecos.a;


