"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""


def suma (*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print (resultado)



suma (2,5,7)
suma (5,7)
suma (2,5,7,45,32)