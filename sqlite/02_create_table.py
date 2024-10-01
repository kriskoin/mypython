#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 107
#

import sqlite3

con = sqlite3.connect("app.db")
cursor = con.cursor()
cursor.execute(
    """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key,nombre VARCHAR(50));
    """
               )
con.commit()
con.close()
