#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 100
#

from pathlib import Path

archivo = Path("archivo_prueba.txt")
texto = archivo.read_text()
print(texto)

texto2 = archivo.read_text("utf-8").split("\n")
print(texto2)

texto2.insert(0,"Hola soy kris")
archivo.write_text("\n".join(texto),"utf-8")