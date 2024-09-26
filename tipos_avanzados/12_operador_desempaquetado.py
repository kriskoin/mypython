"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

lista = [1,2,3,4]
print(lista)
print(*lista)

#combinar listas

lista2 =[5,6]
combinada = [*lista ,*lista2]
print(combinada)

combinada2 = ["Hola",*lista ,"mundo",*lista2, "Chanchito"]
print(combinada2)

punto1 = {"x":19}
punto2 = {"y":15}

nuevopunto={**punto1,**punto2}
print(nuevopunto)
