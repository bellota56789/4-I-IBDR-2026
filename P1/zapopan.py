CREATE TABLE central_autobuses_zapopan (
  nombre id int NOT NULL,
  autobuses date NOT NULL,
  ruta date NOT NULL,
  codigo_incapacidad varchar(25) DEFAULT NULL,
  PRIMARY KEY (nombre_id, ruta)
);
 
CREATE TABLE zapopan_id (
  autobuses_id int NOT NULL,
  llegada NOT NULL,
  destino NOT NULL,
  costo NOT NULL,
  codigo_incapacidad varchar(25) DEFAULT NULL,
  zapopan varchar(25) DEFAULT NULL,
  PRIMARY KEY (autobuses_id, costo)
);

CREATE TABLE autobuses_id (
  horario_id int NOT NULL AUTO_INCREMENT,
  frecuencia_id int DEFAULT NULL,
  servicio int DEFAULT NULL,
  PRIMARY KEY (horario_id)
);
 
INSERT INTO central_autobuses_zapopan (autobuses_zapopan, dia, codigo_incapacidad, autobuses)
  VALUES 
  (1, 1, NULL, '1/10'),
  (1, 2, NULL, '1/11,5'),
  (1, 3, NULL, '1/10'),
  (1, 4, NULL, '1/11,5'),
  (1, 5, NULL, '1/10'),
  (1, 6, 'autobuses', NULL),
  (1, 7, 'autobuses', NULL),
  (2, 2, NULL, '1/11,5'),
  (2, 3, NULL, '2/11,5'),
  (2, 4, NULL, '1|11.5'),
  (2, 5, NULL, '1/11,5'),
  (2, 6, 'autobuses', NULL),
  (2, 7, 'autobuses', NULL),
  (3, 1, NULL, '1#8'),
  (3, 2, NULL, '1.0'),
  (3, 3, 'viaje_ciudad', NULL);
 
 
INSERT INTO central_autobuses_zapopan (autobuses_id, zapopan_id)
  VALUES (1, 5),
		 (2, 1),
		 (4, 2),
		 (3, 3),
		 (5, 4);
INSERT INTO('Vallarta Plus', 'Primera Plus', 'Tufesa', 'ETN', 
'Tequila Plus', 'Turistar', 'Elite', 'Servicios coordinados'
'Ómnibus de México', 'Futura',)

SELECT tabla1
FROM central_autobuses_zapopan 
WHERE condición = 'valor'
LINIT '10'

SELECT tabla2
FROM zapopan_id
WHERE condición = 'valor'
LINIT '10'

SELECT tabla3
FROM autobuses_id
WHERE codicion = 'valor'
LINIT '10'




