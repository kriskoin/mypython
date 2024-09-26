"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

class Perro:
    patas = 4
    def __init__(self,nombre):
        self.nombre= nombre
    

    def habla(self):
        print(f"guau !! me llamo: {self.nombre}")



    @classmethod
    def factory(cls):
        return cls("theo")


perro2 = Perro.factory()
perro2.habla()
print(perro2.__dict__)