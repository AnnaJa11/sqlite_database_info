import sqlite3
from sqlite3 import Error


def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
       return conn
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

if __name__ == '__main__':
   db_file = "database.db"
   create_connection(db_file)
   