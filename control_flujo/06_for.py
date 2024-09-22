"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

buscar = 3
for  numero in range(5): #0 ,1,2,3,4
    print (numero,numero * " Hola soy kris")

buscar2 = 10
for  numero in range(5): #0 ,1,2,3,4
    print (numero)
    if numero == buscar2:
        print ( "encontrado: ", buscar)
        break
else:
    print ("no se encpntro el numero: ", buscar2)


    #iterables
for char in "ultimate python":
    print (char)