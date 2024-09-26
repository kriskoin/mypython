"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

class Perro:
    patas = 4
    def __init__(self,nombre):
        self.nombre= nombre
    
    @classmethod
    def habla(cls):
        print(f"guau !! me llamo: {self.nombre}")



    @classmethod
    def factory(cls):
        return cls("theo")

Perro.habla()

perro1 = Perro("Toby")
perro2 = Perro.factory
perro3 = Perro("Thor")