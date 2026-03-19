CREATE TABLE Proceso.indeterminado (
	ID INT auto_increment NOT NULL,
	flujo varchar(100) NOT NULL,
	paso INT NOT NULL,
	Estado varchar(100) NOT NULL,
	PRIMARY KEY(ID)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Proceso.indeterminado
(ID, flujo, paso, Estado)
VALUES
(1, 'Alpha', 1, 'Error'),
(2, 'Alpha', 2, 'Finalizado'),
(3, 'Alpha', 3, 'Corriendo'),
(4, 'Bravo', 1, 'Finalizado'),
(5, 'Bravo', 2, 'Finalizado'),
(6, 'Charlie', 1, 'Corriendo'),
(7, 'Charlie', 2, 'Corriendo'),
(8, 'Delta', 1, 'Error'),
(9, 'Delta', 2, 'Error'),
(10, 'Echo', 1, 'Corriendo'),
(11, 'Echo', 2, 'Finalizado');

SELECT 'Alpha' AS estado, 'indeterminado'
UNION ALL
SELECT 'Bravo', 'finalizado'
UNION ALL
SELECT 'Charlie', 'corriendo'
UNION ALL
SELECT 'Delta', 'error'
UNION ALL 
SELECT 'Echo', 'corriendo';

CREATE TABLE a.Marcador (
	id INT auto_increment NOT NULL,
	jugador_a INT NOT NULL,
	jugador_b INT NOT NULL,
	marcador INT NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO a.Marcador
(id, jugador_a, jugador_b, marcador)
VALUES(1, 1001, 2002, 150),
(2, 3003, 4004, 15),
(3, 4004, 3003, 125);

SELECT 1001 AS jugador_a, 2002 AS jugador_b, 150 AS
marcador
UNION ALL 
SELECT 3003, 4004, 15;


CREATE TABLE Concatenacion.grupo (
	id INT auto_increment NOT NULL,
	secuencia INT NOT NULL,
	sintaxis varchar(100) NOT NULL,
	PRIMARY KEY(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO Concatenacion.grupo
(id, secuencia, sintaxis)
VALUES
(1001, 1, 'SELECT'),
(1002, 2, 'Producto'),
(1003, 3, 'Precio'),
(2002, 4, 'Disponibilidad'),
(2004, 5, 'FROM'),
(3003, 6, 'Productos'),
(4004, 7, 'WHERE'),
(4008, 8, 'Precio'),
(5005, 9, '>100');


SELECT 'SELECT', 'Producto', 'Disponibilidad', '
FROM', 'Productos', 
'WHERE', 'Precio',
'<100';







