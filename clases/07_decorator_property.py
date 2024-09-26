"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

class Perro:
    patas = 4
    def __init__(self,nombre):
        self.nombre=nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return
    
    

    
perro = Perro("Theo")
print(perro.nombre)