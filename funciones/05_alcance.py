"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

saludo = "Hola global"

def saludar():
    global saludo
    saludo = "Hola"
    print (saludo)


def saludarChanchito():
    saludo = "Hola chanchito"
    print (saludo)


print (saludo)