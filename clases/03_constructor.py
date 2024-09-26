"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

class Perro:
    def __init__(self,nombre):
        self.nombre= nombre
    
    def habla(self):
        print(f"guau !! me llamo: {self.nombre}")


mi_perro = Perro("theo")
print(mi_perro.nombre)
mi_perro.habla()