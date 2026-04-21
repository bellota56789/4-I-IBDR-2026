import pymysql
import copy
from Constants import Constants

class MyDatabase:

    def __init__(self, host, port, database, user, password): 
        timeout = 10
        self.connection = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            database=database,
            host=host,
            password=password,
            read_timeout=timeout,
            port=port,
            user=user,
            write_timeout=timeout,
        )

    def query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results_original = cursor.fetchall()
            return copy.deepcopy(results_original)
        finally:
            self.connection.commit()

    def close(self):
        self.connection.close()      

const = Constants()

test = MyDatabase( 
  const.decrypt(Constants.e_host),
  int(const.decrypt(Constants.e_port)),
  const.decrypt(Constants.e_database),
  const.decrypt(Constants.e_user),
  const.decrypt(Constants.e_password),
  )
