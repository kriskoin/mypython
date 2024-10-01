#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 108
#

import sqlite3

with sqlite3.connect("app.db") as  con:
    cursor = con.cursor()
    cursor.execute(
        """
            CREATE TABLE if not exists usuarios
            (id INTEGER primary key,nombre VARCHAR(50));
        """
                )
