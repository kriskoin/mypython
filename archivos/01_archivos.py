#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 99 
#

from pathlib import Path
from time import ctime

archivo = Path("archivo_prueba.txt")

print("acceso: ",ctime(archivo.stat().st_atime))
print("creacion: ",ctime(archivo.stat().st_ctime))
print("modificacion: ",ctime(archivo.stat().st_mtime))