/* 
Implementacion de una base de datos en un sistema de informacion
2026/03/04 4-I
Juan Antonio Ortega Sandoval
Nombre de la practica
*/

CREATE TABLE departamentos (
  id int NOT NULL,
  name varchar(25) NOT NULL,
  location date NOT NULL,
  PRIMARY KEY (id, name)
);


-- Crear una tabla llamaba "empleados" con las columnas  id, nombre, edad, and salario.
CREATE TABLE Empleados (
	id INT auto_increment NOT NULL,
	edad TIMESTAMP NOT NULL,
	salario DECIMAL NOT NULL,
	PRIMARY KEY(id)

-- Insertar 5 registros en la tabla "emplados".
INSERT INTO Empleados 
(id, nombre, edad, salario)
VALUES (1, 'Francisco', 21, 18),
    (2, 'Erika', 22, 15),
    (3, 'Maria', 25, 19),
    (4, 'Luis', 19, 13),
    (5, 'Leo', 29, 22);

-- Agregar una nueva columna "departamento" a la tabla "empleados".
ALTER TABLE Empleados 
ADD COLUMN departamento INTEGER NOT NULL;


-- Cambiar el tipo de dato de la columna "salario" a Integer.
ALTER TABLE Empleados 
ADD COLUMN salario INTEGER NOT NULL,


-- Eliminar la columna "departamento de la tabla "empleados".
ALTER TABLE Empleados ADD COLUMN
DELETE departamento INTEGER NOT NULL;

-- Eliminar la tabla "departamentos" permanentemente.
ALTER TABLE Empleados ADD COLUMN
DROP departamento INTEGER NOT NULL;
-- Renombrar la tabla "empleados" a "staff".
ALTER TABLE Empleados
RENAME TABLE staff
-- Definir 0 como valor predeterminado en la comlumna "salario".
ALTER TABLE staff 
ADD COLUMN salario DECIMAL (10, 2) DEFAULT 0

-- Crear un nuevo esquema llamado "rh_db".
CREATE SCHEMA  rh_db
-- Mover la tabla "empleados" al esquema "rh_db".
CREATE SCHEMA  rh_db
CREATE TABLE Empleados
id INT auto_increment NOT NULL,
	edad TIMESTAMP NOT NULL,
	salario DECIMAL NOT NULL,
	PRIMARY KEY(id)

