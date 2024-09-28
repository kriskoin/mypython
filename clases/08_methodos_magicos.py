"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""


class Perro:
   
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao perro :( {self.nombre}")

    def __str__(self):
        return f"clase perro :{self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice guau!")



perro = Perro ("chanchito",7)
perro.habla()
print(perro)
texto = str(perro)
print(texto)
del perro