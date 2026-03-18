CREATE TABLE Precio.demanda (
	ID INT auto_increment NOT NULL,
	fecha varchar(100) NOT NULL,
	precio INT NOT NULL,
	PRIMARY KEY(ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Precio.demanda
(ID, fecha, precio)
VALUES(1001, '2025-01-01', 19.99),
(1002, '2025-04-15', 59.99),
(1003, '2025-06-08', 79.99),
(2002, '2025-04-17', 39.99),
(2003, '2025-05-19', 59.99);

SELECT 1001 AS ID,
'2025-06-08' AS fecha, 79.99 AS
precio
UNION ALL 
SELECT 2003, '2025-05-19', 59.99;

CREATE TABLE Ventas.promedio (
	id INT auto_increment NOT NULL,
	id_cliente INT NOT NULL,
	fecha varchar(100) NOT NULL,
	total NUMERIC NOT NULL,
	estado varchar(100) NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Ventas.promedio
(id, id_cliente, fecha, total, estado)
VALUES(1, 1001, '2025-01-01', 100, 'JAL'),
(2, 1002, '2025-01-01', 150, 'JAL'),
(3, 1003, '2025-01-01', 75, 'JAL'),
(4, 1004, '2025-02-01', 100, 'JAL'),
(5, 1005, '2025-03-01', 100, 'JAL'),
(6, 2002, '2025-02-01', 75, 'JAL'),
(7, 2002, '2025-02-01', 150,'JAL'),
(8, 3003, '2025-01-01', 100, 'CDMX'),
(9, 3003, '2025-02-01', 100, 'CDMX'),
(10, 3003, '2025-01-03', 100, 'CDMX'),
(11, 4004, '2025-04-01', 100, 'CDMX'),
(12, 4004, '2025-05-01', 50, 'CDMX'),
(13, 4004, '2025-05-01', 100, 'CDMX');

SELECT 'JAL' AS estado

CREATE TABLE Ocurrencias.a (
	id INT auto_increment NOT NULL,
	proceso varchar(100) NOT NULL,
	mesnaje varchar(100) NOT NULL,
	ocr INT NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Ocurrencias.a
(id, proceso, mesnaje, ocr)
VALUES
(1, 'Web', 'Error: No se puede dividir por 0', 3),
(2, 'RestAPI', 'Error: Fallo la conversión', 5),
(3, 'App', 'Error: Fallo la conversión', 7),
(4, 'RestAPI', 'Error: Error sin identificar', 9),
(5, 'Web', 'Error: Error sin identificar', 1),
(6, 'App', 'Error: Error sin identificar', 10),
(7, 'Web', 'Estado Completado', 8), 
(8, 'RestAPI', 'Estado Completado', 6);

SELECT 'Web' AS Proceso, 'Error: No se puede dividir por 0' AS Mensaje, 3 AS Ocurrencia
UNION ALL
SELECT 'App', 'Error: Fallo la conversión', 7
UNION ALL
SELECT 'App', 'Error: Error sin identificar', 10
UNION ALL
SELECT 'RestAPI', 'Estado Completado', 8;


