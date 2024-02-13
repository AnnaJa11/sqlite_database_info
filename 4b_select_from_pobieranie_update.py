import sqlite3
from sqlite3 import Error

from pobieranie_danych_4a import *
from update_5 import *


conn = sqlite3.connect('database.db')

print(select_all(conn, "books"))

update(conn, "movies", 2, status="watched")
   
conn.close()