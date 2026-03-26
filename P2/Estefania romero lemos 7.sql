CREATE TABLE Desagrupacion.a (
	id INT auto_increment NOT NULL,
	producto varchar(100) NOT NULL,
	cantidad INT NOT NULL,
	PRIMARY KEY(id)
);
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Desagrupacion.a
(id, producto, cantidad)
VALUES(1, 'Lapiz', 3),
(2, 'Borrador', 4),
(3, 'Cuaderno', 2);

SELECT 'Lápiz' AS Producto, 1 AS Cantidad
UNION ALL SELECT 'Lápiz', 1
UNION ALL SELECT 'Lápiz', 1
UNION ALL SELECT 'Borrador', 1
UNION ALL SELECT 'Borrador', 1
UNION ALL SELECT 'Borrador', 1
UNION ALL SELECT 'Borrador', 1
UNION ALL SELECT 'Cuaderno', 1
UNION ALL SELECT 'Cuaderno', 1;

CREATE TABLE asientos.a (
	id INT auto_increment NOT NULL,
	num_asientos INTEGER NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO asientos.a
(id, num_asientos)
VALUES(1, 7),
(2, 13),
(3, 14),
(4, 15),
(5, 27),
(6, 28),
(7, 29),
(8, 30), 
(9, 31),
(10, 32),
(11, 33),
(12, 34),
(13, 35),
(14, 52),
(15, 53),
(16, 54);

SELECT 
    MIN(id) AS espacio_inicio, 
    MAX(id) AS espacio_final
FROM (
    SELECT 
        id, 
        id - ROW_NUMBER() OVER (ORDER BY id) AS grupo
    FROM asientos.a  
) t
GROUP BY grupo
ORDER BY espacio_inicio;

SELECT 
    IF(id % 2 = 0, 'pares', 'impares') AS tipo, 
    COUNT(*) AS total
FROM asientos.a
GROUP BY tipo;

SELECT COUNT(*) AS disponibles 
FROM asientos.a;

CREATE TABLE futuro.a (
	id INT auto_increment NOT NULL,
	inicio TIMESTAMP NOT NULL,
	`final` TIMESTAMP NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO futuro.a
(id, inicio, `final`)
VALUES(1, '2025-01-01', '2025-01-05'),
(2, '2025-01-03', '2025-01-09'),
(3, '2025-01-10', '2025-01-11'),
(4, '2025-01-12',  '2025-01-16'),
(5, '2025-01-15', '2025-01-19');

SELECT '2025-01-01' AS inicio, '2025-01-09' AS final
UNION ALL 
SELECT '2025-01-10', '2025-01-11'
UNION ALL
SELECT '2025-01-12', '2025-01-19';
