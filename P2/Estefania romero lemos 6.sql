CREATE TABLE Videojuegos.a (
	id_jugador INT auto_increment NOT NULL,
	marcador INT NOT NULL,
	PRIMARY KEY(id_jugador)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Videojuegos.a
(id_jugador, marcador)
VALUES(1001, 2343),
(2002, 9432),
(3003, 6598),
(4004, 1054),
(5005, 6832);

SELECT (CASE WHEN a.Marcador >= b.Corte THEN 1 ELSE 2 END) AS Categoria, a.*
FROM Videojuegos.a a
CROSS JOIN (SELECT AVG(Marcador) AS Corte FROM Videojuegos.a) b
ORDER BY Categoria, Marcador DESC;

CREATE TABLE Pagina.a (
	id_orden INT auto_increment NOT NULL,
	id_cliente INT NOT NULL,
	fecha TIMESTAMP NOT NULL,
	cantidad INT NOT NULL,
	estado varchar(100) NOT NULL,
	PRIMARY KEY(id_orden)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Pagina.a
(id_orden, id_cliente, fecha, cantidad, estado)
VALUES(1, 1001, '2025/01/01', 100, 'JAL'),
(2, 3003, '2025/01/01', 100,'COL'),
(7, 1001, '2025/01/01', 150,'JAL'),
(10, 1001,'2025/01/01', 75,'JAL'),
(4, 2002, '2025/01/02', 150,'JAL'),
(5, 1001, '2025/01/02', 100, 'JAL'),
(11, 2002,'2025/01/02', 75, 'JAL'),
(12, 3003, '2025/01/02', 100, 'COL'),
(3, 1001, '2025/01/03', 100, 'JAL'),
(8, 3003, '2025/01/03', 100, 'COL'),
(9, 4004, '2025/01/04', 100, 'COL'),
(6, 4004, '2025/01/05', 50, 'COL'),
(13, 4004, '2025/01/05', 100, 'COL');

SELECT Id_orden, Id_cliente, Fecha, Cantidad, Estado
FROM Pagina.a
ORDER BY Id_orden ASC
LIMIT 5 OFFSET 4;

CREATE TABLE Proovedores.a (
	id_orden INT auto_increment NOT NULL,
	id_cliente INT NOT NULL,
	cantidad NUMERIC NOT NULL,
	proovedor varchar(100) NOT NULL,
	PRIMARY KEY(id_orden)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Proovedores.a
(id_orden, id_cliente, cantidad, proovedor)
VALUES(1, 1001, 12, 'IBM'),
(2, 1001, 54, 'IBM'),
(3, 1001, 32, 'Amazon'),
(4, 2002, 7, 'Amazon'),
(5, 2002, 16, 'Amazon'),
(6, 2002, 5, 'IBM');

SELECT t1.Id_cliente, t1.Proovedor
FROM (
    SELECT Id_cliente, Proovedor, COUNT(*) as total
    FROM Proovedores.a
    GROUP BY Id_cliente, Proovedor
) AS t1
WHERE t1.total = (
    SELECT MAX(total)
    FROM (
        SELECT Id_cliente, Proovedor, COUNT(*) as total
        FROM Proovedores.a
        GROUP BY Id_cliente, Proovedor
    ) AS t2
    WHERE t1.Id_cliente = t2.Id_cliente
);



	
	

