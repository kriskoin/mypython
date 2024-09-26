"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

class Perro:
    patas = 4
    def __init__(self,nombre):
        self.nombre= nombre
    
    def habla(self):
        print(f"guau !! me llamo: {self.nombre}")

Perro.patas=3

mi_perro = Perro("Theo")
mi_perro.patas =5
print(Perro.patas)
print(mi_perro.patas)
