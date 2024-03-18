from datetime import datetime
import pymysql
import os

class MysqlQuery():
    def __init__(self, host, port, user, password, database):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8'
        )
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.commit()
        self.conn.close()
    
    def fetch(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchall()

            return data
      
class PylibMysql():
    def __init__(self, host="", port=3306, user='root', password="", database=""):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def init(self):
        return MysqlQuery(self.host, self.port, self.user, self.password, self.database)