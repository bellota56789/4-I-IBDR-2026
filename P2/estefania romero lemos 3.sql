CREATE TABLE Promedio.dias (
	Id INT auto_increment NOT NULL,
	desarrollo varchar(100) NOT NULL,
	terminacion TIMESTAMP NOT NULL,
	PRIMARY KEY(Id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Promedio.dias
(Id, desarrollo, terminacion)
VALUES
(1, 'RestAPI', '2024-06-01'),
(2, 'RestAPI', '2024-06-14'),
(3, 'RestAPI', '2024-06-15'),
(4, 'Web', '2024-06-01'),
(5, 'Web', '2024-06-02'),
(6, 'Web', '2024-06-19'),
(7, 'App', '2024-06-01'),
(8, 'App', '2024-05-15'),
(9, 'App', '2024-06-30');

SELECT 
    Desarrollo, 
    AVG(ID) AS Promedio 
FROM Promedio.dias
GROUP BY Desarrollo
ORDER BY Promedio ASC;

CREATE TABLE Inventario.a (
	ID INT auto_increment NOT NULL,
	fecha TIMESTAMP NOT NULL,
	Ajuste INT NOT NULL,
	PRIMARY KEY(ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Inventario.a
(ID, fecha, Ajuste)
VALUES(1, '2025-03-01', 100),
(2, '2025-04-01', 75),
(3, '2025-05-01', -150),
(4, '2025-06-01', 50),
(5, '2025-07-01', -70);


SELECT 
    Fecha, 
    Ajuste, 
    SUM(Ajuste) OVER (ORDER BY Fecha ASC) AS Inventario
FROM Inventario.a
ORDER BY Fecha ASC;


