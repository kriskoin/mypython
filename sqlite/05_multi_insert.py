#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 110
#

import sqlite3

with sqlite3.connect("app.db") as  con:
    cursor = con.cursor()
    usuarios = [
        (2,"Chanchito Feliz"),
        (3,"Chanchito Triste"),
    ]
    cursor.executemany(
            "INSERT INTO  usuarios values (?,?)",usuarios,
                )
