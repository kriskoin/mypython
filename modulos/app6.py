"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""
""" Lecture 92 """

import usuarios.impuestos
from  usuarios.impuestos.gravamenes import pagar_impuestos
import usuarios
print(dir(usuarios))

print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)

print(usuarios.impuestos.__name__)
print(usuarios.impuestos.__package__)
print(usuarios.impuestos.__path__)
print(usuarios.impuestos.__file__)