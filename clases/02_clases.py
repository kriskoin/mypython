"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

class Perro:
    def habla(self):
        print("Guau!")

mi_perro = Perro()
print(type(mi_perro))

mi_perro.habla()

print(isinstance(mi_perro,Perro))