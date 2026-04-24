import binascii
import os

from MyDataBase import MyDatabase
from Constants import Constants

class CRUD:
    const = Constants()
    conn = MyDatabase(
            const.decrypt(Constants.host),
            int(const.decrypt(Constants.port)),
            const.decrypt(Constants.database),
            const.decrypt(Constants.user),
            const.decrypt(Constants.password)
        )

    def generate_key():
        return binascii.hexlify(os.urandom(20)).decode()
    
    def testing(self):
        sql = "SELECT * FROM mytest"
        result = self.conn.query(sql)
        return result

    def get_profile(self):
        sql = "SELECT idx, name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type" \
        " FROM defaultdb.profiles;"
        result = self.conn.query(sql) 
        print(result)

    def get_profile(self, email, token):
        sql = "SELECT idx, name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type" \
        " FROM defaultdb.profiles WHERE email = {} and token = {};".format(email, token)
        result = self.conn.query(sql) 
        return result

    def set_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type):
        sql = "INSERT INTO defaultdb.profiles " \
        "(idx, name, alias, token, birthdate, email, lang_code, `routine`, alarm, inactivity_time, inactivity_type) " \
        "VALUES(0, '{}', '{}', '{}', {}, '{}', '{}', {}, {}, {}, {});".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type
            )

    def update_profile(self, name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx):
        sql = "UPDATE defaultdb.profiles " \
        "SET name='{}', alias='{}', token='{}', birthdate={}, email='{}', lang_code='{}', `routine`={}, alarm={}, inactivity_time={}, inactivity_type={} " \
        "WHERE idx={};".format(
            name, alias, token, birthdate, email, lang_code, routine, alarm, inactivity_time, inactivity_type, idx
            )

    def delete_profile(self, idx):
        sql = "DELETE FROM defaultdb.profiles " \
        "WHERE idx={};".format(idx)
    
    



#crud = CRUD()
#crud.get_usuario_info()