class aplicacion:
    def __init__ (self):
        self.aplicacion
 
def tabla(self):
    nueva_tabla = {
        "id": "INTEGER PRIMARY KEY",
        "name": "VARCHAR(255)",
        "created": "DATETIME",
        "modified": "DATETIME"
    }
    self.create_table.append(nueva_tabla)

def insert(self, id, name, created, modified):
    insertar = {
        "id": id,
        "name": name,
        "created": created,
        "modified": modified
    }
   
    self.base_de_datos.append(insertar)

 
def get_profile(self):
    sql = "SELECT id, name, created, modified FROM students;"
    result = self.conn.query(sql) 
    return result

def set_profile(self, name, created, modified):
    sql = "INSERT INTO students (name, created, modified) VALUES ('{}', '{}', '{}');".format(
        name, created, modified
    )
    result = self.conn.query(sql) 
    return result

def update_profile(self, id_estudiante, name, created, modified):
    sql = "UPDATE students SET name='{}', created='{}', modified='{}' WHERE id={};".format(
        name, created, modified, id_estudiante
    )
    result = self.conn.query(sql)
    return result