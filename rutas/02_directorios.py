"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""
""" Lecture 96 """

from pathlib import Path

path=Path("../rutas")


# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename()
print(path.iterdir())

for p in path.iterdir() :
    print (p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

archivos2 = [p for p in path.glob("*.py")]
print(archivos2)

# de forma recursiva
archivos3 = [p for p in path.glob("**/*.py")]
print(archivos3)

# de forma recursiva
archivos4 = [p for p in path.rglob("*.py")]
print(archivos4)