import os.path
import sqlite3

currentdirectory = os.path.dirname(os.path.abspath(__file__))

con = sqlite3.connect(currentdirectory + "\\database.db", check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()