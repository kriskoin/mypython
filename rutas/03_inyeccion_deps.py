"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""
""" Lecture 97 ,98"""


from pathlib import Path

import db
import graphql
import api

path = Path()

paths = [p for p in path.iterdir() if p.is_dir() ]

dependencias = {
    "db" : db,
    "api": api,
    "graphl":graphql
}

def load(p):
    #print(str(p).replace("/","."))
    paquete = __import__(str(p).replace("/","."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcion init")

list(map(load,paths))