CREATE TABLE Permutaciones.a (
	ID INT auto_increment NOT NULL,
	Letra varchar(100) NOT NULL,
	PRIMARY KEY(ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Permutaciones.a
(ID, Letra)
VALUES(1, 'a'),
(2, 'b'),
(3, 'c');

SELECT 
    CONCAT(a.letra, ',', b.letra, ',', c.letra) AS Permutacion
FROM Permutaciones.a a
JOIN Permutaciones.a b ON a.letra <> b.letra
JOIN Permutaciones.a c ON a.letra <> c.letra AND b.letra <> c.letra
ORDER BY a.letra, b.letra, c.letra;


