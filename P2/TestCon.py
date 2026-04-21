import pymysql
from MyDataBase import MyDatabase
from Constants import Constants

timeout = 10
const = Constants()
conn = MyDatabase(
        const.decrypt(Constants.e_host),
        int(const.decrypt(Constants.e_port)),
        const.decrypt(Constants.e_database),
        const.decrypt(Constants.e_user),
        const.decrypt(Constants.e_password)
    )
  
#conn.query("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
#conn.query("INSERT INTO mytest (id) VALUES (1), (2)")
print (conn.query("SELECT * FROM mytest"))

