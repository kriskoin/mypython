"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

numeros = [1,2,3,4,5]

primero = numeros[1]
segundo = numeros [2]

primero,segundo,tercer,cuarto,quinto = numeros

primero, *otros = numeros
print (primero,otros)

numeros = [1,2,3,4,5,6,7,8,9]
primero,segundo, *otros = numeros
print (primero,segundo,otros)

primero,segundo, *otros,peultimo,ultimo = numeros
print (primero,segundo, otros,peultimo,ultimo )