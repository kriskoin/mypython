#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 112
#

import sqlite3

with sqlite3.connect("app.db") as  con:
    cursor = con.cursor()
   
    cursor.execute(
            "SELECT * from usuarios"
                )
    print(cursor.fetchall())
