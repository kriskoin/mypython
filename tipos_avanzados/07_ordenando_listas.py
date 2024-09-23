"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

numeros = [2,4,1,45,75,22]

numeros.sort(reverse = True)
print(numeros)

numeros2 = sorted(numeros)  #->regresaun nuevo listado no altera al original
print(numeros2)

usuarios = [["chanchito",4],["Felipe",1],["Pulga",5]]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena)
print(usuarios)

print ("usando lambda ")

usuarios = [["chanchito",4],["Felipe",1],["Pulga",5]]

usuarios.sort(key=lambda el:el[1])
print(usuarios)