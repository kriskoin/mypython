"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""
""" Lecture 95 """

from pathlib import Path
#on windows
#r raw string
#Path(r"C:\Archivos de Programa\...")

#Path("/usr/bin")
#Path() #current path

#Path().home() #user home

# ruta a un archivo
#Path("one/__init__.py")

path = Path("mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()


print (
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chanchito.py")
print(p)

p = path.with_suffix(".bat")
print(p)

p = path.with_stem ("feliz")
print(p)