
from MyDataBase import MyDatabase
from Constants import Constants

class CRUD:
    const = Constants()
    conn = MyDatabase(
            const.decrypt(Constants.e_host),
            int(const.decrypt(Constants.e_port)),
            const.decrypt(Constants.e_database),
            const.decrypt(Constants.e_user),
            const.decrypt(Constants.e_password)
        )
    
    def create_profile(self):
        sql  = '''
        CREATE TABLE defaultdb.profiles ( 
        idx INT Auto_increment NOT NULL,
        name VARCHAR(100) NOT NULL, 
        alias VARCHAR(100) NOT NULL,
        token VARCHAR(100) NOT NULL,
        birthdate DATE NOT NULL,
        email VARCHAR(100) NOT NULL,
        lang_code VARCHAR(100) NOT NULL,
        ´routine´ INT NOT NULL,
        alarm TIMESTAMP NOT NULL,
        inactivity_time TIMESTAMP NOT NULL,
        inactivity_type VARCHAR(100) NOT NULL,
        PRIMARY KEY(idx)
        );
    
        '''
        result = self.conn.query(sql)
        print(result)

    def get_profile(self):
        sql = "SELECT idx, name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type" \
        " FROM defaultdb.profiles;"
        result = self.conn.query(sql) 
        print(result)

    def set_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type):
        sql = "INSERT INTO defaultdb.profiles " \
        "(name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type) " \
        "VALUES ('{}', '{}', '{}', {}, '{}', '{}', {}, {}, {}, {});".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type
            )
        print(sql)
        result = self.conn.query(sql) 
        print(result)

    def update_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx):
        sql = "UPDATE defaultdb.profiles " \
        "SET name='{}', alias='{}', token='{}', birthdate={}, email='{}', lang_code='{}', `routine`={}, alarm={}, inactivity_time={}, inactivity_type={} " \
        "WHERE idx={};".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx
            )

    def delete_profile(self, idx):
        sql = "DELETE FROM defaultdb.profiles " \
        "WHERE idx={};".format(idx)
    
crud = CRUD()
#crud.create_profile()
crud.set_profile('pablo', 'work', 'rojo', '2000-02-17', 'perezpablo@gmail.com', 'aceptado', '34', '2000-01-01 10:20', '2000-01-01 12:30', 'inactivo')
crud.set_profile('lucia', 'work', 'azul', '1997-08-12', 'dominguezlucia@gmail.com', 'aceptado', '45', '2000-01-01  01:20', '2000-01-01 06:09', 'inactivo')
crud.set_profile('fernanda', 'work', 'morado', '2002-01-16', 'lopezfernanda@gmail.com', 'aceptado', '78', '2000-01-01 12:30', '2000-01-01 07:40', 'inactivo')
crud.set_profile('esau', 'office', 'amarillo', '1990-01-03', 'montañoesau@gmail.com', 'aceptado', '90','2000-01-01 02:00', '2000-01-01 07:00', 'activo')
crud.set_profile('rosaura', 'office', 'naranja', '1998-12-17', 'cruzrosaura@gmail.com', 'rechazado', '56', '2000-01-01 03:09', '2000-01-01 06:30', 'inactivo')
crud.set_profile('ricardo', 'express', 'cafe','1990-02-08', 'mendesricardo@gmail.com', 'rechazado', '34', '2000-01-01 05:30', '2000-01-01 06:00', 'inactivo')
crud.set_profile('marcelo', 'express', 'cian', '2006-04-12', 'chavezmarcelo@gmail,com', 'aceptado',  '65', '2000-01-01 06:07', '2000-01-01 09:00', 'activo')
crud.set_profile('lucio', 'work', 'rosa', '1990-06-03', 'riveralucio@gmail.com', 'aceptado', '45','2000-01-01 04:50', '2000-01-01 06:30', 'inactivo') 
crud.set_profile('amanda', 'office', 'verde', '1994-03-08', 'sanchezamanda@gmail.com',  'rechazado', '46', '2000-01-01 03:10', '2000-01-01 01:50', 'activo')
crud.set_profile('calletano', 'work', 'cian','1996-04-01', 'lunacalletano@gmail.com', 'rechazado',  '73', '2000-01-01 07:13', '2000-01-01 10:00', 'inactivo')