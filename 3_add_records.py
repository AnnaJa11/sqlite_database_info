import sqlite3

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
   except sqlite3.Error as e:
       print(e)
   return conn

def add_books(conn, book):
   """
   Create a new book into the books table
   :param conn:
   :param book:
   :return: book id
   """
   sql = '''INSERT INTO books(name, release_date)
             VALUES(?,?)'''
   cur = conn.cursor()
   cur.execute(sql, book)
   conn.commit()
   return cur.lastrowid

def add_movies(conn, movie):
   """
   Create a new movie into the movies table
   :param conn:
   :param movie:
   :return: movie id
   """
   sql = '''INSERT INTO movies(book_id, name, description, status, release_date)
             VALUES(?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, movie)
   conn.commit()
   return cur.lastrowid



if __name__ == "__main__":
   book = ("The perfect book title", "2022-11-20 00:00:00")

   conn = create_connection("database.db")
   bk_id = add_books(conn, book)

   movie = (
       bk_id,
       "Kill Bill",
       "After awakening from a four-year coma, a former assassin wreaks vengeance on the team of assassins who betrayed her.",
       "unwatched",
       "2003-05-11 20:00:00"     
   )

   movie_id = add_movies(conn, movie)

   print(bk_id, movie_id)
   conn.commit()
   
   
   cur = conn.cursor()
