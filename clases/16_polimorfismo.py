"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""
""" Lecture 79 , 80 """

from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print ("Guardando en BBDD")


class Sesion(Model):
    def guardar(self):
        print ("Guardando en archivo")

def guardar(entidad):
    entidad.guardar()

def guardar2(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion = Sesion()

guardar(sesion)
guardar(usuario)

guardar2([sesion,usuario])