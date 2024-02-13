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
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_books_sql = """
   -- books table
   CREATE TABLE IF NOT EXISTS books (
      id integer PRIMARY KEY,
      name text NOT NULL,
      release_date text
   );
   """

   create_movies_sql = """
   -- movies table
   CREATE TABLE IF NOT EXISTS movies (
      id integer PRIMARY KEY,
      book_id integer NOT NULL,
      name VARCHAR(250) NOT NULL,
      description TEXT,
      status VARCHAR(15) NOT NULL,
      release_date text NOT NULL,
      FOREIGN KEY (book_id) REFERENCES books (id)
   );
   """

   db_file = "database.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_books_sql)
       execute_sql(conn, create_movies_sql)
       conn.close()